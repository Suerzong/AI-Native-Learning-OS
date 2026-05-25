For user: teach-course.prompt.md 作用：固定“教我课程”这个任务。

---
name: teach-course
description: 根据学习进度和课程资料讲解指定知识点
agent: ask
---

请执行课程辅导任务。

必须先读取：
- `learning-progress.md`
- `course-index.md`
- 当前课程的 `course-config.md`
- 当前课程的 `materials/references.md`（如存在）

然后根据我指定的课程和知识点，查找对应课程资料。

## 课程源隔离

如果当前课程的 `course-config.md` 声明 `source_mode: textbook-only`：

1. 只允许使用 `course-config.md` 和 `materials/references.md` 明确列入的允许源。
2. 不输出工程例子、路线联系、代码练习、外部资料扩展或未学过的大块内容。
3. 输出结构改为课本讲解结构：
   - 这个知识点在课本哪里
   - 课本原文要解决什么问题
   - 核心定义/公式/结构
   - 前置知识
   - 和已学课本内容的关系
   - 易混点
   - 课本范围内练习建议

## 默认输出结构

如果课程没有声明 `textbook-only`，按以下结构输出：

1. 这个知识点是什么
2. 需要哪些前置知识
3. 和我已学内容的关系
4. 核心原理
5. 示例或应用场景
6. 练习建议

所有课程都必须遵守：不要编造课程资料中没有的内容；如果课程资料不足，明确说明缺少哪些资料。
