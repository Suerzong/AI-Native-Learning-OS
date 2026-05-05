For user  :  ti-daily-test.prompt.md  作用：TI 板子每日测试，生成当日测试题、批改、记录结果，决定是否允许推进。

---
name: ti-daily-test
description: TI 板子每日测试，生成当日测试题、批改、记录结果，决定是否允许推进
agent: agent
---

请执行 TI 板子每日测试任务。

$ARGUMENTS

---

# 必须先读取的文件

- `.github/agents/mastery-learn.agent.md` — 教学引擎（推进规则）
- `courses/ti-board/course-config.md`
- `courses/ti-board/mastery-tracker.md`
- `courses/ti-board/daily-tests.md`
- `courses/ti-board/mistakes.md`
- `courses/ti-board/exercises.md`
- `plan/daily-plan.md`

---

# 测试流程

## 1. 测试前检查

- 查看 `mastery-tracker.md`，确认当前知识点练习正确率是否 >= 80%
- 如果正确率不足 80%，不允许进入测试
- 查看 `mistakes.md`，确认之前的错误点是否已复习

## 2. 生成测试题

根据当前知识点从 `course-config.md` 知识图谱出题：
- 覆盖核心概念和关键操作
- 3-5 道题，难度逐步递增
- 至少 1 题涉及代码编写
- 至少 1 题针对历史错误点

## 3. 批改

- 逐题判断正确/错误
- 计算得分
- 通过线：80 分

## 4. 记录结果到 `daily-tests.md`

## 5. 更新 `mastery-tracker.md`

- 通过：更新为"初步掌握"或"已掌握"，允许推进
- 未通过：更新为"部分掌握"，不允许推进

## 6. 更新 `mistakes.md`

- 测试中新出现的错误记录到 mistakes.md

---

# 输出格式

## 测试题
（3-5 道题）

## 批改结果
（逐题评分）

## 下一步
- 通过：可以推进到下一知识点
- 未通过：需要重新学习

## 已更新文件
列出已更新的文件
