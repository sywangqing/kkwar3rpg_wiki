---
title: 神墓 2.7C — 🎒 05 物品系统
category: kk-triggers
slug: shenmu/05-items
description: 物品合成/使用/丢弃/出售
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 🎒 05 物品系统

> 物品合成/使用/丢弃/出售

**共 4 个触发器**

## 📑 触发器目录

- [ItemSynthesis](#trigger-05_000_ItemSynthesis)
- [ItemUseable](#trigger-05_001_ItemUseable)
- [ItemUseableTarget](#trigger-05_002_ItemUseableTarget)
- [ItemDrop](#trigger-05_003_ItemDrop)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-05_000_ItemSynthesis">
<summary><strong>📌 ItemSynthesis</strong> <code>05_000_ItemSynthesis</code></summary>

```text
触发器: ItemSynthesis (物品系统) [✓] — 基地升级迷幻之刃
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-05_001_ItemUseable">
<summary><strong>📌 ItemUseable</strong> <code>05_001_ItemUseable</code></summary>

```text
触发器: ItemUseable (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-05_002_ItemUseableTarget">
<summary><strong>📌 ItemUseableTarget</strong> <code>05_002_ItemUseableTarget</code></summary>

```text
触发器: ItemUseableTarget (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, AIwb)
  │    │    ├─ 技能目标单位() == gg_unit_n001_0166
  │    │    ├─ iStepHaoYue == 4
  │    ├─ 则
  │    │    设置 iStepHaoYue = 5
  │    │    设置 pTemp = (gg_unit_n001_0166的位置)
  │    │    销毁特效 创建特效(war3mapImported\chronospher_fx_mediumq.mdx, pTemp)
  │    │    移除 gg_unit_n001_0166
  │    │    隐藏单位: gg_unit_h003_0002
  │    │    销毁触发器(自身)
  │    │    清除点 pTemp
  │    │    显示文本→grpOnline: "TRIGSTR_1123"
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02M)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01D)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01N)
  │    │    UnitAddItemByIdSwapped: I01A, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02N)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01A)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01O)
  │    │    UnitAddItemByIdSwapped: I01B, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02O)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01B)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01P)
  │    │    UnitAddItemByIdSwapped: I01C, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02L)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01C)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01Q)
  │    │    UnitAddItemByIdSwapped: I019, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02P)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01I)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01R)
  │    │    UnitAddItemByIdSwapped: I01J, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02Q)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01J)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01S)
  │    │    UnitAddItemByIdSwapped: I01K, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02R)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01K)
  │    │    ├─ 物品有归属(技能目标物品()) == TRUE
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01U)
  │    │    UnitAddItemByIdSwapped: I01L, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02S)
       │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01L)
       │    ├─ 物品有归属(技能目标物品()) == TRUE
       ├─ 则
       │    删除物品: 技能目标物品()
       │    删除物品: 单位携带物品(按类型)(触发单位(), I01T)
       │    UnitAddItemByIdSwapped: I01M, 触发单位()
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-05_003_ItemDrop">
<summary><strong>📌 ItemDrop</strong> <code>05_003_ItemDrop</code></summary>

```text
触发器: ItemDrop (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroDropItem
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, dsum)
  │    ├─ 则
  │    │    SetItemUserData: 被操作物品(), 0
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, rde1)
  │    ├─ 则
  │    │    删除物品: 被操作物品()
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位持有物品类型(触发单位(), rde1) == TRUE
  │    │      │    ├─ 单位技能等级(Agyb, 触发单位()) == 0
  │    │      ├─ 则
  │    │      │    SetHeroLevel: 触发单位(), 1, ShowHideShow
  │    │      │    杀死 触发单位()
  │    │      └─ 否则: (无)
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I04N)
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位类型判断(触发单位(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    删除物品: 被操作物品()
  │    │      │    返回
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I05D)
       ├─ 则
       │    如果
       │      ├─ 条件: 单位类型判断(触发单位(), 英雄) == TRUE
       │      ├─ 则
       │      │    删除物品: 被操作物品()
       │      │    返回
       │      └─ 否则: (无)
       └─ 否则: (无)
```

</details>

