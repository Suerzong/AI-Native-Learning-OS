# exercises.md — 机器学习练习库

## 练习模板

每个练习包含以下字段：

```
## 练习 [编号]: [标题]
- **目标技能**: [skill-map 中的技能]
- **难度**: Level [0-5]
- **类型**: 识别 / 解释 / 修改 / 编写 / 调试 / 迁移
- **题目**: [具体要求]
- **成功标准**: [可衡量的完成条件]
- **常见错误**: [该练习容易犯的错误]
```

---

## Layer 1: ML 基础与数据准备

### 练习 001: 数据探索与基本信息提取

- **目标技能**: data-preparation — 数据理解与 EDA
- **难度**: Level 1
- **类型**: 编写
- **题目**:
  给定一个 CSV 数据集 `housing.csv`（包含列：price, area, bedrooms, bathrooms, stories, parking），
  编写代码完成以下任务：
  1. 读取 CSV 文件并显示前 5 行
  2. 显示数据的基本信息（列名、非空数量、数据类型）
  3. 计算每列的均值、标准差、最小值、最大值
  4. 检查每列缺失值的数量

- **成功标准**:
  - 使用 `pd.read_csv()` 读取数据
  - 使用 `.head()` 显示前 5 行
  - 使用 `.info()` 显示基本信息
  - 使用 `.describe()` 显示统计摘要
  - 使用 `.isnull().sum()` 统计缺失值

- **常见错误**:
  - 混淆 `.info()` 和 `.describe()` 的作用
  - 忘记检查缺失值
  - 直接打印整个 DataFrame 导致输出过长

---

### 练习 002: 数据清洗 — 缺失值与异常值处理

- **目标技能**: data-preparation — 数据清洗
- **难度**: Level 2
- **类型**: 编写
- **题目**:
  给定以下数据：
  ```python
  import pandas as pd
  import numpy as np
  data = pd.DataFrame({
      'age': [25, 30, np.nan, 45, 200, 28, 35, np.nan, 40, 22],
      'salary': [5000, 8000, 6000, np.nan, 7000, 5500, 9000, 6500, np.nan, 4800],
      'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'M']
  })
  ```
  完成以下任务：
  1. 统计每列缺失值数量
  2. 用中位数填充 `age` 列的缺失值
  3. 用均值填充 `salary` 列的缺失值
  4. 用 IQR 方法检测并删除 `age` 列的异常值（< Q1-1.5*IQR 或 > Q3+1.5*IQR）

- **成功标准**:
  - 使用 `.fillna()` 填充缺失值
  - 使用 `df['age'].median()` 获取中位数
  - 正确计算 IQR（Q3 - Q1）
  - 使用布尔索引过滤异常值
  - 最终 DataFrame 无缺失值且 age 列无异常值

- **常见错误**:
  - 忘记 `inplace=True` 或重新赋值
  - IQR 计算时混淆 Q1 和 Q3
  - 填充前忘记检查数据分布

---

### 练习 003: 特征编码与缩放

- **目标技能**: data-preparation — 特征工程
- **难度**: Level 2
- **类型**: 编写
- **题目**:
  给定以下数据：
  ```python
  data = pd.DataFrame({
      'city': ['北京', '上海', '北京', '广州', '上海', '广州'],
      'education': ['本科', '硕士', '博士', '本科', '硕士', '本科'],
      'experience': [1, 3, 5, 2, 4, 1],
      'salary': [8000, 15000, 25000, 10000, 18000, 7500]
  })
  ```
  完成以下任务：
  1. 对 `city` 列进行独热编码（One-Hot Encoding）
  2. 对 `education` 列进行标签编码（Label Encoding），本科=0，硕士=1，博士=2
  3. 对 `experience` 列进行标准化（StandardScaler）
  4. 对 `salary` 列进行归一化（MinMaxScaler）

- **成功标准**:
  - 使用 `pd.get_dummies()` 或 `OneHotEncoder` 进行独热编码
  - 使用 `LabelEncoder` 或自定义映射进行标签编码
  - 使用 `StandardScaler` 标准化（均值 0，标准差 1）
  - 使用 `MinMaxScaler` 归一化（范围 0-1）
  - 理解 fit_transform 和 transform 的区别

