Diffusers 文档

加速推理

# 加速推理

扩散模型在推理时速度较慢，因为生成是一个迭代过程，噪声在一定数量的「步骤」中逐渐精炼为图像或视频。要加速此过程，可以尝试使用不同的调度器（schedulers）、降低模型权重的精度以加快计算速度、使用更高效的注意力机制等。

本指南将介绍如何加速推理。

## 模型数据类型

模型权重的精度和数据类型影响推理速度，因为更高的精度需要更多内存加载和更多时间执行计算。PyTorch 默认以 float32（全精度）加载模型权重，因此更改数据类型是快速获得更快推理的简单方法。

- **bfloat16**：类似于 float16，但对数值错误更鲁棒
- **float16**：半精度
- **TensorFloat-32**：张量浮点

    import torch
    from diffusers import StableDiffusionXLPipeline

    pipeline = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.bfloat16
    ).to("cuda")

## 缩放点积注意力（SDPA）

缩放点积注意力实现了多个注意力后端——FlashAttention、xFormers 和原生 C++ 实现，自动选择最适合硬件的后端。

如果你使用 PyTorch >= 2.0，SDPA 默认启用，无需额外修改代码。

## torch.compile

`torch.compile` 通过将 PyTorch 代码和操作编译为优化的内核来加速推理。Diffusers 通常编译计算量更大的模型，如 UNet、Transformer 或 VAE。

启用以下编译器设置以获得最大速度。将内存布局更改为 `channels_last` 也可以优化内存和推理速度。

编译第一次很慢，但一旦编译完成，就会显著加快。避免在不同图像大小上调用编译后的 Pipeline，因为这会重新触发编译。

### 动态形状编译

在 `torch.compile` 中添加 `dynamic=True` 以在条件变化时避免重新编译。

### 区域编译

区域编译通过只编译模型的「小型且频繁重复的块」（通常是 Transformer 层）来减少冷启动延迟。

### 图断点

在 `torch.compile` 中指定 `fullgraph=True` 确保底层模型中没有图断点，从而获得最佳性能。

## 动态量化

动态量化通过降低精度来实现更快的数学运算来提高推理速度。使用 torchao 库对 UNet 和 VAE 应用动态 int8 量化。

## 融合投影矩阵

在注意力块中，输入被投影到三个子空间（Q、K、V）。可以水平组合这些投影矩阵，在单个步骤中执行投影。

## 参考资料

- [Presenting Flux Fast](https://pytorch.org/blog/presenting-flux-fast-making-flux-go-brrr-on-h100s/) 博客文章
- [torch.compile and Diffusers](https://pytorch.org/blog/torch-compile-and-diffusers-a-hands-on-guide-to-peak-performance/) 博客文章
