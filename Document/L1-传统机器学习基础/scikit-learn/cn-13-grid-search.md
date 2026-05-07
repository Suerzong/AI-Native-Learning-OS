# 3.2. 调整估计器的超参数 {#grid-search}

超参数调整是机器学习中的重要步骤，用于找到最佳的模型配置。

## 3.2.1. 网格搜索 {#grid-search-exhaustive}

[`GridSearchCV`](generated/sklearn.model_selection.GridSearchCV.html) 对指定的参数值进行详尽搜索。

```python
>>> from sklearn.model_selection import GridSearchCV
>>> from sklearn import svm
>>> parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
>>> svc = svm.SVC()
>>> clf = GridSearchCV(svc, parameters, cv=5)
>>> clf.fit(X, y)
>>> print(clf.best_params_)
>>> print(clf.best_score_)
```

## 3.2.2. 随机搜索 {#random-search}

[`RandomizedSearchCV`](generated/sklearn.model_selection.RandomizedSearchCV.html) 从参数分布中采样固定数量的参数设置。

```python
>>> from sklearn.model_selection import RandomizedSearchCV
>>> from scipy.stats import uniform
>>> distributions = {'C': uniform(loc=0, scale=10), 'kernel': ['linear', 'rbf']}
>>> clf = RandomizedSearchCV(svc, distributions, n_iter=10, random_state=0)
>>> clf.fit(X, y)
```

随机搜索的优点：
- 比网格搜索更高效
- 可以搜索连续的参数分布
- 对于高维参数空间更实用

## 3.2.3. 参数搜索技巧 {#search-tips}

### 指定目标度量 {#specifying-metric}

```python
>>> GridSearchCV(svc, parameters, scoring='accuracy')
>>> GridSearchCV(svc, parameters, scoring='f1_macro')
```

### 复合估计器的参数空间 {#composite-estimators}

使用 `__` 语法指定嵌套参数：

```python
>>> from sklearn.pipeline import Pipeline
>>> from sklearn.decomposition import PCA
>>> pipe = Pipeline([('pca', PCA()), ('svc', svm.SVC())])
>>> parameters = {'pca__n_components': [2, 5, 10], 'svc__C': [0.1, 1, 10]}
>>> GridSearchCV(pipe, parameters)
```

### 并行化 {#parallelization}

```python
>>> GridSearchCV(svc, parameters, n_jobs=-1)  # 使用所有 CPU 核心
```

## 3.2.4. 替代方法 {#alternative-search}

### Halving GridSearchCV {#halving-grid-search}

[`HalvingGridSearchCV`](generated/sklearn.model_selection.HalvingGridSearchCV.html) 使用连续减半策略，逐步淘汰表现不佳的候选参数：

```python
>>> from sklearn.experimental import enable_halving_search_cv
>>> from sklearn.model_selection import HalvingGridSearchCV
>>> halving_cv = HalvingGridSearchCV(svc, parameters, factor=2)
>>> halving_cv.fit(X, y)
```

### Halving Random SearchCV {#halving-random-search}

```python
>>> from sklearn.model_selection import HalvingRandomSearchCV
>>> halving_cv = HalvingRandomSearchCV(svc, distributions, factor=2)
```

Halving 方法的优点：
- 比传统网格搜索更高效
- 在计算资源有限时特别有用
