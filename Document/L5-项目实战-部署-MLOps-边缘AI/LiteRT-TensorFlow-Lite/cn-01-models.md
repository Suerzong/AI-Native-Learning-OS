# TensorFlow 模型转换概述

> 来源：https://ai.google.dev/edge/litert/conversion/tensorflow/overview

你在 LiteRT 中使用的机器学习（ML）模型最初是使用 TensorFlow 核心库和工具构建和训练的。一旦你使用 TensorFlow 核心构建了模型，就可以将其转换为更小、更高效的 ML 模型格式，称为 LiteRT 模型。本节提供将 TensorFlow 模型转换为 LiteRT 模型格式的指导。

**注意：** 如果你还没有要转换的模型，请参阅[模型概述](https://ai.google.dev/edge/litert/conversion/tensorflow/pretrained_models)页面获取选择或构建模型的指导。

## 转换工作流

将 TensorFlow 模型转换为 LiteRT 格式可能有几种路径，取决于你的 ML 模型内容。作为该过程的第一步，你应该评估模型以确定它是否可以直接转换。此评估根据模型使用的 TensorFlow 操作（Operations）确定模型内容是否受标准 LiteRT 运行时环境支持。如果你的模型使用了支持集合之外的操作，你可以选择重构模型或使用高级转换技术。

下图显示了模型转换的高级步骤。

**图 1.** LiteRT 转换工作流。

以下各节概述了评估和转换模型以供 LiteRT 使用的过程。

### 输入模型格式

你可以将转换器与以下输入模型格式一起使用：

- [SavedModel](https://www.tensorflow.org/guide/saved_model)（**_推荐_**）：保存为磁盘上一组文件的 TensorFlow 模型。
- [Keras 模型](https://www.tensorflow.org/guide/keras/overview)：使用高级 Keras API 创建的模型。
- [Keras H5 格式](https://www.tensorflow.org/guide/keras/save_and_serialize#keras_h5_format)：Keras API 支持的 SavedModel 格式的轻量级替代方案。
- [从具体函数构建的模型](https://www.tensorflow.org/guide/intro_to_graphs)：使用低级 TensorFlow API 创建的模型。

你可以将 Keras 模型和具体函数模型都保存为 SavedModel，并使用推荐路径进行转换。

**注意：** 为避免推理过程中出现错误，在导出到 SavedModel 格式时请包含签名（Signatures）。TensorFlow 转换器支持将 TensorFlow 模型的输入/输出规范转换为 LiteRT 模型。请参阅[添加签名](https://ai.google.dev/edge/litert/conversion/tensorflow/signatures)主题。

如果你有 JAX 模型，可以使用 `TFLiteConverter.experimental_from_jax` API 将其转换为 LiteRT 格式。请注意，此 API 在实验模式下可能会发生变化。

### 转换评估

评估模型是尝试转换之前的重要步骤。评估时，你需要确定模型的内容是否与 LiteRT 格式兼容。你还应确定模型在移动和边缘设备上使用是否合适，包括模型使用的数据大小、硬件处理要求以及模型的整体大小和复杂性。

对于许多模型，转换器应该可以直接工作。但是，LiteRT 内置操作符库只支持 TensorFlow 核心操作符的子集，这意味着某些模型在转换为 LiteRT 之前可能需要额外的步骤。此外，LiteRT 支持的某些操作出于性能原因有使用限制。请参阅[操作符兼容性](https://ai.google.dev/edge/litert/conversion/tensorflow/ops_compatibility)指南以确定你的模型是否需要重构以进行转换。

**关键点：** 大多数模型可以直接转换为 LiteRT 格式。某些模型可能需要重构或使用高级转换技术以使其兼容。

### 模型转换

LiteRT 转换器接收 TensorFlow 模型并生成 LiteRT 模型（一种优化的 [FlatBuffer](https://google.github.io/flatbuffers/) 格式，以 `.tflite` 文件扩展名标识）。你可以加载 SavedModel 或直接转换在代码中创建的模型。

转换器接受 3 个主要标志（或选项）来自定义模型的转换：

1. [兼容性标志](https://ai.google.dev/edge/litert/conversion/tensorflow/ops_compatibility)允许你指定转换是否应允许自定义操作符。
2. [优化标志](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/model_optimization)允许你指定在转换期间应用的优化类型。最常用的优化技术是[训练后量化（Post-training Quantization）](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/post_training_quant)。
3. [元数据标志](https://ai.google.dev/edge/litert/conversion/tensorflow/metadata)允许你向转换后的模型添加元数据，这使得在设备上部署模型时更容易创建特定于平台的包装代码。

你可以使用 [Python API](https://ai.google.dev/edge/litert/conversion/tensorflow/convert_tf#python_api) 或[命令行](https://ai.google.dev/edge/litert/conversion/tensorflow/convert_tf#cmdline)工具转换模型。请参阅[转换 TF 模型](https://ai.google.dev/edge/litert/conversion/tensorflow/convert_tf)指南获取在模型上运行转换器的分步说明。

通常你会为标准 LiteRT [运行时环境](https://ai.google.dev/edge/litert/android/index#runtime)或 LiteRT 的 [Google Play 服务运行时环境](https://ai.google.dev/edge/litert/android/play_services)（Beta）转换模型。一些高级用例需要自定义模型运行时环境，这需要在转换过程中执行额外步骤。请参阅 Android 概述的[高级运行时环境](https://ai.google.dev/edge/litert/android#adv_runtime)部分获取更多指导。

## 高级转换

如果在模型上运行转换器时遇到[错误](https://ai.google.dev/edge/litert/conversion/tensorflow/convert_tf#conversion_errors)，很可能是操作符兼容性问题。并非所有 TensorFlow 操作都受 TensorFlow Lite 支持。你可以通过重构模型或使用高级转换选项来解决这些问题，这些选项允许你创建修改后的 LiteRT 格式模型和该模型的自定义运行时环境。

- 有关 TensorFlow 和 LiteRT 模型兼容性考虑的更多信息，请参阅[模型兼容性概述](https://ai.google.dev/edge/litert/conversion/tensorflow/ops_compatibility)。
- 模型兼容性概述下的主题涵盖了重构模型的高级技术，例如[选择操作符](https://ai.google.dev/edge/litert/conversion/tensorflow/ops_select)指南。
- 有关操作和限制的完整列表，请参阅 [LiteRT Ops 页面](https://www.tensorflow.org/mlir/tfl_ops)。

## 下一步

- 参阅[转换 TF 模型](https://ai.google.dev/edge/litert/conversion/tensorflow/convert_tf)指南快速开始转换模型。
- 参阅[优化概述](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/model_optimization)了解如何使用[训练后量化](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/post_training_quantization)等技术优化转换后的模型。
- 参阅[添加元数据概述](https://ai.google.dev/edge/litert/conversion/tensorflow/metadata)了解如何向模型添加元数据。元数据为其他用户提供模型描述以及代码生成器可以利用的信息。
