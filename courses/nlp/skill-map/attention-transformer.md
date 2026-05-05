# 注意力机制与 Transformer 技能地图

## 目标

学习者能理解注意力机制的原理，掌握 Self-Attention 和 Transformer 架构的完整结构。

## 必会概念

- 注意力机制（Attention）：让模型关注输入中最相关的部分
- Query（查询）、Key（键）、Value（值）
- Scaled Dot-Product Attention
- Multi-Head Attention（多头注意力）
- 位置编码（Positional Encoding）
- Encoder-Decoder 架构
- Layer Normalization
- 残差连接（Residual Connection）

## Scaled Dot-Product Attention 公式

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) × V

其中：
  Q: Query 矩阵 (n × d_k)
  K: Key 矩阵 (m × d_k)
  V: Value 矩阵 (m × d_v)
  d_k: Key 的维度
  sqrt(d_k): 缩放因子，防止点积过大导致 softmax 饱和
```

### 直觉理解

- QK^T 计算每对 Query-Key 的相似度（点积越大越相关）
- / sqrt(d_k) 缩放，防止 d_k 很大时点积值过大
- softmax 归一化为注意力权重（和为 1）
- 加权求和 V，得到注意力输出

### 为什么要除以 sqrt(d_k)？

```
当 d_k 很大时：
  - 点积值的方差 ≈ d_k（假设 Q、K 元素独立同分布）
  - softmax 对大的输入值会变得"尖锐"（梯度趋近于 0）
  - 除以 sqrt(d_k) 使方差归一化到 1
```

## Multi-Head Attention

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) × W_O

其中 head_i = Attention(Q × W_i^Q, K × W_i^K, V × W_i^V)

作用：
  - 不同 head 关注不同方面的信息
  - head_1 可能关注语法关系
  - head_2 可能关注语义关系
  - head_3 可能关注位置关系
```

## Transformer 完整架构

```
                    ┌─────────────────────────────┐
                    │         Output               │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │      Linear + Softmax        │
                    └──────────┬──────────────────┘
                               │
              ┌────────────────▼───────────────────────┐
              │            Decoder                      │
              │  ┌──────────────────────────────────┐  │
              │  │  Output Embedding + Pos Encoding  │  │
              │  └──────────────┬───────────────────┘  │
              │                 │                       │
              │  ┌──────────────▼───────────────────┐  │
              │  │  Masked Multi-Head Attention      │  │ × N 层
              │  │  + Add & LayerNorm                │  │
              │  └──────────────┬───────────────────┘  │
              │                 │                       │
              │  ┌──────────────▼───────────────────┐  │
              │  │  Cross-Attention (Q from Decoder  │  │
              │  │  K,V from Encoder)                │  │ × N 层
              │  │  + Add & LayerNorm                │  │
              │  └──────────────┬───────────────────┘  │
              │                 │                       │
              │  ┌──────────────▼───────────────────┐  │
              │  │  Feed Forward (Linear+ReLU+Linear)│  │ × N 层
              │  │  + Add & LayerNorm                │  │
              │  └──────────────────────────────────┘  │
              └────────────────┬───────────────────────┘
                               │ ← Cross-Attention 连接
              ┌────────────────▼───────────────────────┐
              │            Encoder                      │
              │  ┌──────────────────────────────────┐  │
              │  │  Input Embedding + Pos Encoding   │  │
              │  └──────────────┬───────────────────┘  │
              │                 │                       │
              │  ┌──────────────▼───────────────────┐  │
              │  │  Multi-Head Self-Attention        │  │ × N 层
              │  │  + Add & LayerNorm                │  │
              │  └──────────────┬───────────────────┘  │
              │                 │                       │
              │  ┌──────────────▼───────────────────┐  │
              │  │  Feed Forward (Linear+ReLU+Linear)│  │ × N 层
              │  │  + Add & LayerNorm                │  │
              │  └──────────────────────────────────┘  │
              └────────────────┬───────────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │         Input                │
                    └─────────────────────────────┘
```

## 位置编码公式

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

其中：pos 是位置, i 是维度索引, d_model 是模型维度
```

- 为什么需要？Self-Attention 是位置无关的，需要额外注入位置信息
- 为什么用 sin/cos？可以让模型学习相对位置关系

## 代码示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q, K, V, mask=None):
    """Scaled Dot-Product Attention"""
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)

    attn_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attn_weights, V)
    return output, attn_weights

# 示例：batch=1, heads=1, seq_len=4, d_k=8
Q = torch.randn(1, 1, 4, 8)
K = torch.randn(1, 1, 4, 8)
V = torch.randn(1, 1, 4, 8)

output, weights = scaled_dot_product_attention(Q, K, V)
print("注意力输出 shape:", output.shape)     # (1, 1, 4, 8)
print("注意力权重 shape:", weights.shape)    # (1, 1, 4, 4)
```

```python
# 使用 PyTorch 内置的 MultiheadAttention
mha = nn.MultiheadAttention(embed_dim=512, num_heads=8, batch_first=True)

# batch=2, seq_len=10, embed_dim=512
x = torch.randn(2, 10, 512)
output, attn_weights = mha(x, x, x)  # Self-Attention: Q=K=V=x
print("输出 shape:", output.shape)       # (2, 10, 512)
print("注意力权重 shape:", attn_weights.shape)  # (2, 10, 10)
```

## 常见错误

1. **不理解 Q/K/V 的来源**：在 Self-Attention 中 Q=K=V=输入；在 Cross-Attention 中 Q 来自 Decoder，K/V 来自 Encoder
2. **忘记缩放因子**：不除以 sqrt(d_k) 会导致 softmax 梯度消失
3. **Mask 的作用不理解**：Decoder 的 Masked Attention 防止看到未来信息
4. **位置编码不理解**：Transformer 没有循环结构，需要位置编码注入位置信息
5. **LayerNorm vs BatchNorm**：Transformer 用 LayerNorm，不是 BatchNorm

## 训练阶梯

1. **注意力直觉**：理解"关注最相关的部分"的直觉
2. **公式推导**：能写出 Scaled Dot-Product Attention 的公式
3. **NumPy 实现**：能用 NumPy 手写 Attention
4. **Transformer 架构**：能画出完整架构图并解释每个组件
5. **PyTorch 实现**：能用 PyTorch 搭建 Transformer 模型

## 掌握标准

- 能写出 Scaled Dot-Product Attention 公式并解释每一步
- 能解释为什么要除以 sqrt(d_k)
- 能画出 Transformer 的 Encoder-Decoder 架构图
- 能解释 Self-Attention、Cross-Attention、Masked Attention 的区别
- 能用 PyTorch 的 nn.MultiheadAttention 做实验
