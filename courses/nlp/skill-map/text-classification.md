# 文本分类 技能地图

## 目标

学习者能完成从原始文本到分类结果的完整流程，掌握传统方法（朴素贝叶斯、SVM）和深度学习方法。

## 必会概念

- 文本分类的定义：给文本分配预定义类别
- 特征提取 → 分类器 的 pipeline
- 朴素贝叶斯（基于条件独立假设的概率分类器）
- SVM（支持向量机，在高维稀疏空间中效果好）
- 深度学习方法（TextCNN、BERT 微调）
- 评估指标：Accuracy、Precision、Recall、F1

## 分类方法演进

```
传统方法 Pipeline：
  原始文本 → 预处理 → 特征提取(TF-IDF) → 分类器(NB/SVM) → 类别

深度学习 Pipeline：
  原始文本 → 预处理 → Tokenizer → 模型(BERT/TextCNN) → 类别
```

## 朴素贝叶斯

### 核心公式

```
P(类别|文本) ∝ P(类别) × ∏ P(词i|类别)

预测类别 = argmax P(类别) × ∏ P(词i|类别)
```

- 条件独立假设：每个词的出现是独立的（"朴素"的来源）
- 优点：简单、快速、小数据集效果不错
- 缺点：忽略词序和上下文

## 代码示例

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 示例数据
texts = ["这部电影很好看", "太无聊了浪费时间", "演员演技在线", "剧情太烂了", "强烈推荐"]
labels = [1, 0, 1, 0, 1]  # 1=正面, 0=负面

# 特征提取
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# 朴素贝叶斯
nb = MultinomialNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
print("朴素贝叶斯:", classification_report(y_test, y_pred_nb))

# SVM
svm = LinearSVC()
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print("SVM:", classification_report(y_test, y_pred_svm))
```

## 深度学习方法：TextCNN

```python
import torch
import torch.nn as nn

class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes, kernel_sizes=[2,3,4], num_filters=100):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.convs = nn.ModuleList([
            nn.Conv1d(embed_dim, num_filters, k) for k in kernel_sizes
        ])
        self.fc = nn.Linear(num_filters * len(kernel_sizes), num_classes)

    def forward(self, x):
        # x: (batch, seq_len)
        x = self.embedding(x)        # (batch, seq_len, embed_dim)
        x = x.permute(0, 2, 1)       # (batch, embed_dim, seq_len)
        x = [torch.relu(conv(x)).max(dim=2)[0] for conv in self.convs]
        x = torch.cat(x, dim=1)      # (batch, num_filters * len(kernel_sizes))
        return self.fc(x)
```

## 常见错误

1. **不做特征提取直接分类**：原始文本不能直接传入分类器
2. **训练集测试集划分不当**：测试集参与了 fit_transform
3. **类别不平衡不处理**：少数类被忽略
4. **只看 Accuracy**：类别不平衡时 Accuracy 不靠谱
5. **朴素贝叶斯假设过强**：忽略词序导致信息丢失

## 训练阶梯

1. **朴素贝叶斯**：能用 sklearn 实现文本分类
2. **SVM**：理解 SVM 在高维空间的优势
3. **评估指标**：能计算和解读 Precision、Recall、F1
4. **TextCNN**：能用 PyTorch 搭建 TextCNN
5. **BERT 微调**：能用 Hugging Face 微调 BERT 做分类

## 掌握标准

- 能写出从文本到分类结果的完整代码
- 能对比不同分类器的效果
- 能计算和解读分类评估指标
- 能分析分类错误的原因
- 能根据数据规模选择合适的方法
