[Skip to main content](<#content-area>)

Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. [Buy tickets >](<https://interrupt.langchain.com/>)

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](</>)

![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source

Search...

⌘K

  * [Ask AI](<https://chat.langchain.com/>)
  * [GitHub](<https://github.com/langchain-ai>)
  * [Try LangSmith](<https://smith.langchain.com/>)
  * [Try LangSmith](<https://smith.langchain.com/>)

Search...

Navigation

LangChain overview

[Deep Agents](</oss/python/deepagents/overview>)[LangChain](</oss/python/langchain/overview>)[LangGraph](</oss/python/langgraph/overview>)[Integrations](</oss/python/integrations/providers/overview>)[Learn](</oss/python/learn>)[Reference](</oss/python/reference/overview>)[Contribute](</oss/python/contributing/overview>)

Python

  * [Overview](</oss/python/langchain/overview>)

##### Get started

  * [Install](</oss/python/langchain/install>)
  * [Quickstart](</oss/python/langchain/quickstart>)
  * [Changelog](<https://docs.langchain.com/oss/python/releases/changelog>)
  * [Philosophy](</oss/python/langchain/philosophy>)

##### Core components

  * [Agents](</oss/python/langchain/agents>)
  * [Models](</oss/python/langchain/models>)
  * [Messages](</oss/python/langchain/messages>)
  * [Tools](</oss/python/langchain/tools>)
  * [Short-term memory](</oss/python/langchain/short-term-memory>)
  * [Streaming](</oss/python/langchain/streaming>)
  * [Structured output](</oss/python/langchain/structured-output>)

##### Middleware

  * [Overview](</oss/python/langchain/middleware/overview>)
  * [Prebuilt middleware](</oss/python/langchain/middleware/built-in>)
  * [Custom middleware](</oss/python/langchain/middleware/custom>)

##### Frontend

  * [Overview](</oss/python/langchain/frontend/overview>)
  * Patterns

  * Integrations

##### Advanced usage

  * [Guardrails](</oss/python/langchain/guardrails>)
  * [Runtime](</oss/python/langchain/runtime>)
  * [Context engineering](</oss/python/langchain/context-engineering>)
  * [Model Context Protocol (MCP)](</oss/python/langchain/mcp>)
  * [Human-in-the-loop](</oss/python/langchain/human-in-the-loop>)
  * Multi-agent

  * [Retrieval](</oss/python/langchain/retrieval>)
  * [Long-term memory](</oss/python/langchain/long-term-memory>)

##### Agent development

  * [LangSmith Studio](</oss/python/langchain/studio>)
  * Test

  * [Agent Chat UI](</oss/python/langchain/ui>)

##### Deploy with LangSmith

  * [Deployment](</oss/python/langchain/deploy>)
  * [Observability](</oss/python/langchain/observability>)

On this page

  * [ Create an agent](<#create-an-agent>)
  * [ Core benefits](<#core-benefits>)

# LangChain overview

Copy page

LangChain is an open source framework with a prebuilt agent architecture and integrations for any model or tool—so you can build agents that adapt as fast as the ecosystem evolves

Copy page

> ## Documentation Index
>
> Fetch the complete documentation index at: <https://docs.langchain.com/llms.txt>
>
> Use this file to discover all available pages before exploring further.

Build completely custom agents and applications powered by LLMs in under 10 lines of code, with integrations for [OpenAI, Anthropic, Google, and more](</oss/python/integrations/providers/overview>). LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.

**LangChain vs. LangGraph vs. Deep Agents** Start with [Deep Agents](</oss/python/deepagents/overview>) for a “batteries-included” agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain [agents](</oss/python/langchain/agents>) which you can also use LangChain directly.Use [LangGraph](</oss/python/langgraph/overview>), our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.

##

[​](<#create-an-agent>)

Create an agent

OpenAI

Google Gemini

Claude (Anthropic)

OpenRouter

Fireworks

Baseten

Ollama

Azure

AWS Bedrock

HuggingFace

    # pip install -qU langchain "langchain[openai]"
    from langchain.agents import create_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_agent(
        model="openai:gpt-5.4",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )
    print(result["messages"][-1].content_blocks)

See the [Installation instructions](</oss/python/langchain/install>) and [Quickstart guide](</oss/python/langchain/quickstart>) to get started building your own agents and applications with LangChain.

Use [LangSmith](</langsmith/home>) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

##

[​](<#core-benefits>)

Core benefits

## Standard model interface

Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in.

Learn more

## Easy to use, highly flexible agent

LangChain’s agent abstraction is designed to be easy to get started with, letting you build a simple agent in under 10 lines of code. But it also provides enough flexibility to allow you to do all the context engineering your heart desires.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81)

## Built on top of LangGraph

LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc)

## Debug with LangSmith

Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.

Learn more

* * *

[Connect these docs](</use-these-docs>) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](<https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx>) or [file an issue](<https://github.com/langchain-ai/docs/issues/new/choose>).

Was this page helpful?

YesNo

[Install LangChainNext](</oss/python/langchain/install>)

⌘I

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](</>)

[github](<https://github.com/langchain-ai>)[x](<https://x.com/LangChain>)[linkedin](<https://www.linkedin.com/company/langchain>)[youtube](<https://www.youtube.com/@LangChain>)

Resources

[Forum](<https://forum.langchain.com/>)[Changelog](<https://changelog.langchain.com/>)[LangChain Academy](<https://academy.langchain.com/>)[Contact Sales](<https://www.langchain.com/contact-sales>)

Company

[Home](<https://langchain.com/>)[Trust Center](<https://trust.langchain.com/>)[Careers](<https://langchain.com/careers>)[Blog](<https://blog.langchain.com/>)

[github](<https://github.com/langchain-ai>)[x](<https://x.com/LangChain>)[linkedin](<https://www.linkedin.com/company/langchain>)[youtube](<https://www.youtube.com/@LangChain>)
