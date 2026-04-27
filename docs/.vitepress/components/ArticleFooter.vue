<template>
  <div v-if="hasMetadata" class="article-footer">
    <!-- AI 质量评分 -->
    <div v-if="qualityScore !== null" class="quality-section">
      <span class="quality-label">📊 AI 质量评分</span>
      <span class="quality-stars" :title="`质量分: ${qualityScore}`">
        <span
          v-for="n in 5"
          :key="n"
          class="star"
          :class="{ filled: n <= filledStars, half: n === halfStar }"
        >{{ n <= filledStars ? '★' : (n === halfStar ? '⯨' : '☆') }}</span>
      </span>
      <span class="quality-score-text">{{ (qualityScore * 100).toFixed(0) }}分</span>
      <span v-if="qualityWarning" class="quality-warning" :title="qualityWarning">
        ⚠️ {{ qualityWarning }}
      </span>
    </div>

    <!-- 徽章区域 -->
    <div class="badges-section">
      <span v-if="discoveredVia && discoveredVia !== 'manual'" class="badge badge-ai">
        🤖 {{ discoveredViaLabel }}
      </span>
      <span v-else-if="discoveredVia === 'manual'" class="badge badge-manual">
        ✍️ 人工整理
      </span>
      <span v-if="model" class="badge badge-model" :title="`生成模型: ${model}`">
        ⚡ {{ modelShortName }}
      </span>
      <span v-if="updated" class="badge badge-updated">
        🕐 {{ updated }}
      </span>
    </div>

    <div v-if="sourcesCount > 0" class="sources-count">
      📚 本文参考了 <strong>{{ sourcesCount }}</strong> 个来源
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'

const { frontmatter } = useData()

const qualityScore = computed<number | null>(() => {
  const v = frontmatter.value?.quality_score
  return typeof v === 'number' ? v : null
})

const qualityWarning = computed<string | null>(() => frontmatter.value?.quality_warning ?? null)

const filledStars = computed(() => {
  if (qualityScore.value === null) return 0
  return Math.floor(qualityScore.value * 5)
})

const halfStar = computed(() => {
  if (qualityScore.value === null) return 0
  const remainder = (qualityScore.value * 5) - filledStars.value
  return remainder >= 0.4 ? filledStars.value + 1 : 0
})

const discoveredVia = computed<string | null>(() => frontmatter.value?.discovered_via ?? null)

const discoveredViaLabel = computed(() => {
  const map: Record<string, string> = {
    hive_workshop: 'Hive 社区发现',
    reddit: 'Reddit 发现',
    nga: 'NGA 论坛发现',
    dota9: '9 DOTA 论坛发现',
    auto: 'AI 自动发现',
  }
  return map[discoveredVia.value ?? ''] ?? `AI 发现 (${discoveredVia.value})`
})

const model = computed<string | null>(() => frontmatter.value?.model ?? null)

const modelShortName = computed(() =>
  (model.value ?? '').replace(/openai\//, '').replace(/-highspeed$/, '').replace(/-/g, ' ')
)

const updated = computed<string | null>(() => frontmatter.value?.updated ?? null)

const sourcesCount = computed<number>(() => {
  const s = frontmatter.value?.sources
  if (Array.isArray(s)) return s.length
  if (typeof s === 'number') return s
  return 0
})

const hasMetadata = computed(() =>
  qualityScore.value !== null || discoveredVia.value !== null || model.value !== null
)
</script>

<style scoped>
.article-footer {
  margin-top: 2rem;
  padding: 1rem 1.25rem;
  border-top: 1px solid var(--vp-c-divider);
  border-radius: 0.5rem;
  background: var(--vp-c-bg-soft);
  font-size: 0.875rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.quality-section {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.quality-label { font-weight: 600; color: var(--vp-c-text-2); }

.quality-stars {
  display: inline-flex;
  gap: 1px;
  font-size: 1.1rem;
  line-height: 1;
}

.star.filled { color: #f5a623; }
.star.half   { color: #f5a623; opacity: 0.6; }
.star:not(.filled):not(.half) { color: var(--vp-c-text-3); }

.quality-score-text { color: var(--vp-c-text-2); font-variant-numeric: tabular-nums; }

.quality-warning {
  font-size: 0.8rem;
  background: #fff8e6;
  color: #b45309;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.badges-section { display: flex; gap: 0.4rem; flex-wrap: wrap; align-items: center; }

.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.2rem 0.6rem;
  border-radius: 99px;
  font-size: 0.75rem;
  font-weight: 500;
  white-space: nowrap;
}

.badge-ai     { background: #eff6ff; color: #3b82f6; border: 1px solid #bfdbfe; }
.badge-manual { background: #f0fdf4; color: #16a34a; border: 1px solid #86efac; }
.badge-model  { background: #faf5ff; color: #9333ea; border: 1px solid #d8b4fe; }
.badge-updated {
  background: var(--vp-c-bg-elv, #f6f6f7);
  color: var(--vp-c-text-2, #666);
  border: 1px solid var(--vp-c-divider, #ddd);
}

.sources-count { color: var(--vp-c-text-2); font-size: 0.8rem; }
.sources-count strong { color: #3b82f6; }
</style>
