# ONNX：开放神经网络交换格式

> 来源：https://onnx.ai ，Apache 2.0 协议。当前版本 ONNX 1.22.0

---

## 1. 什么是 ONNX

**ONNX（Open Neural Network Exchange）** 是一种开放的机器学习模型交换格式。它定义了一套标准的 **计算图表示**，使模型可以在不同框架之间移植和部署。

### 核心价值

```
  PyTorch ──┐
            │
TensorFlow ─┼──→ ONNX 格式 ──→ ONNX Runtime / TFLite / TensorRT / ...
            │
  JAX ──────┘
```

- **框架无关**：一次导出，多处部署
- **硬件无关**：同一个 ONNX 模型可运行在 CPU / GPU / NPU / FPGA
- **生态广泛**：被 PyTorch、TensorFlow、scikit-learn、MXNet、PaddlePaddle 等主流框架支持

---

## 2. ONNX 核心概念

### 2.1 模型结构

一个 ONNX 模型包含：

```
Model
  ├── Graph
  │     ├── Node（算子节点，如 Conv, Relu, MatMul）
  │     ├── Tensor（数据张量：输入/输出/中间结果）
  │     └── Initializer（权重/偏置等静态值）
  ├── Operator Sets（算子集版本）
  └── Metadata（输入输出名称、维度信息）
```

### 2.2 关键术语

| 术语 | 含义 |
|---|---|
| **Model** | 完整的 ML 模型，包含一个主 Graph 和元数据 |
| **Graph** | 有向无环图（DAG），描述数据如何流过算子 |
| **Node** | 图中的一个算子操作（如 Conv, Relu, Add） |
| **Tensor** | 多维数组，通过边（edge）连接节点 |
| **Operator** | 节点执行的具体运算（卷积、激活、矩阵乘法等） |
| **Initializer** | 预训练权重/偏置，在推理时不变 |
| **Shape** | 张量的维度信息 |
| **Opset** | 算子集版本号，控制可用算子集合 |

### 2.3 ONNX 的文件格式

ONNX 模型使用 Protocol Buffers（protobuf）序列化为 `.onnx` 文件。

---

## 3. 支持的框架

| 框架 | 导出方式 | 说明 |
|---|---|---|
| **PyTorch** | `torch.onnx.export()` | 原生支持，最常用 |
| **TensorFlow / Keras** | `tf2onnx` 工具 | 第三方转换 |
| **scikit-learn** | `skl2onnx` | 传统 ML 模型也能转 |
| **JAX** | `jax2onnx` | 实验性支持 |
| **PaddlePaddle** | `paddle.onnx.export()` | 国内主流 |
| **MXNet** | 原生 | 历史支持 |
| **XGBoost / LightGBM** | `hummingbird` 或转换工具 | 树模型转神经网络 |
| **Core ML（Apple）** | `coremltools` → ONNX | 双向转换 |

---

## 4. ONNX Runtime 概述

**ONNX Runtime（ORT）** 是微软主导的高性能跨平台推理引擎，专门为运行 ONNX 模型优化。

### 4.1 特点

| 特性 | 说明 |
|---|---|
| **跨平台** | Linux / Windows / macOS / Android / iOS / Web |
| **跨语言** | Python / C++ / C# / Java / JavaScript / Rust / Objective-C / Swift |
| **多硬件后端** | CPU / CUDA / TensorRT / OpenVINO / DirectML / CoreML / QNN / ROCm / XNNPACK |
| **图优化** | 算子融合、常量折叠、冗余消除 |
| **量化支持** | INT8 / INT4 量化（PTQ + QAT） |
| **模型格式** | 支持直接运行 PyTorch 和 TF 模型（除 ONNX 格式外） |

### 4.2 Execution Providers（执行后端）

| EP | 硬件 | 适用场景 |
|---|---|---|
| **CPU (Default)** | x86 / ARM CPU | 通用场景 |
| **CUDA** | NVIDIA GPU | 云端/PC 加速推理 |
| **TensorRT** | NVIDIA GPU | 极致 GPU 加速 |
| **OpenVINO** | Intel CPU/GPU/VPU | Intel 芯片优化 |
| **DirectML** | Windows GPU | Windows 桌面应用 |
| **CoreML** | Apple Neural Engine | iOS / macOS |
| **QNN** | Qualcomm DSP | 安卓手机端 |
| **NNAPI** | Android SoC | 安卓手机端 |
| **XNNPACK** | 多 CPU 架构 | 移动端/嵌入式 CPU |
| **ROCm** | AMD GPU | AMD 硬件 |
| **ACL (Arm Compute Library)** | ARM CPU | 嵌入式 Linux |

### 4.3 安装

```bash
# CPU 版
pip install onnxruntime

# GPU 版（CUDA）
pip install onnxruntime-gpu

# 移动端
# Android: org.pytorch:pytorch_android 或独立编译
# iOS: 通过 CocoaPods 或 Swift Package
```

---

## 5. ONNX 模型导出工作流（以 PyTorch 为例）

```python
import torch
import torch.onnx

# 1. 定义/加载模型
model = YourModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()  # 必须设为 eval 模式

# 2. 准备示例输入（决定图结构和维度）
dummy_input = torch.randn(1, 3, 224, 224)

# 3. 导出
torch.onnx.export(
    model,
    dummy_input,          # 示例输入
    "model.onnx",         # 输出文件名
    export_params=True,   # 存储训练好的权重
    opset_version=17,     # 算子集版本（推荐 17）
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={        # 动态维度配置
        "input": {0: "batch_size"},
        "output": {0: "batch_size"}
    }
)
```

