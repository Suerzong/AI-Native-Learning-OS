# CMSIS-NN：ARM Cortex-M 神经网络部署库

> 来源：https://github.com/ARM-software/CMSIS-NN ，Apache 2.0 协议

---

## 1. 什么是 CMSIS-NN

**CMSIS-NN** 是 ARM 官方开发的**高效神经网络内核库**，专门为 ARM Cortex-M 系列处理器优化。它的目标是**最大化性能、最小化内存占用**，让神经网络能跑在资源极度受限的微控制器上。

> CMSIS = Cortex Microcontroller Software Interface Standard（Cortex 微控制器软件接口标准）

---

## 2. 定位

```
TensorFlow / PyTorch 模型
        │
        ▼ 量化 + 转换
    TFLite 模型 (.tflite)
        │
        ▼ TFLite Micro 解释器
    调用 CMSIS-NN 内核 ←── 你在这里
        │
        ▼
    ARM Cortex-M 处理器
```

**CMSIS-NN 不做的事**：
- 不处理模型加载/解析
- 不做内存管理
- 不做推理调度

**CMSIS-NN 做的事**：
- 提供极致优化的算子实现（Conv2D、FC、Pooling、LSTM 等）
- 被 **TFLite Micro** 调用，作为底层运算加速
- 与 TFLite Micro 参考内核**逐比特一致**（int8 / int16 量化模式）

---

## 3. 量化规范

CMSIS-NN 遵循 TFLite Micro 的量化规范：

| 类型 | 说明 |
|---|---|
| **int8** | 8-bit 权重 + 8-bit 激活值（最常用） |
| **int16** | 16-bit 权重 + 16-bit 激活值（更高精度） |
| **int4** | 4-bit 权重 + 8-bit 激活值（实验性，极致压缩） |

所有运算结果与 TFLite Micro 参考实现**逐比特一致（bit-exact）**。

---

## 4. 三种优化层级

CMSIS-NN 根据处理器的架构能力，自动选择最优实现：

### 4.1 Pure C（纯 C 实现）

- **适用处理器**：Cortex-M0, Cortex-M3
- **无任何加速指令**
- 始终作为回退方案

### 4.2 DSP 扩展

- **适用处理器**：Cortex-M4, Cortex-M33 (+DSP)
- 使用 **SIMD**（Single Instruction Multiple Data）指令加速
- 单指令处理多个数据，显著提速

### 4.3 MVE 扩展（Helium 技术）

- **适用处理器**：Cortex-M55, Cortex-M85
- 使用 **ARM M-Profile Vector Extension (MVE)** 指令
- **最高性能**：向量级并行运算

---

## 5. 支持的算子矩阵

| Operator | C int8 | C int16 | C int4 | DSP int8 | MVE int8 |
|---|---|---|---|---|---|
| **Conv2D** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **DepthwiseConv2D** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **TransposeConv2D** | ✅ | ❌ | ❌ | ✅ | ✅ |
| **Fully Connected** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Batch Matmul** | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Add** | ✅ | ✅ | N/A | ✅ | ✅ |
| **Mul** | ✅ | ✅ | N/A | ✅ | ✅ |
| **Minimum** | ✅ | ❌ | N/A | ❌ | ✅ |
| **Maximum** | ✅ | ❌ | N/A | ❌ | ✅ |
| **MaxPooling** | ✅ | ✅ | N/A | ✅ | ✅ |
| **AvgPooling** | ✅ | ✅ | N/A | ✅ | ✅ |
| **Softmax** | ✅ | ✅ | N/A | ✅ | ✅ |
| **LSTM** | ✅ | ✅ | ❌ | ✅ | ✅ |
| **SVDF** | ✅ | ❌ | ❌ | ✅ | ✅ |
| **Pad** | ✅ | ❌ | N/A | ❌ | ✅ |
| **Transpose** | ✅ | ❌ | N/A | ❌ | ✅ |

> DSP int16 / int4 / MVE int16 列同样广泛支持，详见原文档。

### 算子说明

