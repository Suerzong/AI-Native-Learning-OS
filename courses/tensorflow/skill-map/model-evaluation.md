# 模型评估技能地图

## 目标

学习者能用各种指标评估模型性能，能分析模型在不同类别上的表现，能通过评估结果指导模型改进。

## 必会概念

- 训练集 vs 验证集 vs 测试集的区别
- accuracy 在类别不平衡时不可靠
- precision、recall、F1 的含义和计算
- 混淆矩阵的解读
- 过拟合（训练指标好但验证指标差）的判断
- evaluate 和 predict 的区别

## 必会 API

| 函数/类 | 用途 | 示例 |
|---------|------|------|
| `model.evaluate()` | 在测试集上评估 | `model.evaluate(x_test, y_test)` |
| `model.predict()` | 生成预测值 | `model.predict(x_new)` |
| `tf.keras.metrics.Accuracy()` | 准确率 | `metrics=['accuracy']` |
| `tf.keras.metrics.Precision()` | 精确率 | `tf.keras.metrics.Precision()` |
| `tf.keras.metrics.Recall()` | 召回率 | `tf.keras.metrics.Recall()` |
| `tf.keras.metrics.AUC()` | AUC | `tf.keras.metrics.AUC()` |
| `tf.math.confusion_matrix()` | 混淆矩阵 | `tf.math.confusion_matrix(labels, predictions)` |
| `tf.keras.metrics.BinaryAccuracy()` | 二分类准确率 | `tf.keras.metrics.BinaryAccuracy(threshold=0.5)` |

## 常用评估指标

### 分类问题

| 指标 | 含义 | 何时重要 |
|------|------|---------|
| Accuracy | 正确预测 / 总数 | 类别平衡时 |
| Precision | TP / (TP + FP) | 假阳性的代价高时（如垃圾邮件）|
| Recall | TP / (TP + FN) | 假阴性的代价高时（如疾病检测）|
| F1 Score | 2 * P * R / (P + R) | 需要平衡 P 和 R 时 |
| AUC-ROC | ROC 曲线下面积 | 二分类问题，阈值选择 |

### 回归问题

| 指标 | 含义 | 用途 |
|------|------|------|
| MSE | 均方误差 | 默认选择 |
| MAE | 平均绝对误差 | 对异常值鲁棒 |
| RMSE | 均方根误差 | 与目标变量同单位 |

## 评估代码示例

```python
import tensorflow as tf
import numpy as np

# 基本评估
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)

# 预测
y_pred_probs = model.predict(x_test)           # 概率
y_pred = np.argmax(y_pred_probs, axis=1)       # 类别索引

# 混淆矩阵
cm = tf.math.confusion_matrix(y_test, y_pred)

# 使用 sklearn 的分类报告（推荐）
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred, target_names=class_names))
```

## 训练曲线分析

```python
import matplotlib.pyplot as plt

# 从 history 对象获取指标
history = model.fit(...)
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['accuracy'], label='train_acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.legend()
```

**判断训练状态**：
- train_loss 下降 + val_loss 下降 → 正常训练
- train_loss 下降 + val_loss 上升 → 过拟合，需要正则化/更多数据/early stopping
- train_loss 不下降 → 欠拟合，需要更大模型/更多训练/更高学习率
- train_loss 震荡 → 学习率太大

## 常见错误

1. 在训练集上评估准确率（应该用测试集）
2. accuracy 在类别不平衡时不靠谱（如 99% 负样本，全预测负就有 99% 准确率）
3. 多分类时 Precision/Recall 的 average 参数选错（macro vs micro vs weighted）
4. evaluate 和 predict 的区别混淆
5. 忘记将预测概率转为类别索引（argmax）
6. 测试集上使用了数据增强

## 训练阶梯

1. **基本评估**：能用 evaluate 获取 loss 和 accuracy
2. **预测分析**：能用 predict 生成预测并转为类别
3. **多指标评估**：能计算 precision、recall、F1
4. **混淆矩阵**：能生成和解读混淆矩阵
5. **训练曲线**：能从 loss/accuracy 曲线判断训练状态

## 掌握标准

- 能不查文档写出完整的评估代码
- 能用 confusion_matrix 分析模型在各类别上的表现
- 能从训练曲线判断过拟合/欠拟合
- 能根据评估结果提出改进策略
- 理解不同指标的适用场景
