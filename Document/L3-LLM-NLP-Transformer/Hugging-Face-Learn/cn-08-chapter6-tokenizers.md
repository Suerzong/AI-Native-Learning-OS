[ Hugging Face](/)

  * [ Models ](/models)
  * [ Datasets ](/datasets)
  * [ Spaces ](/spaces)
  * [ Buckets new](/storage)
  * [ Docs ](/docs)
  * [ Enterprise ](/enterprise)
  * [Pricing](/pricing)
  *   * * * *

  * [Log In](/login)
  * [Sign Up](/join)

LLM 课程文档

简介

# LLM 课程

🏡 查看全部资源智能体课程音频课程社区计算机视觉课程深度强化学习课程扩散模型课程LLM 课程MCP 课程3D 机器学习课程游戏机器学习课程开源 AI 实践手册机器人课程a smol course

搜索文档

ARBNDEENESFAFRGJHEHIIDITJAKOMYNEPLPTRORURUMTETHTRVIZH-CNZH-TW

[ ](https://github.com/huggingface/course)

0\. 环境搭建

1\. Transformer 模型

2\. 使用 🤗 Transformers

3\. 微调预训练模型

4\. 共享模型与分词器

5\. 🤗 Datasets 库

6\. 🤗 Tokenizers 库

[简介](/learn/llm-course/chapter6/1)[从旧分词器训练新的分词器](/learn/llm-course/chapter6/2)[快速分词器的特殊能力](/learn/llm-course/chapter6/3)[问答 Pipeline 中的快速分词器](/learn/llm-course/chapter6/3b)[标准化与预分词](/learn/llm-course/chapter6/4)[字节对编码分词](/learn/llm-course/chapter6/5)[WordPiece 分词](/learn/llm-course/chapter6/6)[Unigram 分词](/learn/llm-course/chapter6/7)[从零构建分词器，逐块搭建](/learn/llm-course/chapter6/8)[分词器，搞定！](/learn/llm-course/chapter6/9)[章节测验](/learn/llm-course/chapter6/10)

7\. 经典 NLP 任务

8\. 如何寻求帮助

9\. 构建与共享演示

10\. 策划高质量数据集

11\. 微调大语言模型

12\. 构建推理模型 new

课程活动

加入 Hugging Face 社区

获取增强的文档体验

在模型、数据集和 Spaces 上协作

通过加速推理获得更快的示例

切换文档主题

[Sign Up](/join)

to get started

Copy page

# [](#introduction) 简介

[](https://discuss.huggingface.co/t/chapter-6-questions)

在[第 3 章](/course/chapter3)中，我们了解了如何在给定任务上微调模型。当我们这样做时，我们使用的是模型预训练时相同的分词器 —— 但当我们想从头开始训练一个模型时该怎么办？在这些情况下，使用在另一个领域或语言的语料库上预训练的分词器通常效果不佳。例如，在英语语料库上训练的分词器在日语文本语料库上表现会很差，因为两种语言中空格和标点符号的使用方式非常不同。

在本章中，你将学习如何在文本语料库上训练一个全新的分词器，以便随后用于预训练语言模型。这一切都将在 [🤗 Tokenizers](https://github.com/huggingface/tokenizers) 库的帮助下完成，该库为 [🤗 Transformers](https://github.com/huggingface/transformers) 库提供了"快速"分词器。我们将深入了解该库提供的功能，并探索快速分词器与"慢速"版本之间的区别。

我们将涵盖的主题包括：

  * 如何在新的文本语料库上训练与给定检查点类似的分词器
  * 快速分词器的特殊功能
  * 当今 NLP 中使用的三种主要子词分词算法之间的区别
  * 如何使用 🤗 Tokenizers 库从头构建分词器并在数据上训练它

本章介绍的技术将为你准备[第 7 章](/course/chapter7/6)中创建 Python 源代码语言模型的内容。让我们首先了解"训练"分词器到底意味着什么。

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter6/1.mdx)

[←章节测验](/learn/llm-course/chapter5/8) [从旧分词器训练新的分词器→](/learn/llm-course/chapter6/2)

[简介](#introduction)
