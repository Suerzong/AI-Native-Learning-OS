# CNN 图像分类实战技能地图

## 目标

学习者能构建 CNN 完成图像分类任务（MNIST、CIFAR-10），能调试训练过程，能达到合理的准确率。

## 必会概念

- 卷积层（Conv2d）：提取局部特征
- 池化层（MaxPool2d）：降低空间分辨率
- 全连接层（Linear）：分类决策
- Batch Normalization：稳定训练
- Dropout：防止过拟合
- 特征图（Feature Map）：卷积层的输出
- 参数量计算：(K*K*in_channels) * out_channels + out_channels

## 典型 CNN 架构

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    """MNIST 分类 CNN"""
    def __init__(self):
        super().__init__()
        # 输入: (batch, 1, 28, 28)
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)   # → (batch, 32, 28, 28)
        self.pool = nn.MaxPool2d(2)                     # → (batch, 32, 14, 14)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)   # → (batch, 64, 14, 14)
        # pool → (batch, 64, 7, 7)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)     # flatten: (batch, 3136)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)                # 不加 softmax
        return x
```

```python
class CIFAR10CNN(nn.Module):
    """CIFAR-10 分类 CNN"""
    def __init__(self):
        super().__init__()
        # 输入: (batch, 3, 32, 32)
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),    # → (batch, 32, 32, 32)
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),                    # → (batch, 32, 16, 16)
            nn.Conv2d(32, 64, 3, padding=1),   # → (batch, 64, 16, 16)
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),                    # → (batch, 64, 8, 8)
            nn.Conv2d(64, 128, 3, padding=1),  # → (batch, 128, 8, 8)
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),                    # → (batch, 128, 4, 4)
        )
        self.classifier = nn.Sequential(
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)     # (batch, 2048)
        x = self.classifier(x)
        return x
```

## Shape 追踪模板

```
输入: (batch, 3, 32, 32)
Conv2d(3, 32, 3, padding=1)  → (batch, 32, 32, 32)
BatchNorm2d(32)              → (batch, 32, 32, 32)  shape不变
ReLU()                       → (batch, 32, 32, 32)  shape不变
MaxPool2d(2)                 → (batch, 32, 16, 16)
Conv2d(32, 64, 3, padding=1) → (batch, 64, 16, 16)
BatchNorm2d(64)              → (batch, 64, 16, 16)
ReLU()                       → (batch, 64, 16, 16)
MaxPool2d(2)                 → (batch, 64, 8, 8)
flatten                      → (batch, 64*8*8) = (batch, 4096)
Linear(4096, 10)             → (batch, 10)
```

## 调参经验

| 超参数 | MNIST 推荐 | CIFAR-10 推荐 |
|--------|-----------|---------------|
| batch_size | 64 | 64-128 |
| learning_rate | 0.001 | 0.001 |
| optimizer | Adam | Adam |
| epochs | 10 | 20-50 |
| 预期准确率 | 99%+ | 75-85%（简单CNN）|

## 常见错误

1. Conv2d → Linear 的 flatten 维度算错
2. 输出层加了 ReLU（限制了输出范围）
3. 模型太大、数据太少导致过拟合
4. 忘记 to(device)
5. 验证时忘记 eval() + no_grad()

## 掌握标准

- MNIST 准确率 98%+
- CIFAR-10 准确率 75%+（简单 CNN）
- 能画出网络结构图和每层 shape
- 能解释每个层的作用
- 能用 Sequential 快速搭建网络
