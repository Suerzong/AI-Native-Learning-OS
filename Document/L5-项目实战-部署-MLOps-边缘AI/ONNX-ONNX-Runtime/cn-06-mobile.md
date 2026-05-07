# 如何使用 ONNX Runtime 开发移动应用

> 来源：https://onnxruntime.ai/docs/tutorials/mobile/

ONNX Runtime 为你提供了多种将机器学习添加到移动应用中的选择。本页概述了开发过程的流程。你也可以查看本节中的教程：

- [在 iOS 上构建目标检测应用](/docs/tutorials/mobile/deploy-ios.html)
- [在 Android 上构建图像分类应用](/docs/tutorials/mobile/deploy-android.html)
- [在 iOS 上构建超分辨率应用](/docs/tutorials/mobile/superres.html#ios-app)
- [在 Android 上构建超分辨率应用](/docs/tutorials/mobile/superres.html#android-app)

## ONNX Runtime 移动应用开发流程

### 获取模型

开发移动机器学习应用的第一步是获取模型。

你需要了解你的移动应用场景并获取适合该场景的 ONNX 模型。例如，应用是否对图像进行分类、在视频流中进行目标检测、总结或预测文本，或进行数值预测。

要在 ONNX Runtime 移动端运行，模型需要为 ONNX 格式。ONNX 模型可从 [ONNX 模型库](https://github.com/onnx/models)获取。如果你的模型尚未为 ONNX 格式，可以使用转换器将其从 PyTorch、TensorFlow 和其他格式转换为 ONNX。

由于模型在设备上加载和运行，模型必须适合设备磁盘并能够加载到设备内存中。

### 开发应用

一旦有了模型，就可以使用 ONNX Runtime API 加载和运行它。

你使用的语言绑定和运行时包取决于你选择的开发环境和目标平台。

- Android Java/C/C++：onnxruntime-android 包
- iOS C/C++：onnxruntime-c 包
