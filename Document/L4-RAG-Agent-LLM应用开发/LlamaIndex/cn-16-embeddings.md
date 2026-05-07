# 嵌入模型（Embeddings）

嵌入模型将文本转换为数值向量表示，用于语义相似性搜索。LlamaIndex 支持多种嵌入模型提供商。

## 使用嵌入模型

    from llama_index.embeddings.openai import OpenAIEmbedding

    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    embeddings = embed_model.get_text_embedding("Hello, world!")
    print(len(embeddings))  # 1536 dimensions

## 支持的嵌入提供商

LlamaIndex 支持 50+ 种嵌入模型：

  * **OpenAI**：text-embedding-3-small、text-embedding-3-large、text-embedding-ada-002
  * **HuggingFace**：sentence-transformers、BGE、E5 等
  * **Cohere**：embed-english-v3.0、embed-multilingual-v3.0
  * **Google**：text-embedding-004、Gemini 嵌入
  * **本地模型**：Ollama、LlamaCPP、HuggingFace 本地推理
  * **其他**：MistralAI、VoyageAI、Jina、Nomic 等

## 配置嵌入模型

### 全局配置

    from llama_index.core import Settings
    from llama_index.embeddings.openai import OpenAIEmbedding

    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

### 本地嵌入（HuggingFace）

    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )
    Settings.embed_model = embed_model

### Ollama 嵌入

    from llama_index.embeddings.ollama import OllamaEmbedding

    embed_model = OllamaEmbedding(
        model_name="nomic-embed-text",
        base_url="http://localhost:11434"
    )

## 嵌入维度

不同嵌入模型产生不同维度的向量。选择模型时需考虑：
  * **维度越高**：通常捕获更多语义细节，但存储和计算成本更高
  * **维度越低**：更快、更节省存储，但可能丢失一些语义信息
