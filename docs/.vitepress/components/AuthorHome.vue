<script setup lang="ts">
// AuthorHome.vue — KK 作者中心首页（方案 B）
// 数据来自 prebuild 脚本生成的 _author_data.json
import data from '../_author_data.json'
import { withBase } from 'vitepress'

const { stats, recent } = data

// VitePress 子路径感知（base = /kkwar3rpg_wiki/）
const link = (p: string) => withBase(p)
</script>

<template>
  <div class="au-page">

    <!-- 英雄区 -->
    <section class="au-hero">
      <span class="au-hero-badge">面向 KK 新作者 · 持续更新</span>
      <h1>从注册到上线，<br/>把第一张图做出来。</h1>
      <p class="au-hero-sub">
        不灌鸡汤，不堆术语。
        <strong>{{ stats.editor }}+ 篇 KK 实战教程</strong> +
        <strong>{{ stats.demos }} 个演示图源码</strong> +
        <strong>KK 平台运营手册</strong>，按你需要的顺序铺好。
      </p>
      <div class="au-hero-actions">
        <a class="au-btn au-btn-primary" :href="link('/author/editor')">🚀 入职 KK · 5 分钟开始</a>
        <a class="au-btn au-btn-ghost" href="https://create.kkdzpt.com/docs/guides/Editor/About" target="_blank" rel="noreferrer">📖 KK 官方启航手册</a>
      </div>

      <!-- KK 作者旅程 -->
      <div id="start-here" class="au-journey">
        <div class="au-journey-title">📍 KK 作者旅程</div>
        <div class="au-journey-grid">
          <a class="au-journey-step" :href="link('/author/editor')">
            <div class="au-step-num">1</div>
            <div class="au-step-title">注册入职</div>
            <div class="au-step-desc">填登记表 · 进社群</div>
          </a>
          <a class="au-journey-step" :href="link('/author/editor')">
            <div class="au-step-num">2</div>
            <div class="au-step-title">学编辑器</div>
            <div class="au-step-desc">Y3 / KKWE 怎么选</div>
          </a>
          <a class="au-journey-step" :href="link('/author/editor')">
            <div class="au-step-num">3</div>
            <div class="au-step-title">做第一张图</div>
            <div class="au-step-desc">从编辑器教学开始</div>
          </a>
        </div>
      </div>
    </section>

    <!-- 三大板块大卡片 -->
    <section class="au-section-cards">
      <a class="au-card" :href="link('/author/newbie/faq/产品手册')">
        <div class="au-card-icon">🚀</div>
        <div class="au-card-tag au-card-tag-purple">第一站 · 官方入驻 + 产品手册</div>
        <div class="au-card-title">新人必读</div>
        <p class="au-card-desc">KK 官方入驻流程（登记 → 启航手册 → 社群）+ 完整产品手册（立项/玩法/商业化/上线）。</p>
        <ul class="au-card-list">
          <li>• KK 官方入驻流程（4 步）</li>
          <li>• 目标用户画像</li>
          <li>• 立项决策（7 问 + 赛道选择）</li>
          <li>• 玩法设计（黄金 10 分钟 + 核心循环）</li>
          <li>• 商业化设计与付费节奏</li>
          <li>• 上线检查 + 踩坑指南</li>
        </ul>
        <div class="au-card-cta au-card-tag-purple">进入新人必读 →</div>
      </a>

      <a class="au-card" :href="link('/author/editor')">
        <div class="au-card-icon">🛠️</div>
        <div class="au-card-tag au-card-tag-amber">能力树 · {{ stats.editor }}+ 篇</div>
        <div class="au-card-title">编辑器教学</div>
        <p class="au-card-desc">按"学习阶段"重排，不再按工具堆。从零基础的"前 30 分钟"到大型 RPG 架构。</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;font-size:14px;color:var(--vp-c-text-2);">
          <div style="display:flex;justify-content:space-between"><span>快速入门</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['getting-started'] }}</span></div>
          <div style="display:flex;justify-content:space-between"><span>触发器 GUI</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['triggers'] }}</span></div>
          <div style="display:flex;justify-content:space-between"><span>对象编辑器</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['objects'] }}</span></div>
          <div style="display:flex;justify-content:space-between"><span>地形与场景</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['terrain'] }}</span></div>
          <div style="display:flex;justify-content:space-between;font-weight:600;color:#d97706"><span>🎯 实战库</span><span style="font-size:12px">{{ data.editorBuckets['demos'] }}+</span></div>
          <div style="display:flex;justify-content:space-between"><span>RPG 系统</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['systems'] + data.editorBuckets['advanced'] }}</span></div>
          <div style="display:flex;justify-content:space-between"><span>JASS / Lua</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['scripting'] }}</span></div>
          <div style="display:flex;justify-content:space-between"><span>第三方工具</span><span style="color:var(--vp-c-text-3);font-size:12px">{{ data.editorBuckets['tools'] }}</span></div>
        </div>
        <div class="au-card-cta au-card-tag-amber">进入编辑器教学 →</div>
      </a>

      <a class="au-card au-card-ops" :href="link('/author/operations')">
        <div class="au-card-icon">📈</div>
        <div class="au-card-tag au-card-tag-orange">作者必修 · {{ stats.ops }} 篇</div>
        <div class="au-card-title">运营教学</div>
        <p class="au-card-desc">很多人只顾做图、忽略运营，结果地图没人玩。KK 生态、上线、平台工具、商业化——新作者最容易缺的一课。</p>
        <ul class="au-card-list">
          <li>• 入门 KK 生态（审核 / 课程 / 月度发行观察）</li>
          <li>• 上线发布（上传 / 加密 / 性能）</li>
          <li>• 平台工具（宝箱 / 礼包码 / 签到 / 数据分析）</li>
          <li>• 商业化与增长（氪金点 / 推广 / 付费洞察）</li>
        </ul>
        <div class="au-card-cta au-card-tag-orange">进入运营教学 →</div>
      </a>
    </section>

    <!-- 数据条 -->
    <section class="au-stats">
      <div class="au-stats-grid">
        <div>
          <div class="au-stat-num au-purple">{{ stats.editor }}+</div>
          <div class="au-stat-label">编辑器实战篇</div>
        </div>
        <div>
          <div class="au-stat-num au-green">{{ stats.demos }}</div>
          <div class="au-stat-label">KK 演示图 GUI 源码</div>
        </div>
        <div>
          <div class="au-stat-num au-amber">{{ stats.shenmuTriggers }}</div>
          <div class="au-stat-label">神墓 2.7C 全量触发器</div>
        </div>
        <div>
          <div class="au-stat-num au-orange">{{ stats.ops }}</div>
          <div class="au-stat-label">KK 运营 / 平台教程</div>
        </div>
      </div>
      <div class="au-stats-foot">数据由构建脚本扫描 docs/ 目录自动生成</div>
    </section>

    <!-- 最常翻 6 篇 + 月度观察 -->
    <div style="display:grid;grid-template-columns:2fr 1fr;gap:1.25rem;margin:1.5rem 0;">
      <div class="au-stats" style="margin:0">
        <h3 style="margin:0 0 1rem;font-size:1.125rem;font-weight:700;display:flex;align-items:center;gap:6px">🔥 新作者最常翻的 6 篇</h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
          <a class="au-grid-item" :href="link('/author/editor')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">打开编辑器的前 30 分钟</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 快速入门</div>
          </a>
          <a class="au-grid-item" :href="link('/author/editor')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">事件 / 条件 / 动作 三要素</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 触发器 GUI</div>
          </a>
          <a class="au-grid-item" :href="link('/author/editor')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">5 个触发器模板（直接套用）</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 触发器 GUI</div>
          </a>
          <a class="au-grid-item" :href="link('/author/editor')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">神墓 2.7C 全量 171 触发器</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 KK 触发器实战</div>
          </a>
          <a class="au-grid-item au-card-ops" :href="link('/author/operations')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">如何把地图发布到 KK 平台</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 上线发布 · 运营</div>
          </a>
          <a class="au-grid-item au-card-ops" :href="link('/author/operations')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">KK 用户付费行为洞察</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">📁 商业化 · 运营</div>
          </a>
        </div>
        <div style="font-size:11px;color:var(--vp-c-text-3);margin-top:.75rem">现阶段手工挑选，未来接 PV 数据自动更新</div>
      </div>

      <a class="au-watch-card" :href="link('/author/operations#monthly-watch')" style="text-decoration:none;color:inherit;display:flex;flex-direction:column">
        <div style="font-size:.875rem;color:var(--vp-c-kk-3);display:flex;align-items:center;gap:6px">📅 KK 月度地图发行观察</div>
        <div style="font-weight:700;font-size:1.25rem;margin-top:.5rem;line-height:1.4;color:var(--vp-c-text-1)">每月哪些图火了，<br/>为什么火？</div>
        <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:.5rem 0 1rem;line-height:1.6">KK 运营官方课件整理。新作者立项前一定要看一眼。</p>
        <div style="background:rgba(255,255,255,0.6);border-radius:6px;padding:.625rem;backdrop-filter:blur(4px)">
          <div style="font-size:.75rem;color:var(--vp-c-kk-3)">最近一期</div>
          <div style="font-weight:600;font-size:.875rem;margin-top:2px;color:var(--vp-c-text-1)">2025 全年运营课程回顾</div>
        </div>
        <div style="font-size:.75rem;color:var(--vp-c-kk-3);margin-top:.5rem;line-height:1.6">
          往期 6 篇：3月 · 6月 · 8-9月 · 10月 · 11月 · 1-28 重点事件
        </div>
        <div style="margin-top:auto;padding-top:1rem;font-size:.875rem;font-weight:600;color:var(--vp-c-kk-2)">进入观察栏目 →</div>
      </a>
    </div>

    <!-- 最近更新 -->
    <section class="au-stats" v-if="recent && recent.length">
      <h3 style="margin:0 0 1rem;font-size:1.125rem;font-weight:700;display:flex;align-items:center;gap:6px">🆕 最近更新</h3>
      <ul style="padding:0;margin:0;list-style:none;font-size:.875rem">
        <li v-for="r in recent" :key="r.path" style="display:flex;justify-content:space-between;gap:.5rem;padding:.5rem 0;border-bottom:1px solid var(--vp-c-divider)">
          <a :href="link(r.path)" style="flex:1;text-decoration:none;color:var(--vp-c-text-1)">{{ r.title }}</a>
          <span style="font-size:.75rem;color:var(--vp-c-text-3);flex-shrink:0">{{ r.updated }}</span>
        </li>
      </ul>
    </section>

    <!-- 我想做… -->
    <section style="margin-top:2rem">
      <h2 style="border:none;padding:0;font-size:1.125rem;font-weight:700;margin-bottom:.5rem">🔎 我想做……</h2>
      <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:0 0 1rem">老作者直奔主题入口，按场景跳到对应文章。</p>
      <div class="au-tags">
        <a class="au-tag" :href="link('/author/editor')">英雄选择</a>
        <a class="au-tag" :href="link('/author/editor')">背包系统</a>
        <a class="au-tag" :href="link('/author/editor')">存档读档</a>
        <a class="au-tag" :href="link('/author/editor')">弹道技能</a>
        <a class="au-tag" :href="link('/author/editor')">商城</a>
        <a class="au-tag" :href="link('/author/editor')">伤害计算</a>
        <a class="au-tag" :href="link('/author/editor')">Boss AI</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">发到 KK</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">配宝箱</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">设计氪金点</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">看付费数据</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">配活动</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">发礼包码</a>
        <a class="au-tag au-tag-ops" :href="link('/author/operations')">看数据后台</a>
      </div>
    </section>

  </div>
</template>
