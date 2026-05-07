# 3.3. 模型评估：量化预测质量 {#model-evaluation}

scikit-learn 提供了多种评估预测模型质量的方法。

## 3.3.1. 分类指标 {#classification-metrics}

### 准确率 {#accuracy-score}

```python
>>> from sklearn.metrics import accuracy_score
>>> accuracy_score(y_true, y_pred)
```

### 混淆矩阵 {#confusion-matrix}

```python
>>> from sklearn.metrics import confusion_matrix
>>> confusion_matrix(y_true, y_pred)
```

### 分类报告 {#classification-report}

```python
>>> from sklearn.metrics import classification_report
>>> print(classification_report(y_true, y_pred))
```

### 精确率、召回率和 F1 分数 {#precision-recall-f1}

```python
>>> from sklearn.metrics import precision_score, recall_score, f1_score
>>> precision_score(y_true, y_pred, average='macro')
>>> recall_score(y_true, y_pred, average='macro')
>>> f1_score(y_true, y_pred, average='macro')
```

### ROC 曲线和 AUC {#roc-curve}

```python
>>> from sklearn.metrics import roc_curve, auc
>>> fpr, tpr, thresholds = roc_curve(y_true, y_score)
>>> roc_auc = auc(fpr, tpr)
```

### PR 曲线 {#precision-recall-curve}

```python
>>> from sklearn.metrics import precision_recall_curve
>>> precision, recall, thresholds = precision_recall_curve(y_true, y_score)
```

## 3.3.2. 回归指标 {#regression-metrics}

### 均方误差（MSE） {#mean-squared-error}

```python
>>> from sklearn.metrics import mean_squared_error
>>> mean_squared_error(y_true, y_pred)
```

### 平均绝对误差（MAE） {#mean-absolute-error}

```python
>>> from sklearn.metrics import mean_absolute_error
>>> mean_absolute_error(y_true, y_pred)
```

### R² 分数 {#r2-score}

```python
>>> from sklearn.metrics import r2_score
>>> r2_score(y_true, y_pred)
```

### 解释方差 {#explained-variance}

```python
>>> from sklearn.metrics import explained_variance_score
>>> explained_variance_score(y_true, y_pred)
```

## 3.3.3. 聚类指标 {#clustering-metrics}

参见 [2.3. 聚类](clustering.html) 章节中的聚类评估部分。

## 3.3.4. 多指标评估 {#multi-metric-evaluation)

```python
>>> from sklearn.model_selection import cross_validate
>>> scoring = ['accuracy', 'f1_macro', 'precision_macro', 'recall_macro']
>>> results = cross_validate(clf, X, y, scoring=scoring)
```

## 常用分类指标速查表 {#classification-metrics-summary}

| 指标 | 函数 | 描述 |
|------|------|------|
| 准确率 | `accuracy_score` | 正确预测的比例 |
| 精确率 | `precision_score` | 预测为正类中真正为正类的比例 |
| 召回率 | `recall_score` | 真正为正类中被预测为正类的比例 |
| F1 | `f1_score` | 精确率和召回率的调和平均 |
| AUC | `roc_auc_score` | ROC 曲线下面积 |

## 常用回归指标速查表 {#regression-metrics-summary}

| 指标 | 函数 | 描述 |
|------|------|------|
| MSE | `mean_squared_error` | 预测误差的平方的均值 |
| RMSE | `mean_squared_error(..., squared=False)` | MSE 的平方根 |
| MAE | `mean_absolute_error` | 预测误差的绝对值的均值 |
| R² | `r2_score` | 模型解释的方差比例 |
| MAPE | `mean_absolute_percentage_error` | 平均绝对百分比误差 |
