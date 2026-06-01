---
title: 勇者斗兽人 - 演示图实战
category: kk-triggers
slug: demo-maps/hero-vs-beast
description: 演示图 勇者斗兽人 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 勇者斗兽人 — 演示图实战

> 演示图：勇者斗兽人_未加密 (1).w3x
>
> 触发器数：**89**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\勇者斗兽人_未加密 (1).w3x`

## 📑 触发器目录

- Melee Initialization
- xinshi
- quantu
- juankuan
- baohuqi
- kaijujishiqi
- fuhuo
- kaijushijianxianzhi
- xuanren
- 忍者技能
- 流体电流
- 雷遁·天雷引
- 影子死亡删除尸体
- 技能 忍者
- 刺客技能
- 刺客技能隐匿
- 刺客技能 心眼
- 刺客技能-暗影突袭
- 刺客技能技艺·闪
- 圣弓技能
- shenfa
- 神官技能
- shenguanqh
- shenguanhuyou
- 赶尸人技能
- ganshirenqh
- 矿人技能
- tujinglingluo
- 半蜥人技能
- longyan
- 法师技能
- lieyanchongji
- zddj
- jiechufuzhou
- huo
- huoqh
- shui
- feng
- fengqh
- tu
- 猎人技能
- miaozhun
- 战士技能
- zhanshigongji
- zhanshi
- zhanshixuexi
- zhanshishanbi
- zhanshiqidong
- 暗夜骑士技能
- anyeqishi
- sanags
- sanayc
- 当玩家位置存在电脑时默认建造
- computerai
- 玩家超过1分钟没有选择难度默认难度1
- mrnd
- 玩家输入yzyw进入建造模式
- p1
- 选择难度
- ndxz
- 不同难度的科技奖励
- jl
- fc
- zdyz
- 吸血
- liandao
- liandaono
- jingjizhijia
- wanghundediyu
- sishenliandao
- cuidianzhiren
- leishenquanzhang
- kexuemianju
- dazao
- zbxz
- jzxz
- yuanguyizhi
- yuanbguyizhixianzhi
- yzywjinyongzhuangbei
- chattxet
- chat_attack
- chat_hypotenemia
- bossstart
- 1-1-BOSS群体击晕
- 1-3-BOSS跳斩
- 1-4-BOSS分身
- 1-5-BOSS分身死亡
- bossAI
- bosskill

---

## 📜 触发器代码

### Melee Initialization

```text
触发器: Melee Initialization (初始化) [✓] — 这张图是我用时一个半月时间更新的地图

内容十分简陋且贫乏

起初我做这张图的初衷是探索魔兽本身的玩法可以做到什么样的程度

目前看来，原生的内容可操作空间还是太小了

这张图我会放在kk平台萌新作者群

以供萌新参考学习

