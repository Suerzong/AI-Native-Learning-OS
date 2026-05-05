For user  :  ti-study-session.prompt.md  作用：TI 板子一对一教学会话，讲解知识点、出题、批改。

---
name: ti-study-session
description: TI 板子一对一教学会话，讲解知识点、出题、批改、记录错题和掌握度
agent: agent
---

请执行 TI 板子一对一教学任务。

$ARGUMENTS

---

# 教学目标

帮助用户系统掌握 TI 开发板的基础概念、开发环境、外设使用、代码实验、调试方法和综合项目能力。

---

# 加载教学引擎

按顺序读取：

1. `.github/agents/mastery-learn.agent.md` — 2 Sigma 教学引擎
2. `courses/ti-board/course-config.md` — TI 板子课程配置

---

# 教学循环

严格按照 `mastery-learn.agent.md` 中定义的 8 步循环执行：
诊断 → 微目标 → 知识教学 → 任务 → 即时反馈 → 迁移测试 → 状态更新 → 推进/补救

---

# 文件权限

**允许写入：**
- `courses/ti-board/mastery-tracker.md`
- `courses/ti-board/mistakes.md`
- `courses/ti-board/daily-tests.md`
- `courses/ti-board/learner/state.md`
- `plan/daily-plan.md`

**谨慎写入：**
- `learning-progress.md`

**不要写入：**
- `course-config.md`
- `.github/` 下的配置文件
