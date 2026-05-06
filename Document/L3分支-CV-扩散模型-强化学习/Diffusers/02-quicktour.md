Diffusers documentation

Quickstart

# Diffusers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv0.38.0v0.37.1v0.36.0v0.35.1v0.34.0v0.33.1v0.32.2v0.31.0v0.30.3v0.29.2v0.28.2v0.27.2v0.26.3v0.25.1v0.24.0v0.23.1v0.22.3v0.21.0v0.20.0v0.19.3v0.18.2v0.17.1v0.16.0v0.15.0v0.14.0v0.13.0v0.12.0v0.11.0v0.10.2v0.9.0v0.8.0v0.7.0v0.6.0v0.5.1v0.4.1v0.3.0v0.2.4 ENJAKOPTZH

[ ](https://github.com/huggingface/diffusers)

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

#  Quickstart

Diffusers is a library for developers and researchers that provides an easy inference API for generating images, videos and audio, as well as the building blocks for implementing new workflows.

Diffusers provides many optimizations out-of-the-box that makes it possible to load and run large models on setups with limited memory or to accelerate inference.

This Quickstart will give you an overview of Diffusers and get you up and generating quickly.

> Before you begin, make sure you have a Hugging Face [account](https://huggingface.co/join) in order to use gated models like [Flux](https://huggingface.co/black-forest-labs/FLUX.1-dev).

Follow the [Installation](./installation) guide to install Diffusers if it’s not already installed.

##  DiffusionPipeline

A diffusion model combines multiple components to generate outputs in any modality based on an input, such as a text description, image or both.

For a standard text-to-image model:

  1. A text encoder turns a prompt into embeddings that guide the denoising process. Some models have more than one text encoder.

  2. A scheduler contains the algorithmic specifics for gradually denoising initial random noise into clean outputs. Different schedulers affect generation speed and quality.

  3. A UNet or diffusion transformer (DiT) is the workhorse of a diffusion model.

At each step, it performs the denoising predictions, such as how much noise to remove or the general direction in which to steer the noise to generate better quality outputs.

The UNet or DiT repeats this loop for a set amount of steps to generate the final output.

  4. A variational autoencoder (VAE) encodes and decodes pixels to a spatially compressed latent-space. _Latents_ are compressed representations of an image and are more efficient to work with. The UNet or DiT operates on latents, and the clean latents at the end are decoded back into images.

The [DiffusionPipeline](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline) packages all these components into a single class for inference. There are several arguments in `__call__()` you can change, such as `num_inference_steps`, that affect the diffusion process. Try different values and arguments to see how they change generation quality or speed.

Load a model with [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained) and describe what you’d like to generate. The example below uses the default argument values.

text-to-image 

text-to-video 

Use `.images[0]` to access the generated image output.

Copied
    
    
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

##  LoRA

Adapters insert a small number of trainable parameters to the original base model. Only the inserted parameters are fine-tuned while the rest of the model weights remain frozen. This makes it fast and cheap to fine-tune a model on a new style. Among adapters, [LoRAs](./tutorials/using_peft_for_inference) are the most popular.

Add a LoRA to a pipeline with the [load_lora_weights()](/docs/diffusers/v0.38.0/en/api/loaders/lora#diffusers.loaders.QwenImageLoraLoaderMixin.load_lora_weights) method. Some LoRAs require a special word to trigger them, such as `Realism`, in the example below. Check a LoRA’s model card to see if it requires a trigger word.

Copied
    
    
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

Check out the [LoRA](./tutorials/using_peft_for_inference) docs or Adapters section to learn more.

##  Quantization

[Quantization](./quantization/overview) stores data in fewer bits to reduce memory usage. It may also speed up inference because it takes less time to perform calculations with fewer bits.

Diffusers provides several quantization backends and picking one depends on your use case. For example, [bitsandbytes](./quantization/bitsandbytes) and [torchao](./quantization/torchao) are both simple and easy to use for inference, but torchao supports more [quantization types](./quantization/torchao#supported-quantization-types) like fp8.

Configure [PipelineQuantizationConfig](/docs/diffusers/v0.38.0/en/api/quantization#diffusers.PipelineQuantizationConfig) with the backend to use, the specific arguments (refer to the [API](./api/quantization) reference for available arguments) for that backend, and which components to quantize. The example below quantizes the model to 4-bits and only uses 14.93GB of memory.

Copied
    
    
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

Take a look at the [Quantization](./quantization/overview) section for more details.

##  Optimizations

> Optimization is dependent on hardware specs such as memory. Use this [Space](https://huggingface.co/spaces/diffusers/optimized-diffusers-code) to generate code examples that include all of Diffusers’ available memory and speed optimization techniques for any model you’re using.

Modern diffusion models are very large and have billions of parameters. The iterative denoising process is also computationally intensive and slow. Diffusers provides techniques for reducing memory usage and boosting inference speed. These techniques can be combined with quantization to optimize for both memory usage and inference speed.

###  Memory usage

The text encoders and UNet or DiT can use up as much as ~30GB of memory, exceeding the amount available on many free-tier or consumer GPUs.

Offloading stores weights that aren’t currently used on the CPU and only moves them to the GPU when they’re needed. There are a few offloading types and the example below uses [model offloading](./optimization/memory#model-offloading). This moves an entire model, like a text encoder or transformer, to the CPU when it isn’t actively being used.

Call [enable_model_cpu_offload()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.enable_model_cpu_offload) to activate it. By combining quantization and offloading, the following example only requires ~12.54GB of memory.

Copied
    
    
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

Refer to the [Reduce memory usage](./optimization/memory) docs to learn more about other memory reducing techniques.

###  Inference speed

The denoising loop performs a lot of computations and can be slow. Methods like [torch.compile](./optimization/fp16#torchcompile) increases inference speed by compiling the computations into an optimized kernel. Compilation is slow for the first generation but successive generations should be much faster.

The example below uses [regional compilation](./optimization/fp16#regional-compilation) to only compile small regions of a model. It reduces cold-start latency while also providing a runtime speed up.

Call [compile_repeated_blocks()](/docs/diffusers/v0.38.0/en/api/models/overview#diffusers.ModelMixin.compile_repeated_blocks) on the model to activate it.

Copied
    
    
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

Check out the [Accelerate inference](./optimization/fp16) or [Caching](./optimization/cache) docs for more methods that speed up inference.

[ Update on GitHub](https://github.com/huggingface/diffusers/blob/main/docs/source/en/quicktour.md)

[←Installation](/docs/diffusers/installation) [Basic performance→](/docs/diffusers/stable_diffusion)
