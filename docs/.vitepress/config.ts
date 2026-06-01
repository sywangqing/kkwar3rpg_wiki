import { defineConfig } from 'vitepress'
import { generateSidebar } from '../../scripts/gen_sidebar'

export default defineConfig({
  // ── 站点基础信息 ──────────────────────────────────────────────
  lang: 'zh-CN',
  title: 'War3 地图开发者 Wiki',
  description: 'AI 自动整理的权威资料站 · 每日持续更新 · 面向所有开发者免费开放',

  // 构建输出目录（vercel.json 里 outputDirectory 指向这里）
  outDir: './.vitepress/dist',

  // GitHub Pages 子路径（仓库名即为 base）
  base: '/kkwar3rpg_wiki/',

  // 去掉 .html 后缀，更美观的 URL
  cleanUrls: true,

  // 死链检查：wiki 文章由 pipeline 持续生成，未完成的文章链接属于预期行为
  ignoreDeadLinks: true,

  // ── Head 标签 ─────────────────────────────────────────────────
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#1e6fcf' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'War3 地图开发者 Wiki' }],
    ['meta', { property: 'og:description', content: 'RPG 地图编辑器知识库' }],
    // Pagefind 搜索 UI 样式（构建后注入，路径需含 base）
    ['link', { rel: 'stylesheet', href: '/kkwar3rpg_wiki/pagefind/pagefind-ui.css' }],
  ],

  // ── 主题配置 ───────────────────────────────────────────────────
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'War3 Wiki',

    // ── 导航栏 ──────────────────────────────────────────────────
    nav: [
      { text: '🚀 快速入门', link: '/getting-started/war3-地图编辑器安装与配置' },
      { text: '🎮 KK 触发器实战', link: '/kk-triggers/index' },
      { text: '🛤️ 学习路径', link: '/learning-path' },
      { text: '🔍 搜索', link: '/search' },
      {
        text: '🗂️ 分类',
        items: [
          { text: '🎮 KK 触发器实战', link: '/kk-triggers/index' },
          { text: '⚡ 触发器系统', link: '/triggers/触发器是什么用大白话解释游戏逻辑' },
          { text: '🗺️ 地形编辑', link: '/terrain/5个让新手地图看起来更好看的地形技巧' },
          { text: '🎭 对象编辑器', link: '/object-editor/对象编辑器入门修改单位属性' },
          { text: '🏰 RPG 系统', link: '/rpg-systems/rpg英雄系统经验升级和属性设计' },
          { text: '📤 发布上线', link: '/publishing/如何把地图发布到kk平台完整上传步骤' },
          { text: '❓ 常见问题', link: '/faq/新手最常遇到的10个错误和解决方法' },
        ],
      },
      { text: '📋 更新日志', link: '/changelog' },
    ],

    // ── 侧边栏（由 gen_sidebar.ts 动态生成）────────────────────
    sidebar: generateSidebar(),

    // ── 社交链接 ────────────────────────────────────────────────
    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-org/war3-wiki' },
    ],

    // ── 页脚 ────────────────────────────────────────────────────
    footer: {
      message: '内容由多智能体 AI 系统自动生成，仅供学习参考',
      copyright: `Copyright © ${new Date().getFullYear()} War3 Wiki`,
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
  },
})
