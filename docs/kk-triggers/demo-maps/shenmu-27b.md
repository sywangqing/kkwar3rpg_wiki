---
title: 神墓27b - 演示图实战
category: kk-triggers
slug: demo-maps/shenmu-27b
description: 演示图 神墓27b 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 神墓27b — 演示图实战

> 演示图：神墓27b.w3x
>
> 触发器数：**146**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- InitVariable
- InitMapSetting
- LVChoose
- LVSet
- CreateQuest
- CreateLeaderboard
- BuyHero
- BuyHero2
- RandomHero
- ReviveHero
- ReviveHeroLumber
- 主机命令
- ModifyLevel
- AddBoss
- AddTeShu
- CleanItem
- 群体命令
- ExitCenimaMode
- BackBase
- BackRevivePoint
- MoveCase
- ShowWangCaiKill
- NoTeleport
- TFHQ
- PlayerLeft
- OfflinePlayerControl
- OfflinePlayerResource
- MoneyTooMuch
- LumberExchangeMoney
- MoneyExchangeLumber
- ChangeLeaderboardLumber
- ShowWeaponKill
- 关闭触发
- TurnOffOrder
- 埋骨地触发
- BaseBeDamaged
- BaseRevive
- 测试选项
- Player1Cheat1
- Player1Cheat2
- SetLV
- JustForTestNoCD
- xiaoxiongmao
- xiaoxiaoxiongmao
- sanqing
- xiongmao
- shangshandalaohu
- mi
- yuanguzhishustart
- yuanguzhishu
- PanNiu
- XiaoPanNiu
- 主线剧情
- juetian
- xuanyuan
- linghunshashou
- diyouyoubf
- diyouyoustart
- diyouyoudie
- modi
- yaohuang
- binglingyeye
- shoumulaoren
- 四血卫
- xueying
- wangchen
- NFC
- NFCEffect
- PoXu
- 传说
- wumingmubei
- yinshuang
- haotian
- xinzang
- 千丝不悔花
- QSBHHShow
- QSBHHHide
- 上山打老虎
- KillAllDistrutable
- ShouHuZhe
- DuoLuoShuRen
- WangQueZhiLu
- ForbideEnter1
- ForbideEnter2
- ForbideOut
- ForbideTeleport
- RuoShui
- ShuiYuJianSu
- ShuiYuJianSuHuiFu
- 寒冰炽炎合体技能
- HeTiEnter1
- HeTiOut1
- HeTiEnter2
- HeTiOut2
- HeTiCheck
- ItemSynthesis
- ItemUseable
- ItemUseableTarget
- UnitDie
- UnitDieCinema
- UsableAbility
- PassiveAbility
- AnyUnitDamaged
- UnitSummon
- UnitEnterMap
- HeroLevelUp
- HeroLearnSkill
- AbilityStartCast
- 其他类别
- YLWuJinChangYe
- CYHuoJingLingInit
- CYHuoJingLing
- JinShengWuWei
- SetHeroInvincible
- UnBlinkable
- UnBlinkableFushen
- RepickAbility
- 技能计时器
- tTianShuXiaJuan
- tBingZhiDiaoLing
- tJiCiTianYa
- tNJKL
- tBaoFengxue
- tShunZhuanQianNian
- tKongJianGeLie
- tSiWangQiXi
- tFengChenMoShi
- tChuanXinCi
- tDaoXuanZXSH
- 初始单位
- CreateAnimal
- LianJi
- Boss
- 刷兵
- JinGongSheZhi
- JinGongGuai
- JinGongDengDai
- JinGongTooMany
- MoDiJinGong
- 特殊怪
- TeShuGuai
- 最后的战争
- MyGod
- LastBattle
- FuShenMoDiStrength
- MyGod 复制

---

## 📜 触发器代码

### InitVariable

```text
触发器: InitVariable (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
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
  ├─ ── 设置千丝不悔花位置 ──
  ├─ 设置 pShuaGuai[51] = (区域gg_rct_______0001中心)
  ├─ 设置 pShuaGuai[52] = (区域gg_rct_______0002中心)
  ├─ 设置 pShuaGuai[53] = (区域gg_rct_______0003中心)
  ├─ 设置 pShuaGuai[54] = (区域gg_rct_______0004中心)
  ├─ 设置 pShuaGuai[55] = (区域gg_rct_______0005中心)
  ├─ ── 设置复活点 ──
  ├─ 设置 pFuHuo = (gg_unit_H00F_0003的位置)
  ├─ ── 设置回城点 ──
  ├─ 设置 pHG = (区域gg_rct_____________0000中心)
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
  ├─ 设置 uHeroType[15] = N00Y
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
  ├─ 设置 uJinGong[36] = efdr
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
  ├─ 设置 aJinGongGuaiHard[25] = AIlx
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
  ├─ 设置 iFaZeColor[21] = 100
  ├─ 设置 iFaZeColor[22] = 175
  ├─ 设置 iFaZeColor[23] = 255
  ├─ 设置 iFaZeColor[24] = 255
  ├─ 设置 iFaZeColor[25] = 255
  ├─ 设置 iFaZeColor[26] = 175
  ├─ 设置 iFaZeColor[27] = 75
  ├─ 设置 iFaZeColor[28] = 255
  ├─ ── 创建树及传送门 ──
  ├─ CustomScriptCode: "call CreateMoJiang()"
  ├─ ── 设置NPC对话 ──
  ├─ 设置 sXiongMao[0] = "|cff00ffff小熊猫：世间真正的宝物从不需要获得我们的认可，这个东西是我多年来的心血，若是此生有缘能看到它饮尽天下魔血的形态，我死而无憾。|r"
  ├─ 设置 sXiongMao[1] = "不要一下子给太多，忙不过来容易失败。"
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
  ├─ 设置 sXiongMao[33] = "|cffffcc00小小熊猫：哎。。。听说我们本来是挂了的，有一个叫thodylk的人硬是把我们挖了出来。|r"
  ├─ 设置 sXiongMao[34] = "|cffffcc00小小熊猫：希望下次出现的时候别老是拉我们熊猫军团围观破虚那妖孽了。|r"
  ├─ 设置 sXiongMao[35] = "|cffffcc00啊……你吓到我了……|r"
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

### InitMapSetting

```text
触发器: InitMapSetting (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.10)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 战争迷雾开关: EnabledDisabledEnabled
  ├─ 迷雾遮罩开关: EnabledDisabledEnabled
  ├─ ── 中立单位初始化 ──
  ├─ SetDestructableInvulnerableBJ: gg_dest_LTg3_2661, InvulnerabilityInvulnerable
  ├─ SetDestructableInvulnerableBJ: gg_dest_LTg3_2208, InvulnerabilityInvulnerable
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, gg_unit_N00N_0054
  ├─ 设置无敌: gg_unit_N00N_0054, InvulnerabilityInvulnerable
  ├─ 播放动画: gg_unit_N00N_0054, "attack walk stand spin"
  ├─ 播放动画: gg_unit_unp2_0034, "birth"
  ├─ PauseUnitBJ: PauseUnpauseOptionPause, gg_unit_H00C_0033
  ├─ 设置无敌: gg_unit_H00C_0033, InvulnerabilityInvulnerable
  ├─ 循环整数A 1→6: 隐藏单位(uJuHunZhen[循环整数A])
  ├─ SetPlayerFlag: 玩家9(灰), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerAllianceStateBJ: 玩家9(灰), PlayerNA, AllianceSettingAlliedVision
  ├─ SetPlayerAllianceStateBJ: PlayerNA, 玩家9(灰), AllianceSettingAlliedVision
  ├─ 升级玩家科技: 玩家9(灰), R006, 1
  ├─ 升级玩家科技: 玩家9(灰), R008, 1
  ├─ 升级玩家科技: 玩家9(灰), R009, 1
  ├─ 设置 uPlayerHeros[10] = gg_unit_N00N_0054
  ├─ 设置 uPlayerHeros[13] = gg_unit_H001_0087
  ├─ UnitRemoveAbilityBJ: Arav, gg_unit_Hmkg_0067
  ├─ 隐藏单位: gg_unit_nmrr_0068
  ├─ 设置 itemLunHui = 单位携带物品(按类型)(gg_unit_H00F_0003, ajen)
  ├─ ── 设置在线玩家组 ──
  ├─ 播放动画: gg_unit_ubon_0001, "birth"
  ├─ AddSpecialEffectTargetUnitBJ: "origin", gg_unit_ubon_0001, TimeAura.mdx
  ├─ 设置 grpUserPlayers = 符合条件的玩家(玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser))
  ├─ 设置 grpOnline = 符合条件的玩家((玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser) 且 玩家槽位状态比较(玩家槽位状态(过滤玩家()), OperatorEqualENE, PlayerSlotStatePlaying)))
  ├─ 设置 grpOffline = 符合条件的玩家((玩家控制者比较(玩家控制者类型(过滤玩家()), OperatorEqualENE, MapControlUser) 且 玩家槽位状态比较(玩家槽位状态(过滤玩家()), OperatorNotEqualENE, PlayerSlotStatePlaying)))
  ├─ 显示文本→grpOnline: "TRIGSTR_143"
  ├─ 显示文本→grpOnline: "TRIGSTR_963"
  ├─ 显示文本→grpOnline: "TRIGSTR_4582"
  ├─ ForForceMultiple: grpUserPlayers
  ├─ 循环整数A 1→7
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 玩家控制者比较(玩家控制者类型(玩家循环整数A), OperatorEqualENE, MapControlUser)
  │         │    ├─ 玩家槽位状态比较(玩家槽位状态(玩家循环整数A), OperatorEqualENE, PlayerSlotStatePlaying)
  │         ├─ 则
  │         │    设置 pFirstPlayer = 玩家循环整数A
  │         │    CustomScriptCode: "set bj_forLoopAIndex=8"
  │         └─ 否则: (无)
  ├─ 添加事件到 gg_trg_ModifyLevel: 玩家聊天(pFirstPlayer, "-nd ", ChatMatchTypeSubstring)
  ├─ 添加事件到 gg_trg_AddBoss: 玩家聊天(pFirstPlayer, "-boss", ChatMatchTypeExact)
  ├─ 添加事件到 gg_trg_AddTeShu: 玩家聊天(pFirstPlayer, "-ts", ChatMatchTypeExact)
  └─ 添加事件到 gg_trg_CleanItem: 玩家聊天(pFirstPlayer, "-qc", ChatMatchTypeExact)
