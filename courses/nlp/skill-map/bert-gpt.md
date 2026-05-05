# BERT 与 GPT 技能地图

## 目标

学习者能理解 BERT 和 GPT 的架构区别、预训练目标，掌握使用 Hugging Face 进行微调和推理。

## 必会概念

- 预训练 + 微调范式
- BERT（Bidirectional Encoder Representations from Transformers）
- GPT（Generative Pre-trained Transformer）
- MLM（Masked Language Model）
- NSP（Next Sentence Prediction）
- 自回归（Autoregressive）vs 双向编码（Bidirectional）
- Fine-tuning（微调）
- Zero-shot / Few-shot

## BERT vs GPT 对比

```
BERT（Encoder-only）:
  ┌──────────────────────────────────────┐
  │  [CLS] 自然 语言 处理 很 有趣 [SEP]  │
  │      ↓    ↓    ↓   ↓  ↓   ↓         │
  │     双向 Self-Attention（看到所有词）│
  │      ↓    ↓    ↓   ↓  ↓   ↓         │
  │   输出每个 token 的上下文表示         │
  └──────────────────────────────────────┘
  预训练目标：MLM（遮住一些词预测）+ NSP（判断两句话是否连续）
  适合任务：分类、NER、阅读理解（需要理解整个输入）

GPT（Decoder-only）:
  ┌──────────────────────────────────────┐
  │  [BOS] 自然 → 语言 → 处理 → 很      │
  │    ↓    ↓      ↓      ↓     ↓       │
  │   因果 Self-Attention（只看到左侧）  │
  │    ↓    ↓      ↓      ↓     ↓       │
  │   预测下一个 token                    │
  └──────────────────────────────────────┘
  预训练目标：自回归语言建模（预测下一个词）
  适合任务：文本生成、对话、摘要（需要生成文本）
```

## BERT 预训练目标

### MLM（Masked Language Model）

```
输入：  我  喜欢  [MASK]  语言  处理
标签：  -    -    自然    -     -

随机 mask 15% 的 token：
  - 80% 替换为 [MASK]
  - 10% 替换为随机词
  - 10% 保持不变
```

### NSP（Next Sentence Prediction）

```
输入：[CLS] 今天天气很好 [SEP] 我们去公园 [SEP]  标签：IsNext
输入：[CLS] 今天天气很好 [SEP] 人工智能发展 [SEP]  标签：NotNext

（注：后续研究如 RoBERTa 发现 NSP 作用不大，可以去掉）
```

## GPT 自回归原理

```
训练时：P(w_1, w_2, ..., w_n) = ∏ P(w_i | w_1, ..., w_{i-1})

输入：  [BOS] 我 喜欢 自然 语言
预测：    我   喜欢  自然  语言  处理
              ↓     ↓     ↓     ↓
           P(w|BOS) P(w|我) P(w|我喜欢) P(w|我喜欢自然)

生成时：
  1. 输入 prompt
  2. 模型预测下一个 token 的概率分布
  3. 采样（greedy/top-k/top-p）得到下一个 token
  4. 将新 token 拼到输入末尾，重复 2-4
```

## Hugging Face 使用示例

### BERT 文本分类

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 加载模型和 Tokenizer
model_name = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 准备输入
text = "这部电影非常精彩"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
# inputs 包含: input_ids, attention_mask, token_type_ids

# 推理
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1)
print("预测类别:", prediction.item())
```

### GPT 文本生成

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "uer/gpt2-chinese-cluecorpussmall"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 生成文本
prompt = "人工智能"
inputs = tokenizer(prompt, return_tensors="pt")

# 生成参数
outputs = model.generate(
    **inputs,
    max_length=50,           # 最大长度
    temperature=0.7,         # 温度（越低越确定）
    top_k=50,                # top-k 采样
    top_p=0.9,               # top-p (nucleus) 采样
    do_sample=True,          # 使用采样（而非 greedy）
    repetition_penalty=1.2   # 重复惩罚
)

generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("生成结果:", generated)
```

## 微调关键超参数

| 超参数 | 推荐值 | 说明 |
|--------|--------|------|
| 学习率 | 2e-5 ~ 5e-5 | 比从头训练小 100 倍 |
| Batch size | 16 或 32 | 受显存限制 |
| Epochs | 2 ~ 5 | 微调不需要太多 epochs |
| Warmup | 总步数的 6-10% | 线性 warmup |
| Max length | 128 或 512 | 根据数据特点选择 |
| Weight decay | 0.01 | 轻微正则化 |

## 常见错误

1. **BERT 用于生成**：BERT 是 Encoder-only，不能自回归生成
2. **GPT 用于分类**：GPT 能做分类但效果通常不如 BERT
3. **微调学习率太大**：1e-3 会破坏预训练特征
4. **Tokenizer 不匹配**：用错误的 Tokenizer 导致 [UNK] 过多
5. **不理解 [CLS] 和 [SEP]**：BERT 的特殊 token 有特定含义

## 训练阶梯

1. **概念理解**：能解释 BERT 和 GPT 的核心区别
2. **预训练目标**：能解释 MLM 和自回归语言建模
3. **Hugging Face 入门**：能加载模型和 Tokenizer
4. **微调实践**：能用 BERT 微调文本分类
5. **生成实践**：能用 GPT 生成文本并调节参数

## 掌握标准

- 能画出 BERT（Encoder）和 GPT（Decoder）的架构对比图
- 能解释 MLM 的三个替换策略（80/10/10）
- 能用 Hugging Face 完成 BERT 微调的完整流程
- 能用 Hugging Face 完成 GPT 文本生成
- 能说出微调的关键超参数及其推荐值
- 能解释什么时候用 BERT，什么时候用 GPT
