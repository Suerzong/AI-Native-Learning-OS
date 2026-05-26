# 激活函数技能地图

## 目标

学习者能写出 Sigmoid、Tanh、ReLU、Softmax 的公式和导数，能用 NumPy 实现，能解释各自的优缺点和适用场景。

## 必会概念

- 为什么要用激活函数（引入非线性，否则多层等价于单层）
- 梯度消失和梯度饱和
- 零中心特性
- 死亡 ReLU（Dead ReLU）

## 核心公式

### Sigmoid

```
σ(z) = 1 / (1 + e^(-z))
σ'(z) = σ(z) * (1 - σ(z))

输出范围: (0, 1)
用途: 二分类输出层
问题: 梯度消失（|z| 大时梯度接近 0）
```

### Tanh

```
tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))
tanh'(z) = 1 - tanh(z)^2

输出范围: (-1, 1)
优于 Sigmoid: 零中心（均值接近 0）
问题: 仍有梯度消失
```

### ReLU

```
ReLU(z) = max(0, z)
ReLU'(z) = 1 if z > 0, else 0

输出范围: [0, +∞)
优点: 计算快，缓解梯度消失
问题: Dead ReLU（z < 0 时梯度为 0，神经元 "死亡"）
```

### Softmax

```
softmax(z_i) = e^(z_i) / Σ_j e^(z_j)

输出: 概率分布（和为 1）
用途: 多分类输出层
注意: 输入是 logits（未经归一化的分数）
```

## 代码实现

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def softmax(z):
    z_shifted = z - np.max(z)  # 数值稳定
    exp_z = np.exp(z_shifted)
    return exp_z / np.sum(exp_z)
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| Sigmoid 导数用 z 表示 | 推导时没利用 σ(z) | 用 σ(z)(1-σ(z)) 更简洁 |
| Softmax 不做数值稳定 | 大输入导致 exp 溢出 | 先减去 max(z) |
| 深层用 Sigmoid | 梯度逐层衰减 | 隐藏层用 ReLU |
| 输出层用 ReLU 做分类 | 输出无界且非概率 | 输出层用 Sigmoid 或 Softmax |

## 训练阶梯

1. **公式记忆**：写出四种激活函数的表达式
2. **曲线绘制**：用 matplotlib 画出函数和导数曲线
3. **导数计算**：给定 z 值，手算激活值和梯度
4. **NumPy 实现**：写出可运行的激活函数
5. **梯度消失演示**：模拟 10 层网络的梯度传播
6. **Softmax 验证**：验证输出概率和为 1
7. **数值稳定**：实现带数值稳定的 Softmax
8. **场景选择**：给定任务类型，选择合适的激活函数

## 掌握标准

- 能写出四种激活函数的公式和导数
- 能画出函数曲线并标注梯度消失区域
- 能用 NumPy 实现（含数值稳定版本）
- 能解释 "隐藏层用 ReLU、输出层看任务" 的原则
