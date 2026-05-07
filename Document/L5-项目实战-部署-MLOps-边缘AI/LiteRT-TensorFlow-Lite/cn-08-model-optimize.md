# 模型优化

> 来源：https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/model_optimization

边缘设备通常内存或计算能力有限。可以对模型应用各种优化，以便在这些约束条件下运行。此外，一些优化允许使用专用硬件进行加速推理。

LiteRT 和 [TensorFlow 模型优化工具包](https://www.tensorflow.org/model_optimization)提供了最小化优化推理复杂性的工具。

建议你在应用开发过程中考虑模型优化。本文档概述了一些优化 TensorFlow 模型以部署到边缘硬件的最佳实践。

## 为什么要优化模型

模型优化可以通过几种主要方式帮助应用开发。

### 减小大小

某些形式的优化可用于减小模型的大小。较小的模型有以下好处：

- **更小的存储大小**：较小的模型在用户设备上占用更少的存储空间。例如，使用较小模型的 Android 应用在用户的移动设备上占用更少的存储空间。
- **更小的下载大小**：较小的模型下载到用户设备需要更少的时间和带宽。
- **更少的内存使用**：较小的模型在运行时使用更少的 RAM，这为应用的其他部分释放了内存，可以转化为更好的性能和稳定性。

量化（Quantization）可以在所有这些情况下减小模型大小，但可能会牺牲一些精度。剪枝（Pruning）和聚类（Clustering）可以通过使模型更容易压缩来减小下载大小。

### 降低延迟

_延迟_是使用给定模型运行单次推理所需的时间量。某些形式的优化可以减少使用模型运行推理所需的计算量，从而降低延迟。延迟也会影响功耗。

目前，量化可以通过简化推理期间发生的计算来降低延迟，但可能会牺牲一些精度。

### 加速器兼容性

某些硬件加速器（如 [Edge TPU](https://cloud.google.com/edge-tpu/)）可以使用正确优化的模型极快地运行推理。

通常，这些类型的设备要求模型以特定方式量化。请参阅每个硬件加速器的文档以了解更多关于其要求的信息。

## 权衡

优化可能会导致模型精度变化，这必须在应用开发过程中加以考虑。

精度变化取决于被优化的单个模型，很难提前预测。通常，针对大小或优化的模型会损失少量精度。根据你的应用，这可能会影响也可能不会影响用户体验。在极少数情况下，某些模型可能因优化过程而获得一些精度。

## 优化类型

LiteRT 目前支持通过量化、剪枝和聚类进行优化。

这些是 [TensorFlow 模型优化工具包](https://www.tensorflow.org/model_optimization)的一部分，该工具包提供了与 TensorFlow Lite 兼容的模型优化技术的资源。

### 量化（Quantization）

[量化](https://www.tensorflow.org/model_optimization/guide/quantization/post_training)通过降低用于表示模型参数的数值精度来工作，默认情况下这些参数是 32 位浮点数。这导致更小的模型大小和更快的计算。

LiteRT 中提供以下类型的量化：

| 技术 | 数据要求 | 大小减少 | 精度影响 | 支持的硬件 |
|---|---|---|---|---|
| [训练后 float16 量化](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/post_training_float16_quant.ipynb) | 无数据 | 最多 50% | 精度损失可忽略 | CPU, GPU |
| [训练后动态范围量化](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/post_training_quant.ipynb) | 无数据 | 最多 75% | 最小精度损失 | CPU, GPU (Android) |
| [训练后整数量化](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/post_training_integer_quant.ipynb) | 无标签代表性样本 | 最多 75% | 小精度损失 | CPU, GPU (Android), EdgeTPU |
| [量化感知训练](http://www.tensorflow.org/model_optimization/guide/quantization/training) | 有标签训练数据 | 最多 75% | 最小精度损失 | CPU, GPU (Android), EdgeTPU |

以下决策树帮助你根据预期模型大小和精度选择量化方案。

以下是训练后量化和量化感知训练在几个模型上的延迟和精度结果。所有延迟数据均在 Pixel 2 设备上使用单个大核 CPU 测量：

| 模型 | Top-1 精度（原始） | Top-1 精度（训练后量化） | Top-1 精度（量化感知训练） | 延迟（原始）(ms) | 延迟（训练后量化）(ms) | 延迟（量化感知训练）(ms) | 大小（原始）(MB) | 大小（优化后）(MB) |
|---|---|---|---|---|---|---|---|---|
| Mobilenet-v1-1-224 | 0.709 | 0.657 | 0.70 | 124 | 112 | 64 | 16.9 | 4.3 |
| Mobilenet-v2-1-224 | 0.719 | 0.637 | 0.709 | 89 | 98 | 54 | 14 | 3.6 |
| Inception_v3 | 0.78 | 0.772 | 0.775 | 1130 | 845 | 543 | 95.7 | 23.9 |
| Resnet_v2_101 | 0.770 | 0.768 | N/A | 3973 | 2868 | N/A | 178.3 | 44.9 |

**表 1** 选定 CNN 模型的模型量化优势

### 使用 int16 激活和 int8 权重的全整数量化

[使用 int16 激活的量化](https://www.tensorflow.org/model_optimization/guide/quantization/post_training)是一种全整数量化方案，激活使用 int16，权重使用 int8。与激活和权重都使用 int8 的全整数量化方案相比，此模式可以提高量化模型的精度，同时保持相似的模型大小。当激活对量化敏感时推荐使用。

_注意：_ 目前 TFLite 中只有非优化的参考内核实现可用于此量化方案，因此默认情况下性能将比 int8 内核慢。此模式的全部优势目前可以通过专用硬件或自定义软件访问。

以下是一些受益于此模式的模型的精度结果：

| 模型 | 精度指标类型 | 精度（float32 激活） | 精度（int8 激活） | 精度（int16 激活） |
|---|---|---|---|---|
| Wav2letter | WER | 6.7% | 7.7% | 7.2% |
| DeepSpeech 0.5.1 (unrolled) | CER | 6.13% | 43.67% | 6.52% |
| YoloV3 | mAP(IOU=0.5) | 0.577 | 0.563 | 0.574 |
| MobileNetV1 | Top-1 精度 | 0.7062 | 0.694 | 0.6936 |
| MobileNetV2 | Top-1 精度 | 0.718 | 0.7126 | 0.7137 |
| MobileBert | F1（精确匹配） | 88.81(81.23) | 2.08(0) | 88.73(81.15) |

**表 2** 使用 int16 激活的模型量化优势

### 剪枝（Pruning）

[剪枝](https://www.tensorflow.org/model_optimization/guide/pruning)通过移除模型中对其预测只有轻微影响的参数来工作。剪枝后的模型在磁盘上大小相同，运行时延迟相同，但可以更有效地压缩。这使得剪枝成为减小模型下载大小的有用技术。

未来，LiteRT 将为剪枝后的模型提供延迟降低。

### 聚类（Clustering）

[聚类](https://www.tensorflow.org/model_optimization/guide/clustering)通过将模型中每层的权重分组为预定义数量的簇，然后共享属于每个簇的权重的质心值来工作。这减少了模型中唯一权重值的数量，从而降低了其复杂性。

因此，聚类后的模型可以更有效地压缩，提供与剪枝类似的部署优势。

## 开发工作流

作为起点，检查[托管模型](https://ai.google.dev/edge/litert/conversion/tensorflow/pretrained_models.md)中的模型是否适合你的应用。如果不适合，我们建议用户从[训练后量化工具](/edge/litert/conversion/tensorflow/quantization/post_training_quantization)开始，因为这广泛适用且不需要训练数据。

对于精度和延迟目标未达到，或硬件加速器支持很重要的情况，[量化感知训练](https://www.tensorflow.org/model_optimization/guide/quantization/training)是更好的选择。请参阅 [TensorFlow 模型优化工具包](https://www.tensorflow.org/model_optimization)下的其他优化技术。

如果你想进一步减小模型大小，可以在量化模型之前尝试剪枝和/或聚类。
