# TensorFlow Lite 模型转换与量化

> 来源：https://www.tensorflow.org/lite ，Apache 2.0 协议

---

## 1. TensorFlow Lite 概述

TensorFlow Lite 是一套在**移动端、嵌入式和边缘设备**上运行 ML 模型的上具集。

### 核心优势

| 特性 | 说明 |
|---|---|
| **低延迟** | 无需往返服务器，本地推理 |
| **隐私保护** | 个人数据不离开设备 |
| **离线运行** | 不需要网络连接 |
| **体积小** | 全量 125+ 算子二进制仅 ~1MB（ARM 32-bit）；精简后不到 300KB |
| **低功耗** | 高效推理，无网络开销 |

### 支持的平台和语言

| 平台 | 支持语言 |
|---|---|
| Android | Java, C++ |
| iOS | Swift, Objective-C, C++ |
| 嵌入式 Linux | Python, C++ |
| 微控制器（MCU） | C/C++ (TFLite Micro) |

---

## 2. 开发工作流

```
训练好的 TF/PyTorch 模型
        │
        ▼
   模型转换（TFLite Converter）
        │  可选：量化优化
        ▼
   .tflite 文件（FlatBuffers 格式）
        │
        ▼
   端侧推理（TFLite Interpreter / Task Library）
```

### 2.1 生成 .tflite 模型的三种方式

| 方式 | 说明 |
|---|---|
| **直接使用已有模型** | TensorFlow Hub 上预训练好的 .tflite 模型 |
| **Model Maker 创建** | 用自己的数据集重新训练（自动生成元数据） |
| **转换 TF 模型** | 使用 TFLite Converter 将 SavedModel/Keras/ConcreteFunction 转为 .tflite |

### 2.2 FlatBuffers 优势

- 相比 TF 的 Protocol Buffer 格式，**体积更小**
- **推理更快**：数据无需额外解析/解包，直接从内存读取
- 适合资源受限设备

---

## 3. 模型转换（TFLite Converter）

### 3.1 基本用法

```python
import tensorflow as tf

# 方式 1：从 SavedModel 转换
converter = tf.lite.TFLiteConverter.from_saved_model("path/to/saved_model")
tflite_model = converter.convert()

# 方式 2：从 Keras 模型转换
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 方式 3：从 ConcreteFunction 转换
converter = tf.lite.TFLiteConverter.from_concrete_functions([func])
tflite_model = converter.convert()

# 保存
with open("model.tflite", "wb") as f:
    f.write(tflite_model)
```

### 3.2 模型签名（Signatures）

TensorFlow 2.7+ 支持通过签名指定输入输出：

```python
# 指定特定签名的 representative dataset
def representative_dataset():
    for data in dataset:
        yield {
            "image": data.image,
            "bias": data.bias,
        }
```

### 3.3 算子兼容性

