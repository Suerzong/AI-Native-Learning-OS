[Skip to main content](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack Documentation**](</>)

[2.28](</docs/agents>)

  * [2.29-unstable](</docs/next/agents>)
  * [2.28](</docs/agents>)
  * [2.27](</docs/2.27/agents>)
  * [2.26](</docs/2.26/agents>)
  * [2.25](</docs/2.25/agents>)
  * [2.24](</docs/2.24/agents>)
  * * * *

  * [1.x archived documentation](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x archived documentation](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[Docs](</docs/intro>)[API Reference](</reference/>)

[Contribute](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

🔍Search documentation...

  * [Introduction](</docs/intro>)
  * [Overview](</docs/installation>)

  * [Haystack Concepts](</docs/concepts-overview>)

    * [Haystack Concepts Overview](</docs/concepts-overview>)
    * [Agents](</docs/agents>)

      * [State](</docs/state>)
    * [Components](</docs/components>)

    * [Pipelines](</docs/pipelines>)

    * [Data Classes](</docs/data-classes>)

    * [Document Store](</docs/document-store>)

    * [Metadata Filtering](</docs/metadata-filtering>)
    * [Device Management](</docs/device-management>)
    * [Secret Management](</docs/secret-management>)
    * [Jinja Templates](</docs/jinja-templates>)
    * [Introduction to Integrations](</docs/integrations>)
    * [Experimental Package](</docs/experimental-package>)
  * [Document Stores](</docs/inmemorydocumentstore>)

  * [Pipeline Components](</docs/agent>)

  * [Tools](</docs/tool>)

  * [Optimization](</docs/evaluation>)

  * [Development](</docs/logging>)

  * [](</>)
  * Haystack Concepts
  * Agents
Version: 2.28

On this page

Copy

# Agents

This page explains how to create an AI agent in Haystack capable of retrieving information, generating responses, and taking actions using various Haystack components.

## What’s an AI Agent?[​](<#whats-an-ai-agent> "Direct link to What’s an AI Agent?")

An AI agent is a system that can:

  * Understand user input (text, image, audio, and other queries),
  * Retrieve relevant information (documents or structured data),
  * Generate intelligent responses (using LLMs like OpenAI or Hugging Face models),
  * Perform actions (calling APIs, fetching live data, executing functions).

### Understanding AI Agents[​](<#understanding-ai-agents> "Direct link to Understanding AI Agents")

AI agents are autonomous systems that use large language models (LLMs) to make decisions and solve complex tasks. They interact with their environment using tools, memory, and reasoning.

### What Makes an AI Agent[​](<#what-makes-an-ai-agent> "Direct link to What Makes an AI Agent")

An AI agent is more than a chatbot. It actively plans, chooses the right tools and executes tasks to achieve a goal. Unlike traditional software, it adapts to new information and refines its process as needed.

  1. **LLM as the Brain** : The agent's core is an LLM, which understands context, processes natural language and serves as the central intelligence system.
  2. **Tools for Interaction** : Agents connect to external tools, APIs, and databases to gather information and take action.
  3. **Memory for Context** : Short-term memory helps track conversations, while long-term memory stores knowledge for future interactions.
  4. **Reasoning and Planning** : Agents break down complex problems, come up with step-by-step action plans, and adapt based on new data and feedback.

### How AI Agents Work[​](<#how-ai-agents-work> "Direct link to How AI Agents Work")

An AI agent starts with a prompt that defines its role and objectives. It decides when to use tools, gathers data, and refines its approach through loops of reasoning and action. It evaluates progress and adjusts its strategy to improve results.

For example, a customer service agent answers queries using a database. If it lacks an answer, it fetches real-time data, summarizes it, and provides a response. A coding assistant understands project requirements, suggests solutions, and even writes code.

## Key Components[​](<#key-components> "Direct link to Key Components")

### Agents[​](<#agents-1> "Direct link to Agents")

Haystack has a universal [Agent](</docs/agent>) component that interacts with chat-based LLMs and tools to solve complex queries. It requires a Chat Generator that supports tools to work and can be customizable according to your needs. Check out the [Agent](</docs/agent>) documentation, or the [example](<#tool-calling-agent>) below to see how it works.

### Additional Components[​](<#additional-components> "Direct link to Additional Components")

You can build an AI agent in Haystack yourself, using the three main elements in a pipeline:

  * [Chat Generators](</docs/generators>) to generate tool calls (with tool name and arguments) or assistant responses with an LLM,
  * [`Tool`](</docs/tool>) class that allows the LLM to perform actions such as running a pipeline or calling an external API, connecting to the external world,
  * [`ToolInvoker`](</docs/toolinvoker>) component to execute tool calls generated by an LLM. It parses the LLM's tool-calling responses and invokes the appropriate tool with the correct arguments from the pipeline.

There are three ways of creating a tool in Haystack:

  * [`Tool`](</docs/tool>) class – Creates a tool representation for a consistent tool-calling experience across all Generators. It allows for most customization, as you can define its own name and description.
  * [`ComponentTool`](</docs/componenttool>) class – Wraps a Haystack component as a callable tool.
  * [`@tool`](</docs/tool#tool-decorator>) decorator – Creates tools from Python functions and automatically uses their function name and docstring.
  * [Toolset](</docs/toolset>) – A container for grouping multiple tools that can be passed directly to Agents or Generators.

## Example Agents[​](<#example-agents> "Direct link to Example Agents")

### Tool-Calling Agent[​](<#tool-calling-agent> "Direct link to Tool-Calling Agent")

You can create a similar tool-calling agent with the `Agent` component:

python

    from haystack.components.agents import Agent

    from haystack.components.generators.chat import OpenAIChatGenerator

    from haystack.components.websearch import SerperDevWebSearch

    from haystack.dataclasses import Document, ChatMessage

    from haystack.tools.component_tool import ComponentTool

    ## Create the web search component

    web_search = SerperDevWebSearch(top_k=3)

    ## Create the ComponentTool with simpler parameters

    web_tool = ComponentTool(

        component=web_search,

        name="web_search",

        description="Search the web for current information like weather, news, or facts.",

    )

    ## Create the agent with the web tool

    tool_calling_agent = Agent(

        chat_generator=OpenAIChatGenerator(model="gpt-4o-mini"),

        system_prompt="""You're a helpful agent. When asked about current information like weather, news, or facts,

                         use the web_search tool to find the information and then summarize the findings.

                         When you get web search results, extract the relevant information and present it in a clear,

                         concise manner.""",

        tools=[web_tool],

    )

    ## Run the agent with the user message

    user_message = ChatMessage.from_user("How is the weather in Berlin?")

    result = tool_calling_agent.run(messages=[user_message])

    ## Print the result - using .text instead of .content

    print(result["messages"][-1].text)

Resulting in:

python

    >>> The current weather in Berlin is approximately 60°F. The forecast for today includes clouds in the morning with some sunshine later. The high temperature is expected to be around 65°F, and the low tonight will drop to 40°F.

    - **Morning**: 49°F

    - **Afternoon**: 57°F

    - **Evening**: 47°F

    - **Overnight**: 39°F

    For more details, you can check the full forecasts on [AccuWeather](https://www.accuweather.com/en/de/berlin/10178/current-weather/178087) or [Weather.com](https://weather.com/weather/today/l/5ca23443513a0fdc1d37ae2ffaf5586162c6fe592a66acc9320a0d0536be1bb9).

### Pipeline With Tools[​](<#pipeline-with-tools> "Direct link to Pipeline With Tools")

Here’s an example of how you would build a tool-calling agent with the help of `ToolInvoker`.

This is what’s happening in this code example:

  1. `OpenAIChatGenerator` uses an LLM to analyze the user's message and determines whether to provide an assistant response or initiate a tool call.
  2. `ConditionalRouter` directs the output from the `OpenAIChatGenerator` to `there_are_tool_calls` branch if it’s a tool call or to `final_replies` to return to the user directly.
  3. `ToolInvoker` executes the tool call generated by the LLM. `ComponentTool` wraps the `SerperDevWebSearch` component that fetches real-time search results, making it accessible for `ToolInvoker` to execute it as a tool.
  4. After the tool provides its output, the `ToolInvoker` sends this information back to the `OpenAIChatGenerator`, along with the original user question stored by the `MessageCollector`.

python

    from haystack import component, Pipeline

    from haystack.components.tools import ToolInvoker

    from haystack.components.generators.chat import OpenAIChatGenerator

    from haystack.components.routers import ConditionalRouter

    from haystack.components.websearch import SerperDevWebSearch

    from haystack.core.component.types import Variadic

    from haystack.dataclasses import ChatMessage

    from haystack.tools import ComponentTool

    from typing import Any

    ## helper component to temporarily store last user query before the tool call

    @component()

    class MessageCollector:

        def __init__(self):

            self._messages = []

        @component.output_types(messages=list[ChatMessage])

        def run(self, messages: Variadic[list[ChatMessage]]) -> dict[str, Any]:

            self._messages.extend([msg for inner in messages for msg in inner])

            return {"messages": self._messages}

        def clear(self):

            self._messages = []

    ## Create a tool from a component

    web_tool = ComponentTool(component=SerperDevWebSearch(top_k=3))

    ## Define routing conditions

    routes = [

        {

            "condition": "{{replies[0].tool_calls | length > 0}}",

            "output": "{{replies}}",

            "output_name": "there_are_tool_calls",

            "output_type": list[ChatMessage],

        },

        {

            "condition": "{{replies[0].tool_calls | length == 0}}",

            "output": "{{replies}}",

            "output_name": "final_replies",

            "output_type": list[ChatMessage],

        },

    ]

    ## Create the pipeline

    tool_agent = Pipeline()

    tool_agent.add_component("message_collector", MessageCollector())

    tool_agent.add_component(

        "generator",

        OpenAIChatGenerator(model="gpt-4o-mini", tools=[web_tool]),

    )

    tool_agent.add_component("router", ConditionalRouter(routes, unsafe=True))

    tool_agent.add_component("tool_invoker", ToolInvoker(tools=[web_tool]))

    tool_agent.connect("generator.replies", "router")

    tool_agent.connect("router.there_are_tool_calls", "tool_invoker")

    tool_agent.connect("router.there_are_tool_calls", "message_collector")

    tool_agent.connect("tool_invoker.tool_messages", "message_collector")

    tool_agent.connect("message_collector", "generator.messages")

    messages = [

        ChatMessage.from_system(

            "You're a helpful agent choosing the right tool when necessary",

        ),

        ChatMessage.from_user("How is the weather in Berlin?"),

    ]

    result = tool_agent.run({"messages": messages})

    print(result["router"]["final_replies"][0].text)

Resulting in:

python

    >>> The current weather in Berlin is around 46°F (8°C) with cloudy conditions. The high for today is forecasted to reach 48°F (9°C) and the low is expected to be around 37°F (3°C). The humidity is quite high at 92%, and there is a light wind blowing at 4 mph.

    For more detailed weather updates, you can check the following links:

    - [AccuWeather](https://www.accuweather.com/en/de/berlin/10178/weather-forecast/178087)

    - [Weather.com](https://weather.com/weather/today/l/5ca23443513a0fdc1d37ae2ffaf5586162c6fe592a66acc9320a0d0536be1bb9)

[Edit this page](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/agents.mdx>)

[PreviousHaystack Concepts Overview](</docs/concepts-overview>)[NextState](</docs/state>)

  * [What’s an AI Agent?](<#whats-an-ai-agent>)
    * [Understanding AI Agents](<#understanding-ai-agents>)
    * [What Makes an AI Agent](<#what-makes-an-ai-agent>)
    * [How AI Agents Work](<#how-ai-agents-work>)
  * [Key Components](<#key-components>)
    * [Agents](<#agents-1>)
    * [Additional Components](<#additional-components>)
  * [Example Agents](<#example-agents>)
    * [Tool-Calling Agent](<#tool-calling-agent>)
    * [Pipeline With Tools](<#pipeline-with-tools>)

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
