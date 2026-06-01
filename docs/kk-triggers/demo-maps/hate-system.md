---
title: 仇恨系统 - 演示图实战
category: kk-triggers
slug: demo-maps/hate-system
description: 演示图 仇恨系统 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 仇恨系统 — 演示图实战

> 演示图：仇恨系统.w3x
>
> 触发器数：**24**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\仇恨系统.w3x`

## 📑 触发器目录

- 伤害阻断与复活
- Prevent
- Recover
- Comeback
- 添加
- GameStart
- 魔法书
- CHero1
- CHero2
- CUnit1
- DeleteAll
- TimeOn
- TimeOff
- CBuilding
- WhereAreYou
- 物品
- Item1
- Item2
- Item3
- Item4
- Item5
- 仇恨系统
- 设置
- 转变a

---

## 📜 触发器代码

### 伤害阻断与复活

```text
触发器: 伤害阻断与复活 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### Prevent

```text
触发器: Prevent (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位状态(UnitStateLife, 触发单位()) OperatorLess 伤害值()
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 设置无敌: 触发单位(), InvulnerabilityInvulnerable
  └─ 启动计时器: 创建计时器(), 0.00s (一次性)
```

### Recover

```text
触发器: Recover (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 单位在单位组中(触发单位(), Recover) == TRUE
       ├─ 则
       │    保存数据到哈希表: [单位类型.触发单位()."RecoverTime"] = 5.00
       │    添加 触发单位() → Recover
       │    启动计时器: 创建计时器(), 0.05s (循环)
       └─ 否则
            保存数据到哈希表: [单位类型.触发单位()."RecoverTime"] = 5.00
```

### Comeback

```text
触发器: Comeback (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 启动计时器: 创建计时器(), 3.50s (一次性)
```

### 添加

```text
触发器: 添加 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### GameStart

```text
触发器: "GameStart" (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 设置局部变量:"i"=区域内符合条件的单位(可用地图区域(), (布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true) 且 玩家比较((过滤单位()的所有者), OperatorEqualENE, Player00)))
  ├─ 单位组: 选取 读取局部变量("i") 中所有单位
  │    └─ UnitAddAbilityBJ: A006, 选取单位()
  ├─ 删除单位组 读取局部变量("i")
  ├─ SetPlayerAllianceStateBJ: Player00, 玩家2(蓝), AllianceSettingAlliedVision
  ├─ SetPlayerAllianceStateBJ: 玩家2(蓝), Player00, AllianceSettingAlliedVision
  ├─ SetPlayerAllianceStateBJ: Player00, 玩家1(红), AllianceSettingUnallied
  ├─ SetPlayerAllianceStateBJ: 玩家1(红), Player00, AllianceSettingUnallied
  ├─ 设置玩家属性: Player00, PlayerStateGold, 1000000
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  ├─ 迷雾遮罩开关: EnabledDisabledDisabled
  ├─ 设置 Buildings[1] = n000
  ├─ 设置 Buildings[2] = n001
  ├─ 设置 Buildings[3] = n003
  ├─ 设置 Buildings[4] = n002
  ├─ 设置 Buildings[5] = h002
  ├─ 设置 Buildings[6] = n004
  ├─ 设置 Buildings[7] = n005
  ├─ 设置 Buildings[8] = o000
  ├─ 设置 Buildings[9] = n006
  ├─ 设置 Buildings[10] = e000
  ├─ 设置 Buildings[11] = u000
  └─ 设置 Buildings[12] = u001
```

### 魔法书

```text
触发器: 魔法书 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### CHero1

```text
触发器: CHero1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"p"=技能目标点()
  ├─ 创建 1个|H000|→玩家1(红) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  ├─ 添加 bj_lastCreatedUnit → Create
  └─ 清除点 读取局部变量("p")
```

### CHero2

```text
触发器: CHero2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A001)
动作
  ├─ 设置局部变量:"p"=技能目标点()
  ├─ 创建 1个|H000|→玩家2(蓝) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  ├─ 添加 bj_lastCreatedUnit → Create
  └─ 清除点 读取局部变量("p")
```

### CUnit1

