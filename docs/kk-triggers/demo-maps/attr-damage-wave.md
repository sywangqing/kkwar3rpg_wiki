---
title: 属性伤害冲击波 - 演示图实战
category: kk-triggers
slug: demo-maps/attr-damage-wave
description: 演示图 属性伤害冲击波 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 属性伤害冲击波 — 演示图实战

> 演示图：属性伤害冲击波.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\属性伤害冲击波.w3x`

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
  ├─ 战争迷雾开关: EnabledDisabledDisabled
  └─ 迷雾遮罩开关: EnabledDisabledDisabled
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, AOsh)
  └─ 单位类型判断(GetSpellAbilityUnit(), 英雄) == TRUE
动作
  ├─ 设置局部变量:"d"=GetSpellAbilityUnit()
  ├─ ── 可以使用坐标就不要使用点，坐标不用排泄 ──
  ├─ 设置局部变量:"x"=单位X坐标(读取局部变量("d"))
  ├─ 设置局部变量:"y"=单位Y坐标(读取局部变量("d"))
  ├─ 设置局部变量:"x1"=GetSpellTargetX()
  ├─ 设置局部变量:"y1"=GetSpellTargetY()
  ├─ ── 设置属性伤害数值 ──
  ├─ 设置局部变量:"ll"=英雄属性(HeroStatStr, 读取局部变量("d"), InclusionInclude)
  ├─ 设置局部变量:"s"=((读取局部变量("ll")转实数) x 10.00)
  ├─ ── 创建马甲释放技能 ──
  ├─ 设置局部变量:"m"=创建单位(指定坐标)((读取局部变量("d")的所有者), ewsp, 读取局部变量("x"), 读取局部变量("y"), 0)
  ├─ UnitApplyTimedLife: 读取局部变量("m"), TimedLifeBuffCodeWaterElemental, 2.00
  ├─ 添加技能: 读取局部变量("m"), AOs2
  ├─ 命令 读取局部变量("m") → UnitOrderShockwave 到 读取局部变量("x1")
  ├─ ── 新建触发，赋予属性伤害 ──
  ├─ 设置局部变量:"cfq"=CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 读取局部变量("cfq")
  ├─ ── 逆天计时器清除创建的触发，这个时间是需要比冲击波飞行的时间长一点点。 ──
  └─ 启动计时器: 创建计时器(), 4.00s (一次性)
```

