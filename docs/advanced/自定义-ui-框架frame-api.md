---
title: 自定义 UI 框架（Frame API）
category: advanced
updated: 2026-05-21
model: openai/MiniMax-M2.7-highspeed
quality_score: 0.82
discovered_via: manual
sources:
  - https://www.hiveworkshop.com/pastebin/e23909d8468ff4942ccea268fbbcafd1.20598
  - https://warcraft.wiki.gg/wiki/UIOBJECT_Frame
---

# 自定义 UI 框架（Frame API）

## 概述

本节将带你了解 **Frame API（自定义 UI 框架）** 的基本概念。读完本节后，你会明白什么是 UI 框架，以及它能为你创建一个什么样的界面。

### 什么是 UI 框架？

简单来说，**UI 框架（Frame）** 就是你在游戏中看到的各种界面元素——按钮、血条、弹窗、进度条、甚至是输入框，都属于 UI 框架的范畴[^1]。在 RPG 地图中，你经常需要显示角色信息、菜单选项、背包系统等，这些都需要用到 UI 框架。

Frame API 是暴雪官方提供的创建自定义 UI 的接口，通过它你可以[^1]：
- 在屏幕上**显示文本**（比如伤害数字、任务提示）
- **显示图片或模型**（如技能图标、角色立绘）
- 创建**可交互的界面元素**——按钮、滑块、输入框等[^1]

> **💡 新手提示**：UI 框架和触发器（Trigger）的关系是这样的：触发器负责"逻辑"，决定"什么时候做什么事"；UI 框架负责"显示"，决定"玩家看到什么"。两者配合才能做出完整的游戏界面。

### 框架的分类

从功能上，框架可以分为两大类[^1]：

| 类型 | 说明 | 举例 |
|------|------|------|
| **显示型** | 纯展示，不响应玩家操作 | 文本框、纹理、模型 |
| **交互型** | 可以接收玩家输入 | 按钮、滑块、输入框 |

交互型框架可以通过**脚本事件**（如 OnEnter、OnLeave）来响应玩家的操作[^3]——比如鼠标悬停在按钮上时变色、点击按钮触发某个功能。

### 小结

Frame API 是创建自定义游戏界面的核心工具，它让我们能够突破魔兽默认界面的限制，为玩家打造独特的 RPG 体验。下一节，我们将学习如何打开 Frame 编辑器，并创建你的第一个简单框架。

## 参考来源

[^1]: [The Big UI-Frame Tutorial - Hive Workshop](https://www.hiveworkshop.com/pastebin/e23909d8468ff4942ccea268fbbcafd1.20598) — accessed 2026-05-21
[^3]: [Frame - Warcraft Wiki](https://warcraft.wiki.gg/wiki/UIOBJECT_Frame) — accessed 2026-05-21