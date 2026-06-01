---
title: 穿透机制 - 演示图实战
category: kk-triggers
slug: demo-maps/pierce-mechanism
description: 演示图 穿透机制 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 穿透机制 — 演示图实战

> 演示图：穿透机制2.0.w3x
>
> 触发器数：**5**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\穿透机制2.0.w3x`

## 📑 触发器目录

- 简介
- 未命名触发器 001
- 未命名触发器 004
- 未命名触发器 002
- 未命名触发器 003

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ DzTriggerRegisterMallItemSyncData()
条件
  ├─ DzGetTriggerMallItem() == "商品key"
  └─ DzGetTriggerMallItemPlayer() == Player00
动作
  ├─ ── 欢迎使用世界编辑器，开始你的地图创造之旅。 ──
  ├─ ── 你可以从dz.163.com获取最新编辑器咨询。 ──
  ├─ ── 当你的地图意外损坏时，你可以在backups目录找到你最近26次保存的地图。 ──
  ├─ ── 任何疑问请加官方作者群：QQ35063417。 ──
  └─ DzAPI_Map_OpenMall: Player00, "商品key"
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: YDWEIsEventDamageType(DamageTypeNormal) == TRUE
       ├─ 则
       │    如果
       │      ├─ 条件: 单位状态(触发单位(), UnitStateArmor) OperatorGreaterEq 0.00
       │      ├─ 则
       │      │    保存数据到哈希表: [单位类型.触发单位()."原始抗性"] = ((单位状态(触发单位(), UnitStateArmor) x 6.00) / (100.00 + (单位状态(触发单位(), UnitStateArmor) x 6.00)))
       │      │    保存数据到哈希表: [单位类型.触发单位()."伤害数值"] = (伤害值() / (1.00 - 从哈希表读取数据(单位类型, 触发单位(), "原始抗性")))
       │      │    保存数据到哈希表: [单位类型.触发单位()."实际抗性"] = ((RMaxBJ(0.00, ((单位状态(触发单位(), UnitStateArmor) x (1.00 - 从哈希表读取数据(单位类型, 伤害来源(), "百分比穿甲"))) - 从哈希表读取数据(单位类型, 伤害来源(), "固定穿甲"))) x 6.00) / (100.00 + (((单位状态(触发单位(), UnitStateArmor) x (1.00 - 从哈希表读取数据(单位类型, 伤害来源(), "百分比穿甲"))) - 从哈希表读取数据(单位类型, 伤害来源(), "固定穿甲")) x 6.00)))
       │      │    保存数据到哈希表: [单位类型.触发单位()."实际伤害"] = (从哈希表读取数据(单位类型, 触发单位(), "伤害数值") x (1.00 - 从哈希表读取数据(单位类型, 触发单位(), "实际抗性")))
       │      └─ 否则
       │           保存数据到哈希表: [单位类型.触发单位()."实际伤害"] = 伤害值()
       │    YDWESetEventDamage: 从哈希表读取数据(单位类型, 触发单位(), "实际伤害")
       │    CreateTextTagUnitBJ: R2SW(伤害值(), 1, 0), 触发单位(), 0, 10, 100, 100, 100, 0
       │    YDWETimerDestroyTextTag: 2, GetLastCreatedTextTag()
       │    SetTextTagVelocityBJ: GetLastCreatedTextTag(), 64, GetRandomDirectionDeg()
       └─ 否则: (无)
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: YDWEIsEventDamageType(DamageTypeNormal) == TRUE
       ├─ 则
       │    如果
       │      ├─ 条件: 单位状态(触发单位(), UnitStateArmor) OperatorGreaterEq 0.00
       │      ├─ 则
       │      │    YDWESetEventDamage: ((伤害值() / (1.00 - ((单位状态(触发单位(), UnitStateArmor) x 6.00) / (100.00 + (单位状态(触发单位(), UnitStateArmor) x 6.00))))) x (1.00 - (RMaxBJ(0.00, (((单位状态(触发单位(), UnitStateArmor) x (1.00 - 从哈希表读取数据(单位类型, 伤害来源(), "百分比穿甲"))) - 从哈希表读取数据(单位类型, 伤害来源(), "固定穿甲")) x 6.00)) / ((((单位状态(触发单位(), UnitStateArmor) x (1.00 - 从哈希表读取数据(单位类型, 伤害来源(), "百分比穿甲"))) - 从哈希表读取数据(单位类型, 伤害来源(), "固定穿甲")) x 6.00) + 100.00))))
       │      └─ 否则: (无)
       │    CreateTextTagUnitBJ: R2SW(伤害值(), 1, 0), 触发单位(), 0, 10, 100, 100, 100, 0
       │    YDWETimerDestroyTextTag: 2, GetLastCreatedTextTag()
       │    SetTextTagVelocityBJ: GetLastCreatedTextTag(), 64, GetRandomDirectionDeg()
       └─ 否则: (无)
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [typename11_itemcode.I001."固定穿甲"] = 10.00
  ├─ 保存数据到哈希表: [typename11_itemcode.I000."百分比穿甲"] = 0.50
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "1"
条件
  └─ 无
动作
  └─ 显示文本→Player00: 0
```

