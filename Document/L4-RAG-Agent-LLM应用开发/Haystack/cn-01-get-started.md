跳转到主要内容

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/get-started>)

  * [2.29-unstable](</docs/next/get-started>)
  * [2.28](</docs/get-started>)
  * [2.27](</docs/2.27/get-started>)
  * [2.26](</docs/2.26/get-started>)
  * [2.25](</docs/2.25/get-started>)
  * [2.24](</docs/2.24/get-started>)
  * * * *

  * [1.x 归档文档](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x 归档文档](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[文档](</docs/intro>)[API 参考](</reference/>)

[贡献](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

搜索文档...

  * [简介](</docs/intro>)
  * [概览](</docs/installation>)

    * [安装](</docs/installation>)
    * [快速入门](</docs/get-started>)
    * [常见问题](</docs/faq>)
    * [遥测](</docs/telemetry>)
    * [破坏性变更政策](</docs/breaking-change-policy>)
    * [迁移指南](</docs/migration>)
    * [从 LangGraph/LangChain 迁移到 Haystack](</docs/migrating-from-langgraphlangchain-to-haystack>)
  * [Haystack 概念](</docs/concepts-overview>)

  * [文档存储](</docs/inmemorydocumentstore>)

  * [管道组件](</docs/agent>)

  * [工具](</docs/tool>)

  * [优化](</docs/evaluation>)

  * [开发](</docs/logging>)

  * [](</>)
  * 概览
  * 快速入门
版本: 2.28

本页内容

复制

# 快速入门

阅读本页了解如何快速上手 Haystack。本页包含安装说明、构建你的第一个 RAG 管道以及创建工具调用 Agent 的步骤。

## 构建你的第一个 RAG 应用

让我们来构建你的第一个检索增强生成（Retrieval Augmented Generation, RAG）管道，看看 Haystack 是如何回答问题的。

首先，安装 Haystack 的最小版本：

```shell
pip install haystack-ai
```

在下面的示例中，我们展示了如何使用 Haystack 的 Secret 设置 API 密钥。从下方的选项卡中选择你喜欢的 LLM 提供商。为方便使用，你也可以将 API 密钥设置为环境变量。

  * OpenAI
  * Hugging Face
  * Anthropic
  * Amazon Bedrock
  * Google Gemini
  * 更多提供商

OpenAIChatGenerator 已包含在 haystack-ai 包中。

```python
from haystack import Pipeline, Document
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import ChatPromptBuilder
from haystack.utils import Secret
from haystack.dataclasses import ChatMessage

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)

prompt_template = [
    ChatMessage.from_system(
        """
        Given these documents, answer the question.

        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        """,
    ),
    ChatMessage.from_user("{{question}}"),
]

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables="*")
llm = OpenAIChatGenerator(
    api_key=Secret.from_env_var("OPENAI_API_KEY"),
    model="gpt-4o-mini",
)

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "Who lives in Paris?"
results = rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    },
)

print(results["llm"]["replies"])
```

HuggingFaceAPIChatGenerator 已包含在 haystack-ai 包中。你可以获取免费的 Hugging Face 令牌来使用 Serverless Inference API。

```python
from haystack import Pipeline, Document
from haystack.components.generators.chat import HuggingFaceAPIChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import ChatPromptBuilder
from haystack.utils import Secret
from haystack.dataclasses import ChatMessage

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)

prompt_template = [
    ChatMessage.from_system(
        """
        Given these documents, answer the question.

        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        """,
    ),
    ChatMessage.from_user("{{question}}"),
]

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables="*")
llm = HuggingFaceAPIChatGenerator(
    api_type="serverless_inference_api",
    api_params={"model": "Qwen/Qwen2.5-72B-Instruct"},
    token=Secret.from_env_var("HF_API_TOKEN"),
)

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "Who lives in Paris?"
results = rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    },
)

print(results["llm"]["replies"])
```

安装 Anthropic 集成：

```bash
pip install anthropic-haystack
```

详见 AnthropicChatGenerator 文档。

```python
from haystack import Pipeline, Document
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import ChatPromptBuilder
from haystack.utils import Secret
from haystack.dataclasses import ChatMessage

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)

prompt_template = [
    ChatMessage.from_system(
        """
        Given these documents, answer the question.

        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        """,
    ),
    ChatMessage.from_user("{{question}}"),
]

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables="*")
llm = AnthropicChatGenerator(
    api_key=Secret.from_env_var("ANTHROPIC_API_KEY"),
    model="claude-sonnet-4-5-20250929",
)

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "Who lives in Paris?"
results = rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    },
)

print(results["llm"]["replies"])
```

安装 Amazon Bedrock 集成：

```bash
pip install amazon-bedrock-haystack
```

详见 AmazonBedrockChatGenerator 文档。

```python
import os
from haystack import Pipeline, Document
from haystack_integrations.components.generators.amazon_bedrock import (
    AmazonBedrockChatGenerator,
)
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage

os.environ["AWS_ACCESS_KEY_ID"] = "YOUR_AWS_ACCESS_KEY_ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "YOUR_AWS_SECRET_ACCESS_KEY"
os.environ["AWS_DEFAULT_REGION"] = "YOUR_AWS_REGION"

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)

prompt_template = [
    ChatMessage.from_system(
        """
        Given these documents, answer the question.

        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        """,
    ),
    ChatMessage.from_user("{{question}}"),
]

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables="*")
llm = AmazonBedrockChatGenerator(model="anthropic.claude-3-5-sonnet-20240620-v1:0")

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "Who lives in Paris?"
results = rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    },
)

print(results["llm"]["replies"])
```

安装 Google Gen AI 集成：

```bash
pip install google-genai-haystack
```

详见 GoogleGenAIChatGenerator 文档。

```python
from haystack import Pipeline, Document
from haystack_integrations.components.generators.google_genai import (
    GoogleGenAIChatGenerator,
)
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import ChatPromptBuilder
from haystack.utils import Secret
from haystack.dataclasses import ChatMessage

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)

prompt_template = [
    ChatMessage.from_system(
        """
        Given these documents, answer the question.

        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        """,
    ),
    ChatMessage.from_user("{{question}}"),
]

retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables="*")
llm = GoogleGenAIChatGenerator(
    api_key=Secret.from_env_var("GOOGLE_API_KEY"),
    model="gemini-2.5-flash",
)

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", retriever)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "Who lives in Paris?"
results = rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    },
)

print(results["llm"]["replies"])
```

Haystack 支持更多模型提供商，包括 Cohere、Mistral、NVIDIA、Ollama 等——涵盖云端托管和本地部署选项。

在生成器文档中浏览所有支持的模型和聊天生成器。

你也可以在 Haystack 集成页面上探索所有可用的集成。

### 后续步骤

准备深入了解？查看创建你的第一个带检索增强的问答管道教程，获取构建完整 RAG 管道的逐步指南。

## 构建你的第一个 Agent

Agent（智能体）是可以使用工具来收集信息、执行操作和与外部系统交互的 AI 系统。让我们构建一个能够搜索网页来回答问题的 Agent。

此示例需要 SerperDev API 密钥来进行网页搜索。将其设置为环境变量 SERPERDEV_API_KEY。

  * OpenAI
  * Hugging Face
  * Anthropic
  * Amazon Bedrock
  * Google Gemini
  * 更多提供商

OpenAIChatGenerator 已包含在 haystack-ai 包中。

```python
from haystack.components.agents import Agent
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch
from haystack.utils import Secret

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=OpenAIChatGenerator(
        api_key=Secret.from_env_var("OPENAI_API_KEY"),
        model="gpt-4o-mini",
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)
```

HuggingFaceAPIChatGenerator 已包含在 haystack-ai 包中。

```python
from haystack.components.agents import Agent
from haystack.components.generators.chat import HuggingFaceAPIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch
from haystack.utils import Secret

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=HuggingFaceAPIChatGenerator(
        api_type="serverless_inference_api",
        api_params={"model": "Qwen/Qwen2.5-72B-Instruct"},
        token=Secret.from_env_var("HF_API_TOKEN"),
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)
```

安装 Anthropic 集成：

```bash
pip install anthropic-haystack
```

```python
from haystack.components.agents import Agent
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch
from haystack.utils import Secret

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=AnthropicChatGenerator(
        api_key=Secret.from_env_var("ANTHROPIC_API_KEY"),
        model="claude-sonnet-4-5-20250929",
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)
```

安装 Amazon Bedrock 集成：

```bash
pip install amazon-bedrock-haystack
```

```python
import os
from haystack.components.agents import Agent
from haystack_integrations.components.generators.amazon_bedrock import (
    AmazonBedrockChatGenerator,
)
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch

os.environ["AWS_ACCESS_KEY_ID"] = "YOUR_AWS_ACCESS_KEY_ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "YOUR_AWS_SECRET_ACCESS_KEY"
os.environ["AWS_DEFAULT_REGION"] = "YOUR_AWS_REGION"

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=AmazonBedrockChatGenerator(
        model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)
```

安装 Google Gen AI 集成：

```bash
pip install google-genai-haystack
```

```python
from haystack.components.agents import Agent
from haystack_integrations.components.generators.google_genai import (
    GoogleGenAIChatGenerator,
)
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch
from haystack.utils import Secret

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=GoogleGenAIChatGenerator(
        api_key=Secret.from_env_var("GOOGLE_API_KEY"),
        model="gemini-2.5-flash",
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)
```

Haystack 支持更多模型提供商，包括 Cohere、Mistral、NVIDIA、Ollama 等——涵盖云端托管和本地部署选项。

在生成器文档中浏览所有支持的模型和聊天生成器。

你也可以在 Haystack 集成页面上探索所有可用的集成。

### 后续步骤

想要获取创建工具调用 Agent 的实践指南，该 Agent 可以将组件和管道作为工具使用，请查看构建工具调用 Agent 教程。

编辑此页面

上一节：安装 下一节：常见问题

  * 构建你的第一个 RAG 应用
    * 后续步骤
  * 构建你的第一个 Agent
    * 后续步骤

社区

  * Discord GitHub X

LinkedIn YouTube

学习

  * 教程
  * Cookbook

更多

  * 集成
  * 平台 - 免费试用
  * 企业支持

公司

  * 关于
  * 招聘
  * 博客

法律

  * 隐私政策
  * 法律声明

© 2026 deepset GmbH. 保留所有权利。
