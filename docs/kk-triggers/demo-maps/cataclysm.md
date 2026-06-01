---
title: 大灾变 - 演示图实战
category: kk-triggers
slug: demo-maps/cataclysm
description: 演示图 大灾变 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 大灾变 — 演示图实战

> 演示图：大灾变2.0.w3x
>
> 触发器数：**133**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\大灾变2.0.w3x`

## 📑 触发器目录

- 地图初始化
- 解锁单位寻路上限
- HPMP
- JiaZiYuan
- FuHuo
- TiShi
- YingXiong
- JingTouGaoDu
- XZnandu
- KNnandu
- BeiJingYinYue
- ++2
- CanFei-qt
- ZuZhou-qt
- AnYingTuXi-qt
- ShuangDongXinXing-qt
- ShanDianHuDun-qt
- JingLingZhiHuo-qt
- SiWangChanRao-qt
- 红，青，黑，绿，蓝龙，龙龟，蜥蜴领主吞噬
- tunshi
- 龙龟，深渊领主冲击波
- chongjibo
- 净化
- jinghua
- 献祭
- xianji
- 纠缠根须（中立敌对1）
- jiuchangenxu
- 纠缠根须（中立敌对2）
- jiuchangenxu2
- 占据
- zhanju
- 暴风雪
- baofengxue
- 暗影突袭
- anyingtuxi
- 生命恢复
- shengminghuifu
- 生命恢复（熊怪）
- shengminghuifu2
- 霹雳闪电
- pilishandian
- 治疗守卫
- zhiliaoshouwei
- 野兽幽魂
- yeshouyouhun
- 闪电护盾
- shandianhudun
- 闪电链
- shandianlian
- 雷霆一击（雷霆蜥蜴）
- leitingyiji
- 雷霆一击（中立敌对）
- leitingyiji2
- 法力燃烧（中立敌对1）
- fashao1
- 法力燃烧（中立敌对3）
- fashao3
- 残废
- canfei
- 召唤巨虾
- zhaohuanjuxia
- 腐臭蜂群
- fuchoufengqun
- 邪恶狂热
- xieekuangre
- 震荡波
- zhendangbo
- 投石
- toushi
- 恐怖嚎叫
- kongbuhaojiao
- 霜冻闪电
- shuangdongshandian
- 霜冻闪电（2）
- shuangdongshandian2
- 霜冻新星
- shuangdongxinxing
- 战争践踏（中立敌对1）
- zhanzhengjianta1
- 战争践踏（中立敌对2）
- zhanzhengjianta2
- 医疗波
- yiliaobo
- 魔法护盾
- mofahudun
- 操纵死尸
- caozongsishi
- 叉状闪电
- chazhuangshandian1
- 季风
- jifeng
- 死亡缠绕
- siwangchanrao1
- 地狱火
- diyuhuo
- 火焰呼吸
- huoyanhuxi
- 痛苦之指
- tongkuzhizhi
- 召唤海元素
- zhaohuanhaiyuansu
- 生命汲取
- shengmingjiqu
- 火焰雨
- huoyanyu
- ++
- DaoZhenXuanFeng
- ShanDianLian
- CanFei
- ShuangDongXinXing
- FuChouFengQun
- ZhenDangBo
- SiWangDiaoLing
- HuoYanYu
- BaoFengXue
- LieYanFengBao
- ShanDianHuDun
- ZuZhou
- AnYingTuXi
- JingLingZhiHuo
- SiWangChanRao
- FaLiRanShao
- ChaZhuangShanDian
- XiLan
- 本体吸魂
- 马甲
- on
- off
- 三维书
- NengLiangYaSuo
- HeiAnZhiMen

---

## 📜 触发器代码

### 地图初始化

```text
触发器: 地图初始化 (初始化) [✓] — Inicializaci贸n predeterminada de partida de refriega para todos los jugadores
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ MeleeStartingVisibility
  ├─ MeleeStartingResources
  ├─ MeleeClearExcessUnits
  ├─ MeleeStartingUnits
  ├─ MeleeStartingHeroLimit
  ├─ FogEnableOff
  ├─ FogMaskEnableOff
  ├─ SetCameraField: CameraFieldTargetDistance, 2800.00, 0
  ├─ 设置玩家属性: Player00, PlayerStateGold, 1000000
  ├─ 设置玩家属性: Player00, PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家1(红), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家1(红), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家2(蓝), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家2(蓝), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家3(青), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家3(青), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家4(紫), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家4(紫), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家5(黄), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家5(黄), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家6(橙), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家6(橙), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家7(绿), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家7(绿), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家8(粉), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家8(粉), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家9(灰), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家9(灰), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家10(淡蓝), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家10(淡蓝), PlayerStateLumber, 1000000
  ├─ 设置玩家属性: 玩家11(暗绿), PlayerStateGold, 1000000
  ├─ 设置玩家属性: 玩家11(暗绿), PlayerStateLumber, 1000000
  ├─ SetPlayerHandicapXP: 玩家1(红), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家2(蓝), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家3(青), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家4(紫), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家5(黄), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家6(橙), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家7(绿), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家8(粉), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家9(灰), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家10(淡蓝), 1000000000.00
  ├─ SetPlayerHandicapXP: 玩家11(暗绿), 1000000000.00
  ├─ SetPlayerMaxHeroesAllowed: 1000, Player00
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家1(红)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家2(蓝)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家3(青)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家4(紫)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家5(黄)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家6(橙)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家7(绿)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家8(粉)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家9(灰)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家10(淡蓝)
  ├─ SetPlayerMaxHeroesAllowed: 1000, 玩家11(暗绿)
  ├─ PlayMusicBJ: gg_snd_feichangshuang
  ├─ 设置 DH = gg_unit_Edem_0737
  ├─ StartMeleeAI: 玩家1(红), war3mapImported\human.ai
  ├─ StartMeleeAI: 玩家2(蓝), war3mapImported\human.ai
  ├─ StartMeleeAI: 玩家3(青), war3mapImported\human.ai
  ├─ StartMeleeAI: 玩家4(紫), war3mapImported\orc.ai
  ├─ StartMeleeAI: 玩家5(黄), war3mapImported\orc.ai
  ├─ StartMeleeAI: 玩家6(橙), war3mapImported\orc.ai
  ├─ StartMeleeAI: 玩家7(绿), war3mapImported\orc.ai
  ├─ StartMeleeAI: 玩家8(粉), war3mapImported\undead.ai
  ├─ StartMeleeAI: 玩家9(灰), war3mapImported\undead.ai
  ├─ StartMeleeAI: 玩家10(淡蓝), war3mapImported\undead.ai
  └─ StartMeleeAI: 玩家11(暗绿), war3mapImported\undead.ai
