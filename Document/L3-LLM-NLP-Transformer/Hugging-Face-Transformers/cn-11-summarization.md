[ Hugging Face](/)

Transformers 文档

摘要

# Transformers

摘要

摘要（Summarization）创建文档或文章的较短版本，捕获所有重要信息。与翻译一样，它可以被表述为序列到序列（sequence-to-sequence）任务。摘要可以是：

  * 抽取式（Extractive）：从文档中提取最相关的信息。
  * 生成式（Abstractive）：生成捕获最相关信息的新文本。

本指南将向你展示如何：

  1. 在 [BillSum](https://huggingface.co/datasets/FiscalNote/billsum) 数据集的加州州法案子集上微调 [T5](https://huggingface.co/google-t5/t5-small) 进行生成式摘要。
  2. 使用微调后的模型进行推理。

## [](#load-billsum-dataset) 加载 BillSum 数据集

首先从 🤗 Datasets 库加载 BillSum 数据集较小的加州州法案子集：

    >>> from datasets import load_dataset
    >>> billsum = load_dataset("billsum", split="ca_test")

使用 `train_test_split` 方法将数据集分为训练集和测试集：

    >>> billsum = billsum.train_test_split(test_size=0.2)

有两个字段你将需要使用：

  * `text`：法案文本，作为模型输入。
  * `summary`：`text` 的浓缩版本，作为模型目标。

## [](#preprocess) 预处理

加载 T5 分词器来处理 `text` 和 `summary`：

    >>> from transformers import AutoTokenizer
    >>> checkpoint = "google-t5/t5-small"
    >>> tokenizer = AutoTokenizer.from_pretrained(checkpoint)

你需要创建的预处理函数需要：

  1. 在输入前添加提示前缀，使 T5 知道这是摘要任务。
  2. 在对标签分词时使用 `text_target` 关键字参数。
  3. 将序列截断为不超过 `max_length` 参数设置的最大长度。

    >>> prefix = "summarize: "

    >>> def preprocess_function(examples):
    ...     inputs = [prefix + doc for doc in examples["text"]]
    ...     model_inputs = tokenizer(inputs, max_length=1024, truncation=True)
    ...     labels = tokenizer(text_target=examples["summary"], max_length=128, truncation=True)
    ...     model_inputs["labels"] = labels["input_ids"]
    ...     return model_inputs

使用 🤗 Datasets 的 `map` 方法将预处理函数应用于整个数据集：

    >>> tokenized_billsum = billsum.map(preprocess_function, batched=True)

使用 [DataCollatorForSeq2Seq](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForSeq2Seq) 创建一批示例：

    >>> from transformers import DataCollatorForSeq2Seq
    >>> data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)

## [](#evaluate) 评估

对于此任务，加载 [ROUGE](https://huggingface.co/spaces/evaluate-metric/rouge) 指标：

    >>> import evaluate
    >>> rouge = evaluate.load("rouge")

创建一个函数将预测和标签传递给 [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) 来计算 ROUGE 指标：

    >>> import numpy as np

    >>> def compute_metrics(eval_pred):
    ...     predictions, labels = eval_pred
    ...     decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    ...     labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    ...     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    ...     result = rouge.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    ...     prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
    ...     result["gen_len"] = np.mean(prediction_lens)
    ...     return {k: round(v, 4) for k, v in result.items()}

## [](#train) 训练

使用 [AutoModelForSeq2SeqLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSeq2SeqLM) 加载 T5：

    >>> from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
    >>> model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

定义训练参数并开始训练：

    >>> training_args = Seq2SeqTrainingArguments(
    ...     output_dir="my_awesome_billsum_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     weight_decay=0.01,
    ...     save_total_limit=3,
    ...     num_train_epochs=4,
    ...     predict_with_generate=True,
    ...     fp16=True,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Seq2SeqTrainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_billsum["train"],
    ...     eval_dataset=tokenized_billsum["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

## [](#inference) 推理

对于 T5，你需要根据任务在输入前添加前缀。对于摘要，你应该如下所示添加前缀：

    >>> text = "summarize: The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history..."

使用 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 进行推理：

    >>> from transformers import pipeline
    >>> summarizer = pipeline("summarization", model="username/my_awesome_billsum_model")
    >>> summarizer(text)

或手动进行推理：

    >>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_billsum_model")
    >>> inputs = tokenizer(text, return_tensors="pt").input_ids
    >>> model = AutoModelForSeq2SeqLM.from_pretrained("username/my_awesome_billsum_model")
    >>> outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
    >>> tokenizer.decode(outputs[0], skip_special_tokens=True)

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/summarization.md)

[←翻译](/docs/transformers/tasks/translation) [多项选择→](/docs/transformers/tasks/multiple_choice)

[摘要](#summarization)[加载 BillSum 数据集](#load-billsum-dataset)[预处理](#preprocess)[评估](#evaluate)[训练](#train)[推理](#inference)
