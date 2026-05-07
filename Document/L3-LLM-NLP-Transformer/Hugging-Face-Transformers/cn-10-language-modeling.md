[ Hugging Face](/)

Transformers 文档

因果语言建模

# Transformers

因果语言建模

语言建模有两种类型：因果（causal）和掩码（masked）。本指南说明因果语言建模。因果语言模型常用于文本生成。你可以将这些模型用于创意应用，如选择你自己的文字冒险或像 Copilot 或 CodeParrot 这样的智能编码助手。

因果语言建模预测词元序列中的下一个词元，模型只能关注左侧的词元。这意味着模型无法看到未来的词元。GPT-2 是因果语言模型的一个例子。

本指南将向你展示如何：

  1. 在 [ELI5](https://huggingface.co/datasets/dany0407/eli5_category) 数据集的 [r/askscience](https://www.reddit.com/r/askscience/) 子集上微调 [DistilGPT2](https://huggingface.co/distilbert/distilgpt2)。
  2. 使用微调后的模型进行推理。

## [](#load-eli5-dataset) 加载 ELI5 数据集

首先使用 🤗 Datasets 库从 [ELI5-Category](https://huggingface.co/datasets/dany0407/eli5_category) 数据集加载前 5000 个示例：

    >>> from datasets import load_dataset
    >>> eli5 = load_dataset("dany0407/eli5_category", split="train[:5000]")

使用 `train_test_split` 方法将数据集的 `train` 分割为训练集和测试集：

    >>> eli5 = eli5.train_test_split(test_size=0.2)

语言建模任务的妙处在于你不需要标签（也称为无监督任务），因为下一个词_就是_标签。

## [](#preprocess) 预处理

加载 DistilGPT2 分词器来处理 `text` 子字段：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")

使用 [`flatten`](https://huggingface.co/docs/datasets/process#flatten) 方法从嵌套结构中提取 `text` 子字段：

    >>> eli5 = eli5.flatten()

每个子字段现在是一个单独的列。创建第一个预处理函数来连接每个示例的字符串列表并对结果进行分词：

    >>> def preprocess_function(examples):
    ...     return tokenizer([" ".join(x) for x in examples["answers.text"]])

使用 🤗 Datasets 的 `map` 方法将此预处理函数应用于整个数据集：

    >>> tokenized_eli5 = eli5.map(
    ...     preprocess_function,
    ...     batched=True,
    ...     num_proc=4,
    ...     remove_columns=eli5["train"].column_names,
    ... )

现在使用第二个预处理函数来：

  * 连接所有序列
  * 将连接的序列拆分为由 `block_size` 定义的较短块

    >>> block_size = 128

    >>> def group_texts(examples):
    ...     concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    ...     total_length = len(concatenated_examples[list(examples.keys())[0]])
    ...     if total_length >= block_size:
    ...         total_length = (total_length // block_size) * block_size
    ...     result = {
    ...         k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
    ...         for k, t in concatenated_examples.items()
    ...     }
    ...     result["labels"] = result["input_ids"].copy()
    ...     return result

    >>> lm_dataset = tokenized_eli5.map(group_texts, batched=True, num_proc=4)

使用 [DataCollatorForLanguageModeling](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForLanguageModeling) 创建一批示例。使用序列结束词元作为填充词元，并设置 `mlm=False`：

    >>> from transformers import DataCollatorForLanguageModeling
    >>> tokenizer.pad_token = tokenizer.eos_token
    >>> data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

## [](#train) 训练

使用 [AutoModelForCausalLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForCausalLM) 加载 DistilGPT2：

    >>> from transformers import AutoModelForCausalLM, TrainingArguments, Trainer
    >>> model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

定义训练参数并开始训练：

    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_eli5_clm-model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     weight_decay=0.01,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=lm_dataset["train"],
    ...     eval_dataset=lm_dataset["test"],
    ...     data_collator=data_collator,
    ...     processing_class=tokenizer,
    ... )

    >>> trainer.train()

训练完成后，使用 [evaluate()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.evaluate) 方法评估模型并获取困惑度（perplexity）：

    >>> import math
    >>> eval_results = trainer.evaluate()
    >>> print(f"Perplexity: {math.exp(eval_results['eval_loss']):.2f}")
    Perplexity: 49.61

## [](#inference) 推理

使用 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 进行推理：

    >>> from transformers import pipeline

    >>> generator = pipeline("text-generation", model="username/my_awesome_eli5_clm-model")
    >>> generator("Somatic hypermutation allows the immune system to")

你也可以手动进行推理。对文本进行分词并将 `input_ids` 作为 PyTorch 张量返回：

    >>> from transformers import AutoTokenizer
    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_eli5_clm-model")
    >>> inputs = tokenizer(prompt, return_tensors="pt").input_ids

使用 [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) 方法生成文本：

    >>> from transformers import AutoModelForCausalLM
    >>> model = AutoModelForCausalLM.from_pretrained("username/my_awesome_eli5_clm-model")
    >>> outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)

解码生成的词元 ID 回文本：

    >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/language_modeling.md)

[←问答](/docs/transformers/tasks/question_answering) [掩码语言建模→](/docs/transformers/tasks/masked_language_modeling)

[因果语言建模](#causal-language-modeling)[加载 ELI5 数据集](#load-eli5-dataset)[预处理](#preprocess)[训练](#train)[推理](#inference)
