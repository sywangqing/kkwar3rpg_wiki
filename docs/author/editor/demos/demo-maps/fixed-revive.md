---
title: 定点复活 - 演示图实战
category: kk-triggers
slug: demo-maps/fixed-revive
description: 演示图 定点复活 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 定点复活 — 演示图实战

> 演示图：定点复活.w3x
>
> 触发器数：**5**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\定点复活.w3x`

## 📑 触发器目录

- 未命名触发器 001
- 未命名触发器 002
- 未命名触发器 003
- 未命名触发器 004
- 未命名触发器 005

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 设置 HXB = YDWEInitHashtable()
  ├─ 运行计时器 T (循环, 1.00s)
  ├─ YDWESetLocalVariableInteger: "id", 自定义代码("'hfoo'")
  ├─ SaveInteger: HXB, YDWES2Id("ID"), 1, YDWEGetLocalVariableInteger("id")
  ├─ SaveInteger: HXB, YDWES2Id("SJ"), 1, 10
  ├─ YDWESetLocalVariableInteger: "id", 自定义代码("'hpea'")
  ├─ SaveInteger: HXB, YDWES2Id("ID"), 2, YDWEGetLocalVariableInteger("id")
  ├─ SaveInteger: HXB, YDWES2Id("SJ"), 2, 5
  ├─ YDWESetLocalVariableInteger: "id", 自定义代码("'hkni'")
  ├─ SaveInteger: HXB, YDWES2Id("ID"), 3, YDWEGetLocalVariableInteger("id")
  └─ SaveInteger: HXB, YDWES2Id("SJ"), 3, 2
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ YDWESetLocalVariableGroup: "dwz", 区域内全部单位(可用地图区域())
  ├─ 单位组: 选取 YDWEGetLocalVariableGroup("dwz") 中所有单位
  │    └─ 循环整数A 1→10000000
  │         └─ 如果
  │              ├─ 条件: LoadInteger(HXB, YDWES2Id("ID"), 循环整数A) OperatorGreater 0
  │              ├─ 则
  │              │    如果
  │              │      ├─ 条件: LoadInteger(HXB, YDWES2Id("ID"), 循环整数A) == YDWEGetUnitTypeID((选取单位()类型ID))
  │              │      ├─ 则
  │              │      │    SaveReal: HXB, YDWEGetUnitID(选取单位()), YDWES2Id("X"), 单位X坐标(选取单位())
  │              │      │    SaveReal: HXB, YDWEGetUnitID(选取单位()), YDWES2Id("Y"), 单位Y坐标(选取单位())
  │              │      │    YDWEExitLoop
  │              │      └─ 否则: (无)
  │              └─ 否则
  │                   YDWEExitLoop
  ├─ GroupClear: YDWEGetLocalVariableGroup("dwz")
  ├─ 删除单位组 YDWEGetLocalVariableGroup("dwz")
  └─ YDWELocalVariableEnd
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(可用地图区域())
条件
  └─ 无
动作
  └─ 循环整数A 1→10000000
       └─ 如果
            ├─ 条件: LoadInteger(HXB, YDWES2Id("ID"), 循环整数A) OperatorGreater 0
            ├─ 则
            │    如果
            │      ├─ 条件: LoadInteger(HXB, YDWES2Id("ID"), 循环整数A) == YDWEGetUnitTypeID((触发单位()类型ID))
            │      ├─ 则
            │      │    SaveReal: HXB, YDWEGetUnitID(触发单位()), YDWES2Id("X"), 单位X坐标(触发单位())
            │      │    SaveReal: HXB, YDWEGetUnitID(触发单位()), YDWES2Id("Y"), 单位Y坐标(触发单位())
            │      │    YDWEExitLoop
            │      └─ 否则: (无)
            └─ 否则
                 YDWEExitLoop
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 T 到期
条件
  └─ 无
动作
  ├─ YDWESetLocalVariableInteger: "tmax", LoadInteger(HXB, 0, YDWES2Id("MAX"))
  ├─ 如果
  │    ├─ 条件: YDWEGetLocalVariableInteger("tmax") OperatorGreater 0
  │    ├─ 则
  │    │    循环整数A 1→YDWEGetLocalVariableInteger("tmax")
  │    │      ├─ YDWESetLocalVariableInteger: "id", LoadInteger(HXB, 循环整数A, YDWES2Id("ID"))
  │    │      └─ 如果
  │    │           ├─ 条件: YDWEGetLocalVariableInteger("id") OperatorGreater 0
  │    │           ├─ 则
  │    │           │    YDWESetLocalVariableInteger: "sj", LoadInteger(HXB, 循环整数A, YDWES2Id("SJ"))
  │    │           │    YDWESetLocalVariableInteger: "sj", (YDWEGetLocalVariableInteger("sj") - 1)
  │    │           │    SaveInteger: HXB, 循环整数A, YDWES2Id("SJ"), YDWEGetLocalVariableInteger("sj")
  │    │           │    如果
  │    │           │      ├─ 条件: YDWEGetLocalVariableInteger("sj") OperatorLessEq 0
  │    │           │      ├─ 则
  │    │           │      │    YDWESetLocalVariableReal: "x", LoadReal(HXB, 循环整数A, YDWES2Id("X"))
  │    │           │      │    YDWESetLocalVariableReal: "y", LoadReal(HXB, 循环整数A, YDWES2Id("Y"))
  │    │           │      │    YDWESetLocalVariableInteger: "pid", LoadInteger(HXB, 循环整数A, YDWES2Id("PID"))
  │    │           │      │    YDWESetLocalVariableReal: "du", 随机实数(0, 360.00)
  │    │           │      │    YDWESetLocalVariableReal: "jl", 随机实数(0, 300.00)
  │    │           │      │    YDWESetLocalVariableReal: "cx", (YDWEGetLocalVariableReal("x") + (余弦(弧度转角度(YDWEGetLocalVariableReal("du"))) x YDWEGetLocalVariableReal("jl")))
  │    │           │      │    YDWESetLocalVariableReal: "cy", (YDWEGetLocalVariableReal("y") + (正弦(弧度转角度(YDWEGetLocalVariableReal("du"))) x YDWEGetLocalVariableReal("jl")))
  │    │           │      │    YDWESetLocalVariableUnit: "u", 创建单位(指定坐标)(玩家YDWEGetLocalVariableInteger("pid"), YDWEI2UnitId(YDWEGetLocalVariableInteger("id")), YDWEGetLocalVariableReal("cx"), YDWEGetLocalVariableReal("cy"), 0)
  │    │           │      │    YDWESetLocalVariableUnit: "u", UnitNull
  │    │           │      │    如果
  │    │           │      │      ├─ 条件: 循环整数A == YDWEGetLocalVariableInteger("tmax")
  │    │           │      │      ├─ 则
  │    │           │      │      │    FlushChildHashtable: HXB, 循环整数A
  │    │           │      │      └─ 否则
  │    │           │      │           YDWESetLocalVariableInteger: "tmax", LoadInteger(HXB, 0, YDWES2Id("MAX"))
  │    │           │      │           YDWESetLocalVariableInteger: "id", LoadInteger(HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("ID"))
  │    │           │      │           YDWESetLocalVariableInteger: "sj", LoadInteger(HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("SJ"))
  │    │           │      │           YDWESetLocalVariableReal: "x", LoadReal(HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("X"))
  │    │           │      │           YDWESetLocalVariableReal: "y", LoadReal(HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("Y"))
  │    │           │      │           YDWESetLocalVariableInteger: "pid", LoadInteger(HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("PID"))
  │    │           │      │           FlushChildHashtable: HXB, YDWEGetLocalVariableInteger("tmax")
  │    │           │      │           SaveInteger: HXB, 循环整数A, YDWES2Id("ID"), YDWEGetLocalVariableInteger("id")
  │    │           │      │           SaveInteger: HXB, 循环整数A, YDWES2Id("PID"), YDWEGetLocalVariableInteger("pid")
  │    │           │      │           SaveInteger: HXB, 循环整数A, YDWES2Id("SJ"), YDWEGetLocalVariableInteger("sj")
  │    │           │      │           SaveReal: HXB, 循环整数A, YDWES2Id("X"), YDWEGetLocalVariableReal("x")
  │    │           │      │           SaveReal: HXB, 循环整数A, YDWES2Id("Y"), YDWEGetLocalVariableReal("y")
  │    │           │      │           CustomScriptCode: "set bj_forLoopAIndex = bj_forLoopAIndex - 1"
  │    │           │      │    YDWESetLocalVariableInteger: "tmax", LoadInteger(HXB, 0, YDWES2Id("MAX"))
  │    │           │      │    YDWESetLocalVariableInteger: "tmax", (YDWEGetLocalVariableInteger("tmax") - 1)
  │    │           │      │    SaveInteger: HXB, 0, YDWES2Id("MAX"), YDWEGetLocalVariableInteger("tmax")
  │    │           │      └─ 否则: (无)
  │    │           └─ 否则
  │    │                YDWEExitLoop
  │    └─ 否则: (无)
  └─ YDWELocalVariableEnd
```

