# 模型导出技能地图

## 目标

学习者能将 PyTorch 模型导出为 ONNX 和 TorchScript 格式，能做基本的模型优化（量化、剪枝），理解端侧部署的完整流程。

## 必会概念

- ONNX（Open Neural Network Exchange）：跨框架模型交换格式
- TorchScript：PyTorch 的序列化格式（支持 C++ 加载）
- torch.jit.trace：通过运行一次记录模型结构
- torch.jit.script：通过分析源码编译模型
- 量化（Quantization）：浮点 → 整数，减小模型和加速推理
- 剪枝（Pruning）：移除不重要的权重
- dynamic_axes：ONNX 导出时的动态维度
- dummy_input：导出时需要的示例输入

## 必会 API

### ONNX 导出

| 函数 | 用途 | 关键参数 |
|------|------|---------|
| `torch.onnx.export(model, dummy, path)` | 导出 ONNX | input_names, output_names, dynamic_axes |

### TorchScript

| 函数 | 用途 | 关键参数 |
|------|------|---------|
| `torch.jit.trace(model, input)` | Trace 导出 | 需要示例输入 |
| `torch.jit.script(model)` | Script 导出 | 需要类型标注 |
| `torch.jit.save(scripted, path)` | 保存 | - |
| `torch.jit.load(path)` | 加载 | - |

### 量化

| 函数 | 用途 |
|------|------|
| `torch.quantization.quantize_dynamic(model, {nn.Linear}, dtype=torch.qint8)` | 动态量化 |

### 剪枝

| 函数 | 用途 |
|------|------|
| `torch.nn.utils.prune.l1_unstructured(module, 'weight', amount=0.3)` | L1 非结构化剪枝 |

## 代码片段

```python
import torch
import torch.onnx

# === ONNX 导出 ===
model = MyCNN()
model.eval()
dummy_input = torch.randn(1, 3, 32, 32)

torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={
        "input": {0: "batch_size"},
        "output": {0: "batch_size"}
    }
)

# 验证 ONNX
import onnxruntime as ort
import numpy as np

session = ort.InferenceSession("model.onnx")
onnx_input = dummy_input.numpy()
onnx_output = session.run(None, {"input": onnx_input})
pytorch_output = model(dummy_input).detach().numpy()

diff = np.abs(onnx_output[0] - pytorch_output).max()
print(f"Max diff: {diff}")  # 应该 < 1e-5
```

```python
# === TorchScript 导出 ===

# Trace（适合无分支的模型）
traced = torch.jit.trace(model, dummy_input)
torch.jit.save(traced, "model_traced.pt")

# Script（适合有分支的模型）
scripted = torch.jit.script(model)
torch.jit.save(scripted, "model_scripted.pt")
```

```python
# === 模型量化 ===
import torch.quantization

# 动态量化（最简单）
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear, torch.nn.Conv2d},
    dtype=torch.qint8
)

# 对比大小
def get_model_size(model, path):
    torch.save(model.state_dict(), path)
    import os
    size_mb = os.path.getsize(path) / 1024 / 1024
    return size_mb

print(f"原始: {get_model_size(model, 'orig.pth'):.2f} MB")
print(f"量化: {get_model_size(quantized_model, 'quant.pth'):.2f} MB")
```

```python
# === 模型剪枝 ===
import torch.nn.utils.prune as prune

# 对 Conv2d 层做 L1 非结构化剪枝
prune.l1_unstructured(model.conv1, name='weight', amount=0.3)

# 查看稀疏率
weight = model.conv1.weight
sparsity = 100. * float(torch.sum(weight == 0)) / float(weight.nelement())
print(f"Sparsity: {sparsity:.1f}%")
```

## 端侧部署流程图

```
PyTorch 模型
    ↓
[模型优化：剪枝、量化]
    ↓
ONNX 导出 (torch.onnx.export)
    ↓
ONNX Runtime 验证（PC 端确认正确性）
    ↓
[选择推理框架]
    ├── NCNN（移动端，ARM 优化）
    ├── MNN（阿里，移动端）
    ├── TFLite（Google，移动端）
    ├── TVM（通用编译优化）
    └── TensorRT（NVIDIA，GPU 部署）
    ↓
嵌入式设备部署
    ├── STM32 + CMSIS-NN（MCU 级）
    ├── TI + 深度学习加速器
    ├── 树莓派 + NCNN
    └── Jetson Nano + TensorRT
```

## 常见错误

1. 导出时模型不在 eval 模式（BN 用的是 running stats）
2. dummy_input 的 shape 不对
3. dynamic_axes 设置错误导致推理 shape 不匹配
4. ONNX 推理结果和 PyTorch 不一致（精度误差）
5. Trace 不能捕获 if/for 等控制流
6. Script 要求类型标注，Python 代码不规范会报错

## 训练阶梯

1. **ONNX 导出**：导出简单模型并用 Netron 可视化
2. **ONNX 验证**：用 ONNX Runtime 对比推理结果
3. **TorchScript**：分别用 trace 和 script 导出
4. **量化**：对比量化前后的模型大小和精度
5. **端到端**：训练 → 导出 → 验证 → 说明部署步骤

## 掌握标准

- 能正确导出 ONNX 并验证推理一致性
- 能区分 trace 和 script 的适用场景
- 能做动态量化并分析精度/大小变化
- 能画出完整的端侧部署流程图
- 能说出 PyTorch → 嵌入式部署需要的每一步
