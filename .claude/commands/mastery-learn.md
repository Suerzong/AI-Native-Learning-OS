---
description: 启动掌握学习教学会话，用法 /mastery-learn <课程名>
---

请执行基于 2 Sigma Problem 的掌握学习教学任务。

$ARGUMENTS

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

---

# 第三步：开始教学循环

严格按照 `mastery-learn.prompt.md` 中定义的教学循环执行：
诊断 → 微目标拆解 → 简短教学 → 主动练习 → 即时反馈 → 错误纠正 → 复测 → 掌握判断 → 状态更新
