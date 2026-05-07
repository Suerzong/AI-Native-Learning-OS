[跳转到主要内容](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/components>)

  * [2.29-unstable](</docs/next/components>)
  * [2.28](</docs/components>)
  * [2.27](</docs/2.27/components>)
  * [2.26](</docs/2.26/components>)
  * [2.25](</docs/2.25/components>)
  * [2.24](</docs/2.24/components>)
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

      * [创建自定义组件](</docs/custom-components>)
      * [SuperComponents](</docs/supercomponents>)
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
  * 组件
版本: 2.28

本页内容

复制

# 组件（Components）

组件是管道的构建块。它们执行诸如预处理、检索或摘要文本等任务，同时将查询路由到管道的不同分支。本页是 Haystack 中所有可用组件类型的概要。

组件通过[管道](</docs/pipelines>)相互连接，它们的功能类似于可以轻松互换的构建块。一个组件可以接收其他组件的选定输出作为输入。你也可以在调用 `pipeline.run()` 时向组件提供输入。

## 独立使用或在管道中使用

你可以在管道中集成组件来执行特定任务。但你也可以独立使用其中一些组件，无需在管道中。例如，你可以单独运行 `DocumentWriter` 来将文档写入文档存储。要了解如何使用组件以及它是否可以在管道外使用，请查看组件文档页面的「用法」部分。

每个组件都有一个 `run()` 方法。当你在管道中连接组件，并通过调用 `Pipeline.run()` 运行管道时，它会依次调用每个组件的 `run()` 方法。

## 输入和输出

要在管道中连接组件，你需要知道它们接受的输入和输出的名称。一个组件的输出必须与后续组件接受的输入兼容。例如，要在管道中连接检索器（Retriever）和排序器（Ranker），你必须知道检索器输出 `documents`，而排序器接受 `documents` 作为输入。

必需的输入和输出列在每个组件文档页面顶部的表格中，方便你快速查看：

![DocumentWriter 组件规格表，显示名称、文件夹路径、管道位置、输入（documents 列表）和输出（documents_written 整数）](/img/3a53f3e-inputs_and_outputs.png)

你也可以在代码的组件 `run()` 方法中查找它们。以下是 `TransformerSimilarityRanker` 的输入和输出示例：

```python
@component.output_types(documents=List[Document])  # "documents" 是在管道中连接组件时需要的输出名称

def run(self, query: str, documents: List[Document], top_k: Optional[int] = None):
    # "query" 和 "documents" 是必需输入，还可以指定可选的 top_k 参数

    """
    返回按与给定查询相似度排序的文档列表。

    :param query: 查询字符串。
    :param documents: 文档列表。
    :param top_k: 你希望排序器返回的最大文档数量。
    :return: 按与查询相似度排序的文档列表，最相似的文档排在前面。
    """
```

## 预热组件

使用重量级资源（如 LLM 或嵌入模型）的组件有一个 `warm_up()` 方法，用于将必要的资源（如模型）加载到内存中。该方法在组件首次运行时自动调用，因此你可以直接使用组件而无需显式调用 `warm_up()`：

```python
from haystack import Document
from haystack.components.embedders import SentenceTransformersDocumentEmbedder

doc = Document(content="I love pizza!")
doc_embedder = SentenceTransformersDocumentEmbedder()
result = doc_embedder.run([doc])  # 首次运行时自动调用 warm_up()
print(result["documents"][0].embedding)
```

如果你想控制资源加载的时间，仍然可以显式调用 `warm_up()`。

[编辑此页面](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/components.mdx>)

[上一节：State](</docs/state>)[下一节：创建自定义组件](</docs/custom-components>)

  * [独立使用或在管道中使用](<#stand-alone-or-in-a-pipeline>)
  * [输入和输出](<#input-and-output>)
  * [预热组件](<#warming-up-components>)

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