群号：174936168

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ 设置 player[1] = 0
  ├─ 设置 player[2] = 0
  ├─ 设置 player[3] = 0
  ├─ 设置 player[4] = 0
  ├─ 设置 player[5] = 0
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_666", "TRIGSTR_667", ReplaceableTextures\CommandButtons\BTNManual2.blp
  ├─ 创建任务: QuestTypeReqDiscovered, "TRIGSTR_670", "TRIGSTR_671", ReplaceableTextures\CommandButtons\BTNManual2.blp
  ├─ 创建任务: QuestTypeOptDiscovered, "TRIGSTR_672", "TRIGSTR_673", ReplaceableTextures\CommandButtons\BTNManual2.blp
  ├─ 创建任务: QuestTypeOptDiscovered, "TRIGSTR_674", "TRIGSTR_675", ReplaceableTextures\CommandButtons\BTNManual2.blp
  ├─ 创建任务: QuestTypeOptDiscovered, "TRIGSTR_676", "TRIGSTR_677", ReplaceableTextures\CommandButtons\BTNManual2.blp
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_381"
  ├─ SetMapFlag: MapFlagResourceTradingLock, OnOffOn
  ├─ 平移镜头: Player00, (区域gg_rct_Endboss中心), 0
  ├─ 平移镜头: 玩家1(红), (区域gg_rct_Endboss中心), 0
  ├─ 平移镜头: 玩家2(蓝), (区域gg_rct_Endboss中心), 0
  ├─ 平移镜头: 玩家3(青), (区域gg_rct_Endboss中心), 0
  ├─ 平移镜头: 玩家4(紫), (区域gg_rct_Endboss中心), 0
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, Player00, FogStateVisible, gg_rct_Endboss
  ├─ 设置 K1 = GetLastCreatedFogModifier()
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, 玩家1(红), FogStateVisible, gg_rct_Endboss
  ├─ 设置 K2 = GetLastCreatedFogModifier()
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, 玩家2(蓝), FogStateVisible, gg_rct_Endboss
  ├─ 设置 K3 = GetLastCreatedFogModifier()
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, 玩家3(青), FogStateVisible, gg_rct_Endboss
  ├─ 设置 K4 = GetLastCreatedFogModifier()
  ├─ CreateFogModifierRectBJ: EnabledDisabledEnabled, 玩家4(紫), FogStateVisible, gg_rct_Endboss
  ├─ 设置 K5 = GetLastCreatedFogModifier()
  ├─ MeleeStartingVisibility
  ├─ MeleeStartingHeroLimit
  ├─ MeleeGrantHeroItems
  ├─ MeleeStartingResources
  ├─ MeleeClearExcessUnits
  ├─ MeleeStartingUnitsForPlayer: RaceHuman, 玩家5(黄), GetPlayerStartLocationLoc(玩家5(黄)), InclusionInclude
  ├─ 创建 1个|h006|→玩家5(黄) 在 GetPlayerStartLocationLoc(玩家5(黄)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家6(橙), GetPlayerStartLocationLoc(玩家6(橙)), InclusionInclude
  ├─ 创建 1个|h006|→玩家6(橙) 在 GetPlayerStartLocationLoc(玩家6(橙)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家7(绿), GetPlayerStartLocationLoc(玩家7(绿)), InclusionInclude
  ├─ 创建 1个|h006|→玩家7(绿) 在 GetPlayerStartLocationLoc(玩家7(绿)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家8(粉), GetPlayerStartLocationLoc(玩家8(粉)), InclusionInclude
  ├─ 创建 1个|h006|→玩家8(粉) 在 GetPlayerStartLocationLoc(玩家8(粉)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家9(灰), GetPlayerStartLocationLoc(玩家9(灰)), InclusionInclude
  ├─ 创建 1个|h006|→玩家9(灰) 在 GetPlayerStartLocationLoc(玩家9(灰)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家10(淡蓝), GetPlayerStartLocationLoc(玩家10(淡蓝)), InclusionInclude
  ├─ 创建 1个|h006|→玩家10(淡蓝) 在 GetPlayerStartLocationLoc(玩家10(淡蓝)) 面向默认朝向
  ├─ MeleeStartingUnitsForPlayer: RaceOrc, 玩家11(暗绿), GetPlayerStartLocationLoc(玩家11(暗绿)), InclusionInclude
  ├─ 创建 1个|h006|→玩家11(暗绿) 在 GetPlayerStartLocationLoc(玩家11(暗绿)) 面向默认朝向
  ├─ MeleeStartingAI
  ├─ MeleeInitVictoryDefeat
  ├─ 设置玩家属性: Player00, PlayerStateGold, 0
  ├─ 设置玩家属性: 玩家1(红), PlayerStateGold, 0
  ├─ 设置玩家属性: 玩家2(蓝), PlayerStateGold, 0
  ├─ 设置玩家属性: 玩家3(青), PlayerStateGold, 0
  ├─ 设置玩家属性: 玩家4(紫), PlayerStateGold, 0
  ├─ 设置玩家属性: Player00, PlayerStateLumber, 0
  ├─ 设置玩家属性: 玩家1(红), PlayerStateLumber, 0
  ├─ 设置玩家属性: 玩家2(蓝), PlayerStateLumber, 0
  ├─ 设置玩家属性: 玩家3(青), PlayerStateLumber, 0
  ├─ 设置玩家属性: 玩家4(紫), PlayerStateLumber, 0
  ├─ SetPlayerTeam: Player00, 0
  ├─ SetPlayerTeam: 玩家1(红), 0
  ├─ SetPlayerTeam: 玩家2(蓝), 0
  ├─ SetPlayerTeam: 玩家3(青), 0
  ├─ SetPlayerTeam: 玩家4(紫), 0
  ├─ SetPlayerFlag: 玩家5(黄), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家6(橙), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家7(绿), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家8(粉), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家9(灰), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家10(淡蓝), PlayerFlagGivesBounty, OnOffIntOn
  ├─ SetPlayerFlag: 玩家11(暗绿), PlayerFlagGivesBounty, OnOffIntOn
  ├─ 关闭触发器 当前触发器()
  └─ 销毁触发器(自身)
```

### xinshi

```text
触发器: xinshi (初始化) [✓] — 这部分触发的作用是限制信使可购买的数量

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01C)
动作
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 物品比较(单位携带物品(按类型)(GetManipulatingUnit(), I01C), OperatorEqualENE, 被操作物品())
       │    ├─ CountLivingPlayerUnitsOfTypeId(n00U, (GetManipulatingUnit()的所有者)) == 0
       │    ├─ GetPlayerTeam((GetManipulatingUnit()的所有者)) == 2
       ├─ 则
       └─ 否则
            如果
              ├─ 条件: GetPlayerTeam((GetManipulatingUnit()的所有者)) == 2
              ├─ 则
              │    显示文本→(GetManipulatingUnit()的所有者): 0
              └─ 否则
                   显示文本→(GetManipulatingUnit()的所有者): 0
            调整 (GetManipulatingUnit()的所有者) 的 PlayerStateGold: 300
            删除物品: 被操作物品()
```

### quantu

```text
触发器: quantu (初始化) [✓] — 显示全图，后来发现，其实只要不是属性书和等级书技能，并不会因为非英雄单位使用技能使地图崩溃，后来懒得改了

但是可以依托这种方法做出宠物吃书给英雄增加三维

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01D)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: gomn, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, texp)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01F, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tstr)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01G, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tst2)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01H, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tdex)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01I, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tdx2)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01J, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tpow)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01K, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tint)
  │    ├─ 则
  │    │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("hero") 中所有单位
  │    │      └─ 添加物品: I01L, 选取单位()
  │    │    GroupClear: 读取局部变量("hero")
  │    │    删除单位组 读取局部变量("hero")
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tin2)
       ├─ 则
       │    设置局部变量:"hero"=玩家符合条件的单位((GetManipulatingUnit()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
       │    单位组: 选取 读取局部变量("hero") 中所有单位
       │      └─ 添加物品: I01M, 选取单位()
       │    GroupClear: 读取局部变量("hero")
       │    删除单位组 读取局部变量("hero")
       │    返回
       └─ 否则: (无)
```

### juankuan

```text
触发器: juankuan (初始化) [✓] — 这部分内容的作用是赠送资源给盟友

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I013)
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 调整 玩家5(黄) 的 PlayerStateGold: 500
  └─ 开启触发器 当前触发器()
```

### baohuqi

```text
触发器: baohuqi (初始化) [✓] — 这部分内容是到达一定时间移除一部分初始设置的单位

如果使用马甲单位在地图中间释放覆盖全图的巫毒技能

则可以实现开局规定时间内指定玩家的所有单位无敌

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(180.00)
条件
  └─ 无
动作
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_1585"
  ├─ 设置局部变量:"tawo"=GetUnitsOfTypeIdAll(h006)
  ├─ 单位组: 选取 读取局部变量("tawo") 中所有单位
  │    ├─ 设置局部变量:"t"=选取单位()
  │    └─ 移除 读取局部变量("t")
  ├─ GroupClear: 读取局部变量("tawo")
  ├─ 删除单位组 读取局部变量("tawo")
  ├─ 关闭触发器 当前触发器()
  └─ 销毁触发器(自身)
```

### kaijujishiqi

```text
触发器: kaijujishiqi (初始化) [✓] — 计时器窗口

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(1.00)
条件
  └─ 无
动作
  ├─ 运行计时器 创建计时器() (一次性, 59.00s)
  ├─ 设置局部变量:"jsq"=bj_lastStartedTimer
  ├─ 计时器窗口: 读取局部变量("jsq") 标题="TRIGSTR_629"
  ├─ YDWESetAnyTypeLocalArray: typename25_timerdialog, "jsqck", 0, bj_lastCreatedTimerDialog
  ├─ TimerDialogDisplay: YDWEGetAnyTypeLocalArray("jsqck", 0), ShowHideShow
  ├─ 启动计时器: 创建计时器(), 59.00s (一次性)
  ├─ 运行计时器 创建计时器() (一次性, 179.00s)
  ├─ 设置局部变量:"bhq"=bj_lastStartedTimer
  ├─ 计时器窗口: 读取局部变量("bhq") 标题="TRIGSTR_1161"
  ├─ YDWESetAnyTypeLocalArray: typename25_timerdialog, "bhqck", 0, bj_lastCreatedTimerDialog
  ├─ TimerDialogDisplay: YDWEGetAnyTypeLocalArray("bhqck", 0), ShowHideShow
  ├─ 启动计时器: 创建计时器(), 179.00s (一次性)
  ├─ 关闭触发器 当前触发器()
  └─ 销毁触发器(自身)
```

### fuhuo

```text
触发器: fuhuo (初始化) [✓] — 英雄复活

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ GetPlayerTeam((触发单位()的所有者)) == 2
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"id"=GetHeroProperName(触发单位())
  ├─ 设置局部变量:"sw"=触发单位()
  ├─ 设置局部变量:"syz"=(读取局部变量("sw")的所有者)
  ├─ 设置局部变量:"dj"=GetUnitLevel(触发单位())
  ├─ 设置局部变量:"fhsj"=OperatorRealMultiply((读取局部变量("dj")转实数), 6.00)
  ├─ 设置局部变量:"fhd"=(区域gg_rct_Endboss中心)
  ├─ 显示文本→读取局部变量("syz"): 0
  ├─ 运行计时器 创建计时器() (一次性, 读取局部变量("fhsj")s)
  ├─ 设置局部变量:"jsq"=bj_lastStartedTimer
  ├─ 计时器窗口: 读取局部变量("jsq") 标题=读取局部变量("id") + "复活时间"
  ├─ YDWESetAnyTypeLocalArray: typename25_timerdialog, "jsqck", 0, bj_lastCreatedTimerDialog
  ├─ TimerDialogDisplay: YDWEGetAnyTypeLocalArray("jsqck", 0), ShowHideShow
  ├─ 启动计时器: 创建计时器(), 读取局部变量("fhsj")s (一次性)
  └─ 开启触发器 当前触发器()
```

### kaijushijianxianzhi

```text
触发器: kaijushijianxianzhi (初始化) [✓] — 选英雄时间结束后限制玩家不可选取英雄

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(60.00)
条件
  └─ 无
动作
  ├─ DestroyFogModifier: K1
  ├─ DestroyFogModifier: K2
  ├─ DestroyFogModifier: K3
  ├─ DestroyFogModifier: K4
  ├─ DestroyFogModifier: K5
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(Player00) != 1
  │    ├─ 则
  │    │    SetPlayerTeam: Player00, 2
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(玩家1(红)) != 1
  │    ├─ 则
  │    │    SetPlayerTeam: 玩家1(红), 2
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(玩家2(蓝)) != 1
  │    ├─ 则
  │    │    SetPlayerTeam: 玩家2(蓝), 2
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(玩家3(青)) != 1
  │    ├─ 则
  │    │    SetPlayerTeam: 玩家3(青), 2
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(玩家4(紫)) != 1
  │    ├─ 则
  │    │    SetPlayerTeam: 玩家4(紫), 2
  │    └─ 否则: (无)
  ├─ 关闭触发器 gg_trg_xuanren
  ├─ 销毁触发器(自身)
  ├─ 关闭触发器 当前触发器()
  └─ 销毁触发器(自身)
```

### xuanren

```text
触发器: xuanren (初始化) [✓] — 选择英雄并创建初始物品

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  ├─ 注册玩家选择事件(Player00, 选择)
  ├─ 注册玩家选择事件(玩家1(红), 选择)
  ├─ 注册玩家选择事件(玩家2(蓝), 选择)
  ├─ 注册玩家选择事件(玩家3(青), 选择)
  └─ 注册玩家选择事件(玩家4(紫), 选择)
条件
  ├─ 任一成立
  ├─ (触发单位()的所有者) == 非玩家
  └─ 单位类型判断(触发单位(), 英雄) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"cfwj"=触发玩家()
  ├─ 设置局部变量:"yx"=触发单位()
  ├─ 设置局部变量:"yxdw"=(读取局部变量("yx")类型ID)
  ├─ 设置局部变量:"yxd"=(读取局部变量("yx")的位置)
  ├─ 设置局部变量:"wjbh"=GetPlayerTeam(读取局部变量("cfwj"))
  ├─ 设置局部变量:"yxbh"=单位自定义值(触发单位())
  ├─ 设置局部变量:"wjid"=玩家号(读取局部变量("cfwj"))
  ├─ 设置局部变量:"csqz"=stel
  ├─ 设置局部变量:"ygyz"=I00I
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 读取局部变量("wjbh") == 0
       │    ├─ 读取局部变量("yxbh") == 读取局部变量("wjbh")
       ├─ 则
       │    显示文本→读取局部变量("cfwj"): 0
       │    设置单位归属: 读取局部变量("yx"), 读取局部变量("cfwj"), 改变颜色
       │    添加物品: 读取局部变量("csqz"), 读取局部变量("yx")
       │    创建物品: 读取局部变量("ygyz"), 读取局部变量("yxd")
       │    设置局部变量:"xwp"=bj_lastCreatedItem
       │    SetItemUserData: 读取局部变量("xwp"), 读取局部变量("wjid")
       │    单位添加物品: 读取局部变量("yx"), 读取局部变量("xwp")
       │    设置玩家属性: 读取局部变量("cfwj"), PlayerStateGold, 500
       │    SetPlayerTeam: 读取局部变量("cfwj"), 2
       │    清除点 读取局部变量("yxd")
       └─ 否则
            设置单位自定义值: 读取局部变量("yx"), 读取局部变量("wjid")
            启动计时器: 创建计时器(), 0.20s (一次性)
            清除点 读取局部变量("yxd")
```

### 忍者技能

```text
触发器: 忍者技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 流体电流

```text
触发器: 流体电流 (玩家/英雄) [✓] — 忍者和刺客技能是我后期写的

这部分触发我更换了不同是书写手法

如果你可以理解其中的原理

尽可能使用这些触发器的书写手法

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ (伤害来源()类型ID) == N00W
  └─ YDWEIsEventAttackDamage() == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 伤害目标: 伤害来源(), 触发单位(), OperatorRealMultiply(OperatorRealAdd(单位状态(伤害来源(), UnitStateDamageBase), 单位状态(伤害来源(), UnitStateDamageBonus)), 0.50), IsNotNot, IsNotNot, AttackTypeMagic, DamageTypeLightning, WEAPON_TYPE_WHOKNOWS
  └─ 开启触发器 当前触发器()
```

### 雷遁·天雷引

```text
触发器: 雷遁·天雷引 (玩家/英雄) [✓] — 给单位添加乌鸦形态技能可以使单位可以飞行

有关于跳跃函数其实就是利用这个原理制作

如果你有兴趣制作自定义跳跃轨迹的技能

这个触发可以很好的帮助你理解跳跃的原理

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A05V)
动作
  ├─ 设置局部变量:"A"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"B"=技能目标单位()
  ├─ SetPlayerAbilityAvailable: (读取局部变量("A")的所有者), A05V, EnableDisableDisable
  ├─ 设置单位自定义值: 读取局部变量("A"), 3
  ├─ 添加技能: 读取局部变量("A"), S000
  ├─ 添加技能: 读取局部变量("A"), A05X
  ├─ 启动计时器: 创建计时器(), 15.00s (一次性)
  ├─ 设置局部变量:"tx"=创建特效(附着单位)(Abilities\Spells\Other\Drain\ManaDrainCaster.mdl, 读取局部变量("A"), "overhead")
  ├─ 添加技能: 读取局部变量("A"), Amrf
  ├─ SetUnitPathing: 读取局部变量("A"), PathingOff
  ├─ 添加技能: 读取局部变量("A"), Amrf
  ├─ YDWEFlyEnable: GetSpellAbilityUnit()
  ├─ 设置局部变量:"h"=GetUnitFlyHeight(读取局部变量("A"))
  ├─ 启动计时器: 创建计时器(), 0.03s (循环)
  ├─ 设置局部变量:"tx1"=创建特效(附着单位)(Abilities\Spells\Other\Drain\ManaDrainTarget.mdl, 读取局部变量("b"), "overhead")
  ├─ PolledWait: 2
  ├─ 设置局部变量:"x"=单位X坐标(读取局部变量("B"))
  ├─ 设置局部变量:"y"=单位Y坐标(读取局部变量("B"))
  ├─ 移动单位: 读取局部变量("A"), 读取局部变量("x"), 读取局部变量("y")
  ├─ SetUnitFlyHeightBJ: 读取局部变量("A"), 0.00, 0.00
  ├─ 移除技能: 读取局部变量("A"), Amrf
  ├─ SetUnitPathing: 读取局部变量("A"), PathingOn
  ├─ 销毁特效 读取局部变量("tx")
  ├─ 销毁特效 读取局部变量("tx1")
  ├─ 设置局部变量:"tx2"=创建特效(指定坐标)(Abilities\Spells\Human\Thunderclap\ThunderClapCaster.mdl, 读取局部变量("x"), 读取局部变量("y"))
  ├─ EXSetEffectSize: 读取局部变量("tx2"), 2.00
  ├─ YDWETimerDestroyEffect: 2, 读取局部变量("tx2")
  ├─ 设置局部变量:"mj"=创建单位(指定坐标)((读取局部变量("A")的所有者), n003, 读取局部变量("x"), 读取局部变量("y"), 0)
  ├─ 添加技能: 读取局部变量("mj"), Awrs
  ├─ 单位发布命令(立即): 读取局部变量("mj"), UnitOrderStomp
  ├─ YDWETimerRemoveUnit: 2, 读取局部变量("mj")
  ├─ 设置局部变量:"j"=0.00
  ├─ 设置局部变量:"x"=单位X坐标(读取局部变量("A"))
  ├─ 设置局部变量:"y"=单位Y坐标(读取局部变量("A"))
  ├─ 设置局部变量:"d"=Location(读取局部变量("x"), 读取局部变量("y"))
  ├─ 循环整数A 1→3
  │    ├─ 设置局部变量:"C"=创建单位(指定坐标)((读取局部变量("A")的所有者), n00X, 点X坐标(PolarProjectionBJ(读取局部变量("d"), 400.00, 读取局部变量("j"))), 点Y坐标(PolarProjectionBJ(读取局部变量("d"), 400.00, 读取局部变量("j"))), 0)
  │    ├─ 设置单位自定义值: 读取局部变量("C"), 循环整数A()
  │    ├─ 设置局部变量:"j"=OperatorRealAdd(读取局部变量("j"), 120.00)
  │    ├─ 设置 ying[循环整数A()] = 读取局部变量("C")
  │    └─ 启动计时器: 创建计时器(), 15.00s (一次性)
  └─ 清除点 读取局部变量("d")
```

### 影子死亡删除尸体

```text
触发器: 影子死亡删除尸体 (玩家/英雄) [✓] — 任何单位死亡都会留下尸体

捕捉单位死亡的瞬间删除单位

就可以实现不出现单位尸体

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ (死亡单位()类型ID) == n00X
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  └─ 移除 死亡单位()
```

### 技能 忍者

```text
触发器: 技能 忍者 (玩家/英雄) [✓] — 这部分触发是忍者技能的核心机制

利用全局变量记录影子

从而在场地上出现不同的马甲单位时

可以精准选中需要的单位

另外，也可以利用单位的自定义

绑定数组的索引实现每一个影子都能传送

或者利用诱捕等技能可以实现

类似DOTA幽鬼一样选择单位进行互换位置的操作

类似于火影忍者羁绊中四代目火影的瞬身苦无的制作方法

污染者锤石的守护污染者锤石开源图中有详细制作方法

有需要的可以去看看

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == N00W
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"A"=GetSpellAbilityUnit()
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A05R)
  │    ├─ 则
  │    │    SetPlayerAbilityAvailable: (读取局部变量("A")的所有者), A05R, EnableDisableDisable
  │    │    添加技能: 读取局部变量("A"), A05Q
  │    │    设置局部变量:"cd"=OperatorRealMultiply((单位技能等级(读取局部变量("A"), A05R)转实数), 5.00)
  │    │    启动计时器: 创建计时器(), 读取局部变量("cd")s (一次性)
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A05Q)
  │    ├─ 则
  │    │    设置局部变量:"x1"=单位X坐标(读取局部变量("A"))
  │    │    设置局部变量:"y1"=单位Y坐标(读取局部变量("A"))
  │    │    设置局部变量:"group"=玩家符合条件的单位((读取局部变量("A")的所有者), (单位比较(过滤单位(), OperatorNotEqualENE, ying[1]) 且 (单位比较(过滤单位(), OperatorNotEqualENE, ying[1]) 且 (单位比较(过滤单位(), OperatorNotEqualENE, ying[2]) 且 (单位比较(过滤单位(), OperatorNotEqualENE, ying[3]) 且 单位类型比较((过滤单位()类型ID), OperatorEqualENE, n00X))))))
  │    │    设置局部变量:"B"=单位组第一个单位(读取局部变量("group"))
  │    │    GroupClear: 读取局部变量("group")
  │    │    删除单位组 读取局部变量("group")
  │    │    设置局部变量:"x2"=单位X坐标(读取局部变量("B"))
  │    │    设置局部变量:"y2"=单位Y坐标(读取局部变量("B"))
  │    │    移动单位: 读取局部变量("A"), 读取局部变量("x2"), 读取局部变量("y2")
  │    │    移动单位: 读取局部变量("B"), 读取局部变量("x1"), 读取局部变量("y1")
  │    │    移除技能: 读取局部变量("A"), A05Q
  │    │    SetPlayerAbilityAvailable: (读取局部变量("A")的所有者), A05R, EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A05P)
  │    ├─ 则
  │    │    设置局部变量:"x"=GetSpellTargetX()
  │    │    设置局部变量:"y"=GetSpellTargetY()
  │    │    设置局部变量:"group"=玩家指定类型单位((读取局部变量("A")的所有者), n00X)
  │    │    单位组: 选取 读取局部变量("group") 中所有单位
  │    │      ├─ 设置局部变量:"B"=选取单位()
  │    │      ├─ 添加技能: 读取局部变量("B"), A05S
  │    │      ├─ 设置技能等级: 读取局部变量("B"), A05S, 单位技能等级(读取局部变量("A"), A05P)
  │    │      └─ 命令 读取局部变量("B") → UnitOrderCarrionSwarm 到 读取局部变量("x")
  │    │    GroupClear: 读取局部变量("group")
  │    │    删除单位组 读取局部变量("group")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03Q)
  │    ├─ 则
  │    │    设置局部变量:"group"=玩家指定类型单位((读取局部变量("A")的所有者), n00X)
  │    │    单位组: 选取 读取局部变量("group") 中所有单位
  │    │      ├─ 设置局部变量:"B"=选取单位()
  │    │      ├─ 添加技能: 读取局部变量("B"), A05U
  │    │      ├─ 设置技能等级: 读取局部变量("B"), A05S, 单位技能等级(读取局部变量("A"), A03Q)
  │    │      └─ 单位发布命令(立即): 读取局部变量("B"), UnitOrderThunderClap
  │    │    GroupClear: 读取局部变量("group")
  │    │    删除单位组 读取局部变量("group")
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A05X)
       ├─ 则
       │    设置局部变量:"x1"=单位X坐标(读取局部变量("A"))
       │    设置局部变量:"y1"=单位Y坐标(读取局部变量("A"))
       │    设置局部变量:"B"=ying[单位自定义值(读取局部变量("A"))]
       │    设置局部变量:"x2"=单位X坐标(读取局部变量("B"))
       │    设置局部变量:"y2"=单位Y坐标(读取局部变量("B"))
       │    移动单位: 读取局部变量("A"), 读取局部变量("x2"), 读取局部变量("y2")
       │    移动单位: 读取局部变量("B"), 读取局部变量("x1"), 读取局部变量("y1")
       │    设置单位自定义值: 读取局部变量("A"), OperatorIntegerSubtract(单位自定义值(读取局部变量("A")), 1)
       │    如果
       │      ├─ 条件: 单位自定义值(读取局部变量("A")) == 0
       │      ├─ 则
       │      │    移除技能: 读取局部变量("A"), A05X
       │      │    SetPlayerAbilityAvailable: (读取局部变量("A")的所有者), A05V, EnableDisableEnable
       │      └─ 否则: (无)
       │    返回
       └─ 否则: (无)
```

### 刺客技能

```text
触发器: 刺客技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### 刺客技能隐匿

```text
触发器: 刺客技能隐匿 (玩家/英雄) [✓] — 由于类似于隐身术这样的技能

在单位进行攻击时会优先移除魔法效果

所以这边为了防止因为魔法效果丢失造成的bug

使用自定义值记录是否可以触发隐藏效果

——by.萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A05J)
  └─ 技能目标单位() == GetSpellAbilityUnit()
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"a"=GetSpellAbilityUnit()
  ├─ 设置单位自定义值: 读取局部变量("a"), 1
  └─ 启动计时器: 创建计时器(), 60.00s (一次性)
```

### 刺客技能 心眼

```text
触发器: 刺客技能 心眼 (玩家/英雄) [✓] — 根据技能等级计算出概率和伤害倍率

很简单的算法

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ (伤害来源()类型ID) == E003
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"assassin"=伤害来源()
  ├─ 设置局部变量:"d"=触发单位()
  ├─ 设置局部变量:"random"=随机实数(0, 100.00)
  ├─ 设置局部变量:"a"=OperatorRealMultiply((单位技能等级(读取局部变量("assassin"), A05K)转实数), 10.00)
  ├─ 如果
  │    ├─ 条件: 单位有魔法效果(读取局部变量("d"), BEsh) == TRUE
  │    ├─ 则
  │    │    设置局部变量:"a"=OperatorRealMultiply(读取局部变量("a"), 2.00)
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 单位自定义值(读取局部变量("assassin")) == 1
  │    ├─ 则
  │    │    设置局部变量:"a"=100.00
  │    │    设置单位自定义值: 读取局部变量("assassin"), 0
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 读取局部变量("a") OperatorGreaterEq 读取局部变量("random")
       ├─ 则
       │    YDWESetEventDamage: (伤害值() x OperatorRealAdd((单位技能等级(读取局部变量("assassin"), A05K)转实数), 1.00))
       │    设置局部变量:"text"=(实数转整数(伤害值())转字符串)
       │    CreateTextTagUnitBJ: 读取局部变量("text") + "锛?", 读取局部变量("d"), 0, 10, 100, 0.00, 0.00, 0
       │    设置局部变量:"showtext"=bj_lastCreatedTextTag
       │    YDWETimerDestroyTextTag: 2, 读取局部变量("showtext")
       │    SetTextTagVelocityBJ: 读取局部变量("showtext"), 64, 90
       │    SetTextTagFadepointBJ: 读取局部变量("showtext"), 1.00
       └─ 否则: (无)
