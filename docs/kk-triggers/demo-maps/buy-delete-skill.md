---
title: 购买删除技能 - 演示图实战
category: kk-triggers
slug: demo-maps/buy-delete-skill
description: 演示图 购买删除技能 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 购买删除技能 — 演示图实战

> 演示图：购买删除技能.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\购买删除技能.w3x`

## 📑 触发器目录

- 简介
- 未命名触发器 001

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  ├─ 迷雾遮罩开关: EnabledDisabledDisabled
  ├─ 保存数据到哈希表: [typename11_itemcode.tint."技能"] = A001
  ├─ 保存数据到哈希表: [typename11_itemcode.tdex."技能"] = A002
  └─ 保存数据到哈希表: [typename11_itemcode.tstr."技能"] = A000
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 设置局部变量:"d"=GetManipulatingUnit()
  ├─ 设置局部变量:"wj"=(读取局部变量("d")的所有者)
  ├─ 设置局部变量:"w"=被操作物品()
  ├─ 设置局部变量:"wp"=物品类型ID(读取局部变量("w"))
  ├─ 如果
  │    ├─ 条件: 检查哈希表有数据(typename11_itemcode, 读取局部变量("wp"), typename09_abilcode, "技能") == TRUE
  │    ├─ 则
  │    │    设置局部变量:"jn"=从哈希表读取数据(typename11_itemcode, 读取局部变量("wp"), "技能")
  │    │    如果
  │    │      ├─ 条件: 检查哈希表有数据(单位类型, 读取局部变量("d"), typename09_abilcode, "1") == TRUE
  │    │      ├─ 则
  │    │      │    保存数据到哈希表: [单位类型.读取局部变量("d")."1"] = 读取局部变量("jn")
  │    │      │    添加技能: 读取局部变量("d"), 读取局部变量("jn")
  │    │      │    显示文本→读取局部变量("wj"): 0
  │    │      └─ 否则
  │    │           如果
  │    │             ├─ 条件: 检查哈希表有数据(单位类型, 读取局部变量("d"), typename09_abilcode, "2") == TRUE
  │    │             ├─ 则
  │    │             │    保存数据到哈希表: [单位类型.读取局部变量("d")."2"] = 读取局部变量("jn")
  │    │             │    添加技能: 读取局部变量("d"), 读取局部变量("jn")
  │    │             │    显示文本→读取局部变量("wj"): 0
  │    │             └─ 否则
  │    │                  如果
  │    │                    ├─ 条件: 检查哈希表有数据(单位类型, 读取局部变量("d"), typename09_abilcode, "3") == TRUE
  │    │                    ├─ 则
  │    │                    │    保存数据到哈希表: [单位类型.读取局部变量("d")."3"] = 读取局部变量("jn")
  │    │                    │    添加技能: 读取局部变量("d"), 读取局部变量("jn")
  │    │                    │    显示文本→读取局部变量("wj"): 0
  │    │                    └─ 否则
  │    │                         显示文本→读取局部变量("wj"): 0
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(读取局部变量("wp"), OperatorEqualENE, manh)
       ├─ 则
       │    设置局部变量:"n"=玩家号(读取局部变量("wj"))
       │    DialogDestroy: jineng/*技能表*/[读取局部变量("n")]
       │    设置 jineng/*技能表*/[读取局部变量("n")] = DialogCreate()
       │    DialogSetMessageBJ: jineng/*技能表*/[读取局部变量("n")], "TRIGSTR_023"
       │    设置局部变量:"jn"=从哈希表读取数据(单位类型, 读取局部变量("d"), "1")
       │    设置局部变量:"1"=DialogAddButton(jineng/*技能表*/[读取局部变量("n")], 技能名称(读取局部变量("jn")), HotKeyIntNull)
       │    设置局部变量:"jn"=从哈希表读取数据(单位类型, 读取局部变量("d"), "2")
       │    设置局部变量:"2"=DialogAddButton(jineng/*技能表*/[读取局部变量("n")], 技能名称(读取局部变量("jn")), HotKeyIntNull)
       │    设置局部变量:"jn"=从哈希表读取数据(单位类型, 读取局部变量("d"), "3")
       │    设置局部变量:"3"=DialogAddButton(jineng/*技能表*/[读取局部变量("n")], 技能名称(读取局部变量("jn")), HotKeyIntNull)
       │    DialogDisplay: 读取局部变量("wj"), jineng/*技能表*/[读取局部变量("n")], ShowHideShow
       │    设置局部变量:"cfq"=CreateTrigger()
       │    YDWERegisterTriggerMultiple: 读取局部变量("cfq")
       └─ 否则: (无)
```

