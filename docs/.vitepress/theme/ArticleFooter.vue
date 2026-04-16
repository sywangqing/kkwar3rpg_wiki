<template>
  <div v-if="frontmatter.ai_generated" class="article-footer">
    <div class="ai-meta">
      <div class="ai-badge">
        <span class="badge-icon">🤖</span>
        <span class="badge-text">AI 自动生成内容</span>
      </div>
      <div class="meta-details">
        <span v-if="frontmatter.generated_at" class="meta-item">
          📅 生成于 {{ formatDate(frontmatter.generated_at) }}
        </span>
        <span v-if="frontmatter.sources_count > 0" class="meta-item">
          📚 参考来源 {{ frontmatter.sources_count }} 篇
        </span>
        <span v-if="frontmatter.category_name" class="meta-item">
          📂 {{ frontmatter.category_name }}
        </span>
      </div>
    </div>

    <div class="feedback-section">
      <p class="feedback-text">
        本文由 AI 根据网络公开资料自动整理，内容仅供参考。<br />
        如发现错误或有补充建议，欢迎：
      </p>
      <div class="feedback-actions">
        <a
          :href="issueUrl"
          target="_blank"
          rel="noopener"
          class="feedback-btn primary"
        >
          🐛 提交错误反馈
        </a>
        <a
          :href="editUrl"
          target="_blank"
          rel="noopener"
          class="feedback-btn secondary"
        >
          ✏️ 直接编辑改进
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useData, useRoute } from 'vitepress'

const { frontmatter } = useData()
const route = useRoute()

const GITHUB_REPO = 'https://github.com/your-org/war3-wiki'

const issueUrl = computed(() => {
  const title = encodeURIComponent(`[内容反馈] ${frontmatter.value.title || route.path}`)
  return `${GITHUB_REPO}/issues/new?title=${title}&labels=content-feedback`
})

const editUrl = computed(() => {
  return `${GITHUB_REPO}/edit/main/docs${route.path}.md`
})

function formatDate(isoDate: string): string {
  try {
    const d = new Date(isoDate)
    return d.toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
  } catch {
    return isoDate
  }
}
</script>

<style scoped>
.article-footer {
  margin-top: 40px;
  padding: 20px;
  border-top: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}

.ai-meta {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 16px;
}

.ai-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background: var(--vp-c-brand-soft);
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  color: var(--vp-c-brand-1);
}

.meta-details {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.meta-item {
  font-size: 13px;
  color: var(--vp-c-text-2);
  padding: 2px 8px;
  background: var(--vp-c-bg-mute);
  border-radius: 4px;
}

.feedback-section {
  border-top: 1px dashed var(--vp-c-divider);
  padding-top: 16px;
}

.feedback-text {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin-bottom: 12px;
  line-height: 1.6;
}

.feedback-actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.feedback-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 13px;
  text-decoration: none;
  transition: opacity 0.2s;
}

.feedback-btn:hover {
  opacity: 0.8;
}

.feedback-btn.primary {
  background: var(--vp-c-brand-1);
  color: #fff;
}

.feedback-btn.secondary {
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
}
</style>
