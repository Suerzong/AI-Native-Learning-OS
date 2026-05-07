[ Hugging Face](/)

PEFT 文档

模型

# PEFT

# PEFT 模型 API 参考

[PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) 是用于指定基础 Transformer 模型和要应用的 PEFT 方法的基础模型类。基础 `PeftModel` 包含从 Hub 加载和保存模型的方法。

## [](#peft.PeftModel) PeftModel

### class peft.PeftModel

基础 PEFT 模型类，封装各种 Peft 方法。

主要参数：
  * **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) — 用于 PEFT 的基础 Transformer 模型。
  * **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) — Peft 模型的配置。
  * **adapter_name** (`str`, 可选) — 适配器名称，默认为 `"default"`。
  * **autocast_adapter_dtype** (`bool`, 可选) — 是否自动转换适配器数据类型。

主要方法：

#### add_adapter

根据传递的配置向模型添加适配器。

    model.add_adapter(adapter_name="my_adapter", peft_config=lora_config)

#### delete_adapter

删除现有适配器。

    model.delete_adapter("adapter_name")

#### disable_adapter

禁用适配器模块的上下文管理器。用于在基础模型上运行推理。

    with model.disable_adapter():
        model(inputs)

#### forward

模型的前向传播。

#### from_pretrained

从预训练模型和已加载的 PEFT 权重实例化 PEFT 模型。

    model = PeftModel.from_pretrained(base_model, "path/to/adapter")

参数：
  * **model** (`torch.nn.Module`) — 要适配的模型。
  * **model_id** (`str` 或 `os.PathLike`) — PEFT 配置的名称或路径。
  * **adapter_name** (`str`, 可选) — 要加载的适配器名称。
  * **is_trainable** (`bool`, 可选) — 适配器是否可训练。
  * **ephemeral_gpu_offload** (`bool`, 可选) — 是否使用临时 GPU 卸载。

#### get_nb_trainable_parameters

返回模型中可训练参数的数量和所有参数的数量。

#### get_prompt

返回用于 Peft 的虚拟提示。仅适用于提示学习方法。

#### load_adapter

将训练好的适配器加载到模型中。

    model.load_adapter("path/to/adapter", adapter_name="new_adapter")

#### print_trainable_parameters

打印模型中可训练参数的数量。

    model.print_trainable_parameters()
    # "trainable params: 2359296 || all params: 1231940608 || trainable%: 0.19151053100118282"

#### save_pretrained

将适配器模型和配置文件保存到目录。

    model.save_pretrained("output_dir")

参数：
  * **save_directory** (`str`) — 保存目录。
  * **safe_serialization** (`bool`, 可选) — 是否以 safetensors 格式保存。
  * **selected_adapters** (`List[str]`, 可选) — 要保存的适配器列表。
  * **save_embedding_layers** (`Union[bool, str]`, 可选) — 是否保存嵌入层。
  * **path_initial_model_for_weight_conversion** (`str`, 可选) — PiSSA/CorDA/OLoRA 初始化适配器的路径。

#### set_adapter

设置活动适配器。

    model.set_adapter("adapter_name")

#### set_requires_grad

启用或禁用给定适配器的梯度。

    model.set_requires_grad("adapter_name", requires_grad=True)

## [](#peft.PeftModelForSequenceClassification) PeftModelForSequenceClassification

用于序列分类任务的 `PeftModel`。

    from transformers import AutoModelForSequenceClassification
    from peft import PeftModelForSequenceClassification, get_peft_config

    peft_config = get_peft_config(config)
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased")
    peft_model = PeftModelForSequenceClassification(model, peft_config)

## [](#peft.PeftModelForTokenClassification) PeftModelForTokenClassification

用于词元分类任务的 `PeftModel`。

## [](#peft.PeftModelForCausalLM) PeftModelForCausalLM

用于因果语言建模的 `PeftModel`。

    from transformers import AutoModelForCausalLM
    from peft import PeftModelForCausalLM, get_peft_config

    model = AutoModelForCausalLM.from_pretrained("gpt2-large")
    peft_model = PeftModelForCausalLM(model, peft_config)

## [](#peft.PeftModelForSeq2SeqLM) PeftModelForSeq2SeqLM

用于序列到序列语言建模的 `PeftModel`。

## [](#peft.PeftModelForQuestionAnswering) PeftModelForQuestionAnswering

用于抽取式问答的 `PeftModel`。

## [](#peft.PeftModelForFeatureExtraction) PeftModelForFeatureExtraction

用于从 Transformer 模型提取特征/嵌入的 `PeftModel`。

## [](#peft.PeftMixedModel) PeftMixedModel

用于混合不同适配器类型（如 LoRA 和 LoHa）的 `PeftModel`。

    base_model = ...  # 加载基础模型
    peft_model = PeftMixedModel.from_pretrained(base_model, path_to_adapter1, "adapter1").eval()
    peft_model.load_adapter(path_to_adapter2, "adapter2")
    peft_model.set_adapter(["adapter1", "adapter2"])  # 激活两个适配器

## [](#utilities) 工具函数

#### peft.get_peft_model

从模型和配置返回 PeftModel 对象。

    from peft import get_peft_model, LoraConfig

    peft_config = LoraConfig(r=8, lora_alpha=32, target_modules=["q", "v"], lora_dropout=0.1)
    peft_model = get_peft_model(model, peft_config)

#### peft.inject_adapter_in_model

在模型中原地创建 PEFT 层并注入。

#### peft.get_peft_model_state_dict

获取给定适配器的状态字典。仅包含 PEFT 参数，不包含基础模型参数。

#### peft.prepare_model_for_kbit_training

为 k-bit 量化训练准备模型。包括：将 layernorm 转换为 fp32、使输出嵌入层需要梯度、冻结基础模型层。

#### peft.get_layer_status

获取模型中每个适配器层的状态。

#### peft.get_model_status

获取模型调优器的状态。

[ 在 GitHub 上更新](https://github.com/huggingface/peft/blob/main/docs/source/package_reference/peft_model.md)

[←AutoPeftModel](/docs/peft/package_reference/auto_class) [PEFT 类型→](/docs/peft/package_reference/peft_types)

[PeftModel](#peft.PeftModel)[PeftModelForSequenceClassification](#peft.PeftModelForSequenceClassification)[PeftModelForCausalLM](#peft.PeftModelForCausalLM)[PeftMixedModel](#peft.PeftMixedModel)[工具函数](#utilities)
