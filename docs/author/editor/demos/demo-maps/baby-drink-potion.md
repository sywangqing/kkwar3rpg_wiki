---
title: 宝宝吃药 - 演示图实战
category: kk-triggers
slug: demo-maps/baby-drink-potion
description: 演示图 宝宝吃药 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 宝宝吃药 — 演示图实战

> 演示图：宝宝吃药吃书＋物品叠加 纯T.w3x
>
> 触发器数：**8**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\宝宝吃药吃书＋物品叠加 纯T.w3x`

## 📑 触发器目录

- 对战初始化
- Text
- Press ESC
- ITEM GET
- drug
- book str
- book agi
- book int

---

## 📜 触发器代码

### 对战初始化

```text
触发器: 对战初始化 (初始化) [✓] — 默认的对所有玩家的对战游戏初始化 
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ MeleeStartingVisibility
  └─ SetUnitLifeBJ: gg_unit_ewsp_0001, 1.00
```

### Text

```text
触发器: Text (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_013"
  └─ DisplayTimedTextToForce: GetPlayersAll(), 999999.00, "TRIGSTR_020"
```

### Press ESC

```text
触发器: Press ESC (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  └─ SetUnitLifeBJ: gg_unit_Ewar_0002, 1.00
```

### ITEM GET

```text
触发器: ITEM GET (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I000)
动作
  └─ 循环整数A 1→6
       └─ 如果
            ├─ 条件: 全部成立
            │    ├─ 物品类型比较(物品类型ID(单位栏位物品(触发单位(), 循环整数A())), OperatorEqualENE, 物品类型ID(被操作物品()))
            │    ├─ 物品比较(单位栏位物品(触发单位(), 循环整数A()), OperatorNotEqualENE, 被操作物品())
            ├─ 则
            │    SetItemCharges: 单位栏位物品(触发单位(), 循环整数A()), (物品剩余使用次数(单位栏位物品(触发单位(), 循环整数A())) + 物品剩余使用次数(被操作物品()))
            │    删除物品: 被操作物品()
            └─ 否则: (无)
```

### drug

```text
触发器: drug (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroUseItem
条件
  ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I000)
  └─ (触发单位()类型ID) == ewsp
动作
  ├─ SetUnitLifeBJ: 触发单位(), 1.00
  └─ SetUnitLifeBJ: gg_unit_Ewar_0002, (单位状态(UnitStateLife, gg_unit_Ewar_0002) + 250.00)
```

### book str

```text
触发器: book str (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I001)
动作
  └─ 修改 gg_unit_Ewar_0002 的HeroStatStr: ModifyMethodAdd1
```

### book agi

```text
触发器: book agi (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I002)
动作
  └─ 修改 gg_unit_Ewar_0002 的HeroStatAgi: ModifyMethodAdd1
```

### book int

```text
触发器: book int (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I003)
动作
  └─ 修改 gg_unit_Ewar_0002 的HeroStatInt: ModifyMethodAdd1
```

