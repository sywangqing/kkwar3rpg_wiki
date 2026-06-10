---
title: 冷却缩减 - 演示图实战
category: kk-triggers
slug: demo-maps/cooldown-reduction
description: 演示图 冷却缩减 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 冷却缩减 — 演示图实战

> 演示图：冷却缩减.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\冷却缩减.w3x`

## 📑 触发器目录

- 未命名触发器 001
- Item
- CD

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [typename11_itemcode.I000."冷却缩减"] = 20.00
  ├─ 保存数据到哈希表: [typename11_itemcode.I001."冷却缩减"] = 100.00
  ├─ 保存数据到哈希表: [typename11_itemcode.I002."冷却缩减"] = -100.00
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  └─ 迷雾遮罩开关: EnabledDisabledDisabled
```

### Item

```text
触发器: Item (初始化) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 任意单位 - PlayerUnitEventHeroPickUpItem
  └─ 任意单位 - PlayerUnitEventHeroDropItem
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: YDWEIsTriggerEventId(ID_EVENT_PLAYER_UNIT_PICKUP_ITEM) == TRUE
       ├─ 则
       │    保存数据到哈希表: [单位类型.触发单位()."冷却缩减"] = (从哈希表读取数据(单位类型, 触发单位(), "冷却缩减") + 从哈希表读取数据(typename11_itemcode, 物品类型ID(被操作物品()), "冷却缩减"))
       └─ 否则
            保存数据到哈希表: [单位类型.触发单位()."冷却缩减"] = (从哈希表读取数据(单位类型, 触发单位(), "冷却缩减") - 从哈希表读取数据(typename11_itemcode, 物品类型ID(被操作物品()), "冷却缩减"))
```

### CD

```text
触发器: CD (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 从哈希表读取数据(单位类型, 触发单位(), "冷却缩减") != 0.00
  └─ YDWEGetUnitAbilityDataReal(触发单位(), 施法技能ID(), 单位技能等级(触发单位(), 施法技能ID()), ABILITY_DATA_COOL) OperatorGreater 0.00
动作
  └─ 如果
       ├─ 条件: 从哈希表读取数据(单位类型, 触发单位(), "冷却缩减") OperatorGreater 0.00
       ├─ 则
       │    启动计时器: 创建计时器(), 0.01s (循环)
       └─ 否则
            启动计时器: 创建计时器(), 0.01s (循环)
```

