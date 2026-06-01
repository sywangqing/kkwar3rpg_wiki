/**
 * gen_sidebar.ts — 自动侧边栏生成器
 *
 * 扫描 docs/ 目录结构，按 taxonomy 分类顺序生成 VitePress sidebar 配置。
 * 文章标题从 Markdown frontmatter 的 title 字段读取。
 * 使用 ESM 语法，兼容 VitePress config.ts 的导入方式。
 */
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

// ESM 中获取 __dirname 的标准方式
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

// 分类顺序（与 taxonomy.yaml 保持一致）
const CATEGORY_ORDER = [
  'getting-started',
  'kk-triggers',     // 🎮 KK 触发器实战（73+ 篇真实案例，放在显眼位置）
  'triggers',
  'terrain',
  'scripting',
  'object-editor',
  'rpg-systems',
  'tools',
  'advanced',
  'publishing',
  'faq',
]

const CATEGORY_LABELS: Record<string, string> = {
  'getting-started': '🚀 快速入门',
  'kk-triggers':     '🎮 KK 触发器实战',
  'terrain':         '🗺️ 地形编辑',
  'triggers':        '⚡ 触发器系统',
  'scripting':       '💻 脚本编程',
  'object-editor':   '🎭 对象编辑器',
  'rpg-systems':     '🏰 RPG 系统',
  'tools':           '🛠️ 工具生态',
  'advanced':        '🎨 进阶开发',
  'publishing':      '🚢 发布上线',
  'faq':             '❓ 常见问题',
}

// kk-triggers 的子目录配置（自动嵌套展示）
const KK_TRIGGERS_SUBDIRS: Record<string, { label: string; collapsed?: boolean }> = {
  'shenmu':    { label: '🏆 神墓 2.7C 全量（171 触发器）', collapsed: true },
  'demo-maps': { label: '🎮 50 张演示图详解',           collapsed: true },
}

function extractFrontmatterTitle(filePath: string): string | null {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    const match = content.match(/^---\n([\s\S]*?)\n---/)
    if (!match) return null
    const titleMatch = match[1].match(/^title:\s*(.+)$/m)
    return titleMatch ? titleMatch[1].trim().replace(/^['"]|['"]$/g, '') : null
  } catch {
    return null
  }
}

function buildCategoryItems(categoryDir: string, categoryId: string): any[] {
  if (!fs.existsSync(categoryDir)) return []

  const items: any[] = []

  // 1) 先收集该目录的顶层 .md（除 index.md 外）
  const topFiles = fs.readdirSync(categoryDir)
    .filter(f => f.endsWith('.md') && f !== 'index.md')
    .sort()

  for (const file of topFiles) {
    const filePath = path.join(categoryDir, file)
    const link = `/${categoryId}/${file.replace('.md', '')}`
    const title = extractFrontmatterTitle(filePath) || file.replace('.md', '')
    items.push({ text: title, link })
  }

  // 2) 再处理子目录（仅对 kk-triggers 生效）
  if (categoryId === 'kk-triggers') {
    const subdirs = fs.readdirSync(categoryDir)
      .filter(f => {
        const stat = fs.statSync(path.join(categoryDir, f))
        return stat.isDirectory() && KK_TRIGGERS_SUBDIRS[f]
      })
      .sort()

    for (const sub of subdirs) {
      const subDir = path.join(categoryDir, sub)
      const subFiles = fs.readdirSync(subDir)
        .filter(f => f.endsWith('.md'))
        .sort()

      const subItems = subFiles.map(file => {
        const filePath = path.join(subDir, file)
        const link = `/${categoryId}/${sub}/${file.replace('.md', '')}`
        const title = extractFrontmatterTitle(filePath) || file.replace('.md', '')
        return { text: title, link }
      })

      if (subItems.length > 0) {
        items.push({
          text: KK_TRIGGERS_SUBDIRS[sub].label,
          collapsed: KK_TRIGGERS_SUBDIRS[sub].collapsed ?? true,
          items: subItems,
        })
      }
    }
  }

  return items
}

export function generateSidebar(): any {
  // __dirname 此处为 scripts/，所以 docs/ 在 ../docs/
  const docsDir = path.resolve(__dirname, '../docs')
  const sidebar: Record<string, any[]> = {}

  // 为每个分类生成侧边栏
  for (const categoryId of CATEGORY_ORDER) {
    const categoryDir = path.join(docsDir, categoryId)
    const items = buildCategoryItems(categoryDir, categoryId)
    if (items.length > 0) {
      const label = CATEGORY_LABELS[categoryId] || categoryId
      if (!sidebar['/']) {
        sidebar['/'] = []
      }
      sidebar['/'].push({
        text: label,
        collapsed: false,
        items,
      })
    }
  }

  return sidebar
}
