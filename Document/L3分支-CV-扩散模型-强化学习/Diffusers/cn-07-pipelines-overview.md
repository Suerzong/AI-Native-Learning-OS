Diffusers 文档

Pipelines 概览

# Pipelines

Pipelines 提供了一种通过将所有必要的组件（多个独立训练的模型、调度器和处理器）打包到一个端到端的类中来运行最先进扩散模型进行推理的简单方法。Pipelines 是灵活的，可以适应使用不同的调度器甚至模型组件。

所有 Pipeline 都从基础 DiffusionPipeline 类构建，该类提供加载、下载和保存所有组件的基本功能。使用 `from_pretrained()` 加载的特定 Pipeline 类型会自动检测，Pipeline 组件被加载并传递给 Pipeline 的 `__init__` 函数。

> 你不应该使用 DiffusionPipeline 类进行训练。扩散模型的各个组件通常单独训练，因此建议直接使用它们。Pipelines 不提供任何训练功能。

## 当前可用的 Pipelines

Pipeline | 任务
---|---
AnimateDiff | 文本到视频（text2video）
AuraFlow | 文本到图像（text2image）
CogVideoX | 文本到视频（text2video）
ControlNet | 文本到图像、图像到图像、图像修复
DDIM | 无条件图像生成
DDPM | 无条件图像生成
DeepFloyd IF | 文本到图像、图像到图像、图像修复、超分辨率
DiT | 文本到图像
Flux | 文本到图像
Hunyuan-DiT | 文本到图像
InstructPix2Pix | 图像编辑
Kandinsky 2.1/2.2/3 | 文本到图像、图像到图像
Kolors | 文本到图像
Latent Consistency Models | 文本到图像
PixArt-α/Σ | 文本到图像
Shap-E | 文本到 3D、图像到 3D
Stable Audio | 文本到音频（text2audio）
Stable Cascade | 文本到图像
Stable Diffusion | 文本到图像、图像到图像、深度到图像、图像修复、超分辨率
Stable Diffusion XL | 文本到图像、图像到图像、图像修复

## DiffusionPipeline 类

DiffusionPipeline 是所有 Pipeline 的基类。提供方法来：
- 将所有 PyTorch 模块移动到你选择的设备
- 启用/禁用去噪迭代的进度条

### 主要方法

- `__call__()`：调用 Pipeline 执行推理
- `to()`：执行 Pipeline 数据类型和/或设备转换
- `components`：返回包含初始化 Pipeline 所需所有模块的字典
- `from_pretrained()`：从预训练 Pipeline 权重实例化 PyTorch 扩散 Pipeline
- `save_pretrained()`：将 Pipeline 保存到目录
- `from_pipe()`：从给定 Pipeline 创建新 Pipeline，复用模型而不重新分配内存
- `enable_attention_slicing()`：启用切片注意力计算以节省内存
- `enable_xformers_memory_efficient_attention()`：启用 xFormers 内存高效注意力
- `enable_model_cpu_offload()`：使用 accelerate 将模型卸载到 CPU 以减少内存使用
- `enable_sequential_cpu_offload()`：使用 accelerate 顺序将模型卸载到 CPU
- `enable_group_offload()`：分组卸载，平衡模块级和叶级卸载
- `enable_freeu()`：启用 FreeU 机制以改善生成质量
