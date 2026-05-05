# PyTorch 注意力机制

-

# PyTorch 注意力机制

注意力机制（Attention Mechanism）是深度学习中最重要的概念之一。

注意力机制让模型学会"关注"输入中最相关的部分，在自然语言处理、计算机视觉等领域取得了巨大成功。

本节详细介绍注意力机制的核心原理、PyTorch 实现以及各种注意力变体。

**适用版本：**本文代码基于 PyTorch 2.0+ 编写。`nn.MultiheadAttention` 的 `batch_first` 参数在 PyTorch 1.9 引入，早期版本需要手动处理维度。

## 1. 注意力机制基础

### 1.1 为什么需要注意力

传统的序列到序列（Seq2Seq）模型存在一个根本问题：Encoder 需要将所有信息压缩到一个固定长度的向量中。对于长序列，这个向量会成为信息瓶颈——句子越长，信息丢失越严重。

注意力机制的核心理念是：让 Decoder 在生成每个输出时，能够"看"到 Encoder 的所有隐藏状态，并根据当前上下文动态地分配不同的注意力权重。这就像人类翻译时，每翻译一个词都会回头去看原文的对应部分。

  Seq2Seq：固定向量 vs 注意力机制

  固定向量（信息瓶颈）

    x₁

    x₂

    x₃

    x₄

-

  c（固定向量）

-

    y₁

    y₂

    y₃

    y₄

  所有解码步共享同一个 c

-

  注意力机制（动态加权）

    h₁

    h₂

    h₃

    h₄

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

    y₁

    y₂

    y₃

    y₄

  每步生成不同的上下文向量 c_t

  线越粗 → 注意力权重越大 → 该位置信息越重要

### 1.2 注意力机制的本质

注意力机制可以看作是一种加权求和操作。给定查询（Query）、键（Key）和值（Value），通过计算 Query 与每个 Key 的相似度来分配权重，再对 Value 进行加权求和：

\[\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\]$$

其中：

- **Q（Query）**：查询向量，表示"我正在寻找什么信息"

- **K（Key）**：键向量，表示"我这里有什么信息"（用于匹配）

- **V（Value）**：值向量，表示"我实际能提供的内容"

- **$$d_k$$**：Key 的维度，$$\sqrt{d_k}$$ 用于缩放，防止点积值过大导致 softmax 梯度消失

为什么要除以 $$\sqrt{d_k}$$？当 $$d_k$$ 较大时，Q 和 K 的点积的方差会随维度线性增长，导致 softmax 的输入值过大，梯度趋近于零。缩放后使方差恢复到 1，保证梯度正常流动。

  Scaled Dot-Product Attention 计算流程

  Q
  [batch, seq_q, d_k]

  K
  [batch, seq_k, d_k]

-

-

  MatMul
  QKᵀ

-

  Scale
  ÷ √d_k

-

  Softmax
  归一化

-

  V
  [batch, seq_k, d_v]

-

  MatMul
  × V

-

  Output

    Mask（可选）
    -∞ 填充

-

    Output = softmax(QKᵀ / √d_k) · V

    输出形状: [batch, seq_q, d_v] — 每个 Query 位置得到一个 d_v 维的上下文向量

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

def scaled_dot_product_attention(Q, K, V, mask=None):

    """

    缩放点积注意力

    参数:

        Q: 查询张量 [batch, n_heads, seq_len_q, d_k]

        K: 键张量 [batch, n_heads, seq_len_k, d_k]

        V: 值张量 [batch, n_heads, seq_len_v, d_v]

        mask: 掩码张量，被掩码位置设为 False/0

    返回:

        output: 注意力输出 [batch, n_heads, seq_len_q, d_v]

        attention_weights: 注意力权重 [batch, n_heads, seq_len_q, seq_len_k]

    """

    d_k = Q.size(-1)

    # 1. 计算 QK^T / sqrt(d_k)

    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)

    # 2. 应用掩码（可选）

    #    掩码位置设为极小值，softmax 后趋近于 0

    if mask is not None:

        scores = scores.masked_fill(mask == 0, -1e9)

    # 3. Softmax 归一化 → 注意力权重

    attention_weights = F.softmax(scores, dim=-1)

    # 4. 加权求和

    output = torch.matmul(attention_weights, V)

    return output, attention_weights

# 测试

batch_size, n_heads = 2, 4