```

### LVChoose

```text
触发器: LVChoose (初始化) [✓] — 难度添加
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.10)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
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
  └─ DialogDisplay: pFirstPlayer, dlgNanDu, ShowHideShow
```

### LVSet

```text
触发器: LVSet (初始化) [✓] — 难度选择
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(dlgNanDu)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  └─ 循环整数A 1→20
       └─ 如果
            ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, btnNanDu[循环整数A()])
            ├─ 则
            │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), 玩家9(灰)
            │    SetPlayerTechResearchedSwap: Rhme, 循环整数A(), PlayerNA
            │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), 玩家9(灰)
            │    SetPlayerTechResearchedSwap: Rhar, 循环整数A(), PlayerNA
            │    SetPlayerTechResearchedSwap: R003, 循环整数A(), 玩家9(灰)
            │    SetPlayerTechResearchedSwap: R004, 循环整数A(), PlayerNA
            │    显示文本→grpOnline: 自定义代码(" GetPlayerName(GetTriggerPlayer()) + "选择了|cffcc00ff难度|r"+ I2S(GetForLoopIndex...")
            │    MultiboardSetTitleText: TopBoard, "神之墓地2.7B 难度" + (循环整数A转字符串)
            │    返回
            └─ 否则: (无)
```

### CreateQuest

```text
触发器: CreateQuest (初始化) [✓] — 任务创建，效果创建
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1084", "TRIGSTR_1085", ReplaceableTextures\CommandButtons\BTNTornado.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_1012", "TRIGSTR_1013", Buildings\Other\TempArtB\BTNTempB.blp
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

### CreateLeaderboard

```text
触发器: CreateLeaderboard (初始化) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.50)
条件
  └─ 无
动作
  ├─ CreateMultiboardBJ: 5, 8, "神之墓地2.7B 难度" + (玩家科技等级(Rhme, 玩家9(灰))转字符串)
  ├─ 设置 TopBoard = 最后创建的排行榜()
  ├─ 排行榜 TopBoard[1,1] = "TRIGSTR_1116"
  ├─ 排行榜 TopBoard[2,1] = "TRIGSTR_1126"
  ├─ 排行榜 TopBoard[3,1] = "TRIGSTR_1127"
  ├─ 排行榜 TopBoard[4,1] = "TRIGSTR_1128"
  ├─ 排行榜 TopBoard[5,1] = "TRIGSTR_1129"
  ├─ 循环整数A 2→8
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
  │    └─ ForLoopBMultiple: 1, 8
  └─ 销毁触发器(自身)
```

### BuyHero

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
  ├─ 设置 (被贩卖单位()的所有者) 名字 = "銆?" + (玩家名:(被贩卖单位()的所有者)) + "銆?" + (单位名:被贩卖单位())
  ├─ 循环整数A 1→7: 限制单位可用((被贩卖单位()类型ID), 0, 玩家循环整数A())
  ├─ 如果
  │    ├─ 条件: 单位类型比较((被贩卖单位()类型ID), OperatorEqualENE, N007)
  │    ├─ 则: 添加物品到栏位(被贩卖单位(), I03H, 0)
  │    └─ 否则: 无动作()
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

### BuyHero2

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
  ├─ 设置 (被贩卖单位()的所有者) 名字 = "銆?" + (玩家名:(被贩卖单位()的所有者)) + "銆?" + (单位名:被贩卖单位())
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

### RandomHero

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
       │    设置 触发玩家() 名字 = "銆?" + (玩家名:触发玩家()) + "銆?" + (单位名:uTemp)
       │    SetPlayerHandicapXPBJ: 触发玩家(), 110.00
       │    显示文本→grpOnline: (玩家名:触发玩家()) + "选择了随机英雄，额外获得10%的经验加成。"
       │    循环整数A 1→7: 限制单位可用((uTemp类型ID), 0, 玩家循环整数A())
       │    如果
       │      ├─ 条件: 单位类型比较((uTemp类型ID), OperatorEqualENE, N007)
       │      ├─ 则: 添加物品到栏位(uTemp, I03H, 0)
       │      └─ 否则: 无动作()
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

### ReviveHero

```text
触发器: ReviveHero (玩家/英雄) [✓] — 死亡复活
───────────────────────────────────────────────────────
事件
  └─ 玩家单位 - 单位死亡
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
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
  │    │      ├─ 条件: (触发单位()的所有者) == 玩家8(粉)
  │    │      ├─ 则
  │    │      │    等待 10.00s
  │    │      └─ 否则
  │    │           等待 2.00s
  │    └─ 否则
  │         如果
  │           ├─ 条件: (触发单位()的所有者) == 玩家8(粉)
  │           ├─ 则
  │           │    等待 60.00s
  │           └─ 否则
  │                等待 (5.00 + (玩家科技等级(Rhme, 玩家9(灰))转实数))s
  ├─ 如果
  │    ├─ 条件: (触发单位()的所有者) == 玩家8(粉)
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

### ReviveHeroLumber

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

### 主机命令

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

### ModifyLevel

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
       │    MultiboardSetTitleText: TopBoard, "神之墓地2.7B 难度提升" + 取子字符串(玩家聊天字符串(), 5, 7)
       │    SetPlayerTechResearchedSwap: Rhme, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: Rhme, iTemp, PlayerNA
       │    SetPlayerTechResearchedSwap: Rhar, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: Rhar, iTemp, PlayerNA
       │    SetPlayerTechResearchedSwap: R003, iTemp, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: R004, iTemp, PlayerNA
       │    如果
       │      ├─ 条件: iTemp OperatorGreater 90
       │      ├─ 则
       │      │    设置技能等级: gg_unit_Uclc_0123, A09M, (iTemp - 90)
       │      └─ 否则: (无)
       └─ 否则
            显示文本→Player00: 0
```

### AddBoss

