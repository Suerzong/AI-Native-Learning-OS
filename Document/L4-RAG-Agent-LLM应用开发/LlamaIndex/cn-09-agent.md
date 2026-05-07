# 智能体（Agents）

智能体是由 LLM 驱动的知识工作者，通过工具增强，从简单的辅助函数到 API 集成等。智能体在推理循环中做出决策，选择要使用的工具并迭代地解决问题。

## 构建智能体

LlamaIndex 中的智能体使用 `AgentRunner` 和 `AgentWorker` 构建：

    from llama_index.core.agent import AgentRunner
    from llama_index.agent.openai import OpenAIAgentWorker

    # 创建工具
    from llama_index.core.tools import FunctionTool

    def multiply(a: int, b: int) -> int:
        return a * b

    multiply_tool = FunctionTool.from_defaults(fn=multiply)

    # 创建智能体
    agent = OpenAIAgentWorker.from_tools([multiply_tool], llm=llm, verbose=True)
    agent_runner = AgentRunner(agent)

    response = agent_runner.chat("What is 2 * 3?")
    print(response)

## 核心概念

  * **工具（Tools）**：智能体可以调用的函数或操作。可以是自定义函数、查询引擎或现有 API。
  * **记忆（Memory）**：智能体维护对话历史和状态。
  * **工具调用**：LLM 决定何时以及如何调用工具。
  * **迭代推理**：智能体在循环中工作，使用工具结果来指导下一步行动。

## 使用现有工具

LlamaIndex 提供了大量预构建工具和工具包，来自 [LlamaHub](https://llamahub.ai/)：

  * 搜索工具
  * 数据库查询工具
  * 代码解释器
  * API 集成工具

## 流式输出和事件

智能体支持流式输出，提供实时反馈：

    handler = agent_runner.stream_chat("Tell me a joke")
    for token in handler.stream_gen():
        print(token, end="")

## 人机协作

智能体支持人机协作模式，允许在关键步骤暂停并等待人工输入。

## 多智能体模式

LlamaIndex 支持多智能体协作模式，允许多个智能体分工协作完成复杂任务。

    from llama_index.core.agent import AgentRunner
    from llama_index.packs.multi_tool_agent import MultiToolAgentPack
