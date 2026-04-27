// 扩展默认主题，注册自定义组件
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import ArticleFooter from '../components/ArticleFooter.vue'
import DiscoveredTopics from '../components/DiscoveredTopics.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // 注册全局组件
    app.component('ArticleFooter', ArticleFooter)
    app.component('DiscoveredTopics', DiscoveredTopics)
  },
} satisfies Theme
