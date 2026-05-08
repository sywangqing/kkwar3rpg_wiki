---
title: JASS 常用函数参考
category: scripting
updated: 2026-05-08
model: openai/MiniMax-M2.7-highspeed
quality_score: 0.72
discovered_via: manual
sources:
  - https://jass.fandom.com/wiki/Functions
  - https://github.com/lep/jassdoc
  - https://jass.sourceforge.net/doc/
  - https://blog.csdn.net/weixin_32251525/article/details/143220228
  - https://www.hiveworkshop.com/threads/beginning-jass-tutorial-series.30765/
  - https://forum.wc3edit.net/viewtopic.php?t=11005
  - https://wc3we.fandom.com/wiki/Jass_Coding
  - https://www.thehelper.net/threads/is-there-a-complete-jass-function-list.54372/
---

# JASS 常用函数参考

## JASS 简介与入门基础

本节将带你认识 JASS 脚本语言，了解它是什么、为什么地图需要它，以及如何打开编辑器开始编写你的第一行代码。学完本节后，你将能够区分 JASS 和可视化触发器，并成功打开 JASS 脚本编辑器查看代码[^3]。

### 什么是 JASS 及其作用

JASS 是 Warcraft III（魔兽争霸3）内置的脚本编程语言，全称是 "JavaScript-like Assistant Scripting System"（类JavaScript辅助脚本系统）[^3]。简单来说，**JASS 就是让地图"动起来"的命令清单**。

当你想要实现以下功能时就需要用到 JASS：
- 让单位在受到攻击时自动播放特效
- 创建复杂的技能系统（如连锁闪电）
- 编写AI让电脑控制的敌人更聪明
- 管理游戏中的计时器和事件

> **💡 新手提示**：你可以把 JASS 想象成一份"任务清单"，你告诉电脑"当XX发生时，就去做YY事情"。World Editor（世界编辑器）中的**触发器编辑器**本质上就是用可视化方式帮你写 JASS 代码[^5]。

### JASS 脚本编辑器开启方法

虽然触发器编辑器可以可视化地创建逻辑，但你也可以直接查看和编写原始 JASS 代码。以下是打开方法：

1. **启动 World Editor** — 双击桌面图标或在魔兽争霸3文件夹中找到 `World Editor.exe` 打开[^3]
2. **打开或创建地图** — 点击菜单栏 "文件" → "新建" 创建一个空白地图，或用 Ctrl+O 打开现有地图
3. **进入触发器编辑器** — 在工具栏找到并点击 **"触发器编辑器"**（也叫"触发编辑器"），快捷键是 F4
4. **查看 JASS 代码** — 在触发器列表中选中任意触发器，双击右侧的"动作"区域，你将看到对应的 JASS 代码窗口[^5]

> **⚠️ 常见错误**：新手经常把触发器编辑器和 JASS 编辑器搞混。触发器编辑器是可视化界面，而 JASS 代码显示在代码窗口中。如果你想纯手写 JASS，需要在地图脚本中编写（右键点击"地图脚本"选择"编辑"）[^7]。

### JASS 基本语法结构

JASS 的代码由几个核心元素组成，理解它们是入门的关键[^4]：

**1. 函数（Function）**
函数是 JASS 的基本执行单元，每段代码都写在函数内部：
```jass
function MyFunction takes nothing returns nothing
    // 你的代码写在这里
endfunction
```
- `takes nothing` 表示这个函数不需要任何参数
- `returns nothing` 表示函数执行完不返回任何值

**2. 变量（Variable）**
变量用于存储数据，就像一个带名字的盒子：
```jass
local integer myScore = 0    // 整数变量
local unit hero               // 单位变量
local boolean isAlive = true  // 布尔变量（真假）
```

**3. 常用关键字**
- `call` — 调用一个函数：`call DisplayTextToPlayer(...)`
- `set` — 给变量赋值：`set myScore = 100`
- `if/then/else` — 条件判断
- `loop/endloop` — 循环执行[^5]

> **💡 新手提示**：JASS 对大小写敏感！`Set` 和 `set` 是不同的。写代码时务必保持大小写一致，否则运行时会报错[^4]。

### 小结

完成以上内容后，你应该已经：
- ✅ 理解了 JASS 是用于控制地图逻辑的脚本语言
- ✅ 学会了如何在 World Editor 中打开触发器编辑器并查看 JASS 代码
- ✅ 认识了函数、变量、关键字等基本语法元素

这些知识将为你后续学习更复杂的 JASS 编程打下坚实基础！

## 常用输出与调试函数

