# 反向传播技能地图

## 目标

学习者能理解反向传播的数学原理（链式法则），能手推简单网络的梯度，能用 NumPy 实现反向传播。

## 必会概念

- 链式法则（Chain Rule）
- 计算图（Computational Graph）
- 局部梯度（Local Gradient）
- 上游梯度（Upstream Gradient）
- 梯度流的方向：从 loss 到参数

## 核心公式

### 链式法则（标量）

```
若 y = f(g(x))，则 dy/dx = (dy/dg) * (dg/dx)

反向传播中：
dL/dw = (dL/dz) * (dz/dw)
      = upstream_grad * local_grad
```

### 全连接层的反向传播

```
前向: z = W @ x + b,  a = activation(z)

反向:
dL/dW = dz @ x.T          # (n_out, n_in)
dL/db = dz                # (n_out, 1) 沿 batch 求和
dL/dx = W.T @ dz          # (n_in, 1)

其中 dz = da * activation'(z)  # 逐元素乘法
```

### Sigmoid 的反向传播

```
前向: a = σ(z)

反向: dz = da * a * (1 - a)

其中 da 是上游传来的梯度
```

## 代码实现

```python
import numpy as np

class TwoLayerNetwork:
    def __init__(self, n_in, n_hidden, n_out):
        self.W1 = np.random.randn(n_hidden, n_in) * 0.1
        self.b1 = np.zeros((n_hidden, 1))
        self.W2 = np.random.randn(n_out, n_hidden) * 0.1
        self.b2 = np.zeros((n_out, 1))

    def forward(self, X):
        # X: (n_in, batch_size)
        self.z1 = self.W1 @ X + self.b1       # (n_hidden, batch)
        self.a1 = np.maximum(0, self.z1)       # ReLU
        self.z2 = self.W2 @ self.a1 + self.b2  # (n_out, batch)
        self.a2 = 1.0 / (1.0 + np.exp(-self.z2))  # Sigmoid
        return self.a2

    def backward(self, X, y):
        m = X.shape[1]  # batch_size

        # 输出层梯度 (Sigmoid + BCE 的简洁形式)
        dz2 = self.a2 - y                     # (n_out, batch)
        dW2 = (1/m) * dz2 @ self.a1.T         # (n_out, n_hidden)
        db2 = (1/m) * np.sum(dz2, axis=1, keepdims=True)

        # 隐藏层梯度
        da1 = self.W2.T @ dz2                 # (n_hidden, batch)
        dz1 = da1 * (self.z1 > 0)             # ReLU 导数
        dW1 = (1/m) * dz1 @ X.T               # (n_hidden, n_in)
        db1 = (1/m) * np.sum(dz1, axis=1, keepdims=True)

        return dW1, db1, dW2, db2
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 维度不匹配 | 转置位置搞错 | 每步写出 shape |
| 梯度符号搞反 | 不理解梯度指向增大方向 | w -= lr * grad |
| 忘记除以 m | 没有对 batch 取平均 | 所有梯度除以 batch_size |
| ReLU 导数写错 | z>0 返回 bool 不是 float | 用 .astype(float) |

## 训练阶梯

1. **链式法则练习**：给定复合函数，手写梯度
2. **单层推导**：推导单层网络的 dW 和 db
3. **两层推导**：推导两层网络的完整梯度
4. **维度检查**：验证每个梯度矩阵的 shape 和对应参数一致
5. **NumPy 实现**：写出 TwoLayerNetwork 的 backward
6. **梯度检验**：用数值梯度验证解析梯度是否正确
7. **XOR 训练**：用前向+反向在 XOR 上验证
8. **调试练习**：故意引入维度错误并排查

## 掌握标准

- 能手推两层网络的反向传播（从 loss 到 W1）
- 能用 NumPy 实现反向传播并验证梯度正确
- 能解释 "上游梯度 × 本地梯度" 的含义
- 能通过数值梯度检验解析梯度
