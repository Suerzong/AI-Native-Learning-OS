[ Hugging Face](/)

Transformers 文档

快速入门

# Transformers

快速入门

Transformers 设计得快速且易于使用，让每个人都可以开始学习或构建 Transformer 模型。

面向用户的抽象数量有限，仅包括用于实例化模型的三个类和用于推理或训练的两个 API。本快速入门介绍 Transformers 的关键特性，并展示如何：

  * 加载预训练模型
  * 使用 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 运行推理
  * 使用 [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) 微调模型

## [](#set-up) 环境搭建

首先，我们建议创建一个 Hugging Face [账户](https://hf.co/join)。拥有账户后，你可以在 Hugging Face [Hub](https://hf.co/docs/hub/index)（一个用于发现和构建的协作平台）上托管和访问版本控制的模型、数据集和 [Spaces](https://hf.co/spaces)。

创建 [用户访问令牌](https://hf.co/docs/hub/security-tokens#user-access-tokens) 并登录你的账户。

安装 PyTorch。

    !pip install torch

然后安装最新版本的 Transformers 以及来自 Hugging Face 生态系统的一些额外库，用于访问数据集和视觉模型、评估训练以及为大型模型优化训练。

    !pip install -U transformers datasets evaluate accelerate timm

## [](#pretrained-models) 预训练模型

每个预训练模型都继承自三个基类。

**类** | **描述**
---|---
[PreTrainedConfig](/docs/transformers/v5.8.0/en/main_classes/configuration#transformers.PreTrainedConfig) | 指定模型属性的文件，例如注意力头数量或词汇表大小。
[PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel) | 由配置文件中的模型属性定义的模型（或架构）。预训练模型仅返回原始隐藏状态。对于特定任务，请使用适当的模型头部将原始隐藏状态转换为有意义的结果（例如，[LlamaModel](/docs/transformers/v5.8.0/en/model_doc/llama2#transformers.LlamaModel) 与 [LlamaForCausalLM](/docs/transformers/v5.8.0/en/model_doc/llama2#transformers.LlamaForCausalLM)）。
预处理器 | 用于将原始输入（文本、图像、音频、多模态）转换为模型数值输入的类。例如，[PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend) 将文本转换为张量，[ImageProcessingMixin](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.ImageProcessingMixin) 将像素转换为张量。

我们建议使用 [AutoClass](./model_doc/auto) API 加载模型和预处理器，因为它可以根据预训练权重和配置文件的名称或路径自动推断每个任务和机器学习框架的适当架构。

使用 [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 从 Hub 将权重和配置文件加载到模型和预处理器类中。

加载模型时，配置以下参数以确保模型以最优方式加载。

  * `device_map="auto"` 自动首先将模型权重分配到最快的设备。
  * `dtype="auto"` 直接以权重存储的数据类型初始化模型权重，这有助于避免两次加载权重（PyTorch 默认以 `torch.float32` 加载权重）。

    from transformers import AutoModelForCausalLM, AutoTokenizer

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", dtype="auto", device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

使用分词器对文本进行分词并返回 PyTorch 张量。如果有加速器可用，将模型移至加速器以加速推理。

    model_inputs = tokenizer(["The secret to baking a good cake is "], return_tensors="pt").to(model.device)

模型现在已准备好进行推理或训练。

对于推理，将分词后的输入传递给 [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) 以生成文本。使用 [batch_decode()](/docs/transformers/v5.8.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode) 将词元 ID 解码回文本。

    generated_ids = model.generate(**model_inputs, max_length=30)
    tokenizer.batch_decode(generated_ids)[0]
    '<s> The secret to baking a good cake is 100% in the preparation. There are so many recipes out there,'

> 跳转到 [Trainer](#trainer-api) 部分了解如何微调模型。

## [](#pipeline) Pipeline

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 类是使用预训练模型进行推理最便捷的方式。它支持多种任务，如文本生成、图像分割、自动语音识别、文档问答等。

> 请参阅 [Pipeline](./main_classes/pipelines) API 参考以获取可用任务的完整列表。

创建 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 对象并选择一个任务。默认情况下，[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 会为给定任务下载并缓存默认的预训练模型。将模型名称传递给 `model` 参数以选择特定模型。

    from transformers import pipeline
    from accelerate import Accelerator

    device = Accelerator().device

    pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf", device=device)

使用一些初始文本提示 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 生成更多文本。

    pipeline("The secret to baking a good cake is ", max_length=50)
    [{'generated_text': 'The secret to baking a good cake is 100% in the batter. The secret to a great cake is the icing.\nThis is why we\'ve created the best buttercream frosting reci'}]

## [](#trainer) Trainer

[Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) 是 PyTorch 模型的完整训练和评估循环。它抽象了通常手动编写训练循环涉及的大量样板代码，因此你可以更快地开始训练并专注于训练设计选择。你只需要一个模型、数据集、预处理器和数据整理器来从数据集构建批次。

使用 [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments) 类自定义训练过程。它提供了许多用于训练、评估等的选项。尝试训练超参数和功能，如批量大小、学习率、混合精度、torch.compile 等，以满足你的训练需求。你也可以使用默认训练参数快速生成基线。

加载用于训练的模型、分词器和数据集。

    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from datasets import load_dataset

    model = AutoModelForSequenceClassification.from_pretrained("distilbert/distilbert-base-uncased")
    tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
    dataset = load_dataset("rotten_tomatoes")

创建一个函数对文本进行分词并转换为 PyTorch 张量。使用 `map` 方法将此函数应用于整个数据集。

    def tokenize_dataset(dataset):
        return tokenizer(dataset["text"])
    dataset = dataset.map(tokenize_dataset, batched=True)

加载数据整理器以创建数据批次，并将分词器传递给它。

    from transformers import DataCollatorWithPadding

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

接下来，使用训练功能和超参数设置 [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments)。

    from transformers import TrainingArguments

    training_args = TrainingArguments(
        output_dir="distilbert-rotten-tomatoes",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=2,
        push_to_hub=True,
    )

最后，将所有这些独立的组件传递给 [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) 并调用 [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) 开始训练。

    from transformers import Trainer

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()

使用 [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) 将你的模型和分词器共享到 Hub。

    trainer.push_to_hub()

恭喜，你刚刚使用 Transformers 训练了你的第一个模型！

## [](#next-steps) 后续步骤

现在你对 Transformers 及其功能有了更好的理解，是时候继续探索并学习你最感兴趣的内容了。

  * **基类** ：了解更多关于配置、模型和处理器类的信息。这将帮助你理解如何创建和自定义模型，预处理不同类型的输入（音频、图像、多模态），以及如何共享你的模型。
  * **推理** ：进一步探索 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)、使用 LLM 进行推理和聊天、智能体，以及如何使用机器学习框架和硬件优化推理。
  * **训练** ：更详细地学习 [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer)，以及分布式训练和在特定硬件上优化训练。
  * **量化（Quantization）** ：通过量化减少内存和存储需求，并通过用更少的位表示权重来加速推理。
  * **资源** ：寻找如何针对特定任务使用模型进行训练和推理的端到端实践手册？查看任务手册！

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/quicktour.md)

[←安装](/docs/transformers/installation) [动态权重加载→](/docs/transformers/weightconverter)

[快速入门](#quickstart)[环境搭建](#set-up)[预训练模型](#pretrained-models)[Pipeline](#pipeline)[Trainer](#trainer)[后续步骤](#next-steps)
