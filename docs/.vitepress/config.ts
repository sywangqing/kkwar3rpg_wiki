import { defineConfig } from 'vitepress'

// GitHub Pages 部署时需要设置 base 为仓库名
// 如仓库名为 war3-wiki，base 为 '/war3-wiki/'
// 若使用自定义域名或根路径部署，改为 '/'
const base = process.env.GITHUB_PAGES === 'true' ? '/kkwar3rpg_wiki/' : '/'

export default defineConfig({
  base,
  title: 'War3 Wiki',
  description: 'Warcraft III RPG 地图编辑器 AI 自动化知识库',
  lang: 'zh-CN',

  // 关闭严格模式，允许自定义 frontmatter 字段（新 AI 生成字段不会报错）
  ignoreDeadLinks: true,

  themeConfig: {
    nav: [
      { text: '🏠 首页', link: '/' },
      { text: '📚 知识库', link: '/getting-started/editor-installation' },
      { text: '🛤️ 学习路径', link: '/learning-path' },
      { text: '📋 更新日志', link: '/changelog' },
    ],

    sidebar: {
      '/': [
        {
          text: '🚀 快速入门',
          collapsed: false,
          items: [
            { text: 'War3 地图编辑器安装与配置', link: '/getting-started/editor-installation' },
          ],
        },
      ],
    },

    search: { provider: 'local' },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-org/war3-wiki' },
    ],

    // 页脚
    footer: {
      message: '由 AI Agent 自动生成，内容仅供参考',
      copyright: '© 2025 War3 Wiki',
    },

    // 搜索（Pagefind 集成在构建后）
    search: {
      provider: 'local',
    },

    docFooter: { prev: '上一篇', next: '下一篇' },
    outline: { level: [2, 3], label: '本文目录' },
    lastUpdated: { text: '最后更新于' },

    editLink: {
      pattern: 'https://github.com/your-org/war3-wiki/edit/main/docs/:path',
      text: '✏️ 在 GitHub 上编辑此页',
    },
  },

  markdown: {
    lineNumbers: true,
    image: { lazyLoading: true },
  },

  // 构建配置
  vite: {
    // 允许从 pipeline 生成的文章中读取 frontmatter
    build: {
      chunkSizeWarningLimit: 2000,
    },
  },
})