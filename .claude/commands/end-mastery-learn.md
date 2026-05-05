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
6. 输出“结束教学总结”，并留下下一次 `/mastery-learn <课程名>` 的继续入口。
