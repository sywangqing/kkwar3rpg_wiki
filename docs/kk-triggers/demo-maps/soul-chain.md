---
title: 灵魂锁链 - 演示图实战
category: kk-triggers
slug: demo-maps/soul-chain
description: 演示图 灵魂锁链 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 灵魂锁链 — 演示图实战

> 演示图：[黑科技]灵魂锁链 伤害变魔法.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\[黑科技]灵魂锁链 伤害变魔法.w3x`

## 📑 触发器目录

- 简介
- 未命名触发器 001
- 未命名触发器 002

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ ── 欢迎使用世界编辑器，开始你的地图创造之旅。 ──
  ├─ ── 你可以从https://reckfeng.com/获取最新编辑器咨询。 ──
  ├─ ── 当你的地图意外损坏时，你可以在backups目录找到你最近26次保存的地图。 ──
  ├─ ── 任何疑问请加官方作者群：QQ433807374。 ──
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  └─ 迷雾遮罩开关: EnabledDisabledDisabled
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 伤害值() OperatorGreater 0.00
动作
  ├─ 如果
  │    ├─ 条件: YDWEIsEventPhysicalDamage() == TRUE
  │    ├─ 则
  │    │    BJDebugMsg: "TRIGSTR_003"
  │    └─ 否则
  │         BJDebugMsg: "TRIGSTR_004"
  ├─ 设置局部变量:"n"=触发单位()
  └─ 启动计时器: 创建计时器(), 0.00s (一次性)
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  └─ 单位发布命令(目标): gg_unit_hfoo_0004, UnitOrderSpiritLink, gg_unit_hpea_0001
```

