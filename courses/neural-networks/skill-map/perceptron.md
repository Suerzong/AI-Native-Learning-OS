# 感知机技能地图

## 目标

学习者能理解感知机的数学原理，能用 NumPy 实现感知机并训练简单逻辑门，能解释为什么 XOR 需要多层网络。

## 必会概念

- 感知机模型：加权求和 + 激活函数
- 权重（weight）和偏置（bias）
- 阶跃函数（Step Function）作为激活
- 线性可分
- 感知机收敛定理

## 核心公式

```
y = f(Σ w_i * x_i + b) = f(W·X + b)

其中：
- X: 输入向量 (n,)
- W: 权重向量 (n,)
- b: 标量偏置
- f: 激活函数（阶跃函数）
- y: 输出（0 或 1）

权重更新规则：
Δw = η * (y_true - y_pred) * x
w_new = w_old + Δw
```

## 代码实现

```python
import numpy as np

class Perceptron:
    def __init__(self, n_inputs, lr=0.1):
        self.W = np.random.randn(n_inputs) * 0.1
        self.b = 0.0
        self.lr = lr

    def step(self, z):
        return 1.0 if z >= 0 else 0.0

    def predict(self, x):
        z = np.dot(self.W, x) + self.b
        return self.step(z)

    def train(self, X, y, epochs=100):
        for _ in range(epochs):
            for xi, yi in zip(X, y):
                y_pred = self.predict(xi)
                error = yi - y_pred
                self.W += self.lr * error * xi
                self.b += self.lr * error
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 忘记偏置项 | 把模型简化为 y = f(W·X) | 偏置决定决策边界的位置 |
| 学习率太大导致震荡 | 权重更新步长过大 | 降到 0.01-0.1 |
| XOR 收敛不了 | XOR 不是线性可分的 | 需要多层网络（MLP） |
| 阶跃函数不可导 | 无法用梯度下降 | 后续用 Sigmoid 替代 |

## 训练阶梯

1. **概念理解**：解释感知机的输入、权重、输出分别是什么
2. **公式记忆**：写出 y = f(W·X + b) 和 Δw = η(y-y_hat)x
3. **代码跟做**：跟着写出 Perceptron 类
4. **数值验证**：给定 W 和 X，手算输出并用代码验证
5. **训练 AND 门**：用感知机训练 AND 逻辑门
6. **理解 XOR**：尝试 XOR，理解为什么收敛不了，画图说明
7. **独立实现**：不看参考，从零写出感知机并训练 OR 门
8. **迁移**：修改感知机用不同的激活函数，观察行为变化

## 掌握标准

- 能写出感知机的数学表达式和权重更新规则
- 能用 NumPy 实现感知机并成功训练 AND/OR 门
- 能解释为什么 XOR 需要多层网络（画图证明线性不可分）
- 能解释学习率对训练的影响
