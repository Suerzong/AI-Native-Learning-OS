# 文本表示 技能地图

## 目标

学习者能将文本数据转换为数值向量，理解从离散表示（BoW、TF-IDF）到分布式表示（词嵌入）的演进。

## 必会概念

- 词袋模型（Bag of Words, BoW）：忽略词序，只统计词频
- TF-IDF：词频 × 逆文档频率，衡量词的重要性
- 词嵌入（Word Embedding）：将词映射为密集向量
- Word2Vec：基于上下文学习词向量（CBOW / Skip-gram）
- 稀疏向量 vs 密集向量
- 词汇表（Vocabulary）

## 关键公式

### TF-IDF

```
TF(t, d) = 词 t 在文档 d 中出现的次数 / 文档 d 的总词数

IDF(t) = log(文档总数 / (包含词 t 的文档数 + 1))

TF-IDF(t, d) = TF(t, d) × IDF(t)
```

- TF 衡量：词在当前文档中的重要性
- IDF 衡量：词在整个语料中的稀有程度
- TF-IDF 衡量：词对当前文档的独特重要性

### Word2Vec（Skip-gram 目标函数）

```
P(context | word) = softmax(W_c · h)

其中 h 是词的嵌入向量，W_c 是上下文词的权重矩阵
```

## 架构对比

```
BoW/TF-IDF（离散表示）：
  文档 → [0, 1, 0, 3, 0, 2, ...]  (维度 = 词汇表大小，通常很高)
  优点：简单、可解释
  缺点：维度高、稀疏、无语义信息

Word2Vec（分布式表示）：
  词 → [0.23, -0.45, 0.67, ..., 0.12]  (维度 = 嵌入维度，通常 100-300)
  优点：密集、有语义信息（"国王"-"男人"+"女人"≈"女王"）
  缺点：一词一向量，无法处理多义词
```

## 代码示例

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# 示例文档
docs = [
    "自然语言处理是人工智能的重要分支",
    "深度学习在自然语言处理中广泛应用",
    "人工智能和深度学习改变世界"
]

# TF-IDF 向量化
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

print("词汇表:", vectorizer.get_feature_names_out())
print("TF-IDF 矩阵形状:", tfidf_matrix.shape)  # (3, 词汇数)
print("第一篇文档的向量:", tfidf_matrix[0].toarray())
```

```python
# 使用 gensim 训练 Word2Vec
from gensim.models import Word2Vec

# 分词后的句子
sentences = [
    ["自然", "语言", "处理", "是", "人工智能", "的", "分支"],
    ["深度", "学习", "在", "自然", "语言", "处理", "中", "应用"],
]

# 训练 Word2Vec
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

# 获取词向量
vector = model.wv["语言"]
print("语言 的词向量:", vector)

# 找最相似的词
similar = model.wv.most_similar("语言", topn=3)
print("与 语言 最相似的词:", similar)
```

## 常见错误

1. **TF 公式分母用错**：分母应该是文档总词数，不是文档总数
2. **IDF 的 +1 忘记**：不加 1 会导致包含词 t 的文档数为 0 时除零错误
3. **fit 和 fit_transform 混淆**：训练集用 fit_transform，测试集只用 transform
4. **词汇表太大**：不做任何过滤导致维度灾难
5. **混淆 one-hot 和词嵌入**：one-hot 是稀疏的、无语义的；词嵌入是密集的、有语义的

## 训练阶梯

1. **BoW**：能手动构建词袋向量
2. **TF-IDF**：能手动计算 TF-IDF 并用 sklearn 验证
3. **sklearn 实践**：能用 TfidfVectorizer 完整处理文本数据
4. **词嵌入概念**：理解 Word2Vec 的直觉和训练方式
5. **综合选型**：能根据任务选择合适的文本表示方法

## 掌握标准

- 能手动计算 TF-IDF
- 能用 sklearn 完成文本向量化
- 能解释 BoW、TF-IDF、词嵌入的优缺点
- 理解稀疏表示和密集表示的区别
- 能根据任务选择合适的表示方法
