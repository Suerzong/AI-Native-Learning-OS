# 大语言模型简介

- 本模块探讨语言模型（Language Model），它估计一个词元（Token）或词元序列在更长词元序列中出现的概率，从而实现文本生成、翻译和摘要等任务。
- 语言模型利用上下文（Context）——目标词元周围的信息——来提高预测准确性，循环神经网络（Recurrent Neural Network）比传统 N-gram 提供更多上下文。
- N-gram 是用于构建语言模型的有序词序列，较长的 N-gram 提供更多上下文但可能遇到稀疏性（Sparsity）问题。
- 词元是语言建模的原子单位，代表单词、子词或字符，对于理解和处理语言至关重要。
- 虽然循环神经网络比 N-gram 改善了上下文理解，但它们有局限性，这为能够同时评估整个上下文的大语言模型（Large Language Model, LLM）的出现铺平了道路。

## 什么是语言模型？

[**语言模型**](</machine-learning/glossary#language-model>)估计一个[**词元**](</machine-learning/glossary#token>)或词元序列在更长词元序列中出现的概率。词元可以是一个单词、一个子词（单词的子集），甚至是一个字符。

#### 点击图标了解更多关于词元的信息。

大多数现代语言模型通过子词进行分词（Tokenization），即按包含语义含义的文本块进行切分。块的长度可以从单个字符（如标点符号或所有格 _s_）到整个单词不等。前缀和后缀可能表示为单独的子词。例如，单词 _unwatched_ 可能由以下三个子词表示：

- un（前缀）
- watch（词根）
- ed（后缀）

单词 _cats_ 可能由以下两个子词表示：

- cat（词根）
- s（后缀）

更复杂的单词如 "antidisestablishmentarianism" 可能表示为六个子词：

- anti
- dis
- establish
- ment
- arian
- ism

分词是语言特定的，因此每个词元的字符数因语言而异。对于英语，一个词元约对应 4 个字符或约 3/4 个单词，因此 400 个词元约等于 300 个英文单词。

词元是语言建模的原子单位或最小单位。

词元现在也被成功应用于[计算机视觉](<https://ai.googleblog.com/2023/03/scaling-vision-transformers-to-22.html>)和[音频生成](<https://ai.googleblog.com/2022/10/audiolm-language-modeling-approach-to.html>)。

考虑以下句子以及可能补全它的词元：

    When I hear rain on my roof, I _______ in my kitchen.

语言模型确定补全该空白的不同词元或词元序列的概率。例如，以下概率表标识了一些可能的词元及其概率：

概率 | 词元
---|---
9.4% | cook soup
5.2% | warm up a kettle
3.6% | cower
2.5% | nap
2.2% | relax

在某些情况下，词元序列可能是整个句子、段落甚至整篇文章。

应用可以使用概率表进行预测。预测可能是最高概率（例如 "cook soup"），也可能是从概率高于某个阈值的词元中随机选择。

估计文本序列中填空内容的概率可以扩展到更复杂的任务，包括：

- 生成文本。
- 将文本从一种语言翻译为另一种语言。
- 文档摘要。

通过对词元的统计模式建模，现代语言模型开发出极其强大的语言内部表示，并可以生成合理的语言。

### N-gram 语言模型

[**N-gram**](</machine-learning/glossary#n-gram>)是用于构建语言模型的有序词序列，其中 N 是序列中的词数。例如，当 N 为 2 时，N-gram 称为 **2-gram**（或[**二元组（Bigram）**](</machine-learning/glossary#bigram>)）；当 N 为 5 时，N-gram 称为 5-gram。给定训练文档中的以下短语：

    you are very nice

得到的 2-gram 如下：

- you are
- are very
- very nice

当 N 为 3 时，N-gram 称为 **3-gram**（或[**三元组（Trigram）**](</machine-learning/glossary#trigram>)）。给定相同短语，得到的 3-gram 为：

- you are very
- are very nice

给定两个词作为输入，基于 3-gram 的语言模型可以预测第三个词的可能性。例如，给定以下两个词：

    orange is

语言模型检查其训练语料库中所有以 `orange is` 开头的不同 3-gram，以确定最可能的第三个词。可能有数百个 3-gram 以 `orange is` 这两个词开头，但你可以只关注以下两种可能性：

    orange is ripe
    orange is cheerful

第一种可能性（`orange is ripe`）中的 orange 指的是水果橙子，而第二种可能性（`orange is cheerful`）中的 orange 指的是颜色橙色。

## 上下文

人类可以保留相对较长的上下文。在观看戏剧的第三幕时，你保留了第一幕中介绍的对角色的记忆。同样，一个长笑话的笑点之所以让你发笑，是因为你能记住笑话铺垫中的上下文。

在语言模型中，**上下文（Context）** 是目标词元之前或之后的有用信息。上下文可以帮助语言模型确定 "orange" 指的是柑橘水果还是颜色。

上下文可以帮助语言模型做出更好的预测，但 3-gram 是否提供了足够的上下文？遗憾的是，3-gram 提供的唯一上下文是前两个词。例如，`orange is` 这两个词没有为语言模型提供足够的上下文来预测第三个词。由于缺乏上下文，基于 3-gram 的语言模型会犯很多错误。

较长的 N-gram 当然比较短的 N-gram 提供更多上下文。然而，随着 N 增大，每个实例的相对出现次数会减少。当 N 变得非常大时，语言模型通常每个 N 词序列只有一个实例，这对预测目标词元没有太大帮助。

### 循环神经网络

[**循环神经网络（Recurrent Neural Network）**](</machine-learning/glossary#recurrent-neural-network>)比 N-gram 提供更多上下文。循环神经网络是一种在词元序列上训练的[**神经网络**](</machine-learning/glossary#neural-network>)。例如，循环神经网络可以_逐渐_学习（并学会忽略）句子中每个词的选定上下文，有点像你在听别人说话时那样。大型循环神经网络可以从几个句子的段落中获取上下文。

虽然循环神经网络比 N-gram 学习更多上下文，但循环神经网络可以推断的有用上下文量仍然相对有限。循环神经网络"逐词元"评估信息。相比之下，大语言模型——下一节的主题——可以同时评估整个上下文。

请注意，训练循环神经网络处理长上下文受到[**梯度消失问题（Vanishing Gradient Problem）**](</machine-learning/glossary#vanishing-gradient-problem>)的限制。

## 练习：检验理解

哪种语言模型对英文文本的预测效果更好？

- 基于 6-gram 的语言模型
- 基于 5-gram 的语言模型

答案取决于训练集的大小和多样性。

如果训练集涵盖数百万个多样化的文档，那么基于 6-gram 的模型可能会优于基于 5-gram 的模型。

**基于 6-gram 的语言模型。**

这种语言模型有更多上下文，但除非该模型在大量文档上训练过，否则大多数 6-gram 将很罕见。

**基于 5-gram 的语言模型。**

这种语言模型上下文较少，因此不太可能优于基于 6-gram 的语言模型。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/embeddings/test-your-knowledge>)

[ 下一页 什么是大语言模型？（15 分钟） arrow_forward  ](</machine-learning/crash-course/llm/transformers>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2026-01-09 UTC。
