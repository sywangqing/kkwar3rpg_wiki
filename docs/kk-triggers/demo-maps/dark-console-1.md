---
title: 暗黑控制台1 - 演示图实战
category: kk-triggers
slug: demo-maps/dark-console-1
description: 演示图 暗黑控制台1 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 暗黑控制台1 — 演示图实战

> 演示图：暗黑控制台1.w3x
>
> 触发器数：**10**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\暗黑控制台1.w3x`

## 📑 触发器目录

- 简介
- 未命名触发器 001
- 未命名触发器 003
- 未命名触发器 004
- 未命名触发器 006
- -----------
- 未命名触发器 005
- 1注册UI
- 2实时更新
- 未命名触发器 007

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
  ├─ CameraSetSmoothingFactorBJ: 100.00
  ├─ SetTimeOfDay: 12
  ├─ SetTimeOfDayScale: 0
  ├─ EnableWorldFogBoundary: EnableDisableDisable
  ├─ DzUnlockBlpSizeLimit: true
  ├─ DzFrameEnableClipRect: NO
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  ├─ 迷雾遮罩开关: EnabledDisabledDisabled
  ├─ DzFrameHideInterface
  ├─ DzEnableWideScreen: optionEnable_Enable
  ├─ DzFrameEditBlackBorders: 0.00, 0.00
  ├─ ── === ──
  ├─ DzLoadToc: custom.toc
  ├─ ── === ──
  ├─ 设置 YX[1] = gg_unit_Hpal_0002
  ├─ 设置 YX[2] = gg_unit_Hpal_0001
  ├─ 设置 YX[3] = gg_unit_Hpal_0000
  ├─ 设置 YX[4] = gg_unit_Hpal_0003
  ├─ 保存数据到哈希表: [单位类型.gg_unit_Hpal_0002."体力"] = 50.00
  ├─ ── === ──
  ├─ 设置局部变量:"UI2"=DzFrameGetMinimap()
  ├─ DzFrameClearAllPoints: 读取局部变量("UI2")
  ├─ DzFrameSetSize: 读取局部变量("UI2"), OperatorRealDivide(218.00, 2400.00), OperatorRealDivide(140.00, 1800.00)
  ├─ DzFrameSetPoint: 读取局部变量("UI2"), FramePoints_Center, DzGetGameUI(), FramePoints_TopRight, OperatorRealDivide(-126.00, 2400.00), OperatorRealDivide(-114.00, 1800.00)
  └─ DzFrameShow: 读取局部变量("UI2"), true
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
  ├─ ── =========== ──
  ├─ 设置局部变量:"UI"=DzFrameGetChatMessage()
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(700.00, 2400.00), OperatorRealDivide(150.00, 1800.00)
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_BottomLeft, DzGetGameUI(), FramePoints_TopLeft, OperatorRealDivide(120.00, 2400.00), OperatorRealDivide(-700.00, 1800.00)
  ├─ DzFrameShow: 读取局部变量("UI"), true
  ├─ ── =========== ──
  ├─ 设置局部变量:"UI"=DzFrameGetUnitMessage()
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(700.00, 2400.00), OperatorRealDivide(200.00, 1800.00)
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_BottomLeft, DzGetGameUI(), FramePoints_TopLeft, OperatorRealDivide(120.00, 2400.00), OperatorRealDivide(-470.00, 1800.00)
  ├─ DzFrameShow: 读取局部变量("UI"), true
  ├─ ── =========== ──
  ├─ 设置局部变量:"UI"=DzFrameGetWorldFrameMessage()
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(700.00, 2400.00), OperatorRealDivide(90.00, 1800.00)
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_Center, DzGetGameUI(), FramePoints_Bottom, OperatorRealDivide(150.00, 2400.00), OperatorRealDivide(360.00, 1800.00)
  ├─ DzFrameShow: 读取局部变量("UI"), true
  ├─ ── === ──
  ├─ 设置局部变量:"UI"=DzCreateFrameByTagName("BACKDROP", "name", DzFrameGetParent(DzFrameGetPortrait()), "template", 0)
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), 0.80, 0.60
  ├─ DzFrameSetAlpha: 读取局部变量("UI"), 128
  ├─ DzFrameSetTexture: 读取局部变量("UI"), UI\yinying.tga, 0
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_Center, DzGetGameUI(), FramePoints_Center, 0.00, 0.00
  ├─ ── === ──
  ├─ 设置 KZT[0] = DzCreateFrameByTagName("FRAME", "name", DzFrameGetParent(DzFrameGetMinimap()), "template", 0)
  ├─ DzFrameSetSize: KZT[0], OperatorRealDivide(1114.00, 2400.00), OperatorRealDivide(153.00, 1800.00)
  ├─ DzFrameSetPoint: KZT[0], FramePoints_Bottom, DzGetGameUI(), FramePoints_Bottom, 0.00, 0.00
  ├─ ── 控制台背景 ──
  ├─ 设置 KZT[1] = DzCreateFrameByTagName("BACKDROP", "name", KZT[0], "template", 0)
  ├─ DzFrameSetSize: KZT[1], OperatorRealDivide(1114.00, 2400.00), OperatorRealDivide(153.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[1], UI\kzt (1).tga, 0
  ├─ DzFrameSetPoint: KZT[1], FramePoints_Bottom, DzGetGameUI(), FramePoints_Bottom, 0.00, 0.00
  ├─ 执行区域代码块: "小地图背景"
  ├─ ── === ──
  └─ 执行区域代码块: "物品技能按钮"
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 执行区域代码块: "经验Z&修炼"
  ├─ 执行区域代码块: "功能按钮"
  ├─ 执行区域代码块: "怒气"
  ├─ 设置 KZT[40] = DzCreateFrame("文本01", KZT[1], 40)
  ├─ DzFrameSetFont: KZT[40], "ziti.ttf", OperatorRealDivide(12.00, 1800.00), 0
  ├─ DzFrameSetSize: KZT[40], OperatorRealDivide(234.00, 2400.00), 0.00
  ├─ DzFrameSetTextAlignment: KZT[40], 0
  ├─ DzFrameSetText: KZT[40], "|cffffff00怒气值：100%|r"
  └─ DzFrameSetPoint: KZT[40], FramePoints_Left, DzGetGameUI(), FramePoints_BottomLeft, OperatorRealDivide(10.00, 2400.00), OperatorRealDivide(20.00, 1800.00)
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  └─ 执行区域代码块: "头像"
```

