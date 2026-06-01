---
title: 千千万万个胖虎 - 演示图实战
category: kk-triggers
slug: demo-maps/panghu-many
description: 演示图 千千万万个胖虎 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 千千万万个胖虎 — 演示图实战

> 演示图：千千万万个胖虎.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\千千万万个胖虎.w3x`

## 📑 触发器目录

- 1
- 2

---

## 📜 触发器代码

### 1

```text
触发器: 1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 设置 A/*波数单位类型*/[1] = hmil
  ├─ 设置 A/*波数单位类型*/[2] = hfoo
  ├─ 设置 A/*波数单位类型*/[3] = hkni
  ├─ 设置 A/*波数单位类型*/[4] = hrif
  ├─ 设置 A/*波数单位类型*/[5] = hmtt
  ├─ 设置 A/*波数单位类型*/[6] = hcth
  ├─ 设置 B3/*BOSS类型*/[1] = Hart
  ├─ 设置 B3/*BOSS类型*/[2] = Hpb2
  ├─ 运行计时器 J/*计时器*/ (一次性, 5.00s)
  ├─ 计时器窗口: J/*计时器*/ 标题="TRIGSTR_001"
  ├─ 设置 C/*计时器窗口*/ = bj_lastCreatedTimerDialog
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### 2

```text
触发器: 2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 B2/*波数*/ = (B2/*波数*/ + 1)
  ├─ 运行计时器 J/*计时器*/ (一次性, 10.00s)
  ├─ TimerDialogSetTitleBJ: C/*计时器窗口*/, "第" + (B2/*波数*/转字符串) + "波"
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

