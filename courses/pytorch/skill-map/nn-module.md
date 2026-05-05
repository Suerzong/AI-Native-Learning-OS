# nn.Module 技能地图

## 目标

学习者能创建 nn.Module 子类，能组合各种层构建网络，能正确计算每一层的输出 shape。

## 必会概念

- nn.Module：所有 PyTorch 模型的基类
- `__init__`：定义层（自动注册参数）
- `forward`：定义前向传播逻辑
- parameters()：返回所有可学习参数
- named_parameters()：返回参数名和参数
- children() / modules()：返回子模块
- train() / eval()：切换训练/推理模式

## 必会 API

| 类 | 用途 | 关键参数 |
|------|------|---------|
| `nn.Module` | 模型基类 | - |
| `nn.Linear(in, out)` | 全连接层 | in_features, out_features |
| `nn.Conv2d(in_c, out_c, k, stride, padding)` | 2D 卷积 | 通道数、核大小、步长、填充 |
| `nn.BatchNorm2d(num_features)` | 批归一化 | 通道数 |
| `nn.ReLU(inplace=)` | 激活函数 | inplace 是否原地操作 |
| `nn.Dropout(p=)` | Dropout 正则化 | 丢弃概率 |
| `nn.MaxPool2d(kernel_size)` | 最大池化 | 核大小 |
| `nn.AvgPool2d(kernel_size)` | 平均池化 | 核大小 |
| `nn.Flatten()` | 展平 | - |
| `nn.Sequential(*args)` | 顺序容器 | 层的列表 |

## 代码片段

```python
import torch
import torch.nn as nn

# 基本 Module 结构
class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2)
        self.fc = nn.Linear(16 * 16 * 16, 10)

    def forward(self, x):
        # x: (batch, 3, 32, 32)
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        # x: (batch, 16, 16, 16)
        x = x.view(x.size(0), -1)
        # x: (batch, 4096)
        x = self.fc(x)
        # x: (batch, 10)
        return x

# 使用
model = MyCNN()
print(model)                        # 打印模型结构
print(sum(p.numel() for p in model.parameters()))  # 参数量
output = model(torch.randn(2, 3, 32, 32))          # 前向传播
```

## 输出 Shape 计算公式

### Conv2d
```
output_h = (input_h - kernel_size + 2*padding) / stride + 1
output_w = (input_w - kernel_size + 2*padding) / stride + 1
```

### MaxPool2d
```
output_h = input_h / kernel_size
output_w = input_w / kernel_size
```

## 常见错误

1. 在 `forward()` 里定义层（每次 forward 都创建新参数）
2. 忘记调用 `super().__init__()`
3. 忘记写 `forward()` 方法
4. Conv2d → Linear 过渡处 flatten 维度算错
5. 输出层用 ReLU（分类任务最后不加激活函数）

## 训练阶梯

1. **识别**：打印模型结构，理解每层参数
2. **Shape 追踪**：手动计算每层输出 shape
3. **简单修改**：增加/减少一层
4. **自定义网络**：从零构建 MLP
5. **构建 CNN**：组合 Conv2d + BN + ReLU + Pool + Linear

## 掌握标准

- 能从零定义 nn.Module 子类
- 能计算 Conv2d 和 Linear 的输出 shape
- 能用 Sequential 快速构建网络
- 能解释 parameters() 返回什么
- 能理解 train/eval 对不同层的影响
