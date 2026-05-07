# 在 IoT 和边缘设备上部署 ML 模型

> 来源：https://onnxruntime.ai/docs/tutorials/iot-edge/

ONNX Runtime 允许你部署到许多 IoT 和边缘设备，以支持各种用例。有可用的包支持多种板卡架构[安装 ONNX Runtime 时包含](https://pypi.org/project/onnxruntime/#files)。以下是决定在设备上部署是否适合你的用例时的一些考虑因素。

## 在设备上进行推理的好处和限制

- **更快**：没错，当推理直接在客户端进行时，对于针对较弱硬件优化的模型，可以缩短推理时间。
- **更安全**，有助于保护隐私：因为数据不会离开设备进行推理，这是一种更安全的推理方法。
- **支持离线**：即使失去网络连接，模型仍然可以进行推理。
- **更便宜**：通过将推理卸载到设备，可以降低云服务成本。
- **模型大小限制**：如果要在设备上部署，你需要一个经过优化且足够小的模型以在设备上运行。
- **硬件处理限制**：模型需要针对较弱的硬件进行优化。

## 示例

- [Raspberry Pi 设备端推理](/docs/tutorials/iot-edge/rasp-pi-cv.html)
- [Jetson Nano 嵌入式设备：快速模型推理](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-arm64.md)
- [使用 OpenVINO 的 Intel VPU 边缘设备：部署小型量化模型](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-OpenVINO.md)

## 目录

- [在 Raspberry Pi 上进行 IoT 部署](/docs/tutorials/iot-edge/rasp-pi-cv.html)
