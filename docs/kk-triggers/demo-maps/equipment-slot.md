---
title: 装备栏 - 演示图实战
category: kk-triggers
slug: demo-maps/equipment-slot
description: 演示图 装备栏 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 装备栏 — 演示图实战

> 演示图：装备栏.w3x
>
> 触发器数：**10**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\装备栏.w3x`

## 📑 触发器目录

- ZBL_Seti
- ZBL_MakeItem
- ZBL_BackItem
- 套装
- all no
- all off
- 吸血
- xixue
- 猩红狂热
- xinghongkuangre

---

## 📜 触发器代码

### ZBL_Seti

```text
触发器: ZBL_Seti (初始化) [✓] — 装备栏没图标。武器更换失败。
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ ── 武器区 ──
  ├─ 设置 ZBL_int = 0
  ├─ 设置 ZBL_ExchangeSpell[((6 x ZBL_int) + 1)] = A007
  ├─ 设置 ZBL_itemtype[((6 x ZBL_int) + 1)] = I000
  ├─ 设置 ZBL_effectsepll[((6 x ZBL_int) + 1)] = A003
  ├─ 设置 ZBL_Itemspell[((6 x ZBL_int) + 1)] = A005
  ├─ 设置 ZBL_int = (ZBL_int + 1)
  ├─ 设置 ZBL_ExchangeSpell[((6 x ZBL_int) + 1)] = A00D
  ├─ 设置 ZBL_itemtype[((6 x ZBL_int) + 1)] = I001
  ├─ 设置 ZBL_effectsepll[((6 x ZBL_int) + 1)] = A00B
  ├─ 设置 ZBL_Itemspell[((6 x ZBL_int) + 1)] = A00C
  └─ 设置 ZBL_int = (ZBL_int + 1)
```

### ZBL_MakeItem

```text
触发器: ZBL_MakeItem (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroUseItem
条件
  └─ 无
动作
  ├─ 设置 ZBL_unit = 触发单位()
  ├─ 设置 ZBL_Doitemtype = 物品类型ID(被操作物品())
  ├─ 删除物品: 被操作物品()
  ├─ ForLoopVarMultiple: ZBL_Temp_1, 1, 6
  └─ ForLoopVarMultiple: ZBL_Temp_1, 1, 999
```

### ZBL_BackItem

```text
触发器: ZBL_BackItem (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  ├─ 设置 ZBL_unit = 触发单位()
  └─ ForLoopVarMultiple: ZBL_Temp_1, 1, 999
```

### 套装

```text
触发器: 套装 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### all no

```text
触发器: all no (初始化) [✗]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroUseItem
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ OperatorIntegerAdd(单位技能等级(A003, 触发单位()), 单位技能等级(A00D, 触发单位())) == 2
       │    ├─ 单位技能等级(A01K, 触发单位()) == 0
       ├─ 则
       │    UnitAddAbilityBJ: ?, 触发单位()
       └─ 否则: (无)
```

### all off

```text
触发器: all off (初始化) [✗]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  ├─ 等待 0.00s
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ OperatorIntegerAdd(单位技能等级(A003, 触发单位()), 单位技能等级(A00D, 触发单位())) != 2
       │    ├─ 单位技能等级(A01K, 触发单位()) == 1
       ├─ 则
       │    UnitRemoveAbilityBJ: ?, 触发单位()
       └─ 否则: (无)
```

### 吸血

```text
触发器: 吸血 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### xixue

```text
触发器: xixue (玩家/英雄) [✗]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位技能等级(A01H, 伤害来源()) == 1
  ├─ 单位存活判断(触发单位()) == TRUE
  └─ 单位存活判断(伤害来源()) == TRUE
动作
  └─ SetUnitLifeBJ: 伤害来源(), (单位状态(UnitStateLife, 伤害来源()) + 伤害值())
```

### 猩红狂热

```text
触发器: 猩红狂热 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### xinghongkuangre

```text
触发器: xinghongkuangre (玩家/英雄) [✗]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ 单位技能等级(A01H, 凶手单位()) == 1
  └─ 单位存活判断(凶手单位()) == TRUE
动作
  └─ SetUnitLifeBJ: 凶手单位(), (单位状态(UnitStateLife, 凶手单位()) + (0.20 x 单位状态(UnitStateMaxLife, 凶手单位())))
```

