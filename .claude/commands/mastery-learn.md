---
description: 启动掌握学习教学会话，用法 /mastery-learn <课程名>
---

请执行基于 2 Sigma Problem 的掌握学习教学任务。

$ARGUMENTS

---


# 运行约束：避免工具误用和重复试错

- 云端默认工作区是 `/home/ubuntu/Edge-AI`，所有文件路径都按 Linux 路径处理。
- 课程定位只读 `course-index.md`；用户说 `神经网络`、`neural`、`neural-network`、`neural-networks` 时，直接使用 `courses/neural-networks/`。
- 不要为了定位课程去 Grep `profile.md`、`plan/ability-framework.md`、`.github/copilot-instructions.md`。
- 搜索中文或普通关键词时优先用固定字符串：`rg -n -F -e "神经网络" -e "neural" <已知文件或目录>`。
- `1 line of output` 不是报错；只要命令返回了相关内容，就继续教学流程。
- 同类工具调用失败后最多换一种方法重试一次，不要连续重复同一条命令。

---

# 第一步：定位课程

请读取 `course-index.md`，根据用户指定的课程名找到对应的课程路径。

如果用户未指定课程名，请列出 `course-index.md` 中所有可用课程，让用户选择。

如果课程名无法匹配 `course-index.md` 中的任何课程，请告诉用户找不到该课程，并列出现有课程列表。

---

# 第二步：加载教学引擎

定位到课程后，请按顺序读取并执行：

1. `.github/agents/mastery-learn.agent.md` — 2 Sigma 教学引擎（完整教学循环定义）
2. `courses/<课程路径>/course-config.md` — 该课程的领域知识和配置

如果 `course-config.md` 不存在，请告诉用户该课程尚未配置教学引擎支持，并列出需要创建的文件。

如果 `course-config.md` 声明 `source_mode: textbook-only`，后续教学必须只使用该课程明确列入的允许源。不得混入外部资料、工程例子、代码任务或未学过的大块内容。

---

# 第三步：开始教学循环

严格按照 `mastery-learn.prompt.md` 中定义的教学循环执行：
诊断 → 微目标拆解 → 简短教学 → 主动练习 → 即时反馈 → 错误纠正 → 复测 → 掌握判断 → 状态更新

---

# 结束教学

如果用户在 `/mastery-learn` 会话中输入以下任一内容：

- `/end-mastery-learn`
- `/结束教学`
- `结束教学`
- `今天先到这里`
- `本次教学结束`

请不要继续讲新知识点、不要继续布置新练习，而是执行 `.github/agents/mastery-learn.agent.md` 中的“结束教学命令（全局）”收尾流程。
