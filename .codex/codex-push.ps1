#!/usr/bin/env pwsh
# codex-push.ps1 - Codex 推送 helper
# 注意: push 会触发 GitHub Actions 部署, 永远需要用户明确确认

[CmdletBinding()]
param(
    [switch]$Force,    # 即使在 CI 环境也 push (默认在 CI 环境拒绝)
    [switch]$NoVerify  # 跳过 pre-push hook
)

$ErrorActionPreference = "Stop"
Set-Location (git rev-parse --show-toplevel)

# 1) 检查是否在 CI
if ($env:CI -and -not $Force) {
    Write-Host "[codex-push] ❌ 拒绝在 CI 环境自动 push" -ForegroundColor Red
    Write-Host "  如需强制: pwsh .codex/codex-push.ps1 -Force" -ForegroundColor Yellow
    exit 1
}

# 2) 检查未 push 的 commits
$unpushed = git log "@{u}..HEAD" 2>$null
if (-not $unpushed) {
    Write-Host "[codex-push] 没有未 push 的 commit" -ForegroundColor DarkGray
    exit 0
}

# 3) 显示待 push 内容
$count = ($unpushed -split "`n" | Measure-Object -Line).Count
Write-Host ""
Write-Host "==== 待 push 的 commits ($count) ====" -ForegroundColor Cyan
git log "@{u}..HEAD" --oneline
Write-Host ""

# 4) 总体变更统计
$totalFiles = 0
$totalInsertions = 0
$totalDeletions = 0
git log "@{u}..HEAD" --shortstat | ForEach-Object {
    if ($_ -match '(\d+) files? changed') { $totalFiles += [int]$Matches[1] }
    if ($_ -match '(\d+) insertions?') { $totalInsertions += [int]$Matches[1] }
    if ($_ -match '(\d+) deletions?') { $totalDeletions += [int]$Matches[1] }
}
Write-Host "总计: $totalFiles files, +$totalInsertions / -$totalDeletions" -ForegroundColor Gray
Write-Host ""

# 5) 警告: 大变更或敏感信息
if ($totalFiles -gt 50) {
    Write-Host "[codex-push] ⚠️  大变更 ($totalFiles 个文件). push 后会触发 GitHub Actions 部署到 GitHub Pages." -ForegroundColor Yellow
    Write-Host "  站点: https://sywangqing.github.io/kkwar3rpg_wiki/" -ForegroundColor Yellow
}

# 6) 确认
Write-Host ""
$ans = Read-Host "确认 push 到 origin/main? (y/N)"
if ($ans -ne "y") {
    Write-Host "用户取消"
    exit 1
}

# 7) 执行
Write-Host "[codex-push] 推送中..." -ForegroundColor Cyan
if ($NoVerify) {
    git push --no-verify origin HEAD
} else {
    git push origin HEAD
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "[codex-push] ❌ push 失败" -ForegroundColor Red
    exit 1
}

Write-Host "[codex-push] ✅ push 成功" -ForegroundColor Green
Write-Host "GitHub Actions 部署已触发: https://github.com/sywangqing/kkwar3rpg_wiki/actions" -ForegroundColor DarkGray