---
description: TI 板子每日测试，生成当日测试题、批改、记录结果，决定是否允许推进
---

请执行 TI 板子每日测试任务。

$ARGUMENTS

---

# 必须先读取的文件

- `courses/ti-board/syllabus.md`
- `courses/ti-board/mastery-tracker.md`
- `courses/ti-board/daily-tests.md`
- `courses/ti-board/mistakes.md`
- `courses/ti-board/concepts.md`
- `courses/ti-board/examples.md`
- `courses/ti-board/exercises.md`
- `plan/daily-plan.md`

---

# 测试流程

## 1. 测试前检查

- 查看 `courses/ti-board/mastery-tracker.md`，确认当前知识点练习正确率是否 >= 80%
- 如果正确率不足 80%，不允许进入测试，必须回到 `/ti-study-session` 继续练习
- 查看 `courses/ti-board/mistakes.md`，确认之前的错误点是否已复习

## 2. 生成测试题

根据当前知识点从以下来源出题：
- `courses/ti-board/concepts.md`
- `courses/ti-board/examples.md`
- `courses/ti-board/mistakes.md` 中的历史错误点（优先考察薄弱环节）

测试题要求：
- 覆盖当前知识点的核心概念和关键操作
- 包含 3-5 道题，难度逐步递增
- 至少 1 题涉及实际操作或代码编写
- 至少 1 题针对历史错误点
- 如果资料不足，明确说明"当前课程资料不足，无法生成有效测试题"，不要编造题目

## 3. 批改

如果用户已提交答案，则批改：
- 逐题判断正确/错误
- 计算得分
- 判断通过/未通过（通过线：80 分）

## 4. 记录结果到 `courses/ti-board/daily-tests.md`

格式：
```markdown
## YYYY-MM-DD Daily Test

测试范围：XXX

题目：
1. ……
2. ……

用户答案：
1. ……
2. ……

批改：
1. 正确/错误 — ……
2. 正确/错误 — ……

得分：XX/100

结论：通过 / 未通过

后续建议：……
```

## 5. 更新 `courses/ti-board/mastery-tracker.md`

- 通过测试：将知识点状态更新为"初步掌握"或"已掌握"，允许推进
- 未通过测试：知识点状态更新为"部分掌握"，不允许推进，标注需要重新学习的部分

## 6. 更新 `courses/ti-board/mistakes.md`

- 如果测试中出现新错误，记录到 `mistakes.md`

---

# 通过后的推进规则

测试通过后：
1. 更新 `courses/ti-board/mastery-tracker.md` 为"允许推进"
2. 更新 `plan/daily-plan.md` 中 TI 相关任务状态
3. 告知用户可以使用 `/ti-study-session` 开始学习下一个知识点
4. 只有当用户明确表示形成了新的稳定工程能力时，才更新 `learning-progress.md`

---

# 输出格式

# TI Board Daily Test

日期：YYYY-MM-DD

## 测试范围
- 知识点：XXX
- 对应 syllabus 阶段：XXX

## 测试题

### 题 1：（概念/操作/代码）
……

### 题 2：
……

### 题 3：
……

### 题 4：
……

### 题 5：
……

## 请提交答案
请使用 `/ti-check-answer` 或在 `/ti-daily-test` 中直接提交你的答案。

---

（如果用户在调用时已经提交了答案，则在测试题后追加批改部分）

## 批改结果

| 题号 | 判断 | 说明 |
| --- | --- | --- |
| 1 | 正确/错误 | …… |
| 2 | …… | …… |

得分：XX/100
结论：通过 / 未通过

## 错误分析
……

## 下一步
- 通过：可以推进到下一知识点（使用 `/ti-study-session`）
- 未通过：需要重新学习 XX 部分（使用 `/ti-study-session` 补课）

## 已更新文件
- `courses/ti-board/daily-tests.md`：已更新
- `courses/ti-board/mastery-tracker.md`：已更新
- `courses/ti-board/mistakes.md`：已/未更新
