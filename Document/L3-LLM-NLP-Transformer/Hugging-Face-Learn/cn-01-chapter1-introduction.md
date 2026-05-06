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

简介

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

# [](#introduction) 简介

[](https://discuss.huggingface.co/t/chapter-1-questions)

## [](#welcome-to-the-course) 欢迎来到 🤗 课程！

本课程将使用 [Hugging Face](https://huggingface.co/) 生态系统中的库来教你大语言模型（LLM）和自然语言处理（NLP）——包括 [🤗 Transformers](https://github.com/huggingface/transformers)、[🤗 Datasets](https://github.com/huggingface/datasets)、[🤗 Tokenizers](https://github.com/huggingface/tokenizers) 和 [🤗 Accelerate](https://github.com/huggingface/accelerate)，以及 [Hugging Face Hub](https://huggingface.co/models)。

我们还将涵盖 Hugging Face 生态系统之外的库。这些是对 AI 社区的杰出贡献，也是非常实用的工具。

本课程完全免费且无广告。

## [](#understanding-nlp-and-llms) 理解 NLP 与 LLM

虽然本课程最初专注于 NLP（自然语言处理），但现在已经演变为强调大语言模型（LLM），后者代表了该领域的最新进展。

**两者有什么区别？**

  * **NLP（自然语言处理）** 是一个更广泛的领域，致力于让计算机理解、解释和生成人类语言。NLP 包含许多技术和任务，如情感分析、命名实体识别和机器翻译。
  * **LLM（大语言模型）** 是 NLP 模型的一个强大子集，其特点是规模巨大、训练数据广泛，并且能够在极少的任务特定训练下执行各种语言任务。Llama、GPT 或 Claude 系列等模型就是 LLM 的例子，它们彻底改变了 NLP 的可能性。

在本课程中，你将同时学习传统的 NLP 概念和前沿的 LLM 技术，因为理解 NLP 的基础对于有效使用 LLM 至关重要。

## [](#what-to-expect) 课程概览

以下是课程的简要概述：

  * 第 1 至 4 章介绍了 🤗 Transformers 库的主要概念。学完这部分内容后，你将熟悉 Transformer 模型的工作原理，并学会如何从 [Hugging Face Hub](https://huggingface.co/models) 使用模型、在数据集上微调模型，以及在 Hub 上分享你的成果！
  * 第 5 至 8 章在深入经典 NLP 任务和 LLM 技术之前，教授 🤗 Datasets 和 🤗 Tokenizers 的基础知识。学完这部分后，你将能够独立处理最常见的语言处理挑战。
  * 第 9 章超越 NLP，介绍如何在 🤗 Hub 上构建和共享模型演示。学完这部分后，你将准备好向全世界展示你的 🤗 Transformers 应用！
  * 第 10 至 12 章深入探讨高级 LLM 主题，如微调、整理高质量数据集和构建推理模型。

本课程：

  * 需要具备良好的 Python 知识
  * 最好在学过入门深度学习课程后学习，例如 [fast.ai](https://www.fast.ai/) 的 [Practical Deep Learning for Coders](https://course.fast.ai/) 或 [DeepLearning.AI](https://www.deeplearning.ai/) 开发的课程之一
  * 不要求事先掌握 [PyTorch](https://pytorch.org/) 或 [TensorFlow](https://www.tensorflow.org/)，但对其中任何一个有基本了解会有所帮助

完成本课程后，我们推荐学习 DeepLearning.AI 的 [自然语言处理专项课程](https://www.coursera.org/specializations/natural-language-processing?utm_source=deeplearning-ai&utm_medium=institutions&utm_campaign=20211011-nlp-2-hugging_face-page-nlp-refresh)，该课程涵盖了朴素贝叶斯和 LSTM 等一系列值得了解的传统 NLP 模型！

## [](#who-are-we) 我们是谁

关于作者：

[**Abubakar Abid**](https://huggingface.co/abidlabs) 在斯坦福大学获得应用机器学习博士学位。在博士期间，他创立了 [Gradio](https://github.com/gradio-app/gradio)——一个开源 Python 库，已被用于构建超过 60 万个机器学习演示。Gradio 被 Hugging Face 收购，Abubakar 目前在 Hugging Face 担任机器学习团队负责人。

[**Ben Burtenshaw**](https://huggingface.co/burtenshaw) 是 Hugging Face 的机器学习工程师。他在安特卫普大学获得自然语言处理博士学位，在那里他应用 Transformer 模型生成儿童故事以提高读写能力。此后，他一直专注于为更广泛的社区开发教育材料和工具。

[**Matthew Carrigan**](https://huggingface.co/Rocketknight1) 是 Hugging Face 的机器学习工程师。他住在爱尔兰都柏林，之前在 Parse.ly 担任 ML 工程师，更早之前在都柏林圣三一学院担任博士后研究员。他不相信通过扩展现有架构可以实现 AGI，但对机器人永生寄予厚望。

[**Lysandre Debut**](https://huggingface.co/lysandre) 是 Hugging Face 的机器学习工程师，从非常早期的开发阶段就一直在参与 🤗 Transformers 库的开发。他的目标是通过开发具有极简 API 的工具，使 NLP 对每个人都触手可及。

[**Sylvain Gugger**](https://huggingface.co/sgugger) 是 Hugging Face 的研究工程师，也是 🤗 Transformers 库的核心维护者之一。他之前是 fast.ai 的研究科学家，并与 Jeremy Howard 合著了 _[Deep Learning for Coders with fastai and PyTorch](https://learning.oreilly.com/library/view/deep-learning-for/9781492045519/)_。他的研究重点是通过设计和改进技术使深度学习更加普及，让模型能够在有限资源上快速训练。

[**Dawood Khan**](https://huggingface.co/dawoodkhan82) 是 Hugging Face 的机器学习工程师。他来自纽约市，毕业于纽约大学计算机科学专业。在担任 iOS 工程师几年后，Dawood 辞职与联合创始人一起创办了 Gradio。Gradio 最终被 Hugging Face 收购。

[**Merve Noyan**](https://huggingface.co/merve) 是 Hugging Face 的开发者倡导者，致力于开发工具并围绕它们构建内容，以实现机器学习的大众化。

[**Lucile Saulnier**](https://huggingface.co/SaulLu) 是 Hugging Face 的机器学习工程师，致力于开发和支持开源工具的使用。她还积极参与自然语言处理领域的许多研究项目，如协作训练和 BigScience。

[**Lewis Tunstall**](https://huggingface.co/lewtun) 是 Hugging Face 的机器学习工程师，专注于开发开源工具并使其更广泛地为社区所用。他还是 O'Reilly 书籍 [Natural Language Processing with Transformers](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) 的合著者。

[**Leandro von Werra**](https://huggingface.co/lvwerra) 是 Hugging Face 开源团队的机器学习工程师，也是 O'Reilly 书籍 [Natural Language Processing with Transformers](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) 的合著者。他拥有多年将 NLP 项目推向生产的行业经验，横跨整个机器学习技术栈。

## [](#faq) 常见问题

以下是一些常见问题的解答：

  * **完成本课程是否可以获得认证？** 目前我们没有本课程的认证。但是，我们正在开发 Hugging Face 生态系统的认证计划——敬请期待！

  * **我应该在本课程上花多少时间？** 本课程的每一章设计为 1 周完成，每周大约需要 6-8 小时。但是，你可以根据自己的需要安排时间来完成课程。

  * **如果有问题，可以在哪里提问？** 如果你对课程的任何部分有疑问，只需点击页面顶部的" _提问_ "横幅，系统会自动跳转到 [Hugging Face 论坛](https://discuss.huggingface.co/) 的相应版块：

请注意，论坛上还提供了一份[项目创意列表](https://discuss.huggingface.co/c/course/course-event/25)，供你在完成课程后进行更多实践。

  * **在哪里可以获取课程代码？** 对于每个章节，点击页面顶部的横幅，即可在 Google Colab 或 Amazon SageMaker Studio Lab 中运行代码：

包含课程所有代码的 Jupyter 笔记本托管在 [`huggingface/notebooks`](https://github.com/huggingface/notebooks) 仓库中。如果你想在本地生成它们，请查看 GitHub 上 [`course`](https://github.com/huggingface/course#-jupyter-notebooks) 仓库中的说明。

  * **如何为课程做出贡献？** 有很多方式可以为课程做出贡献！如果你发现拼写错误或程序错误，请在 [`course`](https://github.com/huggingface/course) 仓库中提交 issue。如果你想帮助将课程翻译成你的母语，请查看[这里](https://github.com/huggingface/course#translating-the-course-into-your-language)的说明。

  * **每次翻译做了哪些术语选择？** 每个翻译版本都附有术语表和 `TRANSLATING.txt` 文件，详细说明了机器学习术语等方面的选择。你可以在[这里](https://github.com/huggingface/course/blob/main/chapters/de/TRANSLATING.txt)找到德语的示例。

  * **我可以重用本课程吗？** 当然！本课程在宽松的 [Apache 2 许可证](https://www.apache.org/licenses/LICENSE-2.0.html)下发布。这意味着你必须给出适当的署名、提供许可证链接，并说明是否做了修改。你可以以任何合理的方式进行，但不能以任何暗示许可人认可你或你的使用的方式。如果你想引用本课程，请使用以下 BibTeX：

已复制


    @misc{huggingfacecourse,
      author = {Hugging Face},
      title = {The Hugging Face Course, 2022},
      howpublished = "\url{https://huggingface.co/course}",
      year = {2022},
      note = "[Online; accessed <today>]"
    }

## [](#languages-and-translations) 语言与翻译

感谢我们优秀的社区，本课程除了英语之外还提供多种语言版本 🔥！查看下表了解可用的语言以及翻译贡献者：

语言 | 作者
---|---
[法语](https://huggingface.co/course/fr/chapter1/1) | [@lbourdois](https://github.com/lbourdois), [@ChainYo](https://github.com/ChainYo), [@melaniedrevet](https://github.com/melaniedrevet), [@abdouaziz](https://github.com/abdouaziz)
[越南语](https://huggingface.co/course/vi/chapter1/1) | [@honghanhh](https://github.com/honghanhh)
[简体中文](https://huggingface.co/course/zh-CN/chapter1/1) | [@zhlhyx](https://github.com/zhlhyx), [petrichor1122](https://github.com/petrichor1122), [@yaoqih](https://github.com/yaoqih)
[孟加拉语](https://huggingface.co/course/bn/chapter1/1) (进行中) | [@avishek-018](https://github.com/avishek-018), [@eNipu](https://github.com/eNipu)
[德语](https://huggingface.co/course/de/chapter1/1) (进行中) | [@JesperDramsch](https://github.com/JesperDramsch), [@MarcusFra](https://github.com/MarcusFra), [@fabridamicelli](https://github.com/fabridamicelli)
[西班牙语](https://huggingface.co/course/es/chapter1/1) (进行中) | [@camartinezbu](https://github.com/camartinezbu), [@munozariasjm](https://github.com/munozariasjm), [@fordaz](https://github.com/fordaz)
[波斯语](https://huggingface.co/course/fa/chapter1/1) (进行中) | [@jowharshamshiri](https://github.com/jowharshamshiri), [@schoobani](https://github.com/schoobani)
[古吉拉特语](https://huggingface.co/course/gu/chapter1/1) (进行中) | [@pandyaved98](https://github.com/pandyaved98)
[希伯来语](https://huggingface.co/course/he/chapter1/1) (进行中) | [@omer-dor](https://github.com/omer-dor)
[印地语](https://huggingface.co/course/hi/chapter1/1) (进行中) | [@pandyaved98](https://github.com/pandyaved98)
[印度尼西亚语](https://huggingface.co/course/id/chapter1/1) (进行中) | [@gstdl](https://github.com/gstdl)
[意大利语](https://huggingface.co/course/it/chapter1/1) (进行中) | [@CaterinaBi](https://github.com/CaterinaBi), [@ClonedOne](https://github.com/ClonedOne), [@Nolanogenn](https://github.com/Nolanogenn), [@EdAbati](https://github.com/EdAbati), [@gdacciaro](https://github.com/gdacciaro)
[日语](https://huggingface.co/course/ja/chapter1/1) (进行中) | [@hiromu166](https://github.com/@hiromu166), [@younesbelkada](https://github.com/@younesbelkada), [@HiromuHota](https://github.com/@HiromuHota)
[韩语](https://huggingface.co/course/ko/chapter1/1) (进行中) | [@Doohae](https://github.com/Doohae), [@wonhyeongseo](https://github.com/wonhyeongseo), [@dlfrnaos19](https://github.com/dlfrnaos19)
[葡萄牙语](https://huggingface.co/course/pt/chapter1/1) (进行中) | [@johnnv1](https://github.com/johnnv1), [@victorescosta](https://github.com/victorescosta), [@LincolnVS](https://github.com/LincolnVS)
[俄语](https://huggingface.co/course/ru/chapter1/1) (进行中) | [@pdumin](https://github.com/pdumin), [@svv73](https://github.com/svv73)
[泰语](https://huggingface.co/course/th/chapter1/1) (进行中) | [@peeraponw](https://github.com/peeraponw), [@a-krirk](https://github.com/a-krirk), [@jomariya23156](https://github.com/jomariya23156), [@ckingkan](https://github.com/ckingkan)
[土耳其语](https://huggingface.co/course/tr/chapter1/1) (进行中) | [@tanersekmen](https://github.com/tanersekmen), [@mertbozkir](https://github.com/mertbozkir), [@ftarlaci](https://github.com/ftarlaci), [@akkasayaz](https://github.com/akkasayaz)
[繁体中文](https://huggingface.co/course/zh-TW/chapter1/1) (进行中) | [@davidpeng86](https://github.com/davidpeng86)

对于某些语言，[课程 YouTube 视频](https://youtube.com/playlist?list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o)有该语言的字幕。你可以先点击视频右下角的 _CC_ 按钮启用字幕。然后，在设置图标 ⚙️ 下，选择 _字幕/CC_ 选项来选择你想要的语言。

> 在上表中没有看到你的语言，或者你想为现有翻译做出贡献？你可以按照[这里](https://github.com/huggingface/course#translating-the-course-into-your-language)的说明帮助我们翻译课程。

## [](#lets-go-) 开始吧 🚀

你准备好了吗？在本章中，你将学习：

  * 如何使用 `pipeline()` 函数解决文本生成和分类等 NLP 任务
  * Transformer 架构的原理
  * 如何区分编码器（encoder）、解码器（decoder）和编码器-解码器（encoder-decoder）架构及其用例

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter1/1.mdx)

[←简介](/learn/llm-course/chapter0/1) [自然语言处理与大语言模型→](/learn/llm-course/chapter1/2)

[简介](#introduction)[欢迎来到 🤗 课程！](#welcome-to-the-course)[理解 NLP 与 LLM](#understanding-nlp-and-llms)[课程概览](#what-to-expect)[我们是谁？](#who-are-we)[常见问题](#faq)[语言与翻译](#languages-and-translations)[开始吧 🚀](#lets-go-)