### 5.1 验证导出结果

```python
import onnx

# 检查模型是否合法
onnx_model = onnx.load("model.onnx")
onnx.checker.check_model(onnx_model)

# 可视化（需安装 netron）
import netron
netron.start("model.onnx")
```

### 5.2 opset_version 选择指南

| Opset | 关键特性 |
|---|---|
| 13 | 基础算子集，广泛兼容 |
| 14-16 | 改进的循环/条件算子 |
| **17**（推荐）| 较新，PyTorch 1.13+ 默认 |
| 18+ | 最新功能，兼容性可能受限 |

选太低 → 模型导出失败（新算子不支持）
选太高 → 部署端 Runtime 可能不支持

---

## 6. ONNX Runtime 推理

```python
import onnxruntime as ort
import numpy as np

# 1. 创建推理会话
session = ort.InferenceSession("model.onnx")

# 2. 查看输入输出信息
for inp in session.get_inputs():
    print(f"Input: {inp.name}, shape: {inp.shape}")

for out in session.get_outputs():
    print(f"Output: {out.name}, shape: {out.shape}")

# 3. 准备数据
input_data = np.random.randn(1, 3, 224, 224).astype(np.float32)

# 4. 推理
outputs = session.run(None, {"input": input_data})

# 5. 获取结果
result = outputs[0]
```

### 指定 Execution Provider

```python
# CPU
session = ort.InferenceSession("model.onnx",
    providers=["CPUExecutionProvider"])

# CUDA GPU
session = ort.InferenceSession("model.onnx",
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

# TensorRT（需要编译对应版本）
session = ort.InferenceSession("model.onnx",
    providers=["TensorrtExecutionProvider", "CUDAExecutionProvider"])
```

---

## 7. ONNX 量化

### 7.1 静态量化（需要校准数据）

```python
from onnxruntime.quantization import quantize_static, QuantType

# 校准数据读取器
def calibration_data_reader():
    for _ in range(100):
        yield {"input": np.random.randn(1, 3, 224, 224).astype(np.float32)}

quantize_static(
    model_input="model.onnx",
    model_output="model_int8.onnx",
    calibration_data_reader=calibration_data_reader,
    quant_format=QuantType.QInt8,   # 或 QInt8
    weight_type=QuantType.QInt8,
)
```

### 7.2 动态量化（无需校准数据）

```python
from onnxruntime.quantization import quantize_dynamic, QuantType

quantize_dynamic(
    model_input="model.onnx",
    model_output="model_int8_dynamic.onnx",
    weight_type=QuantType.QInt8,
)
```

### 7.3 Float16 量化

```python
from onnxruntime.transformers import float16

model = onnx.load("model.onnx")
model_fp16 = float16.convert_float_to_float16(model)
onnx.save(model_fp16, "model_fp16.onnx")
```

---

## 8. ONNX Runtime 图优化

```python
session_options = ort.SessionOptions()

# 图优化级别
session_options.graph_optimization_level = (
    ort.GraphOptimizationLevel.ORT_ENABLE_ALL
)

# 启用内存优化
session_options.enable_mem_pattern = True
session_options.enable_cpu_mem_arena = True

session = ort.InferenceSession("model.onnx", session_options)
```

优化级别说明：

| 级别 | 说明 |
|---|---|
| ORT_DISABLE_ALL | 不做任何优化 |
| ORT_ENABLE_BASIC | 基本优化：常量折叠、冗余消除 |
| ORT_ENABLE_EXTENDED | 扩展优化：算子融合 |
| ORT_ENABLE_ALL | 全部优化（推荐） |

---

## 9. 常用工具

| 工具 | 用途 |
|---|---|
| [netron](https://netron.app) | 可视化 ONNX 计算图（Web / 桌面版） |
| `onnx.checker.check_model()` | 检查模型合法性 |
| `onnx.helper` | 编程方式构建 ONNX 图 |
| `onnxsim` | 简化/优化 ONNX 图（pip install onnxsim） |
| `onnx2torch` | ONNX → PyTorch 反向转换 |

```bash
# 安装
pip install onnx onnxruntime netron onnxsim
```

---

## 10. 与 TFLite 的对比

| 维度 | ONNX | TFLite |
|---|---|---|
| 生态 | 全框架通用 | TensorFlow 生态为主 |
| 微控制器 | 不直接支持 MCU | TFLite Micro 原生支持 MCU |
| 硬件后端 | 多 EP（CUDA/TensorRT/CoreML/QNN...） | 多 Delegate（GPU/NNAPI/Hexagon...） |
| 文件格式 | Protocol Buffers (.onnx) | FlatBuffers (.tflite) |
| 移动端 | 支持（Android/iOS 包） | 官方一流支持 |
| 服务器端 | ONNX Runtime 为服务器优化 | 不是主要使用场景 |
| 典型用途 | 训练框架→通用部署 | TF→移动端/嵌入式部署 |

> **Edge AI 实践中常见路径**：PyTorch 训练 → ONNX 中间格式 → TFLite（如果需要 MCU）或直接 ONNX Runtime 部署
