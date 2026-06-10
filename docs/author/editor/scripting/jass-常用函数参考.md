---
title: JASS 常用函数参
category: scripting
updated: 2026-05-30
model: openai/MiniMax-M2.7-highspeed
quality_score: 0.72
discovered_via: manual
sources:
  - https://jass.sourceforge.net/doc/
  - https://github.com/lep/jassdoc
  - https://www.hiveworkshop.com/forums/scripting-tutorials.280/
  - https://www.hiveworkshop.com/threads/beginning-jass-tutorial-series.30765/
  - https://wc3we.fandom.com/wiki/Jass_Coding
---

# JASS 常用函数参

## JASS简介与环境准备

本节将带你认识什么是JASS语言，了解触发编辑器的基本界面，以及它与传统GUI触发器的区别。学完本节后，你将能够区分两种触发方式，为后续学习代码编写打下基础

### 操作步骤

1. **第一步：认识JASS语言** JASS全称"Just Another Scripting Syntax"，直译为"另一种脚本语[^6]。简单来说，它是一种用于编触发的编程语言。触发器就像游戏自动指令，告Warcraft III 在什么情况下做什么事。例如：当单位死亡时、当地图开始时、当玩家点击某个按钮时——这些都需要触发器来控制

2. **第二步：打开触发编辑* 在World Editor（世界编辑器）中，按下键盘快捷键 **F4** 即可打开触发编辑器窗口[^4]。或者你也可以点击顶部菜单栏触发按钮。这个界面分为左右两栏：左边是触发器列表，右边是选中触发器的具体内容

3. **第三步：了解GUI触发* GUI图形用户界面"的缩写[^5]。当你用鼠标点击、拖拽来创建触发器时，实际上就是在使用GUI触发器。这种方式不需要写代码，适合简单功能，但缺点是功能受限，且生成的代码不够灵活

4. **第四步：切换到JASS视图** 在触发编辑器中，选中任意一个触发器，右键点击触发器名称，选择"转换为自定义代码"（Convert to Custom Text）[^5]。此时，原本的图形界面会变成一行行代码——这才是真正的JASS代码。恭喜你，你已经迈出了学习代码的第一步！

> **💡 新手提示**：别被代码吓到！JASS代码其实就像一机械指令"，每个单词都有固定含义。你不需要记住所有内容，只需要理..发生"（事件）如果..."（条件）就执.."（动作）这三个核心概念即可

> **⚠️ 常见错误**：很多新手误以为必须完全抛弃GUI才能学JASS。实际上*GUI和JASS可以混合使用**！你完全可以用GUI创建基础框架，然后用JASS扩展复杂功能，这样学习曲线会更平缓

### 小结

完成以上步骤后，你应该已经理解了JASS是一种用于控制游戏逻辑的脚本语言，能够打开触发编辑器查看触发器列表，并且学会了如何在GUI和代码视图之间切换。接下来，我们将深入学习如何编写你的第一段JASS代码

## 常用显示与信息输出函

本节将介JASS 中最常用*显示函数**，学完后你能在游戏屏幕上向玩家展示文字消息，还能创建点击式的对话框交互。这些是 RPG 游戏*任务提示***系统公告***玩家选择菜单**的基础

### 屏幕消息显示函数

1. **DisplayTextToPlayer 在指定位置显示消* 这是最基础的显示函数[^2]

   语法：`DisplayTextToPlayer(player, x, y, message)`
   
   - `player`：要显示给哪个玩家，`Player(0)` 表示玩家1
   - `x, y`：屏幕坐标（常用 `0, 0` 表示左上角）
   - `message`：要显示的文字，记得加引`"你好"`

2. **DisplayTimedTextToPlayer 显示带倒计时的消息** 消息会在几秒后自动消失[^2]

   比上面多一个参数：`duration`（持续秒数），常用于"5秒后开始游这类提示

3. **SimError 显示红色错误提示** 专门用于提示玩家操作有误[^2]

   语法：`SimError(player, "背包已满)`
   
   这种消息会自动变红色，玩家一眼就能注意到

4. **BJDebugMsg 调试专用消息** 只在测试时用，不会出现在正式游戏中[^5]

