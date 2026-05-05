For user  :  ti-check-answer.prompt.md  作用：TI 板子批改答案，记录错误点到 mistakes.md，更新 mastery-tracker.md。

---
name: ti-check-answer
description: TI 板子批改答案，记录错误点到 mistakes.md，更新 mastery-tracker.md
agent: agent
---

请执行答案批改任务。

$ARGUMENTS

用户将提交练习题目的答案。你需要批改并记录结果。

---

# 必须先读取的文件

- `courses/ti-board/course-config.md`
- `courses/ti-board/mastery-tracker.md`
- `courses/ti-board/mistakes.md`
- `courses/ti-board/exercises.md`

---

# 批改流程

1. 识别用户正在回答的是哪个知识点、哪道题目
2. 对照 `course-config.md` 中的知识图谱进行判断
3. 逐项检查用户的答案
4. 标注每道题的正确、部分正确或错误
5. 计算正确率
6. 分析错误原因

---

# 记录要求

## 记录到 `courses/ti-board/mistakes.md`

如果存在错误，记录：
- 日期
- 错误点名称
- 出现位置
- 错误类型（概念理解错误 / 计算错误 / 流程遗漏 / 代码语法错误 / 配置错误）
- 原因分析
- 修正方法
- 是否已复习

## 更新 `courses/ti-board/mastery-tracker.md`

根据正确率更新：
- 正确率 < 60%：未掌握，不允许推进
- 正确率 60%-79%：部分掌握，需要补题
- 正确率 80%-89%：初步掌握，可进入当日测试
- 正确率 >= 90%：掌握，可以推进

---

# 输出格式

## 批改结果
- 知识点：XXX
- 正确率：XX/XX = XX%
- 掌握度判断：XX

## 错误分析
（如果有错误）每个错误点的类型、原因、建议

## 下一步
- 通过：可使用 `/ti-daily-test` 进行当日测试
- 未通过：需要重新学习后再次练习
