# Tensor 操作技能地图

## 目标

学习者能创建、运算、变形各种 Tensor，能在不运行代码的情况下预测每一步的 shape 和 dtype。

## 必会概念

- Tensor 是什么（多维数组，TF 2.x 默认 Eager Execution 即时求值）
- dtype（float32、float64、int32、int64 等）
- shape（各维度的大小）
- rank（阶，即维度数）
- broadcasting（自动扩展规则）
- tf.constant（不可变）vs tf.Variable（可变）

## 必会 API（必须能不查文档写出调用）

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.constant(value, dtype=)` | 从 Python 数据创建 tensor | `tf.constant([1,2,3], dtype=tf.float32)` |
| `tf.Variable(initial_value)` | 创建可变 tensor | `tf.Variable([1.0, 2.0])` |
| `tf.zeros(shape, dtype=)` | 创建全零 tensor | `tf.zeros((3, 4))` |
| `tf.ones(shape)` | 创建全一 tensor | `tf.ones((2, 3))` |
| `tf.random.normal(shape, mean, stddev)` | 正态分布随机 tensor | `tf.random.normal((2, 3, 4))` |
| `tf.random.uniform(shape, minval, maxval)` | 均匀分布随机 tensor | `tf.random.uniform((3, 4))` |
| `tf.range(start, limit, delta)` | 等差序列 | `tf.range(0, 10, 2)` |
| `tf.linspace(start, stop, num)` | 等间距序列 | `tf.linspace(0.0, 1.0, 5)` |
| `tf.eye(num_rows)` | 单位矩阵 | `tf.eye(3)` |
| `tf.fill(dims, value)` | 填充指定值 | `tf.fill((2, 3), 5)` |
| `x.shape` | 获取 shape | `x.shape` |
| `x.dtype` | 获取数据类型 | `x.dtype` |
| `tf.cast(x, dtype)` | 类型转换 | `tf.cast(x, tf.float32)` |
| `x.numpy()` | 转 numpy 数组 | `x.numpy()` |
| `tf.reshape(x, shape)` | 改变形状 | `tf.reshape(x, (6, 4))` |
| `tf.expand_dims(x, axis)` | 增加维度 | `tf.expand_dims(x, 0)` |
| `tf.squeeze(x, axis)` | 去掉 size=1 的维度 | `tf.squeeze(x)` |
| `tf.transpose(x, perm)` | 转置 | `tf.transpose(x, perm=[2, 0, 1])` |

## 必会运算

| 运算 | API | 备注 |
|------|-----|------|
| 逐元素加 | `a + b` 或 `tf.add(a, b)` | 支持 broadcasting |
| 逐元素乘 | `a * b` 或 `tf.multiply(a, b)` | 不是矩阵乘法！|
| 矩阵乘法 | `a @ b` 或 `tf.matmul(a, b)` | 最后两个维度做矩阵乘 |
| 转置 | `tf.transpose(x)` | 需要指定 perm 参数 |
| 求和 | `tf.reduce_sum(x, axis=)` | 可指定 axis |
| 均值 | `tf.reduce_mean(x, axis=)` | 可指定 axis |
| 最大值 | `tf.reduce_max(x)` / `tf.argmax(x)` | argmax 返回索引 |
| 拼接 | `tf.concat([a, b], axis=)` | 沿指定维度拼接 |
| 堆叠 | `tf.stack([a, b], axis=)` | 创建新维度 |

## 代码片段

```python
import tensorflow as tf

# 创建
x = tf.constant([1, 2, 3])                # 从 list 创建
y = tf.zeros((2, 3))                      # 全零
z = tf.random.normal((3, 4))              # 随机
v = tf.Variable([1.0, 2.0])              # 可变 tensor

# 运算
result = x + 10                           # broadcasting
mat = tf.random.normal((3, 4)) @ tf.random.normal((4, 5))  # 矩阵乘 (3,5)

# 形状
x = tf.random.normal((2, 3, 4))
x_reshaped = tf.reshape(x, (6, 4))        # reshape
x_unsq = tf.expand_dims(x, 0)             # (1, 2, 3, 4)
x_sq = tf.squeeze(x_unsq, 0)             # (2, 3, 4)
x_perm = tf.transpose(x, perm=[2, 0, 1]) # (4, 2, 3)
```

## 常见错误

1. `tf.constant()` 创建的是不可变 tensor，修改需要用 `tf.Variable()`
2. `*` 是逐元素乘法，不是矩阵乘法
3. broadcasting 从右向左匹配
4. `tf.transpose()` 必须指定 `perm` 参数（不同于 PyTorch 的默认行为）
5. `tf.reshape()` 和 `tf.transpose()` 的区别搞混
6. `tf.expand_dims()` 的 `axis` 参数从 0 开始计数
7. dtype 不匹配时需要显式 `tf.cast()`

## 训练阶梯

1. **创建**：能用各种函数创建指定 shape 和 dtype 的 tensor
2. **运算**：能做基本运算并预测 dtype
3. **Shape 预测**：能预测 broadcasting 后的 shape
4. **变形**：能用 reshape/expand_dims/squeeze/transpose 改变形状
5. **综合**：能不运行代码，写出创建 → 运算 → 变形的完整链并预测最终 shape

## 掌握标准

- 能不查文档创建各种 tensor
- 能预测 broadcasting 后的 shape
- 能在纸上写出 reshape/transpose 后的 shape
- 能解释 `*` 和 `@` 的区别
- 能处理 dtype 不匹配的错误
