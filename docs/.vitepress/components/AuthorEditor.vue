<script setup lang="ts">
// AuthorEditor.vue — 编辑器教学落地页
import data from '../_author_data.json'
import { withBase } from 'vitepress'
const link = (p: string) => withBase(p)
const buckets = data.editorBuckets
</script>

<template>
  <div class="au-page">

    <!-- 「我该从哪开始」分流 -->
    <div class="au-info">
      <div class="au-info-title">ℹ️ 不知道从哪开始？</div>
      <div style="display:flex;flex-direction:column;gap:.5rem;font-size:.875rem">
        <div>
          <strong>▸ 我是纯新手，从没碰过 WE</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">走「快速入门」{{ buckets['getting-started'] }} 篇，按顺序读完就能开第一张图。</span>
          <a :href="link('/author/newbie/打开编辑器的前30分钟你应该做什么')" style="color:var(--vp-c-brand-1)">→ 跳过去</a>
        </div>
        <div>
          <strong>▸ 我用过 WE，要补 KK 平台知识</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">直接看「KK 触发器实战库」，看差异和实战。</span>
          <a :href="link('/author/editor/demos/index')" style="color:var(--vp-c-brand-1)">→ 跳过去</a>
        </div>
        <div>
          <strong>▸ 我有具体问题，想直接查</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">用顶栏搜索，或翻到底下「编辑器场景跳转」标签。</span>
        </div>
      </div>
    </div>

    <!-- 学习路径 -->
    <h2 style="border-left:4px solid var(--vp-c-brand-1);padding-left:.75rem;margin-top:2.5rem">⭐ 学习路径</h2>
    <div class="au-path">
      <div class="au-path-grid">
        <div class="au-path-step">
          <div class="au-path-circle" style="background:var(--vp-c-brand-soft);color:var(--vp-c-brand-1)">🌱</div>
          <div class="au-path-name">新手起步</div>
          <div class="au-path-meta">快速入门 {{ buckets['getting-started'] }}</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:#ddd6fe;color:#5b21b6">🔧</div>
          <div class="au-path-name">核心技能</div>
          <div class="au-path-meta">触发器 {{ buckets['triggers'] }} · 对象 {{ buckets['objects'] }} · 地形 {{ buckets['terrain'] }}</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:#a78bfa;color:#fff">🎯</div>
          <div class="au-path-name">实战临摹 ⭐</div>
          <div class="au-path-meta">实战库 {{ buckets['demos'] }}+</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:var(--vp-c-brand-2);color:#fff">🚀</div>
          <div class="au-path-name">进阶</div>
          <div class="au-path-meta">RPG {{ buckets['systems'] + buckets['advanced'] }} · JASS {{ buckets['scripting'] }} · 工具 {{ buckets['tools'] }}</div>
        </div>
      </div>
    </div>

    <!-- 子主题宫格 -->
    <h2 style="border-left:4px solid var(--vp-c-brand-1);padding-left:.75rem;margin-top:2.5rem">📚 子主题</h2>
    <div class="au-grid">

      <a id="quickstart" class="au-grid-item" :href="link('/author/newbie/打开编辑器的前30分钟你应该做什么')">
        <div class="au-grid-head"><span class="au-grid-icon">🌱</span><span class="au-grid-badge">{{ buckets['getting-started'] }} 篇</span></div>
        <div class="au-grid-title">快速入门</div>
        <div class="au-grid-sub">装好编辑器，做出能跑的第一张图</div>
        <ul class="au-grid-list">
          <li>• 打开编辑器的前 30 分钟</li>
          <li>• 编辑器界面功能全览</li>
          <li>• 创建第一张 RPG 地图</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/triggers/事件条件动作触发器三要素详解')">
        <div class="au-grid-head"><span class="au-grid-icon">⚡</span><span class="au-grid-badge">{{ buckets['triggers'] }} 篇</span></div>
        <div class="au-grid-title">触发器 GUI</div>
        <div class="au-grid-sub">不会写代码也能写游戏逻辑</div>
        <ul class="au-grid-list">
          <li>• 事件 / 条件 / 动作 三要素</li>
          <li>• 5 个触发器模板（直接套用）</li>
          <li>• 触发器不生效怎么办：调试排错</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/objects/对象编辑器入门修改单位属性')">
        <div class="au-grid-head"><span class="au-grid-icon">⚙️</span><span class="au-grid-badge">{{ buckets['objects'] }} 篇</span></div>
        <div class="au-grid-title">对象编辑器</div>
        <div class="au-grid-sub">单位 / 技能 / 物品 / 光环 / 升级</div>
        <ul class="au-grid-list">
          <li>• 对象编辑器入门：修改单位属性</li>
          <li>• 制作简单技能：给英雄加专属能力</li>
          <li>• 物品编辑器与物品系统</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/terrain/5个让新手地图看起来更好看的地形技巧')">
        <div class="au-grid-head"><span class="au-grid-icon">🗺️</span><span class="au-grid-badge">{{ buckets['terrain'] }} 篇</span></div>
        <div class="au-grid-title">地形与场景</div>
        <div class="au-grid-sub">让地图看起来不像新手做的</div>
        <ul class="au-grid-list">
          <li>• 5 个让新手地图更好看的技巧</li>
          <li>• 地形纹理与贴图技巧</li>
          <li>• 灯光与氛围：让地图有场景感</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <!-- KK 实战库 ⭐ 加重 -->
      <a id="kk-triggers" class="au-grid-item au-emph" :href="link('/author/editor/demos/index')">
        <span class="au-star-corner">⭐ 新作者最常用</span>
        <div class="au-grid-head">
          <span class="au-grid-icon">🎯</span>
          <span class="au-grid-badge au-purple">{{ buckets['demos'] }}+ 演示图</span>
        </div>
        <div class="au-grid-title" style="color:var(--vp-c-brand-3);font-size:1.25rem">KK 触发器实战库</div>
        <div style="font-size:.875rem;color:var(--vp-c-brand-2);margin-bottom:.75rem">真实演示图 GUI 源码，复制到 KKWE 即用。这是 KK 作者最实用的一档。</div>
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:.5rem;font-size:.75rem;margin-top:.75rem">
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🦸 英雄</div><div style="color:var(--vp-c-text-3)">5</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">⚔️ 战斗</div><div style="color:var(--vp-c-text-3)">5</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🎯 技能</div><div style="color:var(--vp-c-text-3)">12</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🎒 物品</div><div style="color:var(--vp-c-text-3)">9</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🖼️ UI</div><div style="color:var(--vp-c-text-3)">10</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">💾 存档</div><div style="color:var(--vp-c-text-3)">3</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">📐 数学</div><div style="color:var(--vp-c-text-3)">7</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🔧 黑科技</div><div style="color:var(--vp-c-text-3)">8</div>
          </div>
          <div style="background:var(--vp-c-bg);border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600">🚪 其他</div><div style="color:var(--vp-c-text-3)">7</div>
          </div>
          <div style="background:#fef3c7;border:1px solid #fcd34d;border-radius:4px;padding:.5rem;text-align:center">
            <div style="font-weight:600;color:#b45309">📦 神墓 ⭐</div><div style="color:#d97706">171</div>
          </div>
        </div>
        <div class="au-grid-cta" style="margin-top:1rem">进入实战库 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/systems/rpg英雄系统经验升级和属性设计')">
        <div class="au-grid-head"><span class="au-grid-icon">🏆</span><span class="au-grid-badge">{{ buckets['systems'] + buckets['advanced'] }} 篇</span></div>
        <div class="au-grid-title">RPG 系统搭建</div>
        <div class="au-grid-sub">英雄 / 背包 / 商店 / Boss / 存档 / 多人</div>
        <ul class="au-grid-list">
          <li>• RPG 英雄系统：经验升级和属性</li>
          <li>• 存档读档系统</li>
          <li>• 设计第一个 Boss AI</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/scripting/jass入门从t触发翻译到代码')">
        <div class="au-grid-head"><span class="au-grid-icon">💻</span><span class="au-grid-badge">{{ buckets['scripting'] }} 篇</span></div>
        <div class="au-grid-title">JASS / Lua 进阶</div>
        <div class="au-grid-sub">GUI 不够用了？开始写代码</div>
        <ul class="au-grid-list">
          <li>• JASS 入门：从 T 触发翻译到代码</li>
          <li>• Lua 脚本基础（重制版）</li>
          <li>• vJASS 进阶编程</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item" :href="link('/author/editor/tools/ydwe-雨滴编辑器使用指南')">
        <div class="au-grid-head"><span class="au-grid-icon">🔧</span><span class="au-grid-badge">{{ buckets['tools'] }} 篇</span></div>
        <div class="au-grid-title">第三方工具</div>
        <div class="au-grid-sub">YDWE / JNGP / MPQ / WEU / Hive</div>
        <ul class="au-grid-list">
          <li>• YDWE 雨滴编辑器使用指南</li>
          <li>• JNGP 工具包</li>
          <li>• MPQ 文件工具与资源导入</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>
    </div>

    <!-- 编辑器场景跳转 -->
    <h2 style="border-left:4px solid var(--vp-c-brand-1);padding-left:.75rem;margin-top:2.5rem">🔎 编辑器场景跳转</h2>
    <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:0 0 1rem">直奔主题，按场景跳到对应文章。</p>
    <div class="au-tags">
      <a class="au-tag" :href="link('/author/editor/demos/hero-system')">英雄选择面板</a>
      <a class="au-tag" :href="link('/author/editor/demos/item-inventory')">背包多页</a>
      <a class="au-tag" :href="link('/author/editor/demos/combat-system')">伤害计算</a>
      <a class="au-tag" :href="link('/author/editor/demos/skill-impl')">弹道技能</a>
      <a class="au-tag" :href="link('/author/editor/systems/设计第一个bossai技能和挑战性')">Boss AI</a>
      <a class="au-tag" :href="link('/author/editor/demos/save-data')">存档加密</a>
      <a class="au-tag" :href="link('/author/editor/demos/ui-interface')">对话框</a>
      <a class="au-tag" :href="link('/author/editor/demos/ui-interface')">血条</a>
      <a class="au-tag" :href="link('/author/editor/demos/combat-system')">仇恨系统</a>
      <a class="au-tag" :href="link('/author/editor/advanced/多人游戏同步机制')">多人同步</a>
      <a class="au-tag" :href="link('/author/editor/triggers/触发器内存泄漏处理')">内存泄漏</a>
      <a class="au-tag" :href="link('/author/editor/triggers/触发器不生效怎么办新手调试排错指南')">触发器调试</a>
      <a class="au-tag" :href="link('/terrain/地形纹理与贴图技巧')">地形纹理</a>
      <a class="au-tag" :href="link('/terrain/区域region的用法配合触发器实现进入事件')">区域触发</a>
    </div>

    <!-- 上下页 -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--vp-c-divider)">
      <a :href="link('/author/')" class="au-grid-item" style="padding:1rem">
        <div style="font-size:.75rem;color:var(--vp-c-text-3)">← 返回</div>
        <div style="color:var(--vp-c-brand-1);font-weight:600">主页</div>
      </a>
      <a :href="link('/author/operations')" class="au-grid-item au-card-ops" style="padding:1rem;text-align:right">
        <div style="font-size:.75rem;color:var(--vp-c-text-3)">下一站 →</div>
        <div style="color:var(--vp-c-kk-2);font-weight:600">运营教学</div>
      </a>
    </div>

  </div>
</template>
