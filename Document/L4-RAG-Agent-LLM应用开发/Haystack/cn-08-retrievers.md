[跳转到主要内容](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/retrievers>)

  * [2.29-unstable](</docs/next/retrievers>)
  * [2.28](</docs/retrievers>)
  * [2.27](</docs/2.27/retrievers>)
  * [2.26](</docs/2.26/retrievers>)
  * [2.25](</docs/2.25/retrievers>)
  * [2.24](</docs/2.24/retrievers>)
  * * * *

  * [1.x 归档文档](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x 归档文档](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[文档](</docs/intro>)[API 参考](</reference/>)

[贡献](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

搜索文档...

  * [简介](</docs/intro>)
  * [概览](</docs/installation>)

  * [Haystack 概念](</docs/concepts-overview>)

  * [文档存储](</docs/inmemorydocumentstore>)

  * [管道组件](</docs/agent>)

    * [智能体](</docs/agent>)
    * [音频](</docs/audio>)
    * [构建器](</docs/builders>)
    * [缓存](</docs/cachechecker>)
    * [分类器](</docs/classifiers>)
    * [连接器](</docs/connectors>)
    * [转换器](</docs/converters>)
    * [下载器](</docs/s3downloader>)
    * [嵌入器](</docs/embedders>)
    * [评估器](</docs/evaluators>)
    * [提取器](</docs/extractors>)
    * [获取器](</docs/fetchers>)
    * [生成器](</docs/generators>)
    * [合并器](</docs/joiners>)
    * [预处理器](</docs/preprocessors>)
    * [查询](</docs/queryexpander>)
    * [排序器](</docs/rankers>)
    * [阅读器](</docs/readers>)
    * [检索器](</docs/retrievers>)

      * [ArcadeDBEmbeddingRetriever](</docs/arcadedbembeddingretriever>)
      * [AstraEmbeddingRetriever](</docs/astraretriever>)
      * [AutoMergingRetriever](</docs/automergingretriever>)
      * [AzureAISearchBM25Retriever](</docs/azureaisearchbm25retriever>)
      * [AzureAISearchEmbeddingRetriever](</docs/azureaisearchembeddingretriever>)
      * [AzureAISearchHybridRetriever](</docs/azureaisearchhybridretriever>)
      * [ChromaEmbeddingRetriever](</docs/chromaembeddingretriever>)
      * [ChromaQueryTextRetriever](</docs/chromaqueryretriever>)
      * [ElasticsearchBM25Retriever](</docs/elasticsearchbm25retriever>)
      * [ElasticsearchEmbeddingRetriever](</docs/elasticsearchembeddingretriever>)
      * [FAISSEmbeddingRetriever](</docs/faissembeddingretriever>)
      * [FilterRetriever](</docs/filterretriever>)
      * [InMemoryBM25Retriever](</docs/inmemorybm25retriever>)
      * [InMemoryEmbeddingRetriever](</docs/inmemoryembeddingretriever>)
      * [MongoDBAtlasEmbeddingRetriever](</docs/mongodbatlasembeddingretriever>)
      * [MongoDBAtlasFullTextRetriever](</docs/mongodbatlasfulltextretriever>)
      * [MultiQueryEmbeddingRetriever](</docs/multiqueryembeddingretriever>)
      * [MultiQueryTextRetriever](</docs/multiquerytextretriever>)
      * [OpenSearchBM25Retriever](</docs/opensearchbm25retriever>)
      * [OpenSearchEmbeddingRetriever](</docs/opensearchembeddingretriever>)
      * [OpenSearchHybridRetriever](</docs/opensearchhybridretriever>)
      * [PgvectorEmbeddingRetriever](</docs/pgvectorembeddingretriever>)
      * [PgvectorKeywordRetriever](</docs/pgvectorkeywordretriever>)
      * [PineconeEmbeddingRetriever](</docs/pineconedenseretriever>)
      * [QdrantEmbeddingRetriever](</docs/qdrantembeddingretriever>)
      * [QdrantHybridRetriever](</docs/qdranthybridretriever>)
      * [QdrantSparseEmbeddingRetriever](</docs/qdrantsparseembeddingretriever>)
      * [SentenceWindowRetriever](</docs/sentencewindowretrieval>)
      * [SnowflakeTableRetriever](</docs/snowflaketableretriever>)
      * [ValkeyEmbeddingRetriever](</docs/valkeyembeddingretriever>)
      * [WeaviateBM25Retriever](</docs/weaviatebm25retriever>)
      * [WeaviateEmbeddingRetriever](</docs/weaviateembeddingretriever>)
      * [WeaviateHybridRetriever](</docs/weaviatehybridretriever>)
    * [路由器](</docs/routers>)

    * [采样器](</docs/toppsampler>)

    * [工具](</docs/toolinvoker>)

    * [翻译器](</docs/laradocumenttranslator>)

    * [验证器](</docs/jsonschemavalidator>)

    * [网页搜索](</docs/websearch>)

    * [写入器](</docs/documentwriter>)

  * [工具](</docs/tool>)

  * [优化](</docs/evaluation>)

  * [开发](</docs/logging>)

  * [](</>)
  * 管道组件
  * 检索器
版本: 2.28

本页内容

复制

# 检索器（Retrievers）

检索器遍历文档存储中的所有文档，选择与用户查询匹配的文档。

## 检索器如何工作？

检索器是大多数搜索系统的基本组件。它们用于检索增强生成（RAG）管道的检索部分，是文档检索管道的核心，也与阅读器（Reader）配对用于抽取式问答管道。

给定查询时，检索器筛选文档存储中的文档，为每个文档分配一个分数以表示其与查询的相关性，并返回最相关的候选文档。然后，它将选中的文档传递给管道中的下一个组件，或将其作为查询的答案返回。

需要注意的是，大多数基于稠密嵌入的检索器不会逐一比较每个文档与查询，而是使用近似技术以获得几乎相同的结果和更好的性能。

## 检索器类型

根据它们计算查询和文档之间相似度的方式，可以将检索器分为稀疏关键词检索器、稠密嵌入检索器和稀疏嵌入检索器。多种文档存储可以与不同类型的检索器配合使用。

### 稀疏关键词检索器

稀疏关键词检索器使用 BM25 算法或类似算法查找文档和查询之间共享的关键词。该算法计算文档和查询之间的加权词重叠。

主要特点：

  * 简单但有效，无需训练，开箱即用效果良好
  * 可以处理任何语言
  * 不考虑词序或语法
  * 无法处理未登录词（out-of-vocabulary words）
  * 适用于精确措辞很重要的使用场景
  * 无法处理同义词或含义相近的词

### 稠密嵌入检索器

稠密嵌入检索器使用嵌入（embedding）工作，嵌入是捕获词语语义的向量表示。稠密检索器首先需要[嵌入器](</docs/embedders>)将文档和查询转换为向量。然后，它计算查询与文档存储中每个文档的向量相似度，以获取最相关的文档。

主要特点：

  * 功能强大，但计算成本比稀疏检索器更高
  * 在标记数据集上训练
  * 是特定语言的，意味着它们只能在训练数据集的语言上工作。不过，多语言嵌入模型也是可用的。
  * 因为使用嵌入工作，它们考虑词序和语法
  * 在一定程度上可以处理未登录词

### 稀疏嵌入检索器

此类别包括 [SPLADE](<https://www.pinecone.io/learn/splade/>) 等方法。这些技术使用特定的嵌入模型结合了关键词检索器和稠密嵌入检索器的优点。

特别是，SPLADE 使用 BERT 等语言模型来衡量查询中不同术语的相关性，并执行自动术语扩展，减少词汇不匹配问题（查询和相关文档往往缺乏术语重叠）。

主要特点：

  * 在精确关键词匹配方面优于稠密嵌入检索器
  * 在语义匹配方面优于 BM25
  * 比 BM25 慢
  * 与 BM25 和稠密嵌入相比仍然处于实验阶段：支持的模型和文档存储较少

### 过滤检索器

`FilterRetriever` 是一种特殊类型的检索器，可以与所有文档存储配合使用，检索与提供的过滤器匹配的所有文档。

更多信息请阅读此检索器的[文档页面](</docs/filterretriever>)。

### 高级检索器技术

#### 组合检索器

你可以在一个管道中使用不同类型的检索器，以利用各自的优势并减轻劣势。有两种最常见的策略：组合稀疏和稠密检索器（混合检索），以及使用两个稠密检索器，每个使用不同的模型（多嵌入检索）。

##### 混合检索

你可以在一个管道中使用不同类型的检索器——稀疏和稠密——以利用它们的优势，使管道对不同类型的查询和文档更加鲁棒。当两个检索器都获取到候选文档后，你可以合并它们以生成最终排序并获取最相关的文档。

在我们的 [`DocumentJoiner` 文档](</docs/documentjoiner#in-a-pipeline>)中查看此方法的示例。

元数据过滤

在讨论混合检索时，某些数据库提供商指的是对稠密嵌入检索进行_元数据过滤_。虽然这与组合不同的检索器不同，但 Haystack 检索器通常支持此功能。更多信息请查看[元数据过滤页面](</docs/metadata-filtering>)。

混合检索器

一些文档存储在数据库层面提供混合检索。通常，这些方案可以提供更好的性能，但自定义选项较少（例如，关于如何合并不同检索技术的结果）。Haystack 提供了一些混合检索器，如 [`QdrantHybridRetriever`](</docs/qdranthybridretriever>)。如果你首选的文档存储没有可用的混合检索器，或者你想进一步自定义行为，请查看混合检索管道[教程](<https://haystack.deepset.ai/tutorials/33_hybrid_retrieval>)。

##### 多查询检索

多查询检索通过将单个用户查询扩展为多个语义相似的查询来提高召回率。每个查询变体可以捕获用户意图的不同方面，并匹配使用不同术语的文档。

此方法适用于基于文本和基于嵌入的检索器：

  * [`MultiQueryTextRetriever`](</docs/multiquerytextretriever>)：包装基于文本的检索器（如 BM25），并行运行多个查询。
  * [`MultiQueryEmbeddingRetriever`](</docs/multiqueryembeddingretriever>)：包装基于嵌入的检索器，并行运行多个查询。

要生成查询变体，使用 [`QueryExpander`](</docs/queryexpander>) 组件，它使用 LLM 从原始查询创建语义相似的查询。

##### 多嵌入检索

在此策略中，你使用两个基于嵌入的检索器，每个使用不同的模型来嵌入相同的文档。你最终会得到一个文档的多个嵌入表示。如果你需要多模态检索，这也很有用。

## 检索器与文档存储

检索器与[文档存储](</docs/document-store>)紧密耦合。大多数文档存储可以同时与稀疏或稠密检索器配合使用，或两种类型组合使用。查看特定文档存储的文档以了解它支持哪些检索器。

### 命名约定

Haystack 中的检索器名称由以下部分组成：

  * 文档存储名称 +
  * 检索方法 +
  * _Retriever_。

实际示例：

  * `ElasticsearchBM25Retriever`：BM25 是稀疏关键词检索技术，此检索器与 `ElasticsearchDocumentStore` 配合使用。
  * `ElasticsearchEmbeddingRetriever`：当未提及具体类型时，Embedding 指的是稠密嵌入，此检索器与 `ElasticsearchDocumentStore` 配合使用。
  * `QdrantSparseEmbeddingRetriever`（开发中）：稀疏嵌入是技术名称，此检索器与 `QdrantDocumentStore` 配合使用。

虽然我们尽量遵循此约定，但有时需要灵活处理以适应特定文档存储的功能。例如：

  * `ChromaQueryTextRetriever`：此检索器使用 Chroma 的查询 API 并期望文本输入。它与 `ChromaDocumentStore` 配合使用。

## FilterPolicy

`FilterPolicy` 决定在文档检索过程中如何应用过滤器。它控制检索器初始化时设置的静态过滤器与运行时提供的动态过滤器之间的交互。可能的值为：

  * **REPLACE**（默认）：任何运行时过滤器完全覆盖初始化过滤器。这允许特定查询动态更改过滤范围。
  * **MERGE**：将运行时过滤器与初始化过滤器合并，缩小搜索结果范围。

`FilterPolicy` 在选定检索器的 init 方法中设置，而 `filters` 可以在 init 和 run 方法中设置。

## 使用检索器

有关如何在管道中初始化和使用检索器的详细信息，请参阅特定检索器的文档。Haystack 中可用的检索器如下：

| 组件 | 描述 |
|------|------|
| [ArcadeDBEmbeddingRetriever](</docs/arcadedbembeddingretriever>) | 与 ArcadeDB 文档存储兼容的基于嵌入的检索器。 |
| [AstraEmbeddingRetriever](</docs/astraretriever>) | 与 AstraDocumentStore 兼容的基于嵌入的检索器。 |
| [AutoMergingRetriever](</docs/automergingretriever>) | 当多个相关片段匹配查询时，检索完整的父文档而非碎片化的块。 |
| [AzureAISearchEmbeddingRetriever](</docs/azureaisearchembeddingretriever>) | 与 Azure AI Search 文档存储兼容的嵌入检索器。 |
| [AzureAISearchBM25Retriever](</docs/azureaisearchbm25retriever>) | 从 Azure AI Search 文档存储中获取匹配查询的文档的关键词检索器。 |
| [AzureAISearchHybridRetriever](</docs/azureaisearchhybridretriever>) | 基于稠密和稀疏嵌入的检索器，与 Azure AI Search 文档存储兼容。 |
| [ChromaEmbeddingRetriever](</docs/chromaembeddingretriever>) | 与 Chroma 文档存储兼容的基于嵌入的检索器。 |
| [ChromaQueryTextRetriever](</docs/chromaqueryretriever>) | 与 Chroma 文档存储兼容的检索器，使用 Chroma 查询 API。 |
| [ElasticsearchEmbeddingRetriever](</docs/elasticsearchembeddingretriever>) | 与 Elasticsearch 文档存储兼容的基于嵌入的检索器。 |
| [ElasticsearchBM25Retriever](</docs/elasticsearchbm25retriever>) | 从 Elasticsearch 文档存储中获取匹配查询的文档的关键词检索器。 |
| [InMemoryBM25Retriever](</docs/inmemorybm25retriever>) | 与 InMemoryDocumentStore 兼容的关键词检索器。 |
| [InMemoryEmbeddingRetriever](</docs/inmemoryembeddingretriever>) | 与 InMemoryDocumentStore 兼容的基于嵌入的检索器。 |
| [FilterRetriever](</docs/filterretriever>) | 可与任何文档存储一起使用的特殊检索器，获取匹配特定过滤器的文档。 |
| [MultiQueryEmbeddingRetriever](</docs/multiqueryembeddingretriever>) | 使用基于嵌入的检索器并行运行多个查询来检索文档。 |
| [MultiQueryTextRetriever](</docs/multiquerytextretriever>) | 使用基于文本的检索器并行运行多个查询来检索文档。 |
| [MongoDBAtlasEmbeddingRetriever](</docs/mongodbatlasembeddingretriever>) | 与 MongoDB Atlas 文档存储兼容的嵌入检索器。 |
| [OpenSearchBM25Retriever](</docs/opensearchbm25retriever>) | 从 OpenSearch 文档存储中获取匹配查询的文档的关键词检索器。 |
| [OpenSearchEmbeddingRetriever](</docs/opensearchembeddingretriever>) | 与 OpenSearch 文档存储兼容的基于嵌入的检索器。 |
| [OpenSearchHybridRetriever](</docs/opensearchhybridretriever>) | 在单个组件中实现混合检索器的 SuperComponent，以 OpenSearch 为后端文档存储。 |
| [PgvectorEmbeddingRetriever](</docs/pgvectorembeddingretriever>) | 与 Pgvector 文档存储兼容的基于嵌入的检索器。 |
| [PgvectorKeywordRetriever](</docs/pgvectorkeywordretriever>) | 从 Pgvector 文档存储中获取匹配查询的文档的关键词检索器。 |
| [PineconeEmbeddingRetriever](</docs/pineconedenseretriever>) | 与 Pinecone 文档存储兼容的基于嵌入的检索器。 |
| [QdrantEmbeddingRetriever](</docs/qdrantembeddingretriever>) | 与 Qdrant 文档存储兼容的基于嵌入的检索器。 |
| [QdrantSparseEmbeddingRetriever](</docs/qdrantsparseembeddingretriever>) | 与 Qdrant 文档存储兼容的基于稀疏嵌入的检索器。 |
| [QdrantHybridRetriever](</docs/qdranthybridretriever>) | 基于稠密和稀疏嵌入的检索器，与 Qdrant 文档存储兼容。 |
| [SentenceWindowRetriever](</docs/sentencewindowretrieval>) | 检索相关句子周围的相邻句子以获取完整上下文。 |
| [SnowflakeTableRetriever](</docs/snowflaketableretriever>) | 连接到 Snowflake 数据库以执行 SQL 查询。 |
| [WeaviateBM25Retriever](</docs/weaviatebm25retriever>) | 从 Weaviate 文档存储中获取匹配查询的文档的关键词检索器。 |
| [WeaviateEmbeddingRetriever](</docs/weaviateembeddingretriever>) | 与 Weaviate 文档存储兼容的嵌入检索器。 |
| [WeaviateHybridRetriever](</docs/weaviatehybridretriever>) | 结合 BM25 关键词搜索和向量相似度，从 Weaviate 文档存储中获取文档。 |

[编辑此页面](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/pipeline-components/retrievers.mdx>)

[上一节：ExtractiveReader](</docs/extractivereader>)[下一节：ArcadeDBEmbeddingRetriever](</docs/arcadedbembeddingretriever>)

  * [检索器如何工作？](<#how-do-retrievers-work>)
  * [检索器类型](<#retriever-types>)
    * [稀疏关键词检索器](<#sparse-keyword-based-retrievers>)
    * [稠密嵌入检索器](<#dense-embedding-based-retrievers>)
    * [稀疏嵌入检索器](<#sparse-embedding-based-retrievers>)
    * [过滤检索器](<#filter-retriever>)
    * [高级检索器技术](<#advanced-retriever-techniques>)
  * [检索器与文档存储](<#retrievers-and-document-stores>)
    * [命名约定](<#naming-conventions>)
  * [FilterPolicy](<#filterpolicy>)
  * [使用检索器](<#using-a-retriever>)

社区

  * [![Discord](/img/discord.svg)](<https://discord.com/invite/haystack>)[![GitHub](/img/github.svg)](<https://github.com/deepset-ai/haystack>)[![X](/img/x.svg)](<https://x.com/haystack_ai>)

[![LinkedIn](/img/linkedin.svg)](<https://www.linkedin.com/company/deepset-ai/>)[![YouTube](/img/youtube.svg)](<https://www.youtube.com/channel/UC5dfn9m310oyt-cbeegfvZw>)

学习

  * [教程](<https://haystack.deepset.ai/tutorials>)
  * [Cookbook](<https://haystack.deepset.ai/cookbook>)

更多

  * [集成](<https://haystack.deepset.ai/integrations>)
  * [平台 - 免费试用](<https://landing.deepset.ai/deepset-studio-signup>)
  * [企业支持](<https://landing.deepset.ai/deepset-studio-signup>)

公司

  * [关于](<https://deepset.ai/about>)
  * [招聘](<https://deepset.ai/careers>)
  * [博客](<https://deepset.ai/blog>)

法律

  * [隐私政策](<https://www.deepset.ai/privacy-policy>)
  * [法律声明](<https://www.deepset.ai/imprint>)

© 2026 deepset GmbH. 保留所有权利。
