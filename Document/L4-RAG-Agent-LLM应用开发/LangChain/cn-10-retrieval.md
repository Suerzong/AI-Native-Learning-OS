# 检索（Retrieval）

检索是构建智能体的重要组成部分，使智能体能够访问和利用外部数据源来增强其响应能力。

## 概述

检索增强生成（RAG）是一种技术，允许模型在生成响应前从外部数据源检索相关信息。这对于以下场景非常有用：

  * 智体需要访问最新的或领域特定的信息
  * 智体需要引用特定文档或知识库
  * 减少模型幻觉，提供基于事实的响应

## LangChain 中的检索

LangChain 提供了检索的构建模块，包括：

  * **文档加载器（Document Loaders）**——从各种来源加载文档（PDF、网页、数据库等）
  * **文本分割器（Text Splitters）**——将长文档分割为较小的块
  * **嵌入模型（Embedding Models）**——将文本转换为向量表示
  * **向量存储（Vector Stores）**——存储和检索文档嵌入
  * **检索器（Retrievers）**——根据查询检索相关文档

## 使用工具进行检索

在 LangChain 中，检索通常通过工具来实现。智能体可以使用检索工具来查询外部数据：

    from langchain.tools import tool

    @tool
    def search_knowledge_base(query: str) -> str:
        """搜索知识库获取相关信息。"""
        # 实现检索逻辑
        results = vector_store.similarity_search(query, k=3)
        return "\n".join([doc.page_content for doc in results])

## RAG 智能体

构建 RAG 智能体的关键步骤：

  1. 准备文档并创建向量存储
  2. 创建检索工具
  3. 将检索工具添加到智能体
  4. 智体在需要时自动调用检索工具

更多详情请参阅 [LangChain RAG 教程](https://docs.langchain.com/oss/python/langchain/rag)和[向量存储集成](https://docs.langchain.com/oss/python/integrations/vectorstores)页面。