```text
触发器: AddBoss (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
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

### AddTeShu

```text
触发器: AddTeShu (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 显示文本→grpOnline: "TRIGSTR_2513"
  ├─ 设置 bTeShu = true
  ├─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2208
  └─ ModifyGateBJ: GateOperationOpen, gg_dest_LTg3_2661
```

### CleanItem

```text
触发器: CleanItem (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 显示文本→grpOnline: "TRIGSTR_1362"
  ├─ EnumItemsInRectBJMultiple: gg_rct_____________01
  ├─ EnumItemsInRectBJMultiple: gg_rct__________01
  ├─ PolledWait: 120.00
  └─ 开启触发器 当前触发器()
```

### 群体命令

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

### ExitCenimaMode

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
       └─ 否则
            设置 bExitCnima[玩家号(触发玩家())] = true
            PolledWait: 0.10
            设置 bExitCnima[玩家号(触发玩家())] = false
```

### BackBase

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

### BackRevivePoint

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

### MoveCase

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

### ShowWangCaiKill

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

### NoTeleport

```text
触发器: NoTeleport (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: uPlayerHeros[玩家号(触发玩家())] == UnitNull
       ├─ 则
       │    UnitAddType: uPlayerHeros[玩家号(触发玩家())], UnitTypeSapperAdd
       └─ 否则: (无)
```

### TFHQ

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
  ├─ 设置 iTemp = 随机[1~14]
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
              ├─ 条件: iTemp == 14
              ├─ 则
              │    添加事件到 gg_trg_JinShengWuWei: 单位生命值事件(uPlayerHeros[玩家号(触发玩家())], 小于, 0.90)
              └─ 否则: (无)
            显示文本→grpOnline: (单位名:uPlayerHeros[玩家号(触发玩家())]) + "获取了天赋技能：" + 技能名称(aTianFu[iTemp])
            设置 bTFHQ[玩家号(触发玩家())] = true
```

### PlayerLeft

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
  │    ├─ 循环整数A 1→6: 移动物品到点(单位栏位物品(选取单位(), 循环整数A), pHG)
  │    └─ 移动单位: 选取单位(), pFuHuo
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

### OfflinePlayerControl

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
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) == 1
  │    ├─ 则
  │    │    设置 uTemp = 单位组第一个单位(grpTemp)
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ 玩家在玩家组中((uTemp的所有者), grpOffline) == TRUE
  │    │      │    ├─ iPlayerControlList[玩家号((uTemp的所有者))] == 0
  │    │      │    ├─ 玩家属性值(触发玩家(), PlayerStateLumber) OperatorGreater 500
  │    │      ├─ 则
  │    │      │    SetPlayerAllianceStateBJ: (uTemp的所有者), 触发玩家(), AllianceSettingAlliedAdvUnits
  │    │      │    调整 触发玩家() 的 PlayerStateLumber: -500
  │    │      │    PolledWait: 0.10
  │    │      │    MultiboardDisplayBJ: ShowHideShow, TopBoard
  │    │      └─ 否则
  │    │           显示文本→触发玩家(): 0
  │    └─ 否则
  │         显示文本→触发玩家(): 0
  ├─ 删除单位组 grpTemp
  ├─ 开启触发器 当前触发器()
  └─ 开启触发器 gg_trg_OfflinePlayerResource
```

### OfflinePlayerResource

```text
触发器: OfflinePlayerResource (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(30.00)
条件
  └─ 无
动作
  └─ ForForceMultiple: grpOffline
```

### MoneyTooMuch

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

### LumberExchangeMoney

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

### MoneyExchangeLumber

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
       └─ 否则: (无)
```

### ChangeLeaderboardLumber

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

### ShowWeaponKill

```text
触发器: ShowWeaponKill (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置 grpTemp = 玩家选中的全部单位(触发玩家())
  ├─ 单位组: 选取 grpTemp 中所有单位
  │    └─ 如果
  │         ├─ 条件: 单位类型判断(选取单位(), 英雄) == TRUE
  │         ├─ 则
  │         │    设置 uTemp = 选取单位()
  │         │    循环整数A 1→6
  │         │      ├─ 设置 itemTemp = 单位栏位物品(uTemp, 循环整数A)
  │         │      └─ 如果
  │         │           ├─ 条件: 任一成立
  │         │           ├─ 则
  │         │           │    显示文本→触发玩家(): 0
  │         │           └─ 否则: (无)
  │         └─ 否则: (无)
  ├─ 删除单位组 grpTemp
  └─ 开启触发器 当前触发器()
```

### 关闭触发

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

### TurnOffOrder

```text
触发器: TurnOffOrder (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(60.00)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 玩家科技等级(Rhme, 玩家9(灰)) == 0
  │    ├─ 则
  │    │    DialogDisplay: Player00, dlgNanDu, ShowHideHide
  │    │    显示文本→grpOnline: "TRIGSTR_4083"
  │    │    MultiboardSetTitleText: TopBoard, "TRIGSTR_4084"
  │    │    SetPlayerTechResearchedSwap: Rhme, 100, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: Rhme, 100, PlayerNA
  │    │    SetPlayerTechResearchedSwap: Rhar, 100, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: Rhar, 100, PlayerNA
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
  └─ 销毁触发器(自身)
```

### 埋骨地触发

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

### BaseBeDamaged

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

### BaseRevive

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

### 测试选项

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

### Player1Cheat1

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

### Player1Cheat2

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

### SetLV

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

### JustForTestNoCD

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

### xiaoxiongmao

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
       │    ├─ 单位持有物品类型(触发单位(), I038) == TRUE
       ├─ 则
       │    删除物品: 单位携带物品(按类型)(触发单位(), I037)
       │    如果
       │      ├─ 条件: 随机[1~3] == 1
       │      ├─ 则
       │      │    显示文本→(触发单位()的所有者): 0
       │      │    添加物品: I038, 触发单位()
       │      └─ 否则
       │           显示文本→(触发单位()的所有者): 0
       └─ 否则
            显示文本→(触发单位()的所有者): 0
```

### xiaoxiaoxiongmao

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
  │    │    添加物品: I04R, 触发单位()
  │    │    设置 uTianShuXiaJuan = 触发单位()
  │    │    设置 itemTSXJ = 最后创建的物品()
  │    │    运行计时器 tTianShuXiaJuan (循环, 0.10s)
  │    │    AddLightningLoc: LightningTypeDRAL, pHG, pHG
  │    │    设置 lightTSXJ = 最后创建的闪电效果()
  │    │    显示文本→(触发单位()的所有者): 0
  │    └─ 否则: (无)
  ├─ 设置 itemTemp = 单位栏位物品(触发单位(), 6)
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

### sanqing

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

### xiongmao

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

### shangshandalaohu

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
  │    │      │      │    添加物品: I01W, 触发单位()
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

### mi

```text
触发器: mi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(300.00, gg_unit_n00D_0026)
条件
  ├─ (触发单位()的所有者) == PlayerNA
  └─ (触发单位()的所有者) == 非玩家
动作
  └─ 如果
       ├─ 条件: 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
       ├─ 则
       │    如果
       │      ├─ 条件: (触发单位()类型ID) == E000
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 玩家科技等级(Rhcd, (触发单位()的所有者)) == 0
       │      │      │    ├─ 英雄等级(触发单位()) OperatorGreater 100
       │      │      │    ├─ uYuanGuChuanCheng == UnitNull
       │      │      ├─ 则
       │      │      │    关闭触发器 当前触发器()
       │      │      │    设置 uYuanGuChuanCheng = 触发单位()
       │      │      │    PauseUnitBJ: PauseUnpauseOptionPause, uYuanGuChuanCheng
       │      │      │    PanCameraToTimed: 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_1419", SoundNull, "TRIGSTR_1421", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3829", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3830", SoundNull, "TRIGSTR_3831", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3832", SoundNull, "TRIGSTR_3833", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3835", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3836", SoundNull, "TRIGSTR_3837", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3839", AddSetToAdd, 0, WaitDontWait
       │      │      │    播放动画: gg_unit_n00D_0026, "attack"
       │      │      │    显示文本→grpOnline: "TRIGSTR_1332"
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │      │    PolledWait: 120.00
       │      │      │    IssueImmediateOrderById: gg_unit_n00D_0026, OrderCodeStop
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_n00D_0026, "TRIGSTR_3840", SoundNull, "TRIGSTR_3841", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, uYuanGuChuanCheng, (单位名:uYuanGuChuanCheng), SoundNull, "TRIGSTR_3842", AddSetToAdd, 0, WaitDontWait
       │      │      │    SetPlayerTechResearchedSwap: Rhcd, 1, (uYuanGuChuanCheng的所有者)
       │      │      │    显示文本→grpOnline: "TRIGSTR_3843"
       │      │      │    PauseUnitBJ: PauseUnpauseOptionUnpause, uYuanGuChuanCheng
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (uYuanGuChuanCheng的所有者)
       │      │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │      │    销毁触发器(自身)
       │      │      │    隐藏单位: gg_unit_n00D_0026
       │      │      └─ 否则: (无)
       │      └─ 否则
       │           伤害: gg_unit_n00D_0026→触发单位(): 25000000.00 (AttackTypeNormal/DamageTypeUniversal)
       │           ForceClear: grpPlayerGroupTemp
       │           ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │           TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_n00D_0026, "TRIGSTR_3844", SoundNull, "TRIGSTR_3845", AddSetToAdd, 0, WaitDontWait
       └─ 否则: (无)
```

### yuanguzhishustart

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

### yuanguzhishu

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

### PanNiu

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

### XiaoPanNiu

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

### 主线剧情

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

### juetian

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
  ├─ 设置单位归属: 触发单位(), 玩家8(粉), 改变颜色
  ├─ ForForceMultiple: grpOnline
  ├─ 复活英雄 触发单位() 在 pHG
  ├─ 设置 uPlayerHeros[9] = gg_unit_N006_0102
  ├─ PolledWait: 0.10
  └─ MultiboardDisplayBJ: ShowHideShow, TopBoard
```

### xuanyuan

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

### linghunshashou

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

### diyouyoubf

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

### diyouyoustart

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

### diyouyoudie

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
  ├─ 设置无敌: gg_unit_unp2_0034, InvulnerabilityVulnerable
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  └─ SetPlayerTechResearchedSwap: Rhhb, 1, 玩家9(灰)
```

### modi

```text
触发器: modi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(150.00, gg_unit_h005_0137)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I026)) == TRUE
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02H)) == TRUE
  │    ├─ 则
  │    │    显示文本→(触发单位()的所有者): 0
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I026)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I02H)
  │    │    添加物品: I02G, 触发单位()
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I036)) == TRUE
  │    │    ├─ 物品有归属(单位携带物品(按类型)(触发单位(), I02H)) == TRUE
  │    │    ├─ bHaoJie == 1
  │    │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I036)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I02H)
  │    │    添加物品: I03M, 触发单位()
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_h005_0137), 单位Y坐标(gg_unit_h005_0137), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_4114", SoundNull, "TRIGSTR_4115", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4113", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4116", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_4117", SoundNull, "TRIGSTR_4118", AddSetToAdd, 0, WaitDontWait
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
  │    │    ├─ bHaoJie == 2
  │    │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I054)
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_h005_0137), 单位Y坐标(gg_unit_h005_0137), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_906", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_1156", SoundNull, "TRIGSTR_1389", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_1408", SoundNull, "TRIGSTR_1414", AddSetToAdd, 0, WaitDontWait
  │    │    添加物品: I04P, 触发单位()
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_1494", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_1495", SoundNull, "TRIGSTR_1497", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    设置 bHaoJie = 3
  │    │    开启触发器 当前触发器()
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位持有物品类型(触发单位(), I05N) == TRUE
       │    ├─ 单位持有物品类型(触发单位(), I05O) == TRUE
       │    ├─ bHaoJie == 3
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除物品: 单位携带物品(按类型)(触发单位(), I05N)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I05O)
       │    设置 bHaoJie = 4
       │    PanCameraToTimed: 单位X坐标(gg_unit_h005_0137), 单位Y坐标(gg_unit_h005_0137), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_5237", SoundNull, "TRIGSTR_5238", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5236", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_5245", SoundNull, "TRIGSTR_5246", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_5239", SoundNull, "TRIGSTR_5240", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_5242", SoundNull, "TRIGSTR_5243", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5244", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    PolledWait: 60.00
       │    设置 pTemp = (gg_unit_h005_0137的位置)
       │    设置 uQianSi = 创建单位(指定点)(玩家8(粉), h00I, pTemp, 270.00)
       │    清除点 pTemp
       │    开启触发器 当前触发器()
       └─ 否则: (无)
```

### yaohuang

```text
触发器: yaohuang (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(150.00, gg_unit_Ecen_0088)
条件
  ├─ 单位持有物品类型(触发单位(), I05K) == TRUE
  ├─ 单位持有物品类型(触发单位(), I03N) == TRUE
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
动作
  ├─ 销毁触发器(自身)
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I05K)
  ├─ 删除物品: 单位携带物品(按类型)(触发单位(), I03N)
  ├─ SetUnitAbilityLevelSwapped: AEah, gg_unit_Ecen_0088, 1
  ├─ 移除技能: gg_unit_Ecen_0088, 自定义代码("'Amov'")
  ├─ SetHeroLevel: gg_unit_Ecen_0088, 1, ShowHideHide
  ├─ SuspendHeroXPBJ: EnableDisableDisable, gg_unit_Ecen_0088
  ├─ 设置单位归属: gg_unit_Ecen_0088, 非玩家, 改变颜色
  ├─ ForForceMultiple: grpUserPlayers
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_Ecen_0088), 单位Y坐标(gg_unit_Ecen_0088), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_4999", SoundNull, "TRIGSTR_5181", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5654", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_5655", SoundNull, "TRIGSTR_5660", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_908", SoundNull, "TRIGSTR_4234", AddSetToAdd, 0, WaitDontWait
  ├─ 添加物品: stel, 触发单位()
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_Ecen_0088, "TRIGSTR_5665", SoundNull, "TRIGSTR_5666", AddSetToAdd, 0, WaitDontWait
  ├─ 添加物品: I054, 触发单位()
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  └─ 电影模式: OnOffOff, grpPlayerGroupTemp
```

### binglingyeye

```text
触发器: binglingyeye (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_H002_0094)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepGuanChuan == 1
  │    │    ├─ 单位持有物品类型(触发单位(), I033) == TRUE
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    设置单位归属: gg_unit_H002_0094, 非玩家, 改变颜色
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4068", SoundNull, "TRIGSTR_4069", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4071", SoundNull, "TRIGSTR_4072", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4070", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4073", SoundNull, "TRIGSTR_4074", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4075", SoundNull, "TRIGSTR_4076", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4077", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4078", SoundNull, "TRIGSTR_4079", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_4080", SoundNull, "TRIGSTR_4081", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    设置 iStepGuanChuan = 2
  │    │    QuestSetDiscoveredBJ: quests[3], DiscoveredOptionDiscovered
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ iStepGuanChuan == 2
  │    │    ├─ 单位持有物品类型(触发单位(), I034) == TRUE
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I034)
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_1049", SoundNull, "TRIGSTR_1061", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_1063", SoundNull, "TRIGSTR_1078", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_1082", SoundNull, "TRIGSTR_1138", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_1944", SoundNull, "TRIGSTR_3993", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_3994", SoundNull, "TRIGSTR_3995", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    添加物品: I042, 触发单位()
  │    │    设置 iStepGuanChuan = 3
  │    │    QuestSetCompletedBJ: quests[3], CompletionOptionCompleted
  │    │    QuestSetDiscoveredBJ: quests[4], DiscoveredOptionDiscovered
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ iStepGuanChuan == 3
       │    ├─ 单位持有物品类型(触发单位(), I033) == TRUE
       │    ├─ 单位持有物品类型(触发单位(), I03E) == TRUE
       │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
       ├─ 则
       │    销毁触发器(自身)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I033)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I03E)
       │    PanCameraToTimed: 单位X坐标(gg_unit_H002_0094), 单位Y坐标(gg_unit_H002_0094), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_3996", SoundNull, "TRIGSTR_3997", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5182", SoundNull, "TRIGSTR_5183", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_5184", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5223", SoundNull, "TRIGSTR_5224", AddSetToAdd, 0, WaitDontWait
       │    添加物品: I05P, 触发单位()
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_H002_0094, "TRIGSTR_5225", SoundNull, "TRIGSTR_5226", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    设置 iStepGuanChuan = 4
       │    返回
       └─ 否则: (无)
```

### shoumulaoren

```text
触发器: shoumulaoren (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(100.00, gg_unit_u003_0122)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ bLiuHuang == TRUE
  │    │    ├─ 单位持有物品类型(触发单位(), I04X) == TRUE
  │    ├─ 则
  │    │    设置 bLiuHuang = true
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I04X)
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3848", SoundNull, "TRIGSTR_3849", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    添加技能: gg_unit_ubon_0001, A033
  │    │    设置 pTemp = (gg_unit_ubon_0001的位置)
  │    │    循环整数A 1→6
  │    │      └─ CustomScriptCode: "call CreateUnit(Player(7),'nchp',GetLocationX(udg_pTemp)+512*CosBJ(bj_forLoop..."
  │    │    清除点 pTemp
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 英雄等级(触发单位()) OperatorGreater 100
       ├─ 则
       │    如果
       │      ├─ 条件: bShenLiJieJing == TRUE
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 随机[1~10] == 1
       │      │      ├─ 则
       │      │      │    设置 bShenLiJieJing = true
       │      │      │    添加物品: I03E, 触发单位()
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │      │    电影模式: OnOffOn, grpPlayerGroupTemp
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_4326", SoundNull, "TRIGSTR_4467", AddSetToAdd, 0, WaitDontWait
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │      └─ 否则
       │      │           杀死 触发单位()
       │      │           修改 触发单位() 的HeroStatStr: ModifyMethodSub随机[100~300]
       │      │           修改 触发单位() 的HeroStatAgi: ModifyMethodSub随机[100~300]
       │      │           修改 触发单位() 的HeroStatInt: ModifyMethodSub随机[100~300]
       │      │           ForceClear: grpPlayerGroupTemp
       │      │           ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │           TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_u003_0122, "TRIGSTR_4473", SoundNull, "TRIGSTR_4474", AddSetToAdd, 0, WaitDontWait
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 全部成立
       │      │    ├─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
       │      │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 0
       │      │    ├─ 单位持有物品类型(触发单位(), I042) == TRUE
       │      │    ├─ 触发单位() == uPlayerHeros[玩家号((触发单位()的所有者))]
       │      │    ├─ bShenLiJieJing == TRUE
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
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3914", SoundNull, (单位名:触发单位()) + "经过生与死的徘徊领悟了半神法则！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3916", SoundNull, (单位名:触发单位()) + "获得半神怒焰！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3917", SoundNull, (单位名:触发单位()) + "获得审判降临！", AddSetToAdd, 0, WaitDontWait
       │      │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3918", SoundNull, (单位名:触发单位()) + "获得湮灭雷电！", AddSetToAdd, 0, WaitDontWait
       │      │      │    ForceClear: grpPlayerGroupTemp
       │      │      │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │      │    电影模式: OnOffOff, grpPlayerGroupTemp
       │      │      │    QuestSetCompletedBJ: quests[4], CompletionOptionCompleted
       │      │      └─ 否则
       │      │           杀死 触发单位()
       │      │           ForceClear: grpPlayerGroupTemp
       │      │           ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │      │           TransmissionFromUnitWithNameBJ: grpPlayerGroupTemp, gg_unit_u003_0122, "TRIGSTR_3891", SoundNull, "TRIGSTR_3911", AddSetToAdd, 0, WaitDontWait
       │      └─ 否则: (无)
       └─ 否则: (无)
```

### 四血卫

```text
触发器: 四血卫 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### xueying

```text
触发器: xueying (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00E_0104)
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
  └─ bLiuHuang == TRUE
动作
  ├─ 销毁触发器(自身)
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00E_0104), 单位Y坐标(gg_unit_N00E_0104), 0
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOn, grpPlayerGroupTemp
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_4051", SoundNull, "TRIGSTR_4052", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_4056", SoundNull, "TRIGSTR_4057", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_4058", SoundNull, "TRIGSTR_4059", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_4060", SoundNull, "TRIGSTR_4061", AddSetToAdd, 0, WaitDontWait
  ├─ 添加物品: I052, 触发单位()
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_N00E_0104, gg_unit_u003_0122, 0.00
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_4062", SoundNull, "TRIGSTR_4063", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_4064", SoundNull, "TRIGSTR_4065", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00E_0104, "TRIGSTR_2512", SoundNull, "TRIGSTR_5097", AddSetToAdd, 0, WaitDontWait
  ├─ ForceClear: grpPlayerGroupTemp
  ├─ ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  ├─ 电影模式: OnOffOff, grpPlayerGroupTemp
  ├─ 设置 pTemp = (gg_unit_N00E_0104的位置)
  ├─ 销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  ├─ 清除点 pTemp
  ├─ 设置 pTemp = Location((单位X坐标(gg_unit_ubon_0001) + 500.00), 单位Y坐标(gg_unit_ubon_0001))
  ├─ 移动单位: gg_unit_N00E_0104, pTemp
  ├─ 设置单位归属: gg_unit_N00E_0104, 玩家8(粉), 改变颜色
  ├─ SetUnitFacingTimed: gg_unit_N00E_0104, 180.00, 0
  ├─ UnitAddAbilityBJ: AInv, gg_unit_N006_0102
  ├─ 修改 gg_unit_N006_0102 的HeroStatStr: ModifyMethodAdd20000
  ├─ 修改 gg_unit_N006_0102 的HeroStatAgi: ModifyMethodAdd20000
  ├─ 修改 gg_unit_N006_0102 的HeroStatInt: ModifyMethodAdd20000
  └─ 清除点 pTemp
```

### wangchen

```text
触发器: wangchen (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_N00F_0106)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ bLiuHuang == TRUE
  │    │    ├─ bHaoJie == 2
  │    │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  │    │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
  │    │    ├─ 单位持有物品类型(触发单位(), I052) == TRUE
  │    │    ├─ (gg_unit_N00F_0106的所有者) == 非玩家
  │    │    ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 2
  │    ├─ 则
  │    │    关闭触发器 当前触发器()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I052)
  │    │    PanCameraToTimed: 单位X坐标(gg_unit_N00F_0106), 单位Y坐标(gg_unit_N00F_0106), 0
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4031", SoundNull, "TRIGSTR_4032", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4030", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4033", SoundNull, "TRIGSTR_4034", AddSetToAdd, 0, WaitDontWait
  │    │    UnitAddItemSwapped: 单位携带物品(按类型)(触发单位(), I052), gg_unit_N00F_0106
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4035", AddSetToAdd, 0, WaitDontWait
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  │    │    移动单位: 触发单位(), pHG
  │    │    清除点 pTemp
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_4036", SoundNull, "TRIGSTR_4037", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4038", SoundNull, "TRIGSTR_4039", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_h005_0137, "TRIGSTR_4040", SoundNull, "TRIGSTR_4041", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4042", SoundNull, "TRIGSTR_4043", AddSetToAdd, 0, WaitDontWait
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4044", SoundNull, "TRIGSTR_4045", AddSetToAdd, 0, WaitDontWait
  │    │    ForceClear: grpPlayerGroupTemp
  │    │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
  │    │    电影模式: OnOffOff, grpPlayerGroupTemp
  │    │    设置 pTemp = (gg_unit_N00F_0106的位置)
  │    │    销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  │    │    清除点 pTemp
  │    │    设置 pTemp = Location((单位X坐标(gg_unit_ubon_0001) - 500.00), 单位Y坐标(gg_unit_ubon_0001))
  │    │    移动单位: gg_unit_N00F_0106, pTemp
  │    │    设置单位归属: gg_unit_N00F_0106, 玩家8(粉), 改变颜色
  │    │    SetUnitFacingTimed: gg_unit_N00F_0106, 0.00, 0
  │    │    修改 gg_unit_N006_0102 的HeroStatStr: ModifyMethodAdd40000
  │    │    修改 gg_unit_N006_0102 的HeroStatAgi: ModifyMethodAdd40000
  │    │    修改 gg_unit_N006_0102 的HeroStatInt: ModifyMethodAdd40000
  │    │    清除点 pTemp
  │    │    开启触发器 当前触发器()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 单位持有物品类型(触发单位(), I04Y) == TRUE
       │    ├─ 单位类型判断(触发单位(), 英雄) == TRUE
       │    ├─ 玩家科技等级(R009, (触发单位()的所有者)) == 1
       │    ├─ (gg_unit_N00F_0106的所有者) == 玩家8(粉)
       │    ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 4
       ├─ 则
       │    销毁触发器(自身)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I04Y)
       │    设置单位归属: gg_unit_N00F_0106, 非玩家, 改变颜色
       │    SetUnitFacingToFaceUnitTimed: gg_unit_N00F_0106, 触发单位(), 0
       │    PanCameraToTimed: 单位X坐标(gg_unit_N00F_0106), 单位Y坐标(gg_unit_N00F_0106), 0
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOn, grpPlayerGroupTemp
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4046", SoundNull, "TRIGSTR_4047", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4049", SoundNull, "TRIGSTR_4050", AddSetToAdd, 0, WaitDontWait
       │    ForceClear: grpPlayerGroupTemp
       │    ForceAddPlayer: grpPlayerGroupTemp, (触发单位()的所有者)
       │    电影模式: OnOffOff, grpPlayerGroupTemp
       │    SetUnitFacingToFaceUnitTimed: gg_unit_N00F_0106, gg_unit_N00G_0105, 0
       │    循环整数A 1→6: UnitRemoveItemFromSlotSwapped(循环整数A, gg_unit_N00F_0106)
       │    单位添加物品: gg_unit_N00F_0106, 单位携带物品(按类型)(触发单位(), I052)
       │    单位添加物品: gg_unit_N00F_0106, 单位携带物品(按类型)(触发单位(), I04Y)
       │    运行计时器 tNFCEffect (循环, 3.00s)
       │    运行计时器 tNieFanChen (一次性, 180.00s)
       │    计时器窗口: tNieFanChen 标题="TRIGSTR_1788"
       │    设置 dNieFanChen = 最后创建的计时器窗口()
       │    TimerDialogDisplay: dNieFanChen, ShowHideShow
       └─ 否则: (无)
```

### NFC

```text
触发器: NFC (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tNieFanChen 到期
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─ 销毁触发器(自身)
  ├─ 暂停计时器 tNFCEffect
  ├─ TimerDialogDisplay: dNieFanChen, ShowHideHide
  ├─ 删除计时器窗口 dNieFanChen
  ├─ 循环整数A 1→6: UnitRemoveItemFromSlotSwapped(循环整数A, gg_unit_N00F_0106)
  ├─ 设置单位归属: gg_unit_N00F_0106, 玩家8(粉), 改变颜色
  ├─ 设置单位归属: gg_unit_N00G_0105, 玩家8(粉), 改变颜色
  ├─ SetUnitFacingToFaceUnitTimed: gg_unit_N00G_0105, gg_unit_N00F_0106, 0
  ├─ 单位发布命令(立即): gg_unit_N00G_0105, UnitOrderRoboGoblin
  ├─ PanCameraToTimed: 单位X坐标(gg_unit_N00G_0105), 单位Y坐标(gg_unit_N00G_0105), 0
  ├─ 电影模式: OnOffOn, grpOnline
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00G_0105, "TRIGSTR_4026", SoundNull, "TRIGSTR_4027", AddSetToAdd, 0, WaitDontWait
  ├─ TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00F_0106, "TRIGSTR_4029", SoundNull, "TRIGSTR_4028", AddSetToAdd, 0, WaitDontWait
  ├─ 电影模式: OnOffOff, grpOnline
  ├─ 修改 gg_unit_N006_0102 的HeroStatStr: ModifyMethodAdd40000
  ├─ 修改 gg_unit_N006_0102 的HeroStatAgi: ModifyMethodAdd40000
  ├─ 修改 gg_unit_N006_0102 的HeroStatInt: ModifyMethodAdd40000
  ├─ 设置 pTemp = (gg_unit_N00G_0105的位置)
  ├─ 销毁特效 创建特效(Abilities\Spells\Human\MassTeleport\MassTeleportCaster.mdl, pTemp)
  ├─ 移动单位: gg_unit_N00G_0105, pHG
  └─ 清除点 pTemp
```

### NFCEffect

```text
触发器: NFCEffect (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 计时器 tNFCEffect 到期
条件
  └─ 无
动作
  ├─ 播放动画: gg_unit_N00F_0106, "Spell Slam"
  ├─ 设置 pTemp = (gg_unit_N00F_0106的位置)
  ├─ 销毁特效 创建特效(Abilities\Spells\Demon\DarkPortal\DarkPortalTarget.mdl, pTemp)
  ├─ 清除点 pTemp
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Charm\CharmTarget.mdl, (单位X坐标(gg_unit_N00G_0105) + 120.00), (单位Y坐标(gg_unit_N00G_0105) + 120.00))
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Charm\CharmTarget.mdl, (单位X坐标(gg_unit_N00G_0105) - 120.00), (单位Y坐标(gg_unit_N00G_0105) + 120.00))
  ├─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Charm\CharmTarget.mdl, (单位X坐标(gg_unit_N00G_0105) + 120.00), (单位Y坐标(gg_unit_N00G_0105) - 120.00))
  └─ 销毁特效 创建特效(指定坐标)(Abilities\Spells\Other\Charm\CharmTarget.mdl, (单位X坐标(gg_unit_N00G_0105) - 120.00), (单位Y坐标(gg_unit_N00G_0105) - 120.00))
