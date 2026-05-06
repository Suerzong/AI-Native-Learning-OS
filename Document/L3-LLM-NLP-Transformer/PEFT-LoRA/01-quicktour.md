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

Quicktour

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

# [](#quicktour) Quicktour

PEFT offers parameter-efficient methods for finetuning large pretrained models. The traditional paradigm is to finetune all of a model’s parameters for each downstream task, but this is becoming exceedingly costly and impractical because of the enormous number of parameters in models today. Instead, it is more efficient to train a smaller number of prompt parameters or use a reparametrization method like low-rank adaptation (LoRA) to reduce the number of trainable parameters.

This quicktour will show you PEFT’s main features and how you can train or run inference on large models that would typically be inaccessible on consumer devices.

## [](#train) Train

Each PEFT method is defined by a [PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig) class that stores all the important parameters for building a [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel). For example, to train with LoRA, load and create a [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) class and specify the following parameters:

  * `task_type`: the task to train for (sequence-to-sequence language modeling in this case)
  * `inference_mode`: whether you’re using the model for inference or not
  * `r`: the dimension of the low-rank matrices
  * `lora_alpha`: the scaling factor for the low-rank matrices
  * `lora_dropout`: the dropout probability of the LoRA layers

Copied


    from peft import LoraConfig, TaskType

    peft_config = LoraConfig(task_type=TaskType.SEQ_2_SEQ_LM, inference_mode=False, r=8, lora_alpha=32, lora_dropout=0.1)

> See the [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) reference for more details about other parameters you can adjust, such as the modules to target or the bias type.

Once the [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) is setup, create a [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) with the [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) function. It takes a base model - which you can load from the Transformers library - and the [LoraConfig](/docs/peft/v0.19.0/en/package_reference/lora#peft.LoraConfig) containing the parameters for how to configure a model for training with LoRA.

Load the base model you want to finetune.

Copied


    from transformers import AutoModelForSeq2SeqLM

    model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/mt0-large")

Wrap the base model and `peft_config` with the [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) function to create a [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel). To get a sense of the number of trainable parameters in your model, use the `print_trainable_parameters` method.

Copied


    from peft import get_peft_model

    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    "output: trainable params: 2359296 || all params: 1231940608 || trainable%: 0.19151053100118282"

Out of [bigscience/mt0-large’s](https://huggingface.co/bigscience/mt0-large) 1.2B parameters, you’re only training 0.19% of them!

That is it 🎉! Now you can train the model with the Transformers [Trainer](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer), Accelerate, or any custom PyTorch training loop.

For example, to train with the [Trainer](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer) class, setup a [TrainingArguments](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.TrainingArguments) class with some training hyperparameters.

Copied


    training_args = TrainingArguments(
        output_dir="your-name/bigscience/mt0-large-lora",
        learning_rate=1e-3,
        per_device_train_batch_size=32,
        per_device_eval_batch_size=32,
        num_train_epochs=2,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

Pass the model, training arguments, dataset, tokenizer, and any other necessary component to the [Trainer](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer), and call [train](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/trainer#transformers.Trainer.train) to start training.

Copied


    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        processing_class=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    trainer.train()

### [](#save-model) Save model

After your model is finished training, you can save your model to a directory using the [save_pretrained](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.save_pretrained) function.

Copied


    model.save_pretrained("output_dir")

You can also save your model to the Hub (make sure you’re logged in to your Hugging Face account first) with the [push_to_hub](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.push_to_hub) function.

Copied


    from huggingface_hub import notebook_login

    notebook_login()
    model.push_to_hub("your-name/bigscience/mt0-large-lora")

Both methods only save the extra PEFT weights that were trained, meaning it is super efficient to store, transfer, and load. For example, this [facebook/opt-350m](https://huggingface.co/ybelkada/opt-350m-lora) model trained with LoRA only contains two files: `adapter_config.json` and `adapter_model.safetensors`. The `adapter_model.safetensors` file is just 6.3MB!

The adapter weights for a opt-350m model stored on the Hub are only ~6MB compared to the full size of the model weights, which can be ~700MB.

## [](#inference) Inference

> Take a look at the [AutoPeftModel](package_reference/auto_class) API reference for a complete list of available `AutoPeftModel` classes.

Easily load any PEFT-trained model for inference with the [AutoPeftModel](/docs/peft/v0.19.0/en/package_reference/auto_class#peft.AutoPeftModel) class and the [from_pretrained](https://huggingface.co/docs/transformers/v5.5.4/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method:

Copied


    from peft import AutoPeftModelForCausalLM
    from transformers import AutoTokenizer
    import torch

    model = AutoPeftModelForCausalLM.from_pretrained("ybelkada/opt-350m-lora")
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")

    model = model.to("cuda")
    model.eval()
    inputs = tokenizer("Preheat the oven to 350 degrees and place the cookie dough", return_tensors="pt")

    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"), max_new_tokens=50)
    print(tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0])

    "Preheat the oven to 350 degrees and place the cookie dough in the center of the oven. In a large bowl, combine the flour, baking powder, baking soda, salt, and cinnamon. In a separate bowl, combine the egg yolks, sugar, and vanilla."

For other tasks that aren’t explicitly supported with an `AutoPeftModelFor` class - such as automatic speech recognition - you can still use the base [AutoPeftModel](/docs/peft/v0.19.0/en/package_reference/auto_class#peft.AutoPeftModel) class to load a model for the task.

Copied


    from peft import AutoPeftModel

    model = AutoPeftModel.from_pretrained("smangrul/openai-whisper-large-v2-LORA-colab")

## [](#next-steps) Next steps

Now that you’ve seen how to train a model with one of the PEFT methods, we encourage you to try out some of the other methods like prompt tuning. The steps are very similar to the ones shown in the quicktour:

  1. prepare a [PeftConfig](/docs/peft/v0.19.0/en/package_reference/config#peft.PeftConfig) for a PEFT method
  2. use the [get_peft_model()](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.get_peft_model) method to create a [PeftModel](/docs/peft/v0.19.0/en/package_reference/peft_model#peft.PeftModel) from the configuration and base model

Then you can train it however you like! To load a PEFT model for inference, you can use the [AutoPeftModel](/docs/peft/v0.19.0/en/package_reference/auto_class#peft.AutoPeftModel) class.

Feel free to also take a look at the task guides if you’re interested in training a model with another PEFT method for a specific task such as semantic segmentation, multilingual automatic speech recognition, DreamBooth, token classification, and more.

[ Update on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/quicktour.md)

[←🤗 PEFT](/docs/peft/index) [Installation→](/docs/peft/install)

[Quicktour](#quicktour)[Train](#train)[Save model](#save-model)[Inference](#inference)[Next steps](#next-steps)
