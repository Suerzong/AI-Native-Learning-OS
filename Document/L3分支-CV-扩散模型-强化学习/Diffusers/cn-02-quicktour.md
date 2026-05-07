# 快速开始

Diffusers 是一个面向开发者和研究者的库，提供了简便的推理 API 来生成图像、视频和音频，以及实现新工作流的构建模块。

Diffusers 提供了许多开箱即用的优化功能，使你能够在有限内存的设置上加载和运行大型模型，或加速推理。

本快速入门将为你概述 Diffusers 并让你快速开始生成。

> 开始之前，请确保你拥有 Hugging Face [账号](https://huggingface.co/join)，以便使用受限模型如 [Flux](https://huggingface.co/black-forest-labs/FLUX.1-dev)。

如果尚未安装，请按照[安装](./installation)指南安装 Diffusers。

## DiffusionPipeline

扩散模型将多个组件组合在一起，根据输入（如文本描述、图像或两者）在任意模态中生成输出。

对于标准的文本到图像模型：

  1. 文本编码器（Text Encoder）将提示词转换为嵌入向量，引导去噪过程。某些模型有多个文本编码器。

  2. 调度器（Scheduler）包含将初始随机噪声逐步去噪为干净输出的算法细节。不同的调度器影响生成速度和质量。

  3. UNet 或扩散变换器（DiT）是扩散模型的核心工作组件。在每一步中，它执行去噪预测，如需要去除多少噪声或引导噪声生成更高质量输出的大致方向。UNet 或 DiT 重复此循环指定步数以生成最终输出。

  4. 变分自编码器（VAE）将像素编码和解码到空间压缩的潜空间（Latent Space）。_潜变量（Latents）_ 是图像的压缩表示，操作效率更高。UNet 或 DiT 在潜变量上操作，最终的干净潜变量被解码回图像。

[DiffusionPipeline](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline) 将所有这些组件打包为一个用于推理的单一类。`__call__()` 中有几个参数可以更改，如 `num_inference_steps`，会影响扩散过程。尝试不同的值和参数来观察它们如何改变生成质量或速度。

使用 [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained) 加载模型并描述你想生成的内容。

    import torch
    from diffusers import DiffusionPipeline

    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image", torch_dtype=torch.bfloat16, device_map="cuda"
    )

    prompt = """
    cinematic film still of a cat sipping a margarita in a pool in Palm Springs, California
    highly detailed, high budget hollywood movie, cinemascope, moody, epic, gorgeous, film grain
    """
    pipeline(prompt).images[0]

## LoRA

适配器（Adapters）向原始基础模型插入少量可训练参数。仅插入的参数被微调，而模型的其余权重保持冻结。这使得在新风格上微调模型变得快速且成本低廉。在适配器中，[LoRA](./tutorials/using_peft_for_inference) 最为流行。

使用 [load_lora_weights()](/docs/diffusers/v0.38.0/en/api/loaders/lora#diffusers.loaders.QwenImageLoraLoaderMixin.load_lora_weights) 方法向流水线添加 LoRA。某些 LoRA 需要特殊触发词，如下例中的 `Realism`。请查看 LoRA 的模型卡片以确认是否需要触发词。

    import torch
    from diffusers import DiffusionPipeline

    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image", torch_dtype=torch.bfloat16, device_map="cuda"
    )
    pipeline.load_lora_weights(
      "flymy-ai/qwen-image-realism-lora",
    )

    prompt = """
    super Realism cinematic film still of a cat sipping a margarita in a pool in Palm Springs in the style of umempart, California
    highly detailed, high budget hollywood movie, cinemascope, moody, epic, gorgeous, film grain
    """
    pipeline(prompt).images[0]

查看 [LoRA](./tutorials/using_peft_for_inference) 文档或适配器章节了解更多。

## 量化（Quantization）

[量化](./quantization/overview)以更少的位数存储数据以减少内存使用。它还可能加速推理，因为使用更少的位数执行计算所需时间更短。