```

### 刺客技能-暗影突袭

```text
触发器: 刺客技能-暗影突袭 (玩家/英雄) [✓] — 这个触发展示了新建单位组的使用方法

先创建单位组再添加单位的方法

可以有效避免单位组泄露

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A05L)
  └─ (GetSpellAbilityUnit()类型ID) == E003
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"A"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"x1"=单位X坐标(GetSpellAbilityUnit())
  ├─ 设置局部变量:"y1"=单位Y坐标(GetSpellAbilityUnit())
  ├─ 设置局部变量:"x2"=GetSpellTargetX()
  ├─ 设置局部变量:"y2"=GetSpellTargetY()
  ├─ 设置局部变量:"group"=CreateGroup()
  ├─ GroupEnumUnitsInRange: 读取局部变量("group"), 读取局部变量("x2"), 读取局部变量("y2"), 200.00, (布尔比较(单位类型判断(过滤单位(), 建筑), OperatorEqualENE, false) 且 (布尔比较(是敌方单位(过滤单位(), (读取局部变量("A")的所有者)), OperatorEqualENE, true) 且 布尔比较(单位存活判断(过滤单位()), OperatorEqualENE, true)))
  └─ 单位组: 选取 读取局部变量("group") 中所有单位
       ├─ 设置局部变量:"B"=选取单位()
       ├─ 设置局部变量:"mj"=创建单位(指定坐标)((读取局部变量("A")的所有者), n00P, 读取局部变量("x1"), 读取局部变量("y1"), 0)
       ├─ 添加技能: 读取局部变量("mj"), A05M
       ├─ 设置技能等级: 读取局部变量("mj"), A05M, 单位技能等级(读取局部变量("A"), A05L)
       ├─ 单位发布命令(目标): 读取局部变量("mj"), UnitOrderShadowStrike, 读取局部变量("B")
       └─ 启动计时器: 创建计时器(), 16.00s (一次性)
```

### 刺客技能技艺·闪

```text
触发器: 刺客技能技艺·闪 (玩家/英雄) [✓] — 这部分涉及到单位组的灵活使用

这个触发的原理是

选取单位做动作后将单位移除单位组

有必要说明这个技能和无影拳不是同一个原理

虽然利用这个原理也可以做出无影拳的效果

请注意甄别

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellCast
条件
  └─ 技能ID比较(施法技能ID(), OperatorEqualENE, A05I)
动作
  └─ 启动计时器: 创建计时器(), 0.02s (循环)
```

### 圣弓技能

```text
触发器: 圣弓技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shenfa

```text
触发器: shenfa (玩家/英雄) [✓] — 这边是基本的马甲操作触发

由于没有模型的单位使用无目标技能会让特效丢失

所以需要额外创建特效在马甲单位所在地点

另外，有必要说明

释放技能尽可能不要使用创建点

即使你认真排泄

点还是会出现部分泄露情况

最好的方式是使用坐标

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"mj"=n003
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"sfd"=技能目标点()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 启动计时器: 创建计时器(), 1.00s (一次性)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A01K)
  │    ├─ 则
  │    │    AddSpecialEffectLocBJ: 读取局部变量("sfd"), Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl
  │    │    设置局部变量:"tx"=bj_lastCreatedEffect
  │    │    创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  │    │    设置局部变量:"mjdw"=bj_lastCreatedUnit
  │    │    添加技能: 读取局部变量("mjdw"), A01L
  │    │    设置技能等级: 读取局部变量("mjdw"), A01L, 单位技能等级(读取局部变量("sfz"), A01K)
  │    │    单位发布命令(立即): 读取局部变量("mjdw"), UnitOrderStomp
  │    │    启动计时器: 创建计时器(), 1.00s (一次性)
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A01H)
  │    ├─ 则
  │    │    AddSpecialEffectLocBJ: 读取局部变量("sfd"), Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl
  │    │    设置局部变量:"tx"=bj_lastCreatedEffect
  │    │    创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  │    │    设置局部变量:"mjdw"=bj_lastCreatedUnit
  │    │    添加技能: 读取局部变量("mjdw"), A01M
  │    │    设置技能等级: 读取局部变量("mjdw"), A01M, 单位技能等级(读取局部变量("sfz"), A01H)
  │    │    单位发布命令(立即): 读取局部变量("mjdw"), UnitOrderStomp
  │    │    启动计时器: 创建计时器(), 1.00s (一次性)
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A01G)
  │    ├─ 则
  │    │    AddSpecialEffectLocBJ: 读取局部变量("sfd"), Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl
  │    │    设置局部变量:"tx"=bj_lastCreatedEffect
  │    │    创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  │    │    设置局部变量:"mjdw"=bj_lastCreatedUnit
  │    │    添加技能: 读取局部变量("mjdw"), A01N
  │    │    设置技能等级: 读取局部变量("mjdw"), A01N, 单位技能等级(读取局部变量("sfz"), A01G)
  │    │    单位发布命令(立即): 读取局部变量("mjdw"), UnitOrderStomp
  │    │    启动计时器: 创建计时器(), 1.00s (一次性)
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A01I)
       ├─ 则
       │    AddSpecialEffectLocBJ: 读取局部变量("sfd"), Abilities\Spells\Human\MarkOfChaos\MarkOfChaosTarget.mdl
       │    设置局部变量:"tx"=bj_lastCreatedEffect
       │    创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
       │    设置局部变量:"mjdw"=bj_lastCreatedUnit
       │    添加技能: 读取局部变量("mjdw"), A01J
       │    设置技能等级: 读取局部变量("mjdw"), A01J, 单位技能等级(读取局部变量("sfz"), A01I)
       │    单位发布命令(立即): 读取局部变量("mjdw"), UnitOrderStomp
       │    启动计时器: 创建计时器(), 1.00s (一次性)
       └─ 否则: (无)
```

### 神官技能

```text
触发器: 神官技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### shenguanqh

```text
触发器: shenguanqh (玩家/英雄) [✓] — 这部分是利用捕捉伤害类型做动作

可以实现读取部分反击类技能做动作

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ (伤害来源()类型ID) == E000
  ├─ 单位持有物品类型(伤害来源(), I00V) == TRUE
  └─ YDWEIsEventDamageType(DamageTypeMagic) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"mj"=n00T
  ├─ 设置局部变量:"sfz"=伤害来源()
  ├─ 设置局部变量:"sfmb"=触发单位()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"sfd"=(读取局部变量("sfmb")的位置)
  ├─ 创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  ├─ 设置局部变量:"mjdw"=bj_lastCreatedUnit
  ├─ 添加技能: 读取局部变量("mjdw"), A01J
  ├─ 单位发布命令(立即): 读取局部变量("mjdw"), UnitOrderStomp
  └─ 启动计时器: 创建计时器(), 1.00s (一次性)
```

### shenguanhuyou

```text
触发器: shenguanhuyou (玩家/英雄) [✓] — 这部分是所谓工资装获得收益的做法

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ (触发单位()的所有者) == Player00
  ├─ (触发单位()的所有者) == 玩家1(红)
  ├─ (触发单位()的所有者) == 玩家2(蓝)
  ├─ (触发单位()的所有者) == 玩家3(青)
  ├─ (触发单位()的所有者) == 玩家4(紫)
  └─ (触发单位()的所有者) == 玩家5(黄)
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  └─ YDWEEnumUnitsInRangeMultiple: 点X坐标((触发单位()的位置)), 点Y坐标((触发单位()的位置)), 1000.00
```

### 赶尸人技能

```text
触发器: 赶尸人技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### ganshirenqh

```text
触发器: ganshirenqh (玩家/英雄) [✓] — 将技能图标的坐标设置成0,-11

可以实现将技能图标隐藏

目前已知这种隐藏图标方案有效

其他坐标会导致游戏崩溃

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00V)
  └─ (GetManipulatingUnit()类型ID) == H005
动作
  ├─ 移除技能: GetManipulatingUnit(), A00Z
  ├─ 添加技能: GetManipulatingUnit(), A04M
  └─ 添加技能: GetManipulatingUnit(), A04A
```

### 矿人技能

```text
触发器: 矿人技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### tujinglingluo

```text
触发器: tujinglingluo (玩家/英雄) [✓] — 利用类似于地狱火这样的技能

可以让召唤物变成马甲

从而达到范围伤害眩晕并进行其他操作

同时也可以实现纯物编模拟陨石

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSummoned
条件
  ├─ (GetSummonedUnit()类型ID) == n003
  ├─ (GetSummoningUnit()类型ID) == H003
  └─ 单位持有物品类型(GetSummoningUnit(), I00V) == TRUE
动作
  ├─ 添加技能: GetSummonedUnit(), A03C
  └─ 单位发布命令(立即): GetSummonedUnit(), UnitOrderThunderClap
```

### 半蜥人技能

```text
触发器: 半蜥人技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### longyan

```text
触发器: longyan (玩家/英雄) [✓] — 部分技能没有图标同时也不会有特效产出

所以需要用球体技能绑定特效并赋予单位

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ 技能ID比较(学习的技能(), OperatorEqualENE, A03X)
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 添加技能: GetLearningUnit(), A03W
  └─ 添加技能: GetLearningUnit(), A03V
```

### 法师技能

```text
触发器: 法师技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### lieyanchongji

```text
触发器: lieyanchongji (玩家/英雄) [✓] — 这部分触发是关联技能的触发

可以利用敌对马甲释放0.01伤害的技能

通过读取伤害来进行技能关联的操作

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(单位组第一个单位(玩家指定类型单位((触发单位()的所有者), H009)), I00V) == TRUE
  ├─ 任一成立
  ├─ (伤害来源()的所有者) == PlayerNA
  ├─ YDWEIsEventAttackType(AttackTypeNormal) == TRUE
  └─ YDWEIsEventDamageType(DamageTypeSonic) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"shly"=(伤害来源()类型ID)
  ├─ 设置局部变量:"mj1"=n003
  ├─ 设置局部变量:"mj2"=n00J
  ├─ 设置局部变量:"sr"=触发单位()
  ├─ 设置局部变量:"xj"=A02X
  ├─ 设置局部变量:"hx"=A02Y
  ├─ 设置局部变量:"hl"=A035
  ├─ 设置局部变量:"tx"=A036
  ├─ 设置局部变量:"wz"=(读取局部变量("sr")的位置)
  ├─ 设置局部变量:"zr"=(读取局部变量("sr")的所有者)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("shly") == 读取局部变量("mj1")
  │    ├─ 则
  │    │    移除技能: 读取局部变量("sr"), 读取局部变量("hx")
  │    │    移除技能: 读取局部变量("sr"), 读取局部变量("hl")
  │    │    移除技能: 读取局部变量("sr"), 读取局部变量("tx")
  │    │    添加技能: 读取局部变量("sr"), 读取局部变量("xj")
  │    │    设置技能等级: 读取局部变量("sr"), 读取局部变量("xj"), huo
  │    │    清除点 读取局部变量("wz")
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 读取局部变量("shly") == 读取局部变量("mj2")
       ├─ 则
       │    移除技能: 读取局部变量("sr"), 读取局部变量("xj")
       │    添加技能: 读取局部变量("sr"), 读取局部变量("hx")
       │    设置技能等级: 读取局部变量("sr"), 读取局部变量("hx"), shui
       │    添加技能: 读取局部变量("sr"), 读取局部变量("hl")
       │    设置技能等级: 读取局部变量("sr"), 读取局部变量("hl"), shui
       │    添加技能: 读取局部变量("sr"), 读取局部变量("tx")
       └─ 否则: (无)
```

### zddj

```text
触发器: zddj (玩家/英雄) [✓] — 物品自动叠加

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=触发单位()
  ├─ 设置局部变量:"bcz"=被操作物品()
  ├─ 设置局部变量:"ys1"=I00C
  ├─ 设置局部变量:"ys2"=I00D
  ├─ 设置局部变量:"ys3"=I00E
  └─ 如果
       ├─ 条件: 任一成立
       ├─ 则
       │    循环整数A 0→5
       │      └─ 如果
       │           ├─ 条件: 全部成立
       │           │    ├─ 物品比较(读取局部变量("bcz"), OperatorNotEqualENE, UnitItemInSlot(读取局部变量("sfz"), 循环整数A))
       │           │    ├─ 物品类型比较(物品类型ID(UnitItemInSlot(读取局部变量("sfz"), 循环整数A())), OperatorEqualENE, 物品类型ID(读取局部变量("bcz")))
       │           ├─ 则
       │           │    SetItemCharges: UnitItemInSlot(读取局部变量("sfz"), 循环整数A), OperatorIntegerAdd(物品剩余使用次数(读取局部变量("bcz")), 物品剩余使用次数(UnitItemInSlot(读取局部变量("sfz"), 循环整数A)))
       │           │    删除物品: 读取局部变量("bcz")
       │           └─ 否则: (无)
       └─ 否则: (无)
```

### jiechufuzhou

```text
触发器: jiechufuzhou (玩家/英雄) [✓] — 法师的技能原理

通过禁用再允许的方式可以实现多面板技能

即用技能后切换面板上的技能

通过禁用再添加的方式则不能记录模拟的第二目录的技能cd

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A02G)
  └─ (GetSpellAbilityUnit()类型ID) == H009
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"sfjn"=施法技能ID()
  ├─ 设置局部变量:"huo"=A026
  ├─ 设置局部变量:"shui"=A028
  ├─ 设置局部变量:"feng"=A027
  ├─ 设置局部变量:"tu"=A029
  ├─ 设置局部变量:"f"=A02G
  ├─ 设置局部变量:"tuq"=A034
  ├─ 设置局部变量:"tuw"=A02E
  ├─ 设置局部变量:"tue"=A03B
  ├─ 设置局部变量:"tur"=A03F
  ├─ 设置局部变量:"huoq1"=A02R
  ├─ 设置局部变量:"huoq2"=A02S
  ├─ 设置局部变量:"huoq3"=A02T
  ├─ 设置局部变量:"huow"=A02P
  ├─ 设置局部变量:"huoe"=A02I
  ├─ 设置局部变量:"huor"=A02B
  ├─ 设置局部变量:"fengq"=A039
  ├─ 设置局部变量:"fengw"=A02F
  ├─ 设置局部变量:"fenge"=A037
  ├─ 设置局部变量:"fengr"=A02L
  ├─ 设置局部变量:"shuiq"=A030
  ├─ 设置局部变量:"shuiw"=A003
  ├─ 设置局部变量:"shuie"=A02H
  ├─ 设置局部变量:"shuir"=A022
  ├─ UnitRemoveBuffs: 读取局部变量("sfz"), InclusionExclude, InclusionInclude
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huow")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huoe")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("huor")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("shuie")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("shuir")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("fengq")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("fengw")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("fenge")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("fengr")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("tuq")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("tuw")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("tue")
  ├─ 移除技能: 读取局部变量("sfz"), 读取局部变量("tur")
  ├─ SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  ├─ SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  ├─ SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  └─ SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
```

### huo

```text
触发器: huo (玩家/英雄) [✓] — 末日审判这样的技能

如果单个技能设置等级就会出现

技能第二级无法使用的情况

所以需要单独制作各个等级的马甲技能模拟

