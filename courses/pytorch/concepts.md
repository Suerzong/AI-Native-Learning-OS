# 核心概念索引

本文件记录学习者需要掌握的关键概念。每个概念都应能回答三个问题：它是什么、为什么需要它、在 PyTorch 代码里哪里出现。

## Tensor 基础

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| Tensor | PyTorch 的多维数组，类似 numpy 的 ndarray 但支持 GPU 和自动求导 | 02 |
| dtype | Tensor 的数据类型（float32、int64 等），影响计算精度和内存 | 02 |
| device | Tensor 所在的设备（cpu 或 cuda），不同设备的 tensor 不能直接运算 | 08 |
| shape | Tensor 各维度的大小，是调试代码的第一线索 | 02 |
| broadcasting | 不同 shape 的 tensor 做运算时的自动扩展规则 | 04 |
| 索引与切片 | 类似 numpy 的数据选取方式 | 05 |
| reshape/view | 改变 tensor 的形状（不改变数据） | 06 |
| squeeze/unsqueeze | 去掉/增加 size=1 的维度 | 06 |
| permute/transpose | 维度重排 | 06 |
| cat/stack | 沿已有维度拼接/沿新维度堆叠 | 07 |

## 自动求导

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| requires_grad | 标记 tensor 需要计算梯度 | 09 |
| 计算图 | 记录运算关系的有向图，用于反向传播 | 09 |
| backward() | 从标量 loss 开始反向传播梯度 | 09 |
| .grad | 存储计算得到的梯度 | 09 |
| torch.no_grad() | 禁用梯度计算的上下文管理器（推理时用） | 10 |
| detach() | 从计算图中分离 tensor | 10 |
| 梯度清零 | 每次 backward 前需要清除之前累积的梯度 | 10 |

## 模型构建

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| nn.Module | PyTorch 所有模型的基类 | 11 |
| forward() | 定义前向传播逻辑的方法 | 11 |
| parameters() | 返回模型所有可学习参数 | 11 |
| Linear | 全连接层：y = xW^T + b | 12 |
| Conv2d | 二维卷积层 | 12 |
| BatchNorm2d | 批量归一化层 | 12 |
| ReLU | 激活函数：max(0, x) | 13 |
| Dropout | 训练时随机置零一部分神经元（正则化） | 13 |
| MaxPool2d | 最大池化层 | 13 |
| Flatten | 将多维输入展平为 1D | 13 |

## 训练

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| 损失函数 | 衡量模型输出与真实标签差距的函数 | 15 |
| CrossEntropyLoss | 分类任务的损失函数（内部含 log_softmax） | 15 |
| MSELoss | 回归任务的损失函数 | 15 |
| BCELoss | 二分类损失函数（需要先过 sigmoid） | 15 |
| 优化器 | 根据梯度更新模型参数的算法 | 16 |
| SGD | 随机梯度下降 | 16 |
| Adam | 自适应学习率优化器 | 16 |
| learning_rate | 控制参数更新步长的超参数 | 16 |
| zero_grad() | 清除参数的梯度 | 16 |
| step() | 执行一次参数更新 | 16 |
| model.train() | 设置模型为训练模式（启用 Dropout/BatchNorm 训练行为） | 17 |
| model.eval() | 设置模型为推理模式（禁用 Dropout，用 BatchNorm 的 running stats） | 17 |

## 数据处理

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| Dataset | 自定义数据集的抽象基类，需要实现 __len__ 和 __getitem__ | 19 |
| DataLoader | 数据加载器，提供 batch、shuffle、并行加载等功能 | 20 |
| transforms | 数据预处理和增强的变换组合 | 21 |
| Normalize | 标准化：(x - mean) / std | 21 |
| 数据增强 | 通过随机变换增加训练数据多样性 | 26 |

## 评估与调参

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| accuracy | 准确率：正确预测数 / 总数 | 24 |
| precision | 精确率：TP / (TP + FP) | 24 |
| recall | 召回率：TP / (TP + FN) | 24 |
| F1 | precision 和 recall 的调和平均 | 24 |
| 混淆矩阵 | 展示各类别预测情况的矩阵 | 24 |
| 过拟合 | 训练集表现好但测试集差 | 25 |
| 正则化 | 防止过拟合的技术（L2、Dropout、数据增强） | 25 |
| 学习率调度 | 训练过程中动态调整学习率 | 27 |
| TensorBoard | 训练过程可视化工具 | 29 |
| 迁移学习 | 利用预训练模型的特征提取能力 | 30-31 |
| state_dict | 模型参数的字典（保存和加载的核心） | 28 |

## 部署

| 概念 | 简要说明 | 对应课节 |
|------|---------|---------|
| ONNX | 开放神经网络交换格式，用于跨框架模型导出 | 35 |
| torch.onnx.export | PyTorch 模型导出为 ONNX 的函数 | 35 |
| TorchScript | PyTorch 的模型序列化格式（支持 C++ 加载） | 37 |
| torch.jit.trace | 通过运行一次输入来记录模型结构 | 37 |
| torch.jit.script | 通过分析源代码来编译模型 | 37 |
| 量化 | 将浮点权重转为低精度整数（减少模型大小和推理时间） | 38 |
| 剪枝 | 移除不重要的权重或通道（减少计算量） | 39 |
| ONNX Runtime | 微软的跨平台推理引擎 | 36 |
