# RNN 技能地图

## 目标

学习者能理解 RNN 处理序列数据的原理，能解释 LSTM 和 GRU 的门控机制，能用 PyTorch 搭建序列模型。

## 必会概念

- 序列数据：时间依赖，顺序重要
- 隐藏状态（Hidden State）：记忆之前时间步的信息
- 梯度消失/爆炸在时间维度上的问题（长期依赖）
- 门控机制：用 sigmoid 控制信息流

## 核心公式

### Vanilla RNN

```
h_t = tanh(W_hh @ h_{t-1} + W_xh @ x_t + b_h)
y_t = W_hy @ h_t + b_y

问题：梯度需要沿时间步连乘
∂h_T/∂h_1 = Π(t=2..T) ∂h_t/∂h_{t-1}
当 ||∂h_t/∂h_{t-1}|| < 1 时 → 梯度消失
当 ||∂h_t/∂h_{t-1}|| > 1 时 → 梯度爆炸
```

### LSTM

```
f_t = σ(W_f @ [h_{t-1}, x_t] + b_f)      # 遗忘门：丢弃哪些旧信息
i_t = σ(W_i @ [h_{t-1}, x_t] + b_i)      # 输入门：写入哪些新信息
c_tilde = tanh(W_c @ [h_{t-1}, x_t] + b_c)  # 候选记忆
c_t = f_t * c_{t-1} + i_t * c_tilde       # Cell State 更新
o_t = σ(W_o @ [h_{t-1}, x_t] + b_o)      # 输出门
h_t = o_t * tanh(c_t)                      # Hidden State

关键：Cell State 的加法更新（c_t = f*c + i*c~）
使梯度可以 "无损" 地流过时间步，解决长期依赖
```

### GRU

```
z_t = σ(W_z @ [h_{t-1}, x_t] + b_z)      # 更新门
r_t = σ(W_r @ [h_{t-1}, x_t] + b_r)      # 重置门
h_tilde = tanh(W @ [r_t * h_{t-1}, x_t] + b)
h_t = (1 - z_t) * h_{t-1} + z_t * h_tilde  # 线性插值

GRU vs LSTM：GRU 少一个门，参数更少，效果通常相当
```

## 代码实现

```python
import torch
import torch.nn as nn

# PyTorch LSTM
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size,
                             batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # x: (batch, seq_len, input_size)
        lstm_out, (h_n, c_n) = self.lstm(x)
        # 取最后一个时间步的输出
        out = self.fc(lstm_out[:, -1, :])
        return out

# 简单 LSTM cell（NumPy 风格伪代码）
def lstm_cell(x_t, h_prev, c_prev, W_f, W_i, W_c, W_o):
    concat = np.concatenate([h_prev, x_t])
    f_t = sigmoid(W_f @ concat)        # 遗忘门
    i_t = sigmoid(W_i @ concat)        # 输入门
    c_hat = np.tanh(W_c @ concat)      # 候选
    c_t = f_t * c_prev + i_t * c_hat   # Cell 更新
    o_t = sigmoid(W_o @ concat)        # 输出门
    h_t = o_t * np.tanh(c_t)           # Hidden 更新
    return h_t, c_t
```

## LSTM vs GRU 对比

| 特性 | LSTM | GRU |
|------|------|-----|
| 门数量 | 3（遗忘、输入、输出） | 2（更新、重置） |
| Cell State | 有 | 无（合并到 h） |
| 参数量 | 更多 | 更少（约少 33%） |
| 长序列 | 通常更好 | 短序列可能更快 |
| 推荐 | 长依赖、大模型 | 参数受限、快速实验 |

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 混淆 h_t 和 c_t | 不理解 Cell State | h_t 是输出，c_t 是记忆 |
| batch_first 设错 | 输入维度顺序不对 | 确认 (batch, seq, feat) |
| 不 detach hidden | 反向传播穿越整个数据集 | 每个 batch 要 detach |
| 序列长度不一致 | 不会用 pack_padded_sequence | 先 padding 再用 pack |

## 训练阶梯

1. **概念理解**：解释 RNN 如何处理变长序列
2. **梯度消失**：演示 Vanilla RNN 的梯度消失
3. **LSTM 门控**：解释遗忘门、输入门、输出门各自的作用
4. **PyTorch 搭建**：用 nn.LSTM 搭建序列模型
5. **序列预测**：做一个简单的序列预测任务
6. **GRU 对比**：用 GRU 替换 LSTM 对比效果
7. **调参实验**：调整 hidden_size 和层数

## 掌握标准

- 能画出 LSTM 的门控结构图
- 能解释 Cell State 如何解决长期依赖
- 能用 PyTorch 搭建 LSTM/GRU 模型
- 能解释 LSTM 和 GRU 的区别和适用场景
