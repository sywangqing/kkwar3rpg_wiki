---
title: 神墓 2.7C — 👤 01 玩家命令与英雄
category: kk-triggers
slug: shenmu/01-commands
description: 买英雄/选英雄/复活/玩家操作相关
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 👤 01 玩家命令与英雄

> 买英雄/选英雄/复活/玩家操作相关

**共 41 个触发器**

## 📑 触发器目录

- [BuyHero](#trigger-01_000_BuyHero)
- [BuyHero2](#trigger-01_001_BuyHero2)
- [RandomHero](#trigger-01_002_RandomHero)
- [RandomJiuGui](#trigger-01_003_RandomJiuGui)
- [ReviveHero](#trigger-01_004_ReviveHero)
- [ReviveHeroLumber](#trigger-01_005_ReviveHeroLumber)
- [主机命令](#trigger-01_006_主机命令)
- [ModifyLevel](#trigger-01_007_ModifyLevel)
- [AddBoss](#trigger-01_008_AddBoss)
- [AddTeShu](#trigger-01_009_AddTeShu)
- [CleanItem](#trigger-01_010_CleanItem)
- [群体命令](#trigger-01_011_群体命令)
- [ExitCenimaMode](#trigger-01_012_ExitCenimaMode)
- [BackBase](#trigger-01_013_BackBase)
- [BackRevivePoint](#trigger-01_014_BackRevivePoint)
- [MoveCase](#trigger-01_015_MoveCase)
- [ShowWangCaiKill](#trigger-01_016_ShowWangCaiKill)
- [ShowDaoXuanBaoJi](#trigger-01_017_ShowDaoXuanBaoJi)
- [TFHQ](#trigger-01_018_TFHQ)
- [PlayerLeft](#trigger-01_019_PlayerLeft)
- [HigherCamera](#trigger-01_020_HigherCamera)
- [OfflinePlayerControl](#trigger-01_021_OfflinePlayerControl)
- [OfflinePlayerResource](#trigger-01_022_OfflinePlayerResource)
- [MoneyTooMuch](#trigger-01_023_MoneyTooMuch)
- [LumberExchangeMoney](#trigger-01_024_LumberExchangeMoney)
- [MoneyExchangeLumber](#trigger-01_025_MoneyExchangeLumber)
- [ChangeLeaderboardLumber](#trigger-01_026_ChangeLeaderboardLumber)
- [ShowWeaponKill](#trigger-01_027_ShowWeaponKill)
- [GetHelp](#trigger-01_028_GetHelp)
- [ExchangeHero](#trigger-01_029_ExchangeHero)
- [关闭触发](#trigger-01_030_关闭触发)
- [TurnOffOrder](#trigger-01_031_TurnOffOrder)
- [埋骨地触发](#trigger-01_032_埋骨地触发)
- [BaseBeDamaged](#trigger-01_033_BaseBeDamaged)
- [BaseRevive](#trigger-01_034_BaseRevive)
- [测试选项](#trigger-01_035_测试选项)
- [Player1Cheat1](#trigger-01_036_Player1Cheat1)
- [Player1Cheat2](#trigger-01_037_Player1Cheat2)
- [SetLV](#trigger-01_038_SetLV)
- [SetTIME](#trigger-01_039_SetTIME)
- [JustForTestNoCD](#trigger-01_040_JustForTestNoCD)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-01_000_BuyHero">
<summary><strong>📌 BuyHero</strong> <code>01_000_BuyHero</code></summary>

```text
触发器: BuyHero (玩家/英雄) [✓] — 英雄选择
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_ntav_0012 - 出售单位
条件
  └─ 无
动作
  ├─ 设置 uPlayerHeros[玩家号((被贩卖单位()的所有者))] = 被贩卖单位()
  ├─ 为 (触发单位()的所有者) 选择 触发单位()
  ├─ 设置 pTemp = (gg_unit_ubon_0001的位置)
  ├─ 创建 1个|ufro|→(被贩卖单位()的所有者) 在 pTemp 面向默认朝向
  ├─ 设置 uXiaoBingLong[玩家号((被贩卖单位()的所有者))] = 最后创建的单位()
  ├─ 创建 1个|hrtt|→(被贩卖单位()的所有者) 在 pTemp 面向默认朝向
  ├─ 设置 uXiangZi[玩家号((被贩卖单位()的所有者))] = 最后创建的单位()
  ├─ 清除点 pTemp
  ├─ 设置 (被贩卖单位()的所有者) 名字 = "銆?" + sPlayerInitName[玩家号((被贩卖单位()的所有者))] + "銆?" + (单位名:被贩卖单位())
  ├─ 循环整数A 1→7: 限制单位可用((被贩卖单位()类型ID), 0, 玩家循环整数A())
  ├─ 如果
  │    ├─ 条件: (被贩卖单位()类型ID) == N00L
  │    ├─ 则
  │    │    运行计时器 tBaoFengXue[玩家号((被贩卖单位()的所有者))] (循环, 5.00s)
  │    │    设置 uWuJinChangYe = 被贩卖单位()
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (被贩卖单位()类型ID) == E000
  │    ├─ 则
  │    │    设置 uSiWangQiXi = 被贩卖单位()
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (被贩卖单位()类型ID) == N00K
  │    ├─ 则
  │    │    添加事件到 gg_trg_SetHeroInvincible: 单位生命值事件(被贩卖单位(), 小于, 1.00)
  │    └─ 否则: (无)
  ├─ 循环整数A 1→14
  │    ├─ 限制 (被贩卖单位()的所有者) 的 uHeroType[循环整数A]: 上限0
  │    └─ 如果
  │         ├─ 条件: (被贩卖单位()类型ID) == uHeroType[循环整数A]
  │         ├─ 则
  │         │    设置 bHeroSelected[循环整数A] = true
  │         └─ 否则: (无)
  └─ 限制 (被贩卖单位()的所有者) 的 N00Y: 上限0
```

</details>

<details id="trigger-01_001_BuyHero2">
<summary><strong>📌 BuyHero2</strong> <code>01_001_BuyHero2</code></summary>

```text
触发器: BuyHero2 (玩家/英雄) [✓] — 英雄选择
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_hcth_0063 - 出售单位
条件
  └─ 无
动作
  ├─ 设置 uPlayerHeros[玩家号((被贩卖单位()的所有者))] = 被贩卖单位()
  ├─ 为 (触发单位()的所有者) 选择 触发单位()
  ├─ 设置 pTemp = (gg_unit_ubon_0001的位置)
  ├─ 创建 1个|ufro|→(被贩卖单位()的所有者) 在 pTemp 面向默认朝向
  ├─ 设置 uXiaoBingLong[玩家号((被贩卖单位()的所有者))] = 最后创建的单位()
  ├─ 创建 1个|hrtt|→(被贩卖单位()的所有者) 在 pTemp 面向默认朝向
  ├─ 设置 uXiangZi[玩家号((被贩卖单位()的所有者))] = 最后创建的单位()
  ├─ 清除点 pTemp
  ├─ 设置 (被贩卖单位()的所有者) 名字 = "銆?" + sPlayerInitName[玩家号((被贩卖单位()的所有者))] + "銆?" + (单位名:被贩卖单位())
  ├─ 如果
  │    ├─ 条件: (被贩卖单位()类型ID) == N00W
  │    ├─ 则
  │    │    添加事件到 gg_trg_JinShengWuWei: 单位生命值事件(被贩卖单位(), LimitOpEqual, 0.00)
  │    └─ 否则: (无)
  ├─ 循环整数A 1→7: 限制单位可用((被贩卖单位()类型ID), 0, 玩家循环整数A())
  ├─ 循环整数A 1→14
  │    ├─ 限制 (被贩卖单位()的所有者) 的 uHeroType[循环整数A]: 上限0
  │    └─ 如果
  │         ├─ 条件: (被贩卖单位()类型ID) == uHeroType[循环整数A]
  │         ├─ 则
  │         │    设置 bHeroSelected[循环整数A] = true
  │         └─ 否则: (无)
  └─ 限制 (被贩卖单位()的所有者) 的 N00Y: 上限0
```

</details>

<details id="trigger-01_002_RandomHero">
<summary><strong>📌 RandomHero</strong> <code>01_002_RandomHero</code></summary>

```text
触发器: RandomHero (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ uPlayerHeros[玩家号(触发玩家())] == UnitNull
动作
  ├─ CustomScriptCode: "local integer i"
  ├─ CustomScriptCode: "local integer c"
  ├─ CustomScriptCode: "local integer m"
  └─ 如果
       ├─ 条件: 随机[1~50] != 3
       ├─ 则
       │    设置玩家属性: 触发玩家(), PlayerStateLumber, (玩家属性值(触发玩家(), PlayerStateLumber) - 20)
       │    CustomScriptCode: "set c=1"
       │    CustomScriptCode: "set m=0"
       │    关闭触发器 当前触发器()
       │    设置 pTemp = (gg_unit_ntav_0012的位置)
       │    设置 iTemp = 0
       │    循环整数A 1→14
       │      └─ 如果
       │           ├─ 条件: bHeroSelected[循环整数A] == TRUE
       │           ├─ 则
       │           │    设置 iTemp = (iTemp + 1)
       │           └─ 否则: (无)
       │    CustomScriptCode: "set i=GetRandomInt(1,udg_iTemp)"
       │    CustomScriptCode: "loop"
       │    CustomScriptCode: "exitwhen c>14"
       │    CustomScriptCode: "if not udg_bHeroSelected[c] then"
       │    CustomScriptCode: "set m=m+1"
       │    CustomScriptCode: "endif"
       │    CustomScriptCode: "if m==i then"
       │    CustomScriptCode: "set udg_uPlayerHeros[GetConvertedPlayerId(GetTriggerPlayer())] = CreateUnitAt..."
       │    CustomScriptCode: "set c=20"
       │    CustomScriptCode: "endif"
       │    CustomScriptCode: "set c=c+1"
       │    CustomScriptCode: "endloop"
       │    清除点 pTemp
       │    为 触发玩家() 选择 uPlayerHeros[玩家号(触发玩家())]
       │    设置 pTemp = (gg_unit_ubon_0001的位置)
       │    创建 1个|ufro|→触发玩家() 在 pTemp 面向默认朝向
       │    设置 uXiaoBingLong[玩家号(触发玩家())] = 最后创建的单位()
       │    创建 1个|hrtt|→触发玩家() 在 pTemp 面向默认朝向
       │    设置 uXiangZi[玩家号(触发玩家())] = 最后创建的单位()
       │    清除点 pTemp
       │    设置 uTemp = uPlayerHeros[玩家号(触发玩家())]
       │    设置 触发玩家() 名字 = "銆?" + sPlayerInitName[玩家号(触发玩家())] + "銆?" + (单位名:uTemp)
       │    SetPlayerHandicapXPBJ: 触发玩家(), 110.00
       │    显示文本→grpOnline: (玩家名:触发玩家()) + "选择了随机英雄，额外获得10%的经验加成。"
       │    循环整数A 1→7: 限制单位可用((uTemp类型ID), 0, 玩家循环整数A())
       │    如果
       │      ├─ 条件: (uTemp类型ID) == N00L
       │      ├─ 则
       │      │    运行计时器 tBaoFengXue[玩家号(触发玩家())] (循环, 5.00s)
       │      │    设置 uWuJinChangYe = uTemp
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: (uTemp类型ID) == E000
       │      ├─ 则
       │      │    设置 uSiWangQiXi = uTemp
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: (uTemp类型ID) == N00K
       │      ├─ 则
       │      │    添加事件到 gg_trg_SetHeroInvincible: 单位生命值事件(uTemp, 小于, 1.00)
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: (uTemp类型ID) == N00W
       │      ├─ 则
       │      │    添加事件到 gg_trg_JinShengWuWei: 单位生命值事件(uPlayerHeros[玩家号(触发玩家())], 小于, 0.90)
       │      └─ 否则: (无)
       │    循环整数A 1→14
       │      ├─ 限制 触发玩家() 的 uHeroType[循环整数A]: 上限0
       │      └─ 如果
       │           ├─ 条件: (uTemp类型ID) == uHeroType[循环整数A]
       │           ├─ 则
       │           │    设置 bHeroSelected[循环整数A] = true
       │           └─ 否则: (无)
       │    限制 触发玩家() 的 N00Y: 上限0
       │    开启触发器 当前触发器()
       └─ 否则
            设置 pTemp = (gg_unit_ntav_0012的位置)
            设置 uPlayerHeros[玩家号(触发玩家())] = 创建单位(指定点)(触发玩家(), N00Y, pTemp, 0)
            添加事件到 gg_trg_RepickAbility: 注册单位事件(uPlayerHeros[玩家号(触发玩家())], UnitEventSpellEffect)
            SetPlayerTechResearchedSwap: Rhcd, 1, 触发玩家()
            设置玩家属性: 触发玩家(), PlayerStateLumber, (玩家属性值(触发玩家(), PlayerStateLumber) - 20)
            为 触发玩家() 选择 uPlayerHeros[玩家号(触发玩家())]
            设置 pTemp = (gg_unit_ubon_0001的位置)
            创建 1个|ufro|→触发玩家() 在 pTemp 面向默认朝向
            设置 uXiaoBingLong[玩家号(触发玩家())] = 最后创建的单位()
            创建 1个|hrtt|→触发玩家() 在 pTemp 面向默认朝向
            设置 uXiangZi[玩家号(触发玩家())] = 最后创建的单位()
            清除点 pTemp
            设置 uTemp = uPlayerHeros[玩家号(触发玩家())]
            设置 触发玩家() 名字 = "銆?" + (玩家名:触发玩家()) + "銆?" + (单位名:uTemp)
            SetPlayerHandicapXPBJ: 触发玩家(), 110.00
            显示文本→grpOnline: (玩家名:触发玩家()) + "选择了随机英雄，额外获得10%的经验加成。"
            循环整数A 1→14
              ├─ 限制 触发玩家() 的 uHeroType[循环整数A]: 上限0
              └─ 如果
                   ├─ 条件: (uTemp类型ID) == uHeroType[循环整数A]
                   ├─ 则
                   │    设置 bHeroSelected[循环整数A] = true
                   └─ 否则: (无)
            限制 触发玩家() 的 N00Y: 上限0
            开启触发器 当前触发器()
```

</details>

<details id="trigger-01_003_RandomJiuGui">
<summary><strong>📌 RandomJiuGui</strong> <code>01_003_RandomJiuGui</code></summary>

```text
触发器: RandomJiuGui (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ uPlayerHeros[玩家号(触发玩家())] == UnitNull
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 pTemp = (gg_unit_ntav_0012的位置)
  ├─ 设置 uPlayerHeros[玩家号(触发玩家())] = 创建单位(指定点)(触发玩家(), N00Y, pTemp, 0)
  ├─ 添加事件到 gg_trg_RepickAbility: 注册单位事件(uPlayerHeros[玩家号(触发玩家())], UnitEventSpellEffect)
  ├─ SetPlayerTechResearchedSwap: Rhcd, 1, 触发玩家()
  ├─ 设置玩家属性: 触发玩家(), PlayerStateLumber, (玩家属性值(触发玩家(), PlayerStateLumber) - 20)
  ├─ 为 触发玩家() 选择 uPlayerHeros[玩家号(触发玩家())]
  ├─ 设置 pTemp = (gg_unit_ubon_0001的位置)
  ├─ 创建 1个|ufro|→触发玩家() 在 pTemp 面向默认朝向
  ├─ 设置 uXiaoBingLong[玩家号(触发玩家())] = 最后创建的单位()
  ├─ 创建 1个|hrtt|→触发玩家() 在 pTemp 面向默认朝向
  ├─ 设置 uXiangZi[玩家号(触发玩家())] = 最后创建的单位()
  ├─ 清除点 pTemp
  ├─ 设置 uTemp = uPlayerHeros[玩家号(触发玩家())]
  ├─ 设置 触发玩家() 名字 = "銆?" + sPlayerInitName[玩家号(触发玩家())] + "銆?" + (单位名:uTemp)
  ├─ SetPlayerHandicapXPBJ: 触发玩家(), 110.00
  ├─ 显示文本→grpOnline: (玩家名:触发玩家()) + "选择了随机英雄，额外获得10%的经验加成。"
  ├─ 循环整数A 1→14
  │    ├─ 限制 触发玩家() 的 uHeroType[循环整数A]: 上限0
  │    └─ 如果
  │         ├─ 条件: (uTemp类型ID) == uHeroType[循环整数A]
  │         ├─ 则
  │         │    设置 bHeroSelected[循环整数A] = true
  │         └─ 否则: (无)
  ├─ 限制 触发玩家() 的 N00Y: 上限0
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-01_004_ReviveHero">
<summary><strong>📌 ReviveHero</strong> <code>01_004_ReviveHero</code></summary>

```text
触发器: ReviveHero (玩家/英雄) [✓] — 死亡复活
───────────────────────────────────────────────────────
事件
  └─ 玩家单位 - 单位死亡
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: (凶手单位()类型ID) == U002
  │    ├─ 则
  │    │    设置生命百分比: 凶手单位(), (单位生命百分比(凶手单位()) + 5.00)
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 单位在单位组中(触发单位(), grpReviveHeroLumber) == TRUE
  │    ├─ 则
  │    │    添加 触发单位() → grpReviveHeroLumber
  │    │    添加事件到 gg_trg_ReviveHeroLumber: 注册单位事件(触发单位(), 复活完成)
  │    └─ 否则: (无)
  ├─ 设置 iTemp = 玩家号((触发单位()的所有者))
  ├─ 设置 iHeroDeadTime[iTemp] = (iHeroDeadTime[iTemp] + 1)
  ├─ 排行榜 TopBoard[5,(iTemp + 1)] = (iHeroDeadTime[iTemp]转字符串)
  ├─ 循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, (单位名:触发单位()) + "|cffffcc00刚刚惨死于|r" + (单位名:凶手单位()) + "|cffffcc00之手。|r")
  ├─ 如果
  │    ├─ 条件: 整数比较(单位技能等级(A084, 触发单位()), ==, 1)
  │    ├─ 则: 暂停计时器(tBaoFengXue[iTemp])
  │    └─ 否则: 无动作()
  ├─ 如果
  │    ├─ 条件: 单位比较(触发单位(), OperatorEqualENE, uSiWangQiXi)
  │    ├─ 则: 暂停计时器(tSiWangQiXi)
  │    └─ 否则: 无动作()
  ├─ 如果
  │    ├─ 条件: 单位持有物品类型(触发单位(), I04B) == TRUE
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: (触发单位()的所有者) == 玩家7(绿)
  │    │      ├─ 则
  │    │      │    等待 10.00s
  │    │      └─ 否则
  │    │           等待 2.00s
  │    └─ 否则
  │         如果
  │           ├─ 条件: (触发单位()的所有者) == 玩家7(绿)
  │           ├─ 则
  │           │    等待 60.00s
  │           └─ 否则
  │                等待 (5.00 + (玩家科技等级(Rhme, 玩家9(灰))转实数))s
  ├─ 如果
  │    ├─ 条件: (触发单位()的所有者) == 玩家7(绿)
  │    ├─ 则
  │    │    复活英雄 触发单位() 在 pHG
  │    └─ 否则
  │         复活英雄 触发单位() 在 pFuHuo
  ├─ 如果
  │    ├─ 条件: 整数比较(单位技能等级(A084, 触发单位()), ==, 1)
  │    ├─ 则: 运行计时器(tBaoFengXue[玩家号((触发单位()的所有者))], 循环, 5.00)
  │    └─ 否则: 无动作()
  └─ 如果
       ├─ 条件: (单位比较(触发单位(), OperatorEqualENE, uSiWangQiXi) 且 整数比较(单位技能等级(A03B, 触发单位()), ==, 1))
       ├─ 则: 运行计时器(tSiWangQiXi, 循环, 1.00)
       └─ 否则: 无动作()
```

</details>

<details id="trigger-01_005_ReviveHeroLumber">
<summary><strong>📌 ReviveHeroLumber</strong> <code>01_005_ReviveHeroLumber</code></summary>

```text
触发器: ReviveHeroLumber (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 整数比较(单位技能等级(A084, 正复活的单位()), ==, 1)
  │    ├─ 则: 运行计时器(tBaoFengXue[玩家号((正复活的单位()的所有者))], 循环, 5.00)
  │    └─ 否则: 无动作()
  └─ 如果
       ├─ 条件: (单位比较(正复活的单位(), OperatorEqualENE, uSiWangQiXi) 且 整数比较(单位技能等级(A03B, 正复活的单位()), ==, 1))
       ├─ 则: 运行计时器(tSiWangQiXi, 循环, 1.00)
       └─ 否则: 无动作()
```

</details>

<details id="trigger-01_006_主机命令">
<summary><strong>📌 主机命令</strong> <code>01_006_主机命令</code></summary>

```text
触发器: 主机命令 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-01_007_ModifyLevel">
<summary><strong>📌 ModifyLevel</strong> <code>01_007_ModifyLevel</code></summary>

```text
触发器: ModifyLevel (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 iTemp = 字符串转整数(取子字符串(玩家聊天字符串(), 5, 7))
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iTemp OperatorGreater 玩家科技等级(Rhme, 玩家9(灰))
       │    ├─ iTemp OperatorLessEq 100
       ├─ 则
       │    销毁触发器(自身)
       │    显示文本→grpOnline: "|cffff0000玩家一提升了游戏难度，当前难度为" + 取子字符串(玩家聊天字符串(), 5, 7)
       │    MultiboardSetTitleText: TopBoard, "神之墓地2.7C 难度提升" + 取子字符串(玩家聊天字符串(), 5, 7)
       │    SetPlayerTechResearchedSwap: Rhme, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: Rhme, iTemp, PlayerNA
       │    SetPlayerTechResearchedSwap: Rhar, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: Rhar, iTemp, PlayerNA
       │    SetPlayerTechResearchedSwap: R004, iTemp, 玩家8(粉)
       │    SetPlayerTechResearchedSwap: R003, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: R004, iTemp, PlayerNA
       │    如果
       │      ├─ 条件: iTemp OperatorGreater 90
       │      ├─ 则
       │      │    设置技能等级: gg_unit_Uclc_0123, A09M, (iTemp - 90)
       │      └─ 否则: (无)
       └─ 否则
            显示文本→pFirstPlayer: 0
```

</details>

<details id="trigger-01_008_AddBoss">
<summary><strong>📌 AddBoss</strong> <code>01_008_AddBoss</code></summary>

```text
触发器: AddBoss (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ bXianFeng == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ 设置 bXianFeng = true
  ├─ 显示文本→grpOnline: "TRIGSTR_1148"
  ├─ 设置 uXianFeng[1] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[2] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[3] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[4] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  └─ 循环整数A 1→4
       ├─ SetHeroLevel: uXianFeng[循环整数A()], 5, ShowHideHide
       ├─ SelectHeroSkill: uXianFeng[循环整数A()], A074
       ├─ SelectHeroSkill: uXianFeng[循环整数A()], A073
       ├─ SelectHeroSkill: uXianFeng[循环整数A()], A075
       └─ SelectHeroSkill: uXianFeng[循环整数A()], A076
```

</details>

<details id="trigger-01_009_AddTeShu">
<summary><strong>📌 AddTeShu</strong> <code>01_009_AddTeShu</code></summary>

```text
触发器: AddTeShu (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ bTeShu == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ 显示文本→grpOnline: "TRIGSTR_2513"
  ├─ 设置 bTeShu = true
  ├─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
  └─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
```

</details>

<details id="trigger-01_010_CleanItem">
<summary><strong>📌 CleanItem</strong> <code>01_010_CleanItem</code></summary>

```text
触发器: CleanItem (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 显示文本→grpOnline: "|cffff0000" + (玩家名:触发玩家()) + "清空了地面的食人魔血液和金币。|r"
  ├─ EnumItemsInRectBJMultiple: gg_rct_____________01
  ├─ EnumItemsInRectBJMultiple: gg_rct__________01
  ├─ PolledWait: 120.00
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-01_011_群体命令">
<summary><strong>📌 群体命令</strong> <code>01_011_群体命令</code></summary>

```text
触发器: 群体命令 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-01_012_ExitCenimaMode">
<summary><strong>📌 ExitCenimaMode</strong> <code>01_012_ExitCenimaMode</code></summary>

```text
触发器: ExitCenimaMode (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: bExitCnima[玩家号(触发玩家())] == TRUE
       ├─ 则
       │    设置 bExitCnima[玩家号(触发玩家())] = false
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, 触发玩家()
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    战争迷雾开关: EnabledDisabledEnabled
       │    迷雾遮罩开关: EnabledDisabledEnabled
       └─ 否则
            设置 bExitCnima[玩家号(触发玩家())] = true
            PolledWait: 0.10
            设置 bExitCnima[玩家号(触发玩家())] = false
```

</details>

<details id="trigger-01_013_BackBase">
<summary><strong>📌 BackBase</strong> <code>01_013_BackBase</code></summary>

```text
触发器: BackBase (玩家/英雄) [✓] — 回城
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 触发玩家() == (uFuShenMoDi的所有者)
动作
  ├─ 如果
  │    ├─ 条件: 单位是否暂停(uPlayerHeros[玩家号(触发玩家())]) == TRUE
  │    ├─ 则
  │    │    移动单位: uPlayerHeros[玩家号(触发玩家())], pHG
  │    └─ 否则: (无)
  ├─ 移动单位: uPlayerHeros[(20 + 玩家号(触发玩家()))], pHG
  └─ 平移镜头: 触发玩家(), pHG, 0
```

</details>

<details id="trigger-01_014_BackRevivePoint">
<summary><strong>📌 BackRevivePoint</strong> <code>01_014_BackRevivePoint</code></summary>

```text
触发器: BackRevivePoint (玩家/英雄) [✓] — 回城
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 触发玩家() == (uFuShenMoDi的所有者)
动作
  ├─ 如果
  │    ├─ 条件: 单位是否暂停(uPlayerHeros[玩家号(触发玩家())]) == TRUE
  │    ├─ 则
  │    │    移动单位: uPlayerHeros[玩家号(触发玩家())], pFuHuo
  │    └─ 否则: (无)
  ├─ 移动单位: uPlayerHeros[(20 + 玩家号(触发玩家()))], pFuHuo
  └─ 平移镜头: 触发玩家(), pFuHuo, 0
```

</details>

<details id="trigger-01_015_MoveCase">
<summary><strong>📌 MoveCase</strong> <code>01_015_MoveCase</code></summary>

```text
触发器: MoveCase (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uPlayerHeros[玩家号(触发玩家())]的位置)
  ├─ 移动单位: uXiangZi[玩家号(触发玩家())], pTemp
  └─ 清除点 pTemp
```

</details>

<details id="trigger-01_016_ShowWangCaiKill">
<summary><strong>📌 ShowWangCaiKill</strong> <code>01_016_ShowWangCaiKill</code></summary>

```text
触发器: ShowWangCaiKill (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 iTemp = 玩家号(触发玩家())
  ├─ 设置 uTemp = uPlayerHeros[iTemp]
  └─ 如果
       ├─ 条件: 单位技能等级(uTemp, A006) OperatorGreater 0
       ├─ 则
       │    显示文本→触发玩家(): 0
       └─ 否则
            显示文本→触发玩家(): 0
```

</details>

<details id="trigger-01_017_ShowDaoXuanBaoJi">
<summary><strong>📌 ShowDaoXuanBaoJi</strong> <code>01_017_ShowDaoXuanBaoJi</code></summary>

```text
触发器: ShowDaoXuanBaoJi (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 iTemp = 玩家号(触发玩家())
  ├─ 设置 uTemp = uPlayerHeros[iTemp]
  └─ 如果
       ├─ 条件: 单位技能等级(uTemp, A08V) OperatorGreater 0
       ├─ 则
       │    显示文本→触发玩家(): 0
       └─ 否则
            显示文本→触发玩家(): 0
```

</details>

<details id="trigger-01_018_TFHQ">
<summary><strong>📌 TFHQ</strong> <code>01_018_TFHQ</code></summary>

```text
触发器: TFHQ (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ bTFHQ[玩家号(触发玩家())] == TRUE
  └─ uPlayerHeros[玩家号(触发玩家())] == UnitNull
动作
  ├─ 如果
  │    ├─ 条件: (uPlayerHeros[玩家号(触发玩家())]类型ID) == Eilm
  │    ├─ 则
  │    │    显示文本→触发玩家(): 0
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 49
  │    ├─ 则
  │    │    设置 iTemp = 字符串转整数(取子字符串(玩家聊天字符串(), 6, 8))
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ iTemp OperatorGreater 14
  │    │      │    ├─ iTemp OperatorLess 1
  │    │      ├─ 则
  │    │      │    设置 iTemp = 随机[1~14]
  │    │      └─ 否则: (无)
  │    └─ 否则
  │         设置 iTemp = 随机[1~14]
  └─ 如果
       ├─ 条件: 单位技能等级(uPlayerHeros[玩家号(触发玩家())], aTianFu[iTemp]) OperatorGreater 0
       ├─ 则
       │    显示文本→grpOnline: (单位名:uPlayerHeros[玩家号(触发玩家())]) + "获取了天赋技能：" + "自己的天赋，奖励重新选取的机会。"
       └─ 否则
            添加技能: uPlayerHeros[玩家号(触发玩家())], aTianFu[iTemp]
            UnitMakeAbilityPermanent: uPlayerHeros[玩家号(触发玩家())], OnOffOn, aTianFu[iTemp]
            如果
              ├─ 条件: iTemp == 3
              ├─ 则
              │    运行计时器 tBaoFengXue[玩家号(触发玩家())] (循环, 5.00s)
              └─ 否则: (无)
            如果
              ├─ 条件: iTemp == 4
              ├─ 则
              │    添加技能: uPlayerHeros[玩家号(触发玩家())], A004
              │    UnitMakeAbilityPermanent: uPlayerHeros[玩家号(触发玩家())], OnOffOn, A004
              └─ 否则: (无)
            如果
              ├─ 条件: iTemp == 12
              ├─ 则
              │    UnitMakeAbilityPermanent: uPlayerHeros[玩家号(触发玩家())], OnOffOn, A099
              └─ 否则: (无)
            如果
              ├─ 条件: iTemp == 14
              ├─ 则
              │    添加事件到 gg_trg_JinShengWuWei: 单位生命值事件(uPlayerHeros[玩家号(触发玩家())], 小于, 0.90)
              └─ 否则: (无)
            显示文本→grpOnline: (单位名:uPlayerHeros[玩家号(触发玩家())]) + "获取了天赋技能：" + 技能名称(aTianFu[iTemp])
            设置 bTFHQ[玩家号(触发玩家())] = true
```

</details>

<details id="trigger-01_019_PlayerLeft">
<summary><strong>📌 PlayerLeft</strong> <code>01_019_PlayerLeft</code></summary>

```text
触发器: PlayerLeft (玩家/英雄) [✓] — 玩家离开
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: grpOnline
  ├─ ForForceMultiple: grpOffline
  ├─ ForceAddPlayer: grpOffline, 触发玩家()
  ├─ ForceRemovePlayer: grpOnline, 触发玩家()
  ├─ 循环整数A 1→6: 移动物品到点(单位栏位物品(uXiaoBingLong[玩家号(触发玩家())], 循环整数A), pHG)
  ├─ 循环整数A 1→6: 移动物品到点(单位栏位物品(uXiangZi[玩家号(触发玩家())], 循环整数A), pHG)
  ├─ 设置 grpTemp = 玩家符合条件的单位(触发玩家(), (布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false) 且 整数比较(单位技能等级(过滤单位(), Aloc), ==, 0)))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ 移除 选取单位()
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 玩家全部单位(触发玩家())
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ 如果
  │         ├─ 条件: 单位类型判断(选取单位(), 英雄) == TRUE
  │         ├─ 则
  │         │    循环整数A 1→6: 移动物品到点(单位栏位物品(选取单位(), 循环整数A), pHG)
  │         │    移动单位: 选取单位(), pFuHuo
  │         └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ ForForceMultiple: grpOnline
  └─ 如果
       ├─ 条件: 触发玩家() == pFirstPlayer
       ├─ 则
       │    循环整数A 1→7
       │      └─ 如果
       │           ├─ 条件: 全部成立
       │           │    ├─ 玩家控制者比较(玩家控制者类型(玩家循环整数A), OperatorEqualENE, MapControlUser)
       │           │    ├─ 玩家槽位状态比较(玩家槽位状态(玩家循环整数A), OperatorEqualENE, PlayerSlotStatePlaying)
       │           ├─ 则
       │           │    设置 pFirstPlayer = 玩家循环整数A
       │           │    CustomScriptCode: "set bj_forLoopAIndex=8"
       │           └─ 否则: (无)
       │    添加事件到 gg_trg_ModifyLevel: 玩家聊天(pFirstPlayer, "-nd ", ChatMatchTypeSubstring)
       │    添加事件到 gg_trg_AddBoss: 玩家聊天(pFirstPlayer, "-boss", ChatMatchTypeExact)
       │    添加事件到 gg_trg_AddTeShu: 玩家聊天(pFirstPlayer, "-ts", ChatMatchTypeExact)
       │    添加事件到 gg_trg_CleanItem: 玩家聊天(pFirstPlayer, "-qc", ChatMatchTypeExact)
       └─ 否则: (无)
```

</details>

<details id="trigger-01_020_HigherCamera">
<summary><strong>📌 HigherCamera</strong> <code>01_020_HigherCamera</code></summary>

```text
触发器: HigherCamera (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 rTemp = 镜头属性(CameraFieldTargetDistance)
  └─ SetCameraFieldForPlayer: 触发玩家(), CameraFieldTargetDistance, (rTemp + 200.00), 0.50
```

</details>

<details id="trigger-01_021_OfflinePlayerControl">
<summary><strong>📌 OfflinePlayerControl</strong> <code>01_021_OfflinePlayerControl</code></summary>

```text
触发器: OfflinePlayerControl (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 grpTemp = 玩家选中的全部单位(触发玩家())
  └─ 如果
       ├─ 条件: (grpTemp中的单位数) == 1
       ├─ 则
       │    设置 uTemp = 单位组第一个单位(grpTemp)
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 玩家控制者比较(玩家控制者类型((uTemp的所有者)), OperatorEqualENE, MapControlUser)
       │      │    ├─ 玩家槽位状态比较(玩家槽位状态((uTemp的所有者)), OperatorEqualENE, PlayerSlotStateLeft)
       │      │    ├─ iPlayerControlList[玩家号((uTemp的所有者))] == 0
       │      │    ├─ 玩家属性值(触发玩家(), PlayerStateLumber) OperatorGreater 500
       │      ├─ 则
       │      │    SetPlayerAllianceStateBJ: (uTemp的所有者), 触发玩家(), AllianceSettingAlliedAdvUnits
       │      │    调整 触发玩家() 的 PlayerStateLumber: -500
       │      │    设置 iPlayerControlList[玩家号((uTemp的所有者))] = 玩家号(触发玩家())
       │      │    如果
       │      │      ├─ 条件: 玩家在玩家组中((uTemp的所有者), grpOffline) == TRUE
       │      │      ├─ 则
       │      │      │    ForceAddPlayer: grpOffline, (uTemp的所有者)
       │      │      └─ 否则: (无)
       │      │    删除单位组 grpTemp
       │      │    开启触发器 当前触发器()
       │      │    开启触发器 gg_trg_OfflinePlayerResource
       │      │    PolledWait: 0.10
       │      │    MultiboardDisplayBJ: ShowHideShow, TopBoard
       │      └─ 否则
       │           显示文本→触发玩家(): 0
       └─ 否则
            显示文本→触发玩家(): 0
            删除单位组 grpTemp
```

</details>

<details id="trigger-01_022_OfflinePlayerResource">
<summary><strong>📌 OfflinePlayerResource</strong> <code>01_022_OfflinePlayerResource</code></summary>

```text
触发器: OfflinePlayerResource (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(30.00)
条件
  └─ 无
动作
  └─ ForForceMultiple: grpOffline
```

</details>

<details id="trigger-01_023_MoneyTooMuch">
<summary><strong>📌 MoneyTooMuch</strong> <code>01_023_MoneyTooMuch</code></summary>

```text
触发器: MoneyTooMuch (玩家/英雄) [✓] — 钱满换木头
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置玩家属性: 触发玩家(), PlayerStateGold, 0
  ├─ 调整 触发玩家() 的 PlayerStateLumber: 90
  └─ 显示文本→触发玩家(): 0
```

</details>

<details id="trigger-01_024_LumberExchangeMoney">
<summary><strong>📌 LumberExchangeMoney</strong> <code>01_024_LumberExchangeMoney</code></summary>

```text
触发器: LumberExchangeMoney (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 玩家属性值(触发玩家(), PlayerStateLumber) OperatorGreaterEq 1
       ├─ 则
       │    调整 触发玩家() 的 PlayerStateGold: 10000
       │    调整 触发玩家() 的 PlayerStateLumber: -1
       └─ 否则: (无)
```

</details>

<details id="trigger-01_025_MoneyExchangeLumber">
<summary><strong>📌 MoneyExchangeLumber</strong> <code>01_025_MoneyExchangeLumber</code></summary>

```text
触发器: MoneyExchangeLumber (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 玩家属性值(触发玩家(), PlayerStateGold) OperatorGreaterEq 100000
       ├─ 则
       │    调整 触发玩家() 的 PlayerStateLumber: 10
       │    调整 触发玩家() 的 PlayerStateGold: -100000
       └─ 否则
            如果
              ├─ 条件: 玩家属性值(触发玩家(), PlayerStateGold) OperatorGreaterEq 10000
              ├─ 则
              │    调整 触发玩家() 的 PlayerStateLumber: 1
              │    调整 触发玩家() 的 PlayerStateGold: -10000
              └─ 否则: (无)
```

</details>

<details id="trigger-01_026_ChangeLeaderboardLumber">
<summary><strong>📌 ChangeLeaderboardLumber</strong> <code>01_026_ChangeLeaderboardLumber</code></summary>

```text
触发器: ChangeLeaderboardLumber (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 排行榜 TopBoard[4,(玩家号(触发玩家()) + 1)] = (玩家属性值(触发玩家(), PlayerStateLumber)转字符串)
```

</details>

<details id="trigger-01_027_ShowWeaponKill">
<summary><strong>📌 ShowWeaponKill</strong> <code>01_027_ShowWeaponKill</code></summary>

```text
触发器: ShowWeaponKill (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 uTemp = uPlayerHeros[玩家号(触发玩家())]
  ├─ 循环整数A 1→6
  │    ├─ 设置 itemTemp = 单位栏位物品(uTemp, 循环整数A)
  │    └─ 如果
  │         ├─ 条件: 任一成立
  │         ├─ 则
  │         │    显示文本→触发玩家(): 0
  │         └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-01_028_GetHelp">
<summary><strong>📌 GetHelp</strong> <code>01_028_GetHelp</code></summary>

```text
触发器: GetHelp (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ bGetHelp[玩家号(触发玩家())] == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 bGetHelp[玩家号(触发玩家())] = true
  ├─ 设置 iTemp = 15
  ├─ 循环整数A 15→25
  │    └─ 如果
  │         ├─ 条件: 随机[1~20] OperatorGreater 3
  │         ├─ 则
  │         │    设置 iTemp = (iTemp + 1)
  │         └─ 否则
  │              CustomScriptCode: "set bj_forLoopAIndex = 5000"
  ├─ 如果
  │    ├─ 条件: iTemp OperatorLess 26
  │    ├─ 则
  │    │    设置 uTemp = 创建单位(指定点)(触发玩家(), uJinGong[iTemp], pHG, 0)
  │    │    循环整数A 1→4
  │    │      └─ 如果
  │    │           ├─ 条件: 随机[1~2] == 1
  │    │           ├─ 则
  │    │           │    SetUnitAbilityLevelSwapped: aJinGongGuai[iTemp], uTemp, 循环整数A
  │    │           └─ 否则
  │    │                CustomScriptCode: "set bj_forLoopAIndex = 5000"
  │    │    如果
  │    │      ├─ 条件: 随机[1~2] == 1
  │    │      ├─ 则
  │    │      │    UnitAddAbilityBJ: aJinGongGuaiHard[iTemp], uTemp
  │    │      │    循环整数A 1→4
  │    │      │      └─ 如果
  │    │      │           ├─ 条件: 随机[1~2] == 1
  │    │      │           ├─ 则
  │    │      │           │    SetUnitAbilityLevelSwapped: aJinGongGuaiHard[iTemp], uTemp, 循环整数A
  │    │      │           └─ 否则
  │    │      │                CustomScriptCode: "set bj_forLoopAIndex = 5000"
  │    │      └─ 否则: (无)
  │    └─ 否则
  │         设置 uTemp = 创建单位(指定点)(触发玩家(), h008, pHG, 0)
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-01_029_ExchangeHero">
<summary><strong>📌 ExchangeHero</strong> <code>01_029_ExchangeHero</code></summary>

```text
触发器: ExchangeHero (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ uPlayerHeros[玩家号(触发玩家())] == UnitNull
动作
  ├─ 设置 iTemp = 字符串转整数(取子字符串(玩家聊天字符串(), 5, 7))
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iTemp OperatorGreater 0
       │    ├─ iTemp OperatorLess 6
       ├─ 则
       │    如果
       │      ├─ 条件: iExchangeHero[iTemp] == 玩家号(触发玩家())
       │      ├─ 则
       │      │    设置 uTemp = uPlayerHeros[玩家号(触发玩家())]
       │      │    设置 uPlayerHeros[玩家号(触发玩家())] = uPlayerHeros[iTemp]
       │      │    SetUnitOwner: uPlayerHeros[iTemp], 触发玩家(), 改变颜色
       │      │    设置 uPlayerHeros[iTemp] = uTemp
       │      │    SetUnitOwner: uTemp, 玩家iTemp, 改变颜色
       │      │    设置 触发玩家() 名字 = "銆?" + sPlayerInitName[玩家号(触发玩家())] + "銆?" + (单位名:uPlayerHeros[玩家号(触发玩家())])
       │      │    设置 玩家iTemp 名字 = "銆?" + sPlayerInitName[iTemp] + "銆?" + (单位名:uPlayerHeros[iTemp])
       │      │    设置 iExchangeHero[玩家号(触发玩家())] = 0
       │      │    设置 iExchangeHero[iTemp] = 0
       │      │    CustomScriptCode: "call DisplayTextToForce( udg_grpOnline, "玩家|cffff0000"+GetUnitName(udg_uPlaye..."
       │      └─ 否则
       │           设置 iExchangeHero[玩家号(触发玩家())] = iTemp
       │           CustomScriptCode: "call DisplayTextToForce( udg_grpOnline, "玩家|cffff0000"+GetUnitName(udg_uPlaye..."
       │           CustomScriptCode: "call DisplayTextToForce( udg_grpOnline,"请玩家|cffff0000"+GetUnitName(udg_uPlaye..."
       └─ 否则: (无)
```

</details>

<details id="trigger-01_030_关闭触发">
<summary><strong>📌 关闭触发</strong> <code>01_030_关闭触发</code></summary>

```text
触发器: 关闭触发 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-01_031_TurnOffOrder">
<summary><strong>📌 TurnOffOrder</strong> <code>01_031_TurnOffOrder</code></summary>

```text
触发器: TurnOffOrder (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(60.00)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 玩家科技等级(Rhme, 玩家9(灰)) == 0
  │    ├─ 则
  │    │    DialogDisplay: pFirstPlayer, dlgNanDu, ShowHideHide
  │    │    DialogDisplay: pFirstPlayer, dlgHigLevel, ShowHideHide
  │    │    DialogDisplay: pFirstPlayer, dlgChooseBoss, ShowHideHide
  │    │    显示文本→grpOnline: "TRIGSTR_4083"
  │    │    MultiboardSetTitleText: TopBoard, "TRIGSTR_4084"
  │    │    SetPlayerTechResearchedSwap: Rhme, 100, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: Rhme, 100, PlayerNA
  │    │    SetPlayerTechResearchedSwap: Rhar, 100, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: Rhar, 100, PlayerNA
  │    │    SetPlayerTechResearchedSwap: R004, 100, 玩家8(粉)
  │    │    SetPlayerTechResearchedSwap: R003, 100, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: R004, 100, PlayerNA
  │    │    设置技能等级: gg_unit_Uclc_0123, A09M, 10
  │    │    设置 bXianFeng = true
  │    │    显示文本→grpOnline: "TRIGSTR_965"
  │    │    设置 uXianFeng[1] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    设置 uXianFeng[2] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    设置 uXianFeng[3] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    设置 uXianFeng[4] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    循环整数A 1→4
  │    │      ├─ SetHeroLevel: uXianFeng[循环整数A()], 5, ShowHideHide
  │    │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A074
  │    │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A073
  │    │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A075
  │    │      └─ SelectHeroSkill: uXianFeng[循环整数A()], A076
  │    │    显示文本→grpOnline: "TRIGSTR_5260"
  │    │    设置 bTeShu = true
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
  │    └─ 否则: (无)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-01_032_埋骨地触发">
<summary><strong>📌 埋骨地触发</strong> <code>01_032_埋骨地触发</code></summary>

```text
触发器: 埋骨地触发 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-01_033_BaseBeDamaged">
<summary><strong>📌 BaseBeDamaged</strong> <code>01_033_BaseBeDamaged</code></summary>

```text
触发器: BaseBeDamaged (玩家/英雄) [✓] — 生命值提示
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_ubon_0001 - UnitEventDamaged
条件
  ├─ 伤害值() OperatorGreaterEq 10.00
  └─ 单位生命百分比(触发单位()) OperatorLessEq 50.00
动作
  └─ 循环整数A 1→5: 显示文本(玩家)(玩家循环整数A(), 0, 0, "|c00ff0000埋骨地生命值：|r" + 实数转字符串(单位生命百分比(触发单位())) + "%")
```

</details>

<details id="trigger-01_034_BaseRevive">
<summary><strong>📌 BaseRevive</strong> <code>01_034_BaseRevive</code></summary>

```text
触发器: BaseRevive (玩家/英雄) [✓] — 生命值提示
───────────────────────────────────────────────────────
事件
  └─ 单位生命值事件(gg_unit_ubon_0001, LimitOpLessThanOrEqual, 0.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 显示文本→grpOnline: "TRIGSTR_2514"
  ├─ PolledWait: 30.10
  ├─ 移除技能: 触发单位(), A07U
  └─ 播放动画: gg_unit_ubon_0001, "birth"
```

</details>

<details id="trigger-01_035_测试选项">
<summary><strong>📌 测试选项</strong> <code>01_035_测试选项</code></summary>

```text
触发器: 测试选项 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-01_036_Player1Cheat1">
<summary><strong>📌 Player1Cheat1</strong> <code>01_036_Player1Cheat1</code></summary>

```text
触发器: Player1Cheat1 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-test"
条件
  └─ 玩家组玩家数(grpOnline) == 1
动作
  ├─ 关闭触发器 当前触发器()
  ├─ CustomScriptCode: "call Cheat("greedisgood 500000")"
  ├─ PolledWait: 0.10
  ├─ 如果
  │    ├─ 条件: 玩家属性值(玩家9(灰), PlayerStateLumber) OperatorGreater 100000
  │    ├─ 则
  │    │    销毁触发器(自身)
  │    │    显示文本→Player00: 0
  │    │    CreateFogModifierRectBJ: EnabledDisabledEnabled, Player00, FogStateVisible, 可用地图区域()
  │    │    添加技能: gg_unit_ubon_0001, ACes
  │    │    添加技能: gg_unit_ubon_0001, Apxf
  │    │    添加技能: gg_unit_ubon_0001, A031
  │    │    开启触发器 gg_trg_Player1Cheat2
  │    │    开启触发器 gg_trg_JustForTestNoCD
  │    │    开启触发器 gg_trg_SetLV
  │    │    开启触发器 gg_trg_SetTIME
  │    │    运行计时器 tFengChenMoShi (循环, 1.00s)
  │    │    SetTerrainTypeBJ: pHG, TerrainTypeWsnw, -1, 100, TerrainShapeSquare
  │    │    循环整数A 1→35
  │    │      └─ 创建 1个|uJinGong[循环整数A]|→Player00 在 pHG 面向默认朝向
  │    │    关闭触发器 gg_trg_KillAllDistrutable
  │    │    EnumDestructablesInRectAllMultiple: 可用地图区域()
  │    │    开启触发器 gg_trg_KillAllDistrutable
  │    │    添加事件到 gg_trg_KillAllDistrutable: 注册可破坏物死亡事件(gg_rct_________________000)
  │    │    循环整数A 0→255
  │    │      └─ 创建物品(指定坐标): 自定义代码("'I020'+bj_forLoopAIndex"), (点X坐标(pHG) + 自定义代码("ModuloInteger(bj_forLoopAIndex,40)*50-1000")), (点Y坐标(pHG) + 自定义代码("R2I(bj_forLoopAIndex/100)*50"))
  │    │    循环整数A 0→255
  │    │      └─ 创建物品(指定坐标): 自定义代码("'I030'+bj_forLoopAIndex"), (点X坐标(pHG) + 自定义代码("ModuloInteger(bj_forLoopAIndex,40)*50-1000")), (点Y坐标(pHG) + 自定义代码("R2I(bj_forLoopAIndex/100)*50"))
  │    │    循环整数A 0→255
  │    │      └─ 创建物品(指定坐标): 自定义代码("'I040'+bj_forLoopAIndex"), (点X坐标(pHG) + 自定义代码("ModuloInteger(bj_forLoopAIndex,40)*50-1000")), (点Y坐标(pHG) + 自定义代码("R2I(bj_forLoopAIndex/100)*50"))
  │    │    循环整数A 0→255
  │    │      └─ 创建物品(指定坐标): 自定义代码("'I050'+bj_forLoopAIndex"), (点X坐标(pHG) + 自定义代码("ModuloInteger(bj_forLoopAIndex,40)*50-1000")), (点Y坐标(pHG) + 自定义代码("R2I(bj_forLoopAIndex/100)*50"))
  │    │    返回
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-01_037_Player1Cheat2">
<summary><strong>📌 Player1Cheat2</strong> <code>01_037_Player1Cheat2</code></summary>

```text
触发器: Player1Cheat2 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-test1"
条件
  └─ 玩家组玩家数(grpOnline) == 1
动作
  ├─ 销毁触发器(自身)
  ├─ SetPlayerTechResearchedSwap: R006, 1, Player00
  ├─ SetPlayerTechResearchedSwap: R009, 1, Player00
  ├─ SetPlayerTechResearchedSwap: R008, 1, Player00
  ├─ SetPlayerTechResearchedSwap: Rhcd, 1, Player00
  └─ ForLoopBMultiple: 1, 14
```

</details>

<details id="trigger-01_038_SetLV">
<summary><strong>📌 SetLV</strong> <code>01_038_SetLV</code></summary>

```text
触发器: SetLV (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-lv "
条件
  └─ 无
动作
  ├─ 设置 iTemp = 字符串转整数(取子字符串(玩家聊天字符串(), 5, 6))
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iTemp OperatorGreater 0
       │    ├─ iTemp OperatorLess 36
       ├─ 则
       │    显示文本→grpOnline: "当前波数修改为：" + (iTemp转字符串)
       │    设置 LVCurrent = iTemp
       └─ 否则
            显示文本→Player00: 0
```

</details>

<details id="trigger-01_039_SetTIME">
<summary><strong>📌 SetTIME</strong> <code>01_039_SetTIME</code></summary>

```text
触发器: SetTIME (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-time "
条件
  └─ 无
动作
  ├─ 设置 iTemp = 字符串转整数(取子字符串(玩家聊天字符串(), 7, 8))
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iTemp OperatorGreaterEq 0
       │    ├─ iTemp OperatorLess 24
       ├─ 则
       │    SetTimeOfDay: (iTemp转实数)
       └─ 否则
            显示文本→Player00: 0
```

</details>

<details id="trigger-01_040_JustForTestNoCD">
<summary><strong>📌 JustForTestNoCD</strong> <code>01_040_JustForTestNoCD</code></summary>

```text
触发器: JustForTestNoCD (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 任意单位 - PlayerUnitEventSpellCast
  ├─ 任意单位 - PlayerUnitEventSpellEndCast
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ UnitResetCooldown: 触发单位()
  └─ 设置魔法百分比: 触发单位(), 100
```

</details>

