# LiteRT for Android

> 来源：https://ai.google.dev/edge/litert/android

以下 LiteRT 运行时 API 可用于 Android 开发：

- **`CompiledModel`** API：**高性能**推理的现代标准，简化跨 CPU/GPU/NPU 的硬件加速。了解更多关于[为什么选择 CompiledModel API](https://ai.google.dev/edge/litert/inference)。
- **`Interpreter`** API：基本推理 API，为向后兼容而维护。

## 开始使用 `CompiledModel` API

- **对于经典 ML 模型**，请参阅以下演示应用：
  - [图像分割 Kotlin 应用](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api/image_segmentation)：CPU/GPU/NPU 推理。
  - [图像分割 C++ 应用](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api/image_segmentation/async_segmentation)：支持**异步**执行的 CPU/GPU/NPU 推理。

- **对于 GenAI 模型**，请参阅以下演示应用：
  - [EmbeddingGemma 语义相似度 C++ 应用](https://github.com/google-ai-edge/LiteRT/tree/main/litert/samples/semantic_similarity)：CPU/GPU/NPU 推理。

## 支持的 Android 版本和 API

| LiteRT 版本 | 状态 | 支持的 API | 最低 SDK 级别 | 最低 NDK 版本 | 发布日期 |
|---|---|---|---|---|---|
| **`v2.1.0`** | 最新 | `CompiledModel` + `Interpreter`（仅 CPU） | `23`（Android 6 Marshmallow） | `r26a` | 2025-12-19 |
| **`v2.0.3`** | 旧版 | `CompiledModel` | `26`（Android 8 Oreo） | `r26a` | 2025-11-08 |
| **`v1.4.1`** | 最新 | `Interpreter` | `21`（Android 5 Lollipop） | `r26a` | 2025-11-07 |
| **`v1.4.0`** | 旧版 | `Interpreter` | `26`（Android 8 Oreo） | `r26a` | 2025-06-25 |
| **`v1.3.0`** | 旧版 | `Interpreter` | `21`（Android 5 Lollipop） | `r26a` | 2025-05-19 |
| **`v1.2.0`** | 旧版 | `Interpreter` | `21`（Android 5 Lollipop） | `r26a` | 2025-03-13 |

**重要提示：** _保持依赖项更新以确保与最新功能和安全更新的兼容性。_

## `CompiledModel` API 快速入门

将 LiteRT Maven 包添加到你的 Android 项目：

```groovy
dependencies {
  ...
  implementation 'com.google.ai.edge.litert:litert:2.1.0'
}
```

使用 `CompiledModel` API 集成你的 `.tflite` 模型。以下代码片段展示了 Kotlin 和 C++ 的基本实现。

### Kotlin

```kotlin
// 加载模型并初始化运行时
val compiledModel = CompiledModel.create(
    "/path/to/mymodel.tflite",
    CompiledModel.Options(Accelerator.CPU))

// 预分配输入/输出缓冲区
val inputBuffers = compiledModel.createInputBuffers()
val outputBuffers = compiledModel.createOutputBuffers()

// 填充输入缓冲区
inputBuffers.get(0).writeFloat(input0)
inputBuffers.get(1).writeFloat(input1)

// 执行推理
compiledModel.run(inputBuffers, outputBuffers)

// 读取输出
val output = outputBuffers.get(0).readFloat()
```

### C++

```cpp
// 加载模型并初始化运行时
LITERT_ASSIGN_OR_RETURN(auto env, GetEnvironment());
LITERT_ASSIGN_OR_RETURN(auto options, GetOptions());
LITERT_ASSIGN_OR_RETURN(
    auto compiled_model,
    CompiledModel::Create(env, "/path/to/mymodel.tflite", options));

// 预分配输入/输出缓冲区
LITERT_ASSIGN_OR_RETURN(auto input_buffers, compiled_model.CreateInputBuffers(signature_index));
LITERT_ASSIGN_OR_RETURN(auto output_buffers, compiled_model.CreateOutputBuffers(signature_index));

// 填充输入缓冲区
LITERT_ABORT_IF_ERROR(input_buffers[0].Write(input0));
LITERT_ABORT_IF_ERROR(input_buffers[1].Write(input1));

// 执行推理
LITERT_ABORT_IF_ERROR(compiled_model.Run(signature_index, input_buffers, output_buffers));

// 读取输出
LITERT_ABORT_IF_ERROR(output_buffers[0].Read(output0));
```
