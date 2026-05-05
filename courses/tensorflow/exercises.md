# 训练任务库

训练任务用于 10-30 分钟内完成一个明确技能点。

## 任务模板

```md
## 任务名称

- 目标技能：
- 前置知识：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 反馈重点：
```

---

## TF-Tensor-01：创建指定形状的 Tensor

- 目标技能：使用 tf API 创建各种 tensor
- 前置知识：TensorFlow 环境搭建
- 任务要求：不查文档，写出以下代码：
  1. 创建一个 3x4 的全零 float32 tensor
  2. 创建一个 2x3x4 的标准正态分布随机 tensor
  3. 创建一个从 0 到 9（不含 10）的一维 int32 tensor
  4. 创建一个和已知 tensor `x` 形状相同但全为 1 的 tensor
  5. 创建一个 5x5 的单位矩阵
- 限制条件：必须指定正确的 dtype 和 shape
- 成功标准：5 个 tensor 全部创建成功，shape 和 dtype 正确
- 常见错误：
  - `tf.zeros()` 默认 dtype 是 float32 不是 float64
  - `tf.random.normal()` 参数是 shape 而不是单个数字
  - `tf.eye()` 和 `tf.ones()` 混淆
  - `tf.constant([0,1,2])` 默认是 int32（不同于 PyTorch 的 int64）
- 反馈重点：每个 API 的参数含义和默认行为

## TF-Tensor-02：Tensor 运算与 Shape 预测

- 目标技能：预测 tensor 运算后的 shape
- 前置知识：Tensor 创建、基本运算、broadcasting
- 任务要求：不运行代码，预测以下运算的输出 shape：
  1. `(3,4) + (4,)` → ?
  2. `(2,3,4) * (1,4)` → ?
  3. `(5,1,3) + (3,1)` → ?
  4. `tf.matmul(形状(2,3,4), 形状(2,4,5))` → ?
  5. `(2,3) @ tf.transpose(形状(4,3))` → ?
- 限制条件：必须写出 broadcasting 的匹配过程
- 成功标准：5 个 shape 全部预测正确
- 常见错误：
  - broadcasting 从右向左匹配搞错
  - matmul 和 * 的区别不理解
  - 不理解 tf.transpose 会交换所有维度（需指定 perm）
- 反馈重点：broadcasting 规则的可视化解释

## TF-Tensor-03：reshape 练习

- 目标技能：使用 tf.reshape 改变 tensor 形状
- 前置知识：Tensor shape 操作
- 任务要求：给定 `x = tf.random.normal((2, 3, 4))`，写出代码完成：
  1. 将 x 变形为 (6, 4)
  2. 将 x 变形为 (2, 12)
  3. 在第 1 维（从 0 开始计数）增加一个维度，变成 (2, 1, 3, 4)
  4. 去掉所有 size=1 的维度（如果有）
  5. 将 x 转置为 (4, 3, 2)
- 限制条件：第 3 题只能用 expand_dims，第 5 题只能用 tf.transpose 配合 perm
- 成功标准：5 个操作后的 shape 完全正确
- 常见错误：
  - expand_dims 的 axis 参数从 0 开始计数
  - tf.transpose 的 perm 参数是维度索引的排列
  - reshape 的总元素数必须和原始一致
- 反馈重点：每步操作后的 shape 标注

## TF-Keras-01：Sequential 模型构建

- 目标技能：使用 tf.keras.Sequential 构建模型
- 前置知识：Keras API 基础
- 任务要求：
  1. 构建一个接受 (28, 28, 1) 输入的 Sequential 模型
  2. 第一层：Conv2D，16 个 3x3 卷积核，ReLU 激活，padding='same'
  3. 第二层：MaxPooling2D，pool_size=2
  4. 第三层：Flatten
  5. 第四层：Dense，128 个单元，ReLU 激活
  6. 第五层：Dense，10 个单元，softmax 激活
  7. 用 `model.summary()` 打印模型结构
