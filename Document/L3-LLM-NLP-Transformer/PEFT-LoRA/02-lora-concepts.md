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

[🤗 PEFT](/docs/peft/main/en/index)[Quicktour](/docs/peft/main/en/quicktour)[Installation](/docs/peft/main/en/install)

Tutorial

[Configurations and models](/docs/peft/main/en/tutorial/peft_model_config)[Integrations](/docs/peft/main/en/tutorial/peft_integrations)

PEFT method guides

[Prompt-based methods](/docs/peft/main/en/task_guides/prompt_based_methods)[LoRA methods](/docs/peft/main/en/task_guides/lora_based_methods)[IA3](/docs/peft/main/en/task_guides/ia3)

Developer guides

[Model merging](/docs/peft/main/en/developer_guides/model_merging)[Quantization](/docs/peft/main/en/developer_guides/quantization)[LoRA](/docs/peft/main/en/developer_guides/lora)[Custom models](/docs/peft/main/en/developer_guides/custom_models)[Adapter injection](/docs/peft/main/en/developer_guides/low_level_api)[Mixed adapter types](/docs/peft/main/en/developer_guides/mixed_models)[torch.compile](/docs/peft/main/en/developer_guides/torch_compile)[Contribute to PEFT](/docs/peft/main/en/developer_guides/contributing)[Troubleshooting](/docs/peft/main/en/developer_guides/troubleshooting)[PEFT checkpoint format](/docs/peft/main/en/developer_guides/checkpoint)

🤗 Accelerate integrations

[DeepSpeed](/docs/peft/main/en/accelerate/deepspeed)[Fully Sharded Data Parallel](/docs/peft/main/en/accelerate/fsdp)

Conceptual guides

[Adapters](/docs/peft/main/en/conceptual_guides/adapter)[Soft prompts](/docs/peft/main/en/conceptual_guides/prompting)[IA3](/docs/peft/main/en/conceptual_guides/ia3)[OFT/BOFT](/docs/peft/main/en/conceptual_guides/oft)

API reference

Main classes

[AutoPeftModel](/docs/peft/main/en/package_reference/auto_class)[PEFT model](/docs/peft/main/en/package_reference/peft_model)[PEFT types](/docs/peft/main/en/package_reference/peft_types)[Configuration](/docs/peft/main/en/package_reference/config)[Tuner](/docs/peft/main/en/package_reference/tuners)

Adapters

[AdaLoRA](/docs/peft/main/en/package_reference/adalora)[AdaMSS](/docs/peft/main/en/package_reference/adamss)[IA3](/docs/peft/main/en/package_reference/ia3)[Llama-Adapter](/docs/peft/main/en/package_reference/llama_adapter)[LoHa](/docs/peft/main/en/package_reference/loha)[LoKr](/docs/peft/main/en/package_reference/lokr)[LoRA](/docs/peft/main/en/package_reference/lora)[OSF](/docs/peft/main/en/package_reference/osf)[X-LoRA](/docs/peft/main/en/package_reference/xlora)[LyCORIS](/docs/peft/main/en/package_reference/adapter_utils)[Multitask Prompt Tuning](/docs/peft/main/en/package_reference/multitask_prompt_tuning)[OFT](/docs/peft/main/en/package_reference/oft)[BOFT](/docs/peft/main/en/package_reference/boft)[PSOFT](/docs/peft/main/en/package_reference/psoft)[Polytropon](/docs/peft/main/en/package_reference/poly)[P-tuning](/docs/peft/main/en/package_reference/p_tuning)[Prefix tuning](/docs/peft/main/en/package_reference/prefix_tuning)[Cartridges](/docs/peft/main/en/package_reference/cartridges)[Prompt tuning](/docs/peft/main/en/package_reference/prompt_tuning)[Layernorm tuning](/docs/peft/main/en/package_reference/layernorm_tuning)[VeRA](/docs/peft/main/en/package_reference/vera)[PVeRA](/docs/peft/main/en/package_reference/pvera)[FourierFT](/docs/peft/main/en/package_reference/fourierft)[GraLoRA](/docs/peft/main/en/package_reference/gralora)[VB-LoRA](/docs/peft/main/en/package_reference/vblora)[HRA](/docs/peft/main/en/package_reference/hra)[CPT](/docs/peft/main/en/package_reference/cpt)[Trainable Tokens](/docs/peft/main/en/package_reference/trainable_tokens)[RandLora](/docs/peft/main/en/package_reference/randlora)[SHiRA](/docs/peft/main/en/package_reference/shira)[C3A](/docs/peft/main/en/package_reference/c3a)[MiSS](/docs/peft/main/en/package_reference/miss)[RoAd](/docs/peft/main/en/package_reference/road)[WaveFT](/docs/peft/main/en/package_reference/waveft)[DeLoRA](/docs/peft/main/en/package_reference/delora)[TinyLoRA](/docs/peft/main/en/package_reference/tinylora)[Lily](/docs/peft/main/en/package_reference/lily)[PEANuT](/docs/peft/main/en/package_reference/peanut)[BEFT](/docs/peft/main/en/package_reference/beft)