seq_len_q, seq_len_k = 5, 6

d_k, d_v = 8, 16

Q = torch.randn(batch_size, n_heads, seq_len_q, d_k)

K = torch.randn(batch_size, n_heads, seq_len_k, d_k)

V = torch.randn(batch_size, n_heads, seq_len_k, d_v)

output, attn_weights = scaled_dot_product_attention(Q, K, V)

print(f"输出形状: {output.shape}")            # [2, 4, 5, 16]

print(f"注意力权重形状: {attn_weights.shape}")  # [2, 4, 5, 6]

print(f"权重行求和（应为 1.0）: {attn_weights[0, 0, 0].sum().item():.4f}")
```

注意力权重的本质是概率分布——经过 softmax 后，每一行的和为 1。权重越大表示模型对该位置越"关注"。

## 2. PyTorch 注意力模块

### 2.1 Multi-Head Attention

Multi-Head Attention（多头注意力） 允许模型同时关注来自不同位置的不同表示子空间的信息。它将 Q、K、V 分别通过不同的线性投影映射到多个子空间，在每个子空间独立计算注意力，最后拼接结果再做一次线性变换。

这就像让多个人从不同角度同时审视同一段文本——有人关注语法结构，有人关注语义关联，有人关注长距离依赖。多头机制让模型能捕获更丰富的模式。

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$

$$\text{where head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0, "d_model 必须能被 n_heads 整除"

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads  # 每个头的维度

        # Q、K、V 的线性投影（一次计算所有头，更高效）

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        # 输出投影

        self.w_o = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):

        """

        参数:

            query: [batch, seq_len_q, d_model]

            key:   [batch, seq_len_k, d_model]

            value: [batch, seq_len_k, d_model]

            mask:  [batch, 1, 1, seq_len_k] 或 [batch, 1, seq_len_q, seq_len_k]

        """

        batch_size = query.size(0)

        # 1. 线性投影，然后分头

        #    [batch, seq_len, d_model] → [batch, seq_len, n_heads, d_k]

        #    → [batch, n_heads, seq_len, d_k]

        Q = self.w_q(query).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        K = self.w_k(key).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        V = self.w_v(value).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        # 2. 缩放点积注意力

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:

            scores = scores.masked_fill(mask == 0, -1e9)

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 3. 加权求和

        context = torch.matmul(attn_weights, V)

        # 4. 合并多头：[batch, n_heads, seq_len, d_k] → [batch, seq_len, d_model]

        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # 5. 输出投影

        output = self.w_o(context)

        return output, attn_weights

# 测试

d_model, n_heads = 128, 8

seq_len, batch = 10, 4

layer = MultiHeadAttention(d_model, n_heads)

query = torch.randn(batch, seq_len, d_model)

key = torch.randn(batch, seq_len, d_model)

value = torch.randn(batch, seq_len, d_model)

output, attn_weights = layer(query, key, value)

print(f"输出形状: {output.shape}")           # [4, 10, 128]

print(f"注意力权重形状: {attn_weights.shape}") # [4, 8, 10, 10]

print(f"每头维度 d_k = {d_model // n_heads}")
```

### 2.2 PyTorch 内置 MultiheadAttention

PyTorch 提供了经过高度优化的 `nn.MultiheadAttention`，底层使用了融合算子（fused kernels），在大多数场景下比手动实现更快。推荐在生产环境中使用。

## 实例

```python
import torch

import torch.nn as nn

class TransformerAttention(nn.Module):

    """使用 PyTorch 内置 MultiheadAttention 的自注意力层"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        self.attention = nn.MultiheadAttention(

            embed_dim=d_model,

            num_heads=n_heads,

            dropout=dropout,

            batch_first=True,  # 输入格式为 [batch, seq, features]

            # PyTorch 2.0+ 可启用 Flash Attention 后端：

            # attn_implementation="flash_attention_2"  # 需要安装 flash-attn

        )

        self.layernorm = nn.LayerNorm(d_model)

    def forward(self, x, key_padding_mask=None):

        """

        自注意力：Q、K、V 都是 x

        参数:

            x: [batch, seq_len, d_model]

            key_padding_mask: [batch, seq_len]，True 表示该位置是 padding

        """

        attn_output, attn_weights = self.attention(

            x, x, x,  # self-attention

            key_padding_mask=key_padding_mask

        )

        # Pre-Norm 残差连接（比 Post-Norm 训练更稳定）

        output = self.layernorm(x + attn_output)

        return output, attn_weights

# 测试

d_model, n_heads = 128, 8

seq_len, batch = 10, 4

model = TransformerAttention(d_model, n_heads)

x = torch.randn(batch, seq_len, d_model)

# 创建 padding mask：True 表示该位置应被忽略

key_padding_mask = torch.zeros(batch, seq_len, dtype=torch.bool)

key_padding_mask[0, 7:] = True   # 第一个样本的后 3 个位置是 padding

key_padding_mask[1, 5:] = True   # 第二个样本的后 5 个位置是 padding

output, attn_weights = model(x, key_padding_mask=key_padding_mask)

print(f"输出形状: {output.shape}")           # [4, 10, 128]

print(f"注意力权重形状: {attn_weights.shape}") # [4, 10, 10]
```

