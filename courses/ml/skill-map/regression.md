# skill-map: regression — 回归算法（线性、多元、多项式、逻辑回归）

## 目标

掌握回归算法的核心原理，能用 sklearn 训练和评估回归模型，理解线性回归到逻辑回归的演进关系。

## 必知概念

### 线性回归（Linear Regression）
- **目标**：找到一条直线 y = wx + b，使预测值与真实值的误差最小
- **损失函数**：MSE（均方误差）= 1/n * sum((y_i - y_hat_i)^2)
- **求解方法**：
  - 正规方程：w = (X^T X)^(-1) X^T y（直接求解，适合小数据）
  - 梯度下降：迭代更新 w = w - alpha * dL/dw（适合大数据）
- **sklearn**：`LinearRegression()`

### 多元线性回归（Multiple Linear Regression）
- **公式**：y = w1*x1 + w2*x2 + ... + wn*xn + b
- **关键点**：多个特征可能量纲不同，需要特征缩放
- **多重共线性**：特征之间高度相关会导致系数不稳定
- **sklearn**：与线性回归相同，只是 X 是多列

### 多项式回归（Polynomial Regression）
- **思路**：将原始特征扩展为高次项，用线性回归拟合非线性关系
- **方法**：x -> [1, x, x^2, x^3, ...]
- **风险**：阶数过高 → 过拟合
- **sklearn**：`PolynomialFeatures(degree=n)` + `LinearRegression()`

### 逻辑回归（Logistic Regression）
- **本质**：分类算法（虽然名字叫"回归"）
- **Sigmoid 函数**：sigma(z) = 1 / (1 + e^(-z))，将输出映射到 [0, 1]
- **决策边界**：P(y=1|x) >= 0.5 → 预测为 1
- **损失函数**：交叉熵（Log Loss）= -1/n * sum(y*log(p) + (1-y)*log(1-p))
- **sklearn**：`LogisticRegression()`

### 回归评估指标
| 指标 | 公式 | 含义 |
|------|------|------|
| MSE | mean((y - y_hat)^2) | 均方误差，越小越好 |
| RMSE | sqrt(MSE) | 与 y 同单位，更直观 |
| MAE | mean(|y - y_hat|) | 平均绝对误差，对异常值更鲁棒 |
| R² | 1 - SS_res/SS_tot | 解释方差的比例，1 为完美 |

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `LinearRegression()` | 线性回归 | `model.fit(X, y)` |
| `PolynomialFeatures(n)` | 多项式特征扩展 | `poly.fit_transform(X)` |
| `LogisticRegression()` | 逻辑回归 | `model.fit(X, y)` |
| `mean_squared_error()` | MSE | `mse(y_test, y_pred)` |
| `r2_score()` | R² | `r2_score(y_test, y_pred)` |
| `mean_absolute_error()` | MAE | `mae(y_test, y_pred)` |
| `.coef_` | 系数 | `model.coef_` |
| `.intercept_` | 截距 | `model.intercept_` |

## 常见错误

1. **忘记 reshape 一维数据**
   ```python
   # 错误：X 是一维数组
   model.fit(X, y)  # ValueError!

   # 正确：reshape 为二维
   model.fit(X.reshape(-1, 1), y)
   ```

2. **评估指标参数顺序**
   ```python
   # 顺序错误可能导致结果异常
   r2_score(y_pred, y_test)  # 参数反了

   # 正确
   r2_score(y_test, y_pred)
   ```

3. **逻辑回归当回归用**
   ```python
   # 逻辑回归是分类算法
   model = LogisticRegression()
   model.fit(X, y)
   model.predict(X)  # 输出 0 或 1，不是连续值
   ```

4. **多项式回归阶数过高**
   ```python
   # 过拟合风险
   poly = PolynomialFeatures(degree=15)  # 太高了

   # 应该用交叉验证选择最优阶数
   ```

## 训练阶梯

### Step 1: 线性回归基础（Level 0→2）
- 理解 y = wx + b 的含义
- 用 sklearn 训练线性回归
- 可视化拟合结果

### Step 2: 多元回归（Level 2）
- 处理多特征输入
- 理解特征缩放的重要性
- 解读系数的含义

### Step 3: 多项式回归（Level 2→3）
- 使用 PolynomialFeatures 扩展特征
- 比较不同阶数的拟合效果
- 识别过拟合

### Step 4: 逻辑回归（Level 3）
- 理解 Sigmoid 函数
- 可视化决策边界
- 区分分类和回归

### Step 5: 评估指标（Level 3）
- 计算并解释 MSE、RMSE、MAE、R²
- 知道各指标的适用场景
- 理解 R² 的含义

### Step 6: 模型优化（Level 4）
- 特征选择
- 正则化（Ridge/Lasso）
- 交叉验证选择最优模型

## 掌握标准

- **Level 3**: 能用 sklearn 训练各种回归模型，能计算和解释评估指标
- **Level 4**: 能选择合适的回归方法，能用正则化控制过拟合
- **Level 5**: 能推导损失函数的梯度，能从零实现梯度下降

## 参考资料

- materials/noob/021_ml-linear-regression.md
- materials/noob/022_ml-multiple-linear-regression.md
- materials/noob/023_ml-multinomial-regression.md
- materials/noob/024_ml-logistic-regression.md
- materials/noob/025_ml-regression-model-evaluation.md
- scikit-learn 线性模型：https://scikit-learn.org/stable/modules/linear_model.html
