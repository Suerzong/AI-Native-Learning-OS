[跳转到主要内容](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/agents>)

  * [2.29-unstable](</docs/next/agents>)
  * [2.28](</docs/agents>)
  * [2.27](</docs/2.27/agents>)
  * [2.26](</docs/2.26/agents>)
  * [2.25](</docs/2.25/agents>)
  * [2.24](</docs/2.24/agents>)
  * * * *

  * [1.x 归档文档](</docs/faq#where-can-i-find-tutorials-and-documentation-for-haystack-1x>)
  * [2.x 归档文档](</docs/faq#where-can-i-find-documentation-for-older-haystack-versions>)

[文档](</docs/intro>)[API 参考](</reference/>)

[贡献](<https://github.com/deepset-ai/haystack/blob/main/docs-website/CONTRIBUTING.md>)[GitHub](<https://github.com/deepset-ai/haystack/tree/main/docs-website>)

搜索文档...

  * [简介](</docs/intro>)
  * [概览](</docs/installation>)

  * [Haystack 概念](</docs/concepts-overview>)

    * [Haystack 概念概览](</docs/concepts-overview>)
    * [智能体](</docs/agents>)

      * [State](</docs/state>)
    * [组件](</docs/components>)

    * [管道](</docs/pipelines>)

    * [数据类](</docs/data-classes>)

    * [文档存储](</docs/document-store>)

    * [元数据过滤](</docs/metadata-filtering>)
    * [设备管理](</docs/device-management>)
    * [密钥管理](</docs/secret-management>)
    * [Jinja 模板](</docs/jinja-templates>)
    * [集成简介](</docs/integrations>)
    * [实验性包](</docs/experimental-package>)
  * [文档存储](</docs/inmemorydocumentstore>)

  * [管道组件](</docs/agent>)

  * [工具](</docs/tool>)

  * [优化](</docs/evaluation>)

  * [开发](</docs/logging>)

  * [](</>)
  * Haystack 概念
  * 智能体
版本: 2.28

本页内容

复制

# 智能体（Agents）

本页介绍如何在 Haystack 中创建 AI 智能体（Agent），它能够检索信息、生成响应并使用各种 Haystack 组件执行操作。

## 什么是 AI 智能体？

AI 智能体是一个能够执行以下操作的系统：

  * 理解用户输入（文本、图像、音频和其他查询），
  * 检索相关信息（文档或结构化数据），
  * 生成智能响应（使用 OpenAI 或 Hugging Face 模型等 LLM），
  * 执行操作（调用 API、获取实时数据、执行函数）。

### 理解 AI 智能体

AI 智能体是使用大语言模型（LLM）进行决策和解决复杂任务的自主系统。它们通过工具、记忆和推理与环境交互。

### AI 智能体的构成

AI 智能体不仅仅是一个聊天机器人。它会主动规划、选择正确的工具并执行任务以实现目标。与传统软件不同，它能适应新信息并根据需要调整过程。

  1. **LLM 作为大脑**：智能体的核心是 LLM，它理解上下文、处理自然语言并作为中央智能系统。
  2. **用于交互的工具**：智能体连接到外部工具、API 和数据库，以收集信息并采取行动。
  3. **用于上下文的记忆**：短期记忆有助于跟踪对话，而长期记忆则存储知识以供将来交互使用。
  4. **推理与规划**：智能体分解复杂问题，制定分步行动计划，并根据新数据和反馈进行调整。

### AI 智能体如何工作

AI 智能体从定义其角色和目标的提示（prompt）开始。它决定何时使用工具、收集数据，并通过推理和行动的循环来完善其方法。它评估进展并调整策略以改善结果。

例如，客服智能体使用数据库回答查询。如果它缺乏答案，它会获取实时数据、总结并提供响应。编程助手理解项目需求、提出解决方案，甚至编写代码。

## 关键组件

### Agent 组件

Haystack 有一个通用的 [Agent](</docs/agent>) 组件，可以与基于聊天的 LLM 和工具交互以解决复杂查询。它需要一个支持工具的聊天生成器（Chat Generator）来工作，并且可以根据你的需求进行自定义。查看 [Agent](</docs/agent>) 文档或下面的[示例](<#tool-calling-agent>)以了解其工作方式。

### 附加组件

你可以在 Haystack 中自行构建 AI 智能体，使用管道中的三个主要元素：

  * [聊天生成器](</docs/generators>)用于使用 LLM 生成工具调用（包含工具名称和参数）或助手响应。
  * [`Tool`](</docs/tool>) 类允许 LLM 执行操作，例如运行管道或调用外部 API，连接外部世界。
  * [`ToolInvoker`](</docs/toolinvoker>) 组件用于执行 LLM 生成的工具调用。它解析 LLM 的工具调用响应，并使用管道中的正确参数调用相应的工具。

在 Haystack 中有三种创建工具的方式：

  * [`Tool`](</docs/tool>) 类——创建工具表示，实现跨所有生成器的一致工具调用体验。它允许最大程度的自定义，因为你可以定义自己的名称和描述。
  * [`ComponentTool`](</docs/componenttool>) 类——将 Haystack 组件包装为可调用工具。
  * [`@tool`](</docs/tool#tool-decorator>) 装饰器——从 Python 函数创建工具，自动使用函数名和文档字符串。
  * [Toolset](</docs/toolset>)——用于将多个工具分组的容器，可以直接传递给智能体或生成器。

## 示例智能体

### 工具调用智能体

你可以使用 `Agent` 组件创建类似的工具调用智能体：

```python
from haystack.components.agents import Agent
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.websearch import SerperDevWebSearch
from haystack.dataclasses import Document, ChatMessage
from haystack.tools.component_tool import ComponentTool

## 创建网页搜索组件
web_search = SerperDevWebSearch(top_k=3)

## 使用更简洁的参数创建 ComponentTool
web_tool = ComponentTool(
    component=web_search,
    name="web_search",
    description="Search the web for current information like weather, news, or facts.",
)

## 创建带有网页工具的智能体
tool_calling_agent = Agent(
    chat_generator=OpenAIChatGenerator(model="gpt-4o-mini"),
    system_prompt="""You're a helpful agent. When asked about current information like weather, news, or facts,
                     use the web_search tool to find the information and then summarize the findings.
                     When you get web search results, extract the relevant information and present it in a clear,
                     concise manner.""",
    tools=[web_tool],
)

## 使用用户消息运行智能体
user_message = ChatMessage.from_user("How is the weather in Berlin?")
result = tool_calling_agent.run(messages=[user_message])

## 打印结果 - 使用 .text 而不是 .content
print(result["messages"][-1].text)
```

运行结果：

```python
>>> The current weather in Berlin is approximately 60°F. The forecast for today includes clouds in the morning with some sunshine later. The high temperature is expected to be around 65°F, and the low tonight will drop to 40°F.

    - **Morning**: 49°F
    - **Afternoon**: 57°F
    - **Evening**: 47°F
    - **Overnight**: 39°F

    For more details, you can check the full forecasts on [AccuWeather](https://www.accuweather.com/en/de/berlin/10178/current-weather/178087) or [Weather.com](https://weather.com/weather/today/l/5ca23443513a0fdc1d37ae2ffaf5586162c6fe592a66acc9320a0d0536be1bb9).
```

### 带工具的管道

以下示例展示如何借助 `ToolInvoker` 构建工具调用智能体。

此代码示例的工作流程如下：

  1. `OpenAIChatGenerator` 使用 LLM 分析用户消息，决定是提供助手响应还是发起工具调用。
  2. `ConditionalRouter` 将 `OpenAIChatGenerator` 的输出路由到 `there_are_tool_calls` 分支（如果是工具调用）或 `final_replies`（直接返回给用户）。
  3. `ToolInvoker` 执行 LLM 生成的工具调用。`ComponentTool` 包装了 `SerperDevWebSearch` 组件，该组件获取实时搜索结果，使 `ToolInvoker` 能够将其作为工具执行。
  4. 工具提供输出后，`ToolInvoker` 将此信息连同 `MessageCollector` 存储的原始用户问题一起发送回 `OpenAIChatGenerator`。

```python
from haystack import component, Pipeline
from haystack.components.tools import ToolInvoker
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.routers import ConditionalRouter
from haystack.components.websearch import SerperDevWebSearch
from haystack.core.component.types import Variadic
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from typing import Any

## 辅助组件，用于在工具调用前临时存储最后的用户查询
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

## 从组件创建工具
web_tool = ComponentTool(component=SerperDevWebSearch(top_k=3))

## 定义路由条件
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

## 创建管道
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
```

运行结果：

```python
>>> The current weather in Berlin is around 46°F (8°C) with cloudy conditions. The high for today is forecasted to reach 48°F (9°C) and the low is expected to be around 37°F (3°C). The humidity is quite high at 92%, and there is a light wind blowing at 4 mph.

    For more detailed weather updates, you can check the following links:

    - [AccuWeather](https://www.accuweather.com/en/de/berlin/10178/weather-forecast/178087)
    - [Weather.com](https://weather.com/weather/today/l/5ca23443513a0fdc1d37ae2ffaf5586162c6fe592a66acc9320a0d0536be1bb9)
```

[编辑此页面](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/agents.mdx>)

[上一节：Haystack 概念概览](</docs/concepts-overview>)[下一节：State](</docs/state>)

  * [什么是 AI 智能体？](<#whats-an-ai-agent>)
    * [理解 AI 智能体](<#understanding-ai-agents>)
    * [AI 智能体的构成](<#what-makes-an-ai-agent>)
    * [AI 智能体如何工作](<#how-ai-agents-work>)
  * [关键组件](<#key-components>)
    * [Agent 组件](<#agents-1>)
    * [附加组件](<#additional-components>)
  * [示例智能体](<#example-agents>)
    * [工具调用智能体](<#tool-calling-agent>)
    * [带工具的管道](<#pipeline-with-tools>)

社区

  * [![Discord](/img/discord.svg)](<https://discord.com/invite/haystack>)[![GitHub](/img/github.svg)](<https://github.com/deepset-ai/haystack>)[![X](/img/x.svg)](<https://x.com/haystack_ai>)

[![LinkedIn](/img/linkedin.svg)](<https://www.linkedin.com/company/deepset-ai/>)[![YouTube](/img/youtube.svg)](<https://www.youtube.com/channel/UC5dfn9m310oyt-cbeegfvZw>)

学习

  * [教程](<https://haystack.deepset.ai/tutorials>)
  * [Cookbook](<https://haystack.deepset.ai/cookbook>)

更多

  * [集成](<https://haystack.deepset.ai/integrations>)
  * [平台 - 免费试用](<https://landing.deepset.ai/deepset-studio-signup>)
  * [企业支持](<https://landing.deepset.ai/deepset-studio-signup>)

公司

  * [关于](<https://deepset.ai/about>)
  * [招聘](<https://deepset.ai/careers>)
  * [博客](<https://deepset.ai/blog>)

法律

  * [隐私政策](<https://www.deepset.ai/privacy-policy>)
  * [法律声明](<https://www.deepset.ai/imprint>)

© 2026 deepset GmbH. 保留所有权利。
