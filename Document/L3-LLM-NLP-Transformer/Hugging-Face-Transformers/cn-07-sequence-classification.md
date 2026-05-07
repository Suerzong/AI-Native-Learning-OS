[ Hugging Face](/)

Transformers 文档

文本分类

# Transformers

文本分类

文本分类是一种常见的 NLP 任务，为文本分配标签或类别。一些最大的公司在生产环境中运行文本分类，用于各种实际应用。最流行的文本分类形式之一是情感分析（sentiment analysis），它为文本序列分配如 🙂 正面、🙁 负面或 😐 中性的标签。

本指南将向你展示如何：

  1. 在 [IMDb](https://huggingface.co/datasets/imdb) 数据集上微调 [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) 以判断电影评论是正面还是负面。
  2. 使用微调后的模型进行推理。

> 要查看兼容此任务的所有架构和检查点，我们建议查看[任务页面](https://huggingface.co/tasks/text-classification)。

开始之前，确保安装了所有必要的库：

    pip install transformers datasets evaluate accelerate

我们鼓励你登录 Hugging Face 账户，以便与社区上传和共享你的模型。

## [](#load-imdb-dataset) 加载 IMDb 数据集

首先从 🤗 Datasets 库加载 IMDb 数据集：

    >>> from datasets import load_dataset
    >>> imdb = load_dataset("imdb")

然后查看一个示例：

    >>> imdb["test"][0]

此数据集有两个字段：

  * `text`：电影评论文本。
  * `label`：值为 `0`（负面评论）或 `1`（正面评论）。

## [](#preprocess) 预处理

下一步是加载 DistilBERT 分词器以预处理 `text` 字段：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

创建一个预处理函数来对 `text` 进行分词，并将序列截断为不超过 DistilBERT 的最大输入长度：

    >>> def preprocess_function(examples):
    ...     return tokenizer(examples["text"], truncation=True)

要将预处理函数应用于整个数据集，使用 🤗 Datasets 的 `map` 函数。通过设置 `batched=True` 可以一次处理数据集的多个元素来加速 `map`：

    tokenized_imdb = imdb.map(preprocess_function, batched=True)

现在使用 [DataCollatorWithPadding](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorWithPadding) 创建一批示例。在整理期间将句子_动态填充_到批次中最长长度，比将整个数据集填充到最大长度更高效。

    >>> from transformers import DataCollatorWithPadding
    >>> data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

## [](#evaluate) 评估

在训练期间包含指标通常有助于评估模型性能。你可以使用 🤗 [Evaluate](https://huggingface.co/docs/evaluate/index) 库快速加载评估方法。对于此任务，加载 [accuracy](https://huggingface.co/spaces/evaluate-metric/accuracy) 指标：

    >>> import evaluate
    >>> accuracy = evaluate.load("accuracy")

然后创建一个函数，将预测和标签传递给 [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) 来计算准确率：

    >>> import numpy as np

    >>> def compute_metrics(eval_pred):
    ...     predictions, labels = eval_pred
    ...     predictions = np.argmax(predictions, axis=1)
    ...     return accuracy.compute(predictions=predictions, references=labels)

## [](#train) 训练

在开始训练模型之前，使用 `id2label` 和 `label2id` 创建预期 ID 到标签的映射：

    >>> id2label = {0: "NEGATIVE", 1: "POSITIVE"}
    >>> label2id = {"NEGATIVE": 0, "POSITIVE": 1}

你已准备好开始训练模型！使用 [AutoModelForSequenceClassification](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification) 加载 DistilBERT，以及预期的标签数量和标签映射：

    >>> from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

    >>> model = AutoModelForSequenceClassification.from_pretrained(
    ...     "distilbert/distilbert-base-uncased", num_labels=2, id2label=id2label, label2id=label2id
    ... )

此时，只剩下三个步骤：

  1. 在 [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments) 中定义训练超参数。
  2. 将训练参数传递给 [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer)。
  3. 调用 [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) 微调模型。

    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_model",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=2,
    ...     weight_decay=0.01,
    ...     eval_strategy="epoch",
    ...     save_strategy="epoch",
    ...     load_best_model_at_end=True,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_imdb["train"],
    ...     eval_dataset=tokenized_imdb["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

训练完成后，使用 [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) 方法将模型共享到 Hub：

    >>> trainer.push_to_hub()

## [](#inference) 推理

很好，现在你已经微调了模型，可以使用它进行推理！

获取一些你想运行推理的文本：

    >>> text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

尝试微调模型进行推理的最简单方法是在 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 中使用它。使用你的模型实例化一个用于情感分析的 `pipeline`，并将文本传递给它：

    >>> from transformers import pipeline

    >>> classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")
    >>> classifier(text)
    [{'label': 'POSITIVE', 'score': 0.9994940757751465}]

你也可以手动复制 `pipeline` 的结果：

对文本进行分词并返回 PyTorch 张量：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
    >>> inputs = tokenizer(text, return_tensors="pt")

将输入传递给模型并返回 `logits`：

    >>> from transformers import AutoModelForSequenceClassification
    >>> model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits

获取概率最高的类，并使用模型的 `id2label` 映射将其转换为文本标签：

    >>> predicted_class_id = logits.argmax().item()
    >>> model.config.id2label[predicted_class_id]
    'POSITIVE'

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/sequence_classification.md)

[←Unsloth](/docs/transformers/community_integrations/unsloth) [词元分类→](/docs/transformers/tasks/token_classification)

[文本分类](#text-classification)[加载 IMDb 数据集](#load-imdb-dataset)[预处理](#preprocess)[评估](#evaluate)[训练](#train)[推理](#inference)