### 未命名触发器 006

```text
触发器: 未命名触发器 006 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  └─ YDWEForLoopLocVarMultiple: "A", 105, 109
```

### -----------

```text
触发器: ----------- (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 005

```text
触发器: 未命名触发器 005 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.01)
条件
  └─ 无
动作
  └─ DzFrameSetUpdateCallbackMultiple: GetLocalPlayer()
```

### 1注册UI

```text
触发器: 1注册UI (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.10)
条件
  └─ 无
动作
  ├─ 设置 Heros = 区域内全部单位(可用地图区域())
  ├─ 设置局部变量:"UI计数"=0
  └─ 单位组: 选取 Heros 中所有单位
       ├─ 设置局部变量:"UI计数"=OperatorIntegerAdd(读取局部变量("UI计数"), 1)
       ├─ 设置 UItb[读取局部变量("UI计数")] = DzCreateFrameByTagName("BACKDROP", "name", DzGetGameUI(), "template", 0)
       ├─ DzFrameSetSize: UItb[读取局部变量("UI计数")], OperatorRealDivide(32.00, 2400.00), OperatorRealDivide(32.00, 1800.00)
       ├─ DzFrameSetPoint: UItb[读取局部变量("UI计数")], FramePoints_Center, DzFrameGetMinimap(), FramePoints_Center, 0.00, 0.00
       ├─ 如果
       │    ├─ 条件: 单位类型判断(选取单位(), 建筑) == TRUE
       │    ├─ 则
       │    │    DzFrameSetTexture: UItb[读取局部变量("UI计数")], touxiang\02.tga, 0
       │    └─ 否则
       │         如果
       │           ├─ 条件: IsPlayerAlly((选取单位()的所有者), Player00) == TRUE
       │           ├─ 则
       │           │    DzFrameSetTexture: UItb[读取局部变量("UI计数")], touxiang\01.tga, 0
       │           └─ 否则
       │                如果
       │                  ├─ 条件: 单位类型判断(选取单位(), UnitTypeAncient) == TRUE
       │                  ├─ 则
       │                  │    DzFrameSetTexture: UItb[读取局部变量("UI计数")], touxiang\03.tga, 0
       │                  └─ 否则
       │                       如果
       │                         ├─ 条件: 单位类型判断(选取单位(), UnitTypeGiant) == TRUE
       │                         ├─ 则
       │                         │    DzFrameSetTexture: UItb[读取局部变量("UI计数")], touxiang\04.tga, 0
       │                         └─ 否则
       │                              如果
       │                                ├─ 条件: IsPlayerEnemy((选取单位()的所有者), Player00) == TRUE
       │                                ├─ 则
       │                                │    DzFrameSetTexture: UItb[读取局部变量("UI计数")], touxiang\05.tga, 0
       │                                └─ 否则: (无)
       └─ 设置单位自定义值: 选取单位(), 读取局部变量("UI计数")
