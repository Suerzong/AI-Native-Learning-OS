# 查询（Querying）

查询是 RAG 流水线的关键阶段，涉及从索引中检索相关信息并使用 LLM 生成响应。

## 查询引擎

查询引擎是端到端的流程，允许你对数据提问。它接收自然语言查询，返回响应以及检索到并传递给 LLM 的参考上下文。

    from llama_index.core import VectorStoreIndex

    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    print(response)

## 核心组件

### 检索器（Retrievers）

检索器定义了在给定查询时如何高效地从索引中检索相关上下文。检索策略是检索数据相关性和效率的关键。

### 路由器（Routers）

路由器确定使用哪个检索器从知识库中检索相关上下文。`RouterRetriever` 类负责选择一个或多个候选检索器来执行查询。

### 节点后处理器（Node Postprocessors）

节点后处理器接收一组检索到的节点，并对它们应用转换、过滤或重新排序逻辑。

  * **相似性后处理器**：基于相似性分数过滤节点
  * **关键词后处理器**：基于关键词过滤节点
  * **重新排序器**：使用交叉编码器重新排序节点

### 响应合成器（Response Synthesizers）

响应合成器使用 LLM 根据用户查询和一组检索到的文本块生成响应。

响应模式：
  * **紧凑（Compact）**：将所有相关文本块合并为一个提示
  * **细化（Refine）**：逐个处理文本块，逐步细化响应
  * **树形总结（Tree Summarize）**：递归地将文本块总结为树形结构
  * **简单（Simple）**：仅使用检索到的文本块作为上下文
