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

Transformers documentation

Transformers

# Transformers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv5.8.0v5.7.0v5.6.2v5.5.4v5.4.0v5.3.0v5.2.0v5.1.0v5.0.0v4.57.6v4.56.2v4.55.4v4.53.3v4.52.3v4.51.3v4.50.0v4.49.0v4.48.2v4.47.1v4.46.3v4.45.2v4.44.2v4.43.4v4.42.4v4.41.2v4.40.2v4.39.3v4.38.2v4.37.2v4.36.1v4.35.2v4.34.1v4.33.3v4.32.1v4.31.0v4.30.0v4.29.1v4.28.1v4.27.2v4.26.1v4.25.1v4.24.0v4.23.1v4.22.2v4.21.3v4.20.1v4.19.4v4.18.0v4.17.0v4.16.2v4.15.0v4.14.1v4.13.0v4.12.5v4.11.3v4.10.1v4.9.2v4.8.2v4.7.0v4.6.0v4.5.1v4.4.2v4.3.3v4.2.2v4.1.1v4.0.1v3.5.1v3.4.0v3.3.1v3.2.0v3.1.0v3.0.2v2.11.0v2.10.0v2.9.1v2.8.0v2.7.0v2.6.0v2.5.1v2.4.1v2.3.0v2.2.2v2.1.1v2.0.0v1.2.0v1.1.0v1.0.0doc-builder-html ARDEENESFRHIITJAKOPTTRZH

[ ](https://github.com/huggingface/transformers)

Get started

[Transformers](/docs/transformers/index)[Installation](/docs/transformers/installation)[Quickstart](/docs/transformers/quicktour)

Base classes

Models

Preprocessors

Inference

Pipeline API

Generate API

Optimization

Chat with models

Serving

Training

Get started

Customization

[Parameter-efficient fine-tuning](/docs/transformers/peft)

Performance

Distributed training

Hardware

Quantization

Ecosystem integrations

Resources

API

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#transformers) Transformers

###

Transformers acts as the model-definition framework for state-of-the-art machine learning models in text, computer vision, audio, video, and multimodal models, for both inference and training.

It centralizes the model definition so that this definition is agreed upon across the ecosystem. `transformers` is the pivot across frameworks: if a model definition is supported, it will be compatible with the majority of training frameworks (Axolotl, Unsloth, DeepSpeed, FSDP, PyTorch-Lightning, …), inference engines (vLLM, SGLang, TGI, …), and adjacent modeling libraries (llama.cpp, mlx, …) which leverage the model definition from `transformers`.

We pledge to help support new state-of-the-art models and democratize their usage by having their model definition be simple, customizable, and efficient.

There are over 1M+ Transformers [model checkpoints](https://huggingface.co/models?library=transformers&sort=trending) on the [Hugging Face Hub](https://huggingface.com/models) you can use.

Explore the [Hub](https://huggingface.com/) today to find a model and use Transformers to help you get started right away.

Explore the [Models Timeline](./models_timeline) to discover the latest text, vision, audio and multimodal model architectures in Transformers.

## [](#features) Features

Transformers provides everything you need for inference or training with state-of-the-art pretrained models. Some of the main features include:

  * [Pipeline](./pipeline_tutorial): Simple and optimized inference class for many machine learning tasks like text generation, image segmentation, automatic speech recognition, document question answering, and more.
  * [Trainer](./trainer): A comprehensive trainer that supports features such as mixed precision, torch.compile, and FlashAttention for training and distributed training for PyTorch models.
  * [generate](./llm_tutorial): Fast text generation with large language models (LLMs) and vision language models (VLMs), including support for streaming and multiple decoding strategies.

## [](#design) Design

> Read our [Philosophy](./philosophy) to learn more about Transformers’ design principles.

Transformers is designed for developers and machine learning engineers and researchers. Its main design principles are:

  1. Fast and easy to use: Every model is implemented from only three main classes (configuration, model, and preprocessor) and can be quickly used for inference or training with [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) or [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer).
  2. Pretrained models: Reduce your carbon footprint, compute cost and time by using a pretrained model instead of training an entirely new one. Each pretrained model is reproduced as closely as possible to the original model and offers state-of-the-art performance.

[](https://huggingface.co/support)

## [](#learn) Learn

If you’re new to Transformers or want to learn more about transformer models, we recommend starting with the [LLM course](https://huggingface.co/learn/llm-course/chapter1/1?fw=pt). This comprehensive course covers everything from the fundamentals of how transformer models work to practical applications across various tasks. You’ll learn the complete workflow, from curating high-quality datasets to fine-tuning large language models and implementing reasoning capabilities. The course contains both theoretical and hands-on exercises to build a solid foundational knowledge of transformer models as you learn.

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/index.md)

[Installation→](/docs/transformers/installation)

[Transformers](#transformers)[Features](#features)[Design](#design)[Learn](#learn)
