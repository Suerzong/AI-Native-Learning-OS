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

LangGraph overview

[Deep Agents](</oss/python/deepagents/overview>)[LangChain](</oss/python/langchain/overview>)[LangGraph](</oss/python/langgraph/overview>)[Integrations](</oss/python/integrations/providers/overview>)[Learn](</oss/python/learn>)[Reference](</oss/python/reference/overview>)[Contribute](</oss/python/contributing/overview>)

Python

  * [Overview](</oss/python/langgraph/overview>)

##### Get started

  * [Install](</oss/python/langgraph/install>)
  * [Quickstart](</oss/python/langgraph/quickstart>)
  * [Local server](</oss/python/langgraph/local-server>)
  * [Changelog](<https://docs.langchain.com/oss/python/releases/changelog>)
  * [Thinking in LangGraph](</oss/python/langgraph/thinking-in-langgraph>)
  * [Workflows + agents](</oss/python/langgraph/workflows-agents>)

##### Capabilities

  * [Persistence](</oss/python/langgraph/persistence>)
  * [Durable execution](</oss/python/langgraph/durable-execution>)
  * [Fault tolerance](</oss/python/langgraph/fault-tolerance>)
  * [Streaming](</oss/python/langgraph/streaming>)
  * [Interrupts](</oss/python/langgraph/interrupts>)
  * [Time travel](</oss/python/langgraph/use-time-travel>)
  * [Memory](</oss/python/langgraph/add-memory>)
  * [Subgraphs](</oss/python/langgraph/use-subgraphs>)

##### Production

  * [Application structure](</oss/python/langgraph/application-structure>)
  * [Test](</oss/python/langgraph/test>)
  * [Backward compatibility](</oss/python/langgraph/backward-compatibility>)
  * [LangSmith Studio](</oss/python/langgraph/studio>)
  * [Agent Chat UI](</oss/python/langgraph/ui>)
  * [LangSmith Deployment](</oss/python/langgraph/deploy>)
  * [LangSmith Observability](</oss/python/langgraph/observability>)

##### Frontend

  * [Overview](</oss/python/langgraph/frontend/overview>)
  * [Graph execution](</oss/python/langgraph/frontend/graph-execution>)

##### LangGraph APIs

  * Graph API

  * Functional API

  * [Runtime](</oss/python/langgraph/pregel>)

On this page

  * [ Install](<#install>)
  * [Core benefits](<#core-benefits>)
  * [LangGraph ecosystem](<#langgraph-ecosystem>)
  * [Acknowledgements](<#acknowledgements>)

# LangGraph overview

Copy page

Gain control with LangGraph to design agents that reliably handle complex tasks

Copy page

> ## Documentation Index
>
> Fetch the complete documentation index at: <https://docs.langchain.com/llms.txt>
>
> Use this file to discover all available pages before exploring further.

Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph is very low-level, and focused entirely on agent **orchestration**. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with [models](</oss/python/langchain/models>) and [tools](</oss/python/langchain/tools>). We will commonly use [LangChain](</oss/python/langchain/overview>) components throughout the documentation to integrate models and tools, but you don’t need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain’s [agents](</oss/python/langchain/agents>) that provide prebuilt architectures for common LLM and tool-calling loops. LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more.

Show How LangChain products fit together

  * [Deep Agents](</oss/python/deepagents/overview>) is an [agent harness](</oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk>): planning, subagents, filesystem tools, and context management on top of LangGraph.
  * [LangChain](</oss/python/langchain/overview>) is the agent framework: abstractions and integrations for models, tools, and agent loops.
  * [LangGraph](</oss/python/langgraph/overview>) is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
  * [LangSmith](</langsmith/home>) is the platform for tracing, evaluation, prompts, and deployment across frameworks.
  * [LangSmith Fleet](</langsmith/fleet/index>) is the no-code agent builder for templates, integrations, and routine automation.

Read [Frameworks, runtimes, and harnesses](</oss/python/concepts/products>) for a comparison of the open source stack.

##

[​](<#install>)

Install

pip

uv

    pip install -U langgraph

Then, create a simple hello world example:

    from langgraph.graph import StateGraph, MessagesState, START, END

    def mock_llm(state: MessagesState):
        return {"messages": [{"role": "ai", "content": "hello world"}]}

    graph = StateGraph(MessagesState)
    graph.add_node(mock_llm)
    graph.add_edge(START, "mock_llm")
    graph.add_edge("mock_llm", END)
    graph = graph.compile()

    graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})

Use [LangSmith](</langsmith/home>) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

##

[​](<#core-benefits>)

Core benefits

LangGraph provides low-level supporting infrastructure for _any_ long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:

  * [Durable execution](</oss/python/langgraph/durable-execution>): Build agents that persist through failures and can run for extended periods, resuming from where they left off.
  * [Human-in-the-loop](</oss/python/langgraph/interrupts>): Incorporate human oversight by inspecting and modifying agent state at any point.
  * [Comprehensive memory](</oss/python/concepts/memory>): Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions.
  * [Debugging with LangSmith](</langsmith/home>): Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
  * [Production-ready deployment](</langsmith/deployment>): Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

##

[​](<#langgraph-ecosystem>)

LangGraph ecosystem

While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc)

## LangSmith Observability

Trace requests, evaluate outputs, and monitor deployments in one place. Prototype locally with LangGraph, then move to production with integrated observability and evaluation to build more reliable agent systems.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deployment-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=024e3712d388bfa55f4f160cc9d6a85b](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deployment-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=024e3712d388bfa55f4f160cc9d6a85b)

## LangSmith Deployment

Deploy and scale agents effortlessly with a purpose-built deployment platform for long running, stateful workflows. Discover, reuse, configure, and share agents across teams — and iterate quickly with visual prototyping in Studio.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4)

## LangChain

Provides integrations and composable components to streamline LLM application development. Contains agent abstractions built on top of LangGraph.

Learn more

##

[​](<#acknowledgements>)

Acknowledgements

LangGraph is inspired by [Pregel](<https://research.google/pubs/pub37252/>) and [Apache Beam](<https://beam.apache.org/>). The public interface draws inspiration from [NetworkX](<https://networkx.org/documentation/latest/>). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

* * *

[Connect these docs](</use-these-docs>) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](<https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/overview.mdx>) or [file an issue](<https://github.com/langchain-ai/docs/issues/new/choose>).

Was this page helpful?

YesNo

[Install LangGraphNext](</oss/python/langgraph/install>)

⌘I

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](</>)

[github](<https://github.com/langchain-ai>)[x](<https://x.com/LangChain>)[linkedin](<https://www.linkedin.com/company/langchain>)[youtube](<https://www.youtube.com/@LangChain>)

Resources

[Forum](<https://forum.langchain.com/>)[Changelog](<https://changelog.langchain.com/>)[LangChain Academy](<https://academy.langchain.com/>)[Contact Sales](<https://www.langchain.com/contact-sales>)

Company

[Home](<https://langchain.com/>)[Trust Center](<https://trust.langchain.com/>)[Careers](<https://langchain.com/careers>)[Blog](<https://blog.langchain.com/>)

[github](<https://github.com/langchain-ai>)[x](<https://x.com/LangChain>)[linkedin](<https://www.linkedin.com/company/langchain>)[youtube](<https://www.youtube.com/@LangChain>)
