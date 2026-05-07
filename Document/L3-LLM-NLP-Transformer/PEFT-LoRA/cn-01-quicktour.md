[ Hugging Face](/)

PEFT 文档

快速入门

# PEFT

快速入门

PEFT 为微调大型预训练模型提供了参数高效的方法。传统范式是为每个下游任务微调模型的所有参数，但这在当今模型的巨大参数量下变得极其昂贵和不切实际。相反，训练较少数量的提示参数或使用重参数化方法（如低秩适配 LoRA）来减少可训练参数数量更为高效。

本快速入门将向你展示 PEFT 的主要功能，以及如何在消费级设备上通常无法访问的大型模型上进行训练或推理。

## [](#train) 训练

每种 PEFT 方法由 [PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig) 类定义，该类存储构建 [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) 的所有重要参数。例如，要使用 LoRA 进行训练，加载并创建 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 类并指定以下参数：

  * `task_type`：要训练的任务（本例中为序列到序列语言建模）
  * `inference_mode`：是否将模型用于推理
  * `r`：低秩矩阵的维度
  * `lora_alpha`：低秩矩阵的缩放因子
  * `lora_dropout`：LoRA 层的 dropout 概率

    from peft import LoraConfig, TaskType

    peft_config = LoraConfig(task_type=TaskType.SEQ_2_SEQ_LM, inference_mode=False, r=8, lora_alpha=32, lora_dropout=0.1)

设置好 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 后，使用 [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) 函数创建 [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)。它接受一个基础模型（可以从 Transformers 库加载）和包含如何配置模型进行 LoRA 训练参数的 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig)。

加载要微调的基础模型。

    from transformers import AutoModelForSeq2SeqLM

    model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/mt0-large")

使用 [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) 函数包装基础模型和 `peft_config` 以创建 [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)。要了解模型中可训练参数的数量，使用 `print_trainable_parameters` 方法。

    from peft import get_peft_model

    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    "output: trainable params: 2359296 || all params: 1231940608 || trainable%: 0.19151053100118282"

在 [bigscience/mt0-large](https://huggingface.co/bigscience/mt0-large) 的 1.2B 参数中，你只训练了 0.19%！

就是这样！现在你可以使用 Transformers [Trainer](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer)、Accelerate 或任何自定义 PyTorch 训练循环来训练模型。

例如，使用 [Trainer](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer) 类训练：

    training_args = TrainingArguments(
        output_dir="your-name/bigscience/mt0-large-lora",
        learning_rate=1e-3,
        per_device_train_batch_size=32,
        per_device_eval_batch_size=32,
        num_train_epochs=2,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        processing_class=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    trainer.train()

### [](#save-model) 保存模型

训练完成后，使用 [save_pretrained](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.save_pretrained) 函数将模型保存到目录。

    model.save_pretrained("output_dir")

你也可以使用 [push_to_hub](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.push_to_hub) 函数将模型保存到 Hub。

    from huggingface_hub import notebook_login

    notebook_login()
    model.push_to_hub("your-name/bigscience/mt0-large-lora")

两种方法仅保存训练过的额外 PEFT 权重，这意味着存储、传输和加载都非常高效。例如，这个用 LoRA 训练的 [facebook/opt-350m](https://huggingface.co/ybelkada/opt-350m-lora) 模型只包含两个文件：`adapter_config.json` 和 `adapter_model.safetensors`。`adapter_model.safetensors` 文件只有 6.3MB！

## [](#inference) 推理

使用 [AutoPeftModel](/docs/peft/v0.19.0/en/package_reference/auto_class#peft.AutoPeftModel) 类和 [from_pretrained](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 方法轻松加载任何 PEFT 训练的模型进行推理：

    from peft import AutoPeftModelForCausalLM
    from transformers import AutoTokenizer
    import torch

    model = AutoPeftModelForCausalLM.from_pretrained("ybelkada/opt-350m-lora")
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")

    model = model.to("cuda")
    model.eval()
    inputs = tokenizer("Preheat the oven to 350 degrees and place the cookie dough", return_tensors="pt")

    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"), max_new_tokens=50)
    print(tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0])

    "Preheat the oven to 350 degrees and place the cookie dough in the center of the oven..."

## [](#next-steps) 后续步骤

现在你已经看到了如何使用 PEFT 方法之一训练模型，我们鼓励你尝试其他方法，如提示微调（prompt tuning）。步骤与快速入门中展示的非常相似：

  1. 为 PEFT 方法准备 [PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)
  2. 使用 [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) 方法从配置和基础模型创建 [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)

然后你可以按你喜欢的方式训练它！要加载 PEFT 模型进行推理，可以使用 [AutoPeftModel](/docs/peft/v0.19.0/en/package_reference/auto_class#peft.AutoPeftModel) 类。

[ 在 GitHub 上更新](https://github.com/huggingface/peft/blob/main/docs/source/quicktour.md)

[←🤗 PEFT](/docs/peft/index) [安装→](/docs/peft/install)

[快速入门](#quicktour)[训练](#train)[保存模型](#save-model)[推理](#inference)[后续步骤](#next-steps)
