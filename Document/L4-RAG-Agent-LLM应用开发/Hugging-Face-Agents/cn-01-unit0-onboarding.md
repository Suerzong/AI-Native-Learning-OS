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

入门指南：你的第一步 ⛵

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

# [](<#onboarding-your-first-steps->) 入门指南：你的第一步 ⛵

![是时候入门了](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/time-to-onboard.jpg)

现在你已经了解了所有细节，让我们开始吧！我们将做四件事：

  1. **创建你的 Hugging Face 账号**（如果还没有的话）
  2. **加入 Discord 并做自我介绍**（不要害羞 🤗）
  3. **在 Hub 上关注 Hugging Face Agents 课程**
  4. **传播**关于本课程的信息

### [](<#step-1-create-your-hugging-face-account>) 第 1 步：创建你的 Hugging Face 账号

（如果你还没有）在[这里](<https://huggingface.co/join>)创建一个 Hugging Face 账号。

### [](<#step-2-join-our-discord-community>) 第 2 步：加入我们的 Discord 社区

👉🏻 在[这里](<https://discord.gg/UrrTSsSyjb>)加入我们的 Discord 服务器。

加入后，记得在 `#introduce-yourself` 频道做自我介绍。

访问 `Hugging Face Hub` 下的 `courses` 频道，获取所有与课程相关的问题和解答。

如果你是第一次使用 Discord，我们写了一份 Discord 101 指南来帮助你了解最佳实践。请查看[下一章节](<discord101>)。

### [](<#step-3-follow-the-hugging-face-agent-course-organization>) 第 3 步：关注 Hugging Face Agent 课程组织

**通过关注 Hugging Face Agents 课程组织**，及时了解最新的课程材料、更新和公告。

👉 前往[这里](<https://huggingface.co/agents-course>)并点击 **follow（关注）**。

![关注](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/hf_course_follow.gif)

### [](<#step-4-spread-the-word-about-the-course>) 第 4 步：传播课程信息

帮助我们提高课程的知名度！你可以通过两种方式帮助我们：

  1. ⭐ [给课程仓库点星](<https://github.com/huggingface/agents-course>)来表示你的支持。

![仓库点星](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/please_star.gif)

  2. 分享你的学习之旅：让其他人**知道你正在学习这门课程**！我们准备了一张插图，你可以在社交媒体帖子中使用

![](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/share.png)

你可以点击 👉 [这里](<https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/share.png?download=true>)下载图片。

### [](<#step-5-running-models-locally-with-ollama-in-case-you-run-into-credit-limits>) 第 5 步：使用 Ollama 在本地运行模型（以防遇到额度限制）

  1. **安装 Ollama**

按照[这里](<https://ollama.com/download>)的官方说明进行安装。

  2. **在本地拉取模型**

Copied

         ollama pull qwen2:7b

这里我们拉取 [qwen2:7b 模型](<https://ollama.com/library/qwen2:7b>)。查看 [Ollama 网站](<https://ollama.com/search>)获取更多模型。

  3. **在后台启动 Ollama（在一个终端中）**

Copied

         ollama serve

如果你遇到 "listen tcp 127.0.0.1:11434: bind: address already in use" 错误，可以使用命令 `sudo lsof -i :11434` 来识别当前正在使用该端口的进程 ID（PID）。如果该进程是 `ollama`，很可能是上面的安装脚本已经启动了 Ollama 服务，所以你可以跳过此命令。

  4. **使用 `LiteLLMModel` 替代 `InferenceClientModel`**

要使用 `smolagents` 中的 `LiteLLMModel` 模块，你可以运行 `pip` 命令来安装该模块。

Copied

        pip install 'smolagents[litellm]'

Copied

        from smolagents import LiteLLMModel

        model = LiteLLMModel(
            model_id="ollama_chat/qwen2:7b",  # 或尝试其他 Ollama 支持的模型
            api_base="http://127.0.0.1:11434",  # 默认 Ollama 本地服务器
            num_ctx=8192,
        )

  5. **为什么这样可以工作？**

  * Ollama 使用 OpenAI 兼容的 API 在本地提供模型服务，地址为 `http://localhost:11434`。
  * `LiteLLMModel` 可以与任何支持 OpenAI chat/completion API 格式的模型通信。
  * 这意味着你可以直接将 `InferenceClientModel` 替换为 `LiteLLMModel`，无需修改其他代码。这是一个无缝的即插即用解决方案。

恭喜！🎉 **你已经完成了入门流程**！你现在可以开始学习 AI Agent 了。祝你学习愉快！

继续学习，保持优秀 🤗

[ 在 GitHub 上更新](<https://github.com/huggingface/agents-course/blob/main/units/en/unit0/onboarding.mdx>)

[←欢迎来到课程 🤗](</learn/agents-course/unit0/introduction>) [(可选) Discord 101→](</learn/agents-course/unit0/discord101>)

[入门指南：你的第一步 ⛵](<#onboarding-your-first-steps->)[第 1 步：创建你的 Hugging Face 账号](<#step-1-create-your-hugging-face-account>)[第 2 步：加入我们的 Discord 社区](<#step-2-join-our-discord-community>)[第 3 步：关注 Hugging Face Agent 课程组织](<#step-3-follow-the-hugging-face-agent-course-organization>)[第 4 步：传播课程信息](<#step-4-spread-the-word-about-the-course>)[第 5 步：使用 Ollama 在本地运行模型（以防遇到额度限制）](<#step-5-running-models-locally-with-ollama-in-case-you-run-into-credit-limits>)
