---
title: 神墓305 - 演示图实战
category: kk-triggers
slug: demo-maps/shenmu-305
description: 演示图 神墓305 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 神墓305 — 演示图实战

> 演示图：神墓305.w3x
>
> 触发器数：**158**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 伤害注册
- A18
- 死亡
- A12
- 被召唤
- A11
- 学习技能
- A9
- 接受伤害
- A5
- A1
- 被攻击
- A2
- A01
- A22
- A27
- 咫尺天涯
- A36
- 发动技能
- A3
- 停止技能
- A4
- A35RH0
- A34MRY
- A33HMXL
- A32SB
- 乾坤刺
- A39
- A38
- 蕾帝
- A37FBZL
- A34YM
- A30WD
- 蒙羽仙
- A28CH
- A291
- A292
- A293
- A294
- 寒涟漪
- A23SDXX
- A25
- A25 复制
- A25 复制 2
- A26
- A24BZTL
- 人皇
- RH3
- 苍龙
- A21
- 狂魔
- A15
- 属性
- A8
- A10
- 龙神
- A13
- 天地囚笼
- A19
- 剑尊
- JZ0
- 空间之刃
- A20
- B1
- B2
- 英雄选择
- C2
- 英雄回城
- C3
- C10
- 英雄复活
- C4
- C7
- 钱木
- C5
- 等级提升
- C6
- D1
- D2
- D11
- D12
- 升级基地
- D3
- 初级装备升级
- D4
- 进入各种地点
- 未命名触发器 017
- 中级武器升级
- 未命名触发器 022
- 装备合成
- 未命名触发器 023
- 物品叠加
- 未命名触发器 003
- 使用物品
- 未命名触发器 007
- 初始单位
- E1
- 刷兵
- E2
- 计时器
- E3
- E4
- E5
- E6
- 练级房和刷钱木
- E7
- E8
- E9
- E15
- E10
- 野兽
- E11
- 宝石掉落
- E12
- 死亡复活
- E13
- E14
- 失败
- 未命名触发器 010
- 胜利
- 未命名触发器 027
- 未命名触发器 021
- 未命名触发器 005
- 基地生命提示
- 未命名触发器 030
- 难度选择
- 未命名触发器 035
- 未命名触发器 036
- 玩家离开
- 未命名触发器 038
- 未命名触发器 020
- 未命名触发器 018
- 未命名触发器 016
- 未命名触发器 049
- 未命名触发器 053
- 未命名触发器 052
- 未命名触发器 051
- 未命名触发器 002
- 毁灭前夕
- 未命名触发器 006
- 未命名触发器 006 复制
- 未命名触发器 001
- 隐尘
- 未命名触发器 046
- 半神之力
- 未命名触发器 008
- 霜寒淬
- 未命名触发器 024
- 未命名触发器 011
- 远古
- 未命名触发器 013
- 未命名触发器 014
- 未命名触发器 012
- 未命名触发器 056
- 未命名触发器 070
- 001
- 未命名触发器 004
- 未命名触发器 009

---

## 📜 触发器代码

### 伤害注册

```text
触发器: 伤害注册 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A18

```text
触发器: A18 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(可用地图区域())
条件
  └─ 无
动作
  ├─ 添加事件到 gg_trg_A1: 注册单位事件(触发单位(), UnitEventDamaged)
  └─ 添加事件到 gg_trg_A5: 注册单位事件(触发单位(), UnitEventDamaged)
```

### 死亡

```text
触发器: 死亡 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A12

```text
触发器: A12 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │    ├─ 单位持有物品类型(凶手单位(), I03J) == TRUE
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(凶手单位(), I03J)) OperatorGreaterEq 500
  │    │      ├─ 则
  │    │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatStr: ModifyMethodAdd350
  │    │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd350
  │    │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatInt: ModifyMethodAdd350
  │    │      │    SetItemCharges: 单位携带物品(按类型)(凶手单位(), I03J), 0
  │    │      └─ 否则
  │    │           SetItemCharges: 单位携带物品(按类型)(凶手单位(), I03J), (物品剩余使用次数(单位携带物品(按类型)(凶手单位(), I03J)) + 1)
  │    └─ 否则
  │         如果
  │           ├─ 条件: 全部成立
  │           │    ├─ 单位持有物品类型(凶手单位(), I038) == TRUE
  │           │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │           ├─ 则
  │           │    如果
  │           │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(凶手单位(), I038)) OperatorGreaterEq 500
  │           │      ├─ 则
  │           │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatStr: ModifyMethodAdd200
  │           │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd250
  │           │      │    修改 YX_7[玩家号((凶手单位()的所有者))] 的HeroStatInt: ModifyMethodAdd300
  │           │      │    SetItemCharges: 单位携带物品(按类型)(凶手单位(), I038), 0
  │           │      └─ 否则
  │           │           SetItemCharges: 单位携带物品(按类型)(凶手单位(), I038), (物品剩余使用次数(单位携带物品(按类型)(凶手单位(), I038)) + 1)
  │           └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 随机[1~15] == 5
  │    │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │    ├─ 英雄属性(HeroStatInt, 凶手单位(), InclusionExclude) OperatorLess 50000
  │    ├─ 则
  │    │    循环整数A 1→5
  │    │      └─ 如果
  │    │           ├─ 条件: 单位持有物品类型(凶手单位(), WP_SYMJ[循环整数A()]) == TRUE
  │    │           ├─ 则
  │    │           │    单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00F, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderAttackUnit, 凶手单位()
  │    │           │    CustomScriptCode: ScriptCode00
  │    │           └─ 否则: (无)
  │    └─ 否则
  │         如果
  │           ├─ 条件: 全部成立
  │           │    ├─ 随机[21~35] == 24
  │           │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │           │    ├─ 英雄属性(HeroStatStr, 凶手单位(), InclusionExclude) OperatorLess 50000
  │           ├─ 则
  │           │    循环整数A 1→5
  │           │      └─ 如果
  │           │           ├─ 条件: 单位持有物品类型(凶手单位(), WP_SHC[循环整数A()]) == TRUE
  │           │           ├─ 则
  │           │           │    单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00D, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderAttackUnit, 凶手单位()
  │           │           │    CustomScriptCode: ScriptCode00
  │           │           └─ 否则: (无)
  │           └─ 否则
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 随机[15~29] == 20
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 英雄属性(HeroStatAgi, 凶手单位(), InclusionExclude) OperatorLess 50000
  │                  ├─ 则
  │                  │    循环整数A 1→5
  │                  │      └─ 如果
  │                  │           ├─ 条件: 单位持有物品类型(凶手单位(), WP_SY[循环整数A()]) == TRUE
  │                  │           ├─ 则
  │                  │           │    单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00E, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderAttackUnit, 凶手单位()
  │                  │           │    CustomScriptCode: ScriptCode00
  │                  │           └─ 否则: (无)
  │                  └─ 否则
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 随机[31~45] == 36
  │                         │    ├─ 单位持有物品类型(凶手单位(), I03M) == TRUE
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 英雄属性(HeroStatInt, 凶手单位(), InclusionExclude) OperatorLess 80000
  │                         │    ├─ 英雄属性(HeroStatAgi, 凶手单位(), InclusionExclude) OperatorLess 80000
  │                         │    ├─ 英雄属性(HeroStatAgi, 凶手单位(), InclusionExclude) OperatorLess 80000
  │                         ├─ 则
  │                         │    单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00G, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderAttackUnit, 凶手单位()
  │                         └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │    ├─ 单位技能等级(触发单位(), A00F) == 1
  │    ├─ 则
  │    │    设置 X_dian = (触发单位()的位置)
  │    │    命令 创建单位(指定坐标)((触发单位()的所有者), e00C, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0) → UnitOrderDeathAndDecay 到 X_dian
  │    │    清除点 X_dian
  │    └─ 否则
  │         如果
  │           ├─ 条件: 触发单位() == DSYY_DW
  │           ├─ 则
  │           │    设置无敌: YX_7[玩家号((触发单位()的所有者))], InvulnerabilityVulnerable
  │           └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 随机[1~40] == 7
  │    │    ├─ (触发单位()的所有者) == 玩家6(橙)
  │    ├─ 则
  │    │    移动物品到坐标: 创建物品(指定坐标)(I02R, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 单位在单位组中(触发单位(), MRY_DW) == TRUE
  │    ├─ 则
  │    │    从单位组移除单位: 触发单位(), MRY_DW
  │    │    移除 触发单位()
  │    └─ 否则
  │         如果
  │           ├─ 条件: 单位在单位组中(触发单位(), RH1) == TRUE
  │           ├─ 则
  │           │    从单位组移除单位: 触发单位(), RH1
  │           └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
       │    ├─ 单位技能等级(触发单位(), A01A) == 1
       │    ├─ HB_5[玩家号((触发单位()的所有者))] == UnitNull
       ├─ 则
       │    设置 X_dian = (触发单位()的位置)
       │    设置 HB_5[玩家号((触发单位()的所有者))] = 创建单位(指定坐标)((触发单位()的所有者), e00V, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
       │    SetUnitVertexColorBJ: HB_5[玩家号((触发单位()的所有者))], 100, 100, 100, 50.00
       │    销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\NightElf\NEDeathSmall\NEDeathSmall.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
       │    循环整数A 1→10
       │      ├─  CreateUnit: (触发单位()的所有者), e00Q, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), (36.00 x (循环整数A()转实数))
       │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 356.00, (36.00 x (循环整数A()转实数)))
       │      ├─ 销毁特效 创建特效(Abilities\Spells\Undead\FrostNova\FrostNovaTarget.mdl, X_dian2)
       │      └─ 清除点 X_dian2
       │    清除点 X_dian
       │    开启触发器 gg_trg_A24BZTL
       └─ 否则
            如果
              ├─ 条件: (触发单位()类型ID) == e00V
              ├─ 则
              │    销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\NightElf\NEDeathSmall\NEDeathSmall.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
              │    设置 HB_5[玩家号((触发单位()的所有者))] = UnitNull
              └─ 否则: (无)
```

### 被召唤

```text
触发器: 被召唤 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A11

```text
触发器: A11 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSummoned
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ (触发单位()类型ID) == H007
       │    ├─ 单位有魔法效果(触发单位(), B00F) == TRUE
       ├─ 则
       │    设置 DSYY_DW = 触发单位()
       │    设置无敌: GetSummoningUnit(), InvulnerabilityInvulnerable
       └─ 否则
            如果
              ├─ 条件: (触发单位()类型ID) == n005
              ├─ 则
              │    如果
              │      ├─ 条件: DYH == UnitNull
              │      ├─ 则
              │      │    设置 DYH = 触发单位()
              │      └─ 否则
              │           移除 DYH
              │           设置 DYH = 触发单位()
              └─ 否则: (无)
```

### 学习技能

```text
触发器: 学习技能 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A9

```text
触发器: A9 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A00J)
       ├─ 则
       │    开启触发器 gg_trg_A21
       └─ 否则
            如果
              ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A03B)
              ├─ 则
              │    开启触发器 gg_trg_A13
              └─ 否则
                   如果
                     ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A03K)
                     ├─ 则
                     │    开启触发器 gg_trg_RH3
                     └─ 否则
                          如果
                            ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A06L)
                            ├─ 则
                            │    开启触发器 gg_trg_A23SDXX
                            └─ 否则
                                 如果
                                   ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A06S)
                                   ├─ 则
                                   │    添加事件到 gg_trg_A25: 注册单位事件(触发单位(), UnitEventIssueUnitOrder)
                                   │    添加事件到 gg_trg_A25_______u: 注册单位事件(触发单位(), UnitEventIssuePointOrder)
                                   │    添加事件到 gg_trg_A25________2: 注册单位事件(触发单位(), UnitEventIssueOrder)
                                   │    设置 YLL_DW[玩家号((触发单位()的所有者))] = 创建单位(指定坐标)((触发单位()的所有者), u004, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
                                   │    开启触发器 gg_trg_A25
                                   │    开启触发器 gg_trg_A25________2
                                   │    开启触发器 gg_trg_A25_______u
                                   │    开启触发器 gg_trg_A26
                                   └─ 否则
                                        如果
                                          ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A06W)
                                          ├─ 则
                                          │    循环整数A 1→5
                                          │      ├─ 设置 HJZL_DW[循环整数A()] = 创建单位(指定坐标)((触发单位()的所有者), e00R, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
                                          │      ├─ SetUnitVertexColorBJ: HJZL_DW[循环整数A()], 100, 100, 100, 60.00
                                          │      └─ AddSpecialEffectTargetUnitBJ: "chest", HJZL_DW[循环整数A()], war3mapImported\angelwing.mdx
                                          │    添加事件到 gg_trg_A291: 注册单位事件(触发单位(), UnitEventIssueUnitOrder)
                                          │    添加事件到 gg_trg_A292: 注册单位事件(触发单位(), UnitEventIssueOrder)
                                          │    添加事件到 gg_trg_A293: 注册单位事件(触发单位(), UnitEventIssuePointOrder)
                                          │    开启触发器 gg_trg_A291
                                          │    开启触发器 gg_trg_A292
                                          │    开启触发器 gg_trg_A293
                                          │    开启触发器 gg_trg_A294
                                          │    单位发布命令(立即): 触发单位(), UnitOrderStop
                                          └─ 否则
                                               如果
                                                 ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A077)
                                                 ├─ 则
                                                 │    运行计时器 YM_jsq (一次性, 15.00s)
                                                 └─ 否则: (无)
```

### 接受伤害

```text
触发器: 接受伤害 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A5

```text
触发器: A5 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 伤害值() != 0.00
  ├─ 单位技能等级(伤害来源(), Aloc) == 1
  └─ 是敌方单位(触发单位(), (伤害来源()的所有者)) == TRUE
