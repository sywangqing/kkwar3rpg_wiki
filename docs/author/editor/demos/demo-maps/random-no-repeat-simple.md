---
title: 随机不重复简易 - 演示图实战
category: kk-triggers
slug: demo-maps/random-no-repeat-simple
description: 演示图 随机不重复简易 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 随机不重复简易 — 演示图实战

> 演示图：随机不重复简易版.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\随机不重复简易版.w3x`

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
  └─ YDWEForLoopLocVarMultiple: "i", 1, 10
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"tree"=RandomDestructableInRectSimpleBJ(gg_rct______________000)
  ├─ 设置局部变量:"v"=从哈希表读取数据(typename15_destructable, 读取局部变量("tree"), "值")
  ├─ RemoveDestructable: 读取局部变量("tree")
  └─ 显示文本→Player00: 0
```

