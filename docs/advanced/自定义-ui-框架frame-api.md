---
title: 自定义 UI 框架（Frame API）
category: advanced
updated: 2026-05-09
model: openai/MiniMax-M2.7-highspeed
quality_score: 0.82
discovered_via: manual
sources:
  - https://www.hiveworkshop.com/threads/the-big-ui-frame-tutorial.335296/
  - https://www.hiveworkshop.com/threads/how-to-create-new-custom-ui-like-talents-selection.349730/
  - https://www.hiveworkshop.com/threads/ui-frames-starting-guide.318603/
  - https://www.hiveworkshop.com/threads/ui-originframes.316034/page-3
---

# 自定义 UI 框架（Frame API）

## Frame API 简介与基础概念

在本节中，你将了解什么是Frame（框架）以及Frame API的基本概念。学完本节后，你将能够理解自定义UI的核心原理，为后续创建自己的游戏界面打下基础。

### 什么是 Frame（框架）

Frame（框架）是魔兽争霸III中**界面UI的基本组成单元**。你可以把它想象成乐高积木——游戏中的按钮、对话框、角色头顶的血条、屏幕右下角的金币显示，甚至整个英雄面板，都是由一个个Frame组成的[^1]。

简单来说：
- **Frame = 界面上的一个可见元素**（比如一个按钮、一张图片、一段文字）
- **多个Frame组合在一起** = 你看到的完整游戏界面
- Frame可以嵌套（一个Frame包含另一个Frame），就像文件夹里放子文件夹一样

当你想要改变游戏默认界面、创建独特的技能选择面板或自定义设置菜单时，就需要使用Frame[^2]。

### Frame API 的作用与用途

Frame API是暴雪提供的**一组创建和操控自定义UI的命令/函数**。使用它，你可以：

| 功能 | 说明 |
|------|------|
| **创建新界面** | 从零开始制作完全自定义的UI元素 |
| **隐藏/显示** | 控制默认UI的显示与隐藏 |
| **响应点击** | 让玩家点击自定义按钮时执行触发器逻辑[^2] |
| **动态更新** | 实时修改按钮上的文字、图片等内容 |

> **💡 新手提示**：Frame API就像是给开发者发的"装修工具包"，让你能拆掉游戏默认的"精装房"，换成自己设计的"毛坯房"再装修。

### 与默认 UI 的区别

魔兽争霸III的默认UI是**固定写死在游戏程序里的**，普通触发器无法直接修改它的外观或结构。而Frame API让你能够**完全绕过默认UI的限制**，创建属于自己的界面[^1]。

两者的主要区别：

```
默认UI：暴雪设计好的 → 只能通过触发器开关/显示隐藏
Frame API：自己从头创建 → 想长什么样就什么样
```

> **⚠️ 常见错误**：新手容易把"修改默认UI"和"创建自定义Frame"搞混。直接用Frame API创建的界面和游戏默认界面是**完全独立的**，你需要在触发器中手动隐藏默认UI，否则会出现两层界面重叠的情况。

### 小结

完成本节学习后，你应该理解：

- Frame是构成游戏界面的"积木块"
- Frame API是暴雪提供的自定义UI工具集
- 自定义UI与默认UI是独立的，可以自由选择使用哪种

下一步，你将学习如何在World Editor中**实际创建一个Frame**，让我们开始动手吧！

## 准备工作与编辑器设置

本节将学习如何在魔兽争霸III编辑器中启用自定义UI功能，并配置好基本的触发器环境。学完本节后，你就能在地图中使用Frame API创建自定义界面元素（如按钮、背景框等）。

### 操作步骤

1. **第一步：打开World Editor（世界编辑器）** — 双击桌面或开始菜单中的"World Editor.exe"图标，启动魔兽争霸III地图编辑器。这是制作地图的唯一官方工具，我们所有的UI设计都要在这里完成[^2]。

2. **第二步：创建或打开地图** — 点击菜单栏的"文件"→"新建"创建一个空白地图，或"打开"已有地图。我们将在触发器编辑器中编写代码来创建自定义UI[^2]。

