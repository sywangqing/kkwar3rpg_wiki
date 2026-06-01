---
title: 小偷 - 演示图实战
category: kk-triggers
slug: demo-maps/thief
description: 演示图 小偷 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 小偷 — 演示图实战

> 演示图：小偷-胖虎出品！.w3x
>
> 触发器数：**1**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\小偷-胖虎出品！.w3x`

## 📑 触发器目录

- 未命名触发器 001

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.0000)
条件
  └─ 无
动作
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, Player00, FogStateVisible, gg_rct______________003
  ├─ 设置局部变量:"u"=创建单位(指定点)(Player00, nbrg, (区域gg_rct______________004中心), 0)
  ├─ SetUnitState: 读取局部变量("u"), UnitStateDamageCoolSec, 0.2000
  ├─ SetUnitState: 读取局部变量("u"), UnitStateDamageBaseSec, 25.0000
  ├─ SetUnitState: 读取局部变量("u"), UnitStateDamageRangeSec, 1000.0000
  ├─ 添加技能: 读取局部变量("u"), A001
  ├─ 添加技能: 读取局部变量("u"), A000
  └─ 启动计时器: 创建计时器(), 1.0000s (循环)
```

