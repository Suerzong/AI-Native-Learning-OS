# LangChain 概述

LangChain 是一个开源框架，提供预构建的智能体架构和面向任何模型或工具的集成，让你可以构建能跟上生态系统发展速度的智能体。

用不到 10 行代码构建完全自定义的 LLM 驱动的智能体和应用程序，集成 [OpenAI、Anthropic、Google 等](https://docs.langchain.com/oss/python/integrations/providers/overview)。LangChain 提供预构建的智能体架构和模型集成，帮助你快速入门并无缝地将 LLM 融入你的智能体和应用程序。

## 创建智能体

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

使用 [LangSmith](https://smith.langchain.com/) 来追踪请求、调试智能体行为和评估输出。

## 核心优势

### 标准模型接口

不同提供商与模型交互的 API 各不相同。LangChain 标准化了你与模型的交互方式，使你可以无缝切换提供商并避免锁定。

### 易于使用、高度灵活的智能体

LangChain 的智能体抽象设计为易于上手，让你用不到 10 行代码即可构建简单的智能体。同时也提供了足够的灵活性来满足你所有的上下文工程需求。

### 基于 LangGraph 构建

LangChain 的智能体基于 LangGraph 构建，利用 LangGraph 的持久执行、人机协作支持和状态持久化等能力。

### 使用 LangSmith 调试

通过可视化工具深入了解复杂的智能体行为，追踪执行路径、捕获状态转换并提供详细的运行时指标。