末日审判的召唤物同样可以是马甲

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == H009
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"sfdw"=技能目标单位()
  ├─ 设置局部变量:"sfd"=技能目标点()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"dd"=PlayerNA
  ├─ 设置局部变量:"mjdw"=n003
  ├─ 设置局部变量:"mjdw2"=n00J
  ├─ 设置局部变量:"huowmjdw"=n00N
  ├─ 设置局部变量:"sfjn"=施法技能ID()
  ├─ 设置局部变量:"huo"=A026
  ├─ 设置局部变量:"shui"=A028
  ├─ 设置局部变量:"feng"=A027
  ├─ 设置局部变量:"tu"=A029
  ├─ 设置局部变量:"f"=A02G
  ├─ 设置局部变量:"huoq1"=A02R
  ├─ 设置局部变量:"huoq1mj"=A02U
  ├─ 设置局部变量:"huoq2"=A02S
  ├─ 设置局部变量:"huoq2mj"=A02V
  ├─ 设置局部变量:"huoq3"=A02T
  ├─ 设置局部变量:"huoq3mj"=A02W
  ├─ 设置局部变量:"huow"=A02P
  ├─ 设置局部变量:"huowmj"=A02Q
  ├─ 设置局部变量:"huoe"=A02I
  ├─ 设置局部变量:"huoemj"=A02K
  ├─ 设置局部变量:"huoemjd"=A02J
  ├─ 设置局部变量:"huor"=A02B
  ├─ 设置局部变量:"huormj"=A02A
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("huo"))
  │    ├─ 则
  │    │    设置 huo = 单位技能等级(读取局部变量("sfz"), 读取局部变量("huo"))
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableDisable
  │    │    如果
  │    │      ├─ 条件: huo == 1
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: huo == 2
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: huo == 3
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
  │    │      └─ 否则: (无)
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("huow")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("huow"), huo
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("huoe")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("huoe"), huo
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("huor")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("huor"), huo
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 任一成立
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    如果
  │    │      ├─ 条件: huo == 1
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("mj"), 读取局部变量("huoq1mj")
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: huo == 2
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("mj"), 读取局部变量("huoq2mj")
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: huo == 3
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("mj"), 读取局部变量("huoq3mj")
  │    │      └─ 否则: (无)
  │    │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderDoom, 读取局部变量("sfdw")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huow")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoe")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huor")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("huow"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("huowmjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("huowmj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("huowmj"), huo
  │    │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderUnstableConcoction, 读取局部变量("sfdw")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huow")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoe")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huor")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("huoe"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("dd") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj2"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj2"), 读取局部变量("huoemjd")
  │    │    设置技能等级: 读取局部变量("mj2"), 读取局部变量("huoemjd"), huo
  │    │    命令 读取局部变量("mj2") → UnitOrderBreathOfFire 到 点X坐标(读取局部变量("sfd"))
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("huoemj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("huoemj"), huo
  │    │    命令 读取局部变量("mj") → UnitOrderBreathOfFire 到 点X坐标(读取局部变量("sfd"))
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huow")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoe")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("huor")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("huor"))
       ├─ 则
       │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
       │    设置局部变量:"mj"=最后创建的单位()
       │    添加技能: 读取局部变量("mj"), 读取局部变量("huormj")
       │    命令 读取局部变量("mj") → UnitOrderRainOfFire 到 读取局部变量("sfd")
       │    启动计时器: 创建计时器(), 20.00s (一次性)
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq1")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq2")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoq3")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huow")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huoe")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("huor")
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
       │    返回
       └─ 否则: (无)
```

### huoqh

```text
触发器: huoqh (玩家/英雄) [✓] — 同样的单位组的灵活运用

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(单位组第一个单位(玩家指定类型单位((伤害来源()的所有者), H009)), I00V) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"mj"=n003
  ├─ 设置局部变量:"sfz"=伤害来源()
  ├─ 设置局部变量:"sfmb"=触发单位()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"sfd"=(读取局部变量("sfmb")的位置)
  ├─ 创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  ├─ 设置局部变量:"mjdw"=bj_lastCreatedUnit
  ├─ 添加技能: 读取局部变量("mjdw"), A047
  ├─ 命令 读取局部变量("mjdw") → UnitOrderFlameStrike 到 读取局部变量("sfd")
  └─ 启动计时器: 创建计时器(), 10.00s (一次性)
