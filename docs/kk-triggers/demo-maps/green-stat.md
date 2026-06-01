---
title: 绿字属性 - 演示图实战
category: kk-triggers
slug: demo-maps/green-stat
description: 演示图 绿字属性 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 绿字属性 — 演示图实战

> 演示图：绿字属性加成的物品.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\绿字属性加成的物品.w3x`

## 📑 触发器目录

- 简介
- 获得物品HD
- 丢弃物品DQ

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓] — 初始化物品类型属性
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [typename11_itemcode.ratf."攻击力"] = 15.00
  ├─ 保存数据到哈希表: [typename11_itemcode.rde4."护甲"] = 5.00
  ├─ 保存数据到哈希表: [typename11_itemcode.ckng."力量"] = 5
  ├─ 保存数据到哈希表: [typename11_itemcode.ckng."敏捷"] = 5
  ├─ 保存数据到哈希表: [typename11_itemcode.ckng."智力"] = 5
  ├─ 保存数据到哈希表: [typename11_itemcode.bgst."力量"] = 6
  └─ 保存数据到哈希表: [typename11_itemcode.ciri."智力"] = 6
```

### 获得物品HD

```text
触发器: 获得物品HD (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 设置局部变量:"d"=GetManipulatingUnit()
  ├─ 设置局部变量:"w"=被操作物品()
  ├─ 设置局部变量:"wp"=物品类型ID(读取局部变量("w"))
  ├─ ── 读取物品属性 ──
  ├─ 设置局部变量:"gj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "攻击力")
  ├─ 设置局部变量:"hj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "护甲")
  ├─ 设置局部变量:"ll"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "力量")
  ├─ 设置局部变量:"mj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "敏捷")
  ├─ 设置局部变量:"zl"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "智力")
  ├─ ── 读取英雄属性 ──
  ├─ 设置局部变量:"gj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "攻击力")
  ├─ 设置局部变量:"hj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "护甲")
  ├─ 设置局部变量:"ll1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "力量")
  ├─ 设置局部变量:"mj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "敏捷")
  ├─ 设置局部变量:"zl1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "智力")
  ├─ ── 计算属性 ──
  ├─ 设置局部变量:"gj"=(读取局部变量("gj") + 读取局部变量("gj1"))
  ├─ 设置局部变量:"hj"=(读取局部变量("hj") + 读取局部变量("hj1"))
  ├─ 设置局部变量:"ll"=(读取局部变量("ll") + 读取局部变量("ll1"))
  ├─ 设置局部变量:"mj"=(读取局部变量("mj") + 读取局部变量("mj1"))
  ├─ 设置局部变量:"zl"=(读取局部变量("zl") + 读取局部变量("zl1"))
  ├─ ── 修改绿字属性 ──
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A001, 1, ABILITY_DATA_DATA_A, 读取局部变量("gj")
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A000, 1, ABILITY_DATA_DATA_A, 读取局部变量("hj")
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_C, (读取局部变量("ll")转实数)
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_A, (读取局部变量("mj")转实数)
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_B, (读取局部变量("zl")转实数)
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A000
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A000
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A001
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A001
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A002
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A002
  ├─ ── 记录当前属性 ──
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."攻击力"] = 读取局部变量("gj")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."护甲"] = 读取局部变量("hj")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."力量"] = 读取局部变量("ll")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."敏捷"] = 读取局部变量("mj")
  └─ 保存数据到哈希表: [单位类型.读取局部变量("d")."智力"] = 读取局部变量("zl")
```

### 丢弃物品DQ

```text
触发器: 丢弃物品DQ (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroDropItem
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 设置局部变量:"d"=GetManipulatingUnit()
  ├─ 设置局部变量:"w"=被操作物品()
  ├─ 设置局部变量:"wp"=物品类型ID(读取局部变量("w"))
  ├─ ── 读取物品属性 ──
  ├─ 设置局部变量:"gj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "攻击力")
  ├─ 设置局部变量:"hj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "护甲")
  ├─ 设置局部变量:"ll"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "力量")
  ├─ 设置局部变量:"mj"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "敏捷")
  ├─ 设置局部变量:"zl"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "智力")
  ├─ ── 读取英雄属性 ──
  ├─ 设置局部变量:"gj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "攻击力")
  ├─ 设置局部变量:"hj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "护甲")
  ├─ 设置局部变量:"ll1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "力量")
  ├─ 设置局部变量:"mj1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "敏捷")
  ├─ 设置局部变量:"zl1"=从哈希表读取数据(单位类型, 读取局部变量("d"), "智力")
  ├─ ── 计算属性 ──
  ├─ 设置局部变量:"gj"=(读取局部变量("gj1") - 读取局部变量("gj"))
  ├─ 设置局部变量:"hj"=(读取局部变量("hj1") - 读取局部变量("hj"))
  ├─ 设置局部变量:"ll"=(读取局部变量("ll1") - 读取局部变量("ll"))
  ├─ 设置局部变量:"mj"=(读取局部变量("mj1") - 读取局部变量("mj"))
  ├─ 设置局部变量:"zl"=(读取局部变量("zl1") - 读取局部变量("zl"))
  ├─ ── 修改绿字属性 ──
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A001, 1, ABILITY_DATA_DATA_A, 读取局部变量("gj")
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A000, 1, ABILITY_DATA_DATA_A, 读取局部变量("hj")
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_C, (读取局部变量("ll")转实数)
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_A, (读取局部变量("mj")转实数)
  ├─ YDWESetUnitAbilityDataReal: 读取局部变量("d"), A002, 1, ABILITY_DATA_DATA_B, (读取局部变量("zl")转实数)
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A000
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A000
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A001
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A001
  ├─ IncUnitAbilityLevel: 读取局部变量("d"), A002
  ├─ DecUnitAbilityLevel: 读取局部变量("d"), A002
  ├─ ── 记录当前属性 ──
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."攻击力"] = 读取局部变量("gj")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."护甲"] = 读取局部变量("hj")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."力量"] = 读取局部变量("ll")
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."敏捷"] = 读取局部变量("mj")
  └─ 保存数据到哈希表: [单位类型.读取局部变量("d")."智力"] = 读取局部变量("zl")
```

