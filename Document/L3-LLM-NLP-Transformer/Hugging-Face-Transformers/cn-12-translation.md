[ Hugging Face](/)

Transformers 文档

翻译

# Transformers

翻译

翻译（Translation）将文本序列从一种语言转换为另一种语言。它是可以表述为序列到序列（sequence-to-sequence）问题的几种任务之一，是从输入返回输出的强大框架，如翻译或摘要。翻译系统通常用于不同语言文本之间的翻译，但它也可以用于语音或文本到语音、语音到文本等组合。

本指南将向你展示如何：

  1. 在 [OPUS Books](https://huggingface.co/datasets/opus_books) 数据集的英法子集上微调 [T5](https://huggingface.co/google-t5/t5-small) 将英语文本翻译为法语。
  2. 使用微调后的模型进行推理。

## [](#load-opus-books-dataset) 加载 OPUS Books 数据集

首先从 🤗 Datasets 库加载 [OPUS Books](https://huggingface.co/datasets/opus_books) 数据集的英法子集：

    >>> from datasets import load_dataset
    >>> books = load_dataset("opus_books", "en-fr")

使用 `train_test_split` 方法将数据集分为训练集和测试集：

    >>> books = books["train"].train_test_split(test_size=0.2)

`translation`：文本的英语和法语翻译。

## [](#preprocess) 预处理

加载 T5 分词器来处理英法语言对：

    >>> from transformers import AutoTokenizer
    >>> checkpoint = "google-t5/t5-small"
    >>> tokenizer = AutoTokenizer.from_pretrained(checkpoint)

你需要创建的预处理函数需要：

  1. 在输入前添加提示前缀，使 T5 知道这是翻译任务。
  2. 在 `text_target` 参数中设置目标语言（法语），确保分词器正确处理目标文本。
  3. 将序列截断为不超过 `max_length` 参数设置的最大长度。

    >>> source_lang = "en"
    >>> target_lang = "fr"
    >>> prefix = "translate English to French: "

    >>> def preprocess_function(examples):
    ...     inputs = [prefix + example[source_lang] for example in examples["translation"]]
    ...     targets = [example[target_lang] for example in examples["translation"]]
    ...     model_inputs = tokenizer(inputs, text_target=targets, max_length=128, truncation=True)
    ...     return model_inputs

使用 🤗 Datasets 的 `map` 方法将预处理函数应用于整个数据集：

    >>> tokenized_books = books.map(preprocess_function, batched=True)

使用 [DataCollatorForSeq2Seq](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForSeq2Seq) 创建一批示例：

    >>> from transformers import DataCollatorForSeq2Seq
    >>> data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)

## [](#evaluate) 评估

对于此任务，加载 [SacreBLEU](https://huggingface.co/spaces/evaluate-metric/sacrebleu) 指标：

    >>> import evaluate
    >>> metric = evaluate.load("sacrebleu")

创建一个函数将预测和标签传递给 [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) 来计算 SacreBLEU 分数：

    >>> import numpy as np

    >>> def postprocess_text(preds, labels):
    ...     preds = [pred.strip() for pred in preds]
    ...     labels = [[label.strip()] for label in labels]
    ...     return preds, labels

    >>> def compute_metrics(eval_preds):
    ...     preds, labels = eval_preds
    ...     if isinstance(preds, tuple):
    ...         preds = preds[0]
    ...     decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    ...     labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    ...     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    ...     decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)
    ...     result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    ...     result = {"bleu": result["score"]}
    ...     prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    ...     result["gen_len"] = np.mean(prediction_lens)
    ...     result = {k: round(v, 4) for k, v in result.items()}
    ...     return result

## [](#train) 训练

使用 [AutoModelForSeq2SeqLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSeq2SeqLM) 加载 T5：

    >>> from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
    >>> model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

定义训练参数并开始训练：

    >>> training_args = Seq2SeqTrainingArguments(
    ...     output_dir="my_awesome_opus_books_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     weight_decay=0.01,
    ...     save_total_limit=3,
    ...     num_train_epochs=2,
    ...     predict_with_generate=True,
    ...     fp16=True,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Seq2SeqTrainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_books["train"],
    ...     eval_dataset=tokenized_books["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

## [](#inference) 推理

对于从英语到法语的翻译，你应该如下所示为输入添加前缀：

    >>> text = "translate English to French: Legumes share resources with nitrogen-fixing bacteria."

使用 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 进行推理：

    >>> from transformers import pipeline
    >>> translator = pipeline("translation", model="username/my_awesome_opus_books_model")
    >>> translator(text)

或手动进行推理：

    >>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_opus_books_model")
    >>> inputs = tokenizer(text, return_tensors="pt").input_ids
    >>> model = AutoModelForSeq2SeqLM.from_pretrained("username/my_awesome_opus_books_model")
    >>> outputs = model.generate(inputs, max_new_tokens=40, do_sample=True, top_k=30, top_p=0.95)
    >>> tokenizer.decode(outputs[0], skip_special_tokens=True)

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/translation.md)

[←掩码语言建模](/docs/transformers/tasks/masked_language_modeling) [摘要→](/docs/transformers/tasks/summarization)

[翻译](#translation)[加载 OPUS Books 数据集](#load-opus-books-dataset)[预处理](#preprocess)[评估](#evaluate)[训练](#train)[推理](#inference)
