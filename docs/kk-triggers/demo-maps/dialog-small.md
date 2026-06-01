---
title: 对话框小演示 - 演示图实战
category: kk-triggers
slug: demo-maps/dialog-small
description: 演示图 对话框小演示 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 对话框小演示 — 演示图实战

> 演示图：对话框小演示.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\对话框小演示.w3x`

## 📑 触发器目录

- 简介

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"Dui"=DialogCreate()
  ├─ DialogSetMessageBJ: 读取局部变量("Dui"), "TRIGSTR_003"
  ├─ 设置局部变量:"an1"=DialogAddButton(读取局部变量("Dui"), "TRIGSTR_015", HotKeyIntNull)
  ├─ 设置局部变量:"an2"=DialogAddButton(读取局部变量("Dui"), "TRIGSTR_017", HotKeyIntNull)
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  └─ DialogDisplay: Player00, 读取局部变量("Dui"), ShowHideShow
```

