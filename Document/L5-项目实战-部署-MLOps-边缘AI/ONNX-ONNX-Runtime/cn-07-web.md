# 如何使用 ONNX Runtime 将机器学习添加到 Web 应用

> 来源：https://onnxruntime.ai/docs/tutorials/web/

ONNX Runtime Web 使你能够使用 JavaScript API 和库在 Web 应用中运行和部署机器学习模型。本页概述了开发过程的通用流程。

你也可以根据应用开发环境，使用其他语言库将机器学习集成到 Web 应用的服务端。

要查看 Web 开发流程的实践示例，可以按照以下教程中的步骤[使用 Next.js 构建图像分类 Web 应用](/docs/tutorials/web/classify-images-nextjs-github-template.html)。

有关以下步骤的更多详情，请参阅[使用 ONNX Runtime 构建 Web 应用](/docs/tutorials/web/build-web-app.html)参考指南。

## ONNX Runtime Web 应用开发流程

1. **选择部署目标和 ONNX Runtime 包**

   ONNX Runtime 可以根据你的应用需求以多种不同方式集成到 Web 应用中。

   - **浏览器中推理**：使用 `onnxruntime-web` 包。

   在设备端和浏览器中推理有以下好处：

     - **更快**：当推理直接在客户端进行时，对于针对较弱硬件优化的模型，可以大幅缩短推理时间。
     - **更安全**，有助于保护隐私：因为数据不会离开设备进行推理，这是一种更安全的推理方法。
     - **支持离线**：即使失去网络连接，模型仍然可以进行推理。
     - **更便宜**：通过将推理卸载到浏览器，可以降低云服务成本。

   你也可以在 Electron 应用的前端使用 onnxruntime-web 包。

   使用 onnxruntime-web，你可以选择使用 `webgl`、`webgpu` 或 `webnn`（`deviceType` 设为 `gpu`）进行 GPU 处理，以及使用 WebAssembly（`wasm`，即 `cpu` 的别名）或 `webnn`（`deviceType` 设为 `cpu`）进行 CPU 处理。所有 ONNX 操作符都受 WASM 支持，但目前只有子集受 WebGL、WebGPU 和 WebNN 支持。
