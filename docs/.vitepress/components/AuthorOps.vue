<script setup lang="ts">
// AuthorOps.vue — 运营教学落地页
import data from '../_author_data.json'
import { withBase } from 'vitepress'
const link = (p: string) => withBase(p)
const buckets = data.opsBuckets
</script>

<template>
  <div class="au-page">

    <!-- 暖橙警告 -->
    <div class="au-warn">
      <div class="au-warn-title">⚠️ 写在前面</div>
      <blockquote style="font-style:italic;border-left:2px solid var(--vp-c-kk-soft);padding-left:.75rem;margin:0 0 .5rem">
        「做出来的地图质量不错，但没人知道、也没人付费。」
      </blockquote>
      <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:0">
        这是 KK 平台最常见的<strong>新作者陷阱</strong>。运营和开发同样重要。建议每天花 15 分钟看运营资料，<strong>比你多调一个触发器更能让地图活下来</strong>。
      </p>
    </div>

    <!-- 你处在哪一步 -->
    <div class="au-info">
      <div class="au-info-title">ℹ️ 你处在哪一步？</div>
      <div style="display:flex;flex-direction:column;gap:.5rem;font-size:.875rem">
        <div>
          <strong>▸ 还没立项 / 不知道做什么类型的图</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">看「KK 月度地图发行观察」，知道平台现在扶持什么。</span>
          <a href="#monthly-watch" style="color:var(--vp-c-kk-2)">→ 跳过去</a>
        </div>
        <div>
          <strong>▸ 地图做得差不多了，准备发布</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">走「上线发布与发行」+「测试与运营」。</span>
          <a href="#launch" style="color:var(--vp-c-kk-2)">→ 跳过去</a>
        </div>
        <div>
          <strong>▸ 地图已上线，要做大</strong><br/>
          <span style="color:var(--vp-c-text-2);margin-left:1rem">走「平台工具配置」+「商业化与增长」。</span>
          <a href="#monetize" style="color:var(--vp-c-kk-2)">→ 跳过去</a>
        </div>
      </div>
    </div>

    <!-- 运营路径 -->
    <h2 style="border-left:4px solid var(--vp-c-kk-1);padding-left:.75rem;margin-top:2.5rem">⭐ 运营路径</h2>
    <div class="au-path">
      <div class="au-path-grid au-path-5">
        <div class="au-path-step">
          <div class="au-path-circle" style="background:var(--vp-c-kk-soft);color:var(--vp-c-kk-3)">📚</div>
          <div class="au-path-name">看大方向</div>
          <div class="au-path-meta">入门生态 {{ buckets['publishing'] }}</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:#fed7aa;color:#9a3412">🚢</div>
          <div class="au-path-name">上线发布</div>
          <div class="au-path-meta">{{ buckets['publishing'] }} 篇</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:#fdba74;color:#7c2d12">⚙️</div>
          <div class="au-path-name">配置工具</div>
          <div class="au-path-meta">平台工具 {{ buckets['platform'] }}</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:var(--vp-c-kk-1);color:#fff">🧪</div>
          <div class="au-path-name">测试运营</div>
          <div class="au-path-meta">{{ buckets['launch'] }} 篇</div>
        </div>
        <div class="au-path-step">
          <div class="au-path-circle" style="background:var(--vp-c-kk-3);color:#fff">💰</div>
          <div class="au-path-name">商业化</div>
          <div class="au-path-meta">{{ buckets['publishing'] + buckets['launch'] }} 篇</div>
        </div>
      </div>
    </div>

    <!-- 5 子主题宫格 -->
    <h2 style="border-left:4px solid var(--vp-c-kk-1);padding-left:.75rem;margin-top:2.5rem">📚 子主题</h2>
    <div class="au-grid">

      <!-- 入门 KK 生态 ⭐ -->
      <a class="au-grid-item au-emph-orange au-card-ops" :href="link('/author/ops/publishing/kk平台快速帮助运营与发行资料总览')">
        <span class="au-star-corner">⭐ 新作者必读</span>
        <div class="au-grid-head">
          <span class="au-grid-icon">📚</span>
          <span class="au-grid-badge au-orange">{{ buckets['publishing'] }} 篇</span>
        </div>
        <div class="au-grid-title" style="color:var(--vp-c-kk-3);font-size:1.25rem">入门 KK 生态</div>
        <div style="font-size:.875rem;color:var(--vp-c-kk-2);margin-bottom:.75rem">审核标准 / 月度发行观察 / 全年课程回顾。这是 KK 平台运营资料的总入口。</div>
        <ul class="au-grid-list" style="display:grid;grid-template-columns:1fr 1fr;gap:.25rem">
          <li>• KK 平台快速帮助：运营资料总览</li>
          <li>• KK 平台地图发行观察</li>
          <li>• 2025 全年课程回顾与新手学习路线</li>
          <li>• KK 平台地图审核标准与上架要求</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a id="launch" class="au-grid-item au-card-ops" :href="link('/author/ops/publishing/如何把地图发布到kk平台完整上传步骤')">
        <div class="au-grid-head"><span class="au-grid-icon">🚢</span><span class="au-grid-badge">{{ buckets['publishing'] }} 篇</span></div>
        <div class="au-grid-title">上线发布与发行</div>
        <div class="au-grid-sub">从 .w3x 文件到玩家可玩</div>
        <ul class="au-grid-list">
          <li>• 如何把地图发布到 KK 平台</li>
          <li>• 地图加密保护：防止作品被盗用</li>
          <li>• 地图性能优化：解决卡顿掉帧</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item au-card-ops" :href="link('/author/ops/platform/开发者后台基础配置地图信息与版本管理')">
        <div class="au-grid-head"><span class="au-grid-icon">⚙️</span><span class="au-grid-badge">{{ buckets['platform'] }} 篇</span></div>
        <div class="au-grid-title">平台工具配置</div>
        <div class="au-grid-sub">开发者后台 8 个核心模块</div>
        <ul class="au-grid-list">
          <li>• 宝箱 · 礼包码 · 签到 · 任务</li>
          <li>• 数据分析仪表盘</li>
          <li>• 玩家管理：黑名单 / 封号</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a class="au-grid-item au-card-ops" :href="link('/author/ops/launch/测试阶段完整指南内测招募与数据收集')">
        <div class="au-grid-head"><span class="au-grid-icon">🧪</span><span class="au-grid-badge">{{ buckets['launch'] }} 篇</span></div>
        <div class="au-grid-title">测试与运营</div>
        <div class="au-grid-sub">内测招募 + 上线前 checklist</div>
        <ul class="au-grid-list">
          <li>• 测试阶段完整指南：内测招募与数据收集</li>
          <li>• 上线前运营 checklist：预热预告社区建设</li>
          <li>• 上线后运营指南：数据/版本/活动</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>

      <a id="monetize" class="au-grid-item au-card-ops" :href="link('/author/ops/launch/地图商业化入门氪金点设计与付费率优化')">
        <div class="au-grid-head"><span class="au-grid-icon">💰</span><span class="au-grid-badge">{{ buckets['publishing'] + buckets['launch'] }} 篇</span></div>
        <div class="au-grid-title">商业化与增长</div>
        <div class="au-grid-sub">氪金点 / 增长策略 / 付费洞察</div>
        <ul class="au-grid-list">
          <li>• 地图商业化入门：氪金点设计</li>
          <li>• 地图增长策略：自然流量与付费推广</li>
          <li>• KK 用户付费行为洞察</li>
          <li>• 上线后运营指南：数据/版本/活动</li>
        </ul>
        <div class="au-grid-cta">进入 →</div>
      </a>
    </div>

    <!-- KK 月度发行观察 专栏 -->
    <h2 id="monthly-watch" style="border-left:4px solid var(--vp-c-kk-1);padding-left:.75rem;margin-top:3rem">📅 KK 月度地图发行观察 · 完整存档</h2>
    <div class="au-watch-card">
      <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:0 0 1rem">
        每月哪些图火了、为什么火？KK 运营官方课件整理。<strong>新作者立项前先扫一遍最近 3 期</strong>，知道现在什么品类在涨。
      </p>
      <div style="margin-bottom:1rem">
        <div style="font-size:.75rem;font-weight:600;color:var(--vp-c-kk-3);margin-bottom:.5rem">📌 最重要</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem">
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台课程回顾2025全年运营课程要点与新手学习路线')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">2025 全年运营课程回顾</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">年度总览 · 新手学习路线</div>
          </a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台快速帮助运营与发行资料总览')" style="padding:.75rem">
            <div style="font-weight:600;font-size:.875rem">2026 地图发行重点事件</div>
            <div style="font-size:.75rem;color:var(--vp-c-text-3);margin-top:.25rem">平台扶持方向 · 立项前必读</div>
          </a>
        </div>
      </div>
      <div>
        <div style="font-size:.75rem;font-weight:600;color:var(--vp-c-kk-3);margin-bottom:.5rem">📅 月度观察</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem">
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台地图发行观察你该关注哪些指标与节奏')" style="padding:.625rem;font-size:.875rem">3 月发行观察</a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台地图发行观察你该关注哪些指标与节奏')" style="padding:.625rem;font-size:.875rem">6 月发行观察</a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台地图发行观察你该关注哪些指标与节奏')" style="padding:.625rem;font-size:.875rem">8-9 月发行观察</a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台地图发行观察你该关注哪些指标与节奏')" style="padding:.625rem;font-size:.875rem">10 月发行观察</a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台地图发行观察你该关注哪些指标与节奏')" style="padding:.625rem;font-size:.875rem">11 月发行观察</a>
          <a class="au-grid-item" :href="link('/author/ops/publishing/kk平台课程回顾2025全年运营课程要点与新手学习路线')" style="padding:.625rem;font-size:.875rem">12 月运营课件</a>
        </div>
      </div>
    </div>

    <!-- KK 官方资源直达 -->
    <h2 style="border-left:4px solid var(--vp-c-kk-1);padding-left:.75rem;margin-top:3rem">🌐 KK 官方资源直达</h2>
    <p style="font-size:.875rem;color:var(--vp-c-text-2);margin:0 0 1rem">KK 后台 / 启航手册 / 审核手册等高频外链，集中放在这里。</p>
    <div style="background:var(--vp-c-bg);border:1px solid var(--vp-c-divider);border-radius:.75rem;overflow:hidden">
      <table style="width:100%;font-size:.875rem;border-collapse:collapse">
        <tbody>
          <tr style="border-bottom:1px solid var(--vp-c-divider)"><td style="padding:.75rem 1rem;font-weight:600;width:11rem">KK 官网</td><td style="padding:.75rem 1rem"><a href="http://www.kkdzpt.com" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">www.kkdzpt.com ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">玩家入口 / 公司信息</td></tr>
          <tr style="border-bottom:1px solid var(--vp-c-divider)"><td style="padding:.75rem 1rem;font-weight:600">开发者后台</td><td style="padding:.75rem 1rem"><a href="https://create.kkdzpt.com" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">create.kkdzpt.com ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">作者后台 / 上传地图</td></tr>
          <tr style="border-bottom:1px solid var(--vp-c-divider)"><td style="padding:.75rem 1rem;font-weight:600">启航手册</td><td style="padding:.75rem 1rem"><a href="https://create.kkdzpt.com/help/service_support/启航手册" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">/help/.../启航手册 ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">官方新作者入门</td></tr>
          <tr style="border-bottom:1px solid var(--vp-c-divider)"><td style="padding:.75rem 1rem;font-weight:600">地图与商品审核手册</td><td style="padding:.75rem 1rem"><a href="https://create.kkdzpt.com/help/service_support/地图与商品审核手册" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">/help/.../审核手册 ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">上架前必读</td></tr>
          <tr style="border-bottom:1px solid var(--vp-c-divider)"><td style="padding:.75rem 1rem;font-weight:600">KK API 文档</td><td style="padding:.75rem 1rem"><a href="https://create.kkdzpt.com/kkapidoc/" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">/kkapidoc/ ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">触发器 API 参考</td></tr>
          <tr><td style="padding:.75rem 1rem;font-weight:600">作者信息登记表</td><td style="padding:.75rem 1rem"><a href="https://reckfeng.feishu.cn/share/base/form/shrcnzspsykbtSVmCsiBVvKPaHg" target="_blank" rel="noreferrer" style="color:var(--vp-c-kk-2)">reckfeng.feishu.cn/.../作者登记 ↗</a></td><td style="padding:.75rem 1rem;font-size:.75rem;color:var(--vp-c-text-3)">新作者必填</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 常见运营误区 -->
    <h2 style="border-left:4px solid #ef4444;padding-left:.75rem;margin-top:3rem">⚠️ 新作者最常踩的运营坑</h2>
    <div class="au-danger">
      <ol style="display:flex;flex-direction:column;gap:.625rem;font-size:.875rem;color:var(--vp-c-text-1);margin:0;padding-left:1.25rem">
        <li>只顾触发器，不看运营资料 <span style="color:var(--vp-c-text-3)">→</span> <a :href="link('/author/ops/publishing/kk平台快速帮助运营与发行资料总览')" style="color:var(--vp-c-kk-2)">立刻看「入门 KK 生态」</a></li>
        <li>地图做完才想封面、地图名 <span style="color:var(--vp-c-text-3)">→</span> <span style="color:var(--vp-c-text-2)">立项时就要定（亮色封面 + 热门关键词）</span></li>
        <li>上线就走人，不参与官方活动 <span style="color:var(--vp-c-text-3)">→</span> <span style="color:var(--vp-c-text-2)">首日就能申请活动，首周表现关键</span></li>
        <li>数据后台从来不看 <span style="color:var(--vp-c-text-3)">→</span> <a :href="link('/author/ops/platform/数据分析仪表盘使用指南')" style="color:var(--vp-c-kk-2)">跟着「数据分析仪表盘」配仪表</a></li>
        <li>氪金点全堆在前期 <span style="color:var(--vp-c-text-3)">→</span> <a :href="link('/author/ops/publishing/kk用户付费行为洞察新手作者如何定价与做转化')" style="color:var(--vp-c-kk-2)">看「付费行为洞察」分阶段做</a></li>
      </ol>
    </div>

    <!-- 运营场景跳转 -->
    <h2 style="border-left:4px solid var(--vp-c-kk-1);padding-left:.75rem;margin-top:3rem">🔎 运营场景跳转</h2>
    <div class="au-tags">
      <a class="au-tag au-tag-ops" :href="link('/author/ops/publishing/如何把地图发布到kk平台完整上传步骤')">发到 KK</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/launch/kk-平台地图审核标准与上架要求')">拿审核通过</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/launch/地图商业化入门氪金点设计与付费率优化')">设计氪金点</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/宝箱系统配置全流程')">配宝箱</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/礼包码系统创建与发放')">发礼包码</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/签到系统配置每日奖励设置')">配签到</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/活动工具节日活动与限时配置')">配活动</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/launch/地图增长策略自然流量与付费推广')">搞拼团</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/launch/地图增长策略自然流量与付费推广')">开地图会员</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/publishing/如何把地图发布到kk平台完整上传步骤')">写吸量地图名</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/publishing/如何把地图发布到kk平台完整上传步骤')">做亮色封面</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/数据分析仪表盘使用指南')">看付费数据</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/玩家管理工具黑名单禁言封号')">处理黑名单</a>
      <a class="au-tag au-tag-ops" :href="link('/author/ops/platform/玩家管理工具黑名单禁言封号')">封号申诉</a>
    </div>

    <!-- 上下页 -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--vp-c-divider)">
      <a :href="link('/author/editor')" class="au-grid-item" style="padding:1rem">
        <div style="font-size:.75rem;color:var(--vp-c-text-3)">← 上一站</div>
        <div style="color:var(--vp-c-brand-1);font-weight:600">编辑器教学</div>
      </a>
      <div class="au-grid-item" style="padding:1rem;text-align:right">
        <div style="font-size:.75rem;color:var(--vp-c-text-3)">🏠</div>
        <a :href="link('/author/')" style="color:var(--vp-c-brand-1);font-weight:600">返回作者中心首页</a>
      </div>
    </div>

  </div>
</template>
