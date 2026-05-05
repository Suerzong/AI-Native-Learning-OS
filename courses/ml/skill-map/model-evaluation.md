# skill-map: model-evaluation — 模型评估（指标、交叉验证、混淆矩阵）

## 目标

掌握模型评估的完整方法论，能选择合适的评估指标，能用交叉验证可靠地评估模型。

## 必知概念

### 分类评估指标

#### 混淆矩阵
```
                  预测正  预测负
实际正    TP（真阳）  FN（假阴）
实际负    FP（假阳）  TN（真阴）
```

#### 核心指标
| 指标 | 公式 | 含义 | 适用场景 |
|------|------|------|----------|
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | 总体正确率 | 类别平衡时 |
| Precision | TP/(TP+FP) | 预测为正中真正为正的比例 | 关注误报（如垃圾邮件） |
| Recall | TP/(TP+FN) | 真正为正中被找到的比例 | 关注漏报（如疾病检测） |
| F1 | 2*P*R/(P+R) | Precision 和 Recall 的调和平均 | 类别不平衡时 |
| AUC-ROC | ROC 曲线下面积 | 模型区分正负类的能力 | 通用 |

#### ROC 曲线
- X 轴：FPR = FP/(FP+TN)（假阳性率）
- Y 轴：TPR = TP/(TP+FN)（真阳性率 = Recall）
- AUC = 1：完美模型，AUC = 0.5：随机猜测

### 回归评估指标
| 指标 | 公式 | 含义 |
|------|------|------|
| MSE | mean((y - y_hat)^2) | 均方误差 |
| RMSE | sqrt(MSE) | 与 y 同单位 |
| MAE | mean(|y - y_hat|) | 对异常值鲁棒 |
| R² | 1 - SS_res/SS_tot | 解释方差比例 |

### 交叉验证（Cross-Validation）
- **K-Fold**：数据分成 K 份，轮流用 K-1 份训练、1 份评估
- **Stratified K-Fold**：每折保持类别比例（分类任务推荐）
- **Leave-One-Out**：K = n（小数据集）
- **目的**：
  - 更可靠地估计模型性能
  - 减少单次划分的随机性
  - 充分利用有限数据

### 评估指标选择指南
| 场景 | 推荐指标 |
|------|----------|
| 类别平衡的分类 | Accuracy, F1 |
| 类别不平衡的分类 | F1, AUC-ROC, Precision-Recall |
| 关注误报 | Precision |
| 关注漏报 | Recall |
| 回归任务 | RMSE, MAE, R² |
| 模型对比 | 交叉验证分数 |

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `accuracy_score()` | 准确率 | `accuracy_score(y_test, y_pred)` |
| `precision_score()` | 精确率 | `precision_score(y_test, y_pred)` |
| `recall_score()` | 召回率 | `recall_score(y_test, y_pred)` |
| `f1_score()` | F1 分数 | `f1_score(y_test, y_pred)` |
| `roc_auc_score()` | AUC-ROC | `roc_auc_score(y_test, y_prob)` |
| `confusion_matrix()` | 混淆矩阵 | `confusion_matrix(y_test, y_pred)` |
| `classification_report()` | 分类报告 | `classification_report(y_test, y_pred)` |
| `roc_curve()` | ROC 曲线数据 | `fpr, tpr, _ = roc_curve(y_test, y_prob)` |
| `cross_val_score()` | 交叉验证 | `cross_val_score(model, X, y, cv=5)` |
| `mean_squared_error()` | MSE | `mean_squared_error(y_test, y_pred)` |
| `r2_score()` | R² | `r2_score(y_test, y_pred)` |

## 常见错误

1. **不平衡数据只看 Accuracy**
   ```python
   # 99% 负类，全预测为负
   accuracy_score(y_test, y_pred)  # 0.99 —— 虚高

   # 应该看 F1 或 AUC
   f1_score(y_test, y_pred)  # 0.0 —— 真实性能
   ```

2. **混淆矩阵行列含义搞反**
   ```python
   cm = confusion_matrix(y_test, y_pred)
   # 行 = 实际，列 = 预测
   # cm[0][0] = 实际0预测0 = TN
   # cm[1][0] = 实际1预测0 = FN
   ```

3. **ROC 曲线用类别预测而非概率**
   ```python
   # 错误：用 predict 的类别
   roc_curve(y_test, model.predict(X_test))

   # 正确：用 predict_proba 的概率
   roc_curve(y_test, model.predict_proba(X_test)[:, 1])
   ```

4. **交叉验证包含测试集信息**
   ```python
   # 错误：在整个数据集上做预处理
   X_scaled = scaler.fit_transform(X)
   cross_val_score(model, X_scaled, y, cv=5)

   # 正确：在 Pipeline 中做预处理
   pipe = Pipeline([('scaler', StandardScaler()), ('model', model)])
   cross_val_score(pipe, X, y, cv=5)
   ```

## 训练阶梯

### Step 1: 基础指标（Level 0→2）
- 理解 Accuracy、Precision、Recall
- 计算混淆矩阵
- 使用 classification_report

### Step 2: 高级指标（Level 2→3）
- 理解 F1 分数
- 理解 AUC-ROC
- 绘制 ROC 曲线

### Step 3: 回归指标（Level 3）
- 理解 MSE、RMSE、MAE、R²
- 知道各指标的适用场景
- 能解释 R² 的含义

### Step 4: 交叉验证（Level 3→4）
- 使用 cross_val_score
- 理解 K-Fold 和分层采样
- 能解释交叉验证分数的意义

### Step 5: 综合评估（Level 4→5）
- 根据场景选择合适的指标
- 设计完整的评估方案
- 考虑评估的计算成本

## 掌握标准

- **Level 3**: 能计算和解释各种评估指标，能使用交叉验证
- **Level 4**: 能根据场景选择合适的指标，能设计评估方案
- **Level 5**: 能从零实现评估指标，能分析评估结果的统计显著性

## 参考资料

- materials/noob/025_ml-regression-model-evaluation.md
- materials/noob/032_ml-classification-metrics.md
- materials/noob/043_ml-cross-validation.md
- scikit-learn 模型评估：https://scikit-learn.org/stable/modules/model_selection.html
