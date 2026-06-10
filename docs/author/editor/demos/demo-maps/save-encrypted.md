---
title: 存档加密 - 演示图实战
category: kk-triggers
slug: demo-maps/save-encrypted
description: 演示图 存档加密 的完整 GUI 触发器代码
updated: 2026-06-01
---

# 🎮 存档加密 — 演示图实战

> 演示图：存档加密.w3x
>
> 触发器数：**5**
>
> 📁 本地路径：`F:\AI\AI-machine\W3演示图\`

## 📑 触发器目录

- 未命名触发器 001
- 未命名触发器 001 复制
- 未命名触发器 001 复制 复制
- 未命名触发器 002
- 未命名触发器 003

---

## 📜 触发器代码

### 未命名触发器 001

```text
触发器: 未命名触发器 001 (初始化) [✓] — 1位密码：61

2位密码：3843

3位密码：238327
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-s"
条件
  └─ 无
动作
  ├─ 设置 String = (玩家名:Player00)
  ├─ 设置 String2 = "0000000000"
  ├─ 设置 String3 = ""
  ├─ 设置 S = ""
  ├─ 循环整数A 0→11
  │    └─ 如果
  │         ├─ 条件: (Hero类型ID) == HeroType[循环整数A()]
  │         ├─ 则
  │         │    设置 Integer = 循环整数A()
  │         │    设置 String3 = 自定义代码("I2T(udg_Integer)")
  │         └─ 否则: (无)
  ├─ 设置 S = S + String3
  ├─ 设置 Integer = IMinBJ(GetHeroXP(Hero), 238327)
  ├─ 设置 String3 = 自定义代码("I2T(udg_Integer)")
  ├─ 设置 String3 = 取子字符串(String2, 1, (3 - StringLength(String3))) + String3
  ├─ 设置 S = S + String3
  ├─ 设置 Integer = IMinBJ(玩家属性值(Player00, PlayerStateGold), 238327)
  ├─ 设置 String3 = 自定义代码("I2T(udg_Integer)")
  ├─ 设置 String3 = 取子字符串(String2, 1, (3 - StringLength(String3))) + String3
  ├─ 设置 S = S + String3
  ├─ 设置 Integer = IMinBJ(英雄属性(HeroStatStr, Hero, InclusionExclude), 3843)
  ├─ 设置 String3 = 自定义代码("I2T(udg_Integer)")
  ├─ 设置 String3 = 取子字符串(String2, 1, (2 - StringLength(String3))) + String3
  ├─ 设置 S = S + String3
  ├─ 设置 Integer = IMinBJ(英雄属性(HeroStatAgi, Hero, InclusionExclude), 3843)
  ├─ 设置 String3 = 自定义代码("I2T(udg_Integer)")
  ├─ 设置 String3 = 取子字符串(String2, 1, (2 - StringLength(String3))) + String3
  ├─ 设置 S = S + String3
  ├─ 设置 Integer = IMinBJ(英雄属性(HeroStatInt, Hero, InclusionExclude), 3843)
  ├─ 设置 String3 = 自定义代码("I2T(udg_Integer)")
  ├─ 设置 String3 = 取子字符串(String2, 1, (2 - StringLength(String3))) + String3
  ├─ 设置 S = S + String3
  ├─ ForLoopBMultiple: 1, 6
  ├─ CustomScriptCode: "set udg_S = C2P(udg_S,udg_String)"
  ├─ CustomScriptCode: "call SaveCode(udg_S,udg_String)"
  ├─ CustomScriptCode: "set udg_S = CodeColor(udg_S)"
  ├─ 显示文本→Player00: 0
  ├─ 显示文本→Player00: 0
  └─ 显示文本→Player00: 0
```

### 未命名触发器 001 复制

```text
触发器: 未命名触发器 001 复制 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-cn"
条件
  └─ 无
动作
  ├─ 设置 String = 取子字符串(玩家聊天字符串(), 5, StringLength(玩家聊天字符串()))
  └─ 设置 Player00 名字 = String