```

### shui

```text
触发器: shui (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == H009
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"sfdw"=技能目标单位()
  ├─ 设置局部变量:"sfd"=技能目标点()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"dd"=PlayerNA
  ├─ 设置局部变量:"mjdw"=n003
  ├─ 设置局部变量:"mjdw2"=n00J
  ├─ 设置局部变量:"shuiqmjdw"=n00O
  ├─ 设置局部变量:"sfjn"=施法技能ID()
  ├─ 设置局部变量:"huo"=A026
  ├─ 设置局部变量:"shui"=A028
  ├─ 设置局部变量:"feng"=A027
  ├─ 设置局部变量:"tu"=A029
  ├─ 设置局部变量:"f"=A02G
  ├─ 设置局部变量:"shuiq"=A030
  ├─ 设置局部变量:"shuiqmj"=A031
  ├─ 设置局部变量:"shuiw"=A003
  ├─ 设置局部变量:"shuie"=A02H
  ├─ 设置局部变量:"shuiemj"=A02N
  ├─ 设置局部变量:"shuiemjd"=A02O
  ├─ 设置局部变量:"shuir"=A022
  ├─ 设置局部变量:"shuirmj"=A023
  ├─ 设置局部变量:"ys1"=I00C
  ├─ 设置局部变量:"ys2"=I00D
  ├─ 设置局部变量:"ys3"=I00E
  ├─ 设置局部变量:"str"=I00F
  ├─ 设置局部变量:"agi"=I00G
  ├─ 设置局部变量:"int"=I00H
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("shui"))
  │    ├─ 则
  │    │    设置 shui = 单位技能等级(读取局部变量("sfz"), 读取局部变量("shui"))
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableDisable
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("shuiq"), shui
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("shuiw"), shui
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("shuie")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("shuie"), shui
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("shuir")
  │    │    设置技能等级: 读取局部变量("sfz"), 读取局部变量("shuir"), shui
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("shuiq"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("shuiqmjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("shuiqmj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("shuiqmj"), shui
  │    │    命令 读取局部变量("mj") → UnitOrderHealingSpray 到 读取局部变量("sfd")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuie")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuir")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("shuiw"))
  │    ├─ 则
  │    │    设置局部变量:"sjz"=随机实数(0.00, 100.00)
  │    │    设置局部变量:"sjsx"=随机[1~3]
  │    │    如果
  │    │      ├─ 条件: shui == 1
  │    │      ├─ 则
  │    │      │    创建物品: 读取局部变量("ys1"), 读取局部变量("sfzd")
  │    │      │    如果
  │    │      │      ├─ 条件: 读取局部变量("sjz") OperatorLessEq 1.00
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 1
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("str"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 2
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("agi"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 3
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("int"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: shui == 2
  │    │      ├─ 则
  │    │      │    创建物品: 读取局部变量("ys2"), 读取局部变量("sfzd")
  │    │      │    如果
  │    │      │      ├─ 条件: 读取局部变量("sjz") OperatorLessEq 1.00
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 1
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("str"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 2
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("agi"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 3
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("int"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    如果
  │    │      ├─ 条件: shui == 3
  │    │      ├─ 则
  │    │      │    创建物品: 读取局部变量("ys3"), 读取局部变量("sfzd")
  │    │      │    如果
  │    │      │      ├─ 条件: 读取局部变量("sjz") OperatorLessEq 1.00
  │    │      │      ├─ 则
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 1
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("str"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 2
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("agi"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      │    如果
  │    │      │      │      ├─ 条件: 读取局部变量("sjsx") == 3
  │    │      │      │      ├─ 则
  │    │      │      │      │    创建物品: 读取局部变量("int"), 读取局部变量("sfzd")
  │    │      │      │      └─ 否则: (无)
  │    │      │      └─ 否则: (无)
  │    │      └─ 否则: (无)
  │    │    清除点 读取局部变量("sfd")
  │    │    清除点 读取局部变量("sfzd")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuie")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuir")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("shuie"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw2")|→读取局部变量("dd") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj2"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj2"), 读取局部变量("shuiemjd")
  │    │    设置技能等级: 读取局部变量("mj2"), 读取局部变量("shuiemjd"), shui
  │    │    命令 读取局部变量("mj2") → UnitOrderCarrionSwarm 到 读取局部变量("sfd")
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("shuiemj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("shuiemj"), shui
  │    │    命令 读取局部变量("mj") → UnitOrderCarrionSwarm 到 读取局部变量("sfd")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuie")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuir")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("shuir"))
       ├─ 则
       │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
       │    设置局部变量:"mj"=最后创建的单位()
       │    添加技能: 读取局部变量("mj"), 读取局部变量("shuirmj")
       │    设置技能等级: 读取局部变量("mj"), 读取局部变量("shuirmj"), shui
       │    命令 读取局部变量("mj") → UnitOrderBlizzard 到 读取局部变量("sfd")
       │    启动计时器: 创建计时器(), 20.00s (一次性)
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiq")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuiw")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuie")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("shuir")
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
       │    返回
       └─ 否则: (无)
```

### feng

```text
触发器: feng (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == H009
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"sfdw"=技能目标单位()
  ├─ 设置局部变量:"sfd"=技能目标点()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"dd"=PlayerNA
  ├─ 设置局部变量:"mjdw"=n003
  ├─ 设置局部变量:"mjdw2"=n00P
  ├─ 设置局部变量:"shuiqmjdw"=n00O
  ├─ 设置局部变量:"sfjn"=施法技能ID()
  ├─ 设置局部变量:"huo"=A026
  ├─ 设置局部变量:"shui"=A028
  ├─ 设置局部变量:"feng"=A027
  ├─ 设置局部变量:"tu"=A029
  ├─ 设置局部变量:"f"=A02G
  ├─ 设置局部变量:"fengq"=A039
  ├─ 设置局部变量:"fengqmj"=A03A
  ├─ 设置局部变量:"fengw"=A02F
  ├─ 设置局部变量:"fengwmj"=A02C
  ├─ 设置局部变量:"fenge"=A037
  ├─ 设置局部变量:"fengemj"=A038
  ├─ 设置局部变量:"fengr"=A02L
  ├─ 设置局部变量:"fengrmj"=A02M
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("feng"))
  │    ├─ 则
  │    │    设置 feng = 单位技能等级(读取局部变量("sfz"), 读取局部变量("feng"))
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableDisable
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("fengq")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("fengw")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("fenge")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("fengr")
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("fengq"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw2")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("fengqmj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("fengqmj"), feng
  │    │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderForkedLightning, 读取局部变量("sfdw")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fenge")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengr")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("fengw"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("fengwmj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("fengwmj"), feng
  │    │    命令 读取局部变量("mj") → UnitOrderMonsoon 到 读取局部变量("sfd")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fenge")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengr")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("fenge"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("fengemj")
  │    │    设置技能等级: 读取局部变量("mj"), 读取局部变量("fengemj"), feng
  │    │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderCyclone, 读取局部变量("sfdw")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fenge")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengr")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    │    返回
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("fengr"))
       ├─ 则
       │    CreateDestructableLoc: LTlt, 区域内随机点(RectFromCenterSizeBJ(读取局部变量("sfd"), 150.00, 150.00)), GetRandomDirectionDeg(), 1, 0
       │    设置局部变量:"s1"=bj_lastCreatedDestructable
       │    CreateDestructableLoc: LTlt, 区域内随机点(RectFromCenterSizeBJ(读取局部变量("sfd"), 150.00, 150.00)), GetRandomDirectionDeg(), 1, 0
       │    设置局部变量:"s2"=bj_lastCreatedDestructable
       │    启动计时器: 创建计时器(), 2.00s (一次性)
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengq")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengw")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("fenge")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("fengr")
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
       │    返回
       └─ 否则: (无)
```

### fengqh

```text
触发器: fengqh (玩家/英雄) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(单位组第一个单位(玩家指定类型单位((伤害来源()的所有者), H009)), I00V) == TRUE
  ├─ (伤害来源()类型ID) == n00P
  └─ YDWEIsEventDamageType(DamageTypeLightning) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"mj"=n00S
  ├─ 设置局部变量:"sfz"=伤害来源()
  ├─ 设置局部变量:"sfmb"=触发单位()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"sfd"=(读取局部变量("sfmb")的位置)
  ├─ 创建 1个|读取局部变量("mj")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  ├─ 设置局部变量:"mjdw"=bj_lastCreatedUnit
  ├─ 添加技能: 读取局部变量("mjdw"), A049
  ├─ 设置技能等级: 读取局部变量("mjdw"), A049, feng
  ├─ 单位发布命令(目标): 读取局部变量("mjdw"), UnitOrderChainLightning, 读取局部变量("sfmb")
  └─ 启动计时器: 创建计时器(), 10.00s (一次性)
```

### tu

```text
触发器: tu (玩家/英雄) [✓] — 口袋工厂和工厂技能

既可以模拟自动出兵

同样也可以模拟召唤传送门

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == H009
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetSpellAbilityUnit()
  ├─ 设置局部变量:"sfdw"=技能目标单位()
  ├─ 设置局部变量:"sfd"=技能目标点()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"dd"=PlayerNA
  ├─ 设置局部变量:"mjdw"=n003
  ├─ 设置局部变量:"sfjn"=施法技能ID()
  ├─ 设置局部变量:"huo"=A026
  ├─ 设置局部变量:"shui"=A028
  ├─ 设置局部变量:"feng"=A027
  ├─ 设置局部变量:"tu"=A029
  ├─ 设置局部变量:"f"=A02G
  ├─ 设置局部变量:"tuq"=A034
  ├─ 设置局部变量:"tuqmj"=A03E
  ├─ 设置局部变量:"tuw"=A02E
  ├─ 设置局部变量:"tuwmj"=A02D
  ├─ 设置局部变量:"tuwmjqh"=A048
  ├─ 设置局部变量:"tue"=A03B
  ├─ 设置局部变量:"tuemj"=A03C
  ├─ 设置局部变量:"tur"=A03F
  ├─ 设置局部变量:"turmj"=A03G
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("tu"))
  │    ├─ 则
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableDisable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableDisable
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("tuq")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("tuw")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("tue")
  │    │    添加技能: 读取局部变量("sfz"), 读取局部变量("tur")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("tuq"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    添加技能: 读取局部变量("mj"), 读取局部变量("tuqmj")
  │    │    命令 读取局部变量("mj") → UnitOrderSummonFactory 到 读取局部变量("sfd")
  │    │    启动计时器: 创建计时器(), 20.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tue")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tur")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("tuw"))
  │    ├─ 则
  │    │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
  │    │    设置局部变量:"mj"=最后创建的单位()
  │    │    如果
  │    │      ├─ 条件: 单位持有物品类型(读取局部变量("sfz"), I00V) == TRUE
  │    │      ├─ 则
  │    │      │    添加技能: 读取局部变量("mj"), 读取局部变量("tuwmjqh")
  │    │      └─ 否则
  │    │           添加技能: 读取局部变量("mj"), 读取局部变量("tuwmj")
  │    │    单位发布命令(立即): 读取局部变量("mj"), UnitOrderStarfall2
  │    │    启动计时器: 创建计时器(), 35.00s (一次性)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tue")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tur")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("tue"))
  │    ├─ 则
  │    │    设置局部变量:"sj"=0.00
  │    │    设置局部变量:"bd"=1.00
  │    │    AddSpecialEffectLocBJ: 读取局部变量("sfzd"), Abilities\Weapons\FarseerMissile\FarseerMissile.mdl
  │    │    设置局部变量:"sdq"=bj_lastCreatedEffect
  │    │    EXSetEffectSize: 读取局部变量("sdq"), 读取局部变量("bd")
  │    │    EXSetEffectZ: 读取局部变量("sdq"), OperatorRealAdd(EXGetEffectZ(读取局部变量("sdq")), 100.00)
  │    │    启动计时器: 创建计时器(), 0.10s (循环)
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuq")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuw")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tue")
  │    │    移除技能: 读取局部变量("sfz"), 读取局部变量("tur")
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
  │    │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 技能ID比较(读取局部变量("sfjn"), OperatorEqualENE, 读取局部变量("tur"))
       ├─ 则
       │    AddSpecialEffectLocBJ: 读取局部变量("sfd"), Abilities\Spells\Human\Resurrect\ResurrectCaster.mdl
       │    设置局部变量:"tx"=bj_lastCreatedEffect
       │    启动计时器: 创建计时器(), 5.00s (一次性)
       │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfd") 面向默认朝向
       │    设置局部变量:"mj"=最后创建的单位()
       │    添加技能: 读取局部变量("mj"), 读取局部变量("turmj")
       │    单位发布命令(立即): 读取局部变量("mj"), UnitOrderVoodoo
       │    启动计时器: 创建计时器(), 35.00s (一次性)
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("f")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuq")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("tuw")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("tue")
       │    移除技能: 读取局部变量("sfz"), 读取局部变量("tur")
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("huo"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("shui"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("feng"), EnableDisableEnable
       │    SetPlayerAbilityAvailable: 读取局部变量("wj"), 读取局部变量("tu"), EnableDisableEnable
       └─ 否则: (无)
```

### 猎人技能

```text
触发器: 猎人技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### miaozhun

```text
触发器: miaozhun (玩家/英雄) [✓] — 利用科技等级绑定技能等级

可以实现射程的增长等等

技能项目中没有但是科技项目中有的增益效果

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ OperatorCompareHeroSkill(GetLearnedSkillBJ(), OperatorEqualENE, A01Y)
动作
  └─ 升级玩家科技: (触发单位()的所有者), R000, 1
```

### 战士技能

```text
触发器: 战士技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### zhanshigongji

```text
触发器: zhanshigongji (玩家/英雄) [✓] — 这部分是用来限制英雄某些和属性点挂钩的设置

大部分属性可以通过游戏平衡常数调整

特殊的英雄则需要使用特殊的方式

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Level
条件
  └─ (GetLevelingUnit()类型ID) == H000
动作
  ├─ 关闭触发器 当前触发器()
  ├─ SetUnitState: 触发单位(), UnitStateDamageBaseSec, OperatorRealSubtract(单位状态(GetLevelingUnit(), UnitStateDamageBase), 5.00)
  └─ 开启触发器 当前触发器()
```

### zhanshi

```text
触发器: zhanshi (玩家/英雄) [✓] — 此触发器初始处于休眠状态

需要通过其他触发器开启

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位类型判断(触发单位(), 建筑) == TRUE
  ├─ (伤害来源()类型ID) == H000
  └─ YDWEIsEventAttackType(AttackTypeHero) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=伤害来源()
  ├─ 设置局部变量:"mjdw"=n003
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"fn"=A03H
  ├─ 设置局部变量:"fnmj"=A03J
  └─ 如果
       ├─ 条件: 单位技能等级(读取局部变量("sfz"), 读取局部变量("fn")) OperatorGreaterEq 1
       ├─ 则
       │    设置局部变量:"dj"=单位技能等级(读取局部变量("sfz"), 读取局部变量("fn"))
       │    设置局部变量:"sj"=随机[1~10]
       │    如果
       │      ├─ 条件: 读取局部变量("sj") OperatorLessEq 读取局部变量("dj")
       │      ├─ 则
       │      │    设置 fn = 2
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: fn == 2
       │      ├─ 则
       │      │    创建 1个|读取局部变量("mjdw")|→读取局部变量("wj") 在 读取局部变量("sfzd") 面向默认朝向
       │      │    设置局部变量:"mj"=bj_lastCreatedUnit
       │      │    添加技能: 读取局部变量("mj"), 读取局部变量("fnmj")
       │      │    设置技能等级: 读取局部变量("mj"), 读取局部变量("fnmj"), 单位技能等级(读取局部变量("sfz"), 读取局部变量("fn"))
       │      │    单位发布命令(立即): 读取局部变量("mj"), UnitOrderStomp
       │      │    AddSpecialEffectLocBJ: 读取局部变量("sfzd"), Abilities\Spells\Orc\WarStomp\WarStompCaster.mdl
       │      │    设置局部变量:"tx"=bj_lastCreatedEffect
       │      │    启动计时器: 创建计时器(), 2.00s (一次性)
       │      │    设置 fn = 0
       │      └─ 否则
       │           设置 fn = OperatorIntegerAdd(fn, 1)
       └─ 否则: (无)
```

### zhanshixuexi

```text
触发器: zhanshixuexi (玩家/英雄) [✓] — 用于判断条件开启休眠的触发器

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ (GetLearningUnit()类型ID) == H000
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ GetLearnedSkillLevel() == 1
       │    ├─ 技能ID比较(学习的技能(), OperatorEqualENE, A03H)
       ├─ 则
       │    开启触发器 gg_trg_zhanshi
       └─ 否则: (无)
```

### zhanshishanbi

```text
触发器: zhanshishanbi (玩家/英雄) [✓] — 模拟单位受到攻击时几率回复生命值

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ (触发单位()类型ID) == H000
  └─ YDWEIsEventAttackDamage() == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"sjz"=随机[1~10]
  └─ 如果
       ├─ 条件: 读取局部变量("sjz") OperatorLessEq 单位技能等级(触发单位(), A00R)
       ├─ 则
       │    设置局部变量:"dq"=单位状态(触发单位(), UnitStateLife)
       │    设置局部变量:"zd"=单位状态(触发单位(), UnitStateMaxLife)
       │    设置局部变量:"hf"=OperatorRealMultiply(读取局部变量("zd"), OperatorRealMultiply((单位技能等级(触发单位(), A00R)转实数), 0.03))
       │    设置局部变量:"zf"=(实数转整数(读取局部变量("hf"))转字符串)
       │    SetUnitLifeBJ: 触发单位(), OperatorRealAdd(读取局部变量("dq"), 读取局部变量("hf"))
       │    CreateTextTagUnitBJ: "+" + 读取局部变量("zf"), 触发单位(), 0.00, 10, 0.00, 100, 0.00, 0
       │    设置局部变量:"pfwz"=GetLastCreatedTextTag()
       │    YDWETimerDestroyTextTag: 2, 读取局部变量("pfwz")
       │    SetTextTagVelocityBJ: 读取局部变量("pfwz"), 64, 90
       │    SetTextTagFadepointBJ: 读取局部变量("pfwz"), 1.00
       └─ 否则: (无)
```

### zhanshiqidong

```text
触发器: zhanshiqidong (玩家/英雄) [✓] — 这部分其实一开始我制作的是可叠加攻速

也是利用科技的特性制作的

但是后期发现存在一些以我的能力暂时无法修复的bug

所以更换成了现在的样子

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHero_Skill
条件
  └─ 技能ID比较(学习的技能(), OperatorEqualENE, A03I)
动作
  └─ 添加技能: GetLearningUnit(), A03Y
```

### 暗夜骑士技能

```text
触发器: 暗夜骑士技能 (玩家/英雄) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### anyeqishi

```text
触发器: anyeqishi (玩家/英雄) [✓] — 跳跃函数的使用

这部分是我偷懒了

但是有现成的工具为什么不用呢？

对吧？

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  └─ (GetSpellAbilityUnit()类型ID) == E001
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  └─ 如果
       ├─ 条件: 技能ID比较(施法技能ID(), OperatorEqualENE, A03R)
       ├─ 则
       │    YDWEJumpTimer: GetSpellAbilityUnit(), AngleBetweenPoints((GetSpellAbilityUnit()的位置), 技能目标点()), 两点间距((GetSpellAbilityUnit()的位置), 技能目标点()), 0.50, 0.01, 300
       └─ 否则: (无)
```

### sanags

```text
触发器: sanags (玩家/英雄) [✓] — 判断游戏时间添加增益技能

这里其实可以给光环的

不同魔法效果的相同光环可以叠加！

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  ├─ 注册游戏时间事件(LimitOpGreaterThanOrEqual, 0.00)
  └─ 注册游戏时间事件(LimitOpGreaterThanOrEqual, 18.00)
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"yx"=GetUnitsOfTypeIdAll(E001)
  ├─ 单位组: 选取 读取局部变量("yx") 中所有单位
  │    └─ 如果
  │         ├─ 条件: 单位技能等级(选取单位(), A03T) == 1
  │         ├─ 则
  │         └─ 否则
  │              添加技能: 选取单位(), A03T
  ├─ GroupClear: 读取局部变量("yx")
  ├─ 删除单位组 读取局部变量("yx")
  └─ 开启触发器 当前触发器()
```

### sanayc

```text
触发器: sanayc (玩家/英雄) [✓] — 判断游戏内时间移除加成
───────────────────────────────────────────────────────
事件
  └─ 注册游戏时间事件(LimitOpGreaterThanOrEqual, 6.00)
条件
  └─ 游戏时间(24h)() OperatorLess 18.00
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"yx"=GetUnitsOfTypeIdAll(E001)
  ├─ 单位组: 选取 读取局部变量("yx") 中所有单位
  │    └─ 移除技能: 选取单位(), A03T
  ├─ GroupClear: 读取局部变量("yx")
  ├─ 删除单位组 读取局部变量("yx")
  └─ 开启触发器 当前触发器()
```

### 当玩家位置存在电脑时默认建造

```text
触发器: 当玩家位置存在电脑时默认建造 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### computerai

```text
触发器: computerai (剧情/任务) [✓] — 限制某些情况下玩家的游戏模式

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 销毁触发器(自身)
  ├─ SetPlayerTeam: Player00, 1
  ├─ SetPlayerTeam: 玩家1(红), 1
  ├─ SetPlayerTeam: 玩家2(蓝), 1
  ├─ SetPlayerTeam: 玩家3(青), 1
  ├─ SetPlayerTeam: 玩家4(紫), 1
  └─ 启动计时器: 创建计时器(), 5.00s (一次性)
```

### 玩家超过1分钟没有选择难度默认难度1

```text
触发器: 玩家超过1分钟没有选择难度默认难度1 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### mrnd

```text
触发器: mrnd (剧情/任务) [✓] — 设置玩家超过时间限制没有选择难度时默认为难度1

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(60.00)
条件
  └─ nd == 0
动作
  ├─ 设置 nd = 1
  └─ 显示文本→GetPlayersAll(): YDWEOperatorString3("默认难度为难度", (nd转字符串), "，所有兽族部落不会获得额外资源")
```

### 玩家输入yzyw进入建造模式

```text
触发器: 玩家输入yzyw进入建造模式 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### p1

```text
触发器: p1 (剧情/任务) [✓] — 玩家可以开启另外一种游戏模式

这里要注意两种模式利用队伍做区分

玩家设置的联盟胜利的玩家可以在不同队伍中联盟胜利

需要注意的是不同队伍的玩家之间不能开启单位共享

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 玩家 PlayerALL 输入 "-yzyw"
条件
  └─ GetPlayerTeam(触发玩家()) == 0
动作
  ├─ 关闭触发器 当前触发器()
  ├─ SetPlayerTeam: 触发玩家(), 1
  ├─ 如果
  │    ├─ 条件: OperatorCompareRace(GetPlayerRace(触发玩家()), OperatorEqualENE, RaceHuman)
  │    ├─ 则
  │    │    MeleeStartingUnitsForPlayer: RaceHuman, 触发玩家(), GetPlayerStartLocationLoc(触发玩家()), InclusionInclude
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: OperatorCompareRace(GetPlayerRace(触发玩家()), OperatorEqualENE, RaceOrc)
  │    ├─ 则
  │    │    MeleeStartingUnitsForPlayer: RaceOrc, 触发玩家(), GetPlayerStartLocationLoc(触发玩家()), InclusionInclude
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: OperatorCompareRace(GetPlayerRace(触发玩家()), OperatorEqualENE, RaceUndead)
  │    ├─ 则
  │    │    MeleeStartingUnitsForPlayer: RaceUndead, 触发玩家(), GetPlayerStartLocationLoc(触发玩家()), InclusionInclude
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: OperatorCompareRace(GetPlayerRace(触发玩家()), OperatorEqualENE, RaceNightElf)
  │    ├─ 则
  │    │    MeleeStartingUnitsForPlayer: RaceNightElf, 触发玩家(), GetPlayerStartLocationLoc(触发玩家()), InclusionInclude
  │    └─ 否则: (无)
  ├─ 设置玩家属性: 触发玩家(), PlayerStateGold, 975
  ├─ 设置玩家属性: 触发玩家(), PlayerStateLumber, 250
  ├─ SetPlayerFlag: 触发玩家(), PlayerFlagGivesBounty, OnOffIntOn
  ├─ 平移镜头: 触发玩家(), GetPlayerStartLocationLoc(触发玩家()), 0
  └─ 开启触发器 当前触发器()
```

### 选择难度

```text
触发器: 选择难度 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### ndxz

```text
触发器: ndxz (剧情/任务) [✓] — 选择不同的难度

这里是利用整数纪录难度和不同的难度奖励

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 玩家 PlayerALL 输入 玩家聊天字符串()
条件
  └─ nd == 0
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-mx"
  │    ├─ 则
  │    │    设置 nd = -1
  │    │    SetPlayerTechResearchedSwap: R002, 2, 玩家5(黄)
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：萌新", "难度", "，人族部落会增加资源采集速度")
  │    │    显示文本→GetPlayersAll(): "TRIGSTR_1162"
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-n1"
  │    ├─ 则
  │    │    设置 nd = 1
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落不会获得额外资源采集速度")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-n2"
  │    ├─ 则
  │    │    设置 nd = 2
  │    │    设置 jl = 1
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落都会增加资源采集速度")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-n3"
  │    ├─ 则
  │    │    设置 nd = 3
  │    │    设置 jl = 2
  │    │    设置 fc = 1
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落都会增加资源采集速度，所有兽族部落英雄会获得复仇效果")
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("复仇：英雄每次死亡都会增加", (fc转字符串), "全属性")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-n4"
  │    ├─ 则
  │    │    设置 nd = 4
  │    │    设置 jl = 3
  │    │    设置 fc = 2
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落都会增加资源采集速度，所有兽族部落英雄会获得复仇效果")
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("复仇：英雄每次死亡都会增加", (fc转字符串), "全属性")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 玩家聊天字符串() == "-n5"
  │    ├─ 则
  │    │    设置 nd = 5
  │    │    设置 jl = 4
  │    │    设置 fc = 3
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落都会增加资源采集速度，所有兽族部落英雄会获得复仇效果")
  │    │    显示文本→GetPlayersAll(): YDWEOperatorString3("复仇：英雄每次死亡都会增加", (fc转字符串), "全属性")
  │    │    显示文本→GetPlayersAll(): "TRIGSTR_1094"
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 玩家聊天字符串() == "-n6"
       ├─ 则
       │    设置 nd = 6
       │    设置 jl = 5
       │    设置 fc = 4
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家6(橙)
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家7(绿)
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家8(粉)
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家9(灰)
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家10(淡蓝)
       │    SetPlayerTechResearchedSwap: R002, 1, 玩家11(暗绿)
       │    显示文本→GetPlayersAll(): YDWEOperatorString3("当前难度为：难度", (nd转字符串), "，所有兽族部落都会增加资源采集速度，所有兽族部落英雄会获得复仇效果")
       │    显示文本→GetPlayersAll(): "TRIGSTR_1150"
       │    显示文本→GetPlayersAll(): YDWEOperatorString3("复仇：英雄每次死亡都会增加", (fc转字符串), "全属性")
       │    显示文本→GetPlayersAll(): "TRIGSTR_1149"
       └─ 否则: (无)
```

### 不同难度的科技奖励

```text
触发器: 不同难度的科技奖励 (剧情/任务) [注释] [✓]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 无
动作
  └─ (无)
```

### jl

```text
触发器: jl (剧情/任务) [✓] — 不同的难度发放不同的科技奖励给npc

这里也可以制作成各种难度的其他加成

例如护甲血量之类的

常见于防守图和生存图

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 注册计时器单次事件(60.00)
条件
  └─ 无
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 显示文本→GetPlayersAll(): "TRIGSTR_627"
  ├─ 如果
  │    ├─ 条件: 任一成立
  │    ├─ 则
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家6(橙)
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家7(绿)
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家8(粉)
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家9(灰)
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家10(淡蓝)
  │    │    SetPlayerTechResearchedSwap: R003, jl, 玩家11(暗绿)
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: nd == -1
       ├─ 则
       │    显示文本→GetPlayersAll(): "TRIGSTR_1159"
       │    SetPlayerTechResearchedSwap: R003, 10, 玩家5(黄)
       └─ 否则: (无)
```

### fc

```text
触发器: fc (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ 单位类型判断(触发单位(), 英雄) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 修改 死亡单位() 的HeroStatStr: ModifyMethodAddfc
  ├─ 修改 死亡单位() 的HeroStatAgi: ModifyMethodAddfc
  ├─ 修改 死亡单位() 的HeroStatInt: ModifyMethodAddfc
  └─ 如果
       ├─ 条件: 任一成立
       ├─ 则
       │    如果
       │      ├─ 条件: 单位自定义值(死亡单位()) == 1
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 英雄等级(死亡单位()) == 10
       │      │      ├─ 则
       │      │      └─ 否则
       │      │           SetHeroLevelNT: 死亡单位(), OperatorIntegerAdd(英雄等级(死亡单位()), 1), ShowHideHide
       │      │           设置单位自定义值: 死亡单位(), 0
       │      └─ 否则
       │           设置单位自定义值: 死亡单位(), OperatorIntegerAdd(单位自定义值(死亡单位()), 1)
       └─ 否则: (无)
```

### zdyz

```text
触发器: zdyz (剧情/任务) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventTrain_Finish
条件
  ├─ 单位类型判断(GetTrainedUnit(), 英雄) == TRUE
  └─ 任一成立
动作
  └─ 设置单位自定义值: GetTrainedUnit(), 0
```

### 吸血

```text
触发器: 吸血 (技能/物品) [✓] — 由于japi中的伤害事件和死亡面罩技能冲突

所以这里选择重新设计吸血系统

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ YDWEIsEventAttackDamage() == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"a"=OperatorRealMultiply(伤害值(), 0.50)
  ├─ SetUnitLifeBJ: 伤害来源(), OperatorRealAdd(单位状态(伤害来源(), UnitStateLife), 读取局部变量("a"))
  ├─ 设置局部变量:"tx"=创建特效(附着单位)(Abilities\Spells\Undead\VampiricAura\VampiricAuraTarget.mdl, 伤害来源(), "origin")
  ├─ YDWETimerDestroyEffect: 1.00, 读取局部变量("tx")
  └─ 开启触发器 当前触发器()
```

### liandao

```text
触发器: liandao (技能/物品) [✓] — 这里镰刀本身是不可丢弃的

但是需要信使运送物品

所以需要让镰刀在信使的身上时可以丢弃

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ (GetManipulatingUnit()类型ID) == n00U
  └─ 任一成立
动作
  └─ SetItemDroppableBJ: 被操作物品(), DropNoDropOptionDrop
```

### liandaono

```text
触发器: liandaono (技能/物品) [✓] — 信使完成运送任务后

需要将原本不可丢弃的物品

重新设置为不可丢弃

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroDropItem
条件
  ├─ (GetManipulatingUnit()类型ID) == n00U
  └─ 任一成立
动作
  └─ SetItemDroppableBJ: 被操作物品(), DropNoDropOptionNoDrop
```

### jingjizhijia

```text
触发器: jingjizhijia (技能/物品) [✓] — 模拟反甲

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位类型判断(伤害来源(), 建筑) == TRUE
  ├─ YDWEIsEventPhysicalDamage() == TRUE
  └─ 单位持有物品类型(触发单位(), I00P) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sh"=OperatorRealMultiply(伤害值(), 0.30)
  ├─ 伤害目标: 触发单位(), 伤害来源(), 读取局部变量("sh"), IsNotNot, IsNotNot, AttackTypeMagic, DamageTypeMagic, WEAPON_TYPE_WHOKNOWS
  └─ 开启触发器 当前触发器()
```

### wanghundediyu

```text
触发器: wanghundediyu (技能/物品) [✓] — 模拟附加百分比生命值伤害

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(伤害来源(), I016) == TRUE
  ├─ 单位类型判断(触发单位(), 建筑) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sh"=OperatorRealMultiply(单位状态(触发单位(), UnitStateMaxLife), 0.08)
  ├─ 如果
  │    ├─ 条件: 任一成立
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 读取局部变量("sh") OperatorGreaterEq 200.00
  │    │      ├─ 则
  │    │      │    设置局部变量:"sh"=200.00
  │    │      │    伤害目标: 伤害来源(), 触发单位(), 读取局部变量("sh"), IsNotIs, IsNotIs, AttackTypeHero, DamageTypeNormal, WEAPON_TYPE_WHOKNOWS
  │    │      └─ 否则
  │    │           伤害目标: 伤害来源(), 触发单位(), 读取局部变量("sh"), IsNotIs, IsNotIs, AttackTypeHero, DamageTypeNormal, WEAPON_TYPE_WHOKNOWS
  │    └─ 否则
  │         伤害目标: 伤害来源(), 触发单位(), 读取局部变量("sh"), IsNotIs, IsNotIs, AttackTypeHero, DamageTypeNormal, WEAPON_TYPE_WHOKNOWS
  └─ 开启触发器 当前触发器()
```

### sishenliandao

```text
触发器: sishenliandao (技能/物品) [✓] — 模拟斩杀效果

这里需要注意的是

混乱+通用可以视作真实伤害

但是不可以伤害虚无

法术+通用也是真实伤害

但是不能伤害魔免

真实伤害指不受护甲值和护甲类型影响的伤害

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(伤害来源(), I000) == TRUE
  ├─ 单位类型判断(触发单位(), 建筑) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"dwwz"=(触发单位()的位置)
  ├─ 设置局部变量:"smz"=单位生命百分比(触发单位())
  ├─ 如果
  │    ├─ 条件: 读取局部变量("smz") OperatorLessEq 8.00
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: 全部成立
  │    │      │    ├─ YDWEIsEventAttackType(AttackTypeMagic) == TRUE
  │    │      │    ├─ 任一成立
  │    │      ├─ 则
  │    │      │    伤害目标: 伤害来源(), 触发单位(), 9999.00, IsNotNot, IsNotNot, AttackTypeChaos, DamageTypeUniversal, WEAPON_TYPE_WHOKNOWS
  │    │      └─ 否则
  │    │           伤害目标: 伤害来源(), 触发单位(), 9999.00, IsNotNot, IsNotNot, AttackTypeNormal, DamageTypeUniversal, WEAPON_TYPE_WHOKNOWS
  │    │    CreateTextTagLocBJ: "TRIGSTR_1447", 读取局部变量("dwwz"), 0, 10.00, 83.40, 83.40, 83.40, 0
  │    │    设置局部变量:"pfwz"=bj_lastCreatedTextTag
  │    │    SetTextTagVelocityBJ: 读取局部变量("pfwz"), 64, 90
  │    │    SetTextTagFadepointBJ: 读取局部变量("pfwz"), 1.00
  │    │    YDWETimerDestroyTextTag: 2, 读取局部变量("pfwz")
  │    │    清除点 读取局部变量("dwwz")
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

### cuidianzhiren

```text
触发器: cuidianzhiren (技能/物品) [✓] — 模拟电刀

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(伤害来源(), I014) == TRUE
  ├─ 单位类型判断(触发单位(), 建筑) == TRUE
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sfzd"=(伤害来源()的位置)
  ├─ 设置局部变量:"sj"=随机实数(0, 100.00)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") OperatorLessEq 30.00
  │    ├─ 则
  │    │    如果
  │    │      ├─ 条件: (伤害来源()类型ID) == H008
  │    │      ├─ 则
  │    │      │    创建 1个|n003|→(伤害来源()的所有者) 在 读取局部变量("sfzd") 面向默认朝向
  │    │      │    设置局部变量:"mj"=bj_lastCreatedUnit
  │    │      │    添加技能: 读取局部变量("mj"), A04L
  │    │      │    单位发布命令(目标): 读取局部变量("mj"), UnitOrderChainLightning, 触发单位()
  │    │      │    启动计时器: 创建计时器(), 2.00s (一次性)
  │    │      └─ 否则
  │    │           创建 1个|n00S|→(伤害来源()的所有者) 在 读取局部变量("sfzd") 面向默认朝向
  │    │           设置局部变量:"mj"=bj_lastCreatedUnit
  │    │           添加技能: 读取局部变量("mj"), A04L
  │    │           单位发布命令(目标): 读取局部变量("mj"), UnitOrderChainLightning, 触发单位()
  │    │           启动计时器: 创建计时器(), 2.00s (一次性)
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

### leishenquanzhang

```text
触发器: leishenquanzhang (技能/物品) [✓] — 利用触发器关闭再开启

可以有效防止触发死循环

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ 单位持有物品类型(单位组第一个单位(玩家符合条件的单位((伤害来源()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))), I010) == TRUE
  ├─ YDWEIsEventAttackDamage() == TRUE
  ├─ 单位类型判断(触发单位(), 建筑) == TRUE
  └─ IsPlayerAlly(触发玩家(), (伤害来源()的所有者)) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sj"=随机实数(0, 100.00)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") OperatorLessEq 30.00
  │    ├─ 则
  │    │    设置局部变量:"yx"=玩家符合条件的单位((伤害来源()的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    单位组: 选取 读取局部变量("yx") 中所有单位
  │    │      ├─ 伤害目标: 选取单位(), 触发单位(), 80.00, IsNotNot, IsNotNot, AttackTypeNormal, DamageTypeUniversal, WEAPON_TYPE_WHOKNOWS
  │    │      ├─ AddSpecialEffectTargetUnitBJ: "origin", 触发单位(), Abilities\Spells\Other\Monsoon\MonsoonBoltTarget.mdl
  │    │      ├─ 设置局部变量:"tx"=bj_lastCreatedEffect
  │    │      └─ YDWETimerDestroyEffect: 1.00, 读取局部变量("tx")
  │    │    GroupClear: 读取局部变量("yx")
  │    │    删除单位组 读取局部变量("yx")
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

### kexuemianju

```text
触发器: kexuemianju (技能/物品) [✓] — 这部分其实做的不是很好

最好使用光环模拟双速效果

鞋子的移速加成不可以叠加

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventSpellEffect
条件
  ├─ 技能ID比较(施法技能ID(), OperatorEqualENE, A021)
  └─ 单位持有物品类型(GetSpellAbilityUnit(), I00A) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"gs"=A01W
  ├─ 设置局部变量:"jj"=A01Z
  ├─ 添加技能: GetSpellAbilityUnit(), 读取局部变量("gs")
  ├─ 添加技能: GetSpellAbilityUnit(), 读取局部变量("ys")
  ├─ 添加技能: GetSpellAbilityUnit(), 读取局部变量("jj")
  ├─ 启动计时器: 创建计时器(), 6.00s (循环)
  └─ 开启触发器 当前触发器()
```

### dazao

```text
触发器: dazao (技能/物品) [✓] — 简单的装备合成

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I00Y)
动作
  ├─ 关闭触发器 当前触发器()
  └─ 如果
       ├─ 条件: GetPlayerTeam((GetManipulatingUnit()的所有者)) == 2
       ├─ 则
       │    如果
       │      ├─ 条件: 玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold) OperatorGreaterEq 500
       │      ├─ 则
       │      │    设置局部变量:"sb"=0
       │      │    ── 上古魔杖 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I00W) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I00X) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I00W)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I00X)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00V, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 能量法杖 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), prvt) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), cnob) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), cnob)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), prvt)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00X, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 大法师水晶 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), penr) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), rwiz) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), rwiz)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), penr)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00W, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 巨人战斧 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ratf) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I00Z) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), ratf)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I00Z)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00R, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 战斧 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), prvt) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), gcel) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), prvt)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), gcel)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00Z, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 雷神权杖 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I011) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I012) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I011)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I012)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I010, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 贤者法衣 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), rin1) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ciri) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), rin1)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), ciri)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I012, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 闪电石 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), mnst) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), gcel) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), mnst)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), gcel)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I011, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 焠电之刃 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I011) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I015) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I011)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I015)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I014, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 猎人手套 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ratf) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), gcel) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), ratf)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), gcel)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I015, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 绝尘靴 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), bspd) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), pspd) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), bspd)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), pspd)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I017, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 神行靴 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), bspd) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), stel) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), bspd)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), stel)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00L, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 远行鞋 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I00L) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I017) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I00L)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I017)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I006, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 利爪护手 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ratf) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I01A) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), ratf)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I01A)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I01B, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 锋刃 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ratf) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I01B) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), ratf)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I01B)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I008, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 亡魂的低语 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), modt) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I015) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), modt)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I015)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I016, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 渴血面具 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), modt) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), gcel) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), modt)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), gcel)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00A, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 斗士铠甲 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), clfm) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), prvt) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), clfm)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), prvt)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I019, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 医者指环 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), rde4) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), hlst) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), rde4)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), hlst)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I018, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 烈火之甲 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I018) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I019) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I018)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), I019)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00O, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    ── 荆棘之甲 ──
       │      │    如果
       │      │      ├─ 条件: 全部成立
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), I018) == TRUE
       │      │      │    ├─ 单位持有物品类型(GetManipulatingUnit(), ratf) == TRUE
       │      │      ├─ 则
       │      │      │    设置局部变量:"sb"=OperatorIntegerAdd(读取局部变量("sb"), 1)
       │      │      │    设置局部变量:"1"=单位携带物品(按类型)(GetManipulatingUnit(), I018)
       │      │      │    设置局部变量:"2"=单位携带物品(按类型)(GetManipulatingUnit(), ratf)
       │      │      │    删除物品: 读取局部变量("1")
       │      │      │    删除物品: 读取局部变量("2")
       │      │      │    添加物品: I00P, GetManipulatingUnit()
       │      │      │    设置玩家属性: (GetManipulatingUnit()的所有者), PlayerStateGold, OperatorIntegerSubtract(玩家属性值((GetManipulatingUnit()的所有者), PlayerStateGold), 500)
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      │    如果
       │      │      ├─ 条件: 读取局部变量("sb") == 0
       │      │      ├─ 则
       │      │      │    显示文本→(GetManipulatingUnit()的所有者): 0
       │      │      │    开启触发器 当前触发器()
       │      │      │    返回
       │      │      └─ 否则: (无)
       │      └─ 否则
       │           显示文本→(GetManipulatingUnit()的所有者): 0
       │           开启触发器 当前触发器()
       │           返回
       └─ 否则
            显示文本→(GetManipulatingUnit()的所有者): 0
            开启触发器 当前触发器()
