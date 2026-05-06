Diffusers documentation

Schedulers

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

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)

#  Schedulers

A scheduler is an algorithm that provides instructions to the denoising process such as how much noise to remove at a certain step. It takes the model prediction from step _t_ and applies an update for how to compute the next sample at step _t-1_. Different schedulers produce different results; some are faster while others are more accurate.

Diffusers supports many schedulers and allows you to modify their timestep schedules, timestep spacing, and more, to generate high-quality images in fewer steps.

This guide will show you how to load and customize schedulers.

##  Loading schedulers

Schedulers don’t have any parameters and are defined in a configuration file. Access the `.scheduler` attribute of a pipeline to view the configuration.

Copied
    
    
    import torch
    from diffusers import DiffusionPipeline
    
    pipeline = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, device_map="cuda"
    )
    pipeline.scheduler

Load a different scheduler with [from_pretrained()](/docs/diffusers/v0.38.0/en/api/schedulers/overview#diffusers.SchedulerMixin.from_pretrained) and specify the `subfolder` argument to load the configuration file into the correct subfolder of the pipeline repository. Pass the new scheduler to the existing pipeline.

Copied
    
    
    from diffusers import DPMSolverMultistepScheduler
    
    dpm = DPMSolverMultistepScheduler.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler"
    )
    pipeline = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        scheduler=dpm,
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    pipeline.scheduler

##  Timestep schedules

Timestep or noise schedule decides how noise is distributed over the denoising process. The schedule can be linear or more concentrated toward the beginning or end. It is a precomputed sequence of noise levels generated from the scheduler’s default configuration, but it can be customized to use other schedules.

> The `timesteps` argument is only supported for a select list of schedulers and pipelines. Feel free to open a feature request if you want to extend these parameters to a scheduler and pipeline that does not currently support it!

