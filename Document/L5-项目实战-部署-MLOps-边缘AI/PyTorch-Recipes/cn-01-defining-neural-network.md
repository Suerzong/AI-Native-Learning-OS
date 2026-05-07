# 在 PyTorch 中定义神经网络

> 来源：https://docs.pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html

深度学习使用人工神经网络（模型），它是由多层互连单元组成的计算系统。通过将数据传递通过这些互连单元，神经网络能够学习如何近似将输入转换为输出所需的计算。在 PyTorch 中，可以使用 `torch.nn` 包来构建神经网络。

## 简介

PyTorch 提供了优雅设计的模块和类，包括 `torch.nn`，来帮助你创建和训练神经网络。`nn.Module` 包含层和一个返回 `output` 的 `forward(input)` 方法。

在本教程中，我们将使用 `torch.nn` 定义一个用于 [MNIST 数据集](https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html#torchvision.datasets.MNIST)的神经网络。

## 步骤

1. 导入加载数据所需的所有库
2. 定义并初始化神经网络
3. 指定数据如何通过你的模型
4. [可选] 将数据通过你的模型进行测试

### 1. 导入所需库

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
```

### 2. 定义并初始化神经网络

我们的网络将识别图像。我们将使用 PyTorch 中内置的称为卷积（Convolution）的过程。卷积将图像的每个元素与其局部邻居相加，由核（Kernel）或小矩阵加权，帮助我们从输入图像中提取特定特征（如边缘检测、锐度、模糊等）。

定义模型的 `Net` 类有两个要求。首先是编写一个引用 `nn.Module` 的 `__init__` 函数。此函数用于定义神经网络中的全连接层（Fully Connected Layer）。

```python
class Net(nn.Module):
    def __init__(self):
      super(Net, self).__init__()

      # 第一个 2D 卷积层，接收 1 个输入通道（图像），
      # 输出 32 个卷积特征，卷积核大小为 3
      self.conv1 = nn.Conv2d(1, 32, 3, 1)
      # 第二个 2D 卷积层，接收 32 个输入层，
      # 输出 64 个卷积特征，卷积核大小为 3
      self.conv2 = nn.Conv2d(32, 64, 3, 1)

      # 确保相邻像素要么全为 0 要么全激活
      # 带有输入概率
      self.dropout1 = nn.Dropout2d(0.25)
      self.dropout2 = nn.Dropout2d(0.5)

      # 第一个全连接层
      self.fc1 = nn.Linear(9216, 128)
      # 输出 10 个标签的第二个全连接层
      self.fc2 = nn.Linear(128, 10)

my_nn = Net()
print(my_nn)
```

### 3. 指定数据如何通过你的模型

使用 PyTorch 构建模型时，只需定义 `forward` 函数，它将数据传入计算图（即我们的神经网络）。这将表示我们的前馈算法。

```python
class Net(nn.Module):
    def __init__(self):
      super(Net, self).__init__()
      self.conv1 = nn.Conv2d(1, 32, 3, 1)
      self.conv2 = nn.Conv2d(32, 64, 3, 1)
      self.dropout1 = nn.Dropout2d(0.25)
      self.dropout2 = nn.Dropout2d(0.5)
      self.fc1 = nn.Linear(9216, 128)
      self.fc2 = nn.Linear(128, 10)

    # x 代表我们的数据
    def forward(self, x):
      # 数据通过 conv1
      x = self.conv1(x)
      # 在 x 上使用 ReLU 激活函数
      x = F.relu(x)

      x = self.conv2(x)
      x = F.relu(x)

      # 对 x 运行最大池化
      x = F.max_pool2d(x, 2)
      # 数据通过 dropout1
      x = self.dropout1(x)
      # 从 start_dim=1 展平 x
      x = torch.flatten(x, 1)
      # 数据通过 fc1
      x = self.fc1(x)
      x = F.relu(x)
      x = self.dropout2(x)
      x = self.fc2(x)

      # 对 x 应用 softmax
      output = F.log_softmax(x, dim=1)
      return output
```

### 4. [可选] 将数据通过你的模型进行测试

```python
# 等同于一个随机的 28x28 图像
random_data = torch.rand((1, 1, 28, 28))

my_nn = Net()
result = my_nn(random_data)
print(result)
```

恭喜！你已成功在 PyTorch 中定义了一个神经网络。

## 了解更多

- [PyTorch 中的 state_dict 是什么](https://pytorch.org/tutorials/recipes/recipes/what_is_state_dict.html)
- [在 PyTorch 中保存和加载模型进行推理](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_models_for_inference.html)