> **💡 新手提示**：显示中文需要用一对双引号包裹，例`DisplayTextToPlayer(Player(0), 0, 0, "欢迎来到RPG)`。漏掉引号是新手最常见的报错原因

> **⚠️ 常见错误**：直接在函数里写中文字符串，但地图编码没设置对会导致乱码。解决方法是：World Editor 菜单栏「文件」→「打开/保存」→「地图文件编码」改UTF-8

### 游戏内对话框

对话框是弹出一*带按钮的选择窗口**，适合让玩家做选择题（比如选择职业、难度）

1. **创建对话* `DialogCreate()` 返回一个对话框变量[^2]

2. **设置对话框标* `DialogSetMessage(dialog, "请选择你的职业")`

3. **添加按钮** `DialogAddButton(dialog, "战士", 1)`，数字是按钮*返回*

4. **显示给玩* `DialogDisplay(player, dialog, true)`，true=显示，false=隐藏

对话框需要配*触发*监听按钮点击事件才能发挥作用

> **💡 新手提示**：对话框使用完毕后记得用 `DialogClear(dialog)` 清空内容，再`DialogDestroy(dialog)` 销毁，否则会造成**内存泄漏**

### 小结

完成以上内容后，你应该掌握了
- 如何`DisplayTextToPlayer` 在屏幕上显示文字
- 如何`SimError` 显示醒目的错误提
- 如何创建带有选项按钮的对话框

💡 **下一步建*：尝试在触发器编辑器中创建一个简单的触发：当游戏开始时，用 JASS 代码向所有玩家显欢迎进入游戏的欢迎语

## 单位与玩家相关函

本节将带你认识JASS中最常用的两大类函数：操*单位**（游戏中的角色、建筑等）和操作**玩家**（控制游戏中的各个势力）。学完本节后，你就能用代码创建单位、移动它们、修改生命值，以及控制哪个玩家拥有哪个单位

### 单位创建与删

在JASS中，创建一个单位需要四个关键信息：这个单位属于谁（哪个玩家）、单位类型是什么（单位ID）、创建在什么位置（X和Y坐标）[^1]

```jass
// 创建一个骑兵单位，位置在地图坐1000, 1500)
local unit u = CreateUnit(Player(0), 'hpal', 1000, 1500, 0)
```

> **💡 新手提示**：单位ID是一字符代码，如 `'hpal'` 代表圣骑士。你可以在对象编辑器中查看每个单位的ID，将鼠标悬停在单位名称上即可看到

> **⚠️ 常见错误**：新手常忘记`CreateUnit` 的返回值存到变量里。之后想要操作这个单位时，却发现无法引用它。一定要`local unit u = CreateUnit(...)` 来保存这个单位！

删除单位的函数很简单：

```jass
call RemoveUnit(u)
```

### 玩家与势力操

每个玩家在JASS中用 `Player(i)` 函数表示，其`i` 1的数字，代表12个玩家槽位（0号玩家通常是你自己）[^2]。获取单位属于哪个玩家：

```jass
local player p = GetOwningPlayer(u)
```

修改单位的归属（ ownership）：

```jass
call SetUnitOwner(u, Player(1), true)
```

### 单位属性修

修改单位位置是最常用的操作之一[^1]

```jass
call SetUnitX(u, 2000)
call SetUnitY(u, 2000)
// 或者一次性设置：
call SetUnitPosition(u, 2000, 2000)
```

> **💡 新手提示**：`SetUnitX` `SetUnitY` 只改变坐标，不检查障碍物；`SetUnitPosition` 会自动将单位放置在最近的合法位置

修改生命值和魔法值：

```jass
call SetUnitLife(u, 500.0)    // 设置00点生
call SetUnitMana(u, 200.0)    // 设置00点魔
```

### 小结

完成以上学习后，你应该掌握了以下技能：使用 `CreateUnit` 创建单位、`RemoveUnit` 删除单位、`GetOwningPlayer` 获取单位所属玩家、`SetUnitOwner` 更改归属，以`SetUnitX/Y` `SetUnitLife/Mana` 修改单位的位置和属性。这些就是你在RPG地图中实召唤怪物"转移单位所有权"扣血扣蓝"等功能的基石

## 触发器核心函

