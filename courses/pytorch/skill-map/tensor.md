# Tensor 技能地图

## 目标

学习者能创建、运算、变形各种 tensor，能在不运行代码的情况下预测每一步的 shape 和 dtype。

## 必会概念

- Tensor 是什么（多维数组，支持 GPU 和自动求导）
- dtype（float32、float64、int64 等）
- device（cpu / cuda）
- shape（各维度的大小）
- broadcasting（自动扩展规则）

## 必会 API（必须能不查文档写出调用）

| 函数 | 用途 | 示例 |
|------|------|------|
| `torch.tensor(data, dtype=)` | 从 Python 数据创建 tensor | `torch.tensor([1,2,3], dtype=torch.float32)` |
| `torch.zeros(*size, dtype=, device=)` | 创建全零 tensor | `torch.zeros(3, 4)` |
| `torch.ones(*size)` | 创建全一 tensor | `torch.ones(2, 3)` |
| `torch.randn(*size)` | 标准正态分布随机 tensor | `torch.randn(2, 3, 4)` |
| `torch.arange(start, end, step)` | 等差序列 | `torch.arange(0, 10, 2)` |
| `torch.linspace(start, end, steps)` | 等间距序列 | `torch.linspace(0, 1, 5)` |
| `torch.eye(n)` | 单位矩阵 | `torch.eye(3)` |
| `torch.empty(*size)` | 未初始化 tensor | `torch.empty(3, 4)` |
| `x.shape` / `x.size()` | 获取 shape | `x.shape` |
| `x.dtype` | 获取数据类型 | `x.dtype` |
| `x.device` | 获取所在设备 | `x.device` |
| `x.to(dtype=)` | 类型转换 | `x.to(torch.float32)` |
| `x.item()` | 标量转 Python 数值 | `loss.item()` |
| `x.numpy()` | 转 numpy（仅 CPU） | `x.cpu().numpy()` |
| `x.clone()` | 深拷贝 | `x.clone()` |
| `x.detach()` | 从计算图分离 | `x.detach()` |

## 必会运算

| 运算 | API | 备注 |
|------|-----|------|
| 逐元素加 | `a + b` 或 `torch.add(a, b)` | 支持 broadcasting |
| 逐元素乘 | `a * b` | 不是矩阵乘法！|
| 矩阵乘法 | `a @ b` 或 `torch.matmul(a, b)` | 最后两个维度做矩阵乘 |
| 转置 | `x.T` 或 `x.transpose(0, 1)` | .T 只交换最后两个维度 |
| 求和 | `x.sum()` | 可指定 dim |
| 均值 | `x.mean()` | 可指定 dim |
| 最大值 | `x.max()` / `x.argmax()` | argmax 返回索引 |

## 代码片段

```python
import torch

# 创建
x = torch.tensor([1, 2, 3])              # 从 list 创建
y = torch.zeros(2, 3)                    # 全零
z = torch.randn(3, 4)                    # 随机

# 运算
result = x + 10                          # broadcasting
mat = torch.randn(3, 4) @ torch.randn(4, 5)  # 矩阵乘 (3,5)

# 形状
x = torch.randn(2, 3, 4)
x_reshaped = x.reshape(6, 4)             # reshape
x_unsq = x.unsqueeze(0)                  # (1, 2, 3, 4)
x_sq = x_unsq.squeeze(0)                 # (2, 3, 4)
x_perm = x.permute(2, 0, 1)             # (4, 2, 3)
```

## 常见错误

1. `torch.tensor()` 和 `torch.Tensor()` 的区别（前者是函数，后者是类）
2. `*` 是逐元素乘法，不是矩阵乘法
3. broadcasting 从右向左匹配
4. `.numpy()` 在 GPU tensor 上报错
5. `squeeze()` 只去 size=1 的维度

## 训练阶梯

1. **创建**：能用各种函数创建指定 shape 和 dtype 的 tensor
2. **运算**：能做基本运算并预测 dtype
3. **Shape 预测**：能预测 broadcasting 后的 shape
4. **变形**：能用 reshape/squeeze/unsqueeze/permute 改变形状
5. **综合**：能不运行代码，写出创建 → 运算 → 变形的完整链并预测最终 shape

## 掌握标准

- 能不查文档创建各种 tensor
- 能预测 broadcasting 后的 shape
- 能在纸上写出 reshape/permute 后的 shape
- 能解释 `*` 和 `@` 的区别
- 能处理 dtype 和 device 不匹配的错误
