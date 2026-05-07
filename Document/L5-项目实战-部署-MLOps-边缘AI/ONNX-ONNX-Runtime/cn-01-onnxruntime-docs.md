# 欢迎使用 ONNX Runtime

> 来源：https://onnxruntime.ai/docs/

ONNX Runtime 是一个跨平台的机器学习模型加速器，具有灵活的接口以集成特定硬件的库。ONNX Runtime 可与 PyTorch、TensorFlow/Keras、TFLite、scikit-learn 和其他框架的模型一起使用。

## 如何使用 ONNX Runtime

| [ORT 入门](./get-started) | [API 文档](./api) |
|---|---|
| [教程](./tutorials) | [生态系统](./ecosystem) |
| [ONNX Runtime YouTube](https://www.youtube.com/channel/UC_SJk17KdRvDulXz-nc1uFg/featured) | |

## 贡献和自定义

| [构建 ORT 包](./build) | [ONNX Runtime GitHub](https://github.com/microsoft/onnxruntime) |
|---|---|

* * *

## 快速入门模板

| [ORT Web JavaScript 站点模板](https://github.com/microsoft/onnxruntime-nextjs-template) | [ORT C# 控制台应用模板](https://github.com/microsoft/onnxruntime-csharp-cv-template) |
|---|---|

* * *

## ONNX Runtime for 推理（Inferencing）

ONNX Runtime 推理为 Microsoft 关键产品和服务（包括 Office、Azure、Bing）以及数十个社区项目中的机器学习模型提供动力。

ONNX Runtime 推理的示例用例包括：

- 提升各种 ML 模型的推理性能
- 在不同硬件和操作系统上运行
- 在 Python 中训练但部署到 C#/C++/Java 应用中
- 使用不同框架创建的模型进行训练和推理

### 工作原理

前提很简单。

1. **获取模型。** 可以从任何支持导出/转换为 ONNX 格式的框架训练。请参阅[教程](./tutorials)了解一些流行的框架/库。
2. **使用 ONNX Runtime 加载和运行模型。** 请参阅[基础教程](./tutorials/api-basics)了解如何用不同语言运行模型。
3. **_（可选）_ 使用各种运行时配置或硬件加速器调优性能。** 这里有很多选项——请参阅[性能部分](./performance)作为起点。

即使没有第 3 步，ONNX Runtime 通常也会比原始框架提供性能改进。

ONNX Runtime 在模型图上应用多种图优化，然后根据可用的特定硬件加速器将其划分为子图。核心 ONNX Runtime 中优化的计算内核提供性能改进，分配的子图受益于每个[执行提供者（Execution Provider）](./execution-providers)的进一步加速。

### 模型验证

你负责测试和验证使用 ONNX Runtime 的任何模型，包括其准确性、性能和对你预期用例的适用性。ONNX Runtime 将验证模型是否符合 [ONNX](https://onnx.ai/onnx/index.html) 规范。但是，可以构建恶意模型，例如不必要地消耗大量内存或计算资源。如果你使用来自不受信任来源的模型，我们建议在生产环境中使用之前检查模型并在安全环境中测试。

* * *

## ONNX Runtime for 训练（Training）

- [大模型训练](/docs/get-started/training-pytorch.html)
- [端侧训练](/docs/get-started/training-on-device.html)