```

### 2实时更新

```text
触发器: 2实时更新 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.01)
条件
  └─ 无
动作
  ├─ 设置局部变量:"地图宽"=GetRectWidthBJ(可用地图区域())
  ├─ 设置局部变量:"地图高"=GetRectHeightBJ(可用地图区域())
  └─ 如果
       ├─ 条件: OperatorCompareDegree(读取局部变量("地图宽"), OperatorGreaterEq, 读取局部变量("地图高"))
       ├─ 则
       │    单位组: 选取 Heros 中所有单位
       │      ├─ 设置局部变量:"单位X"=单位X坐标(选取单位())
       │      ├─ 设置局部变量:"单位Y"=单位Y坐标(选取单位())
       │      ├─ 设置局部变量:"X"=(读取局部变量("单位X") - 区域最小X(可用地图区域()))
       │      ├─ 设置局部变量:"Y"=(读取局部变量("单位Y") - 区域最小Y(可用地图区域()))
       │      ├─ 设置局部变量:"X比例"=RAbsBJ(OperatorRealDivide(读取局部变量("X"), 读取局部变量("地图宽")))
       │      ├─ 设置局部变量:"Y比例"=RAbsBJ(OperatorRealDivide(读取局部变量("Y"), 读取局部变量("地图高")))
       │      ├─ ── 最终比例需要乘以小地图的尺寸 ──
       │      ├─ 设置局部变量:"最终X比例"=(读取局部变量("X比例") x OperatorRealDivide(218.00, 2400.00))
       │      ├─ 设置局部变量:"最终Y比例"=(读取局部变量("Y比例") x (140.00 / 1800.00))
       │      └─ DzFrameSetPoint: UItb[单位自定义值(选取单位())], FramePoints_Center, DzFrameGetMinimap(), FramePoints_BottomLeft, 读取局部变量("最终X比例"), 读取局部变量("最终Y比例")
       └─ 否则: (无)
```

### 未命名触发器 007

```text
触发器: 未命名触发器 007 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  ├─ 从单位组移除单位: 触发单位(), Heros
  ├─ DzFrameShow: UItb[单位自定义值(触发单位())], false
  └─ DzDestroyFrame: UItb[单位自定义值(触发单位())]
```

