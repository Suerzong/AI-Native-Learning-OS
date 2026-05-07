[ Hugging Face](/)

  * [ Models ](/models)
  * [ Datasets ](/datasets)
  * [ Spaces ](/spaces)
  * [ Buckets new](/storage)
  * [ Docs ](/docs)
  * [ Enterprise ](/enterprise)
  * [Pricing](/pricing)
  *   * * * *

  * [Log In](/login)
  * [Sign Up](/join)

Transformers 文档

Transformers

# Transformers

Transformers 作为文本、计算机视觉、音频、视频和多模态模型的最先进机器学习模型定义框架，同时支持推理和训练。

它集中了模型定义，使得该定义在整个生态系统中得到统一。`transformers` 是跨框架的枢纽：如果支持某个模型定义，它将与大多数训练框架（Axolotl、Unsloth、DeepSpeed、FSDP、PyTorch-Lightning 等）、推理引擎（vLLM、SGLang、TGI 等）以及相邻的建模库（llama.cpp、mlx 等）兼容，这些框架都利用了 `transformers` 的模型定义。

我们致力于支持新的最先进模型，通过使模型定义简单、可定制且高效来普及其使用。

[Hugging Face Hub](https://huggingface.com/models) 上有超过 100 万个 Transformers [模型检查点](https://huggingface.co/models?library=transformers&sort=trending)可供使用。

立即探索 [Hub](https://huggingface.com/)，找到一个模型并使用 Transformers 帮助你快速上手。

探索 [模型时间线](./models_timeline)，发现 Transformers 中最新的文本、视觉、音频和多模态模型架构。

## [](#features) 特性

Transformers 提供了使用最先进预训练模型进行推理或训练所需的一切。主要特性包括：

  * [Pipeline](./pipeline_tutorial)：简单且优化的推理类，适用于多种机器学习任务，如文本生成、图像分割、自动语音识别、文档问答等。
  * [Trainer](./trainer)：全面的训练器，支持混合精度、torch.compile 和 FlashAttention 等功能，用于 PyTorch 模型的训练和分布式训练。
  * [generate](./llm_tutorial)：使用大语言模型（LLM）和视觉语言模型（VLM）进行快速文本生成，支持流式传输和多种解码策略。

## [](#design) 设计

> 阅读我们的[设计理念](./philosophy)以了解更多关于 Transformers 的设计原则。

Transformers 面向开发者和机器学习工程师及研究人员设计。其主要设计原则是：

  1. 快速且易于使用：每个模型仅由三个主要类（配置、模型和预处理器）实现，可以使用 [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) 或 [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) 快速用于推理或训练。
  2. 预训练模型：通过使用预训练模型代替从头训练全新的模型，减少碳足迹、计算成本和时间。每个预训练模型都尽可能忠实地复现原始模型，并提供最先进的性能。

## [](#learn) 学习

如果你是 Transformers 新手或想了解更多关于 Transformer 模型的知识，我们建议从 [LLM 课程](https://huggingface.co/learn/llm-course/chapter1/1?fw=pt)开始。这个全面的课程涵盖了从 Transformer 模型工作原理的基础知识到各种任务的实际应用。你将学习完整的工作流程，从策划高质量数据集到微调大语言模型和实现推理能力。该课程包含理论和实践练习，在学习过程中为你建立扎实的 Transformer 模型基础知识。

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/index.md)

[安装→](/docs/transformers/installation)

[Transformers](#transformers)[特性](#features)[设计](#design)[学习](#learn)