Diffusers 提供多种量化后端，选择取决于你的用例。例如，[bitsandbytes](./quantization/bitsandbytes) 和 [torchao](./quantization/torchao) 都简单易用，但 torchao 支持更多[量化类型](./quantization/torchao#supported-quantization-types)如 fp8。

配置 [PipelineQuantizationConfig](/docs/diffusers/v0.38.0/en/api/quantization#diffusers.PipelineQuantizationConfig)，指定要使用的后端、该后端的特定参数以及要量化的组件。以下示例将模型量化到 4 位，仅使用 14.93GB 内存。

    import torch
    from diffusers import DiffusionPipeline
    from diffusers.quantizers import PipelineQuantizationConfig

    quant_config = PipelineQuantizationConfig(
      quant_backend="bitsandbytes_4bit",
      quant_kwargs={"load_in_4bit": True, "bnb_4bit_quant_type": "nf4", "bnb_4bit_compute_dtype": torch.bfloat16},
      components_to_quantize=["transformer", "text_encoder"],
    )
    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image",
      torch_dtype=torch.bfloat16,
      quantization_config=quant_config,
      device_map="cuda"
    )

    prompt = """
    cinematic film still of a cat sipping a margarita in a pool in Palm Springs, California
    highly detailed, high budget hollywood movie, cinemascope, moody, epic, gorgeous, film grain
    """
    pipeline(prompt).images[0]
    print(f"Max memory reserved: {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")

请查看[量化](./quantization/overview)章节了解更多细节。

## 优化

> 优化取决于硬件规格（如内存）。使用此 [Space](https://huggingface.co/spaces/diffusers/optimized-diffusers-code) 生成包含 Diffusers 所有可用内存和速度优化技术的代码示例。

现代扩散模型非常庞大，拥有数十亿参数。迭代去噪过程也计算密集且缓慢。Diffusers 提供了减少内存使用和提升推理速度的技术。这些技术可以与量化结合使用，同时优化内存使用和推理速度。

### 内存使用

文本编码器和 UNet 或 DiT 可能占用多达约 30GB 的内存，超出许多免费或消费级 GPU 的可用量。

卸载（Offloading）将当前未使用的权重存储在 CPU 上，仅在需要时将它们移动到 GPU。有几种卸载类型，以下示例使用[模型卸载](./optimization/memory#model-offloading)，将整个模型（如文本编码器或变换器）在未被积极使用时移动到 CPU。

调用 [enable_model_cpu_offload()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.enable_model_cpu_offload) 来激活它。通过结合量化和卸载，以下示例仅需要约 12.54GB 内存。

    import torch
    from diffusers import DiffusionPipeline
    from diffusers.quantizers import PipelineQuantizationConfig

    quant_config = PipelineQuantizationConfig(
      quant_backend="bitsandbytes_4bit",
      quant_kwargs={"load_in_4bit": True, "bnb_4bit_quant_type": "nf4", "bnb_4bit_compute_dtype": torch.bfloat16},
      components_to_quantize=["transformer", "text_encoder"],
    )
    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image",
      torch_dtype=torch.bfloat16,
      quantization_config=quant_config,
      device_map="cuda"
    )
    pipeline.enable_model_cpu_offload()

    prompt = """
    cinematic film still of a cat sipping a margarita in a pool in Palm Springs, California
    highly detailed, high budget hollywood movie, cinemascope, moody, epic, gorgeous, film grain
    """
    pipeline(prompt).images[0]
    print(f"Max memory reserved: {torch.cuda.max_memory_allocated() / 1024**3:.2f} GB")

请参阅[减少内存使用](./optimization/memory)文档了解更多内存减少技术。

### 推理速度

去噪循环执行大量计算，可能很慢。[torch.compile](./optimization/fp16#torchcompile) 等方法通过将计算编译为优化的内核来提高推理速度。首次生成时编译较慢，但后续生成会快得多。

以下示例使用[区域编译](./optimization/fp16#regional-compilation)仅编译模型的小区域。它减少了冷启动延迟，同时提供了运行时加速。

在模型上调用 [compile_repeated_blocks()](/docs/diffusers/v0.38.0/en/api/models/overview#diffusers.ModelMixin.compile_repeated_blocks) 来激活它。

    import torch
    from diffusers import DiffusionPipeline

    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image", torch_dtype=torch.bfloat16, device_map="cuda"
    )

    pipeline.transformer.compile_repeated_blocks(
        fullgraph=True,
    )
    prompt = """
    cinematic film still of a cat sipping a margarita in a pool in Palm Springs, California
    highly detailed, high budget hollywood movie, cinemascope, moody, epic, gorgeous, film grain
    """
    pipeline(prompt).images[0]

查看[加速推理](./optimization/fp16)或[缓存](./optimization/cache)文档了解更多加速推理的方法。