| 算子 | 用途 |
|---|---|
| Conv2D | 标准 2D 卷积（图像分类的核心） |
| DepthwiseConv2D | 逐通道卷积（MobileNet 的关键） |
| TransposeConv2D | 转置卷积（上采样/超分辨率） |
| Fully Connected | 全连接层（分类头） |
| Batch Matmul | 批量矩阵乘法（Transformer/Attention） |
| Add / Mul | 逐元素加减乘（残差连接、门控） |
| MaxPooling / AvgPooling | 池化层 |
| Softmax | 分类输出概率 |
| LSTM | 长短期记忆（时序处理） |
| SVDF | 奇异值分解滤波器（语音关键词识别） |
| Pad | 填充操作 |
| Transpose | 转置操作 |

---

## 6. 编译与集成

### 6.1 基本编译

```bash
cd CMSIS-NN
mkdir build && cd build

# Cortex-M55（带 Helium 向量加速）
cmake .. \
  -DCMAKE_TOOLCHAIN_FILE=/path/to/ethos-u-core-platform/cmake/toolchain/arm-none-eabi-gcc.cmake \
  -DTARGET_CPU=cortex-m55
make

# Cortex-M7（带 DSP）
cmake .. \
  -DCMAKE_TOOLCHAIN_FILE=/path/to/ethos-u-core-platform/cmake/toolchain/arm-none-eabi-gcc.cmake \
  -DTARGET_CPU=cortex-m7
make

# Cortex-M3（纯 C）
cmake .. \
  -DCMAKE_TOOLCHAIN_FILE=/path/to/ethos-u-core-platform/cmake/toolchain/arm-none-eabi-gcc.cmake \
  -DTARGET_CPU=cortex-m3
make
```

### 6.2 编译选项

| 选项 | 说明 |
|---|---|
| `CMSIS_OPTIMIZATION_LEVEL` | 优化级别，默认 `Ofast` |
| `CMSIS_NN_USE_SINGLE_ROUNDING` | 使用单次舍入代替双次舍入（可能影响精度） |
| `CMSIS_NN_USE_REQUANTIZE_INLINE_ASSEMBLY` | 对内联汇编的反量化函数（M4 更快，M7 可能更慢） |
| `OPTIONAL_RESTRICT_KEYWORD=__restrict` | 对 M7 的额外优化（推荐启用） |

### 6.3 注意事项

- **不要**使用 `-fno-builtin`：会禁用 memcpy/memset 的优化实现，严重影响性能
- **不要**使用 `-ffreestanding`：会隐式启用 `-fno-builtin`
- **不要**省略 `-fomit-frame-pointer`：在 `-O` 及以上自动启用

### 6.4 支持的编译器

| 编译器 | 状态 |
|---|---|
| ARM Compiler 6 (armclang) | ✅ 正式测试 |
| ARM GNU Toolchain (arm-none-eabi-gcc) | ✅ 正式测试 |
| IAR Compiler | ❌ 未测试（可能有编译/性能问题） |
| Host (x86) 编译 | ⚠️ 理论上可纯 C 实现，需少量修改 |

---

## 7. Python 绑定（可选）

CMSIS-NN 提供 Python 绑定，用于在 Python 中计算缓冲区大小（辅助 TFLite Micro 的内存规划）：

```bash
pip wheel . -w dist
pip install dist/cmsis_nn-*.whl
```

```python
import cmsis_nn

backend = cmsis_nn.Backend.MVE  # 或 DSP / PURE_C

# 计算卷积所需的缓冲区大小
buf_size = cmsis_nn.convolve_wrapper_buffer_size(
    backend,
    cmsis_nn.DataType.A8W8,           # 8-bit 激活 + 8-bit 权重
    input_nhwc=[1, 8, 8, 16],         # NHWC 格式
    filter_nhwc=[8, 3, 3, 16],
    output_nhwc=[1, 6, 6, 8],
    padding_hw=[0, 0],
    stride_hw=[1, 1],
    dilation_hw=[1, 1],
)

# 或根据处理器型号自动推导后端
backend = cmsis_nn.resolve_backend(cmsis_nn.CortexM.M55)
```

---

## 8. 与 TFLite Micro 的关系

