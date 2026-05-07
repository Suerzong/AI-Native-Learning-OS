---
description: 结束当前 /mastery-learn 掌握学习教学会话
---

请结束当前基于 `/mastery-learn` 的掌握学习教学会话。

$ARGUMENTS

---

# 执行规则

请读取并遵循 `.github/agents/mastery-learn.agent.md` 中的“结束教学命令（全局）”。

你必须：

1. 停止继续讲新知识点。
2. 停止布置新的练习题。
3. 根据本次对话证据判断当前微目标是否达标；证据不足时写明“暂不判定达标”。
4. 更新当前课程的 `mastery-tracker.md` 和 `mistakes.md`；如课程存在学习日志文件，也记录简短日志。
5. 仅在用户确实完成可验证学习成果时，才谨慎更新 `learning-progress.md`。
6. 输出”结束教学总结”，并留下下一次 `/mastery-learn <课程名>` 的继续入口。

---

# 自动推送

文件更新完成后，执行以下 git 操作自动同步到远程仓库：

```bash
git add -A && git commit -m “$(cat <<'EOF'
[end-mastery-learn] YYYY-MM-DD 掌握学习结束：XXX

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)” && git push origin main
```

提交信息格式要求：
- 以 `[end-mastery-learn]` 开头，加上今天的日期
- 简要说明本次学习的课程、微目标和达标情况
- 示例：`[end-mastery-learn] 2026-05-07 数据结构-链表：微目标1达标(92%)`

如果 git 操作失败（如网络问题），提示用户但不要中断任务。
