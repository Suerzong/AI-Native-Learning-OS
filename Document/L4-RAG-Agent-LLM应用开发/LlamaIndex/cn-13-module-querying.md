# 查询模块指南

查询是 RAG 流水线的核心阶段。本指南涵盖查询的各种组件和模式。

## 查询引擎

端到端的问答接口：

    query_engine = index.as_query_engine()
    response = query_engine.query("What is the main topic?")

## 检索器

定义如何从索引中高效检索相关上下文：

  * **向量检索器**：基于向量相似性检索
  * **关键词检索器**：基于关键词匹配检索
  * **混合检索器**：结合多种检索策略

## 路由器

根据查询类型选择最合适的检索器或查询引擎：

    from llama_index.core.query_engine import RouterQueryEngine
    from llama_index.core.selectors import PydanticSingleSelector

    query_engine = RouterQueryEngine(
        selector=PydanticSingleSelector.from_defaults(),
        query_engine_tools=[tool1, tool2]
    )

## 节点后处理器

对检索到的节点进行过滤、重新排序等后处理：

  * **SimilarityPostprocessor**：基于相似性分数过滤
  * **KeywordNodePostprocessor**：基于关键词过滤
  * **SentenceEmbeddingOptimizer**：优化嵌入以提高相关性
  * **CohereRerank**：使用 Cohere 重新排序
  * **LLMRerank**：使用 LLM 重新排序

## 响应合成器

根据检索到的节点和用户查询生成最终响应：

  * **CompactAndRefine**：默认模式，紧凑且逐步细化
  * **TreeSummarize**：递归总结为树形结构
  * **SimpleResponseBuilder**：简单响应生成

## 结构化输出

从查询中获取结构化数据：

    from pydantic import BaseModel

    class Output(BaseModel):
        answer: str
        confidence: float

    query_engine = index.as_query_engine(output_cls=Output)
