# PyTorch → ONNX 导出与量化

> 来源：https://pytorch.org/docs/stable/onnx.html ，BSD 协议

---

## 1. torch.onnx.export 概览

`torch.onnx.export()` 是 PyTorch 原生的 ONNX 模型导出函数。它通过 **Tracing（追踪）** 方式，将 PyTorch 模型的计算图导出为 ONNX 格式。

### 基本签名

```python
torch.onnx.export(
    model,          # torch.nn.Module
    args,           # 示例输入（tuple 或 Tensor）
    f,              # 输出文件名 或 文件对象
    export_params=True,    # 是否保存模型参数（权重）
    verbose=False,         # 是否输出详细调试信息
    training=TrainingMode.EVAL,  # 导出模式
    input_names=[],        # 输入节点名称
    output_names=[],       # 输出节点名称
    operator_export_type=OperatorExportTypes.ONNX,
    opset_version=None,    # 算子集版本
    do_constant_folding=True,      # 是否做常量折叠优化
    dynamic_axes=None,     # 动态维度配置
    keep_initializers_as_inputs=None,
    custom_opsets=None,    # 自定义算子集
    export_modules_as_functions=False,
)
```

---

## 2. 基础导出步骤

### 2.1 最简单的例子

```python
import torch
import torch.nn as nn
import torch.onnx

# 1. 定义模型
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 16, 3, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(16, 10)

    def forward(self, x):
        x = self.relu(self.conv(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

model = SimpleModel()
model.eval()  # 必须！

# 2. 创建示例输入（shape 必须与实际输入一致）
dummy_input = torch.randn(1, 3, 224, 224)

# 3. 导出
torch.onnx.export(
    model,
    dummy_input,
    "simple_model.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=17,
)
```

### 2.2 验证导出

```python
import onnx
import onnxruntime as ort
import numpy as np

# 结构验证
onnx_model = onnx.load("simple_model.onnx")
onnx.checker.check_model(onnx_model)
print("ONNX model is valid!")

# 推理验证：确保 PyTorch 和 ONNX Runtime 输出一致
with torch.no_grad():
    torch_out = model(dummy_input)

session = ort.InferenceSession("simple_model.onnx")
onnx_out = session.run(None, {"input": dummy_input.numpy()})

np.testing.assert_allclose(torch_out.numpy(), onnx_out[0], rtol=1e-3, atol=1e-5)
print("Outputs match!")
```

---

## 3. 关键参数详解

### 3.1 opset_version（算子集版本）

```python
# 推荐值
torch.onnx.export(model, dummy_input, "model.onnx", opset_version=17)
```

| Opset | PyTorch 最低版本 | 推荐场景 |
|---|---|---|
| 13 | 1.8+ | 最大兼容性 |
| 14 | 1.9+ | 改进的循环算子 |
| 15 | 1.10+ | 新型激活函数 |
| 16 | 1.12+ | 改进的 scatter/gather |
| **17** | 1.13+ | **推荐：当前默认** |
| 18+ | 2.0+ | 新算子，兼容性下降 |

> **原则**：选能被目标 ONNX Runtime 版本支持的最高 opset。

### 3.2 dynamic_axes（动态维度）

```python
# 允许变长 batch + 变长序列
torch.onnx.export(
    model, dummy_input, "model.onnx",
    dynamic_axes={
        "input": {0: "batch_size", 2: "seq_len"},
        "output": {0: "batch_size"},
    }
)
```

作用：
- 导出后可接受不同 batch size 的输入
- 对 NLP 模型：允许不同长度的序列
- 不设置则**固定维度**，推理时必须完全匹配

### 3.3 多输入/多输出模型

```python
class MultiIOModel(nn.Module):
    def forward(self, x, mask):
        return x * mask, x.sum(dim=1)

model = MultiIOModel()
model.eval()

x = torch.randn(2, 3, 224, 224)
mask = torch.ones(2, 1, 1, 1)

torch.onnx.export(
    model,
    (x, mask),  # tuple of inputs
    "multi_io_model.onnx",
    input_names=["input", "mask"],
    output_names=["masked_output", "sum_output"],
    opset_version=17,
)
```

### 3.4 training 模式

```python
from torch.onnx import TrainingMode

# EVAL 模式（默认，推荐用于推理部署）
torch.onnx.export(model, args, "model.onnx", training=TrainingMode.EVAL)

# TRAINING 模式（导出训练图，用于 on-device training）
torch.onnx.export(model, args, "model.onnx", training=TrainingMode.TRAINING)

# PRESERVE 模式（保持模型当前模式）
torch.onnx.export(model, args, "model.onnx", training=TrainingMode.PRESERVE)
```

