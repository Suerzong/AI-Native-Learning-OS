[Skip to main content](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack Documentation**](</>)

[2.28](</docs/retrievers>)

  * [2.29-unstable](</docs/next/retrievers>)
  * [2.28](</docs/retrievers>)
  * [2.27](</docs/2.27/retrievers>)
  * [2.26](</docs/2.26/retrievers>)
  * [2.25](</docs/2.25/retrievers>)
  * [2.24](</docs/2.24/retrievers>)
  * * * *

  * [1.x archived documentation](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x archived documentation](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[Docs](</docs/intro>)[API Reference](</reference/>)

[Contribute](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

🔍Search documentation...

  * [Introduction](</docs/intro>)
  * [Overview](</docs/installation>)

  * [Haystack Concepts](</docs/concepts-overview>)

  * [Document Stores](</docs/inmemorydocumentstore>)

  * [Pipeline Components](</docs/agent>)

    * [Agents](</docs/agent>)

    * [Audio](</docs/audio>)

    * [Builders](</docs/builders>)

    * [Caching](</docs/cachechecker>)

    * [Classifiers](</docs/classifiers>)

    * [Connectors](</docs/connectors>)

    * [Converters](</docs/converters>)

    * [Downloaders](</docs/s3downloader>)

    * [Embedders](</docs/embedders>)

    * [Evaluators](</docs/evaluators>)

    * [Extractors](</docs/extractors>)

    * [Fetchers](</docs/fetchers>)

    * [Generators](</docs/generators>)

    * [Joiners](</docs/joiners>)

    * [Preprocessors](</docs/preprocessors>)

    * [Query](</docs/queryexpander>)

    * [Rankers](</docs/rankers>)

    * [Readers](</docs/readers>)

    * [Retrievers](</docs/retrievers>)

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
    * [Routers](</docs/routers>)

    * [Samplers](</docs/toppsampler>)

    * [Tools](</docs/toolinvoker>)

    * [Translators](</docs/laradocumenttranslator>)

    * [Validators](</docs/jsonschemavalidator>)

    * [Websearch](</docs/websearch>)

    * [Writers](</docs/documentwriter>)

  * [Tools](</docs/tool>)

  * [Optimization](</docs/evaluation>)

  * [Development](</docs/logging>)

  * [](</>)
  * Pipeline Components
  * Retrievers
Version: 2.28

On this page

Copy

# Retrievers

Retrievers go through all the documents in a Document Store and select the ones that match the user query.

## How Do Retrievers Work?[​](<#how-do-retrievers-work> "Direct link to How Do Retrievers Work?")

Retrievers are the basic components of the majority of search systems. They’re used in the retrieval part of the retrieval-augmented generation (RAG) pipelines, they’re at the core of document retrieval pipelines, and they’re paired up with a Reader in extractive question answering pipelines.

When given a query, the Retriever sifts through the documents in the Document Store, assigns a score to each document to indicate how relevant it is to the query, and returns top candidates. It then passes the selected documents on to the next component in the pipeline or returns them as answers to the query.

Nevertheless, it's important to note that most Retrievers based on dense embedding do not compare each document with the query but use approximate techniques to achieve almost the same result with better performance.

## Retriever Types[​](<#retriever-types> "Direct link to Retriever Types")

Depending on how they calculate the similarity between the query and the document, you can divide Retrievers into sparse keyword-based, dense embedding-based, and sparse embedding-based. Several Document Stores can be coupled with different types of Retrievers.

### Sparse Keyword-Based Retrievers[​](<#sparse-keyword-based-retrievers> "Direct link to Sparse Keyword-Based Retrievers")

The sparse keyword-based Retrievers look for keywords shared between the documents and the query using the BM25 algorithm or similar ones. This algorithm computes a weighted world overlap between the documents and the query.

Main features:

  * Simple but effective, don’t need training, work quite well out of the box
  * Can work on any language
  * Don’t take word order or syntax into account
  * Can’t handle out-of-vocabulary words
  * Are good for use cases where precise wording matters
  * Can’t handle synonyms or words with similar meaning

### Dense Embedding-Based Retrievers[​](<#dense-embedding-based-retrievers> "Direct link to Dense Embedding-Based Retrievers")

Dense embedding-based Retrievers work with embeddings, which are vector representations of words that capture their semantics. Dense Retrievers need an [Embedder](</docs/embedders>) first to turn the documents and the query into vectors. Then, they calculate the vector similarity of the query and each document in the Document Store to fetch the most relevant documents.

Main features:

  * They’re powerful but also more expensive computationally than sparse Retrievers
  * They’re trained on labeled datasets
  * They’re language-specific, which means they can only work in the language of the dataset they were trained on. Nevertheless, multilingual embedding models are available.
  * Because they work with embeddings, they take word order and syntax into account
  * Can handle out-of-vocabulary words to a certain extent

### Sparse Embedding-Based Retrievers[​](<#sparse-embedding-based-retrievers> "Direct link to Sparse Embedding-Based Retrievers")

This category includes approaches such as [SPLADE](<https://www.pinecone.io/learn/splade/>). These techniques combine the positive aspects of keyword-based and dense embedding Retrievers using specific embedding models.

In particular, SPLADE uses Language Models like BERT to weigh the relevance of different terms in the query and perform automatic term expansions, reducing the vocabulary mismatch problem (queries and relevant documents often lack term overlap).

Main features:

  * Better than dense embedding Retrievers on precise keyword matching
  * Better than BM25 on semantic matching
  * Slower than BM25
  * Still experimental compared to both BM25 and dense embeddings: few models supported by few Document Stores

### Filter Retriever[​](<#filter-retriever> "Direct link to Filter Retriever")

`FilterRetriever` is a special kind of Retriever that can work with all Document Stores and retrieves all documents that match the provided filters.

For more information, read this Retriever's [documentation page](</docs/filterretriever>).

### Advanced Retriever Techniques[​](<#advanced-retriever-techniques> "Direct link to Advanced Retriever Techniques")

#### Combining Retrievers[​](<#combining-retrievers> "Direct link to Combining Retrievers")

You can use different types of Retrievers in one pipeline to take advantage of the strengths and mitigate the weaknesses of each of them. There are two most common strategies to do this: combining a sparse and dense Retriever (hybrid retrieval) and using two dense Retrievers, each with a different model (multi-embedding retrieval).

##### Hybrid Retrieval[​](<#hybrid-retrieval> "Direct link to Hybrid Retrieval")

You can use different Retriever types, sparse and dense, in one pipeline to take advantage of their strengths and make your pipeline more robust to different kinds of queries and documents. When both Retrievers fetch their candidate documents, you can combine them to produce the final ranking and get the top documents as a result.

See an example of this approach in our [`DocumentJoiner` docs](</docs/documentjoiner#in-a-pipeline>).

Metadata Filtering

When talking about hybrid retrieval, some database providers mean _metadata filtering_ on dense embedding retrieval. While this is different from combining different Retrievers, it is usually supported by Haystack Retrievers. For more information, check the [Metadata Filtering page](</docs/metadata-filtering>).

Hybrid Retrievers

Some Document Stores offer hybrid retrieval on the database side. In general, these solutions can be performant, but they offer fewer customization options (for instance, on how to merge results from different retrieval techniques). Some hybrid Retrievers are available in Haystack, such as [`QdrantHybridRetriever`](</docs/qdranthybridretriever>). If your preferred Document Store does not have a hybrid Retriever available or if you want to customize the behavior even further, check out the hybrid retrieval pipelines [tutorial](<https://haystack.deepset.ai/tutorials/33_hybrid_retrieval>).

##### Multi-Query Retrieval[​](<#multi-query-retrieval> "Direct link to Multi-Query Retrieval")

Multi-query retrieval improves recall by expanding a single user query into multiple semantically similar queries. Each query variation can capture different aspects of the user's intent and match documents that use different terminology.

This approach works with both text-based and embedding-based Retrievers:

  * [`MultiQueryTextRetriever`](</docs/multiquerytextretriever>): Wraps a text-based Retriever (such as BM25) and runs multiple queries in parallel.
  * [`MultiQueryEmbeddingRetriever`](</docs/multiqueryembeddingretriever>): Wraps an embedding-based Retriever and runs multiple queries in parallel.

To generate query variations, use the [`QueryExpander`](</docs/queryexpander>) component, which uses an LLM to create semantically similar queries from the original.

##### Multi-Embedding Retrieval[​](<#multi-embedding-retrieval> "Direct link to Multi-Embedding Retrieval")

In this strategy, you use two embedding-based Retrievers, each with a different model, to embed the same documents. You then end up having multiple embeddings of one document. It can also be handy if you need multimodal retrieval.

## Retrievers and Document Stores[​](<#retrievers-and-document-stores> "Direct link to Retrievers and Document Stores")

Retrievers are tightly coupled with [Document Stores](</docs/document-store>). Most Document Stores can work both with a sparse or a dense Retriever or both Retriever types combined. See the documentation of a specific Document Store to check which Retrievers it supports.

### Naming Conventions[​](<#naming-conventions> "Direct link to Naming Conventions")

The Retriever names in Haystack consist of:

  * Document Store name +
  * Retrieval method +
  * _Retriever_.

Practical examples:

  * `ElasticsearchBM25Retriever`: BM25 is a sparse keyword-based retrieval technique, and this Retriever works with `ElasticsearchDocumentStore`.
  * `ElasticsearchEmbeddingRetriever`: When not mentioned, Embedding stays for Dense Embedding, and this Retriever works with `ElasticsearchDocumentStore`.
  * `QdrantSparseEmbeddingRetriever` (in construction): Sparse Embedding is the technique, and this Retriever works with `QdrantDocumentStore`.

While we try to stick to this convention, there is sometimes a need to be flexible and accommodate features that are specific to a Document Store. For example:

  * `ChromaQueryTextRetriever`: This Retriever uses the query API of Chroma and expects text inputs. It works with `ChromaDocumentStore`.

## FilterPolicy[​](<#filterpolicy> "Direct link to FilterPolicy")

`FilterPolicy` determines how filters are applied during the document retrieval process. It controls the interaction between static filters set during Retriever initialization and dynamic filters provided at runtime. The possible values are:

  * **REPLACE** (default): Any runtime filters completely override the initialization filters. This allows specific queries to dynamically change the filtering scope.
  * **MERGE** : Combines runtime filters with initialization filters, narrowing down the search results.

The `FilterPolicy` is set in a selected Retriever's init method, while `filters` can be set in both init and run methods.

## Using a Retriever[​](<#using-a-retriever> "Direct link to Using a Retriever")

For details on how to initialize and use a Retriever in a pipeline, see the documentation for a specific Retriever. The following Retrievers are available in Haystack:

Component| Description| [ArcadeDBEmbeddingRetriever](</docs/arcadedbembeddingretriever>)| An embedding-based Retriever compatible with the ArcadeDB Document Store.| [AstraEmbeddingRetriever](</docs/astraretriever>)| An embedding-based Retriever compatible with the AstraDocumentStore.| [AutoMergingRetriever](</docs/automergingretriever>)| Retrieves complete parent documents instead of fragmented chunks when multiple related pieces match a query.| [AzureAISearchEmbeddingRetriever](</docs/azureaisearchembeddingretriever>)| An embedding Retriever compatible with the Azure AI Search Document Store.| [AzureAISearchBM25Retriever](</docs/azureaisearchbm25retriever>)| A keyword-based Retriever that fetches Documents matching a query from the Azure AI Search Document Store.| [AzureAISearchHybridRetriever](</docs/azureaisearchhybridretriever>)| A Retriever based both on dense and sparse embeddings, compatible with the Azure AI Search Document Store.| [ChromaEmbeddingRetriever](</docs/chromaembeddingretriever>)| An embedding-based Retriever compatible with the Chroma Document Store.| [ChromaQueryTextRetriever](</docs/chromaqueryretriever>)| A Retriever compatible with the Chroma Document Store that uses the Chroma query API.| [ElasticsearchEmbeddingRetriever](</docs/elasticsearchembeddingretriever>)| An embedding-based Retriever compatible with the Elasticsearch Document Store.| [ElasticsearchBM25Retriever](</docs/elasticsearchbm25retriever>)| A keyword-based Retriever that fetches Documents matching a query from the Elasticsearch Document Store.| [InMemoryBM25Retriever](</docs/inmemorybm25retriever>)| A keyword-based Retriever compatible with the InMemoryDocumentStore.| [InMemoryEmbeddingRetriever](</docs/inmemoryembeddingretriever>)| An embedding-based Retriever compatible with the InMemoryDocumentStore.| [FilterRetriever](</docs/filterretriever>)| A special Retriever to be used with any Document Store to get the Documents that match specific filters.| [MultiQueryEmbeddingRetriever](</docs/multiqueryembeddingretriever>)| Retrieves documents using multiple queries in parallel with an embedding-based Retriever.| [MultiQueryTextRetriever](</docs/multiquerytextretriever>)| Retrieves documents using multiple queries in parallel with a text-based Retriever.| [MongoDBAtlasEmbeddingRetriever](</docs/mongodbatlasembeddingretriever>)| An embedding Retriever compatible with the MongoDB Atlas Document Store.| [OpenSearchBM25Retriever](</docs/opensearchbm25retriever>)| A keyword-based Retriever that fetches Documents matching a query from an OpenSearch Document Store.| [OpenSearchEmbeddingRetriever](</docs/opensearchembeddingretriever>)| An embedding-based Retriever compatible with the OpenSearch Document Store.| [OpenSearchHybridRetriever](</docs/opensearchhybridretriever>)| A SuperComponent that implements a Hybrid Retriever in a single component, relying on OpenSearch as the backend Document Store.| [PgvectorEmbeddingRetriever](</docs/pgvectorembeddingretriever>)| An embedding-based Retriever compatible with the Pgvector Document Store.| [PgvectorKeywordRetriever](</docs/pgvectorkeywordretriever>)| A keyword-based Retriever that fetches documents matching a query from the Pgvector Document Store.| [PineconeEmbeddingRetriever](</docs/pineconedenseretriever>)| An embedding-based Retriever compatible with the Pinecone Document Store.| [QdrantEmbeddingRetriever](</docs/qdrantembeddingretriever>)| An embedding-based Retriever compatible with the Qdrant Document Store.| [QdrantSparseEmbeddingRetriever](</docs/qdrantsparseembeddingretriever>)| A sparse embedding-based Retriever compatible with the Qdrant Document Store.| [QdrantHybridRetriever](</docs/qdranthybridretriever>)| A Retriever based both on dense and sparse embeddings, compatible with the Qdrant Document Store.| [SentenceWindowRetriever](</docs/sentencewindowretrieval>)| Retrieves neighboring sentences around relevant sentences to get the full context.| [SnowflakeTableRetriever](</docs/snowflaketableretriever>)| Connects to a Snowflake database to execute an SQL query.| [WeaviateBM25Retriever](</docs/weaviatebm25retriever>)| A keyword-based Retriever that fetches Documents matching a query from the Weaviate Document Store.| [WeaviateEmbeddingRetriever](</docs/weaviateembeddingretriever>)| An embedding Retriever compatible with the Weaviate Document Store.| [WeaviateHybridRetriever](</docs/weaviatehybridretriever>)| Combines BM25 keyword search and vector similarity to fetch documents from the Weaviate Document Store.[Edit this page](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/pipeline-components/retrievers.mdx>)[PreviousExtractiveReader](</docs/extractivereader>)[NextArcadeDBEmbeddingRetriever](</docs/arcadedbembeddingretriever>)

  * [How Do Retrievers Work?](<#how-do-retrievers-work>)
  * [Retriever Types](<#retriever-types>)
    * [Sparse Keyword-Based Retrievers](<#sparse-keyword-based-retrievers>)
    * [Dense Embedding-Based Retrievers](<#dense-embedding-based-retrievers>)
    * [Sparse Embedding-Based Retrievers](<#sparse-embedding-based-retrievers>)
    * [Filter Retriever](<#filter-retriever>)
    * [Advanced Retriever Techniques](<#advanced-retriever-techniques>)
  * [Retrievers and Document Stores](<#retrievers-and-document-stores>)
    * [Naming Conventions](<#naming-conventions>)
  * [FilterPolicy](<#filterpolicy>)
  * [Using a Retriever](<#using-a-retriever>)
Community

  * [![Discord](/img/discord.svg)](<https://discord.com/invite/haystack>)[![GitHub](/img/github.svg)](<https://github.com/deepset-ai/haystack>)[![X](/img/x.svg)](<https://x.com/haystack_ai>)[![LinkedIn](/img/linkedin.svg)](<https://www.linkedin.com/company/deepset-ai/>)[![YouTube](/img/youtube.svg)](<https://www.youtube.com/channel/UC5dfn9m310oyt-cbeegfvZw>)
Learn

  * [Tutorials](<https://haystack.deepset.ai/tutorials>)
  * [Cookbooks](<https://haystack.deepset.ai/cookbook>)
More

  * [Integrations](<https://haystack.deepset.ai/integrations>)
  * [Platform - Try Free](<https://landing.deepset.ai/deepset-studio-signup>)
  * [Enterprise Support](<https://landing.deepset.ai/deepset-studio-signup>)
Company

  * [About](<https://deepset.ai/about>)
  * [Careers](<https://deepset.ai/careers>)
  * [Blog](<https://deepset.ai/blog>)
Legal

  * [Privacy Policy](<https://www.deepset.ai/privacy-policy>)
  * [Imprint](<https://www.deepset.ai/imprint>)
© 2026 deepset GmbH. All rights reserved.
