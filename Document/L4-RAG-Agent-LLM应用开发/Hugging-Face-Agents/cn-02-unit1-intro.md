[![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Hugging Face](</>)

  * [ 模型 ](</models>)
  * [ 数据集 ](</datasets>)
  * [ Spaces ](</spaces>)
  * [ Buckets 新功能](</storage>)
  * [ 文档 ](</docs>)
  * [ 企业版 ](</enterprise>)
  * [定价](</pricing>)
  *   * * * *

  * [登录](</login>)
  * [注册](</join>)

Agents 课程文档

Agent 基础介绍

# Agents 课程

🏡 查看所有资源Agents 课程音频课程社区计算机视觉课程深度强化学习课程扩散模型课程LLM 课程MCP 课程3D 机器学习课程游戏机器学习课程开源 AI 食谱机器人课程a smol course

搜索文档

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. 欢迎来到课程

Live 1. 课程说明与答疑

Unit 1. Agent 基础介绍

[简介](</learn/agents-course/unit1/introduction>)[什么是 Agent？](</learn/agents-course/unit1/what-are-agents>)[快速测验 1](</learn/agents-course/unit1/quiz1>)[什么是 LLM？](</learn/agents-course/unit1/what-are-llms>)[消息与特殊标记](</learn/agents-course/unit1/messages-and-special-tokens>)[什么是工具？](</learn/agents-course/unit1/tools>)[快速测验 2](</learn/agents-course/unit1/quiz2>)[通过思考-行动-观察循环理解 AI Agent](</learn/agents-course/unit1/agent-steps-and-structure>)[思考：内部推理与 ReAct 方法](</learn/agents-course/unit1/thoughts>)[行动：让 Agent 与环境交互](</learn/agents-course/unit1/actions>)[观察：整合反馈以反思和适应](</learn/agents-course/unit1/observations>)[Dummy Agent 库](</learn/agents-course/unit1/dummy-agent-library>)[使用 smolagents 创建我们的第一个 Agent](</learn/agents-course/unit1/tutorial>)[Unit 1 最终测验](</learn/agents-course/unit1/final-quiz>)[总结](</learn/agents-course/unit1/conclusion>)

Unit 2. AI Agent 框架

Unit 2.1 smolagents 框架

Unit 2.2 LlamaIndex 框架

Unit 2.3 LangGraph 框架

Unit 3. Agentic RAG 应用案例

Unit 4. 最终项目 - 创建、测试并认证你的 Agent

Bonus Unit 1. 面向函数调用的 LLM 微调

Bonus Unit 2. Agent 可观测性与评估

Bonus Unit 3. 游戏中的 Agent（Pokemon）

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

加入 Hugging Face 社区

获取增强文档体验

在模型、数据集和 Spaces 上协作

通过加速推理获得更快的示例

切换文档主题

[注册](</join>)

开始使用

复制页面

# [](<#introduction-to-agents>) Agent 基础介绍

![缩略图](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/thumbnail.jpg)

欢迎来到第一个单元，在这里**你将为 AI Agent 的基础知识奠定坚实基础**，包括：

  * **理解 Agent**

    * 什么是 Agent，它是如何工作的？
    * Agent 如何使用推理和规划进行决策？
  * **LLM（大型语言模型）在 Agent 中的角色**

    * LLM 如何作为 Agent 的"大脑"。
    * LLM 如何通过消息系统构建对话。
  * **工具与行动**

    * Agent 如何使用外部工具与环境交互。
    * 如何为你的 Agent 构建和集成工具。
  * **Agent 工作流程：**

    * _思考_ → _行动_ → _观察_。

探索完这些主题后，**你将使用 `smolagents` 构建你的第一个 Agent**！

你的 Agent 名叫 Alfred，它将处理一个简单的任务，并展示如何在实践中应用这些概念。

你还将学习如何**在 Hugging Face Spaces 上发布你的 Agent**，以便与朋友和同事分享。

最后，在本单元结束时，你将参加一个测验。通过测验后，你将**获得你的第一个课程认证**：🎓 Agent 基础认证。

![证书示例](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/certificate-example.jpg)

本单元是你的**重要起点**，在你进入更高级主题之前，为理解 Agent 奠定基础。

![Unit 1 规划](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/whiteboard-no-check.jpg)

这是一个很大的单元，所以**请慢慢来**，不要犹豫随时回顾这些章节。

准备好了吗？让我们开始吧！🚀

[ 在 GitHub 上更新](<https://github.com/huggingface/agents-course/blob/main/units/en/unit1/introduction.mdx>)

[←Live 1. 课程说明与答疑](</learn/agents-course/communication/live1>) [什么是 Agent？→](</learn/agents-course/unit1/what-are-agents>)

[Agent 基础介绍](<#introduction-to-agents>)
