# ONNX Runtime 移动端部署

> 来源：https://onnxruntime.ai/docs/get-started/with-mobile.html ，MIT 协议

---

## 1. ONNX Runtime Mobile 简介

ONNX Runtime Mobile（ORT Mobile）是 ONNX Runtime 的**移动端裁剪版本**，专门为 iOS 和 Android 优化，支持在移动设备上进行模型推理。

### 与完整版 ORT 的区别

| 特性 | 完整版 ORT | ORT Mobile |
|---|---|---|
| 包体积 | 较大（含所有算子） | 精简（仅含移动端需要的算子） |
| 算子集 | 全部算子 | 缩减算子集（移动端必要子集） |
| 文件格式 | .onnx | .ort（优化格式） |
| 硬件加速 | CUDA/TensorRT/CoreML 等 | CoreML / XNNPACK / NNAPI / QNN |
| 量化 | 完整支持 | 完整支持 |
| 目标设备 | 服务器/桌面/移动 | **仅移动端（Android / iOS）** |

---

## 2. ORT 移动端格式 (.ort)

ORT Mobile 使用专用的 **ORT 格式** 而非标准 .onnx 文件：

```
.onnx 模型
    │
    ▼
ort_format_model 工具（转换 + 优化）
    │
    ▼
.ort 文件（更小、更快、移动端专用）
```

### 转换为 .ort 格式

```python
import onnxruntime as ort

# 方法 1：Python API
ort.tools.convert_onnx_model_to_ort_format(
    "model.onnx",
    "model.ort"
)

# 方法 2：命令行
# python -m onnxruntime.tools.convert_onnx_model_to_ort model.onnx model.ort
```

### .ort 格式优势

- **更小的二进制体积**：精简不必要的元数据
- **更快的加载速度**：减少解析开销
- **支持运行时优化**：常量折叠、算子融合预计算
- **量化集成**：可直接存储量化参数

---

## 3. 核心特性

### 3.1 移动端 Execution Providers

| EP | Android | iOS | 说明 |
|---|---|---|---|
| **XNNPACK** | ✅ | ✅ | CPU 加速（默认推荐） |
| **CoreML** | ❌ | ✅ | Apple 神经网络引擎 |
| **NNAPI** | ✅ | ❌ | Android SoC AI 加速器 |
| **QNN** | ✅ | ❌ | Qualcomm DSP |
| **CPU** | ✅ | ✅ | 纯 CPU 回退方案 |

```python
# 移动端推理时指定 EP 顺序
session = ort.InferenceSession("model.ort",
    providers=["CoreMLExecutionProvider",  # iOS: 优先 Apple NPU
               "XNNPACKExecutionProvider", # 回退：CPU 加速
               "CPUExecutionProvider"])    # 最终回退
```

### 3.2 移动端支持的操作类型

- 图像分类、目标检测
- 姿态估计
- 图像超分辨率
- 文本/NLP 推理
- 语音处理

### 3.3 移动端不支持

- 分布式训练
- 需要 CUDA 的大模型推理
- 需要特定桌面/服务器 EP 的算子

---

## 4. Android 集成

### 4.1 添加依赖

**build.gradle** (Module):

```gradle
dependencies {
    implementation 'com.microsoft.onnxruntime:onnxruntime-android:latest-version'
    // 或使用 CPU 专用版本（排除不用的 EP 以减小包体积）
    // implementation 'com.microsoft.onnxruntime:onnxruntime-android-cpu:latest-version'
}
```

### 4.2 Kotlin 推理示例

```kotlin
import ai.onnxruntime.*

// 1. 初始化环境
val ortEnv = OrtEnvironment.getEnvironment()

// 2. 加载模型
val session = ortEnv.createSession("model.ort")

// 3. 准备输入
val inputName = session.inputNames.first()
val inputShape = session.getInputInfo(inputName)?.nodeInfo?.shape
    ?: throw RuntimeException("Unknown input shape")

val inputData = OnnxTensor.createTensor(ortEnv, floatArrayOf(/* ... */), inputShape)

// 4. 推理
val outputs = session.run(mapOf(inputName to inputData))

// 5. 获取结果
val result = outputs.use {
    val outputTensor = it[0].value as OnnxTensor
    outputTensor.floatBuffer
}
```

### 4.3 Java 推理示例（简化）

```java
OrtEnvironment env = OrtEnvironment.getEnvironment();
OrtSession session = env.createSession("model.ort");

// 准备输入
OnnxTensor input = OnnxTensor.createTensor(env, inputBuffer, inputShape);
OrtSession.Result result = session.run(Collections.singletonMap("input", input));

// 获取输出
OnnxTensor output = (OnnxTensor) result.get(0);
float[] scores = output.getFloatBuffer().array();
```

---

## 5. iOS 集成

### 5.1 安装

**CocoaPods:**

```ruby
pod 'onnxruntime-objc'
```

**Swift Package Manager:**

```
https://github.com/microsoft/onnxruntime
```

### 5.2 Swift 推理示例

```swift
import onnxruntime

// 1. 加载模型
let env = try ORTEnv(loggingLevel: .warning)
let session = try ORTSession(env: env, modelPath: "model.ort")

// 2. 准备输入
let inputData = try ORTValue(
    tensorData: NSMutableData(data: imageData),
    elementType: .float,
    shape: [1, 3, 224, 224]
)

// 3. 推理
let outputs = try session.run(
    withInputs: ["input": inputData],
    outputNames: ["output"],
    runOptions: nil
)

// 4. 获取结果
if let output = outputs["output"] {
    let data = try output.tensorData()
    // 处理输出...
}
```