Utilities

[Model merge](/docs/peft/main/en/package_reference/merge_utils)[Helpers](/docs/peft/main/en/package_reference/helpers)[Hotswapping adapters](/docs/peft/main/en/package_reference/hotswap)[Functions for PEFT integration](/docs/peft/main/en/package_reference/functional)[Converting non-LoRA adapters to LoRA](/docs/peft/main/en/package_reference/lora_conversion)

You are viewing main version, which requires [installation from source](/docs/peft/install#source). If you'd like regular pip install, checkout the latest stable version ([v0.19.0](/docs/peft/v0.19.0/conceptual_guides/lora)).

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

#  LoRA

This conceptual guide gives a brief overview of [LoRA](https://arxiv.org/abs/2106.09685), a technique that accelerates the fine-tuning of large models while consuming less memory.

To make fine-tuning more efficient, LoRA’s approach is to represent the weight updates with two smaller matrices (called **update matrices**) through low-rank decomposition. These new matrices can be trained to adapt to the new data while keeping the overall number of changes low. The original weight matrix remains frozen and doesn’t receive any further adjustments. To produce the final results, both the original and the adapted weights are combined.

This approach has a number of advantages:

  * LoRA makes fine-tuning more efficient by drastically reducing the number of trainable parameters.
  * The original pre-trained weights are kept frozen, which means you can have multiple lightweight and portable LoRA models for various downstream tasks built on top of them.
  * LoRA is orthogonal to many other parameter-efficient methods and can be combined with many of them.
  * Performance of models fine-tuned using LoRA is comparable to the performance of fully fine-tuned models.
  * LoRA does not add any inference latency because adapter weights can be merged with the base model.

In principle, LoRA can be applied to any subset of weight matrices in a neural network to reduce the number of trainable parameters. However, for simplicity and further parameter efficiency, in Transformer models LoRA is typically applied to attention blocks only. The resulting number of trainable parameters in a LoRA model depends on the size of the low-rank update matrices, which is determined mainly by the rank `r` and the shape of the original weight matrix.

##  Merge LoRA weights into the base model

While LoRA is significantly smaller and faster to train, you may encounter latency issues during inference due to separately loading the base model and the LoRA model. To eliminate latency, use the [merge_and_unload()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.merge_and_unload) function to merge the adapter weights with the base model which allows you to effectively use the newly merged model as a standalone model.

This works because during training, the smaller weight matrices (_A_ and _B_ in the diagram above) are separate. But once training is complete, the weights can actually be merged into a new weight matrix that is identical.

##  Utils for LoRA

Use [merge_adapter()](/docs/peft/main/en/package_reference/tuners#peft.tuners.tuners_utils.BaseTuner.merge_adapter) to merge the LoRa layers into the base model while retaining the PeftModel. This will help in later unmerging, deleting, loading different adapters and so on.

Use [unmerge_adapter()](/docs/peft/main/en/package_reference/tuners#peft.tuners.tuners_utils.BaseTuner.unmerge_adapter) to unmerge the LoRa layers from the base model while retaining the PeftModel. This will help in later merging, deleting, loading different adapters and so on.

Use [unload()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.unload) to get back the base model without the merging of the active lora modules. This will help when you want to get back the pretrained base model in some applications when you want to reset the model to its original state. For example, in Stable Diffusion WebUi, when the user wants to infer with base model post trying out LoRAs.

Use [delete_adapter()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.delete_adapter) to delete an existing adapter.

Use [add_weighted_adapter()](/docs/peft/main/en/package_reference/lora#peft.LoraModel.add_weighted_adapter) to combine multiple LoRAs into a new adapter based on the user provided weighing scheme.

##  Common LoRA parameters in PEFT

As with other methods supported by PEFT, to fine-tune a model using LoRA, you need to:

  1. Instantiate a base model.
  2. Create a configuration (`LoraConfig`) where you define LoRA-specific parameters.
  3. Wrap the base model with `get_peft_model()` to get a trainable `PeftModel`.
  4. Train the `PeftModel` as you normally would train the base model.

`LoraConfig` allows you to control how LoRA is applied to the base model through the following parameters:

  * `r`: the rank of the update matrices, expressed in `int`. Lower rank results in smaller update matrices with fewer trainable parameters.
  * `target_modules`: The modules (for example, attention blocks) to apply the LoRA update matrices.
  * `lora_alpha`: LoRA scaling factor.
  * `bias`: Specifies if the `bias` parameters should be trained. Can be `'none'`, `'all'` or `'lora_only'`.
  * `use_rslora`: When set to True, uses [Rank-Stabilized LoRA](https://doi.org/10.48550/arXiv.2312.03732) which sets the adapter scaling factor to `lora_alpha/math.sqrt(r)`, since it was proven to work better. Otherwise, it will use the original default value of `lora_alpha/r`.
  * `modules_to_save`: List of modules apart from LoRA layers to be set as trainable and saved in the final checkpoint. These typically include model’s custom head that is randomly initialized for the fine-tuning task.
  * `layers_to_transform`: List of layers to be transformed by LoRA. If not specified, all layers in `target_modules` are transformed.
  * `layers_pattern`: Pattern to match layer names in `target_modules`, if `layers_to_transform` is specified. By default `PeftModel` will look at common layer pattern (`layers`, `h`, `blocks`, etc.), use it for exotic and custom models.
  * `rank_pattern`: The mapping from layer names or regexp expression to ranks which are different from the default rank specified by `r`.
  * `alpha_pattern`: The mapping from layer names or regexp expression to alphas which are different from the default alpha specified by `lora_alpha`.

##  LoRA examples

For an example of LoRA method application to various downstream tasks, please refer to the following guides:

  * [Image classification using LoRA](../task_guides/image_classification_lora)
  * [Semantic segmentation](../task_guides/semantic_segmentation_lora)

While the original paper focuses on language models, the technique can be applied to any dense layers in deep learning models. As such, you can leverage this technique with diffusion models. See [Dreambooth fine-tuning with LoRA](../task_guides/task_guides/dreambooth_lora) task guide for an example.

##  Initialization options

The initialization of LoRA weights is controlled by the parameter `init_lora_weights` of the `LoraConfig`. By default, PEFT initializes LoRA weights the same way as the [reference implementation](https://github.com/microsoft/LoRA), i.e. using Kaiming-uniform for weight A and initializing weight B as zeros, resulting in an identity transform.

It is also possible to pass `init_lora_weights="gaussian"`. As the name suggests, this results in initializing weight A with a Gaussian distribution (weight B is still zeros). This corresponds to the way that [diffusers](https://huggingface.co/docs/diffusers/index) initializes LoRA weights.

When quantizing the base model, e.g. for QLoRA training, consider using the [LoftQ initialization](https://arxiv.org/abs/2310.08659), which has been shown to improve the performance with quantization. The idea is that the LoRA weights are initialized such that the quantization error is minimized. To use this option, _do not_ quantize the base model. Instead, proceed as follows:

Copied


    from peft import LoftQConfig, LoraConfig, get_peft_model

    base_model = AutoModelForCausalLM.from_pretrained(...)  # don't quantize here
    loftq_config = LoftQConfig(loftq_bits=4, ...)           # set 4bit quantization
    lora_config = LoraConfig(..., init_lora_weights="loftq", loftq_config=loftq_config)
    peft_model = get_peft_model(base_model, lora_config)

There is also an option to set `initialize_lora_weights=False`. When choosing this option, the LoRA weights are initialized such that they do _not_ result in an identity transform. This is useful for debugging and testing purposes and should not be used otherwise.

Finally, the LoRA architecture scales each adapter during every forward pass by a fixed scalar, which is set at initialization, and depends on the rank `r`. Although the original LoRA method uses the scalar function `lora_alpha/r`, the research [Rank-Stabilized LoRA](https://doi.org/10.48550/arXiv.2312.03732) proves that instead using `lora_alpha/math.sqrt(r)`, stabilizes the adapters and unlocks the increased performance potential from higher ranks. Set `use_rslora=True` to use the rank-stabilized scaling `lora_alpha/math.sqrt(r)`.

[🤗 PEFT→](/docs/peft/main/en/index)

LoRAMerge LoRA weights into the base modelUtils for LoRACommon LoRA parameters in PEFTLoRA examplesInitialization options
