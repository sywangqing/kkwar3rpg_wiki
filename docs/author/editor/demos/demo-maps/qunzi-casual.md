---
title: 裙子休闲 - 演示图实战
category: kk-triggers
slug: demo-maps/qunzi-casual
description: 演示图 裙子休闲 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 裙子休闲 — 演示图实战

> 演示图：裙子休闲.w3x
>
> 触发器数：**44**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- MapSet
- AddGame
- ChoseGame
- PlayerRanking
- UnitEnterReg
- PiaoFuWenZi
- PlayerLeftGame
- 判断一个数是否是小数
- DecimalValueTrigger
- AnShaJieShao__介绍__ 复制
- SaiMaChuFa
- SRGameSet
- SRGameTrigger
- SRGameFunction
- SLGameSet
- SLGameTrigger
- SJGameSet
- SJGameTrigger
- SJGameFunction
- YYGameSet
- YYGameTrigger
- YYFunction
- GHGameSet
- GHGameTrigger
- GHFunction
- ZSGameSet
- ZSGameTrigger
- ZSGameFunction
- ZSGameFunction2
- ZSGameFunction3
- SKGameSet
- SKGameTrigger
- SKFunction
- DGGameSet
- DGGameTrigger
- DGFunction
- ZZGameSet
- ZZGameTrigger
- ZZFunction
- PCGameSet
- PCGameTrigger
- PCFunction
- 1
- 2

---

## 📜 触发器代码

### MapSet

```text
触发器: MapSet (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.01)
条件
  └─ 无
动作
  ├─ ── 是否是测试模式 ──
  ├─ 设置 debug = false
  ├─ ── 提示 ──
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_855"
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_854"
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_856"
  ├─ 执行区域代码块: "选择效果显示"
  ├─ 执行区域代码块: "运行触发器"
  ├─ 执行区域代码块: "变量注册"
  ├─ 执行区域代码块: "玩家组状态"
  ├─ 如果
  │    ├─ 条件: debug == TRUE
  │    ├─ 则
  │    │    ForForceMultiple: OnlinePlayerGroup
  │    └─ 否则
  │         设置 FastGameMod = true
  │         战争迷雾开关: EnabledDisabledDisabled
  │         FogMaskEnableOff
  └─ 执行区域代码块: "在规定时间内选择玩的游戏"
```

### AddGame

```text
触发器: AddGame (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 玩家组玩家数(OnlinePlayerGroup)
  ├─ 设置 GameListNum = 玩家组玩家数(OnlinePlayerGroup)
  ├─ ── 游戏触发器注册 ──
  ├─ 保存数据到哈希表: [typename08_unitcode.h004."GameTrigger"] = gg_trg_AnShaJieShao_________________u
  ├─ 保存数据到哈希表: [typename08_unitcode.h006."GameTrigger"] = gg_trg_SRGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00B."GameTrigger"] = gg_trg_SLGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00F."GameTrigger"] = gg_trg_SJGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00P."GameTrigger"] = gg_trg_YYGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00T."GameTrigger"] = gg_trg_GHGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00V."GameTrigger"] = gg_trg_ZSGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h00Z."GameTrigger"] = gg_trg_SKGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h014."GameTrigger"] = gg_trg_DGGameSet
  ├─ 保存数据到哈希表: [typename08_unitcode.h018."GameTrigger"] = gg_trg_ZZGameSet
  └─ 保存数据到哈希表: [typename08_unitcode.h01E."GameTrigger"] = gg_trg_PCGameSet
```

### ChoseGame

```text
触发器: ChoseGame (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ YDWEForLoopLocVarMultiple: "i", 1, 999
```

### PlayerRanking

```text
触发器: PlayerRanking (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ StopMusicBJ: FadeDontFade
  ├─ PlaySoundBJ: gg_snd_ClanInvitation
  ├─ 显示文本→OnlinePlayerGroup: "TRIGSTR_309"
  ├─ CinematicFadeBJ: FadeTypeOptionFadeOut, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  └─ 启动计时器: 创建计时器(), 5.00s (一次性)
```

### UnitEnterReg

```text
触发器: UnitEnterReg (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("unit")."ChoseHandle"] = CreateTrigger()
  └─ YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("unit"), "ChoseHandle")
```

