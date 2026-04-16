import { defineConfig } from 'vitepress'

// GitHub Pages 部署时需要设置 base 为仓库名
// 如仓库名为 war3-wiki，base 为 '/war3-wiki/'
// 若使用自定义域名或根路径部署，改为 '/'
const base = process.env.GITHUB_PAGES === 'true' ? '/kkwar3rpg_wiki/' : '/'

export default defineConfig({
  base,
  title: 'War3 地图开发者 Wiki',
  description: 'Warcraft III RPG 地图编辑器知识库 —— AI 自动整理，持续更新',
  lang: 'zh-CN',
  ignoreDeadLinks: true,
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['meta', { name: 'keywords', content: 'War3,魔兽争霸,地图编辑器,JASS,Lua,触发器,RPG地图' }],
    ['meta', { name: 'author', content: 'War3 Wiki Bot' }],
  ],

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

    footer: {
      message: '📝 内容由 AI 自动生成，基于网络公开资料整理，仅供参考。',
      copyright: `© ${new Date().getFullYear()} War3 Wiki`,
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
})