# 大语言模型（LLMs）

LLM 是 LlamaIndex 的核心推理引擎。本指南涵盖如何使用和配置各种 LLM。

## 使用 LLM

### 全局配置

    from llama_index.core import Settings
    from llama_index.llms.openai import OpenAI

    Settings.llm = OpenAI(model="gpt-4o")

### 独立使用

    from llama_index.llms.openai import OpenAI

    llm = OpenAI(model="gpt-4o")
    response = llm.complete("Explain quantum computing in one sentence.")
    print(response.text)

### 聊天模式

    from llama_index.core.llms import ChatMessage, MessageRole

    messages = [
        ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant."),
        ChatMessage(role=MessageRole.USER, content="What is the meaning of life?")
    ]
    response = llm.chat(messages)

## 支持的 LLM 提供商

LlamaIndex 支持 80+ 种 LLM 集成：

  * **OpenAI**：GPT-4o、GPT-4、GPT-3.5-turbo
  * **Anthropic**：Claude 3.5 Sonnet、Claude 3 Opus/Haiku
  * **Google**：Gemini Pro、Gemini Flash
  * **本地模型**：Ollama、LlamaCPP、HuggingFace、vLLM
  * **云服务**：AWS Bedrock、Azure OpenAI、Google Vertex AI
  * **其他**：MistralAI、Cohere、Groq、Together AI 等

## 本地 LLM

### Ollama

    from llama_index.llms.ollama import Ollama

    llm = Ollama(model="llama3", request_timeout=120.0)
    response = llm.complete("Hello!")

### LlamaCPP

    from llama_index.llms.llama_cpp import LlamaCPP

    llm = LlamaCPP(
        model_url="https://huggingface.co/...",
        model_kwargs={"n_gpu_layers": 1}
    )

## 自定义 LLM

你可以将任何 LLM 包装为 LlamaIndex 兼容的接口：

    from llama_index.core.llms import CustomLLM

    class MyLLM(CustomLLM):
        @property
        def metadata(self):
            return LLMMetadata(context_window=4096, num_output=256)

        def complete(self, prompt, **kwargs):
            # 你的自定义 LLM 调用
            return CompletionResponse(text="custom response")
