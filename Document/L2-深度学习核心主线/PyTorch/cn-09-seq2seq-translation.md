# 从零开始的 NLP：使用序列到序列网络和注意力机制进行翻译

**作者：** [Sean Robertson](https://github.com/spro)

这是**从零开始 NLP**的第三个也是最后一个教程，我们编写自己的类和函数来预处理数据以完成 NLP 建模任务。

在这个项目中，我们将教神经网络将法语翻译成英语。

    [KEY: > 输入, = 目标, < 输出]

    > il est en train de peindre un tableau .
    = he is painting a picture .
    < he is painting a picture .

    > pourquoi ne pas essayer ce vin delicieux ?
    = why not try that delicious wine ?
    < why not try that delicious wine ?

… 成功率各不相同。

这是通过简单但强大的[序列到序列网络](https://arxiv.org/abs/1409.3215)思想实现的，其中两个循环神经网络协同工作将一个序列转换为另一个序列。编码器网络将输入序列压缩成一个向量，解码器网络将该向量展开成一个新的序列。

为了改进这个模型，我们将使用[注意力机制](https://arxiv.org/abs/1409.0473)，它让解码器学会在输入序列的特定范围内聚焦。

**推荐阅读：**

我假设你至少安装了 PyTorch，了解 Python，并理解张量。

**需求**

    from __future__ import unicode_literals, print_function, division
    from io import open
    import unicodedata
    import re
    import random

    import torch
    import torch.nn as nn
    from torch import optim
    import torch.nn.functional as F

    import numpy as np
    from torch.utils.data import TensorDataset, DataLoader, RandomSampler

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

## 加载数据文件

本项目的数据是一组数以千计的英语到法语的翻译对。

英语到法语的翻译对太大，无法包含在仓库中，所以请先下载到 `data/eng-fra.txt`。该文件是以制表符分隔的翻译对列表：

    I am cold.    J'ai froid.

> 从[此处](https://download.pytorch.org/tutorial/data.zip)下载数据并解压到当前目录。

类似于字符级 RNN 教程中使用的字符编码，我们将把语言中的每个单词表示为一个独热向量，或除单个 1（在单词索引处）外全为 0 的大向量。我们将需要每个单词的唯一索引，以便稍后用作网络的输入和目标。为了跟踪所有这些，我们将使用一个名为 `Lang` 的辅助类，它有 word -> index（`word2index`）和 index -> word（`index2word`）字典，以及每个单词的计数 `word2count`。

    class Lang:
        def __init__(self, name):
            self.name = name
            self.word2index = {}
            self.word2count = {}
            self.index2word = {0: "SOS", 1: "EOS"}
            self.n_words = 2

        def addSentence(self, sentence):
            for word in sentence.split(' '):
                self.addWord(word)

        def addWord(self, word):
            if word not in self.word2index:
                self.word2index[word] = self.n_words
                self.word2count[word] = 1
                self.index2word[self.n_words] = word
                self.n_words += 1
            else:
                self.word2count[word] += 1

准备数据的完整过程是：

  * 读取文本文件并分成行，将行分成对
  * 规范化文本，按长度和内容过滤
  * 从成对的句子中制作单词列表

## Seq2Seq 模型

循环神经网络（RNN）是在序列上操作并使用自己的输出作为后续步骤输入的网络。

[序列到序列网络](https://arxiv.org/abs/1409.3215)，或 seq2seq 网络，或[编码器-解码器网络](https://arxiv.org/pdf/1406.1078v3.pdf)，是由两个 RNN 组成的模型，称为编码器和解码器。编码器读取输入序列并输出单个向量，解码器读取该向量以产生输出序列。

### 编码器

seq2seq 网络的编码器是一个 RNN，它为输入句子中的每个单词输出一些值。对于每个输入单词，编码器输出一个向量和一个隐藏状态，并将隐藏状态用于下一个输入单词。

    class EncoderRNN(nn.Module):
        def __init__(self, input_size, hidden_size, dropout_p=0.1):
            super(EncoderRNN, self).__init__()
            self.hidden_size = hidden_size
            self.embedding = nn.Embedding(input_size, hidden_size)
            self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
            self.dropout = nn.Dropout(dropout_p)

        def forward(self, input):
            embedded = self.dropout(self.embedding(input))
            output, hidden = self.gru(embedded)
            return output, hidden

### 解码器

解码器是另一个 RNN，它接收编码器输出向量并输出单词序列以创建翻译。

#### 简单解码器

在最简单的 seq2seq 解码器中，我们只使用编码器的最后一个输出。这个最后的输出有时被称为_上下文向量_，因为它编码了来自整个序列的上下文。

#### 注意力解码器

如果只有上下文向量在编码器和解码器之间传递，那么单个向量就承担了编码整个句子的负担。

注意力允许解码器网络在解码器自身输出的每一步"聚焦"于编码器输出的不同部分。我们首先计算一组_注意力权重_。这些权重将与编码器输出向量相乘以创建加权组合。

Bahdanau 注意力，也称为加性注意力，是序列到序列模型中常用的注意力机制，特别是在神经机器翻译任务中。

    class BahdanauAttention(nn.Module):
        def __init__(self, hidden_size):
            super(BahdanauAttention, self).__init__()
            self.Wa = nn.Linear(hidden_size, hidden_size)
            self.Ua = nn.Linear(hidden_size, hidden_size)
            self.Va = nn.Linear(hidden_size, 1)

        def forward(self, query, keys):
            scores = self.Va(torch.tanh(self.Wa(query) + self.Ua(keys)))
            scores = scores.squeeze(2).unsqueeze(1)
            weights = F.softmax(scores, dim=-1)
            context = torch.bmm(weights, keys)
            return context, weights

    class AttnDecoderRNN(nn.Module):
        def __init__(self, hidden_size, output_size, dropout_p=0.1):
            super(AttnDecoderRNN, self).__init__()
            self.embedding = nn.Embedding(output_size, hidden_size)
            self.attention = BahdanauAttention(hidden_size)
            self.gru = nn.GRU(2 * hidden_size, hidden_size, batch_first=True)
            self.out = nn.Linear(hidden_size, output_size)
            self.dropout = nn.Dropout(dropout_p)

        def forward(self, encoder_outputs, encoder_hidden, target_tensor=None):
            batch_size = encoder_outputs.size(0)
            decoder_input = torch.empty(batch_size, 1, dtype=torch.long, device=device).fill_(SOS_token)
            decoder_hidden = encoder_hidden
            decoder_outputs = []
            attentions = []

            for i in range(MAX_LENGTH):
                decoder_output, decoder_hidden, attn_weights = self.forward_step(
                    decoder_input, decoder_hidden, encoder_outputs
                )
                decoder_outputs.append(decoder_output)
                attentions.append(attn_weights)

                if target_tensor is not None:
                    decoder_input = target_tensor[:, i].unsqueeze(1)
                else:
                    _, topi = decoder_output.topk(1)
                    decoder_input = topi.squeeze(-1).detach()

            decoder_outputs = torch.cat(decoder_outputs, dim=1)
            decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
            attentions = torch.cat(attentions, dim=1)
            return decoder_outputs, decoder_hidden, attentions

## 训练

### 准备训练数据

为了训练，对于每个对，我们需要一个输入张量（输入句子中单词的索引）和目标张量（目标句子中单词的索引）。在创建这些向量时，我们将 EOS 标记附加到两个序列。

### 训练模型

为了训练，我们通过编码器运行输入句子，并跟踪每个输出和最新的隐藏状态。然后解码器被给予 `<SOS>` 令牌作为其第一个输入，以及编码器的最后隐藏状态作为其第一个隐藏状态。

"教师强制"是使用真实目标输出作为每个下一个输入的概念，而不是使用解码器的猜测作为下一个输入。

整个训练过程如下：

  * 启动计时器
  * 初始化优化器和损失函数
  * 创建训练对集合
  * 为空绘图创建空损失数组

然后我们多次调用 `train`，偶尔打印进度（样本百分比、到目前为止的时间、预计时间）和平均损失。

## 评估

评估与训练大致相同，但没有目标，所以我们只需将解码器的预测反馈到自身每一步。每次预测一个单词时，我们将其添加到输出字符串中，如果预测 EOS 标记，我们就在那里停止。我们还存储解码器的注意力输出以便稍后显示。

### 可视化注意力

注意力机制的一个有用特性是其高度可解释的输出。因为它用于加权输入序列的特定编码器输出，我们可以想象在每一步网络最关注的位置。

## 练习

  * 尝试不同的数据集
    * 另一种语言对
    * 人类 -> 机器（例如 IOT 命令）
    * 聊天 -> 回复
    * 问题 -> 答案
  * 用预训练的词嵌入（如 `word2vec` 或 `GloVe`）替换嵌入
  * 尝试更多层、更多隐藏单元和更多句子。比较训练时间和结果。
