# 2.3. 聚类 {#clustering}

聚类是将一组对象分组的任务，使得同一组（称为簇）中的对象彼此之间比其他组中的对象更相似。

## 2.3.1. K-Means {#k-means}

K-Means 算法将 n 个样本划分为 k 个簇，使簇内平方和最小。

```python
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
>>> kmeans.labels_
>>> kmeans.predict([[0, 0], [4, 4]])
>>> kmeans.cluster_centers_
```

### Mini-Batch K-Means {#mini-batch-k-means}

[`MiniBatchKMeans`](generated/sklearn.cluster.MiniBatchKMeans.html) 是 K-Means 的变体，使用小批量数据进行更快的收敛。

```python
>>> from sklearn.cluster import MiniBatchKMeans
>>> mbk = MiniBatchKMeans(n_clusters=3, random_state=0).fit(X)
```

## 2.3.2. 亲和传播 {#affinity-propagation}

[`AffinityPropagation`](generated/sklearn.cluster.AffinityPropagation.html) 通过在数据点之间传递消息来选择一组代表性的样本。

## 2.3.3. 均值漂移 {#mean-shift}

[`MeanShift`](generated/sklearn.cluster.MeanShift.html) 旨在发现平滑密度样本中的"斑点"。

## 2.3.4. 谱聚类 {#spectral-clustering}

[`SpectralClustering`](generated/sklearn.cluster.SpectralClustering.html) 在样本之间的相似度矩阵上进行聚类，而不是在特征向量上。

```python
>>> from sklearn.cluster import SpectralClustering
>>> sc = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', random_state=0)
>>> sc.fit(X)
```

## 2.3.5. 层次聚类 {#hierarchical-clustering}

### 凝聚聚类 {#agglomerative-clustering}

[`AgglomerativeClustering`](generated/sklearn.cluster.AgglomerativeClustering.html) 递归地合并样本对。

```python
>>> from sklearn.cluster import AgglomerativeClustering
>>> clustering = AgglomerativeClustering(n_clusters=3).fit(X)
```

链接准则（linkage）：
- **ward**：最小化簇内方差
- **complete**：使用两组中所有观测值之间的最大距离
- **average**：使用两组中所有观测值之间的平均距离
- **single**：使用两组中最近观测值之间的距离

### DBSCAN {#dbscan}

[`DBSCAN`](generated/sklearn.cluster.DBSCAN.html) 基于密度进行聚类，可以找到任意形状的簇，并且不需要预先指定簇数。

```python
>>> from sklearn.cluster import DBSCAN
>>> clustering = DBSCAN(eps=0.5, min_samples=5).fit(X)
```

### HDBSCAN {#hdbscan}

[`HDBSCAN`](generated/sklearn.cluster.HDBSCAN.html) 是 DBSCAN 的扩展，将 DBSCAN 转换为层次聚类算法，然后使用基于稳定性的方法提取平坦聚类。

```python
>>> from sklearn.cluster import HDBSCAN
>>> clustering = HDBSCAN(min_cluster_size=5).fit(X)
```

### OPTICS {#optics}

[`OPTICS`](generated/sklearn.cluster.OPTICS.html) 与 DBSCAN 类似，但可以处理不同密度的簇。

## 2.3.6. BIRCH {#birch}

[`BIRCH`](generated/sklearn.cluster.BIRCH.html) 为给定的内存资源增量和动态聚类传入数据构建一个称为聚类特征树（CF Tree）的小型化内存总结。

## 2.3.7. 高斯混合模型 {#gaussian-mixture-models}

[`GaussianMixture`](generated/sklearn.mixture.GaussianMixture.html) 使用期望最大化（EM）算法拟合高斯混合模型。

```python
>>> from sklearn.mixture import GaussianMixture
>>> gmm = GaussianMixture(n_components=3).fit(X)
>>> gmm.predict(X)
```

## 2.3.8. 聚类评估 {#clustering-evaluation}

### 有标签数据的评估指标 {#clustering-evaluation-with-labels}

| 指标 | 函数 | 描述 |
|------|------|------|
| 调整兰德指数 | `adjusted_rand_score` | 衡量两个聚类的相似度 |
| 互信息 | `adjusted_mutual_info_score` | 衡量两个聚类的信息重叠 |
| 同质性、完整性、V-measure | `homogeneity_completeness_v_measure` | 基于条件熵的度量 |
| Fowlkes-Mallows 指数 | `fowlkes_mallows_score` | 几何平均的精度和召回率 |

### 无标签数据的评估指标 {#clustering-evaluation-without-labels}

| 指标 | 函数 | 描述 |
|------|------|------|
| 轮廓系数 | `silhouette_score` | 衡量簇的紧密度和分离度 |
| Calinski-Harabasz 指数 | `calinski_harabasz_score` | 簇间方差与簇内方差的比率 |
| Davies-Bouldin 指数 | `davies_bouldin_score` | 簇间相似度的平均值（越低越好） |

```python
>>> from sklearn.metrics import silhouette_score
>>> score = silhouette_score(X, labels)
```