本节将带你认识三个最常用的输出与调试函数：`BJDebugMsg`、`DisplayTextToPlayer` 和 `SendSysMessage`。学完本节后，你将能够在游戏中显示文字信息，随时检查变量值是否正确，再也不用担心写完触发器后不知道程序运行到哪一步了。

---

### BJDebugMsg 调试消息输出

**BJDebugMsg** 是暴雪封装好的BJ函数（可以直接理解为"简化版函数"），用于向所有玩家同时显示一行调试信息[^1]。

**语法格式：**
```jass
call BJDebugMsg(消息内容)
```

**适用场景：**
- 调试时想知道某段代码是否被执行
- 检查某个变量的当前值
- 追踪触发器的执行流程

> **💡 新手提示**：BJDebugMsg 显示的信息只有游戏主持人（单人模式）或所有玩家能看到，但**不会保存在任何日志文件里**，关闭游戏后这些消息就消失了。如果你想保存调试记录，建议同时使用其他方式记录。

---

### DisplayTextToPlayer 玩家信息显示

**DisplayTextToPlayer** 是原生函数（Native Function），比 BJ 函数更底层、功能更精确[^2]。它可以将消息发送给**指定的一位玩家**，并显示在屏幕特定位置。

**语法格式：**
```jass
call DisplayTextToPlayer(玩家变量, X坐标, Y坐标, 消息内容)
```

**参数说明：**
| 参数 | 含义 | 示例值 |
|------|------|--------|
| 玩家变量 | 要接收消息的玩家编号（0-11） | Player(0) |
| X坐标 | 屏幕上横向位置（0.0-1.0） | 0.5 |
| Y坐标 | 屏幕上纵向位置（0.0-1.0） | 0.5 |
| 消息内容 | 要显示的字符串 | "游戏开始！" |

**适用场景：**
- 只让某个特定玩家看到提示（如剧情对话）
- 为不同玩家显示不同信息
- 显示UI提示文本

> **⚠️ 常见错误**：新手容易把 X 和 Y 坐标写成整数（如 500、300），这会导致消息**无法显示或显示位置异常**。记住，坐标值范围是 **0.0 到 1.0**，0.5 代表屏幕正中央。

---

### SendSysMessage 系统消息函数

**SendSysMessage** 通常是自定义封装的消息函数，功能类似 `DisplayTextToPlayer`，但更简洁——只需指定玩家和消息内容，位置固定为屏幕左下方系统消息区域。

**语法格式（取决于地图作者的封装方式）：**
```jass
call SendSysMessage(玩家变量, 消息内容)
```

**与 BJDebugMsg 的区别：**
| 对比项 | BJDebugMsg | SendSysMessage |
|--------|------------|----------------|
| 显示对象 | 所有玩家 | 指定玩家 |
| 显示位置 | 屏幕中央 | 系统消息区（左下） |
| 是否原生 | BJ封装函数 | 取决于地图实现 |

> **💡 新手提示**：如果地图没有预先定义 SendSysMessage，你可以直接使用 `DisplayTextToPlayer` 并把坐标设为左下角（如 X=0.01, Y=0.01）来实现类似效果。

---

### 小结

掌握这三个函数后，你现在可以：

- ✅ 使用 `BJDebugMsg` 快速输出调试信息，验证代码是否运行
- ✅ 使用 `DisplayTextToPlayer` 精准控制哪位玩家、在哪里看到什么消息
- ✅ 使用或自定义 `SendSysMessage` 实现统一的系统提示风格

**下一步建议**：试着在一个简单触发器中加入 `BJDebugMsg("触发器已执行！")`，运行地图后观察消息是否出现。如果能正常显示，说明你已成功迈出 JASS 调试的第一步！

## 单位创建与操作函数

本节将教你如何在JASS中**创建游戏单位**和**控制单位移动**，这是制作RPG地图最基础、也是最常用的技能。学完本节后，你就能让怪物出现、让NPC移动到指定位置了。

### 操作步骤

1. **第一步：理解单位创建函数** — 在JASS中，`CreateUnit` 是最基础的单位创建函数。它的基本语法是：
   ```jass
   CreateUnit(id, unitid, x, y, face)
   ```
   - `id` 是玩家编号（0-11，对应红、绿、蓝等12个玩家）
   - `unitid` 是单位类型ID（如 "hpea" 代表农民）
   - `x` 和 `y` 是坐标位置
   - `face` 是单位朝向角度（0-360度）[^1][^2]

2. **第二步：使用 CreateUnitAtLoc 创建单位** — 如果你想在**区域（Location）**而非精确坐标处创建单位，可以使用 `CreateUnitAtLoc`。这个函数在制作刷怪点时特别有用，因为它会自动把单位放置在区域中心[^2]：
   ```jass
   CreateUnitAtLoc(id, unitid, loc, face)
   ```

