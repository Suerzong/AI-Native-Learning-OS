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

LoRA

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

# [](#lora) LoRA

Low-Rank Adaptation ([LoRA](https://huggingface.co/papers/2309.15223)) is a PEFT method that decomposes a large matrix into two smaller low-rank matrices in the attention layers. This drastically reduces the number of parameters that need to be fine-tuned.

The abstract from the paper is:

_We propose a neural language modeling system based on low-rank adaptation (LoRA) for speech recognition output rescoring. Although pretrained language models (LMs) like BERT have shown superior performance in second-pass rescoring, the high computational cost of scaling up the pretraining stage and adapting the pretrained models to specific domains limit their practical use in rescoring. Here we present a method based on low-rank decomposition to train a rescoring BERT model and adapt it to new domains using only a fraction (0.08%) of the pretrained parameters. These inserted matrices are optimized through a discriminative training objective along with a correlation-based regularization loss. The proposed low-rank adaptation Rescore-BERT (LoRB) architecture is evaluated on LibriSpeech and internal datasets with decreased training times by factors between 5.4 and 3.6._.

## [](#peft.LoraConfig) LoraConfig

### class peft.LoraConfig

[](#peft.LoraConfig) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/config.py#L323)

( task_type: Optional[Union[str, TaskType]] = None peft_type: Optional[Union[str, PeftType]] = None auto_mapping: Optional[dict] = None peft_version: Optional[str] = None base_model_name_or_path: Optional[str] = None revision: Optional[str] = None inference_mode: bool = False r: int = 8 target_modules: Optional[Union[list[str], str]] = None exclude_modules: Optional[Union[list[str], str]] = None lora_alpha: int = 8 lora_dropout: float = 0.0 fan_in_fan_out: bool = False bias: Literal['none', 'all', 'lora_only'] = 'none' use_rslora: bool = False modules_to_save: Optional[list[str]] = None init_lora_weights: bool | Literal['gaussian', 'eva', 'olora', 'pissa', 'pissa_niter_[number of iters]', 'corda', 'loftq', 'orthogonal'] = True layers_to_transform: Optional[Union[list[int], int]] = None layers_pattern: Optional[Union[list[str], str]] = None rank_pattern: Optional[dict] = <factory> alpha_pattern: Optional[dict] = <factory> megatron_config: Optional[dict] = None megatron_core: Optional[str] = 'megatron.core' trainable_token_indices: Optional[Union[list[int], dict[str, list[int]]]] = None loftq_config: Union[LoftQConfig, dict] = <factory> eva_config: Optional[EvaConfig] = None corda_config: Optional[CordaConfig] = None lora_ga_config: Optional[LoraGAConfig] = None use_dora: bool = False alora_invocation_tokens: Optional[list[int]] = None use_qalora: bool = False qalora_group_size: int = 16 layer_replication: Optional[list[tuple[int, int]]] = None runtime_config: LoraRuntimeConfig = <factory> lora_bias: bool = False target_parameters: Optional[list[str]] = None use_bdlora: Optional[BdLoraConfig] = None arrow_config: Optional[ArrowConfig] = None ensure_weight_tying: bool = False )

Parameters

  * [](#peft.LoraConfig.r) **r** (`int`) -- Lora attention dimension (the "rank").
  * [](#peft.LoraConfig.target_modules) **target_modules** (`Optional[Union[List[str], str]]`) -- The names of the modules to apply the adapter to. If this is specified, only the modules with the specified names will be replaced. When passing a string, a regex match will be performed. When passing a list of strings, either an exact match will be performed or it is checked if the name of the module ends with any of the passed strings. If this is specified as 'all-linear', then all linear/Conv1D modules are chosen (if the model is a PreTrainedModel, the output layer excluded). If this is not specified, modules will be chosen according to the model architecture. If the architecture is not known, an error will be raised -- in this case, you should specify the target modules manually. To avoid targeting any modules (because you want to apply `target_parameters`), set `target_modules=[]`.
  * [](#peft.LoraConfig.exclude_modules) **exclude_modules** (`Optional[Union[List[str], str]]`) -- The names of the modules to not apply the adapter. When passing a string, a regex match will be performed. When passing a list of strings, either an exact match will be performed or it is checked if the name of the module ends with any of the passed strings.
  * [](#peft.LoraConfig.lora_alpha) **lora_alpha** (`int`) -- The alpha parameter for Lora scaling.
  * [](#peft.LoraConfig.lora_dropout) **lora_dropout** (`float`) -- The dropout probability for Lora layers.
  * [](#peft.LoraConfig.fan_in_fan_out) **fan_in_fan_out** (`bool`) -- Set this to True if the layer to replace stores weight like (fan_in, fan_out). For example, gpt-2 uses `Conv1D` which stores weights like (fan_in, fan_out) and hence this should be set to `True`.
  * [](#peft.LoraConfig.bias) **bias** (`str`) -- Bias type for LoRA. Can be 'none', 'all' or 'lora_only'. If 'all' or 'lora_only', the corresponding biases will be updated during training. Be aware that this means that, even when disabling the adapters, the model will not produce the same output as the base model would have without adaptation.
  * [](#peft.LoraConfig.use_rslora) **use_rslora** (`bool`) -- When set to True, uses [Rank-Stabilized LoRA](https://huggingface.co/papers/2312.03732) which sets the adapter scaling factor to `lora_alpha/math.sqrt(r)`, since it was proven to work better. Otherwise, it will use the original default value of `lora_alpha/r`.
  * [](#peft.LoraConfig.modules_to_save) **modules_to_save** (`List[str]`) -- List of modules apart from adapter layers to be set as trainable and saved in the final checkpoint.
  * [](#peft.LoraConfig.init_lora_weights) **init_lora_weights** (`bool` | `Literal["gaussian", "eva", "olora", "pissa", "pissa_niter_[number of iters]", "corda", "loftq", "orthogonal"]`) -- How to initialize the weights of the adapter layers. Passing True (default) results in the default initialization from the reference implementation from Microsoft, with the LoRA B weight being set to 0. This means that without further training, the LoRA adapter will be a no-op. Setting the initialization to False leads to random initialization of LoRA A and B, meaning that LoRA is not a no-op before training; this setting is intended for debugging purposes. Passing 'gaussian' results in Gaussian initialization scaled by the LoRA rank for linear and layers. Pass `'loftq'` to use LoftQ initialization. Passing `'eva'` results in a data-driven initialization of [Explained Variance Adaptation](https://huggingface.co/papers/2410.07170). EVA initializes LoRA based on the SVD of layer input activations and achieves SOTA performance due to its ability to adapt to the finetuning data. Pass `'olora'` to use OLoRA initialization. Passing `'pissa'` results in the initialization of [https://huggingface.co/papers/2404.02948'](’<a)

> Principal Singular values and Singular vectors Adaptation (PiSSA), which converges more rapidly than LoRA and ultimately achieves superior performance. Moreover, PiSSA reduces the quantization error compared to QLoRA, leading to further enhancements. Passing `'pissa_niter_[number of iters]'` initiates Fast-SVD-based PiSSA initialization, where `[number of iters]` indicates the number of subspace iterations to perform FSVD, and must be a nonnegative integer. When `[number of iters]` is set to 16, it can complete the initialization of a 7B model within seconds, and the training effect is approximately equivalent to using SVD. Passing `'corda'` results in the initialization of [Context-Oriented Decomposition Adaptation](https://huggingface.co/papers/2406.05223), which converges even more rapidly than PiSSA in Instruction-Previewed Mode, and preserves world knowledge better than LoRA in Knowledge-Preserved Mode. Passing `"orthogonal"` results in LoRA A and B being intialized orthogonally; in this, it resembles `"olora"`, but the base weights are left untouched (requires `r` to be even, only supported for linear layers for now).

  * [](#peft.LoraConfig.layers_to_transform) **layers_to_transform** (`Union[List[int], int]`) -- The layer indices to transform. If a list of ints is passed, it will apply the adapter to the layer indices that are specified in this list. If a single integer is passed, it will apply the transformations on the layer at this index.
  * [](#peft.LoraConfig.layers_pattern) **layers_pattern** (`Optional[Union[List[str], str]]`) -- The layer pattern name, used only if `layers_to_transform` is different from `None`. This should target the `nn.ModuleList` of the model, which is often called `'layers'` or `'h'`.
  * [](#peft.LoraConfig.rank_pattern) **rank_pattern** (`dict`) -- The mapping from layer names or regexp expression to ranks which are different from the default rank specified by `r`. For example, `{'^model.decoder.layers.0.encoder_attn.k_proj': 16}`.
  * [](#peft.LoraConfig.alpha_pattern) **alpha_pattern** (`dict`) -- The mapping from layer names or regexp expression to alphas which are different from the default alpha specified by `lora_alpha`. For example, `{'^model.decoder.layers.0.encoder_attn.k_proj': 16}`.
  * [](#peft.LoraConfig.megatron_config) **megatron_config** (`Optional[dict]`) -- The TransformerConfig arguments for Megatron. It is used to create LoRA's parallel linear layer. You can get it like this, `core_transformer_config_from_args(get_args())`, these two functions being from Megatron. The arguments will be used to initialize the TransformerConfig of Megatron. You need to specify this parameter when you want to apply LoRA to the ColumnParallelLinear and RowParallelLinear layers of megatron.
  * [](#peft.LoraConfig.megatron_core) **megatron_core** (`Optional[str]`) -- The core module from Megatron to use, defaults to `"megatron.core"`.
  * [](#peft.LoraConfig.trainable_token_indices) **trainable_token_indices** (`Optional[Union[List[int], dict[str, List[int]]]]`) -- Lets you specify which token indices to selectively fine-tune without requiring to re-train the whole embedding matrix using the `peft.TrainableTokensModel` method. You can specify token indices in two ways. Either you specify a list of indices which will then target the model's input embedding layer (or, if not found, `embed_tokens`). Alternatively, you can specify a dictionary where the key is the name of the embedding module and the values are the list of token indices, e.g. `{'embed_tokens': [0, 1, ...]}`. Note that training with FSDP requires `use_orig_params=True` to avoid issues with non-uniform `requires_grad`.
  * [](#peft.LoraConfig.loftq_config) **loftq_config** (`Optional[LoftQConfig]`) -- The configuration of LoftQ. If this is not None, then LoftQ will be used to quantize the backbone weights and initialize Lora layers. Also pass `init_lora_weights='loftq'`. Note that you should not pass a quantized model in this case, as LoftQ will quantize the model itself.
  * [](#peft.LoraConfig.eva_config) **eva_config** (`Optional[EvaConfig]`) -- The configuration of EVA. At a minimum the dataset argument needs to be set (use the same dataset as for finetuning).
  * [](#peft.LoraConfig.corda_config) **corda_config** (`Optional[CordaConfig]`) -- The configuration of CorDA. If this is not None, then CorDA will be used to build the adapter layers. Also pass `init_lora_weights='corda'`.
  * [](#peft.LoraConfig.use_dora) **use_dora** (`bool`) -- Enable 'Weight-Decomposed Low-Rank Adaptation' (DoRA). This technique decomposes the updates of the weights into two parts, magnitude and direction. Direction is handled by normal LoRA, whereas the magnitude is handled by a separate learnable parameter. This can improve the performance of LoRA especially at low ranks. Right now, DoRA only supports linear and Conv2D layers. DoRA introduces a bigger overhead than pure LoRA, so it is recommended to merge weights for inference. For more information, see <https://huggingface.co/papers/2402.09353>.
  * [](#peft.LoraConfig.alora_invocation_tokens) **alora_invocation_tokens** (`List[int]`) -- If not None, enable ['Activated LoRA' (aLoRA)](https://huggingface.co/papers/2504.12397), with alora_invocation_tokens being the tokenized invocation string for the adapter (must be present in all model input strings). This technique selectively activates the adapter weights only on tokens during and after the alora_invocation_tokens. When used in a CausalLM, this means that the KV cache prior to invocation is interchangeable with that of the base model (and other aLoRA adapters operating this way). As a result, in inference pipelines involving switching between base model inference and adapter inference (e.g. agentic pipelines, see paper for examples), significant savings are realized (relative to LoRA) by saving prefill operations. Overall adapter inference speedups of an order of magnitude or more can occur on vLLM, depending on the length of the shared context. Note that merging is not possible due to the selective application of the weights.
  * [](#peft.LoraConfig.layer_replication) **layer_replication** (`List[Tuple[int, int]]`) -- Build a new stack of layers by stacking the original model layers according to the ranges specified. This allows expanding (or shrinking) the model without duplicating the base model weights. The new layers will all have separate LoRA adapters attached to them.
  * [](#peft.LoraConfig.runtime_config) **runtime_config** (`LoraRuntimeConfig`) -- Runtime configurations (which are not saved or restored).
  * [](#peft.LoraConfig.lora_bias) **lora_bias** (`bool`) -- Defaults to `False`. Whether to enable the bias term for the LoRA B parameter. Typically, this should be disabled. The main use case for this is when the LoRA weights were extracted from fully fine-tuned parameters so the bias of those parameters can be taken into account.
  * [](#peft.LoraConfig.target_parameters) **target_parameters** (`List[str]`, _optional_) -- List of parameter names or regex expression of the parameter names to replace with LoRA. This argument behaves similarly to `target_modules`, except that the parameter name should be passed. Generally, you should use `target_modules` to target the module (e.g. `nn.Linear`). However, in some circumstances, this is not possible. E.g., in many mixture of expert (MoE) layers in HF Transformers, instead of using `nn.Linear`, an `nn.Parameter` is used. PEFT normally overwrites the `forward` method for LoRA, but for `nn.Parameter`, there is none. Therefore, to apply LoRA to that parameter, it needs to be targeted with `target_parameters`. As an example, for Llama4, you can pass: `target_parameters=['feed_forward.experts.gate_up_proj', 'feed_forward.experts.down_proj]`. Passing a string for regex matching is not implemented yet.
  * [](#peft.LoraConfig.ensure_weight_tying) **ensure_weight_tying** (`bool`, _optional_) -- Whether to tie weights or not after peft initialization. This will ensure that the adapters added to the tied layers are also tied. This is only applicable for layers passed via `modules_to_save` and `target_modules`.

This is the configuration class to store the configuration of a [LoraModel](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraModel).

#### to_dict

[](#peft.LoraConfig.to_dict) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/config.py#L774)

( )

Returns the configuration for your adapter model as a dictionary. Removes runtime configurations.

## [](#peft.LoraModel) LoraModel

### class peft.LoraModel

[](#peft.LoraModel) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/model.py#L88)

( model peft_config: Union[PeftConfig, dict[str, PeftConfig]] adapter_name: str low_cpu_mem_usage: bool = False state_dict: Optional[dict[str, torch.Tensor]] = None ) → `torch.nn.Module`

Parameters

  * [](#peft.LoraModel.model) **model** (`torch.nn.Module`) -- The model to be adapted.
  * [](#peft.LoraModel.config) **config** ([LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig)) -- The configuration of the Lora model.
  * [](#peft.LoraModel.adapter_name) **adapter_name** (`str`) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.LoraModel.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the loading process.

Returns

`torch.nn.Module`

The Lora model.

Creates Low Rank Adapter (LoRA) model from a pretrained transformers model.

The method is described in detail in <https://huggingface.co/papers/2106.09685>.

[](#peft.LoraModel.example)

Example:

Copied


    >>> from transformers import AutoModelForSeq2SeqLM
    >>> from peft import LoraModel, LoraConfig

    >>> config = LoraConfig(
    ...     task_type="SEQ_2_SEQ_LM",
    ...     r=8,
    ...     lora_alpha=32,
    ...     target_modules=["q", "v"],
    ...     lora_dropout=0.01,
    ... )

    >>> model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
    >>> lora_model = LoraModel(model, config, "default")

[](#peft.LoraModel.example-2)

Copied


    >>> import torch
    >>> import transformers
    >>> from peft import LoraConfig, PeftModel, get_peft_model, prepare_model_for_kbit_training

    >>> rank = ...
    >>> target_modules = ["q_proj", "k_proj", "v_proj", "out_proj", "fc_in", "fc_out", "wte"]
    >>> config = LoraConfig(
    ...     r=4, lora_alpha=16, target_modules=target_modules, lora_dropout=0.1, bias="none", task_type="CAUSAL_LM"
    ... )
    >>> quantization_config = transformers.BitsAndBytesConfig(load_in_8bit=True)

    >>> tokenizer = transformers.AutoTokenizer.from_pretrained(
    ...     "kakaobrain/kogpt",
    ...     revision="KoGPT6B-ryan1.5b-float16",  # or float32 version: revision=KoGPT6B-ryan1.5b
    ...     bos_token="[BOS]",
    ...     eos_token="[EOS]",
    ...     unk_token="[UNK]",
    ...     pad_token="[PAD]",
    ...     mask_token="[MASK]",
    ... )
    >>> model = transformers.GPTJForCausalLM.from_pretrained(
    ...     "kakaobrain/kogpt",
    ...     revision="KoGPT6B-ryan1.5b-float16",  # or float32 version: revision=KoGPT6B-ryan1.5b
    ...     pad_token_id=tokenizer.eos_token_id,
    ...     use_cache=False,
    ...     device_map={"": rank},
    ...     torch_dtype=torch.float16,
    ...     quantization_config=quantization_config,
    ... )
    >>> model = prepare_model_for_kbit_training(model)
    >>> lora_model = get_peft_model(model, config)

**Attributes** :

  * **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) — The model to be adapted.
  * **peft_config** ([LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig)): The configuration of the Lora model.

#### add_weighted_adapter

[](#peft.LoraModel.add_weighted_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/model.py#L652)

( adapters: list[str] weights: list[float] adapter_name: str combination_type: str = 'svd' svd_rank: int | None = None svd_clamp: int | None = None svd_full_matrices: bool = True svd_driver: str | None = None density: float | None = None majority_sign_method: Literal['total', 'frequency'] = 'total' )

Parameters

  * [](#peft.LoraModel.add_weighted_adapter.adapters) **adapters** (`list`) -- List of adapter names to be merged.
  * [](#peft.LoraModel.add_weighted_adapter.weights) **weights** (`list`) -- List of weights for each adapter. Weights can be positive or negative, allowing for both addition and subtraction of adapter effects.
  * [](#peft.LoraModel.add_weighted_adapter.adapter_name) **adapter_name** (`str`) -- Name of the new adapter.
  * [](#peft.LoraModel.add_weighted_adapter.combination_type) **combination_type** (`str`) -- The merging type can be one of [`svd`, `linear`, `cat`, `ties`, `ties_svd`, `dare_ties`, `dare_linear`, `dare_ties_svd`, `dare_linear_svd`, `magnitude_prune`, `magnitude_prune_svd`]. When using the `cat` combination_type, the rank of the resulting adapter is equal to the sum of all adapters ranks (the mixed adapter may be too big and result in OOM errors).
  * [](#peft.LoraModel.add_weighted_adapter.svd_rank) **svd_rank** (`int`, _optional_) -- Rank of output adapter for svd. If None provided, will use max rank of merging adapters.
  * [](#peft.LoraModel.add_weighted_adapter.svd_clamp) **svd_clamp** (`float`, _optional_) -- A quantile threshold for clamping SVD decomposition output. If None is provided, do not perform clamping. Defaults to None.
  * [](#peft.LoraModel.add_weighted_adapter.svd_full_matrices) **svd_full_matrices** (`bool`, _optional_) -- Controls whether to compute the full or reduced SVD, and consequently, the shape of the returned tensors U and Vh. Defaults to True.
  * [](#peft.LoraModel.add_weighted_adapter.svd_driver) **svd_driver** (`str`, _optional_) -- Name of the cuSOLVER method to be used. This keyword argument only works when merging on CUDA. Can be one of [None, `gesvd`, `gesvdj`, `gesvda`]. For more info please refer to `torch.linalg.svd` documentation. Defaults to None.
  * [](#peft.LoraModel.add_weighted_adapter.density) **density** (`float`, _optional_) -- Value between 0 and 1. 0 means all values are pruned and 1 means no values are pruned. Should be used with [`ties`, `ties_svd`, `dare_ties`, `dare_linear`, `dare_ties_svd`, `dare_linear_svd`, `magnintude_prune`, `magnitude_prune_svd`]
  * [](#peft.LoraModel.add_weighted_adapter.majority_sign_method) **majority_sign_method** (`str`) -- The method, should be one of ["total", "frequency"], to use to get the magnitude of the sign values. Should be used with [`ties`, `ties_svd`, `dare_ties`, `dare_ties_svd`]

This method adds a new adapter by merging the given adapters with the given weights.

When using the `cat` combination_type you should be aware that rank of the resulting adapter will be equal to the sum of all adapters ranks. So it’s possible that the mixed adapter may become too big and result in OOM errors.

#### subtract_mutated_init

[](#peft.LoraModel.subtract_mutated_init) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/model.py#L909)

( output_state_dict: dict[str, torch.Tensor] adapter_name: str kwargs = None )

This function can calculate the updates of the PiSSA/CorDA/OLoRA by comparing the parameters of the PiSSA/CorDA/OLoRA adapter in `output_state_dict` with the initial values of PiSSA/CorDA/OLoRA in `adapter_name`, thus converting PiSSA/CorDA/OLoRA to LoRA.

## [](#utility) Utility

### [](#peft.ArrowConfig) ArrowConfig

### class peft.ArrowConfig

[](#peft.ArrowConfig) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/config.py#L74)

( top_k: int = 3 router_temperature: float = 1.0 use_gks: bool = False rng_seed: Optional[int] = None )

This is the sub-configuration class to store the configuration for Arrow and GenKnowSub algorithm. Arrow is a routing algorithm to combine the trained LoRA modules to solve new tasks, proposed in ’[https://huggingface.co/papers/2405.11157’](https://huggingface.co/papers/2405.11157'). GenKnowSub is a refinement on the trained modules before being combined via Arrow, introduced in ’[https://aclanthology.org/2025.acl-short.54/’](https://aclanthology.org/2025.acl-short.54/')

### [](#peft.replace_lora_weights_loftq) LoftQ

#### peft.replace_lora_weights_loftq

[](#peft.replace_lora_weights_loftq) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/utils/loftq_utils.py#L353)

( peft_model model_path: Optional[str] = None adapter_name: str = 'default' callback: Optional[Callable[[torch.nn.Module, str], bool]] = None )

Parameters

  * [](#peft.replace_lora_weights_loftq.peft_model) **peft_model** (`PeftModel`) -- The model to replace the weights of. Must be a quantized PEFT model with LoRA layers.
  * [](#peft.replace_lora_weights_loftq.model_path) **model_path** (`Optional[str]`) -- The path to the model safetensors file. If the model is a Hugging Face model, this will be inferred from the model's config. Otherwise, it must be provided.
  * [](#peft.replace_lora_weights_loftq.adapter_name) **adapter_name** (`str`) -- The name of the adapter to replace the weights of. The default adapter name is "default".
  * [](#peft.replace_lora_weights_loftq.callback) **callback** (`Optional[Callable[[PeftModel, str], bool]]`) -- A callback function that will be called after each module is replaced. The callback function should take the model and the name of the current module as input and return a boolean indicating whether the replacement should be kept. If the callback returns False, the replacement will be rolled back. This can be very useful to confirm that the LoftQ initialization actually decreases the quantization error of the model. As an example, this callback could generate logits for given input and compare it with the logits from the original, non-quanitzed model with the same input, and only return `True` if there is an improvement. As this is a greedy optimization, it's possible that calling this function multiple times yields incremental improvements.

Replace the LoRA weights of a model quantized with bitsandbytes, using the LoftQ technique.

The replacement is done on the fly by loading in the non-quantized weights from a locally stored safetensors model file and initializing the LoRA weights such that the quantization error between the original and quantized weights is minimized.

As lazy loading is not possible with pickle, normal PyTorch checkpoint files cannot be supported.

Depending on the model size, calling this function may take some time to finish.

### [](#eva) Eva

#### [](#peft.EvaConfig) EvaConfig

### class peft.EvaConfig

[](#peft.EvaConfig) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/config.py#L196)

( rho: float = 2.0 tau: float = 0.99 use_label_mask: bool = True label_mask_value: int = -100 whiten: bool = False adjust_scaling_factors: bool = True )

Parameters

  * [](#peft.EvaConfig.rho) **rho** (`float`) -- Rho value for EVA redistribution (>= 1.0). The maximum rank for a layer is lora_r * rho. Default is 2.0, meaning the maximum rank allowed for a layer is 2r. Increasing rho will allow for a higher degree of redistribution of ranks across layers. Some pre-trained models might be more sensitive to a rank redistribution. It can therefore be beneficial to try rho=1.0 (no redistribution) if the performance is lower than expected.
  * [](#peft.EvaConfig.tau) **tau** (`float`) -- Cosine similarity threshold for early stopping. Compares the cosine similarity of right-singular vectors between two consecutive SVD steps. If the cosine similarity is above this threshold, the SVD iteration is stopped. Default is 0.99.
  * [](#peft.EvaConfig.use_label_mask) **use_label_mask** (`bool`) -- Use label mask for EVA initialization. This means that positions where labels=label_mask_value are ignored for the SVD computation. Setting use_label_mask=True is preferred in most cases and can be especially beneficial for multi-turn conversations. The default value is True. Filtering out items based on the label mask can sometimes lead to a small batch size and as a result instabilities in the SVD computation. For cases where a large share of batch items would be filtered out, set use_label_mask=False.
  * [](#peft.EvaConfig.label_mask_value) **label_mask_value** (`int`) -- If use_label_mask=True the value to look for to mask out ignored tokens. Default is -100.
  * [](#peft.EvaConfig.whiten) **whiten** (`bool`) -- Apply whitening to singular vectors. Default is False. Whitening has been shown to be beneficial for EVA in the vision domain.
  * [](#peft.EvaConfig.adjust_scaling_factors) **adjust_scaling_factors** (`bool`) -- Adjust LoRA scaling factors after the rank redistribution. Setting this to True means the scaling factors are adjusted so that all LoRA gradients have the same scale regardless of their rank. Default is True.

This is the sub-configuration class to store the configuration for a data-driven initialization via EVA. EVA was introduced in [Explained Variance Adaptation](https://huggingface.co/papers/2410.07170).

#### [](#peft.initialize_lora_eva_weights) initialize_lora_eva_weights

#### peft.initialize_lora_eva_weights

[](#peft.initialize_lora_eva_weights) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/eva.py#L654)

( model: Module dataloader: typing.Optional[collections.abc.Iterable] = None eva_state_dict: typing.Optional[dict] = None forward_fn: typing.Optional[collections.abc.Callable] = <function forward_fn_dict at 0x7f812213bac0> prepare_model_inputs_fn: typing.Optional[collections.abc.Callable] = <function prepare_model_inputs_fn_language_modeling at 0x7f812213b9a0> prepare_layer_inputs_fn: typing.Union[collections.abc.Callable, dict[str, collections.abc.Callable], NoneType] = <function prepare_layer_inputs_fn_language_modeling at 0x7f812213ba30> adapter_name: str = 'default' gather_distributed_inputs: bool = True show_progress_bar: bool = True ) → model (torch.nn.Module)

Parameters

  * [](#peft.initialize_lora_eva_weights.model) **model** (PeftModel) -- The peft model to compute the SVD for.
  * [](#peft.initialize_lora_eva_weights.dataloader) **dataloader** (Optional[Iterable]) -- The dataloader to use for the forward pass. If None, eva_state_dict needs to be provided.
  * [](#peft.initialize_lora_eva_weights.eva_state_dict) **eva_state_dict** (Optional[dict]) -- The state_dict to load into the model. If None, a dataloader needs to be provided and the state_dict will be computed using `get_eva_state_dict`.
  * [](#peft.initialize_lora_eva_weights.forward_fn) **forward_fn** (Callable) -- The forward function to use for the forward pass. Takes two arguments: `model` and `inputs`. Default behavior is `return model(**inputs)`
  * [](#peft.initialize_lora_eva_weights.prepare_model_inputs_fn) **prepare_model_inputs_fn** (Optional[Callable]) -- This function receives the model inputs and the peft_config and passes the output to `prepare_layer_inputs_fn`. Can be used to modify the input to the SVD computation based on the original model inputs. For example for language modeling the attention mask is used to determine which indices are padding tokens and should not be used for SVD. Any function defined here expects two arguments: `model_input` and `peft_config`. `peft.tuners.lora.eva.prepare_model_inputs_fn_language_modeling` is used by default.
  * [](#peft.initialize_lora_eva_weights.prepare_layer_inputs_fn) **prepare_layer_inputs_fn** (Union[Callable, Dict[str, Callable], None]) -- This function receives the layer inputs, the model inputs (potentially modified by `prepare_model_inputs_fn`) and the name of the layer and returns the inputs that should be used for SVD for that particular layer. Any custom function defined here expects three arguments: `layer_input`, `model_input`, and `layer_name` and should return a 2d tensor. The default logic can be found in peft.tuners.lora.eva.prepare_layer_inputs_fn_language_modeling and works for language modeling. In this case model_inputs is the mask used to determine which indices should be used for SVD (created by `prepare_model_inputs_fn_language_modeling`).
  * [](#peft.initialize_lora_eva_weights.adapter_name) **adapter_name** (str) -- The name of the adapter to initialize the weights for.
  * [](#peft.initialize_lora_eva_weights.gather_distributed_inputs) **gather_distributed_inputs** (bool) -- Whether to gather the layer inputs from all ranks. Default is True meaning in a distributed setting the layer inputs will be gathered from all ranks for the SVD computation. For non-distributed settings this argument is ignored. Set to False if you are using a non-distributed dataloader in a distributed setting.
  * [](#peft.initialize_lora_eva_weights.show_progress_bar) **show_progress_bar** (bool) -- Whether to show a progress bar. Default is True.

Returns

model (torch.nn.Module)

The model with the initialized LoRA weights.

Initialize the weights of the LoRA layers using the EVA method.

This function initializes the weights of the LoRA layers using the EVA method. It computes the SVD for each adapter layer and updates the weights accordingly.

#### [](#peft.get_eva_state_dict) get_eva_state_dict

#### peft.get_eva_state_dict

[](#peft.get_eva_state_dict) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/eva.py#L556)

( model: Module dataloader: Iterable peft_config: typing.Optional[peft.tuners.lora.config.LoraConfig] = None forward_fn: typing.Optional[collections.abc.Callable] = <function forward_fn_dict at 0x7f812213bac0> prepare_model_inputs_fn: typing.Optional[collections.abc.Callable] = <function prepare_model_inputs_fn_language_modeling at 0x7f812213b9a0> prepare_layer_inputs_fn: typing.Union[collections.abc.Callable, dict[str, collections.abc.Callable], NoneType] = <function prepare_layer_inputs_fn_language_modeling at 0x7f812213ba30> adapter_name: str = 'default' gather_distributed_inputs: bool = True show_progress_bar: bool = True ) → eva_state_dict (dict)

Parameters

  * [](#peft.get_eva_state_dict.model) **model** (torch.nn.Module) -- The model to compute the SVD for. Does not need to be a PeftModel.
  * [](#peft.get_eva_state_dict.dataloader) **dataloader** (Iterable) -- The dataloader to use for the forward pass.
  * [](#peft.get_eva_state_dict.peft_config) **peft_config** (Optional[LoraConfig]) -- The configuration for the LoRA layers. Only required if `model` is not a PeftModel.
  * [](#peft.get_eva_state_dict.forward_fn) **forward_fn** (Callable) -- The forward function to use for the forward pass. Takes two arguments: `model` and `inputs`. Default behavior is `return model(**inputs)`
  * [](#peft.get_eva_state_dict.prepare_model_inputs_fn) **prepare_model_inputs_fn** (Optional[Callable]) -- This function receives the model inputs and the peft_config and passes the output to `prepare_layer_inputs_fn`. Can be used to modify the input to the SVD computation based on the original model inputs. For example for language modeling the attention mask is used to determine which indices are padding tokens and should not be used for SVD. Any function defined here expects two arguments: `model_input` and `peft_config`. `peft.tuners.lora.eva.prepare_model_inputs_fn_language_modeling` is used by default.
  * [](#peft.get_eva_state_dict.prepare_layer_inputs_fn) **prepare_layer_inputs_fn** (Union[Callable, Dict[str, Callable], None]) -- This function receives the layer inputs, the model inputs (potentially modified by `prepare_model_inputs_fn`) and the name of the layer and returns the inputs that should be used for SVD for that particular layer. Any custom function defined here expects three arguments: `layer_input`, `model_input`, and `layer_name` and should return a 2d tensor. The default logic can be found in peft.tuners.lora.eva.prepare_layer_inputs_fn_language_modeling and works for language modeling. In this case model_inputs is the mask used to determine which indices should be used for SVD (created by `prepare_model_inputs_fn_language_modeling`).
  * [](#peft.get_eva_state_dict.adapter_name) **adapter_name** (str) -- The name of the adapter to compute the SVD for.
  * [](#peft.get_eva_state_dict.gather_distributed_inputs) **gather_distributed_inputs** (bool) -- Whether to gather the layer inputs from all ranks. Default is True meaning in a distributed setting the layer inputs will be gathered from all ranks for the SVD computation. For non-distributed settings this argument is ignored. Set to False if you are using a non-distributed dataloader in a distributed setting.
  * [](#peft.get_eva_state_dict.show_progress_bar) **show_progress_bar** (bool) -- Whether to show a progress bar. Default is True.

Returns

eva_state_dict (dict)

The state dictionary containing the SVD components for each layer.

Compute the SVD for each layer in the model.

This function computes the Singular Value Decomposition (SVD) for each layer in the model. It uses the incremental PCA method to compute the SVD components. The function also checks for convergence of the computed components using cosine similarity. The rank distribution for each layer is determined based on the explained variance ratio.

## [](#variants) Variants

### [](#lora-ga) LoRA-GA

[LoRA-GA](https://hf.co/papers/2407.05000) (Low-Rank Adaptation with Gradient Approximation) improves upon standard LoRA by using gradient information during initialization to achieve faster convergence. Instead of random initialization, LoRA-GA performs SVD on estimated gradients to initialize adapter weights in a direction that aligns with full fine-tuning, resulting in 2-4x faster convergence with the same final performance.

The abstract from the paper is:

_Low-rank adaptation (LoRA) is a popular technique for parameter-efficient fine-tuning of large language models. However, LoRA’s random initialization of adapter weights leads to slow convergence during the initial training phase. In this paper, we propose LoRA-GA (Low-Rank Adaptation with Gradient Approximation), a novel initialization method that leverages gradient information to initialize LoRA adapters. Specifically, we estimate gradients on a small set of training samples and perform singular value decomposition (SVD) to extract principal components. These components are used to initialize the adapter matrices, aligning the initial update direction with that of full fine-tuning. Our experiments across various tasks and model scales demonstrate that LoRA-GA achieves 2-4x faster convergence compared to standard LoRA while maintaining the same final performance. The method is orthogonal to existing LoRA variants and can be easily integrated with techniques like DoRA and LoRA+._

#### [](#usage-tips) Usage Tips

  * **Gradient Estimation** : LoRA-GA requires a gradient estimation phase before model initialization. Use `preprocess_loraga()` with a `train_step` callback to compute gradients over a small number of training batches (typically 64-128 batches).

  * **Initialization Strategies** : LoRA-GA supports four direction strategies (`direction`): `"ArBr"`, `"A2rBr"`, `"ArB2r"` (default), and `"random"`, and four scaling strategies (`scale`): `"stable"` (default), `"weight_svd"`, `"gd_scale"`, and `"unit"`. The default combination provides the best balance of convergence speed and stability.

  * **Base Weight Modification** : Unlike standard LoRA, LoRA-GA modifies the base model weights during initialization by subtracting a scaled version of the low-rank approximation. This enables better alignment with full fine-tuning gradients. Since base weights are modified, use `save_pretrained()` with the `save_embedding_layers` argument or `save_mutated_as_lora` pattern to properly save the adapter.

  * **Computational Overhead** : The gradient estimation adds a small overhead during initialization (typically 1-2 minutes for 64 batches), but this is quickly amortized by faster convergence during training.

  * **Compatibility** : LoRA-GA requires full-precision weights and does not support quantized models. Can be combined with other LoRA variants like DoRA.

#### [](#peft.LoraGAConfig) LoraGAConfig

### class peft.LoraGAConfig

[](#peft.LoraGAConfig) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/config.py#L898)

( direction: Literal['ArBr', 'A2rBr', 'ArB2r', 'random'] = 'ArB2r' scale: Literal['stable', 'weight_svd', 'gd_scale', 'unit'] = 'stable' stable_gamma: int = 16 )

Parameters

  * [](#peft.LoraGAConfig.direction) **direction** (`Literal["ArBr", "A2rBr", "ArB2r", "random"]`) -- Strategy for distributing gradient SVD components to lora_A and lora_B matrices.
    * "ArBr": Alternating indices (A takes odd, B takes even)
    * "A2rBr": A takes indices [r:2r], B takes indices [:r]
    * "ArB2r": A takes indices [:r], B takes indices [r:2r] (recommended)
    * "random": Random selection of indices Default: "ArB2r"
  * [](#peft.LoraGAConfig.scale) **scale** (`Literal["stable", "weight_svd", "gd_scale", "unit"]`) -- Scaling strategy for adapter initialization.
    * "stable": Stable scaling with gamma parameter
    * "weight_svd": Scale based on weight matrix singular values
    * "gd_scale": Gradient descent based scaling
    * "unit": No additional scaling Default: "stable"
  * [](#peft.LoraGAConfig.stable_gamma) **stable_gamma** (`int`) -- Gamma parameter for stable scaling method. Default: 16

This is the sub-configuration class to store the configuration for LoRA-GA initialization.

LoRA-GA (Low-Rank Adaptation with Gradient Approximation) uses gradient information during initialization to achieve faster convergence (2-4x speedup) by aligning the initial adapter weights with the direction of full fine-tuning gradients.

Reference: <https://arxiv.org/abs/2407.05000>

#### [](#peft.tuners.lora.loraga.estimate_gradients) Utilities

#### peft.tuners.lora.loraga.estimate_gradients

[](#peft.tuners.lora.loraga.estimate_gradients) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/loraga.py#L118)

( model: Module lora_config: LoraConfig train_step: Callable )

Estimate gradients for LoRA-GA initialization.

This function enables gradient computation ONLY on target module weights and runs the train_step callback. This is more memory-efficient than enabling gradients globally.

#### peft.preprocess_loraga

[](#peft.preprocess_loraga) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/loraga.py#L46)

( model: Module lora_config: LoraConfig train_step: Callable cache_file: typing.Optional[str] = None )

Parameters

  * [](#peft.preprocess_loraga.model) **model** (`nn.Module`) -- Model to preprocess.
  * [](#peft.preprocess_loraga.lora_config) **lora_config** (`LoraConfig`) -- Lora configuration of the model. `lora_config.lora_ga_config` should be set.
  * [](#peft.preprocess_loraga.train_step) **train_step** (`Callable[[], None]`) -- Callback to run gradient estimation. Typically you should run model forward and backward passes in this callback. The gradients will be accumulated across all calls within this callback.
  * [](#peft.preprocess_loraga.cache_file) **cache_file** (`Optional[str]`) -- Optional path to cache file for saving/loading gradients. If provided and the file exists, gradients will be loaded from cache. Otherwise, gradients will be estimated and saved to this path.

Build necessary LoRA-GA fields for a model by estimating gradients.

For each linear layer, gradients will be estimated by running the provided train_step callback. These gradients are then attached to the modules and used during initialization.

Upon completion, the following fields are set for each target module: _peft_loraga_grad (`torch.Tensor`): Accumulated gradient for the weight matrix.

## [](#peft.tuners.lora.intruders.reduce_intruder_dimension) Intruder Dimension Reduction

#### peft.tuners.lora.intruders.reduce_intruder_dimension

[](#peft.tuners.lora.intruders.reduce_intruder_dimension) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/tuners/lora/intruders.py#L20)

( peft_model old_adapter_name = 'default' new_adapter_name = 'intruder_reduced' top_k = 10 threshold_epsilon = 0.5 mitigation_lambda = 0.75 logging_sink = <built-in function print> )

Parameters

  * [](#peft.tuners.lora.intruders.reduce_intruder_dimension.peft_model) **peft_model** -- The PEFT model with a loaded LoRA adapter with the name provided in `old_adapter_name`. Currently mixed models are not supported.
  * [](#peft.tuners.lora.intruders.reduce_intruder_dimension.top_k) **top_k** (default -- 10) Consider the top-k dimensions for intruder detection. The larger the value, the more dimensions will be considered for intruder detection analysis (and the more false-postiives there can be). Operates on the cosine similarity between base weights and adapter weights roughly sorted by influence of dimension (determined by singular value decomposition), so a top-k of 10 will look at the 10 most 'important' dimensions.
  * [](#peft.tuners.lora.intruders.reduce_intruder_dimension.threshold_epsilon) **threshold_epsilon** (default -- 0.5) Threshold value when to consider a cosine similarity between base weight and adapter weight as intruder. According to the paper, intruder dimensions show near-zero absolute cosine similarity with pre-trained singular vectors. The lower this value, the less potential intruder dimensions are identified. The higher the value, the more potential false-positives are considered as intruders.
  * [](#peft.tuners.lora.intruders.reduce_intruder_dimension.mitigation_lambda) **mitigation_lambda** (default -- 0.75) The relative portion of the intruder dimensions that is subtracted from the adapter's delta weight. The higher the value the more of the intruder dimension is subtracted but the more information is lost. Refer to Figure 8 in the paper for a trade-off analysis.
  * [](#peft.tuners.lora.intruders.reduce_intruder_dimension.logging_sink) **logging_sink** (default -- print) Function that prints information about the mitigation process. Set to None if you don't want any output.

Intruder dimension mitigation based on <https://huggingface.co/papers/2410.21228> (“LoRA vs Full Fine-tuning: An Illusion of Equivalence”).

This method can recover previous knowledge (i.e. mitigate forgetting) by post-processing already trained low-rank adapters. This comes at a cost of task accuracy - tuning the `migration_lambda` value can be used to trade between these two factors.

After mitigation is done there will be a new adapter with the name set in `new_adapter_name` which is also set to be the currently active adapter. Inference on the mitigated model will therefore use the modified adapter. To switch back to the original adapter you can use `peft_model.set_adapter(<old_adapter_name>)`.

Currently only LoRA is supported as it is not clear whether this method generalizes to other delta-weight methods.

[ Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/package_reference/lora.md)

[←LoKr](/docs/peft/package_reference/lokr) [OSF→](/docs/peft/package_reference/osf)

[LoRA](#lora)[LoraConfig](#peft.LoraConfig)[LoraModel](#peft.LoraModel)[Utility](#utility)[ArrowConfig](#peft.ArrowConfig)[LoftQ](#peft.replace_lora_weights_loftq)[Eva](#eva)[EvaConfig](#peft.EvaConfig)[initialize_lora_eva_weights](#peft.initialize_lora_eva_weights)[get_eva_state_dict](#peft.get_eva_state_dict)[Variants](#variants)[LoRA-GA](#lora-ga)[Usage Tips](#usage-tips)[LoraGAConfig](#peft.LoraGAConfig)[Utilities](#peft.tuners.lora.loraga.estimate_gradients)[Intruder Dimension Reduction](#peft.tuners.lora.intruders.reduce_intruder_dimension)
