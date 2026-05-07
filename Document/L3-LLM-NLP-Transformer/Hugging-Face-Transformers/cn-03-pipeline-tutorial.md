[ Hugging Face](/)

Transformers 文档

Pipeline

# Transformers

Pipeline

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 是一个简单但强大的推理 API，可与 Hugging Face [Hub](https://hf.co/models) 上的任何模型一起用于各种机器学习任务。

使用任务特定参数定制 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)，例如为自动语音识别（ASR）Pipeline 添加时间戳以转录会议记录。[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 支持 GPU、Apple Silicon 和半精度权重以加速推理并节省内存。

Transformers 有两个 Pipeline 类：通用的 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 和许多独立的特定任务 Pipeline，如 [TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextGenerationPipeline)。通过在 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 的 `task` 参数中设置任务标识符来加载这些独立的 Pipeline。你可以在各自的 API 文档中找到每个 Pipeline 的任务标识符。

每个任务配置为使用默认的预训练模型和预处理器，但如果你想使用不同的模型，可以使用 `model` 参数覆盖。

例如，要使用 [TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextGenerationPipeline) 和 [Gemma 2](./model_doc/gemma2)，设置 `task="text-generation"` 和 `model="google/gemma-2-2b"`。

    from transformers import pipeline

    pipeline = pipeline(task="text-generation", model="google/gemma-2-2b")
    pipeline("the secret to baking a really good cake is ")
    [{'generated_text': 'the secret to baking a really good cake is 1. the right ingredients 2. the'}]

当你有多个输入时，将它们作为列表传递。

    from transformers import pipeline
    from accelerate import Accelerator

    device = Accelerator().device

    pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device=device)
    pipeline(["the secret to baking a really good cake is ", "a baguette is "])
    [[{'generated_text': 'the secret to baking a really good cake is 1. the right ingredients 2. the'}],
     [{'generated_text': 'a baguette is 100% bread.\n\na baguette is 100%'}]]

本指南将向你介绍 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)、展示其功能，并展示如何配置其各种参数。

## [](#tasks) 任务

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 兼容不同模态的多种机器学习任务。向 Pipeline 传递适当的输入，它将处理其余部分。