### 5.3 Objective-C 推理示例

```objc
#import <onnxruntime/onnxruntime.h>

ORTEnv *env = [[ORTEnv alloc] initWithLoggingLevel:ORTLoggingLevelWarning];
ORTSession *session = [[ORTSession alloc] initWithEnv:env
                                           modelPath:@"model.ort"];

ORTValue *input = [[ORTValue alloc] initWithTensorData:data
                                          elementType:ORTTensorElementDataTypeFloat
                                                shape:@[@1, @3, @224, @224]];

NSDictionary *outputs = [session runWithInputs:@{@"input": input}
                                  outputNames:[NSSet setWithObject:@"output"]
                                   runOptions:nil
                                       error:&error];
```

---

## 6. 移动端模型优化

### 6.1 算子精简

构建时只包含模型需要的算子，减小包体积：

```bash
# 构建时指定需要的算子
python tools/ci_build/build.py \
    --config Release \
    --build_shared_lib \
    --parallel \
    --minimal_build \
    --include_ops_by_model model.onnx
```

### 6.2 量化（INT8 / FP16）

移动端推理强烈推荐量化：

```python
from onnxruntime.quantization import quantize_static, QuantType

def calibration_reader():
    for _ in range(100):
        yield {"input": np.random.randn(1, 3, 224, 224).astype(np.float32)}

quantize_static(
    "model.onnx",
    "model_int8.onnx",
    calibration_data_reader=calibration_reader,
    weight_type=QuantType.QInt8
)
```

### 6.3 ORT 格式运行时优化

```python
from onnxruntime.transformers.optimizer import optimize_model

# 针对 Transformer 模型的优化（BERT/GPT 等）
model = optimize_model(
    "model.onnx",
    model_type="bert",       # bert / gpt2 / ... 
    num_heads=12,
    hidden_size=768,
    opt_level=99,            # 全部优化
    use_gpu=False            # 移动端用 CPU
)
```

---

## 7. 性能最佳实践

### 7.1 模型预处理

```python
# 使用 ORT 移动端模型导出工具
from onnxruntime.tools.ort_format_model import convert_onnx_model_to_ort_format
from onnxruntime.tools.ort_format_model.ort_model_processor import OrtModelProcessor

processor = OrtModelProcessor("model.onnx", required_operators=[])
processor.convert("model.ort")
```

### 7.2 线程控制

```kotlin
// Android: 控制线程数以匹配设备核心数
val options = OrtSession.SessionOptions()
options.setIntraOpNumThreads(4)  // 算子的并行线程数
options.setInterOpNumThreads(1)  // 算子间的并行度
val session = env.createSession("model.ort", options)
```

```python
# Python 等效
session_options = ort.SessionOptions()
session_options.intra_op_num_threads = 4
session_options.inter_op_num_threads = 1
```

### 7.3 内存管理

- 使用 **arena allocator** 减少内存碎片
- 推理后及时释放 `OrtSession.Result`
- 移动端优先使用 INT8 量化减小 4x 内存

---

## 8. 模型部署工作流总结

```
训练好的 PyTorch 模型 (.pth)
        │
        ▼
torch.onnx.export() ────→ model.onnx
        │
        ▼
静态量化（INT8）────→ model_int8.onnx  (可选但推荐)
        │
        ▼
convert_onnx_model_to_ort_format()
        │
        ▼
model.ort  (移动端专用格式)
        │
        ▼
集成到 App (Android Gradle / iOS CocoaPods)
        │
        ▼
OrtSession.run()  端侧推理
```

---

## 9. 调试与排查

### 检查移动端是否支持模型中的算子

```python
# Python 端检查
import onnx
from onnxruntime.tools.mobile_helpers import check_model_can_use_ort_mobile_package

check_model_can_use_ort_mobile_package("model.onnx")
```

### 常见问题

| 问题 | 可能原因 | 解决 |
|---|---|---|
| 模型加载失败 | .ort 格式不正确 | 重新转换 |
| 推理结果异常 | 量化精度损失过大 | 使用 FP16 或调高精度 |
| 某个算子不支持 | 不在移动端算子子集中 | 用 pure CPU EP 回退 |
| 内存不足 (OOM) | 模型太大 | 量化 / 剪枝 / 更换小模型 |
| 首次推理慢 | 初始化 + JIT 编译 | 提前 warm-up 一次 |
| CoreML 加速不生效 | 算子不兼容 CoreML | 检查 EP 是否注册成功 |

---

## 10. 资源链接

| 资源 | 链接 |
|---|---|
| ORT Mobile 官方文档 | https://onnxruntime.ai/docs/get-started/with-mobile.html |
| Android 示例 | https://github.com/microsoft/onnxruntime-inference-examples |
| iOS 示例 | https://github.com/microsoft/onnxruntime-inference-examples |
| 算子兼容性 | https://onnxruntime.ai/docs/reference/operators/MobileOps.html |
| ORT 移动端性能调优 | https://onnxruntime.ai/docs/performance/mobile-performance.html |

---

## 11. 与你课程 Layer 4 的对接

| Layer 4 技能 | 对应本文章节 |
|---|---|
| 模型导出 | 第 8 章：完整工作流 |
| 量化（PTQ） | 第 6.2 章：INT8 量化 |
| 格式转换 | 第 2 章：.onnx → .ort |
| 嵌入式部署概念 | 第 4 章 (Android) + 第 5 章 (iOS) |
| 硬件加速 | 第 3.1 章：Execution Providers |
