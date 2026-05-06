[跳转到主要内容](#main-content)

__返回顶部

__ `Ctrl`+`K`

评价此页面

★ ★ ★ ★ ★

beginner/blitz/neural_networks_tutorial

![](../../_static/img/pytorch-colab.svg) 在 Google Colab 中运行 Colab ![](../../_static/img/pytorch-download.svg) 下载 Notebook Notebook ![](../../_static/img/pytorch-github.svg) 在 GitHub 上查看 GitHub

提示

[跳转到页面底部](#sphx-glr-download-beginner-blitz-neural-networks-tutorial-py)下载完整示例代码。

# 神经网络[#](#neural-networks "Link to this heading")

创建日期：2017 年 3 月 24 日 | 最后更新：2025 年 12 月 3 日 | 最后验证：2024 年 11 月 5 日

可以使用 `torch.nn` 包来构建神经网络。

你已经对 `autograd` 有了初步了解，`nn` 依赖 `autograd` 来定义模型并对其进行微分。一个 `nn.Module` 包含若干层，以及一个返回 `output` 的 `forward(input)` 方法。

例如，看看这个对数字图像进行分类的网络：

![convnet](../../_images/mnist.png)

convnet[#](#id1 "Link to this image")

这是一个简单的前馈网络。它接收输入，依次通过若干层处理，最后给出输出。

神经网络的典型训练过程如下：

  * 定义具有一些可学习参数（或权重）的神经网络

  * 迭代处理数据集中的输入

  * 通过网络处理输入

  * 计算损失（输出距离正确结果有多远）

  * 将梯度反向传播到网络参数中

  * 更新网络的权重，通常使用简单的更新规则：`weight = weight - learning_rate * gradient`

## 定义网络[#](#define-the-network "Link to this heading")

让我们来定义这个网络：


    import torch
    import torch.nn as nn
    import torch.nn.functional as F


    class Net(nn.Module):

        def __init__(self):
            super(Net, self).__init__()
            # 1 个输入图像通道，6 个输出通道，5x5 卷积核
            self.conv1 = nn.Conv2d(1, 6, 5)
            self.conv2 = nn.Conv2d(6, 16, 5)
            # 仿射操作: y = Wx + b
            self.fc1 = nn.Linear(16 * 5 * 5, 120)  # 5*5 来自图像尺寸
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, input):
            # 卷积层 C1: 1 个输入图像通道，6 个输出通道，
            # 5x5 卷积核，使用 RELU 激活函数，
            # 输出大小为 (N, 6, 28, 28) 的张量，其中 N 为批次大小
            c1 = F.relu(self.conv1(input))
            # 下采样层 S2: 2x2 网格，纯函数式，
            # 该层没有任何参数，输出 (N, 6, 14, 14) 的张量
            s2 = F.max_pool2d(c1, (2, 2))
            # 卷积层 C3: 6 个输入通道，16 个输出通道，
            # 5x5 卷积核，使用 RELU 激活函数，
            # 输出 (N, 16, 10, 10) 的张量
            c3 = F.relu(self.conv2(s2))
            # 下采样层 S4: 2x2 网格，纯函数式，
            # 该层没有任何参数，输出 (N, 16, 5, 5) 的张量
            s4 = F.max_pool2d(c3, 2)
            # 展平操作: 纯函数式，输出 (N, 400) 的张量
            s4 = torch.flatten(s4, 1)
            # 全连接层 F5: 输入 (N, 400) 张量，
            # 输出 (N, 120) 张量，使用 RELU 激活函数
            f5 = F.relu(self.fc1(s4))
            # 全连接层 F6: 输入 (N, 120) 张量，
            # 输出 (N, 84) 张量，使用 RELU 激活函数
            f6 = F.relu(self.fc2(f5))
            # 全连接层 OUTPUT: 输入 (N, 84) 张量，
            # 输出 (N, 10) 张量
            output = self.fc3(f6)
            return output


    net = Net()
    print(net)



    Net(
      (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
      (conv2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
      (fc1): Linear(in_features=400, out_features=120, bias=True)
      (fc2): Linear(in_features=120, out_features=84, bias=True)
      (fc3): Linear(in_features=84, out_features=10, bias=True)
    )


你只需要定义 `forward` 函数，`backward` 函数（用于计算梯度）会通过 `autograd` 自动为你定义。你可以在 `forward` 函数中使用任何张量操作。

模型的可学习参数由 `net.parameters()` 返回


    params = list(net.parameters())
    print(len(params))
    print(params[0].size())  # conv1 的 .weight



    10
    torch.Size([6, 1, 5, 5])


让我们尝试一个随机的 32x32 输入。注意：该网络（LeNet）的预期输入大小是 32x32。要在 MNIST 数据集上使用该网络，请将数据集中的图像调整为 32x32。


    input = torch.randn(1, 1, 32, 32)
    out = net(input)
    print(out)



    tensor([[-0.1649,  0.0338,  0.1873,  0.1751, -0.0093, -0.0097,  0.1403, -0.0990,
              0.0222,  0.0980]], grad_fn=<AddmmBackward0>)


将所有参数的梯度缓冲区清零，并使用随机梯度进行反向传播：


    net.zero_grad()
    out.backward(torch.randn(1, 10))


提示

`torch.nn` 仅支持小批次（mini-batch）。整个 `torch.nn` 包只支持作为小批次样本的输入，不支持单个样本。

例如，`nn.Conv2d` 接受一个 4D 张量：`nSamples x nChannels x Height x Width`。

如果你有一个单独的样本，只需使用 `input.unsqueeze(0)` 添加一个假的批次维度。

在继续之前，让我们回顾一下到目前为止你看到的所有类。

**回顾：**


  * `torch.Tensor` - 支持 `backward()` 等自动微分操作的*多维数组*。同时*保存了相对于该张量的梯度*。

  * `nn.Module` - 神经网络模块。*封装参数的便捷方式*，具有将参数移动到 GPU、导出、加载等辅助功能。

  * `nn.Parameter` - 一种张量，当*作为属性分配给 `Module` 时会自动注册为参数*。

  * `autograd.Function` - *实现自动微分操作的前向和反向定义*。每个 `Tensor` 操作至少创建一个 `Function` 节点，该节点连接到创建 `Tensor` 的函数并*编码其历史记录*。

**到目前为止，我们已经介绍了：**


  * 定义神经网络

  * 处理输入和调用反向传播

**剩余内容：**


  * 计算损失

  * 更新网络权重

## 损失函数[#](#loss-function "Link to this heading")

损失函数接收 (output, target) 对作为输入，并计算一个值来估计输出与目标之间的距离。

nn 包中有几种不同的[损失函数](https://pytorch.org/docs/nn.html#loss-functions)。一个简单的损失函数是：`nn.MSELoss`，它计算输出和目标之间的均方误差。

例如：


    output = net(input)
    target = torch.randn(10)  # 一个虚拟的目标值
    target = target.view(1, -1)  # 使其与 output 形状相同
    criterion = nn.MSELoss()

    loss = criterion(output, target)
    print(loss)



    tensor(0.7390, grad_fn=<MseLossBackward0>)


现在，如果你沿着 `loss` 的反向方向追溯，使用它的 `.grad_fn` 属性，你会看到一个计算图，它看起来像这样：


    input -> conv2d -> relu -> maxpool2d -> conv2d -> relu -> maxpool2d
          -> flatten -> linear -> relu -> linear -> relu -> linear
          -> MSELoss
          -> loss


因此，当我们调用 `loss.backward()` 时，整个计算图相对于神经网络参数进行微分，图中所有 `requires_grad=True` 的张量的 `.grad` 张量会累积梯度。

为了说明，让我们追溯几个步骤：


    print(loss.grad_fn)  # MSELoss
    print(loss.grad_fn.next_functions[0][0])  # Linear
    print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # ReLU



    <MseLossBackward0 object at 0x7f7a39f6d5a0>
    <AddmmBackward0 object at 0x7f7a39f6f700>
    <AccumulateGrad object at 0x7f7a39c66c50>


## 反向传播[#](#backprop "Link to this heading")

要反向传播误差，我们只需调用 `loss.backward()`。但在此之前，你需要清空已有的梯度，否则梯度会累积到已有的梯度上。

现在我们将调用 `loss.backward()`，并查看反向传播前后 conv1 的偏置梯度。


    net.zero_grad()     # 清空所有参数的梯度缓冲区

    print('反向传播前 conv1.bias.grad')
    print(net.conv1.bias.grad)

    loss.backward()

    print('反向传播后 conv1.bias.grad')
    print(net.conv1.bias.grad)



    反向传播前 conv1.bias.grad
    None
    反向传播后 conv1.bias.grad
    tensor([-0.0067, -0.0058, -0.0300,  0.0014, -0.0101, -0.0121])


现在，我们已经了解了如何使用损失函数。

**稍后阅读：**

> 神经网络包包含构成深度神经网络基础的各种模块和损失函数。完整列表及文档见[此处](https://pytorch.org/docs/nn)。

**剩下的唯一内容是：**

>   * 更新网络权重
>
>

## 更新权重[#](#update-the-weights "Link to this heading")

实践中使用的最简单的更新规则是随机梯度下降（SGD, Stochastic Gradient Descent）：


    weight = weight - learning_rate * gradient


我们可以用简单的 Python 代码来实现：


    learning_rate = 0.01
    for f in net.parameters():
        f.data.sub_(f.grad.data * learning_rate)


然而，在使用神经网络时，你可能希望使用各种不同的更新规则，如 SGD、Nesterov-SGD、Adam、RMSProp 等。为了实现这一点，我们构建了一个小包：`torch.optim`，它实现了所有这些方法。使用它非常简单：


    import torch.optim as optim

    # 创建优化器
    optimizer = optim.SGD(net.parameters(), lr=0.01)

    # 在训练循环中:
    optimizer.zero_grad()   # 清空梯度缓冲区
    output = net(input)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()    # 执行更新


提示

注意梯度缓冲区需要使用 `optimizer.zero_grad()` 手动清零。这是因为梯度会累积，如[反向传播](#backprop)部分所述。

**脚本总运行时间：**（0 分钟 0.160 秒）

## 文档

访问 PyTorch 的综合开发者文档

[查看文档](https://docs.pytorch.org/docs/stable/index.html)

## 教程

获取面向初学者和高级开发者的深入教程

[查看教程](https://docs.pytorch.org/tutorials)

## 资源

查找开发资源并获得问题解答

[查看资源](https://pytorch.org/resources)

为分析流量和优化你的体验，我们在本网站上使用 Cookie。通过点击或导航，你同意允许我们使用 Cookie。作为本网站的当前维护者，适用 Facebook 的 Cookie 政策。了解更多，包括可用的控制选项：[Cookie 政策](https://opensource.fb.com/legal/cookie-policy)。
