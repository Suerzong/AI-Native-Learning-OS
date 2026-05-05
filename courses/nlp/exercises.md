# 训练任务库

训练任务用于 10-30 分钟内完成一个明确技能点。

## 任务模板

```md
## 任务名称

- 目标技能：
- 前置知识：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 反馈重点：
```

---

## 第一层：NLP 基础篇

### NLP-01：中文分词与预处理

- 目标技能：使用 jieba 完成中文文本分词和基础预处理
- 前置知识：Python 字符串处理基础
- 任务要求：
  1. 安装 jieba：`pip install jieba`
  2. 对以下句子进行分词："北京邮电大学是中国信息科技领域的顶尖高校"
  3. 使用精确模式、全模式、搜索引擎模式分别分词，对比结果
  4. 加载停用词表，去除分词结果中的停用词
  5. 将处理结果用 `/` 连接输出
- 限制条件：必须使用 jieba，不能手动分词
- 成功标准：三种模式分词结果不同，停用词被正确去除
- 常见错误：
  - 忘记 `jieba.cut()` 返回的是生成器，需要 `list()` 转换
  - 停用词表格式不对（每行一个词，还是逗号分隔）
  - 全模式和搜索引擎模式的区别不理解
- 反馈重点：分词模式的区别和适用场景

### NLP-02：TF-IDF 计算

- 目标技能：理解并手动计算 TF-IDF
- 前置知识：文本表示基础概念
- 任务要求：给定以下 3 篇文档：
  - 文档1："猫 追 老鼠"
  - 文档2："狗 追 猫"
  - 文档3："猫 和 狗 睡觉"
  1. 计算"追"在文档 1 中的 TF 值
  2. 计算"追"的 IDF 值（使用 `log(N/(df+1))` 公式）
  3. 计算"追"在文档 1 中的 TF-IDF 值
  4. 用 sklearn 的 `TfidfVectorizer` 验证结果
  5. 解释为什么"追"的 IDF 值比"猫"低
- 限制条件：先手动计算再用代码验证
- 成功标准：手动计算结果与 sklearn 结果一致，能解释 TF 和 IDF 的含义
- 常见错误：
  - TF 公式中分母用的是文档总词数还是文档总数
  - IDF 公式中 +1 的作用不理解
  - log 的底数（自然对数 vs 以 10 为底）
- 反馈重点：TF 衡量词在当前文档的重要性，IDF 衡量词在整个语料中的稀有程度

### NLP-03：文本分类 Pipeline

- 目标技能：构建完整的文本分类 pipeline
- 前置知识：TF-IDF、朴素贝叶斯
- 任务要求：
  1. 使用 sklearn 的 `fetch_20newsgroups` 加载新闻数据（选 4 个类别）
  2. 用 `TfidfVectorizer` 提取特征
  3. 用 `MultinomialNB` 训练分类器
  4. 在测试集上评估，输出 classification_report
  5. 分析模型在哪些类别上表现最差
- 限制条件：不能使用深度学习方法
- 成功标准：整体准确率 > 70%，能识别表现最差的类别并分析原因
- 常见错误：
  - 没有用 `subset='train'` 和 `subset='test'` 区分数据集
  - TfidfVectorizer 在训练集上 fit，测试集上 transform（不是 fit_transform）
  - 忘记 import 必要的模块
- 反馈重点：train/test 数据划分和 fit/transform 的正确使用

### NLP-04：BIO 标注练习

- 目标技能：理解并使用 BIO 标注方案
- 前置知识：NER 基本概念
- 任务要求：对以下句子进行 BIO 标注：
  "张三在北京大学学习计算机科学"
  1. 标注人名实体（张三）
  2. 标注地名/机构名实体（北京大学）
  3. 标注专业名实体（计算机科学）
  4. 写出完整的 BIO 标签序列
  5. 解释为什么需要 B- 和 I- 的区分
