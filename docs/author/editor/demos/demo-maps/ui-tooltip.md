---
title: UI提示框 - 演示图实战
category: kk-triggers
slug: demo-maps/ui-tooltip
description: 演示图 UI提示框 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 UI提示框 — 演示图实战

> 演示图：技能和物品的自定义UI提示框模拟.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\技能和物品的自定义UI提示框模拟.w3x`

## 📑 触发器目录

- 必要的初始化
- ESC显示时间

---

## 📜 触发器代码

### 必要的初始化

```text
触发器: 必要的初始化 (初始化) [✓] — 记得变量里面的Year什么的 都要复制过去
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.10)
条件
  └─ 无
动作
  └─ CustomScriptCode: "call UpdateTimeAll()"
```

### ESC显示时间

```text
触发器: ESC显示时间 (初始化) [✓] — Week  0表示星期天
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  ├─ ClearTextMessagesBJ: Force00
  ├─ 显示文本→Player00: 0
  ├─ 显示文本→Player00: 0
  └─ 显示文本→Player00: 0
```

