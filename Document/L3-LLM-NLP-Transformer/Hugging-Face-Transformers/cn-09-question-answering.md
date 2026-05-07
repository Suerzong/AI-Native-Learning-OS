[ Hugging Face](/)

Transformers 文档

问答

# Transformers

问答

问答（Question answering）任务在给定问题的情况下返回答案。如果你曾经问过 Alexa、Siri 或 Google 天气如何，那么你之前就使用过问答模型。有两种常见的问答任务类型：

  * 抽取式（Extractive）：从给定上下文中提取答案。
  * 生成式（Abstractive）：从上下文中生成正确回答问题的答案。

本指南将向你展示如何：

  1. 在 [SQuAD](https://huggingface.co/datasets/squad) 数据集上微调 [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) 进行抽取式问答。
  2. 使用微调后的模型进行推理。

## [](#load-squad-dataset) 加载 SQuAD 数据集

首先从 🤗 Datasets 库加载 SQuAD 数据集的较小子集：

    >>> from datasets import load_dataset
    >>> squad = load_dataset("squad", split="train[:5000]")

使用 `train_test_split` 方法将数据集的 `train` 分割为训练集和测试集：

    >>> squad = squad.train_test_split(test_size=0.2)

此数据集有几个重要字段：

  * `answers`：答案词元的起始位置和答案文本。
  * `context`：模型需要从中提取答案的背景信息。
  * `question`：模型应回答的问题。

## [](#preprocess) 预处理

加载 DistilBERT 分词器来处理 `question` 和 `context` 字段：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

问答任务有一些特定的预处理步骤：

  1. 数据集中的一些示例可能有非常长的 `context`，超过模型的最大输入长度。通过设置 `truncation="only_second"` 来仅截断 `context`。
  2. 通过设置 `return_offset_mapping=True` 将答案的起始和结束位置映射到原始 `context`。
  3. 使用 `sequence_ids` 方法查找偏移的哪部分对应 `question`，哪部分对应 `context`。

    >>> def preprocess_function(examples):
    ...     questions = [q.strip() for q in examples["question"]]
    ...     inputs = tokenizer(
    ...         questions,
    ...         examples["context"],
    ...         max_length=384,
    ...         truncation="only_second",
    ...         return_offsets_mapping=True,
    ...         padding="max_length",
    ...     )
    ...     offset_mapping = inputs.pop("offset_mapping")
    ...     answers = examples["answers"]
    ...     start_positions = []
    ...     end_positions = []
    ...     for i, offset in enumerate(offset_mapping):
    ...         answer = answers[i]
    ...         start_char = answer["answer_start"][0]
    ...         end_char = answer["answer_start"][0] + len(answer["text"][0])
    ...         sequence_ids = inputs.sequence_ids(i)
    ...         idx = 0
    ...         while sequence_ids[idx] != 1:
    ...             idx += 1
    ...         context_start = idx
    ...         while sequence_ids[idx] == 1:
    ...             idx += 1
    ...         context_end = idx - 1
    ...         if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
    ...             start_positions.append(0)
    ...             end_positions.append(0)
    ...         else:
    ...             idx = context_start
    ...             while idx <= context_end and offset[idx][0] <= start_char:
    ...                 idx += 1
    ...             start_positions.append(idx - 1)
    ...             idx = context_end
    ...             while idx >= context_start and offset[idx][1] >= end_char:
    ...                 idx -= 1
    ...             end_positions.append(idx + 1)
    ...     inputs["start_positions"] = start_positions
    ...     inputs["end_positions"] = end_positions
    ...     return inputs

使用 🤗 Datasets 的 `map` 函数将预处理函数应用于整个数据集：

    >>> tokenized_squad = squad.map(preprocess_function, batched=True, remove_columns=squad["train"].column_names)

使用 [DefaultDataCollator](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DefaultDataCollator) 创建一批示例：

    >>> from transformers import DefaultDataCollator
    >>> data_collator = DefaultDataCollator()

## [](#train) 训练

使用 [AutoModelForQuestionAnswering](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForQuestionAnswering) 加载 DistilBERT：

    >>> from transformers import AutoModelForQuestionAnswering, TrainingArguments, Trainer
    >>> model = AutoModelForQuestionAnswering.from_pretrained("distilbert/distilbert-base-uncased")

定义训练参数并开始训练：

    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_qa_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=3,
    ...     weight_decay=0.01,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_squad["train"],
    ...     eval_dataset=tokenized_squad["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ... )

    >>> trainer.train()

## [](#evaluate) 评估

问答的评估需要大量的后处理。为避免占用太多时间，本指南跳过评估步骤。[Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) 仍会在训练期间计算评估损失，因此你并非完全不了解模型性能。

## [](#inference) 推理

很好，现在你已经微调了模型，可以使用它进行推理！

提出一个你想让模型预测的问题和一些上下文：

    >>> question = "How many programming languages does BLOOM support?"
    >>> context = "BLOOM has 176 billion parameters and can generate text in 46 languages natural languages and 13 programming languages."

对文本进行分词并返回 PyTorch 张量：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("my_awesome_qa_model")
    >>> inputs = tokenizer(question, context, return_tensors="pt")

将输入传递给模型并返回 `logits`：

    >>> import torch
    >>> from transformers import AutoModelForQuestionAnswering
    >>> model = AutoModelForQuestionAnswering.from_pretrained("my_awesome_qa_model")
    >>> with torch.no_grad():
    ...     outputs = model(**inputs)

获取模型输出中起始和结束位置的最高概率：

    >>> answer_start_index = outputs.start_logits.argmax()
    >>> answer_end_index = outputs.end_logits.argmax()

解码预测的词元以获取答案：

    >>> predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    >>> tokenizer.decode(predict_answer_tokens)
    '176 billion parameters and can generate text in 46 languages natural languages and 13'

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/question_answering.md)

[←词元分类](/docs/transformers/tasks/token_classification) [因果语言建模→](/docs/transformers/tasks/language_modeling)

[问答](#question-answering)[加载 SQuAD 数据集](#load-squad-dataset)[预处理](#preprocess)[训练](#train)[评估](#evaluate)[推理](#inference)
