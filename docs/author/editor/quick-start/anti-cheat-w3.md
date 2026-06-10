---
title: 其他编辑器反作弊概要（KKWE
category: kk-guide
updated: 2026-06-04
sources:
  - https://create.kkdzpt.com/docs/guides/UseEditor/ANTI-cheat/anti-cheat-w3
---

# 其他编辑器反作弊概要

## 商城道具全开

通过 hook 掉两个平台道具级别的 API —[DzAPI_Map_HasMallItem](https://create.kkdzpt.com/kkapidoc/#/kkapi/DzAPI_Map_HasMallItem) [DzAPI_Map_GetMapLevel](https://create.kkdzpt.com/kkapidoc/#/kkapi/DzAPI_Map_GetMapLevel)，修改检查内容，实现商城道具全开和地图等级最大化

**建议**：由HOOK 的商城为全开，作者可以自定义 1 个或多个商城道具，但设为渠道不可获得。地图逻辑在开局和自定义节点，进行该不可获得道具 Key 的状态判断，若用户拥有则视为作弊，采取对应措施，并保持定时更新此类道具

## 修改内存数据，作弊最终上传存档内

通过 CE 或者盒子注War3 客户端，修改地图运行的内容，将作弊后的结算存档数据通过 [DzAPI_Map_SaveServerValue](https://create.kkdzpt.com/kkapidoc/#/kkapi/DzAPI_Map_SaveServerValue) 上传，目前平台支500 Key

**建议**：针对核心资源，特别是货币类存档，使用独立的 int 存档槽位，并配合平台防刷限制（每局/每次/每单位时间变更上限、上传频率等）。同时配合多种存档组合：

- 只增存档记录资源消耗量 + 当前余量 判断作弊
- 只增存档记录合理获得总量，若 < 当前作弊
- table 非明文加密存
- ORPG 道具较多时，在地图逻辑中写死上

## 挂机刷日存档

玩家通过辅助工具自动启动游戏、暂停游戏，在达到作者限制的时间频率后上传存档

**建议**：该作弊目前较难从地图逻辑端排查，平台会根据每次存档分布、内容进行适当排查

## 修改单局游戏数值以便通关

修改局内数值、倍率膨胀属性，降低通关难度。修改单局生效，对存档不产生实质修改

**建议**：使[DzAPI_Map_Statistics](https://create.kkdzpt.com/kkapidoc/#/kkapi/DzAPI_Map_Statistics) 上报数据功能，设置局内节点（开局、X分钟、结算时），上报核心数据（战力、攻击力、本局总资源等），后续分析作弊可能

## 全图（Map Hack

主要出现PVP 场景中，基于修改 War3 客户端的资源、视野、迷雾等函数，属于客户端问题，无法逻辑防护

**建议**
- 通过地图逻辑判断在视野外点击敌对或不可见示例的事件，`DzAPI_Map_Statistics` 上报
- 双方阵营均设1 个不可见单位，如被敌对阵营可见则记录
- 平台会进行该类外挂样本特征检

---

> 📖 上一篇：[Y3编辑器反作弊概要](./anti-cheat-y3) | 下一篇：[编辑器的常见问题汇总](./editor-faq)
