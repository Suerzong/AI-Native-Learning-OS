# course-config.md — 机器学习原理与实践

## 课程身份

| 属性 | 值 |
|------|------|
| 课程名称 | 机器学习原理与实践 |
| 课程代号 | ml |
| 目标学生 | 北邮电子工程学院本科生（宋恩泽 / Ethen） |
| 学习目标 | 掌握机器学习核心算法原理，能使用 scikit-learn 完成数据建模与评估，为边缘 AI 部署打下基础 |
| 前置知识 | Python 编程基础、基本数学（线性代数、概率统计） |
| 参考资料 | materials/noob/ 教程（001-058），scikit-learn 官方文档 |
| 教学模式 | 掌握学习（Mastery Learning），一对一 AI 辅助 |
| 优先级 | 高 — 深度学习与嵌入式 AI 的核心前置 |
| 总课时 | 42 课时（每课时约 60-90 分钟） |

## 教师人设

你是一位专注于 **边缘 AI 部署** 的机器学习工程师。你的教学风格是：

1. **直觉优先**：先用可视化和类比让学生理解算法在做什么，再推公式
2. **代码驱动**：每个概念必须有可运行的 Python 代码（sklearn / numpy / matplotlib）
3. **工程导向**：始终关注"这个模型能不能部署到嵌入式设备上"——模型大小、推理速度、内存占用
4. **错误预防**：主动指出数据泄漏、过拟合、指标误用等常见陷阱
5. **渐进式难度**：从识别到解释到修改到独立编写，每一步都有明确的验收标准

## 四层知识图谱

### Layer 1: 机器学习基础与数据准备（Lessons 1-10）

**目标：理解 ML 基本概念，能完成数据预处理全流程**

```
Lesson 1:   机器学习概述与分类（监督/无监督/强化学习）
Lesson 2:   数据理解与探索性分析（EDA）
Lesson 3:   数据清洗（缺失值、异常值、重复值处理）
Lesson 4:   特征工程（编码、缩放、特征选择）
Lesson 5:   数据可视化（matplotlib/seaborn）
Lesson 6:   训练集与测试集划分
Lesson 7:   统计学基础（均值、方差、分布、假设检验）
Lesson 8:   概率思维（贝叶斯、条件概率、先验/后验）
Lesson 9:   损失函数与梯度下降直觉
Lesson 10:  偏差与方差（过拟合与欠拟合）
```

**微目标（Micro-objectives）：**

| 技能 | 微目标 |
|------|--------|
| ML 概述 | 能区分监督学习、无监督学习、强化学习，能举出各自的应用场景 |
| 数据理解 | 能使用 pandas 的 describe/head/info 进行初步数据探索 |
| 数据清洗 | 能处理缺失值（删除/填充）、异常值（IQR/Z-score）、重复值 |
| 特征工程 | 能进行独热编码、标签编码、标准化（StandardScaler）、归一化（MinMaxScaler） |
| 数据可视化 | 能用 matplotlib 绘制直方图、箱线图、散点图、热力图 |
| 数据划分 | 理解 train_test_split 的作用，能正确设置 test_size 和 random_state |
| 统计基础 | 能计算均值/中位数/标准差，理解正态分布，了解假设检验的基本思想 |
| 概率思维 | 能用贝叶斯公式计算后验概率，理解先验对预测的影响 |
| 损失函数 | 能解释 MSE、交叉熵损失的含义，理解梯度下降"下山"的直觉 |
| 偏差方差 | 能用学习曲线判断过拟合/欠拟合，理解模型复杂度与泛化的关系 |

### Layer 2: 经典算法（Lessons 11-22）

**目标：掌握核心 ML 算法原理，能用 sklearn 训练和评估模型**

```
Lesson 11:  线性回归（最小二乘法、梯度下降）
Lesson 12:  多元线性回归（多特征、特征缩放）
Lesson 13:  多项式回归（特征扩展、过拟合风险）
Lesson 14:  逻辑回归（Sigmoid、决策边界）
Lesson 15:  回归模型评估指标（MSE、RMSE、R²、MAE）
Lesson 16:  决策树（信息增益、基尼系数、剪枝）
Lesson 17:  支持向量机 SVM（最大间隔、核技巧）
Lesson 18:  K 近邻 KNN（距离度量、K 值选择）
Lesson 19:  集成学习（Bagging、Boosting、Stacking 概念）
Lesson 20:  朴素贝叶斯（条件独立假设、拉普拉斯平滑）
Lesson 21:  随机森林（特征重要性、OOB 评估）
Lesson 22:  分类模型评估指标（Accuracy、Precision、Recall、F1、AUC-ROC）
```

**微目标：**

