# 损失函数技能地图

## 目标

学习者能写出 MSE、Binary Cross-Entropy、Categorical Cross-Entropy 的公式，能用 NumPy 实现，能根据任务类型选择合适的损失函数。

## 必会概念

- 损失函数衡量预测值和真实值的差距
- 训练的目标是最小化损失函数
- 不同任务需要不同的损失函数
- 损失函数的可导性决定了能否用梯度下降

## 核心公式

### MSE（Mean Squared Error）

```
L = (1/N) * Σ (y_i - y_hat_i)^2

dL/dy_hat = -2/N * (y - y_hat)

适用: 回归问题
特点: 对大误差惩罚更大（平方）
```

### Binary Cross-Entropy

```
L = -(1/N) * Σ [y_i * log(p_i) + (1 - y_i) * log(1 - p_i)]

其中 p_i = sigmoid(z_i)，y_i ∈ {0, 1}

dL/dz = p - y  （非常简洁！）

适用: 二分类问题
特点: 错误越自信惩罚越大
```

### Categorical Cross-Entropy

```
L = -(1/N) * Σ Σ y_ij * log(p_ij)

其中 p = softmax(z)，y 是 one-hot 编码

适用: 多分类问题
```

## 代码实现

```python
import numpy as np

def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def binary_cross_entropy(y_true, y_pred, eps=1e-8):
    # y_pred 是 sigmoid 输出，值在 (0,1)
    y_pred = np.clip(y_pred, eps, 1 - eps)  # 数值稳定
    return -np.mean(y_true * np.log(y_pred) +
                    (1 - y_true) * np.log(1 - y_pred))

def categorical_cross_entropy(y_true, y_pred, eps=1e-8):
    # y_true 是 one-hot，y_pred 是 softmax 输出
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
```

## 任务类型与损失函数对照

| 任务类型 | 输出层激活 | 损失函数 | 为什么 |
|---------|-----------|---------|--------|
| 回归 | 无（线性） | MSE | 输出是连续值 |
| 二分类 | Sigmoid | Binary CE | 输出是概率 |
| 多分类 | Softmax | Categorical CE | 输出是概率分布 |

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 回归用 Softmax 输出 | 不理解 Softmax 输出和为 1 | 回归用线性输出 |
| 分类用 MSE | 不理解 CE 的梯度优势 | CE 在错误时给更大梯度 |
| log(0) 导致 -inf | 没做数值稳定 | clip 到 [eps, 1-eps] |
| BCE 忘记负号 | 公式记忆错误 | log(p) < 0，需要负号使损失为正 |

## 训练阶梯

1. **公式记忆**：写出 MSE 和 BCE 的表达式
2. **手算验证**：给定 y 和 y_hat，手算损失值
3. **NumPy 实现**：写出可运行的损失函数
4. **梯度对比**：对比 MSE 和 BCE 的梯度曲线
5. **场景选择**：给定任务选择正确的损失函数
6. **数值稳定**：实现带 epsilon 的版本

## 掌握标准

- 能写出三种损失函数的公式
- 能手算并用代码验证损失值
- 能解释 "为什么交叉熵比 MSE 更适合分类"
- 能正确匹配任务类型和损失函数