**注意 mask 类型：**`nn.MultiheadAttention` 的 `key_padding_mask` 使用 **True = 忽略** 的约定，与某些自定义实现中 0 = 忽略的约定相反。使用时务必确认。

## 3. 注意力机制的变体

### 3.1 自注意力（Self-Attention）

自注意力 是注意力机制的一种特殊形式——Q、K、V 都来自同一个输入序列。它让序列中的每个位置都能直接关注到所有其他位置，从而捕获全局依赖关系。这是 Transformer 的核心组件，也是它优于 RNN 的关键所在：RNN 需要逐步传递信息，而自注意力一步到位。

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class SelfAttention(nn.Module):

    """多头自注意力层，支持因果掩码（用于自回归生成）"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        self.out_proj = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def _split_heads(self, x, batch_size):

        """[batch, seq, d_model] → [batch, n_heads, seq, d_k]"""

        return x.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

    def forward(self, x, causal=False):

        """

        自注意力：Q、K、V 都来自同一个输入 x

        参数:

            x: [batch, seq_len, d_model]

            causal: 是否使用因果掩码（防止看到未来位置）

        """

        batch_size, seq_len, _ = x.size()

        # 投影 + 分头

        Q = self._split_heads(self.w_q(x), batch_size)

        K = self._split_heads(self.w_k(x), batch_size)

        V = self._split_heads(self.w_v(x), batch_size)

        # 计算注意力分数

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        # 因果掩码：上三角矩阵设为 -inf，防止看到未来 token

        if causal:

            causal_mask = torch.triu(

                torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),

                diagonal=1

            )

            scores = scores.masked_fill(causal_mask.unsqueeze(0).unsqueeze(0), float('-inf'))

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 加权求和 + 合并多头

        context = torch.matmul(attn_weights, V)

        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

        return self.out_proj(context), attn_weights

# 测试

d_model, n_heads = 256, 8

seq_len, batch = 20, 2

attn = SelfAttention(d_model, n_heads)

x = torch.randn(batch, seq_len, d_model)

# 不使用因果掩码（Encoder 场景）

output_enc, weights_enc = attn(x, causal=False)

print(f"[Encoder] 输出: {output_enc.shape}, 权重: {weights_enc.shape}")

# 使用因果掩码（Decoder / 自回归生成场景）

output_dec, weights_dec = attn(x, causal=True)

print(f"[Decoder] 输出: {output_dec.shape}, 权重: {weights_dec.shape}")

# 验证因果性：第一个 token 不应该关注后面的 token

print(f"causal=True 时，weights[0,0,0,5:]（应全为0）: {weights_dec[0, 0, 0, 5:].tolist()[:5]}")
```

### 3.2 交叉注意力（Cross-Attention）

交叉注意力 中，Q 来自一个序列（如 Decoder），K 和 V 来自另一个序列（如 Encoder）。这是 Encoder-Decoder 架构的桥梁——让 Decoder 在生成每个 token 时，能动态地"查阅"Encoder 的所有输出。

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class CrossAttention(nn.Module):

    """交叉注意力：Q 来自目标序列，K/V 来自源序列"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        self.out_proj = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, target, source, mask=None):

        """

        参数:

            target: 目标序列 [batch, target_len, d_model]  → 提供 Q

            source: 源序列   [batch, source_len, d_model]  → 提供 K, V

            mask:   可选掩码

        """

        batch_size = target.size(0)

        target_len = target.size(1)

        source_len = source.size(1)

        # 投影 + 分头

        Q = self.w_q(target).view(batch_size, target_len, self.n_heads, self.d_k).transpose(1, 2)

        K = self.w_k(source).view(batch_size, source_len, self.n_heads, self.d_k).transpose(1, 2)

        V = self.w_v(source).view(batch_size, source_len, self.n_heads, self.d_k).transpose(1, 2)

        # 注意力计算

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:

            scores = scores.masked_fill(mask == 0, float('-inf'))

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 加权求和 + 合并多头

        context = torch.matmul(attn_weights, V)

        context = context.transpose(1, 2).contiguous().view(batch_size, target_len, self.d_model)

        return self.out_proj(context), attn_weights

