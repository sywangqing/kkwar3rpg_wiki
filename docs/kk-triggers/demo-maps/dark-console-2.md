---
title: 暗黑控制台2 - 演示图实战
category: kk-triggers
slug: demo-maps/dark-console-2
description: 演示图 暗黑控制台2 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 暗黑控制台2 — 演示图实战

> 演示图：暗黑控制台2.w3x
>
> 触发器数：**22**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\暗黑控制台2.w3x`

## 📑 触发器目录

- 简介
- XXK 信息框
- KZT 控制台
- -----------
- YJTB 药剂同步
- -----------
- MZHZ 每帧绘制
- -----------
- SFJN 释放技能
- -----------
- 护盾增加HD 002
- -----------
- 伤害事件SH 003
- -----------
- -----------
- YAOJI
- Q
- W
- E
- R
- D
- F

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
  ├─ DzEnableWideScreen: optionEnable_Enable
  ├─ CameraSetSmoothingFactorBJ: 100.00
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  ├─ 迷雾遮罩开关: EnabledDisabledDisabled
  ├─ DzFrameHideInterface
  ├─ DzUnlockBlpSizeLimit: true
  ├─ DzFrameEditBlackBorders: 0.00, 0.00
  ├─ ── === ──
  ├─ DzLoadToc: custom.toc
  ├─ ── === ──
  ├─ 设置 YX[1] = gg_unit_Hpal_0000
  ├─ 设置 YX[2] = gg_unit_Hpal_0002
  ├─ 设置 YX[3] = gg_unit_Hpal_0001
  ├─ 设置 YX[4] = gg_unit_Hpal_0003
  └─ ── === ──
```

### XXK 信息框

```text
触发器: XXK 信息框 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
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
  └─ ── =========== ──
```

### KZT 控制台