动作
  ├─ 设置 X_DW = YX_7[玩家号((伤害来源()的所有者))]
  └─ 如果
       ├─ 条件: (伤害来源()类型ID) == e002
       ├─ 则
       │    伤害目标: X_DW, 触发单位(), ((1 + ((英雄等级(X_DW)转实数) x 0.05)) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       └─ 否则
            如果
              ├─ 条件: (伤害来源()类型ID) == e004
              ├─ 则
              │    伤害目标: X_DW, 触发单位(), ((1 + ((英雄等级(X_DW)转实数) x 0.10)) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
              └─ 否则
                   如果
                     ├─ 条件: (伤害来源()类型ID) == e005
                     ├─ 则
                     │    伤害目标: X_DW, 触发单位(), ((0.04 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                     └─ 否则
                          如果
                            ├─ 条件: (伤害来源()类型ID) == e006
                            ├─ 则
                            │    伤害目标: X_DW, 触发单位(), ((英雄等级(X_DW)转实数) x (0.10 x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数))), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                            └─ 否则
                                 如果
                                   ├─ 条件: (伤害来源()类型ID) == e007
                                   ├─ 则
                                   │    销毁特效 创建特效(附着单位)(Abilities\Spells\Undead\FrostNova\FrostNovaTarget.mdl, 触发单位(), "origin")
                                   │    伤害目标: X_DW, 触发单位(), ((1 + (0.20 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                   └─ 否则
                                        如果
                                          ├─ 条件: (伤害来源()类型ID) == u002
                                          ├─ 则
                                          │    设置 X_dian = (X_DW的位置)
                                          │    设置 X_zs = 实数转整数(单位状态(UnitStateMaxLife, X_DW))
                                          │    伤害目标: X_DW, 触发单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                          │    CreateTextTagLocBJ: (X_zs转字符串), X_dian, 0, 10, 0.00, 0.00, 0.00, 0
                                          │    TriggerExecute: gg_trg_001
                                          │    清除点 X_dian
                                          └─ 否则
                                               如果
                                                 ├─ 条件: (伤害来源()类型ID) == e003
                                                 ├─ 则
                                                 │    伤害目标: X_DW, 触发单位(), ((1 + (0.10 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: (伤害来源()类型ID) == e00O
                                                        ├─ 则
                                                        │    伤害目标: X_DW, 触发单位(), ((1 + (0.06 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: (伤害来源()类型ID) == u004
                                                               ├─ 则
                                                               │    伤害目标: X_DW, 触发单位(), ((1 + (0.05 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: (伤害来源()类型ID) == e00R
                                                                      ├─ 则
                                                                      │    伤害目标: X_DW, 触发单位(), ((0.04 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                      └─ 否则
                                                                           如果
                                                                             ├─ 条件: (伤害来源()类型ID) == e00S
                                                                             ├─ 则
                                                                             │    伤害目标: X_DW, 触发单位(), ((1 + (0.04 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                             └─ 否则
                                                                                  如果
                                                                                    ├─ 条件: (伤害来源()类型ID) == e00T
                                                                                    ├─ 则
                                                                                    │    销毁特效 创建特效(附着单位)(Abilities\Weapons\Bolt\BoltImpact.mdl, 触发单位(), "origin")
                                                                                    │    伤害目标: X_DW, 触发单位(), ((1 + (0.20 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                    └─ 否则
                                                                                         如果
                                                                                           ├─ 条件: (伤害来源()类型ID) == u006
                                                                                           ├─ 则
                                                                                           │    伤害目标: X_DW, 触发单位(), ((0.05 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                           └─ 否则
                                                                                                如果
                                                                                                  ├─ 条件: (伤害来源()类型ID) == e00U
                                                                                                  ├─ 则
                                                                                                  │    伤害目标: X_DW, 触发单位(), ((1 + (0.03 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatInt, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                                  └─ 否则
                                                                                                       如果
                                                                                                         ├─ 条件: (伤害来源()类型ID) == e00W
                                                                                                         ├─ 则
                                                                                                         │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Stampede\StampedeMissileDeath.mdl, 触发单位(), "chest")
                                                                                                         │    伤害目标: X_DW, 触发单位(), (10000.00 x (英雄等级(X_DW)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                                         └─ 否则
                                                                                                              如果
                                                                                                                ├─ 条件: (伤害来源()类型ID) == e00P
                                                                                                                ├─ 则
                                                                                                                │    伤害目标: X_DW, 触发单位(), ((0.04 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                                                └─ 否则
                                                                                                                     如果
                                                                                                                       ├─ 条件: (伤害来源()类型ID) == e00I
                                                                                                                       ├─ 则
                                                                                                                       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Incinerate\FireLordDeathExplode.mdl, 触发单位(), "chest")
                                                                                                                       │    伤害目标: X_DW, 触发单位(), ((1 + (0.06 x (英雄等级(X_DW)转实数))) x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                                                       └─ 否则: (无)
```

### A1

```text
触发器: A1 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 伤害值() != 0.00
  ├─ 是敌方单位(触发单位(), (伤害来源()的所有者)) == TRUE
  └─ 单位技能等级(伤害来源(), Aloc) != 1
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(触发单位(), A077) == 1
  │    │    ├─ YM_ZJ == TRUE
  │    │    ├─ 伤害值() OperatorGreaterEq 单位状态(UnitStateLife, 触发单位())
  │    ├─ 则
  │    │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
  │    │    循环整数A 1→5
  │    │      └─ 如果
  │    │           ├─ 条件: wudi[循环整数A()] == UnitNull
  │    │           ├─ 则
  │    │           │    设置 wudi[循环整数A()] = 触发单位()
  │    │           │    运行计时器 wudi_JSQ[循环整数A()] (一次性, 0.00s)
  │    │           │    CustomScriptCode: ScriptCode00
  │    │           └─ 否则: (无)
  │    │    设置生命百分比: 触发单位(), 100
  │    └─ 否则
  │         如果
  │           ├─ 条件: 全部成立
  │           │    ├─ 单位持有物品类型(触发单位(), I02Z) == TRUE
  │           │    ├─ 伤害值() OperatorGreaterEq 单位状态(触发单位(), UnitStateLife)
  │           │    ├─ 随机[1~4] == 2
  │           ├─ 则
  │           │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
  │           │    销毁特效 创建特效(指定坐标)(Abilities\Spells\NightElf\BattleRoar\RoarCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │           │    循环整数A 1→5
  │           │      └─ 如果
  │           │           ├─ 条件: wudi[循环整数A()] == UnitNull
  │           │           ├─ 则
  │           │           │    设置 wudi[循环整数A()] = 触发单位()
  │           │           │    运行计时器 wudi_JSQ[循环整数A()] (一次性, 0.00s)
  │           │           │    CustomScriptCode: ScriptCode00
  │           │           └─ 否则: (无)
  │           │    设置生命百分比: 触发单位(), 100
  │           └─ 否则
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 伤害值() OperatorGreaterEq (单位状态(UnitStateMaxLife, 触发单位()) / 10.00)
  │                  │    ├─ 单位技能等级(触发单位(), A06Y) == 1
  │                  │    ├─ YHFS OperatorGreater 0
  │                  ├─ 则
  │                  │    设置 YHFS = (YHFS - 1)
  │                  │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
  │                  │    循环整数A 1→5
  │                  │      └─ 如果
  │                  │           ├─ 条件: wudi[循环整数A()] == UnitNull
  │                  │           ├─ 则
  │                  │           │    设置 wudi[循环整数A()] = 触发单位()
  │                  │           │    运行计时器 wudi_JSQ[循环整数A()] (一次性, 0.00s)
  │                  │           │    CustomScriptCode: ScriptCode00
  │                  │           └─ 否则: (无)
  │                  └─ 否则
  │                       如果
  │                         ├─ 条件: 单位技能等级(触发单位(), A00M) == 1
  │                         ├─ 则
  │                         │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + (3.00 x (GetHeroStr(触发单位(), InclusionInclude)转实数)))
  │                         └─ 否则
  │                              如果
  │                                ├─ 条件: 全部成立
  │                                │    ├─ 单位技能等级(触发单位(), A005) == 1
  │                                │    ├─ 伤害值() OperatorLessEq (单位状态(触发单位(), UnitStateMaxLife) x 0.05)
  │                                ├─ 则
  │                                │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │                                └─ 否则
  │                                     如果
  │                                       ├─ 条件: 单位技能等级(触发单位(), S000) == 1
  │                                       ├─ 则
  │                                       │    SetUnitLifeBJ: 触发单位(), (单位状态(UnitStateLife, 触发单位()) + (100.00 x (英雄等级(触发单位())转实数)))
  │                                       └─ 否则
  │                                            如果
  │                                              ├─ 条件: 单位有魔法效果(触发单位(), B00Y) == TRUE
  │                                              ├─ 则
  │                                              │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + (0.35 x 伤害值()))
  │                                              └─ 否则
  │                                                   如果
  │                                                     ├─ 条件: 全部成立
  │                                                     │    ├─ 单位状态(UnitStateLife, 触发单位()) OperatorGreaterEq (伤害值() x 0.35)
  │                                                     │    ├─ 单位有魔法效果(触发单位(), B00Q) == TRUE
  │                                                     ├─ 则
  │                                                     │    SetUnitLifeBJ: 触发单位(), (单位状态(UnitStateLife, 触发单位()) - (伤害值() x 0.35))
  │                                                     └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位有魔法效果(触发单位(), BOww) == TRUE
       │    ├─ 伤害值() OperatorLessEq 1.00
       ├─ 则
       │    如果
       │      ├─ 条件: (伤害来源()类型ID) == N000
       │      ├─ 则
       │      │    设置 X_zs = 实数转整数(((0.15 x (英雄等级(伤害来源())转实数)) x (英雄属性(HeroStatAgi, 伤害来源(), InclusionInclude)转实数)))
       │      │    伤害目标: 伤害来源(), 触发单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       │      │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Stampede\StampedeMissileDeath.mdl, 触发单位(), "overhead")
       │      └─ 否则
       │           设置 X_zs = 实数转整数(((0.10 x (英雄属性(HeroStatAgi, 伤害来源(), InclusionInclude)转实数)) x (英雄等级(伤害来源())转实数)))
       │           伤害目标: 伤害来源(), 触发单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       │           销毁特效 创建特效(附着单位)(Objects\Spawnmodels\Human\HumanBlood\BloodElfSpellThiefBlood.mdl, 触发单位(), "chest")
       └─ 否则
            设置 X_DW = YX_7[玩家号((伤害来源()的所有者))]
            如果
              ├─ 条件: 单位有魔法效果(触发单位(), B00Z) == TRUE
              ├─ 则
              │    UnitRemoveBuffBJ: B00Z, 触发单位()
              │    添加物品: I001, 伤害来源()
              │    销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\Human\HumanBlood\BloodElfSpellThiefBlood.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
              │    设置 X_zs = 实数转整数(((0.30 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatAgi, X_DW, InclusionInclude)转实数)))
              │    设置 X_dian = (伤害来源()的位置)
              │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 0.00, 0
              │    TriggerExecute: gg_trg_001
              │    清除点 X_dian
              │    伤害目标: 伤害来源(), 触发单位(), (X_zs转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
              └─ 否则
                   如果
                     ├─ 条件: 单位有魔法效果(触发单位(), B005) == TRUE
                     ├─ 则
                     │    UnitRemoveBuffBJ: B005, 触发单位()
                     │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 触发单位(), "origin")
                     │    设置 X_dian = (伤害来源()的位置)
                     │    设置 X_zs = 实数转整数((90.00 x (英雄属性(HeroStatAgi, X_DW, InclusionInclude)转实数)))
                     │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 0.00, 0
                     │    TriggerExecute: gg_trg_001
                     │    伤害目标: 伤害来源(), 触发单位(), (X_zs转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                     │    清除点 X_dian
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 单位技能等级(伤害来源(), A00L) == 1
                            │    ├─ 单位有魔法效果(触发单位(), B00R) == TRUE
                            ├─ 则
                            │    UnitRemoveBuffBJ: B00R, 触发单位()
                            │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
                            │    设置 X_dian = (伤害来源()的位置)
                            │    设置 X_zs = 实数转整数(((((单位技能等级(伤害来源(), A001) x 20) - 5)转实数) x (英雄属性(HeroStatAgi, X_DW, InclusionInclude)转实数)))
                            │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 0.00, 0
                            │    TriggerExecute: gg_trg_001
                            │    设置 X_danweizu = 范围内符合条件的单位(375.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (伤害来源()的所有者)), OperatorEqualENE, true))
                            │    清除点 X_dian
                            │    单位组: 选取 X_danweizu 中所有单位
                            │      └─ 伤害目标: 伤害来源(), 选取单位(), (X_zs转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                            │    删除单位组 X_danweizu
                            └─ 否则
                                 如果
                                   ├─ 条件: 单位有魔法效果(触发单位(), B00U) == TRUE
                                   ├─ 则
                                   │    UnitRemoveBuffBJ: B00U, 触发单位()
                                   │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
                                   │    设置 X_dian = (伤害来源()的位置)
                                   │    设置 X_zs = (5 x (英雄属性(HeroStatStr, 伤害来源(), InclusionInclude) + (英雄属性(HeroStatAgi, 伤害来源(), InclusionInclude) + 英雄属性(HeroStatInt, 伤害来源(), InclusionInclude))))
                                   │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 80.00, 0
                                   │    清除点 X_dian
                                   │    TriggerExecute: gg_trg_001
                                   │    设置 X_dian = (触发单位()的位置)
                                   │    设置 X_danweizu = 范围内符合条件的单位(375.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (伤害来源()的所有者)), OperatorEqualENE, true))
                                   │    清除点 X_dian
                                   │    单位组: 选取 X_danweizu 中所有单位
                                   │      └─ 伤害目标: 伤害来源(), 选取单位(), (X_zs转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                   │    删除单位组 X_danweizu
                                   └─ 否则
                                        如果
                                          ├─ 条件: 单位有魔法效果(触发单位(), BIcb) == TRUE
                                          ├─ 则
                                          │    UnitRemoveBuffBJ: BIcb, 触发单位()
                                          │    伤害目标: 伤害来源(), 触发单位(), 单位状态(UnitStateMaxLife, 伤害来源()), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                          │    设置 X_zs = 实数转整数(单位状态(UnitStateMaxLife, 伤害来源()))
                                          │    设置 X_dian = (伤害来源()的位置)
                                          │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 0.00, 0
                                          │    清除点 X_dian
                                          │    TriggerExecute: gg_trg_001
                                          └─ 否则
                                               如果
                                                 ├─ 条件: 单位有魔法效果(触发单位(), B000) == TRUE
                                                 ├─ 则
                                                 │    UnitRemoveBuffBJ: B000, 触发单位()
                                                 │    如果
                                                 │      ├─ 条件: 随机[90~99] == 95
                                                 │      ├─ 则
                                                 │      │    设置 X_zs = (((英雄属性(HeroStatStr, 伤害来源(), InclusionInclude) + 英雄属性(HeroStatAgi, 伤害来源(), InclusionInclude)) + 英雄属性(HeroStatInt, 伤害来源(), InclusionInclude)) x 190)
                                                 │      └─ 否则
                                                 │           设置 X_zs = (((英雄属性(HeroStatStr, 伤害来源(), InclusionInclude) + 英雄属性(HeroStatAgi, 伤害来源(), InclusionInclude)) + 英雄属性(HeroStatInt, 伤害来源(), InclusionInclude)) x 19)
                                                 │    伤害目标: 伤害来源(), 触发单位(), (X_zs转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                 │    设置 X_dian = (伤害来源()的位置)
                                                 │    CreateTextTagLocBJ: (X_zs转字符串) + "!", X_dian, 0, 10, 100, 0.00, 0.00, 0
                                                 │    清除点 X_dian
                                                 │    TriggerExecute: gg_trg_001
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: 全部成立
                                                        │    ├─ 单位有魔法效果(触发单位(), Bpxf) == TRUE
                                                        │    ├─ IsHeroUnitId((伤害来源()类型ID)) == TRUE
                                                        ├─ 则
                                                        │    UnitRemoveBuffBJ: Bpxf, 触发单位()
                                                        │    如果
                                                        │      ├─ 条件: (伤害来源()类型ID) == H004
                                                        │      ├─ 则
                                                        │      │    伤害目标: 伤害来源(), 触发单位(), ((英雄等级(伤害来源()) x 10000)转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                        │      └─ 否则
                                                        │           伤害目标: 伤害来源(), 触发单位(), ((英雄等级(X_DW) x 10000)转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: 全部成立
                                                               │    ├─ 随机[1~10] == 6
                                                               │    ├─ (伤害来源()类型ID) == n005
                                                               ├─ 则
                                                               │    关闭触发器 当前触发器()
                                                               │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 触发单位(), "origin")
                                                               │    设置 X_dian = (触发单位()的位置)
                                                               │    设置 X_danweizu = 范围内符合条件的单位(185.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (伤害来源()的所有者)), OperatorEqualENE, true))
                                                               │    清除点 X_dian
                                                               │    单位组: 选取 X_danweizu 中所有单位
                                                               │      └─ 伤害目标: 伤害来源(), 选取单位(), ((0.10 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatStr, X_DW, InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                               │    删除单位组 X_danweizu
                                                               │    开启触发器 当前触发器()
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: 全部成立
                                                                      │    ├─ 随机[40~49] == 45
                                                                      │    ├─ 单位持有物品类型(伤害来源(), I03A) == TRUE
                                                                      │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
                                                                      ├─ 则
                                                                      │    销毁特效 创建特效(附着单位)(Abilities\Spells\Undead\DeathCoil\DeathCoilSpecialArt.mdl, 触发单位(), "origin")
                                                                      │    伤害目标: 伤害来源(), 触发单位(), 单位状态(UnitStateLife, 触发单位()), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                      └─ 否则: (无)
```

### 被攻击

```text
触发器: 被攻击 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A2

```text
触发器: A2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  └─ 是敌方单位(触发单位(), (攻击单位()的所有者)) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: (攻击单位()类型ID) == e00D
  │    ├─ 则
  │    │    杀死 攻击单位()
  │    │    循环整数A 1→5
  │    │      └─ 如果
  │    │           ├─ 条件: 单位持有物品类型(触发单位(), WP_SHC[(6 - 循环整数A())]) == TRUE
  │    │           ├─ 则
  │    │           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd((3 x (10 - 循环整数A())) + 2)
  │    │           │    CustomScriptCode: ScriptCode00
  │    │           └─ 否则: (无)
  │    └─ 否则
  │         如果
  │           ├─ 条件: (攻击单位()类型ID) == e00E
  │           ├─ 则
  │           │    杀死 攻击单位()
  │           │    循环整数A 1→5
  │           │      └─ 如果
  │           │           ├─ 条件: 单位持有物品类型(触发单位(), WP_SY[(6 - 循环整数A())]) == TRUE
  │           │           ├─ 则
  │           │           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd((3 x (10 - 循环整数A())) + 2)
  │           │           │    CustomScriptCode: ScriptCode00
  │           │           └─ 否则: (无)
  │           └─ 否则
  │                如果
  │                  ├─ 条件: (攻击单位()类型ID) == e00F
  │                  ├─ 则
  │                  │    杀死 攻击单位()
  │                  │    循环整数A 1→5
  │                  │      └─ 如果
  │                  │           ├─ 条件: 单位持有物品类型(触发单位(), WP_SYMJ[(6 - 循环整数A())]) == TRUE
  │                  │           ├─ 则
  │                  │           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd((3 x (10 - 循环整数A())) + 2)
  │                  │           │    CustomScriptCode: ScriptCode00
  │                  │           └─ 否则: (无)
  │                  └─ 否则
  │                       如果
  │                         ├─ 条件: (攻击单位()类型ID) == e00G
  │                         ├─ 则
  │                         │    杀死 攻击单位()
  │                         │    如果
  │                         │      ├─ 条件: 单位持有物品类型(触发单位(), I03M) == TRUE
  │                         │      ├─ 则
  │                         │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd20
  │                         │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd20
  │                         │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd20
  │                         │      └─ 否则: (无)
  │                         └─ 否则: (无)
  ├─ 设置 X_DW = YX_7[玩家号((攻击单位()的所有者))]
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位技能等级(攻击单位(), A000) == 1
       │    ├─ 随机[1~20] == 9
       ├─ 则
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 单位有魔法效果(攻击单位(), B006) == TRUE
       │      │    ├─ 单位类型判断(攻击单位(), 英雄) == TRUE
       │      │    ├─ 随机[1~5] == 4
       │      ├─ 则
       │      │    SetPlayerAbilityAvailable: (攻击单位()的所有者), A05N, EnableDisableEnable
       │      │    单位发布命令(立即): 攻击单位(), UnitOrderWhirlWind
       │      └─ 否则
       │           播放动画: 攻击单位(), "attack walk stand spin"
       │           设置 X_dian = (攻击单位()的位置)
       │           设置 X_danweizu = 范围内符合条件的单位(375.00, X_dian, (布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
       │           清除点 X_dian
       │           设置 X_zs = 实数转整数(((0.15 x (英雄等级(X_DW)转实数)) x (英雄属性(HeroStatAgi, X_DW, InclusionInclude)转实数)))
       │           单位组: 选取 X_danweizu 中所有单位
       │             ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Stampede\StampedeMissileDeath.mdl, 选取单位(), "overhead")
       │             └─ 伤害目标: 攻击单位(), 选取单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       │           删除单位组 X_danweizu
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ 随机[1~20] == 8
              │    ├─ (攻击单位()类型ID) == H000
              ├─ 则
              │    循环整数A 1→6
              │      └─ 添加 创建单位(指定坐标)((攻击单位()的所有者), e002, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), (((循环整数A() x 10)转实数) + (单位朝向角度(攻击单位()) - 30.00))) → RH1
              │    开启触发器 gg_trg_A35RH0
              └─ 否则
                   如果
                     ├─ 条件: 全部成立
                     │    ├─ 随机[1~20] == 7
                     │    ├─ 单位技能等级(攻击单位(), A046) == 1
                     ├─ 则
                     │    设置 X_dian = (触发单位()的位置)
                     │    命令 创建单位(指定坐标)((攻击单位()的所有者), e004, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), 单位朝向角度(攻击单位())) → UnitOrderStampede 到 X_dian
                     │    清除点 X_dian
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 随机[1~20] == 6
                            │    ├─ 单位技能等级(攻击单位(), A00N) == 1
                            ├─ 则
                            │    设置 X_dian = (攻击单位()的位置)
                            │    单位发布命令(立即): 创建单位(指定坐标)((攻击单位()的所有者), e007, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), 0), UnitOrderStomp
                            │    设置 X_zs = 实数转整数(((1 + (0.20 x (英雄等级(YX_7[玩家号((攻击单位()的所有者))])转实数))) x (英雄属性(HeroStatStr, YX_7[玩家号((攻击单位()的所有者))], InclusionInclude)转实数)))
                            │    CreateTextTagLocBJ: (X_zs转字符串) + "锛?", X_dian, 0, 11.00, 0.00, 100, 100, 0
                            │    TriggerExecute: gg_trg_001
                            │    清除点 X_dian
                            └─ 否则
                                 如果
                                   ├─ 条件: 全部成立
                                   │    ├─ 随机[1~20] == 5
                                   │    ├─ 单位技能等级(攻击单位(), A03C) == 1
                                   ├─ 则
                                   │    设置 XD_CC_CS[循环整数A()] = (XD_CC_CS[循环整数A()] + 5)
                                   │    开启触发器 gg_trg_A10
                                   └─ 否则
                                        如果
                                          ├─ 条件: 全部成立
                                          │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
                                          │    ├─ 随机[1~20] == 4
                                          │    ├─ 单位技能等级(触发单位(), A00K) == 1
                                          ├─ 则
                                          │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\DispelMagic\DispelMagicTarget.mdl, 触发单位(), "origin")
                                          │    设置技能等级: 触发单位(), A00K, 2
                                          │    运行计时器 LSSB_JSQ (一次性, 5.00s)
                                          └─ 否则
                                               如果
                                                 ├─ 条件: 全部成立
                                                 │    ├─ 随机[1~20] == 3
                                                 │    ├─ 单位技能等级(攻击单位(), A056) == 1
                                                 ├─ 则
                                                 │    设置 X_dian = (攻击单位()的位置)
                                                 │    设置 X_danweizu = 范围内符合条件的单位(450.00, X_dian, (布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
                                                 │    循环整数A 1→12
                                                 │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 256, (30.00 x (循环整数A()转实数)))
                                                 │      ├─ 命令 创建单位(指定坐标)((攻击单位()的所有者), e008, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), (30.00 x (循环整数A()转实数))) → UnitOrderCarrionSwarm 到 X_dian2
                                                 │      └─ 清除点 X_dian2
                                                 │    设置 X_zs = ((英雄等级(YX_7[玩家号((攻击单位()的所有者))]) / 5) x 英雄属性(HeroStatStr, YX_7[玩家号((攻击单位()的所有者))], InclusionInclude))
                                                 │    单位组: 选取 X_danweizu 中所有单位
                                                 │      └─ 伤害目标: 攻击单位(), 选取单位(), ((X_zs + 实数转整数((0.03 x 单位状态(选取单位(), UnitStateMaxLife))))转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                 │    删除单位组 X_danweizu
                                                 │    CreateTextTagLocBJ: (X_zs转字符串), X_dian, 0, 10, 0.00, 0.00, 0.00, 0
                                                 │    TriggerExecute: gg_trg_001
                                                 │    清除点 X_dian
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: 全部成立
                                                        │    ├─ 单位是否暂停(触发单位()) == TRUE
                                                        │    ├─ 随机[1~20] == 1
                                                        │    ├─ 单位技能等级(攻击单位(), A03R) == 1
                                                        ├─ 则
                                                        │    杀死 TDQL_DW
                                                        │    清除点 TDQL_D
                                                        │    设置 TDQL_D = (触发单位()的位置)
                                                        │    PlaySoundAtPointBJ: gg_snd_DarkSummoningLaunch1, 100, TDQL_D, 100.00
                                                        │    设置 TDQL = 0
                                                        │    设置 TDQL_DW = 创建单位(指定坐标)((触发单位()的所有者), e00B, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
                                                        │    开启触发器 gg_trg_A19
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: 全部成立
                                                               │    ├─ 单位类型判断(攻击单位(), 英雄) == TRUE
                                                               │    ├─ 随机[1~20] == 1
                                                               │    ├─ 单位持有物品类型(攻击单位(), I02F) == TRUE
                                                               ├─ 则
                                                               │    设置 WP_XTR[1] = 攻击单位()
                                                               │    设置 WP_XTR[2] = 触发单位()
                                                               │    设置 WP_XTR_ZS = 10
                                                               │    开启触发器 gg_trg_A20
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: 全部成立
                                                                      │    ├─ 随机[10~29] == 17
                                                                      │    ├─ 单位技能等级(触发单位(), A06O) == 1
                                                                      ├─ 则
                                                                      │    设置 X_dian = (攻击单位()的位置)
                                                                      │    设置 X_danweizu = 范围内符合条件的单位(450.00, X_dian, (布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
                                                                      │    清除点 X_dian
                                                                      │    单位组: 选取 X_danweizu 中所有单位
                                                                      │      └─ 单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00U, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), 0), UnitOrderEntanglingRoots, 选取单位()
                                                                      │    删除单位组 X_danweizu
                                                                      └─ 否则
                                                                           如果
                                                                             ├─ 条件: 全部成立
                                                                             │    ├─ 任一成立
                                                                             │    ├─ 随机[11~30] == 21
                                                                             ├─ 则
                                                                             │    销毁特效 创建特效(指定坐标)(war3mapImported\bingbao3.mdx, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
                                                                             │    设置 X_dian = (触发单位()的位置)
                                                                             │    设置 X_danweizu = 范围内符合条件的单位(512.00, X_dian, (布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
                                                                             │    设置 X_zs = 实数转整数(((0.25 x (英雄等级(YX_7[玩家号((攻击单位()的所有者))])转实数)) x (英雄属性(HeroStatInt, YX_7[玩家号((攻击单位()的所有者))], InclusionInclude)转实数)))
                                                                             │    单位组: 选取 X_danweizu 中所有单位
                                                                             │      └─ 伤害目标: 攻击单位(), 选取单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                             │    删除单位组 X_danweizu
                                                                             │    CreateTextTagLocBJ: (X_zs转字符串) + "锛?", X_dian, 0, 10, 0.00, 100.00, 100.00, 0
                                                                             │    TriggerExecute: gg_trg_001
                                                                             │    清除点 X_dian
                                                                             └─ 否则
                                                                                  如果
                                                                                    ├─ 条件: 全部成立
                                                                                    │    ├─ 单位类型判断(攻击单位(), 英雄) == TRUE
                                                                                    │    ├─ 单位技能等级(攻击单位(), S001) == 1
                                                                                    │    ├─ 单位技能等级(攻击单位(), A071) != 1
                                                                                    │    ├─ 随机[11~25] == 22
                                                                                    ├─ 则
                                                                                    │    添加技能: 攻击单位(), A071
                                                                                    │    运行计时器 CH_JSQ (一次性, (2.00 + (0.10 x (英雄等级(攻击单位())转实数)))s)
                                                                                    └─ 否则
                                                                                         如果
                                                                                           ├─ 条件: 单位技能等级(攻击单位(), A06X) == 1
                                                                                           ├─ 则
                                                                                           │    如果
                                                                                           │      ├─ 条件: CYNM OperatorLess 25
                                                                                           │      ├─ 则
                                                                                           │      │    设置 CYNM = (CYNM + 1)
                                                                                           │      └─ 否则
                                                                                           │           销毁特效 创建特效(指定坐标)(war3mapImported\firenova2.mdx, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()))
                                                                                           │           如果
                                                                                           │             ├─ 条件: 随机[1~10] OperatorLessEq 5
                                                                                           │             ├─ 则
                                                                                           │             └─ 否则
                                                                                           │                  设置 CYNM = 0
                                                                                           │           设置 X_dian = (触发单位()的位置)
                                                                                           │           设置 X_zs = 实数转整数((((英雄等级(YX_7[玩家号((攻击单位()的所有者))])转实数) x 0.20) x (英雄属性(HeroStatInt, YX_7[玩家号((攻击单位()的所有者))], InclusionInclude)转实数)))
                                                                                           │           设置 X_danweizu = 范围内符合条件的单位(512, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true)))
                                                                                           │           单位组: 选取 X_danweizu 中所有单位
                                                                                           │             ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
                                                                                           │             └─ 伤害目标: 攻击单位(), 选取单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                           │           删除单位组 X_danweizu
                                                                                           │           CreateTextTagLocBJ: (X_zs转字符串) + "锛?", X_dian, 0, 10, 100, 0.00, 0.00, 0
                                                                                           │           TriggerExecute: gg_trg_001
                                                                                           │           清除点 X_dian
                                                                                           └─ 否则: (无)
```

### A01

```text
触发器: A01 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  └─ 是敌方单位(触发单位(), (攻击单位()的所有者)) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位类型判断(攻击单位(), 英雄) == TRUE
  │    │    ├─ 单位技能等级(攻击单位(), A06E) == 1
  │    ├─ 则
  │    │    运行计时器 LD_1JSQ (一次性, 9.00s)
  │    │    如果
  │    │      ├─ 条件: LD_1ZS OperatorLess 10000
  │    │      ├─ 则
  │    │      │    修改 攻击单位() 的HeroStatInt: ModifyMethodAdd(5 + (英雄等级(攻击单位()) / 5))
  │    │      │    设置 LD_1ZS = (LD_1ZS + (5 + (英雄等级(攻击单位()) / 5)))
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位技能等级(触发单位(), A06J) == 1
       │    ├─ 随机[20~39] == 26
       ├─ 则
       │    单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00T, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderChainLightning, 攻击单位()
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ 单位技能等级(攻击单位(), A076) == 1
              │    ├─ 随机[20~34] == 26
              ├─ 则
              │    销毁特效 创建特效(指定坐标)(war3mapImported\leidian.mdx, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
              │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\ManaFlare\ManaFlareBoltImpact.mdl, 触发单位(), "origin")
              │    设置生命百分比: 触发单位(), (单位生命百分比(触发单位()) x 0.92)
              │    设置 X_dian = (触发单位()的位置)
              │    设置 X_danweizu = GetRandomSubGroup(5, 范围内符合条件的单位(512, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true))))
              │    清除点 X_dian
              │    单位组: 选取 X_danweizu 中所有单位
              │      └─ 单位发布命令(目标): 创建单位(指定坐标)((攻击单位()的所有者), e00T, 单位X坐标(选取单位()), 单位Y坐标(选取单位()), 0), UnitOrderChainLightning, 选取单位()
              │    删除单位组 X_danweizu
              └─ 否则
                   如果
                     ├─ 条件: 全部成立
                     │    ├─ 随机[20~39] == 33
                     │    ├─ 单位技能等级(攻击单位(), A077) == 1
                     │    ├─ YM_ZJ == TRUE
                     ├─ 则
                     │    设置生命百分比: 触发单位(), (单位生命百分比(触发单位()) x 0.75)
                     │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\ManaFlare\ManaFlareBoltImpact.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 随机[1~20] == 7
                            │    ├─ 单位持有物品类型(攻击单位(), I016) == TRUE
                            ├─ 则
                            │    循环整数A 1→18
                            │      └─ 添加 创建单位(指定坐标)((攻击单位()的所有者), e00W, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()), ((循环整数A()转实数) x 20.00)) → MRY_DW
                            │    开启触发器 gg_trg_A34MRY
                            └─ 否则
                                 如果
                                   ├─ 条件: 全部成立
                                   │    ├─ 随机[1~20] == 8
                                   │    ├─ (攻击单位()类型ID) == N007
                                   ├─ 则
                                   │    设置 X_dian = (触发单位()的位置)
                                   │    设置 X_danweizu = 范围内符合条件的单位(350.00, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true)))
                                   │    清除点 X_dian
                                   │    单位组: 选取 X_danweizu 中所有单位
                                   │      └─ 单位发布命令(目标): 创建单位(指定坐标)((攻击单位()的所有者), e00I, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderSoulBurn, 选取单位()
                                   │    删除单位组 X_danweizu
                                   └─ 否则
                                        如果
                                          ├─ 条件: 全部成立
                                          │    ├─ 随机[1~20] == 9
                                          │    ├─ 单位技能等级(A00A, 攻击单位()) == 1
                                          │    ├─ 单位类型判断(攻击单位(), 英雄) == TRUE
                                          ├─ 则
                                          │    添加物品: I001, 攻击单位()
                                          │    修改 攻击单位() 的HeroStatAgi: ModifyMethodAdd4
                                          └─ 否则: (无)
```

### A22

```text
触发器: A22 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ (攻击单位()类型ID) == H005
       │    ├─ 随机[1~3] == 2
       ├─ 则
       │    设置 X_dian = (触发单位()的位置)
       │    设置 X_danweizu = 范围内符合条件的单位(350.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true))
       │    清除点 X_dian
       │    单位组: 选取 X_danweizu 中所有单位
       │      ├─ 伤害目标: 攻击单位(), 选取单位(), ((50000 x (玩家科技等级(Rhan, (攻击单位()的所有者)) + 1))转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       │      └─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Undead\FrostNova\FrostNovaTarget.mdl, 选取单位(), "origin")
       │    删除单位组 X_danweizu
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ (触发单位()类型ID) == E00J
              │    ├─ 随机[1~5] == 3
              ├─ 则
              │    设置 X_dian = (攻击单位()的位置)
              │    设置 X_danweizu = 范围内符合条件的单位(350.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
              │    清除点 X_dian
              │    单位组: 选取 X_danweizu 中所有单位
              │      └─ 单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e008, 单位X坐标(选取单位()), 单位Y坐标(选取单位()), 0), UnitOrderEntanglingRoots, 选取单位()
              │    删除单位组 X_danweizu
              └─ 否则
                   如果
                     ├─ 条件: 全部成立
                     │    ├─ 任一成立
                     │    ├─ 随机[1~10] == 3
                     ├─ 则
                     │    设置 X_dian = (触发单位()的位置)
                     │    设置 X_danweizu = 范围内符合条件的单位(700.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
                     │    循环整数A 1→12
                     │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 550.00, ((循环整数A()转实数) x 30.00))
                     │      ├─ 销毁特效 创建特效(Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl, X_dian2)
                     │      └─ 清除点 X_dian2
                     │    清除点 X_dian
                     │    单位组: 选取 X_danweizu 中所有单位
                     │      └─ 伤害目标: 触发单位(), 选取单位(), (单位状态(UnitStateMaxLife, 选取单位()) x (0.15 x ((玩家科技等级(Rhan, PlayerNA) + 1)转实数))), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                     │    删除单位组 X_danweizu
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ (触发单位()类型ID) == Uclc
                            │    ├─ 随机[1~10] == 3
                            ├─ 则
                            │    销毁特效 创建特效(指定坐标)(war3mapImported\leidian.mdx, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()))
                            │    杀死 攻击单位()
                            └─ 否则: (无)
```

### A27

```text
触发器: A27 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ 玩家控制者比较(玩家控制者类型((攻击单位()的所有者)), OperatorEqualENE, MapControlUser)
  └─ 单位类型判断(攻击单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 随机[1~75] == 4
       ├─ 则
       │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\HolyBolt\HolyBoltSpecialArt.mdl, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()))
       │    修改 攻击单位() 的HeroStatStr: ModifyMethodAdd12
       │    修改 攻击单位() 的HeroStatAgi: ModifyMethodAdd12
       │    修改 攻击单位() 的HeroStatInt: ModifyMethodAdd12
       │    显示文本→(攻击单位()的所有者): 0
       └─ 否则
            如果
              ├─ 条件: 随机[1~500] == 7
              ├─ 则
              │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
              │    显示文本→(攻击单位()的所有者): 0
              │    伤害目标: 攻击单位(), 触发单位(), ((250 x ((英雄属性(HeroStatStr, 攻击单位(), InclusionInclude) + 英雄属性(HeroStatAgi, 攻击单位(), InclusionInclude)) + 英雄属性(HeroStatInt, 攻击单位(), InclusionInclude)))转实数), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
              └─ 否则
                   如果
                     ├─ 条件: 全部成立
                     │    ├─ 单位生命百分比(攻击单位()) OperatorLess 20.00
                     │    ├─ 随机[1~100] == 16
                     ├─ 则
                     │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Resurrect\ResurrectTarget.mdl, 单位X坐标(攻击单位()), 单位Y坐标(攻击单位()))
                     │    显示文本→(攻击单位()的所有者): 0
                     │    设置生命百分比: 攻击单位(), 100
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 单位技能等级(攻击单位(), A04W) == 1
                            │    ├─ 玩家科技等级(Rhhb, (攻击单位()的所有者)) == 1
                            │    ├─ 随机[1~50] == 32
                            ├─ 则
                            │    显示文本→(攻击单位()的所有者): 0
                            │    设置 X_dian = (触发单位()的位置)
                            │    设置 X_danweizu = 范围内符合条件的单位(800.00, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true)))
                            │    清除点 X_dian
                            │    单位组: 选取 X_danweizu 中所有单位
                            │      ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
                            │      └─ 伤害目标: 攻击单位(), 选取单位(), ((0.25 x (英雄等级(攻击单位())转实数)) x (英雄属性(HeroStatStr, 攻击单位(), InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                            │    删除单位组 X_danweizu
                            └─ 否则
                                 如果
                                   ├─ 条件: 全部成立
                                   │    ├─ 单位技能等级(攻击单位(), A04W) == 1
                                   │    ├─ 玩家科技等级(Rhhb, (攻击单位()的所有者)) == 1
                                   │    ├─ 随机[1~50] == 22
                                   ├─ 则
                                   │    显示文本→(攻击单位()的所有者): 0
                                   │    设置 X_dian = (触发单位()的位置)
                                   │    设置 X_danweizu = 范围内符合条件的单位(800.00, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true)))
                                   │    清除点 X_dian
                                   │    单位组: 选取 X_danweizu 中所有单位
                                   │      ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Monsoon\MonsoonBoltTarget.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
                                   │      └─ 伤害目标: 攻击单位(), 选取单位(), ((0.25 x (英雄等级(攻击单位())转实数)) x (英雄属性(HeroStatAgi, 攻击单位(), InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                   │    删除单位组 X_danweizu
                                   └─ 否则
                                        如果
                                          ├─ 条件: 全部成立
                                          │    ├─ 单位技能等级(攻击单位(), A04W) == 1
                                          │    ├─ 玩家科技等级(Rhhb, (攻击单位()的所有者)) == 1
                                          │    ├─ 随机[1~50] == 42
                                          ├─ 则
                                          │    显示文本→(攻击单位()的所有者): 0
                                          │    设置 X_dian = (触发单位()的位置)
                                          │    设置 X_danweizu = 范围内符合条件的单位(800.00, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (攻击单位()的所有者)), OperatorEqualENE, true)))
                                          │    清除点 X_dian
                                          │    单位组: 选取 X_danweizu 中所有单位
                                          │      ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Monsoon\MonsoonBoltTarget.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
                                          │      └─ 伤害目标: 攻击单位(), 选取单位(), ((0.25 x (英雄等级(攻击单位())转实数)) x (英雄属性(HeroStatInt, 攻击单位(), InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                          │    删除单位组 X_danweizu
                                          └─ 否则: (无)
```

### 咫尺天涯

```text
触发器: 咫尺天涯 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A36

```text
触发器: A36 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_H001_0087 - UnitEventAcquiredTarget
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\NightElf\Blink\BlinkCaster.mdl, 单位X坐标(GetEventTargetUnit()), 单位Y坐标(GetEventTargetUnit()))
  ├─ SetUnitX: GetEventTargetUnit(), (单位X坐标(触发单位()) + (随机[-100~100]转实数))
  └─ SetUnitY: GetEventTargetUnit(), (单位Y坐标(触发单位()) + (随机[-100~100]转实数))
```

### 发动技能

```text
触发器: 发动技能 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A3

```text
触发器: A3 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A045)
       ├─ 则
       │    开启触发器 gg_trg_JZ0
       └─ 否则
            如果
              ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03A)
              ├─ 则
              │    设置 X_dian = 技能目标点()
              │    循环整数A 1→12
              │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 512.00, (30.00 x (循环整数A()转实数)))
              │      ├─ 创建 1个|e005|→(触发单位()的所有者) 在 X_dian2 面向默认朝向
              │      └─ 清除点 X_dian2
              │    清除点 X_dian
              └─ 否则
                   如果
                     ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A00G)
                     ├─ 则
                     │    单位发布命令(立即): 创建单位(指定坐标)((触发单位()的所有者), e006, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0), UnitOrderStarfall2
                     └─ 否则
                          如果
                            ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03P)
                            ├─ 则
                            │    设置 X_dian = (技能目标单位()的位置)
                            │    设置 X_danweizu = 范围内符合条件的单位(512, X_dian, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
                            │    清除点 X_dian
                            │    单位组: 选取 X_danweizu 中所有单位
                            │      ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Feedback\ArcaneTowerAttack.mdl, 选取单位(), "origin")
                            │      └─ 伤害目标: 触发单位(), 选取单位(), ((0.30 x (英雄属性(HeroStatAgi, 触发单位(), InclusionInclude)转实数)) x (英雄等级(触发单位())转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                            │    删除单位组 X_danweizu
                            └─ 否则
                                 如果
                                   ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03R)
                                   ├─ 则
                                   │    杀死 TDQL_DW
                                   │    清除点 TDQL_D
                                   │    设置 TDQL_D = (触发单位()的位置)
                                   │    PlaySoundAtPointBJ: gg_snd_DarkSummoningLaunch1, 100, TDQL_D, 100.00
                                   │    设置 TDQL = 0
                                   │    设置 TDQL_DW = 创建单位(指定坐标)((触发单位()的所有者), e00B, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
                                   │    开启触发器 gg_trg_A19
                                   └─ 否则
                                        如果
                                          ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03S)
                                          ├─ 则
                                          │    命令 创建单位(指定坐标)((触发单位()的所有者), e003, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0) → UnitOrderMonsoon 到 单位X坐标(触发单位())
                                          └─ 否则
                                               如果
                                                 ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A06O)
                                                 ├─ 则
                                                 │    设置 X_dian = (技能目标单位()的位置)
                                                 │    设置 X_danweizu = 范围内符合条件的单位(512, X_dian, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
                                                 │    清除点 X_dian
                                                 │    单位组: 选取 X_danweizu 中所有单位
                                                 │      └─ 单位发布命令(目标): 创建单位(指定坐标)((触发单位()的所有者), e00U, 单位X坐标(选取单位()), 单位Y坐标(选取单位()), 0), UnitOrderEntanglingRoots, 选取单位()
                                                 │    删除单位组 X_danweizu
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03O)
                                                        ├─ 则
                                                        │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A06Y)
                                                               ├─ 则
                                                               │    设置 YHFS = 17
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A074)
                                                                      ├─ 则
                                                                      │    设置 X_dian = 技能目标点()
                                                                      │    命令 创建单位(指定坐标)((触发单位()的所有者), e00S, 点X坐标(X_dian), 点Y坐标(X_dian), 0) → UnitOrderHeroRainOfFire 到 X_dian
                                                                      │    清除点 X_dian
                                                                      └─ 否则
                                                                           如果
                                                                             ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A04U)
                                                                             ├─ 则
                                                                             │    设置 X_dian = 技能目标点()
                                                                             │    循环整数A 1→10
                                                                             │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 200.00, (36.00 x (循环整数A()转实数)))
                                                                             │      ├─ 创建 1个|e00P|→(触发单位()的所有者) 在 X_dian2 面向默认朝向
                                                                             │      ├─ SetUnitVertexColorBJ: 最后创建的单位(), 100, 0.00, 100, 0
                                                                             │      └─ 清除点 X_dian2
                                                                             │    循环整数A 1→25
                                                                             │      ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 350.00, (14.40 x (循环整数A()转实数)))
                                                                             │      ├─ 创建 1个|e00P|→(触发单位()的所有者) 在 X_dian2 面向默认朝向
                                                                             │      ├─ SetUnitVertexColorBJ: 最后创建的单位(), 0.00, 100.00, 100, 0
                                                                             │      └─ 清除点 X_dian2
                                                                             │    清除点 X_dian
                                                                             └─ 否则
                                                                                  如果
                                                                                    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, ACfn)
                                                                                    ├─ 则
                                                                                    │    伤害目标: 触发单位(), 技能目标单位(), (单位状态(技能目标单位(), UnitStateMaxLife) x (0.15 x ((玩家科技等级(Rhan, 玩家6(橙)) + 1)转实数))), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
                                                                                    └─ 否则
                                                                                         如果
                                                                                           ├─ 条件: 全部成立
                                                                                           │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A049)
                                                                                           │    ├─ 单位类型判断(技能目标单位(), 英雄) == TRUE
                                                                                           ├─ 则
                                                                                           │    设置 SX_WPLL[玩家号((技能目标单位()的所有者))] = (SX_WPLL[玩家号((技能目标单位()的所有者))] + 0.03)
                                                                                           └─ 否则: (无)
```

### 停止技能

```text
触发器: 停止技能 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A4

```text
触发器: A4 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 任意单位 - PlayerUnitEventSpellEndCast
  └─ 任意单位 - PlayerUnitEventSpellFinish
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A05N)
       ├─ 则
       │    SetPlayerAbilityAvailableBJ: EnableDisableDisable, A05N, (触发单位()的所有者)
       └─ 否则
            如果
              ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03O)
              ├─ 则
              │    设置无敌: 触发单位(), InvulnerabilityVulnerable
              └─ 否则: (无)
```

### A35RH0

```text
触发器: A35RH0 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.02)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: (RH1中的单位数) == 0
       ├─ 则
       │    关闭触发器 当前触发器()
       └─ 否则
            单位组: 选取 RH1 中所有单位
              └─ 如果
                   ├─ 条件: 全部成立
                   │    ├─ 单位X坐标(选取单位()) OperatorLess 7600.00
                   │    ├─ 单位Y坐标(选取单位()) OperatorLess 7600.00
                   │    ├─ 单位X坐标(选取单位()) OperatorGreater -7600.00
                   │    ├─ 单位Y坐标(选取单位()) OperatorGreater -7600.00
                   ├─ 则
                   │    SetUnitX: 选取单位(), (单位X坐标(选取单位()) + (40.00 x 余弦(单位朝向角度(选取单位()))))
                   │    SetUnitY: 选取单位(), (单位Y坐标(选取单位()) + (40.00 x 正弦(单位朝向角度(选取单位()))))
                   └─ 否则
                        杀死 选取单位()
                        从单位组移除单位: 选取单位(), RH1
```

### A34MRY

```text
触发器: A34MRY (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.02)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: (MRY_DW中的单位数) == 0
       ├─ 则
       │    关闭触发器 当前触发器()
       └─ 否则
            单位组: 选取 MRY_DW 中所有单位
              └─ 如果
                   ├─ 条件: 全部成立
                   │    ├─ 单位X坐标(选取单位()) OperatorLess 7600.00
                   │    ├─ 单位Y坐标(选取单位()) OperatorLess 7600.00
                   │    ├─ 单位X坐标(选取单位()) OperatorGreater -7600.00
                   │    ├─ 单位Y坐标(选取单位()) OperatorGreater -7600.00
                   ├─ 则
                   │    如果
                   │      ├─ 条件: 单位生命百分比(选取单位()) OperatorLessEq 50.00
                   │      ├─ 则
                   │      │    SetUnitX: 选取单位(), (单位X坐标(选取单位()) + (25.00 x 余弦((单位朝向角度(选取单位()) + 180.00))))
                   │      │    SetUnitY: 选取单位(), (单位Y坐标(选取单位()) + (25.00 x 正弦((单位朝向角度(选取单位()) + 180.00))))
                   │      └─ 否则
                   │           SetUnitX: 选取单位(), (单位X坐标(选取单位()) + (25.00 x 余弦(单位朝向角度(选取单位()))))
                   │           SetUnitY: 选取单位(), (单位Y坐标(选取单位()) + (25.00 x 正弦(单位朝向角度(选取单位()))))
                   └─ 否则: (无)
```

### A33HMXL

```text
触发器: A33HMXL (初始化) [✓] — 鸿蒙洗礼
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(1.50)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 单位持有物品类型(YX_7[循环整数A()], I00W) == TRUE
            ├─ 则
            │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Resurrect\ResurrectTarget.mdl, YX_7[循环整数A()], "origin")
            │    设置生命百分比: YX_7[循环整数A()], (单位生命百分比(YX_7[循环整数A()]) + 30.00)
            └─ 否则: (无)
```

### A32SB

```text
触发器: A32SB (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 LSSB_JSQ 到期
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: (YX_7[循环整数A()]类型ID) == E000
            ├─ 则
            │    设置技能等级: YX_7[循环整数A()], A00K, 1
            └─ 否则: (无)
```

### 乾坤刺

```text
触发器: 乾坤刺 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A39

```text
触发器: A39 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(512.00, gg_unit_H001_0087)
条件
  └─ 单位类型判断(触发单位(), UnitTypeGround) == TRUE
动作
  └─ 开启触发器 gg_trg_A38
```

### A38

```text
触发器: A38 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.30)
条件
  └─ 无
动作
  ├─ 设置 X_dian = (gg_unit_H001_0087的位置)
  ├─ 设置 X_danweizu = GetRandomSubGroup(1, 范围内符合条件的单位(512, X_dian, (布尔比较(单位类型判断(过滤单位(), UnitTypeGround), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), PlayerNA), OperatorEqualENE, true))))
  ├─ 清除点 X_dian
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) == 0
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    └─ 否则
  │         单位组: 选取 X_danweizu 中所有单位
  │           ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
  │           └─ 伤害目标: gg_unit_H001_0087, 选取单位(), 500000.00, IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
  └─ 删除单位组 X_danweizu
```

### 蕾帝

```text
触发器: 蕾帝 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A37FBZL

```text
触发器: A37FBZL (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 LD_1JSQ 到期
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: (YX_7[循环整数A()]类型ID) == N00D
            ├─ 则
            │    修改 YX_7[循环整数A()] 的HeroStatInt: ModifyMethodSubLD_1ZS
            │    设置 LD_1ZS = 0
            └─ 否则: (无)
```

### A34YM

```text
触发器: A34YM (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 YM_jsq 到期
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: YM_ZJ == TRUE
       ├─ 则
       │    设置 YM_ZJ = false
       │    循环整数A 1→5
       │      └─ 如果
       │           ├─ 条件: (YX_7[循环整数A()]类型ID) == N00D
       │           ├─ 则
       │           │    设置 SX_WPZL[玩家号((YX_7[循环整数A()]的所有者))] = (SX_WPZL[玩家号((YX_7[循环整数A()]的所有者))] - 0.90)
       │           └─ 否则: (无)
       │    运行计时器 YM_jsq (一次性, 9.00s)
       └─ 否则
            设置 YM_ZJ = true
            循环整数A 1→5
              └─ 如果
                   ├─ 条件: (YX_7[循环整数A()]类型ID) == N00D
                   ├─ 则
                   │    设置 SX_WPZL[玩家号((YX_7[循环整数A()]的所有者))] = (SX_WPZL[玩家号((YX_7[循环整数A()]的所有者))] + 0.90)
                   └─ 否则: (无)
            运行计时器 YM_jsq (一次性, 7.00s)
```

### A30WD

```text
触发器: A30WD (初始化) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 计时器 wudi_JSQ[1] 到期
  ├─ 计时器 wudi_JSQ[2] 到期
  ├─ 计时器 wudi_JSQ[3] 到期
  ├─ 计时器 wudi_JSQ[4] 到期
  └─ 计时器 wudi_JSQ[5] 到期
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, wudi_JSQ[循环整数A()])
            ├─ 则
            │    设置无敌: wudi[循环整数A()], InvulnerabilityVulnerable
            │    设置 wudi[循环整数A()] = UnitNull
            │    CustomScriptCode: ScriptCode00
            └─ 否则: (无)
```

### 蒙羽仙

```text
触发器: 蒙羽仙 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A28CH

```text
触发器: A28CH (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 CH_JSQ 到期
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: (YX_7[循环整数A()]类型ID) == N00C
            ├─ 则
            │    移除技能: YX_7[循环整数A()], A071
            └─ 否则: (无)
```

### A291

```text
触发器: A291 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 命令目标单位() == UnitNull
  │    ├─ 则
  │    │    设置 X_dian = GetItemLoc(GetOrderTargetItem())
  │    └─ 否则
  │         设置 X_dian = (命令目标单位()的位置)
  ├─ 循环整数A 1→5
  │    ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, ((72 x 循环整数A())转实数))
  │    ├─ 命令 HJZL_DW[循环整数A()] → UnitOrderMove 到 X_dian2
  │    └─ 清除点 X_dian2
  └─ 清除点 X_dian
```

### A292

```text
触发器: A292 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 X_dian = (触发单位()的位置)
  ├─ 循环整数A 1→5
  │    ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, ((72 x 循环整数A())转实数))
  │    ├─ 命令 HJZL_DW[循环整数A()] → UnitOrderMove 到 X_dian2
  │    └─ 清除点 X_dian2
  └─ 清除点 X_dian
```

### A293

```text
触发器: A293 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 X_dian = 命令目标点()
  ├─ 循环整数A 1→5
  │    ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, ((72 x 循环整数A())转实数))
  │    ├─ 如果
  │    │    ├─ 条件: 命令ID比较(GetIssuedOrderIdBJ(), OperatorEqualENE, 字符串转命令ID("patrol"))
  │    │    ├─ 则
  │    │    │    命令 HJZL_DW[循环整数A()] → UnitOrderPatrol 到 X_dian2
  │    │    └─ 否则
  │    │         如果
  │    │           ├─ 条件: 命令ID比较(GetIssuedOrderIdBJ(), OperatorEqualENE, 字符串转命令ID("attack"))
  │    │           ├─ 则
  │    │           │    命令 HJZL_DW[循环整数A()] → UnitOrderAttack 到 X_dian2
  │    │           └─ 否则
  │    │                命令 HJZL_DW[循环整数A()] → UnitOrderMove 到 X_dian2
  │    └─ 清除点 X_dian2
  └─ 清除点 X_dian
```

### A294

```text
触发器: A294 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(2)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       ├─ 设置移动速度: HJZL_DW[循环整数A()], GetUnitMoveSpeed(YX_7[玩家号((HJZL_DW[循环整数A()]的所有者))])
       └─ 如果
            ├─ 条件: 平方根((Pow((单位X坐标(HJZL_DW[循环整数A()]) - 单位X坐标(YX_7[玩家号((HJZL_DW[循环整数A()]的所有者))])), 2.00) + Pow((单位Y坐标(HJZL_DW[循环整数A()]) - 单位Y坐标(YX_7[玩家号((HJZL_DW[循环整数A()]的所有者))])), 2.00))) OperatorGreaterEq 500.00
            ├─ 则
            │    移动单位: HJZL_DW[循环整数A()], (单位X坐标(YX_7[玩家号((HJZL_DW[循环整数A()]的所有者))]) + (256.00 x 余弦(((72 x 循环整数A())转实数)))), (单位Y坐标(HJZL_DW[玩家号((HJZL_DW[循环整数A()]的所有者))]) + (256.00 x 正弦(((72 x 循环整数A())转实数))))
            └─ 否则: (无)
```

### 寒涟漪

```text
触发器: 寒涟漪 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A23SDXX

```text
触发器: A23SDXX (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(4.00)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 单位技能等级(A06L, YX_7[循环整数A()]) == 1
            ├─ 则
            │    设置 X_dian = (YX_7[循环整数A()]的位置)
            │    设置 X_danweizu = GetRandomSubGroup(1, 范围内符合条件的单位(450.00, X_dian, (布尔比较(是敌方单位(过滤单位(), (YX_7[循环整数A()]的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true))))
            │    清除点 X_dian
            │    单位组: 选取 X_danweizu 中所有单位
            │      └─ 单位发布命令(目标): 创建单位(指定坐标)(玩家循环整数A(), e00O, 单位X坐标(选取单位()), 单位Y坐标(选取单位()), 0), UnitOrderFrostNova, 选取单位()
            │    删除单位组 X_danweizu
            └─ 否则: (无)
```

### A25

```text
触发器: A25 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 命令目标单位() == UnitNull
  │    ├─ 则
  │    │    设置 X_dian = GetItemLoc(GetOrderTargetItem())
  │    └─ 否则
  │         设置 X_dian = (命令目标单位()的位置)
  ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, (随机[1~360]转实数))
  ├─ 命令 YLL_DW[玩家号((触发单位()的所有者))] → UnitOrderMove 到 X_dian2
  ├─ 清除点 X_dian
  └─ 清除点 X_dian2
```

### A25 复制

```text
触发器: A25 复制 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 X_dian = 命令目标点()
  ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, (随机[1~360]转实数))
  ├─ 如果
  │    ├─ 条件: 命令ID比较(GetIssuedOrderIdBJ(), OperatorEqualENE, 字符串转命令ID("patrol"))
  │    ├─ 则
  │    │    命令 YLL_DW[玩家号((触发单位()的所有者))] → UnitOrderPatrol 到 X_dian2
  │    └─ 否则
  │         如果
  │           ├─ 条件: 命令ID比较(GetIssuedOrderIdBJ(), OperatorEqualENE, 字符串转命令ID("attack"))
  │           ├─ 则
  │           │    命令 YLL_DW[玩家号((触发单位()的所有者))] → UnitOrderAttack 到 X_dian2
  │           └─ 否则
  │                命令 YLL_DW[玩家号((触发单位()的所有者))] → UnitOrderMove 到 X_dian2
  ├─ 清除点 X_dian
  └─ 清除点 X_dian2
```

### A25 复制 2

```text
触发器: A25 复制 2 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 X_dian = (触发单位()的位置)
  ├─ 设置 X_dian2 = PolarProjectionBJ(X_dian, 175.00, (随机[1~360]转实数))
  ├─ 命令 YLL_DW[玩家号((触发单位()的所有者))] → UnitOrderMove 到 X_dian2
  ├─ 清除点 X_dian
  └─ 清除点 X_dian2
```

### A26

```text
触发器: A26 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(2)
条件
  └─ 无
动作
  ├─ 设置移动速度: YLL_DW[循环整数A()], GetUnitMoveSpeed(YX_7[循环整数A()])
  └─ 如果
       ├─ 条件: 平方根((Pow((单位X坐标(YX_7[循环整数A()]) - 单位X坐标(YLL_DW[循环整数A()])), 2.00) + Pow((单位Y坐标(YX_7[循环整数A()]) - 单位Y坐标(YLL_DW[循环整数A()])), 2.00))) OperatorGreaterEq 500.00
       ├─ 则
       │    移动单位: YLL_DW[循环整数A()], 单位X坐标(YX_7[循环整数A()]), 单位Y坐标(YX_7[循环整数A()])
       └─ 否则: (无)
```

### A24BZTL

```text
触发器: A24BZTL (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(1.00)
条件
  └─ 无
动作
  ├─ ForLoopBMultiple: 1, 5
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ HB_5[1] == UnitNull
       │    ├─ HB_5[2] == UnitNull
       │    ├─ HB_5[3] == UnitNull
       │    ├─ HB_5[4] == UnitNull
       │    ├─ HB_5[5] == UnitNull
       ├─ 则
       │    关闭触发器 当前触发器()
       └─ 否则: (无)
```

### 人皇

```text
触发器: 人皇 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### RH3

```text
触发器: RH3 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.50)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 全部成立
            │    ├─ 单位存活判断(YX_7[循环整数A()]) == TRUE
            │    ├─ 单位技能等级(YX_7[循环整数A()], A03K) == 1
            ├─ 则
            │    设置 X_dian = (YX_7[循环整数A()]的位置)
            │    设置 X_danweizu = 范围内符合条件的单位(250.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (YX_7[循环整数A()]的所有者)), OperatorEqualENE, true))
            │    清除点 X_dian
            │    单位组: 选取 X_danweizu 中所有单位
            │      └─ SetUnitLifeBJ: 选取单位(), (单位状态(UnitStateLife, 选取单位()) - (单位状态(UnitStateLife, 选取单位()) x 0.01))
            │    删除单位组 X_danweizu
            └─ 否则: (无)
```

### 苍龙

```text
触发器: 苍龙 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A21

```text
触发器: A21 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(2.00)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 单位技能等级(A00J, YX_7[循环整数A()]) == 1
            ├─ 则
            │    修改 YX_7[循环整数A()] 的HeroStatStr: ModifyMethodAdd1
            └─ 否则: (无)
```

### 狂魔

```text
触发器: 狂魔 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A15

```text
触发器: A15 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.30)
条件
  └─ 无
动作
  └─ (无)
```

### 属性

```text
触发器: 属性 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A8

```text
触发器: A8 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(1.00)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 玩家槽位状态比较(玩家槽位状态(玩家循环整数A()), OperatorEqualENE, PlayerSlotStatePlaying)
            ├─ 则
            │    修改 YX_7[循环整数A()] 的HeroStatStr: ModifyMethodSubSX_LL[循环整数A()]
            │    修改 YX_7[循环整数A()] 的HeroStatAgi: ModifyMethodSubSX_MJ[循环整数A()]
            │    修改 YX_7[循环整数A()] 的HeroStatInt: ModifyMethodSubSX_ZL[循环整数A()]
            │    设置 SX_LL[循环整数A()] = 实数转整数(((英雄属性(HeroStatStr, YX_7[循环整数A()], InclusionExclude)转实数) x SX_WPLL[循环整数A()]))
            │    设置 SX_MJ[循环整数A()] = 实数转整数(((英雄属性(HeroStatAgi, YX_7[循环整数A()], InclusionExclude)转实数) x SX_WPMJ[循环整数A()]))
            │    设置 SX_ZL[循环整数A()] = 实数转整数(((英雄属性(HeroStatInt, YX_7[循环整数A()], InclusionExclude)转实数) x SX_WPZL[循环整数A()]))
            │    修改 YX_7[循环整数A()] 的HeroStatStr: ModifyMethodAddSX_LL[循环整数A()]
            │    修改 YX_7[循环整数A()] 的HeroStatAgi: ModifyMethodAddSX_MJ[循环整数A()]
            │    修改 YX_7[循环整数A()] 的HeroStatInt: ModifyMethodAddSX_ZL[循环整数A()]
            └─ 否则: (无)
```

### A10

```text
触发器: A10 (初始化) [✓] — 穿刺
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.50)
条件
  └─ 无
动作
  ├─ 循环整数A 1→5
  │    └─ 如果
  │         ├─ 条件: XD_CC_CS[循环整数A()] OperatorGreater 0
  │         ├─ 则
  │         │    设置 XD_CC_CS[循环整数A()] = (XD_CC_CS[循环整数A()] - 1)
  │         │    设置 X_dian = (YX_7[循环整数A()]的位置)
  │         │    设置 X_zs = 实数转整数(((1 + (0.08 x (英雄等级(YX_7[循环整数A()])转实数))) x (英雄属性(HeroStatStr, YX_7[循环整数A()], InclusionInclude)转实数)))
  │         │    设置 X_danweizu = 范围内符合条件的单位(450.00, X_dian, 布尔比较(是敌方单位(过滤单位(), (YX_7[循环整数A()]的所有者)), OperatorEqualENE, true))
  │         │    单位组: 选取 X_danweizu 中所有单位
  │         │      ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Undead\Impale\ImpaleHitTarget.mdl, 选取单位(), "origin")
  │         │      └─ 伤害目标: YX_7[循环整数A()], 选取单位(), (X_zs转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
  │         │    删除单位组 X_danweizu
  │         │    CreateTextTagLocBJ: (X_zs转字符串) + "锛?", X_dian, 0, 10, 100, 50.00, 70.00, 0
  │         │    TriggerExecute: gg_trg_001
  │         │    清除点 X_dian
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: (XD_CC_CS[1] + (XD_CC_CS[2] + (XD_CC_CS[3] + (XD_CC_CS[4] + XD_CC_CS[5])))) OperatorLessEq 0
       ├─ 则
       │    关闭触发器 当前触发器()
       └─ 否则: (无)
```

### 龙神

```text
触发器: 龙神 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A13

```text
触发器: A13 (初始化) [✓] — 祭献
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(1.00)
条件
  └─ 无
动作
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: 全部成立
            │    ├─ 单位技能等级(YX_7[循环整数A()], A03B) == 1
            │    ├─ 单位存活判断(YX_7[循环整数A()]) == TRUE
            ├─ 则
            │    设置 X_dian = (YX_7[循环整数A()]的位置)
            │    设置 X_danweizu = 范围内符合条件的单位(512, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (YX_7[循环整数A()]的所有者)), OperatorEqualENE, true)))
            │    单位组: 选取 X_danweizu 中所有单位
            │      ├─ 销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\Undead\UndeadDissipate\UndeadDissipate.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
            │      └─ 伤害目标: YX_7[循环整数A()], 选取单位(), ((0.08 x (英雄等级(YX_7[循环整数A()])转实数)) x (英雄属性(HeroStatAgi, YX_7[循环整数A()], InclusionInclude)转实数)), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
            │    删除单位组 X_danweizu
            │    清除点 X_dian
            └─ 否则: (无)
```

### 天地囚笼

```text
触发器: 天地囚笼 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A19

```text
触发器: A19 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.10)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: TDQL OperatorLess 50
       ├─ 则
       │    设置 TDQL = (TDQL + 1)
       │    单位组: 选取 TDQL_DWZ 中所有单位
       │      ├─ SetUnitTimeScalePercent: 选取单位(), 100.00
       │      └─ PauseUnit: 选取单位(), PauseUnpauseOptionUnpause
       │    设置 TDQL_DWZ = 范围内符合条件的单位(500.00, TDQL_D, ((布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 整数比较(英雄等级(过滤单位()), OperatorLess, 999)) 且 布尔比较(是敌方单位(过滤单位(), 玩家5(黄)), OperatorEqualENE, true)))
       │    单位组: 选取 TDQL_DWZ 中所有单位
       │      ├─ PauseUnit: 选取单位(), PauseUnpauseOptionPause
       │      └─ SetUnitTimeScalePercent: 选取单位(), 0.00
       └─ 否则
            单位组: 选取 TDQL_DWZ 中所有单位
              ├─ SetUnitTimeScalePercent: 选取单位(), 100.00
              └─ PauseUnit: 选取单位(), PauseUnpauseOptionUnpause
            删除单位组 TDQL_DWZ
            杀死 TDQL_DW
            关闭触发器 当前触发器()
```

### 剑尊

```text
触发器: 剑尊 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### JZ0

```text
触发器: JZ0 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.20)
条件
  └─ 无
动作
  ├─ 循环整数A 1→5
  │    └─ 如果
  │         ├─ 条件: 单位有魔法效果(YX_7[循环整数A()], B006) == TRUE
  │         ├─ 则
  │         │    设置 X_dian = (YX_7[循环整数A()]的位置)
  │         │    设置 X_danweizu = GetRandomSubGroup(1, 范围内符合条件的单位(512, X_dian, (布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true) 且 布尔比较(是敌方单位(过滤单位(), (YX_7[循环整数A()]的所有者)), OperatorEqualENE, true))))
  │         │    清除点 X_dian
  │         │    单位组: 选取 X_danweizu 中所有单位
  │         │      ├─ 设置 X_dian = (选取单位()的位置)
  │         │      ├─ 移动单位: YX_7[循环整数A()], X_dian
  │         │      ├─ 播放动画: YX_7[循环整数A()], "attack slam"
  │         │      ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 单位X坐标(选取单位()), 单位Y坐标(选取单位()))
  │         │      ├─ 伤害目标: YX_7[循环整数A()], 选取单位(), ((随机[2~((英雄等级(YX_7[循环整数A()]) / 10) + 9)]转实数) x (英雄属性(HeroStatAgi, YX_7[循环整数A()], InclusionInclude)转实数)), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WeaponTypeMetalHeavySlice
  │         │      └─ 清除点 X_dian
  │         │    删除单位组 X_danweizu
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位有魔法效果(YX_7[1], B006) == TRUE
       │    ├─ 单位有魔法效果(YX_7[2], B006) == TRUE
       │    ├─ 单位有魔法效果(YX_7[3], B006) == TRUE
       │    ├─ 单位有魔法效果(YX_7[4], B006) == TRUE
       │    ├─ 单位有魔法效果(YX_7[5], B006) == TRUE
       ├─ 则
       │    关闭触发器 当前触发器()
       └─ 否则: (无)
```

### 空间之刃

```text
触发器: 空间之刃 (初始化) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### A20

```text
触发器: A20 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.10)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: WP_XTR_ZS OperatorGreater 0
       ├─ 则
       │    设置 WP_XTR_ZS = (WP_XTR_ZS - 1)
       │    SetUnitFlyHeightBJ: 创建单位(指定坐标)(非玩家, o001, 单位X坐标(WP_XTR[2]), 单位Y坐标(WP_XTR[2]), (随机[45~315]转实数)), GetUnitFlyHeight(WP_XTR[2]), 2400.00
       │    伤害目标: WP_XTR[1], WP_XTR[2], ((英雄等级(WP_XTR[1]) x 12345)转实数), IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
       └─ 否则
            关闭触发器 当前触发器()
```

### B1

```text
触发器: B1 (玩家/英雄) [✓] — 初始化
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ DialogDisplay: Player00, duihua, ShowHideShow
  ├─ 设置单位归属: gg_unit_e00N_0040, PlayerNV, 不改变颜色
  ├─ 播放动画: gg_unit_ubon_0001, "birth"
  ├─ 设置 X_danweizu = 区域内全部单位(可用地图区域())
  ├─ 单位组: 选取 X_danweizu 中所有单位
  │    ├─ 添加事件到 gg_trg_A1: 注册单位事件(选取单位(), UnitEventDamaged)
  │    └─ 添加事件到 gg_trg_A5: 注册单位事件(选取单位(), UnitEventDamaged)
  ├─ 删除单位组 X_danweizu
  ├─ 循环整数A 1→13
  │    └─ 添加事件到 gg_trg_E14: 计时器到期(FH_YGJSQ[循环整数A()])
  ├─ SetPlayerFlag: 玩家6(橙), PlayerFlagGivesBounty, OnOffIntOn
  ├─ CreateMultiboardBJ: 5, 6, "TRIGSTR_9740"
  ├─ 排行榜 最后创建的排行榜()[1,1] = "TRIGSTR_9744"
  ├─ 排行榜 最后创建的排行榜()[2,1] = "TRIGSTR_9745"
  ├─ 排行榜 最后创建的排行榜()[3,1] = "TRIGSTR_9746"
  ├─ 排行榜 最后创建的排行榜()[4,1] = "TRIGSTR_9747"
  ├─ 排行榜 最后创建的排行榜()[5,1] = "TRIGSTR_9748"
  ├─ MultiboardSetItemStyleBJ: 最后创建的排行榜(), 0, 0, ShowHideShow, ShowHideShow
  ├─ 循环整数A 1→6
  │    ├─ MultiboardSetItemIconBJ: 最后创建的排行榜(), 1, (循环整数A() + 1), ReplaceableTextures\CommandButtons\BTNLament.blp
  │    ├─ MultiboardSetItemIconBJ: 最后创建的排行榜(), 2, (循环整数A() + 1), ReplaceableTextures\CommandButtons\BTNArcaniteMelee.blp
  │    ├─ MultiboardSetItemIconBJ: 最后创建的排行榜(), 3, (循环整数A() + 1), ReplaceableTextures\CommandButtons\BTNCannibalize.blp
  │    ├─ MultiboardSetItemIconBJ: 最后创建的排行榜(), 4, (循环整数A() + 1), ReplaceableTextures\WorldEditUI\Doodad-Destructible.blp
  │    ├─ MultiboardSetItemIconBJ: 最后创建的排行榜(), 5, (循环整数A() + 1), ReplaceableTextures\CommandButtons\BTNUrnOfKelThuzad.blp
  │    └─ ForLoopBMultiple: 1, 6
  ├─ 等待 2.00s
  ├─ MultiboardDisplayBJ: ShowHideShow, 最后创建的排行榜()
  ├─ 设置 D_lj[1] = (区域gg_rct______________010中心)
  ├─ 设置 D_lj[2] = (区域gg_rct______________013中心)
  ├─ 设置 D_lj[3] = (区域gg_rct______________011中心)
  ├─ 设置 D_lj[4] = (区域gg_rct______________012中心)
  ├─ 设置 dian1 = Location(0, -5000.00)
  ├─ 设置 LV[1] = hfoo
  ├─ 设置 LV[2] = hkni
  ├─ 设置 LV[3] = hrif
  ├─ 设置 LV[4] = hmtm
  ├─ 设置 LV[5] = hgyr
  ├─ 设置 LV[6] = hgry
  ├─ 设置 LV[7] = hmpr
  ├─ 设置 LV[8] = hsor
  ├─ 设置 LV[9] = hmtt
  ├─ 设置 LV[10] = hspt
  ├─ 设置 LV[11] = hdhw
  ├─ 设置 LV[12] = nnsw
  ├─ 设置 LV[13] = nnmg
  ├─ 设置 LV[14] = nwgs
  ├─ 设置 LV[15] = nsnp
  ├─ 设置 LV[16] = nmyr
  ├─ 设置 LV[17] = nnrg
  ├─ 设置 LV[18] = nhyc
  ├─ 设置 LV[19] = ogru
  ├─ 设置 LV[20] = orai
  ├─ 设置 LV[21] = otau
  ├─ 设置 LV[22] = ohun
  ├─ 设置 LV[23] = ocat
  ├─ 设置 LV[24] = okod
  ├─ 设置 LV[25] = oshm
  ├─ 设置 LV[26] = earc
  ├─ 设置 LV[27] = esen
  ├─ 设置 LV[28] = edry
  ├─ 设置 LV[29] = ebal
  ├─ 设置 LV[30] = ehip
  ├─ 设置 LV[31] = echm
  ├─ 设置 LV[32] = edot
  ├─ 设置 LV[33] = edoc
  ├─ 设置 LV[34] = emtg
  ├─ 设置 LV[35] = efdr
  ├─ 设置 LV[36] = u005
  ├─ 设置 WP_SHC[1] = I01D
  ├─ 设置 WP_SHC[2] = I01A
  ├─ 设置 WP_SHC[3] = I01B
  ├─ 设置 WP_SHC[4] = I01C
  ├─ 设置 WP_SHC[5] = I019
  ├─ 设置 WP_SY[1] = I01I
  ├─ 设置 WP_SY[2] = I01J
  ├─ 设置 WP_SY[3] = I01K
  ├─ 设置 WP_SY[4] = I01L
  ├─ 设置 WP_SY[5] = I01M
  ├─ 设置 WP_SYMJ[1] = I029
  ├─ 设置 WP_SYMJ[2] = I02A
  ├─ 设置 WP_SYMJ[3] = I028
  ├─ 设置 WP_SYMJ[4] = I027
  └─ 设置 WP_SYMJ[5] = I026
```

### B2

```text
触发器: B2 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ FogEnableOn
  ├─ MeleeStartingHeroLimit
  ├─ 设置无敌: gg_unit_Uclc_0123, InvulnerabilityInvulnerable
  ├─ 添加物品: I03Q, gg_unit_Uclc_0123
  ├─ 设置 YX_7[13] = gg_unit_E00K_0041
  ├─ 设置 YX_7[7] = gg_unit_Uclc_0123
  ├─ SetPlayerAbilityAvailable: 非玩家, A05N, EnableDisableDisable
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1614", "TRIGSTR_1615", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_221", "TRIGSTR_1301", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_717", "TRIGSTR_718", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 设置 RW_5[1] = GetLastCreatedQuestBJ()
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_720", "TRIGSTR_725", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 设置 RW_5[2] = GetLastCreatedQuestBJ()
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_727", "TRIGSTR_728", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 设置 RW_5[3] = GetLastCreatedQuestBJ()
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_988", "TRIGSTR_990", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 设置 RW_5[4] = GetLastCreatedQuestBJ()
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_1568", "TRIGSTR_1582", ReplaceableTextures\CommandButtons\BTNAmbush.blp
  ├─ 设置 RW_5[5] = GetLastCreatedQuestBJ()
  ├─ 循环整数A 1→5
  │    ├─ SetPlayerMaxHeroesAllowed: 1, 玩家循环整数A()
  │    ├─ ForceAddPlayerSimple: 玩家循环整数A(), DY_WJZ
  │    ├─ 设置玩家属性: 玩家循环整数A(), 人口上限, 5
  │    ├─ 设置玩家属性: 玩家循环整数A(), PlayerStateGold, 10000
  │    ├─ SetPlayerAbilityAvailable: 玩家循环整数A(), A05N, EnableDisableDisable
  │    ├─ SetPlayerAbilityAvailable: 玩家循环整数A(), A071, EnableDisableDisable
  │    ├─ SetPlayerAllianceStateBJ: 玩家11(暗绿), 玩家循环整数A(), AllianceSettingAlliedUnits
  │    ├─ SetPlayerAllianceStateBJ: 玩家循环整数A(), 玩家11(暗绿), AllianceSettingAlliedUnits
  │    └─ 添加事件到 gg_trg____________________002: TriggerRegisterPlayerStateEvent(玩家循环整数A(), PlayerStateLumber, LimitOpGreaterThanOrEqual, 1.00)
  ├─ 循环整数A 1→6
  │    └─ 添加事件到 gg_trg_C7: 计时器到期(YX_FH[循环整数A()])
  ├─ ClearTextMessages
  ├─ SetPlayerAllianceStateBJ: 玩家6(橙), PlayerNA, AllianceSettingAllied
  ├─ SetPlayerAllianceStateBJ: 玩家6(橙), PlayerNV, AllianceSettingAllied
  ├─ SetPlayerAllianceStateBJ: PlayerNA, 玩家6(橙), AllianceSettingAllied
  ├─ SetPlayerAllianceStateBJ: 玩家11(暗绿), 玩家6(橙), AllianceSettingUnallied
  ├─ SetPlayerAllianceStateBJ: 玩家11(暗绿), 玩家5(黄), AllianceSettingAlliedUnits
  ├─ 设置 玩家11(暗绿) 名字 = "TRIGSTR_1056"
  ├─ AddSpecialEffectTargetUnitBJ: "origin", gg_unit_ubon_0001, TimeAura.mdx
  ├─ 设置 X_danweizu = GetUnitsOfTypeIdAll(uaco)
  ├─ 单位组: 选取 X_danweizu 中所有单位
  │    └─ 添加事件到 gg_trg_C10: 注册单位进入范围事件(25.00, 选取单位())
  └─ 删除单位组 X_danweizu
```

### 英雄选择

```text
触发器: 英雄选择 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### C2

```text
触发器: C2 (剧情/任务) [✓] — 英雄选择
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 出售单位
条件
  └─ 单位类型判断(被贩卖单位(), 英雄) == TRUE
动作
  ├─ 设置 BL5[玩家号((被贩卖单位()的所有者))] = 创建单位(指定坐标)((被贩卖单位()的所有者), ufro, 单位X坐标(购买单位()), 单位Y坐标(购买单位()), 0)
  ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Human\MassTeleport\MassTeleportTarget.mdl, 被贩卖单位(), "origin")
  ├─ 设置 (被贩卖单位()的所有者) 名字 = "[" + (玩家名:(被贩卖单位()的所有者)) + "]" + GetHeroProperName(被贩卖单位())
  ├─ 设置 YX_7[玩家号((被贩卖单位()的所有者))] = 被贩卖单位()
  ├─ PingMinimapLocForForceEx: DY_WJZ, Location(1600.00, -6800.00), 2.00, MinimapPingStyleSimple, 0.00, 100, 100
  ├─ 排行榜 最后创建的排行榜()[1,(玩家号((被贩卖单位()的所有者)) + 1)] = (玩家名:(被贩卖单位()的所有者))
  └─ 如果
       ├─ 条件: (被贩卖单位()类型ID) == N00B
       ├─ 则
       │    添加物品: I03L, 触发单位()
       └─ 否则
            如果
              ├─ 条件: (被贩卖单位()类型ID) == N00D
              ├─ 则
              │    AddSpecialEffectTargetUnitBJ: "sprite first", 被贩卖单位(), Abilities\Weapons\IllidanMissile\IllidanMissile.mdl
              │    AddSpecialEffectTargetUnitBJ: "sprite second", 被贩卖单位(), Abilities\Weapons\IllidanMissile\IllidanMissile.mdl
              │    AddSpecialEffectTargetUnitBJ: "sprite third", 被贩卖单位(), Abilities\Weapons\IllidanMissile\IllidanMissile.mdl
              │    AddSpecialEffectTargetUnitBJ: "chest", 被贩卖单位(), Abilities\Spells\Items\AIso\BIsvTarget.mdl
              └─ 否则: (无)
```

### 英雄回城

```text
触发器: 英雄回城 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### C3

```text
触发器: C3 (剧情/任务) [✓] — 回城
───────────────────────────────────────────────────────
事件
  ├─ 玩家 Player00 输入 "hg"
  ├─ 玩家 玩家1(红) 输入 "hg"
  ├─ 玩家 玩家2(蓝) 输入 "hg"
  ├─ 玩家 玩家3(青) 输入 "hg"
  └─ 玩家 玩家4(紫) 输入 "hg"
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位是否暂停(YX_7[玩家号(触发玩家())]) == TRUE
       │    ├─ 单位持有物品类型(YX_7[玩家号(触发玩家())], I02S) == TRUE
       │    ├─ 单位有魔法效果(YX_7[玩家号(触发玩家())], B00J) == TRUE
       ├─ 则
       │    移动单位: YX_7[玩家号(触发玩家())], dian1
       │    平移镜头: 触发玩家(), dian1, 0
       └─ 否则
            显示文本→触发玩家(): 0
```

### C10

```text
触发器: C10 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 玩家控制者比较(玩家控制者类型((触发单位()的所有者)), OperatorEqualENE, MapControlUser)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  ├─ 移动单位: 触发单位(), dian1
  ├─ 平移镜头: (触发单位()的所有者), dian1, 0
  └─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
```

### 英雄复活

```text
触发器: 英雄复活 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### C4

```text
触发器: C4 (剧情/任务) [✓] — 死亡复活
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ IsUnitAlly(触发单位(), 玩家5(黄)) == TRUE
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 单位持有物品类型(触发单位(), I02Z) == TRUE
  │    ├─ 则
  │    │    运行计时器 YX_FH[玩家号((触发单位()的所有者))] (一次性, 7.00s)
  │    └─ 否则
  │         如果
  │           ├─ 条件: 触发单位() == YX_7[6]
  │           ├─ 则
  │           │    运行计时器 YX_FH[6] (一次性, 60.00s)
  │           └─ 否则
  │                如果
  │                  ├─ 条件: 单位技能等级(A03D, 触发单位()) == 1
  │                  ├─ 则
  │                  │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.05)
  │                  └─ 否则: (无)
  │                运行计时器 YX_FH[玩家号((触发单位()的所有者))] (一次性, 15.00s)
  ├─ 设置 DMB_ZW[玩家号((触发单位()的所有者))] = (DMB_ZW[玩家号((触发单位()的所有者))] + 1)
  └─ 排行榜 最后创建的排行榜()[5,(玩家号((触发单位()的所有者)) + 1)] = (DMB_ZW[玩家号((触发单位()的所有者))]转字符串)
```

### C7

```text
触发器: C7 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 循环整数A 1→6
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, YX_FH[循环整数A()])
            ├─ 则
            │    设置 X_dian = Location(0, -6500.00)
            │    平移镜头: 玩家循环整数A(), X_dian, 0
            │    清除点 X_dian
            │    复活英雄: YX_7[循环整数A()], 0, -6500.00, ShowHideShow
            │    CustomScriptCode: ScriptCode00
            └─ 否则: (无)
```

### 钱木

```text
触发器: 钱木 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### C5

```text
触发器: C5 (剧情/任务) [✓] — 钱满换木头
───────────────────────────────────────────────────────
事件
  ├─ TriggerRegisterPlayerStateEvent(Player00, PlayerStateGold, LimitOpGreaterThanOrEqual, 1000000.00)
  ├─ TriggerRegisterPlayerStateEvent(玩家1(红), PlayerStateGold, LimitOpGreaterThanOrEqual, 1000000.00)
  ├─ TriggerRegisterPlayerStateEvent(玩家3(青), PlayerStateGold, LimitOpGreaterThanOrEqual, 1000000.00)
  ├─ TriggerRegisterPlayerStateEvent(玩家2(蓝), PlayerStateGold, LimitOpGreaterThanOrEqual, 1000000.00)
  └─ TriggerRegisterPlayerStateEvent(玩家4(紫), PlayerStateGold, LimitOpGreaterThanOrEqual, 1000000.00)
条件
  └─ 无
动作
  ├─ 设置玩家属性: 触发玩家(), PlayerStateGold, 100000
  ├─ 调整 触发玩家() 的 PlayerStateLumber: 90
  └─ 显示文本→触发玩家(): 0
```

### 等级提升

```text
触发器: 等级提升 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### C6

```text
触发器: C6 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Level
条件
  └─ 玩家控制者比较(玩家控制者类型((触发单位()的所有者)), OperatorEqualENE, MapControlUser)
动作
  ├─ 循环整数A 1→6
  │    └─ 如果
  │         ├─ 条件: 物品类型比较(物品类型ID(单位栏位物品(触发单位(), 循环整数A())), OperatorEqualENE, I03E)
  │         ├─ 则
  │         │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd28
  │         │    修改 触发单位() 的HeroStatAgi: ModifyMethodAdd20
  │         │    修改 触发单位() 的HeroStatInt: ModifyMethodAdd20
  │         └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家科技等级(Rhan, (触发单位()的所有者)) OperatorLess (英雄等级(触发单位()) / 3)
  │    ├─ 则
  │    │    SetPlayerTechResearchedSwap: Rhan, (玩家科技等级(Rhan, (触发单位()的所有者)) + 1), (触发单位()的所有者)
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 玩家科技等级(Rhfs, (触发单位()的所有者)) == 1
       ├─ 则
       │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.01)
       │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.01)
       │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.01)
       └─ 否则: (无)
```

### D1

```text
触发器: D1 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ OperatorCompareItemType(GetItemType(被操作物品()), OperatorEqualENE, ItemTypeArtifact)
动作
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I041)
       ├─ 则
       │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.40)
       │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.40)
       │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.40)
       └─ 否则
            如果
              ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02Z)
              ├─ 则
              │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.75)
              │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.75)
              │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.75)
              └─ 否则
                   如果
                     ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I03M)
                     ├─ 则
                     │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 1.00)
                     │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 1.00)
                     │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 1.00)
                     └─ 否则
                          如果
                            ├─ 条件: 任一成立
                            ├─ 则
                            │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd(英雄等级(触发单位()) x 8)
                            │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.25)
                            │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.25)
                            │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.25)
                            └─ 否则
                                 如果
                                   ├─ 条件: 任一成立
                                   ├─ 则
                                   │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 1.25)
                                   │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 1.25)
                                   │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 1.25)
                                   └─ 否则
                                        如果
                                          ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I03L)
                                          ├─ 则
                                          │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.50)
                                          └─ 否则: (无)
```

### D2

```text
触发器: D2 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroDropItem
条件
  ├─ OperatorCompareItemType(GetItemType(被操作物品()), OperatorEqualENE, ItemTypeArtifact)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I041)
       ├─ 则
       │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] - 0.40)
       │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] - 0.40)
       │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 0.40)
       └─ 否则
            如果
              ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02Z)
              ├─ 则
              │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] - 0.75)
              │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] - 0.75)
              │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 0.75)
              └─ 否则
                   如果
                     ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I03M)
                     ├─ 则
                     │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] - 1.00)
                     │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] - 1.00)
                     │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 1.00)
                     └─ 否则
                          如果
                            ├─ 条件: 任一成立
                            ├─ 则
                            │    修改 触发单位() 的HeroStatStr: ModifyMethodSub(英雄等级(触发单位()) x 8)
                            │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] - 0.25)
                            │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] - 0.25)
                            │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 0.25)
                            └─ 否则
                                 如果
                                   ├─ 条件: 任一成立
                                   ├─ 则
                                   │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] - 1.25)
                                   │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] - 1.25)
                                   │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 1.25)
                                   └─ 否则
                                        如果
                                          ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I03L)
                                          ├─ 则
                                          │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] - 0.50)
                                          └─ 否则: (无)
```

### D11

```text
触发器: D11 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ OperatorCompareItemType(GetItemType(被操作物品()), OperatorEqualENE, ItemTypeArtifact)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 循环整数A 1→6
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 物品类型比较(物品类型ID(单位栏位物品(触发单位(), 循环整数A())), OperatorEqualENE, 物品类型ID(被操作物品()))
  │         │    ├─ 物品比较(单位栏位物品(触发单位(), 循环整数A()), OperatorNotEqualENE, 被操作物品())
  │         ├─ 则
  │         │    UnitRemoveItemSwapped: 被操作物品(), 触发单位()
  │         │    显示文本→(触发单位()的所有者): 0
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位持有物品类型(触发单位(), I013) == TRUE
       │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00Y)
       ├─ 则
       │    UnitRemoveItemSwapped: 被操作物品(), 触发单位()
       │    显示文本→(触发单位()的所有者): 0
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ 单位持有物品类型(触发单位(), I00Y) == TRUE
              │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I013)
              ├─ 则
              │    UnitRemoveItemSwapped: 被操作物品(), 触发单位()
              │    显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: 全部成立
                     │    ├─ 单位持有物品类型(触发单位(), I03D) == TRUE
                     │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I014)
                     ├─ 则
                     │    UnitRemoveItemSwapped: 被操作物品(), 触发单位()
                     │    显示文本→(触发单位()的所有者): 0
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 单位持有物品类型(触发单位(), I014) == TRUE
                            │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I03D)
                            ├─ 则
                            │    UnitRemoveItemSwapped: 被操作物品(), 触发单位()
                            │    显示文本→(触发单位()的所有者): 0
                            └─ 否则: (无)
```

### D12

```text
触发器: D12 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02S)
  └─ 触发单位() == BL5[玩家号((触发单位()的所有者))]
动作
  ├─ 删除物品: 被操作物品()
  └─ 显示文本→(触发单位()的所有者): 0
```

### 升级基地

```text
触发器: 升级基地 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### D3

```text
触发器: D3 (技能/物品) [✓] — 基地升级
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I000)
动作
  └─ 如果
       ├─ 条件: 玩家科技等级(Rhan, 玩家5(黄)) OperatorLess 100
       ├─ 则
       │    删除物品: 被操作物品()
       │    循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, (玩家名:(触发单位()的所有者)) + "强化了埋骨地的防御能力。")
       │    SetPlayerTechResearchedSwap: Rhan, (玩家科技等级(Rhan, 玩家5(黄)) + 1), 玩家5(黄)
       └─ 否则
            调整 触发玩家() 的 PlayerStateLumber: 25
            删除物品: 被操作物品()
            显示文本→触发玩家(): 0
```

### 初级装备升级

```text
触发器: 初级装备升级 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### D4

```text
触发器: D4 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00H)
  │    ├─ 则
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Charm\CharmTarget.mdl, 触发单位(), "origin")
  │    │    如果
  │    │      ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I003)) == TRUE
  │    │      ├─ 则
  │    │      │    删除物品: 单位携带物品(按类型)(触发单位(), I003)
  │    │      │    添加物品: I004, 触发单位()
  │    │      │    显示文本→触发玩家(): 0
  │    │      └─ 否则
  │    │           如果
  │    │             ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I004)) == TRUE
  │    │             ├─ 则
  │    │             │    删除物品: 单位携带物品(按类型)(触发单位(), I004)
  │    │             │    添加物品: I005, 触发单位()
  │    │             │    显示文本→触发玩家(): 0
  │    │             └─ 否则
  │    │                  如果
  │    │                    ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I005)) == TRUE
  │    │                    ├─ 则
  │    │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I005)
  │    │                    │    添加物品: I006, 触发单位()
  │    │                    │    显示文本→触发玩家(): 0
  │    │                    └─ 否则
  │    │                         如果
  │    │                           ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I006)) == TRUE
  │    │                           ├─ 则
  │    │                           │    删除物品: 单位携带物品(按类型)(触发单位(), I006)
  │    │                           │    添加物品: I002, 触发单位()
  │    │                           │    显示文本→触发玩家(): 0
  │    │                           │    PingMinimap: -3500.00, -6000.00, 3.00
  │    │                           └─ 否则
  │    │                                调整 触发玩家() 的 PlayerStateLumber: 10
  │    │                                显示文本→触发玩家(): 0
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00I)
  │    ├─ 则
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Charm\CharmTarget.mdl, 触发单位(), "origin")
  │    │    如果
  │    │      ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I008)) == TRUE
  │    │      ├─ 则
  │    │      │    删除物品: 单位携带物品(按类型)(触发单位(), I008)
  │    │      │    添加物品: I009, 触发单位()
  │    │      │    显示文本→触发玩家(): 0
  │    │      └─ 否则
  │    │           如果
  │    │             ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I009)) == TRUE
  │    │             ├─ 则
  │    │             │    删除物品: 单位携带物品(按类型)(触发单位(), I009)
  │    │             │    添加物品: I00A, 触发单位()
  │    │             │    显示文本→触发玩家(): 0
  │    │             └─ 否则
  │    │                  如果
  │    │                    ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00A)) == TRUE
  │    │                    ├─ 则
  │    │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I00A)
  │    │                    │    添加物品: I00B, 触发单位()
  │    │                    │    显示文本→触发玩家(): 0
  │    │                    └─ 否则
  │    │                         如果
  │    │                           ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00B)) == TRUE
  │    │                           ├─ 则
  │    │                           │    删除物品: 单位携带物品(按类型)(触发单位(), I00B)
  │    │                           │    添加物品: I007, 触发单位()
  │    │                           │    显示文本→触发玩家(): 0
  │    │                           │    PingMinimap: -3500.00, -6000.00, 3.00
  │    │                           └─ 否则
  │    │                                调整 触发玩家() 的 PlayerStateLumber: 10
  │    │                                显示文本→触发玩家(): 0
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00J)
  │    ├─ 则
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Charm\CharmTarget.mdl, 触发单位(), "origin")
  │    │    如果
  │    │      ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00C)) == TRUE
  │    │      ├─ 则
  │    │      │    删除物品: 单位携带物品(按类型)(触发单位(), I00C)
  │    │      │    添加物品: I00D, 触发单位()
  │    │      │    显示文本→触发玩家(): 0
  │    │      └─ 否则
  │    │           如果
  │    │             ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00D)) == TRUE
  │    │             ├─ 则
  │    │             │    删除物品: 单位携带物品(按类型)(触发单位(), I00D)
  │    │             │    添加物品: I00E, 触发单位()
  │    │             │    显示文本→触发玩家(): 0
  │    │             └─ 否则
  │    │                  如果
  │    │                    ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00E)) == TRUE
  │    │                    ├─ 则
  │    │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I00E)
  │    │                    │    添加物品: I00F, 触发单位()
  │    │                    │    显示文本→触发玩家(): 0
  │    │                    └─ 否则
  │    │                         如果
  │    │                           ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00F)) == TRUE
  │    │                           ├─ 则
  │    │                           │    删除物品: 单位携带物品(按类型)(触发单位(), I00F)
  │    │                           │    添加物品: I00G, 触发单位()
  │    │                           │    显示文本→触发玩家(): 0
  │    │                           │    PingMinimap: -3500.00, -6000.00, 3.00
  │    │                           └─ 否则
  │    │                                调整 触发玩家() 的 PlayerStateLumber: 10
  │    │                                显示文本→触发玩家(): 0
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01E)
       ├─ 则
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Charm\CharmTarget.mdl, 触发单位(), "origin")
       │    如果
       │      ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I00Z)) == TRUE
       │      ├─ 则
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I00Z)
       │      │    添加物品: I012, 触发单位()
       │      │    显示文本→触发玩家(): 0
       │      └─ 否则
       │           如果
       │             ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I012)) == TRUE
       │             ├─ 则
       │             │    删除物品: 单位携带物品(按类型)(触发单位(), I012)
       │             │    添加物品: I011, 触发单位()
       │             │    显示文本→触发玩家(): 0
       │             └─ 否则
       │                  如果
       │                    ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I011)) == TRUE
       │                    ├─ 则
       │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I011)
       │                    │    添加物品: I010, 触发单位()
       │                    │    显示文本→触发玩家(): 0
       │                    └─ 否则
       │                         如果
       │                           ├─ 条件: 物品有归属(单位携带物品(按类型)(触发单位(), I010)) == TRUE
       │                           ├─ 则
       │                           │    删除物品: 单位携带物品(按类型)(触发单位(), I010)
       │                           │    添加物品: I024, 触发单位()
       │                           │    显示文本→触发玩家(): 0
       │                           │    PingMinimap: -3500.00, -6000.00, 3.00
       │                           └─ 否则
       │                                调整 触发玩家() 的 PlayerStateLumber: 20
       │                                显示文本→触发玩家(): 0
       └─ 否则: (无)
```

### 进入各种地点

```text
触发器: 进入各种地点 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 017

```text
触发器: 未命名触发器 017 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00Q)
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    平移镜头: (触发单位()的所有者), D_lj[1], 0
  │    │    移动单位: 触发单位(), D_lj[1]
  │    │    删除物品: 被操作物品()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00L)
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    平移镜头: (触发单位()的所有者), D_lj[2], 0
  │    │    移动单位: 触发单位(), D_lj[2]
  │    │    删除物品: 被操作物品()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00K)
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    平移镜头: (触发单位()的所有者), D_lj[3], 0
  │    │    移动单位: 触发单位(), D_lj[3]
  │    │    删除物品: 被操作物品()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00N)
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    平移镜头: (触发单位()的所有者), D_lj[4], 0
  │    │    移动单位: 触发单位(), D_lj[4]
  │    │    删除物品: 被操作物品()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02O)
  │    ├─ 则
  │    │    设置 X_dian = Location(5000.00, 1700.00)
  │    │    移动单位: 触发单位(), X_dian
  │    │    平移镜头: (触发单位()的所有者), X_dian, 0
  │    │    清除点 X_dian
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01V)
  │    ├─ 则
  │    │    设置 X_dian = Location(-7000.00, 4500.00)
  │    │    移动单位: 触发单位(), X_dian
  │    │    平移镜头: (触发单位()的所有者), X_dian, 0
  │    │    清除点 X_dian
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02C)
  │    ├─ 则
  │    │    移动单位: 触发单位(), 5400.00, -6200.00
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01U)
       ├─ 则
       │    设置 X_dian = Location(-6000.00, -6000.00)
       │    移动单位: 触发单位(), X_dian
       │    平移镜头: (触发单位()的所有者), X_dian, 0
       │    清除点 X_dian
       │    返回
       └─ 否则: (无)
```

### 中级武器升级

```text
触发器: 中级武器升级 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 022

```text
触发器: 未命名触发器 022 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 单位持有物品(触发单位(), 技能目标物品()) == TRUE
动作
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A02M)
       ├─ 则
       │    如果
       │      ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SY[1])
       │      ├─ 则
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I01N)
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SY[1])
       │      │    添加物品: WP_SY[2], 触发单位()
       │      └─ 否则
       │           如果
       │             ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SYMJ[1])
       │             ├─ 则
       │             │    删除物品: 单位携带物品(按类型)(触发单位(), I01N)
       │             │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SYMJ[1])
       │             │    添加物品: WP_SYMJ[2], 触发单位()
       │             └─ 否则
       │                  如果
       │                    ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SHC[1])
       │                    ├─ 则
       │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I01N)
       │                    │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SHC[1])
       │                    │    添加物品: WP_SHC[2], 触发单位()
       │                    └─ 否则: (无)
       └─ 否则
            如果
              ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A02N)
              ├─ 则
              │    如果
              │      ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SY[2])
              │      ├─ 则
              │      │    删除物品: 单位携带物品(按类型)(触发单位(), I01O)
              │      │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SY[2])
              │      │    添加物品: WP_SY[3], 触发单位()
              │      └─ 否则
              │           如果
              │             ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SYMJ[2])
              │             ├─ 则
              │             │    删除物品: 单位携带物品(按类型)(触发单位(), I01O)
              │             │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SYMJ[2])
              │             │    添加物品: WP_SYMJ[3], 触发单位()
              │             └─ 否则
              │                  如果
              │                    ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SHC[2])
              │                    ├─ 则
              │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I01O)
              │                    │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SHC[2])
              │                    │    添加物品: WP_SHC[3], 触发单位()
              │                    └─ 否则
              │                         显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A02O)
                     ├─ 则
                     │    如果
                     │      ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SY[3])
                     │      ├─ 则
                     │      │    删除物品: 单位携带物品(按类型)(触发单位(), I01P)
                     │      │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SY[3])
                     │      │    添加物品: WP_SY[4], 触发单位()
                     │      └─ 否则
                     │           如果
                     │             ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SYMJ[3])
                     │             ├─ 则
                     │             │    删除物品: 单位携带物品(按类型)(触发单位(), I01P)
                     │             │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SYMJ[3])
                     │             │    添加物品: WP_SYMJ[4], 触发单位()
                     │             └─ 否则
                     │                  如果
                     │                    ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SHC[3])
                     │                    ├─ 则
                     │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I01P)
                     │                    │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SHC[3])
                     │                    │    添加物品: WP_SHC[4], 触发单位()
                     │                    └─ 否则: (无)
                     └─ 否则
                          如果
                            ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A02L)
                            ├─ 则
                            │    如果
                            │      ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SY[4])
                            │      ├─ 则
                            │      │    删除物品: 单位携带物品(按类型)(触发单位(), I01Q)
                            │      │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SY[4])
                            │      │    添加物品: WP_SY[5], 触发单位()
                            │      └─ 否则
                            │           如果
                            │             ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SYMJ[4])
                            │             ├─ 则
                            │             │    删除物品: 单位携带物品(按类型)(触发单位(), I01Q)
                            │             │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SYMJ[4])
                            │             │    添加物品: WP_SYMJ[5], 触发单位()
                            │             └─ 否则
                            │                  如果
                            │                    ├─ 条件: 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, WP_SHC[4])
                            │                    ├─ 则
                            │                    │    删除物品: 单位携带物品(按类型)(触发单位(), I01Q)
                            │                    │    删除物品: 单位携带物品(按类型)(触发单位(), WP_SHC[4])
                            │                    │    添加物品: WP_SHC[5], 触发单位()
                            │                    └─ 否则
                            │                         显示文本→(触发单位()的所有者): 0
                            └─ 否则: (无)
```

### 装备合成

```text
触发器: 装备合成 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 023

```text
触发器: 未命名触发器 023 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01Z)
       ├─ 则
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 触发单位(), "origin")
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 单位持有物品类型(触发单位(), I00G) == TRUE
       │      │    ├─ 单位持有物品类型(触发单位(), I03O) == TRUE
       │      ├─ 则
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I00G)
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I03O)
       │      │    添加物品: I01D, 触发单位()
       │      │    显示文本→触发玩家(): 0
       │      └─ 否则
       │           调整 触发玩家() 的 PlayerStateLumber: 50
       │           显示文本→触发玩家(): 0
       └─ 否则
            如果
              ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I020)
              ├─ 则
              │    销毁特效 创建特效(附着单位)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 触发单位(), "origin")
              │    如果
              │      ├─ 条件: 全部成立
              │      │    ├─ 单位持有物品类型(触发单位(), I002) == TRUE
              │      │    ├─ 单位持有物品类型(触发单位(), I007) == TRUE
              │      │    ├─ 单位持有物品类型(触发单位(), I03O) == TRUE
              │      ├─ 则
              │      │    删除物品: 单位携带物品(按类型)(触发单位(), I03O)
              │      │    删除物品: 单位携带物品(按类型)(触发单位(), I007)
              │      │    删除物品: 单位携带物品(按类型)(触发单位(), I002)
              │      │    添加物品: I01I, 触发单位()
              │      │    显示文本→触发玩家(): 0
              │      └─ 否则
              │           调整 触发玩家() 的 PlayerStateLumber: 50
              │           显示文本→触发玩家(): 0
              └─ 否则
                   如果
                     ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02B)
                     ├─ 则
                     │    销毁特效 创建特效(附着单位)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 触发单位(), "origin")
                     │    如果
                     │      ├─ 条件: 全部成立
                     │      │    ├─ 单位持有物品类型(触发单位(), I024) == TRUE
                     │      │    ├─ 单位持有物品类型(触发单位(), I03O) == TRUE
                     │      ├─ 则
                     │      │    删除物品: 单位携带物品(按类型)(触发单位(), I03O)
                     │      │    删除物品: 单位携带物品(按类型)(触发单位(), I024)
                     │      │    添加物品: I029, 触发单位()
                     │      │    显示文本→触发玩家(): 0
                     │      └─ 否则
                     │           调整 触发玩家() 的 PlayerStateLumber: 50
                     │           显示文本→触发玩家(): 0
                     └─ 否则
                          如果
                            ├─ 条件: 全部成立
                            │    ├─ 单位持有物品类型(触发单位(), I02N) == TRUE
                            │    ├─ 单位持有物品类型(触发单位(), I041) == TRUE
                            │    ├─ 单位持有物品类型(触发单位(), I03B) == TRUE
                            ├─ 则
                            │    删除物品: 单位携带物品(按类型)(触发单位(), I041)
                            │    删除物品: 单位携带物品(按类型)(触发单位(), I02N)
                            │    删除物品: 单位携带物品(按类型)(触发单位(), I03B)
                            │    添加物品: I02Z, 触发单位()
                            └─ 否则
                                 如果
                                   ├─ 条件: 全部成立
                                   │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02J)) == TRUE
                                   │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02L)) == TRUE
                                   │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02I)) == TRUE
                                   │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02M)) == TRUE
                                   ├─ 则
                                   │    销毁特效 创建特效(附着单位)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 触发单位(), "origin")
                                   │    删除物品: 单位携带物品(按类型)(触发单位(), I02J)
                                   │    删除物品: 单位携带物品(按类型)(触发单位(), I02L)
                                   │    删除物品: 单位携带物品(按类型)(触发单位(), I02M)
                                   │    删除物品: 单位携带物品(按类型)(触发单位(), I02I)
                                   │    添加物品: I02N, 触发单位()
                                   └─ 否则
                                        如果
                                          ├─ 条件: 全部成立
                                          │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I00U)) == TRUE
                                          │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I00R)) == TRUE
                                          │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I00M)) == TRUE
                                          │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I00P)) == TRUE
                                          ├─ 则
                                          │    销毁特效 创建特效(附着单位)(Abilities\Spells\Items\AIre\AIreTarget.mdl, 触发单位(), "origin")
                                          │    删除物品: 单位携带物品(按类型)(触发单位(), I00U)
                                          │    删除物品: 单位携带物品(按类型)(触发单位(), I00R)
                                          │    删除物品: 单位携带物品(按类型)(触发单位(), I00M)
                                          │    删除物品: 单位携带物品(按类型)(触发单位(), I00P)
                                          │    添加物品: I035, 触发单位()
                                          └─ 否则: (无)
