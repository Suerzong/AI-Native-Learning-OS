# 优化器技能地图

## 目标

学习者能理解 SGD、Momentum、RMSProp、Adam 的更新公式和各自解决的问题，能用 NumPy 实现并对比收敛行为。

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
解决：鞍点问题、不同方向梯度差异大
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

1. **公式记忆**：写出四种优化器的更新公式
2. **NumPy 实现**：写出 SGD、Momentum、Adam
3. **收敛对比**：在同一任务上对比三种优化器的 loss 曲线
4. **偏差修正**：解释为什么 Adam 需要偏差修正
5. **学习率实验**：对同一优化器调不同学习率
6. **迁移**：在 XOR 上用 Adam 训练，调到收敛最快

## 掌握标准

- 能写出 SGD、Momentum、Adam 的更新公式
- 能用 NumPy 实现至少两种优化器
- 能解释偏差修正的作用
- 能在实验中选择合适的优化器和超参数
