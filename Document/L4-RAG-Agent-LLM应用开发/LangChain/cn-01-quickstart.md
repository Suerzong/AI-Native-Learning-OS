# 快速开始

在几分钟内构建你的第一个智能体。

## 安装依赖

    uv init
    uv add langchain deepagents
    uv sync

## 设置 API 密钥

从[任何支持的模型提供商](https://docs.langchain.com/oss/python/integrations/providers/overview)获取 API 密钥。例如：

    export OPENAI_API_KEY="your-api-key"
    export ANTHROPIC_API_KEY="your-api-key"
    export GOOGLE_API_KEY="your-api-key"

## 构建基本智能体

创建一个可以回答问题和调用工具的简单智能体：

    from langchain.agents import create_agent

    def get_weather(city: str) -> str:
        """获取指定城市的天气。"""
        return f"It's always sunny in {city}!"

    agent = create_agent(
        model="openai:gpt-5.4",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )
    print(result["messages"][-1].content_blocks)

智能体理解你正在询问旧金山的天气，因此使用提供的城市名称调用天气工具。

## 构建真实世界的智能体

以下示例构建一个可以回答文本文件问题的研究智能体，涵盖以下概念：

  1. **详细的系统提示**以获得更好的智能体行为
  2. **创建工具**与外部数据集成
  3. **模型配置**以获得一致的响应
  4. **对话记忆**用于聊天式交互
  5. **Deep Agents**提供内置功能
  6. **测试**你的智能体

### 定义系统提示

    SYSTEM_PROMPT = """你是一个文学数据助手。

    ## 能力

    - `fetch_text_from_url`: 从 URL 加载文档文本到对话中。
    不要猜测行数或位置——请以工具结果为准。"""

### 创建工具

    import urllib.error
    import urllib.request
    from langchain.tools import tool

    @tool
    def fetch_text_from_url(url: str) -> str:
        """从 URL 获取文档。"""
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                raw = resp.read()
        except urllib.error.URLError as e:
            return f"获取失败: {e}"
        text = raw.decode("utf-8", errors="replace")
        return text

### 配置模型

    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        "openai:gpt-5.4",
        temperature=0.5,
        timeout=300,
        max_tokens=25000,
    )

### 添加记忆

    from langgraph.checkpoint.memory import InMemorySaver

    checkpointer = InMemorySaver()

### 创建并运行智能体

    from langchain.agents import create_agent
    from deepagents import create_deep_agent

    agent = create_agent(
        model=model,
        tools=[fetch_text_from_url],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )

    deep_agent = create_deep_agent(
        model=model,
        tools=[fetch_text_from_url],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )

## 追踪智能体调用

使用 [LangSmith](https://smith.langchain.com/) 追踪、调试和评估你的智能体。

    export LANGSMITH_TRACING="true"
    export LANGSMITH_API_KEY="..."

## 下一步

你现在拥有的智能体可以：

  * **理解上下文**并记住对话
  * **智能使用工具**
  * **提供结构化响应**
  * **维护对话状态**
  * **规划、研究和综合**（仅 Deep Agents）
