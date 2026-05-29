<template>
  <div class="pagefind-search-wrapper">
    <div id="search" ref="searchContainer"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { withBase } from 'vitepress'

const searchContainer = ref<HTMLElement | null>(null)

onMounted(async () => {
  // 等待 Pagefind 资源加载
  if (typeof window !== 'undefined' && searchContainer.value) {
    try {
      // 使用 withBase 确保路径包含 base 前缀
      const pagefindPath = withBase('/pagefind/pagefind-ui.js')
      const { PagefindUI } = await import(/* @vite-ignore */ pagefindPath)
      
      new PagefindUI({
        element: '#search',
        showSubResults: true,
        showImages: false,
        resetStyles: false,
        translations: {
          placeholder: '搜索文章...',
          zero_results: '未找到「[ TERMS]」的相关结果',
        },
      })
    } catch (e) {
      console.warn('Pagefind UI 加载失败:', e)
    }
  }
})
</script>

<style>
.pagefind-search-wrapper {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}

.pagefind-search-wrapper #search {
  --pagefind-ui-scale: 0.85;
  --pagefind-ui-primary: #3b82f6;
  --pagefind-ui-text: #334155;
  --pagefind-ui-background: #ffffff;
  --pagefind-ui-border: #e2e8f0;
  --pagefind-ui-tag: #f1f5f9;
  --pagefind-ui-border-width: 1px;
  --pagefind-ui-border-radius: 8px;
  --pagefind-ui-image-border-radius: 8px;
  --pagefind-ui-image-box-ratio: 3/2;
  --pagefind-ui-font: 'Noto Sans SC', 'Chinese Quotes', 'Inter var', system-ui, -apple-system, sans-serif;
}

/* 深色模式适配 */
.dark .pagefind-search-wrapper #search {
  --pagefind-ui-text: #f1f5f9;
  --pagefind-ui-background: #1e293b;
  --pagefind-ui-border: #475569;
  --pagefind-ui-tag: #334155;
}
</style>