```

### PoXu

```text
触发器: PoXu (剧情/任务) [✓]
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
  │    ├─ 则: 单位添加物品(触发单位(), 单位携带物品(按类型)(gg_unit_N00M_0083, I041))
  │    └─ 否则: 无动作()
  ├─ PolledWait: 2
  ├─ PauseUnitBJ: PauseUnpauseOptionUnpause, 触发单位()
  └─ PauseUnitBJ: PauseUnpauseOptionUnpause, gg_unit_N00M_0083
```

### 传说

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

### wumingmubei

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
  └─ 设置单位归属: gg_unit_hwtw_0084, 玩家7(绿), 改变颜色
```

### yinshuang

```text
触发器: yinshuang (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册单位进入范围事件(256, gg_unit_h003_0002)
条件
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
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
       │    添加物品: k3m1, 触发单位()
       │    显示文本→grpOnline: "TRIGSTR_1099"
       │    设置 iStepHaoYue = 2
       └─ 否则
            杀死 触发单位()
```

### haotian

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
  │    │    设置单位归属: gg_unit_H001_0087, 非玩家, 改变颜色
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
  │    │    添加物品: I03U, 触发单位()
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
       │    添加物品: I03V, 触发单位()
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

### xinzang

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

### 千丝不悔花

```text
触发器: 千丝不悔花 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### QSBHHShow

```text
触发器: QSBHHShow (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册游戏时间事件(大于, 6.00)
条件
  └─ 无
动作
  ├─ 创建物品: I03N, pShuaGuai[随机[51~55]]
  └─ 设置 itemQSBHH = 最后创建的物品()
```

### QSBHHHide

```text
触发器: QSBHHHide (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册游戏时间事件(大于, 7.00)
条件
  └─ 无
动作
  └─ 删除物品: itemQSBHH
```

### 上山打老虎

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

### KillAllDistrutable

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
       ├─ 条件: iHuGeShu OperatorGreater 50
       ├─ 则
       │    销毁触发器(自身)
       │    PanCameraToTimed: 单位X坐标(gg_unit_N00X_0031), 单位Y坐标(gg_unit_N00X_0031), 0
       │    电影模式: OnOffOn, grpOnline
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00X_0031, "TRIGSTR_5609", SoundNull, "TRIGSTR_5610", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00X_0031, "TRIGSTR_5611", SoundNull, "TRIGSTR_5612", AddSetToAdd, 0, WaitDontWait
       │    电影模式: OnOffOff, grpOnline
       │    设置单位归属: gg_unit_N00X_0031, PlayerNA, 改变颜色
       │    返回
       └─ 否则: (无)
```

### ShouHuZhe

```text
触发器: ShouHuZhe (技能/物品) [✓]
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

### DuoLuoShuRen

```text
触发器: DuoLuoShuRen (技能/物品) [✓]
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

### WangQueZhiLu

```text
触发器: WangQueZhiLu (技能/物品) [✓]
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

### ForbideEnter1

```text
触发器: ForbideEnter1 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  ├─ 注册进入矩形区域事件(gg_rct_____________b)
  ├─ 注册进入矩形区域事件(gg_rct_____________00000000)
  └─ 注册进入矩形区域事件(gg_rct_______a)
条件
  ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  └─ (触发单位()类型ID) == ufro
动作
  ├─ 移动单位: 触发单位(), pHG
  └─ 显示文本→(触发单位()的所有者): 0
```

### ForbideEnter2

```text
触发器: ForbideEnter2 (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct_____________u)
条件
  ├─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 单位技能等级(触发单位(), Aloc) == 0
动作
  ├─ 移动单位: 触发单位(), pHG
  └─ 显示文本→(触发单位()的所有者): 0
```

### ForbideOut

```text
触发器: ForbideOut (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册离开矩形区域事件(gg_rct_____________0000)
条件
  ├─ (触发单位()的所有者) == 玩家8(粉)
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  └─ 移动单位: 触发单位(), pHG
```

### ForbideTeleport

```text
触发器: ForbideTeleport (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A030)
动作
  ├─ 设置 pTemp = 技能目标点()
  └─ 如果
       ├─ 条件: 任一成立
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

### RuoShui

```text
触发器: RuoShui (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册进入矩形区域事件(gg_rct______________123)
条件
  ├─ 单位技能等级(触发单位(), A0AV) == 0
  └─ 玩家在玩家组中((触发单位()的所有者), grpUserPlayers) == TRUE
动作
  └─ 伤害: 触发单位()→触发单位(): 单位状态(UnitStateMaxLife, 触发单位()) (AttackTypeChaos/DamageTypeUniversal)
```

### ShuiYuJianSu

```text
触发器: ShuiYuJianSu (技能/物品) [✓]
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

### ShuiYuJianSuHuiFu

```text
触发器: ShuiYuJianSuHuiFu (技能/物品) [✓]
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
  │         设置单位颜色: 触发单位(), 255, 255, 255, 255
  └─ 设置移动速度: 触发单位(), 单位默认移速(触发单位())
```

### 寒冰炽炎合体技能

```text
触发器: 寒冰炽炎合体技能 (技能/物品) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### HeTiEnter1

```text
触发器: HeTiEnter1 (技能/物品) [✓]
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

### HeTiOut1

```text
触发器: HeTiOut1 (技能/物品) [✓]
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

### HeTiEnter2

```text
触发器: HeTiEnter2 (技能/物品) [✓]
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

### HeTiOut2

```text
触发器: HeTiOut2 (技能/物品) [✓]
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

### HeTiCheck

```text
触发器: HeTiCheck (技能/物品) [✓]
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

### ItemSynthesis

```text
触发器: ItemSynthesis (区域/禁地) [✓] — 基地升级
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### ItemUseable

```text
触发器: ItemUseable (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### ItemUseableTarget

```text
触发器: ItemUseableTarget (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, AIwb)
  │    │    ├─ 技能目标单位() == gg_unit_n001_0166
  │    │    ├─ iStepHaoYue == 4
  │    ├─ 则
  │    │    设置 iStepHaoYue = 5
  │    │    设置 pTemp = (gg_unit_n001_0166的位置)
  │    │    销毁特效 创建特效(war3mapImported\chronospher_fx_mediumq.mdx, pTemp)
  │    │    移除 gg_unit_n001_0166
  │    │    隐藏单位: gg_unit_h003_0002
  │    │    销毁触发器(自身)
  │    │    清除点 pTemp
  │    │    显示文本→grpOnline: "TRIGSTR_1123"
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02M)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01D)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01N)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01D)
  │    │    添加物品: I01A, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02N)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01A)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01O)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01A)
  │    │    添加物品: I01B, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02O)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01B)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01P)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01B)
  │    │    添加物品: I01C, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02L)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01C)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01Q)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01C)
  │    │    添加物品: I019, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02P)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01I)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01R)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01I)
  │    │    添加物品: I01J, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02Q)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01J)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01S)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01J)
  │    │    添加物品: I01K, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02R)
  │    │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01K)
  │    ├─ 则
  │    │    删除物品: 技能目标物品()
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01U)
  │    │    删除物品: 单位携带物品(按类型)(触发单位(), I01K)
  │    │    添加物品: I01L, 触发单位()
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02S)
       │    ├─ 物品类型比较(物品类型ID(技能目标物品()), OperatorEqualENE, I01L)
       ├─ 则
       │    删除物品: 技能目标物品()
       │    删除物品: 单位携带物品(按类型)(触发单位(), I01T)
       │    删除物品: 单位携带物品(按类型)(触发单位(), I01L)
       │    添加物品: I01M, 触发单位()
       │    返回
       └─ 否则: (无)
