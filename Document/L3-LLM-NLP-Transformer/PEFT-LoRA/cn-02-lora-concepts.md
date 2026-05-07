[ Hugging Face](/)

PEFT 文档

LoRA

# PEFT

# LoRA

LoRA 是一种通过低秩分解减少可训练参数数量的方法，可加速大模型微调并使用更少内存。在 PEFT 中，使用 LoRA 就像设置 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 并用 [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) 包装它来创建可训练的 [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) 一样简单。

本指南更详细地探讨使用 LoRA 的其他选项和功能。

## [](#initialization) 初始化

LoRA 权重的初始化由 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 中的 `init_lora_weights` 参数控制。默认情况下，PEFT 使用 Kaiming-uniform 初始化权重 A，使用零初始化权重 B，产生恒等变换（与参考[实现](https://github.com/microsoft/LoRA)相同）。

也可以传递 `init_lora_weights="gaussian"`。顾名思义，这使用高斯分布初始化权重 A，零初始化权重 B（这是 [Diffusers](https://huggingface.co/docs/diffusers/index) 初始化 LoRA 权重的方式）。

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights="gaussian", ...)

还有一个选项 `init_lora_weights=False`，用于调试和测试。当选择此选项时，LoRA 权重被初始化为_不_产生恒等变换。

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights=False, ...)

### [](#pissa) PiSSA

[PiSSA](https://huggingface.co/papers/2404.02948) 使用主奇异值和奇异向量初始化 LoRA 适配器。这种直接的修改使 PiSSA 比 LoRA 收敛更快，最终获得更好的性能。此外，PiSSA 与 QLoRA 相比减少了量化误差，带来进一步的增强。

配置初始化方法为 "pissa"，可能需要几分钟在预训练模型上执行 SVD：

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights="pissa", ...)

或者执行快速 SVD，只需几秒钟。迭代次数决定了误差和计算时间之间的权衡：

    lora_config = LoraConfig(init_lora_weights="pissa_niter_[number of iters]", ...)

### [](#corda) CorDA

