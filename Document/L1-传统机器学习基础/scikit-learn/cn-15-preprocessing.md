# 1.17. 预处理数据 {#preprocessing}

预处理模块提供了数据转换和特征工程的实用工具。

## 1.17.1. 标准化 {#standardization}

### 标准缩放（Z-score 标准化） {#standard-scaler}

[`StandardScaler`](generated/sklearn.preprocessing.StandardScaler.html) 将特征标准化为均值 0 和标准差 1。

```python
>>> from sklearn.preprocessing import StandardScaler
>>> scaler = StandardScaler()
>>> X_scaled = scaler.fit_transform(X)
```

### 最小-最大缩放 {#min-max-scaler}

[`MinMaxScaler`](generated/sklearn.preprocessing.MinMaxScaler.html) 将特征缩放到给定范围（默认 [0, 1]）。

```python
>>> from sklearn.preprocessing import MinMaxScaler
>>> scaler = MinMaxScaler(feature_range=(0, 1))
>>> X_scaled = scaler.fit_transform(X)
```

### 最大绝对值缩放 {#max-abs-scaler}

[`MaxAbsScaler`](generated/sklearn.preprocessing.MaxAbsScaler.html) 将每个特征缩放到 [-1, 1] 范围，保留稀疏性。

### 稳健缩放 {#robust-scaler}

[`RobustScaler`](generated/sklearn.preprocessing.RobustScaler.html) 使用中位数和四分位数范围进行缩放，对异常值更稳健。

### 归一化 {#normalizer}

[`Normalizer`](generated/sklearn.preprocessing.Normalizer.html) 将每个样本缩放为单位范数。

```python
>>> from sklearn.preprocessing import Normalizer
>>> normalizer = Normalizer(norm='l2')
>>> X_normalized = normalizer.fit_transform(X)
```

## 1.17.2. 编码分类特征 {#encoding-categorical-features}

### 标签编码 {#label-encoding}

[`LabelEncoder`](generated/sklearn.preprocessing.LabelEncoder.html) 将分类标签编码为整数。

```python
>>> from sklearn.preprocessing import LabelEncoder
>>> le = LabelEncoder()
>>> le.fit(["paris", "paris", "tokyo", "amsterdam"])
>>> le.transform(["tokyo", "tokyo", "paris"])
array([2, 2, 1]...)
```

### 独热编码 {#one-hot-encoding}

[`OneHotEncoder`](generated/sklearn.preprocessing.OneHotEncoder.html) 将分类特征编码为独热向量。

```python
>>> from sklearn.preprocessing import OneHotEncoder
>>> enc = OneHotEncoder(handle_unknown='ignore')
>>> enc.fit(X)
>>> enc.transform(X).toarray()
```

### 序数编码 {#ordinal-encoding}

[`OrdinalEncoder`](generated/sklearn.preprocessing.OrdinalEncoder.html) 将分类特征编码为整数。

## 1.17.3. 生成多项式特征 {#generating-polynomial-features}

[`PolynomialFeatures`](generated/sklearn.preprocessing.PolynomialFeatures.html) 生成多项式和交互特征。

```python
>>> from sklearn.preprocessing import PolynomialFeatures
>>> poly = PolynomialFeatures(degree=2)
>>> poly.fit_transform(X)
```

## 1.17.4. 自定义变换器 {#custom-transformers}

[`FunctionTransformer`](generated/sklearn.preprocessing.FunctionTransformer.html) 将自定义函数应用为变换器。

```python
>>> from sklearn.preprocessing import FunctionTransformer
>>> transformer = FunctionTransformer(np.log1p)
>>> X_transformed = transformer.fit_transform(X)
```

## 预处理方法总结 {#preprocessing-summary}

| 方法 | 类 | 适用场景 |
|------|-----|---------|
| Z-score 标准化 | `StandardScaler` | 通用，假设正态分布 |
| 最小-最大缩放 | `MinMaxScaler` | 需要固定范围 |
| 稳健缩放 | `RobustScaler` | 存在异常值 |
| 归一化 | `Normalizer` | 基于样本的缩放 |
| 标签编码 | `LabelEncoder` | 目标变量编码 |
| 独热编码 | `OneHotEncoder` | 分类特征编码 |
| 多项式特征 | `PolynomialFeatures` | 特征工程 |
