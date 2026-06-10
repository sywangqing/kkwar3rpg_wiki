---
title: 神墓 2.7C — 🗂️ 00 初始化与变量
category: kk-triggers
slug: shenmu/00-init
description: 全局变量/初始化触发器/玩家设置/刷怪点配置
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 🗂️ 00 初始化与变量

> 全局变量/初始化触发器/玩家设置/刷怪点配置

**共 8 个触发器**

## 📑 触发器目录

- [InitVariable](#trigger-00_000_InitVariable)
- [InitMapSetting](#trigger-00_001_InitMapSetting)
- [LVChoose](#trigger-00_002_LVChoose)
- [LVSet](#trigger-00_003_LVSet)
- [LVSetHigh](#trigger-00_004_LVSetHigh)
- [LVSetBossTS](#trigger-00_005_LVSetBossTS)
- [CreateQuest](#trigger-00_006_CreateQuest)
- [CreateLeaderboard](#trigger-00_007_CreateLeaderboard)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-00_000_InitVariable">
<summary><strong>📌 InitVariable</strong> <code>00_000_InitVariable</code></summary>

```text
触发器: InitVariable (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(0.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 循环整数A 1→5: 设置变量(sPlayerInitName[循环整数A], (玩家名:玩家循环整数A))
  ├─ ── 开启刷怪等待计时器 ──
  ├─ 运行计时器 tNextWave (一次性, 120.00s)
  ├─ 计时器窗口: tNextWave 标题="TRIGSTR_969"
  ├─ 设置 dNextWave = 最后创建的计时器窗口()
  ├─ ── 刷怪点设置 ──
  ├─ 设置 pShuaGuai[1] = (区域gg_rct__________1中心)
  ├─ 设置 pShuaGuai[2] = (区域gg_rct__________2中心)
  ├─ 设置 pShuaGuai[3] = (区域gg_rct__________3中心)
  ├─ 设置 pShuaGuai[4] = (区域gg_rct__________4中心)
  ├─ 设置 pShuaGuai[5] = (区域gg_rct_______01中心)
  ├─ 设置 pShuaGuai[6] = (区域gg_rct_______02中心)
  ├─ 设置 pShuaGuai[7] = (区域gg_rct_______1中心)
  ├─ 设置 pShuaGuai[8] = (区域gg_rct_______2中心)
  ├─ 设置 pShuaGuai[9] = (区域gg_rct_______a中心)
  ├─ 设置 pShuaGuai[10] = (区域gg_rct___________________c中心)
  ├─ ── 传送点设置 ──
  ├─ 设置 pShuaGuai[11] = (区域gg_rct___________________0000中心)
  ├─ 设置 pShuaGuai[12] = (区域gg_rct_____________0中心)
  ├─ 设置 pShuaGuai[13] = (区域gg_rct___________________u中心)
  ├─ 设置 pShuaGuai[14] = (区域gg_rct_______a中心)
  ├─ 设置 pShuaGuai[15] = (区域gg_rct_____________g中心)
  ├─ ── 练功传送点 ──
  ├─ 设置 pShuaGuai[21] = (区域gg_rct______________01中心)
  ├─ 设置 pShuaGuai[22] = (区域gg_rct_____________02中心)
  ├─ 设置 pShuaGuai[23] = (区域gg_rct_____________03中心)
  ├─ 设置 pShuaGuai[24] = (区域gg_rct_____________04中心)
  ├─ 设置 pShuaGuai[25] = (区域gg_rct_____________05中心)
  ├─ 设置 pShuaGuai[26] = (区域gg_rct_____________06中心)
  ├─ 设置 pShuaGuai[27] = (区域gg_rct_____________07中心)
  ├─ ── 野外boss复活点 ──
  ├─ 设置 pShuaGuai[31] = (区域gg_rct_______004中心)
  ├─ 设置 pShuaGuai[32] = (区域gg_rct_______e中心)
  ├─ 设置 pShuaGuai[33] = (区域gg_rct__________f中心)
  ├─ 设置 pShuaGuai[34] = (区域gg_rct_____________a中心)
  ├─ 设置 pShuaGuai[35] = (区域gg_rct_____________00000000中心)
  ├─ 设置 pShuaGuai[41] = (区域gg_rct_____________1中心)
  ├─ 设置 pShuaGuai[42] = (区域gg_rct_____________2中心)
  ├─ 设置 pShuaGuai[43] = (区域gg_rct_____________3中心)
  ├─ 设置 pShuaGuai[44] = (区域gg_rct__________d中心)
  ├─ ── 设置复活点 ──
  ├─ 设置 pFuHuo = (gg_unit_H00F_0003的位置)
  ├─ ── 设置回城点 ──
  ├─ 设置 pHG = (区域gg_rct_____________0000中心)
  ├─ ── 设置墓地魔气 ──
  ├─ 设置 uMuDiMoQi[1] = gg_unit_ushd_0073
  ├─ 设置 uMuDiMoQi[2] = gg_unit_ushd_0075
  ├─ 设置 uMuDiMoQi[3] = gg_unit_ushd_0074
  ├─ 设置 uMuDiMoQi[4] = gg_unit_ushd_0076
  ├─ ── 设置特殊怪进攻点 ──
  ├─ 设置 pTeShuGuai[1] = 可破坏物位置(gg_dest_OTsp_2663)
  ├─ 设置 pTeShuGuai[2] = 可破坏物位置(gg_dest_OTsp_2662)
  ├─ ── 设置特殊怪类型 ──
  ├─ 设置 uTeShuGuai[1] = odoc
  ├─ 设置 uTeShuGuai[2] = otbr
  ├─ 设置 uTeShuGuai[3] = otbr
  ├─ 设置 uTeShuGuai[4] = opeo
  ├─ ── 英雄类型 ──
  ├─ 设置 uHeroType[1] = N000
  ├─ 设置 uHeroType[2] = N00J
  ├─ 设置 uHeroType[3] = N00L
  ├─ 设置 uHeroType[4] = N007
  ├─ 设置 uHeroType[5] = N00K
  ├─ 设置 uHeroType[6] = N00I
  ├─ 设置 uHeroType[7] = H000
  ├─ 设置 uHeroType[8] = O000
  ├─ 设置 uHeroType[9] = U004
  ├─ 设置 uHeroType[10] = U000
  ├─ 设置 uHeroType[11] = H007
  ├─ 设置 uHeroType[12] = E000
  ├─ 设置 uHeroType[13] = N00U
  ├─ 设置 uHeroType[14] = N00W
  ├─ 设置 uHeroType[20] = N00Y
  ├─ ── 准神技能 ──
  ├─ 设置 aZhunShen[1] = A06J
  ├─ 设置 aZhunShen[2] = A077
  ├─ 设置 aZhunShen[3] = A085
  ├─ 设置 aZhunShen[4] = A08J
  ├─ 设置 aZhunShen[5] = A082
  ├─ 设置 aZhunShen[6] = A00L
  ├─ 设置 aZhunShen[7] = A03C
  ├─ 设置 aZhunShen[8] = A06S
  ├─ 设置 aZhunShen[9] = A08Z
  ├─ 设置 aZhunShen[10] = A07M
  ├─ 设置 aZhunShen[11] = A07P
  ├─ 设置 aZhunShen[12] = A06W
  ├─ 设置 aZhunShen[13] = A0A2
  ├─ 设置 aZhunShen[14] = A0AK
  ├─ ── 天赋技能 ──
  ├─ 设置 aTianFu[1] = A045
  ├─ 设置 aTianFu[2] = A078
  ├─ 设置 aTianFu[3] = A084
  ├─ 设置 aTianFu[4] = A005
  ├─ 设置 aTianFu[5] = A07T
  ├─ 设置 aTianFu[6] = S000
  ├─ 设置 aTianFu[7] = A03O
  ├─ 设置 aTianFu[8] = A03N
  ├─ 设置 aTianFu[9] = A04A
  ├─ 设置 aTianFu[10] = A03P
  ├─ 设置 aTianFu[11] = A04Z
  ├─ 设置 aTianFu[12] = A00N
  ├─ 设置 aTianFu[13] = A09I
  ├─ 设置 aTianFu[14] = A0A5
  ├─ ── 自学技能 ──
  ├─ 设置 aHeroAbilityList[1] = A002
  ├─ 设置 aHeroAbilityList[2] = A07C
  ├─ 设置 aHeroAbilityList[3] = A086
  ├─ 设置 aHeroAbilityList[4] = A006
  ├─ 设置 aHeroAbilityList[5] = A09D
  ├─ 设置 aHeroAbilityList[6] = A08P
  ├─ 设置 aHeroAbilityList[7] = A07Q
  ├─ 设置 aHeroAbilityList[8] = A008
  ├─ 设置 aHeroAbilityList[9] = A05C
  ├─ 设置 aHeroAbilityList[10] = A00I
  ├─ 设置 aHeroAbilityList[11] = A04X
  ├─ 设置 aHeroAbilityList[12] = A00M
  ├─ 设置 aHeroAbilityList[13] = A09O
  ├─ 设置 aHeroAbilityList[14] = A0AG
  ├─ 设置 aHeroAbilityList[101] = A001
  ├─ 设置 aHeroAbilityList[102] = A07B
  ├─ 设置 aHeroAbilityList[103] = A088
  ├─ 设置 aHeroAbilityList[104] = A03Q
  ├─ 设置 aHeroAbilityList[105] = A07V
  ├─ 设置 aHeroAbilityList[106] = A08Q
  ├─ 设置 aHeroAbilityList[107] = A00D
  ├─ 设置 aHeroAbilityList[108] = A00A
  ├─ 设置 aHeroAbilityList[109] = A08V
  ├─ 设置 aHeroAbilityList[110] = A00H
  ├─ 设置 aHeroAbilityList[111] = A04V
  ├─ 设置 aHeroAbilityList[112] = A06U
  ├─ 设置 aHeroAbilityList[113] = A09R
  ├─ 设置 aHeroAbilityList[114] = A0AH
  ├─ 设置 aHeroAbilityList[201] = A06H
  ├─ 设置 aHeroAbilityList[202] = A079
  ├─ 设置 aHeroAbilityList[203] = A089
  ├─ 设置 aHeroAbilityList[204] = A007
  ├─ 设置 aHeroAbilityList[205] = A0A4
  ├─ 设置 aHeroAbilityList[206] = A08R
  ├─ 设置 aHeroAbilityList[207] = A00B
  ├─ 设置 aHeroAbilityList[208] = A000
  ├─ 设置 aHeroAbilityList[209] = A08W
  ├─ 设置 aHeroAbilityList[210] = A06X
  ├─ 设置 aHeroAbilityList[211] = A05R
  ├─ 设置 aHeroAbilityList[212] = A00K
  ├─ 设置 aHeroAbilityList[213] = A0A0
  ├─ 设置 aHeroAbilityList[214] = A0AI
  ├─ 设置 aHeroAbilityList[301] = A07N
  ├─ 设置 aHeroAbilityList[302] = A07F
  ├─ 设置 aHeroAbilityList[303] = A08A
  ├─ 设置 aHeroAbilityList[304] = A03S
  ├─ 设置 aHeroAbilityList[305] = A07W
  ├─ 设置 aHeroAbilityList[306] = A08T
  ├─ 设置 aHeroAbilityList[307] = A00F
  ├─ 设置 aHeroAbilityList[308] = A009
  ├─ 设置 aHeroAbilityList[309] = A08X
  ├─ 设置 aHeroAbilityList[310] = A00J
  ├─ 设置 aHeroAbilityList[311] = A07O
  ├─ 设置 aHeroAbilityList[312] = A03B
  ├─ 设置 aHeroAbilityList[313] = A09Y
  ├─ 设置 aHeroAbilityList[314] = A0AJ
  ├─ 设置 aHeroAbilityList[401] = A06I
  ├─ 设置 aHeroAbilityList[402] = A07E
  ├─ 设置 aHeroAbilityList[403] = A08C
  ├─ 设置 aHeroAbilityList[404] = A08H
  ├─ 设置 aHeroAbilityList[405] = A081
  ├─ 设置 aHeroAbilityList[406] = A03R
  ├─ 设置 aHeroAbilityList[407] = A03A
  ├─ 设置 aHeroAbilityList[408] = A03E
  ├─ 设置 aHeroAbilityList[409] = A08Y
  ├─ 设置 aHeroAbilityList[410] = A03D
  ├─ 设置 aHeroAbilityList[411] = A057
  ├─ 设置 aHeroAbilityList[412] = A06V
  ├─ 设置 aHeroAbilityList[413] = A0A1
  ├─ 设置 aHeroAbilityList[414] = A0AF
  ├─ 设置 bHeroAbilityUseable[1] = true
  ├─ 设置 bHeroAbilityUseable[11] = true
  ├─ 设置 bHeroAbilityUseable[103] = true
  ├─ 设置 bHeroAbilityUseable[106] = true
  ├─ 设置 bHeroAbilityUseable[309] = true
  ├─ 设置 bHeroAbilityUseable[312] = true
  ├─ 设置 bHeroAbilityUseable[402] = true
  ├─ 设置 bHeroAbilityUseable[405] = true
  ├─ 设置 bHeroAbilityUseable[406] = true
  ├─ 设置 bHeroAbilityUseable[407] = true
  ├─ 设置 bHeroAbilityUseable[413] = true
  ├─ ── 设置进攻怪类型 ──
  ├─ 设置 uJinGong[1] = hfoo
  ├─ 设置 uJinGong[2] = hkni
  ├─ 设置 uJinGong[3] = hrif
  ├─ 设置 uJinGong[4] = hmtm
  ├─ 设置 uJinGong[5] = hgyr
  ├─ 设置 uJinGong[6] = hgry
  ├─ 设置 uJinGong[7] = hmpr
  ├─ 设置 uJinGong[8] = hsor
  ├─ 设置 uJinGong[9] = hmtt
  ├─ 设置 uJinGong[10] = hspt
  ├─ 设置 uJinGong[11] = hdhw
  ├─ 设置 uJinGong[12] = nnsw
  ├─ 设置 uJinGong[13] = nnmg
  ├─ 设置 uJinGong[14] = nwgs
  ├─ 设置 uJinGong[15] = nsnp
  ├─ 设置 uJinGong[16] = nmyr
  ├─ 设置 uJinGong[17] = nnrg
  ├─ 设置 uJinGong[18] = nhyc
  ├─ 设置 uJinGong[19] = ogru
  ├─ 设置 uJinGong[20] = orai
  ├─ 设置 uJinGong[21] = otau
  ├─ 设置 uJinGong[22] = ohun
  ├─ 设置 uJinGong[23] = ocat
  ├─ 设置 uJinGong[24] = okod
  ├─ 设置 uJinGong[25] = oshm
  ├─ 设置 uJinGong[26] = earc
  ├─ 设置 uJinGong[27] = esen
  ├─ 设置 uJinGong[28] = edry
  ├─ 设置 uJinGong[29] = ebal
  ├─ 设置 uJinGong[30] = ehip
  ├─ 设置 uJinGong[31] = echm
  ├─ 设置 uJinGong[32] = edot
  ├─ 设置 uJinGong[33] = edoc
  ├─ 设置 uJinGong[34] = emtg
  ├─ 设置 uJinGong[35] = efdr
  ├─ 设置 uJinGong[36] = owyv
  ├─ ── 设置进攻怪技能 ──
  ├─ 设置 aJinGongGuai[1] = Adef
  ├─ 设置 aJinGongGuai[2] = Adef
  ├─ 设置 aJinGongGuai[3] = ACat
  ├─ 设置 aJinGongGuai[4] = Adef
  ├─ 设置 aJinGongGuai[5] = Ainf
  ├─ 设置 aJinGongGuai[6] = Adef
  ├─ 设置 aJinGongGuai[7] = ACat
  ├─ 设置 aJinGongGuai[8] = Aslo
  ├─ 设置 aJinGongGuai[9] = Ablo
  ├─ 设置 aJinGongGuai[10] = Amdf
  ├─ 设置 aJinGongGuai[11] = ACat
  ├─ 设置 aJinGongGuai[12] = Acrs
  ├─ 设置 aJinGongGuai[13] = Afae
  ├─ 设置 aJinGongGuai[14] = Ablo
  ├─ 设置 aJinGongGuai[15] = Ainf
  ├─ 设置 aJinGongGuai[16] = Aroa
  ├─ 设置 aJinGongGuai[17] = Awar
  ├─ 设置 aJinGongGuai[18] = Aegr
  ├─ 设置 aJinGongGuai[19] = Awar
  ├─ 设置 aJinGongGuai[20] = Aakb
  ├─ 设置 aJinGongGuai[21] = Awar
  ├─ 设置 aJinGongGuai[22] = Aegr
  ├─ 设置 aJinGongGuai[23] = Ainf
  ├─ 设置 aJinGongGuai[24] = Aakb
  ├─ 设置 aJinGongGuai[25] = Ablo
  ├─ 设置 aJinGongGuai[26] = ACat
  ├─ 设置 aJinGongGuai[27] = ACat
  ├─ 设置 aJinGongGuai[28] = Aakb
  ├─ 设置 aJinGongGuai[29] = ACat
  ├─ 设置 aJinGongGuai[30] = Acri
  ├─ 设置 aJinGongGuai[31] = ACat
  ├─ 设置 aJinGongGuai[32] = Aroa
  ├─ 设置 aJinGongGuai[33] = Aroa
  ├─ 设置 aJinGongGuai[34] = Awar
  ├─ 设置 aJinGongGuai[35] = Ainf
  ├─ 设置 aJinGongGuai[36] = Adef
  ├─ ── 设置进攻怪技能---高难度 ──
  ├─ 设置 aJinGongGuaiHard[1] = Ablo
  ├─ 设置 aJinGongGuaiHard[2] = Ainf
  ├─ 设置 aJinGongGuaiHard[3] = Ainf
  ├─ 设置 aJinGongGuaiHard[4] = Aegr
  ├─ 设置 aJinGongGuaiHard[5] = Aslo
  ├─ 设置 aJinGongGuaiHard[6] = Amdf
  ├─ 设置 aJinGongGuaiHard[7] = Afae
  ├─ 设置 aJinGongGuaiHard[8] = Aakb
  ├─ 设置 aJinGongGuaiHard[9] = Afae
  ├─ 设置 aJinGongGuaiHard[10] = Acrs
  ├─ 设置 aJinGongGuaiHard[11] = Amdf
  ├─ 设置 aJinGongGuaiHard[12] = Ainf
  ├─ 设置 aJinGongGuaiHard[13] = Awar
  ├─ 设置 aJinGongGuaiHard[14] = Acri
  ├─ 设置 aJinGongGuaiHard[15] = Afae
  ├─ 设置 aJinGongGuaiHard[16] = Aakb
  ├─ 设置 aJinGongGuaiHard[17] = Aegr
  ├─ 设置 aJinGongGuaiHard[18] = Afae
  ├─ 设置 aJinGongGuaiHard[19] = Ablo
  ├─ 设置 aJinGongGuaiHard[20] = Awar
  ├─ 设置 aJinGongGuaiHard[21] = Acri
  ├─ 设置 aJinGongGuaiHard[22] = Acrs
  ├─ 设置 aJinGongGuaiHard[23] = Ablo
  ├─ 设置 aJinGongGuaiHard[24] = Acri
  ├─ 设置 aJinGongGuaiHard[25] = Aegr
  ├─ 设置 aJinGongGuaiHard[26] = Afae
  ├─ 设置 aJinGongGuaiHard[27] = Ainf
  ├─ 设置 aJinGongGuaiHard[28] = Adef
  ├─ 设置 aJinGongGuaiHard[29] = Ablo
  ├─ 设置 aJinGongGuaiHard[30] = Acrs
  ├─ 设置 aJinGongGuaiHard[31] = Aegr
  ├─ 设置 aJinGongGuaiHard[32] = Awar
  ├─ 设置 aJinGongGuaiHard[33] = Awar
  ├─ 设置 aJinGongGuaiHard[34] = Aegr
  ├─ 设置 aJinGongGuaiHard[35] = Aegr
  ├─ 设置 aJinGongGuaiHard[36] = Aegr
  ├─ ── 设置法则英雄颜色 ──
  ├─ 设置 iFaZeColor[1] = 0
  ├─ 设置 iFaZeColor[2] = 255
  ├─ 设置 iFaZeColor[3] = 255
  ├─ 设置 iFaZeColor[4] = 255
  ├─ 设置 iFaZeColor[5] = 255
  ├─ 设置 iFaZeColor[6] = 0
  ├─ 设置 iFaZeColor[7] = 255
  ├─ 设置 iFaZeColor[8] = 255
  ├─ 设置 iFaZeColor[9] = 255
  ├─ 设置 iFaZeColor[10] = 255
  ├─ 设置 iFaZeColor[11] = 0
  ├─ 设置 iFaZeColor[12] = 255
  ├─ 设置 iFaZeColor[13] = 0
  ├─ 设置 iFaZeColor[14] = 255
  ├─ 设置 iFaZeColor[15] = 0
  ├─ 设置 iFaZeColor[16] = 255
  ├─ 设置 iFaZeColor[17] = 0
  ├─ 设置 iFaZeColor[18] = 0
  ├─ 设置 iFaZeColor[19] = 255
  ├─ 设置 iFaZeColor[20] = 255
  ├─ ── 设置闪电类型 ──
  ├─ 设置 lgtType[1] = LightningTypeCLPB
  ├─ 设置 lgtType[2] = LightningTypeCLSB
  ├─ 设置 lgtType[3] = LightningTypeDRAB
  ├─ 设置 lgtType[4] = LightningTypeDRAL
  ├─ 设置 lgtType[5] = LightningTypeDRAM
  ├─ 设置 lgtType[6] = LightningTypeAFOD
  ├─ 设置 lgtType[7] = LightningTypeFORK
  ├─ 设置 lgtType[8] = LightningTypeHWPB
  ├─ 设置 lgtType[9] = LightningTypeHWSB
  ├─ 设置 lgtType[10] = LightningTypeCHIM
  ├─ 设置 lgtType[11] = LightningTypeLEAS
  ├─ 设置 lgtType[12] = LightningTypeMBUR
  ├─ 设置 lgtType[13] = LightningTypeMFPB
  ├─ 设置 lgtType[14] = LightningTypeSPLK
  ├─ ── 设置NPC对话 ──
  ├─ 设置 sXiongMao[0] = "|cff00ffff小熊猫：世间真正的宝物从不需要获得我们的认可，这个东西是我多年来的心血，若是此生有缘能看到它饮尽天下魔血的形态，我死而无憾。|r"
  ├─ 设置 sXiongMao[1] = "|cff00ffff小熊猫：这材料不合格，所以你懂的，再拿个来。|r"
  ├─ 设置 sXiongMao[2] = "|cffffcc00小熊猫：好像老是有什么东西在盯着我看……|r"
  ├─ 设置 sXiongMao[3] = "|cffffcc00小熊猫：一念起，万水千山；一念灭，沧海桑田。|r"
  ├─ 设置 sXiongMao[4] = "|cffffcc00小熊猫：我就待在这块地方，装做在思考，没人看的出来……|r"
  ├─ 设置 sXiongMao[5] = "|cffffcc00小熊猫：我觉得这刀太钝了，切个铁块都要用一成力气。。。|r"
  ├─ 设置 sXiongMao[6] = "|cffffcc00小熊猫：好羡慕你啊，为什么你们可以到处跑呢？这真是令人费解的问题。。。|r"
  ├─ 设置 sXiongMao[11] = "|cffffcc00三清：恩。。。。剑尊。。贱尊。。好久不见了啊。自从俺被作者剥夺了作为隐藏英雄的资格后俺的日子可是难过得紧啊。据说作者非常讨厌你啊！|r"
  ├─ 设置 sXiongMao[12] = "|cffffcc00三清：小姐！现在大家都对你乱勾引妖皇严重不满，是不是该收敛一点了！|r"
  ├─ 设置 sXiongMao[13] = "|cffffcc00三清：小姐！虽然你这么风骚的看着我，但是我不得不老实的告诉你，我是未成年的熊猫，还不能化成人形。所以你袒胸露乳的样子对我来说毫无吸引力..."
  ├─ 设置 sXiongMao[14] = "|cffffcc00三清：寒冰来买东西？来来来，别害羞，按照作者给我下的旨意。大叔我会非常照顾你的，绝对不多收半个金币，多和大叔聊聊天，大叔心情好会给宝物..."
  ├─ 设置 sXiongMao[15] = "|cffffcc00三清：你就是那个为了复仇而发誓屠尽火凤凰的家伙吧？有点能耐啊！居然能把凤凰的般涅能力融合到自己的命格当中。当真是了不得的人物。|r"
  ├─ 设置 sXiongMao[16] = "|cffffcc00三清：走过路过不要错过，一份木头一份货，童叟无欺，质量保证。不服……啊不是，不好用的来砍贫道。小美女别看其它地方，大叔给作者QQ你。|r"
  ├─ 设置 sXiongMao[17] = "|cffffcc00三清：干嘛？要神死魔灭的消息？不敢啊！我会被他给删除掉的。落花有意奈何流水无情啊，可怜的孩子。等哪天他从着魔中恢复过来我就给你做媒。|r"
  ├─ 设置 sXiongMao[18] = "|cffffcc00三清：老兄现在混得怎么样了？哇！你果真成为了一个狂人……全是加攻击力的招数。|r"
  ├─ 设置 sXiongMao[19] = "|cffffcc00三清：小子，看你猫头猫脑的外型，莫非是我的传人的传人？|r"
  ├─ 设置 sXiongMao[20] = "|cffffcc00三清：苍龙兄！！！据说你掌握了寂灭那个传说中的邪恶招数，咱们交情这么好，私下教给我吧！我教你大天劫。|r"
  ├─ 设置 sXiongMao[21] = "|cffffcc00三清：黄泉小子，鬼书居然被作者拿走了。老天有眼啊，那么强大的宝物居然被你那么糟蹋。不过你也别生气，那东西给你用你也发挥不出一半的能力。|r"
  ├─ 设置 sXiongMao[22] = "|cffffcc00三清：你再帅、你再酷、女生喜欢的还是我这可爱的熊猫造型，不要嫉妒！这是作者的意思。|r"
  ├─ 设置 sXiongMao[23] = "|cffffcc00三清：富贵？仙人？听说你刚出道的时候过于犀利引得众生不平，现在被打压什么样了！！！|r"
  ├─ 设置 sXiongMao[24] = "|cffffcc00三清：这位霉女你化的妆实在是黑不溜秋，让熊猫我大倒胃口。|r"
  ├─ 设置 sXiongMao[31] = "|cffffcc00听说你对我的敬仰犹如滔滔江水连绵不绝是吗？哎……像我这种具有大智慧的熊猫已经越来越难找了。看在你也相信鼻涕纸的份上，送你个东西把，本来..."
  ├─ 设置 sXiongMao[32] = "|cffffcc00又是十张！离天书下卷越来越近了。|r"
  ├─ 设置 sXiongMao[33] = "|cffffcc00小小熊猫：恩。。。。这些鼻涕纸说不定隐藏着惊天的秘密。|r"
  ├─ 设置 sXiongMao[33] = "|cffffcc00小小熊猫：听说准神之上还有小神通，小神通之上更有大神通，大神通其实和神差不多，但差点什么呢？|r"
  ├─ 设置 sXiongMao[34] = "|cffffcc00小小熊猫：你们一天到晚想成神的都疯了么。。。|r"
  ├─ 设置 sXiongMao[35] = "|cffffcc00小小熊猫：据说你们的小冰龙可以带你们一起飞了，是不是真的？不过看你们还在甩火腿，应该是还没发现这个秘密吧。|r"
  ├─ 设置 sXiongMao[36] = "|cffffcc00小小熊猫：为什么每天晃来晃去就你们几个人的身影呢？|r"
  ├─ 设置 sXiongMao[37] = "|cffffcc00小小熊猫：本无意与众不同，怎奈何品味出众|r"
  ├─ 设置 sXiongMao[41] = "|cffffcc00你欲以剑为奴殊不知剑已奴役你。|r"
  ├─ 设置 sXiongMao[42] = "|cffffcc00顺转千年，物是人非事事休；妖舞阴月，知其圆知其缺不知其圆缺。|r"
  ├─ 设置 sXiongMao[43] = "|cffffcc00吾师常言“世间值与不值不及愿与不愿”|r"
  ├─ 设置 sXiongMao[44] = "|cffffcc00你身上的冰之魂魄只会指引你的憎恨。|r"
  ├─ 设置 sXiongMao[45] = "|cffffcc00即使屠尽天下苍生，失去的亦无法挽回。|r"
  ├─ 设置 sXiongMao[46] = "|cffffcc00传闻世间有一束“火焰”是一切生命的根源|r"
  ├─ 设置 sXiongMao[47] = "|cffffcc00神墓万载，成败一人。怒苍天无眼，恨世人皆盲。|r"
  ├─ 设置 sXiongMao[48] = "|cffffcc00生由天死由命、或许放弃这份永生执念才是正确的选择。|r"
  ├─ 设置 sXiongMao[49] = "|cffffcc00我能感受到你体内只有一魂一魄，你并非一个完整的生灵。|r"
  ├─ 设置 sXiongMao[50] = "|cffffcc00自古邪不能胜正，不知天书绝笔之人是正亦或为邪。|r"
  ├─ 设置 sXiongMao[51] = "|cffffcc00逆乱生死之人、灵魂鬼书的强大你永远不会明白。|r"
  ├─ 设置 sXiongMao[52] = "|cffffcc00生亦何欢，死亦何苦。怜我世人，皆归尘土。潜心参悟一生，终究无法摆脱这份死局。|r"
  ├─ 设置 sXiongMao[53] = "|cffffcc00富贵逼人无人挡，只要有钱，凡间也能做神仙。|r"
  └─ 设置 sXiongMao[54] = "|cffffcc00生生死死已九世，此中执着谁人知？|r"
```

</details>

<details id="trigger-00_001_InitMapSetting">
<summary><strong>📌 InitMapSetting</strong> <code>00_001_InitMapSetting</code></summary>

```text
触发器: InitMapSetting (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(0.10)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 战争迷雾开关: EnabledDisabledEnabled
  ├─ 迷雾遮罩开关: EnabledDisabledEnabled
  ├─ ── 中立单位初始化 ──
  ├─ SetDestructableInvulnerableBJ: gg_dest_LTg3_2661, InvulnerabilityInvulnerable
  ├─ SetDestructableInvulnerableBJ: gg_dest_LTg3_2208, InvulnerabilityInvulnerable
  ├─ SetDestructableInvulnerableBJ: gg_dest_LTg1_0259, InvulnerabilityInvulnerable
  ├─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg1_0259
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, gg_unit_N00N_0054
  ├─ 设置无敌: gg_unit_N00N_0054, InvulnerabilityInvulnerable
  ├─ 播放动画: gg_unit_N00N_0054, "attack walk stand spin"
  ├─ 播放动画: gg_unit_unp2_0034, "birth"
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, gg_unit_H00C_0033
  ├─ 设置无敌: gg_unit_H00C_0033, InvulnerabilityInvulnerable
  ├─ 循环整数A 1→4: 隐藏单位(uMuDiMoQi[循环整数A])
  ├─ SetPlayerFlag: 玩家9(灰), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerAllianceStateBJ: 玩家9(灰), PlayerNA, AllianceSettingAlliedVision
  ├─ SetPlayerAllianceStateBJ: PlayerNA, 玩家9(灰), AllianceSettingAlliedVision
  ├─ 循环整数A 6→10
  │    ├─ 升级玩家科技: 玩家循环整数A, R006, 1
  │    ├─ 升级玩家科技: 玩家循环整数A, R008, 1
  │    └─ 升级玩家科技: 玩家循环整数A, R009, 1
  ├─ 设置 uPlayerHeros[10] = gg_unit_N00N_0054
  ├─ 设置 uPlayerHeros[13] = gg_unit_H001_0087
  ├─ UnitRemoveAbilityBJ: Arav, gg_unit_Hmkg_0067
  ├─ 隐藏单位: gg_unit_nmrr_0068
  ├─ 设置 itemLunHui = 单位携带物品(按类型)(gg_unit_H00F_0003, ajen)
  ├─ 隐藏单位: gg_unit_N00M_0083
  ├─ 隐藏单位: gg_unit_N00E_0104
  ├─ 隐藏单位: gg_unit_N00F_0106
  ├─ 隐藏单位: gg_unit_N00G_0105
  ├─ 设置无敌: gg_unit_nntg_0064, InvulnerabilityInvulnerable
  ├─ 隐藏单位: gg_unit_H002_0094
  ├─ 隐藏单位: gg_unit_N00V_0059
  ├─ 隐藏单位: gg_unit_h00I_0057
  ├─ ── 创建彩灯 ──
  ├─ 如果
  │    ├─ 条件: false == TRUE
  │    ├─ 则
  │    │    设置 rTemp = ((区域最大X(gg_rct_________________065) - 区域最小X(gg_rct_________________065)) / 5.00)
  │    │    循环整数A 0→5
  │    │      ├─ 设置 uTemp = 创建单位(指定坐标)(玩家7(绿), n00Z, (区域最小X(gg_rct_________________065) + (rTemp x (循环整数A转实数))), 区域最小Y(gg_rct_________________065), 0)
  │    │      └─ 设置 uTemp = 创建单位(指定坐标)(玩家7(绿), n00Z, (区域最小X(gg_rct_________________065) + (rTemp x (循环整数A转实数))), 区域最大Y(gg_rct_________________065), 0)
  │    └─ 否则: (无)
  ├─ ── 设置在线玩家组 ──
  ├─ 播放动画: gg_unit_ubon_0001, "birth"
  ├─ AddSpecialEffectTargetUnitBJ: "origin", gg_unit_ubon_0001, TimeAura.mdx
  ├─ 设置 grpUserPlayers = 符合条件的玩家(玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser))
  ├─ 设置 grpOnline = 符合条件的玩家((玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser) 且 玩家槽位状态比较(玩家槽位状态(过滤玩家()), OperatorEqualENE, PlayerSlotStatePlaying)))
  ├─ 设置 grpOffline = 符合条件的玩家((玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser) 且 玩家槽位状态比较(玩家槽位状态(过滤玩家()), OperatorNotEqualENE, PlayerSlotStatePlaying)))
  ├─ 显示文本→grpOnline: "TRIGSTR_5850"
  ├─ 显示文本→grpOnline: "TRIGSTR_5851"
  ├─ 显示文本→grpOnline: "TRIGSTR_5852"
  ├─ ForForceMultiple: grpUserPlayers
  ├─ 循环整数A 1→5
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 玩家控制者比较(玩家控制者类型(玩家循环整数A), OperatorEqualENE, MapControlUser)
  │         │    ├─ 玩家槽位状态比较(玩家槽位状态(玩家循环整数A), OperatorEqualENE, PlayerSlotStatePlaying)
  │         ├─ 则
  │         │    设置 pFirstPlayer = 玩家循环整数A
  │         │    CustomScriptCode: "set bj_forLoopAIndex=8"
  │         └─ 否则: (无)
  ├─ 添加事件到 gg_trg_RandomJiuGui: 玩家聊天(pFirstPlayer, "1573", ChatMatchTypeExact)
  ├─ 添加事件到 gg_trg_ModifyLevel: 玩家聊天(pFirstPlayer, "-nd ", ChatMatchTypeSubstring)
  ├─ 添加事件到 gg_trg_AddBoss: 玩家聊天(pFirstPlayer, "-boss", ChatMatchTypeExact)
  ├─ 添加事件到 gg_trg_AddTeShu: 玩家聊天(pFirstPlayer, "-ts", ChatMatchTypeExact)
  └─ 添加事件到 gg_trg_CleanItem: 玩家聊天(pFirstPlayer, "-qc", ChatMatchTypeExact)
```

</details>

<details id="trigger-00_002_LVChoose">
<summary><strong>📌 LVChoose</strong> <code>00_002_LVChoose</code></summary>

```text
触发器: LVChoose (初始化) [✓] — 难度添加
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(1.10)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ DialogSetMessageBJ: dlgChooseBoss, "TRIGSTR_5810"
  ├─ DialogAddButtonBJ: dlgChooseBoss, "TRIGSTR_5811"
  ├─ 设置 btnChooseBoss[1] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgChooseBoss, "TRIGSTR_5812"
  ├─ 设置 btnChooseBoss[2] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgChooseBoss, "TRIGSTR_5813"
  ├─ 设置 btnChooseBoss[3] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgChooseBoss, "TRIGSTR_5814"
  ├─ 设置 btnChooseBoss[4] = bj_lastCreatedButton
  ├─ DialogSetMessageBJ: dlgHigLevel, "TRIGSTR_5804"
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5805"
  ├─ 设置 btnHighLevel[20] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5806"
  ├─ 设置 btnHighLevel[30] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5807"
  ├─ 设置 btnHighLevel[50] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5808"
  ├─ 设置 btnHighLevel[80] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5809"
  ├─ 设置 btnHighLevel[100] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgHigLevel, "TRIGSTR_5539"
  ├─ 设置 btnHighLevel[101] = bj_lastCreatedButton
  ├─ DialogSetMessageBJ: dlgNanDu, "TRIGSTR_2838"
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_2839"
  ├─ 设置 btnNanDu[1] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_2840"
  ├─ 设置 btnNanDu[3] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_2841"
  ├─ 设置 btnNanDu[5] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_2842"
  ├─ 设置 btnNanDu[8] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_2843"
  ├─ 设置 btnNanDu[10] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: dlgNanDu, "TRIGSTR_009"
  ├─ 设置 btnNanDu[0] = bj_lastCreatedButton
  └─ DialogDisplay: pFirstPlayer, dlgNanDu, ShowHideShow
```

</details>

<details id="trigger-00_003_LVSet">
<summary><strong>📌 LVSet</strong> <code>00_003_LVSet</code></summary>

```text
触发器: LVSet (初始化) [✓] — 难度选择
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(dlgNanDu)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 循环整数A 1→20
  │    └─ 如果
  │         ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnNanDu[循环整数A()])
  │         ├─ 则
  │         │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), PlayerNA
  │         │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), PlayerNA
  │         │    SetPlayerTechResearchedSwap: R004, 循环整数A(), 玩家8(粉)
  │         │    SetPlayerTechResearchedSwap: R003, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: R004, 循环整数A(), PlayerNA
  │         │    显示文本→grpOnline: 自定义代码(" GetPlayerName(GetTriggerPlayer()) + "选择了|cffcc00ff难度|r"+ I2S(GetForLoopIndex...")
  │         │    MultiboardSetTitleText: TopBoard, "神之墓地2.7C 难度" + (循环整数A转字符串)
  │         │    DialogDisplay: pFirstPlayer, dlgChooseBoss, ShowHideShow
  │         │    返回
  │         └─ 否则: (无)
  └─ 如果
       ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnNanDu[0])
       ├─ 则
       │    DialogDisplay: pFirstPlayer, dlgHigLevel, ShowHideShow
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-00_004_LVSetHigh">
<summary><strong>📌 LVSetHigh</strong> <code>00_004_LVSetHigh</code></summary>

```text
触发器: LVSetHigh (初始化) [✓] — 难度选择
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(dlgHigLevel)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 循环整数A 1→100
  │    └─ 如果
  │         ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnHighLevel[循环整数A])
  │         ├─ 则
  │         │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), PlayerNA
  │         │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), PlayerNA
  │         │    SetPlayerTechResearchedSwap: R004, 循环整数A(), 玩家8(粉)
  │         │    SetPlayerTechResearchedSwap: R003, 循环整数A(), 玩家9(灰)
  │         │    SetPlayerTechResearchedSwap: R004, 循环整数A(), PlayerNA
  │         │    显示文本→grpOnline: 自定义代码(" GetPlayerName(GetTriggerPlayer()) + "选择了|cffcc00ff难度|r"+ I2S(GetForLoopIndex...")
  │         │    MultiboardSetTitleText: TopBoard, "神之墓地2.7C 难度" + (循环整数A转字符串)
  │         │    如果
  │         │      ├─ 条件: 循环整数A OperatorGreater 90
  │         │      ├─ 则
  │         │      │    设置技能等级: gg_unit_Uclc_0123, A09M, (循环整数A - 90)
  │         │      └─ 否则: (无)
  │         │    DialogDisplay: pFirstPlayer, dlgChooseBoss, ShowHideShow
  │         │    返回
  │         └─ 否则: (无)
  ├─ SetPlayerTechResearchedSwap: Rhme, 100, 玩家9(灰)
  ├─ SetPlayerTechResearchedSwap: Rhme, 100, PlayerNA
  ├─ SetPlayerTechResearchedSwap: Rhar, 100, 玩家9(灰)
  ├─ SetPlayerTechResearchedSwap: Rhar, 100, PlayerNA
  ├─ SetPlayerTechResearchedSwap: R004, 100, 玩家8(粉)
  ├─ SetPlayerTechResearchedSwap: R003, 100, 玩家9(灰)
  ├─ SetPlayerTechResearchedSwap: R004, 100, PlayerNA
  ├─ 显示文本→grpOnline: 自定义代码("GetPlayerName(GetTriggerPlayer()) + "选择了|cffcc00ff难度|r【寂寞如雪】"")
  ├─ MultiboardSetTitleText: TopBoard, "TRIGSTR_5897"
  ├─ 设置技能等级: gg_unit_Uclc_0123, A09M, 10
  ├─ 设置 bXianFeng = true
  ├─ 设置 uXianFeng[1] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[2] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[3] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 设置 uXianFeng[4] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  ├─ 循环整数A 1→4
  │    ├─ SetHeroLevel: uXianFeng[循环整数A()], 5, ShowHideHide
  │    ├─ SelectHeroSkill: uXianFeng[循环整数A()], A074
  │    ├─ SelectHeroSkill: uXianFeng[循环整数A()], A073
  │    ├─ SelectHeroSkill: uXianFeng[循环整数A()], A075
  │    └─ SelectHeroSkill: uXianFeng[循环整数A()], A076
  ├─ 设置 bTeShu = true
  ├─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
  ├─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
  ├─ 关闭触发器 gg_trg_TFHQ
  └─ 返回
```

</details>

<details id="trigger-00_005_LVSetBossTS">
<summary><strong>📌 LVSetBossTS</strong> <code>00_005_LVSetBossTS</code></summary>

```text
触发器: LVSetBossTS (初始化) [✓] — 难度选择
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(dlgChooseBoss)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnChooseBoss[2])
  │    │    ├─ bXianFeng == TRUE
  │    ├─ 则
  │    │    设置 bXianFeng = true
  │    │    显示文本→grpOnline: "TRIGSTR_5793"
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
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnChooseBoss[3])
  │    │    ├─ bTeShu == TRUE
  │    ├─ 则
  │    │    显示文本→grpOnline: "TRIGSTR_5795"
  │    │    设置 bTeShu = true
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
  │    │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnChooseBoss[4])
       ├─ 则
       │    如果
       │      ├─ 条件: bXianFeng == TRUE
       │      ├─ 则
       │      │    设置 bXianFeng = true
       │      │    显示文本→grpOnline: "TRIGSTR_5798"
       │      │    设置 uXianFeng[1] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
       │      │    设置 uXianFeng[2] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
       │      │    设置 uXianFeng[3] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
       │      │    设置 uXianFeng[4] = 创建单位(指定坐标)(玩家9(灰), U006, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
       │      │    循环整数A 1→4
       │      │      ├─ SetHeroLevel: uXianFeng[循环整数A()], 5, ShowHideHide
       │      │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A074
       │      │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A073
       │      │      ├─ SelectHeroSkill: uXianFeng[循环整数A()], A075
       │      │      └─ SelectHeroSkill: uXianFeng[循环整数A()], A076
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: bTeShu == TRUE
       │      ├─ 则
       │      │    显示文本→grpOnline: "TRIGSTR_5797"
       │      │    设置 bTeShu = true
       │      │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
       │      │    ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
       │      └─ 否则: (无)
       │    返回
       └─ 否则: (无)
```

</details>

<details id="trigger-00_006_CreateQuest">
<summary><strong>📌 CreateQuest</strong> <code>00_006_CreateQuest</code></summary>

```text
触发器: CreateQuest (初始化) [✓] — 任务创建，效果创建
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(1.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1084", "TRIGSTR_1085", ReplaceableTextures\CommandButtons\BTNTornado.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1008", "TRIGSTR_1009", Buildings\Other\TempArtB\BTNTempB.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1014", "TRIGSTR_1015", Buildings\Other\TempArtB\BTNTempB.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_4602", "TRIGSTR_4605", Buildings\Other\TempArtB\BTNTempB.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5135", "TRIGSTR_5572", ReplaceableTextures\CommandButtons\BTNMetamorphosis.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5573", "TRIGSTR_5574", ReplaceableTextures\CommandButtons\BTNWisp.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5575", "TRIGSTR_5576", ReplaceableTextures\CommandButtons\BTNChaosGrom.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5577", "TRIGSTR_5606", ReplaceableTextures\CommandButtons\BTNNagaWeaponUp3.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5652", "TRIGSTR_5653", ReplaceableTextures\CommandButtons\BTNBloodMage2.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_158", "TRIGSTR_269", ReplaceableTextures\CommandButtons\BTNSeaTurtleRed.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5650", "TRIGSTR_5651", ReplaceableTextures\CommandButtons\BTNOrbOfFire.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_5884", "TRIGSTR_5891", ReplaceableTextures\CommandButtons\BTNCloakOfFlames.blp
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_1016", "TRIGSTR_1017", ReplaceableTextures\CommandButtons\BTNDeathAndDecay.blp
  ├─ 设置 quests[1] = bj_lastCreatedQuest
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_1018", "TRIGSTR_1019", ReplaceableTextures\CommandButtons\BTNArthas.blp
  ├─ 设置 quests[2] = bj_lastCreatedQuest
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_1020", "TRIGSTR_1021", ReplaceableTextures\CommandButtons\BTNDeathAndDecay.blp
  ├─ 设置 quests[3] = bj_lastCreatedQuest
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_1043", "TRIGSTR_1044", ReplaceableTextures\CommandButtons\BTNDeathAndDecay.blp
  ├─ 设置 quests[4] = bj_lastCreatedQuest
  ├─ 创建任务: QuestTypeOptUndiscovered, "TRIGSTR_135", "TRIGSTR_2803", ReplaceableTextures\CommandButtons\BTNDeathAndDecay.blp
  ├─ 设置 quests[5] = bj_lastCreatedQuest
  ├─ FlashQuestDialogButtonBJ
  └─ 销毁触发器(自身)
```

</details>

<details id="trigger-00_007_CreateLeaderboard">
<summary><strong>📌 CreateLeaderboard</strong> <code>00_007_CreateLeaderboard</code></summary>

```text
触发器: CreateLeaderboard (初始化) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 注册一次性计时器事件(0.50)
条件
  └─ 无
动作
  ├─ CreateMultiboardBJ: 5, 6, "神之墓地2.7C 难度" + (玩家科技等级(Rhme, 玩家9(灰))转字符串)
  ├─ 设置 TopBoard = 最后创建的排行榜()
  ├─ 排行榜 TopBoard[1,1] = "TRIGSTR_1116"
  ├─ 排行榜 TopBoard[2,1] = "TRIGSTR_1126"
  ├─ 排行榜 TopBoard[3,1] = "TRIGSTR_1127"
  ├─ 排行榜 TopBoard[4,1] = "TRIGSTR_1128"
  ├─ 排行榜 TopBoard[5,1] = "TRIGSTR_1129"
  ├─ 循环整数A 2→6
  │    ├─ MultiboardSetItemIconBJ: TopBoard, 1, 循环整数A(), ReplaceableTextures\CommandButtons\BTNLament.blp
  │    ├─ MultiboardSetItemIconBJ: TopBoard, 2, 循环整数A(), ReplaceableTextures\CommandButtons\BTNSteelMelee.blp
  │    ├─ MultiboardSetItemIconBJ: TopBoard, 3, 循环整数A(), ReplaceableTextures\CommandButtons\BTNArcaniteMelee.blp
  │    ├─ MultiboardSetItemIconBJ: TopBoard, 4, 循环整数A(), ReplaceableTextures\WorldEditUI\Doodad-Destructible.blp
  │    ├─ MultiboardSetItemIconBJ: TopBoard, 5, 循环整数A(), ReplaceableTextures\CommandButtons\BTNUrnOfKelThuzad.blp
  │    ├─ 排行榜 TopBoard[1,循环整数A()] = (玩家名:玩家(循环整数A() - 1))
  │    ├─ 排行榜 TopBoard[2,循环整数A()] = (iKillAll[(循环整数A() - 1)]转字符串)
  │    ├─ 排行榜 TopBoard[3,循环整数A()] = (iKillByHero[(循环整数A() - 1)]转字符串)
  │    ├─ 排行榜 TopBoard[4,循环整数A()] = (玩家属性值(玩家(循环整数A() - 1), PlayerStateLumber)转字符串)
  │    └─ 排行榜 TopBoard[5,循环整数A()] = (iHeroDeadTime[(循环整数A() - 1)]转字符串)
  ├─ 循环整数A 1→5
  │    └─ ForLoopBMultiple: 1, 6
  └─ 销毁触发器(自身)
```

</details>

