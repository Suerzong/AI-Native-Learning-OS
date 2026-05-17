---
name: sync
description: "快速同步本地与云服务器 (tx) 的 Edge-AI 仓库。用法: /sync 双向同步, /sync pull 云→本地, /sync push 本地→云, /sync status 查看状态。"
---

# sync-cloud - Edge-AI 云端同步工具

快速同步 Windows 本地 `e:/Workspace/Edge-AI` 与云服务器 `tx:~/Edge-AI` 两个仓库。

## 原理

两边的 repo 共享同一个 GitHub 远程仓库。脚本通过 SSH 在远端自动 commit+push，本地 pull 完成同步。反之亦然。

## 命令

| 命令 | 行为 |
|------|------|
| `/sync` 或 `bash tools/sync.sh` | 双向同步：先拉云端，再推本地 |
| `/sync pull` 或 `bash tools/sync.sh pull` | 云端 → 本地：云端自动提交并推送，本地拉取 |
| `/sync push` 或 `bash tools/sync.sh push` | 本地 → 云端：本地自动提交并推送，云端拉取 |
| `/sync status` 或 `bash tools/sync.sh status` | 查看两边 git 状态和提交差距 |

## 何时使用

- 在云服务器上编辑了文件，想让本地也跟上：`/sync pull`
- 在本地编辑了文件，想让云端也跟上：`/sync push`
- 不确定两边状态：`/sync status`
- 两边都可能有改动：`/sync`（先拉后推）

## 冲突处理

如果遇到 rebase 冲突：
1. `git status` 查看冲突文件
2. 手动解决冲突
3. `git add . && git rebase --continue`
4. 或 `git rebase --abort` 放弃本次同步

## 配置

脚本中的 SSH 配置通过环境变量覆盖：

```
SYNC_SSH_HOST=tx        # SSH 别名（默认 tx）
SYNC_REMOTE_DIR=~/Edge-AI  # 云端仓库路径
```