```

### 物品叠加

```text
触发器: 物品叠加 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ OperatorCompareItemType(GetItemType(被操作物品()), OperatorEqualENE, ItemTypeCharged)
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorNotEqualENE, I022)
       │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorNotEqualENE, I021)
       │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorNotEqualENE, I01Y)
       │    ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorNotEqualENE, I01X)
       ├─ 则
       │    循环整数A 1→6
       │      └─ 如果
       │           ├─ 条件: 全部成立
       │           │    ├─ 物品类型比较(物品类型ID(单位栏位物品(触发单位(), 循环整数A())), OperatorEqualENE, 物品类型ID(被操作物品()))
       │           │    ├─ 物品比较(单位栏位物品(触发单位(), 循环整数A()), OperatorNotEqualENE, 被操作物品())
       │           ├─ 则
       │           │    SetItemCharges: 单位栏位物品(触发单位(), 循环整数A()), (物品剩余使用次数(单位栏位物品(触发单位(), 循环整数A())) + 物品剩余使用次数(被操作物品()))
       │           │    删除物品: 被操作物品()
       │           └─ 否则: (无)
       └─ 否则
            如果
              ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01X)
              ├─ 则
              │    如果
              │      ├─ 条件: 玩家属性值((触发单位()的所有者), PlayerStateLumber) OperatorGreaterEq YS_LL[玩家号((触发单位()的所有者))]
              │      ├─ 则
              │      │    调整 (触发单位()的所有者) 的 PlayerStateLumber: (YS_LL[玩家号((触发单位()的所有者))] x -1)
              │      │    显示文本→(触发单位()的所有者): 0
              │      │    设置 YS_LL[玩家号((触发单位()的所有者))] = (YS_LL[玩家号((触发单位()的所有者))] + 100)
              │      │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.05)
              │      └─ 否则
              │           显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01Y)
                     ├─ 则
                     │    如果
                     │      ├─ 条件: 玩家属性值((触发单位()的所有者), PlayerStateLumber) OperatorGreaterEq YS_MJ[玩家号((触发单位()的所有者))]
                     │      ├─ 则
                     │      │    调整 (触发单位()的所有者) 的 PlayerStateLumber: (YS_MJ[玩家号((触发单位()的所有者))] x -1)
                     │      │    显示文本→(触发单位()的所有者): 0
                     │      │    设置 YS_MJ[玩家号((触发单位()的所有者))] = (YS_MJ[玩家号((触发单位()的所有者))] + 100)
                     │      │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.05)
                     │      └─ 否则
                     │           显示文本→(触发单位()的所有者): 0
                     └─ 否则
                          如果
                            ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I021)
                            ├─ 则
                            │    如果
                            │      ├─ 条件: 玩家属性值((触发单位()的所有者), PlayerStateLumber) OperatorGreaterEq YS_ZL[玩家号((触发单位()的所有者))]
                            │      ├─ 则
                            │      │    调整 (触发单位()的所有者) 的 PlayerStateLumber: (YS_ZL[玩家号((触发单位()的所有者))] x -1)
                            │      │    显示文本→(触发单位()的所有者): 0
                            │      │    设置 YS_ZL[玩家号((触发单位()的所有者))] = (YS_ZL[玩家号((触发单位()的所有者))] + 100)
                            │      │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.05)
                            │      └─ 否则
                            │           显示文本→(触发单位()的所有者): 0
                            └─ 否则
                                 如果
                                   ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I022)
                                   ├─ 则
                                   │    如果
                                   │      ├─ 条件: 玩家属性值((触发单位()的所有者), PlayerStateLumber) OperatorGreaterEq YS_SW[玩家号((触发单位()的所有者))]
                                   │      ├─ 则
                                   │      │    调整 (触发单位()的所有者) 的 PlayerStateLumber: (YS_SW[玩家号((触发单位()的所有者))] x -1)
                                   │      │    显示文本→(触发单位()的所有者): 0
                                   │      │    设置 YS_SW[玩家号((触发单位()的所有者))] = (YS_SW[玩家号((触发单位()的所有者))] + 200)
                                   │      │    设置 SX_WPLL[玩家号((触发单位()的所有者))] = (SX_WPLL[玩家号((触发单位()的所有者))] + 0.05)
                                   │      │    设置 SX_WPMJ[玩家号((触发单位()的所有者))] = (SX_WPMJ[玩家号((触发单位()的所有者))] + 0.05)
                                   │      │    设置 SX_WPZL[玩家号((触发单位()的所有者))] = (SX_WPZL[玩家号((触发单位()的所有者))] + 0.05)
                                   │      └─ 否则
                                   │           显示文本→(触发单位()的所有者): 0
                                   └─ 否则: (无)
