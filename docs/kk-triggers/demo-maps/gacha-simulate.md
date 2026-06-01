---
title: 模拟抽卡 - 演示图实战
category: kk-triggers
slug: demo-maps/gacha-simulate
description: 演示图 模拟抽卡 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 模拟抽卡 — 演示图实战

> 演示图：模拟抽卡.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 抽卡

---

## 📜 触发器代码

### 抽卡

```text
触发器: 抽卡 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I004)
动作
  ├─ 设置局部变量:"random_real_number"=随机实数(0, 90.00)
  ├─ 设置局部变量:"probability"=OperatorRealAdd((guarantee转实数), 0.50)
  └─ 如果
       ├─ 条件: 读取局部变量("probability") OperatorGreaterEq 读取局部变量("random_real_number")
       ├─ 则
       │    如果
       │      ├─ 条件: big_guarantee == 0
       │      ├─ 则
       │      │    设置局部变量:"ramdom"=随机[1~3]
       │      │    如果
       │      │      ├─ 条件: 读取局部变量("random") OperatorGreaterEq 2
       │      │      ├─ 则
       │      │      │    创建物品: I000, (区域可用地图区域()中心)
       │      │      │    设置 big_guarantee = 0
       │      │      │    设置 small_guarantee = 0
       │      │      └─ 否则
       │      │           创建物品: I001, (区域可用地图区域()中心)
       │      │           设置 big_guarantee = 1
       │      │           设置 small_guarantee = 0
       │      └─ 否则
       │           创建物品: I000, (区域可用地图区域()中心)
       │           设置 big_guarantee = 0
       │           设置 small_guarantee = 0
       │    设置 guarantee = 0
       └─ 否则
            设置 guarantee = OperatorIntegerAdd(guarantee, 1)
            设置局部变量:"random"=随机[1~10]
            如果
              ├─ 条件: 读取局部变量("random") OperatorLessEq small_guarantee
              ├─ 则
              │    创建物品: I002, (区域可用地图区域()中心)
              │    设置 small_guarantee = 0
              └─ 否则
                   创建物品: I003, (区域可用地图区域()中心)
                   设置 small_guarantee = OperatorIntegerAdd(small_guarantee, 1)
```