**并非所有 TF 算子都能转换为 TFLite**。转换前需检查：
- [TFLite 算子兼容性列表](https://www.tensorflow.org/lite/guide/ops_compatibility)
- 不支持的算子可通过 [自定义算子](https://www.tensorflow.org/lite/guide/ops_custom) 添加

---

## 4. 训练后量化（Post-Training Quantization, PTQ）

训练后量化是在**不影响模型精度或精度损失极小**的前提下，将已训练的浮点模型在转换时量化的技术。

### 4.1 量化方案对比

| 方案 | 模型缩小 | 速度提升 | 硬件支持 | 是否需要校准数据 |
|---|---|---|---|---|
| **动态范围量化** | 4x | 2-3x | CPU | 否 |
| **全整数量化** | 4x | 3x+ | CPU, Edge TPU, MCU | **是** |
| **Float16 量化** | 2x | GPU 加速 | CPU, GPU | 否 |
| **16x8 量化（实验性）** | 略增 | 当前较慢 | CPU | 是 |

### 4.2 量化方案选择决策

```
需要支持 Edge TPU 或 MCU？
  ├── 是 → 全整数量化
  └── 否 → 需要最小精度损失？
              ├── 是 → Float16 量化
              └── 否 → 动态范围量化（推荐起点）
```

---

### 4.3 动态范围量化

**推荐的起步方案**。只量化权重（float→int8），激活值在推理时动态量化。

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # 仅此一行
tflite_quant_model = converter.convert()
```

特点：
- **无需校准数据集**
- 权重 int8，激活值运行时动态量化
- 输出仍为浮点（因此加速不如全整数量化）
- 延迟接近全定点推理

---

### 4.4 全整数量化（Full Integer Quantization）

所有运算（权重 + 激活值 + 输入输出）全部 int8，兼容纯整数硬件。

#### 整数+浮点回退（保持浮动接口）

```python
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset  # 需要校准数据
tflite_quant_model = converter.convert()
```

注意：此模式下输入输出仍为浮点，**不兼容纯整数设备（如 MCU、Edge TPU）**。

#### 纯整数模式（兼容 MCU / Edge TPU）

```python
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8    # 或 tf.uint8
converter.inference_output_type = tf.int8   # 或 tf.uint8
tflite_quant_model = converter.convert()
```

这是 **CMSIS-NN、Edge TPU、TFLite Micro** 的标准输入格式。

#### representative_dataset（校准数据集）

用 100~500 个样本的小子集估算各层激活值范围：

```python
def representative_dataset():
    for data in tf.data.Dataset.from_tensor_slices((images)).batch(1).take(100):
        yield [tf.dtypes.cast(data, tf.float32)]

# 或使用签名方式（TF 2.7+ 推荐）
def representative_dataset():
    for data in dataset:
        yield {"image": data.image, "bias": data.bias}
```

**测试用虚拟数据集：**

```python
def representative_dataset():
    for _ in range(100):
        data = np.random.rand(1, 244, 244, 3)
        yield [data.astype(np.float32)]
```

---

### 4.5 Float16 量化

```python
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_quant_model = converter.convert()
```

- 模型缩小 2x（权重 float32→float16）
- 精度损失极小
- GPU Delegate 可直接处理 float16 数据
- CPU 运行时会反量化为 float32（不会减少延迟）

---

### 4.6 16x8 量化（实验性）

激活值 int16 + 权重 int8 + 偏置 int64。适合需要**更高精度**的场景：

- 超分辨率重建
- 音频信号处理（降噪、波束成形）
- 图像去噪
- HDR 重建

```python
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
]
```

缺点：当前推理速度比 8-bit 全整数慢；不兼容硬件加速 delegate。

---

## 5. 量化原理：数学表示

8-bit 量化公式：

```
real_value = (int8_value - zero_point) × scale
```

两个核心部分：

| 组件 | 说明 |
|---|---|
| **scale** | 每轴（per-channel）或每张量（per-tensor），浮点数 |
| **zero_point** | 权重 zero_point = 0；激活值 zero_point ∈ [-128, 127] |
| **int8 范围** | 权重 [-127, 127]；激活值 [-128, 127]（补码） |

### 量化规格文档

硬件厂商接入 TFLite Delegate 接口时，需实现此量化方案：
→ [Quantization Spec](https://www.tensorflow.org/lite/performance/quantization_spec)

---

## 6. 硬件加速（Delegate）

| Delegate | 平台 | 说明 |
|---|---|---|
| GPU Delegate | Android, iOS | OpenGL ES / Metal |
| NNAPI Delegate | Android | 利用 SoC 中的 AI 加速器 |
| Hexagon Delegate | Android (旧设备) | Qualcomm DSP |
| Core ML Delegate | iOS | Apple 神经网络引擎 |
| Edge TPU Delegate | Coral | Google 边缘 AI 芯片 |
| XNNPACK | 多平台 | CPU 浮点加速 |

```python
# 加载模型时启用 GPU Delegate
interpreter = tf.lite.Interpreter(
    model_path="model.tflite",
    experimental_delegates=[tf.lite.experimental.load_delegate("libedgetpu.so.1")]
)
```

---

## 7. 模型精度验证

量化后必须检查精度损失是否可接受：

```bash
# TensorFlow 提供的评估工具
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/evaluation/tasks
```

如果 PTQ 精度损失过大，考虑使用**量化感知训练（QAT）**：
→ https://www.tensorflow.org/model_optimization/guide/quantization/training

---

## 8. 关键约束

| 约束 | 说明 |
|---|---|
| 不是所有 TF 模型都能转 | 需检查算子兼容性 |
| 不支持端侧训练 | 仅推理（训练功能在 Roadmap 中） |
| 模型文件格式 | 专用 FlatBuffers 格式（.tflite），不是 TF 的 Protocol Buffer |

---

## 9. 端侧推理 API

### 无元数据模型：Interpreter API

```python
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])
```

### 有元数据模型：Task Library（推荐）

```python
# 图像分类（自动处理预处理和后处理）
from tflite_support.task import vision

classifier = vision.ImageClassifier.create_from_file("model.tflite")
result = classifier.classify(image)
```

支持语言：Java (Android)，Swift/C++ (iOS) 正在开发中。

---

## 10. 关键 API 速查

```python
# 转换
tf.lite.TFLiteConverter.from_saved_model(dir)
tf.lite.TFLiteConverter.from_keras_model(model)
tf.lite.TFLiteConverter.from_concrete_functions([func])

# 量化
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.target_spec.supported_types = [tf.float16]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

# 推理
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
interpreter.set_tensor(idx, data)
interpreter.invoke()
interpreter.get_tensor(idx)
```

---

## 11. 学习路径

1. 先用**动态范围量化**（一行代码，无需校准数据）感受量化效果
2. 再用**全整数量化**理解 representative_dataset 的作用
3. 对照量化规格文档，手算 scale 和 zero_point
4. 尝试导出纯整数模型 → 接 CMSIS-NN 或 TFLite Micro