> 对于 Layer 4 的端侧推理，使用 `TrainingMode.EVAL`。

---

## 4. 常见注意事项

### 4.1 必须设置 model.eval()

```python
model.eval()  # 关键！否则 Dropout/BN 行为在 ONNX 中不正确
```

忘记设 `eval()` 是导出 ONNX 最常见的错误之一。Dropout 在 eval 模式下被禁用，BN 在 eval 模式下使用 running statistics。

### 4.2 避免 Python 控制流

```python
# ❌ 导出会出错：if 语句在 trace 时被冻结
def bad_forward(self, x):
    if x.sum() > 0:
        return x * 2
    else:
        return x * 3

# ❌ 导出会出错：动态循环
def bad_forward(self, x):
    for i in range(x.size(0)):  # 取决于 batch size
        x = self.layer(x)

# ✅ 好：所有逻辑都在 Tensor 操作中
def good_forward(self, x):
    return torch.where(x.sum(dim=1, keepdim=True) > 0, x * 2, x * 3)
```

### 4.3 避免 NumPy 操作

```python
# ❌ ONNX 无法追踪 NumPy
def bad_forward(self, x):
    arr = x.numpy()          # 断开了计算图
    arr = process(arr)
    return torch.from_numpy(arr)

# ✅ 用 PyTorch 操作替代
def good_forward(self, x):
    return self.torch_process(x)
```

### 4.4 检查算子支持

```python
# 检查模型用了哪些 ONNX 算子
import onnx
model = onnx.load("model.onnx")
ops = set()
for node in model.graph.node:
    ops.add(node.op_type)
print(f"Used ops: {sorted(ops)}")
```

---

## 5. 带控制流的模型（TorchScript 方式）

对于包含 `if/for` 等控制流的模型，使用 `torch.jit.script` 代替 tracing：

```python
# 使用 script 而不是 trace
scripted_model = torch.jit.script(model)

torch.onnx.export(
    scripted_model,
    dummy_input,
    "model.onnx",
    opset_version=17,
)
```

---

## 6. 自定义算子

```python
# 注册自定义 ONNX 算子
@torch.onnx.symbolic_override
def my_custom_op(g, x):
    return g.op("MyDomain::MyCustomOp", x)

# 或使用 register_custom_op_symbolic
from torch.onnx import register_custom_op_symbolic

def my_relu_symbolic(g, input):
    return g.op("MyDomain::MyRelu", input)

register_custom_op_symbolic("mydomain::myrelu", my_relu_symbolic, opset_version=17)
```

---

## 7. 量化：PyTorch → ONNX INT8

### 7.1 PyTorch Eager Mode 量化（QAT）

```python
import torch.quantization as quant

# 1. 准备模型（插入 FakeQuant 节点）
model.qconfig = torch.quantization.get_default_qat_qconfig("fbgemm")
model_prepared = torch.quantization.prepare_qat(model, inplace=False)

# 2. 训练（量化感知训练）
train(model_prepared, train_loader)

# 3. 转为量化模型
model_prepared.eval()
model_int8 = torch.quantization.convert(model_prepared, inplace=False)

# 4. 导出 ONNX
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model_int8, dummy_input, "model_int8.onnx", opset_version=17)
```

### 7.2 PTQ 方式：导出 FP32 ONNX → ORT 量化

实际项目中更常见的做法是导出 FP32 ONNX 后用 ONNX Runtime 量化：

```python
# Step 1: PyTorch 导出 FP32 ONNX
torch.onnx.export(model, dummy_input, "model_fp32.onnx", opset_version=17)

# Step 2: ONNX Runtime 量化
from onnxruntime.quantization import quantize_static, QuantType, CalibrationDataReader

class MyCalibrationDataReader(CalibrationDataReader):
    def __init__(self, data_loader):
        self.data_loader = iter(data_loader)
        self.current = None

    def get_next(self):
        try:
            batch = next(self.data_loader)
            self.current = {"input": batch.numpy().astype(np.float32)}
        except StopIteration:
            self.current = None
        return self.current

quantize_static(
    model_input="model_fp32.onnx",
    model_output="model_int8.onnx",
    calibration_data_reader=MyCalibrationDataReader(calib_loader),
    quant_format=QuantType.QInt8,
    weight_type=QuantType.QInt8,
    activation_type=QuantType.QInt8,
)
```

### 7.3 对比量化精度

