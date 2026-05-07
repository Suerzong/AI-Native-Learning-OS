# 索引（Indexing）

索引是 RAG 流水线的核心阶段。一旦数据被加载，LlamaIndex 帮助你将数据索引为易于检索的结构。

## 索引的工作原理

索引通常涉及生成**向量嵌入（Vector Embeddings）**——数据含义的数值表示——并将其存储在称为**向量存储（Vector Store）**的专用数据库中。索引还可以存储关于数据的各种元数据。

## 常用索引类型

  * **VectorStoreIndex**：最常用的索引类型，使用向量嵌入进行相似性搜索。这是大多数 RAG 应用的默认选择。
  * **属性图索引（Property Graph Index）**：构建知识图谱，捕获实体之间的关系。
  * **LlamaCloudIndex**：LlamaCloud 的托管索引服务。

## 核心概念

  * **嵌入（Embeddings）**：LLM 生成数据的数值表示。LlamaIndex 将查询转换为嵌入，向量存储找到与查询嵌入数值相似的数据。
  * **文档管理**：索引支持文档的增删改查操作。
  * **元数据提取**：自动从文档中提取元数据以增强检索。

## 使用 VectorStoreIndex

    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)

默认情况下，这使用内存中的简单向量存储。你可以配置其他[向量存储](https://developers.llamaindex.ai/python/framework/module_guides/storing/vector_stores/)（如 Pinecone、Chroma、Weaviate 等）。
