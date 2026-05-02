---
description: TI 板子阶段综合考试，考察体系理解，记录到 exams.md 并决定阶段是否通过
---

请执行 TI 板子阶段综合考试任务。

$ARGUMENTS

---

# 必须先读取的文件

- `courses/ti-board/syllabus.md` — 确定考试阶段范围
- `courses/ti-board/mastery-tracker.md` — 当前各知识点掌握度
- `courses/ti-board/daily-tests.md` — 历史测试记录
- `courses/ti-board/mistakes.md` — 历史错误点
- `courses/ti-board/exams.md` — 已有试卷和考试记录
- `courses/ti-board/concepts.md`
- `courses/ti-board/examples.md`
- `courses/ti-board/exercises.md`
- `courses/ti-board/labs.md`
- `plan/daily-plan.md`

---

# 考试前检查

1. 确认当前 syllabus 阶段的所有知识点每日测试是否已通过
2. 查看 `courses/ti-board/mastery-tracker.md`，确认该阶段所有知识点正确率 >= 80%
3. 查看 `courses/ti-board/mistakes.md`，确认该阶段的错误点是否已复习
4. 如果有知识点未通过测试，不允许进行阶段考试，必须先补测

---

# 考试范围

根据 `courses/ti-board/syllabus.md` 中的阶段划分：

- **阶段 1**：开发环境与板卡认识（开发环境安装、工程创建、烧录调试、第一个 LED 程序）
- **阶段 2**：基础外设（GPIO、定时器、中断、PWM、ADC、UART、I2C、SPI）
- **阶段 3**：综合实验（串口通信实验、PWM 控制实验、ADC 采样实验、传感器读取实验、小型综合项目）
- **阶段 4**：能力考核

---

# 试卷生成规则

1. 综合考察该阶段的**所有知识点**
2. 重点考察 `courses/ti-board/mistakes.md` 中记录的薄弱环节
3. 题目类型应包含：
   - 概念理解题
   - 流程/配置题
   - 代码编写或补全题
   - 调试/故障排查题
   - （如果 lab 已完成）实验分析题
4. 总分 100 分，各题型权重合理分配
5. 如果 `courses/ti-board/concepts.md` 或 `courses/ti-board/examples.md` 资料不足，必须明确说明缺少哪些内容，**不要编造题目**
6. 考试题记录到 `courses/ti-board/exams.md`

---

# 评分与记录

## 评分标准
- 90 分以上：优秀，阶段稳固通过
- 80-89 分：良好，通过，可进入下一阶段
- 60-79 分：部分通过，需要针对性补课后再考
- 60 分以下：未通过，需要系统重新学习该阶段

## 记录到 `courses/ti-board/exams.md`

```markdown
## Stage X Exam：（阶段名称）

考试日期：YYYY-MM-DD
考试目标：……

题目：
1. ……
2. ……

用户答案：
1. ……
2. ……

评分：
1. XX/XX — ……
2. XX/XX — ……

总分：XX/100

结论：通过 / 未通过

错误分析：
- ……

后续建议：
- ……
```

## 更新其他文件

- 根据考试结果更新 `courses/ti-board/mastery-tracker.md` 中该阶段所有知识点状态
- 将新发现的错误点记录到 `courses/ti-board/mistakes.md`
- 只有用户通过考试后明确形成了新能力时，才更新 `learning-progress.md`

---

# 输出格式

# TI Board Stage Exam

## 考试信息
- 阶段：Stage X — XXX
- 考试日期：YYYY-MM-DD
- 考察知识点范围：……

## 考试前状态
（来自 mastery-tracker.md 的当前状态总结）

## 试卷

### 一、概念理解题（XX 分）
1. ……
2. ……

### 二、流程/配置题（XX 分）
3. ……

### 三、代码题（XX 分）
4. ……

### 四、调试/故障排查题（XX 分）
5. ……

### 五、实验分析题（XX 分）（如 lab 已完成）
6. ……

## 请提交答案
请逐一作答，使用 `/ti-check-answer` 或在回复中直接提交。

---

（如果用户已提交答案，追加以下部分）

## 评分结果

| 题号 | 满分 | 得分 | 说明 |
| --- | --- | --- | --- |
| 1 | XX | XX | …… |
| …… | …… | …… | …… |

总分：XX/100
等级：优秀/良好/部分通过/未通过
结论：通过 / 未通过

## 错误分析
……

## 下一步
- **通过**：恭喜！可以使用 `/ti-study-session` 开始下一阶段学习
- **未通过**：需要重新学习以下部分……然后使用 `/ti-exam` 补考

## 已更新文件
- `courses/ti-board/exams.md`：已更新
- `courses/ti-board/mastery-tracker.md`：已更新
- `courses/ti-board/mistakes.md`：已/未更新
