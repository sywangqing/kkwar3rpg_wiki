---
title: 判断技能按钮 - 演示图实战
category: kk-triggers
slug: demo-maps/ability-button-check
description: 演示图 判断技能按钮 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 判断技能按钮 — 演示图实战

> 演示图：判断技能按钮是否显示.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\判断技能按钮是否显示.w3x`

## 📑 触发器目录

- 简介

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"1"=DzFrameGetCommandBarButton(2, 0)
  ├─ 设置局部变量:"2"=DzFrameGetAlpha(DzI2F(OperatorIntegerSubtract(DzF2I(读取局部变量("1")), 28)))
  └─ 如果
       ├─ 条件: 读取局部变量("2") == 1
       ├─ 则
       │    显示文本→Player00: 0
       └─ 否则
            显示文本→Player00: 0
```