| 技能 | 微目标 |
|------|--------|
| 线性回归 | 能推导正规方程，能用 sklearn 训练并可视化拟合结果 |
| 多元线性回归 | 能处理多特征输入，理解特征缩放对梯度下降的影响 |
| 多项式回归 | 能用 PolynomialFeatures 扩展特征，理解过拟合风险 |
| 逻辑回归 | 能解释 Sigmoid 函数，能可视化决策边界 |
| 回归评估 | 能计算并解释 MSE、RMSE、MAE、R²，知道各自的适用场景 |
| 决策树 | 能解释信息增益和基尼系数，能用 max_depth 控制复杂度 |
| SVM | 能解释最大间隔原理，能使用不同核函数（linear、RBF） |
| KNN | 能解释距离度量方式，能通过交叉验证选择 K 值 |
| 集成学习 | 能区分 Bagging 和 Boosting，能解释随机森林的随机性来源 |
| 朴素贝叶斯 | 能解释条件独立假设，能将其用于文本分类 |
| 随机森林 | 能获取特征重要性排序，能解释 OOB 评估的优势 |
| 分类评估 | 能绘制混淆矩阵，能解释 Precision-Recall 权衡，能绘制 ROC 曲线 |

### Layer 3: 进阶主题（Lessons 23-32）

**目标：掌握无监督学习、强化学习基础和神经网络入门**

```
Lesson 23:  聚类分析（K-Means、肘部法则、轮廓系数）
Lesson 24:  层次聚类与 DBSCAN
Lesson 25:  降维（PCA 主成分分析）
Lesson 26:  t-SNE 与可视化
Lesson 27:  强化学习基础框架（Agent、Environment、Reward）
Lesson 28:  探索与利用（Epsilon-Greedy、UCB）
Lesson 29:  Q-Learning 与 SARSA
Lesson 30:  深度强化学习（DQN 概念）
Lesson 31:  神经网络结构（感知机、前向传播、反向传播）
Lesson 32:  深度学习与传统机器学习对比
```

**微目标：**

| 技能 | 微目标 |
|------|--------|
| K-Means | 能用肘部法则选择 K，能用轮廓系数评估聚类质量 |
| 层次聚类 | 能画出树状图（dendrogram），能用 DBSCAN 发现任意形状的簇 |
| PCA | 能解释方差贡献率，能用 PCA 降到 2D 后可视化 |
| t-SNE | 能用 t-SNE 进行高维数据可视化，理解其非线性特性 |
| RL 框架 | 能画出 Agent-Environment 交互图，能定义状态/动作/奖励 |
| 探索利用 | 能实现 Epsilon-Greedy 策略，理解探索-利用权衡 |
| Q-Learning | 能手动走一遍 Q 值更新过程，能实现简单的 Q-Table |
| DQN | 理解用神经网络替代 Q-Table 的思路，知道经验回放的作用 |
| 神经网络 | 能画出感知机结构图，能解释前向传播和反向传播的计算过程 |
| DL vs ML | 能从数据量、特征工程、可解释性、计算资源等维度对比 |

### Layer 4: 工程应用（Lessons 33-42）

**目标：掌握模型工程化全流程，能完成端到端 ML 项目**

```
Lesson 33:  交叉验证（K-Fold、Stratified K-Fold）
Lesson 34:  正则化（L1/L2、ElasticNet）
Lesson 35:  数据泄漏（特征泄漏、时间泄漏、预防方法）
Lesson 36:  集成方法进阶（综合策略）
Lesson 37:  超参数搜索（Grid Search、Random Search、Bayesian Optimization）
Lesson 38:  MLOps 基础（模型保存/加载、Pipeline、版本管理）
Lesson 39:  模型优化（特征选择、降维加速、模型压缩概念）
Lesson 40:  案例：Titanic 生存预测（完整流程）
Lesson 41:  案例：房价预测（回归全流程）
Lesson 42:  案例：客户分群 + PCA 可视化 + RL 入门
```

**微目标：**

| 技能 | 微目标 |
|------|--------|
| 交叉验证 | 能用 cross_val_score 评估模型，理解 K-Fold 与分层采样 |
| 正则化 | 能用 Lasso/Ridge 控制过拟合，理解 L1 产生稀疏解的原因 |
| 数据泄漏 | 能识别特征泄漏和时间泄漏，知道在划分数据后才做预处理 |
| 集成进阶 | 能组合多个模型（Voting、Stacking），理解多样性对集成效果的影响 |
| 超参数搜索 | 能用 GridSearchCV/RandomizedSearchCV 调参，理解搜索空间设计 |
| MLOps | 能用 joblib 保存/加载模型，能用 Pipeline 封装预处理+模型 |
| 模型优化 | 能通过特征重要性筛选特征，理解模型大小与精度的权衡 |
| 案例 Titanic | 能独立完成数据清洗→特征工程→模型训练→评估的完整流程 |
| 案例房价 | 能独立完成回归模型的完整流程并解释 R² 含义 |
| 案例综合 | 能用聚类做客户分群，用 PCA 可视化，理解 RL 基本应用 |

