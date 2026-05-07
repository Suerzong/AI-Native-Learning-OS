# 安装和设置

LlamaIndex 生态系统使用一组命名空间化的 Python 包构建。这意味着 `pip install llama-index` 包含一个核心入门包捆绑，其他集成可以按需安装。

## 快速安装

    pip install llama-index

这是一个入门包捆绑，包含：
  * `llama-index-core`
  * `llama-index-llms-openai`
  * `llama-index-embeddings-openai`
  * `llama-index-readers-file`

**注意**：`llama-index-core` 预先捆绑了 NLTK 和 tiktoken 文件，以避免运行时的下载和网络调用。

### 重要：OpenAI 环境设置

默认情况下，我们使用 OpenAI `gpt-3.5-turbo` 模型进行文本生成，使用 `text-embedding-ada-002` 进行检索和嵌入。你需要设置 `OPENAI_API_KEY` 环境变量。

你也可以[使用许多其他可用的 LLM](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/usage_custom)。

## 自定义安装

如果你不使用 OpenAI，或想要更有选择性的安装，可以单独安装所需的包。

例如，使用 Ollama 和 HuggingFace 嵌入的本地设置：

    pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface

## 从源码安装

    git clone https://github.com/run-llama/llama_index.git
    # 安装 poetry
    poetry self add poetry-plugin-shell
    poetry shell
    pip install -e llama-index-core
    poetry install --with dev,docs

从那里，你可以使用 `pip` 安装集成：

    pip install -e llama-index-integrations/readers/llama-index-readers-file
    pip install -e llama-index-integrations/llms/llama-index-llms-ollama
