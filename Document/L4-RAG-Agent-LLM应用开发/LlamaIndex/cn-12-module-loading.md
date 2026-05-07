# 加载模块指南

加载数据是 RAG 流水线的第一步。本指南涵盖 LlamaIndex 中的各种数据加载方法。

## 数据连接器（LlamaHub）

LlamaHub 提供了数百个数据连接器，用于从不同来源加载数据：

  * 文件阅读器：PDF、Word、Excel、Markdown 等
  * 数据库阅读器：SQL 数据库、MongoDB 等
  * 网页阅读器：网页爬虫、Notion、Google Docs 等
  * API 连接器：Slack、GitHub、Gmail 等

### LlamaParse

LlamaParse 是一流的文档解析解决方案，由视觉语言模型（VLM）驱动，适用于复杂文档（嵌套表格、嵌入式图表/图像等）。

## 文档和节点

  * **Document**：任何数据源的容器，包含文本和元数据
  * **Node**：数据的原子单位，表示文档的一个"块"

## 摄入流水线（Ingestion Pipeline）

声明式的数据处理流水线：

    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import TokenTextSplitter

    pipeline = IngestionPipeline(
        transformations=[
            TokenTextSplitter(chunk_size=512, chunk_overlap=20),
        ]
    )
    nodes = pipeline.run(documents=documents)

## 节点解析器（Node Parsers）

将文档拆分为节点的各种方法：
  * **SentenceSplitter**：基于句子分割
  * **TokenTextSplitter**：基于 token 数量分割
  * **HTMLNodeParser**：HTML 特定的分割
  * **JSONNodeParser**：JSON 特定的分割
  * **MarkdownNodeParser**：Markdown 特定的分割

## SimpleDirectoryReader

最简单的阅读器，从目录加载所有文件：

    from llama_index.core import SimpleDirectoryReader
    documents = SimpleDirectoryReader("data").load_data()