```

### 未命名触发器 001 复制 复制

```text
触发器: 未命名触发器 001 复制 复制 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 玩家 Player00 输入 "-l"
条件
  └─ Hero == UnitNull
动作
  ├─ 设置 String = 取子字符串(玩家聊天字符串(), 4, StringLength(玩家聊天字符串()))
  ├─ 设置 String2 = (玩家名:Player00)
  ├─ 设置 String3 = 自定义代码("P2C(udg_String,udg_String2)")
  └─ 如果
       ├─ 条件: String3 == "Error Password Code"
       ├─ 则
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,0,1))")
       │    创建 1个|HeroType[Integer]|→Player00 在 (区域gg_rct______________000中心) 面向默认朝向
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,1,4))")
       │    SetHeroXP: 最后创建的单位(), Integer, ShowHideShow
       │    设置 Hero = 最后创建的单位()
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,4,7))")
       │    设置玩家属性: Player00, PlayerStateGold, Integer
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,7,9))")
       │    修改 Hero 的HeroStatStr: ModifyMethodSetInteger
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,9,11))")
       │    修改 Hero 的HeroStatAgi: ModifyMethodSetInteger
       │    设置 Integer = 自定义代码("T2I(SubString(udg_String3,11,13))")
       │    修改 Hero 的HeroStatInt: ModifyMethodSetInteger
       │    设置 A = 13
       │    循环整数A 1→6
       │      ├─ 设置 Integer = 自定义代码("T2I(SubString(udg_String3,udg_A,udg_A+2))")
       │      ├─ 添加物品: ItemType[Integer], Hero
       │      └─ 设置 A = (A + 2)
       └─ 否则
            显示文本→Player00: 0
```

### 未命名触发器 002

```text
触发器: 未命名触发器 002 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 地图初始化
条件
  └─ 无
动作
  ├─ CustomScriptCode: "call SetPasswordcode()"
  ├─ 显示文本→Player00: 0
  ├─ 设置 HeroType[0] = Hpal
  ├─ 设置 HeroType[1] = Hamg
  ├─ 设置 HeroType[2] = Hmkg
  ├─ 设置 HeroType[3] = Hblm
  ├─ 设置 HeroType[4] = Obla
  ├─ 设置 HeroType[5] = Ofar
  ├─ 设置 HeroType[6] = Otch
  ├─ 设置 HeroType[7] = Oshd
  ├─ 设置 HeroType[8] = Ekee
  ├─ 设置 HeroType[9] = Emoo
  ├─ 设置 HeroType[10] = Edem
  ├─ 设置 HeroType[11] = Ewar
  ├─ 设置 ItemType[0] = ratf
  ├─ 设置 ItemType[1] = ckng
  ├─ 设置 ItemType[2] = desc
  ├─ 设置 ItemType[3] = rde4
  ├─ 设置 ItemType[4] = ofro
  ├─ 设置 ItemType[5] = modt
  ├─ 设置 ItemType[6] = afac
  ├─ 设置 ItemType[7] = ssil
  ├─ 设置 ItemType[8] = stel
  ├─ 设置 ItemType[9] = ciri
  ├─ 设置 ItemType[10] = lhst
  ├─ 设置 ItemType[11] = lgdh
  ├─ 设置 ItemType[12] = clfm
  ├─ 设置 ItemType[13] = gcel
  ├─ 设置 ItemType[14] = bgst
  ├─ 设置 ItemType[15] = rhth
  ├─ 设置 ItemType[16] = kpin
  ├─ 设置 ItemType[17] = hval
  ├─ 设置 ItemType[18] = ward
  ├─ 设置 ItemType[19] = ajen
  └─ SetPlayerMaxHeroesAllowed: 1, Player00
```

### 未命名触发器 003

```text
触发器: 未命名触发器 003 (初始化) [✓]
───────────────────────────────────────────────────────
事件
  └─ 任意单位 - PlayerUnitEventTrain_Finish
条件
  └─ 无
动作
  └─ 设置 Hero = GetTrainedUnit()
```