```

### zbxz

```text
触发器: zbxz (技能/物品) [✓] — 限制不同游戏模式的玩家不可以使用另一个模式的物品

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  ├─ GetPlayerTeam((触发单位()的所有者)) != 2
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"wplx"=物品类型ID(被操作物品())
  ├─ 设置局部变量:"sfzd"=(GetManipulatingUnit()的位置)
  ├─ 显示文本→(GetManipulatingUnit()的所有者): 0
  ├─ 删除物品: 被操作物品()
  ├─ 创建物品: 读取局部变量("wplx"), 读取局部变量("sfzd")
  ├─ 清除点 读取局部变量("sfzd")
  └─ 开启触发器 当前触发器()
```

### jzxz

```text
触发器: jzxz (技能/物品) [✓] — 限制不同模式的玩家不可以使用建筑物

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ GetPlayerTeam((触发单位()的所有者)) == 2
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tgrh)
  │    ├─ 则
  │    │    显示文本→(触发单位()的所有者): 0
  │    │    删除物品: 被操作物品()
  │    │    调整 (触发单位()的所有者) 的 PlayerStateGold: 600
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tsct)
  │    ├─ 则
  │    │    显示文本→(触发单位()的所有者): 0
  │    │    删除物品: 被操作物品()
  │    │    调整 (触发单位()的所有者) 的 PlayerStateGold: 30
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, tcas)
  │    ├─ 则
  │    │    显示文本→(触发单位()的所有者): 0
  │    │    删除物品: 被操作物品()
  │    │    调整 (触发单位()的所有者) 的 PlayerStateGold: 800
  │    └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

