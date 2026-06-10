---
title: 异步特效 - 演示图实战
category: kk-triggers
slug: demo-maps/async-effect
description: 演示图 异步特效 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 异步特效 — 演示图实战

> 演示图：异步特效显示开关.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\异步特效显示开关.w3x`

## 📑 触发器目录

- 初始化
- esc开关
- 咆哮

---

## 📜 触发器代码

### 初始化

```text
触发器: 初始化 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ ── 将实际 玩家1-6 添加到玩家组 ──
  └─ YDWEForLoopLocVarMultiple: "xh", 1, 6
```

### esc开关

```text
触发器: esc开关 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(PlayerALL)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 玩家在玩家组中(触发玩家(), TXplayers) == TRUE
       ├─ 则
       │    ForceRemovePlayerSimple: 触发玩家(), TXplayers
       │    DisplayTimedTextToPlayer: 触发玩家(), 0, 0, 2.00, "TRIGSTR_008"
       └─ 否则
            ForceAddPlayerSimple: 触发玩家(), TXplayers
            DisplayTimedTextToPlayer: 触发玩家(), 0, 0, 2.00, "TRIGSTR_009"
```

### 咆哮

```text
触发器: 咆哮 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
       ├─ 则
       │    ── 异步字符串（模型）显示 ──
       │    如果
       │      ├─ 条件: 玩家在玩家组中(GetLocalPlayer(), TXplayers) == TRUE
       │      ├─ 则
       │      │    设置局部变量:"tx"="Abilities\Spells\NightElf\BattleRoar\RoarCaster.mdl"
       │      └─ 否则
       │           设置局部变量:"tx"=""
       │    YDWETimerDestroyEffect: 2, 创建特效(附着单位)(读取局部变量("tx"), 触发单位(), "origin")
       └─ 否则: (无)
```

