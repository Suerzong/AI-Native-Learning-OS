[ Hugging Face](/)

  * [ 模型 ](/models)
  * [ 数据集 ](/datasets)
  * [ Spaces ](/spaces)
  * [ Buckets 新功能](/storage)
  * [ 文档 ](/docs)
  * [ 企业版 ](/enterprise)
  * [定价](/pricing)
  *   * * * *

  * [登录](/login)
  * [注册](/join)

LLM 课程文档

Transformer 能做什么？

# LLM 课程

🏡 查看所有资源智能体课程音频课程社区计算机视觉课程深度强化学习课程扩散模型课程LLM 课程MCP 课程3D 机器学习课程游戏 AI 课程开源 AI 食谱机器人课程a smol course

搜索文档

ARBNDEENESFAFRGJHEHIIDITJAKOMYNEPLPTRORURUMTETHTRVIZH-CNZH-TW

[ ](https://github.com/huggingface/course)

0\. 环境搭建

1\. Transformer 模型

[简介](/learn/llm-course/chapter1/1)[自然语言处理与大语言模型](/learn/llm-course/chapter1/2)[Transformer 能做什么？](/learn/llm-course/chapter1/3)[Transformer 是如何工作的？](/learn/llm-course/chapter1/4)[🤗 Transformers 如何处理任务](/learn/llm-course/chapter1/5)[Transformer 架构](/learn/llm-course/chapter1/6)[快速测验](/learn/llm-course/chapter1/7)[使用 LLM 进行推理](/learn/llm-course/chapter1/8)[偏见与局限性](/learn/llm-course/chapter1/9)[总结](/learn/llm-course/chapter1/10)[认证考试](/learn/llm-course/chapter1/11)

2\. 使用 🤗 Transformers

3\. 微调预训练模型

4\. 共享模型与分词器

5\. 🤗 Datasets 库

6\. 🤗 Tokenizers 库

7\. 经典 NLP 任务

8\. 如何寻求帮助

9\. 构建与共享演示

10\. 整理高质量数据集

11\. 微调大语言模型

12\. 构建推理模型 新功能

课程活动

加入 Hugging Face 社区

获取增强的文档体验

在模型、数据集和 Spaces 上协作

通过加速推理获得更快的示例

在文档主题间切换

[注册](/join)

开始使用

复制页面

# [](#transformers-what-can-they-do) Transformer 能做什么？

[](https://discuss.huggingface.co/t/chapter-1-questions) [](https://colab.research.google.com/github/huggingface/notebooks/blob/master/course/en/chapter1/section3.ipynb) [](https://studiolab.sagemaker.aws/import/github/huggingface/notebooks/blob/master/course/en/chapter1/section3.ipynb)

在本节中，我们将了解 Transformer 模型的功能，并使用 🤗 Transformers 库中的第一个工具：`pipeline()` 函数。

> 👀 看到右上角的 _Open in Colab_ 按钮了吗？点击它即可打开包含本节所有代码示例的 Google Colab 笔记本。在任何包含代码示例的章节中都会有此按钮。
>
> 如果你想在本地运行示例，我们建议先查看[环境搭建](/course/chapter0)。

## [](#transformers-are-everywhere) Transformer 无处不在！

Transformer 模型用于解决不同模态下的各种任务，包括自然语言处理（NLP）、计算机视觉、音频处理等。以下是一些使用 Hugging Face 和 Transformer 模型的公司和组织，他们也通过共享模型回馈社区：

[🤗 Transformers 库](https://github.com/huggingface/transformers)提供了创建和使用这些共享模型的功能。[模型中心](https://huggingface.co/models)包含数百万个预训练模型，任何人都可以下载和使用。你也可以将自己的模型上传到 Hub！

> ⚠️ Hugging Face Hub 不仅限于 Transformer 模型。任何人都可以共享任何类型的模型或数据集！[创建 huggingface.co 账号](https://huggingface.co/join)以使用所有可用功能！

在深入了解 Transformer 模型的工作原理之前，让我们先看几个它们如何用于解决有趣 NLP 问题的例子。

## [](#working-with-pipelines) 使用 pipeline

🤗 Transformers 库中最基本的对象是 `pipeline()` 函数。它将模型与其必要的预处理和后处理步骤连接起来，使我们可以直接输入任何文本并获得可理解的结果：

已复制


    from transformers import pipeline

    classifier = pipeline("sentiment-analysis")
    classifier("I've been waiting for a HuggingFace course my whole life.")

已复制


    [{'label': 'POSITIVE', 'score': 0.9598047137260437}]

我们甚至可以传递多个句子！

已复制


    classifier(
        ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
    )

已复制


    [{'label': 'POSITIVE', 'score': 0.9598047137260437},
     {'label': 'NEGATIVE', 'score': 0.9994558095932007}]

默认情况下，此 pipeline 选择了一个已在英语情感分析上微调的特定预训练模型。创建 `classifier` 对象时，模型会被下载并缓存。如果你重新运行该命令，将使用缓存的模型，无需再次下载。

将文本传递给 pipeline 时涉及三个主要步骤：

  1. 将文本预处理为模型可以理解的格式。
  2. 将预处理后的输入传递给模型。
  3. 对模型的预测结果进行后处理，以便你可以理解它们。

## [](#available-pipelines-for-different-modalities) 不同模态的可用 pipeline

`pipeline()` 函数支持多种模态，允许你处理文本、图像、音频甚至多模态任务。本课程将重点关注文本任务，但了解 Transformer 架构的潜力很有用，所以我们简要概述一下。

以下是可用功能的概述：

> 有关 pipeline 的完整和最新列表，请参阅 [🤗 Transformers 文档](https://huggingface.co/docs/hub/en/models-tasks)。

### [](#text-pipelines) 文本 pipeline

  * `text-generation`：从提示词生成文本
  * `text-classification`：将文本分类为预定义类别
  * `summarization`：创建文本的较短版本，同时保留关键信息
  * `translation`：将文本从一种语言翻译为另一种语言
  * `zero-shot-classification`：无需对特定标签进行预先训练即可分类文本
  * `feature-extraction`：提取文本的向量表示

### [](#image-pipelines) 图像 pipeline

  * `image-to-text`：生成图像的文本描述
  * `image-classification`：识别图像中的物体
  * `object-detection`：定位和识别图像中的物体

### [](#audio-pipelines) 音频 pipeline

  * `automatic-speech-recognition`：将语音转换为文本
  * `audio-classification`：将音频分类
  * `text-to-speech`：将文本转换为语音

### [](#multimodal-pipelines) 多模态 pipeline

  * `image-text-to-text`：根据文本提示回复图像

让我们更详细地探索其中一些 pipeline！

## [](#zero-shot-classification) 零样本分类（Zero-shot classification）

我们将从处理一个更具挑战性的任务开始，需要对未标注的文本进行分类。这在实际项目中很常见，因为标注文本通常耗时且需要领域专业知识。对于这种用例，`zero-shot-classification` pipeline 非常强大：它允许你指定用于分类的标签，因此你不必依赖预训练模型的标签。你已经看到模型如何使用"积极"和"消极"两个标签对句子进行分类——但它也可以使用你喜欢的任何其他标签集对文本进行分类。

已复制


    from transformers import pipeline

    classifier = pipeline("zero-shot-classification")
    classifier(
        "This is a course about the Transformers library",
        candidate_labels=["education", "politics", "business"],
    )

已复制


    {'sequence': 'This is a course about the Transformers library',
     'labels': ['education', 'business', 'politics'],
     'scores': [0.8445963859558105, 0.111976258456707, 0.043427448719739914]}

这个 pipeline 被称为 _零样本_ 分类，因为你不需要在自己的数据上微调模型即可使用它。它可以为你想要的任何标签列表直接返回概率分数！

> ✏️ **试一试！** 尝试使用你自己的序列和标签，看看模型的表现如何。

## [](#text-generation) 文本生成（Text generation）

现在让我们看看如何使用 pipeline 生成文本。这里的主要思路是你提供一个提示词，模型将通过生成剩余文本来自动补全它。这类似于许多手机上的预测文本功能。文本生成涉及随机性，因此如果你没有获得与下面相同的结果是正常的。

已复制


    from transformers import pipeline

    generator = pipeline("text-generation")
    generator("In this course, we will teach you how to")

已复制


    [{'generated_text': 'In this course, we will teach you how to understand and use '
                        'data flow and data interchange when handling user data. We '
                        'will be working with one or more of the most commonly used '
                        'data flows — data flows of various types, as seen by the '
                        'HTTP'}]

你可以使用 `num_return_sequences` 参数控制生成多少个不同的序列，使用 `max_length` 参数控制输出文本的总长度。

> ✏️ **试一试！** 使用 `num_return_sequences` 和 `max_length` 参数生成两个各 15 个单词的句子。

## [](#using-any-model-from-the-hub-in-a-pipeline) 在 pipeline 中使用 Hub 上的任何模型

前面的示例使用了当前任务的默认模型，但你也可以从 Hub 中选择特定模型用于特定任务的 pipeline——例如文本生成。前往[模型中心](https://huggingface.co/models)并点击左侧的相应标签，仅显示该任务支持的模型。你应该能看到类似[这个页面](https://huggingface.co/models?pipeline_tag=text-generation)。

让我们试试 [`HuggingFaceTB/SmolLM2-360M`](https://huggingface.co/HuggingFaceTB/SmolLM2-360M) 模型！以下是如何在与之前相同的 pipeline 中加载它：

已复制


    from transformers import pipeline

    generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
    generator(
        "In this course, we will teach you how to",
        max_length=30,
        num_return_sequences=2,
    )

已复制


    [{'generated_text': 'In this course, we will teach you how to manipulate the world and '
                        'move your mental and physical capabilities to your advantage.'},
     {'generated_text': 'In this course, we will teach you how to become an expert and '
                        'practice realtime, and with a hands on experience on both real '
                        'time and real'}]

你可以通过点击语言标签来细化模型搜索，并选择一个能在另一种语言中生成文本的模型。模型中心甚至包含支持多种语言的多语言模型的检查点。

一旦你点击选择了一个模型，你会看到有一个组件可以直接在线试用。这样你可以在下载模型之前快速测试其能力。

> ✏️ **试一试！** 使用筛选器找到另一种语言的文本生成模型。不妨使用该组件试一试，并在 pipeline 中使用它！

### [](#inference-providers) 推理服务（Inference Providers）

所有模型都可以通过浏览器直接使用推理服务进行测试，这在 Hugging Face [网站](https://huggingface.co/docs/inference-providers/en/index)上可用。你可以在此页面上通过输入自定义文本来直接使用模型。

驱动该组件的推理服务也作为付费产品提供，如果你的工作流需要的话会很方便。更多详情请参阅[定价页面](https://huggingface.co/docs/inference-providers/en/pricing)。

## [](#mask-filling) 遮掩填充（Mask filling）

你将尝试的下一个 pipeline 是 `fill-mask`。这个任务的想法是填充给定文本中的空白：

已复制


    from transformers import pipeline

    unmasker = pipeline("fill-mask")
    unmasker("This course will teach you all about <mask> models.", top_k=2)

已复制


    [{'sequence': 'This course will teach you all about mathematical models.',
      'score': 0.19619831442832947,
      'token': 30412,
      'token_str': ' mathematical'},
     {'sequence': 'This course will teach you all about computational models.',
      'score': 0.04052725434303284,
      'token': 38163,
      'token_str': ' computational'}]

`top_k` 参数控制你想显示多少个可能性。注意这里模型填充了特殊的 `<mask>` 词，通常被称为 _遮掩标记（mask token）_。其他遮掩填充模型可能有不同的遮掩标记，因此在探索其他模型时最好验证正确的遮掩词。检查方法之一是查看组件中使用的遮掩词。

> ✏️ **试一试！** 在 Hub 上搜索 `bert-base-cased` 模型，并在推理 API 组件中确定其遮掩词。该模型对我们上面 `pipeline` 示例中的句子预测了什么？

## [](#named-entity-recognition) 命名实体识别（Named entity recognition）

命名实体识别（NER）是一个任务，模型需要找出输入文本的哪些部分对应人名、地点或组织等实体。让我们看一个例子：

已复制


    from transformers import pipeline

    ner = pipeline("ner", grouped_entities=True)
    ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")

已复制


    [{'entity_group': 'PER', 'score': 0.99816, 'word': 'Sylvain', 'start': 11, 'end': 18},
     {'entity_group': 'ORG', 'score': 0.97960, 'word': 'Hugging Face', 'start': 33, 'end': 45},
     {'entity_group': 'LOC', 'score': 0.99321, 'word': 'Brooklyn', 'start': 49, 'end': 57}
    ]

这里模型正确地识别出 Sylvain 是人名（PER），Hugging Face 是组织（ORG），Brooklyn 是地点（LOC）。

我们在 pipeline 创建函数中传递 `grouped_entities=True` 选项，以告诉 pipeline 将对应同一实体的句子部分重新组合在一起：这里模型正确地将"Hugging"和"Face"归为一个组织，即使该名称由多个单词组成。事实上，正如我们将在下一章看到的，预处理甚至会将某些单词拆分为更小的部分。例如，`Sylvain` 被拆分为四个部分：`S`、`##yl`、`##va` 和 `##in`。在后处理步骤中，pipeline 成功地将这些部分重新组合。

> ✏️ **试一试！** 在模型中心搜索一个能在英语中进行词性标注（通常缩写为 POS）的模型。该模型对上面示例中的句子预测了什么？

## [](#question-answering) 问答（Question answering）

`question-answering` pipeline 使用给定上下文中的信息来回答问题：

已复制


    from transformers import pipeline

    question_answerer = pipeline("question-answering")
    question_answerer(
        question="Where do I work?",
        context="My name is Sylvain and I work at Hugging Face in Brooklyn",
    )

已复制


    {'score': 0.6385916471481323, 'start': 33, 'end': 45, 'answer': 'Hugging Face'}

请注意，此 pipeline 通过从提供的上下文中提取信息来工作；它不生成答案。

## [](#summarization) 文本摘要（Summarization）

文本摘要是将文本缩减为较短文本同时保留文本中引用的所有（或大部分）重要内容的任务。以下是一个例子：

已复制


    from transformers import pipeline

    summarizer = pipeline("summarization")
    summarizer(
        """
        America has changed dramatically during recent years. Not only has the number of
        graduates in traditional engineering disciplines such as mechanical, civil,
        electrical, chemical, and aeronautical engineering declined, but in most of
        the premier American universities engineering curricula now concentrate on
        and encourage largely the study of engineering science. As a result, there
        are declining offerings in engineering subjects dealing with infrastructure,
        the environment, and related issues, and greater concentration on high
        technology subjects, largely supporting increasingly complex scientific
        developments. While the latter is important, it should not be at the expense
        of more traditional engineering.

        Rapidly developing economies such as China and India, as well as other
        industrial countries in Europe and Asia, continue to encourage and advance
        the teaching of engineering. Both China and India, respectively, graduate
        six and eight times as many traditional engineers as does the United States.
        Other industrial countries at minimum maintain their output, while America
        suffers an increasingly serious decline in the number of engineering graduates
        and a lack of well-educated engineers.
    """
    )

已复制


    [{'summary_text': ' America has changed dramatically during recent years . The '
                      'number of engineering graduates in the U.S. has declined in '
                      'traditional engineering disciplines such as mechanical, civil '
                      ', electrical, chemical, and aeronautical engineering . Rapidly '
                      'developing economies such as China and India, as well as other '
                      'industrial countries in Europe and Asia, continue to encourage '
                      'and advance engineering .'}]

与文本生成一样，你可以为结果指定 `max_length` 或 `min_length`。

## [](#translation) 机器翻译（Translation）

对于翻译，如果你在任务名称中提供语言对（如 `"translation_en_to_fr"`），可以使用默认模型，但最简单的方法是在[模型中心](https://huggingface.co/models)选择你想要使用的模型。这里我们将尝试从法语翻译到英语：

已复制


    from transformers import pipeline

    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    translator("Ce cours est produit par Hugging Face.")

已复制


    [{'translation_text': 'This course is produced by Hugging Face.'}]

与文本生成和文本摘要一样，你可以为结果指定 `max_length` 或 `min_length`。

> ✏️ **试一试！** 搜索其他语言的翻译模型，并尝试将上面的句子翻译成几种不同的语言。

## [](#image-and-audio-pipelines) 图像和音频 pipeline

除了文本之外，Transformer 模型还可以处理图像和音频。以下是几个例子：

### [](#image-classification) 图像分类（Image classification）

已复制


    from transformers import pipeline

    image_classifier = pipeline(
        task="image-classification", model="google/vit-base-patch16-224"
    )
    result = image_classifier(
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
    )
    print(result)

已复制


    [{'label': 'lynx, catamount', 'score': 0.43350091576576233},
     {'label': 'cougar, puma, catamount, mountain lion, painter, panther, Felis concolor',
      'score': 0.034796204417943954},
     {'label': 'snow leopard, ounce, Panthera uncia',
      'score': 0.03240183740854263},
     {'label': 'Egyptian cat', 'score': 0.02394474856555462},
     {'label': 'tiger cat', 'score': 0.02288915030658245}]

### [](#automatic-speech-recognition) 自动语音识别（Automatic speech recognition）

已复制


    from transformers import pipeline

    transcriber = pipeline(
        task="automatic-speech-recognition", model="openai/whisper-large-v3"
    )
    result = transcriber(
        "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
    )
    print(result)

已复制


    {'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}

## [](#combining-data-from-multiple-sources) 组合多源数据

Transformer 模型的一个强大应用是组合和处理来自多个来源的数据的能力。这在以下情况下特别有用：

  1. 跨多个数据库或仓库搜索
  2. 整合来自不同格式（文本、图像、音频）的信息
  3. 创建相关信息的统一视图

例如，你可以构建一个系统：

  * 跨文本和图像等多种模态的数据库搜索信息。
  * 将来自不同来源的结果组合成单个连贯的响应。例如，来自音频文件和文本描述。
  * 从文档和元数据库中呈现最相关的信息。

## [](#conclusion) 总结

本章中展示的 pipeline 主要用于演示目的。它们是为特定任务编程的，无法执行变体任务。在下一章中，你将了解 `pipeline()` 函数的内部结构以及如何自定义其行为。

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter1/3.mdx)

[←自然语言处理与大语言模型](/learn/llm-course/chapter1/2) [Transformer 是如何工作的？→](/learn/llm-course/chapter1/4)

[Transformer 能做什么？](#transformers-what-can-they-do)[Transformer 无处不在！](#transformers-are-everywhere)[使用 pipeline](#working-with-pipelines)[不同模态的可用 pipeline](#available-pipelines-for-different-modalities)[文本 pipeline](#text-pipelines)[图像 pipeline](#image-pipelines)[音频 pipeline](#audio-pipelines)[多模态 pipeline](#multimodal-pipelines)[零样本分类](#zero-shot-classification)[文本生成](#text-generation)[在 pipeline 中使用 Hub 上的任何模型](#using-any-model-from-the-hub-in-a-pipeline)[推理服务](#inference-providers)[遮掩填充](#mask-filling)[命名实体识别](#named-entity-recognition)[问答](#question-answering)[文本摘要](#summarization)[机器翻译](#translation)[图像和音频 pipeline](#image-and-audio-pipelines)[图像分类](#image-classification)[自动语音识别](#automatic-speech-recognition)[组合多源数据](#combining-data-from-multiple-sources)[总结](#conclusion)