本节将带你认JASS 中最重要的几类函数—*触发器管理函**事件条件函数**。学完本节后，你将能够用 JASS 代码创建一个完整的触发器逻辑，理解触发器事件触发"执行动作"的全过程

> **💡 先理解概*：触发器（Trigger）就像一命令清单"——当某个事件发生时（比如单位死亡），触发器检查条件是否满足，如果满足就执行预设的动作。JASS 函数就是用来编写这张"命令清单"的工具

### 触发器创建与管理

触发器的生命周期分为三步*创建 注册事件/条件 启用/销*

#### 第一步：创建触发

JASS 中，创建一个新的触发器使用 `CreateTrigger()` 函数[^1][^2]

```jass
function Trig_Example_Actions takes nothing returns nothing
    // 在这里写你的动作代码
    call DisplayTextToForce(GetPlayersAll(), "触发器执行了)
endfunction

function InitTrig_Example takes nothing returns nothing
    // 创建触发
    local trigger t = CreateTrigger()
    
    // 后续会在这里注册事件和条
    
    // 关联动作函数
    call TriggerAddAction(t, function Trig_Example_Actions)
endfunction
```

> **💡 新手提示**：`CreateTrigger()` 返回一个触发器句柄（可以理解为"编号"），必须用局部变`local trigger` 保存它，这样才能后续操作这个触发器

#### 第二步：启用或禁用触发器

- `EnableTrigger(trigger whichTrigger)` 激活触发器[^1]
- `DisableTrigger(trigger whichTrigger)` 关闭触发器[^1]
- `IsTriggerEnabled(trigger whichTrigger)` 检查触发器是否启用

```jass
call DisableTrigger(t)  // 暂时关闭这个触发
call EnableTrigger(t)  // 重新激
```

> **⚠️ 常见错误**：新手经常忘记触发器默认*启用状*的。如果你在某个条件下调用`DisableTrigger(t)`，一定要记得之后重新 `EnableTrigger(t)`，否则这个触发器就永沉睡"了

#### 第三步：销毁触发器

当触发器不再需要时，应使用 `DestroyTrigger(trigger whichTrigger)` 释放内存[^1]

```jass
call DestroyTrigger(t)  // 销毁后不能再次使用
```

> **💡 新手提示**：销毁后的触发器不能使用，但如果你在 `InitTrig_` 函数中创建触发器（地图初始化时），通常**不需要销*，因为游戏结束时触发器会自动清理

### 事件与条件函

事件（Event）告诉触发器"什么时候执，条件（Condition）告诉触发器"什么情况下才执

#### 第一步：注册事件（Event

事件函数用于将触发器与游戏事件关联[^2][^6]。常见的事件注册方式

```jass
// 监听单位死亡事件
call TriggerRegisterUnitEvent(t, gg_unit_H001_0001, EVENT_UNIT_DEATH)

// 监听变量变化事件
call TriggerRegisterVariableEvent(t, "udg_MyVariable", LESS_THREE, 10)

// 监听玩家聊天事件
call TriggerRegisterPlayerChatEvent(t, Player(0), "hello", false)
```

> **💡 新手提示**：不同的游戏事件需要使用不同的注册函数。例如：
> - 单位相关事件 `TriggerRegisterUnitEvent`
> - 变量变化事件 `TriggerRegisterVariableEvent`
> - 玩家交互事件 `TriggerRegisterPlayerChatEvent`
> 
> 记不住没关系，遇到时查文档即可

#### 第二步：添加条件（Condition

条件函数用于过滤事件，只有满足条件的才会执行动作[^2]

```jass
function IsHero takes nothing returns boolean
    return IsUnitType(GetTriggerUnit(), UNIT_TYPE_HERO)
endfunction

function InitTrig_Hero takes nothing returns nothing
    local trigger t = CreateTrigger()
    call TriggerRegisterUnitEvent(t, gg_unit_H001_0001, EVENT_UNIT_DEATH)
    
    // 添加条件函数
    call TriggerAddCondition(t, Condition(function IsHero))
    
    call TriggerAddAction(t, function Trig_Hero_Actions)
endfunction
```