```

### 解锁单位寻路上限

```text
触发器: 解锁单位寻路上限 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 设置局部变量:"ui"=DzCreateFrameByTagName("FRAME", "name", DzGetGameUI(), "template", 0)
  ├─ 设置局部变量:"i"=DzFrameGetAlpha(DzI2F((DzF2I(读取局部变量("ui")) - 172)))
  ├─ DzDestroyFrame: 读取局部变量("ui")
  ├─ 设置局部变量:"i"=(读取局部变量("i") + 自定义代码("2537628"))
  └─ YDWEForLoopLocVarMultiple: "i", 0, 63
```

### HPMP

```text
触发器: HPMP (初始化) [✗]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ CreateTextTagUnitBJ: (实数转整数(单位状态(读取局部变量("my"), UnitStateLife))转字符串) + "/" + (实数转整数(单位状态(读取局部变量("my"), UnitStateMaxLife))转字符串), 读取局部变量("my"), 0, 8.00, 100, 0.00, 0.00, 20.00
  ├─ 设置局部变量:"hp"=GetLastCreatedTextTag()
  ├─ CreateTextTagUnitBJ: (实数转整数(单位状态(读取局部变量("my"), UnitStateLife))转字符串) + "/" + (实数转整数(单位状态(读取局部变量("my"), UnitStateMaxLife))转字符串), 读取局部变量("my"), 0, 8.00, 0.00, 0.00, 100.00, 20.00
  ├─ 设置局部变量:"mp"=GetLastCreatedTextTag()
  └─ 启动计时器: 创建计时器(), 0.03s (循环)
