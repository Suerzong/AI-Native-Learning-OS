[Skip to main content](<#__docusaurus_skipToContent_fallback>)

[![Haystack Logo](/img/logo.svg)![Haystack Logo](/img/logo.svg)**Haystack Documentation**](</>)

[2.28](</docs/components>)

  * [2.29-unstable](</docs/next/components>)
  * [2.28](</docs/components>)
  * [2.27](</docs/2.27/components>)
  * [2.26](</docs/2.26/components>)
  * [2.25](</docs/2.25/components>)
  * [2.24](</docs/2.24/components>)
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

    * [Components](</docs/components>)

      * [Creating Custom Components](</docs/custom-components>)
      * [SuperComponents](</docs/supercomponents>)
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
  * Components
Version: 2.28

On this page

Copy

# Components

Components are the building blocks of a pipeline. They perform tasks such as preprocessing, retrieving, or summarizing text while routing queries through different branches of a pipeline. This page is a summary of all component types available in Haystack.

Components are connected to each other using a [pipeline](</docs/pipelines>), and they function like building blocks that can be easily switched out for each other. A component can take the selected outputs of other components as input. You can also provide input to a component when you call `pipeline.run()`.

## Stand-Alone or In a Pipeline[​](<#stand-alone-or-in-a-pipeline> "Direct link to Stand-Alone or In a Pipeline")

You can integrate components in a pipeline to perform a specific task. But you can also use some of them stand-alone, outside of a pipeline. For example, you can run `DocumentWriter` on its own, to write documents into a Document Store. To check how to use a component and if it's usable outside of a pipeline, check the _Usage_ section on the component's documentation page.

Each component has a `run()` method. When you connect components in a pipeline, and you run the pipeline by calling `Pipeline.run()`, it invokes the `run()` method for each component sequentially.

## Input and Output[​](<#input-and-output> "Direct link to Input and Output")

To connect components in a pipeline, you need to know the names of the inputs and outputs they accept. The output of one component must be compatible with the input the subsequent component accepts. For example, to connect Retriever and Ranker in a pipeline, you must know that the Retriever outputs `documents` and the Ranker accepts `documents` as input.

The mandatory inputs and outputs are listed in a table at the top of each component's documentation page so that you can quickly check them:

![DocumentWriter component specification table showing Name, Folder Path, Position in Pipeline, Inputs \(documents list\), and Outputs \(documents_written integer\)](/img/3a53f3e-inputs_and_outputs.png)

You can also look them up in the code in the component`run()` method. Here's an example of the inputs and outputs of `TransformerSimilarityRanker`:

python

    @component.output_types(documents=List[Document]) # "documents" is the output name you need when connecting components in a pipeline

    def run(self, query: str, documents: List[Document], top_k: Optional[int] = None):# "query" and "documents" are the mandatory inputs, additionally you can also specify the optional top_k parameter

    """

    Returns a list of Documents ranked by their similarity to the given query.

    :param query: Query string.

    :param documents: List of Documents.

    :param top_k: The maximum number of Documents you want the Ranker to return.

    :return: List of Documents sorted by their similarity to the query with the most similar Documents appearing first.

    """

## Warming Up Components[​](<#warming-up-components> "Direct link to Warming Up Components")

Components that use heavy resources, like LLMs or embedding models, have a `warm_up()` method that loads the necessary resources (such as models) into memory. This method is automatically called the first time the component runs, so you can use components directly without explicitly calling `warm_up()`:

python

    from haystack import Document

    from haystack.components.embedders import SentenceTransformersDocumentEmbedder

    doc = Document(content="I love pizza!")

    doc_embedder = SentenceTransformersDocumentEmbedder()

    result = doc_embedder.run([doc])  # warm_up() is called automatically on first run

    print(result["documents"][0].embedding)

You can still call `warm_up()` explicitly if you want to control when resources are loaded.

[Edit this page](<https://github.com/deepset-ai/haystack/tree/main/docs-website/versioned_docs/version-2.28/concepts/components.mdx>)

[PreviousState](</docs/state>)[NextCreating Custom Components](</docs/custom-components>)

  * [Stand-Alone or In a Pipeline](<#stand-alone-or-in-a-pipeline>)
  * [Input and Output](<#input-and-output>)
  * [Warming Up Components](<#warming-up-components>)

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