> **⚠️ 常见错误**：`TriggerAddCondition` 接收的是**函数引用**，必须用 `Condition(function 函数` 包裹，直接写 `IsHero` `Condition(IsHero)` 都是错误的

#### 第三步：关联动作（Action

动作函数是触发器真正要执行的代码[^1]

```jass
function Trig_Hero_Actions takes nothing returns nothing
    local unit dyingHero = GetTriggerUnit()
    
    // 给击杀者奖00金币
    call SetPlayerState(GetKillingUnit(), PLAYER_STATE_GOLD_GAINED, 100)
    
    call DisplayTextToForce(GetPlayersAll(), GetUnitName(dyingHero) + " 阵亡了！")
endfunction
```

### 小结

完成以上步骤后，你应该掌握了

- 使用 `CreateTrigger()` 创建新触发器
- 使用 `EnableTrigger()` / `DisableTrigger()` 控制触发器开
- 使用 `TriggerRegisterUnitEvent()` 等函数注册事
- 使用 `TriggerAddCondition()` 添加条件过滤
- 使用 `TriggerAddAction()` 关联动作函数

> **🎯 实战任务**：尝试编写一个完整触发器：当任意英雄死亡时，显示"XXX 阵亡了！"的消息，并给击杀者增50 金币。完成后在地图中测试，观察效果是否符合预期

## 数学与特效函

本节将带你认识JASS中最常用*数学运算函数***特效函数**。学完后，你将能够实现单位移动、距离计算，以及给技能添加炫酷的视觉效果

### 常用数学运算

JASS提供了丰富的数学函数，让你可以计算角度、距离、随机数值等[^2]

#### 操作步骤

1. **第一步：理解数学函数的作* 数学函数在触发器中无处不在。比如你想让一个技击退"敌人，就需要计算移动方向和距离；想让技能只对范围内目标生效，就需要计算距离。数学函数就是这些计算的基础工具

2. **第二步：掌握三角函数** `Sin(角度)` `Cos(角度)` 用于计算正弦和余弦值，常用于计算坐标偏移。例如让单位向右移动50距离：`SetUnitX(单位, GetUnitX(单位) + 50 * Cos(角度))`[^2]

3. **第三步：学会计算距离** `SquareRoot(数` 计算平方根，结合Pow函数可以计算两点间的距离：`SquareRoot(Pow(x2-x1, 2) + Pow(y2-y1, 2))`。或者使用更简单的 `DistanceBetweenPoints(, )` 函数[^2]

4. **第四步：获取角度** `Atan2(y差 x差` 返回两点间的角度（弧度制），需要时可转换为角度：`角度 * bj_RAD_TO_DEG`

5. **第五步：生成随机* `GetRandomInt(最小 最大` 生成整数随机数，`GetRandomReal(最小 最大` 生成小数随机数。掷骰子、随机伤害都用这个[^2]

> **💡 新手提示**：角度和弧度是两回事！JASS中很多函数（如Sin、Cos）使*弧度**而非角度。转换公式：角度 = 弧度 × 57.380/π），弧度 = 角度 × 0.01745（π/180

> **⚠️ 常见错误**：新手经常忘记给除法加小数点，导致整数除法丢失精度！例如 `5 / 2` 会得2 而不2.5，正确写法应该是 `5.0 / 2.0`

### 特效与施法函

特效函数可以创建炫酷的视觉表现，让你的技能更加生动[^2]

#### 操作步骤

1. **第一步：创建特效** 使用 `AddSpecialEffect(模型路径, x坐标, y坐标)` 创建普通特效，例如 `AddSpecialEffect("Abilities\\Spells\\Human\\ThunderClap\\ThunderClapCaster.mdl", x, y)`。模型路径可以在编辑器中右键资源查找[^2]

2. **第二步：绑定特效到单* 如果想让特效跟随单位移动，使`AddSpecialEffectTarget(模型路径, 单位, 挂载`。挂载点可以"origin"（原点）head"（头部）chest"（胸部）等[^2]

3. **第三步：销毁特* 特效创建后必须手动销毁，否则会造成内存泄漏导致游戏变卡！使`DestroyEffect(特效变量)` 在适当时候移除它[^2]