以下是一些关于如何将 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 用于不同任务和模态的示例。

    from transformers import pipeline

    pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
    pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
    {'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}

## [](#parameters) 参数

至少，[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 只需要一个任务标识符、模型和适当的输入。但有许多参数可用于配置 Pipeline，从任务特定参数到优化性能。

本节介绍一些更重要的参数。

### [](#device) 设备

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 兼容多种硬件类型，包括 GPU、CPU、Apple Silicon 等。使用 `device` 参数配置硬件类型。默认情况下，[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 在 CPU 上运行，由 `device=-1` 指定。

要在 GPU 上运行 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)，将 `device` 设置为相关的 CUDA 设备 ID。例如，`device=0` 在第一个 GPU 上运行。

    from transformers import pipeline

    pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device=0)
    pipeline("the secret to baking a really good cake is ")

你也可以让 [Accelerate](https://hf.co/docs/accelerate/index)（一个用于分布式训练的库）自动选择如何在适当的设备上加载和存储模型权重。如果你有多个设备，这尤其有用。Accelerate 首先在最快的设备上加载和存储模型权重，然后根据需要将权重移动到其他设备（CPU、硬盘）。设置 `device_map="auto"` 让 Accelerate 选择设备。

> 确保已安装 [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install)。
>
>     !pip install -U accelerate

    from transformers import pipeline

    pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device_map="auto")
    pipeline("the secret to baking a really good cake is ")

### [](#batch-inference) 批量推理

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 也可以使用 `batch_size` 参数处理批量输入。批量推理可能会提高速度，尤其是在 GPU 上，但不能保证。其他变量（如硬件、数据和模型本身）会影响批量推理是否能提高速度。因此，默认禁用批量推理。

在下面的示例中，当有 4 个输入且 `batch_size` 设置为 2 时，[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 每次将 2 个输入作为一批传递给模型。

    from transformers import pipeline
    from accelerate import Accelerator

    device = Accelerator().device

    pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device=device, batch_size=2)
    pipeline(["the secret to baking a really good cake is", "a baguette is", "paris is the", "hotdogs are"])

以下是一些确定批量推理是否有助于提高性能的一般经验法则。

  1. 确定的唯一方法是测量你的模型、数据和硬件上的性能。
  2. 如果你受延迟约束（例如实时推理产品），请不要进行批量推理。
  3. 如果你使用 CPU，请不要进行批量推理。
  4. 如果你不知道数据的 `sequence_length`，请不要进行批量推理。测量性能，逐步增加 `sequence_length`，并包含内存不足（OOM）检查以从失败中恢复。
  5. 如果你的 `sequence_length` 规则，请进行批量推理，并不断增大直到出现 OOM 错误。GPU 越大，批量推理越有帮助。
  6. 如果你决定进行批量推理，请确保能够处理 OOM 错误。

### [](#task-specific-parameters) 任务特定参数

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 接受每个任务 Pipeline 支持的任何参数。请务必查看每个独立的任务 Pipeline 以了解可用的参数类型。如果找不到对你的用例有用的参数，请随时在 GitHub 上提交 [issue](https://github.com/huggingface/transformers/issues/new?assignees=&labels=feature&template=feature-request.yml) 进行请求！

以下示例展示了一些可用的任务特定参数。

传递 `return_timestamps="word"` 参数给 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 以返回每个单词被说出的时间。

    from transformers import pipeline

    pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
    pipeline(audio="https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac", return_timestamp="word")

## [](#chunk-batching) 分块批量处理

在某些情况下，你需要以分块方式处理数据。

  * 对于某些数据类型，单个输入（例如，一个非常长的音频文件）可能需要分块成多个部分才能处理
  * 对于某些任务（如零样本文本分类或问答），单个输入可能需要多次前向传播，这可能导致 `batch_size` 参数出现问题

[ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) 类旨在处理这些用例。两个 Pipeline 类的使用方式相同，但由于 [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) 可以自动处理批量，你不需要担心输入触发的前向传播次数。相反，你可以独立于输入优化 `batch_size`。

下面的示例展示了它与 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 的区别。

    # ChunkPipeline
    all_model_outputs = []
    for preprocessed in pipeline.preprocess(inputs):
        model_outputs = pipeline.model_forward(preprocessed)
        all_model_outputs.append(model_outputs)
    outputs =pipeline.postprocess(all_model_outputs)

    # Pipeline
    preprocessed = pipeline.preprocess(inputs)
    model_outputs = pipeline.forward(preprocessed)
    outputs = pipeline.postprocess(model_outputs)

## [](#large-datasets) 大型数据集

对于大型数据集的推理，你可以直接在数据集本身上迭代。这避免了立即为整个数据集分配内存，你也不需要自己创建批次。尝试使用 `batch_size` 参数进行[批量推理](#batch-inference)以查看是否能提高性能。

    from transformers.pipelines.pt_utils import KeyDataset
    from transformers import pipeline
    from accelerate import Accelerator
    from datasets import load_dataset

    device = Accelerator().device

    dataset = datasets.load_dataset("imdb", name="plain_text", split="unsupervised")
    pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=device)
    for out in pipeline(KeyDataset(dataset, "text"), batch_size=8, truncation="only_first"):
        print(out)

其他在大型数据集上使用 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 运行推理的方法包括使用迭代器或生成器。

    def data():
        for i in range(1000):
            yield f"My example {i}"

    pipeline = pipeline(model="openai-community/gpt2", device=0)
    generated_characters = 0
    for out in pipeline(data()):
        generated_characters += len(out[0]["generated_text"])

## [](#large-models) 大型模型

[Accelerate](https://hf.co/docs/accelerate/index) 为使用 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 运行大型模型提供了多种优化。首先确保安装了 Accelerate。

    !pip install -U accelerate

`device_map="auto"` 设置对于自动将模型分布到最快的设备（GPU）上非常有用，然后再分配到其他较慢的设备（CPU、硬盘）。

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 支持半精度权重（torch.float16），这可以显著加快速度并节省内存。对于大多数模型，性能损失可以忽略不计，尤其是较大的模型。如果你的硬件支持，可以启用 torch.bfloat16 以获得更大的范围。

> 输入在内部转换为 torch.float16，仅适用于具有 PyTorch 后端的模型。

最后，[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 也接受量化模型以进一步减少内存使用。确保首先安装了 [bitsandbytes](https://hf.co/docs/bitsandbytes/installation) 库，然后将 `quantization_config` 添加到 Pipeline 的 `model_kwargs` 中。

    import torch
    from transformers import pipeline, BitsAndBytesConfig

    pipeline = pipeline(model="google/gemma-7b", dtype=torch.bfloat16, device_map="auto", model_kwargs={"quantization_config": BitsAndBytesConfig(load_in_8bit=True)})
    pipeline("the secret to baking a good cake is ")
    [{'generated_text': 'the secret to baking a good cake is 1. the right ingredients 2. the right'}]

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/pipeline_tutorial.md)

[←处理器](/docs/transformers/processors) [机器学习应用→](/docs/transformers/pipeline_gradio)

[Pipeline](#pipeline)[任务](#tasks)[参数](#parameters)[设备](#device)[批量推理](#batch-inference)[任务特定参数](#task-specific-parameters)[分块批量处理](#chunk-batching)[大型数据集](#large-datasets)[大型模型](#large-models)
