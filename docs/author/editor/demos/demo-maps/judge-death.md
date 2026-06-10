---
title: 正确判断死亡 - 演示图实战
category: kk-triggers
slug: demo-maps/judge-death
description: 演示图 正确判断死亡 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 正确判断死亡 — 演示图实战

> 演示图：正确判断死亡 演示图.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\正确判断死亡 演示图.w3x`

## 📑 触发器目录

- 设置血量
- Esc 判断

---

## 📜 触发器代码

### 设置血量

```text
触发器: 设置血量 (初始化) [✓] — 聊天输入血量，比如 0.406 和 0.405


───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 ""
条件
  └─ 无
动作
  ├─ 设置局部变量:"v"=S2R(玩家聊天字符串())
  └─ SetUnitState: gg_unit_hfoo_0002, UnitStateLifeSec, 读取局部变量("v")
```

### Esc 判断

```text
触发器: Esc 判断 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"u"=gg_unit_hfoo_0002
  └─ 如果
       ├─ 条件: 单位存活判断(读取局部变量("u")) == TRUE
       ├─ 则
       │    显示文本→Player00: 0
       └─ 否则
            显示文本→Player00: 0
```

