[ Hugging Face](/)

PEFT 文档

LoRA

# PEFT

# LoRA 开发者指南

本指南详细探讨使用 LoRA 的各种选项和功能，包括初始化、变体、训练策略和推理技巧。

## 初始化

LoRA 权重的初始化由 `LoraConfig` 中的 `init_lora_weights` 参数控制。

### PiSSA

[PiSSA](https://huggingface.co/papers/2404.02948) 使用主奇异值和奇异向量初始化 LoRA 适配器，比 LoRA 收敛更快，性能更好。

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights="pissa", ...)

### CorDA

[CorDA](https://huggingface.co/papers/2406.05223) 从面向下游任务上下文的权重分解中构建任务感知 LoRA 适配器，分为指令预览模式（IPM）和知识保持模式（KPM）。

### OLoRA

[OLoRA](https://huggingface.co/papers/2406.01775) 使用 QR 分解初始化 LoRA 适配器，显著提高稳定性和收敛速度。

    from peft import LoraConfig
    config = LoraConfig(init_lora_weights="olora", ...)

### EVA

[EVA](https://huggingface.co/papers/2410.07170) 对每层输入激活执行 SVD 并使用右奇异向量初始化 LoRA 权重，是数据驱动的初始化方案。

    from peft import LoraConfig, EvaConfig
    peft_config = LoraConfig(init_lora_weights="eva", eva_config=EvaConfig(rho=2.0), ...)

### LoftQ

在 QLoRA 训练中，使用 [LoftQ 初始化](https://huggingface.co/papers/2310.08659)可最小化量化误差。

### 秩稳定 LoRA

[rsLoRA](https://huggingface.co/papers/2312.03732) 使用 `lora_alpha/math.sqrt(r)` 代替原始的 `lora_alpha/r`，稳定适配器并释放更高秩的性能潜力。

    from peft import LoraConfig
    config = LoraConfig(use_rslora=True, ...)

### LoRA-GA

[LoRA-GA](https://hf.co/papers/2407.05000) 通过梯度信息初始化适配器权重，实现 2-4 倍收敛加速。

## 变体

### DoRA（权重分解低秩适配）

DoRA 将权重更新分解为幅度和方向两部分，可提高 LoRA 尤其在低秩时的性能。

    from peft import LoraConfig
    config = LoraConfig(use_dora=True, ...)

注意事项：
  * DoRA 目前仅支持 embedding、linear 和 Conv2d 层
  * DoRA 比纯 LoRA 开销更大，建议推理时合并权重
  * 与 bitsandbytes 量化兼容（"QDoRA"）

## 训练策略

### QLoRA 风格训练

将 LoRA 应用于所有线性层：

    config = LoraConfig(target_modules="all-linear", ...)

### 使用 LoRA 进行层复制

扩展模型层以构建更大模型：

    config = LoraConfig(layer_replication=[[0,4], [2,5]], ...)

### 对秩和 alpha 的细粒度控制

使用 `rank_pattern` 和 `alpha_pattern` 为不同层指定不同的秩和 alpha：

    config = LoraConfig(r=8, rank_pattern={"foo": 42}, ...)

### 目标 nn.Parameter

对于 MoE 层中使用 `nn.Parameter` 而非 `nn.Linear` 的情况，使用 `target_parameters`：

    config = LoraConfig(target_parameters=['feed_forward.experts.gate_up_proj', 'feed_forward.experts.down_proj'], ...)

### 高效训练词元

PEFT LoRA 适配器支持通过 `trainable_token_indices` 参数选择性地微调特定词元：

    config = LoraConfig(trainable_token_indices=[idx_1, idx_2, ...], ...)

### 权重绑定

使用 `ensure_weight_tying=True` 保持绑定层的适配器端更新同步。

## 优化器

### LoRA-FA

固定矩阵 A，仅调整矩阵 B，减少激活内存消耗：

    from peft.optimizers import create_lorafa_optimizer
    optimizer = create_lorafa_optimizer(model=model, r=128, lora_alpha=32, lr=7e-5)

### LoRA+

对适配器矩阵 A 和 B 使用不同学习率，可提高 2 倍收敛速度：

    from peft.optimizers import create_loraplus_optimizer
    optimizer = create_loraplus_optimizer(model=model, optimizer_cls=bnb.optim.Adam8bit, lr=5e-5, loraplus_lr_ratio=16)

## 训练后处理

### 合并 LoRA 权重

    model = model.merge_and_unload()

使用 `merge_adapter()` 合并但保留 PeftModel，使用 `unmerge_adapter()` 取消合并。

### 合并多个适配器

    model.add_weighted_adapter(adapters=["sft", "dpo"], weights=[0.7, 0.3], adapter_name="sft-dpo", combination_type="linear")

### 侵入维度缩减

[peft.tuners.lora.intruders.reduce_intruder_dimension()](/docs/peft/v0.19.0/en/package_reference/lora#peft.tuners.lora.intruders.reduce_intruder_dimension) 通过后处理已训练的低秩适配器恢复先前知识（减轻遗忘）。

## 推理

### 在同一批次中使用不同 LoRA 适配器

使用 `adapter_names` 参数指定每个样本使用的适配器：

    adapter_names = ["__base__", "__base__", "__base__", "adapter_fr", "adapter_fr", "adapter_fr", "adapter_de", "adapter_de", "adapter_de"]
    output = peft_model.generate(**inputs, adapter_names=adapter_names, max_new_tokens=20)

注意事项：
  * 仅支持推理，不支持训练
  * 不支持 DoRA
  * 存在一定的运行时开销

### 组合和复用 LoRA 适配器

#### Arrow

[Arrow](https://huggingface.co/papers/2405.11157) 是一种模块化路由算法，用于组合多个预训练的任务特定 LoRA 适配器来解决给定任务。

    from peft import create_arrow_model, ArrowConfig
    arrow_config = ArrowConfig(top_k=3, router_temperature=1.0, rng_seed=42)
    model = create_arrow_model(base_model=base_model, task_specific_adapter_paths=task_specific_adapter_paths, arrow_config=arrow_config)

#### GenKnowSub

[GenKnowSub](https://aclanthology.org/2025.acl-short.54/) 通过在路由前净化任务特定 LoRA 适配器来增强 Arrow。

[ 在 GitHub 上更新](https://github.com/huggingface/peft/blob/main/docs/source/developer_guides/lora.md)

[LoRA 开发者指南](#)[初始化](#initialization)[变体](#variants)[训练策略](#training)[优化器](#optimizers)[训练后处理](#post-training)[推理](#inference)