3. **第三步：打开触发器编辑器** — 在编辑器左侧的模块面板中，点击"触发器"（Trigger）模块。这是编写游戏逻辑的地方，自定义UI的所有代码都将在这里编写。我们使用"BlzCreateFrame"等函数来创建界面元素[^2]。

4. **第四步：创建一个新的触发器** — 右键点击触发器列表空白处，选择"新建触发器"，命名为"自定义UI初始化"（可以随意命名）。这个触发器将在地图开始时运行，创建我们需要的UI元素。

5. **第五步：编写UI初始化代码** — 双击新触发器打开编辑器，添加"游戏开始时"事件，然后添加"运行触发器"动作。在编辑框中输入JASS代码，创建第一个自定义框架：
   ```jass
   local framehandle myFrame = BlzCreateFrame("IconButtonTemplate", BlzGetFrameByName("ConsoleUIBackdrop", 0), 0, 0)
   ```
   这行代码的意思是：创建一个按钮模板，并把它放在"ConsoleUIBackdrop"这个父级框架上[^2]。

6. **第六步：为UI元素添加交互** — 继续在触发器中添加代码，让按钮可以被点击：
   ```jass
   local trigger t = CreateTrigger()
   call BlzTriggerRegisterFrameEvent(t, myFrame, FRAMEEVENT_CONTROL_CLICK)
   ```
   这样当玩家点击这个按钮时，就会触发我们定义的事件[^2]。

> **💡 新手提示**：如果你的UI元素没有显示出来，首先检查父级框架是否正确。使用"ConsoleUIBackdrop"作为父级可以让元素显示在游戏界面之上，但如果需要更灵活的层级控制，可以考虑其他父级框架[^1]。

> **⚠️ 常见错误**：新手经常忘记在触发器开头添加"本地变量"声明。Frame API需要使用本地变量（用`local`关键字），而很多教程省略了这一点。另外，务必确保触发器事件设置为"游戏开始时"，否则代码可能在游戏环境还没准备好时就执行了。

### 小结

完成以上步骤后，你的地图应该能够在游戏开始时自动创建一个自定义按钮框架。当你运行地图测试时，按钮会出现在屏幕下方区域。你可以继续在这个基础上添加更多UI元素，如背景框、文本标签等。记住，所有的自定义UI都需要通过触发器代码来创建和配置，这是魔兽争霸III地图制作的基本工作流程[^2][^3]。

## 常见 Frame 类型详解

本节将带你认识 UI 框架中最常用的几种 Frame 类型。学完本节后，你将能够区分不同 Frame 的用途，并知道如何找到游戏内置的所有 Frame 列表。

### 基础 Frame 类型（BUTTON、BACKDROP、STRING）

Frame（框架）是 UI 界面的基本构建单元，可以理解为界面上的一"块"东西。在 WarCraft 3 Reforged 中，有三种最基础的 Frame 类型必须掌握：

**1. BUTTON（按钮）**
这是最常用的交互元素——可以点击的按钮。通过 `BlzCreateFrame("ScriptDialogButton", ...)` 可以创建。在源码示例中，我们看到 `IconButtonTemplate` 就是一种预设的按钮模板[^2]。

**2. BACKDROP（背景图）**
用于显示图片或纯色背景的 Frame。它没有交互功能，纯粹负责"看起来是什么样子"。在 Big UI 教程中提到，使用 `ConsoleUIBackdrop` 作为父级可以将界面元素从 4:3 屏幕限制中解放出来[^1]。

**3. STRING（文本）**
显示文字信息的 Frame，比如标签、说明文字等。通过它你可以让界面显示玩家需要的信息。

> **💡 新手提示**：记住一个简单规律——**能点的用 BUTTON，要看的用 BACKDROP，要读的用 STRING**。

### 布局类 Frame（FRAME、GLUEBUTTON）

这两个 Frame 类型主要用于**组织和定位**其他 Frame：