# 测试

d_model, n_heads = 256, 8

batch = 2

target_len, source_len = 10, 15

cross_attn = CrossAttention(d_model, n_heads)

target = torch.randn(batch, target_len, d_model)  # Decoder 输出

source = torch.randn(batch, source_len, d_model)  # Encoder 输出

output, weights = cross_attn(target, source)

print(f"目标序列形状: {target.shape}")

print(f"源序列形状:   {source.shape}")

print(f"输出形状:     {output.shape}")            # [2, 10, 256]

print(f"权重形状:     {weights.shape}")            # [2, 8, 10, 15]

# 权重含义：每个 target 位置对每个 source 位置的关注程度
```

**自注意力 vs 交叉注意力：**自注意力中 Q/K/V 形状相同（$$seq \times seq$$ 的权重矩阵）；交叉注意力中 Q 长度与 K 长度可以不同（$$target \times source$$ 的权重矩阵）。

### 3.3 位置编码（Positional Encoding）

注意力机制本身具有**置换不变性**——打乱输入顺序不会改变输出。但语言和图像都是有序的，因此需要通过位置编码显式注入位置信息。原始 Transformer 使用正弦/余弦函数生成固定的位置编码：

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right), \quad PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

## 实例

```python
import torch

import torch.nn as nn

import math

class PositionalEncoding(nn.Module):

    """正弦/余弦位置编码（Transformer 原始方案）"""

    def __init__(self, d_model, max_len=5000, dropout=0.1):

        super().__init__()

        self.dropout = nn.Dropout(p=dropout)

        # 预计算位置编码矩阵 [max_len, d_model]

        pe = torch.zeros(max_len, d_model)

        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # div_term: 控制不同频率维度的衰减速度

        div_term = torch.exp(

            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)

        )

        pe[:, 0::2] = torch.sin(position * div_term)  # 偶数维度

        pe[:, 1::2] = torch.cos(position * div_term)  # 奇数维度

        pe = pe.unsqueeze(0)  # [1, max_len, d_model]

        self.register_buffer('pe', pe)  # 不参与训练

    def forward(self, x):

        """

        x: [batch, seq_len, d_model]

        返回: x + positional_encoding

        """

        x = x + self.pe[:, :x.size(1), :]

        return self.dropout(x)

# 测试

d_model = 128

seq_len = 50

batch = 4

pe = PositionalEncoding(d_model)

x = torch.randn(batch, seq_len, d_model)

output = pe(x)

print(f"输入形状: {x.shape}")

print(f"输出形状: {output.shape}")

print(f"位置编码形状: {pe.pe.shape}")  # [1, 5000, 128]
```

## 4. 注意力机制的视觉应用

注意力机制不仅适用于序列数据，在计算机视觉中同样大放异彩。以下介绍三种经典的视觉注意力模块：

### 4.1 通道注意力（Channel Attention）

通道注意力（如 SENet）让网络学习"哪些通道更重要"。它对每个通道进行全局池化压缩空间信息，再通过两层全连接网络学习通道间的依赖关系。

## 实例

```python
import torch

import torch.nn as nn

