# 命名实体识别（NER） 技能地图

## 目标

学习者能理解 NER 任务的定义、标注方案，掌握基于规则、CRF、深度学习的 NER 方法。

## 必会概念

- 命名实体：文本中具有特定意义的实体（人名、地名、机构名、时间等）
- 序列标注：为序列中的每个 token 分配一个标签
- BIO 标注方案：B=Begin, I=Inside, O=Outside
- BIOES 标注方案：增加 E=End, S=Single
- CRF（条件随机场）：考虑标签间转移概率的序列标注模型

## BIO 标注方案

```
句子：张三 在 北京大学 学习 计算机科学

BIO 标注：
张  B-PER
三  I-PER
在  O
北  B-ORG
京  I-ORG
大  I-ORG
学  I-ORG
学  O
习  O
计  B-Major
算  I-Major
机  I-Major
科  I-Major
学  I-Major

其中：PER=人名, ORG=机构名, Major=专业名
```

### 为什么需要 B- 和 I- 区分？

- 区分连续实体的边界："北京大学清华大学"中，两个机构名需要 B- 标记来区分
- B- 标记实体的开始，I- 标记实体的延续

## NER 方法演进

```
规则方法 → 统计方法(CRF) → 深度学习(BiLSTM-CRF) → 预训练模型(BERT-NER)
```

### BiLSTM-CRF 架构

```
输入序列: [张, 三, 在, 北, 京, ...]
    ↓
Embedding 层: 每个字/词 → 向量
    ↓
BiLSTM 层: 前向 LSTM + 后向 LSTM → 拼接
    ↓
线性层: 映射到标签空间
    ↓
CRF 层: 考虑标签转移约束（B-PER 后面不能接 B-LOC）
    ↓
输出标签: [B-PER, I-PER, O, B-ORG, I-ORG, ...]
```

### CRF 的作用

- 学习标签间的转移规则（如 B-PER → I-PER 合理，B-PER → B-LOC 不合理）
- 解码时使用 Viterbi 算法找到全局最优标签序列

## 代码示例

```python
import jieba
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# 方案1：基于规则的 NER（简单示例）
def rule_based_ner(text, entity_dict):
    """基于词典的 NER"""
    words = jieba.lcut(text)
    entities = []
    for word in words:
        for entity_type, names in entity_dict.items():
            if word in names:
                entities.append((word, entity_type))
    return entities

entity_dict = {
    "人名": ["张三", "李四"],
    "地名": ["北京", "上海"],
    "机构名": ["北京大学", "清华大学"]
}
text = "张三在北京大学读书"
print(rule_based_ner(text, entity_dict))
# [('张三', '人名'), ('北京大学', '机构名')]
```

```python
# 方案2：使用 Hugging Face BERT-NER
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = AutoModelForTokenClassification.from_pretrained(
    "ckiplab/bert-base-chinese-ner"
)

text = "张三在北京大学读书"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=2)

# 解码预测结果
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
labels = [model.config.id2label[p.item()] for p in predictions[0]]
for token, label in zip(tokens, labels):
    if label != "O":
        print(f"{token}: {label}")
```

## 常见错误

1. **实体边界标错**：I- 和 B- 标签使用不当
2. **非实体标成 I-**：实体外面的字被标成 Inside
3. **嵌套实体**："北京大学计算机系"中"北京大学"和"计算机系"都是实体
4. **中文 NER 没有空格**：必须先分词或用字符级标注
5. **忽略 O 标签**：O 是大多数 token 的标签，不能忽略

## 训练阶梯

1. **BIO 标注**：能手动对文本做 BIO 标注
2. **规则方法**：能用词典实现简单 NER
3. **CRF 理解**：理解 CRF 的转移矩阵作用
4. **BiLSTM-CRF**：能用 PyTorch 搭建 BiLSTM-CRF
5. **BERT-NER**：能用 Hugging Face 做预训练模型 NER

## 掌握标准

- 能对中文文本做正确的 BIO 标注
- 能解释 CRF 的转移矩阵和 Viterbi 解码
- 能用 Hugging Face 加载 NER 模型并推理
- 能处理嵌套实体和不常见实体类型
- 能评估 NER 模型的 F1 值（实体级别）