```

### UnitDie

```text
触发器: UnitDie (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 地形可通行(单位X坐标(触发单位()), 单位Y坐标(触发单位()), PathingTypeFloatability) == TRUE
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
  │    │      │      ├─ 条件: (布尔比较(单位持有物品类型(凶手单位(), I00M), OperatorEqualENE, true) 或 布尔比较(单位有魔法效果(凶手单位(), BIrl), OperatorEqualENE, true))
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 英雄等级(凶手单位()) OperatorGreater 156
  │    │      │      │      ├─ 则
  │    │      │      │      │    AddHeroXP: 凶手单位(), 随机[100~1000], ShowHideShow
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
  │    │      ├─ 条件: (凶手单位()类型ID) == n008
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
  │    │    设置 grpTemp = 范围内符合条件的单位(500.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      ├─ SetUnitTimeScale: 选取单位(), 1
  │    │      └─ PauseUnitBJ: PauseUnpauseOptionUnpause, 选取单位()
  │    │    清除点 pTemp
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
  ├─ ── ===================================== ──
  ├─ ── 道玄元神Kill ──
  ├─ 如果
  │    ├─ 条件: 单位技能等级(触发单位(), A04A) == 1
  │    ├─ 则
  │    │    设置 grpTemp = 玩家指定类型单位((触发单位()的所有者), hwt2)
  │    │    单位组: 选取 grpTemp 中所有单位
  │    │      └─ 杀死 选取单位()
  │    │    删除单位组 grpTemp
  │    └─ 否则: (无)
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
  ├─ ── 石头4 ──
  ├─ 如果
  │    ├─ 条件: (触发单位()类型ID) == U001
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~3], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01T, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    如果
  │    │      ├─ 条件: 整数比较(随机[1~3], ==, 1)
  │    │      ├─ 则: 创建物品(指定坐标)(I01Q, 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
  │    │    PolledWait: 60.00
  │    │    复活英雄: 触发单位(), 区域中心X(gg_rct_______004), 区域中心Y(gg_rct_______004), ShowHideShow
  │    │    设置单位朝向: 触发单位(), 90.00
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
  │    ├─ 条件: 全部成立
  │    │    ├─ 触发单位() == gg_unit_H00J_0028
  │    │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    ├─ 则
  │    │    修改 凶手单位() 的HeroStatStr: ModifyMethodAddGetHeroStr(触发单位(), InclusionExclude)
  │    │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd英雄敏捷(触发单位(), InclusionExclude)
  │    │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd英雄智力(触发单位(), InclusionExclude)
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

### UnitDieCinema

```text
触发器: UnitDieCinema (物品系统) [✓]
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
  ├─ ── 贯穿-真 ──
  ├─ 如果
  │    ├─ 条件: 单位持有物品类型(凶手单位(), I01M) == TRUE
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ iStepGuanChuan == 0
  │    │      │    ├─ 单位类型判断(凶手单位(), 英雄) == TRUE
  │    │      │    ├─ 单位类型判断(凶手单位(), UnitTypeSummoned) == TRUE
  │    │      │    ├─ 玩家在玩家组中((凶手单位()的所有者), grpUserPlayers) == TRUE
  │    │      │    ├─ 任一成立
  │    │      ├─ 则
  │    │      │    修改 凶手单位() 的HeroStatStr: ModifyMethodSub1000
  │    │      │    修改 凶手单位() 的HeroStatAgi: ModifyMethodSub1000
  │    │      │    修改 凶手单位() 的HeroStatInt: ModifyMethodSub1000
  │    │      │    删除物品: 单位携带物品(按类型)(凶手单位(), I01M)
  │    │      │    添加物品: I033, 凶手单位()
  │    │      │    杀死 凶手单位()
  │    │      │    设置 iStepGuanChuan = 1
  │    │      │    PanCameraToTimed: 单位X坐标(凶手单位()), 单位Y坐标(凶手单位()), 0
  │    │      │    电影模式: OnOffOn, grpOnline
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_5547", AddSetToAdd, 0, WaitDontWait
  │    │      │    电影模式: OnOffOff, grpOnline
  │    │      │    显示文本→grpOnline: (单位名:凶手单位()) + "使用的妖弓-   贯穿天地   杀戮过多，妖弓吸收庞大死气彻底妖化。英雄受妖气影响瞬间死亡，全属性降低1000。"
  │    │      └─ 否则
  │    │           SetItemUserData: 单位携带物品(按类型)(凶手单位(), I01M), (物品自定义值(单位携带物品(按类型)(凶手单位(), I01M)) + 1)
  │    └─ 否则: (无)
  ├─ ── 埋骨地 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_ubon_0001
  │    ├─ 则
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

### UsableAbility

```text
触发器: UsableAbility (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### PassiveAbility

```text
触发器: PassiveAbility (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### AnyUnitDamaged

```text
触发器: AnyUnitDamaged (物品系统) [✓]
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
  │    │      │    ├─ 随机[1~10] == 9
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
  │    ├─ 条件: 全部成立
  │    │    ├─ (伤害来源()类型ID) == nalb
  │    │    ├─ 伤害值() OperatorGreater 0.01
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
  │    │    伤害: uPlayerHeros[玩家号((伤害来源()的所有者))]→触发单位(): (单位状态(UnitStateMaxLife, 触发单位()) / 4.00) (AttackTypeChaos/DamageTypeUniversal)
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
  ├─ ── 冰玄煞 ──
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ 触发单位() == gg_unit_H002_0094
  │    │    ├─ 伤害值() OperatorGreaterEq 100000.00
  │    │    ├─ 两点距离(触发单位(), 伤害来源()) OperatorGreaterEq 600.00
  │    ├─ 则
  │    │    设置 pTemp = (触发单位()的位置)
  │    │    设置 grpTemp = 范围内符合条件的单位(512, pTemp, 布尔比较(是敌方单位(过滤单位(), (触发单位()的所有者)), OperatorEqualENE, true))
  │    │    设置 uTemp = 随机选取单位组单位(grpTemp)
  │    │    清除点 pTemp
  │    │    设置 pTemp = pTemp
  │    │    销毁特效 创建特效(Abilities\Spells\Undead\Impale\ImpaleHitTarget.mdl, pTemp)
  │    │    伤害目标: 触发单位(), uTemp, 2500000.00, IsNotIs, IsNotNot, AttackTypeChaos, DamageTypeMagic, WEAPON_TYPE_WHOKNOWS
  │    │    清除点 pTemp
  │    │    删除单位组 grpTemp
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

### UnitSummon

```text
触发器: UnitSummon (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### UnitEnterMap

```text
触发器: UnitEnterMap (物品系统) [✓]
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
  │    │      └─ 否则
  │    │           设置单位颜色: 触发单位(), 255, 255, 255, 100
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

### HeroLevelUp

```text
触发器: HeroLevelUp (物品系统) [✓]
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
  │    │      │      │    添加物品: I04N, 触发单位()
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

### HeroLearnSkill

```text
触发器: HeroLearnSkill (物品系统) [✓]
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

### AbilityStartCast

```text
触发器: AbilityStartCast (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 其他类别

```text
触发器: 其他类别 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### YLWuJinChangYe

```text
触发器: YLWuJinChangYe (物品系统) [✓]
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

### CYHuoJingLingInit

```text
触发器: CYHuoJingLingInit (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置 pTemp = (uChiYanHuoJingLing[0]的位置)
  ├─ 循环整数A 1→5
  │    ├─ 设置 uChiYanHuoJingLing[循环整数A] = 创建单位(指定点)((触发单位()的所有者), nlv2, pTemp, 0)
  │    └─ SetUnitVertexColorBJ: uChiYanHuoJingLing[循环整数A], 100, 100, 100, 50.00
  ├─ 添加事件到 gg_trg_CYHuoJingLing: 注册单位事件(uChiYanHuoJingLing[0], UnitEventIssuePointOrder)
  ├─ 添加事件到 gg_trg_CYHuoJingLing: 注册单位事件(uChiYanHuoJingLing[0], UnitEventIssueUnitOrder)
  ├─ 清除点 pTemp
  └─ 销毁触发器(自身)
```

### CYHuoJingLing

```text
触发器: CYHuoJingLing (物品系统) [✓]
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

### JinShengWuWei

```text
触发器: JinShengWuWei (物品系统) [✓]
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

### SetHeroInvincible

```text
触发器: SetHeroInvincible (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 玩家科技等级(R006, (触发单位()的所有者)) == 1
动作
  ├─ 设置无敌: 触发单位(), InvulnerabilityInvulnerable
  ├─ PolledWait: 2
  └─ 设置无敌: 触发单位(), InvulnerabilityVulnerable
```

### UnBlinkable

```text
触发器: UnBlinkable (物品系统) [✓] — 防止魔帝被放风筝有木有
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 是敌方单位(触发单位(), 玩家9(灰)) == TRUE
动作
  ├─ 设置 uTemp = 创建单位(指定坐标)(玩家9(灰), osw3, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
  └─ 单位发布命令(目标): uTemp, UnitOrderPurge, 触发单位()
```

### UnBlinkableFushen

```text
触发器: UnBlinkableFushen (物品系统) [✓] — 防止魔帝被放风筝有木有
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 是敌方单位(触发单位(), (uFuShenMoDi的所有者)) == TRUE
动作
  ├─ 设置 uTemp = 创建单位(指定坐标)((uFuShenMoDi的所有者), osw3, 单位X坐标(触发单位()), 单位Y坐标(触发单位()), 0)
  └─ 单位发布命令(目标): uTemp, UnitOrderPurge, 触发单位()
```

### RepickAbility

```text
触发器: RepickAbility (物品系统) [✓]
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

### 技能计时器

```text
触发器: 技能计时器 (物品系统) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### tTianShuXiaJuan

```text
触发器: tTianShuXiaJuan (物品系统) [✓]
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
       │    修改 uTianShuXiaJuan 的HeroStatStr: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
       │    修改 uTianShuXiaJuan 的HeroStatAgi: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
       │    修改 uTianShuXiaJuan 的HeroStatInt: ModifyMethodSub(物品自定义值(itemTSXJ) x 33)
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

### tBingZhiDiaoLing

```text
触发器: tBingZhiDiaoLing (物品系统) [✓]
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

### tJiCiTianYa

```text
触发器: tJiCiTianYa (物品系统) [✓]
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

### tNJKL

```text
触发器: tNJKL (物品系统) [✓]
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

### tBaoFengxue

```text
触发器: tBaoFengxue (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 循环整数A 1→7
       └─ 如果
            ├─ 条件: 计时器比较(到期计时器(), OperatorEqualENE, tBaoFengXue[循环整数A])
            ├─ 则
            │    设置 uTemp = uPlayerHeros[循环整数A]
            │    如果
            │      ├─ 条件: 单位存活判断(uTemp) == TRUE
            │      ├─ 则
            │      │    设置 pTemp = (uTemp的位置)
            │      │    创建 1个|nalb|→(uTemp的所有者) 在 pTemp 面向默认朝向
            │      │    如果
            │      │      ├─ 条件: 全部成立
            │      │      │    ├─ 单位技能等级(uTemp, A08C) == 1
            │      │      │    ├─ 玩家科技等级(R006, (uTemp的所有者)) == 1
            │      │      ├─ 则
            │      │      │    设置技能等级: 最后创建的单位(), A083, 2
            │      │      └─ 否则: (无)
            │      │    命令 最后创建的单位() → UnitOrderBlizzard 到 pTemp
            │      │    清除点 pTemp
            │      └─ 否则: (无)
            └─ 否则: (无)
```

### tShunZhuanQianNian

```text
触发器: tShunZhuanQianNian (物品系统) [✓]
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
            销毁特效 创建特效(Abilities\Spells\Other\Charm\CharmTarget.mdl, pTemp)
            清除点 pTemp
            如果
              ├─ 条件: 取模(单位自定义值(uShunZhuanQianNian), 10) == 0
              ├─ 则
              │    设置 pTemp = (uShunZhuanQianNian的位置)
              │    设置 grpTemp = 范围内符合条件的单位(500.00, pTemp, 布尔比较(是敌方单位(过滤单位(), (uShunZhuanQianNian的所有者)), OperatorEqualENE, true))
              │    单位组: 选取 grpTemp 中所有单位
              │      ├─ CustomScriptCode: "local unit tu = udg_uShunZhuanQianNian"
              │      ├─ CustomScriptCode: "local integer lv=GetHeroLevel(udg_uShunZhuanQianNian)"
              │      ├─ CustomScriptCode: "local integer ll=GetHeroStatBJ(bj_HEROSTAT_STR, udg_uShunZhuanQianNian, true)"
              │      ├─ CustomScriptCode: "local integer mj=GetHeroStatBJ(bj_HEROSTAT_AGI, udg_uShunZhuanQianNian, true)"
              │      ├─ CustomScriptCode: "local integer zl=GetHeroStatBJ(bj_HEROSTAT_INT, udg_uShunZhuanQianNian, true) "
              │      └─ CustomScriptCode: "call UnitDamageTargetBJ(udg_uShunZhuanQianNian,GetEnumUnit(),0.4*lv*(ll*3.4+m..."
              │    清除点 pTemp
              └─ 否则: (无)
```

### tKongJianGeLie

```text
触发器: tKongJianGeLie (物品系统) [✓]
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

### tSiWangQiXi

```text
触发器: tSiWangQiXi (物品系统) [✓]
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

### tFengChenMoShi

```text
触发器: tFengChenMoShi (物品系统) [✓]
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

### tChuanXinCi

```text
触发器: tChuanXinCi (物品系统) [✓]
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

### tDaoXuanZXSH

```text
触发器: tDaoXuanZXSH (物品系统) [✓]
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

### 初始单位

```text
触发器: 初始单位 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### CreateAnimal

```text
触发器: CreateAnimal (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(2.00)
条件
  └─ 无
动作
  ├─ 销毁触发器(自身)
  ├─  CreateUnit: PlayerNA, ngrd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  ├─  CreateUnit: PlayerNA, nbzd, 区域中心X(gg_rct_____________3), 区域中心Y(gg_rct_____________3), 180.00
  ├─  CreateUnit: PlayerNA, nbwm, 区域中心X(gg_rct_____________2), 区域中心Y(gg_rct_____________2), 180.00
  ├─  CreateUnit: PlayerNA, nadr, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  ├─  CreateUnit: PlayerNA, nrwm, 区域中心X(gg_rct_____________1), 区域中心Y(gg_rct_____________1), 180.00
  ├─  CreateUnit: PlayerNA, U001, 区域中心X(gg_rct_______004), 区域中心Y(gg_rct_______004), 90.00
  ├─  CreateUnit: PlayerNA, nomg, 区域中心X(gg_rct_______u), 区域中心Y(gg_rct_______u), 90.00
  ├─  CreateUnit: PlayerNA, n00O, 区域中心X(gg_rct_______c), 区域中心Y(gg_rct_______c), 270.00
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

### LianJi

```text
触发器: LianJi (单位/战斗) [✓] — 练功房
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

### Boss

```text
触发器: Boss (单位/战斗) [✓]
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
  ├─ ── 老头 ──
  ├─ 如果
  │    ├─ 条件: 触发单位() == gg_unit_H002_0094
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 布尔比较(单位持有物品类型(触发单位(), I03I), OperatorEqualENE, true)
  │    │      ├─ 则: 移动物品到坐标(单位携带物品(按类型)(触发单位(), I03I), 单位X坐标(触发单位()), 单位Y坐标(触发单位()))
  │    │      └─ 否则: 无动作()
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
  │    │      │    开启触发器 gg_trg_QSBHHShow
  │    │      │    开启触发器 gg_trg_QSBHHHide
  │    │      │    创建物品(指定坐标): I036, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    设置 bHaoJie = 1
  │    │      │    创建物品(指定坐标): I02H, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOn, grpPlayerGroupTemp
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3949", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 凶手单位(), (单位名:凶手单位()), SoundNull, "TRIGSTR_3950", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_3987", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_u003_0122, "TRIGSTR_3988", SoundNull, "TRIGSTR_3999", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4000", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4085", AddSetToAdd, 0, WaitDontWait
  │    │      │    TransmissionFromUnitWithNameBJ: grpOnline, 触发单位(), (单位名:触发单位()), SoundNull, "TRIGSTR_4086", AddSetToAdd, 0, WaitDontWait
  │    │      │    ForceClear: grpPlayerGroupTemp
  │    │      │    ForceAddPlayer: grpPlayerGroupTemp, (凶手单位()的所有者)
  │    │      │    电影模式: OnOffOff, grpPlayerGroupTemp
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
  │    │    设置单位归属: gg_unit_Hmkg_0067, PlayerNA, 改变颜色
  │    │    返回
  │    └─ 否则: (无)
  ├─ ── 玄武 ──
  └─ 如果
       ├─ 条件: 触发单位() == gg_unit_Hmkg_0067
       ├─ 则
       │    如果
       │      ├─ 条件: bXuanWu == TRUE
       │      ├─ 则
       │      │    创建物品(指定坐标): kpin, 单位X坐标(触发单位()), 单位Y坐标(触发单位())
       │      │    设置水面颜色: 255, 255, 255, 255
       │      │    设置 bXuanWu = true
       │      └─ 否则: (无)
       │    PolledWait: 60.00
       │    复活英雄: 触发单位(), 区域中心X(gg_rct_______011), 区域中心Y(gg_rct_______011), ShowHideShow
       │    返回
       └─ 否则: (无)
```

### 刷兵

```text
触发器: 刷兵 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### JinGongSheZhi

```text
触发器: JinGongSheZhi (单位/战斗) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 tNextWave 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 dNextWave
  ├─ 运行计时器 tWait (一次性, 120.00s)
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
  │    ├─ 条件: uJinGong[LVCurrent] == nnsw
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家9(灰), Hvsh, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5638")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: uJinGong[LVCurrent] == ogru
  │    ├─ 则
  │    │    设置 uTemp = 创建单位(指定坐标)(玩家9(灰), Hkal, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00)
  │    │    命令 uTemp → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    添加事件到 gg_trg_diyouyoubf: 注册单位事件(uTemp, 单位死亡)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5656")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: uJinGong[LVCurrent] == esen
  │    ├─ 则
  │    │    命令 创建单位(指定坐标)(玩家9(灰), Eevi, 区域中心X(gg_rct__________d), 区域中心Y(gg_rct__________d), 270.00) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_5658")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 全部成立
  │    │    ├─ uJinGong[LVCurrent] == ebal
  │    │    ├─ 玩家科技等级(Rhme, 玩家9(灰)) OperatorGreater 4
  │    ├─ 则
  │    │    电影模式: OnOffOn, grpOnline
  │    │    TransmissionFromUnitWithNameBJ: grpOnline, gg_unit_N00M_0083, "TRIGSTR_3937", SoundNull, "TRIGSTR_3938", AddSetToAdd, 0, WaitDontWait
  │    │    电影模式: OnOffOff, grpOnline
  │    │    循环整数A 1→7: 显示文本(玩家)(玩家循环整数A(), 0, 0, "TRIGSTR_1415")
  │    │    开启触发器 gg_trg_PoXu
  │    │    SetUnitPathing: gg_unit_N00M_0083, PathingOff
  │    │    单位添加物品: gg_unit_N00M_0083, 单位携带物品(按类型)(gg_unit_Uclc_0123, I041)
  │    │    设置单位归属: gg_unit_N00M_0083, 玩家9(灰), 改变颜色
  │    │    IssuePointOrderByIdLoc: gg_unit_N00M_0083, OrderCodeAttack, pHG
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: uJinGong[LVCurrent] == efdr
       ├─ 则
       │    关闭触发器 当前触发器()
       │    删除计时器窗口 最后创建的计时器窗口()
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

### JinGongGuai

```text
触发器: JinGongGuai (单位/战斗) [✓] — 刷怪
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(3.00)
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________001), 区域中心Y(gg_rct__________001), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________002), 区域中心Y(gg_rct__________002), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________003), 区域中心Y(gg_rct__________003), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  └─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[LVCurrent], 区域中心X(gg_rct__________004), 区域中心Y(gg_rct__________004), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
```

### JinGongDengDai

```text
触发器: JinGongDengDai (单位/战斗) [✓] — 计时器
───────────────────────────────────────────────────────
事件
  └─ 计时器 tWait 到期
条件
  └─ 无
动作
  ├─ 运行计时器 tNextWave (一次性, 60.00s)
  ├─ 删除计时器窗口 dNextWave
  ├─ 计时器窗口: tNextWave 标题="第" + ((LVCurrent + 1)转字符串) + "波敌人即将到来"
  ├─ 设置 dNextWave = 最后创建的计时器窗口()
  ├─ 关闭触发器 gg_trg_JinGongGuai
  ├─ 关闭触发器 gg_trg_TeShuGuai
  └─ 设置 LVCurrent = (LVCurrent + 1)
```

### JinGongTooMany

```text
触发器: JinGongTooMany (单位/战斗) [✓] — 计时器满
───────────────────────────────────────────────────────
事件
  └─ 计时器 tTooMany 到期
条件
  └─ 无
动作
  ├─ 删除计时器窗口 dTooMany
  ├─ 设置 grpTemp = 玩家符合条件的单位(玩家9(灰), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, false))
  ├─ 如果
  │    ├─ 条件: (grpTemp中的单位数) OperatorGreaterEq 60
  │    ├─ 则
  │    │    循环整数A 1→7: 宣布失败(玩家循环整数A(), "TRIGSTR_1117")
  │    └─ 否则
  │         关闭触发器 当前触发器()
  └─ 删除单位组 grpTemp
```

### MoDiJinGong

```text
触发器: MoDiJinGong (单位/战斗) [✓]
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

### 特殊怪

```text
触发器: 特殊怪 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### TeShuGuai

```text
触发器: TeShuGuai (单位/战斗) [✓]
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

### 最后的战争

```text
触发器: 最后的战争 (单位/战斗) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### MyGod

```text
触发器: MyGod (单位/战斗) [✓]
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
       │    设置单位归属: 触发单位(), 非玩家, 改变颜色
       │    如果
       │      ├─ 条件: 触发单位() == uChiYanHuoJingLing[0]
       │      ├─ 则
       │      │    循环整数A 1→5
       │      │      ├─ 隐藏单位: uChiYanHuoJingLing[循环整数A]
       │      │      └─ 设置单位归属: uChiYanHuoJingLing[循环整数A], 非玩家, 改变颜色
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
       │    SetPlayerAllianceStateBJ: 玩家9(灰), (uFuShenMoDi的所有者), AllianceSettingAlliedVision
       │    SetPlayerAllianceStateBJ: (uFuShenMoDi的所有者), PlayerNA, AllianceSettingAlliedVision
       │    SetPlayerAllianceStateBJ: PlayerNA, (uFuShenMoDi的所有者), AllianceSettingAlliedVision
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
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, gg_unit_u003_0122, "TRIGSTR_4296", SoundNull, "TRIGSTR_4297", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, uFuShenMoDi, "TRIGSTR_4311", SoundNull, "TRIGSTR_4312", AddSetToAdd, 0, WaitDontWait
       │    TransmissionFromUnitWithNameBJ: bj_FORCE_ALL_PLAYERS, gg_unit_u003_0122, "TRIGSTR_4313", SoundNull, "TRIGSTR_4314", AddSetToAdd, 0, WaitDontWait
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
       │    设置无敌: uFuShenMoDi, InvulnerabilityVulnerable
       │    PauseUnit: uFuShenMoDi, PauseUnpauseOptionUnpause
       │    UnitAddAbilityBJ: Aloc, uFuShenMoDi
       │    UnitRemoveAbilityBJ: Aloc, uFuShenMoDi
       │    命令 uFuShenMoDi → UnitOrderAttack 到 pHG
       └─ 否则
            移动物品到坐标: 被操作物品(), 单位X坐标(触发单位()), 单位Y坐标(触发单位())
```

### LastBattle

```text
触发器: LastBattle (单位/战斗) [✓] — 刷怪
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(3.00)
条件
  └─ 无
动作
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[随机[26~35]], 区域中心X(gg_rct__________001), 区域中心Y(gg_rct__________001), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[随机[26~35]], 区域中心X(gg_rct__________002), 区域中心Y(gg_rct__________002), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[随机[26~35]], 区域中心X(gg_rct__________003), 区域中心Y(gg_rct__________003), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定坐标)(玩家9(灰), uJinGong[随机[26~35]], 区域中心X(gg_rct__________004), 区域中心Y(gg_rct__________004), 0) → UnitOrderAttack 到 区域中心X(gg_rct_____________0000)
  ├─ 命令 创建单位(指定点)(玩家9(灰), H00D, pTeShuGuai[1], 270.00) → UnitOrderAttack 到 pHG
  └─ 命令 创建单位(指定点)(玩家9(灰), H00D, pTeShuGuai[2], 270.00) → UnitOrderAttack 到 pHG
```

### FuShenMoDiStrength

```text
触发器: FuShenMoDiStrength (单位/战斗) [✓]
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

### MyGod 复制

```text
触发器: MyGod 复制 (刷怪/进攻) [✗]
───────────────────────────────────────────────────────
事件
  └─ 单位 gg_unit_uabo_0095 - UnitEventSellItem
条件
  └─ 物品比较(UnitItemInSlot(GetLearningUnit(), 0), OperatorEqualENE, ItemNull)
动作
  ├─ 设置水面颜色: 255, 0, 0, 255
  └─ UnitAddItemSwapped: 最后创建的物品(), gg_unit_H00F_0003
```

