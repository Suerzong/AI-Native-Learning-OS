# 错题与误区记录

本文件只记录会影响后续能力形成的错误，不记录一次性笔误。

## 模板

```md
## YYYY-MM-DD：错误标题

- 所属技能：
- 错误表现：
- 错误原因：
- 正确理解：
- 纠正任务：
- 是否已复测通过：
```

---

## 常见误区样例

### 中文未分词直接处理

- 所属技能：NLP-L104 中文分词
- 错误表现：将中文句子直接传入 TF-IDF 向量化器，按字符而不是按词切分
- 错误原因：习惯了英文处理方式（英文有空格天然分词），忽略中文没有词边界
- 正确理解：中文文本必须先分词再做后续处理。jieba 是最常用的中文分词库，分词后的结果用空格连接后再传入 TfidfVectorizer（设置 `token_pattern=r"(?u)\b\w+\b"` 或使用自定义 tokenizer）
- 纠正任务：对比"分词后再向量化"和"直接按字符向量化"的分类效果差异
- 是否已复测通过：否

### Tokenizer 与模型不匹配

- 所属技能：NLP-L307 Tokenizer 原理与使用
- 错误表现：使用英文 BERT 的 Tokenizer 处理中文文本，导致中文被拆分成单个字符或 [UNK]
- 错误原因：不理解不同预训练模型使用不同的词表和 Tokenizer，以为所有 BERT 都通用
- 正确理解：每个预训练模型都有对应的 Tokenizer，必须使用同一个模型的 Tokenizer。中文任务应使用 `bert-base-chinese`，英文任务使用 `bert-base-uncased`。使用 `AutoTokenizer.from_pretrained()` 可以确保匹配
- 纠正任务：分别用 `bert-base-chinese` 和 `bert-base-uncased` 的 Tokenizer 处理同一段中文文本，对比分词结果
- 是否已复测通过：否

### 序列长度不统一导致 DataLoader 报错

- 所属技能：NLP-L204 RNN 原理与实现
- 错误表现：将不同长度的文本索引序列直接放入 DataLoader，报 `Expected tensor of same size` 错误
- 错误原因：一个 batch 中的 tensor 必须形状相同，但不同文本的长度不同
- 正确理解：NLP 中必须处理变长序列。标准做法是：(1) 确定 max_length；(2) 短序列在右侧 padding（或使用 pad_sequence）；(3) 记录 attention_mask 标记哪些是真实 token 哪些是 padding；(4) DataLoader 中使用 collate_fn 自定义批处理
- 纠正任务：写一个自定义 collate_fn，实现对变长序列的 padding 和 mask 生成
- 是否已复测通过：否

### 微调 BERT 学习率过大

- 所属技能：NLP-L302 BERT 微调
- 错误表现：微调 BERT 时使用 1e-3 的学习率，训练 loss 不收敛或先降后升
- 错误原因：习惯了从头训练模型的学习率（1e-3 ~ 1e-2），不知道预训练模型微调需要更小的学习率
- 正确理解：BERT 微调的标准学习率在 2e-5 到 5e-5 之间。因为预训练已经学到了很好的特征表示，微调只是在小数据集上做小幅调整。大学习率会破坏这些预训练特征。通常使用线性 warmup + 衰减的学习率调度策略
- 纠正任务：对比学习率为 1e-3、1e-4、2e-5 时 BERT 微调的 loss 曲线和最终准确率
- 是否已复测通过：否

### attention_mask 忽略导致模型关注 padding

- 所属技能：NLP-L307 Tokenizer 原理与使用
- 错误表现：模型训练时只传了 input_ids 没传 attention_mask，导致模型对 padding 位置也计算注意力
- 错误原因：不理解 attention_mask 的作用，以为 Tokenizer 输出的三个字段只有 input_ids 重要
- 正确理解：attention_mask 标记哪些位置是真实 token（值为 1）哪些是 padding（值为 0）。在 Attention 计算中，mask=0 的位置会被设为负无穷（-inf），经过 softmax 后变为 0，从而不参与计算。不传 attention_mask 会让模型把 padding 当成有效信息，影响性能
- 纠正任务：对比传/不传 attention_mask 时模型输出的差异
- 是否已复测通过：否
