# 欢迎使用 LlamaIndex！

LlamaIndex 是构建基于 [LLM](https://en.wikipedia.org/wiki/Large_language_model) 和[工作流](https://developers.llamaindex.ai/python/llamaagents/workflows)的智能体的领先框架。

## 什么是智能体？

[智能体](https://developers.llamaindex.ai/python/framework/understanding/agent)是 LLM 驱动的知识助手，使用工具执行研究、数据提取等任务。智能体的范围从简单的问题回答到能够感知、决策和采取行动以完成任务。

LlamaIndex 提供了构建智能体的框架，包括将 RAG 流水线作为众多工具之一来完成任务的能力。

## 什么是工作流？

[工作流](https://developers.llamaindex.ai/python/llamaagents/workflows)是多步骤过程，结合一个或多个智能体、数据连接器和其他工具来完成任务。它们是事件驱动的软件，允许你组合 RAG 数据源和多个智能体来创建复杂的应用程序。

## 什么是上下文增强？

LLM 在人类和数据之间提供了自然语言界面。LLM 在大量公开可用数据上进行了预训练，但它们没有在**你的**数据上训练。上下文增强使你的数据可供 LLM 使用以解决当前问题。

最流行的上下文增强示例是[检索增强生成（RAG）](https://developers.llamaindex.ai/python/framework/getting_started/concepts)，它在推理时将上下文与 LLM 结合。

## LlamaIndex 工具

  * **数据连接器**从原生来源和格式获取现有数据
  * **数据索引**以中间表示结构化数据，便于 LLM 使用
  * **引擎**提供对数据的自然语言访问（查询引擎、聊天引擎）
  * **智能体**是由工具增强的 LLM 驱动的知识工作者
  * **可观测性/评估**集成，支持严格的实验和监控
  * **工作流**将所有内容组合成事件驱动系统

## 用例

  * [问答](https://developers.llamaindex.ai/python/framework/use_cases/q_and_a)（RAG）
  * [聊天机器人](https://developers.llamaindex.ai/python/framework/use_cases/chatbots)
  * [文档理解和数据提取](https://developers.llamaindex.ai/python/framework/use_cases/extraction)
  * [自主智能体](https://developers.llamaindex.ai/python/framework/use_cases/agents)
  * [多模态应用](https://developers.llamaindex.ai/python/framework/use_cases/multimodal)
  * [微调](https://developers.llamaindex.ai/python/framework/use_cases/fine_tuning)

## 30 秒快速开始

    pip install llama-index

    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("关于数据的某个问题")
    print(response)

## LlamaCloud

LlamaCloud 是端到端托管服务，用于文档解析、提取、索引和检索：

  * **文档解析（LlamaParse）**：一流的文档解析解决方案，由 VLM 驱动
  * **文档提取（LlamaExtract）**：根据定义或推断的模式从任何文档提取结构化数据
  * **索引/检索**：设置端到端流水线为检索索引文档集合
