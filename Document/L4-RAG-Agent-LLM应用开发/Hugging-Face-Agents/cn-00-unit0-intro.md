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

欢迎来到 🤗 AI Agents 课程

# Agents 课程

🏡 查看所有资源Agents 课程音频课程社区计算机视觉课程深度强化学习课程扩散模型课程LLM 课程MCP 课程3D 机器学习课程游戏机器学习课程开源 AI 食谱机器人课程a smol course

搜索文档

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. 欢迎来到课程

[欢迎来到课程 🤗](</learn/agents-course/unit0/introduction>)[入门指南](</learn/agents-course/unit0/onboarding>)[（可选）Discord 101](</learn/agents-course/unit0/discord101>)

Live 1. 课程说明与答疑

Unit 1. Agent 基础介绍

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

# [](<#introduction>) 欢迎来到 🤗 AI Agents 课程

![AI Agents 课程缩略图](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/thumbnail.jpg) 图片背景使用 [Scenario.com](<https://scenario.com/>) 生成

欢迎来到当今 AI 领域最激动人心的主题：**Agent（智能体）**！

这门免费课程将带你踏上一段旅程，**从入门到精通**，理解和构建 AI Agent。

第一个单元将帮助你入门：

  * 了解**课程大纲**。
  * **选择你的学习路径**（旁听模式或认证流程）。
  * **获取认证流程的更多信息**。
  * 认识课程背后的团队。
  * 创建你的 **Hugging Face 账号**。
  * **加入我们的 Discord 服务器**，认识你的同学和我们。

让我们开始吧！

## [](<#expect>) 这门课程能学到什么？

在本课程中，你将：

  * 📖 从**理论、设计和实践**三个方面学习 AI Agent。
  * 🧑‍💻 学习**使用成熟的 AI Agent 库**，如 [smolagents](<https://huggingface.co/docs/smolagents/en/index>)、[LlamaIndex](<https://www.llamaindex.ai/>) 和 [LangGraph](<https://langchain-ai.github.io/langgraph/>)。
  * 💾 在 Hugging Face Hub 上**分享你的 Agent**，并探索社区创建的 Agent。
  * 🏆 参与挑战，**将你的 Agent 与其他同学的进行评估对比**。
  * 🎓 通过完成作业**获得结业证书**。

还有更多！

在本课程结束时，你将理解**Agent 的工作原理以及如何使用最新的库和工具构建自己的 Agent**。

别忘了**[注册课程！](<https://bit.ly/hf-learn-agents>)**

（我们尊重你的隐私。我们收集你的电子邮件地址是为了**在每个单元发布时向你发送链接，并提供有关挑战和更新的信息**）。

## [](<#course-look-like>) 课程是什么样的？

课程由以下部分组成：

  * _基础单元_：学习 Agent 的**理论概念**。
  * _实践环节_：学习**使用成熟的 AI Agent 库**在独特环境中训练你的 Agent。这些实践部分将以预配置环境的 **Hugging Face Spaces** 形式提供。
  * _应用案例作业_：将所学概念应用于解决你选择的真实世界问题。
  * _挑战赛_：让你的 Agent 与其他 Agent 进行竞争。还有一个[排行榜](<https://huggingface.co/spaces/agents-course/Students_leaderboard>)供你比较 Agent 的表现。

这门**课程是一个持续发展的项目，会根据你的反馈和贡献不断演进！** 欢迎在 GitHub 上[提交 Issue 和 PR](<https://github.com/huggingface/agents-course>)，并在我们的 Discord 服务器中参与讨论。

完成课程后，你也可以通过[👉 使用此表单](<https://docs.google.com/forms/d/e/1FAIpQLSe9VaONn0eglax0uTwi29rIn4tM7H2sYmmybmG5jJNlE5v0xA/viewform?usp=dialog>)发送你的反馈。

## [](<#syllabus>) 课程大纲是什么？

以下是**课程的总体大纲**。每个单元将发布更详细的主题列表。

章节 | 主题 | 描述
---|---|---
0 | 入门 | 设置你将使用的工具和平台。
1 | Agent 基础 | 解释工具（Tools）、思考（Thoughts）、行动（Actions）、观察（Observations）及其格式。解释 LLM、消息、特殊标记（special tokens）和聊天模板（chat templates）。展示使用 Python 函数作为工具的简单用例。
2 | 框架 | 理解基础知识如何在流行库中实现：smolagents、LangGraph、LLamaIndex
3 | 应用案例 | 构建一些真实场景的应用案例（欢迎有经验的 Agent 构建者提交 PR 🤗）
4 | 最终作业 | 为选定的基准测试构建一个 Agent，并在学生排行榜上证明你对 Agent 的理解 🚀

除主大纲外，还有 3 个奖励单元：

  * _奖励单元 1_：面向函数调用的 LLM 微调
  * _奖励单元 2_：Agent 可观测性与评估
  * _奖励单元 3_：游戏中的 Agent（Pokemon）

例如，在奖励单元 3 中，你将学习构建你的 Agent 来进行 Pokemon 对战 🥊。

## [](<#what-are-the-prerequisites>) 有什么前提条件？

要学习本课程，你需要具备：

  * Python 基础知识
  * LLM 基础知识（我们在 Unit 1 中有一个章节帮你回顾）

## [](<#tools>) 我需要什么工具？

你只需要 2 样东西：

  * 一台能上网的_电脑_。
  * 一个 _Hugging Face 账号_：用于推送和加载模型、Agent 以及创建 Spaces。如果你还没有账号，可以**[在这里](<https://hf.co/join>)**免费创建。 ![课程所需工具](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/tools.jpg)

## [](<#certification-process>) 认证流程

![两条路径](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/three-paths.jpg)

你可以选择以_旁听模式_学习本课程，或者完成活动并_获得我们颁发的两种证书之一_。

如果你旁听课程，你可以参与所有挑战并完成作业（如果你愿意），**不需要通知我们**。

认证流程**完全免费**：

  * _获得基础认证_：你需要完成课程的 Unit 1。适合希望了解 Agent 最新趋势的学生。
  * _获得结业证书_：你需要完成 Unit 1、我们将在课程中提出的一个应用案例作业以及最终挑战。

认证流程**没有截止日期**。

## [](<#recommended-pace>) 推荐的学习节奏是什么？

本课程的每个章节设计为**在 1 周内完成，每周大约 3-4 小时的学习时间**。

我们为你提供了推荐的学习节奏：

![推荐节奏](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/recommended-pace.jpg)

## [](<#advice>) 如何充分利用本课程？

为了充分利用本课程，我们有一些建议：

  1. [在 Discord 中加入学习小组](<https://discord.gg/UrrTSsSyjb>)：团队学习总是更容易。为此，你需要加入我们的 Discord 服务器并验证你的 Hugging Face 账号。
  2. **完成测验和作业**：最好的学习方式是通过实践和自我评估。
  3. **制定学习计划以保持同步**：你可以使用我们下面推荐的节奏计划，也可以创建自己的。

![课程建议](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/advice.jpg)

## [](<#who-are-we>) 我们是谁

本课程由 [Ben Burtenshaw](<https://huggingface.co/burtenshaw>) 和 [Sergio Paniego](<https://huggingface.co/sergiopaniego>) 维护。如有任何问题，请在 Hub 上联系我们！

## [](<#acknowledgments>) 致谢

我们要向以下对本课程做出宝贵贡献的个人表示感谢：

  * **[Joffrey Thomas](<https://huggingface.co/Jofthomas>)** - 编写和开发课程。
  * **[Thomas Simonini](<https://huggingface.co/ThomasSimonini>)** - 编写和开发课程。
  * **[Pedro Cuenca](<https://huggingface.co/pcuenq>)** - 指导课程并提供反馈。
  * **[Aymeric Roucher](<https://huggingface.co/m-ric>)** - 制作了精彩的演示 Space（解码和最终 Agent）以及在 smolagents 部分的帮助。
  * **[Joshua Lochner](<https://huggingface.co/Xenova>)** - 制作了关于分词（tokenization）的精彩演示 Space。
  * **[Quentin Gallouédec](<https://huggingface.co/qgallouedec>)** - 在课程内容方面的帮助。
  * **[David Berenstein](<https://huggingface.co/davidberenstein1957>)** - 在课程内容和审核方面的帮助。
  * **[XiaXiao (ShawnSiao)](<https://huggingface.co/SSSSSSSiao>)** - 课程中文翻译。
  * **[Jiaming Huang](<https://huggingface.co/nordicsushi>)** - 课程中文翻译。
  * **[Kim Noel](<https://github.com/knoel99>)** - 课程法语翻译。
  * **[Loïck Bourdois](<https://huggingface.co/lbourdois>)** - 来自 [CATIE](<https://www.catie.fr/>) 的课程法语翻译。

## [](<#contribute>) 我发现了错误，或想改进课程

欢迎**贡献** 🤗

  * 如果你_在 notebook 中发现了错误 🐛_，请[提交 Issue](<https://github.com/huggingface/agents-course/issues>)并**描述问题**。
  * 如果你_想改进课程_，可以[提交 Pull Request](<https://huggingface/agents-course/pulls>)。
  * 如果你_想添加完整章节或新单元_，最好先[提交 Issue](<https://github.com/huggingface/agents-course/issues>)并**描述你想添加的内容，在开始编写之前，以便我们为你提供指导**。

## [](<#questions>) 我还有问题

请在我们的 [Discord 服务器 #agents-course-questions](<https://discord.gg/UrrTSsSyjb>) 中提问。

现在你已经掌握了所有信息，让我们开始登船吧 ⛵

![是时候入门了](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/time-to-onboard.jpg) [在 GitHub 上更新](<https://github.com/huggingface/agents-course/blob/main/units/en/unit0/introduction.mdx>)

[入门指南→](</learn/agents-course/unit0/onboarding>)

[欢迎来到 🤗 AI Agents 课程](<#introduction>)[这门课程能学到什么？](<#expect>)[课程是什么样的？](<#course-look-like>)[课程大纲是什么？](<#syllabus>)[有什么前提条件？](<#what-are-the-prerequisites>)[我需要什么工具？](<#tools>)[认证流程](<#certification-process>)[推荐的学习节奏是什么？](<#recommended-pace>)[如何充分利用本课程？](<#advice>)[我们是谁](<#who-are-we>)[致谢](<#acknowledgments>)[我发现了错误，或想改进课程](<#contribute>)[我还有问题](<#questions>)