- **常见错误**:
  - 独热编码时忘记 `drop_first=True` 导致多重共线性
  - 标签编码的顺序与期望不符
  - 在整个数据集上 fit 而非仅在训练集上 fit（数据泄漏）

---

### 练习 004: 训练集划分与数据可视化

- **目标技能**: data-preparation — 数据划分与可视化
- **难度**: Level 2
- **类型**: 编写
- **题目**:
  使用 sklearn 的 `make_classification` 生成一个二分类数据集（200 个样本，2 个特征，2 个类别），
  完成以下任务：
  1. 将数据按 80/20 划分为训练集和测试集（random_state=42）
  2. 绘制训练集的散点图，用不同颜色区分两个类别
  3. 绘制两个特征各自的直方图
  4. 打印训练集和测试集的样本数量

- **成功标准**:
  - 使用 `train_test_split(test_size=0.2, random_state=42)`
  - 使用 `matplotlib.pyplot.scatter()` 绘制散点图
  - 使用 `c=y_train` 参数区分颜色
  - 使用 `plt.hist()` 绘制直方图
  - 图表有标题和坐标轴标签

- **常见错误**:
  - 忘记设置 `random_state` 导致结果不可复现
  - 散点图的 x, y 参数传错
  - 忘记 plt.show() 导致图像不显示

---

## Layer 2: 经典算法

### 练习 005: 线性回归建模与评估

- **目标技能**: regression — 线性回归
- **难度**: Level 2
- **类型**: 编写
- **题目**:
  使用 sklearn 生成一个简单的线性回归数据集（`make_regression`，100 个样本，1 个特征，噪声=10），
  完成以下任务：
  1. 划分训练/测试集（80/20，random_state=42）
  2. 训练一个线性回归模型
  3. 打印模型的系数和截距
  4. 在测试集上预测并计算 MSE 和 R²
  5. 绘制散点图和回归线

- **成功标准**:
  - 使用 `LinearRegression()` 训练模型
  - 使用 `.coef_` 和 `.intercept_` 获取参数
  - 使用 `mean_squared_error()` 和 `r2_score()` 评估
  - 绘制训练数据散点图和回归线（红色）
  - R² > 0.7

- **常见错误**:
  - 忘记 reshape 一维数据（需要二维输入）
  - 在测试集上 fit 模型（应该只在训练集上 fit）
  - 评估指标函数的参数顺序弄反

---

### 练习 006: 逻辑回归与决策边界可视化

- **目标技能**: regression — 逻辑回归
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 `make_classification` 生成二分类数据集（100 个样本，2 个特征，无冗余特征），
  完成以下任务：
  1. 训练一个逻辑回归模型
  2. 打印模型在测试集上的准确率
  3. 绘制决策边界（使用 meshgrid 和 contourf）
  4. 在决策边界图上叠加测试数据点

- **成功标准**:
  - 使用 `LogisticRegression()` 训练
  - 使用 `.predict_proba()` 计算网格上每点的概率
  - 使用 `np.meshgrid()` 创建网格
  - 使用 `plt.contourf()` 绘制决策区域
  - 准确率 > 0.75

- **常见错误**:
  - meshgrid 的范围没有包含所有数据点
  - contourf 的 Z 数组维度与 meshgrid 不匹配
  - 决策边界的颜色含义搞反

---

### 练习 007: 决策树与特征重要性

- **目标技能**: classification — 决策树
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 sklearn 的 `load_iris()` 数据集，完成以下任务：
  1. 训练一个决策树分类器（max_depth=3）
  2. 打印分类报告（precision、recall、f1-score）
  3. 获取并排序特征重要性
  4. 使用 `plot_tree` 可视化决策树
  5. 尝试 max_depth=10，观察是否过拟合（比较训练和测试准确率）

- **成功标准**:
  - 使用 `DecisionTreeClassifier(max_depth=3)`
  - 使用 `classification_report()` 输出评估
  - 使用 `.feature_importances_` 获取重要性
  - 使用 `plot_tree()` 可视化
  - 能解释 max_depth=10 时训练准确率 >> 测试准确率的现象

- **常见错误**:
  - 没有划分训练/测试集就评估
  - 特征重要性没有与特征名对应
  - 不理解 max_depth 对过拟合的影响

---

### 练习 008: SVM 核函数对比

