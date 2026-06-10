---
title: 开关门 - 演示图实战
category: kk-triggers
slug: demo-maps/door-switch
description: 演示图 开关门 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 开关门 — 演示图实战

> 演示图：开关门.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 未命名触发器 001
- 未命名触发器 001 复制

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"U"=触发单位()
  ├─ 如果
  │    ├─ 条件: 从哈希表读取数据(单位类型, 读取局部变量("U"), "门") == 0
  │    ├─ 则
  │    │    ReplaceUnitBJ: 读取局部变量("U"), h001, UnitStateMethodRelative
  │    │    设置局部变量:"U2"=bj_lastReplacedUnit
  │    │    SetUnitAnimationByIndex: 读取局部变量("U2"), 2
  │    │    保存数据到哈希表: [单位类型.读取局部变量("U2")."门"] = 1
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 从哈希表读取数据(单位类型, 读取局部变量("U"), "门") == 1
       ├─ 则
       │    ReplaceUnitBJ: 读取局部变量("U"), h000, UnitStateMethodRelative
       │    设置局部变量:"U2"=bj_lastReplacedUnit
       │    SetUnitAnimationByIndex: 读取局部变量("U2"), 1
       │    清除哈希表: [单位类型.读取局部变量("U").整数]
       └─ 否则: (无)
```

### 未命名触发器 001 复制

```text
触发器: 未命名触发器 001 复制 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A001)
动作
  ├─ 设置局部变量:"U"=触发单位()
  ├─ 如果
  │    ├─ 条件: 从哈希表读取数据(单位类型, 读取局部变量("U"), "门") == 0
  │    ├─ 则
  │    │    ReplaceUnitBJ: 读取局部变量("U"), h003, UnitStateMethodRelative
  │    │    设置局部变量:"U2"=bj_lastReplacedUnit
  │    │    SetUnitAnimationByIndex: 读取局部变量("U2"), 2
  │    │    保存数据到哈希表: [单位类型.读取局部变量("U2")."门"] = 1
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 从哈希表读取数据(单位类型, 读取局部变量("U"), "门") == 1
       ├─ 则
       │    ReplaceUnitBJ: 读取局部变量("U"), h002, UnitStateMethodRelative
       │    设置局部变量:"U2"=bj_lastReplacedUnit
       │    SetUnitAnimationByIndex: 读取局部变量("U2"), 1
       │    清除哈希表: [单位类型.读取局部变量("U").整数]
       └─ 否则: (无)
```

