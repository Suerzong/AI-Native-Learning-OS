# 文本数据处理技能地图

## 目标

学习者能用 TensorFlow 的文本处理工具完成文本向量化、序列填充、词嵌入，能构建文本分类任务的完整数据管道。

## 必会概念

- Tokenization（分词）：将文本拆分为词/token
- Vocabulary（词汇表）：所有 token 的索引映射
- Padding（填充）：将变长序列填充为等长
- Embedding（嵌入）：将整数索引映射为稠密向量
- TextVectorization 是 Keras 的文本预处理标准层
- Pre vs Post padding 的区别

## 必会 API

### TextVectorization

```python
import tensorflow as tf

# 创建层
text_vectorizer = tf.keras.layers.TextVectorization(
    max_tokens=10000,            # 最大词汇量
    output_mode='int',            # 输出整数序列
    output_sequence_length=200,   # 序列长度
    standardize='lower_and_strip_punctuation',  # 标准化方式
    split='whitespace'            # 分词方式
)

# 学习词汇表
text_vectorizer.adapt(text_dataset)  # 传入文本数据集

# 转换文本
vectorized = text_vectorizer(["hello world", "tensorflow is great"])
# 输出：形状为 (2, 200) 的整数 tensor
```

| 参数 | 含义 | 常用值 |
|------|------|-------|
| `max_tokens` | 词汇表大小 | 10000-50000 |
| `output_mode` | 输出格式 | 'int'（整数序列）、'binary'（词袋）、'tf-idf' |
| `output_sequence_length` | 序列长度 | 根据文本长度分布选择 |
| `standardize` | 标准化 | 'lower_and_strip_punctuation'、None |
| `split` | 分词 | 'whitespace'、'character'、None |

### Embedding 层

```python
embedding_layer = tf.keras.layers.Embedding(
    input_dim=10000,   # 词汇表大小（= max_tokens）
    output_dim=128,    # 嵌入向量维度
    input_length=200   # 输入序列长度（= output_sequence_length）
)
# 输入形状：(batch_size, 200) 整数
# 输出形状：(batch_size, 200, 128) 浮点数
```

### 文本分类模型示例

```python
import tensorflow as tf

# 1. 文本向量化层
text_vectorizer = tf.keras.layers.TextVectorization(max_tokens=10000, output_sequence_length=200)
text_vectorizer.adapt(train_texts)

# 2. 构建模型
model = tf.keras.Sequential([
    text_vectorizer,                              # 文本 → 整数序列
    tf.keras.layers.Embedding(10000, 128),        # 整数 → 嵌入向量
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),  # LSTM
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # 二分类
])

# 3. 编译和训练
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_texts, train_labels, epochs=10)
```

### 其他文本处理 API

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.strings.lower()` | 转小写 | `tf.strings.lower("Hello")` |
| `tf.strings.strip()` | 去除空白 | `tf.strings.strip(" hello ")` |
| `tf.strings.split()` | 分词 | `tf.strings.split("hello world")` |
| `tf.keras.preprocessing.sequence.pad_sequences()` | 填充序列（旧 API）| 已被 TextVectorization 取代 |

## Padding 方向

| 方式 | 效果 | 适用场景 |
|------|------|---------|
| Pre padding | 填充在前面：[0, 0, 1, 2, 3] | LSTM/GRU（推荐，避免填充影响最后状态）|
| Post padding | 填充在后面：[1, 2, 3, 0, 0] | CNN（通常影响较小）|

TextVectorization 默认不做 padding，而是在 adapt 时截断/填充到 output_sequence_length。

## 常见错误

1. 忘记 adapt 直接调用 TextVectorization 导致词汇表为空
2. max_tokens 太小导致未知词被标记为 [UNK]
3. output_sequence_length 太短截断了文本
4. Embedding 的 input_dim 不等于 TextVectorization 的 max_tokens
5. 二分类输出层用了 softmax（应该用 sigmoid）
6. 文本标签格式和 loss 不匹配

## 训练阶梯

1. **基本向量化**：能用 TextVectorization 将文本转为整数序列
2. **Embedding**：能用 Embedding 层将整数转为向量
3. **简单分类**：能构建 Embedding + Dense 的文本分类模型
4. **RNN 模型**：能构建 Embedding + LSTM/GRU 的序列模型
5. **预训练嵌入**：能使用预训练的词向量（如 GloVe）

## 掌握标准

- 能用 TextVectorization + Embedding 构建文本分类 pipeline
- 理解 max_tokens、output_sequence_length、input_dim 的关系
- 能选择合适的 RNN 结构（LSTM/GRU、单向/双向）
- 能处理变长序列（padding）
- 理解 Pre vs Post padding 的区别