**FRAME（框架）**
这是一个"容器"Frame，本身不显示任何内容，但可以包含其他 Frame。把它想象成一个透明的收纳盒，你把其他 Frame 放进去，它们就会相对于这个"盒子"来定位。在 OriginFrames 教程中，可以通过 Frame-Child API 访问框架并改变父子关系[^4]。

**GLUEBUTTON（粘合按钮）**
这是游戏界面自带的内置按钮，比如单位选择框里的按钮、物品栏按钮等。可以直接复用它们来快速创建 UI。

> **⚠️ 常见错误**：新手经常把 BUTTON 和 GLUEBUTTON 搞混。简单说——BUTTON 是你自己"创造"的按钮，GLUEBUTTON 是 WarCraft 3 "自带"的按钮模板。

### 如何查看所有可用 Frame 类型

在 World Editor 中查看所有内置 Frame 类型的方法如下：

**操作步骤**

1. **打开触发编辑器** — 在顶部菜单栏点击"触发器"按钮（或按 F4）
2. **创建或打开一个自定义代码片段** — 新建一个触发器，进入"文本 - 执行自定义代码"动作
3. **输入调试代码** — 在代码区域尝试使用 `BlzGetOriginFrame` 或查阅社区资源了解可用名称

> **💡 新手提示**：推荐查看 Hive Workshop 上的 UI Frames 起始教程，它详细介绍了如何使用 SPRITE 和模型资产（如 `WarCraftIIILogo.mdl`）来定义自定义框架[^3]。这些社区资源是学习 Frame API 的最佳途径。

### 小结

完成以上学习后，你应该已经理解了三对核心 Frame 类型的区别：**BUTTON vs STRING**（交互 vs 显示）、**BACKDROP vs FRAME**（外观 vs 容器）、以及**自定义 BUTTON vs 内置 GLUEBUTTON**（创造 vs 复用）。下一步，你可以尝试在触发器中用代码创建一个简单的按钮界面！

## 创建自定义 UI 的基本步骤

本节将教你如何使用 Frame API 在 Warcraft III 中创建自定义 UI 元素。学完本节后，你将能够创建自己的按钮、面板或信息框，并将它们显示在游戏画面上。

### 操作步骤

1. **第一步：创建 Frame（界面框架）** — 在触发器中使用 `BlzCreateFrame` 函数创建一个 UI 元素[^2]。这个函数需要一个"模板名称"作为参数，Warcraft III 内置了很多模板，比如 "IconButtonTemplate"（图标按钮模板）、"QuestButtonTemplate"（任务按钮模板）等。创建时还需要指定一个"父级 Frame"，通常使用 `BlzGetFrameByName("ConsoleUIBackdrop", 0)` 作为父级，这样你的 UI 会显示在游戏画面的最上层[^1]。

2. **第二步：设置 Frame 的位置和大小** — 创建好 Frame 后，需要使用 `BlzSetFramePosition` 设置它在屏幕上的位置（坐标原点是屏幕左下角），用 `BlzSetFrameSize` 设置宽高尺寸[^2]。你还可以用 `BlzSetFrameTexture` 来更换 Frame 的纹理图片，用 `BlzFrameSetAlpha` 调整透明度。

3. **第三步：将 Frame 添加到游戏界面** — 最后一步是让 Frame 真正显示出来。使用 `BlzFrameSetVisible(myFrame, true)` 可以让 Frame 显示在屏幕上，参数改为 `false` 则隐藏。需要注意的是，Frame 默认是隐藏的，如果不设置可见性，你就看不到它！

> **💡 新手提示**：在 Warcraft III Reforged 中，如果使用 `("ConsoleUIBackdrop",0)` 作为父级创建 Frame，可以突破 4:3 屏幕比例的限制，让 UI 在宽屏显示器上显示更灵活[^1]。但这样做会让 Frame 处于较低的层级，可能被其他界面元素遮挡。

> **⚠️ 常见错误**：新手经常忘记设置 Frame 的位置（`BlzSetFramePosition`），导致创建的 UI 元素出现在屏幕外的"虚空"中，看不见也点不到。一定要记得在创建 Frame 后立即设置它的坐标位置！

### 小结

