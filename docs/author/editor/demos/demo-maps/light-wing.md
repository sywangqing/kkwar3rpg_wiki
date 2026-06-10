---
title: 光翼展开 - 演示图实战
category: kk-triggers
slug: demo-maps/light-wing
description: 演示图 光翼展开 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 光翼展开 — 演示图实战

> 演示图：光翼展开.w3x
>
> 触发器数：**8**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 简介
- 排泄 gfhfg
- 视野 dgfd
- 伤害显示  khjhj
- 镜头+300 fdhfd
- 镜头-300 gdgdf
- 技能
- 光翼展开 jhgjh

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ DzTriggerRegisterMallItemSyncData()
条件
  ├─ DzGetTriggerMallItem() == "商品key"
  └─ DzGetTriggerMallItemPlayer() == Player00
动作
  ├─ ── 欢迎使用世界编辑器，开始你的地图创造之旅。 ──
  ├─ ── 你可以从dz.163.com获取最新编辑器咨询。 ──
  ├─ ── 当你的地图意外损坏时，你可以在backups目录找到你最近26次保存的地图。 ──
  ├─ ── 任何疑问请加官方作者群：QQ35063417。 ──
  └─ DzAPI_Map_OpenMall: Player00, "商品key"
```

### 排泄 gfhfg

```text
触发器: 排泄 gfhfg (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  └─ YDWEMemoryLeakHelperDisplayLeaks
```

### 视野 dgfd

```text
触发器: 视野 dgfd (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  └─ CreateFogModifierRectBJ: EnabledDisabledEnabled, Player00, FogStateVisible, 可用地图区域()
```

### 伤害显示  khjhj

```text
触发器: 伤害显示  khjhj (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 伤害值() OperatorGreater 0.00
动作
  ├─ CreateTextTagUnitBJ: (实数转整数(伤害值())转字符串), 触发单位(), 0, 10, 100, 0.00, 0.00, 0
  ├─ SetTextTagColor: bj_lastCreatedTextTag, 255, 0, 0, 255
  ├─ SetTextTagVelocityBJ: GetLastCreatedTextTag(), 120.00, 角度叠加(90.00, 弧度转角度(随机实数(-30.00, 30.00)))
  ├─ SetTextTagPermanentBJ: GetLastCreatedTextTag(), EnableDisableDisable
  ├─ SetTextTagLifespanBJ: GetLastCreatedTextTag(), 1.50
  ├─ SetTextTagFadepointBJ: GetLastCreatedTextTag(), 1.00
  └─ 启动计时器: 创建计时器(), 0.01s (循环)
```

### 镜头+300 fdhfd

```text
触发器: 镜头+300 fdhfd (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 PlayerALL 输入 "+"
条件
  └─ 无
动作
  ├─ 设置局部变量:"a"=0
  └─ 启动计时器: 创建计时器(), 0.01s (循环)
```

### 镜头-300 gdgdf

```text
触发器: 镜头-300 gdgdf (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 PlayerALL 输入 "-"
条件
  └─ 无
动作
  ├─ 设置局部变量:"a"=0
  └─ 启动计时器: 创建计时器(), 0.01s (循环)
```

### 技能

```text
触发器: 技能 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 光翼展开 jhgjh

```text
触发器: 光翼展开 jhgjh (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"a"=0
  ├─ 设置局部变量:"q1"=触发单位()
  └─ 启动计时器: 创建计时器(), 0.10s (循环)
```