### PiaoFuWenZi

```text
触发器: PiaoFuWenZi (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"pf"=CreateTextTag()
  ├─ SetTextTagPos: 读取局部变量("pf"), 读取局部变量("posX"), 读取局部变量("posY"), 0
  ├─ SetTextTagTextBJ: 读取局部变量("pf"), 读取局部变量("text"), 20.00
  └─ 保存数据到哈希表: [单位类型.读取局部变量("unit")."pfwz"] = 读取局部变量("pf")
```

### PlayerLeftGame

```text
触发器: PlayerLeftGame (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventLeave(PlayerALL)
条件
  └─ 无
动作
  ├─ 显示文本→OnlinePlayerGroup: (玩家名:触发玩家()) + " 离开了游戏！"
  ├─ 销毁触发器(自身)
  └─ 移除 从哈希表读取数据(玩家, 触发玩家(), "systemUnit")
```

### 判断一个数是否是小数

```text
触发器: 判断一个数是否是小数 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### DecimalValueTrigger

```text
触发器: DecimalValueTrigger (玩家/英雄) [✓] — ture 不是小数

false 是小数
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"math"=读取局部变量("num")
  ├─ 设置局部变量:"math2"=实数转整数(读取局部变量("math"))
  └─ 如果
       ├─ 条件: (读取局部变量("math") - (读取局部变量("math2")转实数)) == 0.00
       ├─ 则
       │    设置 DecimalReturnVaule = true
       └─ 否则
            设置 DecimalReturnVaule = false
