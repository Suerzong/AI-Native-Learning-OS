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

Models

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

# [](#models) Models

[PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) is the base model class for specifying the base Transformer model and configuration to apply a PEFT method to. The base `PeftModel` contains methods for loading and saving models from the Hub.

## [](#peft.PeftModel) PeftModel

### class peft.PeftModel

[](#peft.PeftModel) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L72)

( model: PreTrainedModel peft_config: PeftConfig adapter_name: str = 'default' autocast_adapter_dtype: bool = True low_cpu_mem_usage: bool = False )

Parameters

  * [](#peft.PeftModel.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- The base transformer model used for Peft.
  * [](#peft.PeftModel.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the Peft model.
  * [](#peft.PeftModel.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModel.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.
  * [](#peft.PeftModel.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the loading loading process.

> > Don't use `low_cpu_mem_usage=True` when creating a new PEFT adapter for training.

Base model encompassing various Peft methods.

**Attributes** :

  * **base_model** (`torch.nn.Module`) — The base transformer model used for Peft.
  * **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) — The configuration of the Peft model.
  * **modules_to_save** (`list` of `str`) — The list of sub-module names to save when saving the model.
  * **prompt_encoder** ([PromptEncoder](/docs/peft/v0.19.0/en/package_reference/p_tuning#peft.PromptEncoder)) — The prompt encoder used for Peft if using [PromptLearningConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PromptLearningConfig).
  * **prompt_tokens** (`torch.Tensor`) — The virtual prompt tokens used for Peft if using [PromptLearningConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PromptLearningConfig).
  * **transformer_backbone_name** (`str`) — The name of the transformer backbone in the base model if using [PromptLearningConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PromptLearningConfig).
  * **word_embeddings** (`torch.nn.Embedding`) — The word embeddings of the transformer backbone in the base model if using [PromptLearningConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PromptLearningConfig).

#### add_adapter

[](#peft.PeftModel.add_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1020)

( adapter_name: str peft_config: PeftConfig low_cpu_mem_usage: bool = False autocast_adapter_dtype: bool = True )

Parameters

  * [](#peft.PeftModel.add_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftModel.add_adapter.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the adapter to be added.
  * [](#peft.PeftModel.add_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the process when loading saved adapters. Don't use this option when creating a new PEFT adapter for training.
  * [](#peft.PeftModel.add_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Add an adapter to the model based on the passed configuration.

This adapter is not trained. To load a trained adapter, check out [PeftModel.load_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.load_adapter).

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

#### create_or_update_model_card

[](#peft.PeftModel.create_or_update_model_card) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1572)

( output_dir: str )

Updates or create model card to include information about peft:

  1. Adds `peft` library tag
  2. Adds peft version
  3. Adds base model info
  4. Adds quantization information if it was used

#### delete_adapter

[](#peft.PeftModel.delete_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1098)

( adapter_name: str )

Parameters

  * [](#peft.PeftModel.delete_adapter.adapter_name) **adapter_name** (str) -- Name of the adapter to be deleted.

Deletes an existing adapter.

#### disable_adapter

[](#peft.PeftModel.disable_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L960)

( )

Context manager that disables the adapter module. Use this to run inference on the base model.

[](#peft.PeftModel.disable_adapter.example)

Example:

Copied


    >>> with model.disable_adapter():
    ...     model(inputs)

#### forward

[](#peft.PeftModel.forward) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L939)

( *args: Any **kwargs: Any )

Forward pass of the model.

#### from_pretrained

[](#peft.PeftModel.from_pretrained) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L398)

( model: torch.nn.Module model_id: Union[str, os.PathLike] adapter_name: str = 'default' is_trainable: bool = False config: Optional[PeftConfig] = None autocast_adapter_dtype: bool = True ephemeral_gpu_offload: bool = False low_cpu_mem_usage: bool = False key_mapping: Optional[dict[str, str]] = None **kwargs: Any )

Parameters

  * [](#peft.PeftModel.from_pretrained.model) **model** (`torch.nn.Module`) -- The model to be adapted. For 🤗 Transformers models, the model should be initialized with the [from_pretrained](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.from_pretrained).
  * [](#peft.PeftModel.from_pretrained.model_id) **model_id** (`str` or `os.PathLike`) -- The name of the PEFT configuration to use. Can be either:
    * A string, the `model id` of a PEFT configuration hosted inside a model repo on the Hugging Face Hub.
    * A path to a directory containing a PEFT configuration file saved using the `save_pretrained` method (`./my_peft_config_directory/`).
  * [](#peft.PeftModel.from_pretrained.adapter_name) **adapter_name** (`str`, _optional_ , defaults to `"default"`) -- The name of the adapter to be loaded. This is useful for loading multiple adapters.
  * [](#peft.PeftModel.from_pretrained.is_trainable) **is_trainable** (`bool`, _optional_ , defaults to `False`) -- Whether the adapter should be trainable or not. If `False`, the adapter will be frozen and can only be used for inference.
  * [](#peft.PeftModel.from_pretrained.config) **config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig), _optional_) -- The configuration object to use instead of an automatically loaded configuration. This configuration object is mutually exclusive with `model_id` and `kwargs`. This is useful when configuration is already loaded before calling `from_pretrained`.
  * [](#peft.PeftModel.from_pretrained.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.
  * [](#peft.PeftModel.from_pretrained.ephemeral_gpu_offload) **ephemeral_gpu_offload** (`bool`, _optional_) -- Whether to use ephemeral GPU offloading for partially loaded modules. Defaults to `False`. This is useful when parts of the model and/or components (such as adapters) are kept in CPU memory until they are needed. Rather than perform expensive operations on small data, the data is transferred to the GPU on-demand, the operation(s) performed, and the results moved back to CPU memory. This brings a slight momentary VRAM overhead but gives orders of magnitude speedup in certain cases.
  * [](#peft.PeftModel.from_pretrained.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device before loading the saved weights. Useful to speed up the process.
  * [](#peft.PeftModel.from_pretrained.torch_device) **torch_device** (`str`, _optional_ , defaults to None) -- The device to load the adapter on. If `None`, the device will be inferred.
  * [](#peft.PeftModel.from_pretrained.key_mapping) **key_mapping** (dict, _optional_ , defaults to None) -- Extra mapping of PEFT `state_dict` keys applied before loading the `state_dict`. When this mapping is applied, the PEFT-specific `"base_model.model"` prefix is removed beforehand and the adapter name (e.g. `"default"`) is not inserted yet. Only pass this argument if you know what you're doing.
  * [](#peft.PeftModel.from_pretrained.kwargs) **kwargs** -- (`optional`): Additional keyword arguments passed along to the specific PEFT configuration class.

Instantiate a PEFT model from a pretrained model and loaded PEFT weights.

Note that the passed `model` may be modified inplace.

#### get_base_model

[](#peft.PeftModel.get_base_model) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1014)

( )

Returns the base model.

#### get_layer_status

[](#peft.PeftModel.get_layer_status) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1130)

( ) → list`peft.peft_model.TunerLayerStatus`

Parameters

  * [](#peft.PeftModel.get_layer_status.model) **model** ([~PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)) -- The model to get the adapter layer status from.

Returns

list`peft.peft_model.TunerLayerStatus`

A list of dataclasses, each containing the status of the corresponding adapter layer.

Get the status of each adapter layer in the model.

This method returns a list of `TunerLayerStatus` dataclass instances, each of which contains the following attributes:

  * `name` (`str`): The name of the adapter layer, e.g. `model.encoder.block.0.layer.0.SelfAttention.q`.
  * `module_type` (`str`): The type of the adapter layer, e.g. `lora.Linear`.
  * `enabled` (`bool`): Whether the adapter layer is enabled.
  * `active_adapters` (`list[str]`): The names of the active adapters, if any, e.g. `["default"]`.
  * `merged_adapters` (`list[str]`): The names of the merged adapters, if any, e.g. `["default"]`.
  * `available_adapters` (`list[str]`): The names of the available adapters, e.g. `["default"]`.

#### get_model_status

[](#peft.PeftModel.get_model_status) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1160)

( ) → `peft.peft_model.TunerModelStatus`

Parameters

  * [](#peft.PeftModel.get_model_status.model) **model** ([~PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)) -- The model to get the adapter layer status from.

Returns

`peft.peft_model.TunerModelStatus`

A dataclass containing the status of the model.

Get the status of tuners of the model.

This method returns a `TunerModelStatus` dataclass instance, which contains the following attributes:

  * `base_model_type` (`str`): The type of the base model, e.g. `T5Model`.
  * `adapter_model_type` (`str`): The type of the adapter model, e.g. `LoraModel`.
  * `peft_types` (`dict[str, str]`): The mapping of adapter name to adapter type, e.g. `{"default": "LORA"}`.
  * `trainable_params` (`int`): The number of trainable parameters in the model.
  * `total_params` (`int`): The total number of parameters in the model.
  * `num_adapter_layers` (`int`): The number of adapter layers in the model.
  * `enabled` (`bool`, `Literal["irregular"]`): Whether all adapter layers are enabled. If some are enabled and some are not, this will be `"irregular"`. This means that your model is in an inconsistent state and might not work as expected.
  * `active_adapters` (`list[str]`, `Literal["irregular"]`): The names of the active adapters. If the active adapters are not consistent across all layers, this will be `"irregular"`, which means that your model is in an inconsistent state and might not work as expected.
  * `merged_adapters` (`list[str]`, `Literal["irregular"]`): The names of the merged adapters. If the merged adapters are not consistent across all layers, this will be `"irregular"`, which means that your model is in an inconsistent state and might not work as expected.
  * `available_adapters` (`list[str]`): The names of the available adapters, e.g. `["default"]`.

#### get_nb_trainable_parameters

[](#peft.PeftModel.get_nb_trainable_parameters) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L870)

( )

Returns the number of trainable parameters and the number of all parameters in the model.

#### get_prompt

[](#peft.PeftModel.get_prompt) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L745)

( batch_size: int task_ids: Optional[torch.Tensor] = None max_cache_len: Optional[int] = None )

Returns the virtual prompts to use for Peft. Only applicable when using a prompt learning method.

#### get_prompt_embedding_to_save

[](#peft.PeftModel.get_prompt_embedding_to_save) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L724)

( adapter_name: str )

Returns the prompt embedding to save when saving the model. Only applicable when using a prompt learning method.

#### load_adapter

[](#peft.PeftModel.load_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1324)

( model_id: Union[str, os.PathLike] adapter_name: str is_trainable: bool = False torch_device: Optional[str] = None autocast_adapter_dtype: bool = True ephemeral_gpu_offload: bool = False low_cpu_mem_usage: bool = False key_mapping: Optional[dict[str, str]] = None **kwargs: Any )

Parameters

  * [](#peft.PeftModel.load_adapter.model_id) **model_id** (`str` or `os.PathLike`) -- The name of the PEFT configuration to use. Can be either:
    * A string, the `model id` of a PEFT configuration hosted inside a model repo on the Hugging Face Hub.
    * A path to a directory containing a PEFT configuration file saved using the `save_pretrained` method (`./my_peft_config_directory/`).
  * [](#peft.PeftModel.load_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftModel.load_adapter.is_trainable) **is_trainable** (`bool`, _optional_ , defaults to `False`) -- Whether the adapter should be trainable or not. If `False`, the adapter will be frozen and can only be used for inference.
  * [](#peft.PeftModel.load_adapter.torch_device) **torch_device** (`str`, _optional_ , defaults to None) -- The device to load the adapter on. If `None`, the device will be inferred.
  * [](#peft.PeftModel.load_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.
  * [](#peft.PeftModel.load_adapter.ephemeral_gpu_offload) **ephemeral_gpu_offload** (`bool`, _optional_ , defaults to `False`) -- Whether to use ephemeral GPU offloading for partially loaded modules. Defaults to `False`.
  * [](#peft.PeftModel.load_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device before loading the saved weights. Useful to speed up the process.
  * [](#peft.PeftModel.load_adapter.key_mapping) **key_mapping** (dict, _optional_ , defaults to None) -- Extra mapping of PEFT `state_dict` keys applied before loading the `state_dict`. When this mapping is applied, the PEFT-specific `"base_model.model"` prefix is removed beforehand and the adapter name (e.g. `"default"`) is not inserted yet. Only pass this argument if you know what you're doing.
  * [](#peft.PeftModel.load_adapter.kwargs) **kwargs** -- (`optional`): Additional arguments to modify the way the adapter is loaded, e.g. the token for Hugging Face Hub.

Load a trained adapter into the model.

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

#### prepare_model_for_gradient_checkpointing

[](#peft.PeftModel.prepare_model_for_gradient_checkpointing) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L702)

( model: PreTrainedModel )

Prepares the model for gradient checkpointing if necessary

#### print_trainable_parameters

[](#peft.PeftModel.print_trainable_parameters) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L900)

( )

Prints the number of trainable parameters in the model.

Note: print_trainable_parameters() uses get_nb_trainable_parameters() which is different from num_parameters(only_trainable=True) from huggingface/transformers. get_nb_trainable_parameters() returns (trainable parameters, all parameters) of the Peft Model which includes modified backbone transformer model. For techniques like LoRA, the backbone transformer model is modified in place with LoRA modules. However, for prompt tuning, the backbone transformer model is unmodified. num_parameters(only_trainable=True) returns number of trainable parameters of the backbone transformer model which can be different.

#### save_pretrained

[](#peft.PeftModel.save_pretrained) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L190)

( save_directory: str safe_serialization: bool = True selected_adapters: Optional[list[str]] = None save_embedding_layers: Union[str, bool] = 'auto' is_main_process: bool = True path_initial_model_for_weight_conversion: Optional[str] = None **kwargs: Any )

Parameters

  * [](#peft.PeftModel.save_pretrained.save_directory) **save_directory** (`str`) -- Directory where the adapter model and configuration files will be saved (will be created if it does not exist).
  * [](#peft.PeftModel.save_pretrained.safe_serialization) **safe_serialization** (`bool`, _optional_) -- Whether to save the adapter files in safetensors format, defaults to `True`.
  * [](#peft.PeftModel.save_pretrained.selected_adapters) **selected_adapters** (`List[str]`, _optional_) -- A list of adapters to be saved. If `None`, will default to all adapters.
  * [](#peft.PeftModel.save_pretrained.save_embedding_layers) **save_embedding_layers** (`Union[bool, str]`, _optional_ , defaults to `"auto"`) -- If `True`, save the embedding layers in addition to adapter weights. If `auto`, checks the common embedding layers `peft.utils.other.EMBEDDING_LAYER_NAMES` in config's `target_modules` when available. and automatically sets the boolean flag. This only works for 🤗 transformers models.
  * [](#peft.PeftModel.save_pretrained.is_main_process) **is_main_process** (`bool`, _optional_) -- Whether the process calling this is the main process or not. Will default to `True`. Will not save the checkpoint if not on the main process, which is important for multi device setups (e.g. DDP).
  * [](#peft.PeftModel.save_pretrained.path_initial_model_for_weight_conversion) **path_initial_model_for_weight_conversion** (`str, *optional*`) -- The path to the initialized adapter, which is obtained after initializing the model with PiSSA/CorDA/OLoRA and before performing any training. When `path_initial_model_for_weight_conversion` is not None, the difference in adapter before and after fine-tuning is calculated. This difference can be represented as the parameters of a standard LoRA adapter. Using this converted adapter does not require changes to the base model, thus conveniently allowing the use of multiple PiSSA/CorDA/OLoRA adapters with LoRA adapters, and the activation or deactivation of any adapters. Note that this conversion is not supported if `rslora` is used in combination with `rank_pattern` or `alpha_pattern`.
  * [](#peft.PeftModel.save_pretrained.kwargs) **kwargs** (additional keyword arguments, _optional_) -- Additional keyword arguments passed along to the `push_to_hub` method.

This function saves the adapter model and the adapter configuration files to a directory, so that it can be reloaded using the [PeftModel.from_pretrained()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.from_pretrained) class method, and also used by the `PeftModel.push_to_hub()` method.

#### set_adapter

[](#peft.PeftModel.set_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1497)

( adapter_name: str inference_mode: bool = False )

Parameters

  * [](#peft.PeftModel.set_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be set as active. The adapter must be loaded first.
  * [](#peft.PeftModel.set_adapter.inference_mode) **inference_mode** (`bool`, optional) -- Whether the activated adapter should be frozen (i.e. `requires_grad=False`). Default is False.

Sets the active adapter.

Only one adapter can be active at a time.

Additionally, this function will set the specified adapter to trainable (i.e., requires_grad=True) unless inference_mode is True.

#### set_requires_grad

[](#peft.PeftModel.set_requires_grad) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1522)

( adapter_names: str | Sequence[str] requires_grad: bool = True )

Parameters

  * [](#peft.PeftModel.set_requires_grad.adapter_name) **adapter_name** (`str` or `Sequence[str]`) -- The name of the adapter(s) whose gradients should be enabled/disabled.
  * [](#peft.PeftModel.set_requires_grad.requires_grad) **requires_grad** (`bool`, _optional_) -- Whether to enable (`True`, default) or disable (`False`).

Enable or disable gradients on the given adapter(s).

Note: Not supported for prompt learning methods like prompt tuning.

#### supports_lora_conversion

[](#peft.PeftModel.supports_lora_conversion) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1637)

( adapter_name: str = 'default' )

Whether it is possible for the adapter of this model to be converted to LoRA.

Normally, this works if the PEFT method is additive, i.e. W’ = W_base + delta_weight.

## [](#peft.PeftModelForSequenceClassification) PeftModelForSequenceClassification

A `PeftModel` for sequence classification tasks.

### class peft.PeftModelForSequenceClassification

[](#peft.PeftModelForSequenceClassification) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1653)

( model: torch.nn.Module peft_config: PeftConfig adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForSequenceClassification.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForSequenceClassification.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForSequenceClassification.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForSequenceClassification.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for sequence classification tasks.

**Attributes** :

  * **config** (`PretrainedConfig`) — The configuration object of the base model.
  * **cls_layer_name** (`str`) — The name of the classification layer.

[](#peft.PeftModelForSequenceClassification.example)

Example:

Copied


    >>> from transformers import AutoModelForSequenceClassification
    >>> from peft import PeftModelForSequenceClassification, get_peft_config

    >>> config = {
    ...     "peft_type": "PREFIX_TUNING",
    ...     "task_type": "SEQ_CLS",
    ...     "inference_mode": False,
    ...     "num_virtual_tokens": 20,
    ...     "token_dim": 768,
    ...     "num_transformer_submodules": 1,
    ...     "num_attention_heads": 12,
    ...     "num_layers": 12,
    ...     "encoder_hidden_size": 768,
    ...     "prefix_projection": False,
    ...     "postprocess_past_key_value_function": None,
    ... }

    >>> peft_config = get_peft_config(config)
    >>> model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased")
    >>> peft_model = PeftModelForSequenceClassification(model, peft_config)
    >>> peft_model.print_trainable_parameters()
    trainable params: 370178 || all params: 108680450 || trainable%: 0.3406113979101117

## [](#peft.PeftModelForTokenClassification) PeftModelForTokenClassification

A `PeftModel` for token classification tasks.

### class peft.PeftModelForTokenClassification

[](#peft.PeftModelForTokenClassification) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L2551)

( model: torch.nn.Module peft_config: PeftConfig = None adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForTokenClassification.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForTokenClassification.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForTokenClassification.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForTokenClassification.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for token classification tasks.

**Attributes** :

  * **config** (`PretrainedConfig`) — The configuration object of the base model.
  * **cls_layer_name** (`str`) — The name of the classification layer.

[](#peft.PeftModelForTokenClassification.example)

Example:

Copied


    >>> from transformers import AutoModelForSequenceClassification
    >>> from peft import PeftModelForTokenClassification, get_peft_config

    >>> config = {
    ...     "peft_type": "PREFIX_TUNING",
    ...     "task_type": "TOKEN_CLS",
    ...     "inference_mode": False,
    ...     "num_virtual_tokens": 20,
    ...     "token_dim": 768,
    ...     "num_transformer_submodules": 1,
    ...     "num_attention_heads": 12,
    ...     "num_layers": 12,
    ...     "encoder_hidden_size": 768,
    ...     "prefix_projection": False,
    ...     "postprocess_past_key_value_function": None,
    ... }

    >>> peft_config = get_peft_config(config)
    >>> model = AutoModelForTokenClassification.from_pretrained("bert-base-cased")
    >>> peft_model = PeftModelForTokenClassification(model, peft_config)
    >>> peft_model.print_trainable_parameters()
    trainable params: 370178 || all params: 108680450 || trainable%: 0.3406113979101117

#### add_adapter

[](#peft.PeftModelForTokenClassification.add_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L2621)

( adapter_name: str peft_config: PeftConfig low_cpu_mem_usage: bool = False autocast_adapter_dtype: bool = True )

Parameters

  * [](#peft.PeftModelForTokenClassification.add_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftModelForTokenClassification.add_adapter.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the adapter to be added.
  * [](#peft.PeftModelForTokenClassification.add_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the process when loading saved adapters. Don't use this option when creating a new PEFT adapter for training.
  * [](#peft.PeftModelForTokenClassification.add_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Add an adapter to the model based on the passed configuration.

This adapter is not trained. To load a trained adapter, check out [PeftModel.load_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.load_adapter).

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

## [](#peft.PeftModelForCausalLM) PeftModelForCausalLM

A `PeftModel` for causal language modeling.

### class peft.PeftModelForCausalLM

[](#peft.PeftModelForCausalLM) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L1911)

( model: torch.nn.Module peft_config: PeftConfig adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForCausalLM.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForCausalLM.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForCausalLM.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForCausalLM.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for causal language modeling.

[](#peft.PeftModelForCausalLM.example)

Example:

Copied


    >>> from transformers import AutoModelForCausalLM
    >>> from peft import PeftModelForCausalLM, get_peft_config

    >>> config = {
    ...     "peft_type": "PREFIX_TUNING",
    ...     "task_type": "CAUSAL_LM",
    ...     "inference_mode": False,
    ...     "num_virtual_tokens": 20,
    ...     "token_dim": 1280,
    ...     "num_transformer_submodules": 1,
    ...     "num_attention_heads": 20,
    ...     "num_layers": 36,
    ...     "encoder_hidden_size": 1280,
    ...     "prefix_projection": False,
    ...     "postprocess_past_key_value_function": None,
    ... }

    >>> peft_config = get_peft_config(config)
    >>> model = AutoModelForCausalLM.from_pretrained("gpt2-large")
    >>> peft_model = PeftModelForCausalLM(model, peft_config)
    >>> peft_model.print_trainable_parameters()
    trainable params: 1843200 || all params: 775873280 || trainable%: 0.23756456724479544

## [](#peft.PeftModelForSeq2SeqLM) PeftModelForSeq2SeqLM

A `PeftModel` for sequence-to-sequence language modeling.

### class peft.PeftModelForSeq2SeqLM

[](#peft.PeftModelForSeq2SeqLM) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L2271)

( model: torch.nn.Module peft_config: PeftConfig adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForSeq2SeqLM.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForSeq2SeqLM.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForSeq2SeqLM.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForSeq2SeqLM.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for sequence-to-sequence language modeling.

[](#peft.PeftModelForSeq2SeqLM.example)

Example:

Copied


    >>> from transformers import AutoModelForSeq2SeqLM
    >>> from peft import PeftModelForSeq2SeqLM, get_peft_config

    >>> config = {
    ...     "peft_type": "LORA",
    ...     "task_type": "SEQ_2_SEQ_LM",
    ...     "inference_mode": False,
    ...     "r": 8,
    ...     "target_modules": ["q", "v"],
    ...     "lora_alpha": 32,
    ...     "lora_dropout": 0.1,
    ...     "fan_in_fan_out": False,
    ...     "enable_lora": None,
    ...     "bias": "none",
    ... }

    >>> peft_config = get_peft_config(config)
    >>> model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
    >>> peft_model = PeftModelForSeq2SeqLM(model, peft_config)
    >>> peft_model.print_trainable_parameters()
    trainable params: 884736 || all params: 223843584 || trainable%: 0.3952474242013566

## [](#peft.PeftModelForQuestionAnswering) PeftModelForQuestionAnswering

A `PeftModel` for question answering.

### class peft.PeftModelForQuestionAnswering

[](#peft.PeftModelForQuestionAnswering) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L2789)

( model: torch.nn.Module peft_config: PeftConfig adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForQuestionAnswering.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForQuestionAnswering.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForQuestionAnswering.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForQuestionAnswering.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for extractive question answering.

**Attributes** :

  * **config** (`PretrainedConfig`) — The configuration object of the base model.
  * **cls_layer_name** (`str`) — The name of the classification layer.

[](#peft.PeftModelForQuestionAnswering.example)

Example:

Copied


    >>> from transformers import AutoModelForQuestionAnswering
    >>> from peft import PeftModelForQuestionAnswering, get_peft_config

    >>> config = {
    ...     "peft_type": "LORA",
    ...     "task_type": "QUESTION_ANS",
    ...     "inference_mode": False,
    ...     "r": 16,
    ...     "target_modules": ["query", "value"],
    ...     "lora_alpha": 32,
    ...     "lora_dropout": 0.05,
    ...     "fan_in_fan_out": False,
    ...     "bias": "none",
    ... }

    >>> peft_config = get_peft_config(config)
    >>> model = AutoModelForQuestionAnswering.from_pretrained("bert-base-cased")
    >>> peft_model = PeftModelForQuestionAnswering(model, peft_config)
    >>> peft_model.print_trainable_parameters()
    trainable params: 592900 || all params: 108312580 || trainable%: 0.5473971721475013

#### add_adapter

[](#peft.PeftModelForQuestionAnswering.add_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L2857)

( adapter_name: str peft_config: PeftConfig low_cpu_mem_usage: bool = False autocast_adapter_dtype: bool = True )

Parameters

  * [](#peft.PeftModelForQuestionAnswering.add_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftModelForQuestionAnswering.add_adapter.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the adapter to be added.
  * [](#peft.PeftModelForQuestionAnswering.add_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the process when loading saved adapters. Don't use this option when creating a new PEFT adapter for training.
  * [](#peft.PeftModelForQuestionAnswering.add_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Add an adapter to the model based on the passed configuration.

This adapter is not trained. To load a trained adapter, check out [PeftModel.load_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.load_adapter).

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

## [](#peft.PeftModelForFeatureExtraction) PeftModelForFeatureExtraction

A `PeftModel` for getting extracting features/embeddings from transformer models.

### class peft.PeftModelForFeatureExtraction

[](#peft.PeftModelForFeatureExtraction) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L3048)

( model: torch.nn.Module peft_config: PeftConfig adapter_name: str = 'default' **kwargs )

Parameters

  * [](#peft.PeftModelForFeatureExtraction.model) **model** ([PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Base transformer model.
  * [](#peft.PeftModelForFeatureExtraction.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Peft config.
  * [](#peft.PeftModelForFeatureExtraction.adapter_name) **adapter_name** (`str`, _optional_) -- The name of the adapter, defaults to `"default"`.
  * [](#peft.PeftModelForFeatureExtraction.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Peft model for extracting features/embeddings from transformer models

**Attributes** :

  * **config** (`PretrainedConfig`) — The configuration object of the base model.

[](#peft.PeftModelForFeatureExtraction.example)

Example:

Copied


    >>> from transformers import AutoModel
    >>> from peft import PeftModelForFeatureExtraction, get_peft_config

    >>> config = {
    ...     "peft_type": "LORA",
    ...     "task_type": "FEATURE_EXTRACTION",
    ...     "inference_mode": False,
    ...     "r": 16,
    ...     "target_modules": ["query", "value"],
    ...     "lora_alpha": 32,
    ...     "lora_dropout": 0.05,
    ...     "fan_in_fan_out": False,
    ...     "bias": "none",
    ... }
    >>> peft_config = get_peft_config(config)
    >>> model = AutoModel.from_pretrained("bert-base-cased")
    >>> peft_model = PeftModelForFeatureExtraction(model, peft_config)
    >>> peft_model.print_trainable_parameters()

## [](#peft.PeftMixedModel) PeftMixedModel

A `PeftModel` for mixing different adapter types (e.g. LoRA and LoHa).

### class peft.PeftMixedModel

[](#peft.PeftMixedModel) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L67)

( model: nn.Module peft_config: PeftConfig adapter_name: str = 'default' )

Parameters

  * [](#peft.PeftMixedModel.model) **model** (`torch.nn.Module`) -- The model to be tuned.
  * [](#peft.PeftMixedModel.config) **config** (`PeftConfig`) -- The config of the model to be tuned. The adapter type must be compatible.
  * [](#peft.PeftMixedModel.adapter_name) **adapter_name** (`str`, `optional`, defaults to `"default"`) -- The name of the first adapter.
  * [](#peft.PeftMixedModel.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the loading process.

PeftMixedModel for loading mixing different types of adapters for inference.

This class does not support loading/saving, and it shouldn’t usually be initialized directly. Instead, use `get_peft_model` with the argument `mixed=True`.

> > Read the [Mixed adapter types](https://huggingface.co/docs/peft/en/developer_guides/mixed_models) guide to learn > more about using different adapter types.

[](#peft.PeftMixedModel.example)

Example:

Copied


    >>> base_model = ...  # load the base model, e.g. from transformers
    >>> peft_model = PeftMixedModel.from_pretrained(base_model, path_to_adapter1, "adapter1").eval()
    >>> peft_model.load_adapter(path_to_adapter2, "adapter2")
    >>> peft_model.set_adapter(["adapter1", "adapter2"])  # activate both adapters
    >>> peft_model(data)  # forward pass using both adapters

#### add_adapter

[](#peft.PeftMixedModel.add_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L203)

( adapter_name: str peft_config: PeftConfig low_cpu_mem_usage: bool = False autocast_adapter_dtype: bool = True )

Parameters

  * [](#peft.PeftMixedModel.add_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftMixedModel.add_adapter.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the adapter to be added.
  * [](#peft.PeftMixedModel.add_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the process when loading saved adapters.

> > Don't use `low_cpu_mem_usage=True` when creating a new PEFT adapter for training (training is untested > and discouraged for PeftMixedModel in general).

  * [](#peft.PeftMixedModel.add_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners. If set to `False`, the dtypes will stay the same as those of the corresponding layer.

Add an adapter to the model based on the passed configuration.

This adapter is not trained. To load a trained adapter, check out [PeftModel.load_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.load_adapter).

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

#### disable_adapter

[](#peft.PeftMixedModel.disable_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L192)

( )

Disables the adapter module.

#### forward

[](#peft.PeftMixedModel.forward) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L180)

( *args: Any **kwargs: Any )

Forward pass of the model.

#### from_pretrained

[](#peft.PeftMixedModel.from_pretrained) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L394)

( model: nn.Module model_id: str | os.PathLike adapter_name: str = 'default' is_trainable: bool = False config: Optional[PeftConfig] = None **kwargs: Any )

Parameters

  * [](#peft.PeftMixedModel.from_pretrained.model) **model** (`nn.Module`) -- The model to be adapted.
  * [](#peft.PeftMixedModel.from_pretrained.model_id) **model_id** (`str` or `os.PathLike`) -- The name of the PEFT configuration to use. Can be either:
    * A string, the `model id` of a PEFT configuration hosted inside a model repo on the Hugging Face Hub.
    * A path to a directory containing a PEFT configuration file saved using the `save_pretrained` method (`./my_peft_config_directory/`).
  * [](#peft.PeftMixedModel.from_pretrained.adapter_name) **adapter_name** (`str`, _optional_ , defaults to `"default"`) -- The name of the adapter to be loaded. This is useful for loading multiple adapters.
  * [](#peft.PeftMixedModel.from_pretrained.is_trainable) **is_trainable** (`bool`, _optional_ , defaults to `False`) -- Whether the adapter should be trainable or not. If `False`, the adapter will be frozen and use for inference
  * [](#peft.PeftMixedModel.from_pretrained.config) **config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig), _optional_) -- The configuration object to use instead of an automatically loaded configuration. This configuration object is mutually exclusive with `model_id` and `kwargs`. This is useful when configuration is already loaded before calling `from_pretrained`.
  * [](#peft.PeftMixedModel.from_pretrained.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device before loading the saved weights. Useful to speed up the process.
  * [](#peft.PeftMixedModel.from_pretrained.kwargs) **kwargs** -- (`optional`): Additional keyword arguments passed along to the specific PEFT configuration class.

Instantiate a PEFT mixed model from a pretrained model and loaded PEFT weights.

Note that the passed `model` may be modified inplace.

#### generate

[](#peft.PeftMixedModel.generate) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L186)

( *args: Any **kwargs: Any )

Generate output.

#### get_nb_trainable_parameters

[](#peft.PeftMixedModel.get_nb_trainable_parameters) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L126)

( )

Returns the number of trainable parameters and number of all parameters in the model.

#### load_adapter

[](#peft.PeftMixedModel.load_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L345)

( model_id: str adapter_name: str *args: Any **kwargs: Any )

Parameters

  * [](#peft.PeftMixedModel.load_adapter.adapter_name) **adapter_name** (`str`) -- The name of the adapter to be added.
  * [](#peft.PeftMixedModel.load_adapter.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- The configuration of the adapter to be added.
  * [](#peft.PeftMixedModel.load_adapter.is_trainable) **is_trainable** (`bool`, _optional_ , defaults to `False`) -- Whether the adapter should be trainable or not. If `False`, the adapter will be frozen and can only be used for inference.
  * [](#peft.PeftMixedModel.load_adapter.torch_device) **torch_device** (`str`, _optional_ , defaults to None) -- The device to load the adapter on. If `None`, the device will be inferred.
  * [](#peft.PeftMixedModel.load_adapter.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_ , defaults to `True`) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 and bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners.
  * [](#peft.PeftMixedModel.load_adapter.ephemeral_gpu_offload) **ephemeral_gpu_offload** (`bool`, _optional_ , defaults to `False`) -- Whether to use ephemeral GPU offloading for partially loaded modules. Defaults to `False`.
  * [](#peft.PeftMixedModel.load_adapter.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device before loading the saved weights. Useful to speed up the process.
  * [](#peft.PeftMixedModel.load_adapter.kwargs) **kwargs** -- (`optional`): Additional arguments to modify the way the adapter is loaded, e.g. the token for Hugging Face Hub.

Load a trained adapter into the model.

The name for the new adapter should be unique.

The new adapter is not automatically set as the active adapter. Use [PeftModel.set_adapter()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel.set_adapter) to set the active adapter.

#### merge_and_unload

[](#peft.PeftMixedModel.merge_and_unload) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L308)

( *args: Any **kwargs: Any )

Parameters

  * [](#peft.PeftMixedModel.merge_and_unload.progressbar) **progressbar** (`bool`) -- whether to show a progressbar indicating the unload and merge process
  * [](#peft.PeftMixedModel.merge_and_unload.safe_merge) **safe_merge** (`bool`) -- whether to activate the safe merging check to check if there is any potential Nan in the adapter weights
  * [](#peft.PeftMixedModel.merge_and_unload.adapter_names) **adapter_names** (`List[str]`, _optional_) -- The list of adapter names that should be merged. If None, all active adapters will be merged. Defaults to `None`.

This method merges the adapter layers into the base model. This is needed if someone wants to use the base model as a standalone model.

#### print_trainable_parameters

[](#peft.PeftMixedModel.print_trainable_parameters) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L151)

( )

Prints the number of trainable parameters in the model.

Note: print_trainable_parameters() uses get_nb_trainable_parameters() which is different from num_parameters(only_trainable=True) from huggingface/transformers. get_nb_trainable_parameters() returns (trainable parameters, all parameters) of the Peft Model which includes modified backbone transformer model. For techniques like LoRA, the backbone transformer model is modified in place with LoRA modules. However, for prompt tuning, the backbone transformer model is unmodified. num_parameters(only_trainable=True) returns number of trainable parameters of the backbone transformer model which can be different.

#### set_adapter

[](#peft.PeftMixedModel.set_adapter) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L266)

( adapter_name: Union[str, list[str]] inference_mode: bool = False )

Parameters

  * [](#peft.PeftMixedModel.set_adapter.adapter_name) **adapter_name** (str, list[str]) -- The name(s) of the adapter(s) to set as active
  * [](#peft.PeftMixedModel.set_adapter.inference_mode) **inference_mode** (bool, optional) -- Whether the activated adapter should be frozen (i.e. `requires_grad=False`). Default is False.

Sets the active adapter(s) for the model.

Note that the order in which the adapters are applied during the forward pass may not be the same as the order in which they are passed to this function. Instead, the order during the forward pass is determined by the order in which the adapters were loaded into the model. The active adapters only determine which adapters are active during the forward pass, but not the order in which they are applied.

Additionally, this function will set the specified adapter to trainable (i.e., requires_grad=True) unless inference_mode is True.

#### unload

[](#peft.PeftMixedModel.unload) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mixed_model.py#L325)

( *args: Any **kwargs: Any )

Gets back the base model by removing all the adapter modules without merging. This gives back the original base model.

## [](#peft.cast_mixed_precision_params) Utilities

#### peft.cast_mixed_precision_params

[](#peft.cast_mixed_precision_params) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/utils/other.py#L1364)

( model dtype )

Parameters

  * [](#peft.cast_mixed_precision_params.model) **model** (`torch.nn.Module`) -- The model to cast the non-trainable parameters of.
  * [](#peft.cast_mixed_precision_params.dtype) **dtype** (`torch.dtype`) -- The dtype to cast the non-trainable parameters to. The `dtype` can be `torch.float16` or

Cast all non-trainable parameters of the model to the given `dtype`. The `dtype` can be `torch.float16` or `torch.bfloat16` as per the mixed-precision training you are performing. The trainable parameters are cast to full precision. This is meant to reduce the GPU memory usage when using PEFT methods by using half-precision dtype for non-trainable parameters. Having the trainable parameters in full-precision preserves training stability when using automatic mixed-precision training.

`torch.bfloat16` as per the mixed-precision training you are performing.

#### peft.get_peft_model

[](#peft.get_peft_model) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mapping_func.py#L30)

( model: PreTrainedModel peft_config: PeftConfig adapter_name: str = 'default' mixed: bool = False autocast_adapter_dtype: bool = True revision: Optional[str] = None low_cpu_mem_usage: bool = False )

Parameters

  * [](#peft.get_peft_model.model) **model** ([transformers.PreTrainedModel](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel)) -- Model to be wrapped.
  * [](#peft.get_peft_model.peft_config) **peft_config** ([PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig)) -- Configuration object containing the parameters of the Peft model.
  * [](#peft.get_peft_model.adapter_name) **adapter_name** (`str`, `optional`, defaults to `"default"`) -- The name of the adapter to be injected, if not provided, the default adapter name is used ("default").
  * [](#peft.get_peft_model.mixed) **mixed** (`bool`, `optional`, defaults to `False`) -- Whether to allow mixing different (compatible) adapter types.
  * [](#peft.get_peft_model.autocast_adapter_dtype) **autocast_adapter_dtype** (`bool`, _optional_) -- Whether to autocast the adapter dtype. Defaults to `True`. Right now, this will only cast adapter weights using float16 or bfloat16 to float32, as this is typically required for stable training, and only affect select PEFT tuners.
  * [](#peft.get_peft_model.revision) **revision** (`str`, `optional`, defaults to `main`) -- The revision of the base model. If this isn't set, the saved peft model will load the `main` revision for the base model
  * [](#peft.get_peft_model.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the loading process. Leave this setting as False if you intend on training the model, unless the adapter weights will be replaced by different weights before training starts.

Returns a Peft model object from a model and a config, where the model will be modified in-place.

#### peft.inject_adapter_in_model

[](#peft.inject_adapter_in_model) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/mapping.py#L47)

( peft_config: PeftConfig model: torch.nn.Module adapter_name: str = 'default' low_cpu_mem_usage: bool = False state_dict: Optional[dict[str, torch.Tensor]] = None )

Parameters

  * [](#peft.inject_adapter_in_model.peft_config) **peft_config** (`PeftConfig`) -- Configuration object containing the parameters of the PEFT model.
  * [](#peft.inject_adapter_in_model.model) **model** (`torch.nn.Module`) -- The input model where the adapter will be injected.
  * [](#peft.inject_adapter_in_model.adapter_name) **adapter_name** (`str`, `optional`, defaults to `"default"`) -- The name of the adapter to be injected, if not provided, the default adapter name is used ("default").
  * [](#peft.inject_adapter_in_model.low_cpu_mem_usage) **low_cpu_mem_usage** (`bool`, `optional`, defaults to `False`) -- Create empty adapter weights on meta device. Useful to speed up the loading process.
  * [](#peft.inject_adapter_in_model.state_dict) **state_dict** (`dict`, _optional_ , defaults to `None`) -- If a `state_dict` is passed here, the adapters will be injected based on the entries of the state_dict. This can be useful when the exact `target_modules` of the PEFT method is unknown, for instance because the checkpoint was created without meta data. Note that the values from the `state_dict` are not used, only the keys are used to determine the correct layers that should be adapted.

Create PEFT layers and inject them into the model in-place.

Currently the API does not support prompt learning methods and adaption prompt.

This function is similar to [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) but it does not return a [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) instance. Instead, it returns the original, mutated instance of the passed model.

#### peft.get_peft_model_state_dict

[](#peft.get_peft_model_state_dict) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/utils/save_and_load.py#L77)

( model state_dict = None adapter_name = 'default' unwrap_compiled = False save_embedding_layers = 'auto' )

Parameters

  * [](#peft.get_peft_model_state_dict.model) **model** ([PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel)) -- The Peft model. When using torch.nn.DistributedDataParallel, DeepSpeed or FSDP, the model should be the underlying model/unwrapped model (i.e. model.module).
  * [](#peft.get_peft_model_state_dict.state_dict) **state_dict** (`dict`, _optional_ , defaults to `None`) -- The state dict of the model. If not provided, the state dict of the passed model will be used.
  * [](#peft.get_peft_model_state_dict.adapter_name) **adapter_name** (`str`, _optional_ , defaults to `"default"`) -- The name of the adapter whose state dict should be returned.
  * [](#peft.get_peft_model_state_dict.unwrap_compiled) **unwrap_compiled** (`bool`, _optional_ , defaults to `False`) -- Whether to unwrap the model if torch.compile was used.
  * [](#peft.get_peft_model_state_dict.save_embedding_layers) **save_embedding_layers** (`Union[bool, str]`, , _optional_ , defaults to `auto`) -- If `True`, save the embedding layers in addition to adapter weights. If `auto`, checks the common embedding layers `peft.utils.other.EMBEDDING_LAYER_NAMES` in config's `target_modules` when available. Based on it sets the boolean flag. This only works for 🤗 transformers models.

Get the state dict of the given adapter of the PEFT model.

This only includes the PEFT parameters, not the parameters of the base model. Thus the returned `state_dict` is generally small compared to the full model size. To retrieve the full `state_dict`, just call `model.state_dict()`.

Note that the adapter name is removed from the `state_dict`, as this is just an arbitrary name that can be changed when loading the adapter. So e.g. if the adapter name is `'default'` and the original key is `'model.q_proj.lora_A.default.weight'`, the returned key will be `'model.q_proj.lora_A.weight'`. Use this function in conjunction with [set_peft_model_state_dict()](/docs/peft/v0.19.0/en/package_reference/functional#peft.set_peft_model_state_dict) to take care of the adapter name when loading weights.

#### peft.prepare_model_for_kbit_training

[](#peft.prepare_model_for_kbit_training) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/utils/other.py#L141)

( model use_gradient_checkpointing = True gradient_checkpointing_kwargs = None )

Parameters

  * [](#peft.prepare_model_for_kbit_training.model) **model** (`transformers.PreTrainedModel`) -- The loaded model from `transformers`
  * [](#peft.prepare_model_for_kbit_training.use_gradient_checkpointing) **use_gradient_checkpointing** (`bool`, _optional_ , defaults to `True`) -- If True, use gradient checkpointing to save memory at the expense of slower backward pass.
  * [](#peft.prepare_model_for_kbit_training.gradient_checkpointing_kwargs) **gradient_checkpointing_kwargs** (`dict`, _optional_ , defaults to `None`) -- Keyword arguments to pass to the gradient checkpointing function, please refer to the documentation of `torch.utils.checkpoint.checkpoint` for more details about the arguments that you can pass to that method. Note this is only available in the latest transformers versions (> 4.34.1).

Note this method only works for `transformers` models.

This method wraps the entire protocol for preparing a model before running a training. This includes: 1- Cast the layernorm in fp32 2- making output embedding layer require grads 3- Add the upcasting of the lm head to fp32 4- Freezing the base model layers to ensure they are not updated during training

#### peft.get_layer_status

[](#peft.get_layer_status) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L3169)

( model: torch.nn.Module ) → list`peft.peft_model.TunerLayerStatus`

Parameters

  * [](#peft.get_layer_status.model) **model** ([Union[`~PeftModel`, `~transformers.PreTrainedModel`, `nn.Module`]]) -- The model to get the adapter layer status from.

Returns

list`peft.peft_model.TunerLayerStatus`

A list of dataclasses, each containing the status of the corresponding adapter layer.

Get the status of each adapter layer in the model.

This function returns a list of `TunerLayerStatus` dataclass instances, each of which contains the following attributes:

  * `name` (`str`): The name of the adapter layer, e.g. `model.encoder.block.0.layer.0.SelfAttention.q`.
  * `module_type` (`str`): The type of the adapter layer, e.g. `lora.Linear`.
  * `enabled` (`bool`): Whether the adapter layer is enabled.
  * `active_adapters` (`list[str]`): The names of the active adapters, if any, e.g. `["default"]`.
  * `merged_adapters` (`list[str]`): The names of the merged adapters, if any, e.g. `["default"]`.
  * requires_grad : dict[str, bool | Literal[“irregular”]] The requires_grad status of the parameters for each adapter module. Ideally, it should be either `True` or `False`. If the requires_grad status is not consistent across all parameters, the value will be set to `"irregular"`.
  * `available_adapters` (`list[str]`): The names of the available adapters, e.g. `["default"]`.
  * `devices` (`dict[str, list[str]]`): The devices where the parameters of the given adapter are stored, e.g. `["cuda"]`.

#### peft.get_model_status

[](#peft.get_model_status) [< source >](https://github.com/huggingface/peft/blob/v0.19.0/src/peft/peft_model.py#L3296)

( model: torch.nn.Module ) → `peft.peft_model.TunerModelStatus`

Parameters

  * [](#peft.get_model_status.model) **model** ([Union[`~PeftModel`, `~transformers.PreTrainedModel`, `nn.Module`]]) -- The model to get the adapter layer status from.

Returns

`peft.peft_model.TunerModelStatus`

A dataclass containing the status of the model.

Get the status of tuners of the model.

This function returns a `TunerModelStatus` dataclass instance, which contains the following attributes:

  * `base_model_type` (`str`): The type of the base model, e.g. `T5Model`.
  * `adapter_model_type` (`str`): The type of the adapter model, e.g. `LoraModel`.
  * `peft_types` (`dict[str, str]`): The mapping of adapter name to adapter type, e.g. `{"default": "LORA"}`.
  * `trainable_params` (`int`): The number of trainable parameters in the model.
  * `total_params` (`int`): The total number of parameters in the model.
  * `num_adapter_layers` (`int`): The number of adapter layers in the model.
  * `enabled` (`bool`, `Literal["irregular"]`): Whether all adapter layers are enabled. If some are enabled and some are not, this will be `"irregular"`. This means that your model is in an inconsistent state and might not work as expected.
  * `active_adapters` (`list[str]`, `Literal["irregular"]`): The names of the active adapters. If the active adapters are not consistent across all layers, this will be `"irregular"`, which means that your model is in an inconsistent state and might not work as expected.
  * `merged_adapters` (`list[str]`, `Literal["irregular"]`): The names of the merged adapters. If the merged adapters are not consistent across all layers, this will be `"irregular"`, which means that your model is in an inconsistent state and might not work as expected.
  * `requires_grad` (`dict[str, bool | Literal["irregular"]]`): Whether for the given adapter, all adapter layers have `requires_grad` set to `True` or `False`. If there is a mix, this will be set to `"irregular"`, which means that your model is in an inconsistent state and might not work as expected.
  * `available_adapters` (`list[str]`): The names of the available adapters, e.g. `["default"]`.
  * `devices` (`dict[str, list[str]]`): The devices where the parameters of the given adapter are stored, e.g. `["cuda"]`.

[ Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/package_reference/peft_model.md)

[←AutoPeftModel](/docs/peft/package_reference/auto_class) [PEFT types→](/docs/peft/package_reference/peft_types)

[Models](#models)[PeftModel](#peft.PeftModel)[PeftModelForSequenceClassification](#peft.PeftModelForSequenceClassification)[PeftModelForTokenClassification](#peft.PeftModelForTokenClassification)[PeftModelForCausalLM](#peft.PeftModelForCausalLM)[PeftModelForSeq2SeqLM](#peft.PeftModelForSeq2SeqLM)[PeftModelForQuestionAnswering](#peft.PeftModelForQuestionAnswering)[PeftModelForFeatureExtraction](#peft.PeftModelForFeatureExtraction)[PeftMixedModel](#peft.PeftMixedModel)[Utilities](#peft.cast_mixed_precision_params)
