---
title: 移动大头像 - 演示图实战
category: kk-triggers
slug: demo-maps/move-portrait
description: 演示图 移动大头像 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 移动大头像 — 演示图实战

> 演示图：移动大头像下方文本.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\移动大头像下方文本.w3x`

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
  ├─ 设置局部变量:"ui"=自定义代码("DzFrameGetAlpha(DzFrameGetPortrait() + 0x194)")
  ├─ DzFrameClearAllPoints: 读取局部变量("ui")
  ├─ DzFrameSetAbsolutePoint: 读取局部变量("ui"), FramePoints_Center, 0.40, 0.30
  ├─ 设置局部变量:"ui1"=自定义代码("DzFrameGetAlpha(DzFrameGetPortrait() + 0x198)")
  ├─ DzFrameClearAllPoints: 读取局部变量("ui1")
  └─ DzFrameSetPoint: 读取局部变量("ui1"), FramePoints_Top , 读取局部变量("ui"), FramePoints_Bottom, 0, 0
```

