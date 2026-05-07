# 训练分类器

就是这样。你已经了解了如何定义神经网络、计算损失并更新网络权重。

现在你可能在想，

## 那数据呢？

通常，当你需要处理图像、文本、音频或视频数据时，你可以使用标准的 Python 包将数据加载到 numpy 数组中。然后你可以将这个数组转换为 `torch.*Tensor`。

  * 对于图像，Pillow、OpenCV 等包很有用
  * 对于音频，scipy 和 librosa 等包很有用
  * 对于文本，原始 Python 或基于 Cython 的加载，或 NLTK 和 SpaCy 很有用

特别针对视觉领域，我们创建了一个名为 `torchvision` 的包，它包含常见数据集（如 ImageNet、CIFAR10、MNIST 等）的数据加载器和图像数据转换器，即 `torchvision.datasets` 和 `torch.utils.data.DataLoader`。

这提供了极大的便利，避免了编写样板代码。

在本教程中，我们将使用 CIFAR10 数据集。它的类别有：'airplane'（飞机）、'automobile'（汽车）、'bird'（鸟）、'cat'（猫）、'deer'（鹿）、'dog'（狗）、'frog'（青蛙）、'horse'（马）、'ship'（船）、'truck'（卡车）。CIFAR-10 中的图像大小为 3x32x32，即 3 通道彩色图像，尺寸为 32x32 像素。

## 训练图像分类器

我们将按以下步骤进行：

  1. 使用 `torchvision` 加载并归一化 CIFAR10 训练集和测试集
  2. 定义卷积神经网络
  3. 定义损失函数
  4. 在训练数据上训练网络
  5. 在测试数据上测试网络

### 1. 加载并归一化 CIFAR10

使用 `torchvision`，加载 CIFAR10 非常简单。

    import torch
    import torchvision
    import torchvision.transforms as transforms

torchvision 数据集的输出是范围在 [0, 1] 的 PILImage 图像。我们将它们转换为归一化范围 [-1, 1] 的张量。

> 如果你在 Windows 或 MacOS 上运行本教程并遇到 BrokenPipeError 或与多进程相关的 RuntimeError，请尝试将 torch.utils.data.DataLoader() 的 num_worker 设置为 0。

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    batch_size = 4

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                              shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck)

让我们展示一些训练图像，找点乐趣。

    import matplotlib.pyplot as plt
    import numpy as np

    # 显示图像的函数
    def imshow(img):
        img = img / 2 + 0.5     # 反归一化
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

    # 获取一些随机训练图像
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # 显示图像
    imshow(torchvision.utils.make_grid(images))
    # 打印标签
    print(' '.join(f'{classes[labels[j]]:5s}' for j in range(batch_size)))

### 2. 定义卷积神经网络

从之前复制神经网络并修改它以接收 3 通道图像（而不是之前定义的 1 通道图像）。

    import torch.nn as nn
    import torch.nn.functional as F

    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = torch.flatten(x, 1) # 展平除批次维度外的所有维度
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = Net()

### 3. 定义损失函数和优化器

让我们使用分类交叉熵损失和带动量的 SGD。

    import torch.optim as optim

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

### 4. 训练网络

有趣的部分开始了。我们只需遍历数据迭代器，将输入馈送到网络并优化。

    for epoch in range(2):  # 多次遍历数据集

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # 获取输入；data 是 [inputs, labels] 的列表
            inputs, labels = data

            # 梯度清零
            optimizer.zero_grad()

            # 前向传播 + 反向传播 + 优化
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # 打印统计信息
            running_loss += loss.item()
            if i % 2000 == 1999:    # 每 2000 个小批次打印一次
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    print('训练完成')

让我们快速保存训练好的模型：

    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

