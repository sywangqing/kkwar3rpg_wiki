# Codex 自动 Commit 策略

> 本文件定义 Codex (基于 GPT-5 的编码代理) 在 `war3-wiki` 仓库中的自动 commit 行为。
> 适用于 Codex 的所有实例 (Codex CLI / Codex Desktop / 其他).

## 核心约定

**Codex 在每次完成有产物的任务后, 默认自动执行一次 `git add -A && git commit`, 不再询问用户.**

```
触发条件:
  ✓ 修改/新增/删除了 1 个或多个工作区文件
  ✗ 工作区完全干净 (跳过 commit)
  ✗ 仅修改了构建产物 (docs/.vitepress/dist, node_modules, etc.)
  ✗ 仅修改了临时文件 (.codex/.cache, *.tmp, .pyc)

不自动 push:
  push 永远需要用户在终端明确输入 `git push` 或调用 push helper
```

## Commit Message 规范

**格式**: Conventional Commits 1.0.0

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**Type 字典** (按本仓库历史 commit 习惯选择):

| Type | 场景 | 示例 |
| --- | --- | --- |
| `feat` | 新增功能/文档/页面 | `feat(kk-triggers): 添加 5 个新 demo 地图讲解` |
| `fix` | 修复错误/链接/构建 | `fix(sidebar): 修复 /models/ 路由 404` |
| `docs` | 纯文档内容修改 (无功能变化) | `docs(getting-started): 修正新手引导语序` |
| `chore` | 杂项: 配置、清理、脚本 | `chore(docs): 清理 Y3 整页与本地路径泄露` |
| `refactor` | 重构 (无功能变化) | `refactor(pipeline): 抽取 agent 基类` |
| `style` | 格式调整 (无逻辑变化) | `style(md): 统一标题层级` |
| `test` | 测试相关 | `test(pipeline): 添加 researcher agent 单测` |

**Scope 字典** (本仓库常见范围):

- `docs` - 文档内容
- `kk-triggers` / `triggers` / `terrain` / `scripting` / `object-editor` / `rpg-systems` / `tools` / `advanced` / `publishing` / `faq` / `tbwlm-mirror` - 各分类
- `pipeline` - AI 内容生成管线
- `sidebar` - 侧边栏配置
- `vitepress` - VitePress 配置/主题
- `ci` - GitHub Actions

**Subject 规范**:
- 中文优先 (本仓库 commit history 99% 是中文)
- 不超过 50 个汉字/字符
- 不以句号结尾
- 用动词开头: 添加/删除/修复/更新/重构/调整/合并/拆分

**Body 规范**:
- 中文, 简洁的项目符号列表
- 列出本次任务做了什么, 每行一个动作
- 重要的修复/删除单独成行
- 不超过 20 行

**Footer 规范** (可选):
- 引用相关 issue: `Refs: #123`
- 标记破坏性变更: `BREAKING CHANGE: <说明>`

## 自动识别 Type

Codex 应当根据变更内容自动判断 type, 而不是固定一个:

```
检测到删除/重命名文件 (D/R 状态)           -> chore 或 fix
检测到新增文件 (?? 状态)                  -> feat 或 docs
检测到 .vitepress/config.ts / sidebar     -> chore(vitepress) 或 fix(sidebar)
检测到 pipeline/ 目录                     -> refactor(pipeline) / feat(pipeline) / fix(pipeline)
检测到 docs/<category>/*.md 内容修改      -> docs(<category>) / fix(<category>)
检测到纯格式/换行/空白                     -> style 或 chore
```

**冲突时的优先级**:
1. `fix` > `feat` > `refactor` > `docs` > `chore` > `style` (有 fix 就用 fix)
2. 同等优先级, 选影响范围大的

## 完整示例

```
chore(docs): 清理 Y3 整页与本地路径泄露

第一期内容范围收敛到 War3 RPG 地图编辑器:
- 删除 2 个 Y3 编辑器整页
- 修复 2 处本地断链
- 移除 154 处 F:\AI\AI-machine\... 本地路径泄露

保留的 Y3 引用 (保守方案):
- 10 处营销/推荐引用
- 6 处对比性提示
- 8 处触发器代码
```

## 不自动 Commit 的场景

- 用户明确说"不要 commit" 或 "等一下" → 跳过
- 检测到敏感信息泄露 (F:\ 路径, API key, 个人邮箱等) → 修复后再 commit
- 工作区只有构建产物 (dist/ 目录) → 不 commit
- 正在执行 push/hotfix/回滚等关键操作 → 中断 commit 流程

## Push 策略 (永远手动)

**Codex 永远不自动 push.** push 是不可逆操作, 一旦 push 触发 GitHub Actions 部署, 影响生产环境.

push 流程:
1. 用户明确说 "push 远端" 或 "部署" 或 "上线"
2. Codex 先展示本次 commit 内容 (git log -1, git show --stat)
3. 用户确认 → git push
4. 用户没说 → 只在本地 commit, 不 push

## Helper 脚本

`.codex/codex-commit.ps1` (Windows) / `.codex/codex-commit.sh` (Bash) 实现了:
- 自动检测变更
- 自动建议 type/scope
- 接受 stdin 传入的 subject + body
- 自动 commit, 输出 diff 摘要

用法:
```powershell
# Codex 调用: 自动用 stdin 传入 subject 和 body
"清理 demo 页面过期链接" | .codex/codex-commit.ps1 -Type fix -Scope docs -Body "修正 12 处 404 链接"

# 手动调试: 交互式
.codex/codex-commit.ps1
```

## 自我审计

Codex 在每次自动 commit 前应自问:
1. 有没有意外的构建产物? (dist/, cache/)
2. 有没有敏感信息? (密码, key, 本地路径)
3. commit message 是否清晰描述了本次任务?
4. 是否遗漏了重要变更?

若有 1-2 项问题, 先修再 commit. 若有 3-4 项问题, 写完 message 给用户审一次.

## 修订历史

- 2026-06-26: 初始版本, 定义基本自动 commit 策略