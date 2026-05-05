For user  :  ti-exam.prompt.md  作用：TI 板子阶段综合考试，考察体系理解，决定阶段是否通过。

---
name: ti-exam
description: TI 板子阶段综合考试，考察体系理解，记录结果并决定阶段是否通过
agent: agent
---

请执行 TI 板子阶段综合考试任务。

$ARGUMENTS

---

# 必须先读取的文件

- `.github/agents/mastery-learn.agent.md` — 教学引擎（推进规则）
- `courses/ti-board/course-config.md` — 知识图谱和阶段划分
- `courses/ti-board/mastery-tracker.md` — 当前掌握度
- `courses/ti-board/daily-tests.md` — 历史测试记录
- `courses/ti-board/mistakes.md` — 历史错误点
- `courses/ti-board/exercises.md`
- `plan/daily-plan.md`

---

# 考试前检查

1. 确认当前阶段的所有知识点每日测试已通过
2. 查看 `mastery-tracker.md`，确认所有知识点正确率 >= 80%
3. 如果有知识点未通过测试，不允许进行阶段考试

---

# 试卷生成规则

1. 综合考察该阶段所有知识点
2. 重点考察 `mistakes.md` 中的薄弱环节
3. 题目类型：概念理解 + 流程/配置 + 代码编写 + 调试排查
4. 总分 100 分
5. 考试结果记录到练习相关文件中

---

# 评分标准

- 90 分以上：优秀，阶段稳固通过
- 80-89 分：良好，通过
- 60-79 分：部分通过，需补课后再考
- 60 分以下：未通过，需系统重新学习

---

# 记录要求

- 更新 `mastery-tracker.md` 中该阶段所有知识点状态
- 新错误记录到 `mistakes.md`
- 仅当用户明确形成新能力时才更新 `learning-progress.md`

---

# 输出格式

## 考试信息
- 阶段：Stage X
- 考察范围：……

## 试卷
（各题型题目）

## 请提交答案

## 评分结果（用户提交后）
逐题评分 + 总分 + 结论

## 下一步
- 通过：开始下一阶段
- 未通过：针对性补课
