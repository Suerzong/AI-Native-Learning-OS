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

[简介](/learn/llm-course/chapter5/1)[如果我的数据集不在 Hub 上怎么办？](/learn/llm-course/chapter5/2)[数据切片与处理](/learn/llm-course/chapter5/3)[大数据？🤗 Datasets 来帮忙！](/learn/llm-course/chapter5/4)[创建你自己的数据集](/learn/llm-course/chapter5/5)[使用 FAISS 进行语义搜索](/learn/llm-course/chapter5/6)[🤗 Datasets，完成！](/learn/llm-course/chapter5/7)[章节测验](/learn/llm-course/chapter5/8)

6\. 🤗 Tokenizers 库

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

[](https://discuss.huggingface.co/t/chapter-5-questions)

在[第 3 章](/course/chapter3)中，你初次接触了 🤗 Datasets 库，并看到微调模型涉及三个主要步骤：

  1. 从 Hugging Face Hub 加载数据集。
  2. 使用 `Dataset.map()` 预处理数据。
  3. 加载并计算指标。

但这只是 🤗 Datasets 功能的冰山一角！在本章中，我们将深入了解这个库。在此过程中，我们将找到以下问题的答案：

  * 当你的数据集不在 Hub 上时该怎么办？
  * 如何对数据集进行切片和处理？（如果你_真的_需要使用 Pandas 怎么办？）
  * 当你的数据集非常大，会导致笔记本电脑内存不足时该怎么办？
  * "内存映射"和 Apache Arrow 到底是什么？
  * 如何创建自己的数据集并将其推送到 Hub？

你在这里学到的技术将为[第 6 章](/course/chapter6)和[第 7 章](/course/chapter7)中的高级分词和微调任务做好准备 —— 所以泡杯咖啡，让我们开始吧！

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter5/1.mdx)

[←章节测验](/learn/llm-course/chapter4/6) [如果我的数据集不在 Hub 上怎么办？→](/learn/llm-course/chapter5/2)

[简介](#introduction)
