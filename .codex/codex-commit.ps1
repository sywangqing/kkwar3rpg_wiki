# codex-commit.ps1 - Codex automatic commit helper (Windows)
#
# Usage:
#   powershell .codex/codex-commit.ps1 -Type chore -Scope docs -Subject "..." -Body "..."
#   powershell .codex/codex-commit.ps1 -Type feat -Subject "..." -DryRun
#   powershell .codex/codex-commit.ps1 -Interactive
#
# Exit codes: 0=success, 1=failure, 2=no changes

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("feat","fix","docs","chore","refactor","style","test","perf","build","ci")]
    [string]$Type,
    [string]$Scope = "",
    [Parameter(Mandatory=$true)]
    [string]$Subject,
    [string]$Body = "",
    [switch]$Interactive,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# Find git root (walk up from script directory looking for .git)
function Find-GitRoot {
    param([string]$StartDir)
    $current = (Resolve-Path $StartDir).Path
    while ($true) {
        if (Test-Path (Join-Path $current ".git")) {
            return $current
        }
        $parent = Split-Path $current -Parent
        if ($parent -eq $null -or $parent -eq $current) { break }
        $current = $parent
    }
    throw "Cannot find .git directory. Run this script inside a git repository."
}

try {
    $gitRoot = Find-GitRoot -StartDir $PSScriptRoot
} catch {
    Write-Host "[codex-commit] Error: $_" -ForegroundColor Red
    exit 1
}

Set-Location $gitRoot
Write-Host "[codex-commit] git root: $gitRoot" -ForegroundColor DarkGray

# 1) Check for changes
$statusOutput = git status --porcelain
$hasChanges = -not [string]::IsNullOrWhiteSpace($statusOutput)

if (-not $hasChanges) {
    Write-Host "[codex-commit] No changes in working tree, skipping commit" -ForegroundColor DarkGray
    exit 2
}

# 2) Detect sensitive information
$utf8Enc = [System.Text.UTF8Encoding]::new($false, $true)
$staged = git diff --cached --name-only
$modified = git diff --name-only
$untracked = git ls-files --others --exclude-standard
$allFiles = @($staged) + @($modified) + @($untracked) | Where-Object { $_ }

$warnings = @()
foreach ($f in $allFiles) {
    $isLeaf = Test-Path $f -PathType Leaf
    if ($isLeaf -and $f -notmatch '^\.codex/') {
        $filePath = (Resolve-Path $f).Path
        $content = [System.IO.File]::ReadAllText($filePath, $utf8Enc)
        if ($content -cmatch '[A-Z]:\\[A-Za-z]') {
            $warnings += "$f contains Windows absolute path"
        }
        if ($content -match 'sk-[a-zA-Z0-9]{20,}|gho_[a-zA-Z0-9]{20,}|tvly-[a-zA-Z0-9]{20,}') {
            $warnings += "$f contains suspected API key"
        }
    }
    if ($f -match '/dist/|/node_modules/|\.vitepress/cache/|\.vitepress/dist/') {
        $warnings += "$f is build artifact (consider .gitignore)"
    }
}

if ($warnings.Count -gt 0) {
    Write-Host "[codex-commit] WARNING - detected issues:" -ForegroundColor Yellow
    foreach ($w in $warnings) { Write-Host "  - $w" -ForegroundColor Yellow }
    if (-not $Interactive) {
        Write-Host "[codex-commit] Stopping commit. Please fix and retry." -ForegroundColor Red
        exit 1
    }
    $ans = Read-Host "Continue commit? (y/N)"
    if ($ans -ne "y") { Write-Host "User cancelled"; exit 1 }
}

# 3) Assemble message
if ($Scope) {
    $header = "{0}({1}): {2}" -f $Type, $Scope, $Subject
} else {
    $header = "{0}: {1}" -f $Type, $Subject
}

Write-Host ""
Write-Host "==== Commit Message ====" -ForegroundColor Cyan
Write-Host $header
if ($Body) { Write-Host ""; Write-Host $Body }
Write-Host "========================" -ForegroundColor Cyan
Write-Host ""

# 4) Change stats
$statusLines = $statusOutput -split "`n" | Where-Object { $_.Trim() -ne "" }
$fileCount = $statusLines.Count
$diffStat = git diff --shortstat 2>$null
Write-Host "==== Changes ====" -ForegroundColor Cyan
Write-Host ("  Files: {0} | {1}" -f $fileCount, $diffStat) -ForegroundColor Gray
Write-Host ""

if ($DryRun) {
    Write-Host "[codex-commit] Dry run mode, not committing" -ForegroundColor Yellow
    exit 0
}

if ($Interactive) {
    $ans = Read-Host "Confirm commit? (y/N)"
    if ($ans -ne "y") { Write-Host "User cancelled"; exit 1 }
}

# 5) Execute
git add -A
if ($Body) {
    $result = git commit -m $header -m $Body 2>&1
} else {
    $result = git commit -m $header 2>&1
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "[codex-commit] commit FAILED:" -ForegroundColor Red
    Write-Host $result -ForegroundColor Red
    exit 1
}

Write-Host "[codex-commit] commit OK" -ForegroundColor Green
git log --oneline -1
Write-Host ""
Write-Host "Next: push with .codex/codex-push.ps1" -ForegroundColor DarkGray
