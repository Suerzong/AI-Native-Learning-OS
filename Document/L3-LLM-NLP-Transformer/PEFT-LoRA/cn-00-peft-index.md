[ Hugging Face](/)

PEFT 文档

LoRA

# PEFT

# LoRA

本概念指南简要介绍 [LoRA](https://arxiv.org/abs/2106.09685)，一种在减少内存消耗的同时加速大模型微调的技术。

为了使微调更高效，LoRA 的方法是通过低秩分解（low-rank decomposition）用两个较小的矩阵（称为**更新矩阵**）来表示权重更新。这些新矩阵可以被训练以适应新数据，同时保持整体更改数量较低。原始权重矩阵保持冻结状态，不再接收任何进一步调整。为了产生最终结果，原始权重和适配后的权重会被合并。

这种方法有许多优势：

  * LoRA 通过大幅减少可训练参数数量使微调更高效。
  * 原始预训练权重保持冻结，这意味着你可以为各种下游任务拥有多个轻量级且可移植的 LoRA 模型。
  * LoRA 与许多其他参数高效方法正交，可以与其中许多方法结合使用。
  * 使用 LoRA 微调的模型性能与完全微调的模型性能相当。
  * LoRA 不增加任何推理延迟，因为适配器权重可以与基础模型合并。

原则上，LoRA 可以应用于神经网络中任何权重矩阵的子集以减少可训练参数数量。然而，为了简单性和进一步的参数效率，在 Transformer 模型中，LoRA 通常仅应用于注意力块。LoRA 模型中的可训练参数数量取决于低秩更新矩阵的大小，这主要由秩 `r` 和原始权重矩阵的形状决定。

##  将 LoRA 权重合并到基础模型

虽然 LoRA 显著更小且训练更快，但由于分别加载基础模型和 LoRA 模型，你可能在推理时遇到延迟问题。要消除延迟，使用 [merge_and_unload()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.merge_and_unload) 函数将适配器权重与基础模型合并，这样你可以有效地使用新合并的模型作为独立模型。

这是因为在训练期间，较小的权重矩阵（上图中的 _A_ 和 _B_）是分开的。但一旦训练完成，权重实际上可以合并为一个新的相同权重矩阵。

##  LoRA 工具函数

使用 [merge_adapter()](/docs/peft/main/en/package_reference/tuners#peft.tuners.tuners_utils.BaseTuner.merge_adapter) 将 LoRA 层合并到基础模型中，同时保留 PeftModel。这有助于后续取消合并、删除、加载不同的适配器等。

使用 [unmerge_adapter()](/docs/peft/main/en/package_reference/tuners#peft.tuners.tuners_utils.BaseTuner.unmerge_adapter) 从基础模型中取消合并 LoRA 层，同时保留 PeftModel。

使用 [unload()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.unload) 获取不带活动 LoRA 模块合并的基础模型。

使用 [delete_adapter()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.delete_adapter) 删除现有适配器。

使用 [add_weighted_adapter()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.add_weighted_adapter) 基于用户提供的加权方案将多个 LoRA 合并为一个新适配器。

##  PEFT 中常见的 LoRA 参数

与 PEFT 支持的其他方法一样，要使用 LoRA 微调模型，你需要：

  1. 实例化基础模型。
  2. 创建配置（`LoraConfig`），在其中定义 LoRA 特定参数。
  3. 使用 `get_peft_model()` 包装基础模型以获得可训练的 `PeftModel`。
  4. 像通常训练基础模型一样训练 `PeftModel`。

`LoraConfig` 允许你通过以下参数控制 LoRA 如何应用于基础模型：

  * `r`：更新矩阵的秩，用 `int` 表示。较低的秩意味着更新矩阵更小，可训练参数更少。
  * `target_modules`：应用 LoRA 更新矩阵的模块（例如注意力块）。
  * `lora_alpha`：LoRA 缩放因子。
  * `bias`：指定是否应训练 `bias` 参数。可以是 `'none'`、`'all'` 或 `'lora_only'`。
  * `use_rslora`：设为 True 时使用[秩稳定 LoRA](https://doi.org/10.48550/arXiv.2312.03732)，将适配器缩放因子设为 `lora_alpha/math.sqrt(r)`，已被证明效果更好。
  * `modules_to_save`：除 LoRA 层之外要设为可训练并保存在最终检查点中的模块列表。
  * `layers_to_transform`：要由 LoRA 转换的层列表。
  * `layers_pattern`：如果指定了 `layers_to_transform`，用于匹配 `target_modules` 中层名称的模式。
  * `rank_pattern`：从层名称或正则表达式到与 `r` 指定的默认秩不同的秩的映射。
  * `alpha_pattern`：从层名称或正则表达式到与 `lora_alpha` 指定的默认 alpha 不同的 alpha 的映射。

##  LoRA 示例

  * [使用 LoRA 进行图像分类](../task_guides/image_classification_lora)
  * [语义分割](../task_guides/semantic_segmentation_lora)

虽然原始论文专注于语言模型，但该技术可以应用于深度学习模型中的任何密集层。因此，你可以将此技术与扩散模型一起使用。参见[使用 LoRA 进行 Dreambooth 微调](../task_guides/task_guides/dreambooth_lora)任务指南了解示例。

##  初始化选项

LoRA 权重的初始化由 `LoraConfig` 的 `init_lora_weights` 参数控制。默认情况下，PEFT 以与[参考实现](https://github.com/microsoft/LoRA)相同的方式初始化 LoRA 权重，即权重 A 使用 Kaiming-uniform，权重 B 初始化为零，产生恒等变换。

也可以传递 `init_lora_weights="gaussian"`。顾名思义，这导致权重 A 使用高斯分布初始化（权重 B 仍然是零）。

当对基础模型进行量化时（例如 QLoRA 训练），考虑使用 [LoftQ 初始化](https://arxiv.org/abs/2310.08659)，已被证明在量化时可以提高性能。思路是初始化 LoRA 权重以最小化量化误差。

    from peft import LoftQConfig, LoraConfig, get_peft_model

    base_model = AutoModelForCausalLM.from_pretrained(...)  # 不在此处量化
    loftq_config = LoftQConfig(loftq_bits=4, ...)           # 设置 4 位量化
    lora_config = LoraConfig(..., init_lora_weights="loftq", loftq_config=loftq_config)
    peft_model = get_peft_model(base_model, lora_config)

还可以设置 `initialize_lora_weights=False`。选择此选项时，LoRA 权重被初始化为_不_产生恒等变换。这用于调试和测试目的。

最后，LoRA 架构在每次前向传播时通过固定标量缩放每个适配器，该标量在初始化时设置，并取决于秩 `r`。虽然原始 LoRA 方法使用标量函数 `lora_alpha/r`，但研究[秩稳定 LoRA](https://doi.org/10.48550/arXiv.2312.03732)证明使用 `lora_alpha/math.sqrt(r)` 可以稳定适配器并释放更高秩的性能潜力。设置 `use_rslora=True` 以使用秩稳定缩放 `lora_alpha/math.sqrt(r)`。

[🤗 PEFT→](/docs/peft/main/en/index)

LoRA将 LoRA 权重合并到基础模型LoRA 工具函数PEFT 中常见的 LoRA 参数LoRA 示例初始化选项