```

### JiaZiYuan

```text
触发器: JiaZiYuan (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(1.00)
条件
  └─ 无
动作
  ├─ 调整 玩家1(红) 的 PlayerStateGold: 10000
  ├─ 调整 玩家1(红) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家2(蓝) 的 PlayerStateGold: 10000
  ├─ 调整 玩家2(蓝) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家3(青) 的 PlayerStateGold: 10000
  ├─ 调整 玩家3(青) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家4(紫) 的 PlayerStateGold: 10000
  ├─ 调整 玩家4(紫) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家5(黄) 的 PlayerStateGold: 10000
  ├─ 调整 玩家5(黄) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家6(橙) 的 PlayerStateGold: 10000
  ├─ 调整 玩家6(橙) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家7(绿) 的 PlayerStateGold: 10000
  ├─ 调整 玩家7(绿) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家8(粉) 的 PlayerStateGold: 10000
  ├─ 调整 玩家8(粉) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家9(灰) 的 PlayerStateGold: 10000
  ├─ 调整 玩家9(灰) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家10(淡蓝) 的 PlayerStateGold: 10000
  ├─ 调整 玩家10(淡蓝) 的 PlayerStateLumber: 10000
  ├─ 调整 玩家11(暗绿) 的 PlayerStateGold: 10000
  └─ 调整 玩家11(暗绿) 的 PlayerStateLumber: 10000
```

### FuHuo

```text
触发器: FuHuo (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 全部成立
动作
  ├─ 设置局部变量:"kaishiweizhi"=GetPlayerStartLocationLoc((死亡单位()的所有者))
  ├─ 等待 5.00s
  ├─ 复活英雄 死亡单位() 在 读取局部变量("kaishiweizhi")
  └─ 清除点 读取局部变量("kaishiweizhi")
```

### TiShi

```text
触发器: TiShi (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  └─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeUpdated, "TRIGSTR_018"
```

### YingXiong

```text
触发器: YingXiong (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(300.00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"wanjia2"=GetPlayerStartLocationLoc(玩家1(红))
  ├─ 设置局部变量:"wanjia3"=GetPlayerStartLocationLoc(玩家2(蓝))
  ├─ 设置局部变量:"wanjia4"=GetPlayerStartLocationLoc(玩家3(青))
  ├─ 设置局部变量:"wanjia5"=GetPlayerStartLocationLoc(玩家4(紫))
  ├─ 设置局部变量:"wanjia6"=GetPlayerStartLocationLoc(玩家5(黄))
  ├─ 设置局部变量:"wanjia7"=GetPlayerStartLocationLoc(玩家6(橙))
  ├─ 设置局部变量:"wanjia8"=GetPlayerStartLocationLoc(玩家7(绿))
  ├─ 设置局部变量:"wanjia9"=GetPlayerStartLocationLoc(玩家8(粉))
  ├─ 设置局部变量:"wanjia10"=GetPlayerStartLocationLoc(玩家9(灰))
  ├─ 设置局部变量:"wanjia11"=GetPlayerStartLocationLoc(玩家10(淡蓝))
  ├─ 设置局部变量:"wanjia12"=GetPlayerStartLocationLoc(玩家11(暗绿))
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_019"
  ├─ 创建 1个|Hblm|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家1(红) 在 读取局部变量("wanjia2") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_020"
  ├─ 等待 3.00s
  ├─ 创建 1个|Hblm|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家2(蓝) 在 读取局部变量("wanjia3") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_021"
  ├─ 等待 3.00s
  ├─ 创建 1个|Hblm|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hblm|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hamg|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ 创建 1个|Hpal|→玩家3(青) 在 读取局部变量("wanjia4") 面向默认朝向
  ├─ 添加物品: ofir, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_022"
  ├─ 等待 3.00s
  ├─ 创建 1个|Oshd|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家4(紫) 在 读取局部变量("wanjia5") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_023"
  ├─ 等待 3.00s
  ├─ 创建 1个|Oshd|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家5(黄) 在 读取局部变量("wanjia6") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_024"
  ├─ 等待 3.00s
  ├─ 创建 1个|Oshd|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家6(橙) 在 读取局部变量("wanjia7") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_025"
  ├─ 等待 3.00s
  ├─ 创建 1个|Oshd|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Oshd|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Otch|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ 创建 1个|Ofar|→玩家7(绿) 在 读取局部变量("wanjia8") 面向默认朝向
  ├─ 添加物品: olig, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_026"
  ├─ 等待 3.00s
  ├─ 创建 1个|Udea|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家8(粉) 在 读取局部变量("wanjia9") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_027"
  ├─ 等待 3.00s
  ├─ 创建 1个|Udea|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家9(灰) 在 读取局部变量("wanjia10") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_028"
  ├─ 等待 3.00s
  ├─ 创建 1个|Udea|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家10(淡蓝) 在 读取局部变量("wanjia11") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_029"
  ├─ 等待 3.00s
  ├─ 创建 1个|Udea|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udea|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Udre|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ 创建 1个|Ucrl|→玩家11(暗绿) 在 读取局部变量("wanjia12") 面向默认朝向
  ├─ 添加物品: ocor, 最后创建的单位()
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_030"
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_031"
  ├─ 清除点 读取局部变量("wanjia2")
  ├─ 清除点 读取局部变量("wanjia3")
  ├─ 清除点 读取局部变量("wanjia4")
  ├─ 清除点 读取局部变量("wanjia5")
  ├─ 清除点 读取局部变量("wanjia6")
  ├─ 清除点 读取局部变量("wanjia7")
  ├─ 清除点 读取局部变量("wanjia8")
  ├─ 清除点 读取局部变量("wanjia9")
  ├─ 清除点 读取局部变量("wanjia10")
  ├─ 清除点 读取局部变量("wanjia11")
  ├─ 清除点 读取局部变量("wanjia12")
  └─ 关闭触发器 当前触发器()
```

### JingTouGaoDu

```text
触发器: JingTouGaoDu (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "视角"
条件
  └─ 无
动作
  ├─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_032"
  └─ SetCameraField: CameraFieldTargetDistance, 2800.00, 0
```

### XZnandu

```text
触发器: XZnandu (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.00)
条件
  └─ 无
动作
  ├─ DialogSetMessageBJ: NDXZDHK, "TRIGSTR_033"
  ├─ DialogAddButtonBJ: NDXZDHK, "TRIGSTR_034"
  ├─ 保存数据到哈希表: [typename30_dialog.NDXZDHK."an"] = bj_lastCreatedButton
  ├─ DialogAddButtonBJ: NDXZDHK, "TRIGSTR_035"
  ├─ 保存数据到哈希表: [typename30_dialog.NDXZDHK."an2"] = bj_lastCreatedButton
  └─ DialogDisplay: Player00, NDXZDHK, ShowHideShow
```

### KNnandu

```text
触发器: KNnandu (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册对话框事件(NDXZDHK)
条件
  └─ 无
动作
  ├─ 如果
  │    ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, 从哈希表读取数据(typename30_dialog, NDXZDHK, "an"))
  │    ├─ 则
  │    │    显示文本→GetPlayersAll(): "TRIGSTR_036"
  │    └─ 否则
  │         如果
  │           ├─ 条件: 对话框按钮比较(被点击的对话框按钮(), OperatorEqualENE, 从哈希表读取数据(typename30_dialog, NDXZDHK, "an2"))
  │           ├─ 则
  │           │    显示文本→GetPlayersAll(): "TRIGSTR_037"
  │           │    SetPlayerTechResearchedSwap: R000, 1, 玩家1(红)
  │           │    SetPlayerTechResearchedSwap: R000, 1, 玩家2(蓝)
  │           │    SetPlayerTechResearchedSwap: R000, 1, 玩家3(青)
  │           │    SetPlayerTechResearchedSwap: R002, 1, 玩家4(紫)
  │           │    SetPlayerTechResearchedSwap: R002, 1, 玩家5(黄)
  │           │    SetPlayerTechResearchedSwap: R002, 1, 玩家6(橙)
  │           │    SetPlayerTechResearchedSwap: R002, 1, 玩家7(绿)
  │           │    SetPlayerTechResearchedSwap: R004, 1, 玩家8(粉)
  │           │    SetPlayerTechResearchedSwap: R004, 1, 玩家9(灰)
  │           │    SetPlayerTechResearchedSwap: R004, 1, 玩家10(淡蓝)
  │           │    SetPlayerTechResearchedSwap: R004, 1, 玩家11(暗绿)
  │           │    设置单位归属: gg_unit_nfoh_0190, 玩家1(红), 不改变颜色
  │           │    UnitRemoveAbilityBJ: ANre, gg_unit_nfoh_0190
  │           │    UnitRemoveAbilityBJ: ACnr, gg_unit_nfoh_0190
  │           │    UnitAddAbilityBJ: A014, gg_unit_nfoh_0190
  │           │    UnitAddAbilityBJ: A00U, gg_unit_nfoh_0190
  │           │    UnitAddAbilityBJ: A01B, gg_unit_nfoh_0190
  │           │    UnitAddAbilityBJ: A01D, gg_unit_nfoh_0190
  │           │    UnitAddAbilityBJ: A01A, gg_unit_nfoh_0190
  │           │    添加物品: I000, DH
  │           │    添加物品: I000, DH
  │           └─ 否则: (无)
  ├─ 关闭触发器 gg_trg_KNnandu
  └─ 关闭触发器 gg_trg_XZnandu
```

### BeiJingYinYue

```text
触发器: BeiJingYinYue (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(87.00)
条件
  └─ 无
动作
  └─ PlayMusicBJ: gg_snd_feichangshuang
```

### ++2

```text
触发器: ++2 (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(240.00)
条件
  └─ 无
动作
  ├─ 设置 MP2 = OperatorRealAdd(MP2, 1.00)
  └─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, YDWEOperatorString3("难度提升：魔法值消耗增加 1 点，当前每个群体技能魔法值消耗为 ", 实数转字符串(MP2), " 点。")
```

### CanFei-qt

```text
触发器: CanFei-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00R)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e006|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderCripple, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### ZuZhou-qt

```text
触发器: ZuZhou-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00Y)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e007|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderCurse, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### AnYingTuXi-qt

```text
触发器: AnYingTuXi-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A011)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e008|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderShadowStrike, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### ShuangDongXinXing-qt

```text
触发器: ShuangDongXinXing-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00N)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e009|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderFrostNova, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### ShanDianHuDun-qt

```text
触发器: ShanDianHuDun-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00T)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e00A|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderLightningShield, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### JingLingZhiHuo-qt

```text
触发器: JingLingZhiHuo-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00X)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e00B|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    设置局部变量:"mj"=最后创建的单位()
  │         │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderFaerieFire, 选取单位()
  │         │    YDWETimerRemoveUnit: 2, 读取局部变量("mj")
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### SiWangChanRao-qt

```text
触发器: SiWangChanRao-qt (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A017)
动作
  ├─ 设置局部变量:"chufa"=(触发单位()的位置)
  ├─ 设置局部变量:"mubiao"=技能目标点()
  ├─ 设置局部变量:"zu"=GetUnitsInRangeOfLocAll(512, 读取局部变量("mubiao"))
  ├─ 单位组: 选取 读取局部变量("zu") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 全部成立
  │         │    ├─ 单位类型判断(选取单位(), 建筑) == TRUE
  │         │    ├─ 单位类型判断(选取单位(), UnitTypeDead) == TRUE
  │         │    ├─ 是敌方单位(选取单位(), (触发单位()的所有者)) == TRUE
  │         ├─ 则
  │         │    创建 1个|e005|→(触发单位()的所有者) 在 读取局部变量("chufa") 面向默认朝向
  │         │    单位发布命令(目标): 最后创建的单位(), UnitOrderDeathCoil, 选取单位()
  │         │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP2)
  │         └─ 否则: (无)
  ├─ 删除单位组 读取局部变量("zu")
  ├─ 清除点 读取局部变量("chufa")
  └─ 清除点 读取局部变量("mubiao")
```

### 红，青，黑，绿，蓝龙，龙龟，蜥蜴领主吞噬

```text
触发器: 红，青，黑，绿，蓝龙，龙龟，蜥蜴领主吞噬 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### tunshi

```text
触发器: tunshi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  └─ 全部成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 龙龟，深渊领主冲击波

```text
触发器: 龙龟，深渊领主冲击波 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### chongjibo

```text
触发器: chongjibo (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACcv, ABILITY_STATE_COOLDOWN) == 0.00
  └─ (单位类型比较((攻击单位()类型ID), OperatorEqualENE, ntrd) 或 单位类型比较((攻击单位()类型ID), OperatorEqualENE, nlrv))
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 净化

```text
触发器: 净化 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### jinghua

```text
触发器: jinghua (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACpu, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 献祭

```text
触发器: 献祭 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### xianji

```text
触发器: xianji (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 35.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACim, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 纠缠根须（中立敌对1）

```text
触发器: 纠缠根须（中立敌对1） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### jiuchangenxu

```text
触发器: jiuchangenxu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Aenr, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 纠缠根须（中立敌对2）

```text
触发器: 纠缠根须（中立敌对2） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### jiuchangenxu2

```text
触发器: jiuchangenxu2 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Aenw, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 占据

```text
触发器: 占据 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhanju

```text
触发器: zhanju (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 250.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACps, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 暴风雪

```text
触发器: 暴风雪 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### baofengxue

```text
触发器: baofengxue (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACbz, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 暗影突袭

```text
触发器: 暗影突袭 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### anyingtuxi

```text
触发器: anyingtuxi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 65.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACss, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 生命恢复

```text
触发器: 生命恢复 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shengminghuifu

```text
触发器: shengminghuifu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACrj, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 生命恢复（熊怪）

```text
触发器: 生命恢复（熊怪） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shengminghuifu2

```text
触发器: shengminghuifu2 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 150.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACr2, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 霹雳闪电

```text
触发器: 霹雳闪电 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### pilishandian

```text
触发器: pilishandian (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACfb, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 治疗守卫

```text
触发器: 治疗守卫 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhiliaoshouwei

```text
触发器: zhiliaoshouwei (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 200.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), AChw, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"gjzd"=(读取局部变量("gjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ 清除点 读取局部变量("gjzd")
```

### 野兽幽魂

```text
触发器: 野兽幽魂 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### yeshouyouhun

```text
触发器: yeshouyouhun (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACs9, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 闪电护盾

```text
触发器: 闪电护盾 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shandianhudun

```text
触发器: shandianhudun (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACls, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 闪电链

```text
触发器: 闪电链 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shandianlian

```text
触发器: shandianlian (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 120.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACcl, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 雷霆一击（雷霆蜥蜴）

```text
触发器: 雷霆一击（雷霆蜥蜴） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### leitingyiji

```text
触发器: leitingyiji (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 90.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACt2, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 雷霆一击（中立敌对）

```text
触发器: 雷霆一击（中立敌对） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### leitingyiji2

```text
触发器: leitingyiji2 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 90.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACtc, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 法力燃烧（中立敌对1）

```text
触发器: 法力燃烧（中立敌对1） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### fashao1

```text
触发器: fashao1 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 50.00
  ├─ 单位状态(UnitStateMana, GetAttackedUnitBJ()) OperatorGreaterEq 1.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Ambd, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 法力燃烧（中立敌对3）

```text
触发器: 法力燃烧（中立敌对3） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### fashao3

```text
触发器: fashao3 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 50.00
  ├─ 单位状态(UnitStateMana, GetAttackedUnitBJ()) OperatorGreaterEq 1.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Ambb, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 残废

```text
触发器: 残废 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### canfei

```text
触发器: canfei (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 175.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACcr, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 召唤巨虾

```text
触发器: 召唤巨虾 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhaohuanjuxia

```text
触发器: zhaohuanjuxia (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Aslp, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 腐臭蜂群

```text
触发器: 腐臭蜂群 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### fuchoufengqun

```text
触发器: fuchoufengqun (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACca, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 邪恶狂热

```text
触发器: 邪恶狂热 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### xieekuangre

```text
触发器: xieekuangre (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 50.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACua, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 震荡波

```text
触发器: 震荡波 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhendangbo

```text
触发器: zhendangbo (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACsh, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 投石

```text
触发器: 投石 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### toushi

```text
触发器: toushi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACtb, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 恐怖嚎叫

```text
触发器: 恐怖嚎叫 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### kongbuhaojiao

```text
触发器: kongbuhaojiao (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 100.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Acht, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 霜冻闪电

```text
触发器: 霜冻闪电 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shuangdongshandian

```text
触发器: shuangdongshandian (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACbf, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 霜冻闪电（2）

```text
触发器: 霜冻闪电（2） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shuangdongshandian2

```text
触发器: shuangdongshandian2 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACcb, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 霜冻新星

```text
触发器: 霜冻新星 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shuangdongxinxing

```text
触发器: shuangdongxinxing (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACfn, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 战争践踏（中立敌对1）

```text
触发器: 战争践踏（中立敌对1） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhanzhengjianta1

```text
触发器: zhanzhengjianta1 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 90.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Awrs, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 战争践踏（中立敌对2）

```text
触发器: 战争践踏（中立敌对2） (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhanzhengjianta2

```text
触发器: zhanzhengjianta2 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 90.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), Awrh, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 医疗波

```text
触发器: 医疗波 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### yiliaobo

```text
触发器: yiliaobo (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 90.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), AChv, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 魔法护盾

```text
触发器: 魔法护盾 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### mofahudun

```text
触发器: mofahudun (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 25.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACmf, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 操纵死尸

```text
触发器: 操纵死尸 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### caozongsishi

```text
触发器: caozongsishi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 250.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACad, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 叉状闪电

```text
触发器: 叉状闪电 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### chazhuangshandian1

```text
触发器: chazhuangshandian1 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 110.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACfl, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 季风

```text
触发器: 季风 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### jifeng

```text
触发器: jifeng (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACmo, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 死亡缠绕

```text
触发器: 死亡缠绕 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### siwangchanrao1

```text
触发器: siwangchanrao1 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACdc, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 地狱火

```text
触发器: 地狱火 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### diyuhuo

```text
触发器: diyuhuo (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 175.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ANin, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 火焰呼吸

```text
触发器: 火焰呼吸 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### huoyanhuxi

```text
触发器: huoyanhuxi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACbc, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### 痛苦之指

```text
触发器: 痛苦之指 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### tongkuzhizhi

```text
触发器: tongkuzhizhi (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 50.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACfd, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 召唤海元素

```text
触发器: 召唤海元素 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhaohuanhaiyuansu

```text
触发器: zhaohuanhaiyuansu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACwe, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
```

### 生命汲取

```text
触发器: 生命汲取 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shengmingjiqu

```text
触发器: shengmingjiqu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 75.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACdr, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  └─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
```

### 火焰雨

```text
触发器: 火焰雨 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### huoyanyu

```text
触发器: huoyanyu (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false)))
  ├─ 单位状态(UnitStateMana, 攻击单位()) OperatorGreaterEq 125.00
  ├─ YDWEGetUnitAbilityState(攻击单位(), ACrf, ABILITY_STATE_COOLDOWN) == 0.00
  └─ 任一成立
动作
  ├─ 设置局部变量:"gjz"=攻击单位()
  ├─ 设置局部变量:"bgjz"=GetAttackedUnitBJ()
  ├─ 设置局部变量:"bgjzd"=(读取局部变量("bgjz")的位置)
  ├─ 启动计时器: 创建计时器(), 0.00s (一次性)
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("gjz")
  ├─ YDWEFlushAllByUserData: 单位类型, 读取局部变量("bgjz")
  └─ 清除点 读取局部变量("bgjzd")
```

### ++

```text
触发器: ++ (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(240.00)
条件
  └─ 无
动作
  ├─ 设置 MP = OperatorRealAdd(MP, 1.00)
  └─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, YDWEOperatorString3("难度提升：魔法值消耗增加 1 点，当前每个技能魔法值消耗为 ", 实数转字符串(MP), " 点。")
```

### DaoZhenXuanFeng

```text
触发器: DaoZhenXuanFeng (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"A"=(攻击单位()的位置)
       │    设置局部变量:"B"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("B") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00P
       │    单位发布命令(立即): 最后创建的单位(), UnitOrderFanOfKnives
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2.00, 最后创建的单位()
       │    清除点 读取局部变量("A")
       │    清除点 读取局部变量("B")
       └─ 否则: (无)
```

### ShanDianLian

```text
触发器: ShanDianLian (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"C"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("C") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00K
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderChainLightning, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("C")
       └─ 否则: (无)
```

### CanFei

```text
触发器: CanFei (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 30) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"G"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("G") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00R
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderCripple, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("G")
       └─ 否则: (无)
```

### ShuangDongXinXing

```text
触发器: ShuangDongXinXing (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"I"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("I") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00N
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderFrostNova, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2.00, 最后创建的单位()
       │    清除点 读取局部变量("I")
       └─ 否则: (无)
```

### FuChouFengQun

```text
触发器: FuChouFengQun (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"K"=(攻击单位()的位置)
       │    设置局部变量:"L"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("K") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00M
       │    命令 最后创建的单位() → UnitOrderCarrionSwarm 到 读取局部变量("L")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("K")
       │    清除点 读取局部变量("L")
       └─ 否则: (无)
```

### ZhenDangBo

```text
触发器: ZhenDangBo (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"M"=(攻击单位()的位置)
       │    设置局部变量:"N"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("M") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00L
       │    命令 最后创建的单位() → UnitOrderShockwave 到 读取局部变量("N")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("M")
       │    清除点 读取局部变量("N")
       └─ 否则: (无)
```

### SiWangDiaoLing

```text
触发器: SiWangDiaoLing (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 10) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"O"=(攻击单位()的位置)
       │    设置局部变量:"P"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("O") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00O
       │    命令 最后创建的单位() → UnitOrderDeathAndDecay 到 读取局部变量("P")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 1.00, 最后创建的单位()
       │    清除点 读取局部变量("O")
       │    清除点 读取局部变量("P")
       └─ 否则: (无)
```

### HuoYanYu

```text
触发器: HuoYanYu (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"Q"=(攻击单位()的位置)
       │    设置局部变量:"R"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("Q") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00S
       │    命令 最后创建的单位() → UnitOrderHeroRainOfFire 到 读取局部变量("R")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2.00, 最后创建的单位()
       │    清除点 读取局部变量("Q")
       │    清除点 读取局部变量("R")
       └─ 否则: (无)
```

### BaoFengXue

```text
触发器: BaoFengXue (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"QQ"=(攻击单位()的位置)
       │    设置局部变量:"RR"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("QQ") 面向默认朝向
       │    添加技能: 最后创建的单位(), A008
       │    命令 最后创建的单位() → UnitOrderBlizzard 到 读取局部变量("RR")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2.00, 最后创建的单位()
       │    清除点 读取局部变量("QQ")
       │    清除点 读取局部变量("RR")
       └─ 否则: (无)
```

### LieYanFengBao

```text
触发器: LieYanFengBao (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"S"=(攻击单位()的位置)
       │    设置局部变量:"T"=(GetAttackedUnitBJ()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("S") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00J
       │    命令 最后创建的单位() → UnitOrderFlameStrike 到 读取局部变量("T")
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2.00, 最后创建的单位()
       │    清除点 读取局部变量("S")
       │    清除点 读取局部变量("T")
       └─ 否则: (无)
```

### ShanDianHuDun

```text
触发器: ShanDianHuDun (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 30) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"U"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("U") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00T
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderLightningShield, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("U")
       └─ 否则: (无)
```

### ZuZhou

```text
触发器: ZuZhou (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 30) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"W"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("W") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00Y
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderCurse, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("W")
       └─ 否则: (无)
```

### AnYingTuXi

```text
触发器: AnYingTuXi (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"AA"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("AA") 面向默认朝向
       │    添加技能: 最后创建的单位(), A011
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderShadowStrike, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("AA")
       └─ 否则: (无)
```

### JingLingZhiHuo

```text
触发器: JingLingZhiHuo (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 30) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"Y"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("Y") 面向默认朝向
       │    添加技能: 最后创建的单位(), A00X
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderFaerieFire, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("Y")
       └─ 否则: (无)
```

### SiWangChanRao

```text
触发器: SiWangChanRao (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 50.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"aq"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("aq") 面向默认朝向
       │    添加技能: 最后创建的单位(), A017
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderDeathCoil, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("aq")
       └─ 否则: (无)
```

### FaLiRanShao

```text
触发器: FaLiRanShao (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 40) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  ├─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
  └─ 单位状态(UnitStateMana, GetAttackedUnitBJ()) OperatorGreaterEq 1.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"as"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("as") 面向默认朝向
       │    添加技能: 最后创建的单位(), A018
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderManaBurn, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("as")
       └─ 否则: (无)
```

### ChaZhuangShanDian

```text
触发器: ChaZhuangShanDian (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(GetAttackedUnitBJ(), (攻击单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(攻击单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(GetAttackedUnitBJ(), 建筑), OperatorEqualENE, false))))
  └─ 单位状态(UnitStateMana, DH) OperatorGreaterEq 2.00
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(攻击单位(), I005) == TRUE
       ├─ 则
       │    设置局部变量:"av"=(攻击单位()的位置)
       │    创建 1个|e000|→(攻击单位()的所有者) 在 读取局部变量("av") 面向默认朝向
       │    添加技能: 最后创建的单位(), A019
       │    单位发布命令(目标): 最后创建的单位(), UnitOrderForkedLightning, GetAttackedUnitBJ()
       │    SetUnitState: DH, UnitStateManaSec, OperatorRealSubtract(单位状态(UnitStateMana, DH), MP)
       │    YDWETimerRemoveUnit: 2, 最后创建的单位()
       │    清除点 读取局部变量("av")
       └─ 否则: (无)
```

### XiLan

```text
触发器: XiLan (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A018)
  └─ (GetSpellAbilityUnit()类型ID) == e000
动作
  ├─ 设置局部变量:"A"=RMinBJ(单位状态(UnitStateMana, 技能目标单位()), 50.00)
  ├─ SetUnitState: DH, UnitStateManaSec, OperatorRealAdd(单位状态(UnitStateMana, DH), 读取局部变量("A"))
  └─ YDWEFlushAllByUserData: typename02_real, 读取局部变量("A")
```

### 本体吸魂

```text
触发器: 本体吸魂 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(死亡单位(), (凶手单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(凶手单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(死亡单位(), 建筑), OperatorEqualENE, false))))
动作
  └─ 如果
       ├─ 条件: 单位持有物品类型(凶手单位(), I005) == TRUE
       ├─ 则
       │    修改 凶手单位() 的HeroStatStr: ModifyMethodAdd1
       │    修改 凶手单位() 的HeroStatAgi: ModifyMethodAdd1
       │    修改 凶手单位() 的HeroStatInt: ModifyMethodAdd1
       └─ 否则: (无)
```

### 马甲

```text
触发器: 马甲 (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ (整数比较(随机[1~100], OperatorLessEq, 20) 且 (布尔比较(IsUnitAlly(死亡单位(), (凶手单位()的所有者)), OperatorEqualENE, false) 且 (布尔比较(是镜像单位(凶手单位()), OperatorEqualENE, false) 且 布尔比较(单位类型判断(死亡单位(), 建筑), OperatorEqualENE, false))))
动作
  └─ 如果
       ├─ 条件: (凶手单位()类型ID) == e000
       ├─ 则
       │    修改 DH 的HeroStatStr: ModifyMethodAdd1
       │    修改 DH 的HeroStatAgi: ModifyMethodAdd1
       │    修改 DH 的HeroStatInt: ModifyMethodAdd1
       └─ 否则: (无)
```

### on

```text
触发器: on (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "三维书"
条件
  └─ 无
动作
  ├─ 开启触发器 gg_trg__________u
  └─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_038"
```

### off

```text
触发器: off (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "关闭"
条件
  └─ 无
动作
  ├─ 关闭触发器 gg_trg__________u
  └─ QuestMessageBJ: GetPlayersAll(), QuestMessageTypeAlwaysHint, "TRIGSTR_039"
```

### 三维书

```text
触发器: 三维书 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册循环计时器事件(30.00)
条件
  └─ 无
动作
  ├─ 设置局部变量:"suiji"=区域内随机点(gg_rct______________020)
  ├─ 创建物品: I000, 读取局部变量("suiji")
  └─ 清除点 读取局部变量("suiji")
```

### NengLiangYaSuo

```text
触发器: NengLiangYaSuo (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A005)
动作
  ├─ 修改 DH 的HeroStatInt: ModifyMethodSet实数转整数(YDWEOperatorReal3((英雄属性(HeroStatInt, DH, InclusionExclude)转实数), YOperatorAdd, OperatorRealMultiply((英雄属性(HeroStatStr, DH, InclusionExclude)转实数), 0.90), YOperatorAdd, OperatorRealMultiply((英雄属性(HeroStatAgi, DH, InclusionExclude)转实数), 0.90)))
  ├─ 修改 DH 的HeroStatStr: ModifyMethodSet实数转整数(OperatorRealMultiply((英雄属性(HeroStatStr, DH, InclusionExclude)转实数), 0.10))
  └─ 修改 DH 的HeroStatAgi: ModifyMethodSet实数转整数(OperatorRealMultiply((英雄属性(HeroStatAgi, DH, InclusionExclude)转实数), 0.10))
```

### HeiAnZhiMen

```text
触发器: HeiAnZhiMen (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A00G)
动作
  ├─ 设置局部变量:"jnd"=技能目标点()
  ├─ 等待 0.80s
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  ├─ 创建 1个|ChooseRandomCreepBJ(随机[1~10])|→Player00 在 读取局部变量("jnd") 面向默认朝向
  └─ 清除点 读取局部变量("jnd")
```

