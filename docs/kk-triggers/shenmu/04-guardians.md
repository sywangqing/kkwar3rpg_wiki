---
title: 神墓 2.7C — 🛡️ 04 守护者与合体
category: kk-triggers
slug: shenmu/04-guardians
description: 守护者/合体技能/水域减速/鬼蜮
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 🛡️ 04 守护者与合体

> 守护者/合体技能/水域减速/鬼蜮

**共 20 个触发器**

## 📑 触发器目录

- [ShouHuZhe](#trigger-04_000_ShouHuZhe)
- [DuoLuoShuRen](#trigger-04_001_DuoLuoShuRen)
- [WangQueZhiLu](#trigger-04_002_WangQueZhiLu)
- [ForbideEnter1](#trigger-04_003_ForbideEnter1)
- [ForbideEnter2](#trigger-04_004_ForbideEnter2)
- [ForbideEnterMODI](#trigger-04_005_ForbideEnterMODI)
- [ForbideOut](#trigger-04_006_ForbideOut)
- [ForbideTeleport](#trigger-04_007_ForbideTeleport)
- [RuoShui](#trigger-04_008_RuoShui)
- [ShuiYuJianSu](#trigger-04_009_ShuiYuJianSu)
- [ShuiYuJianSuHuiFu](#trigger-04_010_ShuiYuJianSuHuiFu)
- [GuiXuIn](#trigger-04_011_GuiXuIn)
- [GuiXuLeft](#trigger-04_012_GuiXuLeft)
- [GuiXuShangHai](#trigger-04_013_GuiXuShangHai)
- [寒冰炽炎合体技能](#trigger-04_014_寒冰炽炎合体技能)
- [HeTiEnter1](#trigger-04_015_HeTiEnter1)
- [HeTiOut1](#trigger-04_016_HeTiOut1)
- [HeTiEnter2](#trigger-04_017_HeTiEnter2)
- [HeTiOut2](#trigger-04_018_HeTiOut2)
- [HeTiCheck](#trigger-04_019_HeTiCheck)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-04_000_ShouHuZhe">
<summary><strong>📌 ShouHuZhe</strong> <code>04_000_ShouHuZhe</code></summary>

```text
触发器: ShouHuZhe (区域/禁地) [✗]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct__________00001)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 设置 pTemp = (区域gg_rct__________0002中心)
  ├─ 销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  ├─ 移动单位: 触发单位(), pTemp
  ├─ 平移镜头: (触发单位()的所有者), pTemp, 0
  └─ 清除点 pTemp
```

</details>

<details id="trigger-04_001_DuoLuoShuRen">
<summary><strong>📌 DuoLuoShuRen</strong> <code>04_001_DuoLuoShuRen</code></summary>

```text
触发器: DuoLuoShuRen (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct__________00002)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 设置 pTemp = (区域gg_rct_____________06中心)
  ├─ 销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  ├─ 移动单位: 触发单位(), pTemp
  ├─ 平移镜头: (触发单位()的所有者), pTemp, 0
  └─ 清除点 pTemp
```

</details>

<details id="trigger-04_002_WangQueZhiLu">
<summary><strong>📌 WangQueZhiLu</strong> <code>04_002_WangQueZhiLu</code></summary>

```text
触发器: WangQueZhiLu (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct___________________0)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  └─ bSiWangJueDi == TRUE
动作
  ├─ 设置 pTemp = (区域gg_rct_____________g中心)
  ├─ 销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  ├─ 移动单位: 触发单位(), pTemp
  ├─ 平移镜头: (触发单位()的所有者), pTemp, 0
  └─ 清除点 pTemp
```

</details>

<details id="trigger-04_003_ForbideEnter1">
<summary><strong>📌 ForbideEnter1</strong> <code>04_003_ForbideEnter1</code></summary>

```text
触发器: ForbideEnter1 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 注册进入矩形区域事件(gg_rct_______________0001)
  └─ 注册进入矩形区域事件(gg_rct_____________u)
条件
  ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  └─ (触发单位()类型ID) == ufro
动作
  ├─ 移动单位: 触发单位(), pHG
  └─ 显示文本→(触发单位()的所有者): 0
```

</details>

<details id="trigger-04_004_ForbideEnter2">
<summary><strong>📌 ForbideEnter2</strong> <code>04_004_ForbideEnter2</code></summary>

```text
触发器: ForbideEnter2 (区域/禁地) [✗]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  └─ (触发单位()类型ID) == ufro
动作
  ├─ 移动单位: 触发单位(), pHG
  └─ 显示文本→(触发单位()的所有者): 0
```

</details>

<details id="trigger-04_005_ForbideEnterMODI">
<summary><strong>📌 ForbideEnterMODI</strong> <code>04_005_ForbideEnterMODI</code></summary>

```text
触发器: ForbideEnterMODI (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct______________1111111)
条件
  ├─ 单位存活判断(gg_unit_H00A_0081) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 移动单位: 触发单位(), 单位X坐标(gg_unit_H00A_0081), 单位Y坐标(gg_unit_H00A_0081)
  └─ TransmissionFromUnitWithNameBJ: grpUserPlayers, gg_unit_H00A_0081, "TRIGSTR_4035", SoundNull, "TRIGSTR_4036", AddSetToAdd, 0, WaitDontWait
```

</details>

<details id="trigger-04_006_ForbideOut">
<summary><strong>📌 ForbideOut</strong> <code>04_006_ForbideOut</code></summary>

```text
触发器: ForbideOut (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct_____________0000)
条件
  ├─ (触发单位()的所有者) == 玩家7(绿)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 移动单位: 触发单位(), pHG
```

</details>

<details id="trigger-04_007_ForbideTeleport">
<summary><strong>📌 ForbideTeleport</strong> <code>04_007_ForbideTeleport</code></summary>

```text
触发器: ForbideTeleport (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A030)
动作
  ├─ 设置 pTemp = 技能目标点()
  └─ 如果
       ├─ 条件: 点是否在区域内(gg_rct_______________0001, pTemp) == TRUE
       ├─ 则
       │    清除点 pTemp
       │    设置 pTemp = (触发单位()的位置)
       │    移动单位: 触发单位(), pTemp
       │    清除点 pTemp
       │    单位发布命令(立即): 触发单位(), UnitOrderStop
       │    显示文本→(触发单位()的所有者): 0
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-04_008_RuoShui">
<summary><strong>📌 RuoShui</strong> <code>04_008_RuoShui</code></summary>

```text
触发器: RuoShui (区域/禁地) [✗]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct______________123)
条件
  ├─ 单位技能等级(触发单位(), A0AV) == 0
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  └─ 伤害: 触发单位()→触发单位(): 单位状态(UnitStateMaxLife, 触发单位()) (AttackTypeChaos/DamageTypeUniversal)
```

</details>

<details id="trigger-04_009_ShuiYuJianSu">
<summary><strong>📌 ShuiYuJianSu</strong> <code>04_009_ShuiYuJianSu</code></summary>

```text
触发器: ShuiYuJianSu (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct______________063)
条件
  ├─ 单位类型判断(触发单位(), UnitTypeGround) == TRUE
  └─ 单位技能等级(触发单位(), A0AV) == 0
动作
  ├─ 设置单位颜色: 触发单位(), 100, 100, 255, 255
  └─ 设置移动速度: 触发单位(), (单位默认移速(触发单位()) x 0.50)
```

</details>

<details id="trigger-04_010_ShuiYuJianSuHuiFu">
<summary><strong>📌 ShuiYuJianSuHuiFu</strong> <code>04_010_ShuiYuJianSuHuiFu</code></summary>

```text
触发器: ShuiYuJianSuHuiFu (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct______________063)
条件
  ├─ 单位类型判断(触发单位(), UnitTypeGround) == TRUE
  └─ 单位技能等级(触发单位(), A0AV) == 0
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
  │    │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    设置单位颜色: uPlayerHeros[玩家号((触发单位()的所有者))], iFaZeColor[((iTemp x 1) - 3)], iFaZeColor[((iTemp x 4) - 2)], iFaZeColor[((iTemp x 4) - 1)], iFaZeColor[(iTemp x 4)]
  │    └─ 否则
  │         如果
  │           ├─ 条件: (触发单位()类型ID) == nlv2
  │           ├─ 则
  │           │    设置单位颜色: 触发单位(), 255, 255, 255, 50
  │           └─ 否则
  │                设置单位颜色: 触发单位(), 255, 255, 255, 255
  └─ 设置移动速度: 触发单位(), 单位默认移速(触发单位())
```

</details>

<details id="trigger-04_011_GuiXuIn">
<summary><strong>📌 GuiXuIn</strong> <code>04_011_GuiXuIn</code></summary>

```text
触发器: GuiXuIn (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct_______________0001)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 单位类型判断(触发单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 单位技能等级(触发单位(), Agyb) == 0
  │    │      ├─ 则
  │    │      │    如果
  │    │      │      ├─ 条件: 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  │    │      │      ├─ 则
  │    │      │      │    设置 pTemp = (区域gg_rct_______________0001中心)
  │    │      │      │    SetUnitAbilityLevelSwapped: AInv, 触发单位(), 2
  │    │      │      │    移动单位: 触发单位(), pTemp
  │    │      │      │    清除点 pTemp
  │    │      │      │    ModifyGateBJ: GateOperationClosed, gg_dest_LTg1_0259
  │    │      │      │    运行计时器 tGuiXu (循环, 0.05s)
  │    │      │      │    运行计时器 tGuiXuShiLian (一次性, 30.00s)
  │    │      │      └─ 否则
  │    │      │           杀死 触发单位()
  │    │      └─ 否则: (无)
  │    └─ 否则
  │         移动单位: 触发单位(), pTemp
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-04_012_GuiXuLeft">
<summary><strong>📌 GuiXuLeft</strong> <code>04_012_GuiXuLeft</code></summary>

```text
触发器: GuiXuLeft (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct_______________0001)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 单位技能等级(Agyb, 触发单位()) == 0
  │    ├─ 则
  │    │    SetUnitAbilityLevelSwapped: AInv, 触发单位(), 1
  │    │    杀死 触发单位()
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

</details>

<details id="trigger-04_013_GuiXuShangHai">
<summary><strong>📌 GuiXuShangHai</strong> <code>04_013_GuiXuShangHai</code></summary>

```text
触发器: GuiXuShangHai (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tGuiXu 到期
条件
  └─ 无
动作
  ├─ CustomScriptCode: "local lightning lgtTemp=null"
  ├─ CustomScriptCode: "local unit uTemp=null"
  ├─ 设置 grpTemp = 区域内符合条件的单位(gg_rct_______________0001, 布尔比较(玩家在玩家组中((过滤单位()的所有者), grpUserPlayers), OperatorEqualENE, true))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 0
  │    ├─ 则
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg1_0259
  │    │    暂停计时器 tGuiXu
  │    │    删除单位组 grpTemp
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 1
  │    ├─ 则
  │    │    设置 uTemp = 单位组第一个单位(grpTemp)
  │    │    删除单位组 grpTemp
  │    │    如果
  │    │      ├─ 条件: 单位技能等级(uTemp, A0B3) == 1
  │    │      ├─ 则
  │    │      │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg1_0259
  │    │      │    暂停计时器 tGuiXu
  │    │      │    删除单位组 grpTemp
  │    │      │    返回
  │    │      └─ 否则
  │    │           UnitRemoveBuffsBJ: BuffTypeAll, uTemp
  │    │           设置 pTemp = 区域内随机点(gg_rct_______________0001)
  │    │           销毁特效 创建特效(Objects\Spawnmodels\Human\HCancelDeath\HCancelDeath.mdl, pTemp)
  │    │           CustomScriptCode: "set lgtTemp=AddLightningEx(udg_lgtType[GetRandomInt(1,14)],false,GetLocationX..."
  │    │           CustomScriptCode: "if GetRandomInt(1,20)==1 then"
  │    │           命令 创建单位(指定点)(PlayerNA, nitr, pTemp, 0) → UnitOrderStampede 到 单位X坐标(uTemp)
  │    │           CustomScriptCode: "endif"
  │    │           清除点 pTemp
  │    │           如果
  │    │             ├─ 条件: 单位存活判断(uTemp) == TRUE
  │    │             ├─ 则
  │    │             │    如果
  │    │             │      ├─ 条件: 计时器已过时间(tGuiXuShiLian) OperatorGreaterEq 29.90
  │    │             │      ├─ 则
  │    │             │      │    UnitAddItemByIdSwapped: rde1, uTemp
  │    │             │      │    如果
  │    │             │      │      ├─ 条件: 物品有归属(最后创建的物品()) == TRUE
  │    │             │      │      ├─ 则
  │    │             │      │      │    删除物品: 最后创建的物品()
  │    │             │      │      └─ 否则
  │    │             │      │           SetUnitAbilityLevelSwapped: AInv, uTemp, 1
  │    │             │      └─ 否则: (无)
  │    │             └─ 否则
  │    │                  移动单位: uTemp, pHG
  │    │           PolledWait: 0.10
  │    │           CustomScriptCode: "call DestroyLightning(lgtTemp)"
  │    │           返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) OperatorGreater 1
  │    ├─ 则
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ 杀死 选取单位()
  │    │      └─ 移动单位: 选取单位(), pHG
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg1_0259
  │    │    暂停计时器 tGuiXu
  │    │    删除单位组 grpTemp
  │    │    返回
  │    └─ 否则: (无)
  └─ 删除单位组 grpTemp
```

</details>

<details id="trigger-04_014_寒冰炽炎合体技能">
<summary><strong>📌 寒冰炽炎合体技能</strong> <code>04_014_寒冰炽炎合体技能</code></summary>

```text
触发器: 寒冰炽炎合体技能 (区域/禁地) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

</details>

<details id="trigger-04_015_HeTiEnter1">
<summary><strong>📌 HeTiEnter1</strong> <code>04_015_HeTiEnter1</code></summary>

```text
触发器: HeTiEnter1 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct_____________________01)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  ├─ (触发单位()类型ID) == N00I
  └─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
动作
  ├─ 设置 bHeTiJi[1] = true
  ├─ 设置 uHeTiJi[11] = 触发单位()
  ├─ 显示文本→(触发单位()的所有者): 0
  └─ 如果
       ├─ 条件: bHeTiJi[2] == TRUE
       ├─ 则
       │    运行计时器 tHeTiJi (一次性, 30.00s)
       └─ 否则: (无)
```

</details>

<details id="trigger-04_016_HeTiOut1">
<summary><strong>📌 HeTiOut1</strong> <code>04_016_HeTiOut1</code></summary>

```text
触发器: HeTiOut1 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct_____________________01)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ (触发单位()类型ID) == N00I
动作
  ├─ 设置 bHeTiJi[1] = false
  ├─ 设置 uHeTiJi[11] = UnitNull
  └─ 暂停计时器 tHeTiJi
```

</details>

<details id="trigger-04_017_HeTiEnter2">
<summary><strong>📌 HeTiEnter2</strong> <code>04_017_HeTiEnter2</code></summary>

```text
触发器: HeTiEnter2 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct_____________________02)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  ├─ (触发单位()类型ID) == N007
  └─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
动作
  ├─ 设置 bHeTiJi[2] = true
  ├─ 设置 uHeTiJi[12] = 触发单位()
  ├─ 显示文本→(触发单位()的所有者): 0
  └─ 如果
       ├─ 条件: bHeTiJi[1] == TRUE
       ├─ 则
       │    运行计时器 tHeTiJi (一次性, 30.00s)
       └─ 否则: (无)
```

</details>

<details id="trigger-04_018_HeTiOut2">
<summary><strong>📌 HeTiOut2</strong> <code>04_018_HeTiOut2</code></summary>

```text
触发器: HeTiOut2 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct_____________________01)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ (触发单位()类型ID) == N007
动作
  ├─ 设置 bHeTiJi[2] = false
  ├─ 设置 uHeTiJi[12] = UnitNull
  └─ 暂停计时器 tHeTiJi
```

</details>

<details id="trigger-04_019_HeTiCheck">
<summary><strong>📌 HeTiCheck</strong> <code>04_019_HeTiCheck</code></summary>

```text
触发器: HeTiCheck (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tHeTiJi 到期
条件
  ├─ uHeTiJi[11] == UnitNull
  └─ uHeTiJi[12] == UnitNull
动作
  ├─ 设置 uHeTiJi[1] = uHeTiJi[11]
  ├─ 设置 uHeTiJi[2] = uHeTiJi[12]
  ├─ 设置 uHeTiJi[11] = UnitNull
  ├─ 设置 uHeTiJi[12] = UnitNull
  ├─ 显示文本→grpOnline: "TRIGSTR_4874"
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  └─ 销毁触发器(自身)
```

</details>

