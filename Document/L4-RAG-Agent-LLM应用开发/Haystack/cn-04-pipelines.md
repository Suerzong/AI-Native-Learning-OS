[跳转到主要内容](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/pipelines>)

  * [2.29-unstable](</docs/next/pipelines>)
  * [2.28](</docs/pipelines>)
  * [2.27](</docs/2.27/pipelines>)
  * [2.26](</docs/2.26/pipelines>)
  * [2.25](</docs/2.25/pipelines>)
  * [2.24](</docs/2.24/pipelines>)
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

    * [组件](</docs/components>)

    * [管道](</docs/pipelines>)

      * [创建管道](</docs/creating-pipelines>)
      * [序列化管道](</docs/serialization>)
      * [可视化 Haystack 管道](</docs/visualizing-pipelines>)
      * [调试管道](</docs/debugging-pipelines>)
      * [管道断点](</docs/pipeline-breakpoints>)
      * [管道循环](</docs/pipeline-loops>)
      * [AsyncPipeline](</docs/asyncpipeline>)
      * [智能管道连接](</docs/smart-pipeline-connections>)
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
  * 管道
版本: 2.28

本页内容

复制

# 管道（Pipelines）

要使用 LLM 构建现代搜索管道，你需要两样东西：强大的组件和将它们组合在一起的简便方式。Haystack 管道正是为此而构建的，使你能够设计和扩展与 LLM 的交互。

Haystack 中的管道是由不同 Haystack 组件和集成组成的有向多重图（directed multigraph）。它们让你可以自由地以各种方式连接这些组件。这意味着管道不需要是连续的信息流。借助 Haystack 管道的灵活性，你可以拥有同时运行的流、独立组件、循环和其他类型的连接。

## 灵活性

Haystack 管道不仅仅是查询和索引管道。管道的功能——无论是索引、查询、从 API 获取数据、预处理还是其他——完全取决于你如何设计管道以及使用哪些组件。虽然你仍然可以创建单一功能的管道，比如使用现成组件清理、分割文档并将其写入文档存储的索引管道，或者只是接收查询并返回答案的查询管道，但 Haystack 还允许你通过决策组件（如 `ConditionalRouter`）将多个用例组合到一个管道中。

### Agentic 管道

