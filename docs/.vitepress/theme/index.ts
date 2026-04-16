// 自定义 VitePress 主题：扩展默认主题，注入 ArticleFooter 组件
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import ArticleFooter from './ArticleFooter.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // 在每篇文章底部注入 AI 生成信息 + 反馈入口
      'doc-after': () => h(ArticleFooter),
    })
  },
  enhanceApp({ app }) {
    app.component('ArticleFooter', ArticleFooter)
  },
} satisfies Theme