# 加载数据（摄入）

在你选择的 LLM 处理数据之前，你首先需要处理和加载数据。这与 ML 预域的数据清理/特征工程流水线或传统数据设置中的 ETL 流水线类似。

摄入流水线通常包括三个主要阶段：
  1. 加载数据
  2. 转换数据
  3. 索引和存储数据

## 加载器（Loaders）

在你选择的 LLM 处理数据之前，你需要加载它。LlamaIndex 通过数据连接器（也称为 `Reader`）来实现这一点。数据连接器从不同数据源获取数据并将数据格式化为 `Document` 对象。`Document` 是数据的集合（目前是文本，未来包括图像和音频）以及关于该数据的元数据。

### 使用 SimpleDirectoryReader 加载

最简单的阅读器是 SimpleDirectoryReader，它为给定目录中的每个文件创建文档。它内置于 LlamaIndex，可以读取多种格式，包括 Markdown、PDF、Word 文档、PowerPoint、图像、音频和视频。

    from llama_index.core import SimpleDirectoryReader
    documents = SimpleDirectoryReader("./data").load_data()

### 使用 LlamaHub 的阅读器

因为有太多可能的数据来源，它们并非全部内置于核心库中。你可以从我们的数据连接器注册表 [LlamaHub](https://llamahub.ai/) 下载它们。

    from llama_index.readers.database import DatabaseReader
    reader = DatabaseReader(scheme=..., host=..., port=..., user=..., password=..., dbname=...)
    documents = reader.load_data(query="SELECT * FROM users")

### 直接创建 Document

    from llama_index.core import Document
    doc = Document(text="text")

## 转换（Transformations）

加载数据后，需要在将其放入存储系统之前处理和转换。这些转换包括分块、提取元数据和嵌入每个块。

转换的输入/输出是 `Node` 对象（`Document` 是 `Node` 的子类）。转换可以堆叠和重新排序。

### 高级转换 API

索引有 `.from_documents()` 方法，接受 Document 数组并正确解析和分块。

    from llama_index.core import VectorStoreIndex
    vector_index = VectorStoreIndex.from_documents(documents)

### 低级转换 API

你也可以显式定义这些步骤。

    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import TokenTextSplitter

    pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])
    nodes = pipeline.run(documents=documents)

### 添加元数据

    document = Document(text="text", metadata={"filename": "<doc_file_name>", "category": "<category>"})

### 添加嵌入

要将节点插入向量索引，它应具有嵌入。请参阅[摄入流水线](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline)或[嵌入指南](https://developers.llamaindex.ai/python/framework/module_guides/models/embeddings)。

### 直接创建和传递节点

    from llama_index.core.schema import TextNode
    node1 = TextNode(text="<text_chunk>", id_="<node_id>")
    index = VectorStoreIndex([node1, node2])
