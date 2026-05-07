# LangGraph 概述

LangGraph 是一个低级编排框架和运行时，用于构建、管理和部署长时间运行的有状态智能体。受到 Klarna、Uber、J.P. Morgan 等公司的信赖。

LangGraph 非常底层，完全专注于智能体**编排**。如果你刚接触智能体或需要更高级别的抽象，建议先使用 LangChain 的[智能体](https://docs.langchain.com/oss/python/langchain/agents)，它提供了常见 LLM 和工具调用循环的预构建架构。

## 安装

    pip install -U langgraph

创建一个简单的 Hello World 示例：

    from langgraph.graph import StateGraph, MessagesState, START, END

    def mock_llm(state: MessagesState):
        return {"messages": [{"role": "ai", "content": "hello world"}]}

    graph = StateGraph(MessagesState)
    graph.add_node(mock_llm)
    graph.add_edge(START, "mock_llm")
    graph.add_edge("mock_llm", END)
    graph = graph.compile()

    graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})

## 核心优势

LangGraph 为任何长时间运行的有状态工作流或智能体提供低级支持基础设施：

  * **持久执行（Durable execution）**：构建能够在故障中持久化并可以长时间运行的智能体，从停止处恢复。
  * **人机协作（Human-in-the-loop）**：通过在任意时刻检查和修改智能体状态来纳入人工监督。
  * **全面记忆（Comprehensive memory）**：创建具有短期工作记忆（用于持续推理）和跨会话长期记忆的有状态智能体。
  * **使用 LangSmith 调试**：通过可视化工具深入了解复杂的智能体行为。
  * **生产就绪的部署**：使用可扩展基础设施自信地部署复杂的智能体系统。

## LangGraph 生态系统

  * **Deep Agents**：智能体工具包——规划、子智能体、文件系统工具和上下文管理，基于 LangGraph。
  * **LangChain**：智能体框架——模型、工具和智能体循环的抽象和集成。
  * **LangGraph**：编排运行时——持久执行、流式传输、人机协作和持久化。
  * **LangSmith**：用于追踪、评估、提示和跨框架部署的平台。

## 致谢

LangGraph 受到 [Pregel](https://research.google/pubs/pub37252/) 和 [Apache Beam](https://beam.apache.org/) 的启发。公共接口借鉴了 [NetworkX](https://networkx.org/documentation/latest/)。
