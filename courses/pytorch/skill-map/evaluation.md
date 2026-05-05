# 模型评估技能地图

## 目标

学习者能计算各类评估指标，能分析模型在各类别上的表现，能判断过拟合/欠拟合。

## 必会概念

- Accuracy（准确率）：正确预测 / 总数
- Precision（精确率）：TP / (TP + FP)
- Recall（召回率）：TP / (TP + FN)
- F1 Score：Precision 和 Recall 的调和平均
- 混淆矩阵：各类别的预测 vs 真实分布
- 过拟合：训练集表现好，测试集差
- 欠拟合：训练集和测试集都差

## 必会 API

| 函数 | 用途 | 来源 |
|------|------|------|
| `torch.max(outputs, 1)` | 获取预测类别 | torch |
| `(predicted == labels).sum().item()` | 计算正确数 | - |
| `sklearn.metrics.accuracy_score` | 准确率 | sklearn |
| `sklearn.metrics.classification_report` | 完整分类报告 | sklearn |
| `sklearn.metrics.confusion_matrix` | 混淆矩阵 | sklearn |

## 代码片段

```python
import torch
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# 计算准确率
def evaluate_accuracy(model, dataloader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total

# 完整分类报告
def full_evaluation(model, dataloader, device, class_names):
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs = inputs.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.numpy())

    print(classification_report(all_labels, all_preds,
                                target_names=class_names))
    cm = confusion_matrix(all_labels, all_preds)
    print(cm)
```

## 常见错误

1. 在训练集上评估（应该用测试集/验证集）
2. accuracy 在类别不平衡时不靠谱
3. 不理解 multi-class 的 precision/recall 怎么算
4. 验证时忘记 model.eval() + torch.no_grad()
5. 预测结果没有 .cpu() 就转 numpy

## 训练阶梯

1. **基本准确率**：计算整体准确率
2. **分类报告**：用 sklearn 生成 precision/recall/F1
3. **混淆矩阵**：分析各类别的预测情况
4. **过拟合判断**：对比 train_loss 和 val_loss
5. **可视化**：画出 loss/accuracy 曲线

## 掌握标准

- 能计算 accuracy、precision、recall、F1
- 能生成和解读分类报告
- 能分析混淆矩阵找出模型弱点类别
- 能判断过拟合/欠拟合并给出解决方案
- 能用 TensorBoard 记录评估指标
