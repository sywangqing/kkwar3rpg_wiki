---
title: 对话框选难度 - 演示图实战
category: kk-triggers
slug: demo-maps/dialog-difficulty
description: 演示图 对话框选难度 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 对话框选难度 — 演示图实战

> 演示图：对话框选难度.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 对话框
- 未命名触发器 001
- 未命名触发器 002

---

## 📜 触发器代码

### 对话框

```text
触发器: 对话框 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ DialogSetMessageBJ: dhk, "TRIGSTR_001"
  ├─ DialogAddButtonBJ: dhk, "TRIGSTR_002"
  ├─ 保存数据到哈希表: [typename30_dialog.dhk."an"] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dhk, "TRIGSTR_003"
  ├─ 保存数据到哈希表: [typename30_dialog.dhk."an2"] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dhk, "TRIGSTR_004"
  ├─ 保存数据到哈希表: [typename30_dialog.dhk."an3"] = bj_lastCreatedButton
  └─ DialogDisplay: Player00, dhk, ShowHideShow
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(dhk)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, 从哈希表读取数据(typename30_dialog, dhk, "an"))
       ├─ 则
       │    显示文本→GetPlayersAll(): "TRIGSTR_005"
       └─ 否则
            如果
              ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, 从哈希表读取数据(typename30_dialog, dhk, "an2"))
              ├─ 则
              │    显示文本→GetPlayersAll(): "TRIGSTR_006"
              └─ 否则
                   显示文本→GetPlayersAll(): "TRIGSTR_007"
```

