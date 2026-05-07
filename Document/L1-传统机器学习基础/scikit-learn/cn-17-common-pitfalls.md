# 3.9. 常见陷阱 {#common-pitfalls}

本节描述了使用 scikit-learn 时常见的一些陷阱和错误做法。

## 3.9.1. 数据泄露 {#data-leakage}

数据泄露是指在训练过程中使用了来自测试集或未来数据的信息。

### 使用不正确的交叉验证 {#incorrect-cross-validation}

在交叉验证之前进行预处理会导致数据泄露：

```python
# 错误做法
scaler.fit(X)  # 使用了全部数据
X_scaled = scaler.transform(X)
cross_val_score(model, X_scaled, y, cv=5)

# 正确做法 - 使用 Pipeline
from sklearn.pipeline import make_pipeline
pipe = make_pipeline(StandardScaler(), model)
cross_val_score(pipe, X, y, cv=5)
```

### 特征选择泄露 {#feature-selection-leakage}

特征选择也应在交叉验证内部进行：

```python
# 错误做法
selector.fit(X, y)  # 使用了全部数据
X_selected = selector.transform(X)
cross_val_score(model, X_selected, y, cv=5)

# 正确做法
from sklearn.pipeline import make_pipeline
pipe = make_pipeline(selector, model)
cross_val_score(pipe, X, y, cv=5)
```

## 3.9.2. 过拟合和欠拟合 {#overfitting-underfitting}

### 过拟合 {#overfitting}

过拟合是指模型在训练数据上表现很好，但在测试数据上表现差。

解决方案：
- 增加训练数据
- 减少模型复杂度
- 使用正则化
- 使用交叉验证选择参数

### 欠拟合 {#underfitting}

欠拟合是指模型在训练和测试数据上都表现差。

解决方案：
- 增加模型复杂度
- 添加更多特征
- 减少正则化

## 3.9.3. 样本顺序 {#sample-order}

某些算法对样本顺序敏感。建议在训练前打乱数据：

```python
>>> from sklearn.utils import shuffle
>>> X, y = shuffle(X, y, random_state=0)
```

## 3.9.4. 数值精度 {#numerical-precision}

确保使用适当的数据类型（通常是 `float64`）以避免数值精度问题。

```python
>>> X = X.astype(np.float64)
```

## 3.9.5. 类别不平衡 {#class-imbalance}

当类别分布不均匀时，模型可能偏向多数类。

解决方案：
- 使用 `class_weight='balanced'` 参数
- 过采样少数类（如 SMOTE）
- 欠采样多数类
- 使用适当的评估指标（如 F1、AUC）

```python
>>> from sklearn.svm import SVC
>>> clf = SVC(class_weight='balanced')
```

## 3.9.6. 不当的评估指标 {#inappropriate-metrics}

- 对于不平衡数据集，不要只看准确率
- 对于排序问题，考虑使用排序指标
- 选择与业务目标一致的指标

## 3.9.7. 特征缩放遗漏 {#forgetting-feature-scaling}

某些算法（如 SVM、KNN、神经网络）对特征缩放敏感，需要在训练前缩放数据。

```python
>>> from sklearn.preprocessing import StandardScaler
>>> from sklearn.pipeline import make_pipeline
>>> pipe = make_pipeline(StandardScaler(), SVC())
```

## 3.9.8. 保存和加载模型 {#saving-loading-models}

使用 `joblib` 保存和加载模型：

```python
>>> from joblib import dump, load
>>> dump(clf, 'model.joblib')
>>> clf = load('model.joblib')
```
