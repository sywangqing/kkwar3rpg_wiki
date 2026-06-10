/**
 * add-redirects.ts — 一键为老路径 md 增加 redirect frontmatter
 *
 * 映射表：
 *   /getting-started/<slug>      → /author/newbie/<slug>
 *   /faq/<slug>                  → /author/newbie/faq/<slug>
 *   /triggers/<slug>             → /author/editor/triggers/<slug>
 *   /object-editor/<slug>        → /author/editor/objects/<slug>
 *   /terrain/<slug>              → /author/editor/terrain/<slug>
 *   /rpg-systems/<slug>          → /author/editor/systems/<slug>
 *   /scripting/<slug>            → /author/editor/scripting/<slug>
 *   /tools/<slug>                → /author/editor/tools/<slug>
 *   /advanced/<slug>             → /author/editor/advanced/<slug>
 *   /kk-triggers/<slug>          → /author/editor/demos/<slug>
 *   /operations/<slug>           → /author/ops/launch/<slug>
 *   /platform-tools/<slug>       → /author/ops/platform/<slug>
 *   /publishing/<slug>           → /author/ops/publishing/<slug>
 *
 * VitePress 2.0+ 支持 frontmatter redirect: '/new-path'
 */
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const DOCS = path.resolve(__dirname, '../docs')

const MAPPING: Record<string, string> = {
  'getting-started': '/author/newbie',
  'faq':              '/author/newbie/faq',
  'triggers':         '/author/editor/triggers',
  'object-editor':    '/author/editor/objects',
  'terrain':          '/author/editor/terrain',
  'rpg-systems':      '/author/editor/systems',
  'scripting':        '/author/editor/scripting',
  'tools':            '/author/editor/tools',
  'advanced':         '/author/editor/advanced',
  'kk-triggers':      '/author/editor/demos',
  'operations':       '/author/ops/launch',
  'platform-tools':   '/author/ops/platform',
  'publishing':       '/author/ops/publishing',
}

function addRedirect(filePath: string, from: string, to: string) {
  try {
    let content = fs.readFileSync(filePath, 'utf-8')

    // 跳过已有 redirect 的文件
    if (/^redirect:\s/m.test(content)) {
      console.log(`  SKIP (already has redirect): ${filePath}`)
      return
    }

    // 提取 slug
    const slug = path.basename(filePath, '.md')

    // 排除 index.md（子目录下的概览页也跳过）
    if (slug === 'index') {
      console.log(`  SKIP (index): ${filePath}`)
      return
    }

    // 构造 redirect 目标
    const target = `${to}/${slug}`

    // 如果 frontmatter 已存在（以 --- 开头），在末尾插入 redirect
    if (content.startsWith('---\n') || content.startsWith('---\r\n')) {
      const fmEndFirst = content.indexOf('\n---\n', 4)
      const fmEndSecond = content.indexOf('\n---\r\n', 4)
      const fmEnd = fmEndFirst !== -1 ? fmEndFirst : fmEndSecond
      if (fmEnd !== -1) {
        const fm = content.slice(4, fmEnd)
        const afterFm = content.slice(fmEnd + 5)
        // 确保 frontmatter 末尾有一个换行，然后追加 redirect
        content = `---\n${fm.trimEnd()}\nredirect: '${target}'\n---\n${afterFm}`
      }
    } else {
      // 没有 frontmatter，加一个
      content = `---\nredirect: '${target}'\n---\n\n${content}`
    }

    fs.writeFileSync(filePath, content, 'utf-8')
    console.log(`  OK: ${filePath} → ${target}`)
  } catch (e) {
    console.error(`  ERR: ${filePath} — ${e}`)
  }
}

// 递归处理目录
function processDir(dir: string, prefix: string) {
  if (!fs.existsSync(dir)) return
  for (const entry of fs.readdirSync(dir)) {
    const full = path.join(dir, entry)
    const stat = fs.statSync(full)
    if (stat.isDirectory()) {
      processDir(full, prefix)
    } else if (entry.endsWith('.md')) {
      addRedirect(full, prefix, MAPPING[prefix])
    }
  }
}

function main() {
  for (const [oldCat, newPrefix] of Object.entries(MAPPING)) {
    const dir = path.join(DOCS, oldCat)
    if (!fs.existsSync(dir)) {
      console.log(`[skip] ${oldCat} — directory not found`)
      continue
    }
    console.log(`\n${oldCat}/ → ${newPrefix}/`)
    processDir(dir, oldCat)
  }
}

main()
