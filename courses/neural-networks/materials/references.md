# 学习资源索引

---

# 主要教材（教学权威来源）

| 资料 | 路径 | 说明 |
|------|------|------|
| 《神经网络与深度学习》 | [《神经网络与深度学习》.md](《神经网络与深度学习》.md) | **邱锡鹏著，复旦大学出版社，2019。** 15 章 + 附录 A-E。每次授课前必须读取对应章节。 |

---

# 辅助参考

## 中文教材

| 资料 | 说明 | 推荐用途 |
|------|------|---------|
| 《动手学深度学习》(李沐) | 实践导向，含大量 PyTorch 代码 | 代码实现参考 |
| 周志华《机器学习》 | 机器学习理论经典，"西瓜书" | 机器学习理论基础 |
| 李宏毅机器学习课程 | 中文讲解，覆盖面广 | 入门辅助 |

## 经典教程

| 资源 | 说明 | 推荐用途 |
|------|------|---------|
| CS231n（Stanford） | 卷积神经网络与计算机视觉 | CNN 深入理解 |
| CS224n（Stanford） | 自然语言处理与深度学习 | RNN/Transformer |
| Deep Learning Book（Goodfellow） | 深度学习"圣经" | 理论深入 |
| 3Blue1Brown 神经网络系列 | 可视化讲解反向传播 | 直觉建立 |

## 在线教程（快速查阅）

| 主题 | 链接 | 备注 |
|------|------|------|
| runoob 神经网络教程 | https://www.runoob.com/python3/ | 已降级为辅助参考 |

---

# 工具文档

| 工具 | 用途 |
|------|------|
| NumPy | https://numpy.org/doc/ |
| PyTorch | https://pytorch.org/docs/stable/ |
| Matplotlib | https://matplotlib.org/stable/ |

---

# Edge AI / 端侧部署专题文档

| 文档 | 说明 |
|------|------|
| [TFLite-模型转换与量化.md](TFLite-模型转换与量化.md) | TFLite 转换、PTQ 4 种量化方案、Delegate 硬件加速 |
| [ONNX-导出与Runtime.md](ONNX-导出与Runtime.md) | ONNX 概念、框架导出、ORT 推理、量化 |
| [ONNX-Runtime-移动端.md](ONNX-Runtime-移动端.md) | ORT Mobile 架构、Android/iOS 集成 |
| [PyTorch-ONNX-量化.md](PyTorch-ONNX-量化.md) | torch.onnx.export 详解、ORT 量化流水线 |
| [CMSIS-NN-ARM-MCU部署.md](CMSIS-NN-ARM-MCU部署.md) | Cortex-M 算子加速、TFLite Micro 对接 |

## 外部部署工具

| 工具 | 用途 |
|------|------|
| ONNX Runtime | 跨平台推理引擎 |
| TFLite Micro | MCU 端推理 |
| TensorRT | NVIDIA GPU 推理优化 |
| CMSIS-NN | ARM Cortex-M NN 库 |
| TVM | 编译器级自动优化 |

---

# 论文（经典架构）

| 论文 | 年份 | 关键贡献 |
|------|------|---------|
| LeNet-5 (LeCun) | 1998 | 最早的 CNN |
| AlexNet (Krizhevsky) | 2012 | ImageNet 突破，ReLU、Dropout |
| VGG (Simonyan) | 2014 | 小卷积核堆叠 |
| ResNet (He) | 2015 | 残差连接 |
| Attention Is All You Need | 2017 | Transformer |
| BERT | 2018 | 预训练语言模型 |

---

# 学习路径建议

## 系统学习（推荐）
1. 按教材第 1→2→3→...→15 章顺序推进
2. 每节先读教材原文，再看辅助资料
3. 每个公式都手推一遍
4. 核心算法用 NumPy 从零实现

## 数学基础不足时
1. 教材附录 A-E 随时查阅
2. 3Blue1Brown "线性代数的本质"/"微积分的本质" 系列
