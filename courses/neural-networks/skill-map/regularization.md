# 正则化技能地图

## 目标

学习者能理解过拟合的概念和识别方法，能解释 L1/L2 正则化、Dropout、Batch Normalization 的原理和区别，能在 PyTorch 中正确使用。

## 必会概念

- 过拟合（Overfitting）：训练 loss 低但验证 loss 高
- 欠拟合（Underfitting）：模型能力不足以拟合数据
- 正则化的目的：限制模型复杂度，提高泛化能力
- 偏差-方差权衡（Bias-Variance Tradeoff）

## 核心公式

### L2 正则化（Weight Decay）

```
L_total = L_data + λ/2 * Σ w_i^2

梯度: dL/dw = dL_data/dw + λ * w

效果：权重趋向小值，但不为零
λ 越大，正则化越强
```

### L1 正则化

```
L_total = L_data + λ * Σ |w_i|

效果：权重趋向稀疏（很多变为 0）
适用于特征选择
```

### Dropout

```
训练时：
mask = (np.random.rand(*a.shape) > p)  # p 是丢弃概率
a_dropped = a * mask / (1 - p)          # 缩放

推理时：
a_out = a  # 所有神经元参与，无 dropout

效果：防止神经元共适应，相当于集成多个子网络
```

### Batch Normalization

```
训练时：
μ = mean(x_batch)
σ² = var(x_batch)
x_norm = (x - μ) / sqrt(σ² + ε)
y = γ * x_norm + β        # 可学习参数

running_μ = momentum * running_μ + (1-momentum) * μ
running_σ² = momentum * running_σ² + (1-momentum) * σ²

推理时：
x_norm = (x - running_μ) / sqrt(running_σ² + ε)
y = γ * x_norm + β

效果：加速训练、允许更大学习率、轻微正则化效果
```

## 代码实现

```python
import torch
import torch.nn as nn

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.bn1 = nn.BatchNorm1d(256)
        self.dropout1 = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)          # BN 在激活之前
        x = torch.relu(x)
        x = self.dropout1(x)     # Dropout 在激活之后
        x = self.fc2(x)
        return x

# 使用
model = MyNet()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001,
                              weight_decay=1e-4)  # L2 正则化

# 训练时
model.train()
# ... 训练代码

# 推理时
model.eval()  # 关闭 Dropout，切换 BN 到推理模式
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 推理时不调 eval() | Dropout 还在随机丢弃 | 推理前必须 model.eval() |
| BN 放在激活之后 | 论文常见做法不同 | 先 BN 后激活更常见 |
| Dropout rate 太高 | 过度正则化 | 通常 0.2-0.5 |
| L2 正则化加两次 | 优化器 weight_decay + 手动加 | 只用一种方式 |

## 训练阶梯

1. **概念理解**：用 train/val loss 曲线判断过拟合/欠拟合
2. **L2 实验**：对比加 L2 前后的权重分布
3. **Dropout 实验**：对比 train/eval 模式的输出差异
4. **BN 实验**：对比加 BN 前后的训练速度
5. **PyTorch 实现**：搭建含 Dropout 和 BN 的网络
6. **调参练习**：调整 Dropout rate 和 L2 系数观察效果
7. **综合应用**：在 CNN 中合理组合使用所有正则化手段

## 掌握标准

- 能用 train/val loss 曲线判断过拟合
- 能解释 L1、L2、Dropout、BN 各自的原理
- 能在 PyTorch 中正确使用（含 train/eval 模式切换）
- 能设计合理的正则化策略
