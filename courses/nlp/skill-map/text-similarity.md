# 文本相似度 技能地图

## 目标

学习者能计算多种文本相似度指标，理解字面相似度和语义相似度的区别，能选择合适的相似度方法。

## 必会概念

- 字面相似度：基于字符或词的重叠（Jaccard、编辑距离）
- 语义相似度：基于含义的相似（余弦相似度、语义嵌入）
- 余弦相似度：衡量两个向量的夹角
- 编辑距离（Levenshtein Distance）：从字符串 A 变到 B 的最少操作次数
- Jaccard 相似度：两个集合的交集与并集之比
- 句子嵌入：将整个句子编码为一个向量

## 关键公式

### 余弦相似度

```
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)

取值范围：[-1, 1]
  1: 完全相同方向（最相似）
  0: 正交（无关）
 -1: 完全相反
```

### Jaccard 相似度

```
J(A, B) = |A ∩ B| / |A ∪ B|

其中 A、B 是集合（如分词后的词集合）
取值范围：[0, 1]
```

### 编辑距离（动态规划）

```
dp[i][j] = 从 word1[0..i-1] 变到 word2[0..j-1] 的最少操作数

dp[i][j] = {
  dp[i-1][j-1]                    if word1[i-1] == word2[j-1]
  1 + min(dp[i-1][j],             删除
          dp[i][j-1],             插入
          dp[i-1][j-1])           替换
}
```

## 方法对比

```
┌─────────────┬────────────┬────────────┬──────────────┐
│    方法      │  衡量层面   │  计算复杂度  │   适用场景    │
├─────────────┼────────────┼────────────┼──────────────┤
│ Jaccard     │  词级别     │  O(n)       │  集合重叠度    │
│ 编辑距离     │  字符级别   │  O(m×n)     │  拼写纠错      │
│ 余弦(TF-IDF)│  向量级别   │  O(n)       │  文档检索      │
│ 余弦(嵌入)   │  语义级别   │  O(d)       │  语义匹配      │
│ BERTScore   │  语义级别   │  较高        │  生成评估      │
└─────────────┴────────────┴────────────┴──────────────┘
```

## 代码示例

```python
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ====== 1. Jaccard 相似度 ======
def jaccard_similarity(text1, text2):
    set1 = set(jieba.lcut(text1))
    set2 = set(jieba.lcut(text2))
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)

text_a = "自然语言处理是人工智能的重要分支"
text_b = "NLP 是 AI 的核心研究方向"
print("Jaccard:", jaccard_similarity(text_a, text_b))

# ====== 2. 编辑距离 ======
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

print("编辑距离:", edit_distance("自然语言处理", "自然语言理解"))

# ====== 3. TF-IDF 余弦相似度 ======
docs = ["自然语言处理是人工智能分支", "深度学习在NLP中广泛应用"]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs)
sim = cosine_similarity(tfidf[0:1], tfidf[1:2])
print("TF-IDF 余弦相似度:", sim[0][0])
```

```python
# ====== 4. 使用 sentence-transformers 计算语义相似度 ======
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

sentences = [
    "自然语言处理是人工智能的重要分支",
    "NLP 是 AI 的核心研究方向",
    "今天天气很好"
]

embeddings = model.encode(sentences)
# 计算余弦相似度
cos_sim = util.cos_sim(embeddings, embeddings)
print("语义相似度矩阵:")
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        print(f"  '{sentences[i]}' vs '{sentences[j]}': {cos_sim[i][j]:.4f}")
```

## 常见错误

1. **余弦相似度归一化**：不需要对向量做额外归一化，公式已经处理
2. **编辑距离和相似度混淆**：编辑距离是操作次数（越大越不相似），相似度是 0-1 值
3. **Jaccard 不考虑词频**：只看词是否出现，不看出现几次
4. **语义相似度依赖嵌入质量**：不好的词向量会导致不好的相似度
5. **中英文混合处理**：中文需要分词，英文不需要

## 训练阶梯

1. **Jaccard**：能计算两个文本的 Jaccard 相似度
2. **编辑距离**：能实现编辑距离的动态规划算法
3. **余弦相似度**：能用 TF-IDF + 余弦相似度做文档匹配
4. **语义相似度**：能用 sentence-transformers 计算语义相似度
5. **应用**：能将相似度用于信息检索或文本去重

## 掌握标准

- 能写出余弦相似度公式并手动计算
- 能实现编辑距离的动态规划算法
- 能对比字面相似度和语义相似度的差异
- 能用 sentence-transformers 计算语义相似度
- 能根据场景选择合适的相似度方法