```

### 使用物品

```text
触发器: 使用物品 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 007

```text
触发器: 未命名触发器 007 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroUseItem
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I02R)
       ├─ 则
       │    如果
       │      ├─ 条件: 单位持有物品类型(触发单位(), I03V) == TRUE
       │      ├─ 则
       │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd75
       │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd75
       │      │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd75
       │      └─ 否则
       │           如果
       │             ├─ 条件: 单位持有物品类型(触发单位(), I02Z) == TRUE
       │             ├─ 则
       │             │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd52
       │             │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd52
       │             │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd52
       │             └─ 否则
       │                  如果
       │                    ├─ 条件: 单位持有物品类型(触发单位(), I03E) == TRUE
       │                    ├─ 则
       │                    │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd39
       │                    │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd39
       │                    │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd39
       │                    └─ 否则
       │                         如果
       │                           ├─ 条件: 单位持有物品类型(触发单位(), I03J) == TRUE
       │                           ├─ 则
       │                           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd26
       │                           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd26
       │                           │    修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd26
       │                           └─ 否则
       │                                修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatStr: ModifyMethodAdd13
       │                                修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatAgi: ModifyMethodAdd13
       │                                修改 YX_7[玩家号((触发单位()的所有者))] 的HeroStatInt: ModifyMethodAdd13
       │    如果
       │      ├─ 条件: 单位技能等级(触发单位(), A00A) == 1
       │      ├─ 则
       │      │    添加物品: I001, 触发单位()
       │      └─ 否则
       │           如果
       │             ├─ 条件: 单位技能等级(触发单位(), A00N) == 1
       │             ├─ 则
       │             │    设置生命百分比: 触发单位(), 100
       │             │    添加物品: I03P, 触发单位()
       │             └─ 否则: (无)
       └─ 否则: (无)
```

