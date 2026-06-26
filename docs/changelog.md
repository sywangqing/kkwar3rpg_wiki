# 更新日志

## 2026-06-26 09:10 UTC

本日 **维护事件** （非新文章，单独记录）：

### 第一期定位：仅做 War3

- 删除 2 个 Y3 整页：`y3-editor.md` + `anti-cheat-y3.md`（共 4881 字节）
- 修复 2 处本地断链 → KK 平台官方 URL（`anti-cheat-w3.md`、`other-editors.md`）
- 移除 154 处 `F:\AI\AI-machine\W3演示图\...` 本地路径泄露
  - 149 行 `> 📁 本地路径` 整行删除
  - 5 行替换为外链/通用描述
- 保留 24 处 Y3 营销/对比性引用（保守方案）
- 副作用：433 个 .md 文件 CRLF 换行归一化
- 提交：`2dcfa99 chore(docs): 第一期仅做 War3 - 清理 Y3 内容与本地路径泄露`

### Wiki 地址

- 线上地址：<https://sywangqing.github.io/kkwar3rpg_wiki/>
- 远端仓库：<https://github.com/sywangqing/kkwar3rpg_wiki>
- GitHub Pages 自动部署已配置（`main` 分支 push 触发 Actions）

### GitHub 知识库项目调研

- 直接对标：<https://github.com/AsyncFuncAI/deepwiki-open> (17k stars)
- 中文替代：<https://github.com/aibox22/readmeX>
- 其他参考：OpenDeepWiki、LightRAG、RAGFlow、Dify、Starlight
- 结论：deepwiki-open 技术栈最贴近需求，但中文体验与 KK 平台集成需要自研

### Codex 自动 commit 机制

- 新建 `.codex/` 目录，5 个文件：
  - [COMMIT_POLICY.md](</F:/AI/AI-superpower/war3-wiki/.codex/COMMIT_POLICY.md>) — 规则文档（触发条件 / 跳过 / 安全检查 / 退出码）
  - [codex-commit.ps1](</F:/AI/AI-superpower/war3-wiki/.codex/codex-commit.ps1>) — PowerShell commit helper（UTF-8 no BOM）
  - [codex-commit.sh](</F:/AI/AI-superpower/war3-wiki/.codex/codex-commit.sh>) — Bash 备用
  - [codex-push.ps1](</F:/AI/AI-superpower/war3-wiki/.codex/codex-push.ps1>) — push helper
  - [README.md](</F:/AI/AI-superpower/war3-wiki/.codex/README.md>) — 目录说明
