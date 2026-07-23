---
name: journal
description: "写入进组日报到 InertiaScribe 项目。用法: /journal 生成今日日报, /journal <日期> 补写指定日期日报。"
---

# journal - 进组日报写入工具

将当天的 NNDL 学习内容整理为进组日报，写入 `E:\Project\InertiaScribe\docs\journal\YYYY-MM-DD.md`。

## 核心原则

**只写给导师看的项目相关内容。** 数分作业、大学物理、慕课、复习卡片、其他课程——一概不写。日报只包含两件事：

1. 当天学了哪些 NNDL（《神经网络与深度学习》）知识
2. 这些知识与 InertiaScribe 项目有什么关联

## 工作流程

### Step 1: 收集今日数据

只从以下文件提取 NNDL 相关内容：

1. `plan/record/daily/YYYY-MM-DD.md` — 每日复盘（只取 NNDL 部分）
2. `plan/daily-plan.md` — 今日计划中的 /end-day 记录（只取 NNDL 部分）
3. `courses/neural-networks/progress/mastery-tracker.md` — NNDL 当日新增行
4. `courses/neural-networks/logs/learning-sessions/YYYY-MM-DD-*.md` — 学习日志

### Step 2: 生成日报

按以下模板：

```markdown
# YYYY-MM-DD 学习日报

## NNDL 第X章 · [章节标题] — [完成状态]

[按单元列出知识点表格]

| 单元 | 章节 | 学到什么 | 练习正确率 |
|------|------|---------|:---------:|
| ... | §X.X ... | [核心知识点描述] | XX% |

### 核心收获
[用一段话串联本章的核心概念链]

---

## 与 InertiaScribe 项目的关联

[将当天学到的 NNDL 知识与 InertiaScribe 项目做具体关联——哪个概念对应项目的哪个决策或模块]
```

### Step 3: 写入文件

写入 `E:\Project\InertiaScribe\docs\journal\YYYY-MM-DD.md`。

如果文件已存在，先确认是否覆盖。

### Step 4: 输出文件内容给用户确认

## 禁止写入的內容

- 数分作业、其他课程作业
- 大学物理、电路分析等上课内容
- 复习卡片（review）进度
- 慕课、UCloud 等平台任务
- 非 NNDL 的任何学习内容
- 日常作息、时间安排

## 注意事项

- 知识点描述要具体，不是"学了XX章"一句话带过
- 正确率从 mastery-tracker.md 或学习日志中提取真实数据
- "与 InertiaScribe 项目的关联"要具体映射到项目的技术决策，不要泛泛而谈
- 日期用当天真实日期，不编造
