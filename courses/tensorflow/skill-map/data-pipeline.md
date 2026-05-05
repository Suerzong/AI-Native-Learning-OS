# 数据管道技能地图

## 目标

学习者能用 tf.data.Dataset 构建高效的数据处理管道，理解各操作的顺序和性能影响。

## 必会概念

- tf.data.Dataset 是 TensorFlow 的数据输入标准方式
- Eager 模式下 Dataset 是惰性求值的迭代器
- Pipeline 设计原则：加载 → 转换 → 批处理 → 预取
- prefetch 和 cache 的性能优化作用
- 数据增强只应用于训练集

## 必会 API

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.data.Dataset.from_tensor_slices()` | 从数组/张量创建 | `tf.data.Dataset.from_tensor_slices((x, y))` |
| `tf.data.Dataset.from_tensor_slices(dict)` | 从字典创建 | `tf.data.Dataset.from_tensor_slices({'a': x, 'b': y})` |
| `tf.data.Dataset.list_files()` | 从文件路径创建 | `tf.data.Dataset.list_files('data/*.jpg')` |
| `tf.data.TFRecordDataset()` | 从 TFRecord 创建 | `tf.data.TFRecordDataset('data.tfrecord')` |
| `.map(fn, num_parallel_calls)` | 对每个元素应用函数 | `.map(preprocess, num_parallel_calls=tf.data.AUTOTUNE)` |
| `.batch(batch_size)` | 分批 | `.batch(32)` |
| `.shuffle(buffer_size)` | 打乱 | `.shuffle(1000)` |
| `.prefetch(buffer_size)` | 预取 | `.prefetch(tf.data.AUTOTUNE)` |
| `.cache()` | 缓存 | `.cache()` |
| `.repeat(count)` | 重复 | `.repeat()` |
| `.take(count)` | 取前 n 个 | `.take(100)` |
| `.skip(count)` | 跳过前 n 个 | `.skip(100)` |
| `.flat_map()` | 嵌套数据集展平 | `.flat_map(lambda x: x.batch(5))` |
| `.interleave()` | 并行读取多文件 | `.interleave(map_func, cycle_length=4)` |

## 标准 Pipeline 结构

```python
import tensorflow as tf

# 训练 pipeline（含数据增强）
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_ds = (train_ds
    .shuffle(buffer_size=10000)     # 1. 打乱
    .map(preprocess_fn, num_parallel_calls=tf.data.AUTOTUNE)  # 2. 预处理
    .map(augment_fn, num_parallel_calls=tf.data.AUTOTUNE)     # 3. 数据增强
    .batch(32)                       # 4. 分批
    .prefetch(tf.data.AUTOTUNE)     # 5. 预取
)

# 验证 pipeline（不含数据增强）
val_ds = tf.data.Dataset.from_tensor_slices((x_val, y_val))
val_ds = (val_ds
    .map(preprocess_fn, num_parallel_calls=tf.data.AUTOTUNE)
    .batch(32)
    .prefetch(tf.data.AUTOTUNE)
)
```

## 各操作的正确顺序

```
1. shuffle     ← 在 batch 之前，打乱原始数据顺序
2. map         ← 对每个样本做预处理/增强
3. batch       ← 将样本分批
4. prefetch    ← 在最后，预取下一个 batch
5. cache       ← 可选，在 map 之前（如果数据集小可放内存）或 map 之后（如果 map 耗时）
```

**常见错误顺序**：
- shuffle 在 batch 之后 → 只打乱了 batch 顺序，没有打乱样本顺序
- prefetch 在 batch 之前 → 预取的是单个样本，效率低
- cache 放在最后 → 缓存的是已分批的数据，可能占满内存

## 常见错误

1. shuffle 放在 batch 之后
2. prefetch 不知道放在哪里（应该最后）
3. map 函数不是 `@tf.function` 装饰的导致性能差
4. cache() 在大数据集上导致内存溢出
5. 忘记 `num_parallel_calls=tf.data.AUTOTUNE` 做并行处理
6. map 函数的输入输出类型不一致导致报错

## 训练阶梯

1. **基础创建**：能用 from_tensor_slices 创建 Dataset
2. **基本变换**：能用 map、batch、shuffle 构建简单 pipeline
3. **完整 pipeline**：能构建包含 prefetch 和 cache 的高效 pipeline
4. **文件读取**：能从文件系统加载图片/文本数据
5. **性能优化**：理解并应用 AUTOTUNE、interleave 等优化

## 掌握标准

- 能构建完整的 tf.data pipeline（shuffle → map → batch → prefetch）
- 能从文件系统加载数据
- 能分别构建训练集和验证集的 pipeline
- 理解各操作的顺序对性能和正确性的影响
- 能用 AUTOTUNE 优化 pipeline 性能