```
┌─────────────────────────────┐
│      TFLite Micro           │
│  (模型加载 + 内存管理 + 调度) │
│                             │
│  ┌───────────────────────┐  │
│  │     CMSIS-NN          │  │
│  │  (算子加速实现)        │  │
│  │  - arm_convolve_s8()  │  │
│  │  - arm_fully_connected_s8() │
│  │  - arm_avgpool_s8()   │  │
│  │  - ...                │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

TFLite Micro 调用 CMSIS-NN 的方式：
1. 检测处理器架构
2. 选择对应优化层级（Pure C / DSP / MVE）
3. 为每个算子分配内存
4. 调用 CMSIS-NN 内核执行
5. 回收内存

---

## 9. 与课程 Layer 4 的关系

### 在嵌入式部署链路中的位置

```
Layer 3: CNN 模型 (MobileNet)
    │
    ▼
全整数量化 (TFLite PTQ, INT8)
    │
    ▼
.tflite 模型
    │
    ▼
TFLite Micro 解释器 + CMSIS-NN 内核
    │
    ▼
ARM Cortex-M4/M7/M55 硬件
```

### 与课程技能的对应

| Layer 4 技能 | CMSIS-NN 中的对应 |
|---|---|
| 模型压缩：量化 | int8 / int16 / int4 量化方案（第 3 章） |
| 嵌入式部署概览 | Cortex-M 系列部署（第 6-8 章） |
| ONNX & TFLite | 作为 TFLite Micro 的底层加速（第 8 章） |

---

## 10. 性能参考

以下数值为定性参考（具体取决于处理器频率和模型结构）：

| 处理器 | 加速方式 | 相对纯 C 提速 |
|---|---|---|
| Cortex-M0/M3 | 纯 C（基线） | 1x |
| Cortex-M4 | DSP 扩展 | ~2-5x |
| Cortex-M33 | DSP 扩展 | ~2-5x |
| Cortex-M7 | DSP 扩展 | ~3-7x |
| Cortex-M55 | Helium / MVE | ~5-15x |
| Cortex-M85 | Helium / MVE | ~5-15x |

> CMSIS-NN 官方提供完整的单元测试和基准测试：https://github.com/ARM-software/CMSIS-NN/tree/main/Tests

---

## 11. 版本与发布

- 仓库主分支：`main`
- 每年两次正式发布（Release）
- 版本号遵循语义化版本（Semantic Versioning）
- 每个文件有独立版本号和日期

---

## 12. 快速上手路线

1. **理解 CMSIS-NN 的角色**：读完本文第 1-3 章
2. **选择一个 MCU 开发板**：推荐 STM32F746G-Discovery (Cortex-M7) 或 NXP RT1060 (Cortex-M7)
3. **训练并量化一个小模型**：如 MobileNetV1 0.25x，用 TFLite 全整数量化转成 .tflite
4. **集成 TFLite Micro + CMSIS-NN**：参考 [TFLite Micro 官方示例](https://github.com/tensorflow/tflite-micro)
5. **部署到板子上**：对比启用/不启用 CMSIS-NN 的推理速度差异

### 推荐开发板入门

| 开发板 | 处理器 | CMSIS-NN 层级 | 参考价格 |
|---|---|---|---|
| Arduino Nano 33 BLE Sense | Cortex-M4 | DSP | ~$30 |
| STM32F746G-Discovery | Cortex-M7 | DSP | ~$50 |
| SparkFun Edge | Cortex-M4 | DSP | ~$15 |
| Alif Ensemble E7 | Cortex-M55 | MVE (Helium) | ~$100+ |

---

## 13. 参考链接

| 资源 | URL |
|---|---|
| CMSIS-NN GitHub | https://github.com/ARM-software/CMSIS-NN |
| TFLite Micro | https://www.tensorflow.org/lite/microcontrollers |
| ARM Ethos-U Core Platform | https://review.mlplatform.org/admin/repos/ml/ethos-u/ethos-u-core-platform |
| ARM 编译器工具链 | https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain |
| TFLite 量化规格 | https://www.tensorflow.org/lite/performance/quantization_spec |
