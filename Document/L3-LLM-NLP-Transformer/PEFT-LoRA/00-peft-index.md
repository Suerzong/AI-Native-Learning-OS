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

PEFT documentation

PEFT

# PEFT

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv0.19.0v0.18.0v0.17.0v0.16.0v0.15.0v0.14.0v0.13.0v0.12.0v0.11.0v0.10.0v0.9.0v0.8.2v0.7.1v0.6.2 EN

[ ](https://github.com/huggingface/peft)

Get started

[🤗 PEFT](/docs/peft/index)[Quicktour](/docs/peft/quicktour)[Installation](/docs/peft/install)

Tutorial

[Configurations and models](/docs/peft/tutorial/peft_model_config)[Integrations](/docs/peft/tutorial/peft_integrations)

PEFT method guides

[Prompt-based methods](/docs/peft/task_guides/prompt_based_methods)[LoRA methods](/docs/peft/task_guides/lora_based_methods)[IA3](/docs/peft/task_guides/ia3)

Developer guides

[Model merging](/docs/peft/developer_guides/model_merging)[Quantization](/docs/peft/developer_guides/quantization)[LoRA](/docs/peft/developer_guides/lora)[Custom models](/docs/peft/developer_guides/custom_models)[Adapter injection](/docs/peft/developer_guides/low_level_api)[Mixed adapter types](/docs/peft/developer_guides/mixed_models)[torch.compile](/docs/peft/developer_guides/torch_compile)[Contribute to PEFT](/docs/peft/developer_guides/contributing)[Troubleshooting](/docs/peft/developer_guides/troubleshooting)[PEFT checkpoint format](/docs/peft/developer_guides/checkpoint)

🤗 Accelerate integrations

[DeepSpeed](/docs/peft/accelerate/deepspeed)[Fully Sharded Data Parallel](/docs/peft/accelerate/fsdp)

Conceptual guides

[Adapters](/docs/peft/conceptual_guides/adapter)[Soft prompts](/docs/peft/conceptual_guides/prompting)[IA3](/docs/peft/conceptual_guides/ia3)[OFT/BOFT](/docs/peft/conceptual_guides/oft)

API reference

Main classes

[AutoPeftModel](/docs/peft/package_reference/auto_class)[PEFT model](/docs/peft/package_reference/peft_model)[PEFT types](/docs/peft/package_reference/peft_types)[Configuration](/docs/peft/package_reference/config)[Tuner](/docs/peft/package_reference/tuners)

Adapters

[AdaLoRA](/docs/peft/package_reference/adalora)[AdaMSS](/docs/peft/package_reference/adamss)[IA3](/docs/peft/package_reference/ia3)[Llama-Adapter](/docs/peft/package_reference/llama_adapter)[LoHa](/docs/peft/package_reference/loha)[LoKr](/docs/peft/package_reference/lokr)[LoRA](/docs/peft/package_reference/lora)[OSF](/docs/peft/package_reference/osf)[X-LoRA](/docs/peft/package_reference/xlora)[LyCORIS](/docs/peft/package_reference/adapter_utils)[Multitask Prompt Tuning](/docs/peft/package_reference/multitask_prompt_tuning)[OFT](/docs/peft/package_reference/oft)[BOFT](/docs/peft/package_reference/boft)[PSOFT](/docs/peft/package_reference/psoft)[Polytropon](/docs/peft/package_reference/poly)[P-tuning](/docs/peft/package_reference/p_tuning)[Prefix tuning](/docs/peft/package_reference/prefix_tuning)[Cartridges](/docs/peft/package_reference/cartridges)[Prompt tuning](/docs/peft/package_reference/prompt_tuning)[Layernorm tuning](/docs/peft/package_reference/layernorm_tuning)[VeRA](/docs/peft/package_reference/vera)[PVeRA](/docs/peft/package_reference/pvera)[FourierFT](/docs/peft/package_reference/fourierft)[GraLoRA](/docs/peft/package_reference/gralora)[VB-LoRA](/docs/peft/package_reference/vblora)[HRA](/docs/peft/package_reference/hra)[CPT](/docs/peft/package_reference/cpt)[Trainable Tokens](/docs/peft/package_reference/trainable_tokens)[RandLora](/docs/peft/package_reference/randlora)[SHiRA](/docs/peft/package_reference/shira)[C3A](/docs/peft/package_reference/c3a)[MiSS](/docs/peft/package_reference/miss)[RoAd](/docs/peft/package_reference/road)[WaveFT](/docs/peft/package_reference/waveft)[DeLoRA](/docs/peft/package_reference/delora)[TinyLoRA](/docs/peft/package_reference/tinylora)[Lily](/docs/peft/package_reference/lily)[PEANuT](/docs/peft/package_reference/peanut)

Utilities

[Model merge](/docs/peft/package_reference/merge_utils)[Helpers](/docs/peft/package_reference/helpers)[Hotswapping adapters](/docs/peft/package_reference/hotswap)[Functions for PEFT integration](/docs/peft/package_reference/functional)[Converting non-LoRA adapters to LoRA](/docs/peft/package_reference/lora_conversion)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#peft) PEFT

🤗 PEFT (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting large pretrained models to various downstream applications without fine-tuning all of a model’s parameters because it is prohibitively costly. PEFT methods only fine-tune a small number of (extra) model parameters - significantly decreasing computational and storage costs - while yielding performance comparable to a fully fine-tuned model. This makes it more accessible to train and store large language models (LLMs) on consumer hardware.

PEFT is integrated with the Transformers, Diffusers, and Accelerate libraries to provide a faster and easier way to load, train, and use large models for inference.

[Quicktour Start here if you're new to 🤗 PEFT to get an overview of the library's main features, and how to train a model with a PEFT method.](quicktour) [How-to guides Practical guides demonstrating how to apply various PEFT methods across different types of tasks like image classification, causal language modeling, automatic speech recognition, and more. Learn how to use 🤗 PEFT with the DeepSpeed and Fully Sharded Data Parallel scripts.](./task_guides/prompt_based_methods) [Conceptual guides Get a better theoretical understanding of how LoRA and various soft prompting methods help reduce the number of trainable parameters to make training more efficient.](./conceptual_guides/adapter) [Reference Technical descriptions of how 🤗 PEFT classes and methods work.](./package_reference/config)

[ Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/index.md)

[Quicktour→](/docs/peft/quicktour)

[PEFT](#peft)
