Diffusers 文档

DiffusionPipeline

# Diffusers

## DiffusionPipeline

扩散模型由多个组件组成，如 UNet 或扩散 Transformer（DiT）、文本编码器、变分自编码器（VAE）和调度器（Schedulers）。DiffusionPipeline 将所有这些组件包装到一个易于使用的 API 中，同时保留修改其组件的灵活性。

本指南将展示如何加载 DiffusionPipeline。

## 加载 Pipeline

DiffusionPipeline 是一个基础 Pipeline 类，通过扫描 `model_index.json` 文件中的类名，自动选择并返回模型 Pipeline 子类的实例。将模型 ID 传递给 `from_pretrained()` 以加载 Pipeline。

    import torch
    from diffusers import DiffusionPipeline

    pipeline = DiffusionPipeline.from_pretrained(
      "Qwen/Qwen-Image", torch_dtype=torch.bfloat16, device_map="cuda"
    )

每个模型都有一个继承自 DiffusionPipeline 的特定 Pipeline 子类。子类通常专注于特定任务。

Pipeline 子类 | 任务
---|---
QwenImagePipeline | 文本到图像（text-to-image）
QwenImageImg2ImgPipeline | 图像到图像（image-to-image）
QwenImageInpaintPipeline | 图像修复（inpaint）

你也可以直接使用子类，将模型 ID 传递给 `from_pretrained()`。

### 本地 Pipeline

Pipeline 也可以在本地运行。使用 `snapshot_download` 下载模型仓库，然后将文件夹路径传递给 `from_pretrained()`。当检测到本地路径时，`from_pretrained()` 方法不会从 Hub 下载文件。

## Pipeline 数据类型

使用 `torch_dtype` 参数以特定数据类型加载模型。这允许你以不同精度加载不同模型。例如，以半精度加载大型 Transformer 模型可以减少所需内存。可以将每个模型的数据类型作为字典传递给 `torch_dtype`，使用 `default` 键设置默认数据类型。

## 设备放置

`device_map` 参数决定各个模型或 Pipeline 在加速器（如 GPU）上的放置方式。支持两种选项：

- `"cuda"`：将 Pipeline 放置在 CUDA 等支持的加速器设备上
- `"balanced"`：在所有 GPU 上均匀分布 Pipeline

使用 `max_memory` 参数为每个设备分配最大内存量。使用 `reset_device_map()` 方法重置设备映射。

## 并行加载

大型模型通常被分片（sharded）为更小的文件以便加载。Diffusers 支持并行加载分片以加速加载过程。设置 `HF_ENABLE_PARALLEL_LOADING` 为 `"YES"` 启用并行加载。

## 替换 Pipeline 中的模型

DiffusionPipeline 灵活且支持加载不同的模型或调度器。你可以使用更稳定的 VAE 版本或不同的调度器来优化生成速度或质量。

## 在多个 Pipeline 中复用模型

使用多个使用相同模型的 Pipeline 时，`from_pipe()` 方法支持复用模型而不是每次都重新加载。这允许你使用多个 Pipeline 而不增加内存使用。注意：通过 `from_pipe()` 创建的 Pipeline 共享相同的模型和「状态」。

## 安全检查器

Diffusers 为旧版 Stable Diffusion 模型提供了安全检查器，以防止生成有害内容。如果要禁用安全检查器，在 `from_pretrained()` 中传入 `safety_checker=None`。
