# 1.4. 支持向量机 {#support-vector-machines}

**支持向量机（SVMs）**是一组用于分类、回归和异常值检测的监督学习方法。

支持向量机的优点：

- 在高维空间中有效。
- 在特征数大于样本数的情况下仍然有效。
- 在决策函数中使用训练点的子集（称为支持向量），因此也节省内存。
- 多功能：可以为决策函数指定不同的核函数。提供了常用核，也可以指定自定义核。

支持向量机的缺点：

- 如果特征数远大于样本数，在选择核函数和正则化项时避免过拟合至关重要。
- SVM 不直接提供概率估计，这些是通过昂贵的五折交叉验证计算的。

## 1.4.1. 分类 {#svm-classification}

[`SVC`](<generated/sklearn.svm.SVC.html#sklearn.svm.SVC> "sklearn.svm.SVC")、[`NuSVC`](<generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC> "sklearn.svm.NuSVC") 和 [`LinearSVC`](<generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC> "sklearn.svm.LinearSVC") 是能够在数据集上执行二元和多类分类的类。

```python
>>> from sklearn import svm
>>> X = [[0, 0], [1, 1]]
>>> y = [0, 1]
>>> clf = svm.SVC()
>>> clf.fit(X, y)
SVC()
>>> clf.predict([[2., 2.]])
array([1])
```

SVM 的决策函数依赖于训练数据的某个子集，称为支持向量。这些支持向量的一些属性可以在 `support_vectors_`、`support_` 和 `n_support_` 中找到：

```python
>>> clf.support_vectors_
array([[0., 0.],
       [1., 1.]])
>>> clf.support_
array([0, 1]...)
>>> clf.n_support_
array([1, 1]...)
```

### 1.4.1.1. 多类分类 {#multi-class-classification}

[`SVC`](<generated/sklearn.svm.SVC.html#sklearn.svm.SVC> "sklearn.svm.SVC") 和 [`NuSVC`](<generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC> "sklearn.svm.NuSVC") 为多类分类实现"一对一"（"ovo"）方法，构建 `n_classes * (n_classes - 1) / 2` 个分类器，每个在两个类的数据上训练。

另一方面，[`LinearSVC`](<generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC> "sklearn.svm.LinearSVC") 实现"一对多"（"ovr"）多类策略，因此训练 `n_classes` 个模型。

### 1.4.1.2. 得分和概率 {#scores-and-probabilities}

[`SVC`](<generated/sklearn.svm.SVC.html#sklearn.svm.SVC> "sklearn.svm.SVC") 和 [`NuSVC`](<generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC> "sklearn.svm.NuSVC") 方法的 `decision_function` 为每个样本提供每个类的得分（或每个类的每个样本的单个得分）。当构造函数选项 `probability` 设置为 `True` 时，启用类成员概率估计（来自 `predict_proba` 和 `predict_log_proba` 方法）。

### 1.4.1.3. 不平衡问题 {#unbalanced-problems}

在试图找到分离超平面时，使用 `class_weight` 和/或 `sample_weight` 可能更有利。

```python
>>> clf = svm.SVC(kernel='linear', class_weight={1: 10})
>>> clf.fit(X, y)
```

## 1.4.2. 回归 {#svm-regression}

支持向量回归由 [`SVR`](<generated/sklearn.svm.SVR.html#sklearn.svm.SVR> "sklearn.svm.SVR")、[`NuSVR`](<generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR> "sklearn.svm.NuSVR") 和 [`LinearSVR`](<generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR> "sklearn.svm.LinearSVR") 提供。方法的实现来自 `libsvm` 和 `liblinear`，因此不完全相同。

```python
>>> from sklearn import svm
>>> X = [[0, 0], [2, 2]]
>>> y = [0.5, 2.5]
>>> regr = svm.SVR()
>>> regr.fit(X, y)
SVR()
>>> regr.predict([[1, 1]])
array([1.5])
```

## 1.4.3. 密度估计、异常值检测 {#density-estimation-outlier-detection}

[`OneClassSVM`](<generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM> "sklearn.svm.OneClassSVM") 是一种无监督的异常值检测方法。

## 1.4.4. 复杂度 {#svm-complexity}

SVM 的训练时间复杂度在 \\(O(n_{\text{samples}}^2 n_{\text{features}})\\) 和 \\(O(n_{\text{samples}}^3 n_{\text{features}})\\) 之间，具体取决于核函数和数据。

## 1.4.5. 实用技巧 {#svm-tips}

- **数据缩放**：SVM 对数据的缩放不敏感。建议将数据缩放，例如缩放到 [0, 1] 或 [-1, 1]，或者标准化为均值 0 和方差 1。
- **参数选择**：使用 `GridSearchCV` 或 `RandomizedSearchCV` 来选择最优参数。
- **核选择**：`RBF` 核是一个合理的第一选择。如果特征数很大，可以尝试 `Linear` 核。

## 1.4.6. 核函数 {#svm-kernels}

| 核函数 | 公式 | 参数 |
|--------|------|------|
| 线性（Linear） | \\(\langle x, x'\\rangle\\) | 无 |
| 多项式（Polynomial） | \\((\gamma \langle x, x'\rangle + r)^d\\) | `degree`, `gamma`, `coef0` |
| RBF（径向基函数） | \\(\exp(-\gamma \|x-x'\|^2)\\) | `gamma` |
| Sigmoid | \\(\tanh(\gamma \langle x,x'\rangle + r)\\) | `gamma`, `coef0` |
