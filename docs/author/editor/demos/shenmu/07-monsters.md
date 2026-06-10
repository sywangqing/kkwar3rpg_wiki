---
title: 神墓 2.7C — 👹 07 刷怪与进攻
category: kk-triggers
slug: shenmu/07-monsters
description: 刷兵/Boss/进攻怪/最终战争
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 👹 07 刷怪与进攻

> 刷兵/Boss/进攻怪/最终战争

**共 16 个触发器**

## 📑 触发器目录

- [初始单位](#trigger-07_000_初始单位)
- [CreateAnimal](#trigger-07_001_CreateAnimal)
- [LianJi](#trigger-07_002_LianJi)
- [Boss](#trigger-07_003_Boss)
- [刷兵](#trigger-07_004_刷兵)
- [JinGongSheZhi](#trigger-07_005_JinGongSheZhi)
- [JinGongGuai](#trigger-07_006_JinGongGuai)
- [JinGongDengDai](#trigger-07_007_JinGongDengDai)
- [JinGongTooMany](#trigger-07_008_JinGongTooMany)
- [MoDiJinGong](#trigger-07_009_MoDiJinGong)
- [特殊怪](#trigger-07_010_特殊怪)
- [TeShuGuai](#trigger-07_011_TeShuGuai)
- [最后的战争](#trigger-07_012_最后的战争)
- [MyGod](#trigger-07_013_MyGod)
- [LastBattle](#trigger-07_014_LastBattle)
- [FuShenMoDiStrength](#trigger-07_015_FuShenMoDiStrength)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-07_000_初始单位">
<summary><strong>📌 初始单位</strong> <code>07_000_初始单位</code></summary>

```text
触发器: 初始单位 (刷怪/进攻) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-07_001_CreateAnimal">
<summary><strong>📌 CreateAnimal</strong> <code>07_001_CreateAnimal</code></summary>

```text
触发器: CreateAnimal (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(2.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─  CreateUnit: PlayerNA, ngrd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  ├─  CreateUnit: PlayerNA, nbzd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  ├─  CreateUnit: PlayerNA, nbwm, 区域中心X(gg_rct_____________2), 区域中心Y(gg_rct_____________2), 180.00
  ├─  CreateUnit: PlayerNA, nadr, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  ├─  CreateUnit: PlayerNA, nrwm, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  ├─  CreateUnit: PlayerNA, nomg, 区域中心X(gg_rct_______u), 区域中心Y(gg_rct_______u), 90.00
  ├─  CreateUnit: PlayerNA, n00O, 区域中心X(gg_rct_______c), 区域中心Y(gg_rct_______c), 270.00
  ├─  CreateUnit: PlayerNA, n014, 区域中心X(gg_rct_______12), 区域中心Y(gg_rct_______12), 270.00
  ├─ 设置 pTemp = (区域gg_rct__________01中心)
  ├─ 创建 10个|nogl|→PlayerNA 在 pTemp 面向270.00
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = (区域gg_rct_____________01中心)
  ├─ 创建 20个|npfl|→PlayerNA 在 pTemp 面向270.00
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = (区域gg_rct_______001中心)
  ├─ 创建 10个|n002|→PlayerNA 在 pTemp 面向270.00
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = (区域gg_rct_______002中心)
  ├─ 创建 10个|n003|→PlayerNA 在 pTemp 面向270.00
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = (区域gg_rct_______003中心)
  ├─ 创建 10个|n004|→PlayerNA 在 pTemp 面向270.00
  └─ 清除点 pTemp
```

</details>

<details id="trigger-07_002_LianJi">
<summary><strong>📌 LianJi</strong> <code>07_002_LianJi</code></summary>

```text
触发器: LianJi (刷怪/进攻) [✓] — 练功房
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(5.00)
条件
  └─ 无
动作
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct__________1, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 25个|uJinGong[LVCurrent]|→PlayerNA 在 pShuaGuai[1] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct__________2, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 25个|uJinGong[LVCurrent]|→PlayerNA 在 pShuaGuai[2] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct__________3, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 25个|uJinGong[(LVCurrent + 1)]|→PlayerNA 在 pShuaGuai[3] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct__________4, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 25个|uJinGong[(LVCurrent + 1)]|→PlayerNA 在 pShuaGuai[4] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______01, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|nenc|→PlayerNA 在 pShuaGuai[5] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______02, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|nenc|→PlayerNA 在 pShuaGuai[6] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______1, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: LVCurrent OperatorLess 20
  │    │      ├─ 则
  │    │      │    创建 20个|nban|→PlayerNA 在 pShuaGuai[7] 面向默认朝向
  │    │      └─ 否则
  │    │           创建 20个|nenc|→PlayerNA 在 pShuaGuai[7] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______2, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: LVCurrent OperatorLess 20
  │    │      ├─ 则
  │    │      │    创建 20个|nban|→PlayerNA 在 pShuaGuai[8] 面向默认朝向
  │    │      └─ 否则
  │    │           创建 20个|nenc|→PlayerNA 在 pShuaGuai[8] 面向默认朝向
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______a, (玩家比较((过滤单位()的所有者), OperatorEqualENE, PlayerNA) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    创建 20个|nenp|→PlayerNA 在 pShuaGuai[9] 面向默认朝向
  │    └─ 否则: (无)
  └─ 删除单位组 grpTemp
```

</details>

<details id="trigger-07_003_Boss">
<summary><strong>📌 Boss</strong> <code>07_003_Boss</code></summary>

```text
触发器: Boss (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 玩家单位 - 单位死亡
  └─ 玩家单位 - 单位死亡
条件
  └─ 无
动作
  ├─ ── 昊天 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H001_0087
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 布尔比较(单位持有物品类型(触发单位(), I02F), OperatorEqualENE, true)
  │    │      ├─ 则: 移动物品到坐标(单位携带物品(按类型)(触发单位(), I02F), 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct_____________a), 区域中心Y(gg_rct_____________a), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 270.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 坑爹boss，加波数 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H00A_0081
  │    ├─ 则
  │    │    循环整数A LVCurrent→35
  │    │      ├─ 设置 uJinGong[循环整数A] = uJinGong[(循环整数A + 1)]
  │    │      ├─ 设置 aJinGongGuai[循环整数A] = aJinGongGuai[(循环整数A + 1)]
  │    │      └─ 设置 aJinGongGuaiHard[循环整数A] = aJinGongGuaiHard[(循环整数A + 1)]
  │    │    PolledWait: 120.00
  │    │    复活英雄: 触发单位(), 单位X坐标(触发单位()), 单位Y坐标(触发单位()), ShowHideShow
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 老头 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H002_0094
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 布尔比较(单位持有物品类型(触发单位(), I03I), OperatorEqualENE, true)
  │    │      ├─ 则: 移动物品到坐标(单位携带物品(按类型)(触发单位(), I03I), 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: iStepGuanChuan == 5
  │    │      ├─ 则
  │    │      │    设置 iStepGuanChuan = 6
  │    │      │    UnitAddItemByIdSwapped: I05P, 凶手单位()
  │    │      │    关闭触发器 gg_trg_MuDiMoQi
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4077", SoundNull, "TRIGSTR_4078", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_4079", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00V_0059, "TRIGSTR_4080", SoundNull, "TRIGSTR_4081", AddSetToAdd, 0, WaitDontWait
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │      │    开启触发器 gg_trg_JieYuan
  │    │      └─ 否则: (无)
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct_____________00000000), 区域中心Y(gg_rct_____________00000000), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 270.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 妖皇 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_Ecen_0088
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: bHaoJie == 0
  │    │      ├─ 则
  │    │      │    创建物品(指定坐标): I036, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    设置 bHaoJie = 1
  │    │      │    创建物品(指定坐标): I02H, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3949", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_3950", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3987", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hamg_0122, "TRIGSTR_3988", SoundNull, "TRIGSTR_3999", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4000", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4085", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4086", AddSetToAdd, 0, WaitDontWait
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │      │    设置无敌: gg_unit_unp2_0034, InvulnerabilityVulnerable
  │    │      │    PolledWait: 60.00
  │    │      │    复活英雄: 触发单位(), 区域中心X(gg_rct_______e), 区域中心Y(gg_rct_______e), ShowHideShow
  │    │      │    SetUnitAbilityLevelSwapped: AEah, 触发单位(), 2
  │    │      │    设置单位朝向: 触发单位(), 270.00
  │    │      │    返回
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~10], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I055, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    创建物品(指定坐标): I02H, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct_______e), 区域中心Y(gg_rct_______e), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 270.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 舞九天 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H00B_0032
  │    ├─ 则
  │    │    创建物品(指定坐标): I04W, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct__________f), 区域中心Y(gg_rct__________f), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 90.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 虎哥 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_N00X_0031
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: bHuGe == TRUE
  │    │      ├─ 则
  │    │      │    创建物品(指定坐标): rhth, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    设置 bHuGe = true
  │    │      └─ 否则: (无)
  │    │    设置 iTemp = 随机[0~5]
  │    │    创建物品(指定坐标): 自定义代码("'I000'+udg_iTemp*256+GetRandomInt(0,255)"), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │    设置 itemTemp = 最后创建的物品()
  │    │    如果
  │    │      ├─ 条件: 布尔比较(是消耗品(itemTemp), OperatorEqualENE, true)
  │    │      ├─ 则: 删除物品(itemTemp)
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct______________060), 区域中心Y(gg_rct______________060), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 90.00
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 玄武封印 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_nmrr_0068
  │    ├─ 则
  │    │    PolledWait: 10.00
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Hmkg_0067, (单位名:gg_unit_Hmkg_0067), SoundNull, "TRIGSTR_2994", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    SetUnitOwner: gg_unit_Hmkg_0067, PlayerNA, 改变颜色
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 玄武 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_Hmkg_0067
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: bXuanWu == TRUE
  │    │      ├─ 则
  │    │      │    创建物品(指定坐标): kpin, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    设置水面颜色: 255, 255, 255, 255
  │    │      │    设置 bXuanWu = true
  │    │      └─ 否则: (无)
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct_______011), 区域中心Y(gg_rct_______011), ShowHideShow
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 小啊 ──
  └─ 如果
       ├─ 条件: 触发单位() == gg_unit_U001_0127
       ├─ 则
       │    如果
       │      ├─ 条件: 整数比较(随机[1~3], ==, 1)
       │      ├─ 则: 创建物品(指定坐标)(I01T, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
       │      └─ 否则: 无动作()
       │    如果
       │      ├─ 条件: 整数比较(随机[1~3], ==, 1)
       │      ├─ 则: 创建物品(指定坐标)(I01Q, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
       │      └─ 否则: 无动作()
       │    PolledWait: 60.00
       │    复活英雄: 触发单位(), 区域中心X(gg_rct_______004), 区域中心Y(gg_rct_______004), ShowHideShow
       │    设置单位朝向: 触发单位(), 90.00
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-07_004_刷兵">
<summary><strong>📌 刷兵</strong> <code>07_004_刷兵</code></summary>

```text
触发器: 刷兵 (刷怪/进攻) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-07_005_JinGongSheZhi">
<summary><strong>📌 JinGongSheZhi</strong> <code>07_005_JinGongSheZhi</code></summary>

```text
触发器: JinGongSheZhi (刷怪/进攻) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 tNextWave 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 dNextWave
  ├─ 运行计时器 tWait (一次性, 99.00s)
  ├─ 计时器窗口: tWait 标题="第" + (LVCurrent转字符串) + "波敌人"
  ├─ 设置 dNextWave = 最后创建的计时器窗口()
  ├─ 开启触发器 gg_trg_JinGongGuai
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 任一成立
  │    │    ├─ bTeShu == TRUE
  │    ├─ 则
  │    │    显示文本→grpOnline: "TRIGSTR_3946"
  │    │    开启触发器 gg_trg_TeShuGuai
  │    └─ 否则: (无)
  ├─ 循环整数A 1→7: 调整玩家资源((LVCurrent + 1), 玩家循环整数A(), PlayerStateLumber)
  ├─ 循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_1130")
  ├─ 设置 grpTemp = 玩家符合条件的单位(玩家9(灰), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false))
  ├─ 单位组: 选取 grpTemp 中所有单位
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) OperatorGreaterEq 240
  │    ├─ 则
  │    │    显示文本→grpOnline: "TRIGSTR_937"
  │    │    开启触发器 gg_trg_JinGongTooMany
  │    │    运行计时器 tTooMany (一次性, 60.00s)
  │    │    计时器窗口: tTooMany 标题="TRIGSTR_6687"
  │    │    设置 dTooMany = 最后创建的计时器窗口()
  │    └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  ├─ 如果
  │    ├─ 条件: bXianFeng == TRUE
  │    ├─ 则
  │    │    显示文本→grpOnline: "TRIGSTR_1903"
  │    │    设置 pTemp = (区域gg_rct__________d中心)
  │    │    循环整数A 1→4
  │    │      ├─ 如果
  │    │      │    ├─ 条件: 布尔比较(单位死亡判断(uXianFeng[循环整数A()]), OperatorEqualENE, true)
  │    │      │    ├─ 则: 复活英雄(点)(uXianFeng[循环整数A()], pTemp, ShowHideHide)
  │    │      │    └─ 否则: 无动作()
  │    │      ├─ SetHeroLevel: uXianFeng[循环整数A()], (英雄等级(uXianFeng[循环整数A()]) + 10), ShowHideHide
  │    │      ├─ 修改 uXianFeng[循环整数A()] 的HeroStatStr: ModifyMethodAdd((玩家科技等级(Rhme, 玩家9(灰)) x LVCurrent) x 500)
  │    │      ├─ 修改 uXianFeng[循环整数A()] 的HeroStatAgi: ModifyMethodAdd((玩家科技等级(Rhme, 玩家9(灰)) x LVCurrent) x 35)
  │    │      ├─ 修改 uXianFeng[循环整数A()] 的HeroStatInt: ModifyMethodAdd((玩家科技等级(Rhme, 玩家9(灰)) x LVCurrent) x 50)
  │    │      └─ 命令 uXianFeng[循环整数A()] → UnitOrderAttack 到 pHG
  │    │    清除点 pTemp
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ LVCurrent == iLvPoXu
  │    │    ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 4
  │    ├─ 则
  │    │    电影模式: OnOffOn, grpOnline
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_5893", SoundNull, "TRIGSTR_5894", AddSetToAdd, 0, WaitDontWait
  │    │    电影模式: OnOffOff, grpOnline
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5898")
  │    │    开启触发器 gg_trg_PoXu
  │    │    SetUnitPathing: gg_unit_N00M_0083, PathingOff
  │    │    给单位物品: gg_unit_N00M_0083, 单位携带物品(按类型)(gg_unit_Uclc_0123, I041)
  │    │    SetUnitOwner: gg_unit_N00M_0083, 玩家9(灰), 改变颜色
  │    │    IssuePointOrderByIdLoc: gg_unit_N00M_0083, OrderCodeAttack, pHG
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LVCurrent == 12
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家9(灰), Hvsh, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5638")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LVCurrent == 19
  │    ├─ 则
  │    │    设置 uTemp = 创建单位(指定坐标)(玩家9(灰), Hkal, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    命令 uTemp → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    添加事件到 gg_trg_diyouyoubf: 注册单位事件(uTemp, 单位死亡)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5656")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LVCurrent == 27
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家9(灰), Eevi, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5658")
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: LVCurrent == 35
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除计时器 tWait
       │    删除计时器 tNextWave
       │    关闭触发器 gg_trg_JinGongDengDai
       │    等待 150.00s
       │    关闭触发器 gg_trg_JinGongGuai
       │    电影模式: OnOffOn, grpOnline
       │    TransmissionFromUnitTypeWithNameBJ: grpOnline, 玩家9(灰), Nkjx, "TRIGSTR_3941", pShuaGuai[44], SoundNull, "TRIGSTR_3942", AddSetToAdd, 0, WaitDontWait
       │    电影模式: OnOffOff, grpOnline
       │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_6586")
       │    命令 创建单位(指定坐标)(玩家9(灰), Nkjx, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
       └─ 否则: (无)
```

</details>

<details id="trigger-07_006_JinGongGuai">
<summary><strong>📌 JinGongGuai</strong> <code>07_006_JinGongGuai</code></summary>

```text
触发器: JinGongGuai (刷怪/进攻) [✓] — 刷怪
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(3.00)
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________001), 区域中心Y(gg_rct__________001), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________002), 区域中心Y(gg_rct__________002), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________003), 区域中心Y(gg_rct__________003), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  └─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________004), 区域中心Y(gg_rct__________004), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
```

</details>

<details id="trigger-07_007_JinGongDengDai">
<summary><strong>📌 JinGongDengDai</strong> <code>07_007_JinGongDengDai</code></summary>

```text
触发器: JinGongDengDai (刷怪/进攻) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 计时器 tWait 到期
条件
  └─ 无
动作
  ├─ 运行计时器 tNextWave (一次性, 45.00s)
  ├─ 删除计时器窗口 dNextWave
  ├─ 计时器窗口: tNextWave 标题="第" + ((LVCurrent + 1)转字符串) + "波敌人即将到来"
  ├─ 设置 dNextWave = 最后创建的计时器窗口()
  ├─ 关闭触发器 gg_trg_JinGongGuai
  ├─ 关闭触发器 gg_trg_TeShuGuai
  └─ 设置 LVCurrent = (LVCurrent + 1)
```

</details>

<details id="trigger-07_008_JinGongTooMany">
<summary><strong>📌 JinGongTooMany</strong> <code>07_008_JinGongTooMany</code></summary>

```text
触发器: JinGongTooMany (刷怪/进攻) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 tTooMany 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 dTooMany
  ├─ 设置 grpTemp = 玩家符合条件的单位(玩家9(灰), (布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) OperatorGreaterEq 100
  │    ├─ 则
  │    │    循环整数A 1→7: 宣布失败(玩家循环整数A(), "TRIGSTR_1117")
  │    └─ 否则
  │         关闭触发器 当前触发器()
  └─ 删除单位组 grpTemp
```

</details>

<details id="trigger-07_009_MoDiJinGong">
<summary><strong>📌 MoDiJinGong</strong> <code>07_009_MoDiJinGong</code></summary>

```text
触发器: MoDiJinGong (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(10.00)
条件
  └─ 无
动作
  ├─ 设置 grpTemp = 区域内符合条件的单位(可用地图区域(), (玩家比较((过滤单位()的所有者), OperatorEqualENE, 玩家9(灰)) 且 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true)))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ 命令 选取单位() → UnitOrderAttack 到 pHG
  └─ 删除单位组 grpTemp
```

</details>

<details id="trigger-07_010_特殊怪">
<summary><strong>📌 特殊怪</strong> <code>07_010_特殊怪</code></summary>

```text
触发器: 特殊怪 (刷怪/进攻) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-07_011_TeShuGuai">
<summary><strong>📌 TeShuGuai</strong> <code>07_011_TeShuGuai</code></summary>

```text
触发器: TeShuGuai (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(4.00)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: LVCurrent == 13
  │    ├─ 则
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[1], pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[1], pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LVCurrent == 18
  │    ├─ 则
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[2], pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[2], pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: LVCurrent == 23
  │    ├─ 则
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[3], pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
  │    │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[3], pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: LVCurrent == 28
       ├─ 则
       │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[4], pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
       │    命令 创建单位(指定点)(玩家9(灰), uTeShuGuai[4], pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-07_012_最后的战争">
<summary><strong>📌 最后的战争</strong> <code>07_012_最后的战争</code></summary>

```text
触发器: 最后的战争 (刷怪/进攻) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-07_013_MyGod">
<summary><strong>📌 MyGod</strong> <code>07_013_MyGod</code></summary>

```text
触发器: MyGod (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品比较(被操作物品(), OperatorEqualENE, itemTSXJ)
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 玩家在玩家组中((触发单位()的所有者), grpOnline) == TRUE
       │    ├─ 玩家组玩家数(grpOnline) OperatorGreaterEq 4
       │    ├─ 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
       │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) OperatorGreaterEq 1
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除物品: itemTSXJ
       │    关闭触发器 gg_trg_tTianShuXiaJuan
       │    设置无敌: gg_unit_ubon_0001, InvulnerabilityInvulnerable
       │    隐藏单位: 触发单位()
       │    设置 uFuShenMoDi = 创建单位(指定坐标)((触发单位()的所有者), U002, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
       │    添加事件到 gg_trg_UnBlinkableFushen: 注册单位进入范围事件(600.00, uFuShenMoDi)
       │    开启触发器 gg_trg_UnBlinkableFushen
       │    移除技能: uFuShenMoDi, AInv
       │    设置 uPlayerHeros[玩家号((触发单位()的所有者))] = uFuShenMoDi
       │    SetUnitOwner: 触发单位(), 非玩家, 改变颜色
       │    如果
       │      ├─ 条件: 触发单位() == uChiYanHuoJingLing[0]
       │      ├─ 则
       │      │    循环整数A 1→5
       │      │      ├─ 隐藏单位: uChiYanHuoJingLing[循环整数A]
       │      │      └─ SetUnitOwner: uChiYanHuoJingLing[循环整数A], 非玩家, 改变颜色
       │      └─ 否则: (无)
       │    设置无敌: uFuShenMoDi, InvulnerabilityInvulnerable
       │    PauseUnit: uFuShenMoDi, PauseUnpauseOptionPause
       │    SetPlayerTechResearchedSwap: Rhme, 100, (uFuShenMoDi的所有者)
       │    SetPlayerTechResearchedSwap: Rhar, 100, (uFuShenMoDi的所有者)
       │    SetPlayerTechResearchedSwap: R004, 100, (uFuShenMoDi的所有者)
       │    SetPlayerTechResearchedSwap: R003, 100, (uFuShenMoDi的所有者)
       │    SetPlayerTechResearchedSwap: Rhme, 100, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: Rhar, 100, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: R004, 100, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: R003, 100, 玩家9(灰)
       │    SetPlayerAllianceStateBJ: (uFuShenMoDi的所有者), 玩家9(灰), AllianceSettingAlliedVision
       │    SetPlayerAllianceStateBJ: 玩家9(灰), (uFuShenMoDi的所有者), AllianceSettingAlliedAdvUnits
       │    SetPlayerAllianceStateBJ: (uFuShenMoDi的所有者), PlayerNA, AllianceSettingAlliedVision
       │    SetPlayerAllianceStateBJ: PlayerNA, (uFuShenMoDi的所有者), AllianceSettingAlliedAdvUnits
       │    SetPlayerAllianceStateBJ: 玩家7(绿), (uFuShenMoDi的所有者), AllianceSettingUnallied
       │    SetPlayerAllianceStateBJ: 玩家8(粉), (uFuShenMoDi的所有者), AllianceSettingUnallied
       │    SetPlayerAllianceStateBJ: (uFuShenMoDi的所有者), 玩家7(绿), AllianceSettingUnallied
       │    SetPlayerAllianceStateBJ: (uFuShenMoDi的所有者), 玩家8(粉), AllianceSettingUnallied
       │    设置技能等级: uFuShenMoDi, A09M, 10
       │    设置 pTemp = (uFuShenMoDi的位置)
       │    PanCameraToTimed: 单位X坐标(uFuShenMoDi), 单位Y坐标(uFuShenMoDi), 0
       │    电影模式: OnOffOn, grpOnline
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, uFuShenMoDi, "TRIGSTR_2671", SoundNull, "TRIGSTR_2667", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, uFuShenMoDi, "TRIGSTR_4291", SoundNull, "TRIGSTR_4292", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, gg_unit_Hamg_0122, "TRIGSTR_4296", SoundNull, "TRIGSTR_4297", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, uFuShenMoDi, "TRIGSTR_4311", SoundNull, "TRIGSTR_4312", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, gg_unit_Hamg_0122, "TRIGSTR_4313", SoundNull, "TRIGSTR_4314", AddSetToAdd, 0, WaitDontWait
       │    电影模式: OnOffOff, grpOnline
       │    添加技能: gg_unit_ubon_0001, A03M
       │    添加技能: gg_unit_ubon_0001, A05Q
       │    添加技能: gg_unit_ubon_0001, A05W
       │    设置技能等级: gg_unit_ubon_0001, A05W, 2
       │    设置无敌: gg_unit_ubon_0001, InvulnerabilityVulnerable
       │    PolledWait: 2
       │    关闭触发器 gg_trg_JinGongSheZhi
       │    关闭触发器 gg_trg_JinGongGuai
       │    关闭触发器 gg_trg_JinGongDengDai
       │    关闭触发器 gg_trg_JinGongTooMany
       │    暂停计时器 tWait
       │    暂停计时器 tTooMany
       │    暂停计时器 tNextWave
       │    ForceRemovePlayer: grpOnline, (uFuShenMoDi的所有者)
       │    ForForceMultiple: grpOnline
       │    开启触发器 gg_trg_FuShenMoDiStrength
       │    开启触发器 gg_trg_LastBattle
       │    UnitAddAbilityBJ: Aloc, uFuShenMoDi
       │    移除技能: uFuShenMoDi, Aloc
       │    设置无敌: uFuShenMoDi, InvulnerabilityVulnerable
       │    PauseUnit: uFuShenMoDi, PauseUnpauseOptionUnpause
       │    CustomScriptCode: "call SetPlayerState(GetOwningPlayer(udg_uFuShenMoDi),PLAYER_STATE_OBSERVER,1)"
       │    命令 uFuShenMoDi → UnitOrderAttack 到 pHG
       └─ 否则
            移动物品到坐标: 被操作物品(), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
```

</details>

<details id="trigger-07_014_LastBattle">
<summary><strong>📌 LastBattle</strong> <code>07_014_LastBattle</code></summary>

```text
触发器: LastBattle (刷怪/进攻) [✓] — 刷怪
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(3.00)
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定坐标)((uFuShenMoDi的所有者), uJinGong[随机[26~35]], 区域中心X(gg_rct__________001), 区域中心Y(gg_rct__________001), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)((uFuShenMoDi的所有者), uJinGong[随机[26~35]], 区域中心X(gg_rct__________002), 区域中心Y(gg_rct__________002), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)((uFuShenMoDi的所有者), uJinGong[随机[26~35]], 区域中心X(gg_rct__________003), 区域中心Y(gg_rct__________003), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)((uFuShenMoDi的所有者), uJinGong[随机[26~35]], 区域中心X(gg_rct__________004), 区域中心Y(gg_rct__________004), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定点)((uFuShenMoDi的所有者), H00D, pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
  └─ 命令 创建单位(指定点)((uFuShenMoDi的所有者), H00D, pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
```

</details>

<details id="trigger-07_015_FuShenMoDiStrength">
<summary><strong>📌 FuShenMoDiStrength</strong> <code>07_015_FuShenMoDiStrength</code></summary>

```text
触发器: FuShenMoDiStrength (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(0.20)
条件
  └─ uFuShenMoDi == UnitNull
动作
  ├─ 修改 uFuShenMoDi 的HeroStatStr: ModifyMethodAdd10000
  ├─ 修改 uFuShenMoDi 的HeroStatAgi: ModifyMethodAdd10000
  ├─ 修改 uFuShenMoDi 的HeroStatInt: ModifyMethodAdd10000
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_____________0000, 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    ├─ 销毁特效 创建特效(附着单位)(Abilities\Spells\Human\HolyBolt\HolyBoltSpecialArt.mdl, 选取单位(), "overhead")
  │    ├─ 修改 选取单位() 的HeroStatStr: ModifyMethodAdd500
  │    ├─ 修改 选取单位() 的HeroStatAgi: ModifyMethodAdd500
  │    └─ 修改 选取单位() 的HeroStatInt: ModifyMethodAdd500
  └─ 删除单位组 grpTemp
```

</details>