```

### AnShaJieShao__介绍__ 复制

```text
触发器: AnShaJieShao*/介绍/* 复制 (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  ├─ 执行区域代码块: "游戏提示"
  ├─ 执行区域代码块: "注册移动"
  └─ 执行区域代码块: "注册移动"
```

### SaiMaChuFa

```text
触发器: SaiMaChuFa (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [玩家.Player00."horse"] = gg_unit_h001_0074
  ├─ 保存数据到哈希表: [玩家.玩家1(红)."horse"] = gg_unit_h001_0073
  ├─ 保存数据到哈希表: [玩家.玩家2(蓝)."horse"] = gg_unit_h001_0072
  ├─ 保存数据到哈希表: [玩家.玩家3(青)."horse"] = gg_unit_h001_0071
  ├─ 保存数据到哈希表: [玩家.玩家4(紫)."horse"] = gg_unit_h001_0070
  ├─ 保存数据到哈希表: [玩家.玩家5(黄)."horse"] = gg_unit_h001_0069
  ├─ 保存数据到哈希表: [玩家.玩家6(橙)."horse"] = gg_unit_h001_0068
  ├─ 保存数据到哈希表: [玩家.玩家7(绿)."horse"] = gg_unit_h001_0067
  ├─ 执行区域代码块: "移动合集"
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  ├─ 启动计时器: 创建计时器(), 2.00s (循环)
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### SRGameSet

```text
触发器: SRGameSet (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### SRGameTrigger

```text
触发器: SRGameTrigger (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  ├─ 设置局部变量:"pool"=CreateUnitPool()
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Hpal, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Hmkg, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Hlgr, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Otch, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Nsjs, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Orex, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Udea, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Udre, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Ucrl, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Npld, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Obla, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Usyl, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Ewrd, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Edem, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Emoo, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Nngs, 1
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Uwar, 0.30
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Nmag, 0.50
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), Uktl, 1.00
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 888
  ├─ 设置局部变量:"num"=0
  └─ YDWEForLoopLocVarMultiple: "i", 1, 888
```

### SRGameFunction

```text
触发器: SRGameFunction (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    YDWEForLoopLocVarMultiple: "o", 1, 8
       └─ 否则
            如果
              ├─ 条件: 读取局部变量("functionID") == 2
              ├─ 则
              │    保存数据到哈希表: [单位类型.读取局部变量("fz")."fzSkillTrigger"] = CreateTrigger()
              │    YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("fz"), "fzSkillTrigger")
              └─ 否则
                   如果
                     ├─ 条件: 读取局部变量("functionID") == 3
                     ├─ 则
                     │    启动计时器: 创建计时器(), 5.00s (循环)
                     └─ 否则: (无)
```

### SLGameSet

```text
触发器: SLGameSet (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ 设置局部变量:"g"=区域内符合条件的单位(gg_rct_SenLinHuoZai, 单位类型比较((过滤单位()类型ID), OperatorEqualENE, n000))
  ├─ 单位组: 选取 读取局部变量("g") 中所有单位
  │    └─ 播放动画: 选取单位(), "stand"
  ├─ 删除单位组 读取局部变量("g")
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### SLGameTrigger

```text
触发器: SLGameTrigger (区域/禁地) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 启动计时器: 创建计时器(), 4.00s (循环)
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### SJGameSet

```text
触发器: SJGameSet (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### SJGameTrigger

```text
触发器: SJGameTrigger (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"pool"=CreateUnitPool()
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), h00I, 6.00
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), h00J, 4.00
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), h00L, 3.50
  ├─ UnitPoolAddUnitType: 读取局部变量("pool"), h00K, 2.00
  ├─ 启动计时器: 创建计时器(), 0.50s (循环)
  ├─ 保存数据到哈希表: [玩家.PlayerNA."SkillTrigger"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, PlayerNA, "SkillTrigger")
  ├─ 保存数据到哈希表: [玩家.PlayerNA."SkillTrigger2"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, PlayerNA, "SkillTrigger2")
  ├─ 保存数据到哈希表: [玩家.PlayerNA."DeadEvent"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, PlayerNA, "DeadEvent")
  └─ 执行区域代码块: "游戏时间设置"
```

### SJGameFunction

```text
触发器: SJGameFunction (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    保存数据到哈希表: [单位类型.读取局部变量("dw")."SkillTrigger"] = CreateTrigger()
       │    YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("dw"), "SkillTrigger")
       └─ 否则: (无)
```

### YYGameSet

```text
触发器: YYGameSet (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea1
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea2
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea3
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea4
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea5
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea6
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea7
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 YYArea[读取局部变量("num")] = gg_rct_PlayerArea8
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 10
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### YYGameTrigger

```text
触发器: YYGameTrigger (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 执行区域代码块: "游戏时间设置"
```

### YYFunction

```text
触发器: YYFunction (单位/战斗) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    保存数据到哈希表: [单位类型.读取局部变量("dw")."SkillTrigger"] = CreateTrigger()
       │    YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("dw"), "SkillTrigger")
       └─ 否则: (无)
```

### GHGameSet

```text
触发器: GHGameSet (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### GHGameTrigger

```text
触发器: GHGameTrigger (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### GHFunction

```text
触发器: GHFunction (刷怪/进攻) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    保存数据到哈希表: [单位类型.读取局部变量("dw")."SkillTrigger"] = CreateTrigger()
       │    YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("dw"), "SkillTrigger")
       └─ 否则: (无)
```

### ZSGameSet

```text
触发器: ZSGameSet (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea1
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea2
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea3
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea4
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea5
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea6
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea7
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置 ZSarea[读取局部变量("num")] = gg_rct_QDPlayerArea8
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### ZSGameTrigger

```text
触发器: ZSGameTrigger (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("first") == TRUE
       ├─ 则
       │    YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction, tirggerexecute_notcondition
       │    YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction, tirggerexecute_notcondition
       └─ 否则
            YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction, tirggerexecute_notcondition
            YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction, tirggerexecute_notcondition
```

### ZSGameFunction

```text
触发器: ZSGameFunction (其他) [✓] — function1  初始化题库

function2  存入题目

function3  随机取出题目
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    ── 初始化题库ID ──
       │    YDWEForLoopLocVarMultiple: "i", 1, 50
       └─ 否则
            如果
              ├─ 条件: 读取局部变量("functionID") == 2
              ├─ 则
              │    ── 存入题目 ──
              │    YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction3, tirggerexecute_notcondition
              └─ 否则
                   如果
                     ├─ 条件: 读取局部变量("functionID") == 3
                     ├─ 则
                     │    ── 获取题库中的题目数量 ──
                     │    YDWEForLoopLocVarMultiple: "i", 1, 50
                     │    ── 从题库中抽题 ──
                     │    设置局部变量:"num"=随机[1~TiKuLong]
                     │    设置 QuestionData = YDWEGetIntegerByInteger(YDWEGetForceID(TiKu), 读取局部变量("num"))
                     └─ 否则
                          如果
                            ├─ 条件: 读取局部变量("functionID") == 4
                            ├─ 则
                            │    YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction, tirggerexecute_notcondition
                            │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), gg_unit_h00W_0128, "TRIGSTR_497", SoundNull, YDWEOperatorString3("题目是： ", 从哈希表读取数据(整数, QuestionData, "题目"), " 请输入你们的答案"), AddSetToSet, 5.00, WaitDontDont
                            │    YDWERegisterTriggerMultiple: CreateTrigger()
                            └─ 否则: (无)
```

### ZSGameFunction2

```text
触发器: ZSGameFunction2 (其他) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"data"=随机[100000~1000000]
  ├─ 保存数据到哈希表: [整数.读取局部变量("data")."题目"] = 读取局部变量("question")
  ├─ 保存数据到哈希表: [整数.读取局部变量("data")."答案"] = 读取局部变量("answer")
  ├─ 如果
  │    ├─ 条件: 读取局部变量("txwt") == TRUE
  │    ├─ 则
  │    │    保存数据到哈希表: [整数.读取局部变量("data")."正确答案"] = 读取局部变量("zq")
  │    │    保存数据到哈希表: [整数.读取局部变量("data")."错误答案"] = 读取局部变量("cw")
  │    └─ 否则: (无)
  └─ YDWEForLoopLocVarMultiple: "i", 1, 50
```

### ZSGameFunction3

```text
触发器: ZSGameFunction3 (其他) [✓] — 存入题目触发
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置局部变量:"n1"=随机[1~100]
  ├─ 设置局部变量:"n2"=随机[1~100]
  ├─ 设置局部变量:"n3"=(读取局部变量("n1") x 读取局部变量("n2"))
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置局部变量:"n1"=随机[1~1000]
  ├─ 设置局部变量:"n2"=随机[1~1000]
  ├─ 设置局部变量:"n3"=(读取局部变量("n1") + 读取局部变量("n2"))
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置局部变量:"n1"=随机[1~100]
  ├─ 设置局部变量:"n2"=随机[1~10]
  ├─ 设置局部变量:"n3"=(读取局部变量("n1") / 读取局部变量("n2"))
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ 设置局部变量:"n1"=随机[1001~10000]
  ├─ 设置局部变量:"n2"=随机[1~1000]
  ├─ 设置局部变量:"n3"=(读取局部变量("n1") - 读取局部变量("n2"))
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  ├─ 设置局部变量:"num"=(读取局部变量("num") + 1)
  ├─ YDWEExecuteTriggerMultiple: gg_trg_ZSGameFunction2, tirggerexecute_notcondition
  └─ 如果
       ├─ 条件: debug == TRUE
       ├─ 则
       │    BJDebugMsg: YDWEOperatorString3("题库目前有：", (读取局部变量("num")转字符串), " 道题")
       └─ 否则: (无)
```

### SKGameSet

```text
触发器: SKGameSet (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  └─ 执行区域代码块: "游戏提示"
```

### SKGameTrigger

```text
触发器: SKGameTrigger (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ YDWERegisterTriggerMultiple: CreateTrigger()
  ├─ YDWEExecuteTriggerMultiple: gg_trg_SKFunction, tirggerexecute_notcondition
  ├─ 设置 SKcount = (SKcount + 1)
  └─ 执行区域代码块: "游戏时间设置"
```

### SKFunction

```text
触发器: SKFunction (分类9) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    显示文本→OnlinePlayerGroup: "TRIGSTR_639"
       │    保存数据到哈希表: [玩家.Player00."locationSave"] = true
       │    启动计时器: 创建计时器(), 0.01s (循环)
       │    启动计时器: 创建计时器(), 1.00s (循环)
       └─ 否则: (无)
```

### DGGameSet

```text
触发器: DGGameSet (分类10) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 执行区域代码块: "区域注册"
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### DGGameTrigger

```text
触发器: DGGameTrigger (分类10) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ YDWEExecuteTriggerMultiple: gg_trg_DGFunction, tirggerexecute_notcondition
```

### DGFunction

```text
触发器: DGFunction (分类10) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    设置局部变量:"g"=区域内全部单位(gg_rct______________099)
       │    单位组: 选取 读取局部变量("g") 中所有单位
       │      └─ 移除 选取单位()
       │    删除单位组 读取局部变量("g")
       │    设置局部变量:"n1"=从哈希表读取数据(玩家, 非玩家, "EndpointNum1")
       │    设置局部变量:"n2"=从哈希表读取数据(玩家, 非玩家, "EndpointNum2")
       │    设置局部变量:"n3"=从哈希表读取数据(玩家, 非玩家, "EndpointNum3")
       │    设置局部变量:"endnum"=YDWEOperatorInt3(读取局部变量("n1"), YOperatorAdd, 读取局部变量("n2"), YOperatorAdd, 读取局部变量("n3"))
       │    保存数据到哈希表: [玩家.非玩家."dgEndNum"] = 读取局部变量("endnum")
       │    启动计时器: 创建计时器(), 3.00s (循环)
       └─ 否则
            如果
              ├─ 条件: 读取局部变量("functionID") == 2
              ├─ 则
              │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), gg_unit_h00W_0146, "TRIGSTR_714", SoundNull, "TRIGSTR_715", AddSetToSet, 5.00, WaitDontDont
              │    保存数据到哈希表: [玩家.非玩家."dgTimer1"] = 创建计时器()
              │    设置局部变量:"timer"=从哈希表读取数据(玩家, 非玩家, "dgTimer1")
              │    计时器窗口: 读取局部变量("timer") 标题="TRIGSTR_716"
              │    保存数据到哈希表: [计时器.读取局部变量("timer")."timerBox"] = 最后创建的计时器窗口()
              │    启动计时器: 读取局部变量("timer"), 10.00s (一次性)
              │    保存数据到哈希表: [玩家.非玩家."dgTrigger1"] = CreateTrigger()
              │    YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, 非玩家, "dgTrigger1")
              └─ 否则
                   如果
                     ├─ 条件: 读取局部变量("functionID") == 3
                     ├─ 则
                     │    启动计时器: 创建计时器(), 3.00s (一次性)
                     └─ 否则
                          如果
                            ├─ 条件: 读取局部变量("functionID") == 4
                            ├─ 则
                            │    设置 DGgameNum = (DGgameNum + 1)
                            │    如果
                            │      ├─ 条件: DGgameNum != 6
                            │      ├─ 则
                            │      │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), gg_unit_h00W_0146, "TRIGSTR_779", SoundNull, YDWEOperatorString3("现在进行第", (DGgameNum转字符串), "轮游戏！"), AddSetToSet, 5.00, WaitDontDont
                            │      │    保存数据到哈希表: [玩家.非玩家."EndpointNum1"] = 随机[1~6]
                            │      │    保存数据到哈希表: [玩家.非玩家."EndpointNum2"] = 随机[1~6]
                            │      │    保存数据到哈希表: [玩家.非玩家."EndpointNum3"] = 随机[1~6]
                            │      │    启动计时器: 创建计时器(), 3.00s (一次性)
                            │      └─ 否则
                            │           设置局部变量:"arrayLength"=8
                            │           YDWEForLoopLocVarMultiple: "i", 1, 读取局部变量("arrayLength")
                            │           YDWEForLoopLocVarMultiple: "a", 1, 读取局部变量("arrayLength")
                            │           YDWEForLoopLocVarMultiple: "i", 1, 3
                            │           YDWEExecuteTriggerMultiple: gg_trg_PlayerRanking, tirggerexecute_notcondition
                            │           YDWEForLoopLocVarMultiple: "i", 1, 8
                            │           设置局部变量:"g2"=区域内全部单位(gg_rct_DuGouYouXi)
                            │           单位组: 选取 读取局部变量("g2") 中所有单位
                            │             ├─ 销毁触发器(自身)
                            │             ├─ YDWEFlushAllByUserData: 单位类型, 选取单位()
                            │             └─ 移除 选取单位()
                            │           删除单位组 读取局部变量("g2")
                            └─ 否则
                                 如果
                                   ├─ 条件: 读取局部变量("functionID") == 5
                                   ├─ 则
                                   │    保存数据到哈希表: [单位类型.读取局部变量("dw")."SkillTrigger"] = CreateTrigger()
                                   │    YDWERegisterTriggerMultiple: 从哈希表读取数据(单位类型, 读取局部变量("dw"), "SkillTrigger")
                                   └─ 否则: (无)
```

### ZZGameSet

```text
触发器: ZZGameSet (分类11) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  ├─ PauseAllUnitsBJ: PauseUnpauseOptionPause
  └─ 执行区域代码块: "游戏提示"
```

### ZZGameTrigger

```text
触发器: ZZGameTrigger (分类11) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 25
  ├─ 执行区域代码块: "游戏时间设置"
  └─ YDWEExecuteTriggerMultiple: gg_trg_ZZFunction, tirggerexecute_notcondition
```

### ZZFunction

```text
触发器: ZZFunction (分类11) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    保存数据到哈希表: [玩家.非玩家."clickTrigger"] = CreateTrigger()
       │    YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, 非玩家, "clickTrigger")
       └─ 否则: (无)
```

### PCGameSet

```text
触发器: PCGameSet (分类12) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ ForForceMultiple: OnlinePlayerGroup
  ├─ YDWEForLoopLocVarMultiple: "i", 1, 8
  ├─ CinematicFadeBJ: FadeTypeOptionFadeIn, 5.00, CineFilterTextureBlack, 0, 0, 0, 0
  └─ 执行区域代码块: "游戏提示"
```

### PCGameTrigger

```text
触发器: PCGameTrigger (分类12) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  ├─ 保存数据到哈希表: [玩家.非玩家."PcGameTrigger1"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, 非玩家, "PcGameTrigger1")
  ├─ 保存数据到哈希表: [玩家.非玩家."PcGameTrigger2"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, 非玩家, "PcGameTrigger2")
  ├─ 保存数据到哈希表: [玩家.非玩家."PcGameTrigger3"] = CreateTrigger()
  ├─ YDWERegisterTriggerMultiple: 从哈希表读取数据(玩家, 非玩家, "PcGameTrigger3")
  └─ YDWERegisterTriggerMultiple: CreateTrigger()
```

### PCFunction

```text
触发器: PCFunction (分类12) [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ 如果
       ├─ 条件: 读取局部变量("functionID") == 1
       ├─ 则
       │    设置局部变量:"dw"=读取局部变量("unit")
       │    设置局部变量:"d"=(读取局部变量("dw")的位置)
       │    设置局部变量:"d2"=PolarProjectionBJ(读取局部变量("d"), 从哈希表读取数据(玩家, (读取局部变量("dw")的所有者), "reallong"), 单位朝向角度(读取局部变量("dw")))
       │    设置局部变量:"jd"=AngleBetweenPoints(读取局部变量("d"), 读取局部变量("d2"))
       │    设置局部变量:"ss"=两点间距(读取局部变量("d"), 读取局部变量("d2"))
       │    设置局部变量:"ss2"=0.00
       │    设置局部变量:"ss3"=0.00
       │    添加技能: 读取局部变量("dw"), Amrf
       │    移除技能: 读取局部变量("dw"), Amrf
       │    启动计时器: 创建计时器(), 0.03s (循环)
       │    销毁特效 读取局部变量("tx")
       │    销毁特效 读取局部变量("tx2")
       └─ 否则: (无)
```

### 1

```text
触发器: 1 (分类13) [✓]
───────────────────────────────────────────────────────
事件
  └─ TriggerRegisterPlayerEventEndCinematic(Player00)
条件
  └─ debug == TRUE
动作
  └─ YDWEExecuteTriggerMultiple: 从哈希表读取数据(typename08_unitcode, h01E, "GameTrigger"), tirggerexecute_notcondition
```

### 2

```text
触发器: 2 (分类13) [✓]
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(0.01)
条件
  └─ debug == TRUE
动作
  └─ 执行区域代码块: "区域注册"
```