- 限制条件：必须使用 BIO 格式
- 成功标准：标签序列正确，能解释 B- 和 I- 的含义
- 常见错误：
  - 实体开头忘记用 B- 标签
  - 非实体词标成 I- 而不是 O
  - 多个实体之间没有 O 分隔
- 反馈重点：BIO 方案的编码规则和嵌套实体的处理

---

## 第二层：NLP 进阶任务篇

### NLP-05：文本相似度计算

- 目标技能：使用多种方法计算文本相似度
- 前置知识：文本表示、向量运算
- 任务要求：给定两段文本：
  - 文本A："自然语言处理是人工智能的重要分支"
  - 文本B："NLP 是 AI 的核心研究方向之一"
  1. 用 jieba 分词后计算 Jaccard 相似度
  2. 用 TF-IDF 向量化后计算余弦相似度
  3. 计算编辑距离
  4. 对比三种方法的结果，解释差异
- 限制条件：必须实现三种方法
- 成功标准：三种方法都能运行，能解释各自的优缺点
- 常见错误：
  - 余弦相似度公式中忘记归一化
  - 编辑距离的动态规划实现错误
  - Jaccard 没有先分词就直接比较字符
- 反馈重点：不同相似度指标的适用场景

### NLP-06：PyTorch 搭建 RNN 文本分类

- 目标技能：用 PyTorch 搭建 RNN 做文本分类
- 前置知识：PyTorch 基础、RNN 原理
- 任务要求：
  1. 构建词汇表，将文本转为索引序列
  2. 使用 `nn.Embedding` 层将索引转为词向量
  3. 使用 `nn.RNN` 或 `nn.LSTM` 处理序列
  4. 取最后一个时间步的隐藏状态做分类
  5. 在简单数据集（如 IMDB 子集）上训练
- 限制条件：序列需要 padding 到相同长度
- 成功标准：模型能训练，loss 下降，能打印每一步的 tensor shape
- 常见错误：
  - 序列长度不一致导致 DataLoader 报错
  - Embedding 的 padding_idx 没设置
  - RNN 输出的 hidden state 维度不理解（num_layers, batch, hidden）
  - pack_padded_sequence 的用法不清楚
- 反馈重点：序列处理的标准流程和维度变化

---

## 第三层：现代 NLP 模型篇

### NLP-07：Hugging Face Transformers 入门

- 目标技能：使用 Hugging Face 加载预训练模型并推理
- 前置知识：预训练模型概念
- 任务要求：
  1. 安装 transformers：`pip install transformers`
  2. 使用 `AutoTokenizer` 加载 `bert-base-chinese` 的 Tokenizer
  3. 对"自然语言处理很有趣"进行 tokenize，打印 token 和 input_ids
  4. 使用 `AutoModel` 加载 BERT 模型，获取最后一层隐藏状态
  5. 解释 Tokenizer 输出的三个字段（input_ids, attention_mask, token_type_ids）
- 限制条件：必须使用 Hugging Face 的 Auto 类
- 成功标准：Tokenize 结果正确，模型输出 shape 正确，能解释各字段含义
- 常见错误：
  - Tokenizer 和模型不匹配（用英文 Tokenizer 处理中文）
  - 不理解 [CLS] 和 [SEP] token 的作用
  - attention_mask 不理解（1 表示真实 token，0 表示 padding）
  - 模型输出是一个对象而不是 tensor，不知道怎么取值
- 反馈重点：Tokenizer 和模型的对应关系

### NLP-08：BERT 微调文本分类

- 目标技能：用 Hugging Face 微调 BERT 做文本分类
- 前置知识：BERT 原理、PyTorch 训练循环
- 任务要求：
  1. 加载中文情感数据集（如 ChnSentiCorp）
  2. 使用 `BertForSequenceClassification` 加载预训练模型
  3. 构建 DataLoader，处理 padding 和 attention_mask
  4. 写标准训练循环微调模型
  5. 在测试集上评估 Accuracy 和 F1
