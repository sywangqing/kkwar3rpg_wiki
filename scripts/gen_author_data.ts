/**
 * gen_author_data.ts — KK 作者中心 首页/落地页 数据脚本
 *
 * 扫描 docs/author/ 目录，按新三级结构聚合：
 *   author/newbie/           → 新人必读
 *   author/editor/triggers/  → 触发器
 *   author/editor/objects/   → 对象编辑器
 *   author/editor/terrain/   → 地形
 *   author/editor/demos/     → KK 触发器实战库
 *   author/editor/systems/   → RPG 系统
 *   author/editor/advanced/  → 高级专题
 *   author/editor/scripting/ → JASS/Lua
 *   author/editor/tools/     → 第三方工具
 *   author/ops/platform/     → 平台工具
 *   author/ops/publishing/   → 发布发行
 *   author/ops/launch/       → 测试运营
 *
 * 产物：docs/.vitepress/_author_data.json
 *   被 AuthorHome.vue / AuthorEditor.vue / AuthorOps.vue 通过 import 静态读取
 *
 * 执行时机：prebuild 阶段
 */
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const DOCS = path.resolve(__dirname, '../docs')
const AUTHOR_DIR = path.join(DOCS, 'author')

interface PageInfo {
  path: string
  title: string
  bucket: string        // 宫格 key: newbie, triggers, objects, terrain, demos, systems, scripting, tools, platform, publishing, launch
  updated?: string
}

function readFm(filePath: string): { title?: string; updated?: string } {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    const m = content.match(/^---[\r\n]+([\s\S]*?)[\r\n]+---/)
    if (!m) return {}
    const block = m[1]
    const t = block.match(/^title:\s*(.+)$/m)
    const u = block.match(/^updated:\s*(.+)$/m)
    return {
      title: t ? t[1].trim().replace(/^['"]|['"]$/g, '') : undefined,
      updated: u ? u[1].trim().replace(/^['"]|['"]$/g, '') : undefined,
    }
  } catch {
    return {}
  }
}

function walk(dir: string, prefix: string, bucket: string): PageInfo[] {
  if (!fs.existsSync(dir)) return []
  const out: PageInfo[] = []
  for (const entry of fs.readdirSync(dir)) {
    const full = path.join(dir, entry)
    const stat = fs.statSync(full)
    if (stat.isDirectory()) {
      // 子目录递归，bucket 不变
      out.push(...walk(full, `${prefix}/${entry}`, bucket))
    } else if (entry.endsWith('.md') && entry !== 'index.md' && entry !== 'editor.md' && entry !== 'operations.md') {
      const slug = entry.replace(/\.md$/, '')
      const fm = readFm(full)
      const mtime = stat.mtime.toISOString().slice(0, 10)
      out.push({
        path: `${prefix}/${slug}`,
        title: fm.title || slug,
        bucket,
        updated: fm.updated || mtime,
      })
    }
  }
  return out
}

type BucketMap = { label: string; dir: string; prefix: string }

const EDITOR_BUCKETS: BucketMap[] = [
  { label: 'getting-started', dir: 'newbie', prefix: '/author/newbie' },
  { label: 'triggers',        dir: 'editor/triggers', prefix: '/author/editor/triggers' },
  { label: 'objects',         dir: 'editor/objects', prefix: '/author/editor/objects' },
  { label: 'terrain',         dir: 'editor/terrain', prefix: '/author/editor/terrain' },
  { label: 'demos',           dir: 'editor/demos', prefix: '/author/editor/demos' },
  { label: 'systems',         dir: 'editor/systems', prefix: '/author/editor/systems' },
  { label: 'advanced',        dir: 'editor/advanced', prefix: '/author/editor/advanced' },
  { label: 'scripting',       dir: 'editor/scripting', prefix: '/author/editor/scripting' },
  { label: 'tools',           dir: 'editor/tools', prefix: '/author/editor/tools' },
]

const OPS_BUCKETS: BucketMap[] = [
  { label: 'platform',   dir: 'ops/platform', prefix: '/author/ops/platform' },
  { label: 'publishing', dir: 'ops/publishing', prefix: '/author/ops/publishing' },
  { label: 'launch',     dir: 'ops/launch', prefix: '/author/ops/launch' },
]

function main() {
  const editorPages: PageInfo[] = []
  const opsPages: PageInfo[] = []

  for (const b of EDITOR_BUCKETS) {
    editorPages.push(...walk(path.join(AUTHOR_DIR, b.dir), b.prefix, b.label))
  }
  for (const b of OPS_BUCKETS) {
    opsPages.push(...walk(path.join(AUTHOR_DIR, b.dir), b.prefix, b.label))
  }

  // 数据条
  // demos 里的 demo-maps 子目录文件数
  const demoDir = path.join(AUTHOR_DIR, 'editor/demos/demo-maps')
  const demosCount = fs.existsSync(demoDir)
    ? fs.readdirSync(demoDir).filter(f => f.endsWith('.md')).length
    : 0

  const stats = {
    editor: editorPages.length,
    demos: demosCount,
    shenmuTriggers: 171,  // 神墓 2.7C 全量常量
    ops: opsPages.length,
  }

  // 编辑器子主题计数
  const editorBuckets: Record<string, number> = {}
  for (const b of EDITOR_BUCKETS) {
    editorBuckets[b.label] = editorPages.filter(p => p.bucket === b.label).length
  }

  // 运营子主题计数
  const opsBuckets: Record<string, number> = {}
  for (const b of OPS_BUCKETS) {
    opsBuckets[b.label] = opsPages.filter(p => p.bucket === b.label).length
  }

  // 最近更新（取前 8）
  const recent = [...editorPages, ...opsPages]
    .filter(p => p.updated)
    .sort((a, b) => (b.updated || '').localeCompare(a.updated || ''))
    .slice(0, 8)
    .map(p => ({ title: p.title, path: p.path, updated: p.updated, bucket: p.bucket }))

  const data = {
    generatedAt: new Date().toISOString(),
    stats,
    editorBuckets,
    opsBuckets,
    recent,
  }

  const outPath = path.join(DOCS, '.vitepress', '_author_data.json')
  fs.writeFileSync(outPath, JSON.stringify(data, null, 2), 'utf-8')
  console.log(`[gen_author_data] wrote ${outPath}`)
  console.log(`[gen_author_data] stats:`, stats)
}

main()
