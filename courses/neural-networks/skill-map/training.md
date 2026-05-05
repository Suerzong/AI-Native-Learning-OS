# 训练流程技能地图

## 目标

学习者能理解完整的模型训练流程，包括数据划分、超参数调优、评估指标计算，能系统地做实验并记录结果。

## 必会概念

- 数据划分：训练集/验证集/测试集
- 超参数 vs 模型参数
- 评估指标：Accuracy、Precision、Recall、F1
- 混淆矩阵
- 偏差-方差权衡

## 数据划分

```
总数据
├── 训练集 (60-80%)：用于学习参数
├── 验证集 (10-20%)：用于选超参数、早停
└── 测试集 (10-20%)：最终评估，只用一次

重要：绝不能用测试集调参（数据泄露）
交叉验证：K-fold，每折轮流做验证集
```

## 评估指标公式

```
混淆矩阵：
                    预测正    预测负
实际正（Positive）    TP        FN
实际负（Negative）    FP        TN

Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)    # 预测为正的里面有多少是对的
Recall = TP / (TP + FN)       # 实际为正的里面有多少被找到了
F1 = 2 * Precision * Recall / (Precision + Recall)

多分类：每个类别计算 P/R/F1，然后取宏平均或微平均
```

## 关键超参数

| 超参数 | 作用 | 常见范围 | 调优策略 |
|--------|------|---------|---------|
| 学习率 | 控制更新步长 | 1e-5 ~ 1e-1 | 先粗调（对数尺度） |
| Batch Size | 每批数据量 | 16, 32, 64, 128 | 受显存限制 |
| Epochs | 训练轮数 | 10 ~ 200 | 用 early stopping |
| 隐藏层大小 | 网络容量 | 32 ~ 1024 | 从小到大试 |
| Dropout rate | 正则化强度 | 0.1 ~ 0.5 | 观察 val loss |
| L2 系数 | 正则化强度 | 1e-5 ~ 1e-2 | 配合 Dropout |

## 代码实现

```python
import numpy as np

def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

def precision_recall_f1(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)

    return precision, recall, f1

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    return cm

# Early Stopping
class EarlyStopping:
    def __init__(self, patience=10, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None

    def should_stop(self, val_loss):
        if self.best_loss is None:
            self.best_loss = val_loss
        elif val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
        return self.counter >= self.patience
```

## 调参流程

```
1. 先让模型跑起来（默认超参数）
2. 检查 train loss 是否下降
   - 不下降 → 学习率太小或模型太简单
3. 检查 val loss 是否下降
   - val loss 上升 → 过拟合，加正则化
4. 记录实验结果（超参数 → 指标）
5. 一次只改一个超参数
6. 用验证集选最优组合
7. 最终在测试集上报一次结果
```

## 常见错误

| 错误 | 原因 | 修正 |
|------|------|------|
| 在测试集上调参 | 数据泄露 | 只用验证集调参 |
| 只看 Accuracy | 不均衡数据误导 | 看 P/R/F1 和混淆矩阵 |
| 一次改多个超参数 | 不知道哪个起作用 | 每次只改一个 |
| 不记录实验结果 | 无法对比和复现 | 写实验日志 |

## 训练阶梯

1. **数据划分**：给定数据集，正确划分为 train/val/test
2. **指标计算**：不用 sklearn，用 NumPy 计算 P/R/F1
3. **混淆矩阵**：画出并解释多分类混淆矩阵
4. **实验记录**：调参时记录每组超参数和结果
5. **Early Stopping**：实现并验证其效果
6. **综合调参**：系统调参并在验证集上找到最优组合
7. **最终评估**：在测试集上报告最终指标

## 掌握标准

- 能正确划分数据集并解释为什么不能用测试集调参
- 能用 NumPy 计算 Accuracy、Precision、Recall、F1
- 能画出并解释混淆矩阵
- 能系统地调参并记录实验结果
