# 3.1. 交叉验证：评估估计器性能 {#cross-validation}

交叉验证用于评估模型在未见数据上的泛化能力。

## 3.1.1. 保留交叉验证 {#holdout-cross-validation}

最简单的方法是将数据分为训练集和测试集：

```python
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```

## 3.1.2. K 折交叉验证 {#k-fold-cross-validation}

K 折交叉验证将数据分为 K 个子集，每次使用 K-1 个子集训练，剩余 1 个用于测试。

```python
>>> from sklearn.model_selection import cross_val_score
>>> from sklearn import svm
>>> clf = svm.SVC(kernel='linear', C=1, random_state=42)
>>> scores = cross_val_score(clf, X, y, cv=5)
>>> print(scores)
>>> print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
```

## 3.1.3. 交叉验证迭代器 {#cross-validation-iterators}

### K 折 {#k-fold}

```python
>>> from sklearn.model_selection import KFold
>>> kf = KFold(n_splits=5)
>>> for train, test in kf.split(X):
...     print("%s %s" % (train, test))
```

### 分层 K 折 {#stratified-k-fold}

[`StratifiedKFold`](generated/sklearn.model_selection.StratifiedKFold.html) 保持每个折叠中各类别的比例。

```python
>>> from sklearn.model_selection import StratifiedKFold
>>> skf = StratifiedKFold(n_splits=5)
>>> for train, test in skf.split(X, y):
...     print("%s %s" % (train, test))
```

### 留一法交叉验证（LOOCV） {#leave-one-out}

```python
>>> from sklearn.model_selection import LeaveOneOut
>>> loo = LeaveOneOut()
>>> for train, test in loo.split(X):
...     print("%s %s" % (train, test))
```

### 留 P 法交叉验证 {#leave-p-out}

```python
>>> from sklearn.model_selection import LeavePOut
>>> lpo = LeavePOut(p=2)
```

### 重复 K 折交叉验证 {#repeated-k-fold}

```python
>>> from sklearn.model_selection import RepeatedKFold
>>> rkf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=0)
```

### 时间序列分割 {#time-series-split}

[`TimeSeriesSplit`](generated/sklearn.model_selection.TimeSeriesSplit.html) 用于时间序列数据的交叉验证。

```python
>>> from sklearn.model_selection import TimeSeriesSplit
>>> tscv = TimeSeriesSplit(n_splits=5)
```

### 分组 K 折 {#group-k-fold}

[`GroupKFold`](generated/sklearn.model_selection.GroupKFold.html) 确保同一组的数据不会同时出现在训练集和测试集中。

## 3.1.4. 交叉验证评分 {#cross-validation-scoring}

```python
>>> from sklearn.metrics import make_scorer, accuracy_score, f1_score
>>> cross_val_score(clf, X, y, cv=5, scoring='accuracy')
>>> cross_val_score(clf, X, y, cv=5, scoring=make_scorer(f1_score, average='macro'))
```

## 3.1.5. 交叉验证与网格搜索 {#cross-validation-grid-search}

参见 [3.2. 网格搜索](grid_search.html) 章节。
