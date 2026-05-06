Skip to main content

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack Documentation**](</>)

[2.28](</docs/get-started>)

  * [2.29-unstable](</docs/next/get-started>)
  * [2.28](</docs/get-started>)
  * [2.27](</docs/2.27/get-started>)
  * [2.26](</docs/2.26/get-started>)
  * [2.25](</docs/2.25/get-started>)
  * [2.24](</docs/2.24/get-started>)
  * * * *

  * [1.x archived documentation](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x archived documentation](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[Docs](</docs/intro>)[API Reference](</reference/>)

[Contribute](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

🔍Search documentation...

  * [Introduction](</docs/intro>)
  * [Overview](</docs/installation>)

    * [Installation](</docs/installation>)
    * [Get Started](</docs/get-started>)
    * [FAQ](</docs/faq>)
    * [Telemetry](</docs/telemetry>)
    * [Breaking Change Policy](</docs/breaking-change-policy>)
    * [Migration Guide](</docs/migration>)
    * [Migrating from LangGraph/LangChain to Haystack](</docs/migrating-from-langgraphlangchain-to-haystack>)
  * [Haystack Concepts](</docs/concepts-overview>)

  * [Document Stores](</docs/inmemorydocumentstore>)

  * [Pipeline Components](</docs/agent>)

  * [Tools](</docs/tool>)

  * [Optimization](</docs/evaluation>)

  * [Development](</docs/logging>)

  * [](</>)
  * Overview
  * Get Started
Version: 2.28

On this page

Copy

# Get Started

Have a look at this page to learn how to quickly get up and running with Haystack. It contains instructions for installing Haystack, building your first RAG pipeline, and creating a tool-calling Agent.

## Build your first RAG application​

Let's build your first Retrieval Augmented Generation (RAG) pipeline and see how Haystack answers questions.

First, install the minimal form of Haystack:

shell
    
    
    pip install haystack-ai  
    

In the examples below, we show how to set an API key using a Haystack [Secret](</docs/secret-management>). Choose your preferred LLM provider from the tabs below. For easier use, you can also set the API key as an environment variable.

  * OpenAI
  * Hugging Face
  * Anthropic
  * Amazon Bedrock
  * Google Gemini
  * More Providers

[OpenAIChatGenerator](</docs/openaichatgenerator>) is included in the `haystack-ai` package.

python
    
    
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
    

[HuggingFaceAPIChatGenerator](</docs/huggingfaceapichatgenerator>) is included in the `haystack-ai` package. You can get a [free Hugging Face token](<https://huggingface.co/settings/tokens>) to use the Serverless Inference API.

python
    
    
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
    

Install the [Anthropic integration](<https://haystack.deepset.ai/integrations/anthropic>):

bash
    
    
    pip install anthropic-haystack  
    

See the [AnthropicChatGenerator](</docs/anthropicchatgenerator>) docs for more details.

python
    
    
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
    

Install the [Amazon Bedrock integration](<https://haystack.deepset.ai/integrations/amazon-bedrock>):

bash
    
    
    pip install amazon-bedrock-haystack  
    

See the [AmazonBedrockChatGenerator](</docs/amazonbedrockchatgenerator>) docs for more details.

python
    
    
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
    

Install the [Google Gen AI integration](<https://haystack.deepset.ai/integrations/google-genai>):

bash
    
    
    pip install google-genai-haystack  
    

See the [GoogleGenAIChatGenerator](</docs/googlegenaichatgenerator>) docs for more details.

python
    
    
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
    

Haystack supports many more model providers including **Cohere** , **Mistral** , **NVIDIA** , **Ollama** , and others—both cloud-hosted and local options.

Browse the full list of supported models and chat generators in the [Generators documentation](</docs/generators>).

You can also explore all available integrations on the [Haystack Integrations](<https://haystack.deepset.ai/integrations>) page.

### Next Steps​

Ready to dive deeper? Check out the [Creating Your First QA Pipeline with Retrieval-Augmentation](<https://haystack.deepset.ai/tutorials/27_first_rag_pipeline>) tutorial for a step-by-step guide on building a complete RAG pipeline with your own data.

## Build your first Agent​

Agents are AI systems that can use tools to gather information, perform actions, and interact with external systems. Let's build an agent that can search the web to answer questions.

This example requires a [SerperDev API key](<https://serper.dev/>) for web search. Set it as the `SERPERDEV_API_KEY` environment variable.

  * OpenAI
  * Hugging Face
  * Anthropic
  * Amazon Bedrock
  * Google Gemini
  * More Providers

[OpenAIChatGenerator](</docs/openaichatgenerator>) is included in the `haystack-ai` package.

python
    
    
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
    

[HuggingFaceAPIChatGenerator](</docs/huggingfaceapichatgenerator>) is included in the `haystack-ai` package. You can get a [free Hugging Face token](<https://huggingface.co/settings/tokens>) to use the Serverless Inference API.

python
    
    
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
    

Install the [Anthropic integration](<https://haystack.deepset.ai/integrations/anthropic>):

bash
    
    
    pip install anthropic-haystack  
    

See the [AnthropicChatGenerator](</docs/anthropicchatgenerator>) docs for more details.

python
    
    
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
    

Install the [Amazon Bedrock integration](<https://haystack.deepset.ai/integrations/amazon-bedrock>):

bash
    
    
    pip install amazon-bedrock-haystack  
    

See the [AmazonBedrockChatGenerator](</docs/amazonbedrockchatgenerator>) docs for more details.

python
    
    
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
    

Install the [Google Gen AI integration](<https://haystack.deepset.ai/integrations/google-genai>):

bash
    
    
    pip install google-genai-haystack  
    

See the [GoogleGenAIChatGenerator](</docs/googlegenaichatgenerator>) docs for more details.

python
    
    
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
    

Haystack supports many more model providers including **Cohere** , **Mistral** , **NVIDIA** , **Ollama** , and others—both cloud-hosted and local options.

Browse the full list of supported models and chat generators in the [Generators documentation](</docs/generators>).

You can also explore all available integrations on the [Haystack Integrations](<https://haystack.deepset.ai/integrations>) page.

### Next Steps​

For a hands-on guide on creating a tool-calling agent that can use both components and pipelines as tools, check out the [Build a Tool-Calling Agent](<https://haystack.deepset.ai/tutorials/43_building_a_tool_calling_agent>) tutorial.

[Edit this page](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/overview/get-started.mdx>)

[PreviousInstallation](</docs/installation>)[NextFAQ](</docs/faq>)

  * Build your first RAG application
    * Next Steps
  * Build your first Agent
    * Next Steps

Community

  * [![Discord](/img/discord.svg)](<https://discord.com/invite/haystack>)[![GitHub](/img/github.svg)](<https://github.com/deepset-ai/haystack>)[![X](/img/x.svg)](<https://x.com/haystack_ai>)

[![LinkedIn](/img/linkedin.svg)](<https://www.linkedin.com/company/deepset-ai/>)[![YouTube](/img/youtube.svg)](<https://www.youtube.com/channel/UC5dfn9m310oyt-cbeegfvZw>)

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
