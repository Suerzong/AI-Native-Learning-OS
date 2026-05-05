# mistakes.md — 机器学习错误记录

## 错误记录模板

```
### [日期] 错误 #编号
- **相关技能**: [skill-map 中的技能]
- **错误代码**:
```python
# 学生写的错误代码
```
- **错误类型**: 数据泄漏 / 过拟合 / 指标误用 / 概念错误 / 代码错误
- **错误描述**: [发生了什么错误]
- **错误原因**: [为什么会犯这个错误]
- **正确做法**:
```python
# 正确的代码
```
- **要点总结**: [一句话总结]
- **是否已掌握**: 否
```

---

## 错误记录

### 2026-05-05 错误 #001
- **相关技能**: data-preparation — 数据泄漏
- **错误代码**:
```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 先标准化，再划分 —— 泄漏了测试集信息
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
print(f"测试集准确率: {model.score(X_test, y_test):.3f}")  # 虚高的准确率
```
- **错误类型**: 数据泄漏
- **错误描述**: 在划分训练/测试集之前对整个数据集做了标准化，导致 scaler 学到了测试集的均值和标准差
- **错误原因**: 不理解 StandardScaler 的 fit 和 transform 的区别，不知道"先划分后预处理"的原则
- **正确做法**:
```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 先划分，再标准化
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)    # 只在训练集上 fit
X_test_scaled = scaler.transform(X_test)          # 测试集只 transform

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
print(f"测试集准确率: {model.score(X_test_scaled, y_test):.3f}")
```
- **要点总结**: 永远先划分训练/测试集，再在训练集上 fit 预处理参数，测试集只做 transform
- **是否已掌握**: 否

---

### 2026-05-05 错误 #002
- **相关技能**: model-evaluation — 过拟合判断
- **错误代码**:
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 用 15 阶多项式拟合 20 个数据点
poly = PolynomialFeatures(degree=15)
X_poly = poly.fit_transform(X_train)

model = LinearRegression()
model.fit(X_poly, y_train)

train_r2 = r2_score(y_train, model.predict(X_poly))
test_r2 = r2_score(y_test, model.predict(poly.transform(X_test)))

print(f"训练集 R²: {train_r2:.3f}")   # 0.999
print(f"测试集 R²: {test_r2:.3f}")    # 0.234 —— 严重过拟合！
```
- **错误类型**: 过拟合
- **错误描述**: 使用过高阶数的多项式回归，模型在训练集上表现极好，但在测试集上表现很差
- **错误原因**: 不理解模型复杂度与泛化能力的权衡，没有使用交叉验证选择最优阶数
- **正确做法**:
```python
from sklearn.model_selection import cross_val_score
import numpy as np

best_degree = 1
best_score = -np.inf

for degree in [1, 2, 3, 5, 7, 10]:
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X_train)
    scores = cross_val_score(LinearRegression(), X_poly, y_train, cv=5)
    mean_score = scores.mean()
    print(f"degree={degree}: CV R²={mean_score:.3f}")
    if mean_score > best_score:
        best_score = mean_score
        best_degree = degree

print(f"最优阶数: {best_degree}")
```
- **要点总结**: 不要盲目增加模型复杂度，用交叉验证选择最优的模型复杂度，关注训练/测试分数差距
- **是否已掌握**: 否
