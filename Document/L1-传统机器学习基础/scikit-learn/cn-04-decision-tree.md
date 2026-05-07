# 1.10. 决策树 {#decision-trees}

**决策树（DTs）**是一种非参数监督学习方法，用于分类和回归。目标是创建一个模型，通过学习从数据特征推断出的简单决策规则来预测目标变量的值。树可以被视为分段常数近似。

决策树的优点：

- 易于理解和解释。树可以可视化。
- 需要很少的数据准备。其他技术通常需要数据标准化、创建虚拟变量和删除空白值。某些树和算法组合支持缺失值。
- 使用树的代价（即预测数据）与用于训练树的数据点数量成对数关系。
- 能够处理数值和分类数据。
- 能够处理多输出问题。
- 使用白盒模型。如果给定情况在模型中是可观察的，则可以用布尔逻辑轻松解释条件。
- 可以使用统计测试验证模型。

决策树的缺点：

- 决策树学习器可能创建过于复杂的树，不能很好地泛化数据。这称为过拟合。需要剪叶、设置叶节点所需的最小样本数或设置树的最大深度等机制来避免此问题。
- 决策树可能不稳定，因为数据中的微小变化可能导致生成完全不同的树。
- 决策树的预测既不平滑也不连续，而是分段常数近似。
- 学习最优决策树的问题在多个方面是 NP 完全的。

## 1.10.1. 分类 {#decision-tree-classification}

[`DecisionTreeClassifier`](<generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier> "sklearn.tree.DecisionTreeClassifier") 是能够在数据集上执行多类分类的类。

```python
>>> from sklearn import tree
>>> X = [[0, 0], [1, 1]]
>>> Y = [0, 1]
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, Y)
>>> clf.predict([[2., 2.]])
array([1])
>>> clf.predict_proba([[2., 2.]])
array([[0., 1.]])
```

使用 Iris 数据集，我们可以构建一棵树：

```python
>>> from sklearn.datasets import load_iris
>>> from sklearn import tree
>>> iris = load_iris()
>>> X, y = iris.data, iris.target
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(X, y)
>>> tree.plot_tree(clf)
```

可以使用 [`export_graphviz`](<generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz> "sklearn.tree.export_graphviz") 以 Graphviz 格式导出树。

## 1.10.2. 回归 {#decision-tree-regression}

[`DecisionTreeRegressor`](<generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor> "sklearn.tree.DecisionTreeRegressor") 用于回归任务。

```python
>>> from sklearn import tree
>>> X = [[0, 0], [2, 2]]
>>> y = [0.5, 2.5]
>>> clf = tree.DecisionTreeRegressor()
>>> clf = clf.fit(X, y)
>>> clf.predict([[1, 1]])
array([1.5])
```

## 1.10.3. 多输出问题 {#multi-output-problems}

多输出决策树支持在一次训练中预测多个输出变量。

## 1.10.4. 复杂度 {#decision-tree-complexity}

- 训练：\\(O(n \cdot m \cdot n \log(n))\\)（每个节点排序成本为 \\(O(n \log(n))\\)，共 \\(n\\) 个节点，\\(m\\) 个特征）
- 预测：\\(O(\text{树的深度})\\)

## 1.10.5. 实用参数 {#decision-tree-parameters}

| 参数 | 描述 | 建议 |
|------|------|------|
| `max_depth` | 树的最大深度 | 控制过拟合，建议从 3-10 开始 |
| `min_samples_split` | 拆分内部节点所需的最小样本数 | 增大可减少过拟合 |
| `min_samples_leaf` | 叶节点所需的最小样本数 | 增大可减少过拟合 |
| `max_features` | 寻找最佳拆分时考虑的特征数量 | 适合高维数据 |
| `criterion` | 拆分质量度量 | `'gini'`（默认）或 `'entropy'`（分类）；`'squared_error'`（回归） |

## 1.10.6. 特征重要性 {#decision-tree-feature-importance}

决策树提供特征重要性，衡量每个特征对预测的贡献：

```python
>>> clf.feature_importances_
array([0.        , 0.02666667, 0.41666667, 0.55666667])
```

## 1.10.7. 决策树算法 {#decision-tree-algorithms}

scikit-learn 中的决策树使用 CART（分类和回归树）算法的优化版本，使用以下标准之一进行拆分：

- **分类**：Gini 不纯度（`gini`）或信息增益（`entropy`）
- **回归**：均方误差（`squared_error`）、均方对数误差（`friedman_mse`）、绝对误差（`absolute_error`）或 Poisson 偏差（`poisson`）
