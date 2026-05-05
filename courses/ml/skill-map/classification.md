# skill-map: classification — 分类算法（决策树、SVM、KNN、朴素贝叶斯、随机森林）

## 目标

掌握主流分类算法的原理、优缺点和适用场景，能用 sklearn 训练和评估分类模型。

## 必知概念

### 决策树（Decision Tree）
- **核心思想**：通过一系列条件判断（if-else）将数据分成不同类别
- **分裂准则**：
  - 信息增益（ID3）：选择使信息熵下降最多的特征
  - 基尼系数（CART）：Gini = 1 - sum(p_i^2)，越小越纯
- **剪枝**：防止过拟合，限制 max_depth、min_samples_split 等
- **优点**：可解释性强，不需要特征缩放
- **缺点**：容易过拟合，对噪声敏感
- **sklearn**：`DecisionTreeClassifier()`

### 支持向量机（SVM）
- **核心思想**：找到一个超平面，使两类数据之间的间隔最大
- **核技巧**：
  - linear：线性核，适合线性可分数据
  - RBF（高斯核）：适合非线性数据
  - poly：多项式核
- **关键参数**：C（正则化强度）、gamma（RBF 核宽度）
- **优点**：在高维空间表现好，适合小数据集
- **缺点**：大数据集训练慢，需要特征缩放
- **sklearn**：`SVC()`

### K 近邻（KNN）
- **核心思想**：新样本的类别由最近的 K 个邻居投票决定
- **距离度量**：欧氏距离、曼哈顿距离、余弦相似度
- **关键参数**：K 值（邻居数量）
- **优点**：简单直观，不需要训练过程
- **缺点**：预测慢（需要计算所有距离），对特征缩放敏感
- **sklearn**：`KNeighborsClassifier()`

### 朴素贝叶斯（Naive Bayes）
- **核心思想**：基于贝叶斯定理 + 条件独立假设
- **公式**：P(y|x) = P(x|y) * P(y) / P(x)
- **条件独立假设**：假设所有特征相互独立（"朴素"）
- **变种**：GaussianNB（连续特征）、MultinomialNB（文本特征）
- **优点**：训练极快，适合高维数据和文本分类
- **缺点**：条件独立假设往往不成立
- **sklearn**：`GaussianNB()`

### 随机森林（Random Forest）
- **核心思想**：多棵决策树的 Bagging 集成
- **随机性来源**：
  - 样本随机：每棵树用 Bootstrap 采样
  - 特征随机：每次分裂只考虑部分特征
- **OOB（Out-of-Bag）评估**：用未被采样的数据评估
- **特征重要性**：基于特征在所有树中的平均贡献
- **优点**：不容易过拟合，能评估特征重要性
- **缺点**：可解释性不如单棵决策树
- **sklearn**：`RandomForestClassifier()`

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `DecisionTreeClassifier()` | 决策树 | `model.fit(X, y)` |
| `SVC()` | 支持向量机 | `SVC(kernel='rbf', C=1.0)` |
| `KNeighborsClassifier()` | KNN | `KNeighborsClassifier(n_neighbors=5)` |
| `GaussianNB()` | 朴素贝叶斯 | `model.fit(X, y)` |
| `RandomForestClassifier()` | 随机森林 | `RandomForestClassifier(n_estimators=100)` |
| `plot_tree()` | 可视化决策树 | `plot_tree(model)` |
| `.feature_importances_` | 特征重要性 | `model.feature_importances_` |
| `classification_report()` | 分类报告 | `print(classification_report(y_test, y_pred))` |
| `confusion_matrix()` | 混淆矩阵 | `confusion_matrix(y_test, y_pred)` |

## 常见错误

1. **SVM/KNN 不做特征缩放**
   ```python
   # 错误：不同量纲的特征直接输入 SVM
   # 特征1: 年龄 (0-100)，特征2: 收入 (0-1000000)
   # 收入会完全主导距离计算

   # 正确：先标准化
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   ```

2. **KNN 的 K 值选择不当**
   ```python
   # K 太小：过拟合（只看最近的 1 个邻居）
   model = KNeighborsClassifier(n_neighbors=1)

   # K 太大：欠拟合
   model = KNeighborsClassifier(n_neighbors=100)

   # 应该用交叉验证选择
   ```

3. **随机森林忘记设置 n_estimators**
   ```python
   # 默认 100 棵树，可能不够
   model = RandomForestClassifier()  # 默认 n_estimators=100

   # 根据数据复杂度调整
   model = RandomForestClassifier(n_estimators=200)
   ```

## 训练阶梯

### Step 1: 决策树（Level 0→2）
- 理解信息增益和基尼系数
- 训练和可视化决策树
- 理解剪枝的作用

### Step 2: SVM（Level 2→3）
- 理解最大间隔原理
- 使用不同核函数
- 调节 C 和 gamma 参数

### Step 3: KNN（Level 3）
- 理解距离度量
- 选择 K 值
- 理解计算复杂度

### Step 4: 朴素贝叶斯（Level 3）
- 理解贝叶斯定理
- 应用于文本分类
- 理解条件独立假设

### Step 5: 随机森林（Level 3→4）
- 理解 Bagging 原理
- 获取特征重要性
- 与单棵决策树对比

### Step 6: 模型选择（Level 4→5）
- 根据数据特点选择算法
- 对比多种模型
- 调参优化

## 掌握标准

- **Level 3**: 能用 sklearn 训练各种分类模型，能解释各算法的原理
- **Level 4**: 能根据数据特点选择合适的算法，能调参优化
- **Level 5**: 能从零实现关键算法，能组合多个模型做集成

## 参考资料

- materials/noob/026_ml-decision-tree.md
- materials/noob/027_ml-svm.md
- materials/noob/028_ml-knn.md
- materials/noob/029_ml-ensemble-learning.md
- materials/noob/030_ml-naive-bayes.md
- materials/noob/031_ml-random-forest.md
- scikit-learn 分类文档：https://scikit-learn.org/stable/supervised_learning.html
