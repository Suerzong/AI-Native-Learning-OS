[![](https://raw.githubusercontent.com/huggingface/diffusers/main/docs/source/en/imgs/diffusers_library.jpg)]

# Diffusers

Diffusers 是用于生成图像、音频甚至 3D 分子结构的最先进预训练扩散模型的首选库。无论你是寻找简单的推理解决方案还是训练自己的扩散模型，Diffusers 都是一个支持两者的模块化工具箱。

Diffusers 提供三个核心组件：

  * 只需几行代码即可运行的最先进**扩散 Pipeline**。
  * 适用于不同扩散速度和输出质量的可互换噪声**调度器**（Schedulers）。
  * 可用作构建模块的预训练**模型**，可与调度器组合以创建自己的端到端扩散系统。

## 安装

我们建议在虚拟环境中从 PyPI 或 Conda 安装 Diffusers。

### PyTorch

使用 `pip`：

    pip install --upgrade diffusers[torch]

使用 `conda`：

    conda install -c conda-forge diffusers

### Apple Silicon（M1/M2）支持

请参考 [How to use Stable Diffusion in Apple Silicon](https://huggingface.co/docs/diffusers/optimization/mps) 指南。

## 快速入门

使用 Diffusers 生成输出非常简单。要从文本生成图像，使用 `from_pretrained` 方法加载任何预训练的扩散模型：

    from diffusers import DiffusionPipeline
    import torch

    pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipeline.to("cuda")
    pipeline("An image of a squirrel in Picasso style").images[0]

你还可以深入模型和调度器工具箱，构建自己的扩散系统：

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

## 文档导航

文档 | 内容
---|---
教程（Tutorial） | 学习如何使用库的最重要功能
加载（Loading） | 如何加载和配置所有组件
推理 Pipeline | 如何使用 Pipeline 进行不同推理任务
优化（Optimization） | 如何优化扩散模型以更快运行并消耗更少内存
训练（Training） | 如何为不同任务训练扩散模型

## 热门任务和 Pipeline

任务 | Pipeline | Hub
---|---|---
无条件图像生成 | DDPM | google/ddpm-ema-church-256
文本到图像 | Stable Diffusion | stable-diffusion-v1-5/stable-diffusion-v1-5
文本到图像 | unCLIP | kakaobrain/karlo-v1-alpha
文本到图像 | DeepFloyd IF | DeepFloyd/IF-I-XL-v1.0
文本到图像 | Kandinsky | kandinsky-community/kandinsky-2-2-decoder
文本引导图像到图像 | ControlNet | lllyasviel/sd-controlnet-canny
文本引导图像到图像 | InstructPix2Pix | timbrooks/instruct-pix2pix
文本引导图像修复 | Stable Diffusion Inpainting | stable-diffusion-v1-5/stable-diffusion-inpainting
超分辨率 | Stable Diffusion Upscale | stabilityai/stable-diffusion-x4-upscaler

## 使用 Diffusers 的热门库

  * [TaskMatrix](https://github.com/microsoft/TaskMatrix)
  * [InvokeAI](https://github.com/invoke-ai/InvokeAI)
  * [InstantID](https://github.com/InstantID/InstantID)
  * [Apple ml-stable-diffusion](https://github.com/apple/ml-stable-diffusion)
  * [lama-cleaner](https://github.com/Sanster/lama-cleaner)
  * +14,000 其他优秀的 GitHub 仓库