3. **第三步：移动单位到指定位置** — 创建单位后，你需要移动它们。使用 `SetUnitPosition` 可以瞬间把单位传送到精确坐标[^2]：
   ```jass
   call SetUnitPosition(unitHandle, x, y)
   ```
   或者分别设置X和Y坐标：
   ```jass
   call SetUnitX(unitHandle, x)
   call SetUnitY(unitHandle, y)
   ```

4. **第四步：修改单位属性** — 创建单位后，你可以修改它的属性。常用函数包括：
   - `SetUnitState` — 修改生命值、魔法值等
   - `SetUnitMoveSpeed` — 修改移动速度
   - `SetUnitFacing` — 修改朝向角度[^2][^4]

> **💡 新手提示**：创建单位时记得把返回值（单位句柄）存到变量里！否则你创建了单位却无法控制它，就像凭空消失了。

> **⚠️ 常见错误**：新手经常把 `CreateUnit` 和 `CreateUnitAtLoc` 搞混。前者需要精确的X/Y坐标，后者只需要一个区域对象（用 `Location` 函数创建）。搞混会导致单位出现在奇怪的位置或报错。

### 小结

完成以上步骤后，你应该掌握：
- 如何使用 `CreateUnit` 和 `CreateUnitAtLoc` 在地图上生成单位
- 如何使用 `SetUnitPosition` 系列函数移动单位
- 如何用变量保存和操作单位句柄

建议动手练习：尝试创建一个"刷怪触发器"，当玩家进入某个区域时，自动在附近生成一只怪物。

## 触发器事件注册函数

本节将介绍三个在 JASS 中常用的触发器事件注册函数，它们分别是监听变量变化、设置定时器、以及手动执行触发器的事件[^2]。学完本节后，你将能够在地图中实现"当某个变量改变时自动触发"、"每隔一段时间执行某段代码"等常见功能。

### 操作步骤

1. **TriggerRegisterVariableEvent — 监听变量变化**  
   这个函数用于"注册"一个事件，当指定变量的值发生变化时自动触发[^2]。语法为：  
   ```jass
   TriggerRegisterVariableEvent(trig, varName, opcode, limitval)
   ```  
   其中 `varName` 是变量名（字符串格式），`opcode`是比较方式（如 `LESS THAN`、`EQUAL` 等），`limitval`是比较的数值。例如监听整数变量 `udg_Score` 是否大于 100：  
   ```jass
   call TriggerRegisterVariableEvent(gg_trg_CheckScore, "udg_Score", GREATER THAN, 100)
   ```

2. **TriggerRegisterTimerEvent — 设置定时器事件**  
   这个函数可以让触发器在固定时间间隔后自动执行[^2]。语法为：  
   ```jass
   TriggerRegisterTimerEvent(trig, timeout, periodic)
   ```  
   参数 `timeout` 是时间（秒），`periodic` 为 `true` 时表示重复执行，`false` 则只执行一次。例如让触发器每 5 秒执行一次：  
   ```jass
   call TriggerRegisterTimerEvent(gg_trg_TimerLoop, 5.0, true)
   ```

3. **TriggerExecute — 手动执行触发器**  
   这个函数可以让你在代码中主动"调用"另一个触发器立即执行[^2]。语法为：  
   ```jass
   TriggerExecute(trig)
   ```  
   注意：TriggerExecute 会忽略触发器的条件（conditions），直接执行动作。

> **⚠️ 常见错误**：新手经常混淆 `TriggerRegisterTimerEvent` 和 `TriggerSleepAction`。前者是注册事件（在触发器编辑器中使用），后者是代码中延时（暂停当前函数执行）。在 JASS 代码中请使用 `TriggerSleepAction(1.0)` 来延时，而不是注册新的定时器事件。

### 小结

完成以上步骤后，你已经掌握了三种触发器事件注册的方法：监听变量变化、设置定时器、以及手动执行触发器。建议先在地图中创建一个简单的计时触发器，验证功能正常后再进行更复杂的逻辑开发。

## 数学运算与逻辑函数

本节将带你认识JASS中最常用的数学计算和逻辑判断工具。学完本节后，你就能在触发器中使用数学公式计算伤害值、判断单位距离等核心功能——这是制作技能系统和游戏逻辑的基础！

---

### 1. 数学运算函数

#### 第一步：了解数学函数的分类

JASS的数学函数主要分为**原生函数**（Native）和**BJ辅助函数**两类[^1]：

