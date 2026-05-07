# 性能最佳实践

> 来源：https://ai.google.dev/edge/litert/conversion/tensorflow/build/best_practices

移动和嵌入式设备的计算资源有限，因此保持应用的资源效率非常重要。我们整理了一系列最佳实践和策略，可用于提升 TensorFlow Lite 模型的性能。

## 为任务选择最佳模型

根据任务的不同，你需要在模型复杂性和大小之间进行权衡。如果你的任务需要高精度，那么你可能需要一个大型且复杂的模型。对于精度要求较低的任务，最好使用较小的模型，因为它们不仅占用更少的磁盘空间和内存，而且通常更快且更节能。例如，下图展示了一些常见图像分类模型的精度和延迟权衡。

针对移动设备优化的模型示例是 [MobileNets](https://arxiv.org/abs/1704.04861)，它们针对移动视觉应用进行了优化。[Kaggle Models](https://www.kaggle.com/models?framework=tfLite) 列出了其他几种专门针对移动和嵌入式设备优化的模型。

你可以使用迁移学习在自己的数据集上重新训练列出的模型。

## 对模型进行性能分析

一旦选择了适合任务的候选模型，对模型进行性能分析和基准测试是一个好习惯。LiteRT [基准测试工具](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark)有一个内置的分析器，显示每个操作符的性能分析统计信息。这有助于理解性能瓶颈以及哪些操作符占据了大部分计算时间。

你还可以使用 [LiteRT 追踪](https://ai.google.dev/edge/litert/models/measurement#trace_tensorflow_lite_internals_in_android)在 Android 应用中分析模型，使用标准的 Android 系统追踪，并通过基于 GUI 的性能分析工具按时间可视化操作符调用。

## 分析和优化图中的操作符

如果某个特定操作符在模型中频繁出现，并且根据性能分析你发现该操作符消耗了最多的时间，你可以考虑优化该操作符。这种情况应该很少见，因为 TensorFlow Lite 已经为大多数操作符提供了优化版本。但是，如果你知道操作符执行的约束条件，你可能能够编写自定义操作符的更快版本。查看[自定义操作符指南](https://ai.google.dev/edge/litert/conversion/tensorflow/ops_custom)。

## 优化你的模型

模型优化旨在创建更小的模型，这些模型通常更快、更节能，以便它们可以部署在移动设备上。LiteRT 支持多种优化技术，如量化（Quantization）。

查看[模型优化文档](https://ai.google.dev/edge/litert/conversion/tensorflow/quantization/model_optimization)了解详情。

## 调整线程数量

LiteRT 支持许多操作符的多线程内核。你可以增加线程数并加速操作符的执行。然而，增加线程数会使模型使用更多的资源和电量。

对于某些应用，延迟可能比能源效率更重要。你可以通过设置解释器的[线程数](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L346)来增加线程数。然而，多线程执行的代价是增加的性能变异性，取决于同时执行的其他内容。对于移动应用尤其如此。例如，隔离测试可能显示比单线程快 2 倍，但如果另一个应用同时执行，可能会导致性能比单线程更差。

## 消除冗余拷贝

如果你的应用没有精心设计，在将输入馈送给模型和从模型读取输出时可能会有冗余拷贝。确保消除冗余拷贝。如果你使用更高级的 API（如 Java），请务必仔细检查文档中关于性能的注意事项。例如，如果使用 `ByteBuffers` 作为[输入](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/java/src/main/java/org/tensorflow/lite/Interpreter.java#L175)，Java API 会快得多。

## 使用平台特定工具分析你的应用

平台特定工具（如 [Android Profiler](https://developer.android.com/studio/profile/android-profiler) 和 [Instruments](https://help.apple.com/instruments/mac/current/)）提供了丰富的性能分析信息，可用于调试你的应用。有时性能问题可能不在模型中，而在与模型交互的应用代码部分。确保熟悉你所用平台的特定性能分析工具和最佳实践。

## 评估模型是否受益于设备上的硬件加速器

LiteRT 增加了使用更快硬件（如 GPU、DSP 和神经加速器）加速模型的新方法。通常，这些加速器通过[委托（Delegate）](https://ai.google.dev/edge/litert/performance/delegates)子模块暴露，接管部分解释器执行。LiteRT 可以通过以下方式使用委托：

- GPU 委托在 Android 和 iOS 上可用，分别使用 OpenGL/OpenCL 和 Metal。要试用它们，请参阅 [GPU 委托](https://ai.google.dev/edge/litert/performance/gpu)。
- 如果你可以访问非标准硬件，可以创建自己的委托。更多信息请参阅 [LiteRT 委托](https://ai.google.dev/edge/litert/performance/delegates)。

请注意，某些加速器对不同类型的模型效果更好。某些委托只支持浮点模型或以特定方式优化的模型。重要的是要对每个委托进行[基准测试](https://ai.google.dev/edge/litert/models/measurement)，看它是否是你的应用的好选择。例如，如果你的模型非常小，将模型委托给 GPU 可能不值得。相反，对于具有高算术强度的大型模型，加速器是很好的选择。
