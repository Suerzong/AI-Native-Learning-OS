# Keras API 技能地图

## 目标

学习者能用 Keras 的 Sequential、Functional API 和 Model Subclassing 三种方式构建模型，理解各自的适用场景和限制。

## 必会概念

- Keras 是 TensorFlow 的高级 API（tf.keras）
- Sequential API：线性堆叠层，最简单
- Functional API：支持任意拓扑（多输入/多输出/共享层/分支）
- Model Subclassing：最灵活，继承 tf.keras.Model 自定义
- Layer 是模型的基本构建单元
- compile → fit → evaluate → predict 的标准流程

## 必会 API

### Sequential API

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

| 方法 | 用途 | 示例 |
|------|------|------|
| `model.add(layer)` | 添加层 | `model.add(Dense(64))` |
| `model.summary()` | 打印模型结构 | `model.summary()` |
| `model.compile()` | 配置训练参数 | `model.compile(optimizer, loss, metrics)` |
| `model.fit()` | 训练模型 | `model.fit(x, y, epochs=10)` |
| `model.evaluate()` | 评估模型 | `model.evaluate(x_test, y_test)` |
| `model.predict()` | 预测 | `model.predict(x_new)` |
| `model.save()` | 保存模型 | `model.save('my_model')` |
| `model.layers` | 获取所有层 | `for layer in model.layers` |

### Functional API

```python
import tensorflow as tf

inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

### 三种 API 的选择

| 场景 | 推荐 API |
|------|---------|
| 简单线性堆叠模型 | Sequential |
| 多输入/多输出模型 | Functional |
| 共享层或分支结构 | Functional |
| 需要自定义前向传播逻辑 | Model Subclassing |
| 需要在 forward 中使用控制流（if/for） | Model Subclassing |

## 常用层类型

| 层 | 用途 | 关键参数 |
|---|------|---------|
| `Dense` | 全连接层 | `units`, `activation`, `input_shape` |
| `Conv2D` | 2D 卷积层 | `filters`, `kernel_size`, `strides`, `padding` |
| `MaxPooling2D` | 最大池化 | `pool_size`, `strides` |
| `Flatten` | 展平 | 无 |
| `Dropout` | 随机丢弃 | `rate`（丢弃比例）|
| `BatchNormalization` | 批归一化 | 无（通常放在 Conv/Dense 后）|
| `LSTM` | 长短期记忆 | `units`, `return_sequences` |
| `Embedding` | 词嵌入 | `input_dim`, `output_dim`, `input_length` |
| `GlobalAveragePooling2D` | 全局平均池化 | 无 |

## 代码片段

```python
import tensorflow as tf

# Sequential
model_seq = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Functional（多输入）
input_a = tf.keras.Input(shape=(32,), name='input_a')
input_b = tf.keras.Input(shape=(16,), name='input_b')
x_a = tf.keras.layers.Dense(64, activation='relu')(input_a)
x_b = tf.keras.layers.Dense(32, activation='relu')(input_b)
concat = tf.keras.layers.Concatenate()([x_a, x_b])
outputs = tf.keras.layers.Dense(10, activation='softmax')(concat)
model_func = tf.keras.Model(inputs=[input_a, input_b], outputs=outputs)
```

## 常见错误

1. Sequential 第一层忘记写 `input_shape`
2. 混淆 `filters`（卷积核数量）和 `kernel_size`（卷积核大小）
3. Functional API 忘记 `x = layer(x)` 的赋值
4. compile 后再加层会报错
5. 最后一层分类任务应该用 softmax，回归任务不加激活
6. Dropout 的 `rate` 是丢弃比例（0.2 = 丢弃 20%）

## 训练阶梯

1. **Sequential 基础**：能用 Sequential 构建简单模型
2. **compile/fit**：能正确配置和训练模型
3. **层参数理解**：能计算各层的参数量
4. **Functional API**：能构建多输入/多输出模型
5. **Model Subclassing**：能继承 tf.keras.Model 实现自定义模型

## 掌握标准

- 能用 Sequential 构建 CNN/MLP 模型
- 能用 Functional API 构建多输入模型
- 能计算 Dense 和 Conv2D 层的参数量
- 能根据任务类型选择合适的输出层激活函数
- 能用 model.summary() 解读模型结构
