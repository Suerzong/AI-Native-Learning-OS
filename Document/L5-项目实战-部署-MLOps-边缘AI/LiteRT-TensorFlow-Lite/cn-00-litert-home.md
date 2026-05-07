# LiteRT — Google 端侧 AI 框架

> 来源：https://ai.google.dev/edge/litert

### LiteRT 是 Google 的端侧框架，用于在边缘平台上实现高性能 ML 和 GenAI 部署。

高效的模型转换、运行时和优化，助力端侧机器学习。

### 基于久经考验的 TensorFlow Lite 基础

LiteRT 不仅仅是全新产品，它是全球部署最广泛的机器学习运行时的下一代版本。它驱动着你每天使用的应用，在数十亿设备上提供低延迟和高隐私保护。

## 被最关键的 Google 应用所信赖

10 万+ 应用，数十亿全球用户

## LiteRT 亮点

### 跨平台就绪

### 释放 GenAI 潜力

### 简化的硬件加速

### 多框架支持

## 通过 LiteRT 部署

简化从训练到端侧部署的深度学习工作流。

### 1. 获取模型

使用 .tflite 预训练模型或将 PyTorch、JAX 或 TensorFlow 模型转换为 .tflite 格式。

[了解转换](https://ai.google.dev/edge/litert/conversion/overview)

### 2. 优化

使用 LiteRT 优化工具包对模型进行训练后量化（Post-training Quantization）。

[探索优化](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/model_optimization)

### 3. 运行

使用 LiteRT 部署你的模型，并为应用选择最优的加速器。

[查看部署目标](https://ai.google.dev/edge/litert/overview#hardware-acceleration)

## 选择你的开发路径

使用 LiteRT 在任何地方部署 AI——从高性能移动应用到资源受限的 IoT 设备。

### [现有 TFLite 用户](https://ai.google.dev/edge/litert/migration)

迁移到 LiteRT 以利用增强的性能和跨平台（Android、桌面、Web）统一 API。

### [BYOM：自带模型](https://ai.google.dev/edge/litert/conversion/overview)

拥有 PyTorch 模型，希望在端侧实现视觉或音频体验。

### [部署生成式 AI 模型](https://ai.google.dev/edge/litert/next/litert_lm_npu)

使用优化的开放权重 GenAI 模型（如 Gemma 或其他开放权重模型）创建复杂的端侧聊天机器人。

### [[高级] 模型专家](https://ai.google.dev/edge/litert/genai/overview)

编写自定义模型或执行深度硬件特定的 CPU/GPU/NPU 优化以获得峰值性能。

## 示例、模型和演示

### [在 GitHub 上查看 LiteRT 示例应用](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api)

完整的端到端示例应用。

### [查看 GenAI 模型](https://huggingface.co/litert-community)

预训练的开箱即用 GenAI 模型。

### [查看演示 — Google AI Edge Gallery 应用](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery)

展示使用 LiteRT 的端侧 ML/GenAI 用例的画廊。

## 博客和公告

随时了解 LiteRT 团队的最新公告、技术深入分析和性能基准测试。

### [LiteRT：端侧 AI 的通用框架](https://developers.googleblog.com/litert-the-universal-framework-for-on-device-ai/)

Google 统一的端侧 ML 框架，从 TFLite 演进而来，用于高性能部署。

### [MediaTek NPU 与 LiteRT：驱动下一代端侧 AI](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/)

将 NPU 加速支持扩展到 MediaTek 芯片组，实现高效 AI。

### [在 Qualcomm NPU 上通过 LiteRT 实现峰值性能](https://developers.googleblog.com/unlocking-peak-performance-on-qualcomm-npu-with-litert/)

在 Qualcomm 神经处理单元上实现生成式 AI 的突破性性能。

### [LiteRT：极致性能，化繁为简](https://developers.googleblog.com/litert-maximum-performance-simplified/)

介绍 CompiledModel API，实现自动硬件选择和异步执行。

### [通过 LiteRT-LM 在 Chrome、Chromebook Plus 和 Pixel Watch 上实现端侧 GenAI](https://developers.googleblog.com/on-device-genai-in-chrome-chromebook-plus-and-pixel-watch-with-litert-lm/)

使用 LiteRT-LM 在可穿戴设备和浏览器平台上部署语言模型。

### [Google AI Edge 小型语言模型、多模态和函数调用](https://developers.googleblog.com/google-ai-edge-small-language-models-multimodality-rag-function-calling/)

关于边缘语言模型的 RAG、多模态和函数调用的最新见解。

## 加入社区

### [LiteRT GitHub 社区](https://github.com/google-ai-edge/LiteRT)

直接为项目做贡献并与核心开发者协作。

### [Hugging Face Hub](https://huggingface.co/litert-community)

在 Hugging Face Hub 上获取优化的开放权重模型。

### [开始你的 LiteRT 之旅](https://ai.google.dev/edge/litert/overview)

准备好将你的端侧 ML 提升到新水平了吗？探索文档并立即开始构建。