- **目标技能**: classification — SVM
- **难度**: Level 3
- **类型**: 修改
- **题目**:
  以下代码使用线性核的 SVM 对 `make_circles` 数据集进行分类（准确率很低）。
  请修改代码，分别使用 RBF 核和多项式核，比较三者的准确率和决策边界差异。
  ```python
  from sklearn.svm import SVC
  from sklearn.datasets import make_circles
  X, y = make_circles(n_samples=200, noise=0.1, factor=0.5, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  model = SVC(kernel='linear')
  model.fit(X_train, y_train)
  print(f"线性核准确率: {model.score(X_test, y_test):.3f}")
  ```

- **成功标准**:
  - 将 kernel 改为 'rbf' 和 'poly'
  - 比较三种核的测试准确率
  - 能解释为什么线性核在环形数据上表现差
  - 能解释 RBF 核为何适合非线性可分数据

- **常见错误**:
  - 忘记重新 fit 模型
  - 不理解核函数的作用
  - 混淆 kernel 参数的取值

---

### 练习 009: 随机森林与模型评估

- **目标技能**: classification — 随机森林
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 `load_breast_cancer()` 数据集（乳腺癌分类），完成以下任务：
  1. 训练一个随机森林分类器（n_estimators=100, random_state=42）
  2. 输出混淆矩阵
  3. 绘制 ROC 曲线并计算 AUC 值
  4. 显示前 10 个最重要的特征
  5. 比较随机森林与单棵决策树的性能差异

- **成功标准**:
  - 使用 `RandomForestClassifier(n_estimators=100)`
  - 使用 `confusion_matrix()` 输出混淆矩阵
  - 使用 `roc_curve()` 和 `auc()` 绘制 ROC 曲线
  - 使用 `.feature_importances_` 排序并绘制条形图
  - 随机森林的 AUC > 单棵决策树的 AUC

- **常见错误**:
  - 混淆矩阵的行列含义搞反
  - ROC 曲线需要概率预测而非类别预测
  - 特征重要性排序时忘记对应特征名

---

## Layer 3: 进阶主题

### 练习 010: K-Means 聚类与肘部法则

- **目标技能**: clustering — K-Means
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 `make_blobs` 生成 300 个样本的聚类数据（4 个中心，random_state=42），
  完成以下任务：
  1. 用 K=2 到 K=10 分别训练 K-Means，记录每个 K 的 inertia（惯性）
  2. 绘制肘部法则曲线（X 轴=K，Y 轴=inertia）
  3. 计算 K=2 到 K=10 的轮廓系数
  4. 选择最优 K，绘制聚类结果（用不同颜色表示不同簇，用 X 标记质心）

- **成功标准**:
  - 使用 `KMeans(n_clusters=k)` 训练
  - 使用 `.inertia_` 获取惯性值
  - 使用 `silhouette_score()` 计算轮廓系数
  - 肘部法则曲线能看出拐点
  - 最优 K 选择合理（接近真实中心数）

- **常见错误**:
  - 惯性和轮廓系数混淆
  - 忘记在聚类结果上（而非原始标签上）计算轮廓系数
  - 质心坐标获取方式错误

---

### 练习 011: PCA 降维与可视化

- **目标技能**: dimensionality-reduction — PCA
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 `load_digits()` 数据集（手写数字，64 维特征），完成以下任务：
  1. 使用 PCA 将数据降到 2 维
  2. 绘制 2D 散点图，用不同颜色标记 0-9 十个数字
  3. 打印前两个主成分的方差贡献率
  4. 将数据降到不同维度（2, 10, 30, 50），用随机森林分类，比较准确率

- **成功标准**:
  - 使用 `PCA(n_components=2)` 降维
  - 使用 `.explained_variance_ratio_` 获取方差贡献率
  - 散点图颜色区分清晰，有图例
  - 能解释方差贡献率的含义
  - 不同维度下准确率的变化趋势合理

- **常见错误**:
  - PCA 前忘记标准化（不同量纲的特征对 PCA 结果影响大）
  - 混淆 `n_components` 的含义
  - 降维后忘记保留足够的信息

---

### 练习 012: Q-Learning 网格世界