- 关键设计：
  - Codex 任务结束有产物 → 自动 `git add -A && git commit`，不询问
  - 跳过条件：无变更 / 纯构建产物 / 用户明确说"不 commit"
  - **永远不自动 push**：push 不可逆，需用户明确确认
  - Commit 风格：Conventional Commits，中文 subject
  - 安全检查：检测 Windows 绝对路径（`F:\`）、API key（sk-/gho-/tvly-）、构建产物（dist/node_modules/.vitepress/cache），触发则阻塞
- 退出码：0=成功，1=失败，2=无变更
- 提交：`2ac02d9 chore(codex): add codex auto-commit helper and policy`（已 push）
- 调试记录：原脚本因 GBK 编码 + `git rev-parse` 在 `-File` 模式下失败，重写后用 Python 写文件（UTF-8 no BOM）+ `Find-GitRoot` 手动向上找 `.git`



﻿
## 2026-06-01 06:56 UTC

本次更新 **2** 篇文章：

- [玩家管理工具：黑名单、禁言、封号](docs/platform-tools/玩家管理工具黑名单禁言封号.md)
- [活动工具：节日活动与限时配置](docs/platform-tools/活动工具节日活动与限时配置.md)



## 2026-05-31 19:30 UTC

本次更新 **10** 篇文章：

- [上线前运营 checklist：预热、预告、社区建设](docs/operations/上线前运营-checklist预热预告社区建设.md)
- [上线后运营指南：数据分析、版本更新、活动策划](docs/operations/上线后运营指南数据分析版本更新活动策划.md)
- [地图增长策略：自然流量与付费推广](docs/operations/地图增长策略自然流量与付费推广.md)
- [地图商业化入门：氪金点设计与付费率优化](docs/operations/地图商业化入门氪金点设计与付费率优化.md)
- [开发者后台基础配置：地图信息与版本管理](docs/platform-tools/开发者后台基础配置地图信息与版本管理.md)
- [宝箱系统配置全流程](docs/platform-tools/宝箱系统配置全流程.md)
- [签到系统配置：每日奖励设置](docs/platform-tools/签到系统配置每日奖励设置.md)
- [任务系统配置：日常任务与成就](docs/platform-tools/任务系统配置日常任务与成就.md)
- [礼包码系统：创建与发放](docs/platform-tools/礼包码系统创建与发放.md)
- [数据分析仪表盘使用指南](docs/platform-tools/数据分析仪表盘使用指南.md)



## 2026-05-31 06:30 UTC

本次更新 **10** 篇文章：

- [Hive Workshop 资源站介绍](docs/tools/hive-workshop-资源站介绍.md)
- [MPQ 文件工具与资源导入](docs/tools/mpq-文件工具与资源导入.md)
- [多人游戏同步机制](docs/advanced/多人游戏同步机制.md)
- [存档与读档系统实现](docs/advanced/存档与读档系统实现.md)
- [自定义 UI 框架（Frame API）](docs/advanced/自定义-ui-框架frame-api.md)
- [地图性能优化指南](docs/advanced/地图性能优化指南.md)
- [反作弊机制设计](docs/advanced/反作弊机制设计.md)
- [经典 RPG 系统架构设计](docs/advanced/经典-rpg-系统架构设计.md)
- [KK 平台地图审核标准与上架要求](docs/operations/kk-平台地图审核标准与上架要求.md)
- [测试阶段完整指南：内测招募与数据收集](docs/operations/测试阶段完整指南内测招募与数据收集.md)



## 2026-05-30 19:26 UTC

本次更新 **10** 篇文章：

- [Lua API 参考（重制版）](docs/scripting/lua-api-参考重制版.md)
- [从 GUI 触发器迁移到 JASS](docs/scripting/从-gui-触发器迁移到-jass.md)
- [单位编辑器详解](docs/object-editor/单位编辑器详解.md)
- [技能编辑器与自定义技能](docs/object-editor/技能编辑器与自定义技能.md)
- [物品编辑器与物品系统](docs/object-editor/物品编辑器与物品系统.md)
- [升级编辑器](docs/object-editor/升级编辑器.md)
- [光环与增益效果编辑](docs/object-editor/光环与增益效果编辑.md)
- [YDWE 雨滴编辑器使用指南](docs/tools/ydwe-雨滴编辑器使用指南.md)
- [WE Unlimited 无限编辑器](docs/tools/we-unlimited-无限编辑器.md)
- [JASS NewGen Pack (JNGP)](docs/tools/jass-newgen-pack-jngp.md)



## 2026-05-30 06:01 UTC

本次更新 **10** 篇文章：

- [触发器事件类型详解](docs/triggers/触发器事件类型详解.md)
- [触发器条件编写](docs/triggers/触发器条件编写.md)
- [触发器动作大全](docs/triggers/触发器动作大全.md)
- [触发器变量与数据类型](docs/triggers/触发器变量与数据类型.md)
- [触发器内存泄漏处理](docs/triggers/触发器内存泄漏处理.md)
- [常用触发器模式与技巧](docs/triggers/常用触发器模式与技巧.md)
- [JASS 脚本基础入门](docs/scripting/jass-脚本基础入门.md)
- [JASS 常用函数参考](docs/scripting/jass-常用函数参考.md)
- [vJASS 进阶编程](docs/scripting/vjass-进阶编程.md)
- [Lua 脚本基础（重制版）](docs/scripting/lua-脚本基础重制版.md)



## 2026-05-29 20:37 UTC

本次更新 **10** 篇文章：

- [War3 地图编辑器安装与配置](docs/getting-started/war3-地图编辑器安装与配置.md)
- [编辑器界面功能全览](docs/getting-started/编辑器界面功能全览.md)
- [创建第一张 RPG 地图](docs/getting-started/创建第一张-rpg-地图.md)
- [地图属性与基础设置](docs/getting-started/地图属性与基础设置.md)
- [地图测试与调试方法](docs/getting-started/地图测试与调试方法.md)
- [地形编辑器基础操作](docs/terrain/地形编辑器基础操作.md)
- [地形纹理与贴图技巧](docs/terrain/地形纹理与贴图技巧.md)
- [装饰物与可破坏物](docs/terrain/装饰物与可破坏物.md)
- [高级地形技巧与优化](docs/terrain/高级地形技巧与优化.md)
- [触发器系统概述](docs/triggers/触发器系统概述.md)



## 2026-05-21 08:56 UTC

本次更新 **25** 篇文章：

- [物品编辑器与物品系统](docs/object-editor/物品编辑器与物品系统.md)
- [升级编辑器](docs/object-editor/升级编辑器.md)
- [光环与增益效果编辑](docs/object-editor/光环与增益效果编辑.md)
- [YDWE 雨滴编辑器使用指南](docs/tools/ydwe-雨滴编辑器使用指南.md)
- [WE Unlimited 无限编辑器](docs/tools/we-unlimited-无限编辑器.md)
- [JASS NewGen Pack (JNGP)](docs/tools/jass-newgen-pack-jngp.md)
- [Hive Workshop 资源站介绍](docs/tools/hive-workshop-资源站介绍.md)
- [MPQ 文件工具与资源导入](docs/tools/mpq-文件工具与资源导入.md)
- [多人游戏同步机制](docs/advanced/多人游戏同步机制.md)
- [存档与读档系统实现](docs/advanced/存档与读档系统实现.md)
- [自定义 UI 框架（Frame API）](docs/advanced/自定义-ui-框架frame-api.md)
- [地图性能优化指南](docs/advanced/地图性能优化指南.md)
- [反作弊机制设计](docs/advanced/反作弊机制设计.md)
- [经典 RPG 系统架构设计](docs/advanced/经典-rpg-系统架构设计.md)
- [触发器数组完全指南：从入门到精通](docs/triggers/触发器数组完全指南从入门到精通.md)
- [Wait动作的陷阱：为什么你的触发器不按预期执行](docs/triggers/wait动作的陷阱为什么你的触发器不按预期执行.md)
- [萌新必学的5个触发器模板：实战案例直接套用](docs/triggers/萌新必学的5个触发器模板实战案例直接套用.md)
- [单位组完全指南：从概念到实战](docs/triggers/单位组完全指南从概念到实战.md)
- [触发器循环完全指南：For和ForEach详解](docs/triggers/触发器循环完全指南for和foreach详解.md)
- [JASS入门：从T触发翻译到代码](docs/scripting/jass入门从t触发翻译到代码.md)
- [KK平台 vs 原版WE：触发器差异对比](docs/getting-started/kk平台-vs-原版we触发器差异对比.md)
- [KK平台快速帮助：运营与发行资料总览](docs/publishing/kk平台快速帮助运营与发行资料总览.md)
- [KK平台地图发行观察：你该关注哪些指标与节奏](docs/publishing/kk平台地图发行观察你该关注哪些指标与节奏.md)
- [KK用户付费行为洞察：新手作者如何定价与做转化](docs/publishing/kk用户付费行为洞察新手作者如何定价与做转化.md)
- [KK平台课程回顾：2025全年运营课程要点与新手学习路线](docs/publishing/kk平台课程回顾2025全年运营课程要点与新手学习路线.md)



## 2026-05-09 05:27 UTC

本次更新 **4** 篇文章：

- [自定义 UI 框架（Frame API）](docs/advanced/自定义-ui-框架frame-api.md)
- [地图性能优化指南](docs/advanced/地图性能优化指南.md)
- [反作弊机制设计](docs/advanced/反作弊机制设计.md)
- [经典 RPG 系统架构设计](docs/advanced/经典-rpg-系统架构设计.md)



## 2026-05-08 19:29 UTC

本次更新 **10** 篇文章：

- [物品编辑器与物品系统](docs/object-editor/物品编辑器与物品系统.md)
- [升级编辑器](docs/object-editor/升级编辑器.md)
- [光环与增益效果编辑](docs/object-editor/光环与增益效果编辑.md)
- [YDWE 雨滴编辑器使用指南](docs/tools/ydwe-雨滴编辑器使用指南.md)
- [WE Unlimited 无限编辑器](docs/tools/we-unlimited-无限编辑器.md)
- [JASS NewGen Pack (JNGP)](docs/tools/jass-newgen-pack-jngp.md)
- [Hive Workshop 资源站介绍](docs/tools/hive-workshop-资源站介绍.md)
- [MPQ 文件工具与资源导入](docs/tools/mpq-文件工具与资源导入.md)
- [多人游戏同步机制](docs/advanced/多人游戏同步机制.md)
- [存档与读档系统实现](docs/advanced/存档与读档系统实现.md)



## 2026-05-08 05:06 UTC

本次更新 **10** 篇文章：

- [触发器内存泄漏处理](docs/triggers/触发器内存泄漏处理.md)
- [常用触发器模式与技巧](docs/triggers/常用触发器模式与技巧.md)
- [JASS 脚本基础入门](docs/scripting/jass-脚本基础入门.md)
- [JASS 常用函数参考](docs/scripting/jass-常用函数参考.md)
- [vJASS 进阶编程](docs/scripting/vjass-进阶编程.md)
- [Lua 脚本基础（重制版）](docs/scripting/lua-脚本基础重制版.md)
- [Lua API 参考（重制版）](docs/scripting/lua-api-参考重制版.md)
- [从 GUI 触发器迁移到 JASS](docs/scripting/从-gui-触发器迁移到-jass.md)
- [单位编辑器详解](docs/object-editor/单位编辑器详解.md)
- [技能编辑器与自定义技能](docs/object-editor/技能编辑器与自定义技能.md)



## 2026-05-07 19:53 UTC
## 2026-05-08 12:20 UTC

本次更新 **10** 篇文章：

- [地图测试与调试方法](docs/getting-started/地图测试与调试方法.md)
- [地形编辑器基础操作](docs/terrain/地形编辑器基础操作.md)
- [地形纹理与贴图技巧](docs/terrain/地形纹理与贴图技巧.md)
- [装饰物与可破坏物](docs/terrain/装饰物与可破坏物.md)
- [高级地形技巧与优化](docs/terrain/高级地形技巧与优化.md)
- [触发器系统概述](docs/triggers/触发器系统概述.md)
- [触发器事件类型详解](docs/triggers/触发器事件类型详解.md)
- [触发器条件编写](docs/triggers/触发器条件编写.md)
- [触发器动作大全](docs/triggers/触发器动作大全.md)
- [触发器变量与数据类型](docs/triggers/触发器变量与数据类型.md)



> 以下记录由 AI 管道每次运行后自动追加，展示知识库内容更新历史。

<!-- 管道自动插入更新条目于此行下方 -->
