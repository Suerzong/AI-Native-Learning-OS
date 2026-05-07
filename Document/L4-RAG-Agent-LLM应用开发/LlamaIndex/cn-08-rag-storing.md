# 存储（Storing）

索引数据后，你通常需要存储索引和其他元数据，以避免重新索引。LlamaIndex 支持多种存储后端。

## 存储类型

  * **向量存储（Vector Stores）**：存储向量嵌入以进行相似性搜索。支持 Pinecone、Chroma、Weaviate、Qdrant、Milvus、FAISS 等数十种后端。
  * **文档存储（Document Stores）**：存储文档和节点的原始内容。
  * **索引存储（Index Stores）**：存储索引元数据。
  * **键值存储（Key-Value Stores）**：通用键值存储。
  * **聊天存储（Chat Stores）**：存储聊天历史。

## 持久化和加载

LlamaIndex 支持将索引持久化到磁盘并在以后重新加载：

    # 持久化到磁盘
    index.storage_context.persist(persist_dir="./storage")

    # 从磁盘重新加载
    from llama_index.core import StorageContext, load_index_from_storage

    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

## 自定义存储

你可以自定义存储组件，使用不同的后端来满足特定需求。例如，将向量存储配置为使用 Pinecone，文档存储使用 MongoDB 等。

## 配置向量存储

    import chromadb
    from llama_index.vector_stores.chroma import ChromaVectorStore

    chroma_client = chromadb.PersistentClient()
    chroma_collection = chroma_client.create_collection("my_collection")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