Haystack 的循环和分支功能使创建复杂应用（如智能体）成为可能。以下是一些创建方法的示例：

  * [教程：构建带函数调用的聊天 Agent](<https://haystack.deepset.ai/tutorials/40_building_chat_application_with_function_calling>)
  * [教程：构建带回退到网页搜索的 Agentic RAG](<https://haystack.deepset.ai/tutorials/36_building_fallbacks_with_conditional_routing>)
  * [教程：使用基于循环的自动纠错生成结构化输出](<https://haystack.deepset.ai/tutorials/28_structured_output_with_loop>)
  * [Cookbook：定义和运行工具](<https://haystack.deepset.ai/cookbook/tools_support>)
  * [Cookbook：使用 Memory 的对话式 RAG](<https://haystack.deepset.ai/cookbook/conversational_rag_using_memory>)
  * [Cookbook：使用实验性 Haystack 工具的新闻通讯发送 Agent](<https://haystack.deepset.ai/cookbook/newsletter-agent>)

### 分支

管道可以有多个同时处理数据的分支。例如，要处理不同类型的文件，你可以创建一个包含多个转换器的管道，每个转换器处理特定的文件类型。然后你将所有文件输入管道，它会智能地将它们分配并路由到相应的转换器，省去逐个发送文件的麻烦。

![管道架构图，展示排列在并行分支中然后汇聚到单个管道流的组件](/img/83f686b-Pipeline_Illustrations_1_1.png)

### 循环

管道中的组件可以在迭代循环中工作，你可以限制循环次数。这在自纠错循环等场景中非常有用：生成器产生输出，然后验证器组件检查输出是否正确。如果生成器的输出有错误，验证器组件可以将输出回传给生成器以获取修正后的输出。循环持续进行，直到输出通过验证并可以继续在管道中传递。

请参阅[管道循环](</docs/pipeline-loops>)深入了解循环的执行方式、终止条件以及安全使用方法。

![管道架构图，展示来自后续组件的输出循环回到早期组件的反馈回路](/img/2390eea-Pipeline_Illustrations_1_2.png)

### 异步管道

AsyncPipeline 在依赖关系允许时，支持并行执行 Haystack 组件。这在具有独立操作的复杂管道中可以提高性能。例如，它可以同时运行多个检索器或 LLM 调用、并行执行独立的管道分支，以及高效处理原本会导致延迟的 I/O 密集型操作。通过并发执行，AsyncPipeline 相比顺序执行显著减少了总处理时间。

详情请参阅 [AsyncPipeline](</docs/asyncpipeline>) 文档。

## SuperComponents

为了简化代码，我们引入了 [SuperComponents](</docs/supercomponents>)，允许你将完整的管道包装起来并作为单个组件复用。详情和示例请参阅其文档页面。

## 数据流

当数据（初始查询）流经整个管道时，各个值仅在组件连接时才会从一个组件传递到另一个组件。因此，并非所有组件都能访问所有数据。这种方法带来了速度和调试便利性方面的好处。

要在管道中连接组件和集成，你必须知道它们的输入和输出名称。一个组件的输出必须被后续组件接受为输入。当你使用 `Pipeline.connect()` 在管道中连接组件时，它会验证输入和输出类型是否匹配。

### 智能管道连接

管道支持更智能的连接语义，简化了组件的连接方式。

兼容的输出在连接到单个输入时可以隐式合并。管道还会在连接时对某些选定类型执行隐式类型适配。

这些行为减少了对 `Joiners` 和 `OutputAdapters` 等「粘合」组件的需求，使管道更加简洁易读。

详情和示例请参阅[智能管道连接](</docs/smart-pipeline-connections>)。

## 创建管道的步骤详解

一旦所有组件都已创建并准备好组合到管道中，就需要四个步骤使其工作：

  1. 使用 `Pipeline()` 创建管道。这将创建 Pipeline 对象。
  2. 使用 `.add_component(name, component)` 逐个向管道添加组件。这仅将组件添加到管道中，尚未连接它们。这对于循环特别有用，因为它允许在下一步中顺畅地连接组件，因为它们都已存在于管道中。
  3. 使用 `.connect("producer_component.output_name", "consumer_component.input_name")` 连接组件。在这一步中，你显式地将一个组件的输出连接到下一个组件的输入。这也是管道验证连接的时间，但不会运行组件，因此验证速度很快。
  4. 使用 `.run({"component_1": {"mandatory_inputs": value}})` 运行管道。最后，通过指定管道中的第一个组件并传入其必需输入来运行 Pipeline。你还可以选择性地向其他组件传入输入，例如：`.run({"component_1": {"mandatory_inputs": value}, "component_2": {"inputs": value}})`。

[创建管道](</docs/creating-pipelines>)中的完整管道[示例](</docs/creating-pipelines#example>)展示了如何将所有元素组合在一起创建一个可工作的 RAG 管道。

创建管道后，你可以[以图形方式可视化](</docs/visualizing-pipelines>)它，以了解组件的连接方式并确保它们符合你的预期。你可以使用 Mermaid 图来实现这一点。

## 验证

验证在使用 `.connect()` 连接管道组件时发生，但在运行组件之前进行，以提高速度。管道会验证：

  * 组件是否存在于管道中。
  * 组件的输出和输入是否匹配并明确指定。例如，如果一个组件产生两个输出，当将其连接到另一个组件时，你必须指明哪个输出连接到哪个输入。
  * 组件的类型是否匹配。
  * 对于 `Variadic` 以外的输入类型，检查输入是否已被其他连接占用。

所有这些检查都会产生详细的错误信息，帮助你快速修复发现的问题。

## 序列化

借助序列化，你可以保存和加载管道。序列化是将 Haystack 管道转换为可以存储在磁盘上或通过网络发送的格式。它特别适用于：

  * 编辑、存储和共享管道。
  * 以不同于 Python 的格式修改现有管道。

Haystack 管道将序列化委托给其组件，因此序列化管道仅意味着逐一序列化管道中的每个组件及其连接。管道被序列化为字典格式，作为中间格式，然后你可以将其转换为所需的最终格式。

序列化格式

Haystack 目前仅支持 YAML 格式。我们将逐步推出更多格式。

要使序列化成为可能，组件必须支持从 Python 字典转换以及转换为 Python 字典。所有 Haystack 组件都有两个使它们可序列化的方法：`from_dict` 和 `to_dict`。`Pipeline` 类则有自己的 `from_dict` 和 `to_dict` 方法，负责序列化组件和连接。

[编辑此页面](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/pipelines.mdx>)

[上一节：SuperComponents](</docs/supercomponents>)[下一节：创建管道](</docs/creating-pipelines>)

  * [灵活性](<#flexibility>)
    * [Agentic 管道](<#agentic-pipelines>)
    * [分支](<#branching>)
    * [循环](<#loops>)
    * [异步管道](<#async-pipelines>)
  * [SuperComponents](<#supercomponents>)
  * [数据流](<#data-flow>)
    * [智能管道连接](<#smart-pipeline-connections>)
  * [创建管道的步骤详解](<#steps-to-create-a-pipeline-explained>)
  * [验证](<#validation>)
  * [序列化](<#serialization>)

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
