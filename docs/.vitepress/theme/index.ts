// 扩展默认主题，注册自定义组件
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import ArticleFooter from '../components/ArticleFooter.vue'
import DiscoveredTopics from '../components/DiscoveredTopics.vue'
import SearchBar from '../components/SearchBar.vue'
import AuthorHome from '../components/AuthorHome.vue'
import AuthorEditor from '../components/AuthorEditor.vue'
import AuthorOps from '../components/AuthorOps.vue'
import ModelLibrary from '../components/ModelLibrary.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // 注册全局组件
    app.component('ArticleFooter', ArticleFooter)
    app.component('DiscoveredTopics', DiscoveredTopics)
    app.component('SearchBar', SearchBar)
    // /author/ 三页
    app.component('AuthorHome', AuthorHome)
    app.component('AuthorEditor', AuthorEditor)
    app.component('AuthorOps', AuthorOps)
    app.component('ModelLibrary', ModelLibrary)
  },
} satisfies Theme
