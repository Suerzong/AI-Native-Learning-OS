# 使用 LiteRT 进行端侧推理

> 来源：https://ai.google.dev/edge/litert/inference

LiteRT `CompiledModel` API 代表了端侧 ML 推理的现代标准，提供了**简化的硬件加速**，性能显著优于 `Interpreter` API。该接口通过提供统一的开发者体验和旨在最大化硬件效率的高级功能，简化了 `.tflite` 模型在各种边缘平台上的部署。

## 为什么选择 `CompiledModel` API？

虽然 `Interpreter` API 仍可用于向后兼容，但 `CompiledModel` API 是新性能和加速器功能的优先发展方向。以下是推荐选择它的原因：

- **一流的 GPU 加速**：利用 **ML Drift**（最先进的 GPU 加速库），在移动、Web、桌面和 IoT 设备上提供可靠的 GPU 推理。参见 [LiteRT GPU 加速](https://ai.google.dev/edge/litert/next/gpu)。

- **统一的 NPU 访问**：提供单一、一致的开发者体验来访问来自不同供应商（如 Google Tensor、Qualcomm、MediaTek）的 NPU，抽象掉供应商特定的编译器和运行时复杂性。参见 [LiteRT NPU 加速](https://ai.google.dev/edge/litert/next/npu)。

- **自动硬件选择**：基于可用硬件和内部优先级逻辑，自动在 CPU、GPU 和 NPU 之间选择最优后端，无需手动配置委托（Delegate）。

- **异步执行**：利用操作系统级机制（如同步围栏）允许硬件加速器在前一任务完成时直接触发，无需 CPU 参与。这可以将延迟降低最多 2 倍，并确保更流畅、更交互的 AI 体验。

- **高效的 I/O 缓冲区管理**：利用 `TensorBuffer` API 管理加速器之间的高性能数据流。这包括跨 `AHardwareBuffer`、OpenCL 和 OpenGL 的**零拷贝缓冲区互操作**，消除了预处理、推理和后处理阶段之间昂贵的数据拷贝。

## 开始使用 `CompiledModel` API

- **对于经典 ML 模型**，请参阅以下演示应用：
  - [图像分割 Kotlin 应用](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api/image_segmentation)：CPU/GPU/NPU 推理。
  - [图像分割 C++ 应用](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api/image_segmentation/async_segmentation)：支持**异步**执行的 CPU/GPU/NPU 推理。

- **对于 GenAI 模型**，请参阅以下演示应用：
  - [EmbeddingGemma 语义相似度 C++ 应用](https://github.com/google-ai-edge/LiteRT/tree/main/litert/samples/semantic_similarity)：CPU/GPU/NPU 推理。

## 支持的平台

LiteRT `CompiledModel` API 支持在 Android、iOS、Web、IoT 和桌面设备上进行高性能推理。请参阅[平台特定指南](https://ai.google.dev/edge/litert/overview#integrate-model)。
