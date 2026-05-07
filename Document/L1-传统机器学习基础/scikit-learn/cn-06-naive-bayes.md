# 1.9. 朴素贝叶斯 {#naive-bayes}

朴素贝叶斯方法是一组基于贝叶斯定理的监督学习算法，其"朴素"假设是给定类别变量的值，每对特征之间条件独立。

贝叶斯定理：

\\[P(y | X) = \frac{P(X | y) P(y)}{P(X)}\\]

在朴素贝叶斯中，我们假设特征之间条件独立，因此：

\\[P(X | y) = \prod_{i=1}^{n} P(x_i | y)\\]

## 1.9.1. 高斯朴素贝叶斯 {#gaussian-naive-bayes}

[`GaussianNB`](generated/sklearn.naive_bayes.GaussianNB.html) 适用于连续数据，假设特征服从高斯分布。

```python
>>> from sklearn.naive_bayes import GaussianNB
>>> gnb = GaussianNB()
>>> y_pred = gnb.fit(X, y).predict(X)
```

## 1.9.2. 多项式朴素贝叶斯 {#multinomial-naive-bayes}

[`MultinomialNB`](generated/sklearn.naive_bayes.MultinomialNB.html) 适用于离散数据（如文本分类中的词频）。

```python
>>> from sklearn.naive_bayes import MultinomialNB
>>> clf = MultinomialNB()
>>> clf.fit(X, y)
```

## 1.9.3. 伯努利朴素贝叶斯 {#bernoulli-naive-bayes}

[`BernoulliNB`](generated/sklearn.naive_bayes.BernoulliNB.html) 适用于二元/布尔特征。

```python
>>> from sklearn.naive_bayes import BernoulliNB
>>> clf = BernoulliNB()
>>> clf.fit(X, y)
```

## 1.9.4. 补集朴素贝叶斯 {#complement-naive-bayes}

[`ComplementNB`](generated/sklearn.naive_bayes.ComplementNB.html) 是标准多项式朴素贝叶斯的变体，特别适合不平衡数据集。

## 1.9.5. 分类朴素贝叶斯 {#categorical-naive-bayes}

[`CategoricalNB`](generated/sklearn.naive_bayes.CategoricalNB.html) 适用于分类特征分布的数据。

## 1.9.6. 核心朴素贝叶斯 {#kernel-naive-bayes}

朴素贝叶斯方法的比较：

| 类 | 适用场景 | 特征类型 |
|----|---------|---------|
| `GaussianNB` | 通用 | 连续 |
| `MultinomialNB` | 文本分类 | 离散计数 |
| `BernoulliNB` | 二元特征 | 二元/布尔 |
| `ComplementNB` | 不平衡数据 | 离散计数 |
| `CategoricalNB` | 分类数据 | 分类 |
