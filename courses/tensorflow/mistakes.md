# 错题与误区记录

本文件只记录会影响后续能力形成的错误，不记录一次性笔误。

## 模板

```md
## YYYY-MM-DD：错误标题

- 所属技能：
- 错误表现：
- 错误原因：
- 正确理解：
- 纠正任务：
- 是否已复测通过：
```

---

## 常见误区样例

### Tensor Shape 不匹配导致 reshape 报错

- 所属技能：Tensor 形状操作（TF-L106）
- 错误表现：运行 `tf.reshape(x, (3, 5))` 时，如果 x 有 12 个元素，报错 `InvalidArgumentError: Cannot reshape a tensor with 12 elements to shape [3,5]`
- 错误原因：reshape 的目标 shape 元素总数（3*5=15）与原始 tensor 元素总数（12）不一致
- 正确理解：reshape 前必须确认新 shape 的元素总数等于原始 tensor 的元素总数。可以用 -1 让 TensorFlow 自动推断一个维度，如 `tf.reshape(x, (3, -1))` 会自动推断为 (3, 4)
- 纠正任务：给定 `x = tf.random.normal((2, 3, 4))`，分别写出 reshape 为 (4, 6)、(24,)、(2, -1) 的代码并验证
- 是否已复测通过：否

### 学习率过高导致训练 Loss 震荡不收敛

- 所属技能：模型训练（TF-L205）
- 错误表现：训练过程中 loss 不断震荡，甚至越来越大，没有下降趋势
- 错误原因：学习率（learning rate）设置过大，导致参数更新步长过大，无法收敛到最优解
- 正确理解：默认的 Adam optimizer 学习率是 0.001，通常适合大多数场景。如果 loss 震荡，尝试降低学习率（如 0.0001）。可以先用 `optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4)` 试跑。如果 loss 下降太慢，再适当增大学习率
- 纠正任务：用同一个模型，分别用 lr=0.01、lr=0.001、lr=0.0001 训练 10 个 epoch，对比 loss 曲线
- 是否已复测通过：否

### Conv2D 输出 Shape 计算错误

- 所属技能：常用层类型（TF-L108）
- 错误表现：用 `(W - K) / S + 1` 算 Conv2D 输出尺寸，忘记 padding 项
- 错误原因：只记住了核心公式，忽略了 padding 项
- 正确理解：完整公式是 `output = (W - K + 2P) / S + 1`，其中 W 是输入尺寸，K 是 kernel_size，P 是 padding，S 是 stride。padding='same' 时自动补零使输出尺寸等于输入尺寸（stride=1 时）
- 纠正任务：给定输入 (1, 32, 32, 3)、Conv2D(16, 3, strides=2, padding='valid')，手算输出 shape
- 是否已复测通过：否

### sparse_categorical_crossentropy 与 categorical_crossentropy 混淆

- 所属技能：模型训练（TF-L205）
- 错误表现：标签是整数索引（如 [0, 1, 2]）却用了 categorical_crossentropy，导致 shape 不匹配报错
- 错误原因：不理解两个 loss 函数对标签格式的要求不同
- 正确理解：sparse_categorical_crossentropy 接受整数标签（如 3），categorical_crossentropy 接受 one-hot 编码（如 [0,0,0,1,0,0,0,0,0,0]）。如果标签已经是整数，用 sparse 版本更方便，不用手动转 one-hot
- 纠正任务：用同一个模型，分别用两种 loss 配合正确格式的标签训练，确认结果一致
- 是否已复测通过：否

### 验证集上应用数据增强

- 所属技能：图像数据处理（TF-L203）
- 错误表现：训练集和验证集都用了数据增强（RandomFlip、RandomRotation 等），导致验证指标不稳定
- 错误原因：不理解数据增强的目的——只用于增加训练数据的多样性，验证/测试集应保持一致性
- 正确理解：数据增强只应用于训练集。验证集和测试集只做基本预处理（resize、归一化）。在 tf.data pipeline 中应分别为训练集和验证集构建不同的处理流程
- 纠正任务：构建两个 pipeline——训练 pipeline 含数据增强，验证 pipeline 只含基本预处理，对比验证指标的稳定性
- 是否已复测通过：否

### GradientTape 使用不当导致梯度为空

- 所属技能：自定义训练循环（TF-L206）
- 错误表现：运行 `tape.gradient(loss, model.trainable_variables)` 返回的梯度全部为 None
- 错误原因：前向传播的计算没有放在 GradientTape 的上下文内，或使用了非 tf.Variable 的不可训练参数
- 正确理解：所有涉及可训练变量的计算都必须在 `with tf.GradientTape() as tape:` 块内。模型的 `__call__`（即 `model(x)`）必须在 tape 块内调用。计算完梯度后，tape 默认释放，如果需要多次计算需设置 `persistent=True`
- 纠正任务：写一个正确的 GradientTape 训练循环，然后故意把前向传播移到 tape 外面，观察报错
- 是否已复测通过：否
