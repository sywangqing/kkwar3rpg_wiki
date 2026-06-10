---
title: 翻页商店 - 演示图实战
category: kk-triggers
slug: demo-maps/page-store
description: 演示图 翻页商店 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 翻页商店 — 演示图实战

> 演示图：翻页商店演示图.w3x
>
> 触发器数：**4**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\翻页商店演示图.w3x`

## 📑 触发器目录

- readme
- 可记录展示页面商店
- 不影响队友浏览页面的商店
- 宠物商店

---

## 📜 触发器代码

### readme

```text
触发器: readme (初始化) [✓] — 这张演示图将展示3种不同的可翻页商店，3种商店制作方法各有利弊，请酌情采纳使用。

——by. 萌萌的立华奏.
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ ── 创建宝宝的时候设置好自定义值，如果自定义值有其他用处也可以设置单位的其他绑定值，该值将用于后续判断 ──
  ├─ 设置单位自定义值: gg_unit_h000_0005, 1
  ├─ ── 禁用魔法书内的技能，因为魔法书内的技能触发器无法修改 ──
  ├─ SetPlayerAbilityAvailable: Player00, A002, EnableDisableDisable
  ├─ ── 地图初始化时定义全局变量用于记录当前商店和商店类型，或者在玩家建造完成商店时记录 ──
  ├─ 设置 shop = (gg_unit_n000_0002类型ID)
  └─ 设置 shopnow = gg_unit_n000_0002
```

### 可记录展示页面商店

```text
触发器: 可记录展示页面商店 (初始化) [✓] — 这个商店虽然可以切换并记录商店页面，但是队友也会受其影响且无法记录商品购买间隔时间，如果不介意出现此类情况可以选择此方案。

——by. 萌萌的立华奏.
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I000)
动作
  ├─ ── 变量记录商店位置，用于后续创建单位 ──
  ├─ 设置局部变量:"shopd"=(shopnow的位置)
  ├─ 设置局部变量:"shop1"=n000
  ├─ 设置局部变量:"shop2"=n001
  ├─ 如果
  │    ├─ 条件: shop == 读取局部变量("shop1")
  │    ├─ 则
  │    │    移除 shopnow
  │    │    创建 1个|读取局部变量("shop2")|→非玩家 在 读取局部变量("shopd") 面向默认朝向
  │    │    设置局部变量:"shopnow"=bj_lastCreatedUnit
  │    │    ── 变量记录新的商店和商店单位类型 ──
  │    │    设置 shopnow = 读取局部变量("shopnow")
  │    │    设置 shop = (读取局部变量("shopnow")类型ID)
  │    │    ClearSelectionForPlayer: (GetManipulatingUnit()的所有者)
  │    │    为 (GetManipulatingUnit()的所有者) 选择 读取局部变量("shopnow")
  │    │    ── 不要忘记排泄 ──
  │    │    清除点 读取局部变量("shopd")
  │    │    ── 跳过剩余动作，否则触发器会按照触发器写入顺序触发，直到最后 ──
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: shop == 读取局部变量("shop2")
       ├─ 则
       │    移除 shopnow
       │    移除 单位组第一个单位(读取局部变量("shop"))
       │    创建 1个|读取局部变量("shop1")|→非玩家 在 读取局部变量("shopd") 面向默认朝向
       │    设置局部变量:"shopnow"=bj_lastCreatedUnit
       │    设置 shopnow = 读取局部变量("shopnow")
       │    设置 shop = (读取局部变量("shopnow")类型ID)
       │    为 (GetManipulatingUnit()的所有者) 选择 读取局部变量("shopnow")
       │    清除点 读取局部变量("shopd")
       │    返回
       └─ 否则: (无)
```

### 不影响队友浏览页面的商店

```text
触发器: 不影响队友浏览页面的商店 (初始化) [✓] — 这个商店虽然可以切换页面且不影响其他玩家浏览且能记录购买时间间隔，但是玩家可以通过重复框选的方式切换商店，如果不介意此类问题，可以采用此方案。

——by. 萌萌的立华奏.
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I001)
  │    ├─ 则
  │    │    为 (GetManipulatingUnit()的所有者) 选择 gg_unit_n002_0003
  │    │    开启触发器 当前触发器()
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I002)
       ├─ 则
       │    为 (GetManipulatingUnit()的所有者) 选择 gg_unit_n004_0004
       │    开启触发器 当前触发器()
       └─ 否则: (无)
```

### 宠物商店

```text
触发器: 宠物商店 (初始化) [✓] — 这个商店可以实现随身购买，可以记录购买时间间隔也不会对其他玩家造成影响，但是不能在中立建筑上使用这种方法，如果不介意此类问题可以采用该方案。

——by. 萌萌的立华奏.
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A003)
动作
  ├─ ── 该方案并没有设置购买物品的触发帮助实现购买物品，如果采用本方案请仔细检查技能和购买物品的绑定使用，为了防止同种技能串用，请务必绑定单位自定义值等绑定值使用！ ──
  ├─ 如果
  │    ├─ 条件: 单位自定义值(GetSpellAbilityUnit()) == 1
  │    ├─ 则
  │    │    设置单位自定义值: GetSpellAbilityUnit(), 2
  │    │    SetPlayerAbilityAvailable: Player00, A001, EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: Player00, A002, EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 单位自定义值(GetSpellAbilityUnit()) == 2
       ├─ 则
       │    设置单位自定义值: GetSpellAbilityUnit(), 1
       │    SetPlayerAbilityAvailable: Player00, A002, EnableDisableDisable
       │    SetPlayerAbilityAvailable: Player00, A001, EnableDisableEnable
       │    返回
       └─ 否则: (无)
```