### 初始单位

```text
触发器: 初始单位 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E1

```text
触发器: E1 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(2.00)
条件
  └─ 无
动作
  ├─  CreateUnit: PlayerNA, nbwm, 6700.00, 1400.00, 90.00
  ├─  CreateUnit: PlayerNA, ngrd, 5900.00, 3900.00, 270.00
  ├─  CreateUnit: PlayerNA, nadr, 5900.00, 3900.00, 270.00
  ├─  CreateUnit: PlayerNA, nbzd, 6900.00, 4000.00, 270.00
  ├─  CreateUnit: PlayerNA, nrwm, 6900.00, 4000.00, 270.00
  ├─  CreateUnit: PlayerNA, U001, -6400.00, -3600.00, 90.00
  └─  CreateUnit: PlayerNA, n008, -3500.00, -5700.00, 270.00
```

### 刷兵

```text
触发器: 刷兵 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E2

```text
触发器: E2 (区域/禁地) [✓] — 刷怪
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(3.00)
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定坐标)(玩家6(橙), LV[guai], 区域中心X(gg_rct______________008), 区域中心Y(gg_rct______________008), 0) → UnitOrderAttack 到 0.00
  ├─ 命令 创建单位(指定坐标)(玩家6(橙), LV[guai], 区域中心X(gg_rct______________007), 区域中心Y(gg_rct______________007), 0) → UnitOrderAttack 到 0.00
  ├─ 命令 创建单位(指定坐标)(玩家6(橙), LV[guai], 区域中心X(gg_rct______________006), 区域中心Y(gg_rct______________006), 0) → UnitOrderAttack 到 0.00
  └─ 命令 创建单位(指定坐标)(玩家6(橙), LV[guai], 区域中心X(gg_rct______________005), 区域中心Y(gg_rct______________005), 0) → UnitOrderAttack 到 0.00
```

