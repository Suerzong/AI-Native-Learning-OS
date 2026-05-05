# 自定义组件技能地图

## 目标

学习者能自定义 Keras Layer、Loss 和 Metric，理解 Keras 的扩展机制，能在模型中使用自定义组件。

## 必会概念

- 自定义 Layer 继承 `tf.keras.layers.Layer`
- 自定义 Loss 继承 `tf.keras.losses.Loss`
- 自定义 Metric 继承 `tf.keras.metrics.Metric`
- `build()` 方法用于创建权重（惰性初始化）
- `call()` 方法定义前向传播
- `get_config()` 方法支持序列化（保存/加载）
- 自定义组件在 SavedModel 中需要注册

## 自定义 Layer

### 基本结构

```python
import tensorflow as tf

class MyDense(tf.keras.layers.Layer):
    def __init__(self, units=32, **kwargs):
        super().__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        # build 在第一次 call 时自动调用，input_shape 已知
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer='glorot_uniform',
            trainable=True,
            name='kernel'
        )
        self.b = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            trainable=True,
            name='bias'
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config
```

### 关键方法说明

| 方法 | 调用时机 | 用途 |
|------|---------|------|
| `__init__` | 创建实例时 | 初始化超参数（不含权重）|
| `build(input_shape)` | 第一次 call 前 | 创建权重（用 `add_weight`）|
| `call(inputs)` | 每次前向传播 | 定义计算逻辑 |
| `get_config()` | 保存模型时 | 返回序列化配置 |

### 注意事项

- **不要在 `__init__` 中创建权重**（此时 input_shape 未知）
- **必须用 `self.add_weight()` 创建权重**（不能直接用 `tf.Variable`）
- **`call()` 中可以使用控制流**（if、for、while）
- **`build()` 只在首次调用时执行**（惰性初始化）

## 自定义 Loss

### 基本结构

```python
import tensorflow as tf

class MyHuberLoss(tf.keras.losses.Loss):
    def __init__(self, delta=1.0, **kwargs):
        super().__init__(**kwargs)
        self.delta = delta

    def call(self, y_true, y_pred):
        error = tf.abs(y_true - y_pred)
        condition = error <= self.delta
        small_error = 0.5 * tf.square(error)
        large_error = self.delta * (error - 0.5 * self.delta)
        return tf.where(condition, small_error, large_error)

    def get_config(self):
        config = super().get_config()
        config.update({"delta": self.delta})
        return config
```

### 使用方式

```python
# 方式 1：实例化后传入 compile
loss_fn = MyHuberLoss(delta=2.0)
model.compile(optimizer='adam', loss=loss_fn)

# 方式 2：直接传入类（使用默认参数）
model.compile(optimizer='adam', loss=MyHuberLoss)
```

### 简单方式（函数式 Loss）

```python
# 不需要自定义类时，直接用函数
def my_huber_loss(y_true, y_pred):
    delta = 1.0
    error = tf.abs(y_true - y_pred)
    condition = error <= delta
    return tf.where(condition, 0.5 * tf.square(error), delta * (error - 0.5 * delta))

model.compile(optimizer='adam', loss=my_huber_loss)
```

## 自定义 Metric

### 基本结构

```python
import tensorflow as tf

class MyAccuracy(tf.keras.metrics.Metric):
    def __init__(self, name='my_accuracy', **kwargs):
        super().__init__(name=name, **kwargs)
        self.correct = self.add_weight(name='correct', initializer='zeros')
        self.total = self.add_weight(name='total', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.argmax(y_pred, axis=1)
        y_true = tf.cast(tf.squeeze(y_true), tf.int64)
        matches = tf.cast(y_true == y_pred, tf.float32)
        self.correct.assign_add(tf.reduce_sum(matches))
        self.total.assign_add(tf.cast(tf.size(y_true), tf.float32))

    def result(self):
        return self.correct / self.total

    def reset_state(self):
        self.correct.assign(0.0)
        self.total.assign(0.0)
```

### 关键方法说明

| 方法 | 用途 |
|------|------|
| `__init__` | 用 `add_weight` 创建状态变量 |
| `update_state(y_true, y_pred)` | 每个 batch 后更新状态 |
| `result()` | 返回当前指标值 |
| `reset_state()` | 每个 epoch 开始时重置状态 |

## 自定义组件的保存与加载

```python
# 保存
model.save('my_model')

# 加载（需要提供自定义对象）
loaded = tf.keras.models.load_model(
    'my_model',
    custom_objects={
        'MyDense': MyDense,
        'MyHuberLoss': MyHuberLoss,
        'MyAccuracy': MyAccuracy
    }
)

# 或者在类中定义 get_config() 后，可以注册为可序列化
@tf.keras.utils.register_keras_serializable()
class MyDense(tf.keras.layers.Layer):
    ...
```

## 常见错误

1. 在 `__init__` 中创建权重（应该在 `build` 中）
2. 用 `tf.Variable()` 而不是 `self.add_weight()` 创建权重
3. 自定义 Loss 的 `call` 方法签名错误（应该是 `call(self, y_true, y_pred)`）
4. 自定义 Metric 忘记实现 `reset_state()`
5. 没有实现 `get_config()` 导致保存/加载失败
6. 自定义组件在 TF Lite 转换时可能不支持

## 训练阶梯

1. **函数式 Loss**：能用普通 Python 函数定义简单 Loss
2. **类式 Loss**：能继承 `tf.keras.losses.Loss` 定义 Loss
3. **简单 Layer**：能自定义无权重的 Layer（如自定义激活函数）
4. **有权重 Layer**：能自定义含可训练参数的 Layer
5. **自定义 Metric**：能实现完整的自定义 Metric

## 掌握标准

- 能不查文档写出自定义 Layer 的 build + call 结构
- 能实现至少一种自定义 Loss（如 Huber Loss）
- 理解 `add_weight` 和 `tf.Variable` 的区别
- 能正确实现 `get_config()` 支持模型保存
- 理解自定义组件在 TF Lite 部署时的限制
