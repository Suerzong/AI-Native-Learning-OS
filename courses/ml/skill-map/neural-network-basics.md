# skill-map: neural-network-basics — 神经网络基础（感知机、前向/反向传播）

## 目标

理解神经网络的基本结构和训练过程，为后续深度学习课程打下基础。

## 必知概念

### 感知机（Perceptron）
- **结构**：输入层 -> 加权求和 -> 激活函数 -> 输出
- **公式**：y = f(w1*x1 + w2*x2 + ... + wn*xn + b)
- **激活函数**：
  - 阶跃函数：f(z) = 1 if z >= 0 else 0（感知机原始）
  - Sigmoid：f(z) = 1/(1+e^(-z))（逻辑回归）
  - ReLU：f(z) = max(0, z)（深度学习最常用）
- **局限**：单层感知机只能解决线性可分问题（XOR 问题）

### 多层感知机（MLP）
- **结构**：输入层 -> 隐藏层（多个） -> 输出层
- **万能近似定理**：足够多隐藏层神经元的 MLP 可以近似任何连续函数
- **层与层之间**：全连接（每个神经元与下一层所有神经元相连）

### 前向传播（Forward Propagation）
- **过程**：输入数据从输入层逐层传递到输出层
- **每一层的操作**：z = W * x + b，a = f(z)
- **输出**：模型的预测值

### 反向传播（Backward Propagation）
- **目标**：计算损失函数对每个参数的梯度
- **链式法则**：dL/dw = dL/da * da/dz * dz/dw
- **过程**：从输出层反向逐层计算梯度
- **梯度下降**：用梯度更新参数 w = w - alpha * dL/dw

### 深度学习 vs 传统 ML

| 特性 | 传统 ML | 深度学习 |
|------|---------|----------|
| 特征工程 | 需要手动设计 | 自动学习特征 |
| 数据量 | 小数据也能工作 | 需要大量数据 |
| 计算资源 | CPU 即可 | 通常需要 GPU |
| 可解释性 | 较强 | 较弱（黑盒） |
| 模型大小 | 通常较小 | 通常较大 |
| 适用场景 | 结构化数据 | 图像、语音、文本 |

### 常见网络类型
- **全连接网络（FC/MLP）**：适合结构化数据
- **卷积神经网络（CNN）**：适合图像处理
- **循环神经网络（RNN/LSTM）**：适合序列数据
- **Transformer**：适合 NLP 和越来越多的领域

## 必知公式

### 前向传播
```
z = W * x + b
a = activation(z)
```

### 常见激活函数
```
Sigmoid:  f(z) = 1 / (1 + e^(-z))
ReLU:     f(z) = max(0, z)
Softmax:  f(z_i) = e^(z_i) / sum(e^(z_j))
```

### 反向传播（简化）
```
dL/dW = dL/da * da/dz * dz/dW
dz/dW = x
da/dz = activation'(z)
```

## 常见错误

1. **混淆前向传播和反向传播**
   - 前向传播：计算预测值（从输入到输出）
   - 反向传播：计算梯度（从输出到输入）

2. **激活函数选择不当**
   - 输出层二分类：用 Sigmoid
   - 输出层多分类：用 Softmax
   - 隐藏层：优先用 ReLU

3. **学习率过大导致发散**
   ```python
   # 学习率太大
   optimizer = SGD(lr=10.0)  # 损失爆炸

   # 合适的学习率
   optimizer = SGD(lr=0.01)
   ```

## 训练阶梯

### Step 1: 感知机理解（Level 0→1）
- 理解加权求和 + 激活函数
- 理解线性可分问题
- 了解 XOR 问题

### Step 2: 多层网络（Level 1→2）
- 理解多层结构
- 理解隐藏层的作用
- 了解万能近似定理

### Step 3: 前向传播（Level 2）
- 手动计算一个简单网络的前向传播
- 理解矩阵乘法的作用
- 理解激活函数的非线性

### Step 4: 反向传播（Level 2→3）
- 理解链式法则
- 手动计算一个简单网络的反向传播
- 理解梯度下降

### Step 5: 深度学习 vs ML（Level 3）
- 对比两种方法的优缺点
- 理解各自适用的场景
- 为边缘 AI 部署考虑选择

### Step 6: 实际网络（Level 3→4）
- 用 sklearn 的 MLPClassifier 训练
- 了解 CNN/RNN 的基本概念
- 理解网络类型的选择依据

## 掌握标准

- **Level 3**: 能解释前向传播和反向传播的过程，能用框架训练简单网络
- **Level 4**: 能选择合适的网络结构，能调参优化
- **Level 5**: 能从零实现一个简单的神经网络

## 参考资料

- materials/noob/039_ml-structure-of-neural-networks.md
- materials/noob/040_ml-forward-and-backward-propagation.md
- materials/noob/041_ml-deep-learning-traditional-machine-learning.md
- materials/noob/042_ml-common-network-types.md
