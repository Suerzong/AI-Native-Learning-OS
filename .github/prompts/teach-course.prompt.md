For user:  teach-course.prompt.md  作用：固定“教我课程”这个任务。

---
name: teach-course
description: 根据学习进度和课程资料讲解指定知识点
agent: ask
---

请执行课程辅导任务。

必须先读取：
- `learning-progress.md`
- `course-index.md`

然后根据我指定的课程和知识点，查找对应课程资料。

输出结构：
1. 这个知识点是什么
2. 需要哪些前置知识
3. 和我已学内容的关系
4. 核心原理
5. 工程例子
6. 和 Edge AI / 嵌入式 AI 的联系
7. 练习建议