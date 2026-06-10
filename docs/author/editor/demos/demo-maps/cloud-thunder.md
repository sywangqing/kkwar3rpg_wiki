---
title: 云彩打雷 - 演示图实战
category: kk-triggers
slug: demo-maps/cloud-thunder
description: 演示图 云彩打雷 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 云彩打雷 — 演示图实战

> 演示图：云彩打雷.w3x
>
> 触发器数：**2**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\云彩打雷.w3x`

## 📑 触发器目录

- 简介
- leiJi

---

## 📜 触发器代码

### 简介

```text
触发器: 简介 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ── 欢迎使用世界编辑器，开始你的地图创造之旅。 ──
  ├─ ── 你可以从https://reckfeng.com/获取最新编辑器咨询。 ──
  ├─ ── 当你的地图意外损坏时，你可以在backups目录找到你最近26次保存的地图。 ──
  └─ ── 任何疑问请加官方作者群：QQ433807374。 ──
```

### leiJi

```text
触发器: leiJi (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A000)
动作
  ├─ 设置局部变量:"chuFa"=触发单位()
  ├─ 设置局部变量:"muBiao"=技能目标单位()
  ├─ 设置局部变量:"maJia"=创建单位(指定坐标)(触发玩家(), e000, 单位X坐标(技能目标单位()), 单位Y坐标(技能目标单位()), 0.00)
  ├─ 设置局部变量:"shangHai"=(20.00 + (20.00 x (单位技能等级(触发单位(), A000)转实数)))
  ├─ YDWEAroundSystem: 读取局部变量("maJia"), 技能目标单位(), 0.00, 0.00, 0.00, 7.00, 0.03
  ├─ UnitApplyTimedLife: 读取局部变量("maJia"), TimedLifeBuffCodeWaterElemental, 6.50
  ├─ 单位发布命令(目标): 读取局部变量("maJia"), UnitOrderChainLightning, 读取局部变量("muBiao")
  ├─ 设置局部变量:"p"=(读取局部变量("maJia")的位置)
  ├─ 设置局部变量:"g"=范围内符合条件的单位(150.00, 读取局部变量("p"), (((布尔比较(单位类型判断(过滤单位(), 建筑), OperatorEqualENE, false) 且 布尔比较(单位类型判断(过滤单位(), UnitTypeMagicImmune), OperatorEqualENE, false)) 且 布尔比较(单位类型判断(过滤单位(), UnitTypeAncient), OperatorEqualENE, false)) 且 (布尔比较(单位类型判断(过滤单位(), UnitTypeMechanical), OperatorEqualENE, false) 且 (布尔比较(IsUnitAlly(过滤单位(), (读取局部变量("chuFa")的所有者)), OperatorEqualENE, false) 且 (布尔比较(单位类型判断(过滤单位(), UnitTypeDead), OperatorEqualENE, false) 且 整数比较(GetUnitPointValue(过滤单位()), !=, 999))))))
  ├─ 单位组: 选取 读取局部变量("g") 中所有单位
  │    ├─ 伤害: 读取局部变量("chuFa")→选取单位(): 读取局部变量("shangHai") (AttackTypeNormal/DamageTypeMagic)
  │    └─ 销毁特效 创建特效(附着单位)(Abilities\Weapons\Bolt\BoltImpact.mdl, 选取单位(), "origin")
  ├─ 清除点 读取局部变量("p")
  ├─ 删除单位组 读取局部变量("g")
  ├─ 启动计时器: 创建计时器(), 2.00s (一次性)
  ├─ 启动计时器: 创建计时器(), 4.00s (一次性)
  └─ 启动计时器: 创建计时器(), 6.00s (一次性)
```