```text
触发器: KZT 控制台 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ ── 四周阴影 ──
  ├─ 设置局部变量:"UI"=DzCreateFrameByTagName("BACKDROP", "name", DzFrameGetParent(DzFrameGetPortrait()), "template", 0)
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(960.00, 2400.00), OperatorRealDivide(540.00, 1800.00)
  ├─ DzFrameSetTexture: 读取局部变量("UI"), kzt\123_01.tga, 0
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_BottomRight, DzGetGameUI(), FramePoints_Center, 0.00, 0.00
  ├─ 设置局部变量:"UI"=DzCreateFrameByTagName("BACKDROP", "name", DzFrameGetParent(DzFrameGetPortrait()), "template", 0)
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(960.00, 2400.00), OperatorRealDivide(540.00, 1800.00)
  ├─ DzFrameSetTexture: 读取局部变量("UI"), kzt\123_02.tga, 0
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_BottomLeft, DzGetGameUI(), FramePoints_Center, 0.00, 0.00
  ├─ 设置局部变量:"UI"=DzCreateFrameByTagName("BACKDROP", "name", DzFrameGetParent(DzFrameGetPortrait()), "template", 0)
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(960.00, 2400.00), OperatorRealDivide(540.00, 1800.00)
  ├─ DzFrameSetTexture: 读取局部变量("UI"), kzt\123_03.tga, 0
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_TopRight, DzGetGameUI(), FramePoints_Center, 0.00, 0.00
  ├─ 设置局部变量:"UI"=DzCreateFrameByTagName("BACKDROP", "name", DzFrameGetParent(DzFrameGetPortrait()), "template", 0)
  ├─ DzFrameClearAllPoints: 读取局部变量("UI")
  ├─ DzFrameSetSize: 读取局部变量("UI"), OperatorRealDivide(960.00, 2400.00), OperatorRealDivide(540.00, 1800.00)
  ├─ DzFrameSetTexture: 读取局部变量("UI"), kzt\123_04.tga, 0
  ├─ DzFrameSetPoint: 读取局部变量("UI"), FramePoints_TopLeft, DzGetGameUI(), FramePoints_Center, 0.00, 0.00
  ├─ ── === ──
  ├─ ── 控制台 ──
  ├─ 设置 KZT[0] = DzCreateFrameByTagName("FRAME", "name", DzFrameGetParent(DzFrameGetMinimap()), "template", 0)
  ├─ DzFrameSetSize: KZT[0], OperatorRealDivide(1920.00, 2400.00), OperatorRealDivide(152.00, 1800.00)
  ├─ DzFrameSetPoint: KZT[0], FramePoints_Bottom, DzGetGameUI(), FramePoints_Bottom, 0.00, 0.00
  ├─ ── === ──
  ├─ ── 生命图片 ──
  ├─ 设置 KZT[51] = DzCreateFrameByTagName("BACKDROP", "name", KZT[0], "template", 0)
  ├─ DzFrameSetSize: KZT[51], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[51], kzt\hp (1).tga, 0
  ├─ DzFrameSetPoint: KZT[51], FramePoints_Center, DzGetGameUI(), FramePoints_BottomLeft, OperatorRealDivide(90.00, 2400.00), OperatorRealDivide(80.00, 1800.00)
  ├─ 设置 KZT[52] = DzCreateFrameByTagName("FRAME", "name", KZT[51], "template", 0)
  ├─ DzFrameSetSize: KZT[52], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetPoint: KZT[52], FramePoints_Bottom, KZT[51], FramePoints_Bottom, 0.00, 0.00
  ├─ DzFrameSetClip: KZT[52], OnOffOn
  ├─ 设置 KZT[53] = DzCreateFrameByTagName("BACKDROP", "name", KZT[52], "template", 0)
  ├─ DzFrameSetSize: KZT[53], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[53], kzt\hp (2).tga, 0
  ├─ DzFrameSetPoint: KZT[53], FramePoints_Center, KZT[51], FramePoints_Center, 0.00, 0.00
  ├─ ── 魔法图片 ──
  ├─ 设置 KZT[54] = DzCreateFrameByTagName("BACKDROP", "name", KZT[0], "template", 0)
  ├─ DzFrameSetSize: KZT[54], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[54], kzt\hp (1).tga, 0
  ├─ DzFrameSetPoint: KZT[54], FramePoints_Center, DzGetGameUI(), FramePoints_BottomRight, OperatorRealDivide(-90.00, 2400.00), OperatorRealDivide(80.00, 1800.00)
  ├─ 设置 KZT[55] = DzCreateFrameByTagName("FRAME", "name", KZT[54], "template", 0)
  ├─ DzFrameSetSize: KZT[55], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetPoint: KZT[55], FramePoints_Bottom, KZT[54], FramePoints_Bottom, 0.00, 0.00
  ├─ DzFrameSetClip: KZT[55], OnOffOn
  ├─ 设置 KZT[56] = DzCreateFrameByTagName("BACKDROP", "name", KZT[55], "template", 0)
  ├─ DzFrameSetSize: KZT[56], OperatorRealDivide(134.00, 2400.00), OperatorRealDivide(134.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[56], kzt\hp (3).tga, 0
  ├─ DzFrameSetPoint: KZT[56], FramePoints_Center, KZT[54], FramePoints_Center, 0.00, 0.00
  ├─ ── === ──
  ├─ ── === ──
  ├─ ── 控制台背景 ──
  ├─ 设置 KZT[1] = DzCreateFrameByTagName("BACKDROP", "name", KZT[0], "template", 0)
  ├─ DzFrameSetSize: KZT[1], OperatorRealDivide(1920.00, 2400.00), OperatorRealDivide(152.00, 1800.00)
  ├─ DzFrameSetTexture: KZT[1], kzt\kzt.tga, 0
  ├─ DzFrameSetPoint: KZT[1], FramePoints_Bottom, DzGetGameUI(), FramePoints_Bottom, 0.00, 0.00
  ├─ ── === ──
  ├─ 执行区域代码块: "物品技能按钮"
  ├─ ── 血瓶 ──
  ├─ DzTriggerRegisterKeyEventMultiple: GetLocalPlayer(), GameKeyAction_Press, GameKey_1
  ├─ DzTriggerRegisterKeyEventMultiple: GetLocalPlayer(), GameKeyAction_Press, GameKey_2
  ├─ DzTriggerRegisterKeyEventMultiple: GetLocalPlayer(), GameKeyAction_Press, GameKey_3
  ├─ 执行区域代码块: "护盾经验"
  ├─ ── 功能按钮 ──
  └─ YDWEForLoopLocVarMultiple: "A", 61, 65
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

### YJTB 药剂同步

```text
触发器: YJTB 药剂同步 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ DzTriggerRegisterSyncData("药剂", false)
条件
  └─ 无
