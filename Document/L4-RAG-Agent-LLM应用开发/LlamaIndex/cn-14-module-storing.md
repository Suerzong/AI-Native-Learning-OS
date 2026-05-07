# 存储模块指南

LlamaIndex 的存储系统允许你持久化索引和数据，避免重新处理。

## 向量存储

LlamaIndex 支持 40+ 种向量存储后端：

  * **内存**：SimpleVectorStore（默认，适合开发和测试）
  * **云端托管**：Pinecone、Weaviate、Qdrant、Milvus、Chroma、FAISS
  * **数据库集成**：PostgreSQL（pgvector）、MongoDB Atlas、Redis、Elasticsearch
  * **云服务**：Azure AI Search、Google Vertex AI、AWS OpenSearch

### 使用示例

    import chromadb
    from llama_index.vector_stores.chroma import ChromaVectorStore

    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = chroma_client.get_or_create_collection("my_collection")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    from llama_index.core import StorageContext
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

## 文档存储

存储文档和节点的原始内容：
  * 内存文档存储
  * MongoDB 文档存储
  * Redis 文档存储

## 索引存储

存储索引元数据和结构信息。

## 聊天存储

存储聊天历史以支持多轮对话：

    from llama_index.storage.chat_store.redis import RedisChatStore
    chat_store = RedisChatStore(redis_url="redis://localhost:6379")

## 持久化和加载

    # 持久化
    index.storage_context.persist(persist_dir="./storage")

    # 加载
    from llama_index.core import StorageContext, load_index_from_storage
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
