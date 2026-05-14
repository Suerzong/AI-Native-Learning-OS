#!/bin/bash
# Windows 端同步脚本
# 双击运行或在 Git Bash 中执行: bash sync-local.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

echo "=== Edge-AI 本地同步 ==="
echo "仓库: $REPO_ROOT"
echo ""

# 1. 拉取远端
echo "[1/4] 获取远端更新..."
git fetch origin main
REMOTE_AHEAD=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
echo "  远端领先 $REMOTE_AHEAD 个提交"

# 2. 提交本地更改
echo "[2/4] 检查本地更改..."
if ! git diff --quiet || ! git diff --cached --quiet || \
   [ -n "$(git ls-files --others --exclude-standard)" ]; then
    git add -A
    git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" || echo "  (nothing to commit)"
    echo "  本地更改已提交"
else
    echo "  无本地更改"
fi

# 3. 拉取合并
if [ "$REMOTE_AHEAD" -gt 0 ]; then
    echo "[3/4] 拉取远端..."
    if ! git pull --rebase origin main; then
        echo ""
        echo "!!! 冲突！手动解决后运行:"
        echo "    git mergetool"
        echo "    git rebase --continue"
        echo "    git push origin main"
        read -p "按 Enter 退出..."
        exit 2
    fi
else
    echo "[3/4] 无需拉取"
fi

# 4. 推送
if git rev-list --count origin/main..HEAD | grep -q '[1-9]'; then
    echo "[4/4] 推送到 GitHub..."
    git push origin main
    echo "  推送成功"
else
    echo "[4/4] 无需推送"
fi

echo ""
echo "同步完成 — $(date '+%Y-%m-%d %H:%M:%S')"
read -p "按 Enter 退出..."