[CorDA](https://huggingface.co/papers/2406.05223) 从面向下游任务上下文的权重分解中构建任务感知的 LoRA 适配器。

### [](#olora) OLoRA

[OLoRA](https://huggingface.co/papers/2406.01775) 使用 QR 分解初始化 LoRA 适配器。OLoRA 通过其 QR 分解因子平移模型的基础权重，即在对权重执行任何训练之前对其进行变换。这种方法显著提高了稳定性，加速了收敛速度，并最终实现了更好的性能。

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights="olora", ...)

### [](#eva) EVA

[EVA](https://huggingface.co/papers/2410.07170) 对每层的输入激活执行 SVD，并使用右奇异向量初始化 LoRA 权重。因此它是数据驱动的初始化方案。此外，EVA 根据"解释方差比"自适应地在各层之间分配秩。

    from peft import LoraConfig, EvaConfig
    peft_config = LoraConfig(
        init_lora_weights = "eva",
        eva_config = EvaConfig(rho = 2.0),
        ...
    )

### [](#loftq) LoftQ

在对基础模型进行量化以进行 QLoRA 训练时，考虑使用 [LoftQ 初始化](https://huggingface.co/papers/2310.08659)，已被证明在量化模型训练时能提高性能。

### [](#rank-stabilized-lora) 秩稳定 LoRA

初始化 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 的另一种方法是使用[秩稳定 LoRA (rsLoRA)](https://huggingface.co/papers/2312.03732)方法。LoRA 架构在每次前向传播时通过固定标量缩放每个适配器，该标量在初始化时设置并取决于秩 `r`。原始实现中的标量为 `lora_alpha/r`，但 rsLoRA 使用 `lora_alpha/math.sqrt(r)`，稳定了适配器并增加了使用更高 `r` 的性能潜力。

    from peft import LoraConfig
    config = LoraConfig(use_rslora=True, ...)

### [](#lora-ga) LoRA-GA

[LoRA-GA](https://hf.co/papers/2407.05000)（带梯度近似的低秩适配）通过在初始化期间使用梯度信息实现更快的收敛。LoRA-GA 对估计的梯度执行 SVD 来初始化适配器权重，使初始更新方向与完全微调的方向一致，在保持相同最终性能的同时实现 2-4 倍的收敛加速。

## [](#variants) 变体

### [](#weight-decomposed-low-rank-adaptation-dora) 权重分解低秩适配 (DoRA)

该技术将权重更新分解为两部分：幅度和方向。方向由标准 LoRA 处理，而幅度由单独的可学习参数处理。这可以提高 LoRA 的性能，尤其是在低秩时。更多信息参见 <https://huggingface.co/papers/2402.09353>。

    from peft import LoraConfig
    config = LoraConfig(use_dora=True, ...)

**注意事项：**

  * DoRA 目前仅支持 embedding、linear 和 Conv2d 层。
  * DoRA 比纯 LoRA 引入更大的开销，因此建议合并权重进行推理。
  * DoRA 应与 bitsandbytes 量化权重（"QDoRA"）一起工作。

## [](#training) 训练

### [](#qlora-style-training) QLoRA 风格训练

PEFT 中的默认 LoRA 设置在每个注意力块的 query 和 value 层添加可训练权重。但 [QLoRA](https://hf.co/papers/2305.14314) 在 transformer 模型的所有线性层添加可训练权重，可提供与完全微调模型相等的性能。要将 LoRA 应用于所有线性层（如 QLoRA），设置 `target_modules="all-linear"`。

    config = LoraConfig(target_modules="all-linear", ...)

### [](#memory-efficient-layer-replication-with-lora) 使用 LoRA 进行内存高效的层复制

    config = LoraConfig(layer_replication=[[0,4], [2,5]], ...)

### [](#fine-grained-control-over-ranks-and-alpha-scaling) 对秩和 alpha（缩放）的细粒度控制

默认情况下，所有使用 LoRA 的目标层具有相同的秩 `r` 和相同的 `lora_alpha`。然而，在某些情况下，你可能想为不同层指定不同的值。可以通过向 [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 传递 `rank_pattern` 和 `alpha_pattern` 参数来实现。

### [](#efficiently-train-tokens-alongside-lora) 高效地与 LoRA 一起训练词元

PEFT LoRA 适配器支持通过 `trainable_token_indices` 参数添加新词元。

    # 对于 'embed_tokens' 层
    config = LoraConfig(trainable_token_indices=[idx_1, idx_2, ...], ...)

### [](#weight-tying) 权重绑定

许多因果 LM 使用**权重绑定**，即两个或多个权重共享相同的基础参数。最常见的情况是，输入嵌入权重（`embed_tokens`）和输出投影权重（`lm_head`）共享相同的张量。[LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) 上的 `ensure_weight_tying` 控制 PEFT 是否应显式保持适配器端更新的绑定。

## [](#optimizers) 优化器

LoRA 训练可以可选地包含特殊用途的优化器。目前 PEFT 支持 LoRA-FA 和 LoRA+。

### [](#lora-fa-optimizer) LoRA-FA 优化器

[LoRA-FA](https://huggingface.co/papers/2308.03303) 通过固定矩阵 A 并仅调整矩阵 B 来减少激活内存消耗。

    from peft import LoraConfig, get_peft_model
    from peft.optimizers import create_lorafa_optimizer

    optimizer = create_lorafa_optimizer(model=model, r=128, lora_alpha=32, lr=7e-5)

### [](#lora-optimized-lora) LoRA+ 优化的 LoRA

[LoRA+](https://huggingface.co/papers/2402.12354) 对适配器矩阵 A 和 B 使用不同的学习率，可将微调速度提高最多 2 倍，性能提高 1-2%。

    from peft.optimizers import create_loraplus_optimizer
    optimizer = create_loraplus_optimizer(model=model, optimizer_cls=bnb.optim.Adam8bit, lr=5e-5, loraplus_lr_ratio=16)

## [](#post-training) 训练后处理

### [](#merge-lora-weights-into-the-base-model) 将 LoRA 权重合并到基础模型

    from transformers import AutoModelForCausalLM
    from peft import PeftModel

    base_model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
    peft_model_id = "alignment-handbook/zephyr-7b-sft-lora"
    model = PeftModel.from_pretrained(base_model, peft_model_id)
    model = model.merge_and_unload()

## [](#load-adapters) 加载适配器

    from transformers import AutoModelForCausalLM
    from peft import PeftModel

    base_model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
    peft_model_id = "alignment-handbook/zephyr-7b-sft-lora"
    model = PeftModel.from_pretrained(base_model, peft_model_id)

    # 加载不同适配器
    model.load_adapter("alignment-handbook/zephyr-7b-dpo-lora", adapter_name="dpo")

    # 设置适配器为活动
    model.set_adapter("dpo")

    # 卸载适配器
    model = model.unload()

    # 删除适配器
    model.delete_adapter("dpo")

## [](#inference) 推理

### [](#inference-with-different-lora-adapters-in-the-same-batch) 在同一批次中使用不同 LoRA 适配器进行推理

通常，每个推理批次必须在 PEFT 中使用相同的适配器。但可以使用 `adapter_names` 参数在同一批次中混合不同的 LoRA 适配器。

    adapter_names = [
        "__base__", "__base__", "__base__",
        "adapter_fr", "adapter_fr", "adapter_fr",
        "adapter_de", "adapter_de", "adapter_de",
    ]
    output = peft_model.generate(**inputs, adapter_names=adapter_names, max_new_tokens=20)

[ 在 GitHub 上更新](https://github.com/huggingface/peft/blob/main/docs/source/developer_guides/lora.md)

[←量化](/docs/peft/developer_guides/quantization) [自定义模型→](/docs/peft/developer_guides/custom_models)

[LoRA](#lora)[初始化](#initialization)[变体](#variants)[训练](#training)[训练后处理](#post-training)[加载适配器](#load-adapters)[推理](#inference)
