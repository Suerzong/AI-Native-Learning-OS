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

[简介](/learn/llm-course/chapter3/1)[处理数据](/learn/llm-course/chapter3/2)[使用 Trainer API 微调模型](/learn/llm-course/chapter3/3)[完整训练循环](/learn/llm-course/chapter3/4)[理解学习曲线](/learn/llm-course/chapter3/5)[微调，完成！](/learn/llm-course/chapter3/6)[章节测验](/learn/llm-course/chapter3/7)

4\. 共享模型与分词器

5\. 🤗 Datasets 库

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

[ Pytorch ](?fw=pt)[ TensorFlow ](?fw=tf)

Copy page

# [](#introduction) 简介

[](https://discuss.huggingface.co/t/chapter-3-questions)

在[第 2 章](/course/chapter2)中，我们探索了如何使用分词器和预训练模型进行预测。但如果你想微调预训练模型来解决特定任务呢？这就是本章的主题！你将学习：

  * 如何使用最新的 🤗 Datasets 功能从 Hub 准备大型数据集
  * 如何使用高级 `Trainer` API 以现代最佳实践微调模型
  * 如何实现带有优化技术的自定义训练循环
  * 如何利用 🤗 Accelerate 库轻松在任何设置上运行分布式训练
  * 如何应用当前微调最佳实践以获得最佳性能

> 📚 **必备资源** ：在开始之前，你可能需要查阅 [🤗 Datasets 文档](https://huggingface.co/docs/datasets/)以了解数据处理。

本章还将介绍 🤗 Transformers 库之外的一些 Hugging Face 库！我们将看到 🤗 Datasets、🤗 Tokenizers、🤗 Accelerate 和 🤗 Evaluate 等库如何帮助你更高效、更有效地训练模型。

本章的主要部分将教你不同的内容：

  * **第 2 节** ：学习现代数据预处理技术和高效的数据集处理
  * **第 3 节** ：掌握强大的 Trainer API 及其所有最新功能
  * **第 4 节** ：从头实现训练循环并使用 Accelerate 理解分布式训练

在本章结束时，你将能够使用高级 API 和自定义训练循环在自己的数据集上微调模型，并应用该领域的最新最佳实践。

> 🎯 **你将构建什么** ：在本章结束时，你将微调一个 BERT 模型用于文本分类，并了解如何将这些技术应用到自己的数据集和任务中。

本章专注于 **PyTorch** ，因为它已成为现代深度学习研究和生产的标准框架。我们将使用 Hugging Face 生态系统中的最新 API 和最佳实践。

要将训练好的模型上传到 Hugging Face Hub，你需要一个 Hugging Face 账户：[创建账户](https://huggingface.co/join)

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter3/1.mdx)

[←章节测验](/learn/llm-course/chapter2/9) [处理数据→](/learn/llm-course/chapter3/2)

[简介](#introduction)