4. **第四步：播放音效** `PlaySound(音效路径)` 可以播放音效文件。音效路径格式如 "Sound\\Alert.wav"，注意音效文件必须先导入到地图中[^2]

> **💡 新手提示**：模型路径中的反斜杠要双写！正确写法 `"Abilities\\Spells\\Orc\\WarDrum\\WarDrum.mdl"`，而不是单反斜

> **⚠️ 常见错误**：忘记销毁特效是最常见的性能问题！建议在触发器结尾或单位死亡时立即销毁相关特

### 小结

完成以上步骤后，你应该掌握了
- 使用Sin/Cos进行角度相关计算
- 用SquareRoot计算两点间距
- 创建、绑定、销毁特效的基本流程
- 给技能添加视觉和音效反馈

现在你可以打开World Editor，试着创建一地震技能：为它添加地面裂开的特效和轰鸣音效吧！

## 调试与常见问

本节介绍如何JASS 中查找和修复代码错误，以及新手最容易犯的典型错误。掌握这些技巧后，你就能独立解决大部分代码问题，不用一出错就到处求人了

### 代码调试方法

1. **使用 BJDebugMsg 输出信息** 这是最简单直接的调试方法。把它放在代码中间，如果游戏运行时看到了你输出的文字，说明代码执行到了这里[^2]。语法是 `call BJDebugMsg("调试信息")`，注意字符串要用英文引号

2. **逐段注释* 怀疑某段代码有问题时，在可疑代码前面加 `//` 将其临时禁用，然后测试。如果问题消失了，说明被注释掉的部分有问题。这是最笨但最有效的定位方法

3. **显示变量* 想看看某个变量当前是多少，可以用 `call BJDebugMsg("x = "+I2S(x))` 这样的形式输出。注意数字不能直接和字符串拼接，需要用 I2S 函数把整数转成字符串[^2]

4. **监听触发器执* 在触发器编辑器中，可以右键点击触发器选择"开启调试输，这样每次触发器运行时都会在编辑器里显示日志。这个方法不需要修JASS 代码

> **💡 新手提示**：调试时尽量只修改一小部分代码，然后立刻测试。不要一次性改很多地方，否则出问题都不知道是哪里的锅

> **⚠️ 常见错误**：调试信息里不要用中文引"，JASS 只认英文引号""。很多新手复制代码时会把引号变成中文的，导致脚本报错

### 新手常见错误

1. **大小写搞* JASS 严格区分大小写，`SetUnitX` `Setunitx` 是完全不同的东西。新手常把函数名首字母写成小写，或者把变量名大小写弄错

2. **漏掉分号** JASS 语句必须以分`;` 结尾，忘记加会导致整段代码编译失败。特别是复制粘贴代码时特别容易漏掉

3. **括号不匹* 每个左括`(` 必须有对应的右括`)`，嵌套多了很容易数错。用编辑器的括号高亮功能可以帮助检查

4. **字符串少了引* 所有字符串常量必须用英文双引号包起来，比如 `"Hello"`，漏掉任何一个引号都会报错

5. **使用未声明的变量** JASS 里使用变量前必须先用 `local` 声明它的类型，比`local unit u = null`，没声明就直接用会提找不到这个变

6. **数组索引越界** 如果你声明了一个大小为 10 的数`integer array arr`，它的有效索引是 0 9。访`arr[10]` 虽然不会立刻报错，但可能导致奇怪的 bug

> **

## 参考来

[^1]: [JASS Manual](https://jass.sourceforge.net/doc/) accessed 2026-05-30
[^2]: [GitHub - lep/jassdoc: Document the WarCraft 3 API](https://github.com/lep/jassdoc) accessed 2026-05-30
[^4]: [Warcraft 3 Scripting Tutorials (JASS, Lua, vJASS, TypeScript, AI, etc.)](https://www.hiveworkshop.com/forums/scripting-tutorials.280/) accessed 2026-05-30
[^5]: [Beginning JASS Tutorial Series - Hive Workshop](https://www.hiveworkshop.com/threads/beginning-jass-tutorial-series.30765/) accessed 2026-05-30
[^6]: [Jass Coding | Warcraft 3 World Editor Wiki - Fandom](https://wc3we.fandom.com/wiki/Jass_Coding) accessed 2026-05-30