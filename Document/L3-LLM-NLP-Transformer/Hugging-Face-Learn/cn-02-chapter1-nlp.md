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

自然语言处理与大语言模型

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

# [](#natural-language-processing-and-large-language-models) 自然语言处理与大语言模型

[](https://discuss.huggingface.co/t/chapter-1-questions)

在深入 Transformer 模型之前，让我们先快速了解一下什么是自然语言处理、大语言模型如何改变了这个领域，以及我们为什么关注它。

## [](#what-is-nlp) 什么是 NLP？

NLP 是语言学和机器学习的一个领域，专注于理解与人类语言相关的一切。NLP 任务的目标不仅是单独理解单个词语，还要能够理解这些词语的上下文。

以下是常见 NLP 任务的列表及示例：

  * **句子级分类** ：获取评论的情感、检测邮件是否为垃圾邮件、判断句子是否语法正确或两个句子是否逻辑相关
  * **句子中每个词的分类** ：识别句子的语法成分（名词、动词、形容词），或命名实体（人名、地点、组织）
  * **生成文本内容** ：用自动生成的文本补全提示词（prompt），用遮掩词填充文本中的空白
  * **从文本中提取答案** ：给定一个问题和一段上下文，根据上下文中的信息提取问题的答案
  * **从输入文本生成新句子** ：将文本翻译成另一种语言，对文本进行摘要

NLP 不仅限于书面文本。它还处理语音识别和计算机视觉中的复杂挑战，例如生成音频样本的转录文本或图像的描述。

## [](#rise-of-llms) 大语言模型（LLM）的崛起

近年来，NLP 领域因大语言模型（LLM）而发生了革命性变化。这些模型包括 GPT（生成式预训练 Transformer）和 [Llama](https://huggingface.co/meta-llama) 等架构，彻底改变了语言处理的可能性。

> 大语言模型（LLM）是一种在海量文本数据上训练的 AI 模型，能够理解和生成类人文本、识别语言模式，并在无需任务特定训练的情况下执行各种语言任务。它们代表了自然语言处理（NLP）领域的重大进步。

LLM 的特点是：

  * **规模** ：包含数百万、数十亿甚至数千亿个参数
  * **通用能力** ：无需任务特定训练即可执行多种任务
  * **上下文学习（In-context learning）** ：能从提示词中提供的示例中学习
  * **涌现能力（Emergent abilities）** ：随着模型规模增大，它们展现出未被显式编程或预设的能力

LLM 的出现使范式从为特定 NLP 任务构建专用模型转变为使用单个大型模型，通过提示或微调来处理各种语言任务。这使得复杂的语言处理更加普及，但同时也带来了效率、伦理和部署方面的新挑战。

然而，LLM 也有重要的局限性：

  * **幻觉（Hallucinations）** ：它们可能自信地生成错误信息
  * **缺乏真正的理解** ：它们缺乏对世界的真正理解，纯粹基于统计模式运作
  * **偏见（Bias）** ：它们可能复现训练数据或输入中存在的偏见
  * **上下文窗口（Context windows）** ：上下文窗口有限（尽管正在改善）
  * **计算资源** ：需要大量计算资源

## [](#why-is-it-challenging) 为什么语言处理具有挑战性？

计算机处理信息的方式与人类不同。例如，当我们读到"我饿了"这句话时，我们可以轻松理解其含义。同样，给定"我饿了"和"我难过"两句话，我们也能轻松判断它们的相似程度。对于机器学习（ML）模型来说，这些任务更加困难。文本需要以模型能够学习的方式进行处理。由于语言很复杂，我们需要仔细思考如何进行这种处理。关于如何表示文本已经进行了大量研究，我们将在下一章中探讨一些方法。

即使在 LLM 取得进展的情况下，许多基本挑战仍然存在。这些包括理解歧义、文化背景、讽刺和幽默。LLM 通过对多样化数据集的大规模训练来应对这些挑战，但在许多复杂场景中仍然经常达不到人类水平的理解。

[ 在 GitHub 上更新](https://github.com/huggingface/course/blob/main/chapters/en/chapter1/2.mdx)

[←简介](/learn/llm-course/chapter1/1) [Transformer 能做什么？→](/learn/llm-course/chapter1/3)

[自然语言处理与大语言模型](#natural-language-processing-and-large-language-models)[什么是 NLP？](#what-is-nlp)[大语言模型（LLM）的崛起](#rise-of-llms)[为什么语言处理具有挑战性？](#why-is-it-challenging)
