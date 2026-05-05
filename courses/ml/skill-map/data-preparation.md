# skill-map: data-preparation — 数据准备（清洗、特征工程、可视化）

## 目标

掌握机器学习数据预处理的完整流程：从原始数据到可建模的干净特征矩阵。这是所有 ML 项目的第一步，也是最容易出错的环节。

## 必知概念

### 数据理解（EDA）
- **探索性分析**：在建模之前，先了解数据的基本特征
- **关键操作**：查看数据维度、数据类型、缺失值分布、基本统计量
- **可视化辅助**：直方图看分布、箱线图看异常值、热力图看相关性

### 数据清洗
- **缺失值处理**：
  - 删除：`df.dropna()` — 适合缺失比例很低的情况
  - 填充：`df.fillna(value)` — 均值/中位数/众数/前后值
  - 插值：`df.interpolate()` — 适合时间序列
- **异常值处理**：
  - IQR 方法：Q1 - 1.5*IQR 到 Q3 + 1.5*IQR 之外的为异常值
  - Z-score 方法：|z| > 3 的为异常值
- **重复值处理**：`df.drop_duplicates()`

### 特征工程
- **类别编码**：
  - 独热编码（One-Hot）：`pd.get_dummies()` — 无序类别
  - 标签编码（Label）：`LabelEncoder` — 有序类别
- **特征缩放**：
  - 标准化（StandardScaler）：均值 0，标准差 1
  - 归一化（MinMaxScaler）：缩放到 [0, 1] 区间
- **特征创建**：从已有特征组合/变换产生新特征

### 数据划分
- **train_test_split**：随机划分训练集和测试集
- **关键参数**：test_size, random_state, stratify
- **原则**：划分后才能做预处理（防止数据泄漏）

## 必知函数/API

| 函数/方法 | 用途 | 示例 |
|-----------|------|------|
| `pd.read_csv()` | 读取 CSV 文件 | `df = pd.read_csv('data.csv')` |
| `.head()` / `.tail()` | 查看前/后几行 | `df.head()` |
| `.info()` | 查看数据信息 | `df.info()` |
| `.describe()` | 统计摘要 | `df.describe()` |
| `.isnull().sum()` | 统计缺失值 | `df.isnull().sum()` |
| `.fillna()` | 填充缺失值 | `df['age'].fillna(df['age'].median())` |
| `.dropna()` | 删除缺失值 | `df.dropna(subset=['age'])` |
| `.drop_duplicates()` | 删除重复值 | `df.drop_duplicates()` |
| `pd.get_dummies()` | 独热编码 | `pd.get_dummies(df, columns=['city'])` |
| `StandardScaler()` | 标准化 | `scaler.fit_transform(X_train)` |
| `MinMaxScaler()` | 归一化 | `scaler.fit_transform(X_train)` |
| `train_test_split()` | 划分数据 | `X_train, X_test = train_test_split(X, test_size=0.2)` |

## 常见错误

1. **数据泄漏：在整个数据集上 fit**
   ```python
   # 错误
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)  # 泄漏了测试集
   X_train, X_test = train_test_split(X_scaled, test_size=0.2)

   # 正确
   X_train, X_test = train_test_split(X, test_size=0.2)
   X_train_scaled = scaler.fit_transform(X_train)
   X_test_scaled = scaler.transform(X_test)
   ```

2. **忘记在测试集上用 transform 而非 fit_transform**
   ```python
   # 错误
   X_test_scaled = scaler.fit_transform(X_test)  # 重新 fit 了！

   # 正确
   X_test_scaled = scaler.transform(X_test)
   ```

3. **独热编码导致多重共线性**
   ```python
   # 可能的问题
   pd.get_dummies(df, columns=['city'])  # 北京、上海、广州三列

   # 建议：drop_first=True
   pd.get_dummies(df, columns=['city'], drop_first=True)  # 只需两列
   ```

4. **缺失值填充方式不合理**
   ```python
   # 对偏态分布的收入列用均值填充
   df['income'].fillna(df['income'].mean())  # 受极端值影响大

   # 更好的选择：用中位数
   df['income'].fillna(df['income'].median())  # 对异常值更鲁棒
   ```

## 训练阶梯

### Step 1: 数据加载与探索（Level 0→1）
- 用 pandas 读取 CSV 文件
- 使用 head/info/describe 探索数据
- 统计缺失值和重复值

### Step 2: 缺失值处理（Level 1→2）
- 使用 dropna 删除缺失值
- 使用 fillna 填充缺失值
- 区分数值列和类别列的不同处理方式

### Step 3: 异常值检测（Level 2）
- 使用 IQR 方法检测异常值
- 使用 Z-score 方法检测异常值
- 决定删除还是修正异常值

### Step 4: 特征编码（Level 2→3）
- 使用 pd.get_dummies 独热编码
- 使用 LabelEncoder 标签编码
- 理解编码方式的选择依据

### Step 5: 特征缩放（Level 3）
- 使用 StandardScaler 标准化
- 使用 MinMaxScaler 归一化
- 理解哪些算法需要缩放

### Step 6: 数据划分（Level 3）
- 使用 train_test_split
- 理解 random_state 的作用
- 理解 stratify 参数（分层采样）

### Step 7: Pipeline 封装（Level 4）
- 使用 Pipeline 组合预处理步骤
- 确保预处理只在训练集上 fit
- 理解 ColumnTransformer 处理不同类型列

### Step 8: 完整预处理流程（Level 4→5）
- 从原始数据到建模就绪的完整流程
- 处理各种边界情况
- 考虑预处理对模型性能的影响

## 掌握标准

- **Level 3**: 能独立完成数据清洗、编码、缩放的完整流程
- **Level 4**: 能用 Pipeline 封装预处理步骤，理解数据泄漏的预防
- **Level 5**: 能针对不同数据特点选择合适的预处理策略，能处理各种边界情况

## 参考资料

- materials/noob/011_ml-data-understanding.md
- materials/noob/012_ml-data-cleaning.md
- materials/noob/013_ml-feature-engineering.md
- materials/noob/014_ml-data-visualizations.md
- materials/noob/015_ml-training-and-test-set-splitting.md
- scikit-learn 预处理文档：https://scikit-learn.org/stable/modules/preprocessing.html
