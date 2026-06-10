<script setup lang="ts">
// ModelLibrary.vue — tbwlm.cn 模型库镜像板块（静态复刻）
// 数据来自 docs/.vitepress/_models_data.json
import { ref, computed } from 'vue'
import { withBase } from 'vitepress'
import data from '../_models_data.json'

const link = (p: string) => withBase(p)

const activeCat = ref('all')
const activeTag = ref('')
const sortBy = ref<'newest' | 'downloads' | 'views'>('newest')

const tagCounts = computed(() => {
  const m: Record<string, number> = {}
  for (const md of data.models) for (const t of md.tags) m[t] = (m[t] || 0) + 1
  return m
})
const hotTags = computed(() => data.tags.filter(t => tagCounts.value[t]))

const filtered = computed(() => {
  let list = data.models.slice()
  if (activeCat.value !== 'all') list = list.filter(m => m.category === activeCat.value)
  if (activeTag.value) list = list.filter(m => m.tags.includes(activeTag.value))
  if (sortBy.value === 'downloads') list.sort((a, b) => b.downloads - a.downloads)
  else if (sortBy.value === 'views') list.sort((a, b) => b.views - a.views)
  else list.sort((a, b) => b.createdAt.localeCompare(a.createdAt))
  return list
})

// 首页动画展示：取有缩略图的模型轮播
const showcase = computed(() => data.models.filter(m => m.thumbnail))
</script>

<template>
  <div class="ml-root">
    <!-- Hero 动画展示区 -->
    <section class="ml-hero">
      <div class="ml-hero-bg"></div>
      <div class="ml-hero-inner">
        <div class="ml-hero-text">
          <div class="ml-brand">{{ data.site.name }} · {{ data.site.nameEn }}</div>
          <h1 class="ml-title">{{ data.site.tagline }}</h1>
          <p class="ml-sub">{{ data.site.subtagline }}</p>
          <div class="ml-stats">
            <div><b>{{ data.models.length }}</b><span>模型总数</span></div>
            <div><b>{{ data.categories.length - 1 }}</b><span>分类</span></div>
            <div><b>{{ data.tags.length }}</b><span>标签</span></div>
          </div>
          <p class="ml-mirror-note">
            📦 本板块为
            <a :href="data.site.source" target="_blank" rel="noreferrer">{{ data.site.source }}</a>
            内容镜像（{{ data.site.mirroredAt }}）· 模型文件可直接下载，登录/充值/购物车等交易功能请前往原站。
          </p>
        </div>
        <!-- 模型动画展示卡 -->
        <div class="ml-showcase">
          <a v-for="m in showcase" :key="m.uid" class="ml-showcase-card" :href="'#' + m.uid">
            <div class="ml-showcase-frame">
              <img :src="link(m.thumbnail)" :alt="m.title" loading="lazy" />
              <span class="ml-showcase-badge">⚡ 动画预览</span>
            </div>
            <div class="ml-showcase-name">{{ m.title }}</div>
          </a>
        </div>
      </div>
    </section>

    <!-- 筛选区 -->
    <section class="ml-filters">
      <div class="ml-cat-row">
        <button
          v-for="c in data.categories" :key="c.value"
          class="ml-chip" :class="{ active: activeCat === c.value }"
          @click="activeCat = c.value">
          {{ c.label }}
        </button>
      </div>
      <div class="ml-tag-row" v-if="hotTags.length">
        <span class="ml-tag-label">热门标签：</span>
        <button
          v-for="t in hotTags" :key="t"
          class="ml-tag" :class="{ active: activeTag === t }"
          @click="activeTag = activeTag === t ? '' : t">
          {{ t }} ({{ tagCounts[t] }})
        </button>
      </div>
      <div class="ml-toolbar">
        <span class="ml-count">找到 {{ filtered.length }} 个模型</span>
        <select v-model="sortBy" class="ml-sort">
          <option value="newest">最新发布</option>
          <option value="downloads">下载最多</option>
          <option value="views">浏览最多</option>
        </select>
      </div>
    </section>

    <!-- 模型网格 -->
    <section class="ml-grid">
      <article v-for="m in filtered" :key="m.uid" :id="m.uid" class="ml-card">
        <div class="ml-card-thumb">
          <img :src="link(m.thumbnail)" :alt="m.title" loading="lazy" />
          <span class="ml-card-cat">{{ m.categoryLabel }}</span>
        </div>
        <div class="ml-card-body">
          <h3 class="ml-card-title">{{ m.title }}</h3>
          <p class="ml-card-desc">{{ m.description }}</p>
          <div class="ml-card-tags">
            <span v-for="t in m.tags" :key="t" class="ml-mini-tag">{{ t }}</span>
          </div>
          <div class="ml-card-meta">
            <span>👤 {{ m.author }}</span>
            <span>💾 {{ m.fileSize }}</span>
            <span>📅 {{ m.createdAt }}</span>
          </div>
          <div class="ml-card-stats">
            <span>⬇ {{ m.downloads }}</span>
            <span>👁 {{ m.views }}</span>
            <span>❤ {{ m.likes }}</span>
            <span class="ml-price">💎 {{ m.price }} 积分</span>
          </div>
          <div class="ml-card-actions">
            <a class="ml-dl ml-dl-primary" :href="link(m.modelFile)" download>下载 .mdx</a>
            <a class="ml-dl" :href="link(m.zip)" download>下载完整包 .zip</a>
          </div>
        </div>
      </article>

      <div v-if="!filtered.length" class="ml-empty">该分类 / 标签下暂无模型</div>
    </section>

    <!-- 即将上线占位 -->
    <section class="ml-soon">
      <div class="ml-soon-card">🗺️ 热门地形模板<small>即将上线</small></div>
      <div class="ml-soon-card">🏆 优秀学员作品<small>即将上线</small></div>
      <div class="ml-soon-card">⚡ 炫酷技能<small>即将上线</small></div>
    </section>

    <footer class="ml-foot">
      © 2026 魔兽争霸3模型库 · 为魔兽争霸3社区提供优质模型资源 ·
      原站 <a :href="data.site.source" target="_blank" rel="noreferrer">tbwlm.cn</a>
    </footer>
  </div>