- 限制条件：学习率建议在 2e-5 到 5e-5 之间
- 成功标准：模型在测试集上 Accuracy > 85%，能解释微调过程
- 常见错误：
  - 微调学习率太大（如 1e-3），破坏预训练特征
  - 没有使用 `model.eval()` 和 `torch.no_grad()` 做评估
  - label 的数据类型不是 long（需要 `labels=torch.tensor(..., dtype=torch.long)`）
  - Tokenizer 的 `padding=True` 和 `truncation=True` 没设置
- 反馈重点：微调超参数的选择依据

### NLP-09：文本生成与 GPT

- 目标技能：使用 GPT-2 生成文本
- 前置知识：GPT 原理、自回归生成
- 任务要求：
  1. 加载中文 GPT-2 模型（如 `uer/gpt2-chinese-cluecorpussmall`）
  2. 给定开头"今天天气"，生成后续文本
  3. 对比不同 temperature（0.5, 1.0, 1.5）的生成结果
  4. 对比 greedy、top-k（k=50）、top-p（p=0.9）采样策略
  5. 分析 temperature 和采样策略对生成质量的影响
- 限制条件：生成长度不超过 50 tokens
- 成功标准：能生成连贯文本，能对比不同策略的效果差异
- 常见错误：
  - temperature=0 导致确定性输出（退化为 greedy）
  - top-k 和 top-p 同时使用时的作用不清楚
  - 不理解自回归的含义（每次只预测下一个 token）
- 反馈重点：不同生成策略的适用场景

---

## 第四层：工程应用篇

### NLP-10：端到端 NLP 项目

- 目标技能：完成从数据到部署的完整 NLP 项目
- 前置知识：全部前三层技能
- 任务要求：
  1. 选择一个中文 NLP 数据集（新闻分类或情感分析）
  2. 完成数据加载、清洗、划分
  3. 分别用传统方法（TF-IDF + SVM）和深度学习方法（BERT 微调）训练
  4. 对比两种方法的效果、训练时间、模型大小
  5. 分析 BERT 模型如果要部署到端侧需要做哪些优化
- 限制条件：必须有 baseline（传统方法）对比
- 成功标准：两种方法都能运行，有完整的评估报告，能讨论端侧部署方案
- 常见错误：
  - 不做 baseline 直接上 BERT
  - 对比实验的评估指标不一致
  - 不记录超参数和实验配置
  - 端侧部署只提概念不给具体方案
- 反馈重点：工程项目的完整流程和技术选型的依据

### NLP-11：模型评估与错误分析

- 目标技能：对 NLP 模型进行多维度评估和错误分析
- 前置知识：分类评估指标
- 任务要求：
  1. 训练一个文本分类模型
  2. 计算 Accuracy、Precision、Recall、F1
  3. 绘制混淆矩阵
  4. 找出模型预测错误的 Top 10 样本，分析错误原因
  5. 根据错误分析提出改进建议
- 限制条件：必须分析具体错误样本，不能只看数字
- 成功标准：有完整的评估指标、混淆矩阵、错误分析报告
- 常见错误：
  - 只看 Accuracy 忽略类别不平衡
  - 不区分 macro-F1 和 micro-F1
  - 错误分析只说"模型不好"而不给具体原因
- 反馈重点：如何从评估结果中发现问题并改进

### NLP-12：Prompt 设计实践

- 目标技能：设计有效的 Prompt 完成 NLP 任务
- 前置知识：GPT 原理、Prompt Engineering 概念
- 任务要求：
  1. 选择一个任务（如文本分类、信息抽取、文本摘要）
  2. 设计 zero-shot Prompt
  3. 设计 few-shot Prompt（3-5 个示例）
  4. 设计 chain-of-thought Prompt
  5. 对比三种 Prompt 的效果（如果无法调用 API，可以假设结果分析）
- 限制条件：Prompt 必须用中文设计
- 成功标准：三种 Prompt 设计合理，能分析效果差异的原因
- 常见错误：
  - Prompt 太模糊，模型不知道要做什么
  - few-shot 的示例不具代表性
  - chain-of-thought 的推理步骤不清晰
- 反馈重点：Prompt 设计的原则和技巧
