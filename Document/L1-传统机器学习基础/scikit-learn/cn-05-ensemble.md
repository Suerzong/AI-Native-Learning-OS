# 1.11. 集成方法 {#ensemble-methods}

集成方法（Ensemble methods）通过组合多个基学习器（base estimators）的预测来提高预测性能。

## 1.11.1. Bagging 元估计器 {#bagging-meta-estimator}

Bagging 元估计器在原始数据集的随机子集上拟合每个基学习器，然后聚合它们的预测（通过投票或平均）。

- [`BaggingClassifier`](generated/sklearn.ensemble.BaggingClassifier.html)：分类的 Bagging
- [`BaggingRegressor`](generated/sklearn.ensemble.BaggingRegressor.html)：回归的 Bagging

```python
>>> from sklearn.ensemble import BaggingClassifier
>>> from sklearn.tree import DecisionTreeClassifier
>>> bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10, random_state=0)
>>> bagging.fit(X, y)
```

## 1.11.2. 随机森林 {#random-forests}

随机森林是 Bagging 的一种变体，每棵树在选择拆分特征时引入额外的随机性。

- [`RandomForestClassifier`](generated/sklearn.ensemble.RandomForestClassifier.html)
- [`RandomForestRegressor`](generated/sklearn.ensemble.RandomForestRegressor.html)

```python
>>> from sklearn.ensemble import RandomForestClassifier
>>> clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
>>> clf.fit(X, y)
>>> clf.predict(X[:2])
```

随机森林的优点：
- 不需要特征缩放
- 可以处理混合类型的特征
- 提供特征重要性
- 内置交叉验证（OOB 分数）

## 1.11.3. AdaBoost {#adaboost}

AdaBoost 是一种 Boosting 方法，通过调整错误分类样本的权重来迭代训练弱学习器。

- [`AdaBoostClassifier`](generated/sklearn.ensemble.AdaBoostClassifier.html)
- [`AdaBoostRegressor`](generated/sklearn.ensemble.AdaBoostRegressor.html)

```python
>>> from sklearn.ensemble import AdaBoostClassifier
>>> clf = AdaBoostClassifier(n_estimators=100, random_state=0)
>>> clf.fit(X, y)
```

## 1.11.4. 梯度树提升 {#gradient-tree-boosting}

梯度树提升（Gradient Tree Boosting 或 Gradient Boosted Decision Trees, GBDT）是一种泛化能力强大的 Boosting 方法。

- [`GradientBoostingClassifier`](generated/sklearn.ensemble.GradientBoostingClassifier.html)
- [`GradientBoostingRegressor`](generated/sklearn.ensemble.GradientBoostingRegressor.html)

```python
>>> from sklearn.ensemble import GradientBoostingClassifier
>>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
>>> clf.fit(X, y)
```

关键参数：
- `n_estimators`：提升阶段的数量（树的数量）
- `learning_rate`：学习率，控制每棵树的贡献
- `max_depth`：每棵树的最大深度
- `subsample`：用于拟合各个基学习器的样本比例

## 1.11.5. 投票分类器 {#voting-classifier}

投票分类器组合多个不同的分类器进行预测。

- 硬投票（Hard voting）：预测多数投票
- 软投票（Soft voting）：预测基于预测概率的加权平均

```python
>>> from sklearn.ensemble import VotingClassifier
>>> eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')
>>> eclf.fit(X, y)
```

## 1.11.6. 堆叠泛化 {#stacked-generalization}

堆叠泛化（Stacking）使用一个元学习器来组合多个基学习器的预测。

```python
>>> from sklearn.ensemble import StackingClassifier
>>> estimators = [('rf', RandomForestClassifier()), ('svr', make_pipeline(StandardScaler(), SVC()))]
>>> clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
>>> clf.fit(X, y)
```

## 1.11.7. 极端随机树 {#extremely-randomized-trees}

极端随机树（ExtraTrees）与随机森林类似，但在选择拆分点时引入更多的随机性。

- [`ExtraTreesClassifier`](generated/sklearn.ensemble.ExtraTreesClassifier.html)
- [`ExtraTreesRegressor`](generated/sklearn.ensemble.ExtraTreesRegressor.html)

```python
>>> from sklearn.ensemble import ExtraTreesClassifier
>>> clf = ExtraTreesClassifier(n_estimators=100, random_state=0)
>>> clf.fit(X, y)
```

## 1.11.8. 直方图梯度提升 {#histogram-based-gradient-boosting}

直方图梯度提升是一种更快的梯度提升实现，特别适合大数据集。

- [`HistGradientBoostingClassifier`](generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
- [`HistGradientBoostingRegressor`](generated/sklearn.ensemble.HistGradientBoostingRegressor.html)

```python
>>> from sklearn.ensemble import HistGradientBoostingClassifier
>>> clf = HistGradientBoostingClassifier(max_iter=100).fit(X, y)
```

优点：
- 训练速度快
- 支持缺失值
- 支持分类特征（无需独热编码）
- 内置交叉验证（早停）
