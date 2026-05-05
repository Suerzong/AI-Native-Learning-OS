# daily-tests.md — 机器学习每日测试记录

## 测试模板

```
### [日期] 每日测试

**测试范围**: [本次测试覆盖的技能]
**测试时间**: [预计时间，通常 15-20 分钟]
**题目数量**: 4 题

#### 题目 1: 概念题
- **题目**: [概念性问题]
- **学生回答**: [学生的回答]
- **正确答案**: [标准答案]
- **得分**: [0-25]
- **点评**: [简短评价]

#### 题目 2: 代码定位题
- **题目**: [找出代码中的问题]
- **学生回答**: [学生的回答]
- **正确答案**: [标准答案]
- **得分**: [0-25]
- **点评**: [简短评价]

#### 题目 3: 修改题
- **题目**: [修改给定代码实现新功能]
- **学生代码**: [学生的代码]
- **是否正确**: [是/否]
- **得分**: [0-25]
- **点评**: [简短评价]

#### 题目 4: 调试题
- **题目**: [修复有 bug 的代码]
- **学生代码**: [学生的代码]
- **是否正确**: [是/否]
- **得分**: [0-25]
- **点评**: [简短评价]

**总分**: [0-100]
**通过**: [是/否，≥60 分通过]
**状态更新**: [更新了哪些技能的 Level]
```

---

## 测试记录

### 2026-05-05 每日测试 — 样例（参考）

**测试范围**: Layer 1 基础（ML 概述、数据理解、数据清洗、特征工程）
**测试时间**: 15 分钟
**题目数量**: 4 题

#### 题目 1: 概念题
- **题目**: 什么是数据泄漏（Data Leakage）？请举出两种常见的数据泄漏场景，并说明如何预防。
- **预期答案要点**:
  - 数据泄漏是指测试集的信息以某种方式"泄漏"到了训练过程中
  - 场景 1：在整个数据集上做标准化/特征选择后再划分训练测试集 → 应先划分再预处理
  - 场景 2：使用了与目标变量直接相关的特征（如预测房价时用了"每平米价格"） → 应检查特征与目标的关系
  - 预防方法：使用 Pipeline 封装预处理步骤，确保 fit 只在训练集上进行
- **得分**: [0-25]

#### 题目 2: 代码定位题
- **题目**: 以下代码存在数据泄漏问题，请指出哪一行有问题：
```python
1  from sklearn.preprocessing import StandardScaler
2  from sklearn.model_selection import train_test_split
3
4  scaler = StandardScaler()
5  X_scaled = scaler.fit_transform(X)        # 泄漏点
6  X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
7
8  model.fit(X_train, y_train)
9  print(model.score(X_test, y_test))
```
- **预期答案**:
  - 第 5 行有问题：在划分数据之前对整个数据集做了 fit_transform
  - 这导致 scaler 学到了测试集的均值和标准差
  - 正确做法：先 train_test_split，再在 X_train 上 fit_transform，在 X_test 上只做 transform
- **得分**: [0-25]

#### 题目 3: 修改题
- **题目**: 以下代码对一个分类数据集进行了独热编码。请修改为使用标签编码（Label Encoding），并将结果保存为新列 'city_encoded'。
```python
import pandas as pd
data = pd.DataFrame({'city': ['北京', '上海', '广州', '北京', '上海']})
data_encoded = pd.get_dummies(data['city'])
print(data_encoded)
```
- **预期修改**:
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['city_encoded'] = le.fit_transform(data['city'])
print(data)
# 输出中 city_encoded 列应该是 0, 1, 2, 0, 1
```
- **得分**: [0-25]

#### 题目 4: 调试题
- **题目**: 以下代码试图用 train_test_split 划分数据，但运行时出错。找出并修复。
```python
from sklearn.model_selection import train_test_split
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```
- **预期修复**:
  - X 有 4 个样本，但 y 只有 3 个标签，数量不一致
  - 应该让 y 也有 4 个元素，例如 `y = [0, 1, 0, 1]`
  - 或者让 X 也有 3 个元素
```python
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 0, 1]  # 修复：4 个样本对应 4 个标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```
- **得分**: [0-25]

---

**总分**: 待评分
**通过**: 待定
**状态更新**: 待更新