### yuanguyizhi

```text
触发器: yuanguyizhi (技能/物品) [✓] — 成长性装备制作方法

记录杀敌数并自动升级

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  ├─ GetPlayerTeam((凶手单位()的所有者)) == 2
  ├─ (死亡单位()的所有者) == Player00
  ├─ (死亡单位()的所有者) == 玩家1(红)
  ├─ (死亡单位()的所有者) == 玩家2(蓝)
  ├─ (死亡单位()的所有者) == 玩家3(青)
  ├─ (死亡单位()的所有者) == 玩家4(紫)
  ├─ (死亡单位()的所有者) == 玩家5(黄)
  └─ (死亡单位()的所有者) == 非玩家
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=凶手单位()
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"wjid"=玩家号(读取局部变量("wj"))
  ├─ 设置局部变量:"yg1"=I00I
  ├─ 设置局部变量:"yg2"=I00J
  ├─ 设置局部变量:"yg3"=I00K
  ├─ 单位组: 选取 玩家符合条件的单位(读取局部变量("wj"), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true)) 中所有单位
  │    ├─ 设置局部变量:"yx"=bj_lastCreatedGroup
  │    ├─ 设置局部变量:"pt"=选取单位()
  │    ├─ 设置局部变量:"ptwz"=(读取局部变量("pt")的位置)
  │    └─ 如果
  │         ├─ 条件: 任一成立
  │         ├─ 则
  │         │    如果
  │         │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg1"))) == 50
  │         │      ├─ 则
  │         │      │    删除物品: 单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg1"))
  │         │      │    创建物品: 读取局部变量("yg2"), 读取局部变量("ptwz")
  │         │      │    设置局部变量:"xwp"=bj_lastCreatedItem
  │         │      │    SetItemUserData: 读取局部变量("xwp"), 读取局部变量("wjid")
  │         │      │    单位添加物品: 读取局部变量("pt"), 读取局部变量("xwp")
  │         │      │    启动计时器: 创建计时器(), 1.00s (一次性)
  │         │      └─ 否则
  │         │           SetItemCharges: 单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg1")), OperatorIntegerAdd(物品剩余使用次数(单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg1"))), 1)
  │         │           GroupClear: 读取局部变量("yx")
  │         │           删除单位组 读取局部变量("yx")
  │         │    如果
  │         │      ├─ 条件: 物品剩余使用次数(单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg2"))) == 100
  │         │      ├─ 则
  │         │      │    删除物品: 单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg2"))
  │         │      │    创建物品: 读取局部变量("yg3"), 读取局部变量("ptwz")
  │         │      │    设置局部变量:"xwp"=bj_lastCreatedItem
  │         │      │    SetItemUserData: 读取局部变量("xwp"), 读取局部变量("wjid")
  │         │      │    单位添加物品: 读取局部变量("pt"), 读取局部变量("xwp")
  │         │      │    启动计时器: 创建计时器(), 1.00s (一次性)
  │         │      └─ 否则
  │         │           SetItemCharges: 单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg2")), OperatorIntegerAdd(物品剩余使用次数(单位携带物品(按类型)(读取局部变量("pt"), 读取局部变量("yg2"))), 1)
  │         │           GroupClear: 读取局部变量("yx")
  │         │           删除单位组 读取局部变量("yx")
  │         └─ 否则: (无)
  └─ 开启触发器 当前触发器()
```

### yuanbguyizhixianzhi

```text
触发器: yuanbguyizhixianzhi (技能/物品) [✓] — 限制不同玩家的装备不可以互相拾取

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetManipulatingUnit()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wp"=被操作物品()
  ├─ 设置局部变量:"wplx"=物品类型ID(读取局部变量("wp"))
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 设置局部变量:"wjid"=玩家号(读取局部变量("wj"))
  ├─ 设置局部变量:"wpid"=物品自定义值(读取局部变量("wp"))
  ├─ 设置局部变量:"sl"=物品剩余使用次数(读取局部变量("wp"))
  ├─ 如果
  │    ├─ 条件: 读取局部变量("wpid") == 读取局部变量("wjid")
  │    ├─ 则
  │    └─ 否则
  │         显示文本→读取局部变量("wj"): 0
  │         删除物品: 读取局部变量("wp")
  │         创建物品: 读取局部变量("wplx"), 读取局部变量("sfzd")
  │         设置局部变量:"xwp"=bj_lastCreatedItem
  │         SetItemCharges: 读取局部变量("xwp"), 读取局部变量("sl")
  │         SetItemUserData: 读取局部变量("xwp"), 读取局部变量("wpid")
  │         清除点 读取局部变量("sfzd")
  └─ 开启触发器 当前触发器()
```

### yzywjinyongzhuangbei

```text
触发器: yzywjinyongzhuangbei (技能/物品) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"sfz"=GetManipulatingUnit()
  ├─ 设置局部变量:"sfzd"=(读取局部变量("sfz")的位置)
  ├─ 设置局部变量:"wp"=被操作物品()
  ├─ 设置局部变量:"wplx"=物品类型ID(读取局部变量("wp"))
  ├─ 设置局部变量:"wj"=(读取局部变量("sfz")的所有者)
  ├─ 如果
  │    ├─ 条件: GetPlayerTeam(读取局部变量("wj")) == 2
  │    ├─ 则
  │    └─ 否则
  │         显示文本→读取局部变量("wj"): 0
  │         删除物品: 读取局部变量("wp")
  │         创建物品: 读取局部变量("wplx"), 读取局部变量("sfzd")
  │         清除点 读取局部变量("sfzd")
  └─ 开启触发器 当前触发器()
```

### chattxet

```text
触发器: chattxet (区域/禁地) [✗] — 这部分本身是想模拟单位在战斗过程中会说话发弹幕

可以增加一部分游戏趣味性

后来作为废弃方案了

但是这个触发我保留了

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ ── chat of attack ──
  ├─ 设置 chat_attack[1] = "蚌蚌给你两拳！"
  ├─ 设置 chat_attack[2] = "你怎么回事？小老弟？"
  ├─ 设置 chat_attack[3] = "偷袭！"
  ├─ 设置 chat_attack[4] = "一个右勾拳！"
  ├─ 设置 chat_attack[5] = "一个左正蹬！"
  ├─ 设置 chat_attack[6] = "不气盛能叫年轻人么？"
  ├─ 设置 chat_attack[7] = "兄弟们加把劲！早点打完早点收工！"
  ├─ 设置 chat_attack[8] = "WoCaoNImua[塞伯坦语]"
  ├─ 设置 chat_attack[9] = "师傅，你这瓜保熟么？"
  ├─ 设置 chat_attack[10] = "what's up锛?"
  ├─ 设置 chat_attack[11] = "有bear来！"
  ├─ ── chat of hypotenemia ──
  ├─ 设置 chat_hypotenemia[1] = "NewBee锛?"
  ├─ 设置 chat_hypotenemia[2] = "what's up，什么poi伤害？"
  ├─ 设置 chat_hypotenemia[3] = "我超我的血条呢？"
  ├─ 设置 chat_hypotenemia[4] = "队友呢？队友呢？救一下啊！"
  ├─ 设置 chat_hypotenemia[5] = "ShowPoi宰治，你给我等着！"
  ├─ 设置 chat_hypotenemia[6] = "溜了溜了。。。"
  ├─ 设置 chat_hypotenemia[7] = "我是谁？我在哪？我怎么残血了？"
  ├─ 设置 chat_hypotenemia[8] = "啊啊啊啊！我超！我想回家啊啊啊啊！"
  ├─ ── chat of hyperhp ──
  ├─ 设置 chat_hyperhp[1] = "就这？就这？"
  ├─ 设置 chat_hyperhp[2] = "搁着刮痧呢？"
  ├─ 设置 chat_hyperhp[3] = "没吃早饭么？用力！"
  ├─ 设置 chat_hyperhp[4] = "行不行啊？系√"
  ├─ 设置 chat_hyperhp[5] = "上点强度行不行？"
  ├─ 设置 chat_hyperhp[6] = "这么点力气，你这是在撒娇么？"
  ├─ ── chat of lose ──
  ├─ 设置 chat_lose[1] = "年轻人不讲武德！"
  └─ 设置 chat_lose[2] = "年轻人不要太气盛！"
```

### chat_attack

```text
触发器: chat_attack (区域/禁地) [✗]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ 单位类型判断(攻击单位(), 建筑) == TRUE
  └─ 单位类型判断(攻击单位(), 英雄) == TRUE
动作
  ├─ ── chatting of orc for attack ──
  └─ 如果
       ├─ 条件: OperatorCompareRace(GetPlayerRace((攻击单位()的所有者)), OperatorEqualENE, RaceOrc)
       ├─ 则
       │    设置局部变量:"speak"=随机实数(0, 100.00)
       │    如果
       │      ├─ 条件: 读取局部变量("speak") OperatorLessEq 5.00
       │      ├─ 则
       │      │    CreateTextTagUnitBJ: chat_attack[随机[1~11]], 攻击单位(), 0, 10, 100, 100, 100, 0
       │      │    设置局部变量:"pfwz"=bj_lastCreatedTextTag
       │      │    SetTextTagVelocityBJ: 读取局部变量("pfwz"), 64, 90
       │      │    SetTextTagFadepointBJ: 读取局部变量("pfwz"), 2.00
       │      │    YDWETimerDestroyTextTag: 4.00, GetLastCreatedTextTag()
       │      └─ 否则: (无)
       └─ 否则: (无)
```

### chat_hypotenemia

```text
触发器: chat_hypotenemia (区域/禁地) [✗]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ 单位类型判断(攻击单位(), 建筑) == TRUE
  └─ 单位类型判断(攻击单位(), 英雄) == TRUE
动作
  ├─ ── chatting of orc for attack ──
  └─ 如果
       ├─ 条件: OperatorCompareRace(GetPlayerRace((攻击单位()的所有者)), OperatorEqualENE, RaceOrc)
       ├─ 则
       │    设置局部变量:"speak"=随机实数(0, 100.00)
       │    如果
       │      ├─ 条件: 读取局部变量("speak") OperatorLessEq 5.00
       │      ├─ 则
       │      │    如果
       │      │      ├─ 条件: 伤害值() OperatorLessEq 10.00
       │      │      ├─ 则
       │      │      │    CreateTextTagUnitBJ: chat_hyperhp[随机[1~6]], 攻击单位(), 0, 10, 100, 100, 100, 0
       │      │      │    设置局部变量:"pfwz"=bj_lastCreatedTextTag
       │      │      │    SetTextTagVelocityBJ: 读取局部变量("pfwz"), 64, 90
       │      │      │    SetTextTagFadepointBJ: 读取局部变量("pfwz"), 2.00
       │      │      │    YDWETimerDestroyTextTag: 4.00, GetLastCreatedTextTag()
       │      │      └─ 否则: (无)
       │      │    如果
       │      │      ├─ 条件: 伤害值() OperatorGreaterEq 300.00
       │      │      ├─ 则
       │      │      │    CreateTextTagUnitBJ: chat_hypotenemia[随机[1~8]], 攻击单位(), 0, 10, 100, 100, 100, 0
       │      │      │    设置局部变量:"pfwz"=bj_lastCreatedTextTag
       │      │      │    SetTextTagVelocityBJ: 读取局部变量("pfwz"), 64, 90
       │      │      │    SetTextTagFadepointBJ: 读取局部变量("pfwz"), 2.00
       │      │      │    YDWETimerDestroyTextTag: 4.00, GetLastCreatedTextTag()
       │      │      └─ 否则: (无)
       │      └─ 否则: (无)
       └─ 否则: (无)
```

### bossstart

```text
触发器: bossstart (物品系统) [✓] — 这部分触发是我和污染者锤石共同完成的

电影，boss的AI和击杀判断部分由我完成

剩余部分由污染者锤石制作我又修改了一部分

制作电影时需要注意画面的流畅性

其中也可以制作单位做不同的动作

其中锁定单位身体可以做到让单位只转头之类的操作

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventHeroPickUpItem
条件
  └─ 物品类型比较(物品类型ID(被操作物品()), OperatorEqualENE, I01E)
动作
  ├─ 关闭触发器 当前触发器()
  └─ 如果
       ├─ 条件: nd OperatorGreaterEq 1
       ├─ 则
       │    销毁触发器(自身)
       │    关闭触发器 gg_trg_fuhuo
       │    销毁触发器(自身)
       │    战争迷雾开关: EnabledDisabledDisabled
       │    迷雾遮罩开关: EnabledDisabledDisabled
       │    设置局部变量:"x"=单位X坐标(gg_unit_n001_0147)
       │    设置局部变量:"y"=单位Y坐标(gg_unit_n001_0147)
       │    设置局部变量:"AI"=GetPlayersByMapControl(MapControlComputer)
       │    ForForceMultiple: 读取局部变量("AI")
       │    电影模式: OnOffOn, GetPlayersAll()
       │    EnableUserControl: OnOffOff
       │    CinematicFadeBJ: FadeTypeOptionFadeOutIn, 2, CineFilterTexturePanda, 100.00, 100.00, 100.00, 0
       │    PanCameraToTimed: 读取局部变量("x"), 读取局部变量("y"), 0
       │    设置局部变量:"boss"=创建单位(指定坐标)(PlayerNA, Nsjs, 读取局部变量("x"), 读取局部变量("y"), 270.00)
       │    ShowUnit: 读取局部变量("boss"), ShowHideHide
       │    SetUnitState: 读取局部变量("boss"), UnitStateMaxLifeSec, OperatorRealMultiply(8000.00, (nd转实数))
       │    设置生命百分比: 读取局部变量("boss"), 100.00
       │    SetUnitState: 读取局部变量("boss"), UnitStateArmorSec, OperatorRealMultiply(8.00, (nd转实数))
       │    SetUnitState: 读取局部变量("boss"), UnitStateDamageBaseSec, OperatorRealMultiply(40.00, (nd转实数))
       │    添加物品: kgal, 读取局部变量("boss")
       │    添加物品: stre, 读取局部变量("boss")
       │    添加物品: dtsb, 读取局部变量("boss")
       │    添加物品: amrc, 读取局部变量("boss")
       │    添加物品: stwa, 读取局部变量("boss")
       │    添加物品: rnsp, 读取局部变量("boss")
       │    SetUnitVertexColorBJ: gg_unit_n001_0147, 0.00, 0.00, 100, 0
       │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), 读取局部变量("boss"), GetHeroProperName(读取局部变量("boss")), SoundNull, "TRIGSTR_1678", AddSetToAdd, 2.00, WaitDontWait
       │    SetUnitVertexColorBJ: gg_unit_n001_0147, 0.00, 100.00, 0.00, 0
       │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), 读取局部变量("boss"), GetHeroProperName(读取局部变量("boss")), SoundNull, "TRIGSTR_1679", AddSetToAdd, 2.00, WaitDontWait
       │    SetUnitVertexColorBJ: gg_unit_n001_0147, 100.00, 0.00, 0.00, 0
       │    TransmissionFromUnitWithNameBJ: GetPlayersAll(), 读取局部变量("boss"), GetHeroProperName(读取局部变量("boss")), SoundNull, "TRIGSTR_1680", AddSetToAdd, 2.00, WaitDontWait
       │    ExplodeUnitBJ: gg_unit_n001_0147
       │    ShowUnit: 读取局部变量("boss"), ShowHideShow
       │    ForForceMultiple: 读取局部变量("AI")
       │    EnableUserControl: OnOffOn
       │    电影模式: OnOffOff, GetPlayersAll()
       │    ForceClear: 读取局部变量("AI")
       │    DestroyForce: 读取局部变量("AI")
       └─ 否则
            开启触发器 当前触发器()
            调整 (GetManipulatingUnit()的所有者) 的 PlayerStateGold: 500
            如果
              ├─ 条件: nd == 0
              ├─ 则
              │    显示文本→GetPlayersAll(): "TRIGSTR_1682"
              └─ 否则
                   显示文本→GetPlayersAll(): "TRIGSTR_1681"
```

