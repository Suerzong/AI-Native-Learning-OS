# 学习资源索引

本文件收集神经网络与深度学习相关的学习资料。

---

# 主教材（2026-05-21 起）

| 教材 | 作者 | 版本 | 定位 |
|:--|:--|:--|:--|
| 《动手学深度学习》(D2L) | Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola | 2.0.0 (2022) | **主教材** — 代码驱动，PyTorch 实现，工程导向 |
| 《神经网络与深度学习》(NNDL) | 邱锡鹏（复旦大学）| 2021 | **理论补充** — 数学原理深入，无框架依赖 |

两本教材互补：D2L 负责"能写代码"，NNDL 负责"能推公式"。以 D2L 为主线，在需要深入理论时查阅 NNDL 对应章节。

## 教材文件

| 文件 | 大小 |
|:--|:--|
| `《动⼿学深度学习》.pdf` | 27MB |
| `《神经网络与深度学习》.pdf` | 6.5MB |

---

# 原参考（runoob.com，已切换）

| 主题 | 链接 | 对应章节 |
|------|------|---------|
| 神经网络简介 | https://www.runoob.com/python3/python3-neural-network.html | 01 |
| 感知机 | https://www.runoob.com/python3/python3-perceptron.html | 02 |
| 线性回归 | https://www.runoob.com/python3/python3-linear-regression.html | 03 |
| 逻辑回归 | https://www.runoob.com/python3/python3-logistic-regression.html | 04 |
| 激活函数 | https://www.runoob.com/python3/python3-activation-function.html | 05 |
| 损失函数 | https://www.runoob.com/python3/python3-loss-function.html | 06 |
| 反向传播 | https://www.runoob.com/python3/python3-backpropagation.html | 11-12 |
| 梯度下降 | https://www.runoob.com/python3/python3-gradient-descent.html | 13 |
| 深度学习简介 | https://www.runoob.com/python3/python3-deep-learning.html | 21 |
| 卷积神经网络 | https://www.runoob.com/python3/python3-cnn.html | 22-25 |
| 循环神经网络 | https://www.runoob.com/python3/python3-rnn.html | 26-28 |

---

# 进阶学习资料

## 经典教程

| 资源 | 说明 | 推荐用途 |
|------|------|---------|
| CS231n（Stanford） | 卷积神经网络与计算机视觉 | CNN 深入理解 |
| CS224n（Stanford） | 自然语言处理与深度学习 | RNN/Transformer |
| Deep Learning Book（Ian Goodfellow） | 深度学习 "圣经" | 理论深入 |
| 3Blue1Brown 神经网络系列 | 可视化讲解反向传播 | 直觉建立 |
| 李宏毅机器学习课程 | 中文讲解，覆盖面广 | 入门体系 |

## 工具文档

| 工具 | 文档链接 | 用途 |
|------|---------|------|
| NumPy | https://numpy.org/doc/ | 基础数值计算 |
| PyTorch | https://pytorch.org/docs/stable/ | 深度学习框架 |
| Matplotlib | https://matplotlib.org/stable/ | 数据可视化 |
| ONNX | https://onnx.ai/ | 模型交换格式 |
| TFLite | https://www.tensorflow.org/lite | 端侧推理 |

## 论文（经典架构）

| 论文 | 年份 | 关键贡献 |
|------|------|---------|
| LeNet-5 (LeCun) | 1998 | 最早的 CNN |
| AlexNet (Krizhevsky) | 2012 | ImageNet 突破，ReLU、Dropout |
| VGG (Simonyan) | 2014 | 小卷积核堆叠 |
| ResNet (He) | 2015 | 残差连接，解决深层网络退化 |
| Attention Is All You Need | 2017 | Transformer |
| BERT | 2018 | 预训练语言模型 |

---

# Edge AI 相关资料

| 主题 | 说明 | 用途 |
|------|------|------|
| ONNX Runtime | 跨平台推理引擎 | 模型部署 |
| TFLite Micro | MCU 端推理框架 | 嵌入式部署 |
| TensorRT | NVIDIA 推理优化 | GPU 端加速 |
| CMSIS-NN | ARM 的 NN 库 | Cortex-M 部署 |
| TVM | 编译器级优化框架 | 自动优化 |

---

# 代码参考

## NumPy 从零实现

| 实现 | 说明 |
|------|------|
| 2 层网络前向传播 | skill-map/perceptron.md |
| 激活函数 | skill-map/activation.md |
| 损失函数 | skill-map/loss.md |
| 反向传播 | skill-map/backprop.md |
| 优化器 | skill-map/optimization.md |
| 2D 卷积 | skill-map/cnn.md |

## PyTorch 实现

| 实现 | 说明 |
|------|------|
| MLP 分类 | skill-map/perceptron.md → 第三层 |
| CNN (LeNet) | skill-map/cnn.md |
| LSTM/GRU | skill-map/rnn.md |
| Dropout + BN | skill-map/regularization.md |

---

# 学习路径推荐

## 数学基础不足时

1. 先看 3Blue1Brown 的 "线性代数的本质" 系列
2. 再看 3Blue1Brown 的 "微积分的本质" 系列
3. 然后开始本课程

## 想快速上手时

1. 跳过理论推导，直接从第三层开始
2. 先用 PyTorch 跑通模型
3. 遇到不理解的再回第一、二层补

## 想深入理解时

1. 按课程顺序完整学习
2. 每个公式都手推一遍
3. 每个实现都用 NumPy 从零写
4. 参考 Deep Learning Book 对应章节
