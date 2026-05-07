[ Hugging Face](/)

Transformers 文档

词元分类

# Transformers

词元分类

词元分类（Token classification）为句子中的各个词元分配标签。最常见的词元分类任务之一是命名实体识别（Named Entity Recognition, NER）。NER 试图为句子中的每个实体找到标签，如人物、地点或组织。

本指南将向你展示如何：

  1. 在 [WNUT 17](https://huggingface.co/datasets/wnut_17) 数据集上微调 [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) 以检测新实体。
  2. 使用微调后的模型进行推理。

开始之前，确保安装了所有必要的库：

    pip install transformers datasets evaluate seqeval

## [](#load-wnut-17-dataset) 加载 WNUT 17 数据集

首先从 🤗 Datasets 库加载 WNUT 17 数据集：

    >>> from datasets import load_dataset
    >>> wnut = load_dataset("wnut_17")

`ner_tags` 中的每个数字代表一个实体。将数字转换为标签名称以找出实体：

    >>> label_list = wnut["train"].features[f"ner_tags"].feature.names
    >>> label_list
    ["O", "B-corporation", "I-corporation", "B-creative-work", "I-creative-work",
     "B-group", "I-group", "B-location", "I-location", "B-person", "I-person",
     "B-product", "I-product"]

每个 `ner_tag` 前缀的字母表示实体的词元位置：

  * `B-` 表示实体的开始。
  * `I-` 表示词元包含在同一实体内（例如，`State` 词元是 `Empire State Building` 等实体的一部分）。
  * `0` 表示词元不对应任何实体。

## [](#preprocess) 预处理

下一步是加载 DistilBERT 分词器以预处理 `tokens` 字段：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

你需要设置 `is_split_into_words=True` 来将词分词为子词。但子词分词会在输入和标签之间产生不匹配。你需要通过以下方式重新对齐词元和标签：

  1. 使用 [`word_ids`](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.BatchEncoding.word_ids) 方法将所有词元映射到其对应的词。
  2. 将特殊词元 `[CLS]` 和 `[SEP]` 的标签设为 `-100`，使 PyTorch 损失函数忽略它们。
  3. 仅标记给定词的第一个词元。将同一词的其他子词元设为 `-100`。

    >>> def tokenize_and_align_labels(examples):
    ...     tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)
    ...     labels = []
    ...     for i, label in enumerate(examples[f"ner_tags"]):
    ...         word_ids = tokenized_inputs.word_ids(batch_index=i)
    ...         previous_word_idx = None
    ...         label_ids = []
    ...         for word_idx in word_ids:
    ...             if word_idx is None:
    ...                 label_ids.append(-100)
    ...             elif word_idx != previous_word_idx:
    ...                 label_ids.append(label[word_idx])
    ...             else:
    ...                 label_ids.append(-100)
    ...             previous_word_idx = word_idx
    ...         labels.append(label_ids)
    ...     tokenized_inputs["labels"] = labels
    ...     return tokenized_inputs

使用 🤗 Datasets 的 `map` 函数将预处理函数应用于整个数据集：

    >>> tokenized_wnut = wnut.map(tokenize_and_align_labels, batched=True)

现在使用 [DataCollatorForTokenClassification](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForTokenClassification) 创建一批示例。

    >>> from transformers import DataCollatorForTokenClassification
    >>> data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

## [](#evaluate) 评估

对于此任务，加载 [seqeval](https://huggingface.co/spaces/evaluate-metric/seqeval) 框架。Seqeval 产生多个分数：精确率（precision）、召回率（recall）、F1 和准确率（accuracy）。

    >>> import evaluate
    >>> seqeval = evaluate.load("seqeval")

    >>> import numpy as np

    >>> def compute_metrics(p):
    ...     predictions, labels = p
    ...     predictions = np.argmax(predictions, axis=2)
    ...     true_predictions = [
    ...         [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
    ...         for prediction, label in zip(predictions, labels)
    ...     ]
    ...     true_labels = [
    ...         [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
    ...         for prediction, label in zip(predictions, labels)
    ...     ]
    ...     results = seqeval.compute(predictions=true_predictions, references=true_labels)
    ...     return {
    ...         "precision": results["overall_precision"],
    ...         "recall": results["overall_recall"],
    ...         "f1": results["overall_f1"],
    ...         "accuracy": results["overall_accuracy"],
    ...     }

## [](#train) 训练

使用 [AutoModelForTokenClassification](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForTokenClassification) 加载 DistilBERT：

    >>> from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer

    >>> model = AutoModelForTokenClassification.from_pretrained(
    ...     "distilbert/distilbert-base-uncased", num_labels=13, id2label=id2label, label2id=label2id
    ... )

定义训练参数并开始训练：

    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_wnut_model",
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
    ...     train_dataset=tokenized_wnut["train"],
    ...     eval_dataset=tokenized_wnut["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

训练完成后，使用 [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) 将模型共享到 Hub。

## [](#inference) 推理

使用 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 进行推理：

    >>> from transformers import pipeline

    >>> classifier = pipeline("ner", model="stevhliu/my_awesome_wnut_model")
    >>> classifier("The Golden State Warriors are an American professional basketball team based in San Francisco.")

你也可以手动进行推理：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_wnut_model")
    >>> inputs = tokenizer(text, return_tensors="pt")

    >>> from transformers import AutoModelForTokenClassification
    >>> model = AutoModelForTokenClassification.from_pretrained("stevhliu/my_awesome_wnut_model")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits

    >>> predictions = torch.argmax(logits, dim=2)
    >>> predicted_token_class = [model.config.id2label[t.item()] for t in predictions[0]]

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/token_classification.md)

[←文本分类](/docs/transformers/tasks/sequence_classification) [问答→](/docs/transformers/tasks/question_answering)

[词元分类](#token-classification)[加载 WNUT 17 数据集](#load-wnut-17-dataset)[预处理](#preprocess)[评估](#evaluate)[训练](#train)[推理](#inference)
