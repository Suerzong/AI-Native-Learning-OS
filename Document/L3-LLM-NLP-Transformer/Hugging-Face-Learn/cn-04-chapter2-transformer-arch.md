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

[简介](/learn/llm-course/chapter2/1)[Pipeline 背后的原理](/learn/llm-course/chapter2/2)[模型](/learn/llm-course/chapter2/3)[分词器](/learn/llm-course/chapter2/4)[处理多个序列](/learn/llm-course/chapter2/5)[完整流程](/learn/llm-course/chapter2/6)[基础用法已完成！](/learn/llm-course/chapter2/7)[优化推理部署](/learn/llm-course/chapter2/8)[章节测验](/learn/llm-course/chapter2/9)

3\. 微调预训练模型

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

Copy page

# [](#introduction) 简介

[](https://discuss.huggingface.co/t/chapter-2-questions)

正如你在[第 1 章](/course/chapter1)中看到的，Transformer 模型通常非常庞大。这些模型拥有数百万到数十亿个参数，训练和部署这些模型是一项复杂的任务。此外，几乎每天都有新模型发布，且每个模型都有自己的实现，想要逐一尝试并非易事。

🤗 Transformers 库正是为了解决这个问题而创建的。它的目标是提供一个统一的 API，通过该 API 可以加载、训练和保存任何 Transformer 模型。该库的主要特性包括：

  * **易用性** ：只需两行代码即可下载、加载和使用最先进的 NLP 模型进行推理。
  * **灵活性** ：所有模型的核心都是简单的 PyTorch `nn.Module` 类，可以像各自机器学习（ML）框架中的其他模型一样进行处理。
  * **简洁性** ：库中几乎没有任何抽象层。"全部在一个文件中"是核心概念：模型的前向传播完全定义在单个文件中，因此代码本身易于理解和修改。

最后一个特性使得 🤗 Transformers 与其他 ML 库截然不同。这些模型并非基于跨文件共享的模块构建；相反，每个模型都有自己的层。除了使模型更易于理解和使用外，这还允许你轻松地在一个模型上进行实验，而不会影响其他模型。

本章将以一个端到端的示例开始，我们将模型和分词器结合使用来复现[第 1 章](/course/chapter1)中介绍的 `pipeline()` 函数。接下来，我们将讨论模型 API：深入模型和配置类，展示如何加载模型以及模型如何处理数值输入并输出预测。

然后我们将了解分词器 API，它是 `pipeline()` 函数的另一个主要组件。分词器负责第一个和最后一个处理步骤，处理从文本到神经网络数值输入的转换，以及需要时从数值到文本的反向转换。最后，我们将展示如何处理以准备好的批次形式向模型发送多个句子，然后通过更深入地了解高级 `tokenizer()` 函数来总结本章。

> ⚠️ 为了充分利用 Model Hub 和 🤗 Transformers 的所有功能，我们建议[创建一个账户](https://huggingface.co/join)。

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter2/1.mdx)

[←认证考试](/learn/llm-course/chapter1/11) [Pipeline 背后的原理→](/learn/llm-course/chapter2/2)

[简介](#introduction)