- 限制条件：不能用 Functional API，必须用 Sequential
- 成功标准：模型构建成功，summary 输出各层参数量正确
- 常见错误：
  - 第一层忘记写 input_shape
  - Conv2D 的 filters 和 kernel_size 参数顺序搞混
  - 最后一层 Dense 的 units 应该是分类数（10）
  - 最后一层用 softmax 时 from_logits 默认值的问题
- 反馈重点：每层输出 shape 的计算过程

## TF-Keras-02：Functional API 构建多输入模型

- 目标技能：使用 tf.keras.Functional API 构建非线性模型
- 前置知识：Sequential API、Keras Functional API
- 任务要求：
  1. 定义两个输入层：input_a（形状 (32,)）和 input_b（形状 (16,)）
  2. input_a 经过 Dense(64, relu) 得到 hidden_a
  3. input_b 经过 Dense(32, relu) 得到 hidden_b
  4. 将 hidden_a 和 hidden_b 用 tf.keras.layers.Concatenate 拼接
  5. 拼接后经过 Dense(10, softmax) 输出
  6. 创建 Model(inputs=[input_a, input_b], outputs=output)
- 限制条件：必须用 Functional API
- 成功标准：模型创建成功，能接受两个输入并输出 (None, 10) 的预测
- 常见错误：
  - 忘记用 `inputs=` 和 `outputs=` 参数
  - 层之间的连接忘记赋值（`x = layer(x)`）
  - Concatenate 的 axis 参数搞错
- 反馈重点：Functional API 的数据流概念

## TF-Data-01：tf.data Pipeline 构建

- 目标技能：用 tf.data.Dataset 构建数据管道
- 前置知识：tf.data API
- 任务要求：
  1. 用 `tf.data.Dataset.from_tensor_slices()` 从 numpy 数组创建数据集
  2. 用 `map()` 对每个元素做归一化（除以 255.0）
  3. 用 `shuffle(buffer_size=1000)` 打乱
  4. 用 `batch(32)` 分批
  5. 用 `prefetch(tf.data.AUTOTUNE)` 预取
  6. 遍历 dataset 打印一个 batch 的 shape
- 限制条件：shuffle 必须在 batch 之前
- 成功标准：pipeline 构建成功，输出 batch shape 为 (32, ...)
- 常见错误：
  - shuffle 放在 batch 之后
  - map 中的函数没有返回值
  - prefetch 放在了错误位置
- 反馈重点：各操作的正确顺序和原因

## TF-Training-01：完整训练循环骨架（fit 方式）

- 目标技能：写出标准的 Keras 训练流程
- 前置知识：Keras 模型构建、compile、fit
- 任务要求：不参考任何代码，写出以下训练流程骨架：
  1. 构建一个简单 Sequential 模型
  2. 用 compile 设置 optimizer='adam'、loss='sparse_categorical_crossentropy'、metrics=['accuracy']
  3. 用 fit 训练 10 个 epoch，validation_split=0.2
  4. 用 evaluate 在测试集上评估
  5. 用 predict 对新数据预测
- 限制条件：模型和数据可以用随机数据代替，但训练流程结构必须完整
- 成功标准：流程能运行，loss 在下降
- 常见错误：
  - compile 和 fit 的顺序搞反
  - loss 选择和标签格式不匹配
  - 忘记 validation_split 或 validation_data
- 反馈重点：compile → fit → evaluate → predict 的四步流程

## TF-Training-02：自定义训练循环（GradientTape）

- 目标技能：使用 tf.GradientTape 编写自定义训练循环
- 前置知识：GradientTape、optimizer.apply_gradients
- 任务要求：
  1. 创建一个简单模型（2 层 Dense）
  2. 用 `tf.GradientTape()` 包裹前向传播
  3. 计算 loss
  4. 用 `tape.gradient()` 计算梯度
  5. 用 `optimizer.apply_gradients()` 更新参数
  6. 循环 5 个 epoch，打印 loss
- 限制条件：不能用 model.fit()，必须手写训练步
- 成功标准：循环能运行，loss 在下降
- 常见错误：
  - GradientTape 中的上下文写错（丢失前向传播）
  - apply_gradients 传入格式不对（需要 zip(gradients, variables)）
  - 忘记计算 loss 导致 tape 中无梯度