### 计时器

```text
触发器: 计时器 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E3

```text
触发器: E3 (区域/禁地) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(3.00)
条件
  └─ 无
动作
  ├─ 运行计时器 dengdai (一次性, 90.00s)
  ├─ 计时器窗口: dengdai 标题="TRIGSTR_743"
  └─ 设置 jsqickou = 最后创建的计时器窗口()
```

### E4

```text
触发器: E4 (区域/禁地) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 计时器 xiayibo 到期
条件
  └─ 无
动作
  ├─ 运行计时器 dengdai (一次性, 60.00s)
  ├─ 删除计时器窗口 jsqickou
  ├─ 计时器窗口: dengdai 标题="TRIGSTR_8181"
  ├─ 设置 jsqickou = 最后创建的计时器窗口()
  ├─ 关闭触发器 gg_trg_E2
  └─ 设置 guai = (guai + 1)
```

### E5

```text
触发器: E5 (区域/禁地) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 dengdai 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 jsqickou
  ├─ 运行计时器 xiayibo (一次性, 120.00s)
  ├─ 计时器窗口: xiayibo 标题="第" + (guai转字符串) + "波敌人"
  ├─ 设置 jsqickou = 最后创建的计时器窗口()
  ├─ 开启触发器 gg_trg_E2
  ├─ 循环整数A 1→5: 调整玩家资源((guai + 1), 玩家循环整数A(), PlayerStateLumber)
  ├─ PlaySoundBJ: gg_snd_QuestNew
  ├─ 设置 X_danweizu = 玩家符合条件的单位(玩家6(橙), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false))
  ├─ 单位组: 选取 X_danweizu 中所有单位
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorGreaterEq 250
  │    ├─ 则
  │    │    循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_6758")
  │    │    运行计时器 SB_jsq (一次性, 60.00s)
  │    │    计时器窗口: SB_jsq 标题="TRIGSTR_6687"
  │    │    设置 SB_jsqck = 最后创建的计时器窗口()
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 如果
  │    ├─ 条件: LV[guai] == nnsw
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家6(橙), H005, 0.00, 5000.00, 0) → UnitOrderAttack 到 0.00
  │    │    循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0.50, 0.50, "TRIGSTR_619")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LV[guai] == oshm
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家6(橙), E00J, 0.00, 5000.00, 0) → UnitOrderAttack 到 0.00
  │    │    循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0.50, 0.50, "TRIGSTR_726")
  │    │    StopMusicBJ: FadeDontFade
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: guai == 36
       ├─ 则
       │    删除计时器窗口 最后创建的计时器窗口()
       │    删除计时器 xiayibo
       │    删除计时器 dengdai
       │    关闭触发器 gg_trg_E4
       │    命令 创建单位(指定坐标)(玩家6(橙), N00A, 0.00, 5000.00, 0) → UnitOrderAttack 到 0.00
       │    循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0.50, 0.50, "TRIGSTR_729")
       │    关闭触发器 当前触发器()
       └─ 否则: (无)
```

### E6

```text
触发器: E6 (区域/禁地) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 SB_jsq 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 SB_jsqck
  ├─ 设置 X_danweizu = 玩家全部单位(玩家6(橙))
  └─ 如果
       ├─ 条件: (X_danweizu中的单位数) OperatorGreaterEq 100
       ├─ 则
       │    循环整数A 1→5: 宣布失败(玩家循环整数A(), "TRIGSTR_257")
       └─ 否则
            删除单位组 X_danweizu
```

### 练级房和刷钱木

```text
触发器: 练级房和刷钱木 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E7

```text
触发器: E7 (区域/禁地) [✓] — 练功房
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(5.00)
条件
  └─ 无
动作
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________010, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|LV[guai]|→PlayerNA 在 D_lj[1] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________011, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|LV[(guai + 1)]|→PlayerNA 在 D_lj[3] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________013, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|LV[guai]|→PlayerNA 在 D_lj[2] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________012, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|LV[(guai + 1)]|→PlayerNA 在 D_lj[4] 面向默认朝向
  │    └─ 否则: (无)
  └─ 删除单位组 X_danweizu
```

### E8

```text
触发器: E8 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(7.00)
条件
  └─ 无
动作
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________014, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLess 20
  │    ├─ 则
  │    │    循环整数A 1→(40 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________014)
  │    │      ├─ 创建 1个|nenc|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  └─ 删除单位组 X_danweizu
```

### E9

```text
触发器: E9 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(9.00)
条件
  └─ 无
动作
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________022, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLess 5
  │    ├─ 则
  │    │    循环整数A 1→(10 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________022)
  │    │      ├─ 创建 1个|npfl|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  └─ 删除单位组 X_danweizu
```

### E15

```text
触发器: E15 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(8.00)
条件
  └─ 无
动作
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________002, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLessEq 50
  │    ├─ 则
  │    │    循环整数A 1→(70 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________002)
  │    │      ├─ 创建 1个|nban|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  └─ 删除单位组 X_danweizu
```

### E10

```text
触发器: E10 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(45.00)
条件
  └─ 无
动作
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________018, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLess 5
  │    ├─ 则
  │    │    循环整数A 1→(10 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________018)
  │    │      ├─ 创建 1个|n002|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________019, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLess 5
  │    ├─ 则
  │    │    循环整数A 1→(10 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________019)
  │    │      ├─ 创建 1个|n003|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  ├─ 删除单位组 X_danweizu
  ├─ 设置 X_danweizu = 区域内符合条件的单位(gg_rct______________020, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (X_danweizu中的单位数) OperatorLess 5
  │    ├─ 则
  │    │    循环整数A 1→(10 - (X_danweizu中的单位数))
  │    │      ├─ 设置 X_dian = 区域内随机点(gg_rct______________020)
  │    │      ├─ 创建 1个|n004|→PlayerNA 在 X_dian 面向默认朝向
  │    │      └─ 清除点 X_dian
  │    └─ 否则: (无)
  └─ 删除单位组 X_danweizu
```

### 野兽

```text
触发器: 野兽 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E11

```text
触发器: E11 (区域/禁地) [✓] — 小怪刷出
───────────────────────────────────────────────────────
事件
  └─ 玩家单位 - 单位死亡
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: (死亡单位()类型ID) == npfl
       ├─ 则
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ guai OperatorLessEq 3
       │      │    ├─ 随机[1~10] == 7
       │      ├─ 则
       │      │    设置 X_dian = (触发单位()的位置)
       │      │    创建物品: I037, X_dian
       │      │    清除点 X_dian
       │      └─ 否则
       │           如果
       │             ├─ 条件: 随机[1~18] == 7
       │             ├─ 则
       │             │    设置 X_dian = (触发单位()的位置)
       │             │    创建物品: gold, X_dian
       │             │    清除点 X_dian
       │             └─ 否则
       │                  如果
       │                    ├─ 条件: 随机[1~65] == 43
       │                    ├─ 则
       │                    │    设置 X_dian = (触发单位()的位置)
       │                    │    创建物品: I039, X_dian
       │                    │    清除点 X_dian
       │                    └─ 否则: (无)
       └─ 否则: (无)
```

### 宝石掉落

```text
触发器: 宝石掉落 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E12

```text
触发器: E12 (区域/禁地) [✓] — 神器宝石
───────────────────────────────────────────────────────
事件
  └─ 玩家单位 - 单位死亡
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == n002
       ├─ 则
       │    如果
       │      ├─ 条件: 随机[1~5] == 3
       │      ├─ 则
       │      │    设置 X_dian = (触发单位()的位置)
       │      │    创建物品: I01N, X_dian
       │      │    清除点 X_dian
       │      └─ 否则: (无)
       └─ 否则
            如果
              ├─ 条件: (触发单位()类型ID) == n003
              ├─ 则
              │    如果
              │      ├─ 条件: 随机[1~5] == 2
              │      ├─ 则
              │      │    设置 X_dian = (触发单位()的位置)
              │      │    创建物品: I01O, X_dian
              │      │    清除点 X_dian
              │      └─ 否则: (无)
              └─ 否则
                   如果
                     ├─ 条件: (触发单位()类型ID) == n004
                     ├─ 则
                     │    如果
                     │      ├─ 条件: 随机[1~5] == 4
                     │      ├─ 则
                     │      │    设置 X_dian = (触发单位()的位置)
                     │      │    创建物品: I01P, X_dian
                     │      │    清除点 X_dian
                     │      └─ 否则: (无)
                     └─ 否则: (无)
```

### 死亡复活

```text
触发器: 死亡复活 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### E13

```text
触发器: E13 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 玩家单位 - 单位死亡
  └─ 玩家单位 - 单位死亡
条件
  └─ 是镜像单位(触发单位()) == TRUE