动作
  ├─ 设置局部变量:"WJ"=DzGetTriggerSyncPlayer()
  ├─ 设置局部变量:"ZS"=字符串转整数(DzGetTriggerSyncData())
  ├─ 设置局部变量:"AA"=YX[玩家号(读取局部变量("WJ"))]
  ├─ 如果
  │    ├─ 条件: 读取局部变量("ZS") == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: KKWEGetObjectTableData(玩家, GetLocalPlayer(), 字符串, "血瓶") OperatorGreaterEq 1
  │    │      ├─ 则
  │    │      │    如果
  │    │      │      ├─ 条件: 单位生命百分比(读取局部变量("AA")) OperatorLess 100.00
  │    │      │      ├─ 则
  │    │      │      │    设置生命百分比: 读取局部变量("AA"), OperatorRealAdd(单位生命百分比(读取局部变量("AA")), 30.00)
  │    │      │      │    KKWESetObjectTableData: 玩家, 读取局部变量("WJ"), 字符串, "血瓶", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, 读取局部变量("WJ"), 字符串, "血瓶"), -1)
  │    │      │      └─ 否则
  │    │      │           显示文本→读取局部变量("WJ"): 0
  │    │      └─ 否则
  │    │           显示文本→读取局部变量("WJ"): 0
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("ZS") == 2
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: KKWEGetObjectTableData(玩家, GetLocalPlayer(), 字符串, "蓝瓶") OperatorGreaterEq 1
  │    │      ├─ 则
  │    │      │    如果
  │    │      │      ├─ 条件: GetUnitManaPercent(读取局部变量("AA")) OperatorLess 100.00
  │    │      │      ├─ 则
  │    │      │      │    设置魔法百分比: 读取局部变量("AA"), OperatorRealAdd(GetUnitManaPercent(读取局部变量("AA")), 30.00)
  │    │      │      │    KKWESetObjectTableData: 玩家, 读取局部变量("WJ"), 字符串, "蓝瓶", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, 读取局部变量("WJ"), 字符串, "蓝瓶"), -1)
  │    │      │      └─ 否则
  │    │      │           显示文本→读取局部变量("WJ"): 0
  │    │      └─ 否则
  │    │           显示文本→读取局部变量("WJ"): 0
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 读取局部变量("ZS") == 3
       ├─ 则
       │    如果
       │      ├─ 条件: KKWEGetObjectTableData(玩家, GetLocalPlayer(), 字符串, "重生") OperatorGreaterEq 1
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 单位类型判断(读取局部变量("AA"), UnitTypeDead) == TRUE
       │      │      ├─ 则
       │      │      │    KKWESetObjectTableData: 玩家, 读取局部变量("WJ"), 字符串, "重生", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, 读取局部变量("WJ"), 字符串, "重生"), -1)
       │      │      │    复活英雄: 读取局部变量("AA"), 0, 0, ShowHideShow
       │      │      │    设置局部变量:"D"=(读取局部变量("AA")的位置)
       │      │      │    平移镜头: 读取局部变量("WJ"), 读取局部变量("D"), 0
       │      │      │    清除点 读取局部变量("D")
       │      │      └─ 否则
       │      │           显示文本→读取局部变量("WJ"): 0
       │      └─ 否则
       │           显示文本→读取局部变量("WJ"): 0
       └─ 否则: (无)
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

### MZHZ 每帧绘制

```text
触发器: MZHZ 每帧绘制 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.01)
条件
  └─ 无
动作
  └─ DzFrameSetUpdateCallbackMultiple: GetLocalPlayer()
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

### SFJN 释放技能

```text
触发器: SFJN 释放技能 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_Hpal_0000 - UnitEventSpellEffect
条件
  └─ 无