- **原生函数**是JASS语言自带的底层函数，名称通常较短，如 `Sin(x)`、`Cos(x)`
- **BJ辅助函数**是暴雪封装的"友好版本"，名称带有 `BJ` 后缀，如 `SinBJ(x)`、`CosBJ(x)`，会自动处理一些边界情况[^2]

#### 第二步：认识常用数学函数

以下是新手最常用的数学函数：

| 函数 | 作用 | 示例 |
|------|------|------|
| `Sin(x)` / `SinBJ(x)` | 计算正弦值 | `SetAngle = Sin(30 * bj_DEGTORAD)` |
| `Cos(x)` / `CosBJ(x)` | 计算余弦值 | `SetAngle = Cos(60 * bj_DEGTORAD)` |
| `SquareRoot(x)` | 计算平方根 | `SetDist = SquareRoot(dx*dx + dy*dy)` |
| `Pow(base, exp)` | 计算幂次方 | `SetValue = Pow(2, 8)` |
| `Deg2Rad` / `Rad2Deg` | 角度与弧度转换 | `SetRad = degrees * bj_DEGTORAD` |

> **💡 新手提示**：`bj_DEGTORAD` 是一个常数（约等于 0.01745），用于将角度转换为弧度。在JASS中，三角函数使用的是弧度制，不是角度制！这是新手最容易搞错的地方。

#### 第三步：掌握整数与浮点数转换

JASS区分**整数**（integer）和**实数**（real），需要经常相互转换[^4]：

```
I2R(i)    // 将整数转换为实数
R2I(r)    // 将实数转换为整数（会取整）
```

> **⚠️ 常见错误**：直接用整数除以整数会丢失小数部分。例如 `5 / 2` 的结果是 `2`，而不是 `2.5`。正确做法是 `I2R(5) / I2R(2)` 或 `5.0 / 2.0`。

---

### 2. 条件判断与比较函数

#### 第一步：理解比较运算符

JASS中使用以下比较运算符[^3]：

| 运算符 | 含义 |
|--------|------|
| `==` | 等于 |
| `!=` | 不等于 |
| `<` | 小于 |
| `>` | 大于 |
| `<=` | 小于等于 |
| `>=` | 大于等于 |

#### 第二步：组合多个条件

当需要同时满足多个条件时，使用逻辑函数[^3]：

```
and(条件1, 条件2)  // 两个条件都满足才返回 true
or(条件1, 条件2)   // 任一条件满足就返回 true
not(条件)          // 取反，true变false，false变true
```

**示例**：判断单位是否在范围内且生命值大于50
```jass
if and( DistanceBetweenUnits(u1, u2) < 300, GetUnitLifePercent(u1) > 50 ) then
    // 执行技能效果
endif
```

> **💡 新手提示**：比较函数的返回值是**布尔值**（boolean），只有 `true`（真）或 `false`（假）两种情况。这和数字不一样！

---

### 3. 在触发器中实际使用

#### 第一步：打开触发编辑器

1. 在World Editor中，点击顶部菜单 **「触发器编辑器」**（或按 F4）
2. 双击已有触发器或新建一个触发器

#### 第二步：编写数学运算动作

在触发器的**动作**中添加：
- **数学运算** → **设置实数变量** → 选择变量，设置为 `SquareRoot(100)` 的结果

> **⚠️ 常见错误**：忘记给变量初始化！在使用数学运算前，确保变量已经被声明和赋值，否则可能得到错误结果或导致游戏崩溃。

---

### 小结

完成本节学习后，你应该：
- ✅ 理解原生函数与BJ辅助函数的区别
- ✅ 能在触发器中使用 `Sin`、`Cos`、`SquareRoot` 等数学函数
- ✅ 掌握整数与浮点数的转换方法
- ✅ 学会用 `and`、`or`、`not` 组合多个条件判断

这些函数虽然简单，但组合起来就能实现技能伤害计算、距离判断等核心玩法。继续学习下一节《字符串与文本函数》，让你的地图更丰富！

## 新手常见问题与调试技巧

本节将帮助你识别JASS脚本中最容易犯的错误，学会查看错误信息并修复问题，了解一些基本的代码优化技巧。学完本节后，你将能够独立排查常见的脚本问题，让地图运行得更稳定流畅。

### 新手常犯的错误汇总

1. **语法错误：缺少括号或分号** — JASS对语法要求严格，每个函数调用后面必须加分号`;`，每个括号必须成对出现[^3]。例如`call BJDebugMsg("hello"`会报错，正确的是`call BJDebugMsg("hello")`。

2. **变量未声明就使用** — 在JASS中，所有变量必须先声明（定义类型）才能使用[^4]。新手常忘记写`local integer i`就直接写`set i = 0`，这会导致"未定义的变量"错误。

