---
title: 火球环绕1 - 演示图实战
category: kk-triggers
slug: demo-maps/fireball-orbit-1
description: 演示图 火球环绕1 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 火球环绕1 — 演示图实战

> 演示图：火球环绕1.w3x
>
> 触发器数：**3**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 六颗火球904
- 大灾变908
- 小键盘up增加视角0001

---

## 📜 触发器代码

### 六颗火球904

```text
触发器: 六颗火球904 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"user"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"userpot"=(读取局部变量("user")的位置)
  ├─ 设置局部变量:"allball"=CreateGroup()
  ├─ 循环整数A 1→6
  │    ├─ YDWESetAnyTypeLocalArray: 单位类型, "ball", 循环整数A, 创建单位(指定点)(非玩家, e000, 读取局部变量("userpot"), 0)
  │    └─ 添加 读取局部变量("allball") → YDWEGetAnyTypeLocalArray("ball", 循环整数A)
  ├─ 清除点 读取局部变量("userpot")
  ├─ 设置局部变量:"go"=创建计时器()
  ├─ 启动计时器: 读取局部变量("go"), 0.03s (循环)
  ├─ 设置局部变量:"gogo"=创建计时器()
  └─ 启动计时器: 读取局部变量("gogo"), 3.00s (循环)
```

### 大灾变908

```text
触发器: 大灾变908 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A001)
动作
  ├─ 设置局部变量:"user"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"target_1"=技能目标单位()
  ├─ PauseUnit: 读取局部变量("user"), PauseUnpauseOptionPause
  ├─ 播放动画: 读取局部变量("user"), "walk"
  ├─ 设置局部变量:"height"=GetUnitFlyHeight(读取局部变量("user"))
  ├─ 设置局部变量:"dheight"=OperatorRealSubtract(1200.00, 读取局部变量("height"))
  ├─ 设置局部变量:"control_increase"=0.00
  ├─ 设置局部变量:"increase"=创建计时器()
  ├─ 设置局部变量:"increase_dtime"=0.03
  └─ 启动计时器: 读取局部变量("increase"), 读取局部变量("increase_dtime")s (循环)
```

### 小键盘up增加视角0001

```text
触发器: 小键盘up增加视角0001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerKeyEventBJ(PlayerALL, KeyEventTypeDepress, KeyEventKeyUp)
条件
  └─ 无
动作
  └─ SetCameraFieldForPlayer: 触发玩家(), CameraFieldZOffset, 900.00, 1.00
```

