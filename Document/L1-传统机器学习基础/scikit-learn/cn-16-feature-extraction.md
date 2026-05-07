# 1.16. 特征提取 {#feature-extraction}

特征提取模块用于从原始数据中提取数值特征。

## 1.16.1. 从字典加载特征 {#loading-features-from-dict}

[`DictVectorizer`](generated/sklearn.feature_extraction.DictVectorizer.html) 将特征名称和值组成的字典列表转换为 NumPy 数组或稀疏矩阵。

```python
>>> from sklearn.feature_extraction import DictVectorizer
>>> v = DictVectorizer(sparse=False)
>>> D = [{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}]
>>> v.fit_transform(D)
array([[2., 0., 1.],
       [0., 1., 3.]])
>>> v.get_feature_names_out()
array(['bar', 'baz', 'foo'], dtype=object)
```

## 1.16.2. 文本特征提取 {#text-feature-extraction}

### 词袋模型（Bag of Words） {#count-vectorizer}

[`CountVectorizer`](generated/sklearn.feature_extraction.text.CountVectorizer.html) 将文本文档集合转换为词频矩阵。

```python
>>> from sklearn.feature_extraction.text import CountVectorizer
>>> corpus = [
...     'This is the first document.',
...     'This document is the second document.',
... ]
>>> vectorizer = CountVectorizer()
>>> X = vectorizer.fit_transform(corpus)
>>> print(vectorizer.get_feature_names_out())
>>> print(X.toarray())
```

### TF-IDF 向量化 {#tfidf-vectorizer}

[`TfidfTransformer`](generated/sklearn.feature_extraction.text.TfidfTransformer.html) 将词频矩阵转换为 TF-IDF 表示。

```python
>>> from sklearn.feature_extraction.text import TfidfVectorizer
>>> vectorizer = TfidfVectorizer()
>>> X = vectorizer.fit_transform(corpus)
```

TF-IDF = TF（词频） * IDF（逆文档频率）

### 哈希向量化 {#hashing-vectorizer}

[`HashingVectorizer`](generated/sklearn.feature_extraction.text.HashingVectorizer.html) 使用哈希技巧进行文本特征提取，适合大规模数据。

```python
>>> from sklearn.feature_extraction.text import HashingVectorizer
>>> vectorizer = HashingVectorizer(n_features=2**4)
>>> X = vectorizer.fit_transform(corpus)
```

## 1.16.3. 图像特征提取 {#image-feature-extraction}

[`PatchExtractor`](generated/sklearn.feature_extraction.image.PatchExtractor.html) 从图像中提取小块。

```python
>>> from sklearn.feature_extraction.image import extract_patches_2d
>>> patches = extract_patches_2d(image, patch_size=(2, 2))
```

## 1.16.4. n-gram 特征 {#n-gram-features}

在 `CountVectorizer` 或 `TfidfVectorizer` 中，可以通过 `ngram_range` 参数指定 n-gram：

```python
>>> vectorizer = CountVectorizer(ngram_range=(1, 2))  # unigrams 和 bigrams
```

## 文本特征提取方法选择 {#text-extraction-choice}

| 方法 | 优点 | 缺点 |
|------|------|------|
| `CountVectorizer` | 简单直观 | 不考虑词频分布 |
| `TfidfVectorizer` | 考虑词的重要性 | 需要更多内存 |
| `HashingVectorizer` | 低内存，可增量 | 无法反向映射特征名 |