- **目标技能**: reinforcement-learning — Q-Learning
- **难度**: Level 4
- **类型**: 编写
- **题目**:
  实现一个 4x4 网格世界的 Q-Learning 算法：
  - 状态：16 个格子（0-15）
  - 动作：上下左右（0-3）
  - 奖励：到达目标（格子 15）+10，其他 -1
  - 要求：
    1. 初始化 Q-Table（16x4 的零矩阵）
    2. 实现 Epsilon-Greedy 策略（epsilon=0.1）
    3. 训练 1000 个 episode（alpha=0.1, gamma=0.99）
    4. 打印最终的 Q-Table
    5. 输出从格子 0 到格子 15 的最优路径

- **成功标准**:
  - Q-Table 维度正确（16x4）
  - Epsilon-Greedy 实现正确（探索 vs 利用）
  - Q 值更新公式正确：Q(s,a) = Q(s,a) + alpha * [r + gamma * max(Q(s',a')) - Q(s,a)]
  - 能找到从起点到终点的路径
  - Q-Table 中目标状态附近的值较高

- **常见错误**:
  - Q 值更新公式写错（特别是 gamma 项）
  - 边界处理错误（在边缘格子向上/下会越界）
  - 没有处理终止状态
  - epsilon 衰减逻辑错误

---

### 练习 013: 交叉验证与正则化

- **目标技能**: model-evaluation — 交叉验证
- **难度**: Level 3
- **类型**: 编写
- **题目**:
  使用 `make_regression` 生成一个带噪声的回归数据集（500 个样本，20 个特征，其中 5 个有效特征），
  完成以下任务：
  1. 分别用线性回归、Ridge（alpha=1.0）、Lasso（alpha=1.0）训练模型
  2. 对每个模型进行 5 折交叉验证，打印平均分和标准差
  3. 比较 Lasso 的系数，看哪些特征被压缩为 0（特征选择效果）
  4. 用不同 alpha 值（0.01, 0.1, 1.0, 10.0）训练 Ridge，比较交叉验证分数

- **成功标准**:
  - 使用 `cross_val_score(model, X, y, cv=5)`
  - 使用 `Ridge(alpha=1.0)` 和 `Lasso(alpha=1.0)`
  - 正确解释交叉验证分数的均值和标准差
  - 能识别 Lasso 的稀疏解（系数为 0 的特征）
  - alpha 对模型性能的影响趋势合理

- **常见错误**:
  - 交叉验证的 cv 参数不理解
  - Lasso 的 alpha 过大导致所有系数为 0
  - 忘记在交叉验证前进行数据预处理

---

### 练习 014: 数据泄漏检测与修复

- **目标技能**: model-optimization — 数据泄漏
- **难度**: Level 4
- **类型**: 调试
- **题目**:
  以下代码存在数据泄漏问题。请找出所有泄漏点并修复：
  ```python
  import pandas as pd
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import LogisticRegression
  from sklearn.feature_selection import SelectKBest, f_classif

  # 读取数据
  df = pd.read_csv('data.csv')
  X = df.drop('target', axis=1)
  y = df['target']

  # 特征选择
  selector = SelectKBest(f_classif, k=10)
  X_selected = selector.fit_transform(X, y)

  # 标准化
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X_selected)

  # 划分数据
  X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

  # 训练模型
  model = LogisticRegression()
  model.fit(X_train, y_train)
  print(f"准确率: {model.score(X_test, y_test):.3f}")
  ```

- **成功标准**:
  - 识别出 2 处数据泄漏：特征选择和标准化都在划分之前
  - 将 train_test_split 移到最前面
  - 特征选择和标准化都在训练集上 fit，在测试集上 transform
  - 或使用 Pipeline 封装所有步骤
  - 修复后准确率可能降低但更真实

- **常见错误**:
  - 只修复了部分泄漏
  - 修复后忘记在测试集上用 transform 而非 fit_transform
  - 不理解为什么准确率修复后会降低

---

## Layer 4: 工程应用

### 练习 015: Pipeline 构建与模型保存

- **目标技能**: model-optimization — MLOps
- **难度**: Level 4
- **类型**: 编写
- **题目**:
  使用 `load_wine()` 数据集，完成以下任务：
  1. 构建一个 Pipeline，包含：StandardScaler → PCA(n_components=5) → SVC(kernel='rbf')
  2. 使用 GridSearchCV 搜索最优参数（PCA 的 n_components ∈ {3,5,7}，SVC 的 C ∈ {0.1,1,10}，gamma ∈ {'scale','auto'}）
  3. 打印最优参数和最优分数
  4. 用 joblib 保存最优模型
  5. 加载模型并对新数据进行预测

