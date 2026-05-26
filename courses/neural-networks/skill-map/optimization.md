# 优化器技能地图

## 目标

学习者能理解 SGD、Momentum、RMSProp、Adam 的更新公式和各自解决的问题，能用 NumPy 实现并对比收敛行为。

教学时必须拆分推进：先讲清楚 SGD，再讲 Momentum，再讲 RMSProp，最后讲 Adam。每一轮只讲一个优化方法；不得在同一轮同时讲 Momentum 和 Adam，也不得默认学习者已经理解参数、loss、梯度、学习率和"更新一步"。

## 必会概念

- 梯度下降的目标：沿梯度反方向更新参数
- BGD vs SGD vs Mini-batch GD 的区别
- 学习率的作用
- 动量的概念
- 自适应学习率

## 核心公式

### SGD（Stochastic Gradient Descent）

```
w = w - lr * grad

特点：简单，但可能震荡、收敛慢
```

### SGD with Momentum

```
v = beta * v + grad          # 速度（梯度的指数移动平均）
w = w - lr * v

beta 通常取 0.9
特点：加速收敛、减少震荡
```

### RMSProp

```
s = beta * s + (1 - beta) * grad^2   # 梯度平方的指数移动平均
w = w - lr * grad / (sqrt(s) + eps)

特点：自适应学习率，对每个参数不同
解决：不同方向梯度尺度差异大、更新步长不均的问题
```

### Adam（Adaptive Moment Estimation）

```
m = beta1 * m + (1 - beta1) * grad          # 一阶矩（均值）
v = beta2 * v + (1 - beta2) * grad^2        # 二阶矩（方差）

m_hat = m / (1 - beta1^t)                   # 偏差修正
v_hat = v / (1 - beta2^t)

w = w - lr * m_hat / (sqrt(v_hat) + eps)

beta1 = 0.9, beta2 = 0.999, eps = 1e-8
特点：结合 Momentum + RMSProp，最常用的优化器
```

## 代码实现

```python
import numpy as np

class AdamOptimizer:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.m = None  # 一阶矩
        self.v = None  # 二阶矩
        self.t = 0     # 时间步

    def update(self, params, grads):
        if self.m is None:
            self.m = [np.zeros_like(p) for p in params]
            self.v = [np.zeros_like(p) for p in params]

        self.t += 1
        for i in range(len(params)):
            self.m[i] = self.beta1 * self.m[i] + (1 - self.beta1) * grads[i]
            self.v[i] = self.beta2 * self.v[i] + (1 - self.beta2) * grads[i]**2

            m_hat = self.m[i] / (1 - self.beta1**self.t)
            v_hat = self.v[i] / (1 - self.beta2**self.t)

            params[i] -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps)
        return params
```

## 优化器对比

| 优化器 | 优点 | 缺点 | 适用场景 |
|--------|------|------|---------|
| SGD | 简单，泛化好 | 收敛慢，需调 lr | 最终微调 |
| Momentum | 加速收敛 | 需调 beta | 通用 |
| Adam | 快速收敛，自适应 lr | 可能泛化不如 SGD | 默认首选 |

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 偏差修正不理解 | 初期 m/v 偏向 0 | 除以 (1-beta^t) 修正 |
| beta1/beta2 调反 | 不理解各自的含义 | beta1 控制动量，beta2 控制自适应 |
| 认为 Adam 总是最好 | 忽视 SGD 的泛化优势 | 先用 Adam 快速收敛，再用 SGD 微调 |

## 训练阶梯

0. **前置术语**：解释参数/权重、loss、梯度、学习率、更新一步
1. **SGD**：写出 `w = w - lr * grad`，解释每个符号和减号含义
2. **Momentum**：在 SGD 基础上解释速度项 `v`，说明它解决震荡和收敛慢的问题
3. **RMSProp**：解释梯度平方移动平均 `s`，说明它解决不同参数方向尺度差异的问题
4. **Adam**：先确认 Momentum 和 RMSProp 已掌握，再讲一阶矩、二阶矩和偏差修正
5. **NumPy 实现**：分别实现 SGD、Momentum、Adam
6. **收敛对比**：在同一任务上对比三种优化器的 loss 曲线
7. **学习率实验**：对同一优化器调不同学习率
8. **迁移**：在 XOR 上用 Adam 训练，调到收敛最快

## 掌握标准

- 能写出 SGD、Momentum、Adam 的更新公式
- 能用 NumPy 实现至少两种优化器
- 能解释偏差修正的作用
- 能在实验中选择合适的优化器和超参数
