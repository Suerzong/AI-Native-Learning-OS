# skill-map: model-optimization — 模型优化（正则化、超参数调优、MLOps）

## 目标

掌握模型优化的核心技术，能用正则化控制过拟合，能用超参数搜索找到最优配置，能将模型工程化部署。

## 必知概念

### 正则化（Regularization）

#### L1 正则化（Lasso）
- **公式**：Loss = MSE + alpha * sum(|w_i|)
- **效果**：部分权重变为 0（稀疏解）→ 自动特征选择
- **适用场景**：特征数量多，怀疑部分特征无用

#### L2 正则化（Ridge）
- **公式**：Loss = MSE + alpha * sum(w_i^2)
- **效果**：所有权重变小但不为 0 → 防止权重过大
- **适用场景**：大多数情况的默认选择

#### ElasticNet
- **公式**：Loss = MSE + alpha * (l1_ratio * sum(|w_i|) + (1-l1_ratio) * sum(w_i^2))
- **效果**：结合 L1 和 L2 的优点
- **参数**：alpha 控制正则化强度，l1_ratio 控制 L1/L2 比例

### 超参数搜索

#### Grid Search
- **方法**：穷举所有参数组合
- **优点**：一定能找到搜索空间内的最优解
- **缺点**：参数多时计算量爆炸
- **sklearn**：`GridSearchCV(model, param_grid, cv=5)`

#### Random Search
- **方法**：随机采样参数组合
- **优点**：比 Grid Search 更高效（高维空间中）
- **缺点**：不保证找到最优解
- **sklearn**：`RandomizedSearchCV(model, param_distributions, n_iter=10, cv=5)`

#### Bayesian Optimization（了解）
- **方法**：根据历史评估结果智能选择下一组参数
- **优点**：比 Random Search 更高效
- **库**：optuna, hyperopt

### 数据泄漏（Data Leakage）

#### 特征泄漏
- 使用了与目标变量直接相关的特征
- 例：预测是否患病时，用了"医疗费用"作为特征

#### 时间泄漏
- 使用了未来信息
- 例：用 2024 年的数据预测 2023 年的事件

#### 预处理泄漏
- 在整个数据集上做预处理（fit 包含了测试集信息）
- **预防**：先划分再预处理，或使用 Pipeline

### MLOps 基础

#### 模型保存/加载
```python
import joblib
joblib.dump(model, 'model.pkl')     # 保存
model = joblib.load('model.pkl')    # 加载
```

#### Pipeline
- 将预处理和模型封装为一个整体
- 确保 fit 只在训练集上进行
- 简化部署流程
```python
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=5)),
    ('model', LogisticRegression())
])
```

#### 模型版本管理
- 保存模型文件 + 参数配置 + 数据版本
- 记录训练日期和评估指标
- 可以复现历史结果

### 模型优化策略

#### 特征选择
- 基于模型的特征重要性（Random Forest）
- 基于统计检验（SelectKBest）
- 基于正则化（Lasso 的稀疏解）

#### 模型压缩（嵌入式部署考虑）
- 量化：将浮点权重转为整数（INT8）
- 剪枝：移除对预测贡献小的权重
- 知识蒸馏：用小模型学习大模型的行为

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `Lasso(alpha)` | L1 正则化 | `Lasso(alpha=1.0)` |
| `Ridge(alpha)` | L2 正则化 | `Ridge(alpha=1.0)` |
| `ElasticNet()` | L1+L2 | `ElasticNet(alpha=1.0, l1_ratio=0.5)` |
| `GridSearchCV()` | 网格搜索 | `GridSearchCV(model, params, cv=5)` |
| `RandomizedSearchCV()` | 随机搜索 | `RandomizedSearchCV(model, params, n_iter=10)` |
| `Pipeline()` | 流水线 | `Pipeline([('scaler', ...), ('model', ...)])` |
| `joblib.dump()` | 保存模型 | `joblib.dump(model, 'model.pkl')` |
| `joblib.load()` | 加载模型 | `model = joblib.load('model.pkl')` |
| `cross_val_score()` | 交叉验证 | `cross_val_score(model, X, y, cv=5)` |

## 常见错误

1. **GridSearchCV 参数名格式错误**
   ```python
   pipe = Pipeline([('scaler', StandardScaler()), ('model', SVC())])

   # 错误
   params = {'C': [0.1, 1, 10]}

   # 正确：用双下划线
   params = {'model__C': [0.1, 1, 10]}
   ```

2. **数据泄漏：在 GridSearchCV 外做预处理**
   ```python
   # 错误
   X_scaled = StandardScaler().fit_transform(X)
   GridSearchCV(model, params, cv=5).fit(X_scaled, y)

   # 正确：在 Pipeline 中做
   pipe = Pipeline([('scaler', StandardScaler()), ('model', model)])
   GridSearchCV(pipe, params, cv=5).fit(X, y)
   ```

3. **Lasso alpha 过大**
   ```python
   # 所有系数都变 0
   model = Lasso(alpha=100)
   model.fit(X, y)
   print(model.coef_)  # 全是 0

   # 应该选择合适的 alpha（用交叉验证）
   ```

## 训练阶梯

### Step 1: 正则化基础（Level 0→2）
- 理解 L1 和 L2 的区别
- 用 Lasso/Ridge 训练模型
- 比较系数的变化

### Step 2: 正则化参数选择（Level 2→3）
- 用交叉验证选择 alpha
- 理解正则化强度的影响
- 观察 Lasso 的稀疏解

### Step 3: 超参数搜索（Level 3）
- 使用 GridSearchCV
- 使用 RandomizedSearchCV
- 对比两种方法的效率

### Step 4: 数据泄漏（Level 3→4）
- 识别各种数据泄漏场景
- 用 Pipeline 预防泄漏
- 理解评估结果的可靠性

### Step 5: MLOps（Level 4）
- 使用 Pipeline 封装流程
- 保存和加载模型
- 设计模型评估和部署流程

### Step 6: 模型压缩（Level 4→5）
- 理解量化和剪枝
- 评估模型大小与精度的权衡
- 考虑嵌入式部署的限制

## 掌握标准

- **Level 3**: 能用正则化控制过拟合，能用超参数搜索优化模型
- **Level 4**: 能用 Pipeline 封装完整流程，能识别和预防数据泄漏
- **Level 5**: 能设计完整的模型优化和部署方案，能考虑嵌入式设备的限制

## 参考资料

- materials/noob/044_ml-model-optimization-regularization.md
- materials/noob/045_ml-model-optimization-data-leakage.md
- materials/noob/046_ml-model-optimization-integrated-approaches.md
- materials/noob/047_ml-hyperparameter-search.md
- materials/noob/048_ml-model-optimization-mlops.md
- materials/noob/049_ml-model-optimization-common-problems.md
- scikit-learn Pipeline：https://scikit-learn.org/stable/modules/pipeline.html
- scikit-learn 调参：https://scikit-learn.org/stable/modules/grid_search.html
