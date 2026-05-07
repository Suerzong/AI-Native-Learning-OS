# ONNX Runtime 执行提供者（Execution Providers）

> 来源：https://onnxruntime.ai/docs/execution-providers/

ONNX Runtime 通过其可扩展的**执行提供者（Execution Providers, EP）**框架与不同的硬件加速库协作，以在硬件平台上优化执行 ONNX 模型。该接口为应用开发者提供了灵活性，使其能够在云和边缘的不同环境中部署 ONNX 模型，并通过利用平台的计算能力来优化执行。

ONNX Runtime 使用 `GetCapability()` 接口与执行提供者协作，将特定节点或子图分配给 EP 库在支持的硬件上执行。预安装在执行环境中的 EP 库处理并在硬件上执行 ONNX 子图。这种架构抽象了硬件特定库的细节，这些库对于在 CPU、GPU、FPGA 或专用 NPU 等硬件平台上优化深度神经网络的执行至关重要。

ONNX Runtime 目前支持许多不同的执行提供者。一些 EP 已在生产环境中用于实时服务，而另一些则以预览版发布，使开发者能够使用不同选项开发和自定义其应用。

## 支持的执行提供者概览

| CPU | GPU | IoT/边缘/移动端 | 其他 |
|---|---|---|---|
| 默认 CPU | [NVIDIA CUDA](/docs/execution-providers/CUDA-ExecutionProvider.html) | [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [Rockchip NPU](/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html)（预览） |
| [Intel DNNL](/docs/execution-providers/oneDNN-ExecutionProvider.html) | [NVIDIA TensorRT](/docs/execution-providers/TensorRT-ExecutionProvider.html) | [Arm Compute Library](/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html)（预览） | [Xilinx Vitis-AI](/docs/execution-providers/Vitis-AI-ExecutionProvider.html)（预览） |
| [TVM](/docs/execution-providers/community-maintained/TVM-ExecutionProvider.html)（预览） | [DirectML](/docs/execution-providers/DirectML-ExecutionProvider.html) | [Android NNAPI](/docs/execution-providers/NNAPI-ExecutionProvider.html) | [Huawei CANN](/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html)（预览） |
| [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [AMD MIGraphX](/docs/execution-providers/MIGraphX-ExecutionProvider.html) | [Arm NN](/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html)（预览） | [AZURE](/docs/execution-providers/Azure-ExecutionProvider.html)（预览） |
| [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html) | [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [CoreML](/docs/execution-providers/CoreML-ExecutionProvider.html)（预览） | |
| [AMD ROCm](/docs/execution-providers/ROCm-ExecutionProvider.html)（已弃用） | [Qualcomm QNN](/docs/execution-providers/QNN-ExecutionProvider.html) | [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html) | |

## 添加执行提供者

专门的硬件加速解决方案开发者可以与 ONNX Runtime 集成，在其技术栈上执行 ONNX 模型。要创建与 ONNX Runtime 接口的 EP，你必须首先为 EP 确定一个唯一名称。参见：[添加新的执行提供者](/docs/execution-providers/add-execution-provider.html)获取详细说明。

## 使用 EP 构建 ONNX Runtime 包

ONNX Runtime 包可以使用任何 EP 组合以及默认 CPU 执行提供者构建。**注意**：如果多个 EP 组合到同一个 ONNX Runtime 包中，则所有依赖库必须存在于执行环境中。构建包含不同 EP 的 ONNX Runtime 包的步骤记录在[此处](/docs/build/inferencing.html)。

## 执行提供者 API

所有 EP 使用相同的 ONNX Runtime API。这为应用提供了在不同硬件加速平台上运行的一致接口。设置 EP 选项的 API 在 Python、C/C++/C#、Java 和 Node.js 中均可用。

```python
get_providers: 返回已注册的执行提供者列表。
get_provider_options: 返回已注册的执行提供者的配置。
set_providers: 注册给定的执行提供者列表。底层会话将被重新创建。
    提供者列表按优先级排序。例如 ['CUDAExecutionProvider', 'CPUExecutionProvider']
    表示如果支持则使用 CUDAExecutionProvider 执行节点，否则使用 CPUExecutionProvider 执行。
```
