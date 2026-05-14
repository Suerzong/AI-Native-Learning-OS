#!/bin/bash
# ============================================================
# Edge-AI 双向同步脚本
# 通过 GitHub 保持 Windows 本地与云服务器文件一致
#
# 用法:
#   ./tools/sync.sh              # 全仓库同步
#   ./tools/sync.sh courses      # 只同步 courses/
#   ./tools/sync.sh --dry-run    # 预览模式，不实际执行
#
# 自动运行 (远程):
#   cron: */15 * * * * /home/ubuntu/Edge-AI/tools/sync.sh
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN=false
TARGET="."

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=true; shift ;;
        *) TARGET="$1"; shift ;;
    esac
done

LOG_PREFIX="[sync] $(date '+%Y-%m-%d %H:%M:%S')"

log() { echo "$LOG_PREFIX $*"; }

# ---------- 1. 获取远端最新 ----------
log "fetching origin..."
git fetch origin main 2>&1 || { log "ERROR: fetch failed (network?)"; exit 1; }

# ---------- 2. 检查本地是否有未提交更改 ----------
if ! git diff --quiet -- "$TARGET" || ! git diff --cached --quiet -- "$TARGET" || \
   [ -n "$(git ls-files --others --exclude-standard -- "$TARGET")" ]; then

    if $DRY_RUN; then
        log "DRY-RUN: would stage and commit changes in: $TARGET"
        git status --short -- "$TARGET"
    else
        log "staging changes in: $TARGET"
        git add -A -- "$TARGET"

        if git diff --cached --quiet; then
            log "nothing to commit after staging"
        else
            log "committing..."
            git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" 2>&1 || {
                log "ERROR: commit failed"
                exit 1
            }
        fi
    fi
else
    log "no local changes in: $TARGET"
fi

# ---------- 3. 拉取远端并变基 ----------
LOCAL_AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
REMOTE_AHEAD=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)

if $DRY_RUN; then
    log "DRY-RUN: local=$LOCAL_AHEAD ahead, remote=$REMOTE_AHEAD ahead"
    if [ "$REMOTE_AHEAD" -gt 0 ]; then
        log "DRY-RUN: would pull --rebase"
    fi
    if [ "$LOCAL_AHEAD" -gt 0 ]; then
        log "DRY-RUN: would push"
    fi
else
    if [ "$REMOTE_AHEAD" -gt 0 ]; then
        log "pulling with rebase (remote ahead by $REMOTE_AHEAD)..."
        if ! git pull --rebase origin main 2>&1; then
            log "ERROR: rebase conflict — manual resolution required"
            log "  git status          # 查看冲突文件"
            log "  git mergetool       # 解决冲突"
            log "  git rebase --continue"
            log "  git rebase --abort  # 放弃本次同步"
            exit 2
        fi
    fi

    # ---------- 4. 推送 ----------
    if git rev-list --count origin/main..HEAD 2>/dev/null | grep -q '[1-9]'; then
        log "pushing to origin..."
        if ! git push origin main 2>&1; then
            log "ERROR: push failed"
            exit 1
        fi
        log "push OK"
    else
        log "nothing to push"
    fi
fi

log "sync complete"
