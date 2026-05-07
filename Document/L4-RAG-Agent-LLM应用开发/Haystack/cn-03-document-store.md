[跳转到主要内容](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack 文档**](</>)

[2.28](</docs/document-store>)

  * [2.29-unstable](</docs/next/document-store>)
  * [2.28](</docs/document-store>)
  * [2.27](</docs/2.27/document-store>)
  * [2.26](</docs/2.26/document-store>)
  * [2.25](</docs/2.25/document-store>)
  * [2.24](</docs/2.24/document-store>)
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

    * [数据类](</docs/data-classes>)

    * [文档存储](</docs/document-store>)

      * [选择文档存储](</docs/choosing-a-document-store>)
      * [创建自定义文档存储](</docs/creating-custom-document-stores>)
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
  * 文档存储
版本: 2.28

本页内容

复制

# 文档存储（Document Store）

你可以将文档存储理解为一个数据库，它存储你的数据并在查询时提供给检索器（Retriever）。了解如何在管道中使用文档存储或如何创建你自己的文档存储。

文档存储是一个用于存储文档的对象。在 Haystack 中，文档存储与组件（Component）不同，因为它没有 `run()` 方法。你可以将它理解为你数据库的接口——你可以将信息放入其中，也可以在其中查找。这意味着文档存储不是管道的一部分，而是管道组件可以访问并与之交互的工具。

与检索器配合使用

在 Haystack 中使用文档存储的最常见方式是通过检索器来获取文档。文档存储通常会有一个对应的检索器以充分利用特定技术。更多信息请参阅我们的[检索器](</docs/retrievers>)文档。

如何选择文档存储？

要了解不同类型的文档存储及其优缺点，请前往[选择文档存储](</docs/choosing-a-document-store>)页面。

### DocumentStore 协议

Haystack 中的文档存储设计为使用以下方法作为其协议的一部分：

  * `count_documents` 返回给定存储中存储的文档数量（整数）。
  * `filter_documents` 返回与提供的过滤器匹配的文档列表。
  * `write_documents` 将文档写入或覆盖到给定存储中，并返回写入的文档数量（整数）。
  * `delete_documents` 从文档存储中删除具有给定 `document_ids` 的所有文档。

### 初始化

要在管道中使用文档存储，必须先对其进行初始化。

请参阅左侧导航面板中「文档存储」部分的每个文档存储的安装和初始化详细信息。

### 使用文档

在将数据写入文档存储之前，先将其转换为 `Document` 对象，同时附带元数据和文档 ID。

ID 字段是必填的，如果你没有自己选择特定的 ID，Haystack 会尽力根据文档信息生成唯一的 ID 并自动分配。不过，由于 Haystack 使用文档内容来创建 ID，两个相同的文档可能拥有相同的 ID。在更新文档时请记住这一点，因为 ID 不会自动更新。

```python
document_store = ChromaDocumentStore()

documents = [
    Document(
        meta={"name": DOCUMENT_NAME, ...}, id="document_unique_id", content="this is content"
    ),
    ...
]

document_store.write_documents(documents)
```

要将文档写入 `InMemoryDocumentStore`，只需调用 `.write_documents()` 函数：

```python
document_store.write_documents(
    [
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome."),
    ],
)
```

`DocumentWriter`

查看 `DocumentWriter` 组件[文档](</docs/documentwriter>)以在管道中将文档写入文档存储。

### DuplicatePolicy

`DuplicatePolicy` 是一个类，用于定义在 `DocumentStore` 中处理具有相同 ID 的文档的不同选项。它有三个可能的值：

  * **OVERWRITE**：表示如果 `DocumentStore` 中已存在相同 ID 的文档，则应使用新文档覆盖它。
  * **SKIP**：如果已存在相同 ID 的文档，新文档将被跳过，不会添加到 `DocumentStore` 中。
  * **FAIL**：如果 `DocumentStore` 中已存在相同 ID 的文档，则引发错误。这会防止添加重复文档。

以下是如何应用策略来跳过现有文档的示例：

```python
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.writers import DocumentWriter
from haystack.document_stores.types import DuplicatePolicy

document_store = InMemoryDocumentStore()

document_writer = DocumentWriter(
    document_store=document_store,
    policy=DuplicatePolicy.SKIP,
)
```

### 自定义文档存储

所有自定义文档存储必须实现[协议](<https://github.com/deepset-ai/haystack/blob/13804293b1bb79743e5a30e980b76a0561dcfaf8/haystack/document_stores/types/protocol.py>)中的四个必需方法：`count_documents`、`filter_documents`、`write_documents` 和 `delete_documents`。

`init` 函数应包含所选数据库或向量存储的所有特定配置。

我们还建议创建一个对应的自定义检索器，以充分利用特定的文档存储。

详情请参阅[创建自定义文档存储](</docs/creating-custom-document-stores>)页面。

[编辑此页面](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/document-store.mdx>)

[上一节：ChatMessage](</docs/chatmessage>)[下一节：选择文档存储](</docs/choosing-a-document-store>)

  * [DocumentStore 协议](<#documentstore-protocol>)
  * [初始化](<#initialization>)
  * [使用文档](<#work-with-documents>)
  * [DuplicatePolicy](<#duplicatepolicy>)
  * [自定义文档存储](<#custom-document-store>)

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
