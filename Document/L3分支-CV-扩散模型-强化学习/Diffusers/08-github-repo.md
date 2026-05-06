[![](https://raw.githubusercontent.com/huggingface/diffusers/main/docs/source/en/imgs/diffusers_library.jpg)](https://raw.githubusercontent.com/huggingface/diffusers/main/docs/source/en/imgs/diffusers_library.jpg)   

[![GitHub](https://camo.githubusercontent.com/a4dc7f07b0858130ffed06d1c2ff3357f48e76f3dd8d1c9ceef7bbf6e8add1d8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f68756767696e67666163652f64617461736574732e7376673f636f6c6f723d626c7565)](https://github.com/huggingface/diffusers/blob/main/LICENSE) [![GitHub release](https://camo.githubusercontent.com/d549e74d9071fba80b4b526e12c9ca67cc563c25bb1b6c42d8cd2fe6cb8fb566/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f68756767696e67666163652f6469666675736572732e737667)](https://github.com/huggingface/diffusers/releases) [![GitHub release](https://camo.githubusercontent.com/01f0da8f4e51d966dfc4d06e50ff787471386eb5b1289f89a44034cd55d04d22/68747470733a2f2f7374617469632e706570792e746563682f62616467652f6469666675736572732f6d6f6e7468)](https://pepy.tech/project/diffusers) [![Contributor Covenant](https://camo.githubusercontent.com/4ae39ae593b602cf0ae07972b61c73728b77ec8e2cf40f579a2441948208036b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e7472696275746f72253230436f76656e616e742d322e312d3462616161612e737667)](/huggingface/diffusers/blob/main/CODE_OF_CONDUCT.md) [![X account](https://camo.githubusercontent.com/fc6a91c4049def5bfe7743a75e98295188c967bb558e5d18b142ee4b9d30e3cb/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f75726c2f68747470732f747769747465722e636f6d2f6469666675736572736c69622e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f772532302534306469666675736572736c6962)](https://twitter.com/diffuserslib)

🤗 Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even 3D structures of molecules. Whether you're looking for a simple inference solution or training your own diffusion models, 🤗 Diffusers is a modular toolbox that supports both. Our library is designed with a focus on [usability over performance](https://huggingface.co/docs/diffusers/conceptual/philosophy#usability-over-performance), [simple over easy](https://huggingface.co/docs/diffusers/conceptual/philosophy#simple-over-easy), and [customizability over abstractions](https://huggingface.co/docs/diffusers/conceptual/philosophy#tweakable-contributorfriendly-over-abstraction).

🤗 Diffusers offers three core components:

  * State-of-the-art [diffusion pipelines](https://huggingface.co/docs/diffusers/api/pipelines/overview) that can be run in inference with just a few lines of code.
  * Interchangeable noise [schedulers](https://huggingface.co/docs/diffusers/api/schedulers/overview) for different diffusion speeds and output quality.
  * Pretrained [models](https://huggingface.co/docs/diffusers/api/models/overview) that can be used as building blocks, and combined with schedulers, for creating your own end-to-end diffusion systems.

## Installation

We recommend installing 🤗 Diffusers in a virtual environment from PyPI or Conda. For more details about installing [PyTorch](https://pytorch.org/get-started/locally/), please refer to their official documentation.

### PyTorch

With `pip` (official package):
    
    
    pip install --upgrade diffusers[torch]

With `conda` (maintained by the community):
    
    
    conda install -c conda-forge diffusers

### Apple Silicon (M1/M2) support

Please refer to the [How to use Stable Diffusion in Apple Silicon](https://huggingface.co/docs/diffusers/optimization/mps) guide.

## Quickstart

Generating outputs is super easy with 🤗 Diffusers. To generate an image from text, use the `from_pretrained` method to load any pretrained diffusion model (browse the [Hub](https://huggingface.co/models?library=diffusers&sort=downloads) for 30,000+ checkpoints):
    
    
    from diffusers import DiffusionPipeline
    import torch
    
    pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipeline.to("cuda")
    pipeline("An image of a squirrel in Picasso style").images[0]

You can also dig into the models and schedulers toolbox to build your own diffusion system:
    
    
    from diffusers import DDPMScheduler, UNet2DModel
    from PIL import Image
    import torch
    
    scheduler = DDPMScheduler.from_pretrained("google/ddpm-cat-256")
    model = UNet2DModel.from_pretrained("google/ddpm-cat-256").to("cuda")
    scheduler.set_timesteps(50)
    
    sample_size = model.config.sample_size
    noise = torch.randn((1, 3, sample_size, sample_size), device="cuda")
    input = noise
    
    for t in scheduler.timesteps:
        with torch.no_grad():
            noisy_residual = model(input, t).sample
            prev_noisy_sample = scheduler.step(noisy_residual, t, input).prev_sample
            input = prev_noisy_sample
    
    image = (input / 2 + 0.5).clamp(0, 1)
    image = image.cpu().permute(0, 2, 3, 1).numpy()[0]
    image = Image.fromarray((image * 255).round().astype("uint8"))
    image

Check out the [Quickstart](https://huggingface.co/docs/diffusers/quicktour) to launch your diffusion journey today!

## How to navigate the documentation

**Documentation** | **What can I learn?**  
---|---  
[Tutorial](https://huggingface.co/docs/diffusers/tutorials/tutorial_overview) | A basic crash course for learning how to use the library's most important features like using models and schedulers to build your own diffusion system, and training your own diffusion model.  
[Loading](https://huggingface.co/docs/diffusers/using-diffusers/loading) | Guides for how to load and configure all the components (pipelines, models, and schedulers) of the library, as well as how to use different schedulers.  
[Pipelines for inference](https://huggingface.co/docs/diffusers/using-diffusers/overview_techniques) | Guides for how to use pipelines for different inference tasks, batched generation, controlling generated outputs and randomness, and how to contribute a pipeline to the library.  
[Optimization](https://huggingface.co/docs/diffusers/optimization/fp16) | Guides for how to optimize your diffusion model to run faster and consume less memory.  
[Training](https://huggingface.co/docs/diffusers/training/overview) | Guides for how to train a diffusion model for different tasks with different training techniques.  
  
## Contribution

We ❤️ contributions from the open-source community! If you want to contribute to this library, please check out our [Contribution guide](https://github.com/huggingface/diffusers/blob/main/CONTRIBUTING.md). You can look out for [issues](https://github.com/huggingface/diffusers/issues) you'd like to tackle to contribute to the library.

  * See [Good first issues](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) for general opportunities to contribute
  * See [New model/pipeline](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22New+pipeline%2Fmodel%22) to contribute exciting new diffusion models / diffusion pipelines
  * See [New scheduler](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22New+scheduler%22)

Also, say 👋 in our public Discord channel [![Join us on Discord](https://camo.githubusercontent.com/6df2255d075e0356a86a3db06dda295fda5ee305948a6eb9f76786703c110b1e/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3832333831333135393539323030313533373f636f6c6f723d353836354632266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/G7tWnz98XR). We discuss the hottest trends about diffusion models, help each other with contributions, personal projects or just hang out ☕.

## Popular Tasks & Pipelines

Task | Pipeline | 🤗 Hub  
---|---|---  
Unconditional Image Generation | [ DDPM ](https://huggingface.co/docs/diffusers/api/pipelines/ddpm) | [ google/ddpm-ema-church-256 ](https://huggingface.co/google/ddpm-ema-church-256)  
Text-to-Image | [Stable Diffusion Text-to-Image](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img) | [ stable-diffusion-v1-5/stable-diffusion-v1-5 ](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)  
Text-to-Image | [unCLIP](https://huggingface.co/docs/diffusers/api/pipelines/unclip) | [ kakaobrain/karlo-v1-alpha ](https://huggingface.co/kakaobrain/karlo-v1-alpha)  
Text-to-Image | [DeepFloyd IF](https://huggingface.co/docs/diffusers/api/pipelines/deepfloyd_if) | [ DeepFloyd/IF-I-XL-v1.0 ](https://huggingface.co/DeepFloyd/IF-I-XL-v1.0)  
Text-to-Image | [Kandinsky](https://huggingface.co/docs/diffusers/api/pipelines/kandinsky) | [ kandinsky-community/kandinsky-2-2-decoder ](https://huggingface.co/kandinsky-community/kandinsky-2-2-decoder)  
Text-guided Image-to-Image | [ControlNet](https://huggingface.co/docs/diffusers/api/pipelines/controlnet) | [ lllyasviel/sd-controlnet-canny ](https://huggingface.co/lllyasviel/sd-controlnet-canny)  
Text-guided Image-to-Image | [InstructPix2Pix](https://huggingface.co/docs/diffusers/api/pipelines/pix2pix) | [ timbrooks/instruct-pix2pix ](https://huggingface.co/timbrooks/instruct-pix2pix)  
Text-guided Image-to-Image | [Stable Diffusion Image-to-Image](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/img2img) | [ stable-diffusion-v1-5/stable-diffusion-v1-5 ](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)  
Text-guided Image Inpainting | [Stable Diffusion Inpainting](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/inpaint) | [ stable-diffusion-v1-5/stable-diffusion-inpainting ](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-inpainting)  
Image Variation | [Stable Diffusion Image Variation](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/image_variation) | [ lambdalabs/sd-image-variations-diffusers ](https://huggingface.co/lambdalabs/sd-image-variations-diffusers)  
Super Resolution | [Stable Diffusion Upscale](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/upscale) | [ stabilityai/stable-diffusion-x4-upscaler ](https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler)  
Super Resolution | [Stable Diffusion Latent Upscale](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/latent_upscale) | [ stabilityai/sd-x2-latent-upscaler ](https://huggingface.co/stabilityai/sd-x2-latent-upscaler)  
  
## Popular libraries using 🧨 Diffusers

  * <https://github.com/microsoft/TaskMatrix>
  * <https://github.com/invoke-ai/InvokeAI>
  * <https://github.com/InstantID/InstantID>
  * <https://github.com/apple/ml-stable-diffusion>
  * <https://github.com/Sanster/lama-cleaner>
  * <https://github.com/IDEA-Research/Grounded-Segment-Anything>
  * <https://github.com/ashawkey/stable-dreamfusion>
  * <https://github.com/deep-floyd/IF>
  * <https://github.com/bentoml/BentoML>
  * <https://github.com/bmaltais/kohya_ss>
  * +14,000 other amazing GitHub repositories 💪

Thank you for using us ❤️.

## Credits

This library concretizes previous work by many different authors and would not have been possible without their great research and implementations. We'd like to thank, in particular, the following implementations which have helped us in our development and without which the API could not have been as polished today:

  * @CompVis' latent diffusion models library, available [here](https://github.com/CompVis/latent-diffusion)
  * @hojonathanho original DDPM implementation, available [here](https://github.com/hojonathanho/diffusion) as well as the extremely useful translation into PyTorch by @pesser, available [here](https://github.com/pesser/pytorch_diffusion)
  * @ermongroup's DDIM implementation, available [here](https://github.com/ermongroup/ddim)
  * @yang-song's Score-VE and Score-VP implementations, available [here](https://github.com/yang-song/score_sde_pytorch)

We also want to thank @heejkoo for the very helpful overview of papers, code and resources on diffusion models, available [here](https://github.com/heejkoo/Awesome-Diffusion-Models) as well as @crowsonkb and @rromb for useful discussions and insights.

## Citation
    
    
    @misc{von-platen-etal-2022-diffusers,
      author = {Patrick von Platen and Suraj Patil and Anton Lozhkov and Pedro Cuenca and Nathan Lambert and Kashif Rasul and Mishig Davaadorj and Dhruv Nair and Sayak Paul and William Berman and Yiyi Xu and Steven Liu and Thomas Wolf},
      title = {Diffusers: State-of-the-art diffusion models},
      year = {2022},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/huggingface/diffusers}}
    }