```python
import onnxruntime as ort

# FP32 推理
session_fp32 = ort.InferenceSession("model_fp32.onnx")
out_fp32 = session_fp32.run(None, {"input": test_data.numpy()})

# INT8 推理
session_int8 = ort.InferenceSession("model_int8.onnx")
out_int8 = session_int8.run(None, {"input": test_data.numpy()})

# 对比
diff = np.abs(out_fp32[0] - out_int8[0])
print(f"Max diff: {diff.max():.6f}")
print(f"Mean diff: {diff.mean():.6f}")
```

---

## 8. 文件大小优化

### 8.1 使用 onnxsim 简化图

```bash
# 安装
pip install onnxsim

# 简化（常量折叠 + 冗余消除）
python -m onnxsim model.onnx model_simplified.onnx
```

```python
from onnxsim import simplify

onnx_model = onnx.load("model.onnx")
simplified_model, check = simplify(onnx_model)
assert check, "Simplified model validation failed!"
onnx.save(simplified_model, "model_simplified.onnx")
```

### 8.2 保存时排除外部数据

```python
# 超过 2GB 的模型，权重可以存储为独立文件
torch.onnx.export(
    model, dummy_input, "large_model.onnx",
    opset_version=17,
    # 以下用于大模型
    # use_external_data_format=True,  # PyTorch 2.0+
)
```

---

## 9. 完整提交流程：PyTorch → ONNX → 量化 → 移动端

```python
import torch
import torch.onnx
import onnx
import onnxruntime as ort
from onnxruntime.quantization import quantize_static, QuantType

# ── Step 1: 训练 PyTorch 模型 ──
model = YourTrainedModel()
model.eval()
dummy_input = torch.randn(1, 3, 224, 224)

# ── Step 2: 导出 FP32 ONNX ──
torch.onnx.export(
    model, dummy_input, "model_fp32.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=17,
    dynamic_axes={"input": {0: "batch"}, "output": {0: "batch"}},
)

# ── Step 3: 验证 ONNX ──
onnx_model = onnx.load("model_fp32.onnx")
onnx.checker.check_model(onnx_model)

# 精度验证
session = ort.InferenceSession("model_fp32.onnx")
with torch.no_grad():
    torch_out = model(dummy_input)
ort_out = session.run(None, {"input": dummy_input.numpy()})[0]
assert np.allclose(torch_out.numpy(), ort_out, rtol=1e-3)

# ── Step 4: INT8 量化 ──
class CalibReader:
    def __init__(self):
        self.data = iter([np.random.randn(1,3,224,224).astype(np.float32) for _ in range(100)])
    def get_next(self):
        try:
            return {"input": next(self.data)}
        except StopIteration:
            return None

quantize_static(
    "model_fp32.onnx", "model_int8.onnx",
    calibration_data_reader=CalibReader(),
    weight_type=QuantType.QInt8,
)

# ── Step 5: 转为 .ort 移动端格式 ──
ort.tools.convert_onnx_model_to_ort_format("model_int8.onnx", "model.ort")

print("Done! model.ort ready for mobile deployment.")
```

---

## 10. 调试工具

### 10.1 可视化

```bash
pip install netron
netron model.onnx  # 浏览器中打开交互式图
```

### 10.2 导出过程调试

```python
# 开启 verbose 模式查看所有中间步骤
torch.onnx.export(
    model, dummy_input, "model.onnx",
    verbose=True,  # 打印每一层的转换详情
    opset_version=17,
)
```

### 10.3 图层面检查

```python
onnx_model = onnx.load("model.onnx")

# 查看所有输入
for inp in onnx_model.graph.input:
    print(f"Input: {inp.name}, type: {inp.type}")

# 查看所有输出
for out in onnx_model.graph.output:
    print(f"Output: {out.name}, type: {out.type}")

# 查看所有中间值
for vi in onnx_model.graph.value_info:
    print(f"Value: {vi.name}, shape: {vi.type}")

# 统计算子
from collections import Counter
ops = Counter(node.op_type for node in onnx_model.graph.node)
for op, count in ops.most_common():
    print(f"{op}: {count}")
```

---

## 11. 与你课程 Layer 4 的对接

| Layer 4 技能 | 对应本文章节 |
|---|---|
| ONNX 导出 | 第 2 章：基础导出 + 第 3 章：参数详解 |
| 量化（PTQ） | 第 7.2 章：导出 FP32 → ORT 量化 |
| 模型验证 | 第 2.2 章：输出一致性检查 |
| 超参调优 | 第 3.1 章：opset 选择 |
| 完整工作流 | 第 9 章：PyTorch → ONNX → 量化 → .ort |