### 未命名触发器 005

```text
触发器: 未命名触发器 005 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  └─ 循环整数A 1→100000
       ├─ YDWESetLocalVariableInteger: "id", LoadInteger(HXB, YDWES2Id("ID"), 循环整数A)
       └─ 如果
            ├─ 条件: YDWEGetLocalVariableInteger("id") OperatorGreaterEq 0
            ├─ 则
            │    如果
            │      ├─ 条件: YDWEConverUnitcodeToInt((触发单位()类型ID)) == YDWEGetLocalVariableInteger("id")
            │      ├─ 则
            │      │    YDWESetLocalVariableInteger: "sj", LoadInteger(HXB, YDWES2Id("SJ"), 循环整数A)
            │      │    YDWESetLocalVariableReal: "x", LoadReal(HXB, YDWEGetUnitID(触发单位()), YDWES2Id("X"))
            │      │    YDWESetLocalVariableReal: "y", LoadReal(HXB, YDWEGetUnitID(触发单位()), YDWES2Id("Y"))
            │      │    FlushChildHashtable: HXB, YDWEGetUnitID(触发单位())
            │      │    YDWESetLocalVariableInteger: "tmax", LoadInteger(HXB, 0, YDWES2Id("MAX"))
            │      │    YDWESetLocalVariableInteger: "tmax", (YDWEGetLocalVariableInteger("tmax") + 1)
            │      │    SaveInteger: HXB, 0, YDWES2Id("MAX"), YDWEGetLocalVariableInteger("tmax")
            │      │    SaveInteger: HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("ID"), YDWEConverUnitcodeToInt((触发单位()类型ID))
            │      │    SaveInteger: HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("PID"), 玩家号((触发单位()的所有者))
            │      │    SaveInteger: HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("SJ"), YDWEGetLocalVariableInteger("sj")
            │      │    SaveReal: HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("X"), YDWEGetLocalVariableReal("x")
            │      │    SaveReal: HXB, YDWEGetLocalVariableInteger("tmax"), YDWES2Id("Y"), YDWEGetLocalVariableReal("y")
            │      │    YDWEExitLoop
            │      └─ 否则: (无)
            └─ 否则
                 YDWEExitLoop
```

