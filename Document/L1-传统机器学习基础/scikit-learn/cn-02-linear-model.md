# 1.1. 线性模型 {#linear-models}

以下是一组用于回归的方法，其中目标值预期是特征的线性组合。用数学符号表示，如果 \\(\hat{y}\\) 是预测值：

\\[\hat{y}(w, x) = w_0 + w_1 x_1 + ... + w_p x_p\\]

在整个模块中，我们将向量 \\(w = (w_1, ..., w_p)\\) 指定为 `coef_`，\\(w_0\\) 为 `intercept_`。

要使用广义线性模型进行分类，请参阅逻辑回归。

## 1.1.1. 普通最小二乘法 {#ordinary-least-squares}

[`LinearRegression`](<generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression> "sklearn.linear_model.LinearRegression") 拟合一个线性模型，其系数 \\(w = (w_1, ..., w_p)\\) 用于最小化数据集中观测目标与线性近似预测目标之间的残差平方和。从数学上讲，它解决以下形式的问题：

\\[\min_{w} || X w - y||_2^2\\]

```python
>>> from sklearn import linear_model
>>> reg = linear_model.LinearRegression()
>>> reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
LinearRegression()
>>> reg.coef_
array([0.5, 0.5])
>>> reg.intercept_
0.0
```

普通最小二乘法的系数估计依赖于特征的独立性。当特征相关且设计矩阵 \\(X\\) 的某些列具有近似线性依赖关系时，设计矩阵变得接近奇异，因此最小二乘估计对观测目标中的随机误差高度敏感，产生很大的方差。这种*多重共线性*的情况可能在例如没有实验设计的情况下收集数据时出现。

### 1.1.1.1. 非负最小二乘法 {#non-negative-least-squares}

可以将所有系数约束为非负，当它们表示某些物理上或自然非负的量（例如频率计数或商品价格）时可能很有用。[`LinearRegression`](<generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression> "sklearn.linear_model.LinearRegression") 接受布尔 `positive` 参数：当设置为 `True` 时，应用[非负最小二乘法](<https://en.wikipedia.org/wiki/Non-negative_least_squares>)。

### 1.1.1.2. 普通最小二乘法复杂度 {#ordinary-least-squares-complexity}

使用 \\(X\\) 的奇异值分解计算最小二乘解。如果 \\(X\\) 是形状为 `(n_samples, n_features)` 的矩阵，则该方法的计算代价为 \\(O(n_{\text{samples}} n_{\text{features}}^2)\\)，假设 \\(n_{\text{samples}} \geq n_{\text{features}}\\)。

## 1.1.2. 岭回归和分类 {#ridge-regression-and-classification}

### 1.1.2.1. 回归 {#ridge-regression}

[`Ridge`](<generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge> "sklearn.linear_model.Ridge") 回归通过对系数大小施加惩罚来解决普通最小二乘法的一些问题。岭系数最小化惩罚残差平方和：

\\[\min_{w} || X w - y||_2^2 + \alpha ||w||_2^2\\]

复杂度参数 \\(\alpha \geq 0\\) 控制收缩量：\\(\alpha\\) 的值越大，收缩量越大，因此系数对共线性变得更加稳健。

```python
>>> from sklearn import linear_model
>>> reg = linear_model.Ridge(alpha=.5)
>>> reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
Ridge(alpha=0.5)
>>> reg.coef_
array([0.34545455, 0.34545455])
>>> reg.intercept_
np.float64(0.13636)
```

### 1.1.2.2. 分类 {#ridge-classification}

[`RidgeClassifier`](<generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier> "sklearn.linear_model.RidgeClassifier") 将二元目标转换为 `{-1, 1}`，然后将问题视为回归任务，优化与上述相同的目标。预测类别对应于回归器预测的符号。对于多类分类，问题被视为多输出回归，预测类别对应于最高值的输出。

## 1.1.3. Lasso {#lasso}

[`Lasso`](<generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso> "sklearn.linear_model.Lasso") 是一个拟合稀疏系数的线性模型。它在某些情况下很有用，因为它倾向于使用较少参数的解，从而有效地减少了给定解所依赖的特征数量。因此，Lasso 及其变体是压缩感知领域的基础工具。在一定条件下，它可以恢复精确的非零权重集。

Lasso 最小化以下目标函数：

\\[\min_{w} \frac{1}{2n_{\text{samples}}} ||Xw - y||_2^2 + \alpha ||w||_1\\]

```python
>>> from sklearn import linear_model
>>> reg = linear_model.Lasso(alpha=0.1)
>>> reg.fit([[0, 0], [1, 1]], [0, 1])
Lasso(alpha=0.1)
>>> reg.predict([[1, 1]])
array([0.8])
```

## 1.1.4. 弹性网络 {#elastic-net}

[`ElasticNet`](<generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet> "sklearn.linear_model.ElasticNet") 是一个同时使用 L1 和 L2 先验作为正则化器训练的线性模型。这允许学习到一个稀疏模型，其中很少有非零权重，如 Lasso，同时仍然保持 Ridge 的正则化属性。我们使用 `l1_ratio` 参数控制 L1 和 L2 的凸组合。

当有多个相关特征时，弹性网络也很有用。Lasso 可能会随机选择其中一个，而弹性网络则可能同时选择两者。

```python
>>> from sklearn.linear_model import ElasticNet
>>> regr = ElasticNet(random_state=0)
>>> regr.fit([[0, 0], [1, 1]], [0, 1])
ElasticNet(random_state=0)
>>> regr.predict([[1, 1]])
```

## 1.1.5. 逻辑回归 {#logistic-regression}

逻辑回归虽然名字中有"回归"，但实际上是用于**分类**的线性模型。

```python
>>> from sklearn.linear_model import LogisticRegression
>>> clf = LogisticRegression(random_state=0).fit(X, y)
>>> clf.predict(X[:2, :])
>>> clf.predict_proba(X[:2, :])
```

逻辑回归可以用于：
- 二元分类
- 多元分类（使用 one-vs-rest 或 multinomial）
- 正则化（L1、L2、elasticnet）

## 1.1.6. 贝叶斯回归 {#bayesian-regression}

贝叶斯回归技术可用于在回归问题中包含正则化参数：正则化参数不是严格固定的，而是根据数据进行调整的。

```python
>>> from sklearn import linear_model
>>> reg = linear_model.BayesianRidge()
>>> reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
BayesianRidge()
```

## 1.1.7. 岭回归的其他求解器 {#solvers-for-ridge-regression}

| 求解器 | 适用场景 |
|--------|---------|
| `'svd'` | 通用 |
| `'cholesky'` | 精确解，适合中等规模数据 |
| `'sparse_cg'` | 稀疏数据 |
| `'lsqr'` | 稀疏数据，比 sparse_cg 更快 |
| `'sag'` | 大规模数据 |
| `'saga'` | 大规模数据，支持 L1 正则化 |
| `'lbfgs'` | 非负约束 |
