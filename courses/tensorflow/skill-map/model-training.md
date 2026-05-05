# 模型训练技能地图

## 目标

学习者能用 model.fit() 进行标准训练，能用 tf.GradientTape 编写自定义训练循环，能使用 Callback 监控和控制训练过程。

## 必会概念

- compile 配置训练参数（optimizer、loss、metrics）
- fit 执行训练
- evaluate 评估模型
- predict 生成预测
- Callback 在训练过程中插入自定义逻辑
- GradientTape 是 TensorFlow 的自动微分机制
- 学习率是最重要的超参数之一

## 标准训练流程（Keras 高级 API）

```python
import tensorflow as tf

# 1. 构建模型
model = tf.keras.Sequential([...])

# 2. 编译模型
model.compile(
    optimizer='adam',  # 或 tf.keras.optimizers.Adam(learning_rate=0.001)
    loss='sparse_categorical_crossentropy',  # 整数标签
    metrics=['accuracy']
)

# 3. 训练模型
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,  # 或 validation_data=(x_val, y_val)
    callbacks=[...]
)

# 4. 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)

# 5. 预测
predictions = model.predict(x_new)
```

## 自定义训练循环（GradientTape）

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10)
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# 训练循环
for epoch in range(10):
    for x_batch, y_batch in train_dataset:
        with tf.GradientTape() as tape:
            logits = model(x_batch, training=True)  # 前向传播
            loss = loss_fn(y_batch, logits)          # 计算损失
        gradients = tape.gradient(loss, model.trainable_variables)  # 计算梯度
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))  # 更新参数
```

## 常用 Callback

| Callback | 用途 | 关键参数 |
|----------|------|---------|
| `EarlyStopping` | 防止过拟合 | `monitor`, `patience`, `restore_best_weights` |
| `ModelCheckpoint` | 保存最优模型 | `filepath`, `monitor`, `save_best_only` |
| `ReduceLROnPlateau` | 降低学习率 | `monitor`, `factor`, `patience` |
| `TensorBoard` | 可视化训练 | `log_dir` |
| `LearningRateScheduler` | 自定义学习率调度 | `schedule` 函数 |

```python
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath='best_model.h5',
        monitor='val_accuracy',
        save_best_only=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=3
    )
]
```

## 常用 Loss 函数

| Loss | 用途 | 标签格式 | 输出层激活 |
|------|------|---------|----------|
| `SparseCategoricalCrossentropy` | 多分类（整数标签）| 整数（如 3）| softmax |
| `CategoricalCrossentropy` | 多分类（one-hot 标签）| one-hot 向量 | softmax |
| `BinaryCrossentropy` | 二分类 | 0 或 1 | sigmoid |
| `MSE` / `MeanSquaredError` | 回归 | 连续值 | 无（线性）|
| `MAE` / `MeanAbsoluteError` | 回归（鲁棒）| 连续值 | 无 |

## 常用 Optimizer

| Optimizer | 特点 | 适用场景 |
|-----------|------|---------|
| `SGD` | 需要手动调 lr 和 momentum | 大多数场景，配合 lr 调度 |
| `Adam` | 自适应学习率，收敛快 | 默认首选 |
| `RMSprop` | 适合 RNN | 循环神经网络 |
| `AdamW` | Adam + 权重衰减 | 需要正则化的场景 |

## 常见错误

1. compile 和 fit 的顺序搞反
2. loss 选择和标签格式不匹配（整数标签用了 categorical_crossentropy）
3. from_logits 参数设置错误（如果输出层没加 softmax，需要设 True）
4. 忘记 validation_split 或 validation_data
5. GradientTape 中前向传播没在 tape 块内
6. apply_gradients 传入格式不对（需要 zip(gradients, variables)）
7. 忘记 loss.item()（在 TF 中用 loss.numpy()）

## 训练阶梯

1. **compile + fit**：能用标准 API 完成训练
2. **Callback 使用**：能用 EarlyStopping 和 ModelCheckpoint
3. **loss 选择**：能根据任务类型选择正确的 loss
4. **GradientTape**：能手写自定义训练循环
5. **训练调优**：能调整学习率、batch size 等超参数

## 掌握标准

- 能不查文档写出完整的 compile → fit → evaluate → predict 流程
- 能正确选择 loss 函数和标签格式的组合
- 能用 Callback 控制训练过程
- 能手写 GradientTape 训练循环
- 能观察训练曲线判断是否过拟合/欠拟合