### 1-1-BOSS群体击晕

```text
触发器: 1-1-BOSS群体击晕 (物品系统) [✓] — 这部分污染者锤石已经备注过了

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (攻击单位()类型ID) == Nsjs
  └─ 随机[1~10] == 1
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"d"=攻击单位()
  ├─ 设置局部变量:"u"=触发单位()
  ├─ ── 创建马甲击晕 ──
  ├─ 设置局部变量:"x"=单位X坐标(读取局部变量("u"))
  ├─ 设置局部变量:"y"=单位Y坐标(读取局部变量("u"))
  ├─ 设置局部变量:"m"=创建单位(指定坐标)((读取局部变量("d")的所有者), e002, 读取局部变量("x"), 读取局部变量("y"), 0)
  ├─ 添加技能: 读取局部变量("m"), Awrs
  ├─ UnitApplyTimedLife: 读取局部变量("m"), TimedLifeBuffCodeWaterElemental, 2.00
  ├─ IssueNeutralImmediateOrderById: (读取局部变量("d")的所有者), 读取局部变量("m"), OrderCodeStomp
  ├─ ── 随机发垃圾话 ──
  ├─ 设置局部变量:"sj"=随机[1~4]
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 1
  │    ├─ 则
  │    │    设置局部变量:"zf"="吃我一记重击！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 2
  │    ├─ 则
  │    │    设置局部变量:"zf"="不氪金还敢来挑战我？不知天高地厚！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 3
  │    ├─ 则
  │    │    设置局部变量:"zf"="我这一拳，三十年的氪金功力！你拿什么挡？！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  └─ 如果
       ├─ 条件: 读取局部变量("sj") == 4
       ├─ 则
       │    设置局部变量:"zf"="怎么回事呀，小老弟？咋又被击晕了呀？"
       │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       └─ 否则: (无)
```

### 1-3-BOSS跳斩

```text
触发器: 1-3-BOSS跳斩 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  ├─ (触发单位()类型ID) == Nsjs
  └─ 随机[1~20] == 1
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 设置局部变量:"d"=触发单位()
  ├─ 设置局部变量:"u"=伤害来源()
  ├─ 如果
  │    ├─ 条件: IsUnitRace(读取局部变量("u"), RaceCritters) == TRUE
  │    ├─ 则
  │    │    设置局部变量:"group"=玩家符合条件的单位((读取局部变量("u")的所有者), 布尔比较(单位类型判断(过滤单位(), 英雄), OperatorEqualENE, true))
  │    │    设置局部变量:"hero"=单位组第一个单位(读取局部变量("group"))
  │    │    设置局部变量:"u"=读取局部变量("hero")
  │    │    GroupClear: 读取局部变量("group")
  │    │    删除单位组 读取局部变量("group")
  │    └─ 否则: (无)
  ├─ 设置局部变量:"x"=单位X坐标(读取局部变量("u"))
  ├─ 设置局部变量:"y"=单位Y坐标(读取局部变量("u"))
  ├─ 设置局部变量:"dd"=Location(读取局部变量("x"), 读取局部变量("y"))
  ├─ ── 创建落地点特效 ──
  ├─ 设置局部变量:"tx"=创建特效(指定坐标)(UI\Feedback\SelectionCircleEnemy\SelectionCircleEnemy.mdl, 读取局部变量("x"), 读取局部变量("y"))
  ├─ EXSetEffectSize: 读取局部变量("tx"), 5.00
  ├─ YDWETimerDestroyEffect: 1.00, 读取局部变量("tx")
  ├─ ── 暂停单位，播放准备起跳动作 ──
  ├─ PauseUnit: 读取局部变量("d"), PauseUnpauseOptionPause
  ├─ 播放动画: 读取局部变量("d"), "Spell Throw"
  ├─ ── 起跳前飚垃圾话 ──
  ├─ 设置局部变量:"sj"=随机[1~4]
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 1
  │    ├─ 则
  │    │    设置局部变量:"zf"="让你尝尝我的厉害！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 2
  │    ├─ 则
  │    │    设置局部变量:"zf"="锵锵！污染者锤石登场！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 3
  │    ├─ 则
  │    │    设置局部变量:"zf"="注意注意！帅帅的污染者锤石来了！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 如果
  │    ├─ 条件: 读取局部变量("sj") == 4
  │    ├─ 则
  │    │    设置局部变量:"zf"="准备好起跳！准备好压扁他们！"
  │    │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
  │    └─ 否则: (无)
  ├─ 设置局部变量:"jd"=YDWEAngleBetweenUnitAndPoint(触发单位(), 读取局部变量("dd"))
  ├─ 设置局部变量:"l"=YDWEDistanceBetweenUnitAndPoint(触发单位(), 读取局部变量("dd"))
  ├─ ── 跳跃 ──
  ├─ YDWETimerPatternJumpAttack: 读取局部变量("d"), 读取局部变量("jd"), 读取局部变量("l"), 2.00, 0.03, 200.00, 0, "chest", Abilities\Spells\Other\Incinerate\FireLordDeathExplode.mdl
  ├─ ── 计算伤害 ──
  ├─ 设置局部变量:"s"=YDWEOperatorReal3((nd转实数), YOperatorMultiply, 150.00, YOperatorAdd, 100.00)
  ├─ ── 造成伤害 ──
  ├─ 启动计时器: 创建计时器(), 2.00s (一次性)
  └─ 启动计时器: 创建计时器(), 30.00s (一次性)
```

### 1-4-BOSS分身

```text
触发器: 1-4-BOSS分身 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ YDWE任意单位受伤注册()
条件
  └─ (触发单位()类型ID) == Nsjs
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 如果
  │    ├─ 条件: (伤害来源()类型ID) == h006
  │    ├─ 则
  │    │    YDWESetEventDamage: 0.
  │    └─ 否则: (无)
  ├─ 设置局部变量:"d"=触发单位()
  ├─ ── 免疫击晕 ──
  ├─ UnitRemoveBuffNT: 读取局部变量("d"), BSTN
  ├─ UnitRemoveBuffNT: 读取局部变量("d"), BPSE
  ├─ ── 读取生命值 ──
  ├─ 设置局部变量:"s"=单位生命百分比(读取局部变量("d"))
  ├─ ── 判定施法条件 ──
  └─ 如果
       ├─ 条件: 全部成立
       │    ├─ 读取局部变量("s") OperatorLessEq 70.00
       │    ├─ 检查哈希表有数据(单位类型, 读取局部变量("d"), 布尔, "分身") == TRUE
       ├─ 则
       │    ── 垃圾话环节 ──
       │    设置局部变量:"sj"=随机[1~4]
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 1
       │      ├─ 则
       │      │    设置局部变量:"zf"="一气化三清！"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 2
       │      ├─ 则
       │      │    设置局部变量:"zf"="想杀我？先和我的手下过过手。"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 3
       │      ├─ 则
       │      │    设置局部变量:"zf"="不过尔尔，休息一下我再回来。"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 4
       │      ├─ 则
       │      │    设置局部变量:"zf"="略略略，你来打我呀！可跳可痒痒呢。"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    ── 读取并且记录坐标，在分身死亡之后在回来 ──
       │    设置局部变量:"x"=单位X坐标(读取局部变量("d"))
       │    设置局部变量:"y"=单位Y坐标(读取局部变量("d"))
       │    保存数据到哈希表: [单位类型.读取局部变量("d")."x坐标"] = 读取局部变量("x")
       │    保存数据到哈希表: [单位类型.读取局部变量("d")."y坐标"] = 读取局部变量("y")
       │    ── 创建新单位 ──
       │    设置局部变量:"w"=(读取局部变量("d")的所有者)
       │    设置局部变量:"u1"=创建单位(指定坐标)(读取局部变量("w"), npn5, 读取局部变量("x"), (读取局部变量("y") + 100.00), 0)
       │    SetUnitState: 读取局部变量("u1"), UnitStateMaxLifeSec, OperatorRealMultiply(800.00, (nd转实数))
       │    设置生命百分比: 读取局部变量("u1"), 100.00
       │    SetUnitState: 读取局部变量("u1"), UnitStateArmorSec, OperatorRealMultiply(2.00, (nd转实数))
       │    SetUnitState: 读取局部变量("u1"), UnitStateDamageBaseSec, OperatorRealMultiply(20.00, (nd转实数))
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Demon\DarkConversion\ZombifyTarget.mdl, 读取局部变量("u"), "overhead")
       │    设置局部变量:"u2"=创建单位(指定坐标)(读取局部变量("w"), npn4, (读取局部变量("x") + 100.00), (读取局部变量("y") + 100.00), 0)
       │    SetUnitState: 读取局部变量("u2"), UnitStateMaxLifeSec, OperatorRealMultiply(1000.00, (nd转实数))
       │    设置生命百分比: 读取局部变量("u2"), 100.00
       │    SetUnitState: 读取局部变量("u2"), UnitStateArmorSec, OperatorRealMultiply(3.00, (nd转实数))
       │    SetUnitState: 读取局部变量("u2"), UnitStateDamageBaseSec, OperatorRealMultiply(15.00, (nd转实数))
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Demon\DarkConversion\ZombifyTarget.mdl, 读取局部变量("u"), "overhead")
       │    设置局部变量:"u3"=创建单位(指定坐标)(读取局部变量("w"), npn6, 读取局部变量("x"), 读取局部变量("y"), 0)
       │    SetUnitState: 读取局部变量("u3"), UnitStateMaxLifeSec, OperatorRealMultiply(1500.00, (nd转实数))
       │    设置生命百分比: 读取局部变量("u3"), 100.00
       │    SetUnitState: 读取局部变量("u3"), UnitStateArmorSec, OperatorRealMultiply(4.00, (nd转实数))
       │    SetUnitState: 读取局部变量("u3"), UnitStateDamageBaseSec, OperatorRealMultiply(10.00, (nd转实数))
       │    销毁特效 创建特效(附着单位)(Abilities\Spells\Demon\DarkConversion\ZombifyTarget.mdl, 读取局部变量("u"), "overhead")
       │    ── 移动BOSS，假装隐藏 ──
       │    ShowUnit: 读取局部变量("d"), ShowHideHide
       │    ── 恢复部分生命值和魔法值 ──
       │    设置局部变量:"s"=(读取局部变量("s") + 10.00)
       │    设置生命百分比: 读取局部变量("d"), 读取局部变量("s")
       │    设置魔法百分比: 读取局部变量("d"), 100
       │    ── 用自定义值设置CD ──
       │    保存数据到哈希表: [单位类型.读取局部变量("d")."分身"] = true
       │    启动计时器: 创建计时器(), 120.00s (一次性)
       │    ── 记录分身时间，到时间也会自动回归 ──
       │    启动计时器: 创建计时器(), 60.00s (一次性)
       └─ 否则: (无)
```

### 1-5-BOSS分身死亡

```text
触发器: 1-5-BOSS分身死亡 (物品系统) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 任一成立
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"group"=玩家指定类型单位(PlayerNA, Nsjs)
  ├─ 设置局部变量:"d"=单位组第一个单位(读取局部变量("group"))
  ├─ GroupClear: 读取局部变量("group")
  ├─ 删除单位组 读取局部变量("group")
  ├─ 设置局部变量:"z"=从哈希表读取数据(单位类型, 读取局部变量("d"), "分身数量")
  ├─ 设置局部变量:"z"=(读取局部变量("z") + 1)
  ├─ 保存数据到哈希表: [单位类型.读取局部变量("d")."分身数量"] = 读取局部变量("z")
  └─ 如果
       ├─ 条件: 读取局部变量("z") OperatorGreaterEq 3
       ├─ 则
       │    清除哈希表: [单位类型.读取局部变量("d").整数]
       │    设置局部变量:"x"=从哈希表读取数据(单位类型, 读取局部变量("d"), "x坐标")
       │    设置局部变量:"y"=从哈希表读取数据(单位类型, 读取局部变量("d"), "y坐标")
       │    移动单位: 读取局部变量("d"), 读取局部变量("x"), 读取局部变量("y")
       │    ShowUnit: 读取局部变量("d"), ShowHideShow
       │    ── 垃圾话环节 ──
       │    设置局部变量:"sj"=随机[1~4]
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 1
       │      ├─ 则
       │      │    设置局部变量:"zf"="休息时间结束了！"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 2
       │      ├─ 则
       │      │    设置局部变量:"zf"="没想到吧？我又回来了！"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 3
       │      ├─ 则
       │      │    设置局部变量:"zf"="BOSS登场！记得鼓掌！"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       │    如果
       │      ├─ 条件: 读取局部变量("sj") == 4
       │      ├─ 则
       │      │    设置局部变量:"zf"="桀桀桀！居然还活着吗？"
       │      │    显示文本→GetPlayersAll(): "|cffff0000污染者锤石|r：" + 读取局部变量("zf")
       │      └─ 否则: (无)
       └─ 否则: (无)
```

### bossAI

```text
触发器: bossAI (物品系统) [✓] — 简单的AI

让boss实现酒火连击

其中醉酒云雾技能作为中立敌对单位技能时

中立敌对单位也会使用该技能

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventAttacked
条件
  ├─ (攻击单位()类型ID) == Nsjs
  └─ 单位有魔法效果(GetAttackedUnitBJ(), BNdh) == TRUE
动作
  ├─ 关闭触发器 当前触发器()
  ├─ 开启触发器 当前触发器()
  ├─ 设置局部变量:"x"=单位X坐标(GetAttackedUnitBJ())
  ├─ 设置局部变量:"y"=单位Y坐标(GetAttackedUnitBJ())
  └─ 命令 攻击单位() → UnitOrderBreathOfFire 到 读取局部变量("x")
```

### bosskill

```text
触发器: bosskill (物品系统) [✓] — 判定胜利条件和失败条件

玩家组和单位组一样

是需要清空并删除的

创建时也是利用变量创建组

——by.，萌萌的立华奏
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - 单位死亡
条件
  └─ 死亡单位() == 单位组第一个单位(玩家指定类型单位(PlayerNA, Nsjs))
动作
  ├─ CustomVictoryBJ: (凶手单位()的所有者), UseSkipOptionUse, UseSkipOptionUse
  ├─ 设置局部变量:"lose_player"=符合条件的玩家(布尔比较(IsPlayerAlly(过滤玩家(), (凶手单位()的所有者)), OperatorEqualENE, false))
  ├─ 设置局部变量:"win_player"=符合条件的玩家(布尔比较(IsPlayerAlly(过滤玩家(), (凶手单位()的所有者)), OperatorEqualENE, true))
  ├─ ForForceMultiple: 读取局部变量("lose_player")
  └─ ForForceMultiple: 读取局部变量("win_player")
```

