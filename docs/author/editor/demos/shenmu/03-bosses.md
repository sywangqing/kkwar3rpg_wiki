---
title: 神墓 2.7C — ⚔️ 03 BOSS 与四血卫
category: kk-triggers
slug: shenmu/03-bosses
description: BOSS 系统/血卫系统/觉醒/复活
updated: 2026-06-01
---

# 🏆 神墓 2.7C — ⚔️ 03 BOSS 与四血卫

> BOSS 系统/血卫系统/觉醒/复活

**共 17 个触发器**

## 📑 触发器目录

- [四血卫](#trigger-03_000_四血卫)
- [SMLR](#trigger-03_001_SMLR)
- [FindXueWei](#trigger-03_002_FindXueWei)
- [TPoXuXiXie](#trigger-03_003_TPoXuXiXie)
- [KillPoXu](#trigger-03_004_KillPoXu)
- [NFCJueXing](#trigger-03_005_NFCJueXing)
- [PoXu](#trigger-03_006_PoXu)
- [妖弓](#trigger-03_007_妖弓)
- [binglingyeye](#trigger-03_008_binglingyeye)
- [MuDiMoQi](#trigger-03_009_MuDiMoQi)
- [bingling](#trigger-03_010_bingling)
- [魔帝、千丝](#trigger-03_011_魔帝、千丝)
- [QianSi](#trigger-03_012_QianSi)
- [QianSi2](#trigger-03_013_QianSi2)
- [modi](#trigger-03_014_modi)
- [yaohuang](#trigger-03_015_yaohuang)
- [QianSiDie](#trigger-03_016_QianSiDie)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-03_000_四血卫">
<summary><strong>📌 四血卫</strong> <code>03_000_四血卫</code></summary>

```text
触发器: 四血卫 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-03_001_SMLR">
<summary><strong>📌 SMLR</strong> <code>03_001_SMLR</code></summary>

```text
触发器: SMLR (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(100.00, gg_unit_Hamg_0122)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  └─ 如果
       ├─ 条件: 玩家科技等级(R006, (触发单位()的所有者)) == 1
       ├─ 则
       │    如果
       │      ├─ 条件: iStepXueWei == 0
       │      ├─ 则
       │      │    PanCameraToTimed: 单位X坐标(gg_unit_Hamg_0122), 单位Y坐标(gg_unit_Hamg_0122), 0
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5937", SoundNull, "TRIGSTR_5938", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5941", SoundNull, "TRIGSTR_5942", AddSetToAdd, 0, WaitDontWait
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │    设置无敌: gg_unit_nntg_0064, InvulnerabilityVulnerable
       │      │    设置 iStepXueWei = 1
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ iStepXueWei == 1
       │      │    ├─ bLiuHuang == TRUE
       │      │    ├─ 单位持有物品类型(触发单位(), I04X) == TRUE
       │      ├─ 则
       │      │    关闭触发器 当前触发器()
       │      │    设置 bLiuHuang = true
       │      │    删除物品: 单位携带物品(按类型)(触发单位(), I04X)
       │      │    设置 pTemp = (gg_unit_ubon_0001的位置)
       │      │    循环整数A 1→6
       │      │      └─ CustomScriptCode: "call CreateUnit(Player(7),'nchp',GetLocationX(udg_pTemp)+512*CosBJ(bj_forLoop..."
       │      │    添加技能: gg_unit_ubon_0001, A033
       │      │    清除点 pTemp
       │      │    PanCameraToTimed: 单位X坐标(gg_unit_Hamg_0122), 单位Y坐标(gg_unit_Hamg_0122), 0
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5943", SoundNull, "TRIGSTR_5944", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5950", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5945", SoundNull, "TRIGSTR_5946", AddSetToAdd, 0, WaitDontWait
       │      │    UnitAddItemByIdSwapped: I03E, 触发单位()
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5947", SoundNull, "TRIGSTR_5948", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5949", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5951", SoundNull, "TRIGSTR_5952", AddSetToAdd, 0, WaitDontWait
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │    AddItemToStockBJ: I03E, gg_unit_Hamg_0122, 1, 1
       │      │    开启触发器 gg_trg_FindXueWei
       │      │    设置 iStepXueWei = 2
       │      │    开启触发器 当前触发器()
       │      │    返回
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 0
       │      │    ├─ 单位持有物品类型(触发单位(), I042) == TRUE
       │      │    ├─ 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 随机[1~6] == 1
       │      │      ├─ 则
       │      │      │    SetPlayerTechResearchedSwap: R009, 1, (触发单位()的所有者)
       │      │      │    添加 grpBanShenFaZe → 触发单位()
       │      │      │    CinematicFadeBJ: FadeTypeOptionFadeOutIn, 10.00, CineFilterTextureWhite, 100.00, 0, 0, 0
       │      │      │    显示文本→(触发单位()的所有者): 0
       │      │      │    设置 iTemp = 玩家号((触发单位()的所有者))
       │      │      │    设置单位颜色: uPlayerHeros[iTemp], iFaZeColor[((iTemp x 1) - 3)], iFaZeColor[((iTemp x 4) - 2)], iFaZeColor[((iTemp x 4) - 1)], iFaZeColor[(iTemp x 4)]
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_4030", SoundNull, (单位名:触发单位()) + "经过生与死的徘徊领悟了半神法则！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_4031", SoundNull, (单位名:触发单位()) + "获得半神怒焰！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_4032", SoundNull, (单位名:触发单位()) + "获得审判降临！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_4033", SoundNull, (单位名:触发单位()) + "获得湮灭雷电！", AddSetToAdd, 0, WaitDontWait
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │      │    QuestSetCompletedBJ: quests[4], CompletionOptionCompleted
       │      │      └─ 否则
       │      │           杀死 触发单位()
       │      │           移动物品到坐标: 单位携带物品(按类型)(触发单位(), I042), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │      │           ForceClear: grpPlayerGroupTemp
       │      │           ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │           TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_Hamg_0122, "TRIGSTR_133", SoundNull, "TRIGSTR_4027", AddSetToAdd, 0, WaitDontWait
       │      └─ 否则: (无)
       └─ 否则
            杀死 触发单位()
            ForceClear: grpPlayerGroupTemp
            ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
            TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_5939", SoundNull, "TRIGSTR_5940", AddSetToAdd, 0, WaitDontWait
```

</details>

<details id="trigger-03_002_FindXueWei">
<summary><strong>📌 FindXueWei</strong> <code>03_002_FindXueWei</code></summary>

```text
触发器: FindXueWei (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00M_0083)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位持有物品类型(触发单位(), I03E) == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ 显示单位: gg_unit_N00M_0083
  ├─ 显示单位: gg_unit_N00E_0104
  ├─ 显示单位: gg_unit_N00F_0106
  ├─ 显示单位: gg_unit_N00G_0105
  ├─ 设置 lgtXueWei[1] = 创建闪电效果(LightningTypeDRAL, AllowDontDont, 单位X坐标(gg_unit_N00E_0104), 单位Y坐标(gg_unit_N00E_0104), 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083))
  ├─ 设置 lgtXueWei[2] = 创建闪电效果(LightningTypeDRAL, AllowDontDont, 单位X坐标(gg_unit_N00F_0106), 单位Y坐标(gg_unit_N00F_0106), 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083))
  ├─ 设置 lgtXueWei[3] = 创建闪电效果(LightningTypeDRAL, AllowDontDont, 单位X坐标(gg_unit_N00G_0105), 单位Y坐标(gg_unit_N00G_0105), 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083))
  ├─ 开启触发器 gg_trg_TPoXuXiXie
  ├─ 开启触发器 gg_trg_KillPoXu
  ├─ 运行计时器 tPoXuXiXue (循环, 0.10s)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_5967", SoundNull, "TRIGSTR_5968", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5965", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5971", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_4044", SoundNull, "TRIGSTR_4045", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ SetUnitOwner: gg_unit_N00M_0083, 玩家9(灰), 改变颜色
  └─ 设置 iStepXueWei = (iStepXueWei + 1)
```

</details>

<details id="trigger-03_003_TPoXuXiXie">
<summary><strong>📌 TPoXuXiXie</strong> <code>03_003_TPoXuXiXie</code></summary>

```text
触发器: TPoXuXiXie (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tPoXuXiXue 到期
条件
  └─ 无
动作
  ├─ MoveLightningEx: lgtXueWei[1], AllowDontDont, 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083), 0, 单位X坐标(gg_unit_N00E_0104), 单位Y坐标(gg_unit_N00E_0104), 0
  ├─ MoveLightningEx: lgtXueWei[2], AllowDontDont, 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083), 0, 单位X坐标(gg_unit_N00F_0106), 单位Y坐标(gg_unit_N00F_0106), 0
  └─ MoveLightningEx: lgtXueWei[3], AllowDontDont, 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083), 0, 单位X坐标(gg_unit_N00G_0105), 单位Y坐标(gg_unit_N00G_0105), 0
```

</details>

<details id="trigger-03_004_KillPoXu">
<summary><strong>📌 KillPoXu</strong> <code>03_004_KillPoXu</code></summary>

```text
触发器: KillPoXu (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_N00M_0083 - 单位死亡
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 暂停计时器 tPoXuXiXue
  ├─ DestroyLightningBJ: lgtXueWei[1]
  ├─ DestroyLightningBJ: lgtXueWei[2]
  ├─ DestroyLightningBJ: lgtXueWei[3]
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00M_0083), 单位Y坐标(gg_unit_N00M_0083), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_5972", SoundNull, "TRIGSTR_5973", AddSetToAdd, 0, WaitDontWait
  ├─ 复活英雄: gg_unit_N00M_0083, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), ShowHideShow
  ├─ 设置单位朝向: gg_unit_N00M_0083, 270.00
  ├─ SetUnitOwner: gg_unit_N00M_0083, 非玩家, 改变颜色
  ├─ 设置 iLvPoXu = (LVCurrent + 10)
  ├─ 如果
  │    ├─ 条件: iLvPoXu OperatorGreater 35
  │    ├─ 则
  │    │    设置 iLvPoXu = 35
  │    └─ 否则: (无)
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5974", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00G_0105, "TRIGSTR_5978", SoundNull, "TRIGSTR_5979", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00G_0105, "TRIGSTR_5981", SoundNull, "TRIGSTR_5982", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ SetUnitOwner: gg_unit_N00G_0105, 玩家7(绿), 改变颜色
  ├─ 开启触发器 gg_trg_NFCJueXing
  ├─ 设置 pTemp = Location((单位X坐标(gg_unit_ubon_0001) + 500.00), 单位Y坐标(gg_unit_ubon_0001))
  ├─ 移动单位: gg_unit_N00E_0104, pTemp
  ├─ SetUnitOwner: gg_unit_N00E_0104, 玩家7(绿), 改变颜色
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = Location((单位X坐标(gg_unit_ubon_0001) - 500.00), 单位Y坐标(gg_unit_ubon_0001))
  ├─ 移动单位: gg_unit_N00F_0106, pTemp
  ├─ SetUnitOwner: gg_unit_N00F_0106, 玩家7(绿), 改变颜色
  ├─ 清除点 pTemp
  ├─ UnitAddAbilityBJ: AInv, gg_unit_N006_0102
  ├─ 修改 gg_unit_N006_0102 的HeroStatStr: ModifyMethodAdd40000
  ├─ 修改 gg_unit_N006_0102 的HeroStatAgi: ModifyMethodAdd40000
  └─ 修改 gg_unit_N006_0102 的HeroStatInt: ModifyMethodAdd40000
```

</details>

<details id="trigger-03_005_NFCJueXing">
<summary><strong>📌 NFCJueXing</strong> <code>03_005_NFCJueXing</code></summary>

```text
触发器: NFCJueXing (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_N00G_0105 - UnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 设置 iTemp = 0
  ├─ 循环整数A 1→6
  │    └─ 如果
  │         ├─ 条件: 物品类型比较(物品类型ID(单位栏位物品(触发单位(), 循环整数A)), OperatorEqualENE, I04W)
  │         ├─ 则
  │         │    设置 iTemp = (iTemp + 1)
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: iTemp == 6
       ├─ 则
       │    销毁触发器(自身)
       │    循环整数A 1→6
       │      └─ 删除物品: 单位栏位物品(触发单位(), 循环整数A)
       │    添加技能: 触发单位(), A091
       │    UnitMakeAbilityPermanent: 触发单位(), OnOffOn, A091
       │    PanCameraToTimed: 单位X坐标(gg_unit_N00G_0105), 单位Y坐标(gg_unit_N00G_0105), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00G_0105, "TRIGSTR_4037", SoundNull, "TRIGSTR_4038", AddSetToAdd, 0, WaitDontWait
       │    UnitAddItemByIdSwapped: I04T, 触发单位()
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    移动单位: gg_unit_N00G_0105, pHG
       │    修改 gg_unit_N006_0102 的HeroStatStr: ModifyMethodAdd40000
       │    修改 gg_unit_N006_0102 的HeroStatAgi: ModifyMethodAdd40000
       │    修改 gg_unit_N006_0102 的HeroStatInt: ModifyMethodAdd40000
       └─ 否则: (无)
```

</details>

<details id="trigger-03_006_PoXu">
<summary><strong>📌 PoXu</strong> <code>03_006_PoXu</code></summary>

```text
触发器: PoXu (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(600.00, gg_unit_N00M_0083)
条件
  ├─ 单位持有物品类型(gg_unit_N00M_0083, I041) == TRUE
  ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 4
  └─ (触发单位()类型ID) == N00H
动作
  ├─ 销毁触发器(自身)
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, 触发单位()
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, gg_unit_N00M_0083
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ 电影模式: OnOffOn, grpOnline
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3973", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3976", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_3974", SoundNull, "TRIGSTR_3975", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3977", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_3978", SoundNull, "TRIGSTR_3979", AddSetToAdd, 0, WaitDontWait
  ├─ 电影模式: OnOffOff, grpOnline
  ├─ UnitRemoveItemFromSlotSwapped: 1, 触发单位()
  ├─ 如果
  │    ├─ 条件: 布尔比较(单位存活判断(触发单位()), OperatorEqualENE, true)
  │    ├─ 则: 给单位物品(触发单位(), 单位携带物品(按类型)(gg_unit_N00M_0083, I041))
  │    └─ 否则: 无动作()
  ├─ PolledWait: 2
  ├─ PauseUnitBJ: PauseUnpauseOptionUnpause, 触发单位()
  └─ PauseUnitBJ: PauseUnpauseOptionUnpause, gg_unit_N00M_0083
```

</details>

<details id="trigger-03_007_妖弓">
<summary><strong>📌 妖弓</strong> <code>03_007_妖弓</code></summary>

```text
触发器: 妖弓 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-03_008_binglingyeye">
<summary><strong>📌 binglingyeye</strong> <code>03_008_binglingyeye</code></summary>

```text
触发器: binglingyeye (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_H002_0094)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepGuanChuan == 0
  │    │    ├─ 单位持有物品类型(触发单位(), I03E) == TRUE
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    显示单位: gg_unit_H002_0094
  │    │    显示单位: gg_unit_N00V_0059
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5904", SoundNull, "TRIGSTR_5905", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5908", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4052", SoundNull, "TRIGSTR_4060", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5909", SoundNull, "TRIGSTR_5910", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    设置 iStepGuanChuan = 3
  │    │    开启触发器 当前触发器()
  │    │    开启触发器 gg_trg_MuDiMoQi
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepGuanChuan == 3
  │    │    ├─ 单位持有物品类型(触发单位(), I033) == TRUE
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    设置 iStepGuanChuan = 4
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I033)
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5928", SoundNull, "TRIGSTR_5929", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4063", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4068", AddSetToAdd, 0, WaitDontWait
  │    │    UnitAddItemByIdSwapped: I042, 触发单位()
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iStepGuanChuan == 4
       │    ├─ 单位持有物品类型(触发单位(), I033) == TRUE
       │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
       ├─ 则
       │    关闭触发器 当前触发器()
       │    设置 iStepGuanChuan = 5
       │    SetUnitAbilityLevelSwapped: AInv, 触发单位(), 2
       │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4050", SoundNull, "TRIGSTR_4051", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4061", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4062", SoundNull, "TRIGSTR_4069", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4070", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    删除物品: 单位携带物品(按类型)(触发单位(), I033)
       │    SetUnitAbilityLevelSwapped: AInv, 触发单位(), 1
       │    SetUnitOwner: gg_unit_H002_0094, PlayerNA, 改变颜色
       │    开启触发器 当前触发器()
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-03_009_MuDiMoQi">
<summary><strong>📌 MuDiMoQi</strong> <code>03_009_MuDiMoQi</code></summary>

```text
触发器: MuDiMoQi (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册游戏时间事件(大于, 1.00)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: iStepGuanChuan OperatorGreaterEq 3
  │    ├─ 则
  │    │    EnumItemsInRectBJMultiple: 可用地图区域()
  │    │    设置 grpTemp = 区域内符合条件的单位(可用地图区域(), 布尔比较(单位持有物品类型(过滤单位(), I01M), OperatorEqualENE, true))
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ 删除物品: 单位携带物品(按类型)(选取单位(), I01M)
  │    │      └─ UnitAddItemByIdSwapped: I033, 选取单位()
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
  ├─ 循环整数A 1→4
  │    ├─ 单位发布命令(立即): uMuDiMoQi[循环整数A], UnitOrderLocustSwarm
  │    └─ 显示单位: uMuDiMoQi[循环整数A]
  ├─ PolledWait: 60.00
  ├─ 循环整数A 1→4
  │    └─ 隐藏单位: uMuDiMoQi[循环整数A]
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iStepGuanChuan OperatorGreaterEq 3
       │    ├─ iStepGuanChuan OperatorLess 6
       ├─ 则
       │    EnumItemsInRectBJMultiple: 可用地图区域()
       │    设置 grpTemp = 区域内符合条件的单位(可用地图区域(), 布尔比较(单位持有物品类型(过滤单位(), I033), OperatorEqualENE, true))
       │    单位组: 选取 grpTemp 中所有单位
       │      ├─ 删除物品: 单位携带物品(按类型)(选取单位(), I033)
       │      └─ UnitAddItemByIdSwapped: I01M, 选取单位()
       │    删除单位组 grpTemp
       └─ 否则: (无)
```

</details>

<details id="trigger-03_010_bingling">
<summary><strong>📌 bingling</strong> <code>03_010_bingling</code></summary>

```text
触发器: bingling (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00V_0059)
条件
  ├─ bJieYuan == TRUE
  ├─ 单位持有物品类型(触发单位(), I05P) == TRUE
  └─ 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
动作
  ├─ 销毁触发器(自身)
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I05P)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00V_0059), 单位Y坐标(gg_unit_N00V_0059), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4066", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00V_0059, "TRIGSTR_4064", SoundNull, "TRIGSTR_4065", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ UnitAddAbilityBJ: S002, 触发单位()
  └─ 杀死 gg_unit_N00V_0059
```

</details>

<details id="trigger-03_011_魔帝、千丝">
<summary><strong>📌 魔帝、千丝</strong> <code>03_011_魔帝、千丝</code></summary>

```text
触发器: 魔帝、千丝 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-03_012_QianSi">
<summary><strong>📌 QianSi</strong> <code>03_012_QianSi</code></summary>

```text
触发器: QianSi (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(250.00, gg_unit_h00I_0057)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  ├─ 单位持有物品类型(触发单位(), I03E) == TRUE
  └─ bHaoJie == 1
动作
  ├─ 关闭触发器 当前触发器()
  ├─ ShowUnit: gg_unit_h00I_0057, ShowHideShow
  ├─ UnitRemoveAbilityBJ: Arel, gg_unit_h00I_0057
  ├─ UnitRemoveAbilityBJ: Apiv, gg_unit_h00I_0057
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_h00I_0057), 单位Y坐标(gg_unit_h00I_0057), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5916", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h00I_0057, "TRIGSTR_5924", SoundNull, "TRIGSTR_5921", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5925", AddSetToAdd, 0, WaitDontWait
  ├─ UnitAddItemByIdSwapped: I03N, 触发单位()
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h00I_0057, "TRIGSTR_5926", SoundNull, "TRIGSTR_5927", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置 iStepQS = 1
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-03_013_QianSi2">
<summary><strong>📌 QianSi2</strong> <code>03_013_QianSi2</code></summary>

```text
触发器: QianSi2 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(150.00, gg_unit_h00I_0057)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位持有物品类型(触发单位(), I05B) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ UnitRemoveAbilityBJ: Awan, gg_unit_h00I_0057
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_h00I_0057), 单位Y坐标(gg_unit_h00I_0057), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3918", AddSetToAdd, 0, WaitDontWait
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(gg_unit_h00I_0057), 单位Y坐标(gg_unit_h00I_0057))
  ├─ 移动单位: gg_unit_h00I_0057, 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137)
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  ├─ 移动单位: 触发单位(), 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137), 0
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_4047", SoundNull, "TRIGSTR_4049", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h00I_0057, "TRIGSTR_5226", SoundNull, "TRIGSTR_5547", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h00I_0057, "TRIGSTR_5784", SoundNull, "TRIGSTR_5883", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_5755", SoundNull, "TRIGSTR_5756", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置 iStepQS = 3
  ├─ 开启触发器 gg_trg_yaohuang
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-03_014_modi">
<summary><strong>📌 modi</strong> <code>03_014_modi</code></summary>

```text
触发器: modi (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(250.00, gg_unit_N013_0137)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位持有物品类型(触发单位(), I03N) == TRUE
  │    │    ├─ iStepQS == 1
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_1061", SoundNull, "TRIGSTR_1063", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1078", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_1138", SoundNull, "TRIGSTR_1944", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    开启触发器 当前触发器()
  │    │    开启触发器 gg_trg_QianSi2
  │    │    设置 iStepQS = 2
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I036)) == TRUE
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02H)) == TRUE
  │    │    ├─ bHaoJie == 1
  │    │    ├─ iStepQS OperatorGreater 3
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I036)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I02H)
  │    │    UnitAddItemByIdSwapped: I03M, 触发单位()
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_4114", SoundNull, "TRIGSTR_4115", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4113", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    开启触发器 当前触发器()
  │    │    设置 bHaoJie = 2
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I054)) == TRUE
  │    │    ├─ iStepQS == 4
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I054)
  │    │    UnitAddAbilityBJ: Arel, gg_unit_h00I_0057
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_906", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_1156", SoundNull, "TRIGSTR_1389", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_1408", SoundNull, "TRIGSTR_1414", AddSetToAdd, 0, WaitDontWait
  │    │    UnitAddItemByIdSwapped: I04P, 触发单位()
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1494", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_1495", SoundNull, "TRIGSTR_1497", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    设置 iStepQS = 5
  │    │    开启触发器 当前触发器()
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位持有物品类型(触发单位(), I05N) == TRUE
       │    ├─ 单位持有物品类型(触发单位(), I05O) == TRUE
       │    ├─ iStepQS == 5
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除物品: 单位携带物品(按类型)(触发单位(), I05N)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I05O)
       │    PanCameraToTimed: 单位X坐标(gg_unit_N013_0137), 单位Y坐标(gg_unit_N013_0137), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_5237", SoundNull, "TRIGSTR_5238", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5236", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_5245", SoundNull, "TRIGSTR_5246", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_5239", SoundNull, "TRIGSTR_5240", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N013_0137, "TRIGSTR_5242", SoundNull, "TRIGSTR_5243", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5244", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    设置 iStepQS = 6
       │    PolledWait: 60.00
       │    UnitRemoveAbilityBJ: Aetl, gg_unit_h00I_0057
       │    UnitAddAbilityBJ: A09S, gg_unit_h00I_0057
       │    开启触发器 当前触发器()
       └─ 否则: (无)
```

</details>

<details id="trigger-03_015_yaohuang">
<summary><strong>📌 yaohuang</strong> <code>03_015_yaohuang</code></summary>

```text
触发器: yaohuang (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(250.00, gg_unit_Ecen_0088)
条件
  ├─ 单位持有物品类型(触发单位(), I03N) == TRUE
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ iStepQS == 3
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I03N)
  ├─ 设置 grpTemp = 玩家指定类型单位(PlayerNA, e001)
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ SetUnitOwner: 选取单位(), (触发单位()的所有者), 改变颜色
  ├─ 删除单位组 grpTemp
  ├─ 复活英雄: gg_unit_Ecen_0088, 区域中心X(gg_rct_______e), 区域中心Y(gg_rct_______e), ShowHideHide
  ├─ SetUnitAbilityLevelSwapped: AEah, gg_unit_Ecen_0088, 1
  ├─ 移除技能: gg_unit_Ecen_0088, 自定义代码("'Amov'")
  ├─ SetHeroLevel: gg_unit_Ecen_0088, 1, ShowHideHide
  ├─ SuspendHeroXPBJ: EnableDisableDisable, gg_unit_Ecen_0088
  ├─ SetUnitOwner: gg_unit_Ecen_0088, 非玩家, 改变颜色
  ├─ ForForceMultiple: grpUserPlayers
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_Ecen_0088), 单位Y坐标(gg_unit_Ecen_0088), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_4999", SoundNull, "TRIGSTR_5181", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5654", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_908", SoundNull, "TRIGSTR_4234", AddSetToAdd, 0, WaitDontWait
  ├─ UnitAddItemByIdSwapped: stel, 触发单位()
  ├─ SetUnitOwner: gg_unit_e001_0009, (触发单位()的所有者), 改变颜色
  ├─ SetUnitOwner: gg_unit_e001_0093, (触发单位()的所有者), 改变颜色
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_5665", SoundNull, "TRIGSTR_5666", AddSetToAdd, 0, WaitDontWait
  ├─ UnitAddItemByIdSwapped: I054, 触发单位()
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置 iStepQS = 4
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-03_016_QianSiDie">
<summary><strong>📌 QianSiDie</strong> <code>03_016_QianSiDie</code></summary>

```text
触发器: QianSiDie (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_h00I_0057 - 单位死亡
条件
  └─ 无
动作
  ├─ 关闭触发器 gg_trg_QianSi
  ├─ 关闭触发器 gg_trg_QianSi2
  ├─ 关闭触发器 gg_trg_modi
  └─ 关闭触发器 gg_trg_yaohuang
```

</details>
