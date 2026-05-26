# CNN 技能地图

## 目标

学习者能理解卷积操作的直觉和数学定义，能计算卷积输出尺寸，能用 NumPy 实现 2D 卷积，能用 PyTorch 搭建经典 CNN 架构。

## 必会概念

- 卷积操作：用小核在输入上滑动提取局部特征
- 权值共享：同一个卷积核在所有位置使用相同权重
- 特征图（Feature Map）：卷积操作的输出
- 感受野（Receptive Field）：输出一个像素能看到的输入区域
- 池化：下采样操作，减少空间维度

## 核心公式

### 输出尺寸计算

```
H_out = (H_in - K + 2*P) / S + 1
W_out = (W_in - K + 2*P) / S + 1

其中：
- H_in, W_in: 输入高宽
- K: 卷积核大小
- P: padding
- S: stride
```

### 卷积操作

```
输出特征图的每个位置：
out(i, j) = Σ_m Σ_n input(i*S+m, j*S+n) * kernel(m, n) + bias

对多通道输入：
out(i, j) = Σ_c Σ_m Σ_n input_c(i*S+m, j*S+n) * kernel_c(m, n) + bias
```

### 参数量计算

```
单个卷积核参数量 = K * K * C_in + 1（偏置）
总参数量 = (K * K * C_in + 1) * C_out

例：3x3 卷积，输入 3 通道，输出 64 通道
参数量 = (3*3*3 + 1) * 64 = 1,792
```

## 代码实现

```python
import numpy as np

def conv2d(input, kernel, bias, stride=1, padding=0):
    """
    input: (H, W)
    kernel: (K, K)
    返回: (H_out, W_out)
    """
    H, W = input.shape
    K = kernel.shape[0]

    # padding
    if padding > 0:
        input = np.pad(input, padding, mode='constant')

    H_out = (H + 2*padding - K) // stride + 1
    W_out = (W + 2*padding - K) // stride + 1
    output = np.zeros((H_out, W_out))

    for i in range(H_out):
        for j in range(W_out):
            region = input[i*stride:i*stride+K, j*stride:j*stride+K]
            output[i, j] = np.sum(region * kernel) + bias

    return output

# PyTorch 版本
import torch.nn as nn

conv = nn.Conv2d(in_channels=3, out_channels=64,
                  kernel_size=3, stride=1, padding=1)
```

## 经典架构速查

| 架构 | 年份 | 创新点 | 参数量 |
|------|------|--------|--------|
| LeNet-5 | 1998 | 最早 CNN 之一 | ~60K |
| AlexNet | 2012 | ReLU、Dropout、GPU 训练 | ~60M |
| VGG-16 | 2014 | 全用 3x3 小卷积核、更深 | ~138M |

### LeNet-5 结构

```
Input(32x32x1) → Conv(5x5, 6) → AvgPool(2x2) →
Conv(5x5, 16) → AvgPool(2x2) →
FC(120) → FC(84) → FC(10) → Softmax
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 输出尺寸算错 | padding/stride 公式记错 | 先算公式再写代码 |
| 不理解权值共享 | 混淆卷积和全连接 | 一个核只有一组权重 |
| 忘记 flatten | CNN 输出是 3D，FC 需要 1D | 在 FC 前 flatten |
| 参数量算错 | 忘记 bias 或通道维度 | 用公式仔细算 |

## 训练阶梯

1. **输出尺寸计算**：给定输入和卷积参数，算输出尺寸
2. **NumPy 实现**：写出 conv2d 函数
3. **特征可视化**：用边缘检测核观察卷积效果
4. **PyTorch 搭建**：用 nn.Conv2d 搭建 LeNet
5. **MNIST 训练**：在 MNIST 上训练 LeNet
6. **参数量计算**：算出 LeNet 各层的参数量
7. **架构对比**：对比 LeNet、AlexNet、VGG 的设计差异
8. **CIFAR-10**：搭建 CNN 在 CIFAR-10 上训练

## 掌握标准

- 能计算任意卷积层的输出尺寸和参数量
- 能用 NumPy 实现 2D 卷积
- 能画出 LeNet-5 的结构图
- 能用 PyTorch 搭建 CNN 并训练达到 >80% 准确率
