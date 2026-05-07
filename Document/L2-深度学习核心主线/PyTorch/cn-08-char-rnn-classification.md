# 从零开始的 NLP：使用字符级 RNN 分类姓名

**作者：** [Sean Robertson](https://github.com/spro)

本教程是三部分系列的一部分：

  * [从零开始的 NLP：使用字符级 RNN 分类姓名](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)
  * [从零开始的 NLP：使用字符级 RNN 生成姓名](https://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html)
  * [从零开始的 NLP：使用序列到序列网络和注意力机制进行翻译](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)

我们将构建并训练一个基本的字符级循环神经网络（RNN）来对单词进行分类。本教程与其他两个自然语言处理（NLP）"从零开始"教程一起，展示了如何预处理数据以建模 NLP。特别是，这些教程展示了 NLP 预处理建模如何在底层工作。

字符级 RNN 将单词作为一系列字符读取——在每一步输出一个预测和"隐藏状态"，将其先前的隐藏状态反馈到下一步。我们将最终预测作为输出，即单词属于哪个类别。

具体来说，我们将训练来自 18 种语言来源的几千个姓氏，并根据拼写预测姓名来自哪种语言。

## 推荐准备

在开始本教程之前，建议你已安装 PyTorch，并对 Python 编程语言和张量有基本了解。

## 准备数据

从[此处](https://download.pytorch.org/tutorial/data.zip)下载数据并解压到当前目录。

`data/names` 目录中包含 18 个以 `[Language].txt` 命名的文本文件。每个文件包含一堆姓名，每行一个姓名，大部分是罗马化的（但我们仍然需要将 Unicode 转换为 ASCII）。

第一步是定义和清理我们的数据。最初，我们需要将 Unicode 转换为纯 ASCII 以限制 RNN 输入层。这是通过将 Unicode 字符串转换为 ASCII 并只允许一小组允许的字符来完成的。

    allowed_characters = string.ascii_letters + " .,;'" + "_"
    n_letters = len(allowed_characters)

    def unicodeToAscii(s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
            and c in allowed_characters
        )

## 将姓名转换为张量

现在我们有了所有组织好的姓名，我们需要将它们转换为张量以便使用。

为了表示单个字母，我们使用大小为 `<1 x n_letters>` 的"独热向量"。独热向量除当前字母索引处为 1 外，其余位置都填充为 0。

为了组成一个单词，我们将其中一些连接成一个二维矩阵 `<line_length x 1 x n_letters>`。

## 创建网络

这个 CharRNN 类使用三个组件实现了一个 RNN。首先，我们使用 [nn.RNN 实现](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)。接下来，我们定义一个将 RNN 隐藏层映射到输出的层。最后，我们应用 `softmax` 函数。

    class CharRNN(nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(CharRNN, self).__init__()
            self.rnn = nn.RNN(input_size, hidden_size)
            self.h2o = nn.Linear(hidden_size, output_size)
            self.softmax = nn.LogSoftmax(dim=1)

        def forward(self, line_tensor):
            rnn_out, hidden = self.rnn(line_tensor)
            output = self.h2o(hidden[0])
            output = self.softmax(output)
            return output

然后我们可以创建一个具有 58 个输入节点、128 个隐藏节点和 18 个输出的 RNN：

    n_hidden = 128
    rnn = CharRNN(n_letters, n_hidden, len(alldata.labels_uniq))

## 训练

### 训练网络

现在训练这个网络所需要做的就是给它看一堆例子，让它做出猜测，并告诉它是否错了。

我们通过定义一个 `train()` 函数来做到这一点，该函数使用小批次在给定数据集上训练模型。RNN 的训练方式与其他网络类似；因此，为了完整起见，我们在此包含了一个批次训练方法。

    def train(rnn, training_data, n_epoch=10, n_batch_size=64, report_every=50, learning_rate=0.2, criterion=nn.NLLLoss()):
        current_loss = 0
        all_losses = []
        rnn.train()
        optimizer = torch.optim.SGD(rnn.parameters(), lr=learning_rate)

        for iter in range(1, n_epoch + 1):
            rnn.zero_grad()
            batches = list(range(len(training_data)))
            random.shuffle(batches)
            batches = np.array_split(batches, len(batches) // n_batch_size)

            for idx, batch in enumerate(batches):
                batch_loss = 0
                for i in batch:
                    (label_tensor, text_tensor, label, text) = training_data[i]
                    output = rnn.forward(text_tensor)
                    loss = criterion(output, label_tensor)
                    batch_loss += loss

                batch_loss.backward()
                nn.utils.clip_grad_norm_(rnn.parameters(), 3)
                optimizer.step()
                optimizer.zero_grad()
                current_loss += batch_loss.item() / len(batch)

            all_losses.append(current_loss / len(batches))
            if iter % report_every == 0:
                print(f"{iter} ({iter / n_epoch:.0%}): \t 平均批次损失 = {all_losses[-1]}")
            current_loss = 0

        return all_losses

### 绘制结果

绘制来自 `all_losses` 的历史损失显示了网络的学习过程：

    plt.figure()
    plt.plot(all_losses)
    plt.show()

## 评估结果

要查看网络在不同类别上的表现如何，我们将创建一个混淆矩阵，指示每个实际语言（行）中网络猜测的语言（列）。

    def evaluate(rnn, testing_data, classes):
        confusion = torch.zeros(len(classes), len(classes))
        rnn.eval()
        with torch.no_grad():
            for i in range(len(testing_data)):
                (label_tensor, text_tensor, label, text) = testing_data[i]
                output = rnn(text_tensor)
                guess, guess_i = label_from_output(output, classes)
                label_i = classes.index(label)
                confusion[label_i][guess_i] += 1

        for i in range(len(classes)):
            denom = confusion[i].sum()
            if denom > 0:
                confusion[i] = confusion[i] / denom

        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(confusion.cpu().numpy())
        fig.colorbar(cax)
        ax.set_xticks(np.arange(len(classes)), labels=classes, rotation=90)
        ax.set_yticks(np.arange(len(classes)), labels=classes)
        plt.show()

你可以在主对角线外找出亮点，这些显示了它错误猜测的语言，例如韩语被猜成中文，意大利语被猜成西班牙语。它似乎对希腊语表现很好，对英语表现很差（可能是因为与其他语言重叠）。

## 练习

  * 用更大和/或形状更好的网络获得更好的结果
    * 调整超参数以增强性能，例如改变 epoch 数量、批次大小和学习率
    * 尝试 `nn.LSTM` 和 `nn.GRU` 层
    * 修改层的大小，例如增加或减少隐藏节点数量或添加额外的线性层
  * 尝试不同的行 -> 标签数据集，例如：
    * 任何单词 -> 语言
    * 名字 -> 性别
    * 角色名 -> 作者
    * 页面标题 -> 博客或 subreddit