The example below uses the [Align Your Steps (AYS)](https://research.nvidia.com/labs/toronto-ai/AlignYourSteps/) schedule which can generate a high-quality image in 10 steps, significantly speeding up generation and reducing computation time.

Import the schedule and pass it to the `timesteps` argument in the pipeline.

Copied
    
    
    import torch
    from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
    from diffusers.schedulers import AysSchedules
    
    sampling_schedule = AysSchedules["StableDiffusionXLTimesteps"]
    print(sampling_schedule)
    "[999, 845, 730, 587, 443, 310, 193, 116, 53, 13]"
    
    pipeline = DiffusionPipeline.from_pretrained(
        "SG161222/RealVisXL_V4.0",
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
      pipeline.scheduler.config, algorithm_type="sde-dpmsolver++"
    )
    
    prompt = "A cinematic shot of a cute little rabbit wearing a jacket and doing a thumbs up"
    image = pipeline(
        prompt=prompt,
        negative_prompt="",
        timesteps=sampling_schedule,
    ).images[0]

![](https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/ays.png) AYS timestep schedule 10 steps

![](https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/10.png) Linearly-spaced timestep schedule 10 steps

![](https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/25.png) Linearly-spaced timestep schedule 25 steps

###  Rescaling schedules

Denoising should begin with pure noise and the signal-to-noise (SNR) ration should be zero. However, some models don’t actually start from pure noise which makes it difficult to generate images at brightness extremes.

> Train your own model with `v_prediction` by adding the `--prediction_type="v_prediction"` flag to your training script. You can also [search](https://huggingface.co/search/full-text?q=v_prediction&type=model) for existing models trained with `v_prediction`.

To fix this, a model must be trained with `v_prediction`. If a model is trained with `v_prediction`, then enable the following arguments in the scheduler.

  * Set `rescale_betas_zero_snr=True` to rescale the noise schedule to the very last timestep with exactly zero SNR
  * Set `timestep_spacing="trailing"` to force sampling from the last timestep with pure noise

Copied
    
    
    from diffusers import DiffusionPipeline, DDIMScheduler
    
    pipeline = DiffusionPipeline.from_pretrained("ptx0/pseudo-journey-v2", device_map="cuda")
    
    pipeline.scheduler = DDIMScheduler.from_config(
        pipeline.scheduler.config, rescale_betas_zero_snr=True, timestep_spacing="trailing"
    )

Set `guidance_rescale` in the pipeline to avoid overexposed images. A lower value increases brightness, but some details may appear washed out.

Copied
    
    
    prompt = """
    cinematic photo of a snowy mountain at night with the northern lights aurora borealis
    overhead, 35mm photograph, film, professional, 4k, highly detailed
    """
    image = pipeline(prompt, guidance_rescale=0.7).images[0]

![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/no-zero-snr.png) default Stable Diffusion v2-1 image

![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/zero-snr.png) image with zero SNR and trailing timestep spacing enabled

##  Timestep spacing

Timestep spacing refers to the specific steps _t_ to sample from from the schedule. Diffusers provides three spacing types as shown below.

spacing strategy | spacing calculation | example timesteps  
---|---|---  
`leading` | evenly spaced steps | `[900, 800, 700, ..., 100, 0]`  
`linspace` | include first and last steps and evenly divide remaining intermediate steps | `[1000, 888.89, 777.78, ..., 111.11, 0]`  
`trailing` | include last step and evenly divide remaining intermediate steps beginning from the end | `[999, 899, 799, 699, 599, 499, 399, 299, 199, 99]`  
  
Pass the spacing strategy to the `timestep_spacing` argument in the scheduler.

> The `trailing` strategy typically produces higher quality images with more details with fewer steps, but the difference in quality is not as obvious for more standard step values.

Copied
    
    
    import torch
    from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
    
    pipeline = DiffusionPipeline.from_pretrained(
        "SG161222/RealVisXL_V4.0",
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
      pipeline.scheduler.config, timestep_spacing="trailing"
    )
    
    prompt = "A cinematic shot of a cute little black cat sitting on a pumpkin at night"
    image = pipeline(
        prompt=prompt,
        negative_prompt="",
        num_inference_steps=5,
    ).images[0]
    image

![](https://huggingface.co/datasets/stevhliu/testing-images/resolve/main/trailing_spacing.png) trailing spacing after 5 steps

![](https://huggingface.co/datasets/stevhliu/testing-images/resolve/main/leading_spacing.png) leading spacing after 5 steps

##  Sigmas

Sigmas is a measure of how noisy a sample is at a certain step as defined by the schedule. When using custom `sigmas`, the `timesteps` are calculated from these values instead of the default scheduler configuration.

> The `sigmas` argument is only supported for a select list of schedulers and pipelines. Feel free to open a feature request if you want to extend these parameters to a scheduler and pipeline that does not currently support it!

Pass the custom sigmas to the `sigmas` argument in the pipeline. The example below uses the [sigmas](https://github.com/huggingface/diffusers/blob/6529ee67ec02fcf58d2fd9242164ea002b351d75/src/diffusers/schedulers/scheduling_utils.py#L55) from the 10-step AYS schedule.

Copied
    
    
    import torch
    from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
    
    pipeline = DiffusionPipeline.from_pretrained(
        "SG161222/RealVisXL_V4.0",
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
      pipeline.scheduler.config, algorithm_type="sde-dpmsolver++"
    )
    
    sigmas = [14.615, 6.315, 3.771, 2.181, 1.342, 0.862, 0.555, 0.380, 0.234, 0.113, 0.0]
    prompt = "A cinematic shot of a cute little rabbit wearing a jacket and doing a thumbs up"
    image = pipeline(
        prompt=prompt,
        negative_prompt="",
        sigmas=sigmas,
    ).images[0]

###  Karras sigmas

[Karras sigmas](https://huggingface.co/papers/2206.00364) resamples the noise schedule for more efficient sampling by clustering sigmas more densely in the middle of the sequence where structure reconstruction is critical, while using fewer sigmas at the beginning and end where noise changes have less impact. This can increase the level of details in a generated image.

Set `use_karras_sigmas=True` in the scheduler to enable it.

Copied
    
    
    import torch
    from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
    
    pipeline = DiffusionPipeline.from_pretrained(
        "SG161222/RealVisXL_V4.0",
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
      pipeline.scheduler.config,
      algorithm_type="sde-dpmsolver++",
      use_karras_sigmas=True,
    )
    
    prompt = "A cinematic shot of a cute little rabbit wearing a jacket and doing a thumbs up"
    image = pipeline(
        prompt=prompt,
        negative_prompt="",
        sigmas=sigmas,
    ).images[0]

![](https://huggingface.co/datasets/stevhliu/testing-images/resolve/main/karras_sigmas_true.png) Karras sigmas enabled

![](https://huggingface.co/datasets/stevhliu/testing-images/resolve/main/karras_sigmas_false.png) Karras sigmas disabled

Refer to the scheduler API [overview](../api/schedulers/overview) for a list of schedulers that support Karras sigmas. It should only be used for models trained with Karras sigmas.

##  Choosing a scheduler

It’s important to try different schedulers to find the best one for your use case. Here are a few recommendations to help you get started.

  * DPM++ 2M SDE Karras is generally a good all-purpose option.
  * [TCDScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/tcd#diffusers.TCDScheduler) works well for distilled models.
  * [FlowMatchEulerDiscreteScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/flow_match_euler_discrete#diffusers.FlowMatchEulerDiscreteScheduler) and [FlowMatchHeunDiscreteScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/flow_match_heun_discrete#diffusers.FlowMatchHeunDiscreteScheduler) for FlowMatch models.
  * [EulerDiscreteScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/euler#diffusers.EulerDiscreteScheduler) or [EulerAncestralDiscreteScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/euler_ancestral#diffusers.EulerAncestralDiscreteScheduler) for generating anime style images.
  * DPM++ 2M paired with [LCMScheduler](/docs/diffusers/v0.38.0/en/api/schedulers/lcm#diffusers.LCMScheduler) on SDXL for generating realistic images.

##  Resources

  * Read the [Common Diffusion Noise Schedules and Sample Steps are Flawed](https://huggingface.co/papers/2305.08891) paper for more details about rescaling the noise schedule to enforce zero SNR.

[ Update on GitHub](https://github.com/huggingface/diffusers/blob/main/docs/source/en/using-diffusers/schedulers.md)

[←Reproducibility](/docs/diffusers/using-diffusers/reusing_seeds) [Guiders→](/docs/diffusers/using-diffusers/guiders)