- 反馈重点：GradientTape 的上下文管理器机制

## TF-Save-01：模型保存与加载

- 目标技能：使用 SavedModel 和 HDF5 格式保存/加载模型
- 前置知识：模型训练
- 任务要求：
  1. 训练一个简单模型
  2. 用 `model.save('my_model')` 保存 SavedModel 格式
  3. 用 `model.save('my_model.h5')` 保存 HDF5 格式
  4. 用 `tf.keras.models.load_model('my_model')` 加载 SavedModel
  5. 用 `tf.keras.models.load_model('my_model.h5')` 加载 HDF5
  6. 对比原始模型和加载模型的预测结果是否一致
- 限制条件：必须验证预测一致性
- 成功标准：两种格式保存和加载成功，预测结果完全一致
- 常见错误：
  - SavedModel 格式不需要文件扩展名
  - HDF5 格式需要 .h5 扩展名
  - 自定义层需要 custom_objects 参数
- 反馈重点：SavedModel 和 HDF5 的区别及适用场景

## TF-Lite-01：TF Lite 模型转换与推理

- 目标技能：使用 TFLiteConverter 转换模型并用 Interpreter 推理
- 前置知识：模型保存、TF Lite 基础
- 任务要求：
  1. 训练一个简单模型并保存为 SavedModel 格式
  2. 用 `tf.lite.TFLiteConverter.from_saved_model()` 转换为 TF Lite 格式
  3. 将 TF Lite 模型保存为 .tflite 文件
  4. 用 `tf.lite.Interpreter` 加载 .tflite 文件
  5. 分配输入/输出张量（`allocate_tensors()`）
  6. 设置输入数据并调用 `interpreter.invoke()`
  7. 获取输出并与原始模型对比
- 限制条件：必须对比原始模型和 TF Lite 模型的推理结果（允许小误差）
- 成功标准：TF Lite 模型推理成功，输出与原始模型近似一致
- 常见错误：
  - Converter 的输入不是 SavedModel 路径
  - 忘记 allocate_tensors()
  - 输入数据的 dtype 和 shape 不匹配
  - invoke() 前没有 set_tensor
- 反馈重点：TF Lite 推理的完整流程和各步骤含义

## TF-Augmentation-01：图像数据增强

- 目标技能：使用 tf.keras.layers 和 tf.image 做数据增强
- 前置知识：图像数据处理
- 任务要求：
  1. 用 `tf.keras.Sequential` 构建数据增强层（RandomFlip、RandomRotation、RandomZoom）
  2. 读入一张图片（用 tf.io.read_file + tf.image.decode_image）
  3. 将图片 resize 到 (224, 224)
  4. 转为 float32 并归一化到 [0, 1]
  5. 应用数据增强层，生成 5 张增强后的图片
  6. 对比原始图片和增强后的区别
- 限制条件：数据增强不能用在验证集上
- 成功标准：成功生成 5 张不同的增强图片，shape 正确
- 常见错误：
  - 数据增强层没有放在模型里而是单独使用
  - uint8 图片直接输入增强层
  - RandomRotation 的 fill_mode 参数不理解
- 反馈重点：数据增强在训练时的随机性和推理时的无操作

## TF-Text-01：TextVectorization 文本向量化

- 目标技能：使用 tf.keras.layers.TextVectorization 做文本向量化
- 前置知识：文本数据处理
- 任务要求：
  1. 创建一个 TextVectorization 层，max_tokens=1000，output_sequence_length=20
  2. 用 `adapt()` 在一批文本上学习词汇表
  3. 将文本转为整数序列
  4. 将整数序列输入 Embedding 层（input_dim=1000, output_dim=64）
  5. 打印输出 shape
- 限制条件：必须先 adapt 再使用
- 成功标准：文本成功转为 (batch, 20) 的整数序列，Embedding 输出 (batch, 20, 64)
- 常见错误：
  - 忘记 adapt 直接调用导致词汇表为空
  - max_tokens 太小导致未知词被标记为 [UNK]
  - output_sequence_length 太短截断了文本
- 反馈重点：文本到向量的完整转换过程
