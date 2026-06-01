---
title: 神墓 2.7C — 📖 02 剧情与对白
category: kk-triggers
slug: shenmu/02-story
description: NPC对白/任务对话/剧情演出
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 📖 02 剧情与对白

> NPC对白/任务对话/剧情演出

**共 31 个触发器**

## 📑 触发器目录

- [熊猫军团](#trigger-02_000_熊猫军团)
- [xiaoxiongmao](#trigger-02_001_xiaoxiongmao)
- [xiaoxiaoxiongmao](#trigger-02_002_xiaoxiaoxiongmao)
- [sanqing](#trigger-02_003_sanqing)
- [xiongmao](#trigger-02_004_xiongmao)
- [其他剧情](#trigger-02_005_其他剧情)
- [shangshandalaohu](#trigger-02_006_shangshandalaohu)
- [mi](#trigger-02_007_mi)
- [yuanguzhishustart](#trigger-02_008_yuanguzhishustart)
- [yuanguzhishu](#trigger-02_009_yuanguzhishu)
- [PanNiu](#trigger-02_010_PanNiu)
- [XiaoPanNiu](#trigger-02_011_XiaoPanNiu)
- [杀戮者](#trigger-02_012_杀戮者)
- [JieYuan](#trigger-02_013_JieYuan)
- [ShaLuZheMove](#trigger-02_014_ShaLuZheMove)
- [主线剧情](#trigger-02_015_主线剧情)
- [juetian](#trigger-02_016_juetian)
- [xuanyuan](#trigger-02_017_xuanyuan)
- [linghunshashou](#trigger-02_018_linghunshashou)
- [diyouyoubf](#trigger-02_019_diyouyoubf)
- [diyouyoustart](#trigger-02_020_diyouyoustart)
- [diyouyoudie](#trigger-02_021_diyouyoudie)
- [传说](#trigger-02_022_传说)
- [wumingmubei](#trigger-02_023_wumingmubei)
- [yinshuang](#trigger-02_024_yinshuang)
- [haotian](#trigger-02_025_haotian)
- [xinzang](#trigger-02_026_xinzang)
- [上山打老虎](#trigger-02_027_上山打老虎)
- [KillAllDistrutable](#trigger-02_028_KillAllDistrutable)
- [妖灵专属](#trigger-02_029_妖灵专属)
- [xiongci](#trigger-02_030_xiongci)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-02_000_熊猫军团">
<summary><strong>📌 熊猫军团</strong> <code>02_000_熊猫军团</code></summary>

```text
触发器: 熊猫军团 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_001_xiaoxiongmao">
<summary><strong>📌 xiaoxiongmao</strong> <code>02_001_xiaoxiongmao</code></summary>

```text
触发器: xiaoxiongmao (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_npn1_0119)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位持有物品类型(触发单位(), I037) == TRUE
       │    ├─ 物品剩余使用次数(单位携带物品(按类型)(触发单位(), I037)) OperatorGreater 0
       ├─ 则
       │    如果
       │      ├─ 条件: 单位持有物品类型(触发单位(), I038) == TRUE
       │      ├─ 则
       │      │    设置 itemTemp = 单位携带物品(按类型)(触发单位(), I037)
       │      │    SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) - 1)
       │      │    如果
       │      │      ├─ 条件: 随机[1~3] == 1
       │      │      ├─ 则
       │      │      │    显示文本→(触发单位()的所有者): 0
       │      │      │    UnitAddItemByIdSwapped: I038, 触发单位()
       │      │      └─ 否则
       │      │           显示文本→(触发单位()的所有者): 0
       │      └─ 否则
       │           设置 itemTemp = 单位携带物品(按类型)(触发单位(), I037)
       │           SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) - 1)
       │           如果
       │             ├─ 条件: 随机[1~100] == 1
       │             ├─ 则
       │             │    UnitAddItemByIdSwapped: desc, 触发单位()
       │             └─ 否则: (无)
       └─ 否则
            显示文本→(触发单位()的所有者): 0
```

</details>

<details id="trigger-02_002_xiaoxiaoxiongmao">
<summary><strong>📌 xiaoxiaoxiongmao</strong> <code>02_002_xiaoxiaoxiongmao</code></summary>

```text
触发器: xiaoxiaoxiongmao (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_npn3_0120)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 单位持有物品类型(触发单位(), I04S) == TRUE
  │    │    ├─ 物品剩余使用次数(单位携带物品(按类型)(触发单位(), I039)) OperatorGreaterEq 33
  │    ├─ 则
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I039)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I04S)
  │    │    UnitAddItemByIdSwapped: I04R, 触发单位()
  │    │    设置 uTianShuXiaJuan = 触发单位()
  │    │    设置 itemTSXJ = 最后创建的物品()
  │    │    运行计时器 tTianShuXiaJuan (循环, 0.10s)
  │    │    AddLightningLoc: LightningTypeDRAL, pHG, pHG
  │    │    设置 lightTSXJ = 最后创建的闪电效果()
  │    │    显示文本→(触发单位()的所有者): 0
  │    └─ 否则: (无)
  ├─ 设置 itemTemp = 单位携带物品(按类型)(触发单位(), I039)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(itemTemp), OperatorEqualENE, I039)
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 物品剩余使用次数(itemTemp) OperatorGreater 10
  │    │      ├─ 则
  │    │      │    SetHeroLevel: 触发单位(), (英雄等级(触发单位()) + 10), ShowHideHide
  │    │      │    显示文本→(触发单位()的所有者): 0
  │    │      │    SetItemCharges: itemTemp, (物品剩余使用次数(itemTemp) - 10)
  │    │      └─ 否则
  │    │           SetHeroLevel: 触发单位(), (英雄等级(触发单位()) + 物品剩余使用次数(itemTemp)), ShowHideHide
  │    │           显示文本→(触发单位()的所有者): 0
  │    │           删除物品: itemTemp
  │    └─ 否则
  │         显示文本→(触发单位()的所有者): 0
  └─ 设置 itemTemp = ItemNull
```

</details>

<details id="trigger-02_003_sanqing">
<summary><strong>📌 sanqing</strong> <code>02_003_sanqing</code></summary>

```text
触发器: sanqing (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_n00A_0163)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 循环整数A 1→14
       └─ 如果
            ├─ 条件: (触发单位()类型ID) == uHeroType[循环整数A()]
            ├─ 则
            │    显示文本→(触发单位()的所有者): 0
            │    返回
            └─ 否则: (无)
```

</details>

<details id="trigger-02_004_xiongmao">
<summary><strong>📌 xiongmao</strong> <code>02_004_xiongmao</code></summary>

```text
触发器: xiongmao (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_npn2_0110)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 循环整数A 1→14
       └─ 如果
            ├─ 条件: (触发单位()类型ID) == uHeroType[循环整数A()]
            ├─ 则
            │    显示文本→(触发单位()的所有者): 0
            │    返回
            └─ 否则: (无)
```

</details>

<details id="trigger-02_005_其他剧情">
<summary><strong>📌 其他剧情</strong> <code>02_005_其他剧情</code></summary>

```text
触发器: 其他剧情 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_006_shangshandalaohu">
<summary><strong>📌 shangshandalaohu</strong> <code>02_006_shangshandalaohu</code></summary>

```text
触发器: shangshandalaohu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00X_0031)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: iStepYaoLong == 1
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 单位持有物品类型(触发单位(), I02K) == TRUE
  │    │      │    ├─ 单位持有物品类型(触发单位(), I02H) == TRUE
  │    │      │    ├─ 单位持有物品类型(触发单位(), I055) == TRUE
  │    │      ├─ 则
  │    │      │    如果
  │    │      │      ├─ 条件: 任一成立
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 整数比较(玩家属性值((触发单位()的所有者), PlayerStateLumber), OperatorLess, 1000)
  │    │      │      │      ├─ 则: 返回()
  │    │      │      │      └─ 否则: 无动作()
  │    │      │      │    删除物品: 单位携带物品(按类型)(触发单位(), I02K)
  │    │      │      │    删除物品: 单位携带物品(按类型)(触发单位(), I02H)
  │    │      │      │    删除物品: 单位携带物品(按类型)(触发单位(), I055)
  │    │      │      │    UnitAddItemByIdSwapped: I01W, 触发单位()
  │    │      │      │    显示文本→(触发单位()的所有者): 0
  │    │      │      │    调整 (触发单位()的所有者) 的 PlayerStateLumber: -1000
  │    │      │      │    销毁触发器(自身)
  │    │      │      │    返回
  │    │      │      └─ 否则
  │    │      │           如果
  │    │      │             ├─ 条件: 整数比较(玩家属性值((触发单位()的所有者), PlayerStateLumber), OperatorLess, 1000)
  │    │      │             ├─ 则: 返回()
  │    │      │             └─ 否则: 无动作()
  │    │      │           显示文本→(触发单位()的所有者): 0
  │    │      │           调整 (触发单位()的所有者) 的 PlayerStateLumber: -1000
  │    │      │           返回
  │    │      └─ 否则
  │    │           返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 随机[1~20] == 1
       ├─ 则
       │    关闭触发器 当前触发器()
       │    显示文本→(触发单位()的所有者): 0
       │    PolledWait: 2
       │    显示文本→(触发单位()的所有者): 0
       │    PolledWait: 2
       │    显示文本→(触发单位()的所有者): 0
       │    设置 iStepYaoLong = 1
       │    开启触发器 当前触发器()
       └─ 否则
            如果
              ├─ 条件: 随机[1~4] == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              │    PolledWait: 2
              │    显示文本→(触发单位()的所有者): 0
              │    返回
              └─ 否则: (无)
            如果
              ├─ 条件: 随机[1~3] == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              │    PolledWait: 2
              │    显示文本→(触发单位()的所有者): 0
              │    返回
              └─ 否则: (无)
            如果
              ├─ 条件: 随机[1~2] == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              │    PolledWait: 2
              │    显示文本→(触发单位()的所有者): 0
              │    返回
              └─ 否则: (无)
            如果
              ├─ 条件: 随机[1~1] == 1
              ├─ 则
              │    显示文本→(触发单位()的所有者): 0
              │    PolledWait: 2
              │    显示文本→(触发单位()的所有者): 0
              │    PolledWait: 2
              │    显示文本→(触发单位()的所有者): 0
              │    返回
              └─ 否则: (无)
```

</details>

<details id="trigger-02_007_mi">
<summary><strong>📌 mi</strong> <code>02_007_mi</code></summary>

```text
触发器: mi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(100.00, gg_unit_n00D_0026)
条件
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  └─ 如果
       ├─ 条件: (触发单位()类型ID) == E000
       ├─ 则
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 玩家科技等级(Rhcd, (触发单位()的所有者)) == 0
       │      │    ├─ 英雄等级(触发单位()) OperatorGreater 100
       │      │    ├─ uYuanGuChuanCheng == UnitNull
       │      ├─ 则
       │      │    关闭触发器 当前触发器()
       │      │    设置 uYuanGuChuanCheng = 触发单位()
       │      │    PauseUnitBJ: PauseUnpauseOptionPause, uYuanGuChuanCheng
       │      │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_1419", SoundNull, "TRIGSTR_1421", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3829", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3830", SoundNull, "TRIGSTR_3831", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3832", SoundNull, "TRIGSTR_3833", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3835", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3836", SoundNull, "TRIGSTR_3837", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3839", AddSetToAdd, 0, WaitDontWait
       │      │    显示文本→grpOnline: "TRIGSTR_1332"
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │    PolledWait: 120.00
       │      │    IssueImmediateOrderById: gg_unit_n00D_0026, OrderCodeStop
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3840", SoundNull, "TRIGSTR_3841", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3842", AddSetToAdd, 0, WaitDontWait
       │      │    SetPlayerTechResearchedSwap: Rhcd, 1, (uYuanGuChuanCheng的所有者)
       │      │    显示文本→grpOnline: "TRIGSTR_3843"
       │      │    PauseUnitBJ: PauseUnpauseOptionUnpause, uYuanGuChuanCheng
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │    销毁触发器(自身)
       │      │    隐藏单位: gg_unit_n00D_0026
       │      └─ 否则: (无)
       └─ 否则
            伤害: gg_unit_n00D_0026→触发单位(): 25000000.00 (AttackTypeNormal/DamageTypeUniversal)
            ForceClear: grpPlayerGroupTemp
            ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
            TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_n00D_0026, "TRIGSTR_3844", SoundNull, "TRIGSTR_3845", AddSetToAdd, 0, WaitDontWait
```

</details>

<details id="trigger-02_008_yuanguzhishustart">
<summary><strong>📌 yuanguzhishustart</strong> <code>02_008_yuanguzhishustart</code></summary>

```text
触发器: yuanguzhishustart (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_hatw_0029)
条件
  ├─ 单位持有物品类型(触发单位(), I03A) == TRUE
  ├─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I03A)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_hatw_0029), 单位Y坐标(gg_unit_hatw_0029), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5543", SoundNull, "TRIGSTR_5544", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5545", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5554", SoundNull, "TRIGSTR_5555", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5556", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5559", SoundNull, "TRIGSTR_5560", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5557", SoundNull, "TRIGSTR_5558", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5561", SoundNull, "TRIGSTR_5562", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5565", SoundNull, "TRIGSTR_5566", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置无敌: gg_unit_hatw_0029, InvulnerabilityVulnerable
  └─ SetPlayerTechResearchedSwap: Rhse, 1, PlayerNA
```

</details>

<details id="trigger-02_009_yuanguzhishu">
<summary><strong>📌 yuanguzhishu</strong> <code>02_009_yuanguzhishu</code></summary>

```text
触发器: yuanguzhishu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_hatw_0029 - 单位死亡
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5567", SoundNull, "TRIGSTR_5568", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5583", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_5584", SoundNull, "TRIGSTR_5585", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5586", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ PolledWait: 30.00
  ├─ PauseUnitBJ: PauseUnpauseOptionUnpause, gg_unit_H00C_0033
  └─ 设置无敌: gg_unit_H00C_0033, InvulnerabilityVulnerable
```

</details>

<details id="trigger-02_010_PanNiu">
<summary><strong>📌 PanNiu</strong> <code>02_010_PanNiu</code></summary>

```text
触发器: PanNiu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_uabo_0095 - UnitEventSellItem
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 iPanNiuSell = (iPanNiuSell + 1)
  ├─ 如果
  │    ├─ 条件: iPanNiuSell == 30
  │    ├─ 则
  │    │    AddItemToStockBJ: I05X, gg_unit_nhea_0113, 1, 1
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_uabo_0095), 单位Y坐标(gg_unit_uabo_0095), 0
  │    │    电影模式: OnOffOn, grpOnline
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_uabo_0095, "TRIGSTR_5657", SoundNull, "TRIGSTR_5754", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_uabo_0095, "TRIGSTR_5760", SoundNull, "TRIGSTR_5761", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_nhea_0113, "TRIGSTR_5763", SoundNull, "TRIGSTR_5764", AddSetToAdd, 0, WaitDontWait
  │    │    电影模式: OnOffOff, grpOnline
  │    │    开启触发器 gg_trg_XiaoPanNiu
  │    │    销毁触发器(自身)
  │    │    返回
  │    └─ 否则: (无)
  ├─ PolledWait: 10.00
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-02_011_XiaoPanNiu">
<summary><strong>📌 XiaoPanNiu</strong> <code>02_011_XiaoPanNiu</code></summary>

```text
触发器: XiaoPanNiu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_nhea_0113 - UnitEventSellItem
条件
  └─ 物品类型比较(物品类型ID(被贩卖物品()), OperatorEqualENE, I05X)
动作
  ├─ 销毁触发器(自身)
  └─ RemoveItemFromStockBJ: I05X, gg_unit_nhea_0113
```

</details>

<details id="trigger-02_012_杀戮者">
<summary><strong>📌 杀戮者</strong> <code>02_012_杀戮者</code></summary>

```text
触发器: 杀戮者 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_013_JieYuan">
<summary><strong>📌 JieYuan</strong> <code>02_013_JieYuan</code></summary>

```text
触发器: JieYuan (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_n00Q_0107)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位持有物品类型(触发单位(), I05P) == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ 设置 bJieYuan = true
  ├─ 循环整数A 1→36
  │    ├─ 设置 lgtJieBei[循环整数A] = 创建闪电效果(LightningTypeCLPB, AllowDontDont, 单位X坐标(gg_unit_n00Q_0107), 单位Y坐标(gg_unit_n00Q_0107), 单位X坐标(gg_unit_n00Q_0107), 单位Y坐标(gg_unit_n00Q_0107))
  │    └─ MoveLightningEx: lgtJieBei[循环整数A], AllowDontDont, (单位X坐标(gg_unit_n00Q_0107) + (256.00 x 余弦(弧度转角度(((循环整数A x 10)转实数))))), (单位Y坐标(gg_unit_n00Q_0107) + (256.00 x 正弦(弧度转角度(((循环整数A x 10)转实数))))), 700.00, (单位X坐标(gg_unit_n00Q_0107) + (256.00 x 余弦(弧度转角度((((循环整数A + 3) x 10)转实数))))), (单位Y坐标(gg_unit_n00Q_0107) + (256.00 x 正弦(弧度转角度((((循环整数A + 3) x 10)转实数))))), 2000.00
  ├─ 循环整数A 37→72
  │    ├─ 设置 lgtJieBei[循环整数A] = 创建闪电效果(LightningTypeCLPB, AllowDontDont, 单位X坐标(gg_unit_n00Q_0107), 单位Y坐标(gg_unit_n00Q_0107), 单位X坐标(gg_unit_n00Q_0107), 单位Y坐标(gg_unit_n00Q_0107))
  │    └─ MoveLightningEx: lgtJieBei[循环整数A], AllowDontDont, (单位X坐标(gg_unit_n00Q_0107) + (256.00 x 余弦(弧度转角度(((循环整数A x 10)转实数))))), (单位Y坐标(gg_unit_n00Q_0107) + (256.00 x 正弦(弧度转角度(((循环整数A x 10)转实数))))), 700.00, (单位X坐标(gg_unit_n00Q_0107) + (256.00 x 余弦(弧度转角度((((循环整数A - 3) x 10)转实数))))), (单位Y坐标(gg_unit_n00Q_0107) + (256.00 x 正弦(弧度转角度((((循环整数A - 3) x 10)转实数))))), 2000.00
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_n00Q_0107), 单位Y坐标(gg_unit_n00Q_0107), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitTypeWithNameBJ: grpOnline, 玩家8(粉), Ogld, "TRIGSTR_4056", pHG, SoundNull, "TRIGSTR_4057", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitTypeWithNameBJ: grpOnline, 玩家8(粉), Ogld, "TRIGSTR_4058", pHG, SoundNull, "TRIGSTR_4059", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ PolledWait: 20.00
  ├─ 循环整数A 1→12
  │    ├─ 设置 uShaLuZhe[循环整数A] = 创建单位(指定坐标)(玩家8(粉), Ogld, (单位X坐标(gg_unit_n00Q_0107) + 自定义代码("300*CosBJ(bj_forLoopAIndex*30)")), (单位Y坐标(gg_unit_n00Q_0107) + 自定义代码("300*SinBJ(bj_forLoopAIndex*30)")), 自定义代码("bj_forLoopAIndex*30-180"))
  │    └─ 清除点 pTemp
  ├─ 设置 grpTemp = 区域内全部单位(可用地图区域())
  ├─ 运行计时器 tShaLuZheMove (循环, 10.00s)
  ├─ 开启触发器 gg_trg_ShaLuZheMove
  ├─ 关闭触发器 gg_trg_Boss
  ├─ 关闭触发器 gg_trg_ReviveHero
  ├─ SetPlayerAllianceStateBJ: 玩家8(粉), 非玩家, AllianceSettingUnallied
  ├─ SetPlayerAllianceStateBJ: 非玩家, 玩家8(粉), AllianceSettingUnallied
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    ├─ 设置无敌: 选取单位(), InvulnerabilityVulnerable
  │    └─ PauseUnitBJ: PauseUnpauseOptionUnpause, 选取单位()
  └─ PauseUnit: gg_unit_ntav_0012, PauseUnpauseOptionPause
```

</details>

<details id="trigger-02_014_ShaLuZheMove">
<summary><strong>📌 ShaLuZheMove</strong> <code>02_014_ShaLuZheMove</code></summary>

```text
触发器: ShaLuZheMove (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tShaLuZheMove 到期
条件
  └─ 无
动作
  ├─ 设置 iTemp = 0
  ├─ 循环整数A 1→12
  │    └─ 如果
  │         ├─ 条件: 单位存活判断(uShaLuZhe[循环整数A]) == TRUE
  │         ├─ 则
  │         │    设置 pTemp = 区域内随机点(可用地图区域())
  │         │    命令 uShaLuZhe[循环整数A] → UnitOrderAttack 到 pTemp
  │         │    清除点 pTemp
  │         │    设置 iTemp = (iTemp + 1)
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: iTemp == 0
       ├─ 则
       │    关闭触发器 当前触发器()
       │    暂停计时器 tShaLuZheMove
       │    ForForceMultiple: grpOnline
       └─ 否则: (无)
```

</details>

<details id="trigger-02_015_主线剧情">
<summary><strong>📌 主线剧情</strong> <code>02_015_主线剧情</code></summary>

```text
触发器: 主线剧情 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_016_juetian">
<summary><strong>📌 juetian</strong> <code>02_016_juetian</code></summary>

```text
触发器: juetian (剧情/任务) [✓] — 魔帝之子死亡
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_N006_0102 - 单位死亡
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 移动单位: 凶手单位(), pHG
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N006_0102, "TRIGSTR_3846", SoundNull, "TRIGSTR_3847", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ SetUnitOwner: 触发单位(), 玩家7(绿), 改变颜色
  ├─ ForForceMultiple: grpUserPlayers
  ├─ 复活英雄 触发单位() 在 pHG
  ├─ 设置 uPlayerHeros[8] = gg_unit_N006_0102
  ├─ PolledWait: 0.10
  └─ MultiboardDisplayBJ: ShowHideShow, TopBoard
```

</details>

<details id="trigger-02_017_xuanyuan">
<summary><strong>📌 xuanyuan</strong> <code>02_017_xuanyuan</code></summary>

```text
触发器: xuanyuan (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_H00C_0033 - 单位死亡
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H00C_0033, "TRIGSTR_4489", SoundNull, "TRIGSTR_4519", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00V_0059, "TRIGSTR_5517", SoundNull, "TRIGSTR_5518", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5519", SoundNull, "TRIGSTR_5520", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00V_0059, "TRIGSTR_5521", SoundNull, "TRIGSTR_5522", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5523", SoundNull, "TRIGSTR_5524", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOff, grpOnline
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-02_018_linghunshashou">
<summary><strong>📌 linghunshashou</strong> <code>02_018_linghunshashou</code></summary>

```text
触发器: linghunshashou (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tGuiChengHeiLong 到期
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定点)(玩家9(灰), H00D, pShuaGuai[10], 180.00) → UnitOrderAttack 到 pHG
  └─ 命令 创建单位(指定点)(玩家9(灰), H00D, pShuaGuai[10], 180.00) → UnitOrderAttack 到 pHG
```

</details>

<details id="trigger-02_019_diyouyoubf">
<summary><strong>📌 diyouyoubf</strong> <code>02_019_diyouyoubf</code></summary>

```text
触发器: diyouyoubf (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  └─ 创建物品(指定坐标): mcou, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
```

</details>

<details id="trigger-02_020_diyouyoustart">
<summary><strong>📌 diyouyoustart</strong> <code>02_020_diyouyoustart</code></summary>

```text
触发器: diyouyoustart (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00N_0054)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位持有物品类型(触发单位(), mcou) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), mcou)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00N_0054), 单位Y坐标(gg_unit_N00N_0054), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00N_0054, (单位名:gg_unit_N00N_0054), SoundNull, "TRIGSTR_1055", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00N_0054, (单位名:gg_unit_N00N_0054), SoundNull, "TRIGSTR_962", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1056", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ PauseUnitBJ: PauseUnpauseOptionUnpause, gg_unit_N00N_0054
  ├─ 设置无敌: gg_unit_N00N_0054, InvulnerabilityVulnerable
  ├─ 运行计时器 tGuiChengHeiLong (循环, 4.00s)
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-02_021_diyouyoudie">
<summary><strong>📌 diyouyoudie</strong> <code>02_021_diyouyoudie</code></summary>

```text
触发器: diyouyoudie (剧情/任务) [✓] — 魔帝之子死亡
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_N00N_0054 - 单位死亡
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 暂停计时器 tGuiChengHeiLong
  ├─ 销毁触发器(自身)
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00N_0054, (单位名:触发单位()), SoundNull, "TRIGSTR_4120", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Uclc_0123, "TRIGSTR_3926", SoundNull, "TRIGSTR_4188", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  └─ SetPlayerTechResearchedSwap: Rhhb, 1, 玩家9(灰)
```

</details>

<details id="trigger-02_022_传说">
<summary><strong>📌 传说</strong> <code>02_022_传说</code></summary>

```text
触发器: 传说 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_023_wumingmubei">
<summary><strong>📌 wumingmubei</strong> <code>02_023_wumingmubei</code></summary>

```text
触发器: wumingmubei (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_hwtw_0084)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4022", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4023", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4024", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4025", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置 bSiWangJueDi = true
  └─ SetUnitOwner: gg_unit_hwtw_0084, 玩家7(绿), 改变颜色
```

</details>

<details id="trigger-02_024_yinshuang">
<summary><strong>📌 yinshuang</strong> <code>02_024_yinshuang</code></summary>

```text
触发器: yinshuang (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_h003_0002)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 显示文本→(触发单位()的所有者): 0
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I032)) == TRUE
       │    ├─ 随机[1~5] == 5
       │    ├─ iStepHaoYue == 1
       ├─ 则
       │    销毁触发器(自身)
       │    QuestSetDiscoveredBJ: quests[1], DiscoveredOptionDiscovered
       │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h003_0002, "TRIGSTR_4011", SoundNull, "TRIGSTR_4012", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4013", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h003_0002, "TRIGSTR_4014", SoundNull, "TRIGSTR_4015", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4016", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h003_0002, "TRIGSTR_4017", SoundNull, "TRIGSTR_4018", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4019", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    UnitAddItemByIdSwapped: k3m1, 触发单位()
       │    显示文本→grpOnline: "TRIGSTR_1099"
       │    设置 iStepHaoYue = 2
       └─ 否则
            杀死 触发单位()
```

</details>

<details id="trigger-02_025_haotian">
<summary><strong>📌 haotian</strong> <code>02_025_haotian</code></summary>

```text
触发器: haotian (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_H001_0087)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepHaoYue == 2
  │    │    ├─ 单位持有物品类型(触发单位(), k3m1) == TRUE
  │    │    ├─ 游戏时间(24h)() OperatorGreaterEq 12.00
  │    │    ├─ 游戏时间(24h)() OperatorLessEq 13.00
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), k3m1)
  │    │    SetUnitOwner: gg_unit_H001_0087, 非玩家, 改变颜色
  │    │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4121", SoundNull, "TRIGSTR_4122", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4123", AddSetToAdd, 0, WaitDontWait
  │    │    设置 pTemp = (gg_unit_H001_0087的位置)
  │    │    销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  │    │    清除点 pTemp
  │    │    设置 pTemp = (gg_unit_h003_0002的位置)
  │    │    移动单位: gg_unit_H001_0087, pTemp
  │    │    清除点 pTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4124", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4125", SoundNull, "TRIGSTR_4126", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4127", SoundNull, "TRIGSTR_4128", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    QuestSetCompletedBJ: quests[1], CompletionOptionCompleted
  │    │    设置 iStepHaoYue = 3
  │    │    设置 uPlayerHeros[(玩家号((触发单位()的所有者)) + 20)] = 创建单位(指定点)((触发单位()的所有者), H004, pHG, 0)
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepHaoYue == 3
  │    │    ├─ 单位持有物品类型(触发单位(), I032) == TRUE
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4129", SoundNull, "TRIGSTR_4130", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4131", SoundNull, "TRIGSTR_4132", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4133", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4134", SoundNull, "TRIGSTR_4135", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4136", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4137", SoundNull, "TRIGSTR_4138", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4139", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    UnitAddItemByIdSwapped: I03U, 触发单位()
  │    │    QuestSetDiscoveredBJ: quests[2], DiscoveredOptionDiscovered
  │    │    设置 iStepHaoYue = 4
  │    │    显示文本→grpOnline: "TRIGSTR_4140"
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iStepHaoYue == 5
       │    ├─ 单位持有物品类型(触发单位(), I032) == TRUE
       │    ├─ 单位持有物品类型(触发单位(), I02F) == TRUE
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除物品: 单位携带物品(按类型)(触发单位(), I02F)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I032)
       │    UnitAddItemByIdSwapped: I03V, 触发单位()
       │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4141", SoundNull, "TRIGSTR_4142", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H001_0087, "TRIGSTR_4143", SoundNull, "TRIGSTR_4144", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4145", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4146", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    AddItemToStockBJ: I05L, gg_unit_npn1_0119, 1, 1
       │    QuestSetCompletedBJ: quests[2], CompletionOptionCompleted
       │    销毁触发器(自身)
       │    隐藏单位: gg_unit_H001_0087
       └─ 否则: (无)
```

</details>

<details id="trigger-02_026_xinzang">
<summary><strong>📌 xinzang</strong> <code>02_026_xinzang</code></summary>

```text
触发器: xinzang (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(500.00, gg_unit_n001_0166)
条件
  ├─ iStepHaoYue == 4
  └─ 单位持有物品类型(触发单位(), I032) == TRUE
动作
  └─ DisplayTimedTextToPlayer: (触发单位()的所有者), 0, 0, 30, "TRIGSTR_3980"
```

</details>

<details id="trigger-02_027_上山打老虎">
<summary><strong>📌 上山打老虎</strong> <code>02_027_上山打老虎</code></summary>

```text
触发器: 上山打老虎 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_028_KillAllDistrutable">
<summary><strong>📌 KillAllDistrutable</strong> <code>02_028_KillAllDistrutable</code></summary>

```text
触发器: KillAllDistrutable (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册可破坏物死亡事件(gg_rct_________________000)
条件
  └─ 无
动作
  ├─ 设置 iHuGeShu = (iHuGeShu + 1)
  └─ 如果
       ├─ 条件: iHuGeShu OperatorGreater 40
       ├─ 则
       │    销毁触发器(自身)
       │    PanCameraToTimed: 单位X坐标(gg_unit_N00X_0031), 单位Y坐标(gg_unit_N00X_0031), 0
       │    电影模式: OnOffOn, grpOnline
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00X_0031, "TRIGSTR_5609", SoundNull, "TRIGSTR_5610", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00X_0031, "TRIGSTR_5611", SoundNull, "TRIGSTR_5612", AddSetToAdd, 0, WaitDontWait
       │    电影模式: OnOffOff, grpOnline
       │    SetUnitOwner: gg_unit_N00X_0031, PlayerNA, 改变颜色
       │    关闭触发器 gg_trg_shangshandalaohu
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-02_029_妖灵专属">
<summary><strong>📌 妖灵专属</strong> <code>02_029_妖灵专属</code></summary>

```text
触发器: 妖灵专属 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-02_030_xiongci">
<summary><strong>📌 xiongci</strong> <code>02_030_xiongci</code></summary>

```text
触发器: xiongci (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N017_0037)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ (触发单位()类型ID) == N00L
       │    ├─ 英雄等级(触发单位()) OperatorGreater 123
       ├─ 则
       │    关闭触发器 当前触发器()
       │    如果
       │      ├─ 条件: iCountJTS == 0
       │      ├─ 则
       │      │    设置 iCountJTS = (iCountJTS + 1)
       │      │    SetUnitOwner: gg_unit_N017_0037, 非玩家, 改变颜色
       │      │    PanCameraToTimed: 单位X坐标(gg_unit_N017_0037), 单位Y坐标(gg_unit_N017_0037), 0
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N017_0037, "TRIGSTR_5932", SoundNull, "TRIGSTR_5933", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5934", AddSetToAdd, 0, WaitDontWait
       │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N017_0037, "TRIGSTR_187", SoundNull, "TRIGSTR_323", AddSetToAdd, 0, WaitDontWait
       │      │    ForceClear: grpPlayerGroupTemp
       │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │    设置 grpTemp = 玩家指定类型单位(非玩家, nhyh)
       │      │    单位组: 选取 grpTemp 中所有单位
       │      │      ├─ 设置无敌: 选取单位(), InvulnerabilityVulnerable
       │      │      └─ SetUnitOwner: 选取单位(), PlayerNA, 改变颜色
       │      │    删除单位组 grpTemp
       │      │    开启触发器 当前触发器()
       │      │    返回
       │      └─ 否则
       │           如果
       │             ├─ 条件: iCountJTS OperatorGreater 25
       │             ├─ 则
       │             │    PanCameraToTimed: 单位X坐标(gg_unit_N017_0037), 单位Y坐标(gg_unit_N017_0037), 0
       │             │    ForceClear: grpPlayerGroupTemp
       │             │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │             │    电影模式: OnOffOn, grpPlayerGroupTemp
       │             │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N017_0037, "TRIGSTR_3938", SoundNull, "TRIGSTR_4232", AddSetToAdd, 0, WaitDontWait
       │             │    UnitAddItemByIdSwapped: schl, 触发单位()
       │             │    删除物品: 单位携带物品(按类型)(gg_unit_N017_0037, schl)
       │             │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N017_0037, "TRIGSTR_5540", SoundNull, "TRIGSTR_5821", AddSetToAdd, 0, WaitDontWait
       │             │    ForceClear: grpPlayerGroupTemp
       │             │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │             │    电影模式: OnOffOff, grpPlayerGroupTemp
       │             │    销毁触发器(自身)
       │             │    返回
       │             └─ 否则: (无)
       │    开启触发器 当前触发器()
       └─ 否则
            ForceClear: grpPlayerGroupTemp
            ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
            TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_N017_0037, "TRIGSTR_5917", SoundNull, "TRIGSTR_5918", AddSetToAdd, 0, WaitDontWait
```

</details>

