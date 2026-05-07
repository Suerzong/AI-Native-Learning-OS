# 综合运用

本节展示如何将 LlamaIndex 的各个组件组合在一起构建完整的应用程序。

## 智能体

构建自主智能体，使用工具和推理循环来完成复杂任务。

## 应用程序

### 全栈 Web 应用

使用 LlamaIndex 构建全栈 Web 应用程序的指南，包括前端和后端。

### 聊天机器人

使用 LlamaIndex 构建聊天机器人：

    from llama_index.core.memory import ChatMemoryBuffer

    memory = ChatMemoryBuffer.from_defaults(token_limit=3000)
    chat_engine = index.as_chat_engine(
        chat_mode="condense_plus_context",
        memory=memory,
        system_prompt="You are a helpful assistant."
    )

    response = chat_engine.chat("Hello!")

### 问答模式

各种问答模式的示例和最佳实践，包括：
  * 基于文档的问答
  * 多轮对话
  * 结合多种数据源

### 结构化数据

处理结构化数据（SQL 数据库、CSV、API）的指南。

## 隐私和安全

关于在 LlamaIndex 应用程序中处理隐私和安全的指南。
