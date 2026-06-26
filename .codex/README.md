# .codex/

Codex (基于 GPT-5 的编码代理) 在 `war3-wiki` 项目里的辅助工具与规则。

## 文件清单

| 文件 | 用途 |
| --- | --- |
| `COMMIT_POLICY.md` | Codex 自动 commit 行为规范 (Conventional Commits, type/scope 字典) |
| `codex-commit.ps1` | PowerShell commit helper (Windows 主用) |
| `codex-commit.sh` | Bash commit helper (Linux/macOS / WSL) |
| `codex-push.ps1` | 推送 helper (永远需要用户明确确认, 拒绝在 CI 环境自动 push) |

## 使用约定

Codex 在每次完成有产物的任务后, 默认自动执行:
```
pwsh .codex/codex-commit.ps1 -Type chore -Scope docs -Subject "..." -Body "..."
```

push 永远手动:
```
pwsh .codex/codex-push.ps1
```

## 安全

`codex-commit.ps1` 会自动检测:
- Windows 绝对路径泄露 (如 `F:\...`)
- 疑似 API key (sk-, gho-, tvly- 前缀)
- 误提交构建产物 (`dist/`, `node_modules/`, `.vitepress/cache/`)

如有任一风险, commit 自动中止, 等待修复.