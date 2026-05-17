#!/bin/bash
# ============================================================
# Edge-AI 云端直连同步脚本
# 通过 SSH 在云上自动 commit+push，本地 pull，完成双向同步
#
# 用法:
#   ./tools/sync-cloud.sh status    # 查看两边状态
#   ./tools/sync-cloud.sh pull      # 云 → 本地（云上自动提交+推送，本地拉取）
#   ./tools/sync-cloud.sh push      # 本地 → 云（本地提交+推送，云上拉取）
#   ./tools/sync-cloud.sh           # 双向同步（先拉后推）
#
# 前置条件:
#   SSH 别名 tx 已配置，指向云端服务器
#   (本脚本也可以在你的 linux 云服务上运行)
# ============================================================
set -euo pipefail

SSH_HOST="${SYNC_SSH_HOST:-tx}"
REMOTE_DIR="${SYNC_REMOTE_DIR:-~/Edge-AI}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

bold()  { echo -e "${CYAN}=== $* ===${NC}"; }
ok()    { echo -e "${GREEN}$*${NC}"; }
warn()  { echo -e "${YELLOW}$*${NC}"; }
err()   { echo -e "${RED}$*${NC}"; }

usage() {
    echo "用法: $0 [status|pull|push]"
    echo ""
    echo "  status  查看本地和云端 git 状态"
    echo "  pull    云端 → 本地（拉取云端最新更改）"
    echo "  push    本地 → 云端（推送本地更改到云端）"
    echo "  (无参数) 双向同步：先拉后推"
    exit 0
}

# ---------- 远程执行 git 命令 ----------
remote_git() {
    ssh "$SSH_HOST" "cd $REMOTE_DIR && $*"
}

# ---------- 1. status ----------
cmd_status() {
    bold "本地状态 ($REPO_ROOT)"
    cd "$REPO_ROOT"
    git status --short
    echo ""
    bold "云端状态 ($SSH_HOST:$REMOTE_DIR)"
    remote_git "git status --short"
    echo ""
    bold "提交差距"
    local_head=$(git rev-parse HEAD 2>/dev/null)
    remote_head=$(remote_git "git rev-parse HEAD 2>/dev/null")
    echo "  本地 HEAD: ${local_head:0:8}"
    echo "  云端 HEAD: ${remote_head:0:8}"

    # 对比与 origin 的差距
    git fetch origin main 2>/dev/null || true
    local_ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
    local_behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
    echo "  本地 vs origin/main: 领先 $local_ahead, 落后 $local_behind"
    remote_ahead=$(remote_git "git rev-list --count origin/main..HEAD 2>/dev/null || echo 0")
    remote_behind=$(remote_git "git rev-list --count HEAD..origin/main 2>/dev/null || echo 0")
    echo "  云端 vs origin/main: 领先 $remote_ahead, 落后 $remote_behind"
}

# ---------- 2. pull (云 → 本地) ----------
cmd_pull() {
    bold "同步: 云端 → 本地"
    cd "$REPO_ROOT"

    # 2.1 先处理本地未提交更改（stash 暂存）
    echo "[1/5] 暂存本地更改..."
    local_dirty=false
    if ! git diff --quiet || ! git diff --cached --quiet || \
       [ -n "$(git ls-files --others --exclude-standard)" ]; then
        local_dirty=true
        git add -A
        if ! git diff --cached --quiet; then
            git commit -m "local-sync: $(date '+%Y-%m-%d %H:%M')" || warn "  本地提交失败"
            ok "  本地更改已提交"
        fi
    else
        echo "  本地无更改"
    fi

    # 2.2 检查云端未提交更改
    echo "[2/5] 检查云端更改..."
    cloud_dirty=$(remote_git "git diff --quiet -- . || echo dirty")
    cloud_staged=$(remote_git "git diff --cached --quiet -- . || echo staged")
    cloud_untracked=$(remote_git "test -n \"\$(git ls-files --others --exclude-standard)\" && echo untracked || echo clean")

    if [ "$cloud_dirty" = "dirty" ] || [ "$cloud_staged" = "staged" ] || [ "$cloud_untracked" = "untracked" ]; then
        echo "  云端有未提交更改，正在自动提交..."
        remote_git "git add -A && git diff --cached --quiet || git commit -m \"cloud-sync: \$(date '+%Y-%m-%d %H:%M')\"" || {
            warn "  云端提交失败或无更改"
        }
        ok "  云端更改已提交"
    else
        echo "  云端无更改"
    fi

    # 2.3 云端推送
    echo "[3/5] 云端推送到 GitHub..."
    cloud_ahead=$(remote_git "git rev-list --count origin/main..HEAD 2>/dev/null || echo 0")
    if [ "$cloud_ahead" -gt 0 ]; then
        remote_git "git push origin main" || { err "云端推送失败"; exit 1; }
        ok "  云端已推送 ($cloud_ahead 个提交)"
    else
        echo "  云端无需推送"
    fi

    # 2.4 本地拉取
    echo "[4/5] 本地拉取..."
    git fetch origin main

    local_behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
    if [ "$local_behind" -gt 0 ]; then
        if ! git pull --rebase origin main; then
            err "拉取冲突！手动解决: git mergetool && git rebase --continue"
            exit 2
        fi
        ok "  本地已拉取 ($local_behind 个提交)"
    else
        echo "  本地已是最新"
    fi

    echo "[5/5] 完成"
    ok "云端 → 本地同步完成"
}

# ---------- 3. push (本地 → 云) ----------
cmd_push() {
    bold "同步: 本地 → 云端"
    cd "$REPO_ROOT"

    # 3.1 检查本地更改
    echo "[1/4] 检查本地更改..."
    if ! git diff --quiet || ! git diff --cached --quiet || \
       [ -n "$(git ls-files --others --exclude-standard)" ]; then
        echo "  本地有未提交更改，正在自动提交..."
        git add -A
        if ! git diff --cached --quiet; then
            git commit -m "local-sync: $(date '+%Y-%m-%d %H:%M')" || {
                warn "  本地提交失败"
            }
            ok "  本地更改已提交"
        fi
    else
        echo "  本地无更改"
    fi

    # 3.2 本地推送
    echo "[2/4] 推送到 GitHub..."
    local_ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
    if [ "$local_ahead" -gt 0 ]; then
        git push origin main || { err "本地推送失败"; exit 1; }
        ok "  本地已推送 ($local_ahead 个提交)"
    else
        echo "  本地无需推送"
    fi

    # 3.3 云端拉取
    echo "[3/4] 云端拉取..."
    remote_behind=$(remote_git "git rev-list --count HEAD..origin/main 2>/dev/null || echo 0")
    if [ "$remote_behind" -gt 0 ]; then
        remote_git "git pull --rebase origin main" || {
            warn "云端拉取冲突，需手动解决"
        }
        ok "  云端已拉取 ($remote_behind 个提交)"
    else
        echo "  云端已是最新"
    fi

    echo "[4/4] 完成"
    ok "本地 → 云端同步完成"
}

# ---------- 主入口 ----------
case "${1:-sync}" in
    status)  cmd_status ;;
    pull)    cmd_pull ;;
    push)    cmd_push ;;
    sync)    cmd_pull && echo "" && cmd_push ;;
    -h|--help|help) usage ;;
    *)       echo "未知参数: $1"; usage ;;
esac
