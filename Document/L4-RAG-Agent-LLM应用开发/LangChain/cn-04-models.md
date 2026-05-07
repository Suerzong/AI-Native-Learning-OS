# 模型（Models）

[大语言模型（LLM）](https://en.wikipedia.org/wiki/Large_language_model)是强大的 AI 工具，可以像人类一样解释和生成文本。除了文本生成，许多模型还支持：

  * [工具调用](#工具调用)——调用外部工具（如数据库查询或 API 调用）并在响应中使用结果
  * [结构化输出](#结构化输出)——模型响应被约束为遵循定义的格式
  * [多模态](#多模态)——处理和返回文本以外的数据，如图像、音频和视频
  * [推理](#推理)——模型执行多步推理以得出结论

模型是[智能体](https://docs.langchain.com/oss/python/langchain/agents)的推理引擎，驱动智能体的决策过程。

## 基本用法

模型可以通过两种方式使用：
  1. **与智能体一起使用**——在创建智能体时动态指定模型
  2. **独立使用**——直接调用模型，无需智能体框架

### 初始化模型

使用 `init_chat_model` 从你选择的聊天模型提供商初始化模型：

    from langchain.chat_models import init_chat_model

    # OpenAI
    model = init_chat_model("gpt-5.4")

    # Anthropic
    model = init_chat_model("claude-sonnet-4-6")

    # Google Gemini
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")

### 支持的提供商和模型

LangChain 通过专用集成包支持所有主要模型提供商。每个提供商包实现相同的标准接口，因此你可以无缝切换提供商而无需重写应用程序逻辑。

### 关键方法

  * **Invoke**：模型接收消息作为输入，生成完整响应后输出消息
  * **Stream**：调用模型，但在生成时实时流式输出
  * **Batch**：批量向模型发送多个请求以提高处理效率

### 参数

标准参数包括：

| 参数 | 类型 | 说明 |
|------|------|------|
| `model` | string | 必需。要使用的模型名称或标识符 |
| `api_key` | string | 用于验证的 API 密钥 |
| `temperature` | number | 控制输出的随机性。较高值使响应更具创意 |
| `max_tokens` | number | 限制响应中的最大 token 数 |
| `timeout` | number | 等待模型响应的最长时间（秒） |
| `max_retries` | number | 请求失败时的最大重试次数（默认 6） |

## 工具调用（Tool Calling）

模型可以请求调用工具来执行任务，如从数据库获取数据、搜索网页或运行代码。工具是以下两者的配对：
  1. 模式（Schema）——包括工具名称、描述和参数定义
  2. 要执行的函数或协程

使用 `bind_tools` 将工具绑定到模型。模型的响应包含执行工具的**请求**。你需要执行请求的工具并将结果返回给模型。

支持强制工具调用、并行工具调用和流式工具调用。

## 结构化输出（Structured Output）

可以要求模型以匹配给定模式的格式提供响应。LangChain 支持多种模式类型：

  * **Pydantic**：提供最丰富的功能集，包括字段验证和嵌套结构
  * **TypedDict**：Pydantic 的简单替代方案，不需要运行时验证
  * **JSON Schema**：提供最大控制和互操作性

使用 `with_structured_output` 方法：

    model_with_structure = model.with_structured_output(Movie)
    response = model_with_structure.invoke("Provide details about the movie Inception")

## 高级主题

### 多模态（Multimodal）

某些模型可以处理和返回非文本数据。通过提供[内容块](https://docs.langchain.com/oss/python/langchain/messages#message-content)传递非文本数据。

### 推理（Reasoning）

许多模型能够执行多步推理。如果底层模型支持，可以展示推理过程以更好地理解模型如何得出最终答案。

### 本地模型

LangChain 支持在你自己的硬件上本地运行模型。[Ollama](https://docs.langchain.com/oss/python/integrations/chat/ollama) 是本地运行聊天和嵌入模型的最简单方式之一。

### 提示缓存（Prompt Caching）

许多提供商提供提示缓存功能，以减少对相同 token 重复处理的延迟和成本。分为**隐式缓存**（提供商自动传递节省的成本）和**显式缓存**（允许你手动指示缓存点）。

### 速率限制（Rate Limiting）

聊天模型集成接受 `rate_limiter` 参数，用于控制请求速率。LangChain 内置 `InMemoryRateLimiter`。

### 可配置模型

使用 `configurable_fields` 创建运行时可配置的模型：

    configurable_model = init_chat_model(temperature=0)
    configurable_model.invoke(
        "what's your name",
        config={"configurable": {"model": "gpt-5-nano"}},
    )
