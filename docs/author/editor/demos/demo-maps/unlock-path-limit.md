---
title: 解锁寻路上限 - 演示图实战
category: kk-triggers
slug: demo-maps/unlock-path-limit
description: 演示图 解锁寻路上限 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 解锁寻路上限 — 演示图实战

> 演示图：解锁寻路上限.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 解锁单位寻路上限

---

## 📜 触发器代码

### 解锁单位寻路上限

```text
触发器: 解锁单位寻路上限 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 设置局部变量:"ui"=DzCreateFrameByTagName("FRAME", "name", DzGetGameUI(), "template", 0)
  ├─ 设置局部变量:"i"=DzFrameGetAlpha(DzI2F((DzF2I(读取局部变量("ui")) - 172)))
  ├─ DzDestroyFrame: 读取局部变量("ui")
  ├─ 设置局部变量:"i"=(读取局部变量("i") + 自定义代码("2537628"))
  └─ YDWEForLoopLocVarMultiple: "i", 0, 63
```

