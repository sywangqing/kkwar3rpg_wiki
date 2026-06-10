import { defineConfig } from 'vitepress'
import { generateSidebar, generateAuthorSidebar } from '../../scripts/gen_sidebar'
import { readFileSync } from 'fs'
import { resolve, dirname } from 'path'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))

// ── 自定义 Shiki TextMate Grammars（jass / vjass / trigger）─────────
const jassGrammar   = JSON.parse(readFileSync(resolve(__dirname, 'shiki-langs/jass.tmLanguage.json'), 'utf-8'))
const vjassGrammar  = JSON.parse(readFileSync(resolve(__dirname, 'shiki-langs/vjass.tmLanguage.json'), 'utf-8'))
const triggerGrammar = JSON.parse(readFileSync(resolve(__dirname, 'shiki-langs/trigger.tmLanguage.json'), 'utf-8'))

// vjass 直接复用 jass grammar（同语法，只是别名不同）
const vjassLang = { ...vjassGrammar, patterns: jassGrammar.patterns, repository: jassGrammar.repository }

export default defineConfig({
  // ── 站点基础信息 ──────────────────────────────────────────────
  lang: 'zh-CN',
  title: 'KK 作者中心 · Wiki',
  description: 'KK 编辑器教学 + KK 地图运营手册 · 100+ 篇实战 + 73 个演示图源码 + KK 平台运营教程',

  // 构建输出目录（vercel.json 里 outputDirectory 指向这里）
  outDir: './.vitepress/dist',

  // 自定义域名 durontar.com，根路径
  base: '/',

  // 去掉 .html 后缀，更美观的 URL
  cleanUrls: true,

  // 死链检查：wiki 文章由 pipeline 持续生成，未完成的文章链接属于预期行为
  ignoreDeadLinks: true,

  // ── Head 标签 ─────────────────────────────────────────────────
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#7c3aed' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'KK 作者中心 · Wiki' }],
    ['meta', { property: 'og:description', content: 'KK 编辑器教学 + KK 地图运营手册' }],
    // Pagefind 搜索 UI 样式（构建后注入，路径需含 base）
    ['link', { rel: 'stylesheet', href: '/pagefind/pagefind-ui.css' }],
  ],

  // ── 主题配置 ───────────────────────────────────────────────────
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'KK 作者中心',

    // ── 导航栏 ──────────────────────────────────────────────────
    nav: [
      { text: '🚀 新人必读',     link: '/author/newbie/faq/产品手册' },
      { text: '🛠️ 编辑器教学',   link: '/author/editor' },
      { text: '📈 运营教学',     link: '/author/operations' },
      { text: '🏛️ 模型库',       link: '/models/' },
      { text: '🔍 搜索',         link: '/search' },
      { text: '📋 更新日志',     link: '/changelog' },
    ],

    // ── 侧边栏（/author/ 走作者中心 sidebar，其它走原 sidebar）
    // VitePress sidebar 多前缀：以最长 key 优先匹配
    sidebar: {
      ...generateAuthorSidebar(),
      ...generateSidebar(),
    },

    // ── 社交链接 ────────────────────────────────────────────────
    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-org/war3-wiki' },
    ],

    // ── 页脚 ────────────────────────────────────────────────────
    footer: {
      message: 'KK 作者中心 Wiki · 由 AI 多智能体每日自动维护 · 与 KK 官方独立的社区项目',
      copyright: `© ${new Date().getFullYear()} · KK 官网 <a href="http://www.kkdzpt.com" target="_blank" rel="noreferrer" style="color:var(--vp-c-brand-1)">www.kkdzpt.com</a> · 开发者后台 <a href="https://create.kkdzpt.com" target="_blank" rel="noreferrer" style="color:var(--vp-c-brand-1)">create.kkdzpt.com</a>`,
    },

    // ── 编辑链接 ────────────────────────────────────────────────
    editLink: {
      pattern: 'https://github.com/your-org/war3-wiki/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页',
    },

    // ── 文章底部时间戳 ──────────────────────────────────────────
    lastUpdated: {
      text: '最后更新',
    },

    // ── 本地搜索（Pagefind，在 build 后由 pagefind CLI 生成索引）
    // 注：使用 head 里注入的 pagefind-ui.css，脚本在 theme/index.ts 里挂载
    // 如果要换用 VitePress 内置 minisearch，把下面一行注释删掉即可
    // search: { provider: 'local' },

    // ── 文档目录深度 ────────────────────────────────────────────
    outline: {
      label: '本页目录',
      level: [2, 3],
    },

    // ── 翻页按钮文案 ────────────────────────────────────────────
    docFooter: {
      prev: '上一篇',
      next: '下一篇',
    },

    // ── 返回顶部按钮 ────────────────────────────────────────────
    returnToTopLabel: '返回顶部',

    // ── 侧边栏切换按钮 ───────────────────────────────────────────
    sidebarMenuLabel: '目录',

    // ── 深色/浅色模式切换 ────────────────────────────────────────
    darkModeSwitchLabel: '深色模式',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
  },

  // ── Vite 构建优化：手动拆分大 chunk ─────────────────────────────
  vite: {
    build: {
      // kk-triggers_black-tech.md 单文件 ~14MB（大量 jass 代码），无法继续拆分
      // 保留 15MB 上限，静默已知的内容体积警告
      chunkSizeWarningLimit: 15000,
      rollupOptions: {
        output: {
          manualChunks(id) {
            // Vue core → 独立 vendor chunk
            if (id.includes('node_modules/vue/') || id.includes('node_modules/@vue/')) {
              return 'vendor-vue'
            }
            // shiki 高亮引擎（体积较大，独立出来）
            if (id.includes('node_modules/shiki') || id.includes('node_modules/@shikijs')) {
              return 'vendor-shiki'
            }
            // 旧 wiki 文档页面 —— 按一级目录拆 chunk
            const match = id.match(/[/\\]docs[/\\]([^/\\]+)[/\\].*\.md/)
            if (match && match[1] !== 'author') {
              return `wiki-${match[1]}`
            }
          },
        },
      },
    },
  },

  // ── Markdown 扩展 ─────────────────────────────────────────────
  markdown: {
    // 代码块行号
    lineNumbers: true,
    // 容器（::: tip / warning / danger 等）
    container: {
      tipLabel: '提示',
      warningLabel: '注意',
      dangerLabel: '危险',
      infoLabel: '信息',
      detailsLabel: '详情',
    },
    // ── 注册自定义语言高亮（jass / vjass / trigger）───────────────
    languages: [
      {
        ...jassGrammar,
        name: 'jass',
        aliases: [],
      },
      {
        ...vjassLang,
        name: 'vjass',
        aliases: [],
      },
      {
        ...triggerGrammar,
        name: 'trigger',
        aliases: ['trg'],
      },
    ],
  },
})