有关保存 PyTorch 模型的更多详细信息，请参见[此处](https://pytorch.org/docs/stable/notes/serialization.html)。

### 5. 在测试数据上测试网络

我们已经在训练数据集上训练了 2 遍网络。但我们需要检查网络是否学到了东西。

我们将通过预测神经网络输出的类别标签，并根据真实值进行检查来验证。如果预测正确，我们将样本添加到正确预测列表中。

好的，第一步。让我们显示测试集中的一张图像以熟悉一下。

    dataiter = iter(testloader)
    images, labels = next(dataiter)

    # 打印图像
    imshow(torchvision.utils.make_grid(images))
    print('真实标签: ', ' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))

接下来，让我们加载回保存的模型（注意：这里保存和重新加载模型不是必要的，我们只是这样做来说明如何操作）：

    net = Net()
    net.load_state_dict(torch.load(PATH, weights_only=True))

好的，现在让我们看看神经网络认为上面这些示例是什么：

    outputs = net(images)

输出是 10 个类别的能量值。某个类别的能量越高，网络就越认为图像属于该类别。所以，让我们获取最高能量的索引：

    _, predicted = torch.max(outputs, 1)

    print('预测结果: ', ' '.join(f'{classes[predicted[j]]:5s}'
                                  for j in range(4)))

结果看起来相当不错。

让我们看看网络在整个数据集上的表现。

    correct = 0
    total = 0
    # 因为我们不训练，所以不需要计算输出的梯度
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # 通过网络运行图像计算输出
            outputs = net(images)
            # 具有最高能量的类别就是我们选择的预测
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'网络在 10000 张测试图像上的准确率: {100 * correct // total} %')

这看起来比随机猜测好得多（10% 的准确率，即从 10 个类别中随机选择一个）。看来网络学到了一些东西。

嗯，哪些类别表现良好，哪些类别表现不佳：

    # 准备统计每个类别的预测情况
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    # 同样不需要梯度
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predictions = torch.max(outputs, 1)
            # 收集每个类别的正确预测
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_pred[classes[label]] += 1
                total_pred[classes[label]] += 1

    # 打印每个类别的准确率
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f'类别: {classname:5s} 的准确率为 {accuracy:.1f} %')

好的，接下来呢？

我们如何在 GPU 上运行这些神经网络？

## 在 GPU 上训练

就像你将张量转移到 GPU 一样，你将神经网络转移到 GPU。

让我们首先将设备定义为第一个可见的 CUDA 设备（如果我们有 CUDA 可用的话）：

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # 假设我们在 CUDA 机器上，这应该打印 CUDA 设备：
    print(device)

本节的其余部分假设 `device` 是 CUDA 设备。

然后这些方法将递归地遍历所有模块，并将它们的参数和缓冲区转换为 CUDA 张量：

    net.to(device)

记住，你必须在每一步将输入和目标也发送到 GPU：

    inputs, labels = data[0].to(device), data[1].to(device)

为什么我没有注意到与 CPU 相比有巨大的加速？因为你的网络真的很小。

**练习：** 尝试增加网络的宽度（第一个 `nn.Conv2d` 的参数 2，和第二个 `nn.Conv2d` 的参数 1 -- 它们需要是相同的数字），看看你能获得什么样的加速。

**达到的目标：**

  * 在高层次理解 PyTorch 的张量库和神经网络。
  * 训练一个小型神经网络对图像进行分类

## 在多个 GPU 上训练

如果你想使用所有 GPU 获得更大的加速，请查看[可选：数据并行](data_parallel_tutorial.html)。

## 接下来去哪里？

  * [训练神经网络玩电子游戏](../../intermediate/reinforcement_q_learning.html)
  * [在 ImageNet 上训练最先进的 ResNet 网络](https://github.com/pytorch/examples/tree/master/imagenet)
  * [使用生成对抗网络训练人脸生成器](https://github.com/pytorch/examples/tree/master/dcgan)
  * [使用循环 LSTM 网络训练词级语言模型](https://github.com/pytorch/examples/tree/master/word_language_model)
  * [更多示例](https://github.com/pytorch/examples)
  * [更多教程](https://github.com/pytorch/tutorials)
  * [在论坛上讨论 PyTorch](https://discuss.pytorch.org/)
  * [在 Slack 上与其他用户聊天](https://pytorch.slack.com/messages/beginner/)
