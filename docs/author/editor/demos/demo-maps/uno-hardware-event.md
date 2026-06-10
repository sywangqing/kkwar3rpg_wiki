---
title: uno硬件事件 - 演示图实战
category: kk-triggers
slug: demo-maps/uno-hardware-event
description: 演示图 uno硬件事件 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 uno硬件事件 — 演示图实战

> 演示图：uno硬件事件.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 1
- 2
- 3

---

## 📜 触发器代码

### 1

```text
触发器: 1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ FogEnableOff
  ├─ FogMaskEnableOff
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 12
  ├─ ── 从这里开始 ──
  ├─ DzTriggerRegisterKeyEventMultiple: GetLocalPlayer(), GameKeyAction_Press, GameKey_F2
  └─ DzTriggerRegisterKeyEventMultiple: GetLocalPlayer(), GameKeyAction_Press, GameKey_F3
```

### 2

```text
触发器: 2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ DzTriggerRegisterSyncData("F2", false)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件:              ("true/*可以加条件，例如英雄生命值>0*/")
       ├─ 则
       │    移动单位: hero[字符串转整数(DzGetTriggerSyncData())], 500.00, 500.00
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\MassTeleport\MassTeleportTarget.mdl, hero[字符串转整数(DzGetTriggerSyncData())], "origin")
       └─ 否则: (无)
```

### 3

```text
触发器: 3 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ DzTriggerRegisterSyncData("F3", false)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件:              ("true/*可以加条件，例如英雄生命值>0*/")
       ├─ 则
       │    移动单位: hero[字符串转整数(DzGetTriggerSyncData())], 2000.00, 2000.00
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\MassTeleport\MassTeleportTarget.mdl, hero[字符串转整数(DzGetTriggerSyncData())], "origin")
       └─ 否则: (无)
```

