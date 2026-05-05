# 学习资源索引

本文件收集 NLP 学习的优质资源，按类别组织。

---

## 本课程教材（runoob.com NLP 教程）

| 编号 | 主题 | 路径 |
|------|------|------|
| 001 | NLP 教程概述 | `materials/noob/001_nlp-tutorial.md` |
| 002 | NLP 简介 | `materials/noob/002_nlp-intro.md` |
| 003 | 语言学基础 | `materials/noob/003_nlp-linguistics-basics.md` |
| 004 | 文本预处理 | `materials/noob/004_text-preprocessing.md` |
| 005 | 文本表示 | `materials/noob/005_text-representation.md` |
| 006 | 文本分类 | `materials/noob/006_text-classification.md` |
| 007 | 情感分析 | `materials/noob/007_sentiment-analysis.md` |
| 008 | 命名实体识别 | `materials/noob/008_named-entity-recognition.md` |
| 009 | 关系抽取 | `materials/noob/009_relation-extraction.md` |
| 010 | 文本相似度 | `materials/noob/010_text-similarity.md` |
| 011 | 循环神经网络 | `materials/noob/011_recurrent-neural-network.md` |
| 012 | 注意力机制 | `materials/noob/012_attention-mechanism.md` |
| 013 | Transformer 架构 | `materials/noob/013_transformer-architecture.md` |
| 014 | Seq2Seq 模型 | `materials/noob/014_sequence-to-sequence.md` |
| 015 | 预训练模型 | `materials/noob/015_pre-trained-models.md` |
| 016 | BERT 编码器 | `materials/noob/016_bert-encoder.md` |
| 017 | GPT | `materials/noob/017_generative-pre-trained-transformer.md` |
| 018 | 多模态预训练模型 | `materials/noob/018_multimodal-pre-trained-models.md` |
| 019 | Python NLP 工具 | `materials/noob/019_python-nlp.md` |
| 020 | 深度学习框架 | `materials/noob/020_deep-learning-frameworks.md` |
| 021 | 数据处理工具 | `materials/noob/021_data-processing-tools.md` |
| 完整教程 | NLP 完整教程 | `materials/noob/NLP_完整教程.md` |

---

## 官方文档与工具

| 资源 | URL | 用途 |
|------|-----|------|
| Hugging Face Transformers | https://huggingface.co/docs/transformers/ | 预训练模型加载与微调 |
| Hugging Face Datasets | https://huggingface.co/docs/datasets/ | 数据集加载与处理 |
| Hugging Face Tokenizers | https://huggingface.co/docs/tokenizers/ | 高性能 Tokenizer |
| Hugging Face Model Hub | https://huggingface.co/models | 预训练模型仓库 |
| PyTorch 官方文档 | https://pytorch.org/docs/stable/ | 深度学习框架 |
| sklearn 文本特征提取 | https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction | TF-IDF、CountVectorizer |
| jieba GitHub | https://github.com/fxsjy/jieba | 中文分词 |
| spaCy 官方文档 | https://spacy.io/ | 工业级 NLP 库 |
| NLTK 官方文档 | https://www.nltk.org/ | 教学用 NLP 库 |

## 中文教程与资源

| 资源 | URL | 用途 |
|------|-----|------|
| 菜鸟教程 NLP | https://www.runoob.com/nlp/ | 入门教程（本课程主要参考）|
| Hugging Face 中文社区 | https://huggingface.co/uer | 中文预训练模型 |
| 哈工大 NLP 组 | https://ir.hit.edu.cn/ | 中文 NLP 研究 |
| Chinese-BERT | https://github.com/ymcui/Chinese-BERT | 中文 BERT 模型 |
| 中文预训练模型列表 | https://github.com/InsaneLife/ChineseNLP | 中文 NLP 资源汇总 |

## 中文预训练模型推荐

| 模型 | Hugging Face ID | 用途 |
|------|-----------------|------|
| BERT-Base-Chinese | `bert-base-chinese` | 中文文本分类、NER |
| RoBERTa-wwm-ext | `hfl/chinese-roberta-wwm-ext` | 中文通用任务（效果更好）|
| MacBERT | `hfl/chinese-macbert-base` | 中文 NLU 任务 |
| GPT2-Chinese | `uer/gpt2-chinese-cluecorpussmall` | 中文文本生成 |
| TextCNN | - | 轻量级文本分类 |
| SimBERT | `hfl/simbert-chinese-base` | 中文语义相似度 |

## 视频资源

| 资源 | 平台 | 用途 |
|------|------|------|
| 李沐：动手学深度学习（NLP 章节） | B站 | RNN、Attention、Transformer |
| Stanford CS224N | B站/YouTube | NLP 经典课程 |
| Hugging Face 官方教程 | YouTube | Transformers 库使用 |
| 3Blue1Brown：Attention 机制 | B站/YouTube | 直觉理解注意力 |

## 工具与库

| 工具/库 | 用途 | 安装 |
|---------|------|------|
| jieba | 中文分词 | `pip install jieba` |
| transformers | 预训练模型 | `pip install transformers` |
| datasets | 数据集加载 | `pip install datasets` |
| tokenizers | 高性能分词 | `pip install tokenizers` |
| scikit-learn | TF-IDF、传统 ML | `pip install scikit-learn` |
| nltk | 教学用 NLP | `pip install nltk` |
| spaCy | 工业级 NLP | `pip install spacy` |
| gensim | Word2Vec、主题模型 | `pip install gensim` |
| pandas | 数据处理 | `pip install pandas` |
| torch | 深度学习框架 | `pip install torch` |

## 推荐学习顺序（外部资源配合）

1. **入门**：菜鸟教程 NLP（materials/noob/）→ 理解 NLP 基本概念和流程
2. **预处理**：jieba + sklearn → 掌握中文分词和 TF-IDF
3. **经典方法**：sklearn 文本分类 → 掌握朴素贝叶斯、SVM
4. **深度学习**：PyTorch + RNN/Transformer → 理解序列模型
5. **预训练模型**：Hugging Face Transformers → BERT 微调
6. **实战**：中文数据集 + 微调 → 完整 NLP 项目
7. **端侧**：模型压缩 + 部署 → 端侧 NLP 方案