```text
触发器: CUnit1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A002)
动作
  ├─ 设置局部变量:"p"=技能目标点()
  ├─ 如果
  │    ├─ 条件: TeamUint == TRUE
  │    ├─ 则
  │    │    创建 1个|h001|→玩家1(红) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  │    │    添加 bj_lastCreatedUnit → Create
  │    │    设置 TeamUint = true
  │    └─ 否则
  │         创建 1个|h001|→玩家2(蓝) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  │         添加 bj_lastCreatedUnit → Create
  │         设置 TeamUint = false
  └─ 清除点 读取局部变量("p")
```

### DeleteAll

```text
触发器: DeleteAll (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A003)
动作
  └─ 单位组: 选取 Create 中所有单位
       ├─ 从单位组移除单位: 选取单位(), Create
       └─ 移除 选取单位()
```

### TimeOn

```text
触发器: TimeOn (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00K)
动作
  └─ UnitApplyTimedLife: 技能目标单位(), TimedLifeBuffCodeWaterElemental, 5.00
```

### TimeOff

```text
触发器: TimeOff (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00L)
动作
  └─ UnitPauseTimedLifeBJ: PauseUnpauseOptionPause, 技能目标单位()
```

### CBuilding

```text
触发器: CBuilding (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00J)
动作
  ├─ 设置局部变量:"p"=技能目标点()
  ├─ 设置局部变量:"m"=随机[1~11]
  ├─ 如果
  │    ├─ 条件: TeamBuilding == TRUE
  │    ├─ 则
  │    │    创建 1个|Buildings[读取局部变量("m")]|→玩家1(红) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  │    │    添加 bj_lastCreatedUnit → Create
  │    │    设置 TeamBuilding = true
  │    └─ 否则
  │         创建 1个|Buildings[读取局部变量("m")]|→玩家2(蓝) 在 读取局部变量("p") 面向GetRandomDirectionDeg()
  │         添加 bj_lastCreatedUnit → Create
  │         设置 TeamBuilding = false
  └─ 清除点 读取局部变量("p")
```

### WhereAreYou

```text
触发器: WhereAreYou (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00N)
动作
  ├─ 设置局部变量:"p"=技能目标点()
  ├─ 移动单位: 触发单位(), 读取局部变量("p")
  └─ 清除点 读取局部变量("p")
```

### 物品

```text
触发器: 物品 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### Item1

```text
触发器: Item1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00H)
动作
  └─ 添加物品: I000, 触发单位()
```

### Item2

```text
触发器: Item2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00B)
动作
  └─ 添加物品: I001, 触发单位()
```

### Item3

```text
触发器: Item3 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00E)
动作
  └─ 添加物品: I002, 触发单位()
```

### Item4

```text
触发器: Item4 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00F)
动作
  └─ 添加物品: I003, 触发单位()
```

### Item5

```text
触发器: Item5 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00G)
动作
  ├─ SetTimeOfDay: 6.00
  └─ SetTimeOfDayScalePercentBJ: 0
```

### 仇恨系统

```text
触发器: 仇恨系统 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 设置

```text
触发器: 设置 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"m"=区域内符合条件的单位(可用地图区域(), 单位类型比较((过滤单位()类型ID), OperatorEqualENE, hgtw))
  ├─ 循环整数A 1→(读取局部变量("m")中的单位数)
  │    ├─ 设置局部变量:"u"=单位组第一个单位(读取局部变量("m"))
  │    ├─ 从单位组移除单位: 读取局部变量("u"), 读取局部变量("m")
  │    ├─ 设置 Defend[循环整数A] = 读取局部变量("u")
  │    └─ 启动计时器: 创建计时器(), 0.01s (循环)
  └─ 删除单位组 读取局部变量("m")
```

### 转变a

```text
触发器: 转变a (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位类型判断(伤害来源(), 英雄) == TRUE
动作
  └─ 循环整数A 1→12
       └─ 如果
            ├─ 条件: 全部成立
            │    ├─ IsUnitInRange(伤害来源(), Defend[循环整数A], 900.00) == TRUE
            │    ├─ IsUnitAlly(触发单位(), (Defend[循环整数A]的所有者)) == TRUE
            ├─ 则
            │    设置 Attack[循环整数A] = 伤害来源()
            │    YDWEExitLoop
            └─ 否则: (无)
```