class SEBlock(nn.Module):

    """Squeeze-and-Excitation Block（通道注意力）"""

    def __init__(self, channels, reduction=16):

        super().__init__()

        self.squeeze = nn.AdaptiveAvgPool2d(1)  # 全局平均池化

        self.excitation = nn.Sequential(

            nn.Linear(channels, channels // reduction, bias=False),

            nn.ReLU(inplace=True),

            nn.Linear(channels // reduction, channels, bias=False),

            nn.Sigmoid()  # 输出 0~1 的通道权重

        )

    def forward(self, x):

        # x: [batch, channels, H, W]

        b, c, _, _ = x.size()

        # Squeeze: [B, C, H, W] → [B, C, 1, 1] → [B, C]

        y = self.squeeze(x).view(b, c)

        # Excitation: 学习通道权重 [B, C]

        y = self.excitation(y).view(b, c, 1, 1)

        # 通道加权：每个通道乘以对应的权重

        return x * y.expand_as(x)

# 测试

se = SEBlock(channels=256, reduction=16)

x = torch.randn(4, 256, 32, 32)

output = se(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 4.2 空间注意力（Spatial Attention）

空间注意力 让网络学习"哪些位置更重要"。它在通道维度上进行压缩（取均值和最大值），然后用卷积学习空间权重图。

## 实例

```python
import torch

import torch.nn as nn

class SpatialAttention(nn.Module):

    """空间注意力模块"""

    def __init__(self, kernel_size=7):

        super().__init__()

        padding = kernel_size // 2

        # 输入 2 个通道（均值 + 最大值），输出 1 个通道（注意力图）

        self.conv = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):

        # x: [batch, channels, H, W]

        # 通道压缩：取均值和最大值 → [B, 1, H, W] 各一个

        avg_out = torch.mean(x, dim=1, keepdim=True)

        max_out, _ = torch.max(x, dim=1, keepdim=True)

        # 拼接 → [B, 2, H, W]

        scale = torch.cat([avg_out, max_out], dim=1)

        # 卷积 + Sigmoid → 空间权重图 [B, 1, H, W]

        scale = self.sigmoid(self.conv(scale))

        # 空间加权

        return x * scale

# 测试

spatial_attn = SpatialAttention(kernel_size=7)

x = torch.randn(4, 256, 32, 32)

output = spatial_attn(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 4.3 CBAM（Convolutional Block Attention Module）

CBAM 将通道注意力和空间注意力**串联**应用：先通过通道注意力选择重要通道，再通过空间注意力选择重要位置。两者互补，效果优于单独使用。

## 实例

```python
import torch

import torch.nn as nn

class CBAM(nn.Module):

    """CBAM: 通道注意力 + 空间注意力"""

    def __init__(self, channels, reduction=16, kernel_size=7):

        super().__init__()

        # 通道注意力

        self.channel_attn = nn.Sequential(

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten(),

            nn.Linear(channels, channels // reduction, bias=False),

            nn.ReLU(inplace=True),

            nn.Linear(channels // reduction, channels, bias=False),

            nn.Sigmoid()

        )

        # 空间注意力

        self.spatial_attn = nn.Sequential(

            nn.Conv2d(2, 1, kernel_size, padding=kernel_size // 2, bias=False),

            nn.Sigmoid()

        )

    def forward(self, x):

        # 1. 通道注意力

        b, c, _, _ = x.size()

        ca = self.channel_attn(x).view(b, c, 1, 1)

        x = x * ca

        # 2. 空间注意力

        avg_out = torch.mean(x, dim=1, keepdim=True)

        max_out, _ = torch.max(x, dim=1, keepdim=True)

        sa = self.spatial_attn(torch.cat([avg_out, max_out], dim=1))

        x = x * sa

        return x

# 测试

cbam = CBAM(channels=256)

x = torch.randn(4, 256, 32, 32)

output = cbam(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

## 5. 注意力机制在 NLP 中的应用

### 5.1 Transformer Encoder

Transformer Encoder 由 N 个相同的层堆叠而成，每层包含两个子层：**多头自注意力**和**前馈网络**。每个子层都使用残差连接和层归一化。

## 实例

```python
import torch

import torch.nn as nn

import math

class TransformerEncoderLayer(nn.Module):

    """单层 Transformer Encoder"""

    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):

        super().__init__()

        # 多头自注意力

        self.self_attn = nn.MultiheadAttention(

            d_model, n_heads, dropout=dropout, batch_first=True

        )

        # 前馈网络（两层线性 + 激活）

        self.ffn = nn.Sequential(

            nn.Linear(d_model, d_ff),

            nn.GELU(),  # GELU 比 ReLU 更常用

            nn.Dropout(dropout),

            nn.Linear(d_ff, d_model)

        )

        # 层归一化（Pre-Norm 风格，训练更稳定）

        self.norm1 = nn.LayerNorm(d_model)

        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, key_padding_mask=None):

        # 子层 1: 自注意力

        residual = x

        x = self.norm1(x)  # Pre-Norm

        attn_out, _ = self.self_attn(x, x, x, key_padding_mask=key_padding_mask)

        x = residual + self.dropout(attn_out)

        # 子层 2: 前馈网络

        residual = x

        x = self.norm2(x)  # Pre-Norm

        x = residual + self.dropout(self.ffn(x))

        return x

class TransformerEncoder(nn.Module):

    """多层 Transformer Encoder"""

    def __init__(self, d_model, n_heads, d_ff, num_layers, dropout=0.1):

        super().__init__()

        self.layers = nn.ModuleList([

            TransformerEncoderLayer(d_model, n_heads, d_ff, dropout)

            for _ in range(num_layers)

        ])

        self.final_norm = nn.LayerNorm(d_model)

    def forward(self, x, key_padding_mask=None):

        for layer in self.layers:

            x = layer(x, key_padding_mask)

        return self.final_norm(x)

# 测试

d_model, n_heads, d_ff = 128, 4, 512

num_layers, seq_len, batch = 3, 20, 4

encoder = TransformerEncoder(d_model, n_heads, d_ff, num_layers)

x = torch.randn(batch, seq_len, d_model)

# Padding mask: True = 忽略该位置

key_padding_mask = torch.zeros(batch, seq_len, dtype=torch.bool)

key_padding_mask[0, 15:] = True

output = encoder(x, key_padding_mask=key_padding_mask)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 5.2 注意力可视化

可视化注意力权重是理解和调试 Transformer 模型的重要手段。通过热力图可以直观地看到模型在每个位置关注了哪些信息。

## 实例

```python
import torch

import matplotlib.pyplot as plt

import numpy as np

def visualize_attention(attention_weights, tokens=None, save_path=None):

    """

    可视化多头注意力权重

    参数:

        attention_weights: [n_heads, seq_len, seq_len]

        tokens: token 列表（可选）

        save_path: 保存路径（可选）

    """

    n_heads = attention_weights.shape[0]

    seq_len = attention_weights.shape[1]

    fig, axes = plt.subplots(1, n_heads, figsize=(n_heads * 3, 3.5))

    if n_heads == 1:

        axes = [axes]

    for head in range(n_heads):

        ax = axes[head]

        attn = attention_weights[head].detach().cpu().numpy()

        im = ax.imshow(attn, cmap='Blues', aspect='auto', vmin=0, vmax=attn.max())

        ax.set_title(f'Head {head + 1}', fontsize=10, fontweight='bold')

        ax.set_xlabel('Key')

        ax.set_ylabel('Query')

        if tokens is not None:

            ax.set_xticks(range(len(tokens)))

            ax.set_yticks(range(len(tokens)))

            ax.set_xticklabels(tokens, rotation=90, fontsize=8)

            ax.set_yticklabels(tokens, fontsize=8)

    plt.tight_layout()

    if save_path:

        plt.savefig(save_path, dpi=150, bbox_inches='tight')

    plt.show()

# 模拟训练后的注意力权重

n_heads, seq_len = 4, 8

attention_weights = torch.softmax(torch.randn(n_heads, seq_len, seq_len), dim=-1)

tokens = ['The', 'cat', 'sat', 'on', 'the', 'mat', '.', '[PAD]']

visualize_attention(attention_weights, tokens)
```

## 6. 完整的注意力分类器

### 6.1 基于注意力的文本分类

以下是一个完整的文本分类模型：使用 Transformer Encoder 提取特征，再通过注意力池化（Attention Pooling）将变长序列压缩为固定长度的向量，最后送入分类器。

## 实例

```python
import torch

import torch.nn as nn

import math

class AttentionClassifier(nn.Module):

    """基于 Transformer + 注意力池化的文本分类模型"""

    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes,

                 n_heads=4, num_layers=2, dropout=0.1):

        super().__init__()

        self.embed_dim = embed_dim

        # 词嵌入

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.pos_encoding = PositionalEncoding(embed_dim, dropout=dropout)

        # Transformer 编码器

        encoder_layer = nn.TransformerEncoderLayer(

            d_model=embed_dim,

            nhead=n_heads,

            dim_feedforward=hidden_dim,

            dropout=dropout,

            batch_first=True,

            activation='gelu'

        )

        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)

        # 注意力池化：学习每个位置的重要性权重

        self.attn_pool = nn.Sequential(

            nn.Linear(embed_dim, 1)  # 每个位置输出一个标量权重

        )

        # 分类头

        self.classifier = nn.Sequential(

            nn.Linear(embed_dim, hidden_dim),

            nn.GELU(),

            nn.Dropout(dropout),

            nn.Linear(hidden_dim, num_classes)

        )

    def forward(self, x):

        """

        x: [batch, seq_len] — token ids

        返回: logits [batch, num_classes], attn_weights [batch, seq_len]

        """

        # 词嵌入 + 位置编码

        mask = (x == 0)  # padding mask

        x = self.embedding(x) * math.sqrt(self.embed_dim)

        x = self.pos_encoding(x)

        # Transformer 编码

        x = self.transformer(x, src_key_padding_mask=mask)

        # 注意力池化：为每个位置计算权重，加权求和

        scores = self.attn_pool(x).squeeze(-1)          # [batch, seq_len]

        scores = scores.masked_fill(mask, float('-inf'))  # 忽略 padding

        attn_weights = torch.softmax(scores, dim=1)       # [batch, seq_len]

        pooled = torch.bmm(attn_weights.unsqueeze(1), x).squeeze(1)  # [batch, embed_dim]

        # 分类

        logits = self.classifier(pooled)

        return logits, attn_weights

# 测试

model = AttentionClassifier(

    vocab_size=10000, embed_dim=128, hidden_dim=256, num_classes=5

)

# 模拟输入（含 padding）

x = torch.randint(1, 10000, (16, 50))

x[:, -10:] = 0  # 最后 10 个位置是 padding

logits, attn_weights = model(x)

print(f"输入: {x.shape}")

print(f"Logits: {logits.shape}")          # [16, 5]

print(f"注意力权重: {attn_weights.shape}") # [16, 50]
```

### 6.2 常见注意力变体对比

| 类型 | Q 来源 | K/V 来源 | 核心用途 | 典型应用 |
| --- | --- | --- | --- | --- |
| 自注意力（Self-Attention） | 自身 | 自身 | 序列内部全局交互 | Transformer、BERT、ViT |
| 交叉注意力（Cross-Attention） | 目标序列 | 源序列 | 跨序列信息融合 | 机器翻译、图像描述、Stable Diffusion |
| 通道注意力（Channel Attention） | 全局池化特征 | 同上 | 学习通道重要性 | SENet、CBAM |
| 空间注意力（Spatial Attention） | 通道压缩特征 | 同上 | 学习空间位置重要性 | CBAM、Spatial Transformer |
| 稀疏注意力（Sparse Attention） | 部分位置 | 部分位置 | 降低长序列计算复杂度 | Longformer、BigBird |

## 7. 最佳实践与常见问题

### 7.1 使用技巧

- **掩码一致性**：确保 padding mask 和 causal mask 的方向一致（True = 忽略 vs 1 = 保留）。不同 API 约定可能不同。

- **头数选择**：通常设为 $$d_{model}$$ 的因数，常用 8 或 16。头太多会降低每头的维度 $$d_k$$，可能损害性能。

- **残差连接**：注意力层前后务必使用残差连接 + 层归一化，这是训练深层 Transformer 的必要条件。

- **学习率预热**：Transformer 训练初期梯度波动较大，使用 warmup + cosine decay 调度器可显著提升稳定性。

- **Flash Attention**：PyTorch 2.0+ 支持通过 `nn.functional.scaled_dot_product_attention` 自动调用 Flash Attention，显存和速度均有大幅优化。

### 7.2 常见问题

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 注意力权重全为均匀分布 | 输入未归一化或学习率过大 | 检查输入尺度，使用 LayerNorm，降低学习率 |
| 训练 loss 不下降 | 位置编码缺失或 mask 错误 | 确认位置编码已添加，检查 mask 方向 |
| 显存溢出（长序列） | 注意力矩阵 $$O(n^2)$$ 复杂度 | 使用 Flash Attention、梯度检查点或稀疏注意力 |
| 推理时注意力退化 | 训练/推理时 mask 不一致 | 确保 padding mask 在训练和推理时使用相同逻辑 |

注意力机制是现代深度学习的核心技术。从 NLP 到 CV，从语音到蛋白质结构预测，几乎所有前沿模型都以注意力为基础。理解其原理和实现，是掌握 Transformer、ViT、Stable Diffusion、GPT 等模型的关键第一步。