完成以上三个步骤后，你应该能在游戏画面上看到自己创建的自定义 UI 元素。接下来你可以继续学习如何为这些 UI 添加点击事件响应，让玩家能够与你的界面进行交互。

## 事件响应与交互功能

在本节中，你将学习如何让自定义 UI 按钮能够响应玩家的点击操作。学完本节后，你的按钮就不再只是"好看"，而是真正能与玩家互动的功能组件了。

### 注册 Frame 事件监听

创建好一个 Frame（帧）后，它默认只是一个静态的显示元素。要让它响应玩家的操作，需要通过**触发器（Trigger）**来"监听"这个 Frame 上发生的事件。

#### 操作步骤

1. **创建变量保存你的 Frame** — 首先需要把你要操作的 Frame 保存到一个**变量（Variable）**中，这样后面才能引用它[^2]

2. **创建一个新的触发器** — 在触发器编辑器中新建一个空白触发器，用于存放事件响应代码[^2]

3. **注册 Frame 事件监听** — 在触发器中添加动作，使用 `BlzTriggerRegisterFrameEvent` 函数来告诉 Warcraft III："当玩家点击这个 Frame 时，执行这个触发器"[^2]
   ```
   call BlzTriggerRegisterFrameEvent(t, myFrame, FRAMEEVENT_CONTROL_CLICK)
   ```

4. **编写事件响应动作** — 在触发器中添加你想要执行的指令，比如显示提示文字、触发技能等

### 常见事件类型

不同的 `FRAMEEVENT_*` 常量代表不同类型的交互事件：

| 事件常量 | 含义 | 使用场景 |
|---------|------|---------|
| `FRAMEEVENT_CONTROL_CLICK` | 鼠标左键点击 | 按钮确认操作 |
| `FRAMEEVENT_MOUSE_ENTER` | 鼠标移入区域 | 显示提示信息 |
| `FRAMEEVENT_MOUSE_LEAVE` | 鼠标移出区域 | 隐藏提示信息 |
| `FRAMEEVENT_CHECKBOX_CHECKED` | 复选框勾选 | 开关设置选项 |

> **💡 新手提示**：如果你不确定该用哪个事件类型，可以先从 `FRAMEEVENT_CONTROL_CLICK` 开始，它是按钮最基本的事件。

### 事件回调函数编写

事件响应的核心逻辑写在你触发器的"动作"部分。当事件被触发时，这段代码就会执行。

```jass
function OnButtonClick takes nothing returns nothing
    // 在这里写：当按钮被点击时，要发生什么
    call DisplayTextToForce(bj_FORCE_PLAYER[0], "按钮被点击了！")
endfunction
```

然后在触发器初始化时，把这个函数和事件绑定：

```jass
call TriggerAddAction(t, function OnButtonClick)
```

> **⚠️ 常见错误**：很多新手忘记把"触发器动作"和"事件监听"关联起来，结果点击按钮完全没反应。请确保在触发器中同时添加了"注册 Frame 事件"和"添加触发器动作"两个步骤。

### 小结

完成以上步骤后，你应该已经掌握了：

- 如何使用变量保存自定义 Frame
- 如何创建触发器并注册 Frame 事件
- 常见的 Frame 事件类型及其用途
- 如何编写事件响应函数

现在你的 UI 按钮已经具备了基本的交互能力。你可以尝试为按钮添加更丰富的功能，比如在点击时播放音效、触发技能效果，或者显示/隐藏其他 UI 元素。

## 实战案例与最佳实践

本节将通过两个实战案例，带你从零开始创建自定义 UI 元素。学完本节后，你将能够制作简单的自定义按钮，并搭建一个完整的技能栏界面。

### 简单自定义按钮制作

1. **第一步：创建按钮框架** — 在触发器编辑器中，使用 `BlzCreateFrame` 函数创建按钮[^2]。第一个参数填写 `"IconButtonTemplate"`（按钮模板），第二个参数填写父级框架名称。推荐使用 `"ConsoleUIBackdrop"` 作为父级，这样可以避免 4:3 显示比例的限制[^1]。

