# 2.5. 降维（矩阵分解） {#decomposition}

降维用于减少特征空间的维度，同时保留数据的关键信息。

## 2.5.1. 主成分分析（PCA） {#pca}

[`PCA`](generated/sklearn.decomposition.PCA.html) 使用数据的奇异值分解（SVD）将数据投影到低维空间。

```python
>>> from sklearn.decomposition import PCA
>>> pca = PCA(n_components=2)
>>> pca.fit(X)
>>> print(pca.explained_variance_ratio_)
>>> print(pca.singular_values_)
```

### 增量 PCA {#incremental-pca}

[`IncrementalPCA`](generated/sklearn.decomposition.IncrementalPCA.html) 使用小批量数据进行增量式 PCA，适合大型数据集。

### 核 PCA {#kernel-pca}

[`KernelPCA`](generated/sklearn.decomposition.KernelPCA.html) 使用核技巧进行非线性降维。

### 稀疏 PCA {#sparse-pca}

[`SparsePCA`](generated/sklearn.decomposition.SparsePCA.html) 执行带有 L1 惩罚的 PCA，产生稀疏的主成分。

### 截断 SVD {#truncated-svd}

[`TruncatedSVD`](generated/sklearn.decomposition.TruncatedSVD.html) 使用截断的 SVD 实现降维，特别适合稀疏数据。

## 2.5.2. 字典学习 {#dictionary-learning}

- [`DictionaryLearning`](generated/sklearn.decomposition.DictionaryLearning.html)：找到一个稀疏编码的字典
- [`MiniBatchDictionaryLearning`](generated/sklearn.decomposition.MiniBatchDictionaryLearning.html)：小批量版本

## 2.5.3. 因子分析 {#factor-analysis}

[`FactorAnalysis`](generated/sklearn.decomposition.FactorAnalysis.html) 是一种无监督的线性降维方法。

## 2.5.4. 独立成分分析（ICA） {#ica}

[`FastICA`](generated/sklearn.decomposition.FastICA.html) 用于从多变量信号中分离出独立的源信号。

```python
>>> from sklearn.decomposition import FastICA
>>> ica = FastICA(n_components=3)
>>> S_ = ica.fit_transform(X)
```

## 2.5.5. 非负矩阵分解（NMF） {#nmf}

[`NMF`](generated/sklearn.decomposition.NMF.html) 将非负数据矩阵 V 分解为两个非负矩阵 W 和 H 的乘积：V = W * H。

```python
>>> from sklearn.decomposition import NMF
>>> nmf = NMF(n_components=3)
>>> W = nmf.fit_transform(X)
>>> H = nmf.components_
```

## 2.5.6. 线性判别分析（LDA） {#lda}

[`LinearDiscriminantAnalysis`](generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html) 是一种分类器，但也具有降维功能，通过将数据投影到类别之间最大分离的低维空间。

```python
>>> from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
>>> lda = LinearDiscriminantAnalysis(n_components=2)
>>> X_r = lda.fit(X, y).transform(X)
```

## 2.5.7. t-SNE {#t-sne}

[`TSNE`](generated/sklearn.manifold.TSNE.html) 是一种非线性降维方法，特别适合高维数据的可视化。

```python
>>> from sklearn.manifold import TSNE
>>> tsne = TSNE(n_components=2, random_state=0)
>>> X_embedded = tsne.fit_transform(X)
```

## 降维方法选择指南 {#dim-reduction-guide}

| 方法 | 适用场景 | 线性/非线性 |
|------|---------|------------|
| PCA | 通用，大规模数据 | 线性 |
| Kernel PCA | 非线性结构 | 非线性 |
| NMF | 非负数据（如文本） | 线性 |
| LDA | 有标签的分类问题 | 线性 |
| t-SNE | 可视化 | 非线性 |
| UMAP | 可视化，保持全局结构 | 非线性 |
| ICA | 信号分离 | 线性 |
| Factor Analysis | 潜在因子发现 | 线性 |
