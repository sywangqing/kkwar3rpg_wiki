<!--
  DiscoveredTopics.vue
  显示近 30 天由 AI 自动发现的新主题
  数据来源：从 /topics-meta.json（构建时生成）读取
-->
<template>
  <div class="discovered-section">
    <div v-if="loading" class="discovered-loading">⏳ 加载中...</div>

    <div v-else-if="topics.length === 0" class="discovered-empty">
      <p>暂无 AI 自动发现的主题（最近 30 天）</p>
    </div>

    <div v-else>
      <div class="discovered-topics-grid">
        <a
          v-for="topic in topics"
          :key="topic.slug"
          :href="topic.link"
          class="discovered-topic-card"
        >
          <div class="card-title">{{ topic.title }}</div>
          <div class="card-meta">
            <span class="card-source">🤖 {{ sourceLabel(topic.discovered_via) }}</span>
            <span v-if="topic.quality_score">
              {{ starRating(topic.quality_score) }} {{ (topic.quality_score * 100).toFixed(0) }}分
            </span>
            <span v-if="topic.discovered_at">{{ formatDate(topic.discovered_at) }}</span>
          </div>
        </a>
      </div>
      <p class="discovered-footer">
        共 <strong>{{ topics.length }}</strong> 个近期 AI 发现主题 ·
        <a href="/changelog">查看完整更新日志 →</a>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface TopicMeta {
  slug: string
  title: string
  link: string
  discovered_via: string
  discovered_at: string
  quality_score?: number
  category?: string
}

const topics = ref<TopicMeta[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    // topics-meta.json 由构建脚本（scripts/gen_topics_meta.ts）生成
    const res = await fetch('/topics-meta.json')
    if (res.ok) {
      const data: TopicMeta[] = await res.json()
      // 过滤：非 manual，且 discovered_at 在 30 天内
      const thirtyDaysAgo = Date.now() - 30 * 24 * 60 * 60 * 1000
      topics.value = data.filter((t) => {
        if (!t.discovered_via || t.discovered_via === 'manual') return false
        if (!t.discovered_at) return true // 无日期时显示
        const d = new Date(t.discovered_at).getTime()
        return d >= thirtyDaysAgo
      }).slice(0, 12) // 最多展示 12 个
    }
  } catch (e) {
    console.warn('topics-meta.json 加载失败', e)
  } finally {
    loading.value = false
  }
})

function sourceLabel(via: string): string {
  const map: Record<string, string> = {
    hive_workshop: 'Hive 社区',
    reddit: 'Reddit',
    nga: 'NGA 论坛',
    dota9: '9DOTA',
    auto: 'AI 发现',
  }
  return map[via] ?? via
}

function starRating(score: number): string {
  const filled = Math.round(score * 5)
  return '★'.repeat(filled) + '☆'.repeat(5 - filled)
}

function formatDate(dateStr: string): string {
  const d = new Date(dateStr)
  if (isNaN(d.getTime())) return dateStr
  const now = new Date()
  const diff = Math.floor((now.getTime() - d.getTime()) / (1000 * 60 * 60 * 24))
  if (diff === 0) return '今天'
  if (diff === 1) return '昨天'
  if (diff < 7) return `${diff} 天前`
  return d.toLocaleDateString('zh-CN', { month: 'short', day: 'numeric' })
}
</script>

<style scoped>
.discovered-section {
  margin-top: 0.5rem;
}

.discovered-loading,
.discovered-empty {
  color: var(--vp-c-text-3);
  font-size: 0.875rem;
  padding: 1rem 0;
}

.discovered-topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 0.75rem;
}

.discovered-topic-card {
  padding: 0.9rem 1rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 0.5rem;
  background: var(--vp-c-bg-elv, #fff);
  text-decoration: none;
  color: inherit;
  display: block;
  transition: box-shadow 0.2s, border-color 0.2s, transform 0.15s;
}

.discovered-topic-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  border-color: #93c5fd;
  transform: translateY(-2px);
}

.card-title {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--vp-c-text-1);
  margin-bottom: 0.4rem;
  line-height: 1.4;
}

.card-meta {
  font-size: 0.72rem;
  color: var(--vp-c-text-3);
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  align-items: center;
}

.card-source {
  background: #eff6ff;
  color: #3b82f6;
  padding: 0.1rem 0.45rem;
  border-radius: 99px;
  border: 1px solid #bfdbfe;
  font-size: 0.7rem;
}

.discovered-footer {
  margin-top: 1rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
}

.discovered-footer a {
  color: var(--vp-c-brand-1, #3b82f6);
  text-decoration: none;
}

.discovered-footer a:hover {
  text-decoration: underline;
}
</style>
