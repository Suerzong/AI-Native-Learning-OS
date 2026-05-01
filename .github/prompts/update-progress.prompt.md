For user:  update-progress.prompt.md  作用：固定“更新学习进度”这个任务。

Prompt file 是可以通过 / 调用的固定提示词。官方文档说明，prompt files 适合把常用任务编码成 Markdown 文件，通过 chat 里的 slash command 调用；工作区级 prompt 默认放在 .github/prompts

---
name: update-progress
description: 更新宋恩泽的完整 12 大模块学习进度
agent: agent
---

请执行学习进度更新任务。

必须先读取：
- `learning-progress.md`
- `course-index.md`

任务：
1. 判断新增内容属于哪些模块
2. 合并进 `learning-progress.md`
3. 保持完整 12 大模块结构
4. 区分已了解、已学习、已实践、初步掌握、已掌握、已应用
5. 不夸大能力
6. 如果允许编辑文件，请直接修改 `learning-progress.md`
7. 输出本次更新摘要和当前能力画像摘要