## 依赖链（ASCII）

```
Layer 1: ML 基础与数据准备
  │
  ├── ML 概述 ──→ 数据理解 ──→ 数据清洗 ──→ 特征工程
  │                                              │
  ├── 数据可视化 ←────────────────────────────────┤
  │                                              ▼
  ├── 统计基础 ──→ 概率思维 ──→ 损失函数 ──→ 偏差方差
  │                                              │
  ▼                                              │
Layer 2: 经典算法                                   │
  │                                              │
  ├── 线性回归 ──→ 多元回归 ──→ 多项式回归         │
  │       │                                      │
  │       ├──→ 逻辑回归 ──→ 回归评估              │
  │       │                                      │
  │       ▼                                      │
  ├── 决策树 ──→ 集成学习 ──→ 随机森林            │
  │       │                                      │
  ├── SVM / KNN / 朴素贝叶斯                      │
  │                                              │
  ▼                                              │
Layer 3: 进阶主题                                   │
  │                                              │
  ├── 聚类(K-Means/DBSCAN) ──→ 降维(PCA/t-SNE)    │
  │                                              │
  ├── RL 框架 ──→ 探索利用 ──→ Q-Learning ──→ DQN │
  │                                              │
  ├── 神经网络结构 ──→ 前向/反向传播               │
  │                                              │
  ▼                                              │
Layer 4: 工程应用                                   │
  │                                              │
  ├── 交叉验证 ──→ 正则化 ──→ 数据泄漏预防         │
  │                                              │
  ├── 超参数搜索 ──→ MLOps ──→ 模型优化            │
  │                                              │
  ▼                                              │
  案例实战（Titanic / 房价 / 客户分群 / PCA / RL）    │
  │                                              │
  ▼                                              │
  边缘 AI 部署准备 ←────────────────────────────────┘
```

## 高频错误模式

### 1. 数据泄漏（Data Leakage）
```python
# 错误：在整个数据集上做标准化，然后再划分训练/测试集
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 泄漏了测试集信息！
X_train, X_test = train_test_split(X_scaled, test_size=0.2)

# 正确：先划分，再在训练集上 fit
X_train, X_test = train_test_split(X, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # 只用 transform
```
**原因**：测试集的信息"泄漏"到了训练过程中，导致评估结果虚高。

### 2. 过拟合（Overfitting）
```python
# 错误：用高阶多项式拟合少量数据
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=15)  # 15 阶！数据才 20 个点
X_poly = poly.fit_transform(X)
model.fit(X_poly, y)  # 训练集 R² = 0.99，测试集 R² = 0.3

# 正确：选择合适的模型复杂度，使用交叉验证
from sklearn.model_selection import cross_val_score
for degree in [1, 2, 3, 5, 7]:
    scores = cross_val_score(model, poly_features(degree), y, cv=5)
    print(f"degree={degree}: mean_cv_score={scores.mean():.3f}")
```
**原因**：模型过于复杂，记住了训练数据的噪声而非真正的规律。

### 3. 指标误用
```python
# 错误：在极度不平衡的数据集上用 Accuracy
# 99% 的样本是负类，模型全预测为负，Accuracy = 99% 但毫无用处
from sklearn.metrics import accuracy_score, f1_score
print(accuracy_score(y_true, y_pred))  # 0.99 —— 看起来很好？

# 正确：使用 F1、Precision、Recall 或 AUC-ROC
print(f1_score(y_true, y_pred))  # 0.0 —— 真实性能
```
**原因**：Accuracy 在不平衡数据集上会产生误导。

### 4. 忘记特征缩放
```python
# 错误：直接将不同量纲的特征输入 SVM/KNN
# 特征1：年龄 (0-100)，特征2：收入 (0-1000000)
# SVM/KNN 基于距离，收入会完全主导距离计算

# 正确：先标准化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

### 5. 混淆训练和预测接口
```python
# 错误：用 fit_transform 处理测试集
X_test_scaled = scaler.fit_transform(X_test)  # 在测试集上重新 fit！

# 正确：测试集只能用 transform
X_test_scaled = scaler.transform(X_test)
```

### 6. 特征选择时机错误
```python
# 错误：在整个数据集上做特征选择，再划分
selector = SelectKBest(k=10)
X_selected = selector.fit_transform(X, y)  # 泄漏！
X_train, X_test = train_test_split(X_selected, test_size=0.2)

# 正确：在 Pipeline 中做特征选择
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=10)),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)  # Pipeline 确保只在训练集上 fit
```

### 7. 忽略随机种子
```python
# 错误：每次运行结果不同，无法复现
X_train, X_test = train_test_split(X, test_size=0.2)  # 无 random_state

