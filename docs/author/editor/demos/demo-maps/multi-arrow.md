---
title: 多重箭追踪箭 - 演示图实战
category: kk-triggers
slug: demo-maps/multi-arrow
description: 演示图 多重箭追踪箭 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 多重箭追踪箭 — 演示图实战

> 演示图：多重箭追踪箭.w3x
>
> 触发器数：**8**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 未命名触发器 001
- 未命名触发器 003
- 多重箭
- 未命名触发器 004
- 追踪箭
- 未命名触发器 005
- 万箭齐发
- 未命名触发器 002

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.10)
条件
  └─ 无
动作
  └─ CreateFogModifierRectBJ: EnabledDisabledEnabled, Player00, FogStateVisible, 可用地图区域()
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.10)
条件
  └─ 无
动作
  └─ YDWEMemoryLeakHelperDisplayLeaks
```

### 多重箭

```text
触发器: 多重箭 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"dw"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"d"=(读取局部变量("dw")的位置)
  ├─ 设置局部变量:"d2"=技能目标点()
  ├─ 循环整数A -3→3
  │    ├─ 设置局部变量:"d3"=PolarProjectionBJ(读取局部变量("d"), 24.00, 角度叠加(AngleBetweenPoints(读取局部变量("d"), 读取局部变量("d2")), OperatorDegreeMultiply(10.00, (循环整数A转实数))))
  │    ├─ 创建 1个|hfoo|→(读取局部变量("dw")的所有者) 在 读取局部变量("d") 面向默认朝向
  │    ├─ 添加技能: bj_lastCreatedUnit, A004
  │    ├─ 命令 bj_lastCreatedUnit → UnitOrderCarrionSwarm 到 读取局部变量("d3")
  │    ├─ UnitApplyTimedLife: bj_lastCreatedUnit, TimedLifeBuffCodeGeneric, 2.00
  │    └─ 清除点 读取局部变量("d3")
  ├─ 清除点 读取局部变量("d")
  └─ 清除点 读取局部变量("d2")
```

### 追踪箭

```text
触发器: 追踪箭 (玩家/英雄) [注释] [✓]
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
触发器: 未命名触发器 005 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A003)
动作
  ├─ 设置局部变量:"dw"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"d"=(读取局部变量("dw")的位置)
  ├─ 设置局部变量:"d2"=技能目标点()
  ├─ 设置局部变量:"dwz2"=CreateGroup()
  ├─ 循环整数A -3→3
  │    ├─ 创建 1个|h000|→(读取局部变量("dw")的所有者) 在 读取局部变量("d") 面向角度叠加(AngleBetweenPoints(读取局部变量("d"), 读取局部变量("d2")), OperatorDegreeMultiply(10.00, (循环整数A转实数)))
  │    ├─ UnitApplyTimedLife: bj_lastCreatedUnit, TimedLifeBuffCodeGeneric, 3.00
  │    ├─ 添加 读取局部变量("dwz2") → bj_lastCreatedUnit
  │    └─ 保存数据到哈希表: [单位类型.bj_lastCreatedUnit."zs"] = 0
  ├─ 启动计时器: 创建计时器(), 0.03s (循环)
  ├─ 清除点 读取局部变量("d")
  └─ 清除点 读取局部变量("d2")
```

### 万箭齐发

```text
触发器: 万箭齐发 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A001)
动作
  ├─ 设置局部变量:"dw"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"d"=(读取局部变量("dw")的位置)
  ├─ 设置局部变量:"d2"=技能目标点()
  ├─ 设置局部变量:"dwz"=CreateGroup()
  ├─ 设置局部变量:"dwz3"=CreateGroup()
  ├─ 循环整数A -3→3
  │    ├─ 创建 1个|h000|→(读取局部变量("dw")的所有者) 在 读取局部变量("d") 面向角度叠加(AngleBetweenPoints(读取局部变量("d"), 读取局部变量("d2")), OperatorDegreeMultiply(10.00, (循环整数A转实数)))
  │    ├─ 设置局部变量:"dw2"=bj_lastCreatedUnit
  │    └─ 添加 读取局部变量("dwz") → 读取局部变量("dw2")
  └─ 启动计时器: 创建计时器(), 0.03s (循环)
```

