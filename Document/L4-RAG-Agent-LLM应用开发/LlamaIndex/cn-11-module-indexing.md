# 索引模块指南

索引是 LlamaIndex 中数据结构化和检索的核心。本指南涵盖各种索引类型及其使用方法。

## 索引类型

### VectorStoreIndex

最常用的索引类型。使用向量嵌入进行相似性搜索：

    from llama_index.core import VectorStoreIndex
    index = VectorStoreIndex.from_documents(documents)

### 属性图索引（Property Graph Index）

构建知识图谱以捕获实体关系：

    from llama_index.core.indices.property_graph import PropertyGraphIndex
    pg_index = PropertyGraphIndex.from_documents(documents)

### LlamaCloudIndex

LlamaCloud 的托管索引服务，提供端到端的文档处理和检索。

## 索引操作

  * **文档管理**：添加、更新和删除索引中的文档
  * **元数据提取**：自动从文档中提取元数据
  * **索引指南**：了解每种索引的工作原理，选择最适合你用例的索引

## 核心模块

  * [VectorStoreIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index)
  * [属性图索引指南](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide)
  * [LlamaCloudIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/llama_cloud_index)
  * [文档管理](https://developers.llamaindex.ai/python/framework/module_guides/indexing/document_management)
  * [元数据提取](https://developers.llamaindex.ai/python/framework/module_guides/indexing/metadata_extraction)
