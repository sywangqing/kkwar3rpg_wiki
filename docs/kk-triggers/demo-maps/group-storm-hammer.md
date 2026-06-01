---
title: 群体暴风之锤 - 演示图实战
category: kk-triggers
slug: demo-maps/group-storm-hammer
description: 演示图 群体暴风之锤 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 群体暴风之锤 — 演示图实战

> 演示图：群体暴风之锤 OK.w3x
>
> 触发器数：**4**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\群体暴风之锤 OK.w3x`

## 📑 触发器目录

- 简介
- 初始化
- 群体风暴
- 群体缠绕01

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ── YDWE是《魔兽争霸III》地图编辑器的一个增强Mod。 ──
  ├─ ── 　　你可以从www.ydwe.net获取最新的YDWE。 ──
  ├─ ── 　　你可以由YDWE附带的演示地图开始，快速了解YDWE的功能。 ──
  ├─ ── 　　当你的地图意外损坏时，你可以在backups目录找到你最近26次保存的地图。 ──
  └─ ── 　　当你的YDWE不能正常工作时，你可以前往www.ydwe.net联系我们。 ──
```

### 初始化

```text
触发器: 初始化 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ FogEnableOff
  └─ FogMaskEnableOff
```

### 群体风暴

```text
触发器: 群体风暴 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  └─ 单位组: 选取 范围内符合条件的单位(500.00, 技能目标点(), 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true)) 中所有单位
       ├─ 创建 1个|e001|→(触发单位()的所有者) 在 (选取单位()的位置) 面向默认朝向
       ├─ 添加技能: bj_lastCreatedUnit, A002
       ├─ 隐藏单位: bj_lastCreatedUnit
       ├─ YDWETimerRemoveUnit: 2, bj_lastCreatedUnit
       └─ 单位发布命令(目标): bj_lastCreatedUnit, UnitOrderThunderBolt, 选取单位()
```

### 群体缠绕01

```text
触发器: 群体缠绕01 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A003)
动作
  └─ 单位组: 选取 范围内符合条件的单位(500.00, 技能目标点(), 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true)) 中所有单位
       ├─ 创建 1个|e000|→(触发单位()的所有者) 在 (选取单位()的位置) 面向默认朝向
       ├─ 添加技能: bj_lastCreatedUnit, A001
       ├─ 隐藏单位: bj_lastCreatedUnit
       ├─ YDWETimerRemoveUnit: 2, bj_lastCreatedUnit
       └─ 单位发布命令(目标): bj_lastCreatedUnit, UnitOrderEntanglingRoots, 选取单位()
```

