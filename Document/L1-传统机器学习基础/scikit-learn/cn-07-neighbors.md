# 1.6. 最近邻 {#neighbors}

基于最近邻的监督学习分为两种：对给定数据点的**分类**（针对离散标签）和**回归**（针对连续标签）。

## 1.6.1. 无监督最近邻 {#unsupervised-neighbors}

[`NearestNeighbors`](generated/sklearn.neighbors.NearestNeighbors.html) 实现了无监督的最近邻学习。

```python
>>> from sklearn.neighbors import NearestNeighbors
>>> import numpy as np
>>> X = np.array([[1, 1], [2, 1], [3, 2], [6, 5], [7, 8], [8, 8]])
>>> neigh = NearestNeighbors(n_neighbors=2)
>>> neigh.fit(X)
NearestNeighbors(n_neighbors=2)
>>> neigh.kneighbors([[1.5, 1.5]], return_distance=False)
array([[0, 1]])
```

## 1.6.2. 最近邻分类 {#nearest-neighbors-classification}

### 1.6.2.1. K 最近邻（KNN） {#k-nearest-neighbors-classifiers}

[`KNeighborsClassifier`](generated/sklearn.neighbors.KNeighborsClassifier.html) 基于 k 个最近邻的多数投票进行分类。

```python
>>> from sklearn.neighbors import KNeighborsClassifier
>>> neigh = KNeighborsClassifier(n_neighbors=3)
>>> neigh.fit(X, y)
KNeighborsClassifier(n_neighbors=3)
>>> print(neigh.predict([[1.1, 1.1]]))
```

### 1.6.2.2. 半径最近邻 {#radius-neighbors-classifiers}

[`RadiusNeighborsClassifier`](generated/sklearn.neighbors.RadiusNeighborsClassifier.html) 基于固定半径内邻居的多数投票进行分类。

## 1.6.3. 最近邻回归 {#nearest-neighbors-regression}

[`KNeighborsRegressor`](generated/sklearn.neighbors.KNeighborsRegressor.html) 基于 k 个最近邻的平均值进行回归。

```python
>>> from sklearn.neighbors import KNeighborsRegressor
>>> neigh = KNeighborsRegressor(n_neighbors=2)
>>> neigh.fit(X, y)
KNeighborsRegressor(n_neighbors=2)
>>> print(neigh.predict([[1.5, 1.5]]))
```

## 1.6.4. 最近邻算法 {#nearest-centroid-classifier}

可用的最近邻搜索算法：

| 算法 | 参数 | 适用场景 |
|------|------|---------|
| 暴力搜索 | `algorithm='brute'` | 小数据集 |
| K-D 树 | `algorithm='kd_tree'` | 低维数据 |
| 球树 | `algorithm='ball_tree'` | 高维数据 |
| 自动选择 | `algorithm='auto'` | 默认 |

## 1.6.5. 最近质心分类器 {#nearest-centroid-classifier}

[`NearestCentroid`](generated/sklearn.neighbors.NearestCentroid.html) 将每个类别表示为其特征均值（质心）。

```python
>>> from sklearn.neighbors import NearestCentroid
>>> clf = NearestCentroid()
>>> clf.fit(X, y)
```

## 1.6.6. 距离度量 {#nearest-neighbor-metrics}

可用的距离度量：

| 度量 | 公式 |
|------|------|
| 欧几里得距离 | \\(\sqrt{\sum (x - y)^2}\\) |
| 曼哈顿距离 | \\(\sum |x - y|\\) |
| 切比雪夫距离 | \\(\max |x_i - y_i|\\) |
| 闵可夫斯基距离 | \\((\sum |x - y|^p)^{1/p}\\) |
| 余弦距离 | \\(1 - \frac{x \cdot y}{\|x\| \|y\|}\\) |

## 1.6.7. 实用技巧 {#nearest-neighbor-tips}

- **特征缩放**：最近邻方法对特征缩放敏感。建议标准化或归一化数据。
- **k 的选择**：较小的 k 值使模型更复杂（可能过拟合），较大的 k 值使模型更简单（可能欠拟合）。
- **降维**：对于高维数据，考虑使用 PCA 等降维方法，以减少"维度灾难"的影响。
