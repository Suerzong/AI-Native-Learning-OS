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

7\. 经典 NLP 任务

[简介](/learn/llm-course/chapter7/1)[词元分类](/learn/llm-course/chapter7/2)[微调掩码语言模型](/learn/llm-course/chapter7/3)[翻译](/learn/llm-course/chapter7/4)[摘要](/learn/llm-course/chapter7/5)[从头训练因果语言模型](/learn/llm-course/chapter7/6)[问答](/learn/llm-course/chapter7/7)[精通 LLM](/learn/llm-course/chapter7/8)[章节测验](/learn/llm-course/chapter7/9)

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

[ Pytorch ](?fw=pt)[ TensorFlow ](?fw=tf)

Copy page

# [](#introduction) 简介

[](https://discuss.huggingface.co/t/chapter-7-questions)

在[第 3 章](/course/chapter3)中，你学习了如何微调模型进行文本分类。在本章中，我们将处理以下常见的语言任务，这些任务对于使用传统 NLP 模型和现代 LLM 都至关重要：

  * 词元分类
  * 掩码语言建模（如 BERT）
  * 摘要
  * 翻译
  * 因果语言模型预训练（如 GPT-2）
  * 问答

这些基础任务构成了大语言模型（LLM）工作方式的基础，理解它们对于有效使用当今最先进的语言模型至关重要。

为此，你将需要运用在[第 3 章](/course/chapter3)中学到的关于 `Trainer` API 和 🤗 Accelerate 库的一切知识、在[第 5 章](/course/chapter5)中学到的 🤗 Datasets 库，以及在[第 6 章](/course/chapter6)中学到的 🤗 Tokenizers 库。我们还将像在[第 4 章](/course/chapter4)中那样将结果上传到 Model Hub，所以这真的是所有内容汇聚的一章！

每个部分都可以独立阅读，并将展示如何使用 `Trainer` API 或使用 🤗 Accelerate 编写自己的训练循环来训练模型。请随意跳过其中任何部分，专注于你最感兴趣的内容：`Trainer` API 非常适合在不了解背后发生了什么的情况下微调或训练模型，而使用 `Accelerate` 的训练循环将让你更容易自定义任何部分。

> 如果你按顺序阅读这些部分，你会注意到它们有相当多的代码和文字是重复的。这种重复是有意为之的，以便让你可以随时深入了解（或稍后回来查看）任何你感兴趣的任务，并找到一个完整的工作示例。

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter7/1.mdx)

[←章节测验](/learn/llm-course/chapter6/10) [词元分类→](/learn/llm-course/chapter7/2)

[简介](#introduction)