- **成功标准**:
  - 使用 `Pipeline()` 正确组合步骤
  - 使用 `GridSearchCV(pipe, param_grid, cv=5)` 搜索
  - 搜索参数使用 `estimator__参数名` 格式（如 `svc__C`）
  - 使用 `joblib.dump()` 和 `joblib.load()` 保存/加载
  - 加载后能正确预测

- **常见错误**:
  - GridSearchCV 的参数名格式错误（应该用双下划线）
  - 忘记 Pipeline 中各步骤的命名
  - 保存路径不存在

---

### 练习 016: Titanic 完整流程

- **目标技能**: model-evaluation — 端到端分类项目
- **难度**: Level 4
- **类型**: 编写
- **题目**:
  完成 Titanic 生存预测的完整流程（使用 sklearn 或 pandas）：
  1. 数据探索：查看缺失值、数据分布、特征类型
  2. 数据清洗：处理 Age、Cabin、Embarked 的缺失值
  3. 特征工程：
     - 从 Name 中提取头衔（Mr, Mrs, Miss 等）
     - 对 Sex、Embarked 进行编码
     - 创建 FamilySize = SibSp + Parch + 1
     - 对 Fare 进行对数变换
  4. 特征选择：选择对生存预测有用的特征
  5. 模型训练：使用随机森林，5 折交叉验证
  6. 评估：输出混淆矩阵、分类报告、ROC-AUC
  7. 特征重要性排序

- **成功标准**:
  - 缺失值处理合理（Age 用中位数，Embarked 用众数）
  - 特征工程至少包含 3 个新特征
  - 交叉验证分数 > 0.75
  - 分类报告完整输出
  - 特征重要性排序可视化

- **常见错误**:
  - 处理 Cabin 缺失值时丢弃了太多数据
  - 特征工程后忘记删除原始无用特征
  - 交叉验证时包含了测试集信息

---

### 练习 017: 超参数调优对比

- **目标技能**: model-optimization — 超参数搜索
- **难度**: Level 4
- **类型**: 编写
- **题目**:
  使用 `load_digits()` 数据集，对比三种超参数搜索方法：
  1. GridSearchCV：搜索 SVC 的 C ∈ {0.1, 1, 10}，gamma ∈ {0.01, 0.1, 1}
  2. RandomizedSearchCV：搜索同样的参数空间，但只尝试 10 组组合
  3. 比较两者的最优分数、最优参数和运行时间
  4. 用 `time.time()` 测量运行时间

- **成功标准**:
  - GridSearchCV 和 RandomizedSearchCV 都正确实现
  - 使用 `time.time()` 测量并打印运行时间
  - 能解释为什么 RandomizedSearchCV 更快
  - 输出两者的最优参数和分数对比

- **常见错误**:
  - RandomizedSearchCV 的 `n_iter` 参数设置不合理
  - 时间测量代码位置错误
  - 参数网格定义格式不正确

---

### 练习 018: 模型对比与选型报告

- **目标技能**: model-evaluation — 模型选择
- **难度**: Level 5
- **类型**: 迁移
- **题目**:
  给定一个二分类数据集（可用 `make_classification` 生成，1000 个样本，20 个特征），
  你需要完成一个模型选型报告：
  1. 对比至少 5 种分类器（Logistic Regression, Decision Tree, Random Forest, SVM, KNN）
  2. 对每种分类器进行 5 折交叉验证，记录均值和标准差
  3. 绘制箱线图对比各模型的交叉验证分数分布
  4. 对最优模型进行超参数调优
  5. 输出最终推荐模型及理由（从准确率、速度、可解释性三个维度分析）
  6. 讨论该模型部署到嵌入式设备的可行性

- **成功标准**:
  - 至少 5 种模型对比完成
  - 箱线图绘制正确，有标题和标签
  - 超参数调优使用 GridSearchCV 或 RandomizedSearchCV
  - 推荐理由从三个维度展开
  - 嵌入式部署讨论合理（考虑模型大小、推理速度、内存占用）

- **常见错误**:
  - 只比较准确率忽略标准差
  - 推荐理由过于笼统
  - 忽略模型的计算复杂度
  - 没有考虑嵌入式设备的资源限制

---
