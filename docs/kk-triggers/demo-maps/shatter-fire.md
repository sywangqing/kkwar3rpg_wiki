---
title: 碎裂之火 - 演示图实战
category: kk-triggers
slug: demo-maps/shatter-fire
description: 演示图 碎裂之火 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 碎裂之火 — 演示图实战

> 演示图：10碎裂之火 (1).w3x
>
> 触发器数：**5**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\10碎裂之火 (1).w3x`

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
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  ├─ 迷雾遮罩开关: EnabledDisabledDisabled
  └─ 设置 NewHash = YDWEInitHashtable()
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"TempCaster"=GetSpellAbilityUnit()
  ├─ SaveUnitHandleBJ: 读取局部变量("TempCaster"), YDWEGetUnitID(读取局部变量("TempCaster")), 玩家号((读取局部变量("TempCaster")的所有者)), NewHash
  ├─ 设置局部变量:"TempPoint"=(读取局部变量("TempCaster")的位置)
  ├─ 设置局部变量:"TempPoint2"=技能目标点()
  └─ 启动计时器: 创建计时器(), 0.05s (循环)
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ (死亡单位()类型ID) == n000
动作
  ├─ 设置局部变量:"TempPoint"=(死亡单位()的位置)
  ├─ 设置局部变量:"TempNum"=50
  ├─ 设置局部变量:"TempUnitGroup"=范围内符合条件的单位(300.00, 读取局部变量("TempPoint"), (布尔比较(是敌方单位(过滤单位(), (死亡单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 单位组: 选取 读取局部变量("TempUnitGroup") 中所有单位
  │    └─ 伤害: LoadUnitHandleBJ(单位自定义值(死亡单位()), 玩家号((死亡单位()的所有者)), NewHash)→选取单位(): (读取局部变量("TempNum")转实数) (AttackTypeNormal/DamageTypeNormal)
  ├─ 删除单位组 读取局部变量("TempUnitGroup")
  ├─ 设置局部变量:"TempEffect"=创建特效(Environment\LargeBuildingFire\LargeBuildingFire0.mdl, 读取局部变量("TempPoint"))
  └─ 启动计时器: 创建计时器(), 0.50s (循环)
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "1"
条件
  └─ 无
动作
  ├─ SetPlayerAllianceStateBJ: Player00, 玩家1(红), AllianceSettingAllied
  ├─ SetPlayerAllianceStateBJ: 玩家1(红), Player00, AllianceSettingAllied
  ├─ 设置局部变量:"TempPoint"=(gg_unit_Hblm_0001的位置)
  ├─ 循环整数A 1→500
  │    ├─ 创建 1个|ogru|→玩家1(红) 在 读取局部变量("TempPoint") 面向GetRandomDirectionDeg()
  │    └─ SetUnitAcquireRangeBJ: 最后创建的单位(), 9999.00
  ├─ 清除点 读取局部变量("TempPoint")
  └─ 开启触发器 gg_trg____________________005
```

### 未命名触发器 005

```text
触发器: 未命名触发器 005 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ SetPlayerAllianceStateBJ: Player00, 玩家1(红), AllianceSettingUnallied
  └─ SetPlayerAllianceStateBJ: 玩家1(红), Player00, AllianceSettingUnallied
```

