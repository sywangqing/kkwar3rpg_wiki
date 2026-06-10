---
title: 神墓 2.7C — 💀 06 单位与技能
category: kk-triggers
slug: shenmu/06-battle
description: 单位死亡/技能施放/被动/英雄升级/计时器技能
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 💀 06 单位与技能

> 单位死亡/技能施放/被动/英雄升级/计时器技能

**共 33 个触发器**

## 📑 触发器目录

- [UnitDie](#trigger-06_000_UnitDie)
- [UnitDieCinema](#trigger-06_001_UnitDieCinema)
- [UsableAbility](#trigger-06_002_UsableAbility)
- [PassiveAbility](#trigger-06_003_PassiveAbility)
- [AnyUnitDamaged](#trigger-06_004_AnyUnitDamaged)
- [UnitSummon](#trigger-06_005_UnitSummon)
- [UnitEnterMap](#trigger-06_006_UnitEnterMap)
- [HeroLevelUp](#trigger-06_007_HeroLevelUp)
- [HeroLearnSkill](#trigger-06_008_HeroLearnSkill)
- [AbilityStartCast](#trigger-06_009_AbilityStartCast)
- [其他类别](#trigger-06_010_其他类别)
- [YLWuJinChangYe](#trigger-06_011_YLWuJinChangYe)
- [CYHuoJingLingInit](#trigger-06_012_CYHuoJingLingInit)
- [CYHuoJingLing](#trigger-06_013_CYHuoJingLing)
- [JinShengWuWei](#trigger-06_014_JinShengWuWei)
- [SetHeroInvincible](#trigger-06_015_SetHeroInvincible)
- [UnBlinkable](#trigger-06_016_UnBlinkable)
- [UnBlinkableFushen](#trigger-06_017_UnBlinkableFushen)
- [RepickAbility](#trigger-06_018_RepickAbility)
- [技能计时器](#trigger-06_019_技能计时器)
- [tInvincible](#trigger-06_020_tInvincible)
- [tTianShuXiaJuan](#trigger-06_021_tTianShuXiaJuan)
- [tBingZhiDiaoLing](#trigger-06_022_tBingZhiDiaoLing)
- [tJiCiTianYa](#trigger-06_023_tJiCiTianYa)
- [tNJKL](#trigger-06_024_tNJKL)
- [tBaoFengxue](#trigger-06_025_tBaoFengxue)
- [tShunZhuanQianNian](#trigger-06_026_tShunZhuanQianNian)
- [tKongJianGeLie](#trigger-06_027_tKongJianGeLie)
- [tSiWangQiXi](#trigger-06_028_tSiWangQiXi)
- [tFengChenMoShi](#trigger-06_029_tFengChenMoShi)
- [tChuanXinCi](#trigger-06_030_tChuanXinCi)
- [tDaoXuanZXSH](#trigger-06_031_tDaoXuanZXSH)
- [tHB50](#trigger-06_032_tHB50)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-06_000_UnitDie">
<summary><strong>📌 UnitDie</strong> <code>06_000_UnitDie</code></summary>

```text
触发器: UnitDie (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 地形可通行(单位X坐标(触发单位()), 单位Y坐标(触发单位()), PathingTypeFloatability) == TRUE
  │    │    ├─ 单位技能等级(Aloc, 触发单位()) == 0
  │    ├─ 则
  │    │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Undead\Possession\PossessionMissile.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │    修改 gg_unit_Hmkg_0067 的HeroStatStr: ModifyMethodAdd500
  │    │    修改 gg_unit_Hmkg_0067 的HeroStatAgi: ModifyMethodAdd500
  │    │    修改 gg_unit_Hmkg_0067 的HeroStatInt: ModifyMethodAdd500
  │    │    如果
  │    │      ├─ 条件: iShuiYuSiWang OperatorLess 255
  │    │      ├─ 则
  │    │      │    设置 iShuiYuSiWang = (iShuiYuSiWang + 1)
  │    │      │    设置水面颜色: 255, (255 - iShuiYuSiWang), (255 - iShuiYuSiWang), 255
  │    │      │    如果
  │    │      │      ├─ 条件: iShuiYuSiWang == 255
  │    │      │      ├─ 则
  │    │      │      │    显示单位: gg_unit_nmrr_0068
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 单位掉落血晶石 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ (触发单位()的所有者) == 玩家9(灰)
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~150], ==, 1)
  │    │      ├─ 则: 创建物品(I057, pTemp)
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~150], ==, 2)
  │    │      ├─ 则: 创建物品(I056, pTemp)
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~150], ==, 3)
  │    │      ├─ 则: 创建物品(I058, pTemp)
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~150], ==, 4)
  │    │      ├─ 则: 创建物品(I059, pTemp)
  │    │      └─ 否则: 无动作()
  │    │    设置 iTemp = 玩家号((凶手单位()的所有者))
  │    │    如果
  │    │      ├─ 条件: bQuestPangNiu[iTemp] == TRUE
  │    │      ├─ 则
  │    │      │    设置 iKillPangNiu[iTemp] = (iKillPangNiu[iTemp] + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 取模(iKillPangNiu[iTemp], 100) == 0
  │    │      │      ├─ 则
  │    │      │      │    SetHeroLevel: uPlayerHeros[iTemp], (英雄等级(uPlayerHeros[iTemp]) + 随机[5~10]), ShowHideHide
  │    │      │      │    显示文本→(凶手单位()的所有者): 0
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    清除点 pTemp
  │    └─ 否则: (无)
  ├─ ── 召唤物科技  龙刀 十字架 贯穿 ──
  ├─ 如果
  │    ├─ 条件: 玩家在玩家组中((凶手单位()的所有者), grpUserPlayers) == TRUE
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((凶手单位()的所有者))
  │    │    设置 iKillAll[iTemp] = (iKillAll[iTemp] + 1)
  │    │    排行榜 TopBoard[2,(iTemp + 1)] = (iKillAll[iTemp]转字符串)
  │    │    ── 英雄杀敌数 ──
  │    │    如果
  │    │      ├─ 条件: 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    设置 iKillByHero[iTemp] = (iKillByHero[iTemp] + 1)
  │    │      │    排行榜 TopBoard[3,(iTemp + 1)] = (iKillByHero[iTemp]转字符串)
  │    │      │    如果
  │    │      │      ├─ 条件: 全部成立
  │    │      │      │    ├─ 玩家科技等级(R006, (凶手单位()的所有者)) == 0
  │    │      │      │    ├─ 单位持有物品类型(凶手单位(), I02Q) == TRUE
  │    │      │      │    ├─ 随机[1~1000] == 12
  │    │      │      ├─ 则
  │    │      │      │    设置 uTemp = uPlayerHeros[玩家号((凶手单位()的所有者))]
  │    │      │      │    SetPlayerTechResearchedSwap: R006, 1, (凶手单位()的所有者)
  │    │      │      │    删除物品: 单位携带物品(按类型)(凶手单位(), I02Q)
  │    │      │      │    修改 uTemp 的HeroStatStr: ModifyMethodAdd8000
  │    │      │      │    修改 uTemp 的HeroStatAgi: ModifyMethodAdd8000
  │    │      │      │    修改 uTemp 的HeroStatInt: ModifyMethodAdd8000
  │    │      │      │    SetHeroLevel: uTemp, (英雄等级(uTemp) + 50), ShowHideShow
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 全部成立
  │    │      │      │      │    ├─ uTemp == uWuJinChangYe
  │    │      │      │      │    ├─ 单位技能等级(A08C, uTemp) == 1
  │    │      │      │      ├─ 则
  │    │      │      │      │    添加事件到 gg_trg_YLWuJinChangYe: 注册单位进入范围事件(512.00, uTemp)
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 单位技能等级(A03R, uTemp) == 1
  │    │      │      │      ├─ 则
  │    │      │      │      │    设置 uChiYanHuoJingLing[0] = uTemp
  │    │      │      │      │    TriggerExecute: gg_trg_CYHuoJingLingInit
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    显示文本→grpUserPlayers: "|cffff0000" + (玩家名:(凶手单位()的所有者)) + "在战斗中顿悟了半神的力量！|r"
  │    │      │      └─ 否则: (无)
  │    │      │    如果
  │    │      │      ├─ 条件: (布尔比较(单位持有物品类型(凶手单位(), I00M), OperatorEqualENE, true) 或 布尔比较(单位有魔法效果(凶手单位(), BIrl), OperatorEqualENE, true))
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 英雄等级(凶手单位()) OperatorGreater 156
  │    │      │      │      ├─ 则
  │    │      │      │      │    AddHeroXP: 凶手单位(), 随机[100~666], ShowHideShow
  │    │      │      │      └─ 否则
  │    │      │      │           AddHeroXP: 凶手单位(), 随机[10~100], ShowHideShow
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    ── 地狱火 ──
  │    │    如果
  │    │      ├─ 条件: (凶手单位()类型ID) == n00B
  │    │      ├─ 则
  │    │      │    设置 iKillByDYH[iTemp] = (iKillByDYH[iTemp] + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 整数比较(取模(iKillByDYH[iTemp], 150), ==, 0)
  │    │      │      ├─ 则: 升级玩家科技((凶手单位()的所有者), R007, 1)
  │    │      │      └─ 否则: 无动作()
  │    │      └─ 否则: (无)
  │    │    ── 旺财 ──
  │    │    如果
  │    │      ├─ 条件: 任一成立
  │    │      ├─ 则
  │    │      │    设置 iKillByWangCai[iTemp] = (iKillByWangCai[iTemp] + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 整数比较(iKillByWangCai[iTemp], ==, 5000)
  │    │      │      ├─ 则: 升级玩家科技((凶手单位()的所有者), R005, 1)
  │    │      │      └─ 否则: 无动作()
  │    │      └─ 否则: (无)
  │    │    ── 龙刀 ──
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(凶手单位(), I04N) == TRUE
  │    │      ├─ 则
  │    │      │    设置 itemTemp = 单位携带物品(按类型)(凶手单位(), I04N)
  │    │      │    SetItemUserData: itemTemp, (物品自定义值(itemTemp) + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 全部成立
  │    │      │      │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │      │      │    ├─ (触发单位()类型ID) == H00D
  │    │      │      ├─ 则
  │    │      │      │    SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) + 1)
  │    │      │      └─ 否则: (无)
  │    │      │    如果
  │    │      │      ├─ 条件: 取模(物品自定义值(itemTemp), 250) == 0
  │    │      │      ├─ 则
  │    │      │      │    SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) + 1)
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    ── 杀戮 ──
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(凶手单位(), I05D) == TRUE
  │    │      ├─ 则
  │    │      │    设置 itemTemp = 单位携带物品(按类型)(凶手单位(), I05D)
  │    │      │    SetItemUserData: itemTemp, (物品自定义值(itemTemp) + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 取模(物品自定义值(itemTemp), 100) == 0
  │    │      │      ├─ 则
  │    │      │      │    CustomScriptCode: "call SetShaLuAttack( GetKillingUnitBJ(),udg_itemTemp)"
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    ── 贯穿天地 诅咒全开 ──
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位持有物品类型(凶手单位(), I05P) == TRUE
  │    │      │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    设置 itemTemp = 单位携带物品(按类型)(凶手单位(), I05P)
  │    │      │    SetItemUserData: itemTemp, (物品自定义值(itemTemp) + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 取模(物品自定义值(itemTemp), 10) == 0
  │    │      │      ├─ 则
  │    │      │      │    CustomScriptCode: "call SetGCTD_ZZQK( GetKillingUnitBJ(),udg_itemTemp)"
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    ── 十字架 ──
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位持有物品类型(凶手单位(), I038) == TRUE
  │    │      │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    设置 itemTemp = 单位携带物品(按类型)(凶手单位(), I038)
  │    │      │    SetItemUserData: itemTemp, (物品自定义值(itemTemp) + 1)
  │    │      │    如果
  │    │      │      ├─ 条件: 取模(物品自定义值(itemTemp), 500) == 0
  │    │      │      ├─ 则
  │    │      │      │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd随机[150~300]
  │    │      │      │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd随机[150~300]
  │    │      │      │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd随机[150~300]
  │    │      │      │    SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) + 1)
  │    │      │      │    显示文本→(凶手单位()的所有者): 0
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 吸魂 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │    ├─ 单位持有物品类型(凶手单位(), I04T) == TRUE
  │    │    ├─ 随机[1~10] == 1
  │    ├─ 则
  │    │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │    │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd30
  │    │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd20
  │    │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd10
  │    └─ 否则
  │         如果
  │           ├─ 条件: 全部成立
  │           │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │           │    ├─ 单位持有物品类型(凶手单位(), I02G) == TRUE
  │           │    ├─ 随机[1~10] == 1
  │           ├─ 则
  │           │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │           │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd30
  │           └─ 否则
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I026) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │                  │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd25
  │                  └─ 否则: (无)
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I027) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │                  │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd20
  │                  └─ 否则: (无)
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I028) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │                  │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd15
  │                  └─ 否则: (无)
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I02A) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │                  │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd10
  │                  └─ 否则: (无)
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I029) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'nhew'..."
  │                  │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd5
  │                  └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │    ├─ 单位持有物品类型(凶手单位(), I04V) == TRUE
  │    │    ├─ 随机[1~5] == 20
  │    ├─ 则
  │    │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │    │    SetHeroInt: 凶手单位(), (英雄智力(凶手单位(), InclusionExclude) + 随机[-100~136]), EnableDisableEnable
  │    └─ 否则
  │         如果
  │           ├─ 条件: 全部成立
  │           │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │           │    ├─ 单位持有物品类型(凶手单位(), I03M) == TRUE
  │           │    ├─ 随机[1~10] == 1
  │           ├─ 则
  │           │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │           │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd30
  │           │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd30
  │           │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd30
  │           └─ 否则
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I033) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                  │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd30
  │                  └─ 否则
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01M) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd25
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01L) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd20
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01K) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd15
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01J) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd10
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01I) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd5
  │                         └─ 否则: (无)
  │                如果
  │                  ├─ 条件: 全部成立
  │                  │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                  │    ├─ 单位持有物品类型(凶手单位(), I032) == TRUE
  │                  │    ├─ 随机[1~10] == 1
  │                  ├─ 则
  │                  │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                  │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd30
  │                  └─ 否则
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I019) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd25
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01C) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd20
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01B) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd15
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01A) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd10
  │                         └─ 否则: (无)
  │                       如果
  │                         ├─ 条件: 全部成立
  │                         │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │                         │    ├─ 单位持有物品类型(凶手单位(), I01D) == TRUE
  │                         │    ├─ 随机[1~10] == 1
  │                         ├─ 则
  │                         │    CustomScriptCode: "call IssueTargetOrderById(CreateUnit(GetOwningPlayer(GetTriggerUnit()),'hrdh'..."
  │                         │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd5
  │                         └─ 否则: (无)
  ├─ ── 龙皇号角 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位持有物品类型(触发单位(), I02K) == TRUE
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │    ├─ 随机[1~4] == 3
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    设置 grpTemp = 范围内符合条件的单位(512, pTemp, (布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false) 且 (布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true) 且 布尔比较(单位类型判断(过滤单位(), UnitTypeGiant), OperatorEqualENE, false))))
  │    │    清除点 pTemp
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ 设置 pTemp = (选取单位()的位置)
  │    │      ├─ 销毁特效 创建特效(Units\Demon\Infernal\InfernalBirth.mdl, pTemp)
  │    │      ├─ 清除点 pTemp
  │    │      └─ 伤害目标: 触发单位(), 选取单位(), (单位状态(选取单位(), UnitStateLife) x 2.00), IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeUnknown, WEAPON_TYPE_WHOKNOWS
  │    │    删除单位组 grpTemp
  │    │    显示文本→(触发单位()的所有者): 0
  │    └─ 否则: (无)
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── 囚笼解封 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == hbew
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    设置 grpTemp = 范围内符合条件的单位(600.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ SetUnitTimeScale: 选取单位(), 1
  │    │      └─ PauseUnitBJ: PauseUnpauseOptionUnpause, 选取单位()
  │    │    清除点 pTemp
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
  ├─ ── ===================================== ──
  ├─ ── 道玄 碧海潮生 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(凶手单位(), A08W) == 1
  │    │    ├─ 随机[1~7] == 3
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    销毁特效 创建特效(Objects\Spawnmodels\NightElf\NEDeathSmall\NEDeathSmall.mdl, pTemp)
  │    │    设置 grpTemp = 范围内符合条件的单位(512.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (凶手单位()的所有者)), OperatorEqualENE, true))
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ CustomScriptCode: "local unit tu = GetKillingUnit()"
  │    │      ├─ CustomScriptCode: "local player tp = GetOwningPlayer(tu)"
  │    │      ├─ CustomScriptCode: "local integer tpIndex=GetConvertedPlayerId(tp)"
  │    │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uPlayerHeros[tpIndex])"
  │    │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uPlayerHeros[tpIndex], true)"
  │    │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uPlayerHeros[tpIndex], true)"
  │    │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uPlayerHeros[tpIndex], tr..."
  │    │      └─ CustomScriptCode: "call UnitDamageTargetBJ(tu,GetEnumUnit(),(lv*0.14)*(ll*3+mj*1.2+zl*2.3),ATTAC..."
  │    │    清除点 pTemp
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
  ├─ ── 妖灵影爆 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ (触发单位()类型ID) == N00L
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │    ├─ 单位技能等级(uPlayerHeros[玩家号((触发单位()的所有者))], A089) == 1
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    销毁特效 创建特效(Abilities\Spells\Orc\MirrorImage\MirrorImageCaster.mdl, pTemp)
  │    │    设置 grpTemp = 范围内符合条件的单位(1000.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ CustomScriptCode: "local unit tu = GetTriggerUnit()"
  │    │      ├─ CustomScriptCode: "local player tp = GetOwningPlayer(tu)"
  │    │      ├─ CustomScriptCode: "local integer tpIndex=GetConvertedPlayerId(tp)"
  │    │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uPlayerHeros[tpIndex])"
  │    │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uPlayerHeros[tpIndex], true)"
  │    │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uPlayerHeros[tpIndex], true)"
  │    │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uPlayerHeros[tpIndex], tr..."
  │    │      └─ CustomScriptCode: "call UnitDamageTargetBJ(tu,GetEnumUnit(),(.2*lv+5)*(ll+mj+zl*3),ATTACK_TYPE_C..."
  │    │    清除点 pTemp
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── 小九头怪 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nhyh
  │    ├─ 则
  │    │    设置 iCountJTS = (iCountJTS + 1)
  │    │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │    移除 触发单位()
  │    │    设置 pTemp = (gg_unit_N017_0037的位置)
  │    │    创建 1个|nhyh|→非玩家 在 pTemp 面向默认朝向
  │    │    销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(最后创建的单位()), 单位Y坐标(最后创建的单位()))
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 石头1 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == n002
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01R, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01N, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    设置 pTemp = 区域内随机点(gg_rct_______001)
  │    │    创建 1个|n002|→PlayerNA 在 pTemp 面向270.00
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 石头2 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == n003
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01S, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01O, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    设置 pTemp = 区域内随机点(gg_rct_______002)
  │    │    创建 1个|n003|→PlayerNA 在 pTemp 面向270.00
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 石头3 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == n004
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01U, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01P, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    设置 pTemp = 区域内随机点(gg_rct_______003)
  │    │    创建 1个|n004|→PlayerNA 在 pTemp 面向默认朝向
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 食人魔 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nogl
  │    ├─ 则
  │    │    设置 iKillShiRenMo = (iKillShiRenMo + 1)
  │    │    如果
  │    │      ├─ 条件: iKillShiRenMo == 1314
  │    │      ├─ 则
  │    │      │    设置 pTemp = 区域内随机点(gg_rct__________01)
  │    │      │    创建物品: I05N, pTemp
  │    │      │    清除点 pTemp
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: (布尔比较(单位类型判断(凶手单位(), 英雄), OperatorEqualENE, true) 且 整数比较(随机[1~3], ==, 1))
  │    │      ├─ 则: 创建物品(指定坐标)(I037, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 2.00
  │    │    设置 pTemp = 区域内随机点(gg_rct__________01)
  │    │    创建 1个|nogl|→PlayerNA 在 pTemp 面向270.00
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 致命毒素 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nomg
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~3], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I050, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 30.00
  │    │     CreateUnit: PlayerNA, nomg, 区域中心X(gg_rct_______u), 区域中心Y(gg_rct_______u), 90.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 灵兽 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == n00O
  │    ├─ 则
  │    │    创建物品(指定坐标): I04Z, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 30.00
  │    │     CreateUnit: PlayerNA, n00O, 区域中心X(gg_rct_______c), 区域中心Y(gg_rct_______c), 270.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 石精 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == n014
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 随机[1~3] == 1
  │    │      ├─ 则
  │    │      │    创建物品(指定坐标): sbch, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: 随机[1~3] == 1
  │    │      ├─ 则
  │    │      │    创建物品(指定坐标): dsum, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      └─ 否则: (无)
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, n014, 区域中心X(gg_rct_______12), 区域中心Y(gg_rct_______12), 270.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 狂暴野兽 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == npfl
  │    ├─ 则
  │    │    设置 iKillKuangBaoYeShou = (iKillKuangBaoYeShou + 1)
  │    │    如果
  │    │      ├─ 条件: iKillKuangBaoYeShou == 1314
  │    │      ├─ 则
  │    │      │    设置 pTemp = 区域内随机点(gg_rct_____________01)
  │    │      │    创建物品: I05O, pTemp
  │    │      │    清除点 pTemp
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~100], ==, 23)
  │    │      ├─ 则: 创建物品(指定坐标)(I039, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~20], ==, 4)
  │    │      ├─ 则: 创建物品(指定坐标)(I001, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 2.00
  │    │    设置 pTemp = 区域内随机点(gg_rct_____________01)
  │    │    创建 1个|npfl|→PlayerNA 在 pTemp 面向270.00
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 红龙 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nrwm
  │    ├─ 则
  │    │    创建物品(指定坐标): I02L, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, nrwm, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 蓝龙 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nadr
  │    ├─ 则
  │    │    创建物品(指定坐标): I02J, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, nadr, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 绿龙 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == ngrd
  │    ├─ 则
  │    │    创建物品(指定坐标): I02I, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, ngrd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 青龙 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nbzd
  │    ├─ 则
  │    │    创建物品(指定坐标): I02M, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, nbzd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 黑龙 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nbwm
  │    ├─ 则
  │    │    创建物品(指定坐标): I02K, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │     CreateUnit: PlayerNA, nbwm, 区域中心X(gg_rct_____________2), 区域中心Y(gg_rct_____________2), 180.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── ===================================== ──
  ├─ ── 浮生老头 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H00J_0028
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    修改 凶手单位() 的HeroStatStr: ModifyMethodAddGetHeroStr(触发单位(), InclusionExclude)
  │    │      │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd英雄敏捷(触发单位(), InclusionExclude)
  │    │      │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd英雄智力(触发单位(), InclusionExclude)
  │    │      └─ 否则: (无)
  │    │    删除物品: 单位携带物品(按类型)(gg_unit_H00J_0028, I05D)
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 魔将死亡 ──
  ├─ 如果
  │    ├─ 条件: (单位类型比较((触发单位()类型ID), OperatorEqualENE, H00D) 或 单位类型比较((触发单位()类型ID), OperatorEqualENE, U005))
  │    ├─ 则
  │    │    PolledWait: 1.00
  │    │    移除 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 先锋死亡 ──
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == U006
       ├─ 则
       │    调整 (凶手单位()的所有者) 的 PlayerStateLumber: (LVCurrent + 2)
       └─ 否则: (无)
```

</details>

<details id="trigger-06_001_UnitDieCinema">
<summary><strong>📌 UnitDieCinema</strong> <code>06_001_UnitDieCinema</code></summary>

```text
触发器: UnitDieCinema (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  ├─ ── 封尘魔石 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ bFengChenMoShi == TRUE
  │    │    ├─ 随机[1~(玩家科技等级(Rhme, 玩家9(灰)) x 2500)] == 123
  │    │    ├─ 单位技能等级(Aloc, 触发单位()) == 0
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    创建物品: I04O, pTemp
  │    │    显示文本→grpOnline: "TRIGSTR_5546"
  │    │    运行计时器 tFengChenMoShi (循环, 1.00s)
  │    │    清除点 pTemp
  │    │    设置 bFengChenMoShi = true
  │    └─ 否则: (无)
  ├─ ── 埋骨地 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_ubon_0001
  │    ├─ 则
  │    │    关闭触发器 gg_trg_JinGongSheZhi
  │    │    关闭触发器 gg_trg_JinGongGuai
  │    │    关闭触发器 gg_trg_JinGongDengDai
  │    │    关闭触发器 gg_trg_JinGongTooMany
  │    │    暂停计时器 tWait
  │    │    暂停计时器 tTooMany
  │    │    暂停计时器 tNextWave
  │    │    如果
  │    │      ├─ 条件: uFuShenMoDi == UnitNull
  │    │      ├─ 则
  │    │      │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │      │    电影模式: OnOffOn, grpOnline
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Uclc_0123, "TRIGSTR_5692", SoundNull, "TRIGSTR_5693", AddSetToAdd, 0, WaitDontWait
  │    │      │    电影模式: OnOffOff, grpOnline
  │    │      │    ForForceMultiple: grpOnline
  │    │      │    返回
  │    │      └─ 否则
  │    │           CustomScriptCode: "call SetPlayerState(GetOwningPlayer(udg_uFuShenMoDi),PLAYER_STATE_OBSERVER,0)"
  │    │           PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │           电影模式: OnOffOn, grpOnline
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Uclc_0123, "TRIGSTR_5628", SoundNull, "TRIGSTR_5687", AddSetToAdd, 0, WaitDontWait
  │    │           电影模式: OnOffOff, grpOnline
  │    │           ForForceMultiple: grpOnline
  │    │           宣布失败: (uFuShenMoDi的所有者), "TRIGSTR_5691"
  │    │           返回
  │    └─ 否则: (无)
  ├─ ── 残 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == Nkjx
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 玩家科技等级(Rhar, 玩家9(灰)) OperatorGreater 4
  │    │      ├─ 则
  │    │      │    设置无敌: gg_unit_Uclc_0123, InvulnerabilityVulnerable
  │    │      │    PlaySoundBJ: gg_snd_LichKingTheme
  │    │      │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │      │    电影模式: OnOffOn, grpOnline
  │    │      │    TransmissionFromUnitTypeWithNameBJ: grpOnline, 玩家9(灰), Uclc, "TRIGSTR_5700", pShuaGuai[44], SoundNull, "TRIGSTR_5701", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitTypeWithNameBJ: grpOnline, 玩家9(灰), Uclc, "TRIGSTR_5702", pShuaGuai[44], SoundNull, "TRIGSTR_5703", AddSetToAdd, 0, WaitDontWait
  │    │      │    电影模式: OnOffOff, grpOnline
  │    │      │    命令 创建单位(指定坐标)(玩家9(灰), H009, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │      │    设置无敌: gg_unit_Uclc_0123, InvulnerabilityVulnerable
  │    │      │    返回
  │    │      └─ 否则
  │    │           PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │           电影模式: OnOffOn, grpOnline
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5697", AddSetToAdd, 0, WaitDontWait
  │    │           电影模式: OnOffOff, grpOnline
  │    │           显示文本→grpOnline: "TRIGSTR_5698"
  │    │           PolledWait: 60.00
  │    │           ForForceMultiple: grpOnline
  │    │           返回
  │    └─ 否则: (无)
  ├─ ── 冰封魔帝 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_Uclc_0123
  │    ├─ 则
  │    │    CustomScriptCode: "call FogMaskEnable(false)
  │    │    "
  │    │    CustomScriptCode: "call FogEnable(false)"
  │    │    开启触发器 gg_trg_MoDiJinGong
  │    │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │    电影模式: OnOffOn, grpOnline
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Uclc_0123, "TRIGSTR_5704", SoundNull, "TRIGSTR_5705", AddSetToAdd, 0, WaitDontWait
  │    │    电影模式: OnOffOff, grpOnline
  │    │    显示文本→grpOnline: "TRIGSTR_5706"
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    设置 uTemp = 创建单位(指定点)(玩家9(灰), U002, pTemp, 0)
  │    │    添加事件到 gg_trg_UnBlinkable: 注册单位进入范围事件(600.00, uTemp)
  │    │    开启触发器 gg_trg_UnBlinkable
  │    │    SetHeroLevel: uTemp, 1000, ShowHideHide
  │    │    命令 uTemp → UnitOrderAttack 到 pHG
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 解封魔帝 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ (触发单位()类型ID) == U002
  │    │    ├─ 触发单位() == uFuShenMoDi
  │    ├─ 则
  │    │    关闭触发器 gg_trg_UnBlinkable
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位持有物品(凶手单位(), itemTSXJ) == TRUE
  │    │      │    ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreaterEq 5
  │    │      ├─ 则
  │    │      │    删除物品: itemTSXJ
  │    │      │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │      │    电影模式: OnOffOn, grpOnline
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5709", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5710", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5711", AddSetToAdd, 0, WaitDontWait
  │    │      │    电影模式: OnOffOff, grpOnline
  │    │      │    设置 itemTSXJ = 创建物品(指定坐标)(moon, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      │    开启触发器 gg_trg_MyGod
  │    │      │    PolledWait: 30.00
  │    │      │    如果
  │    │      │      ├─ 条件: uFuShenMoDi == UnitNull
  │    │      │      ├─ 则
  │    │      │      │    ForForceMultiple: grpOnline
  │    │      │      └─ 否则: (无)
  │    │      │    返回
  │    │      └─ 否则
  │    │           EnableWeatherEffect: 添加天气效果(可用地图区域(), WeatherNorthrendHeavySnow), OnOffOn
  │    │           PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │           电影模式: OnOffOn, grpOnline
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5712", AddSetToAdd, 0, WaitDontWait
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5713", AddSetToAdd, 0, WaitDontWait
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5715", AddSetToAdd, 0, WaitDontWait
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5716", AddSetToAdd, 0, WaitDontWait
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5717", AddSetToAdd, 0, WaitDontWait
  │    │           TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5718", AddSetToAdd, 0, WaitDontWait
  │    │           电影模式: OnOffOff, grpOnline
  │    │           显示文本→grpOnline: "TRIGSTR_5719"
  │    │           PolledWait: 60.00
  │    │           ForForceMultiple: grpOnline
  │    │           返回
  │    └─ 否则: (无)
  ├─ ── 附身魔帝 ──
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ (触发单位()类型ID) == U002
       │    ├─ 触发单位() == uFuShenMoDi
       ├─ 则
       │    CustomScriptCode: "call SetPlayerState(GetOwningPlayer(udg_uFuShenMoDi),PLAYER_STATE_OBSERVER,0)"
       │    关闭触发器 gg_trg_UnBlinkableFushen
       │    关闭触发器 gg_trg_LastBattle
       │    关闭触发器 gg_trg_FuShenMoDiStrength
       │    EnableWeatherEffect: 添加天气效果(可用地图区域(), WeatherNorthrendHeavySnow), OnOffOn
       │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
       │    电影模式: OnOffOn, grpOnline
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), "TRIGSTR_5720", SoundNull, "TRIGSTR_5721", AddSetToAdd, 0, WaitDontWait
       │    电影模式: OnOffOff, grpOnline
       │    ForForceMultiple: grpOnline
       │    宣布失败: (触发单位()的所有者), "TRIGSTR_5723"
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-06_002_UsableAbility">
<summary><strong>📌 UsableAbility</strong> <code>06_002_UsableAbility</code></summary>

```text
触发器: UsableAbility (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_003_PassiveAbility">
<summary><strong>📌 PassiveAbility</strong> <code>06_003_PassiveAbility</code></summary>

```text
触发器: PassiveAbility (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_004_AnyUnitDamaged">
<summary><strong>📌 AnyUnitDamaged</strong> <code>06_004_AnyUnitDamaged</code></summary>

```text
触发器: AnyUnitDamaged (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ 是敌方单位(伤害来源(), (触发单位()的所有者)) == TRUE
动作
  ├─ ── 毒蛇守卫追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == osp4
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(uPlayerHeros[玩家号((伤害来源()的所有者))], I04O) == TRUE
  │    │      ├─ 则
  │    │      │    伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (5000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    │      └─ 否则
  │    │           伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (2000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 厚土甲追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nbrg
  │    ├─ 则
  │    │    伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (10000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 雀羽扇追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == n016
  │    ├─ 则
  │    │    伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (30000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 万箭诛仙追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == osp1
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(uTemp, I04O) == TRUE
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),(1+SquareRoot(GetHeroLevel..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),(1+SquareRoot(GetHeroLevel..."
  │    └─ 否则: (无)
  ├─ ── 冰冻箭雨追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nemi
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位技能等级(uTemp, A00B) == 1
  │    │      │    ├─ 随机[6~8] == 7
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ ── 术士 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == njg1
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nsko
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ ── 冰晶追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == ndwm
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(uTemp, I04O) == TRUE
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*(G..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*(G..."
  │    └─ 否则: (无)
  ├─ ── 寒冰天赋减免 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(A005, 触发单位()) == 1
  │    │    ├─ 随机[0~1] == 0
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 伤害值() OperatorGreaterEq ((英雄等级(触发单位())转实数) x 2500.00)
  │    │      ├─ 则
  │    │      │    SetUnitLifeBJ: 触发单位(), (单位状态(UnitStateLife, 触发单位()) + ((英雄等级(触发单位())转实数) x 2500.00))
  │    │      └─ 否则
  │    │           SetUnitLifeBJ: 触发单位(), (单位状态(UnitStateLife, 触发单位()) + 伤害值())
  │    └─ 否则: (无)
  ├─ ── 冰之束缚追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nmpe
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    └─ 否则: (无)
  ├─ ── 空间割裂 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == necr
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位类型判断(触发单位(), UnitTypeGiant) == TRUE
  │    │      ├─ 则
  │    │      │    伤害: uKongJian[0]→触发单位(): (25000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    │      └─ 否则
  │    │           伤害: uKongJian[0]→触发单位(): (50000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 龙神岁月衰老 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == hwt3
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 玩家科技等级(R006, (伤害来源()的所有者)) == 1
  │    │      │    ├─ 玩家科技等级(Rhcd, (伤害来源()的所有者)) == 1
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位有魔法效果(伤害来源(), BNab) == TRUE
  │    │    ├─ 单位技能等级(触发单位(), A00K) == 1
  │    │    ├─ 随机[0~1] == 0
  │    ├─ 则
  │    │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │    └─ 否则: (无)
  ├─ ── 雷霆炼狱伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == uloc
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 玩家科技等级(R006, (伤害来源()的所有者)) == 1
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    └─ 否则: (无)
  ├─ ── 雷电附体伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nsea
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    └─ 否则: (无)
  ├─ ── 灵魂之剑伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nmrl
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),SquareRoot(GetHeroLevel(ud..."
  │    └─ 否则: (无)
  ├─ ── 灵魂之剑被动伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nhef
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ ── 炽炎马甲伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nlv3
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nlv2
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Stampede\StampedeMissileDeath.mdl, 触发单位(), "chest")
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetRandomInt(10,20)*(GetHe..."
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nsce
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    销毁特效 创建特效(附着单位)(Objects\Spawnmodels\Human\HCancelDeath\HCancelDeath.mdl, 触发单位(), "chest")
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ ── 道玄伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == hhes
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Other\Stampede\StampedeMissileDeath.mdl, 触发单位(), "chest")
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == hwat
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(uTemp, I04O) == TRUE
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*10..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*10..."
  │    └─ 否则: (无)
  ├─ ── 妖灵暴风雪伤害 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nalb
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位技能等级(uTemp, A08C) == 1
  │    │      │    ├─ 玩家科技等级(R006, (uTemp的所有者)) == 1
  │    │      ├─ 则
  │    │      │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*(G..."
  │    │      └─ 否则
  │    │           CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*(G..."
  │    └─ 否则: (无)
  ├─ ── 闪电链追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nvul
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((伤害来源()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    CustomScriptCode: "call UnitDamageTargetBJ(udg_uTemp,GetTriggerUnit(),GetHeroLevel(udg_uTemp)*0...."
  │    └─ 否则: (无)
  ├─ ── 怨女准神 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(A077, 触发单位()) == 1
  │    │    ├─ 玩家科技等级(R008, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 随机[1~10] == 5
  │    │      ├─ 则
  │    │      │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Resurrect\ResurrectTarget.mdl, 触发单位(), "overhead")
  │    │      │    设置生命百分比: 触发单位(), 100
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: 单位类型判断(伤害来源(), 英雄) == TRUE
  │    │      ├─ 则
  │    │      │    销毁特效 创建特效(附着单位)(war3mapImported\leidian2.mdx, 伤害来源(), "overhead")
  │    │      │    伤害: 触发单位()→伤害来源(): (单位状态(UnitStateLife, 伤害来源()) x 2.00) (AttackTypeNormal/DamageTypeUniversal)
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 致命毒素追加 ──
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == nech
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(uPlayerHeros[玩家号((伤害来源()的所有者))], I04O) == TRUE
  │    │      ├─ 则
  │    │      │    伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (2500.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeHero/DamageTypeSlowPoison)
  │    │      └─ 否则
  │    │           伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (25000.00 x (英雄等级(uPlayerHeros[玩家号((伤害来源()的所有者))])转实数)) (AttackTypeHero/DamageTypeSlowPoison)
  │    └─ 否则: (无)
  ├─ ── 狐妖追加 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ (伤害来源()类型ID) == e001
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │    ├─ 单位持有物品类型(触发单位(), I03V) == TRUE
  │    │    ├─ 随机[1~10] == 4
  │    ├─ 则
  │    │    伤害: 伤害来源()→触发单位(): (单位状态(UnitStateMaxLife, 触发单位()) / 4.00) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 噬魂球追加 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位持有物品类型(伤害来源(), I04V) == TRUE
  │    │    ├─ 随机[1~20] == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(伤害来源(), I04O) == TRUE
  │    │      ├─ 则
  │    │      │    伤害: 伤害来源()→触发单位(): (10.00 x 伤害值()) (AttackTypeChaos/DamageTypeUniversal)
  │    │      └─ 否则
  │    │           伤害: 伤害来源()→触发单位(): (5.00 x 伤害值()) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 妖灵准神追加 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(伤害来源(), A085) == 1
  │    │    ├─ 玩家科技等级(R008, (伤害来源()的所有者)) == 1
  │    │    ├─ 随机[1~20] == 5
  │    ├─ 则
  │    │    销毁特效 创建特效(附着单位)(Abilities\Spells\Human\Resurrect\ResurrectTarget.mdl, 触发单位(), "overhead")
  │    │    伤害: 伤害来源()→触发单位(): ((随机[5~66]转实数) x 伤害值()) (AttackTypeChaos/DamageTypeUniversal)
  │    └─ 否则: (无)
  ├─ ── 黯灭之戒追加 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位持有物品类型(触发单位(), I04U) == TRUE
  │    │    ├─ 随机[1~10] == 1
  │    ├─ 则
  │    │    伤害: 触发单位()→伤害来源(): (1000.00 x (英雄等级(触发单位())转实数)) (AttackTypeNormal/DamageTypeShadowStrike)
  │    │    SetUnitLifeBJ: 触发单位(), (单位状态(UnitStateLife, 触发单位()) + (1000.00 x (英雄等级(触发单位())转实数)))
  │    └─ 否则: (无)
  ├─ ── 噬魂杖伤害减免 ──
  ├─ 如果
  │    ├─ 条件: 单位持有物品类型(触发单位(), I03I) == TRUE
  │    ├─ 则
  │    │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + (伤害值() x 0.60))
  │    └─ 否则: (无)
  ├─ ── 幽冥伤害减免 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(触发单位(), A078) == 1
  │    │    ├─ 随机[1~2] == 2
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: (布尔比较(单位持有物品类型(触发单位(), I04O), OperatorEqualENE, true) 或 布尔比较(单位持有物品类型(伤害来源(), I04O), OperatorEqualENE, true))
  │    │      ├─ 则
  │    │      │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │    │      └─ 否则
  │    │           如果
  │    │             ├─ 条件: 随机[1~2] == 2
  │    │             ├─ 则
  │    │             │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │    │             └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 玄武 天赋减免 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(触发单位(), A0AV) == 1
  │    │    ├─ 地形可通行(单位X坐标(触发单位()), 单位Y坐标(触发单位()), PathingTypeFloatability) == TRUE
  │    ├─ 则
  │    │    设置生命百分比: 触发单位(), 100
  │    └─ 否则: (无)
  ├─ ── 神格减免 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(触发单位(), A0B3) == 1
  │    │    ├─ 单位技能等级(伤害来源(), A0B3) == 0
  │    │    ├─ 伤害值() OperatorGreaterEq 单位状态(触发单位(), UnitStateLife)
  │    │    ├─ 伤害值() OperatorLessEq (单位状态(UnitStateMaxLife, 触发单位()) x 10.00)
  │    ├─ 则
  │    │    设置无敌: 触发单位(), InvulnerabilityInvulnerable
  │    │    添加 触发单位() → grpInvincible
  │    │    运行计时器 tInvincible (一次性, 0.00s)
  │    └─ 否则: (无)
  ├─ ── 天书下卷减免 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == uTianShuXiaJuan
  │    ├─ 则
  │    │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │    └─ 否则: (无)
  ├─ ── 鲜血领域减免 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位有魔法效果(伤害来源(), B01A) == TRUE
  │    │    ├─ 任一成立
  │    ├─ 则
  │    │    SetUnitLifeBJ: 伤害来源(), (单位状态(伤害来源(), UnitStateLife) + 伤害值())
  │    └─ 否则: (无)
  ├─ ── 虚空之力反弹 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位技能等级(触发单位(), A082) == 1
  │    │    ├─ 玩家科技等级(R008, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 随机[1~10] OperatorLess 4
  │    │      ├─ 则
  │    │      │    伤害: 触发单位()→伤害来源(): 伤害值() (AttackTypeChaos/DamageTypeUniversal)
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: 随机[1~100] OperatorLess 65
  │    │      ├─ 则
  │    │      │    SetUnitLifeBJ: 触发单位(), (单位状态(触发单位(), UnitStateLife) + 伤害值())
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 浮生老头 ──
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 触发单位() == gg_unit_H00J_0028
       │    ├─ 单位类型判断(伤害来源(), 英雄) == TRUE
       │    ├─ 伤害值() OperatorGreaterEq 0.10
       ├─ 则
       │    显示文本→(伤害来源()的所有者): 0
       └─ 否则: (无)
```

</details>

<details id="trigger-06_005_UnitSummon">
<summary><strong>📌 UnitSummon</strong> <code>06_005_UnitSummon</code></summary>

```text
触发器: UnitSummon (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_006_UnitEnterMap">
<summary><strong>📌 UnitEnterMap</strong> <code>06_006_UnitEnterMap</code></summary>

```text
触发器: UnitEnterMap (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(可用地图区域())
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == osp3
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    创建 1个|osp2|→(触发单位()的所有者) 在 pTemp 面向默认朝向
  │    │    UnitApplyTimedLife: 最后创建的单位(), TimedLifeBuffCodeWaterElemental, 60
  │    │    循环整数A 1→5
  │    │      └─ CustomScriptCode: "call CreateUnit(GetOwningPlayer(GetTriggerUnit()), 'nmrl', GetLocationX(udg_p..."
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == eilw
  │    ├─ 则
  │    │    单位发布命令(立即): 触发单位(), UnitOrderLocustSwarm
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == njg1
  │    ├─ 则
  │    │    设置 iTemp = 玩家号((触发单位()的所有者))
  │    │    设置 uTemp = uPlayerHeros[iTemp]
  │    │    命令 触发单位() → UnitOrderStampede 到 单位X坐标(uTemp)
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nsko
  │    ├─ 则
  │    │    命令 触发单位() → UnitOrderClusterRockets 到 单位X坐标(触发单位())
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nske
  │    ├─ 则
  │    │    单位发布命令(立即): 触发单位(), UnitOrderStomp
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == hwt2
  │    ├─ 则
  │    │    设置 grpTemp = 玩家指定类型单位((触发单位()的所有者), hwt2)
  │    │    设置 iTemp = (grpTemp中的单位数)
  │    │    如果
  │    │      ├─ 条件: iTemp OperatorGreater 4
  │    │      ├─ 则
  │    │      │    显示文本→(触发单位()的所有者): 0
  │    │      │    移除 触发单位()
  │    │      └─ 否则: (无)
  │    │    删除单位组 grpTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == nsce
  │    ├─ 则
  │    │    PolledWait: 1.00
  │    │    单位发布命令(立即): 触发单位(), UnitOrderWhirlWind
  │    │    返回
  │    └─ 否则: (无)
  ├─ 循环整数A 1→35
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ (触发单位()类型ID) == uJinGong[循环整数A]
  │         │    ├─ 玩家在玩家组中((触发单位()的所有者), grpOnline) == TRUE
  │         ├─ 则
  │         │    如果
  │         │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 40
  │         │      ├─ 则
  │         │      │    SetUnitAbilityLevelSwapped: aJinGongGuai[循环整数A], 触发单位(), 4
  │         │      │    如果
  │         │      │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 50
  │         │      │      ├─ 则
  │         │      │      │    添加技能: 触发单位(), aJinGongGuaiHard[循环整数A]
  │         │      │      │    如果
  │         │      │      │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 80
  │         │      │      │      ├─ 则
  │         │      │      │      │    SetUnitAbilityLevelSwapped: aJinGongGuaiHard[循环整数A], 触发单位(), 4
  │         │      │      │      │    返回
  │         │      │      │      └─ 否则: (无)
  │         │      │      │    如果
  │         │      │      │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 70
  │         │      │      │      ├─ 则
  │         │      │      │      │    SetUnitAbilityLevelSwapped: aJinGongGuaiHard[循环整数A], 触发单位(), 3
  │         │      │      │      │    返回
  │         │      │      │      └─ 否则: (无)
  │         │      │      │    如果
  │         │      │      │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 60
  │         │      │      │      ├─ 则
  │         │      │      │      │    SetUnitAbilityLevelSwapped: aJinGongGuaiHard[循环整数A], 触发单位(), 2
  │         │      │      │      │    返回
  │         │      │      │      └─ 否则: (无)
  │         │      │      └─ 否则: (无)
  │         │      │    返回
  │         │      └─ 否则: (无)
  │         │    如果
  │         │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 30
  │         │      ├─ 则
  │         │      │    SetUnitAbilityLevelSwapped: aJinGongGuai[循环整数A], 触发单位(), 3
  │         │      │    返回
  │         │      └─ 否则: (无)
  │         │    如果
  │         │      ├─ 条件: 玩家科技等级(Rhme, (触发单位()的所有者)) OperatorGreaterEq 20
  │         │      ├─ 则
  │         │      │    SetUnitAbilityLevelSwapped: aJinGongGuai[循环整数A], 触发单位(), 2
  │         │      │    返回
  │         │      └─ 否则: (无)
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
       │    ├─ uPlayerHeros[玩家号((触发单位()的所有者))] == UnitNull
       │    ├─ uPlayerHeros[玩家号((触发单位()的所有者))] == 触发单位()
       │    ├─ uPlayerHeros[(玩家号((触发单位()的所有者)) + 20)] == 触发单位()
       │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
       │    ├─ 是镜像单位(触发单位()) == TRUE
       ├─ 则
       │    移除 触发单位()
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-06_007_HeroLevelUp">
<summary><strong>📌 HeroLevelUp</strong> <code>06_007_HeroLevelUp</code></summary>

```text
触发器: HeroLevelUp (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Level
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ ── 元神升级 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == H004
  │    ├─ 则
  │    │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd(玩家科技等级(Rhme, 玩家9(灰)) x 100)
  │    │    修改 触发单位() 的HeroStatAgi: ModifyMethodAdd(玩家科技等级(Rhme, 玩家9(灰)) x 100)
  │    │    修改 触发单位() 的HeroStatInt: ModifyMethodAdd(玩家科技等级(Rhme, 玩家9(灰)) x 100)
  │    └─ 否则: (无)
  ├─ ── 内丹升级 ──
  ├─ 如果
  │    ├─ 条件: 单位在单位组中(触发单位(), grpNeiDan) == TRUE
  │    ├─ 则
  │    │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd10
  │    │    修改 触发单位() 的HeroStatAgi: ModifyMethodAdd10
  │    │    修改 触发单位() 的HeroStatInt: ModifyMethodAdd10
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 单位技能等级(触发单位(), A06V) == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 玩家科技等级(Rhcd, (触发单位()的所有者)) == 1
  │    │      │    ├─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
  │    │      ├─ 则
  │    │      │    ── 龙神完全成长 ──
  │    │      │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd英雄等级(触发单位())
  │    │      │    修改 触发单位() 的HeroStatAgi: ModifyMethodAdd英雄等级(触发单位())
  │    │      │    修改 触发单位() 的HeroStatInt: ModifyMethodAdd英雄等级(触发单位())
  │    │      │    如果
  │    │      │      ├─ 条件: 全部成立
  │    │      │      │    ├─ 单位持有物品类型(触发单位(), I04N) == TRUE
  │    │      │      │    ├─ 单位持有物品类型(触发单位(), I02N) == TRUE
  │    │      │      │    ├─ 单位持有物品类型(触发单位(), I02K) == TRUE
  │    │      │      │    ├─ 随机[1~100] == 2
  │    │      │      ├─ 则
  │    │      │      │    删除物品: 单位携带物品(按类型)(触发单位(), I02N)
  │    │      │      │    删除物品: 单位携带物品(按类型)(触发单位(), I02K)
  │    │      │      │    UnitAddItemByIdSwapped: I04N, 触发单位()
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则
  │    │           ── 龙神不完全成长 ──
  │    │           修改 触发单位() 的HeroStatStr: ModifyMethodAdd(英雄等级(触发单位()) / 2)
  │    │           修改 触发单位() 的HeroStatAgi: ModifyMethodAdd(英雄等级(触发单位()) / 5)
  │    │           修改 触发单位() 的HeroStatInt: ModifyMethodAdd(英雄等级(触发单位()) / 10)
  │    └─ 否则: (无)
  ├─ ── 怒剑狂湳持续时间升级 ──
  ├─ 如果
  │    ├─ 条件: 单位技能等级(触发单位(), A045) OperatorGreater 0
  │    ├─ 则
  │    │    设置技能等级: 触发单位(), A045, ((英雄等级(触发单位()) / 100) + 1)
  │    └─ 否则: (无)
  ├─ ── 地狱火科技升级 ──
  └─ 如果
       ├─ 条件: 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
       ├─ 则
       │    SetPlayerTechResearchedSwap: R000, (英雄等级(触发单位()) / 10), (触发单位()的所有者)
       └─ 否则: (无)
```

</details>

<details id="trigger-06_008_HeroLearnSkill">
<summary><strong>📌 HeroLearnSkill</strong> <code>06_008_HeroLearnSkill</code></summary>

```text
触发器: HeroLearnSkill (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 单位技能等级(触发单位(), A03O) == 1
  │    ├─ 则
  │    │    修改 触发单位() 的HeroStatStr: ModifyMethodAdd(6 x 英雄等级(触发单位()))
  │    │    修改 触发单位() 的HeroStatAgi: ModifyMethodAdd(8 x 英雄等级(触发单位()))
  │    │    修改 触发单位() 的HeroStatInt: ModifyMethodAdd(10 x 英雄等级(触发单位()))
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(学习的技能(), OperatorEqualENE, A03B)
  │    │    ├─ 触发单位() == uSiWangQiXi
  │    ├─ 则
  │    │    运行计时器 tSiWangQiXi (循环, 1.00s)
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A03R)
  │    ├─ 则
  │    │    设置 uChiYanHuoJingLing[0] = 触发单位()
  │    │    如果
  │    │      ├─ 条件: 玩家科技等级(R006, (触发单位()的所有者)) == 1
  │    │      ├─ 则
  │    │      │    TriggerExecute: gg_trg_CYHuoJingLingInit
  │    │      └─ 否则: (无)
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(学习的技能(), OperatorEqualENE, A00F)
  │    ├─ 则
  │    │    添加技能: 触发单位(), A08F
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, A08F
  │    │    SetPlayerAbilityAvailable: (触发单位()的所有者), A08F, EnableDisableDisable
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 技能ID比较(学习的技能(), OperatorEqualENE, A08C)
       │    ├─ 触发单位() == uWuJinChangYe
       │    ├─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
       ├─ 则
       │    添加事件到 gg_trg_YLWuJinChangYe: 注册单位进入范围事件(512.00, uWuJinChangYe)
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-06_009_AbilityStartCast">
<summary><strong>📌 AbilityStartCast</strong> <code>06_009_AbilityStartCast</code></summary>

```text
触发器: AbilityStartCast (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_010_其他类别">
<summary><strong>📌 其他类别</strong> <code>06_010_其他类别</code></summary>

```text
触发器: 其他类别 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_011_YLWuJinChangYe">
<summary><strong>📌 YLWuJinChangYe</strong> <code>06_011_YLWuJinChangYe</code></summary>

```text
触发器: YLWuJinChangYe (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 随机[1~5] == 2
       │    ├─ 是敌方单位(触发单位(), (uWuJinChangYe的所有者)) == TRUE
       ├─ 则
       │    设置 pTemp = (触发单位()的位置)
       │    创建 1个|nalb|→(uWuJinChangYe的所有者) 在 pTemp 面向默认朝向
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderSleep, 触发单位()
       │    清除点 pTemp
       └─ 否则: (无)
```

</details>

<details id="trigger-06_012_CYHuoJingLingInit">
<summary><strong>📌 CYHuoJingLingInit</strong> <code>06_012_CYHuoJingLingInit</code></summary>

```text
触发器: CYHuoJingLingInit (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uChiYanHuoJingLing[0]的位置)
  ├─ 循环整数A 1→5
  │    ├─ 设置 uChiYanHuoJingLing[循环整数A] = 创建单位(指定点)((uChiYanHuoJingLing[0]的所有者), nlv2, pTemp, 0)
  │    └─ SetUnitVertexColorBJ: uChiYanHuoJingLing[循环整数A], 100, 100, 100, 50.00
  ├─ 添加事件到 gg_trg_CYHuoJingLing: 注册单位事件(uChiYanHuoJingLing[0], UnitEventIssuePointOrder)
  ├─ 添加事件到 gg_trg_CYHuoJingLing: 注册单位事件(uChiYanHuoJingLing[0], UnitEventIssueUnitOrder)
  ├─ 清除点 pTemp
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-06_013_CYHuoJingLing">
<summary><strong>📌 CYHuoJingLing</strong> <code>06_013_CYHuoJingLing</code></summary>

```text
触发器: CYHuoJingLing (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 循环整数A 1→5
  │    └─ 如果
  │         ├─ 条件: 两点距离(uChiYanHuoJingLing[0], uChiYanHuoJingLing[循环整数A]) OperatorGreaterEq 512.00
  │         ├─ 则
  │         │    移动单位: uChiYanHuoJingLing[循环整数A], (单位X坐标(触发单位()) + 自定义代码("256*CosBJ(bj_forLoopAIndex*72)")), (单位Y坐标(触发单位()) + 自定义代码("256*SinBJ(bj_forLoopAIndex*72)"))
  │         └─ 否则: (无)
  ├─ CustomScriptCode: "if GetTriggerEventId()==EVENT_UNIT_ISSUED_TARGET_ORDER then"
  ├─ 设置 uTemp = 命令目标单位()
  ├─ 如果
  │    ├─ 条件: uTemp == UnitNull
  │    ├─ 则
  │    │    循环整数A 1→5
  │    │      └─ 单位发布命令(目标): uChiYanHuoJingLing[循环整数A], UnitOrderSmartUnit, uTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ CustomScriptCode: "endif"
  ├─ CustomScriptCode: "if GetTriggerEventId()==EVENT_UNIT_ISSUED_POINT_ORDER then"
  ├─ 设置 pTemp = 命令目标点()
  ├─ 循环整数A 1→5
  │    └─ 命令 uChiYanHuoJingLing[循环整数A] → UnitOrderAIMove 到 (点X坐标(pTemp) + (256.00 x 余弦(自定义代码("bj_forLoopAIndex*72"))))
  └─ CustomScriptCode: "endif"
```

</details>

<details id="trigger-06_014_JinShengWuWei">
<summary><strong>📌 JinShengWuWei</strong> <code>06_014_JinShengWuWei</code></summary>

```text
触发器: JinShengWuWei (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 单位技能等级(触发单位(), A0A5) == 1
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 pTemp = (触发单位()的位置)
  ├─ 设置 grpTemp = 范围内符合条件的单位(500.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    ├─ CustomScriptCode: "local unit tu = GetTriggerUnit()"
  │    ├─ CustomScriptCode: "local integer lv=GetHeroLevel(tu)"
  │    ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, tu, true)"
  │    ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, tu, true)"
  │    ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, tu, true) "
  │    ├─ CustomScriptCode: "call DestroyEffect(AddSpecialEffect("war3mapImported\\Ay3s10.mdx",GetUnitX(Ge..."
  │    └─ CustomScriptCode: "call UnitDamageTargetBJ(tu,GetEnumUnit(),lv*(ll+mj*3+zl*2),ATTACK_TYPE_CHAOS,..."
  ├─ 运行计时器 tKuNanJSWW[玩家号((触发单位()的所有者))] (一次性, 30.00s)
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-06_015_SetHeroInvincible">
<summary><strong>📌 SetHeroInvincible</strong> <code>06_015_SetHeroInvincible</code></summary>

```text
触发器: SetHeroInvincible (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
动作
  ├─ 设置无敌: 触发单位(), InvulnerabilityInvulnerable
  ├─ PolledWait: 2
  ├─ 设置无敌: 触发单位(), InvulnerabilityVulnerable
  └─ 如果
       ├─ 条件: 单位技能等级(触发单位(), A080) == 0
       ├─ 则
       │    UnitAddAbilityBJ: A080, 触发单位()
       └─ 否则: (无)
```

</details>

<details id="trigger-06_016_UnBlinkable">
<summary><strong>📌 UnBlinkable</strong> <code>06_016_UnBlinkable</code></summary>

```text
触发器: UnBlinkable (单位/战斗) [✓] — 防止魔帝被放风筝有木有
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 是敌方单位(触发单位(), 玩家9(灰)) == TRUE
动作
  ├─ 设置 uTemp = 创建单位(指定坐标)(玩家9(灰), osw3, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
  └─ 单位发布命令(目标): uTemp, UnitOrderPurge, 触发单位()
```

</details>

<details id="trigger-06_017_UnBlinkableFushen">
<summary><strong>📌 UnBlinkableFushen</strong> <code>06_017_UnBlinkableFushen</code></summary>

```text
触发器: UnBlinkableFushen (单位/战斗) [✓] — 防止魔帝被放风筝有木有
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 是敌方单位(触发单位(), (uFuShenMoDi的所有者)) == TRUE
动作
  ├─ 设置 uTemp = 创建单位(指定坐标)((uFuShenMoDi的所有者), osw3, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
  └─ 单位发布命令(目标): uTemp, UnitOrderPurge, 触发单位()
```

</details>

<details id="trigger-06_018_RepickAbility">
<summary><strong>📌 RepickAbility</strong> <code>06_018_RepickAbility</code></summary>

```text
触发器: RepickAbility (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A0AW)
  └─ (触发单位()类型ID) == N00Y
动作
  ├─ 移除技能: 触发单位(), A004
  ├─ 移除技能: 触发单位(), A080
  ├─ 移除技能: 触发单位(), A099
  ├─ 移除技能: 触发单位(), A097
  ├─ 暂停计时器 PauseResumePause
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aTianFu[循环整数A()]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aHeroAbilityList[(0 + 循环整数A())]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aHeroAbilityList[(100 + 循环整数A())]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aHeroAbilityList[(200 + 循环整数A())]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aHeroAbilityList[(300 + 循环整数A())]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aHeroAbilityList[(400 + 循环整数A())]
  ├─ 循环整数A 1→14
  │    └─ 移除技能: 触发单位(), aZhunShen[循环整数A()]
  ├─ ── 天赋 ──
  ├─ 如果
  │    ├─ 条件: bTFHQ[玩家号(触发玩家())] == TRUE
  │    ├─ 则
  │    │    设置 iTemp = 随机[1~14]
  │    │    添加技能: 触发单位(), aTianFu[iTemp]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aTianFu[iTemp]
  │    │    如果
  │    │      ├─ 条件: iTemp == 3
  │    │      ├─ 则
  │    │      │    运行计时器 tBaoFengXue[玩家号((触发单位()的所有者))] (循环, 5.00s)
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: iTemp == 4
  │    │      ├─ 则
  │    │      │    添加技能: 触发单位(), A004
  │    │      │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, A004
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: iTemp == 14
  │    │      ├─ 则
  │    │      │    添加事件到 gg_trg_JinShengWuWei: 单位生命值事件(触发单位(), 小于, 0.90)
  │    │      └─ 否则: (无)
  │    └─ 否则: (无)
  ├─ ── 英雄技能 ──
  ├─ 如果
  │    ├─ 条件: 英雄等级(触发单位()) OperatorGreaterEq 5
  │    ├─ 则
  │    │    CustomScriptCode: "loop"
  │    │    设置 iTemp = 随机[1~14]
  │    │    CustomScriptCode: "if not udg_bHeroAbilityUseable[0+udg_iTemp] then"
  │    │    添加技能: 触发单位(), aHeroAbilityList[(0 + iTemp)]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(0 + iTemp)]
  │    │    CustomScriptCode: "exitwhen not udg_bHeroAbilityUseable[0+udg_iTemp]"
  │    │    CustomScriptCode: "endif"
  │    │    CustomScriptCode: "endloop"
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 英雄等级(触发单位()) OperatorGreaterEq 25
  │    ├─ 则
  │    │    CustomScriptCode: "loop"
  │    │    设置 iTemp = 随机[1~14]
  │    │    CustomScriptCode: "if not udg_bHeroAbilityUseable[100+udg_iTemp] then"
  │    │    添加技能: 触发单位(), aHeroAbilityList[(100 + iTemp)]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(100 + iTemp)]
  │    │    CustomScriptCode: "exitwhen not udg_bHeroAbilityUseable[100+udg_iTemp]"
  │    │    CustomScriptCode: "endif"
  │    │    CustomScriptCode: "endloop"
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 英雄等级(触发单位()) OperatorGreaterEq 50
  │    ├─ 则
  │    │    CustomScriptCode: "loop"
  │    │    设置 iTemp = 随机[1~14]
  │    │    CustomScriptCode: "if not udg_bHeroAbilityUseable[200+udg_iTemp] then"
  │    │    添加技能: 触发单位(), aHeroAbilityList[(200 + iTemp)]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(200 + iTemp)]
  │    │    CustomScriptCode: "exitwhen not udg_bHeroAbilityUseable[200+udg_iTemp]"
  │    │    CustomScriptCode: "endif"
  │    │    CustomScriptCode: "endloop"
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 英雄等级(触发单位()) OperatorGreaterEq 100
  │    ├─ 则
  │    │    CustomScriptCode: "loop"
  │    │    设置 iTemp = 随机[1~14]
  │    │    CustomScriptCode: "if not udg_bHeroAbilityUseable[300+udg_iTemp] then"
  │    │    添加技能: 触发单位(), aHeroAbilityList[(300 + iTemp)]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(300 + iTemp)]
  │    │    CustomScriptCode: "exitwhen not udg_bHeroAbilityUseable[300+udg_iTemp]"
  │    │    CustomScriptCode: "endif"
  │    │    CustomScriptCode: "endloop"
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家科技等级(R006, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    CustomScriptCode: "loop"
  │    │    设置 iTemp = 随机[1~14]
  │    │    CustomScriptCode: "if not udg_bHeroAbilityUseable[400+udg_iTemp] then"
  │    │    添加技能: 触发单位(), aHeroAbilityList[(400 + iTemp)]
  │    │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(400 + iTemp)]
  │    │    如果
  │    │      ├─ 条件: iTemp == 5
  │    │      ├─ 则
  │    │      │    添加技能: 触发单位(), A080
  │    │      │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, A080
  │    │      └─ 否则: (无)
  │    │    CustomScriptCode: "exitwhen not udg_bHeroAbilityUseable[400+udg_iTemp]"
  │    │    CustomScriptCode: "endif"
  │    │    CustomScriptCode: "endloop"
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 玩家科技等级(R008, (触发单位()的所有者)) == 1
       ├─ 则
       │    设置 iTemp = 随机[1~14]
       │    添加技能: 触发单位(), aZhunShen[iTemp]
       │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, aHeroAbilityList[(400 + iTemp)]
       └─ 否则: (无)
```

</details>

<details id="trigger-06_019_技能计时器">
<summary><strong>📌 技能计时器</strong> <code>06_019_技能计时器</code></summary>

```text
触发器: 技能计时器 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-06_020_tInvincible">
<summary><strong>📌 tInvincible</strong> <code>06_020_tInvincible</code></summary>

```text
触发器: tInvincible (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tInvincible 到期
条件
  └─ 无
动作
  ├─ 单位组: 选取 grpInvincible 中所有单位
  │    └─ 设置无敌: 选取单位(), InvulnerabilityVulnerable
  └─ GroupClear: grpInvincible
```

</details>

<details id="trigger-06_021_tTianShuXiaJuan">
<summary><strong>📌 tTianShuXiaJuan</strong> <code>06_021_tTianShuXiaJuan</code></summary>

```text
触发器: tTianShuXiaJuan (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tTianShuXiaJuan 到期
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 单位持有物品(uTianShuXiaJuan, itemTSXJ) == TRUE
       ├─ 则
       │    MoveLightningEx: lightTSXJ, AllowDontDont, 0.00, 0.00, 60.00, 0.00, 0.00, 60.00
       │    如果
       │      ├─ 条件: 英雄属性(HeroStatStr, uTianShuXiaJuan, InclusionExclude) OperatorGreater (物品自定义值(itemTSXJ) x 33)
       │      ├─ 则
       │      │    修改 uTianShuXiaJuan 的HeroStatStr: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
       │      └─ 否则
       │           修改 uTianShuXiaJuan 的HeroStatStr: ModifyMethodSet1
       │    如果
       │      ├─ 条件: 英雄属性(HeroStatAgi, uTianShuXiaJuan, InclusionExclude) OperatorGreater (物品自定义值(itemTSXJ) x 33)
       │      ├─ 则
       │      │    修改 uTianShuXiaJuan 的HeroStatAgi: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
       │      └─ 否则
       │           修改 uTianShuXiaJuan 的HeroStatAgi: ModifyMethodSet1
       │    如果
       │      ├─ 条件: 英雄属性(HeroStatInt, uTianShuXiaJuan, InclusionExclude) OperatorGreater (物品自定义值(itemTSXJ) x 33)
       │      ├─ 则
       │      │    修改 uTianShuXiaJuan 的HeroStatInt: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
       │      └─ 否则
       │           修改 uTianShuXiaJuan 的HeroStatInt: ModifyMethodSet1
       │    SetItemUserData: itemTSXJ, 0
       │    设置 uTianShuXiaJuan = UnitNull
       │    设置 grpTemp = 区域内符合条件的单位(可用地图区域(), 布尔比较(单位持有物品(过滤单位(), itemTSXJ), OperatorEqualENE, true))
       │    设置 uTianShuXiaJuan = 单位组第一个单位(grpTemp)
       │    删除单位组 grpTemp
       └─ 否则
            如果
              ├─ 条件: 全部成立
              │    ├─ 单位类型判断(uTianShuXiaJuan, 英雄) == TRUE
              │    ├─ 单位存活判断(uTianShuXiaJuan) == TRUE
              │    ├─ 两点距离(uTianShuXiaJuan, gg_unit_ubon_0001) OperatorLess 2000.00
              ├─ 则
              │    MoveLightningEx: lightTSXJ, AllowDontDont, 单位X坐标(gg_unit_ubon_0001), 单位Y坐标(gg_unit_ubon_0001), 60.00, 单位X坐标(uTianShuXiaJuan), 单位Y坐标(uTianShuXiaJuan), 60.00
              │    SetItemUserData: itemTSXJ, (物品自定义值(itemTSXJ) + 1)
              │    修改 uTianShuXiaJuan 的HeroStatStr: ModifyMethodAdd33
              │    修改 uTianShuXiaJuan 的HeroStatAgi: ModifyMethodAdd33
              │    修改 uTianShuXiaJuan 的HeroStatInt: ModifyMethodAdd33
              └─ 否则
                   MoveLightningEx: lightTSXJ, AllowDontDont, 0.00, 0.00, 60.00, 0.00, 0.00, 60.00
                   修改 uTianShuXiaJuan 的HeroStatStr: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
                   修改 uTianShuXiaJuan 的HeroStatAgi: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
                   修改 uTianShuXiaJuan 的HeroStatInt: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
                   SetItemUserData: itemTSXJ, 0
                   设置 uTianShuXiaJuan = UnitNull
```

</details>

<details id="trigger-06_022_tBingZhiDiaoLing">
<summary><strong>📌 tBingZhiDiaoLing</strong> <code>06_022_tBingZhiDiaoLing</code></summary>

```text
触发器: tBingZhiDiaoLing (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tBingZhiDiaoLing 到期
条件
  └─ 无
动作
  ├─ CustomScriptCode: "local integer i = udg_iBZDL"
  ├─ CustomScriptCode: "local unit u = udg_uBZDL"
  ├─ CustomScriptCode: "local real x=GetUnitX(u)"
  ├─ CustomScriptCode: "local real y=GetUnitY(u)"
  └─ 如果
       ├─ 条件: iBZDL OperatorLess 100
       ├─ 则
       │    设置 iBZDL = (iBZDL + 1)
       │    SetUnitFacingTimed: uBZDL, 角度叠加(单位朝向角度(uBZDL), 8.00), 0
       │    CustomScriptCode: "call DestroyEffect( AddSpecialEffect("Abilities\\Spells\\Undead\\FrostNova\\F..."
       └─ 否则
            设置 iBZDL = 0
            PauseUnit: uBZDL, PauseUnpauseOptionUnpause
            暂停计时器 tBingZhiDiaoLing
```

</details>

<details id="trigger-06_023_tJiCiTianYa">
<summary><strong>📌 tJiCiTianYa</strong> <code>06_023_tJiCiTianYa</code></summary>

```text
触发器: tJiCiTianYa (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tJiCiTianYa 到期
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 单位有魔法效果(uJiCiTianYa, B01F) == TRUE
       ├─ 则
       │    设置 pTemp = (uJiCiTianYa的位置)
       │    创建 1个|nalb|→(uJiCiTianYa的所有者) 在 pTemp 面向默认朝向
       │    按ID发布目标命令: 最后创建的单位(), OrderCodeItemIllusion, uJiCiTianYa
       └─ 否则
            移除技能: uJiCiTianYa, A08G
            暂停计时器 tJiCiTianYa
```

</details>

<details id="trigger-06_024_tNJKL">
<summary><strong>📌 tNJKL</strong> <code>06_024_tNJKL</code></summary>

```text
触发器: tNJKL (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 循环整数A 1→7
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, tNJKL[循环整数A])
            ├─ 则
            │    如果
            │      ├─ 条件: 单位有魔法效果(uNJKL[循环整数A], B006) == TRUE
            │      ├─ 则
            │      │    设置 uTemp = uNJKL[循环整数A]
            │      │    设置 pTemp = (uTemp的位置)
            │      │    设置 grpTemp = 范围内符合条件的单位(512, pTemp, (布尔比较(是敌方单位(过滤单位(), (uNJKL[循环整数A]的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(uNJKL[循环整数A]), OperatorEqualENE, true)))
            │      │    设置 uTemp = 随机选取单位组单位(grpTemp)
            │      │    清除点 pTemp
            │      │    删除单位组 grpTemp
            │      │    如果
            │      │      ├─ 条件: 全部成立
            │      │      │    ├─ uTemp == UnitNull
            │      │      │    ├─ 单位存活判断(uTemp) == TRUE
            │      │      ├─ 则
            │      │      │    设置 pTemp = (uTemp的位置)
            │      │      │    移动单位: uNJKL[循环整数A], pTemp
            │      │      │    播放动画: uNJKL[循环整数A], "Attack Slam"
            │      │      │    销毁特效 创建特效(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, pTemp)
            │      │      │    伤害: uNJKL[循环整数A]→uTemp: ((英雄敏捷(uNJKL[循环整数A], InclusionInclude)转实数) x 随机实数(50.00, 200.00)) (AttackTypeChaos/DamageTypeUniversal)
            │      │      │    清除点 pTemp
            │      │      └─ 否则: (无)
            │      └─ 否则
            │           暂停计时器 tNJKL[循环整数A]
            └─ 否则: (无)
```

</details>

<details id="trigger-06_025_tBaoFengxue">
<summary><strong>📌 tBaoFengxue</strong> <code>06_025_tBaoFengxue</code></summary>

```text
触发器: tBaoFengxue (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ CustomScriptCode: "local unit u = null"
  ├─ CustomScriptCode: "local integer i = 0"
  └─ 循环整数A 1→7
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, tBaoFengXue[循环整数A])
            ├─ 则
            │    设置 uTemp = uPlayerHeros[循环整数A]
            │    CustomScriptCode: "set i = bj_forLoopAIndex"
            │    如果
            │      ├─ 条件: 单位存活判断(uTemp) == TRUE
            │      ├─ 则
            │      │    设置 pTemp = (uTemp的位置)
            │      │    创建 1个|nalb|→(uTemp的所有者) 在 pTemp 面向默认朝向
            │      │    CustomScriptCode: "set u = GetLastCreatedUnit()"
            │      │    如果
            │      │      ├─ 条件: 全部成立
            │      │      │    ├─ 单位技能等级(uTemp, A08C) == 1
            │      │      │    ├─ 玩家科技等级(R006, (uTemp的所有者)) == 1
            │      │      ├─ 则
            │      │      │    设置技能等级: 最后创建的单位(), A083, 2
            │      │      └─ 否则: (无)
            │      │    命令 最后创建的单位() → UnitOrderBlizzard 到 pTemp
            │      │    清除点 pTemp
            │      │    PolledWait: 1.80
            │      │    CustomScriptCode: " set udg_uTemp = udg_uPlayerHeros[i]"
            │      │    如果
            │      │      ├─ 条件: 单位持有物品类型(uTemp, schl) == TRUE
            │      │      ├─ 则
            │      │      │    设置 pTemp = (uTemp的位置)
            │      │      │    如果
            │      │      │      ├─ 条件: 全部成立
            │      │      │      │    ├─ 单位技能等级(uTemp, A08C) == 1
            │      │      │      │    ├─ 玩家科技等级(R006, (uTemp的所有者)) == 1
            │      │      │      ├─ 则
            │      │      │      │    设置 grpTemp = 范围内符合条件的单位(2000.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uTemp的所有者)), OperatorEqualENE, true))
            │      │      │      └─ 否则
            │      │      │           设置 grpTemp = 范围内符合条件的单位(800.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uTemp的所有者)), OperatorEqualENE, true))
            │      │      │    CustomScriptCode: " set udg_uTemp1 = u"
            │      │      │    单位组: 选取 grpTemp 中所有单位
            │      │      │      └─ 伤害: uTemp1→选取单位(): 10.00 (AttackTypeChaos/DamageTypeUniversal)
            │      │      │    删除单位组 grpTemp
            │      │      │    清除点 pTemp
            │      │      └─ 否则: (无)
            │      └─ 否则: (无)
            └─ 否则: (无)
```

</details>

<details id="trigger-06_026_tShunZhuanQianNian">
<summary><strong>📌 tShunZhuanQianNian</strong> <code>06_026_tShunZhuanQianNian</code></summary>

```text
触发器: tShunZhuanQianNian (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tShunZhuanQianNian 到期
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uShunZhuanQianNian的位置)
  ├─ 设置 rTemp = 两点间距(pShunZhuanQianNian, pTemp)
  └─ 如果
       ├─ 条件: (实数比较(rTemp, OperatorLessEq, 20.00) 或 整数比较(单位自定义值(uShunZhuanQianNian), OperatorGreaterEq, 250))
       ├─ 则
       │    暂停计时器 tShunZhuanQianNian
       │    SetUnitPathing: uShunZhuanQianNian, PathingOn
       │    设置单位自定义值: uShunZhuanQianNian, 0
       │    单位发布命令(立即): uShunZhuanQianNian, UnitOrderStop
       │    清除点 pShunZhuanQianNian
       │    清除点 pTemp
       └─ 否则
            设置单位自定义值: uShunZhuanQianNian, (单位自定义值(uShunZhuanQianNian) + 1)
            设置 iTemp = 实数转整数((rTemp / 50.00))
            SetUnitX: uShunZhuanQianNian, (单位X坐标(uShunZhuanQianNian) + ((点X坐标(pShunZhuanQianNian) - 单位X坐标(uShunZhuanQianNian)) / (iTemp转实数)))
            SetUnitY: uShunZhuanQianNian, (单位Y坐标(uShunZhuanQianNian) + ((点Y坐标(pShunZhuanQianNian) - 单位Y坐标(uShunZhuanQianNian)) / (iTemp转实数)))
            清除点 pTemp
            如果
              ├─ 条件: 取模(单位自定义值(uShunZhuanQianNian), 10) == 0
              ├─ 则
              │    设置 pTemp = (uShunZhuanQianNian的位置)
              │    销毁特效 创建特效(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, pTemp)
              │    设置 grpTemp = 范围内符合条件的单位(500.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uShunZhuanQianNian的所有者)), OperatorEqualENE, true))
              │    单位组: 选取 grpTemp 中所有单位
              │      ├─ CustomScriptCode: "local unit tu = udg_uShunZhuanQianNian"
              │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uShunZhuanQianNian)"
              │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uShunZhuanQianNian, true)"
              │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uShunZhuanQianNian, true)"
              │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uShunZhuanQianNian, true) "
              │      └─ CustomScriptCode: "call UnitDamageTargetBJ(udg_uShunZhuanQianNian,GetEnumUnit(),0.4*lv*(ll*3.4+m..."
              │    删除单位组 grpTemp
              │    清除点 pTemp
              └─ 否则: (无)
```

</details>

<details id="trigger-06_027_tKongJianGeLie">
<summary><strong>📌 tKongJianGeLie</strong> <code>06_027_tKongJianGeLie</code></summary>

```text
触发器: tKongJianGeLie (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tKongJian 到期
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: iCountKongJian OperatorLess 20
       ├─ 则
       │    设置 pTemp = (uKongJian[1]的位置)
       │    创建 1个|necr|→(uKongJian[0]的所有者) 在 pTemp 面向GetRandomDirectionDeg()
       │    清除点 pTemp
       │    设置 iCountKongJian = (iCountKongJian + 1)
       └─ 否则
            设置 iCountKongJian = 0
            暂停计时器 tKongJian
```

</details>

<details id="trigger-06_028_tSiWangQiXi">
<summary><strong>📌 tSiWangQiXi</strong> <code>06_028_tSiWangQiXi</code></summary>

```text
触发器: tSiWangQiXi (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tSiWangQiXi 到期
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uSiWangQiXi的位置)
  ├─ 设置 grpTemp = 范围内符合条件的单位(512, pTemp, 布尔比较(是敌方单位(过滤单位(), (uSiWangQiXi的所有者)), OperatorEqualENE, true))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    ├─ CustomScriptCode: "local unit tu = udg_uSiWangQiXi"
  │    ├─ CustomScriptCode: "local integer lv=GetHeroLevel(tu)"
  │    ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, tu, true)"
  │    ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, tu, true)"
  │    ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, tu, true)"
  │    ├─ CustomScriptCode: "call DestroyEffect(AddSpecialEffectTarget("Objects\\Spawnmodels\\Undead\\Unde..."
  │    └─ CustomScriptCode: "call UnitDamageTargetBJ(tu,GetEnumUnit(),(SquareRoot(lv)+GetItemCharges(GetIt..."
  ├─ 删除单位组 grpTemp
  └─ 清除点 pTemp
```

</details>

<details id="trigger-06_029_tFengChenMoShi">
<summary><strong>📌 tFengChenMoShi</strong> <code>06_029_tFengChenMoShi</code></summary>

```text
触发器: tFengChenMoShi (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tFengChenMoShi 到期
条件
  └─ 无
动作
  ├─ 设置 grpTemp = 区域内符合条件的单位(可用地图区域(), (布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true) 且 布尔比较(单位持有物品类型(过滤单位(), I04O), OperatorEqualENE, true)))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ 如果
  │         ├─ 条件: 单位状态(UnitStateLife, 选取单位()) OperatorGreater 0.00
  │         ├─ 则
  │         │    CustomScriptCode: "call DestroyEffect(AddSpecialEffectTarget("Abilities\\Spells\\Human\\Resurrec..."
  │         │    CustomScriptCode: "call UnitDamageTargetBJ(GetEnumUnit(),GetEnumUnit(),1250000.,ATTACK_TYPE_CHAO..."
  │         │    CustomScriptCode: "call UnitDamageTargetBJ(GetEnumUnit(),GetEnumUnit(),750000.,ATTACK_TYPE_NORMA..."
  │         │    如果
  │         │      ├─ 条件: 单位状态(UnitStateLife, 选取单位()) OperatorGreater 0.00
  │         │      ├─ 则
  │         │      │    CustomScriptCode: "call ModifyHeroStat(0,GetEnumUnit(),0,GetRandomInt(27,$88))"
  │         │      │    CustomScriptCode: "call ModifyHeroStat(1,GetEnumUnit(),0,GetRandomInt(27,$88))"
  │         │      │    CustomScriptCode: "call ModifyHeroStat(2,GetEnumUnit(),0,GetRandomInt(27,$88))"
  │         │      └─ 否则
  │         │           移动物品到坐标: 单位携带物品(按类型)(选取单位(), I04O), 单位X坐标(选取单位()), 单位Y坐标(选取单位())
  │         └─ 否则
  │              移动物品到坐标: 单位携带物品(按类型)(选取单位(), I04O), 单位X坐标(选取单位()), 单位Y坐标(选取单位())
  └─ 删除单位组 grpTemp
```

</details>

<details id="trigger-06_030_tChuanXinCi">
<summary><strong>📌 tChuanXinCi</strong> <code>06_030_tChuanXinCi</code></summary>

```text
触发器: tChuanXinCi (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tChuanXinCi 到期
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uChuanXinCi的位置)
  ├─ 设置 grpTemp = 范围内符合条件的单位(1024.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uChuanXinCi的所有者)), OperatorEqualENE, true))
  ├─ 设置 iTemp = 随机[3~6]
  ├─ 显示文本→(uChuanXinCi的所有者): 0
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    ├─ CustomScriptCode: "local unit au = udg_uChuanXinCi"
  │    ├─ CustomScriptCode: "local player ap = GetOwningPlayer(au)"
  │    ├─ CustomScriptCode: "local integer apIndex=GetConvertedPlayerId(ap)"
  │    ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uPlayerHeros[apIndex])"
  │    ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uPlayerHeros[apIndex], true)"
  │    ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uPlayerHeros[apIndex], true)"
  │    ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uPlayerHeros[apIndex], true)"
  │    ├─ CustomScriptCode: "local location eLoc=GetUnitLoc(GetEnumUnit())"
  │    ├─ CustomScriptCode: "call DestroyEffect(AddSpecialEffectLoc("Abilities\\Spells\\Undead\\Impale\\Im..."
  │    ├─ CustomScriptCode: "call RemoveLocation(eLoc)"
  │    └─ CustomScriptCode: "call UnitDamageTargetBJ(udg_uPlayerHeros[apIndex],GetEnumUnit(),(0.13*lv*udg_..."
  ├─ 清除点 pTemp
  ├─ 删除单位组 grpTemp
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位技能等级(uChuanXinCi, A03D) == 1
       │    ├─ 玩家科技等级(R006, (uChuanXinCi的所有者)) == 1
       ├─ 则
       │    PolledWait: 0.20
       │    设置 pTemp = (uChuanXinCi的位置)
       │    设置 grpTemp = 范围内符合条件的单位(2048.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uChuanXinCi的所有者)), OperatorEqualENE, true))
       │    设置 iTemp = 随机[9~36]
       │    显示文本→(uChuanXinCi的所有者): 0
       │    单位组: 选取 grpTemp 中所有单位
       │      ├─ CustomScriptCode: "local unit au = udg_uChuanXinCi"
       │      ├─ CustomScriptCode: "local player ap = GetOwningPlayer(au)"
       │      ├─ CustomScriptCode: "local integer apIndex=GetConvertedPlayerId(ap)"
       │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uPlayerHeros[apIndex])"
       │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uPlayerHeros[apIndex], true)"
       │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uPlayerHeros[apIndex], true)"
       │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uPlayerHeros[apIndex], true)"
       │      ├─ CustomScriptCode: "local location eLoc=GetUnitLoc(GetEnumUnit())"
       │      ├─ CustomScriptCode: "call DestroyEffect(AddSpecialEffectLoc("Abilities\\Spells\\Undead\\Impale\\Im..."
       │      ├─ CustomScriptCode: "call RemoveLocation(eLoc)"
       │      └─ CustomScriptCode: "call UnitDamageTargetBJ(udg_uPlayerHeros[apIndex],GetEnumUnit(),(0.13*lv*udg_..."
       │    清除点 pTemp
       │    删除单位组 grpTemp
       └─ 否则: (无)
```

</details>

<details id="trigger-06_031_tDaoXuanZXSH">
<summary><strong>📌 tDaoXuanZXSH</strong> <code>06_031_tDaoXuanZXSH</code></summary>

```text
触发器: tDaoXuanZXSH (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tDaoXuanZXSH 到期
条件
  └─ 无
动作
  ├─ CustomScriptCode: "local real x"
  ├─ CustomScriptCode: "local real y"
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位有魔法效果(uDaoXuanZXSH[0], B01Q) == TRUE
       │    ├─ 单位存活判断(uDaoXuanZXSH[0]) == TRUE
       ├─ 则
       │    设置 iTemp = 单位自定义值(uDaoXuanZXSH[1])
       │    设置 pTemp = (uDaoXuanZXSH[0]的位置)
       │    CustomScriptCode: "set x = GetLocationX(udg_pTemp)"
       │    CustomScriptCode: "set y = GetLocationY(udg_pTemp)"
       │    循环整数A 1→9
       │      ├─ CustomScriptCode: "call SetUnitPosition(udg_uDaoXuanZXSH[bj_forLoopAIndex], x+150*CosBJ(bj_forLo..."
       │      └─ CustomScriptCode: "call SetUnitFacing(udg_uDaoXuanZXSH[bj_forLoopAIndex],bj_forLoopAIndex*40+3*u..."
       │    清除点 pTemp
       │    设置单位自定义值: uDaoXuanZXSH[1], (iTemp + 1)
       │    如果
       │      ├─ 条件: iTemp OperatorGreater 3000
       │      ├─ 则
       │      │    循环整数A 1→9
       │      │      └─ 移除 uDaoXuanZXSH[循环整数A]
       │      │    暂停计时器 tDaoXuanZXSH
       │      └─ 否则: (无)
       └─ 否则
            循环整数A 1→9
              └─ 移除 uDaoXuanZXSH[循环整数A]
            暂停计时器 tDaoXuanZXSH
```

</details>

<details id="trigger-06_032_tHB50">
<summary><strong>📌 tHB50</strong> <code>06_032_tHB50</code></summary>

```text
触发器: tHB50 (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tHB50 到期
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 命令ID比较(单位当前命令(uHB50), OperatorEqualENE, 字符串转命令ID("monsoon"))
       ├─ 则
       │    设置 pTemp = (uHB50的位置)
       │    设置 grpTemp = 范围内符合条件的单位(1500.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uHB50的所有者)), OperatorEqualENE, true))
       │    单位组: 选取 grpTemp 中所有单位
       │      ├─ CustomScriptCode: "local unit au = udg_uHB50"
       │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(au)"
       │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, au, true)"
       │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, au, true)"
       │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, au, true)"
       │      └─ CustomScriptCode: "call UnitDamageTargetBJ(au,GetEnumUnit(),(0.3*lv)*(ll+mj+zl),ATTACK_TYPE_CHAO..."
       │    清除点 pTemp
       │    删除单位组 grpTemp
       └─ 否则
            暂停计时器 tHB50
            设置 uHB50 = UnitNull
```

</details>

