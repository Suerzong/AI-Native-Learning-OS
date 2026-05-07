# Diffusers

Diffusers 是一个用于生成图像、音频甚至分子 3D 结构的最先进预训练扩散模型库。无论你是寻找简单的推理解决方案，还是训练自己的扩散模型，Diffusers 都是一个支持两者的模块化工具箱。本库的设计理念注重 [可用性优先于性能](https://huggingface.co/docs/diffusers/conceptual/philosophy#usability-over-performance)、[简洁优先于便利](https://huggingface.co/docs/diffusers/conceptual/philosophy#simple-over-easy)、[可定制性优先于抽象](https://huggingface.co/docs/diffusers/conceptual/philosophy#tweakable-contributorfriendly-over-abstraction)。

Diffusers 提供三个核心组件：

  * 最先进的[扩散流水线（Diffusion Pipelines）](https://huggingface.co/docs/diffusers/api/pipelines/overview)，只需几行代码即可进行推理。
  * 可互换的噪声[调度器（Schedulers）](https://huggingface.co/docs/diffusers/api/schedulers/overview)，适用于不同的扩散速度和输出质量。
  * 预训练的[模型（Models）](https://huggingface.co/docs/diffusers/api/models/overview)，可作为构建模块与调度器结合，创建你自己的端到端扩散系统。

## 安装

我们推荐在虚拟环境中通过 PyPI 或 Conda 安装 Diffusers。关于安装 [PyTorch](https://pytorch.org/get-started/locally/) 的更多详情，请参阅其官方文档。

### PyTorch

使用 `pip`（官方包）：

    pip install --upgrade diffusers[torch]

使用 `conda`（由社区维护）：

    conda install -c conda-forge diffusers

### Apple Silicon（M1/M2）支持

请参阅 [如何在 Apple Silicon 上使用 Stable Diffusion](https://huggingface.co/docs/diffusers/optimization/mps) 指南。

## 快速开始

使用 Diffusers 生成输出非常简单。要从文本生成图像，使用 `from_pretrained` 方法加载任何预训练的扩散模型（在 [Hub](https://huggingface.co/models?library=diffusers&sort=downloads) 上浏览 30,000+ 检查点）：

    from diffusers import DiffusionPipeline
    import torch

    pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipeline.to("cuda")
    pipeline("An image of a squirrel in Picasso style").images[0]

你也可以深入模型和调度器工具箱，构建自己的扩散系统：

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

查看[快速开始](https://huggingface.co/docs/diffusers/quicktour)来开启你的扩散之旅！

## 如何浏览文档

**文档** | **我能学到什么？**
---|---
[教程](https://huggingface.co/docs/diffusers/tutorials/tutorial_overview) | 学习如何使用库最重要的功能（如使用模型和调度器构建自己的扩散系统、训练自己的扩散模型）的基础速成课程。
[加载](https://huggingface.co/docs/diffusers/using-diffusers/loading) | 关于如何加载和配置库的所有组件（流水线、模型和调度器）以及如何使用不同调度器的指南。
[推理流水线](https://huggingface.co/docs/diffusers/using-diffusers/overview_techniques) | 关于如何使用流水线进行不同推理任务、批量生成、控制生成输出和随机性，以及如何为库贡献流水线的指南。
[优化](https://huggingface.co/docs/diffusers/optimization/fp16) | 关于如何优化扩散模型以更快运行并消耗更少内存的指南。
[训练](https://huggingface.co/docs/diffusers/training/overview) | 关于如何使用不同训练技术为不同任务训练扩散模型的指南。

## 贡献

我们欢迎开源社区的贡献！如果你想为本库做出贡献，请查看我们的[贡献指南](https://github.com/huggingface/diffusers/blob/main/CONTRIBUTING.md)。你可以查看你想解决的 [issues](https://github.com/huggingface/diffusers/issues) 来为库做出贡献。

  * 查看 [Good first issues](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) 了解一般贡献机会
  * 查看 [New model/pipeline](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22New+pipeline%2Fmodel%22) 贡献令人兴奋的新扩散模型/扩散流水线
  * 查看 [New scheduler](https://github.com/huggingface/diffusers/issues?q=is%3Aopen+is%3Aissue+label%3A%22New+scheduler%22)

也欢迎加入我们的公共 Discord 频道。我们讨论扩散模型的最热趋势，互相帮助解决贡献、个人项目问题，或者只是闲聊。

## 热门任务与流水线

任务 | 流水线 | Hub
---|---|---
无条件图像生成 | [DDPM](https://huggingface.co/docs/diffusers/api/pipelines/ddpm) | [google/ddpm-ema-church-256](https://huggingface.co/google/ddpm-ema-church-256)
文本到图像 | [Stable Diffusion Text-to-Image](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img) | [stable-diffusion-v1-5/stable-diffusion-v1-5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)
文本到图像 | [unCLIP](https://huggingface.co/docs/diffusers/api/pipelines/unclip) | [kakaobrain/karlo-v1-alpha](https://huggingface.co/kakaobrain/karlo-v1-alpha)
文本到图像 | [DeepFloyd IF](https://huggingface.co/docs/diffusers/api/pipelines/deepfloyd_if) | [DeepFloyd/IF-I-XL-v1.0](https://huggingface.co/DeepFloyd/IF-I-XL-v1.0)
文本到图像 | [Kandinsky](https://huggingface.co/docs/diffusers/api/pipelines/kandinsky) | [kandinsky-community/kandinsky-2-2-decoder](https://huggingface.co/kandinsky-community/kandinsky-2-2-decoder)
文本引导的图像到图像 | [ControlNet](https://huggingface.co/docs/diffusers/api/pipelines/controlnet) | [lllyasviel/sd-controlnet-canny](https://huggingface.co/lllyasviel/sd-controlnet-canny)
文本引导的图像到图像 | [InstructPix2Pix](https://huggingface.co/docs/diffusers/api/pipelines/pix2pix) | [timbrooks/instruct-pix2pix](https://huggingface.co/timbrooks/instruct-pix2pix)
文本引导的图像到图像 | [Stable Diffusion Image-to-Image](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/img2img) | [stable-diffusion-v1-5/stable-diffusion-v1-5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)
文本引导的图像修复 | [Stable Diffusion Inpainting](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/inpaint) | [stable-diffusion-v1-5/stable-diffusion-inpainting](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-inpainting)
图像变体 | [Stable Diffusion Image Variation](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/image_variation) | [lambdalabs/sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers)
超分辨率 | [Stable Diffusion Upscale](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/upscale) | [stabilityai/stable-diffusion-x4-upscaler](https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler)
超分辨率 | [Stable Diffusion Latent Upscale](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/latent_upscale) | [stabilityai/sd-x2-latent-upscaler](https://huggingface.co/stabilityai/sd-x2-latent-upscaler)

## 使用 Diffusers 的热门库

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
  * 以及 14,000+ 其他优秀的 GitHub 仓库

## 致谢

本库凝聚了许多不同作者先前工作的结晶，没有他们出色的研究和实现就不可能有今天的成果。我们要特别感谢以下对我们的开发提供帮助的实现：

  * @CompVis 的潜在扩散模型库，详见 [这里](https://github.com/CompVis/latent-diffusion)
  * @hojonathanho 的原始 DDPM 实现，详见 [这里](https://github.com/hojonathanho/diffusion)，以及 @pesser 非常有用的 PyTorch 移植版本，详见 [这里](https://github.com/pesser/pytorch_diffusion)
  * @ermongroup 的 DDIM 实现，详见 [这里](https://github.com/ermongroup/ddim)
  * @yang-song 的 Score-VE 和 Score-VP 实现，详见 [这里](https://github.com/yang-song/score_sde_pytorch)

我们还要感谢 @heejkoo 整理的关于扩散模型的论文、代码和资源的非常有帮助的综述，详见 [这里](https://github.com/heejkoo/Awesome-Diffusion-Models)，以及 @crowsonkb 和 @rromb 的有益讨论和见解。

## 引用

    @misc{von-platen-etal-2022-diffusers,
      author = {Patrick von Platen and Suraj Patil and Anton Lozhkov and Pedro Cuenca and Nathan Lambert and Kashif Rasul and Mishig Davaadorj and Dhruv Nair and Sayak Paul and William Berman and Yiyi Xu and Steven Liu and Thomas Wolf},
      title = {Diffusers: State-of-the-art diffusion models},
      year = {2022},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/huggingface/diffusers}}
    }
