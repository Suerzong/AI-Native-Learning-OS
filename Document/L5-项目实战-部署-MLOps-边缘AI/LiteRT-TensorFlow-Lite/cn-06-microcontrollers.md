# LiteRT for Microcontrollers（微控制器）

> 来源：https://ai.google.dev/edge/litert/microcontrollers/overview

LiteRT for Microcontrollers 旨在微控制器和其他只有几千字节内存的设备上运行机器学习模型。核心运行时在 Arm Cortex M3 上仅需 16 KB 即可运行，可以运行许多基本模型。它不需要操作系统支持、任何标准 C 或 C++ 库或动态内存分配。

**注意：** [LiteRT for Microcontrollers 实验](https://experiments.withgoogle.com/collection/tfliteformicrocontrollers)展示了开发者将 Arduino 和 TensorFlow 结合创建出色体验和工具的作品。

## 为什么微控制器很重要

微控制器通常是小型、低功耗的计算设备，嵌入在需要基本计算的硬件中。通过将机器学习引入微型微控制器，我们可以提升我们在生活中使用的数十亿设备的智能，包括家用电器和物联网设备，而无需依赖昂贵的硬件或可靠的互联网连接（这通常受到带宽和功耗限制并导致高延迟）。这也有助于保护隐私，因为数据不会离开设备。想象一下能够适应你日常作息的智能家电、能够区分问题和正常运行的智能工业传感器，以及能够以有趣和愉快的方式帮助孩子们学习的神奇玩具。

## 支持的平台

LiteRT for Microcontrollers 使用 C++ 17 编写，需要 32 位平台。它已在许多基于 [Arm Cortex-M 系列](https://developer.arm.com/ip-products/processors/cortex-m)架构的处理器上进行了广泛测试，并已移植到其他架构，包括 [ESP32](https://www.espressif.com/en/products/hardware/esp32/overview)。该框架可作为 Arduino 库使用。它还可以为 Mbed 等开发环境生成项目。它是开源的，可以包含在任何 C++ 17 项目中。

支持以下开发板：

- [Arduino Nano 33 BLE Sense](https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense-with-headers)
- [SparkFun Edge](https://www.sparkfun.com/products/15170)
- [STM32F746 Discovery kit](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
- [Adafruit EdgeBadge](https://www.adafruit.com/product/4400)
- [Adafruit LiteRT for Microcontrollers Kit](https://www.adafruit.com/product/4317)
- [Adafruit Circuit Playground Bluefruit](https://learn.adafruit.com/tensorflow-lite-for-circuit-playground-bluefruit-quickstart?view=all)
- [Espressif ESP32-DevKitC](https://www.espressif.com/en/products/hardware/esp32-devkitc/overview)
- [Espressif ESP-EYE](https://www.espressif.com/en/products/hardware/esp-eye/overview)
- [Wio Terminal: ATSAMD51](https://www.seeedstudio.com/Wio-Terminal-p-4509.html)
- [Himax WE-I Plus EVB Endpoint AI Development Board](https://www.sparkfun.com/products/17256)
- [Synopsys DesignWare ARC EM Software Development Platform](https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform)
- [Sony Spresense](https://developer.sony.com/develop/spresense/)

## 探索示例

每个示例应用都在 [GitHub](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples) 上，并有一个 `README.md` 文件解释如何将其部署到支持的平台。一些示例还有使用特定平台的端到端教程：

- [Hello World](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/hello_world) — 展示使用 LiteRT for Microcontrollers 的绝对基础
  - [使用任何支持设备的教程](https://ai.google.dev/edge/litert/microcontrollers/get_started)
- [Micro Speech](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/micro_speech) — 使用麦克风捕获音频以检测 "yes" 和 "no" 词汇
  - [使用 SparkFun Edge 的教程](https://codelabs.developers.google.com/codelabs/sparkfun-tensorflow/#0)
- [Person Detection](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/person_detection) — 使用图像传感器捕获摄像头数据以检测是否有人存在

## 工作流

在微控制器上部署和运行 TensorFlow 模型需要以下步骤：

1. **训练模型**：
   - _生成一个小型 TensorFlow 模型_，适合你的目标设备并包含[支持的操作](https://ai.google.dev/edge/litert/microcontrollers/build_convert#operation_support)。
   - 使用 [LiteRT 转换器](https://ai.google.dev/edge/litert/microcontrollers/build_convert#model_conversion)转换为 LiteRT 模型。
   - 使用[标准工具](https://ai.google.dev/edge/litert/microcontrollers/build_convert#convert_to_a_c_array)转换为 C 字节数组，以将其存储在设备上的只读程序内存中。
2. **在设备上运行推理**：使用 [C++ 库](https://ai.google.dev/edge/litert/microcontrollers/library)并处理结果。

## 限制

LiteRT for Microcontrollers 是为微控制器开发的特定约束而设计的。如果你在更强大的设备上工作（例如，像 Raspberry Pi 这样的嵌入式 Linux 设备），标准的 LiteRT 框架可能更容易集成。

应考虑以下限制：

- 支持 TensorFlow 操作的[有限子集](https://ai.google.dev/edge/litert/microcontrollers/build_convert#operation_support)
- 支持有限的设备集合
- 低级 C++ API 需要手动内存管理
- 不支持设备上训练

## 下一步

- [微控制器入门](https://ai.google.dev/edge/litert/microcontrollers/get_started)尝试示例应用并学习如何使用 API。
- [了解 C++ 库](https://ai.google.dev/edge/litert/microcontrollers/library)学习如何在你自己的项目中使用该库。
- [构建和转换模型](https://ai.google.dev/edge/litert/microcontrollers/build_convert)了解更多关于在微控制器上训练和转换模型的知识。