动作
  └─ YDWEForLoopLocVarMultiple: "A", 1, 6
```

### -----------

```text
触发器: ----------- (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 护盾增加HD 002

```text
触发器: 护盾增加HD 002 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [单位类型.YX[1]."最大护盾"] = 100.00
  ├─ 保存数据到哈希表: [单位类型.YX[1]."当前护盾"] = 100.00
  ├─ 设置生命百分比: YX[1], 随机实数(10.00, 100.00)
  └─ 设置魔法百分比: YX[1], 随机实数(10.00, 100.00)
```

### -----------

```text
触发器: ----------- (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 伤害事件SH 003

```text
触发器: 伤害事件SH 003 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 无
动作
  ├─ ── 伤害事件和原生的吸血有冲突 ──
  ├─ 设置局部变量:"S"=伤害值()
  └─ 如果
       ├─ 条件: 从哈希表读取数据(单位类型, 触发单位(), "当前护盾") OperatorLessEq 读取局部变量("S")
       ├─ 则
       │    设置局部变量:"AA"=OperatorRealSubtract(读取局部变量("S"), 从哈希表读取数据(单位类型, 触发单位(), "当前护盾"))
       │    YDWESetEventDamage: 读取局部变量("AA")
       │    保存数据到哈希表: [单位类型.触发单位()."当前护盾"] = 0.00
       │    保存数据到哈希表: [单位类型.触发单位()."最大护盾"] = 0.00
       └─ 否则
            保存数据到哈希表: [单位类型.触发单位()."当前护盾"] = OperatorRealSubtract(从哈希表读取数据(单位类型, 触发单位(), "当前护盾"), 读取局部变量("S"))
            YDWESetEventDamage: 0.00
```

### -----------

```text
触发器: ----------- (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### -----------

```text
触发器: ----------- (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### YAOJI

```text
触发器: YAOJI (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "1"
条件
  └─ 无
动作
  ├─ KKWESetObjectTableData: 玩家, Player00, 字符串, "血瓶", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, Player00, 字符串, "血瓶"), 1)
  ├─ KKWESetObjectTableData: 玩家, Player00, 字符串, "蓝瓶", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, Player00, 字符串, "蓝瓶"), 1)
  └─ KKWESetObjectTableData: 玩家, Player00, 字符串, "重生", 整数, OperatorIntegerAdd(KKWEGetObjectTableData(玩家, Player00, 字符串, "重生"), 1)
```

### Q

```text
触发器: Q (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "Q"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A000
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A000
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 1, typename09_abilcode, A000
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[5], kzt\jn (7).tga, 0
       └─ 否则: (无)
```

### W

```text
触发器: W (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "W"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A003
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A003
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 2, typename09_abilcode, A003
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[6], kzt\jn (8).tga, 0
       └─ 否则: (无)
```

### E

```text
触发器: E (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "E"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A002
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A002
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 3, typename09_abilcode, A002
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[7], kzt\jn (9).tga, 0
       └─ 否则: (无)
```

### R

```text
触发器: R (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "R"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A001
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A001
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 4, typename09_abilcode, A001
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[8], kzt\jn (10).tga, 0
       └─ 否则: (无)
```

### D

```text
触发器: D (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "D"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A004
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A004
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 5, typename09_abilcode, A004
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[9], kzt\jn (11).tga, 0
       └─ 否则: (无)
```

### F

```text
触发器: F (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "F"
条件
  └─ 无
动作
  ├─ 添加技能: YX[1], A005
  ├─ UnitMakeAbilityPermanent: YX[1], OnOffOn, A005
  ├─ KKWESetObjectTableData: 玩家, Player00, 整数, 6, typename09_abilcode, A005
  └─ 如果
       ├─ 条件: Player00 == GetLocalPlayer()
       ├─ 则
       │    DzFrameSetTexture: KZT[10], kzt\jn (12).tga, 0
       └─ 否则: (无)
```