3. **变量类型不匹配** — 比如把一个整数赋值给字符串变量[^7]。`set myString = 100`会报错，因为类型不同。正确做法是`set myString = I2S(100)`将整数转为字符串。

4. **大小写错误** — JASS区分大小写，`Function`和`function`是不同的。新手经常写成`Function main()`而实际上应该是`function main()`。

> **⚠️ 常见错误**：很多新手在复制别人的代码时会忘记修改函数名，导致"函数已存在"或"函数未找到"的错误。养成每复制一段代码就检查函数名的习惯。

### JASS脚本调试方法

1. **使用BJDebugMsg输出信息** — 这是最简单有效的调试方法[^1]。在怀疑出错的地方加入`call BJDebugMsg("变量x的值="+R2S(x))`，运行地图时屏幕上方会显示实际值，帮助你判断程序执行到了哪一步。

2. **查看触发器日志** — 当地图崩溃或出错时，回到World Editor，按F12或通过"场景 > 触发器日志"查看详细错误报告[^2]。错误信息通常会告诉你出错的函数名和行号。

3. **逐行注释法** — 把可疑代码用`//`注释掉，然后逐行取消注释，观察地图何时出现问题。这种"二分查找"的方法特别适合定位复杂问题。

4. **检查函数参数数量** — 调用函数时，参数个数和类型必须完全匹配[^8]。如果函数定义是`takes integer a, real b returns nothing`，那么调用时必须提供这两个参数，顺序也不能错。

> **💡 新手提示**：养成写注释的习惯！在每段重要代码前用`//`加上中文说明，比如`// 判断玩家是否死亡`。这样自己和别人都更容易理解代码逻辑，出错时也能快速定位。

### 脚本优化与运行效率

1. **避免在循环中频繁创建单位组** — 每帧或每次触发都创建新单位组会大量消耗内存（内存泄漏）[^5]。正确做法是预先声明一个全局单位组，每次用完调用`call DestroyGroup(g)`释放，或者使用`ClearNativeGlueHandle`等函数。

2. **减少不必要的字符串操作** — 字符串拼接很消耗性能[^4]。如果需要在循环中频繁拼接字符串，先在循环外定义好，用`SetUnitX`等函数代替字符串传递数据。

3. **使用局部变量代替全局变量** — 全局变量在多人游戏中可能引发同步问题（Desync）[^6]。尽量在函数内部使用`local`声明的局部变量，只在必要时使用全局变量。

4. **合理使用计时器** — 不要创建太多同时运行的计时器，它们会占用系统资源。将可以合并的逻辑合并到一个计时器中处理。

> **💡 新手提示**：优化代码时不要"过度优化"。先把功能做对、做出效果，等地图能正常运行后再考虑性能问题。很多时候可读性比微小的性能提升更重要。

### 小结

完成以上学习后，你应该能够：
- 识别并修复JASS中最常见的语法错误
- 使用BJDebugMsg和触发器日志定位问题代码
- 养成注释和检查函数参数的好习惯
- 了解基本的内存管理和性能优化原则

建议立刻打开World Editor，尝试写一个简单的JASS脚本，故意犯几个常见错误（如漏写分号、变量类型不匹配），然后观察错误信息长什么样——这比任何教程都更直观！

## 参考来源

[^1]: [Functions - Warcraft 3 JASS Wiki](https://jass.fandom.com/wiki/Functions) — accessed 2026-05-08
[^2]: [GitHub - lep/jassdoc: Document the WarCraft 3 API](https://github.com/lep/jassdoc) — accessed 2026-05-08
[^3]: [JASS Manual](https://jass.sourceforge.net/doc/) — accessed 2026-05-08
[^4]: [《魔兽3的Jass语言参考手册》：地图编辑与脚本开发指南-CSDN博客](https://blog.csdn.net/weixin_32251525/article/details/143220228) — accessed 2026-05-08
[^5]: [Beginning JASS Tutorial Series - HIVE](https://www.hiveworkshop.com/threads/beginning-jass-tutorial-series.30765/) — accessed 2026-05-08
[^6]: [[JASS Tutorials] - wc3edit.net](https://forum.wc3edit.net/viewtopic.php?t=11005) — accessed 2026-05-08
[^7]: [Jass Coding | Warcraft 3 World Editor Wiki | Fandom](https://wc3we.fandom.com/wiki/Jass_Coding) — accessed 2026-05-08
[^8]: [Is There A Complete JASS Function List? | The Helper](https://www.thehelper.net/threads/is-there-a-complete-jass-function-list.54372/) — accessed 2026-05-08