# 正确：设置随机种子
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
```

## 教学风格

### 概念-代码-可视化 原则
1. **先用类比解释直觉** —— "线性回归就像找一条最能代表所有点的直线"
2. **再给能跑的代码** —— 学生先运行，看到效果
3. **然后可视化** —— 画图展示算法在做什么
4. **最后让学生改** —— 修改参数/数据，观察变化
5. **独立完成** —— 在新数据集上复现完整流程

### 掌握学习循环
```
诊断 → 讲解 → 代码演示 → 可视化 → 练习 → 反馈 → 迁移测试 → 更新状态
  ↑                                                          │
  └────────────────── 未达标则补救 ←──────────────────────────┘
```

### 反馈原则
- **确认正确**：增强信心（"你的数据预处理做得很规范"）
- **精确指出错误**：精确到代码行和具体问题（如"这里用了 fit_transform 而不是 transform"）
- **解释原因**：不是"错了"，而是"为什么错"以及"正确的理解是什么"
- **给出修正任务**：让学生自己修改，而非直接给答案
- **验证理解**：修改后追问一个迁移问题（"如果换成 SVM 你还需要做什么？"）

## 文件权限矩阵

| 文件 | 修改权限 | 说明 |
|------|----------|------|
| `course-config.md` | 配置变更时 | 课程配置与诊断维度 |
| `exercises.md` | 可修改 | 练习库，持续扩充 |
| `mastery-tracker.md` | 每次测试后 | 技能掌握度追踪 |
| `mistakes.md` | 每次犯错后 | 错误记录 |
| `daily-tests.md` | 每日测试后 | 测试记录 |
| `learner/state.md` | 每次学习后 | 学生状态与弱点 |
| `skill-map/*.md` | 知识更新时 | 知识地图 |
| `agent/task-generation.md` | Agent 升级时 | 任务生成规则 |
| `materials/references.md` | 资料更新时 | 参考资料索引 |

## 诊断维度

每次诊断从以下 5 个维度评估学生的 ML 能力，综合 Level = round(概念×0.20 + 代码×0.25 + 数学×0.20 + 调试×0.15 + 工程×0.20)。

| 维度 | 权重 | 评估目标 |
|------|------|----------|
| 概念理解 | 20% | 是否理解 ML 核心概念（监督/无监督、过拟合、损失函数等） |
| 代码能力 | 25% | 能否用 sklearn/numpy 正确实现算法和数据处理流程 |
| 数学基础 | 20% | 是否理解算法背后的数学原理（线性代数、概率、优化） |
| 调试能力 | 15% | 能否发现数据泄漏、过拟合、指标误用等问题 |
| 工程能力 | 20% | 能否完成端到端的 ML 项目，能否做模型选型和评估 |

**Level 标准（五维度通用）：**

| Level | 概念理解 | 代码能力 | 数学基础 | 调试能力 | 工程能力 |
|-------|----------|----------|----------|----------|----------|
| 0 | 不知道 | 不能写 | 不知道 | 不能识别 | 无思路 |
| 1 | 听说过 | 能抄写 | 能查找 | 能识别 | 有思路 |
| 2 | 能解释 | 能模仿 | 能推导 | 能定位 | 能实现 |
| 3 | 能区分 | 能独立写 | 能应用 | 能修复 | 能优化 |
| 4 | 能教别人 | 能优化 | 能迁移 | 能预防 | 能部署 |

**诊断时机：**
- 前置诊断：首次学习前，概念快问 + 代码阅读 + 数据处理
- 每课诊断：学习新技能前，评估前置技能掌握程度
- 阶段诊断：每 10-11 课时后，全面评估并更新 mastery-tracker.md

## 教材映射

本课程的教学内容基于 `materials/noob/` 目录下的 58 篇教程，覆盖 ML 全生命周期：

| 教程编号 | 主题 | 对应课时 |
|----------|------|----------|
| 001-010 | ML 概述、数据类型、应用 | L01-L02 |
| 011-015 | 数据理解、清洗、特征工程、可视化、数据划分 | L02-L06 |
| 016-019 | 统计、概率、损失函数、偏差方差 | L07-L10 |
| 020-025 | 算法概述、线性/多元/多项式回归、回归评估 | L11-L15 |
| 026-032 | 决策树、SVM、KNN、集成、朴素贝叶斯、随机森林、分类评估 | L16-L22 |
| 033-034 | 聚类、降维 | L23-L26 |
| 035-038 | 强化学习框架、探索利用、Q-Learning/SARSA、深度 RL | L27-L30 |
| 039-042 | 神经网络结构、传播、DL vs ML、网络类型 | L31-L32 |
| 043-053 | 交叉验证、正则化、数据泄漏、集成进阶、超参数、MLOps、可解释性、偏差、成本 | L33-L39 |
| 054-058 | 案例：Titanic、房价、客户分群、PCA、RL | L40-L42 |
