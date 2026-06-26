#!/usr/bin/env bash
# codex-commit.sh - Codex 自动 commit helper (Bash 版本)
#
# 用法: 同 .ps1 版本, 但走 Bash 路径

set -e

TYPE="${1:-}"
SCOPE="${2:-}"
SUBJECT="${3:-}"
BODY="${4:-}"
DRY_RUN=false
INTERACTIVE=false

# 参数解析 (支持 -h/--help)
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=true; shift ;;
        --interactive|-i) INTERACTIVE=true; shift ;;
        -h|--help) echo "用法: $0 <type> [scope] <subject> [body]"; exit 0 ;;
        *) break ;;
    esac
done

if [ -z "$TYPE" ] || [ -z "$SUBJECT" ]; then
    echo "[codex-commit] 用法: $0 <type> [scope] <subject> [body]"
    echo "  type: feat|fix|docs|chore|refactor|style|test|perf|build|ci"
    exit 1
fi

# 切到 git 根目录
cd "$(git rev-parse --show-toplevel)"

# 1) 检查变更
if [ -z "$(git status --porcelain)" ]; then
    echo "[codex-commit] 工作区无变更, 跳过 commit"
    exit 2
fi

# 2) 敏感信息检测
WARNINGS=()
for f in $(git status --porcelain | awk '{print $2}'); do
    if [ -f "$f" ]; then
        if grep -qE '[A-Z]:\\' "$f" 2>/dev/null; then
            WARNINGS+=("$f 含 Windows 绝对路径")
        fi
        if grep -qE 'sk-[a-zA-Z0-9]{20,}|gho_[a-zA-Z0-9]{20,}|tvly-[a-zA-Z0-9]{20,}' "$f" 2>/dev/null; then
            WARNINGS+=("$f 含疑似 API key")
        fi
    fi
    case "$f" in
        */dist/*|*/node_modules/*|*/.vitepress/cache/*)
            WARNINGS+=("$f 是构建产物")
            ;;
    esac
done

if [ ${#WARNINGS[@]} -gt 0 ]; then
    echo "[codex-commit] ⚠️  检测到以下问题:"
    for w in "${WARNINGS[@]}"; do echo "  - $w"; done
    if [ "$INTERACTIVE" = "false" ]; then
        echo "[codex-commit] 停止 commit. 请先修复, 然后重试."
        exit 1
    fi
fi

# 3) 组装 message
if [ -n "$SCOPE" ]; then
    HEADER="$TYPE($SCOPE): $SUBJECT"
else
    HEADER="$TYPE: $SUBJECT"
fi

echo ""
echo "==== Commit Message ===="
echo "$HEADER"
[ -n "$BODY" ] && echo "" && echo "$BODY"
echo "========================"
echo ""

# 4) 显示变更
FILE_COUNT=$(git status --porcelain | wc -l)
SHORT_STAT=$(git diff --shortstat 2>/dev/null || echo "")
echo "==== Changes ===="
echo "  Files: $FILE_COUNT | $SHORT_STAT"
echo ""

if [ "$DRY_RUN" = "true" ]; then
    echo "[codex-commit] Dry run 模式, 不执行 commit"
    exit 0
fi

if [ "$INTERACTIVE" = "true" ]; then
    read -p "确认 commit? (y/N) " ans
    [ "$ans" != "y" ] && { echo "用户取消"; exit 1; }
fi

# 5) 执行
git add -A
if [ -n "$BODY" ]; then
    git commit -m "$HEADER" -m "$BODY"
else
    git commit -m "$HEADER"
fi

echo "[codex-commit] ✅ commit 成功"
git log --oneline -1
echo ""
echo "下一步: push 用 .codex/codex-push.sh"