# RNN/LSTM 技能地图

## 目标

学习者能理解 RNN 处理序列数据的原理，掌握 LSTM/GRU 的门控机制，能用 PyTorch 搭建 RNN 模型。

## 必会概念

- 循环神经网络（RNN）：处理变长序列的神经网络
- 隐藏状态（Hidden State）：编码历史信息的向量
- 时间步展开（Unrolling）：将 RNN 展开为多个时间步
- 梯度消失/爆炸：长序列训练的困难
- LSTM（长短时记忆网络）：通过门控机制解决长距离依赖
- GRU（门控循环单元）：LSTM 的简化版本

## RNN 前向传播公式

```
h_t = tanh(W_hh · h_{t-1} + W_xh · x_t + b_h)
y_t = W_hy · h_t + b_y

其中：
  h_t: 当前时间步隐藏状态
  h_{t-1}: 上一时间步隐藏状态
  x_t: 当前时间步输入
  W_hh, W_xh, W_hy: 权重矩阵
```

### 核心问题：梯度消失

```
反向传播时，梯度经过 t 个时间步：
∂L/∂h_1 = ∏(∂h_t/∂h_{t-1}) × ∂L/∂h_t

当 |∂h_t/∂h_{t-1}| < 1 时，连乘后梯度趋近于 0（梯度消失）
当 |∂h_t/∂h_{t-1}| > 1 时，连乘后梯度趋近于无穷（梯度爆炸）
```

## LSTM 门控机制

```
输入: x_t (当前输入), h_{t-1} (上一步隐藏状态), c_{t-1} (上一步细胞状态)

遗忘门: f_t = σ(W_f · [h_{t-1}, x_t] + b_f)     → 决定丢弃哪些旧信息
输入门: i_t = σ(W_i · [h_{t-1}, x_t] + b_i)     → 决定写入哪些新信息
候选值: c̃_t = tanh(W_c · [h_{t-1}, x_t] + b_c) → 新的候选信息
细胞状态: c_t = f_t ⊙ c_{t-1} + i_t ⊙ c̃_t      → 更新细胞状态
输出门: o_t = σ(W_o · [h_{t-1}, x_t] + b_o)     → 决定输出哪些信息
隐藏状态: h_t = o_t ⊙ tanh(c_t)                  → 当前输出

其中: σ 是 sigmoid, ⊙ 是逐元素乘法
```

### 直觉理解

- **遗忘门**：决定"忘掉"哪些旧记忆（如：换了新话题，旧话题的信息不再重要）
- **输入门**：决定"记住"哪些新信息（如：关键名词要记住）
- **输出门**：决定当前时间步输出什么（如：只有到句末才输出分类结果）
- **细胞状态**：信息的"传送带"，能跨越长距离传递信息

## GRU（LSTM 简化版）

```
重置门: r_t = σ(W_r · [h_{t-1}, x_t])
更新门: z_t = σ(W_z · [h_{t-1}, x_t])
候选状态: h̃_t = tanh(W · [r_t ⊙ h_{t-1}, x_t])
隐藏状态: h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t

GRU vs LSTM：合并了细胞状态和隐藏状态，只有两个门
```

## PyTorch 代码示例

```python
import torch
import torch.nn as nn

# 基本 RNN 使用
rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=2, batch_first=True)
# input_size: 输入特征维度
# hidden_size: 隐藏状态维度
# num_layers: RNN 层数
# batch_first: True 表示输入 shape 为 (batch, seq, feature)

# 输入: batch=5, seq_len=8, feature=10
x = torch.randn(5, 8, 10)
output, h_n = rnn(x)
# output: (5, 8, 20) 每个时间步的隐藏状态
# h_n: (2, 5, 20) 最后一个时间步的隐藏状态（每层一个）

# LSTM 使用
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2, batch_first=True)
output, (h_n, c_n) = lstm(x)
# output: (5, 8, 20)
# h_n: (2, 5, 20) 隐藏状态
# c_n: (2, 5, 20) 细胞状态（LSTM 特有）
```

```python
# 用 LSTM 做文本分类
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        # x: (batch, seq_len)
        x = self.embedding(x)              # (batch, seq_len, embed_dim)
        output, (h_n, _) = self.lstm(x)    # h_n: (1, batch, hidden_dim)
        h_n = h_n.squeeze(0)               # (batch, hidden_dim)
        return self.fc(h_n)                # (batch, num_classes)
```

## 常见错误

1. **隐藏状态不重置**：新序列开始时，需要初始化隐藏状态
2. **output 和 h_n 搞混**：output 是所有时间步，h_n 是最后一个时间步
3. **batch_first 参数**：默认是 False，输入 shape 是 (seq, batch, feature)
4. **pack_padded_sequence**：变长序列需要特殊处理
5. **梯度裁剪**：梯度爆炸时需要 `torch.nn.utils.clip_grad_norm_`

## 训练阶梯

1. **RNN 理解**：能手动展开 RNN 的时间步计算
2. **PyTorch RNN**：能用 nn.RNN 处理简单序列
3. **LSTM 理解**：能画出门控结构并解释每个门的作用
4. **PyTorch LSTM**：能用 nn.LSTM 搭建序列模型
5. **NLP 应用**：能用 LSTM 做文本分类或序列标注

## 掌握标准

- 能写出 RNN 的前向传播公式
- 能画出 LSTM 的门控结构图
- 能解释梯度消失的原因和 LSTM 如何缓解
- 能用 PyTorch 搭建 LSTM 文本分类模型
- 能处理变长序列（padding + pack_padded_sequence）