2. **第二步：设置按钮位置和大小** — 使用 `BlzFrameSetAbsPoint` 或 `BlzFrameSetRelativePoint` 函数设置按钮在屏幕上的位置。位置参数包括 `FRAMEPOINT_CENTER`（中心点）、`FRAMEPOINT_TOP`（顶部）等。

3. **第三步：注册点击事件** — 创建一个触发器（Trigger），使用 `BlzTriggerRegisterFrameEvent` 函数注册按钮的点击事件[^2]。事件类型选择 `FRAMEEVENT_CONTROL_CLICK`。

> **💡 新手提示**：按钮模板名称必须完全匹配，常见模板包括 `"IconButtonTemplate"`、`"ScriptDialogButton"` 等，可以在标准 UI 文件中找到更多模板名称。

> **⚠️ 常见错误**：新手经常忘记设置按钮大小，导致按钮显示为默认尺寸。解决方法是在创建按钮后立即使用 `BlzFrameSetSize` 设置宽度和高度值。

### 完整技能栏 UI 示例

1. **第一步：创建技能栏容器** — 使用 `BlzCreateFrameByType` 函数创建一个背景框架作为技能栏容器。这个容器将包含所有技能按钮。

2. **第二步：循环创建多个技能按钮** — 使用循环语句（如 `ForForce` 或 `ForLoopA`）批量创建技能按钮。每个按钮需要设置独立的锚点和偏移量，确保它们水平或垂直排列。

3. **第三步：为每个按钮关联技能数据** — 通过 `BlzFrameSetTooltip` 函数为每个技能按钮设置鼠标悬停提示（Tooltip），显示技能名称和冷却信息。

> **💡 新手提示**：技能栏通常放置在屏幕底部中央，可以使用 `BlzFrameSetAbsPoint` 将容器锚定到 `FRAMEPOINT_BOTTOM` 位置，这样在不同分辨率下都能保持正确的显示效果。

### 常见错误与调试方法

1. **框架层级问题** — 如果自定义 UI 被游戏默认界面遮挡，可能是因为父级选择不当。使用 `"ConsoleUIBackdrop"` 作为父级会将框架放置在较低层级[^1]，这可能导致显示顺序问题。解决方法是尝试使用 `"GAME_UI"` 作为父级，并手动调整层级顺序。

2. **坐标系统错误** — 新手经常混淆绝对坐标和相对坐标。绝对坐标使用 `BlzFrameSetAbsPoint`，位置固定不变；相对坐标使用 `BlzFrameSetRelativePoint`，位置会随父级移动。建议新手先使用绝对坐标进行调试。

3. **内存泄漏风险** — 频繁创建和销毁框架会消耗内存。在地图初始化时创建所有需要的框架，并在地图关闭时才销毁它们，这是更高效的做法。

> **⚠️ 常见错误**：在调试时看不到任何 UI 元素，大多数情况下是因为框架的可见性没有设置为 `true`。请确保在创建完成后调用 `BlzFrameSetVisible(myFrame, true)`。

### 小结

完成以上实战练习后，你应该掌握了使用 Frame API 创建自定义按钮和技能栏的基本方法。记住"先创建、再定位、后交互"的三步原则，这将帮助你构建更复杂的 UI 系统。建议从简单的单个按钮开始练习，熟练后再尝试制作包含多个元素的完整界面。

## 参考来源

[^1]: [The Big UI-Frame Tutorial - Hive Workshop](https://www.hiveworkshop.com/threads/the-big-ui-frame-tutorial.335296/) — accessed 2026-05-09
[^2]: [[JASS] - how to create new custom UI like talents selection? | HIVE](https://www.hiveworkshop.com/threads/how-to-create-new-custom-ui-like-talents-selection.349730/) — accessed 2026-05-09
[^3]: [UI Frames, starting guide | HIVE](https://www.hiveworkshop.com/threads/ui-frames-starting-guide.318603/) — accessed 2026-05-09
[^4]: [UI: OriginFrames | Page 3 | HIVE](https://www.hiveworkshop.com/threads/ui-originframes.316034/page-3) — accessed 2026-05-09