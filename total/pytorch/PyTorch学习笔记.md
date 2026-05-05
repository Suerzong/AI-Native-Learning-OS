# PyTorch 学习笔记

> 来源：[菜鸟教程 PyTorch](https://www.runoob.com/pytorch/pytorch-tutorial.html)
> 整理日期：2026-05-05

---

## 目录

| 章节 | 内容 |
|------|------|
| 1 | [PyTorch 简介](#1-pytorch-简介) |
| 2 | [环境安装](#2-环境安装) |
| 3 | [PyTorch 基础概念](#3-pytorch-基础概念) |
| 4 | [张量 Tensor](#4-张量-tensor) |
| 5 | [自动求导 Autograd](#5-自动求导-autograd) |
| 6 | [神经网络基础](#6-神经网络基础) |
| 7 | [第一个神经网络](#7-第一个神经网络) |
| 8 | [线性回归](#8-线性回归) |
| 9 | [卷积神经网络 CNN](#9-卷积神经网络-cnn) |
| 10 | [进阶主题概览](#10-进阶主题概览) |

---

## 1. PyTorch 简介

PyTorch 是一个开源的 Python 机器学习库，基于 Torch 库，底层由 C++ 实现，由 Facebook (Meta) 的人工智能研究团队开发。

**核心特性：**

- **动态计算图** — 运行时构建计算图，随时可改，方便调试，接近 Python 原生编程风格
- **自动微分 (Autograd)** — 自动追踪张量操作并计算梯度，通过反向传播实现
- **张量计算** — 类似 NumPy 的多维数组操作，支持 GPU 加速
- **丰富的 API** — 大量预定义层、损失函数、优化算法

**PyTorch 生态系统：**

| 工具库 | 用途 |
|--------|------|
| `torchvision` | 计算机视觉（数据集、模型、图像变换） |
| `torchtext` | 自然语言处理（数据集、预处理） |
| `torchaudio` | 音频处理 |
| `PyTorch Lightning` | 简化 PyTorch 代码的高层库 |

**版本历史里程碑：**

- 2016 — PyTorch 0.1 发布
- 2018 — PyTorch 1.0，增加生产部署能力
- 2020 — PyTorch 1.6，自动混合精度训练
- 2023 — **PyTorch 2.0**，引入编译模式大幅提升性能

---

## 2. 环境安装

### 系统要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10+ / macOS 10.15+ / Linux (Ubuntu 18.04+) |
| Python | 3.8 ~ 3.11（推荐） |
| 内存 | 至少 4GB，推荐 8GB+ |
| GPU（可选） | NVIDIA GPU with CUDA Compute Capability 3.5+ |

### 创建虚拟环境

```bash
# 方式一：conda
conda create -n pytorch_env python=3.10
conda activate pytorch_env

# 方式二：venv
python -m venv pytorch_env
# Windows
pytorch_env\Scripts\activate
# macOS/Linux
source pytorch_env/bin/activate
```

### 安装 PyTorch

```bash
# CPU 版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# GPU 版本（CUDA 12.1）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# conda 安装
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

> 推荐访问 [PyTorch 官网安装工具](https://pytorch.org/get-started/locally/) 根据系统配置选择安装命令。

### 验证安装

```python
import torch
print(torch.__version__)            # 版本号
print(torch.cuda.is_available())    # CUDA 是否可用
```

---

## 3. PyTorch 基础概念

PyTorch 采用**分层架构**设计：

```
┌─────────────────────────────────────────────────────┐
│                  Python API（顶层）                   │
│   torch  |  torch.nn  |  torch.autograd  |  torch.optim  │
├─────────────────────────────────────────────────────┤
│                  C++ 核心（中层）                      │
│   ATen（张量运算核心库） | JIT | Autograd 引擎        │
├─────────────────────────────────────────────────────┤
│                  基础库（底层）                        │
│   TH/THNN（CPU）  |  THC/THCUNN（GPU/CUDA）          │
└─────────────────────────────────────────────────────┘
```

**五大核心概念：**

| 概念 | 说明 |
|------|------|
| **Tensor（张量）** | 核心数据结构，支持多维数组，可在 CPU/GPU 上计算 |
| **Autograd（自动求导）** | 自动计算梯度，实现反向传播 |
| **nn.Module（神经网络）** | 构建神经网络的基类 |
| **Optimizer（优化器）** | SGD、Adam 等，用于更新模型参数 |
| **Device（设备）** | `.to(device)` 将模型/张量移至 GPU 加速 |

---

## 4. 张量 Tensor

张量是 PyTorch 的核心数据结构，类似 NumPy 的多维数组，但支持 GPU 加速和自动梯度。

### 4.1 张量维度

| 类型 | 维度 | 示例 |
|------|------|------|
| 标量 Scalar | 0D | `torch.tensor(3.14)` |
| 向量 Vector | 1D | `torch.tensor([1, 2, 3])` |
| 矩阵 Matrix | 2D | `torch.tensor([[1,2],[3,4]])` |
| 立方体 Cube | 3D | 多个矩阵堆叠（如彩色图像） |
| 更高维 | 4D/5D | 批量图像 `(batch, channel, H, W)` |

### 4.2 创建张量

```python
import torch

# 基本创建方式
x = torch.tensor([1, 2, 3])          # 从列表创建
z = torch.zeros(2, 3)                # 全 0
o = torch.ones(2, 3)                 # 全 1
e = torch.empty(2, 3)                # 未初始化
r = torch.rand(2, 3)                 # 均匀分布 [0, 1)
n = torch.randn(2, 3)                # 正态分布 N(0, 1)
a = torch.arange(0, 10, 2)           # 等差序列 → [0, 2, 4, 6, 8]
l = torch.linspace(0, 1, 5)          # 等间隔 → [0.00, 0.25, 0.50, 0.75, 1.00]
i = torch.eye(3)                     # 单位矩阵

# 从 NumPy 转换
import numpy as np
np_array = np.array([[1, 2], [3, 4]])
tensor = torch.from_numpy(np_array)  # 共享内存！
```

### 4.3 张量属性

```python
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)

tensor.shape          # torch.Size([2, 3])  — 形状
tensor.dtype          # torch.float32       — 数据类型
tensor.device         # cpu                 — 所在设备
tensor.dim()          # 2                   — 维度数
tensor.numel()        # 6                   — 元素总数
tensor.requires_grad  # False               — 是否追踪梯度
tensor.T              # 转置
tensor.item()         # 标量张量取值
```

### 4.4 张量操作

```python
# 基础运算
x + y          # 逐元素加法
x * y          # 逐元素乘法
torch.matmul(x, y)   # 矩阵乘法
torch.dot(x, y)      # 向量点积（仅 1D）
x.sum() / x.mean() / x.max() / x.min()

# 形状变换
x.view(3, 4)         # 改变形状（不改变数据）
x.reshape(3, 4)      # 更灵活的 reshape
x.unsqueeze(0)       # 在第 0 维添加维度
x.squeeze(0)         # 去掉大小为 1 的维度
torch.cat((x, y), dim=1)   # 按维度拼接

# 索引和切片
tensor[0]            # 第一行
tensor[0, 0]         # 第一行第一列
tensor[:, 1]         # 第二列所有元素

# 条件筛选
mask = tensor > 3
filtered = tensor[tensor > 3]   # 筛选大于 3 的元素
```

### 4.5 CPU 与 GPU 互转

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 张量移到 GPU
tensor_gpu = tensor.to(device)

# 移回 CPU
tensor_cpu = tensor_gpu.cpu()
```

---

## 5. 自动求导 Autograd

自动求导是深度学习框架的核心特性，基于**链式法则**自动计算复杂函数的导数。

### 基本用法

```python
# 创建需要梯度的张量
x = torch.randn(2, 2, requires_grad=True)

# 进行计算（PyTorch 自动构建计算图）
y = x + 2
z = y * y * 3
out = z.mean()

# 反向传播，计算梯度
out.backward()

# 查看梯度
print(x.grad)   # ∂out/∂x 的值
```

### 动态图 vs 静态图

| 特性 | 动态图（PyTorch） | 静态图（早期 TensorFlow） |
|------|-------------------|--------------------------|
| 图构建 | 运行时动态创建 | 执行前构建完成 |
| 灵活性 | 高，支持条件分支和循环 | 低，修改困难 |
| 调试 | 可用标准 Python 调试器 | 需要特殊工具 |

### 关键概念

- `requires_grad=True` — 告诉 PyTorch 需要追踪该张量的操作以计算梯度
- `.backward()` — 反向传播，从标量开始自动计算所有 `requires_grad=True` 张量的梯度
- `.grad` — 存储 `.backward()` 计算得到的梯度值
- `torch.no_grad()` — 评估/推理时禁用梯度计算，节省内存

---

## 6. 神经网络基础

### 6.1 神经元与层

**神经元**是基本单元：接收输入 → 加权求和 + 偏置 → 激活函数 → 输出

**网络层的组成：**

| 层 | 作用 |
|----|------|
| 输入层 (Input) | 接收原始数据 |
| 隐藏层 (Hidden) | 提取特征，可有多层 |
| 输出层 (Output) | 产生预测结果 |

### 6.2 网络类型

- **前馈神经网络 (FNN)** — 数据单向流动，无反馈
- **卷积神经网络 (CNN)** — 用卷积核提取空间特征，适合图像
- **循环神经网络 (RNN)** — 处理序列数据，具有"记忆"能力
- **长短期记忆网络 (LSTM)** — RNN 的变体，学习长期依赖

### 6.3 激活函数

```python
import torch.nn.functional as F

F.relu(x)           # ReLU:  max(0, x)  — 最常用
torch.sigmoid(x)    # Sigmoid: 0~1      — 二分类输出层
torch.tanh(x)       # Tanh: -1~1        — 隐藏层
F.softmax(x, dim=1) # Softmax: 概率分布  — 多分类输出层
```

### 6.4 损失函数

| 损失函数 | 适用场景 |
|----------|----------|
| `nn.MSELoss()` | 回归问题（均方误差） |
| `nn.CrossEntropyLoss()` | 多分类问题 |
| `nn.BCEWithLogitsLoss()` | 二分类问题 |

### 6.5 优化器

```python
import torch.optim as optim

optimizer = optim.SGD(model.parameters(), lr=0.01)      # 随机梯度下降
optimizer = optim.Adam(model.parameters(), lr=0.001)     # 自适应学习率
optimizer = optim.RMSprop(model.parameters(), lr=0.001)  # 均方根传播
```

### 6.6 模型定义模板

在 PyTorch 中，通过继承 `nn.Module` 定义模型，需要实现两个方法：

```python
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(2, 4)   # 输入 2 → 隐藏 4
        self.fc2 = nn.Linear(4, 1)   # 隐藏 4 → 输出 1

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 前向传播
        x = self.fc2(x)
        return x
```

### 6.7 训练流程（六步法）

```
1. 准备数据（DataLoader 加载）
2. 定义损失函数和优化器
3. 前向传播：output = model(X)
4. 计算损失：loss = criterion(output, Y)
5. 反向传播：loss.backward()
6. 更新参数：optimizer.step()
```

```python
for epoch in range(100):
    model.train()              # 设为训练模式
    optimizer.zero_grad()      # 清除梯度
    output = model(X)          # 前向传播
    loss = criterion(output, Y)  # 计算损失
    loss.backward()            # 反向传播
    optimizer.step()           # 更新参数

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
```

---

## 7. 第一个神经网络

用 `nn.Sequential` 快速构建一个二分类网络：

```python
import torch
import torch.nn as nn

# 网络结构：10 → 5 → 1
n_in, n_h, n_out, batch_size = 10, 5, 1, 10

# 创建虚拟数据
x = torch.randn(batch_size, n_in)
y = torch.tensor([[1.0], [0.0], [0.0], [1.0], [1.0],
                  [1.0], [0.0], [0.0], [1.0], [1.0]])

# 用 Sequential 快速定义模型
model = nn.Sequential(
    nn.Linear(n_in, n_h),   # 输入层 → 隐藏层
    nn.ReLU(),              # ReLU 激活
    nn.Linear(n_h, n_out),  # 隐藏层 → 输出层
    nn.Sigmoid()            # Sigmoid 激活（二分类）
)

# 损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 训练 50 轮
for epoch in range(50):
    y_pred = model(x)
    loss = criterion(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/50], Loss: {loss.item():.4f}')
```

---

## 8. 线性回归

线性回归是学习 PyTorch 训练流程的最佳入门实例。

### 完整代码

```python
import torch
import torch.nn as nn

# 1. 准备数据
torch.manual_seed(42)
X = torch.randn(100, 2)               # 100 个样本，2 个特征
true_w = torch.tensor([2.0, 3.0])     # 真实权重
true_b = 4.0                          # 真实偏置
Y = X @ true_w + true_b + torch.randn(100) * 0.1  # 加噪声

# 2. 定义模型
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1)   # 2 输入 → 1 输出

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

# 3. 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4. 训练 1000 轮
for epoch in range(1000):
    model.train()
    predictions = model(X)
    loss = criterion(predictions.squeeze(), Y)  # squeeze 压缩维度
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}')

# 5. 查看结果
print(f'预测权重: {model.linear.weight.data.numpy()}')
print(f'预测偏置: {model.linear.bias.data.numpy()}')

# 6. 评估模式（不计算梯度）
model.eval()
with torch.no_grad():
    predictions = model(X)
```

**关键步骤解析：**

| 步骤 | 代码 | 说明 |
|------|------|------|
| 前向传播 | `model(X)` | 计算预测值 |
| 计算损失 | `criterion(pred, Y)` | 预测 vs 真实 |
| 清除梯度 | `optimizer.zero_grad()` | 防止梯度累积 |
| 反向传播 | `loss.backward()` | 自动计算梯度 |
| 更新参数 | `optimizer.step()` | 梯度下降更新权重 |

---

## 9. 卷积神经网络 CNN

CNN 是计算机视觉的核心技术，通过卷积核提取图像的局部特征。

### CNN 结构

```
输入图像 → [卷积 → ReLU → 池化] × N → 展平 → 全连接层 → Softmax → 分类输出
```

### MNIST 手写数字识别完整示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# 1. 数据加载
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))   # 归一化到 [-1, 1]
])

train_dataset = datasets.MNIST(root='./data', train=True,  transform=transform, download=True)
test_dataset  = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = torch.utils.data.DataLoader(test_dataset,  batch_size=64, shuffle=False)

# 2. 定义 CNN 模型
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)   # 1→32 通道
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  # 32→64 通道
        self.fc1 = nn.Linear(64 * 7 * 7, 128)   # 全连接层
        self.fc2 = nn.Linear(128, 10)            # 10 个类别

    def forward(self, x):
        x = F.relu(self.conv1(x))    # 卷积 + ReLU
        x = F.max_pool2d(x, 2)       # 最大池化 28→14
        x = F.relu(self.conv2(x))    # 卷积 + ReLU
        x = F.max_pool2d(x, 2)       # 最大池化 14→7
        x = x.view(-1, 64 * 7 * 7)   # 展平
        x = F.relu(self.fc1(x))      # 全连接 + ReLU
        x = self.fc2(x)              # 输出层
        return x

model = SimpleCNN()

# 3. 损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# 4. 训练
num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss/len(train_loader):.4f}")

# 5. 测试
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Test Accuracy: {100 * correct / total:.2f}%")
```

### CNN 各层作用

| 层 | 作用 | PyTorch API |
|----|------|-------------|
| 卷积层 | 提取局部特征（边缘、纹理） | `nn.Conv2d(in, out, kernel)` |
| 激活函数 | 引入非线性 | `F.relu()` |
| 池化层 | 降维，保留关键特征 | `F.max_pool2d(x, 2)` |
| 全连接层 | 综合特征，分类/回归 | `nn.Linear(in, out)` |
| 展平 | 多维 → 一维 | `x.view(-1, size)` |

---

## 10. 进阶主题概览

菜鸟教程还覆盖以下进阶内容，完整教程请访问对应链接：

| 主题 | 链接 |
|------|------|
| 数据处理与加载 (Dataset/DataLoader) | [教程链接](https://www.runoob.com/pytorch/pytorch-dataset-dataloader.html) |
| 循环神经网络 RNN | [教程链接](https://www.runoob.com/pytorch/pytorch-recurrent-neural-network.html) |
| 数据集与数据转换 | [Dataset](https://www.runoob.com/pytorch/pytorch-datasets.html) / [Transforms](https://www.runoob.com/pytorch/pytorch-transforms.html) |
| GPU / CUDA 加速 | [教程链接](https://www.runoob.com/pytorch/pytorch-gpu-cuda.html) |
| 损失函数详解 | [教程链接](https://www.runoob.com/pytorch/pytorch-loss-function.html) |
| 学习率调度器 | [教程链接](https://www.runoob.com/pytorch/pytorch-lr-scheduler.html) |
| 迁移学习 | [教程链接](https://www.runoob.com/pytorch/pytorch-transfer-learning.html) |
| 批归一化与 Dropout | [教程链接](https://www.runoob.com/pytorch/pytorch-batchnorm-dropout.html) |
| LSTM / GRU | [教程链接](https://www.runoob.com/pytorch/pytorch-lstm-gru.html) |
| 词嵌入 Embedding | [教程链接](https://www.runoob.com/pytorch/pytorch-embedding.html) |
| 生成对抗网络 GAN | [教程链接](https://www.runoob.com/pytorch/pytorch-gan.html) |
| 自编码器 Autoencoder | [教程链接](https://www.runoob.com/pytorch/pytorch-autoencoder.html) |
| Transformer 模型 | [教程链接](https://www.runoob.com/pytorch/transformer-model.html) |
| 注意力机制 | [教程链接](https://www.runoob.com/pytorch/pytorch-attention.html) |
| 混合精度训练 AMP | [教程链接](https://www.runoob.com/pytorch/pytorch-amp.html) |
| 分布式训练 | [教程链接](https://www.runoob.com/pytorch/pytorch-distributed.html) |
| 模型部署 | [教程链接](https://www.runoob.com/pytorch/pytorch-model-deployment.html) |
| 模型保存和加载 | [教程链接](https://www.runoob.com/pytorch/pytorch-model-save.html) |
| 图像分类实例 | [教程链接](https://www.runoob.com/pytorch/pytorch-image-classification.html) |
| 文本情感分析实例 | [教程链接](https://www.runoob.com/pytorch/pytorch-text-classification.html) |

---

## 参考资源

- PyTorch 官网：<https://pytorch.org/>
- PyTorch 官方文档：<https://pytorch.org/docs/stable/index.html>
- PyTorch 入门教程：<https://pytorch.org/get-started/locally/>
- PyTorch GitHub：<https://github.com/pytorch/pytorch>
- 菜鸟教程 PyTorch：<https://www.runoob.com/pytorch/pytorch-tutorial.html>
