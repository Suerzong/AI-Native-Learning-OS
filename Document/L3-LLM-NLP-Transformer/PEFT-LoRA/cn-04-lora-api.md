[ Hugging Face](/)

PEFT 文档

LoRA API

# PEFT

# LoRA API 参考

低秩适配（[LoRA](https://huggingface.co/papers/2309.15223)）是一种 PEFT 方法，将注意力层中的大矩阵分解为两个较小的低秩矩阵。这大幅减少了需要微调的参数数量。

## [](#peft.LoraConfig) LoraConfig

### class peft.LoraConfig

这是存储 [LoraModel](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraModel) 配置的配置类。

主要参数：

  * **r** (`int`) — LoRA 注意力维度（"秩"）。
  * **target_modules** (`Optional[Union[List[str], str]]`) — 要应用适配器的模块名称。可以是字符串（正则匹配）或字符串列表（精确匹配或后缀匹配）。设为 `'all-linear'` 选择所有线性/Conv1D 模块。
  * **exclude_modules** (`Optional[Union[List[str], str]]`) — 不应用适配器的模块名称。
  * **lora_alpha** (`int`) — LoRA 缩放的 alpha 参数。
  * **lora_dropout** (`float`) — LoRA 层的 dropout 概率。
  * **fan_in_fan_out** (`bool`) — 如果要替换的层以 (fan_in, fan_out) 方式存储权重，设为 True。
  * **bias** (`str`) — LoRA 的偏置类型。可以是 `'none'`、`'all'` 或 `'lora_only'`。
  * **use_rslora** (`bool`) — 设为 True 时使用[秩稳定 LoRA](https://huggingface.co/papers/2312.03732)。
  * **modules_to_save** (`List[str]`) — 除适配器层外要设为可训练并保存在最终检查点中的模块列表。
  * **init_lora_weights** (`bool | Literal[...]`) — 如何初始化适配器层的权重。`True`（默认）为标准初始化，`"gaussian"` 为高斯初始化，`"eva"` 为 EVA 初始化，`"olora"` 为 OLoRA 初始化，`"pissa"` 为 PiSSA 初始化，`"corda"` 为 CorDA 初始化，`"loftq"` 为 LoftQ 初始化。
  * **layers_to_transform** (`Union[List[int], int]`) — 要转换的层索引。
  * **layers_pattern** (`Optional[Union[List[str], str]]`) — 层模式名称，仅在 `layers_to_transform` 不为 None 时使用。
  * **rank_pattern** (`dict`) — 从层名称或正则表达式到与默认秩不同的秩的映射。
  * **alpha_pattern** (`dict`) — 从层名称或正则表达式到与默认 alpha 不同的 alpha 的映射。
  * **trainable_token_indices** (`Optional[Union[List[int], dict[str, List[int]]]]`) — 指定要选择性微调的词元索引。
  * **loftq_config** (`Optional[LoftQConfig]`) — LoftQ 的配置。
  * **eva_config** (`Optional[EvaConfig]`) — EVA 的配置。
  * **corda_config** (`Optional[CordaConfig]`) — CorDA 的配置。
  * **use_dora** (`bool`) — 启用权重分解低秩适配（DoRA）。
  * **alora_invocation_tokens** (`List[int]`) — 启用激活 LoRA（aLoRA）的调用词元序列。
  * **layer_replication** (`List[Tuple[int, int]]`) — 通过堆叠原始模型层构建新的层栈。
  * **runtime_config** (`LoraRuntimeConfig`) — 运行时配置。
  * **lora_bias** (`bool`) — 是否为 LoRA B 参数启用偏置项。
  * **target_parameters** (`List[str]`, 可选) — 要用 LoRA 替换的参数名称或正则表达式列表。
  * **ensure_weight_tying** (`bool`, 可选) — peft 初始化后是否绑定权重。

#### to_dict

以字典格式返回适配器模型的配置。移除运行时配置。

## [](#peft.LoraModel) LoraModel

### class peft.LoraModel

创建低秩适配（LoRA）模型。

主要方法：

#### add_weighted_adapter

通过合并给定的适配器和权重添加新适配器。

参数：
  * **adapters** (`list`) — 要合并的适配器名称列表。
  * **weights** (`list`) — 每个适配器的权重列表。
  * **adapter_name** (`str`) — 新适配器的名称。
  * **combination_type** (`str`) — 合并类型，可以是 `svd`、`linear`、`cat`、`ties`、`ties_svd`、`dare_ties`、`dare_linear` 等。

#### subtract_mutated_init

通过比较 `output_state_dict` 中 PiSSA/CorDA/OLoRA 适配器的参数与初始值，计算 PiSSA/CorDA/OLoRA 的更新，从而将 PiSSA/CorDA/OLoRA 转换为 LoRA。

## [](#utility) 工具

### ArrowConfig

Arrow 的子配置类，用于组合多个训练好的 LoRA 模块来解决新任务。

参数：
  * **top_k** (`int`) — 每个词元组合的 LoRA 适配器数量。
  * **router_temperature** (`float`) — 路由系数的 softmax 温度。
  * **use_gks** (`bool`) — 是否使用 GenKnowSub。
  * **rng_seed** (`int`) — 可复现性的随机种子。

### LoftQ

#### peft.replace_lora_weights_loftq

使用 LoftQ 技术替换使用 bitsandbytes 量化的模型的 LoRA 权重。

### EvaConfig

EVA 数据驱动初始化的子配置类。

参数：
  * **rho** (`float`) — EVA 再分配的 rho 值（>= 1.0）。
  * **tau** (`float`) — 早停的余弦相似度阈值。
  * **use_label_mask** (`bool`) — 是否对 EVA 初始化使用标签掩码。
  * **label_mask_value** (`int`) — 要掩码的值。
  * **whiten** (`bool`) — 是否对奇异向量应用白化。
  * **adjust_scaling_factors** (`bool`) — 秩再分配后是否调整缩放因子。

#### initialize_lora_eva_weights

使用 EVA 方法初始化 LoRA 层的权重。

#### get_eva_state_dict

计算模型中每一层的 SVD。

## [](#variants) 变体

### LoRA-GA

[LoRA-GA](https://hf.co/papers/2407.05000) 使用梯度信息在初始化期间实现更快的收敛（2-4 倍加速）。

#### LoraGAConfig

参数：
  * **direction** (`Literal["ArBr", "A2rBr", "ArB2r", "random"]`) — 将梯度 SVD 组件分配到 lora_A 和 lora_B 矩阵的策略。
  * **scale** (`Literal["stable", "weight_svd", "gd_scale", "unit"]`) — 适配器初始化的缩放策略。
  * **stable_gamma** (`int`) — 稳定缩放方法的 gamma 参数。

#### peft.preprocess_loraga

通过估计梯度为模型构建必要的 LoRA-GA 字段。

## [](#peft.tuners.lora.intruders.reduce_intruder_dimension) 侵入维度缩减

基于 <https://huggingface.co/papers/2410.21228>（"LoRA vs 完全微调：等价性的幻觉"）的侵入维度缓解方法。

此方法可以通过后处理已训练的低秩适配器恢复先前知识（即减轻遗忘）。这以任务精度为代价。

参数：
  * **peft_model** — 加载了 LoRA 适配器的 PEFT 模型。
  * **top_k** (默认 10) — 侵入检测考虑的 top-k 维度。
  * **threshold_epsilon** (默认 0.5) — 何时将基础权重和适配器权重之间的余弦相似度视为侵入的阈值。
  * **mitigation_lambda** (默认 0.75) — 从适配器的增量权重中减去的侵入维度的相对比例。
  * **logging_sink** (默认 print) — 打印缓解过程信息的函数。

[ 在 GitHub 上更新](https://github.com/huggingface/peft/blob/main/docs/source/package_reference/lora.md)

[←LoKr](/docs/peft/package_reference/lokr) [OSF→](/docs/peft/package_reference/osf)

[LoraConfig](#peft.LoraConfig)[LoraModel](#peft.LoraModel)[工具](#utility)[ArrowConfig](#peft.ArrowConfig)[LoftQ](#loftq)[EvaConfig](#eva)[LoRA-GA](#lora-ga)[侵入维度缩减](#peft.tuners.lora.intruders.reduce_intruder_dimension)
