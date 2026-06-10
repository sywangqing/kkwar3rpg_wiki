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
  'tbwlm-mirror',    // 🏛️ tbwlm.cn 资源站镜像（2026-06 新增）
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
  'tbwlm-mirror':    '🏛️ tbwlm.cn 镜像',
}

// kk-triggers 的子目录配置（自动嵌套展示）
const KK_TRIGGERS_SUBDIRS: Record<string, { label: string; collapsed?: boolean }> = {
  'shenmu':    { label: '🏆 神墓 2.7C 全量（171 触发器）', collapsed: true },
  'demo-maps': { label: '🎮 50 张演示图详解',           collapsed: true },
}

function extractFrontmatterTitle(filePath: string): string | null {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    const match = content.match(/^---[\r\n]+([\s\S]*?)[\r\n]+---/)
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

// ============================================================
// /author/ 路由 sidebar — 三大组：新人必读 / 编辑器教学 / 运营教学
// ============================================================

function buildAuthorItems(subDir: string, prefix: string): any[] {
  const docsDir = path.resolve(__dirname, '../docs')
  const dir = path.join(docsDir, subDir)
  if (!fs.existsSync(dir)) return []

  const files = fs.readdirSync(dir)
    .filter(f => f.endsWith('.md') && f !== 'index.md')
    .sort()

  return files.map(file => {
    const filePath = path.join(dir, file)
    const link = `${prefix}/${file.replace('.md', '')}`
    const title = extractFrontmatterTitle(filePath) || file.replace('.md', '')
    return { text: title, link }
  })
}

// kk-triggers 实战库子目录（shenmu / demo-maps）
function buildDemosSubdirs(): any[] {
  const docsDir = path.resolve(__dirname, '../docs')
  const baseDir = path.join(docsDir, 'author/editor/demos')
  if (!fs.existsSync(baseDir)) return []

  const subdirs = fs.readdirSync(baseDir)
    .filter(f => {
      const stat = fs.statSync(path.join(baseDir, f))
      return stat.isDirectory()
    })
    .sort()

  return subdirs.map(sub => {
    const subDir = path.join(baseDir, sub)
    const subFiles = fs.readdirSync(subDir)
      .filter(f => f.endsWith('.md'))
      .sort()
    const items = subFiles.map(file => {
      const fp = path.join(subDir, file)
      const link = `/author/editor/demos/${sub}/${file.replace('.md', '')}`
      const title = extractFrontmatterTitle(fp) || file.replace('.md', '')
      return { text: title, link }
    })
    const labels: Record<string, string> = {
      shenmu: '🏆 神墓 2.7C 全量（171 触发器）',
      'demo-maps': '🎮 50 张演示图详解',
    }
    return {
      text: labels[sub] || sub,
      collapsed: true,
      items,
    }
  })
}

export function generateAuthorSidebar(): any {
  // 新人必读（author/newbie/ 下的文章）
  const newbieItems = buildAuthorItems('author/newbie', '/author/newbie')
  const faqItems = buildAuthorItems('author/newbie/faq', '/author/newbie/faq')
  const kkGuideItems = buildAuthorItems('author/newbie/kk-guide', '/author/newbie/kk-guide')

  // 快速入门（启航手册 Section 2 "3分钟带你快速了解编辑器"）
  const quickStartItems = [
    ...buildAuthorItems('author/editor/quick-start', '/author/editor/quick-start'),
  ]

  // 编辑器各子主题
  const triggersItems = buildAuthorItems('author/editor/triggers', '/author/editor/triggers')
  const objectsItems = buildAuthorItems('author/editor/objects', '/author/editor/objects')
  const terrainItems = buildAuthorItems('author/editor/terrain', '/author/editor/terrain')
  const systemsItems = [
    ...buildAuthorItems('author/editor/systems', '/author/editor/systems'),
    ...buildAuthorItems('author/editor/advanced', '/author/editor/advanced'),
  ]
  const scriptingItems = buildAuthorItems('author/editor/scripting', '/author/editor/scripting')
  const toolsItems = buildAuthorItems('author/editor/tools', '/author/editor/tools')

  // kk-triggers 实战库（demos + 子目录）
  const demosRootItems = buildAuthorItems('author/editor/demos', '/author/editor/demos')
  const demosSubdirs = buildDemosSubdirs()

  // 运营各子主题
  const platformItems = buildAuthorItems('author/ops/platform', '/author/ops/platform')
  const publishingItems = buildAuthorItems('author/ops/publishing', '/author/ops/publishing')
  const launchItems = buildAuthorItems('author/ops/launch', '/author/ops/launch')
  const commercialItems = buildAuthorItems('author/ops/commercial', '/author/ops/commercial')
  const supportItems = buildAuthorItems('author/ops/support', '/author/ops/support')

  return {
    '/author/': [
      {
        text: '🚀 新人必读',
        collapsed: false,
        items: [
          { text: '🏠 KK 作者中心首页', link: '/author/' },
          { text: '📘 KK 官方启航手册', collapsed: false, items: kkGuideItems },
          { text: '⭐ 产品手册（入驻 + 立项 + 商业化）', link: '/author/newbie/faq/产品手册' },
          ...faqItems.filter(i => i.link !== '/author/newbie/faq/产品手册'),
        ],
      },
      {
        text: '🛠️ 编辑器教学',
        collapsed: false,
        items: [
          { text: '📋 编辑器教学概览', link: '/author/editor' },
          { text: '🌱 快速入门', collapsed: true, items: [
            ...newbieItems,
            { text: '--- 3分钟快速了解编辑器 ---', link: '/author/editor/quick-start/y3-editor' },
            ...quickStartItems,
          ] },
          { text: '⚡ 触发器 GUI', collapsed: true, items: triggersItems },
          { text: '⚙️ 对象编辑器', collapsed: true, items: objectsItems },
          { text: '🗺️ 地形与场景', collapsed: true, items: terrainItems },
          {
            text: '🎯 KK 触发器实战库 ⭐',
            collapsed: true,
            items: [
              ...demosRootItems.length ? [{
                text: '📖 实战库概览',
                link: '/author/editor/demos/index',
              }] : [],
              ...demosRootItems.filter(i => i.link !== '/author/editor/demos/index'),
              ...demosSubdirs,
            ],
          },
          { text: '🏆 RPG 系统搭建', collapsed: true, items: systemsItems },
          { text: '� JASS / Lua 进阶', collapsed: true, items: scriptingItems },
          { text: '🔧 第三方工具', collapsed: true, items: toolsItems },
        ],
      },
      {
        text: '📈 运营教学',
        collapsed: false,
        items: [
          { text: '📋 运营教学概览', link: '/author/operations' },
          { text: '🚢 上线发布与发行', collapsed: true, items: publishingItems },
          { text: '⚙️ 平台工具配置', collapsed: true, items: platformItems },
          { text: '🧪 测试与运营', collapsed: true, items: launchItems },
          { text: '💰 商业化设计', collapsed: true, items: commercialItems },
          { text: '🚀 成长扶持', collapsed: true, items: supportItems },
        ],
      },
    ],
  }
}

