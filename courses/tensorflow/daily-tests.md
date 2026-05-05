# 每日诊断短测

每日短测用于判断今天应该训练什么，而不是为了打分。

## 模板

```md
## YYYY-MM-DD

### 诊断题

1. 概念题：
2. API 题：
3. Shape 预测题：
4. 调试题：

### 结果

- 正确率：
- 主要错误：
- 今日训练目标：
- 是否允许推进：
```

---

## TensorFlow 基础诊断样例

1. TensorFlow 2.x 默认使用哪种执行模式（Eager Execution 还是 Graph Execution）？这和 1.x 有什么区别？
2. 写出创建一个 (3, 4) 的 float32 全零 tensor 的代码（分别用 tf.constant 和 tf.zeros）。
3. 给定 `x = tf.random.normal((2, 3, 4))`，`tf.reshape(x, (6, -1))` 的输出 shape 是什么？
4. 如果运行 `a = tf.constant([1.0, 2.0]); b = tf.constant([3, 4]); a + b` 会报什么错？为什么？

## Keras API 诊断样例

1. tf.keras.Sequential 和 Functional API 的主要区别是什么？
2. 写出一个包含 input_shape=(28,28,1)、Conv2D(16, 3)、Flatten、Dense(10) 的 Sequential 模型代码。
3. `model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')` 中 sparse_categorical_crossentropy 和 categorical_crossentropy 的区别是什么？
4. 模型 summary 输出的 Param 是怎么计算的？Dense(128, input_dim=64) 有多少参数？

## tf.data 诊断样例

1. tf.data.Dataset 的 map、batch、shuffle、prefetch 分别起什么作用？
2. 构建 tf.data pipeline 时，shuffle 应该放在 batch 之前还是之后？为什么？
3. `tf.data.AUTOTUNE` 的作用是什么？
4. 如果 pipeline 中 map 函数处理太慢，可以用什么方法加速？

## 模型训练诊断样例

1. 写出 model.fit() 的基本调用方式，包含 epochs 和 validation_split 参数。
2. tf.GradientTape 的作用是什么？什么时候需要手写训练循环？
3. EarlyStopping 的 patience 参数是什么含义？monitor 参数可以监控什么？
4. model.evaluate() 和 model.predict() 的区别是什么？

## TF Lite 诊断样例

1. 从 SavedModel 转换为 TF Lite 格式的基本代码是什么？
2. tf.lite.Interpreter 加载模型后，推理前必须调用什么方法？
3. TF Lite 的 full integer quantization 需要什么额外信息？
4. 量化后的模型相比原始模型有什么优势和劣势？
