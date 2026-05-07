# 智能体（Agents）

智能体将语言模型与[工具](https://docs.langchain.com/oss/python/langchain/tools)结合，创建能够推理任务、决定使用哪些工具并迭代地朝着解决方案工作的系统。`create_agent` 提供了一个生产就绪的智能体实现。LLM 智能体在循环中运行工具以实现目标。智能体会一直运行，直到满足停止条件——即模型发出最终输出或达到迭代限制。

`create_agent` 使用 [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) 构建基于**图（Graph）**的智能体运行时。图由节点（步骤）和边（连接）组成，定义了智能体处理信息的方式。智能体在图中移动，执行模型节点（调用模型）、工具节点（执行工具）或中间件等节点。

## 核心组件

### 模型（Model）

[模型](https://docs.langchain.com/oss/python/langchain/models)是智能体的推理引擎。可以以多种方式指定，支持静态和动态模型选择。

**静态模型**：在创建智能体时配置一次，在整个执行过程中保持不变。

    from langchain.agents import create_agent

    agent = create_agent("openai:gpt-5.4", tools=tools)

对于更多控制，直接使用提供商包初始化模型实例：

    from langchain_openai import ChatOpenAI
    model = ChatOpenAI(model="gpt-5.4", temperature=0.1, max_tokens=1000, timeout=30)
    agent = create_agent(model, tools=tools)

**动态模型**：在运行时根据当前状态和上下文选择。使用 `@wrap_model_call` 装饰器创建中间件，在请求中修改模型。

### 工具（Tools）

工具赋予智能体执行动作的能力。智能体支持：

  * 顺序执行多个工具调用
  * 适当时候并行调用工具
  * 基于之前的结果动态选择工具
  * 工具重试逻辑和错误处理
  * 跨工具调用的状态持久化

**静态工具**：在创建智能体时定义。使用 `@tool` 装饰器：

    from langchain.tools import tool
    @tool
    def search(query: str) -> str:
        """搜索信息。"""
        return f"Results for: {query}"

**动态工具**：在运行时修改可用工具集。两种方法：
  1. 过滤预注册的工具（基于状态、Store 或运行时上下文）
  2. 运行时工具注册（需要 `wrap_model_call` 和 `wrap_tool_call` 两个中间件钩子）

### 工具错误处理

使用 `@wrap_tool_call` 装饰器创建中间件来自定义工具错误处理。

### ReAct 循环中的工具使用

智能体遵循 ReAct（"推理 + 行动"）模式，在简短的推理步骤和有针对性的工具调用之间交替，并将观察结果反馈到后续决策中，直到能够提供最终答案。

### 系统提示（System Prompt）

通过 `system_prompt` 参数提供提示来塑造智能体处理任务的方式。支持静态和动态系统提示。

使用 `@dynamic_prompt` 装饰器创建中间件，根据模型请求动态生成系统提示。

### 调用（Invocation）

通过向智能体的 `State` 传递更新来调用智能体：

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )

## 高级概念

### 结构化输出

通过 `response_format` 参数让智能体以特定格式返回输出。支持两种策略：
  * `ToolStrategy`：使用人工工具调用生成结构化输出，适用于任何支持工具调用的模型。
  * `ProviderStrategy`：使用模型提供商的原生结构化输出生成，更可靠但仅适用于支持原生结构化输出的提供商。

### 记忆（Memory）

智能体通过消息状态自动维护对话历史。可以通过中间件或 `state_schema` 参数定义自定义状态模式。

### 流式传输（Streaming）

使用 `stream` 方法流式返回消息，展示中间进度。

### 中间件（Middleware）

[中间件](https://docs.langchain.com/oss/python/langchain/middleware)提供强大的可扩展性，用于在执行的不同阶段自定义智能体行为：
  * 在调用模型前处理状态（如消息修剪、上下文注入）
  * 修改或验证模型响应（如护栏、内容过滤）
  * 使用自定义逻辑处理工具执行错误
  * 基于状态或上下文实现动态模型选择
  * 添加自定义日志记录、监控或分析