</template>

<style scoped>
.ml-root { max-width: 1152px; margin: 0 auto; padding: 0 12px 48px; }

/* Hero */
.ml-hero {
  position: relative; border-radius: 16px; overflow: hidden;
  margin: 16px 0 28px; padding: 36px 32px;
  background: linear-gradient(135deg, #0f1430 0%, #1a1346 55%, #2a1a4d 100%);
  color: #e8e8f5;
}
.ml-hero-bg {
  position: absolute; inset: 0;
  background:
    radial-gradient(circle at 80% 20%, rgba(124,58,237,.35), transparent 45%),
    radial-gradient(circle at 15% 90%, rgba(245,158,11,.18), transparent 40%);
  pointer-events: none;
}
.ml-hero-inner { position: relative; display: flex; gap: 32px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.ml-hero-text { flex: 1 1 420px; }
.ml-brand { font-size: 13px; letter-spacing: .5px; color: #a78bfa; font-weight: 600; }
.ml-title {
  font-size: 40px; font-weight: 800; margin: 10px 0 6px; border: 0; line-height: 1.1;
  background: linear-gradient(90deg, #fbbf24, #f59e0b); -webkit-background-clip: text;
  background-clip: text; color: transparent;
}
.ml-sub { font-size: 16px; color: #c4b5fd; margin: 0 0 18px; }
.ml-stats { display: flex; gap: 14px; margin-bottom: 16px; }
.ml-stats > div {
  background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.1);
  border-radius: 10px; padding: 10px 18px; text-align: center; min-width: 78px;
}
.ml-stats b { display: block; font-size: 22px; color: #fbbf24; }
.ml-stats span { font-size: 12px; color: #b9b6d6; }
.ml-mirror-note { font-size: 12.5px; color: #9d9ac0; line-height: 1.6; margin: 0; }
.ml-mirror-note a { color: #a78bfa; }

/* Showcase */
.ml-showcase { display: flex; gap: 14px; flex-wrap: wrap; flex: 0 1 auto; }
.ml-showcase-card { text-decoration: none; color: inherit; }
.ml-showcase-frame {
  position: relative; width: 168px; height: 168px; border-radius: 14px; overflow: hidden;
  border: 1px solid rgba(167,139,250,.35); background: #0b0e22;
  box-shadow: 0 8px 28px rgba(0,0,0,.4);
}
.ml-showcase-frame img { width: 100%; height: 100%; object-fit: contain; }
.ml-showcase-badge {
  position: absolute; top: 8px; left: 8px; font-size: 11px; padding: 2px 8px;
  background: rgba(124,58,237,.85); border-radius: 999px; color: #fff;
}
.ml-showcase-name { font-size: 13px; color: #d7d4ee; margin-top: 8px; text-align: center; max-width: 168px; }

/* Filters */
.ml-filters { margin-bottom: 20px; }
.ml-cat-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }
.ml-chip {
  border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1); border-radius: 999px; padding: 5px 14px; font-size: 13px; cursor: pointer;
  transition: all .15s;
}
.ml-chip:hover { border-color: var(--vp-c-brand-1); }
.ml-chip.active { background: var(--vp-c-brand-1); color: #fff; border-color: var(--vp-c-brand-1); }
.ml-tag-row { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 12px; }
.ml-tag-label { font-size: 13px; color: var(--vp-c-text-2); }
.ml-tag {
  border: 1px solid var(--vp-c-divider); background: transparent; color: var(--vp-c-text-2);
  border-radius: 6px; padding: 3px 10px; font-size: 12px; cursor: pointer;
}
.ml-tag.active { background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); border-color: var(--vp-c-brand-1); }
.ml-toolbar { display: flex; justify-content: space-between; align-items: center; }
.ml-count { font-size: 14px; color: var(--vp-c-text-2); }
.ml-sort {
  border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); color: var(--vp-c-text-1);
  border-radius: 8px; padding: 6px 12px; font-size: 13px;
}

/* Grid */
.ml-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(248px, 1fr)); gap: 18px; }
.ml-card {
  border: 1px solid var(--vp-c-divider); border-radius: 14px; overflow: hidden;
  background: var(--vp-c-bg-soft); transition: transform .15s, box-shadow .15s;
}
.ml-card:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,.18); }
.ml-card-thumb { position: relative; aspect-ratio: 1; background: #0b0e22; }
.ml-card-thumb img { width: 100%; height: 100%; object-fit: contain; }
.ml-card-cat {
  position: absolute; top: 8px; left: 8px; font-size: 11px; padding: 2px 8px;
  background: rgba(124,58,237,.9); color: #fff; border-radius: 999px;
}
.ml-card-body { padding: 14px; }
.ml-card-title { font-size: 15px; font-weight: 700; margin: 0 0 4px; }
.ml-card-desc { font-size: 13px; color: var(--vp-c-text-2); margin: 0 0 8px; }
.ml-card-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 8px; }
.ml-mini-tag { font-size: 11px; padding: 1px 7px; border-radius: 4px; background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); }
.ml-card-meta, .ml-card-stats { display: flex; flex-wrap: wrap; gap: 10px; font-size: 12px; color: var(--vp-c-text-3); margin-bottom: 8px; }
.ml-price { color: #f59e0b; font-weight: 600; }
.ml-card-actions { display: flex; gap: 8px; flex-wrap: wrap; }
.ml-dl {
  flex: 1; text-align: center; font-size: 13px; padding: 7px 10px; border-radius: 8px;
  border: 1px solid var(--vp-c-brand-1); color: var(--vp-c-brand-1); text-decoration: none; white-space: nowrap;
}
.ml-dl-primary { background: var(--vp-c-brand-1); color: #fff; }
.ml-dl:hover { opacity: .88; }
.ml-empty { grid-column: 1 / -1; text-align: center; color: var(--vp-c-text-3); padding: 48px 0; }

/* Soon */
.ml-soon { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 32px 0; }
.ml-soon-card {
  border: 1px dashed var(--vp-c-divider); border-radius: 12px; padding: 28px; text-align: center;
  font-size: 16px; font-weight: 600; color: var(--vp-c-text-2);
}
.ml-soon-card small { display: block; font-size: 12px; font-weight: 400; color: var(--vp-c-text-3); margin-top: 6px; }

.ml-foot { text-align: center; font-size: 12px; color: var(--vp-c-text-3); margin-top: 28px; padding-top: 18px; border-top: 1px solid var(--vp-c-divider); }
.ml-foot a { color: var(--vp-c-brand-1); }

@media (max-width: 720px) {
  .ml-title { font-size: 30px; }
  .ml-showcase { width: 100%; justify-content: center; }
}
</style>