动作
  └─ 如果
       ├─ 条件: 任一成立
       ├─ 则
       │    循环整数A 1→15
       │      └─ 如果
       │           ├─ 条件: FH_YG[循环整数A()] == UnitTypeNull
       │           ├─ 则
       │           │    如果
       │           │      ├─ 条件: 触发单位() == gg_unit_E00K_0041
       │           │      ├─ 则
       │           │      │    设置 FH_YG[循环整数A()] = E00K
       │           │      └─ 否则
       │           │           设置 FH_YG[循环整数A()] = (触发单位()类型ID)
       │           │    运行计时器 FH_YGJSQ[循环整数A()] (一次性, 40.00s)
       │           │    CustomScriptCode: ScriptCode00
       │           └─ 否则: (无)
       │    设置 X_dian = (触发单位()的位置)
       │    如果
       │      ├─ 条件: (触发单位()类型ID) == nbwm
       │      ├─ 则
       │      │    创建物品: I02K, X_dian
       │      └─ 否则
       │           如果
       │             ├─ 条件: (触发单位()类型ID) == nadr
       │             ├─ 则
       │             │    创建物品: I02J, X_dian
       │             └─ 否则
       │                  如果
       │                    ├─ 条件: (触发单位()类型ID) == nrwm
       │                    ├─ 则
       │                    │    创建物品: I02L, X_dian
       │                    └─ 否则
       │                         如果
       │                           ├─ 条件: (触发单位()类型ID) == nbzd
       │                           ├─ 则
       │                           │    创建物品: I02M, X_dian
       │                           └─ 否则
       │                                如果
       │                                  ├─ 条件: (触发单位()类型ID) == ngrd
       │                                  ├─ 则
       │                                  │    创建物品: I02I, X_dian
       │                                  └─ 否则
       │                                       如果
       │                                         ├─ 条件: (触发单位()类型ID) == n008
       │                                         ├─ 则
       │                                         │    创建物品: I03O, X_dian
       │                                         └─ 否则
       │                                              如果
       │                                                ├─ 条件: (触发单位()类型ID) == H001
       │                                                ├─ 则
       │                                                │    UnitRemoveItemSwapped: 单位携带物品(按类型)(触发单位(), I02F), 触发单位()
       │                                                │    设置 X_zs = 随机[1~4]
       │                                                │    如果
       │                                                │      ├─ 条件: X_zs == 1
       │                                                │      ├─ 则
       │                                                │      │    移动物品到坐标: 创建物品(指定坐标)(I03D, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                │      └─ 否则
       │                                                │           如果
       │                                                │             ├─ 条件: X_zs == 2
       │                                                │             ├─ 则
       │                                                │             │    移动物品到坐标: 创建物品(指定坐标)(I014, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                │             └─ 否则
       │                                                │                  如果
       │                                                │                    ├─ 条件: X_zs == 3
       │                                                │                    ├─ 则
       │                                                │                    │    移动物品到坐标: 创建物品(指定坐标)(I00Y, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                │                    └─ 否则
       │                                                │                         如果
       │                                                │                           ├─ 条件: X_zs == 4
       │                                                │                           ├─ 则
       │                                                │                           │    移动物品到坐标: 创建物品(指定坐标)(I013, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                │                           └─ 否则: (无)
       │                                                └─ 否则
       │                                                     如果
       │                                                       ├─ 条件: (触发单位()类型ID) == U001
       │                                                       ├─ 则
       │                                                       │    移动物品到坐标: 创建物品(指定坐标)(I01Q, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                       └─ 否则
       │                                                            如果
       │                                                              ├─ 条件: (触发单位()类型ID) == H004
       │                                                              ├─ 则
       │                                                              │    如果
       │                                                              │      ├─ 条件: 随机[1~2] == 1
       │                                                              │      ├─ 则
       │                                                              │      │    移动物品到坐标: 创建物品(指定坐标)(I018, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                              │      └─ 否则
       │                                                              │           移动物品到坐标: 创建物品(指定坐标)(I02G, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                              └─ 否则
       │                                                                   如果
       │                                                                     ├─ 条件: (触发单位()类型ID) == H008
       │                                                                     ├─ 则
       │                                                                     │    移动物品到坐标: 创建物品(指定坐标)(I023, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                     └─ 否则
       │                                                                          如果
       │                                                                            ├─ 条件: 任一成立
       │                                                                            ├─ 则
       │                                                                            │    设置 X_zs = 随机[1~3]
       │                                                                            │    如果
       │                                                                            │      ├─ 条件: X_zs == 1
       │                                                                            │      ├─ 则
       │                                                                            │      │    移动物品到坐标: 创建物品(指定坐标)(I041, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                            │      └─ 否则
       │                                                                            │           如果
       │                                                                            │             ├─ 条件: X_zs == 2
       │                                                                            │             ├─ 则
       │                                                                            │             │    移动物品到坐标: 创建物品(指定坐标)(I03E, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                            │             └─ 否则
       │                                                                            │                  移动物品到坐标: 创建物品(指定坐标)(I00V, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                            └─ 否则
       │                                                                                 如果
       │                                                                                   ├─ 条件: 触发单位() == gg_unit_N006_0102
       │                                                                                   ├─ 则
       │                                                                                   │    设置 X_zs = 随机[1~4]
       │                                                                                   │    如果
       │                                                                                   │      ├─ 条件: X_zs == 1
       │                                                                                   │      ├─ 则
       │                                                                                   │      │    移动物品到坐标: 创建物品(指定坐标)(I017, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                   │      └─ 否则
       │                                                                                   │           如果
       │                                                                                   │             ├─ 条件: X_zs == 2
       │                                                                                   │             ├─ 则
       │                                                                                   │             │    移动物品到坐标: 创建物品(指定坐标)(I03A, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                   │             └─ 否则
       │                                                                                   │                  如果
       │                                                                                   │                    ├─ 条件: X_zs == 3
       │                                                                                   │                    ├─ 则
       │                                                                                   │                    │    移动物品到坐标: 创建物品(指定坐标)(I03B, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                   │                    └─ 否则
       │                                                                                   │                         如果
       │                                                                                   │                           ├─ 条件: X_zs == 4
       │                                                                                   │                           ├─ 则
       │                                                                                   │                           │    移动物品到坐标: 创建物品(指定坐标)(I02T, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                   │                           └─ 否则: (无)
       │                                                                                   └─ 否则
       │                                                                                        如果
       │                                                                                          ├─ 条件: 触发单位() == gg_unit_H006_0037
       │                                                                                          ├─ 则
       │                                                                                          │    设置 X_zs = 随机[1~2]
       │                                                                                          │    如果
       │                                                                                          │      ├─ 条件: X_zs == 1
       │                                                                                          │      ├─ 则
       │                                                                                          │      │    移动物品到坐标: 创建物品(指定坐标)(I016, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                          │      └─ 否则
       │                                                                                          │           移动物品到坐标: 创建物品(指定坐标)(I00W, 0, 0), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │                                                                                          └─ 否则: (无)
       │    清除点 X_dian
       └─ 否则: (无)
```

### E14

```text
触发器: E14 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 循环整数A 1→15
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, FH_YGJSQ[循环整数A()])
            ├─ 则
            │    如果
            │      ├─ 条件: IsHeroUnitId(FH_YG[循环整数A()]) == TRUE
            │      ├─ 则
            │      │    如果
            │      │      ├─ 条件: FH_YG[循环整数A()] == nbwm
            │      │      ├─ 则
            │      │      │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, nbwm, 6700.00, 1400.00, 90.00), UnitOrderStop
            │      │      └─ 否则
            │      │           如果
            │      │             ├─ 条件: FH_YG[循环整数A()] == nadr
            │      │             ├─ 则
            │      │             │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, nadr, 5900.00, 3900.00, 90.00), UnitOrderStop
            │      │             └─ 否则
            │      │                  如果
            │      │                    ├─ 条件: FH_YG[循环整数A()] == ngrd
            │      │                    ├─ 则
            │      │                    │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, ngrd, 5900.00, 3900.00, 90.00), UnitOrderStop
            │      │                    └─ 否则
            │      │                         如果
            │      │                           ├─ 条件: FH_YG[循环整数A()] == nrwm
            │      │                           ├─ 则
            │      │                           │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, nrwm, 6900.00, 4000.00, 90.00), UnitOrderStop
            │      │                           └─ 否则
            │      │                                如果
            │      │                                  ├─ 条件: FH_YG[循环整数A()] == nbzd
            │      │                                  ├─ 则
            │      │                                  │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, nbzd, 6900.00, 4000.00, 90.00), UnitOrderStop
            │      │                                  └─ 否则
            │      │                                       如果
            │      │                                         ├─ 条件: FH_YG[循环整数A()] == n008
            │      │                                         ├─ 则
            │      │                                         │    单位发布命令(立即): 创建单位(指定坐标)(PlayerNA, n008, -3500.00, -5700.00, 270.00), UnitOrderStop
            │      │                                         └─ 否则: (无)
            │      └─ 否则
            │           如果
            │             ├─ 条件: FH_YG[循环整数A()] == U001
            │             ├─ 则
            │             │    设置 X_danweizu = 玩家指定类型单位(PlayerNA, U001)
            │             │    单位组: 选取 X_danweizu 中所有单位
            │             │      └─ 复活英雄: 选取单位(), -6500.00, -3500.00, ShowHideShow
            │             │    删除单位组 X_danweizu
            │             └─ 否则
            │                  如果
            │                    ├─ 条件: FH_YG[循环整数A()] == H001
            │                    ├─ 则
            │                    │    复活英雄: gg_unit_H001_0087, -4900.00, 1500.00, ShowHideShow
            │                    └─ 否则
            │                         如果
            │                           ├─ 条件: FH_YG[循环整数A()] == H008
            │                           ├─ 则
            │                           │    复活英雄: gg_unit_H008_0027, -3500.00, -3000.00, ShowHideShow
            │                           └─ 否则
            │                                如果
            │                                  ├─ 条件: FH_YG[循环整数A()] == H004
            │                                  ├─ 则
            │                                  │    复活英雄: gg_unit_H004_0025, -3900.00, -300.00, ShowHideShow
            │                                  └─ 否则
            │                                       如果
            │                                         ├─ 条件: FH_YG[循环整数A()] == E00K
            │                                         ├─ 则
            │                                         │    复活英雄: gg_unit_E00K_0041, 6500.00, -500.00, ShowHideShow
            │                                         └─ 否则
            │                                              如果
            │                                                ├─ 条件: FH_YG[循环整数A()] == N006
            │                                                ├─ 则
            │                                                │    复活英雄: gg_unit_N006_0102, 4000.00, -2500.00, ShowHideShow
            │                                                └─ 否则: (无)
            │    设置 FH_YG[循环整数A()] = UnitTypeNull
            │    CustomScriptCode: ScriptCode00
            └─ 否则: (无)
```

### 失败

```text
触发器: 失败 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 010

```text
触发器: 未命名触发器 010 (物品系统) [✓] — 失败
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_ubon_0001 - 单位死亡
条件
  └─ 无
动作
  ├─ StopMusicBJ: FadeDontFade
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 玩家6(橙), Uclc, "TRIGSTR_9409", dian1, gg_snd_U08Archimonde19, "TRIGSTR_9410", AddSetToAdd, 0.00, WaitDontWait
  └─ 循环整数A 1→5
       └─ 宣布失败: 玩家循环整数A(), "TRIGSTR_015"
```

### 胜利

```text
触发器: 胜利 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 027

```text
触发器: 未命名触发器 027 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家单位 - 单位死亡
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == N00A
       ├─ 则
       │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 玩家5(黄), Nkjx, "TRIGSTR_7844", dian1, SoundNull, "TRIGSTR_7845", AddSetToAdd, 0.00, WaitDontWait
       │    设置无敌: gg_unit_Uclc_0123, InvulnerabilityVulnerable
       └─ 否则
            如果
              ├─ 条件: (触发单位()类型ID) == Uclc
              ├─ 则
              │    关闭触发器 gg_trg_E2
              │    关闭触发器 gg_trg_E3
              │    关闭触发器 gg_trg_E4
              │    关闭触发器 gg_trg_E5
              │    关闭触发器 gg_trg_E6
              │    关闭触发器 gg_trg_E7
              │    关闭触发器 gg_trg_E8
              │    关闭触发器 gg_trg_E9
              │    关闭触发器 gg_trg_E10
              │    关闭触发器 gg_trg_E11
              │    关闭触发器 gg_trg_E12
              │    关闭触发器 gg_trg_E13
              │    关闭触发器 gg_trg_E14
              │    关闭触发器 gg_trg_E15
              │    关闭触发器 gg_trg____________________046
              │    关闭触发器 gg_trg____________________006
              │    关闭触发器 gg_trg____________________006_______u
              │    关闭触发器 gg_trg____________________010
              │    设置无敌: gg_unit_ubon_0001, InvulnerabilityInvulnerable
              │    电影模式: OnOffOn, DY_WJZ
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 玩家6(橙), Uclc, "TRIGSTR_600", dian1, SoundNull, "TRIGSTR_601", AddSetToAdd, 0.00, WaitDontWait
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, (凶手单位()的所有者), (凶手单位()类型ID), GetHeroProperName(凶手单位()), dian1, SoundNull, "TRIGSTR_579", AddSetToAdd, 0.00, WaitDontWait
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 玩家6(橙), Uclc, "TRIGSTR_589", dian1, SoundNull, "TRIGSTR_630", AddSetToAdd, 0.00, WaitDontWait
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, (凶手单位()的所有者), (凶手单位()类型ID), GetHeroProperName(凶手单位()), dian1, SoundNull, "TRIGSTR_641", AddSetToAdd, 0.00, WaitDontWait
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 玩家6(橙), Uclc, "TRIGSTR_642", dian1, SoundNull, "TRIGSTR_643", AddSetToAdd, 0.00, WaitDontWait
              │    电影模式: OnOffOff, DY_WJZ
              │    循环整数A 1→5
              │      └─ 显示文本→玩家循环整数A(): 0
              │    单位组: 选取 区域内符合条件的单位(可用地图区域(), (玩家比较((过滤单位()的所有者), OperatorNotEqualENE, 玩家5(黄)) 且 玩家比较((过滤单位()的所有者), OperatorNotEqualENE, 非玩家))) 中所有单位
              │      └─ 杀死 选取单位()
              │    AddWeatherEffectSaveLast: 可用地图区域(), WeatherAshenvaleHeavyRain
              │    EnableWeatherEffect: GetLastCreatedWeatherEffect(), OnOffOn
              │    SetTerrainFogEx: FogStyleLinear, 100.00, 4000.00, 0.01, 1, 0.00, 0.00
              │    开启触发器 gg_trg____________________021
              │    开启触发器 gg_trg____________________005
              │    SetCameraBounds: -500.00, 1000.00, -500.00, 2000.00, 500.00, 2000.00, 500.00, 1000.00
              │    FogEnableOff
              │    创建 1个|e00A|→非玩家 在 Location(0, 1500.00) 面向270.00
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 非玩家, E00L, "TRIGSTR_1086", dian1, SoundNull, "TRIGSTR_1093", AddSetToAdd, 0.00, WaitDontWait
              │    复活英雄: gg_unit_E00K_0041, 0, 500.00, ShowHideHide
              │    移动单位: gg_unit_E00K_0041, 0, 500.00
              │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, gg_unit_E00K_0041, "origin")
              │    IssuePointOrderById: gg_unit_E00K_0041, OrderCodeMove, 0, 1500.00
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 非玩家, H001, "TRIGSTR_1094", dian1, SoundNull, "TRIGSTR_1104", AddSetToAdd, 0.00, WaitDontWait
              │    移动单位: gg_unit_H001_0087, 0, 500.00
              │    IssuePointOrderById: gg_unit_H001_0087, OrderCodeMove, 0, 1500.00
              │    TransmissionFromUnitTypeWithNameBJ: DY_WJZ, 非玩家, H006, "TRIGSTR_1109", dian1, SoundNull, "TRIGSTR_1115", AddSetToAdd, 0.00, WaitDontWait
              │    移动单位: gg_unit_H006_0037, 0, 500.00
              │    IssuePointOrderById: gg_unit_H006_0037, OrderCodeMove, 0, 1500.00
              │    循环整数A 1→5
              │      └─ 显示文本→玩家循环整数A(): 0
              │    移动单位: gg_unit_npn3_0120, 0, 650.00
              │    移动单位: gg_unit_npn1_0119, 0, 650.00
              │    移动单位: gg_unit_npn2_0110, 0, 650.00
              └─ 否则: (无)
```

### 未命名触发器 021

```text
触发器: 未命名触发器 021 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct______________004)
条件
  └─ 无
动作
  └─ 移除 触发单位()
```

### 未命名触发器 005

```text
触发器: 未命名触发器 005 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.10)
条件
  └─ 无
动作
  ├─ 设置 X_zs = 随机[1~10]
  └─ 如果
       ├─ 条件: X_zs == 1
       ├─ 则
       │    销毁特效 创建特效(指定坐标)(Units\Demon\Infernal\InfernalBirth.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
       └─ 否则
            如果
              ├─ 条件: X_zs == 2
              ├─ 则
              │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Resurrect\ResurrectTarget.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
              └─ 否则
                   如果
                     ├─ 条件: X_zs == 3
                     ├─ 则
                     │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Orc\WarStomp\WarStompCaster.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                     └─ 否则
                          如果
                            ├─ 条件: X_zs == 4
                            ├─ 则
                            │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Charm\CharmTarget.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                            └─ 否则
                                 如果
                                   ├─ 条件: X_zs == 5
                                   ├─ 则
                                   │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                   └─ 否则
                                        如果
                                          ├─ 条件: X_zs == 6
                                          ├─ 则
                                          │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                          └─ 否则
                                               如果
                                                 ├─ 条件: X_zs == 7
                                                 ├─ 则
                                                 │    销毁特效 创建特效(指定坐标)(war3mapImported\bingbao3.mdx, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: X_zs == 8
                                                        ├─ 则
                                                        │    销毁特效 创建特效(指定坐标)(war3mapImported\firenova2.mdx, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: X_zs == 9
                                                               ├─ 则
                                                               │    销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\Naga\NagaDeath\NagaDeath.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: X_zs == 10
                                                                      ├─ 则
                                                                      │    销毁特效 创建特效(指定坐标)(Objects\Spawnmodels\Undead\UDeathMedium\UDeath.mdl, (随机[-1000~1000]转实数), (随机[500~2500]转实数))
                                                                      └─ 否则: (无)
```

### 基地生命提示

```text
触发器: 基地生命提示 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 030

```text
触发器: 未命名触发器 030 (物品系统) [✓] — 生命值提示
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_ubon_0001 - UnitEventAttacked
条件
  └─ 单位生命百分比(触发单位()) OperatorLessEq 50.00
动作
  └─ 循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, "|c00ff0000墓冢生命值：|r" + 实数转字符串(单位生命百分比(触发单位())) + "%")
```

### 难度选择

```text
触发器: 难度选择 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 035

```text
触发器: 未命名触发器 035 (物品系统) [✓] — 难度添加
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  ├─ DialogSetMessageBJ: duihua, "TRIGSTR_2838"
  ├─ DialogAddButtonBJ: duihua, "TRIGSTR_2839"
  ├─ 设置 ndu1 = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: duihua, "TRIGSTR_2840"
  ├─ 设置 ndu2 = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: duihua, "TRIGSTR_2841"
  ├─ 设置 ndu3 = bj_lastCreatedButton
  └─ 销毁触发器(自身)
```

### 未命名触发器 036

```text
触发器: 未命名触发器 036 (物品系统) [✓] — 难度选择
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(duihua)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, ndu1)
       ├─ 则
       │    循环整数A 1→5
       │      └─ 显示文本→玩家循环整数A(): 0
       │    销毁触发器(自身)
       └─ 否则
            如果
              ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, ndu2)
              ├─ 则
              │    SetPlayerTechResearchedSwap: Rhan, 1, PlayerNA
              │    SetPlayerTechResearchedSwap: Rhan, 1, 玩家6(橙)
              │    循环整数A 1→5
              │      └─ 显示文本→玩家循环整数A(): 0
              │    销毁触发器(自身)
              └─ 否则
                   如果
                     ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, ndu3)
                     ├─ 则
                     │    SetPlayerTechResearchedSwap: Rhan, 2, PlayerNA
                     │    SetPlayerTechResearchedSwap: Rhan, 2, 玩家6(橙)
                     │    循环整数A 1→5
                     │      └─ 显示文本→玩家循环整数A(): 0
                     │    销毁触发器(自身)
                     └─ 否则: (无)
```

### 玩家离开

```text
触发器: 玩家离开 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 038

```text
触发器: 未命名触发器 038 (物品系统) [✓] — 玩家离开
───────────────────────────────────────────────────────
事件
  ├─ TriggerRegisterPlayerEventLeave(Player00)
  ├─ TriggerRegisterPlayerEventLeave(玩家1(红))
  ├─ TriggerRegisterPlayerEventLeave(玩家2(蓝))
  ├─ TriggerRegisterPlayerEventLeave(玩家3(青))
  └─ TriggerRegisterPlayerEventLeave(玩家4(紫))
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: (YX_7[玩家号(触发玩家())]类型ID) == N00B
  │    ├─ 则
  │    │    移除 YLL_DW[玩家号((触发单位()的所有者))]
  │    └─ 否则
  │         如果
  │           ├─ 条件: (YX_7[玩家号(触发玩家())]类型ID) == N00C
  │           ├─ 则
  │           │    循环整数A 1→5
  │           │      └─ 移除 HJZL_DW[循环整数A()]
  │           └─ 否则: (无)
  ├─ 循环整数A 1→6
  │    ├─ UnitRemoveItemFromSlotSwapped: 循环整数A(), BL5[玩家号(触发玩家())]
  │    └─ UnitRemoveItemFromSlotSwapped: 循环整数A(), YX_7[玩家号(触发玩家())]
  ├─ 循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, (玩家名:触发玩家()) + "|c00ff0000离开了游戏，他的资源平分给大家。物品掉落在地上。|r")
  ├─ 移除 BL5[玩家号(触发玩家())]
  ├─ 移除 YX_7[玩家号(触发玩家())]
  ├─ 设置 X_wanjiazu = 符合条件的玩家((玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser) 且 玩家槽位状态比较(玩家槽位状态(过滤玩家()), OperatorEqualENE, PlayerSlotStatePlaying)))
  ├─ ForForceMultiple: X_wanjiazu
  └─ DestroyForce: X_wanjiazu
```

### 未命名触发器 020

```text
触发器: 未命名触发器 020 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct______________000)
条件
  ├─ (触发单位()的所有者) == 玩家11(暗绿)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 移动单位: 触发单位(), dian1
```

### 未命名触发器 018

```text
触发器: 未命名触发器 018 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 单位持有物品类型(触发单位(), I02S) == TRUE
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I02S)
  ├─ 设置 X_zs = 随机[5~(10 - guai)]
  ├─ 调整 (触发单位()的所有者) 的 PlayerStateLumber: X_zs
  └─ 显示文本→(触发单位()的所有者): 0
```

### 未命名触发器 016

```text
触发器: 未命名触发器 016 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(185.00, gg_unit_uabo_0054)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 显示文本→(触发单位()的所有者): 0
```

### 未命名触发器 049

```text
触发器: 未命名触发器 049 (单位/战斗) [✓] — 成长装备换取
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(175.00, gg_unit_npn1_0119)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_npn1_0119, 触发单位(), 0.10
  └─ 如果
       ├─ 条件: 单位持有物品类型(触发单位(), I037) == TRUE
       ├─ 则
       │    如果
       │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(触发单位(), I037)) == 1
       │      ├─ 则
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I037)
       │      └─ 否则
       │           SetItemCharges: 单位携带物品(按类型)(触发单位(), I037), (物品剩余使用次数(单位携带物品(按类型)(触发单位(), I037)) - 1)
       │    如果
       │      ├─ 条件: 随机[1~4] == 2
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 随机[5~9] == 7
       │      │      ├─ 则
       │      │      │    添加物品: I03J, 触发单位()
       │      │      │    显示文本→(触发单位()的所有者): 0
       │      │      └─ 否则
       │      │           添加物品: I038, 触发单位()
       │      │           显示文本→(触发单位()的所有者): 0
       │      └─ 否则
       │           显示文本→(触发单位()的所有者): 0
       └─ 否则
            设置 X_zs = 随机[1~10]
            如果
              ├─ 条件: X_zs == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: X_zs == 2
                     ├─ 则
                     │    显示文本→(触发单位()的所有者): 0
                     └─ 否则
                          如果
                            ├─ 条件: X_zs == 3
                            ├─ 则
                            │    显示文本→(触发单位()的所有者): 0
                            └─ 否则
                                 如果
                                   ├─ 条件: X_zs == 4
                                   ├─ 则
                                   │    显示文本→(触发单位()的所有者): 0
                                   └─ 否则
                                        如果
                                          ├─ 条件: X_zs == 5
                                          ├─ 则
                                          │    显示文本→(触发单位()的所有者): 0
                                          └─ 否则: (无)
```

### 未命名触发器 053

```text
触发器: 未命名触发器 053 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(175.00, gg_unit_npn3_0120)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_npn3_0120, 触发单位(), 0.10
  └─ 如果
       ├─ 条件: 单位持有物品类型(触发单位(), I039) == TRUE
       ├─ 则
       │    如果
       │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(触发单位(), I039)) OperatorGreater 3
       │      ├─ 则
       │      │    SetItemCharges: 单位携带物品(按类型)(触发单位(), I039), (物品剩余使用次数(单位携带物品(按类型)(触发单位(), I039)) - 3)
       │      │    SetHeroLevelNT: 触发单位(), (英雄等级(触发单位()) + 3), ShowHideShow
       │      │    显示文本→(触发单位()的所有者): 0
       │      └─ 否则
       │           SetHeroLevelNT: 触发单位(), (英雄等级(触发单位()) + 物品剩余使用次数(单位携带物品(按类型)(触发单位(), I039))), ShowHideShow
       │           删除物品: 单位携带物品(按类型)(触发单位(), I039)
       │           显示文本→(触发单位()的所有者): 0
       └─ 否则
            设置 X_zs = 随机[1~10]
            如果
              ├─ 条件: X_zs == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: X_zs == 2
                     ├─ 则
                     │    显示文本→(触发单位()的所有者): 0
                     └─ 否则
                          如果
                            ├─ 条件: X_zs == 3
                            ├─ 则
                            │    显示文本→(触发单位()的所有者): 0
                            └─ 否则
                                 如果
                                   ├─ 条件: X_zs == 4
                                   ├─ 则
                                   │    显示文本→(触发单位()的所有者): 0
                                   └─ 否则
                                        如果
                                          ├─ 条件: X_zs == 5
                                          ├─ 则
                                          │    显示文本→(触发单位()的所有者): 0
                                          └─ 否则: (无)
```

### 未命名触发器 052

```text
触发器: 未命名触发器 052 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(175.00, gg_unit_npn2_0110)
条件
  ├─ 玩家控制者比较(玩家控制者类型((触发单位()的所有者)), OperatorEqualENE, MapControlUser)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_npn2_0110, 触发单位(), 0.10
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == H000
       ├─ 则
       │    显示文本→(触发单位()的所有者): 0
       └─ 否则
            如果
              ├─ 条件: (触发单位()类型ID) == E000
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              └─ 否则
                   如果
                     ├─ 条件: (触发单位()类型ID) == N007
                     ├─ 则
                     │    显示文本→(触发单位()的所有者): 0
                     └─ 否则
                          如果
                            ├─ 条件: (触发单位()类型ID) == N00B
                            ├─ 则
                            │    显示文本→(触发单位()的所有者): 0
                            └─ 否则
                                 如果
                                   ├─ 条件: (触发单位()类型ID) == H007
                                   ├─ 则
                                   │    显示文本→(触发单位()的所有者): 0
                                   └─ 否则
                                        如果
                                          ├─ 条件: (触发单位()类型ID) == U000
                                          ├─ 则
                                          │    显示文本→(触发单位()的所有者): 0
                                          └─ 否则
                                               如果
                                                 ├─ 条件: (触发单位()类型ID) == N000
                                                 ├─ 则
                                                 │    显示文本→(触发单位()的所有者): 0
                                                 └─ 否则
                                                      如果
                                                        ├─ 条件: (触发单位()类型ID) == O000
                                                        ├─ 则
                                                        │    显示文本→(触发单位()的所有者): 0
                                                        └─ 否则
                                                             如果
                                                               ├─ 条件: (触发单位()类型ID) == N00C
                                                               ├─ 则
                                                               │    显示文本→(触发单位()的所有者): 0
                                                               └─ 否则
                                                                    如果
                                                                      ├─ 条件: (触发单位()类型ID) == N00D
                                                                      ├─ 则
                                                                      │    显示文本→(触发单位()的所有者): 0
                                                                      └─ 否则: (无)
```

### 未命名触发器 051

```text
触发器: 未命名触发器 051 (刷怪/进攻) [✓] — 成长装备
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 玩家控制者比较(玩家控制者类型((凶手单位()的所有者)), OperatorEqualENE, MapControlUser)
       ├─ 则
       │    设置 DMB_SD2[玩家号((凶手单位()的所有者))] = (DMB_SD2[玩家号((凶手单位()的所有者))] + 1)
       │    排行榜 最后创建的排行榜()[3,(玩家号((凶手单位()的所有者)) + 1)] = (DMB_SD2[玩家号((凶手单位()的所有者))]转字符串)
       │    如果
       │      ├─ 条件: 单位类型判断(凶手单位(), 英雄) == TRUE
       │      ├─ 则
       │      │    设置 DMB_SD1[玩家号((凶手单位()的所有者))] = (DMB_SD1[玩家号((凶手单位()的所有者))] + 1)
       │      │    排行榜 最后创建的排行榜()[2,(玩家号((凶手单位()的所有者)) + 1)] = (DMB_SD1[玩家号((凶手单位()的所有者))]转字符串)
       │      └─ 否则: (无)
       └─ 否则: (无)
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 排行榜 最后创建的排行榜()[4,(玩家号(触发玩家()) + 1)] = (玩家属性值(触发玩家(), PlayerStateLumber)转字符串)
```

### 毁灭前夕

```text
触发器: 毁灭前夕 (其他) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 006

```text
触发器: 未命名触发器 006 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_H006_0037 - 单位死亡
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 复活英雄: 触发单位(), 单位X坐标(触发单位()), 单位Y坐标(触发单位()), ShowHideHide
  ├─ 设置单位归属: 触发单位(), 非玩家, 改变颜色
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_769", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_777", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_904", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_984", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_130", AddSetToAdd, 0, WaitDontWait
  ├─ UnitRemoveItemSwapped: 单位携带物品(按类型)(gg_unit_H006_0037, I02V), gg_unit_H006_0037
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  ├─ FlashQuestDialogButtonBJ
  └─ QuestSetDiscoveredBJ: RW_5[1], DiscoveredOptionDiscovered
```

### 未命名触发器 006 复制

```text
触发器: 未命名触发器 006 复制 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_H001_0087 - 单位死亡
条件
  ├─ 玩家科技等级(Rhhb, (凶手单位()的所有者)) == 1
  └─ 单位持有物品类型(凶手单位(), I02V) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 复活英雄: 触发单位(), 单位X坐标(触发单位()), 单位Y坐标(触发单位()), ShowHideHide
  ├─ 设置单位归属: 触发单位(), 非玩家, 改变颜色
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_995", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_996", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1001", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1002", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1003", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1004", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1010", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1014", AddSetToAdd, 0, WaitDontWait
  ├─ UnitRemoveItemSwapped: 单位携带物品(按类型)(gg_unit_H001_0087, I02U), gg_unit_H001_0087
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1012", AddSetToAdd, 0, WaitDontWait
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  ├─ FlashQuestDialogButtonBJ
  ├─ QuestSetDescriptionBJ: RW_5[1], "TRIGSTR_1016"
  └─ 开启触发器 gg_trg____________________001
```

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(185.00, gg_unit_H006_0037)
条件
  ├─ guai == 36
  ├─ 英雄等级(触发单位()) OperatorGreater 400
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_137", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H006_0037, GetHeroProperName(gg_unit_H006_0037), SoundNull, "TRIGSTR_138", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_457", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H006_0037, GetHeroProperName(gg_unit_H006_0037), SoundNull, "TRIGSTR_763", AddSetToAdd, 0, WaitDontWait
  ├─ 移动单位: gg_unit_H001_0087, (gg_unit_H006_0037的位置)
  ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, gg_unit_H001_0087, "origin")
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_H001_0087, gg_unit_H006_0037, 0
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_H006_0037, gg_unit_H001_0087, 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H001_0087, GetHeroProperName(gg_unit_H001_0087), SoundNull, "TRIGSTR_635", AddSetToAdd, 0, WaitDontWait
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_H001_0087, 触发单位(), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H001_0087, GetHeroProperName(gg_unit_H001_0087), SoundNull, "TRIGSTR_1021", AddSetToAdd, 0, WaitDontWait
  ├─ UnitRemoveItemSwapped: 单位携带物品(按类型)(gg_unit_H001_0087, I03V), gg_unit_H001_0087
  ├─ SetUnitFacingToFaceUnitTimed: 触发单位(), gg_unit_H001_0087, 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1023", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H001_0087, GetHeroProperName(gg_unit_H001_0087), SoundNull, "TRIGSTR_1025", AddSetToAdd, 0, WaitDontWait
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_H006_0037, 触发单位(), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H006_0037, GetHeroProperName(gg_unit_H006_0037), SoundNull, "TRIGSTR_1024", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_H006_0037, GetHeroProperName(gg_unit_H006_0037), SoundNull, "TRIGSTR_1028", AddSetToAdd, 0, WaitDontWait
  ├─ UnitRemoveItemSwapped: 单位携带物品(按类型)(gg_unit_H006_0037, I00X), gg_unit_H006_0037
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1022", AddSetToAdd, 0, WaitDontWait
  ├─ FlashQuestDialogButtonBJ
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  └─ QuestSetDescriptionBJ: RW_5[1], "TRIGSTR_1031"
```

### 隐尘

```text
触发器: 隐尘 (其他) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 046

```text
触发器: 未命名触发器 046 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_N006_0102 - 单位死亡
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ FogEnableOn
  ├─ PanCameraToTimed: 3900.00, -2500.00, 0
  ├─ 创建 1个|N001|→玩家11(暗绿) 在 Location(3826.00, -2600.00) 面向180.00
  ├─ 设置 YX_7[6] = 最后创建的单位()
  ├─ SetHeroLevel: 最后创建的单位(), 500, ShowHideHide
  ├─ SuspendHeroXPBJ: EnableDisableDisable, 最后创建的单位()
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, PlayerNA, N006, "TRIGSTR_7801", (触发单位()的位置), SoundNull, "TRIGSTR_7802", AddSetToAdd, 0.00, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, PlayerNA, N006, "TRIGSTR_906", (触发单位()的位置), SoundNull, "TRIGSTR_933", AddSetToAdd, 0.00, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, PlayerNA, N006, "TRIGSTR_944", (触发单位()的位置), SoundNull, "TRIGSTR_947", AddSetToAdd, 0.00, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, PlayerNA, N006, "TRIGSTR_952", (触发单位()的位置), SoundNull, "TRIGSTR_954", AddSetToAdd, 0.00, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, PlayerNA, N006, "TRIGSTR_1234", (触发单位()的位置), SoundNull, "TRIGSTR_1236", AddSetToAdd, 0.00, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: DY_WJZ, (凶手单位()的所有者), (凶手单位()类型ID), GetHeroProperName(凶手单位()), (触发单位()的位置), SoundNull, "TRIGSTR_1269", AddSetToAdd, 0.00, WaitDontWait
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  └─ 销毁触发器(自身)
```

### 半神之力

```text
触发器: 半神之力 (其他) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 008

```text
触发器: 未命名触发器 008 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(175.00, gg_unit_u003_0122)
条件
  ├─ 英雄等级(触发单位()) OperatorGreater 200
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 单位自定义值(gg_unit_u003_0122) == 0
       ├─ 则
       │    关闭触发器 当前触发器()
       │    PanCameraToTimed: 0, -7200.00, 0
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_u003_0122, "TRIGSTR_556", SoundNull, "TRIGSTR_570", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_u003_0122, "TRIGSTR_587", SoundNull, "TRIGSTR_591", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_597", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_u003_0122, "TRIGSTR_610", SoundNull, "TRIGSTR_806", AddSetToAdd, 0, WaitDontWait
       │    添加物品: I02Y, 触发单位()
       │    SetItemInvulnerableBJ: 最后创建的物品(), InvulnerabilityInvulnerable
       │    播放动画: gg_unit_u003_0122, "death"
       │    QuestSetDiscoveredBJ: RW_5[2], DiscoveredOptionDiscovered
       │    FlashQuestDialogButtonBJ
       │    循环整数A 1→5
       │      └─ 显示文本→玩家循环整数A(): 0
       │    销毁触发器(自身)
       └─ 否则: (无)
```

### 霜寒淬

```text
触发器: 霜寒淬 (其他) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 024

```text
触发器: 未命名触发器 024 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(150.00, gg_unit_e00N_0040)
条件
  ├─ 英雄等级(触发单位()) OperatorGreater 250
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家科技等级(Rhhb, (触发单位()的所有者)) == 1
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位自定义值(gg_unit_e00N_0040) == 0
       │    ├─ 单位持有物品类型(触发单位(), I019) == TRUE
       ├─ 则
       │    关闭触发器 当前触发器()
       │    设置单位归属: gg_unit_e00N_0040, 玩家5(黄), 改变颜色
       │    PanCameraToTimed: -1100.00, -7000.00, 0
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_1057", SoundNull, "TRIGSTR_1064", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1081", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_1082", SoundNull, "TRIGSTR_1087", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1096", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_1097", SoundNull, "TRIGSTR_1107", AddSetToAdd, 0, WaitDontWait
       │    FlashQuestDialogButtonBJ
       │    QuestSetDiscoveredBJ: RW_5[3], DiscoveredOptionDiscovered
       │    循环整数A 1→5
       │      └─ 显示文本→玩家循环整数A(): 0.50
       │    设置单位归属: gg_unit_Uktl_0055, 玩家6(橙), 改变颜色
       │    命令 gg_unit_Uktl_0055 → UnitOrderAttack 到 X_dian
       │    设置单位自定义值: gg_unit_e00N_0040, 1
       │    开启触发器 当前触发器()
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ 单位自定义值(gg_unit_e00N_0040) == 1
              │    ├─ 单位持有物品类型(触发单位(), I015) == TRUE
              ├─ 则
              │    关闭触发器 当前触发器()
              │    PanCameraToTimed: -1100.00, -7000.00, 0
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_967", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_965", SoundNull, "TRIGSTR_966", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_968", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_969", SoundNull, "TRIGSTR_970", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_971", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_972", SoundNull, "TRIGSTR_973", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_974", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_975", SoundNull, "TRIGSTR_976", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_977", AddSetToAdd, 0, WaitDontWait
              │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_e00N_0040, "TRIGSTR_978", SoundNull, "TRIGSTR_979", AddSetToAdd, 0, WaitDontWait
              │    设置单位自定义值: gg_unit_e00N_0040, 2
              │    FlashQuestDialogButtonBJ
              │    QuestSetDescriptionBJ: RW_5[3], "TRIGSTR_1106"
              │    循环整数A 1→5
              │      └─ 显示文本→玩家循环整数A(): 0.50
              │    开启触发器 当前触发器()
              └─ 否则: (无)
```

### 未命名触发器 011

```text
触发器: 未命名触发器 011 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I015)
动作
  └─ 如果
       ├─ 条件: IsItemInvulnerable(被操作物品()) == TRUE
       ├─ 则
       │    SetItemInvulnerableBJ: 被操作物品(), InvulnerabilityInvulnerable
       │    FlashQuestDialogButtonBJ
       │    QuestSetDescriptionBJ: RW_5[3], "TRIGSTR_1108"
       │    循环整数A 1→5
       │      └─ 显示文本→玩家循环整数A(): 0.50
       └─ 否则: (无)
```

### 远古

```text
触发器: 远古 (其他) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 未命名触发器 013

```text
触发器: 未命名触发器 013 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(350.00, gg_unit_E009_0029)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == Eilm
       ├─ 则
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 玩家科技等级(Rhhb, (触发单位()的所有者)) != 1
       │      │    ├─ 英雄等级(触发单位()) OperatorGreater 250
       │      ├─ 则
       │      │    关闭触发器 当前触发器()
       │      │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
       │      │    PauseUnit: 触发单位(), PauseUnpauseOptionPause
       │      │    SetUnitFacingToFaceUnitTimed: 触发单位(), gg_unit_E009_0029, 0
       │      │    SetUnitFacingToFaceUnitTimed: gg_unit_E009_0029, 触发单位(), 0
       │      │    PanCameraToTimed: -7000.00, -7000.00, 0
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_804", SoundNull, "TRIGSTR_805", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1105", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_1221", SoundNull, "TRIGSTR_1380", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1384", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_1504", SoundNull, "TRIGSTR_1505", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_1510", SoundNull, "TRIGSTR_1511", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_1512", SoundNull, "TRIGSTR_1513", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1514", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_1515", SoundNull, "TRIGSTR_1516", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_1517", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_649", SoundNull, "TRIGSTR_708", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_721", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_722", SoundNull, "TRIGSTR_723", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, 触发单位(), GetHeroProperName(触发单位()), SoundNull, "TRIGSTR_735", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, "TRIGSTR_736", SoundNull, "TRIGSTR_739", AddSetToAdd, 0, WaitDontWait
       │      │    单位发布命令(目标): gg_unit_E009_0029, UnitOrderAttackUnit, 触发单位()
       │      │    运行计时器 MI_JSQ (一次性, 120.00s)
       │      │    循环整数A 1→5
       │      │      └─ 显示文本→玩家循环整数A(): 0
       │      │    FlashQuestDialogButtonBJ
       │      │    销毁触发器(自身)
       │      └─ 否则
       │           显示文本→(触发单位()的所有者): 0
       └─ 否则
            显示文本→(触发单位()的所有者): 0
            杀死 触发单位()
```

### 未命名触发器 014

```text
触发器: 未命名触发器 014 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 MI_JSQ 到期
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 单位发布命令(立即): gg_unit_E009_0029, UnitOrderStop
  ├─ RemoveGuardPosition: gg_unit_E009_0029
  ├─ PanCameraToTimed: -7000.00, -7000.00, 0
  └─ 循环整数A 1→5
       └─ 如果
            ├─ 条件: (YX_7[循环整数A()]类型ID) == Eilm
            ├─ 则
            │    设置无敌: YX_7[循环整数A()], InvulnerabilityVulnerable
            │    PauseUnit: YX_7[循环整数A()], PauseUnpauseOptionUnpause
            │    TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E009_0029, GetHeroProperName(gg_unit_E009_0029), SoundNull, "TRIGSTR_1519", AddSetToAdd, 0, WaitDontWait
            │    命令 gg_unit_E009_0029 → UnitOrderMove 到 -7900.00
            │    SetPlayerTechResearchedSwap: Rhfs, 1, (YX_7[循环整数A()]的所有者)
            │    移除 gg_unit_E009_0029
            └─ 否则: (无)
```

### 未命名触发器 012

```text
触发器: 未命名触发器 012 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_E00K_0041 - 单位死亡
条件
  ├─ 英雄等级(凶手单位()) OperatorGreaterEq 400
  └─ (凶手单位()类型ID) == Eilm
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 复活英雄: 触发单位(), 单位X坐标(触发单位()), 单位Y坐标(触发单位()), ShowHideHide
  ├─ 设置单位归属: 触发单位(), 非玩家, 改变颜色
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1182", SoundNull, "TRIGSTR_1183", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1368", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1369", SoundNull, "TRIGSTR_1378", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1417", SoundNull, "TRIGSTR_1428", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1386", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1490", SoundNull, "TRIGSTR_1495", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1529", SoundNull, "TRIGSTR_1532", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1533", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1535", SoundNull, "TRIGSTR_1536", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1541", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, gg_unit_E00K_0041, "TRIGSTR_1544", SoundNull, "TRIGSTR_1547", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: DY_WJZ, 凶手单位(), GetHeroProperName(凶手单位()), SoundNull, "TRIGSTR_1553", AddSetToAdd, 0, WaitDontWait
  ├─ FlashQuestDialogButtonBJ
  ├─ QuestSetDescriptionBJ: RW_5[5], "TRIGSTR_1585"
  ├─ 循环整数A 1→5
  │    └─ 显示文本→玩家循环整数A(): 0
  └─ 销毁触发器(自身)
```

### 未命名触发器 056

```text
触发器: 未命名触发器 056 (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.03)
条件
  └─ 无
动作
  └─ 循环整数A 1→10
       └─ 如果
            ├─ 条件: PFWZ_ZS[循环整数A()] != -10
            ├─ 则
            │    SetTextTagTextBJ: PFWZ[循环整数A()], PFWZ_ZCF[循环整数A()], (20.00 - (IAbsBJ(PFWZ_ZS[循环整数A()])转实数))
            │    设置 PFWZ_ZS[循环整数A()] = (PFWZ_ZS[循环整数A()] - 1)
            └─ 否则: (无)
```

### 未命名触发器 070

```text
触发器: 未命名触发器 070 (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 PFWZ_JSQ 到期
条件
  └─ 无
动作
  └─ 关闭触发器 gg_trg____________________056
```

### 001

```text
触发器: 001 (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 循环整数A 1→10
  │    └─ 如果
  │         ├─ 条件: PFWZ_ZS[循环整数A()] == -10
  │         ├─ 则
  │         │    设置 PFWZ_ZCF[循环整数A()] = (X_zs转字符串) + "!"
  │         │    设置 PFWZ[循环整数A()] = bj_lastCreatedTextTag
  │         │    设置 PFWZ_ZS[循环整数A()] = 10
  │         │    开启触发器 gg_trg____________________056
  │         │    运行计时器 PFWZ_JSQ (一次性, 1.00s)
  │         │    CustomScriptCode: ScriptCode00
  │         └─ 否则: (无)
  ├─ SetTextTagVelocityBJ: bj_lastCreatedTextTag, 64, 90
  ├─ SetTextTagPermanentBJ: bj_lastCreatedTextTag, EnableDisableDisable
  ├─ SetTextTagLifespanBJ: bj_lastCreatedTextTag, 4.00
  └─ SetTextTagFadepointBJ: bj_lastCreatedTextTag, 2.00
```

### 未命名触发器 004

```text
触发器: 未命名触发器 004 (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ 攻击单位() == gg_unit_E009_0029
  └─ IsUnitAlly(触发单位(), (攻击单位()的所有者)) == TRUE
动作
  └─ 单位发布命令(立即): 攻击单位(), UnitOrderStop
```

### 未命名触发器 009

```text
触发器: 未命名触发器 009 (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_e00N_0040 - UnitEventDamaged
条件
  └─ 伤害值() OperatorGreater 2.50
动作
  └─ 显示文本→(伤害来源()的所有者): 0
```

