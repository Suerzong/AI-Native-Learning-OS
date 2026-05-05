# PyTorch 完整教程

> 来源：[菜鸟教程 PyTorch](https://www.runoob.com/pytorch/pytorch-tutorial.html)

## 目录

1. [PyTorch 教程](#pytorch-教程)
   - [谁适合阅读本教程？](#谁适合阅读本教程)
   - [阅读本教程前，您需要了解的知识：](#阅读本教程前您需要了解的知识)
   - [参考链接](#参考链接)
2. [PyTorch 简介](#pytorch-简介)
   - [PyTorch 特性](#pytorch-特性)
   - [与其他框架的对比](#与其他框架的对比)
   - [PyTorch 的历史与发展](#pytorch-的历史与发展)
3. [PyTorch 安装](#pytorch-安装)
   - [安装前的准备工作](#安装前的准备工作)
   - [安装 PyTorch](#安装-pytorch)
4. [PyTorch 基础](#pytorch-基础)
   - [PyTorch 架构总览](#pytorch-架构总览)
   - [张量（Tensor）](#张量tensor)
   - [自动求导（Autograd）](#自动求导autograd)
   - [神经网络（nn.Module）](#神经网络nnmodule)
   - [训练模型](#训练模型)
   - [设备（Device）](#设备device)
5. [PyTorch 张量（Tensor）](#pytorch-张量tensor)
   - [创建张量](#创建张量)
   - [张量的属性](#张量的属性)
   - [张量的操作](#张量的操作)
   - [张量的 GPU 加速](#张量的-gpu-加速)
   - [张量与 NumPy 的互操作](#张量与-numpy-的互操作)
6. [PyTorch 神经网络基础](#pytorch-神经网络基础)
   - [torch.nn 参考](#torchnn-参考)
7. [PyTorch 第一个神经网络](#pytorch-第一个神经网络)
   - [另外一个实例](#另外一个实例)
8. [PyTorch 数据处理与加载](#pytorch-数据处理与加载)
   - [自定义 Dataset](#自定义-dataset)
   - [使用 DataLoader 加载数据](#使用-dataloader-加载数据)
   - [预处理与数据增强](#预处理与数据增强)
   - [加载图像数据集](#加载图像数据集)
   - [用多个数据源（Multi-source Dataset）](#用多个数据源multi-source-dataset)
9. [PyTorch 线性回归](#pytorch-线性回归)
   - [数据准备](#数据准备)
   - [定义线性回归模型](#定义线性回归模型)
   - [定义损失函数与优化器](#定义损失函数与优化器)
   - [训练模型](#训练模型)
   - [评估模型](#评估模型)
   - [完整示例代码](#完整示例代码)
   - [运行结果解析](#运行结果解析)
   - [扩展：使用更复杂的优化器](#扩展使用更复杂的优化器)
   - [常见问题](#常见问题)
10. [PyTorch 卷积神经网络](#pytorch-卷积神经网络)
   - [PyTorch 实现一个 CNN 实例](#pytorch-实现一个-cnn-实例)
   - [注意几种错误](#注意几种错误)
11. [PyTorch 循环神经网络（RNN）](#pytorch-循环神经网络rnn)
   - [PyTorch 中的 RNN 基础](#pytorch-中的-rnn-基础)
12. [PyTorch 数据集](#pytorch-数据集)
   - [torch.utils.data.Dataset](#torchutilsdatadataset)
   - [torch.utils.data.DataLoader](#torchutilsdatadataloader)
   - [使用内置数据集](#使用内置数据集)
   - [Dataset 与 DataLoader 的自定义应用](#dataset-与-dataloader-的自定义应用)
13. [PyTorch 数据转换](#pytorch-数据转换)
14. [Pytorch torch 参考手册](#pytorch-torch-参考手册)
   - [PyTorch torch  API 手册](#pytorch-torch-api-手册)
15. [PyTorch torch.nn 参考手册](#pytorch-torchnn-参考手册)
   - [PyTorch torch.nn 模块参考手册](#pytorch-torchnn-模块参考手册)
   - [实例：使用 CNN 进行图像分类](#实例使用-cnn-进行图像分类)
   - [实例：使用 LSTM 进行文本分类](#实例使用-lstm-进行文本分类)
   - [实例：使用 Transformer 编码器](#实例使用-transformer-编码器)
16. [Transformer 模型](#transformer-模型)
   - [Transformer 的核心思想](#transformer-的核心思想)
   - [Transformer 的优势](#transformer-的优势)
   - [Transformer 的应用](#transformer-的应用)
   - [PyTorch 实现 Transformer](#pytorch-实现-transformer)
17. [PyTorch 构建 Transformer 模型](#pytorch-构建-transformer-模型)
   - [使用 PyTorch 构建 Transformer 模型](#使用-pytorch-构建-transformer-模型)
18. [PyTorch torch.optim 优化器模块](#pytorch-torchoptim-优化器模块)
   - [为什么需要优化器](#为什么需要优化器)
   - [常见优化器类型](#常见优化器类型)
   - [优化器核心 API](#优化器核心-api)
   - [常用优化器详解](#常用优化器详解)
   - [优化器高级技巧](#优化器高级技巧)
   - [实例：多种学习率调度器](#实例多种学习率调度器)
   - [完整训练示例](#完整训练示例)
   - [优化器选择指南](#优化器选择指南)
19. [PyTorch torchvision 计算机视觉模块](#pytorch-torchvision-计算机视觉模块)
   - [核心组件解析](#核心组件解析)
   - [实战示例：图像分类流程](#实战示例图像分类流程)
   - [高级功能](#高级功能)
   - [最佳实践建议](#最佳实践建议)
20. [PyTorch 模型部署](#pytorch-模型部署)
   - [模型准备与优化](#模型准备与优化)
   - [部署方案选择](#部署方案选择)
   - [性能优化技巧](#性能优化技巧)
   - [常见问题解答](#常见问题解答)
21. [PyTorch 模型保存和加载](#pytorch-模型保存和加载)
   - [基本保存和加载方法](#基本保存和加载方法)
   - [保存和加载训练状态](#保存和加载训练状态)
   - [跨设备加载模型](#跨设备加载模型)
   - [模型转换与兼容性](#模型转换与兼容性)
   - [最佳实践与常见问题](#最佳实践与常见问题)
   - [实际应用示例](#实际应用示例)
22. [PyTorch 实例 - 图像分类项目](#pytorch-实例---图像分类项目)
   - [环境准备与数据加载](#环境准备与数据加载)
   - [构建卷积神经网络模型](#构建卷积神经网络模型)
   - [训练模型](#训练模型)
   - [模型评估](#模型评估)
   - [模型保存与加载](#模型保存与加载)
23. [PyTorch 实例 - 文本情感分析项目](#pytorch-实例---文本情感分析项目)
   - [环境准备](#环境准备)
   - [数据准备](#数据准备)
   - [模型构建](#模型构建)
   - [模型训练](#模型训练)
   - [模型评估](#模型评估)
   - [模型应用](#模型应用)
24. [PyTorch Autograd 自动微分](#pytorch-autograd-自动微分)
   - [核心概念](#核心概念)
   - [backward() 反向传播](#backward-反向传播)
   - [torch.no_grad() 停止梯度追踪](#torchno_grad-停止梯度追踪)
   - [detach() 从计算图中分离](#detach-从计算图中分离)
   - [retain_graph 保留计算图](#retain_graph-保留计算图)
   - [梯度在神经网络训练中的应用](#梯度在神经网络训练中的应用)
   - [常用 API 速查表](#常用-api-速查表)
   - [常见问题与注意事项](#常见问题与注意事项)
25. [PyTorch GPU / CUDA 加速](#pytorch-gpu-cuda-加速)
   - [1. CPU 与 GPU 的差异](#1-cpu-与-gpu-的差异)
   - [2. 检测 CUDA 环境](#2-检测-cuda-环境)
   - [3. 张量在设备间移动](#3-张量在设备间移动)
   - [4. 模型移动到 GPU](#4-模型移动到-gpu)
   - [5. 完整训练流程](#5-完整训练流程)
   - [6. 多 GPU 训练](#6-多-gpu-训练)
   - [7. 混合精度训练 AMP](#7-混合精度训练-amp)
   - [8. 性能优化技巧](#8-性能优化技巧)
   - [9. 常见错误与排查](#9-常见错误与排查)
   - [10. API 快速参考](#10-api-快速参考)
26. [PyTorch 损失函数](#pytorch-损失函数)
   - [1. 损失函数基础](#1-损失函数基础)
   - [2. 分类任务损失函数](#2-分类任务损失函数)
   - [3. 回归任务损失函数](#3-回归任务损失函数)
   - [4. 进阶损失函数](#4-进阶损失函数)
   - [5. reduction 参数详解](#5-reduction-参数详解)
   - [6. 类别权重与样本权重](#6-类别权重与样本权重)
   - [7. 自定义损失函数](#7-自定义损失函数)
   - [8. 损失函数选择指南](#8-损失函数选择指南)
   - [完整训练示例](#完整训练示例)
27. [PyTorch 学习率调度器](#pytorch-学习率调度器)
   - [1. 基础概念与使用模式](#1-基础概念与使用模式)
   - [2. 固定衰减调度器](#2-固定衰减调度器)
   - [3. 自适应调度器](#3-自适应调度器)
   - [4. 预热调度器](#4-预热调度器)
   - [5. 循环调度器](#5-循环调度器)
   - [6. 自定义调度器](#6-自定义调度器)
   - [7. 调度器可视化对比](#7-调度器可视化对比)
   - [8. 完整训练模板](#8-完整训练模板)
   - [9. 调度器选择指南](#9-调度器选择指南)
28. [PyTorch 迁移学习](#pytorch-迁移学习)
   - [1. 迁移学习核心思想](#1-迁移学习核心思想)
   - [2. 加载预训练模型](#2-加载预训练模型)
   - [3. 三种迁移策略](#3-三种迁移策略)
   - [4. 常用预训练模型](#4-常用预训练模型)
   - [5. 数据预处理与增强](#5-数据预处理与增强)
   - [6. 完整实战：图像二分类](#6-完整实战图像二分类)
   - [7. 完整实战：文本分类（BERT）](#7-完整实战文本分类bert)
   - [8. 模型结构修改技巧](#8-模型结构修改技巧)
   - [9. 迁移学习最佳实践](#9-迁移学习最佳实践)
29. [PyTorch 批归一化与 Dropout](#pytorch-批归一化与-dropout)
   - [1. 批归一化（Batch Normalization）](#1-批归一化batch-normalization)
   - [选择建议速查](#选择建议速查)
   - [2. Dropout](#2-dropout)
   - [3. 训练模式与评估模式](#3-训练模式与评估模式)
   - [4. 在网络中的使用位置](#4-在网络中的使用位置)
   - [流派一：激活函数之前（原始论文）](#流派一激活函数之前原始论文)
   - [流派二：激活函数之后（部分研究认为效果更好）](#流派二激活函数之后部分研究认为效果更好)
   - [全连接网络：放在激活函数之后](#全连接网络放在激活函数之后)
   - [CNN：放在 BN 之后（如有 BN 则 Dropout 可省略）](#cnn放在-bn-之后如有-bn-则-dropout-可省略)
   - [Transformer：放在 FFN 和注意力层内部](#transformer放在-ffn-和注意力层内部)
   - [全连接网络：可以同时使用](#全连接网络可以同时使用)
   - [5. 完整网络实例](#5-完整网络实例)
   - [6. 超参数调优指南](#6-超参数调优指南)
   - [7. 常见错误与注意事项](#7-常见错误与注意事项)
   - [错误写法](#错误写法)
   - [正确写法](#正确写法)
   - [错误写法](#错误写法)
   - [正确写法](#正确写法)
   - [错误写法](#错误写法)
   - [解决方案](#解决方案)
   - [问题](#问题)
   - [解决方案](#解决方案)
   - [错误写法](#错误写法)
   - [正确写法](#正确写法)
30. [PyTorch LSTM / GRU](#pytorch-lstm-gru)
   - [1. RNN 的局限与门控机制](#1-rnn-的局限与门控机制)
   - [2. LSTM 原理](#2-lstm-原理)
   - [3. GRU 原理](#3-gru-原理)
   - [4. PyTorch 中的 LSTM](#4-pytorch-中的-lstm)
   - [5. PyTorch 中的 GRU](#5-pytorch-中的-gru)
   - [6. LSTM 与 GRU 的变体](#6-lstm-与-gru-的变体)
   - [7. 处理变长序列](#7-处理变长序列)
   - [8. 完整实战：文本情感分类](#8-完整实战文本情感分类)
   - [9. 完整实战：时间序列预测](#9-完整实战时间序列预测)
   - [10. LSTM 与 GRU 对比及选型](#10-lstm-与-gru-对比及选型)
31. [PyTorch 词嵌入 (Embedding)](#pytorch-词嵌入-embedding)
   - [1. 词嵌入基础概念](#1-词嵌入基础概念)
   - [2. nn.Embedding 详解](#2-nnembedding-详解)
   - [3. 加载预训练词嵌入](#3-加载预训练词嵌入)
   - [4. 嵌入层与 RNN/LSTM 结合](#4-嵌入层与-rnnlstm-结合)
   - [5. 位置编码 (Positional Encoding)](#5-位置编码-positional-encoding)
   - [6. 嵌入层的进阶技巧](#6-嵌入层的进阶技巧)
   - [7. 完整实战：文本分类模型](#7-完整实战文本分类模型)
   - [8. API 快速参考](#8-api-快速参考)
32. [PyTorch 生成对抗网络 (GAN)](#pytorch-生成对抗网络-gan)
   - [1. GAN 核心原理](#1-gan-核心原理)
   - [2. 基础 GAN 实现](#2-基础-gan-实现)
   - [3. DCGAN - 深度卷积 GAN](#3-dcgan---深度卷积-gan)
   - [4. GAN 的训练技巧](#4-gan-的训练技巧)
   - [5. 条件 GAN (cGAN)](#5-条件-gan-cgan)
   - [6. GAN 评估指标](#6-gan-评估指标)
   - [7. 常见 GAN 变体](#7-常见-gan-变体)
33. [PyTorch 自编码器 (Autoencoder)](#pytorch-自编码器-autoencoder)
   - [1. 自编码器基础原理](#1-自编码器基础原理)
   - [2. 基础自编码器实现](#2-基础自编码器实现)
   - [3. 去噪自编码器 (DAE)](#3-去噪自编码器-dae)
   - [4. 变分自编码器 (VAE)](#4-变分自编码器-vae)
   - [5. 稀疏自编码器](#5-稀疏自编码器)
   - [6. 序列到序列自编码器](#6-序列到序列自编码器)
   - [7. 自编码器的应用场景](#7-自编码器的应用场景)
   - [8. API 快速参考](#8-api-快速参考)
34. [PyTorch 模型评估与调试](#pytorch-模型评估与调试)
   - [1. 损失函数 (Loss) 分析](#1-损失函数-loss-分析)
   - [2. 过拟合与欠拟合处理](#2-过拟合与欠拟合处理)
   - [3. 混淆矩阵 (Confusion Matrix)](#3-混淆矩阵-confusion-matrix)
   - [4. 学习率调度](#4-学习率调度)
   - [5. 梯度问题诊断](#5-梯度问题诊断)
   - [6. 模型性能分析](#6-模型性能分析)
   - [7. 常见问题与调试技巧](#7-常见问题与调试技巧)
   - [8. PyTorch Profiler 使用](#8-pytorch-profiler-使用)
35. [PyTorch torchtext](#pytorch-torchtext)
   - [1. 文本数据预处理基础](#1-文本数据预处理基础)
   - [2. 使用 torchtext (Legacy)](#2-使用-torchtext-legacy)
   - [4. 预训练词向量加载](#4-预训练词向量加载)
   - [5. 文本数据增强](#5-文本数据增强)
   - [6. 常见 NLP 任务示例](#6-常见-nlp-任务示例)
   - [7. 替代方案推荐](#7-替代方案推荐)
   - [8. API 快速参考](#8-api-快速参考)
36. [PyTorch 混合精度训练 (AMP)](#pytorch-混合精度训练-amp)
   - [1. 混合精度训练基础](#1-混合精度训练基础)
   - [2. PyTorch AMP 基础用法](#2-pytorch-amp-基础用法)
   - [3. 进阶技巧与优化](#3-进阶技巧与优化)
   - [4. 常见问题与解决方案](#4-常见问题与解决方案)
   - [5. 性能对比与最佳实践](#5-性能对比与最佳实践)
   - [6. 与其他优化技术的结合](#6-与其他优化技术的结合)
   - [总结](#总结)
37. [PyTorch TorchScript / ONNX 导出](#pytorch-torchscript-onnx-导出)
   - [1. TorchScript 基础](#1-torchscript-基础)
   - [2. TorchScript 追踪 (Tracing)](#2-torchscript-追踪-tracing)
   - [3. TorchScript 脚本 (Scripting)](#3-torchscript-脚本-scripting)
   - [4. ONNX 导出](#4-onnx-导出)
   - [5. 导出的验证与优化](#5-导出的验证与优化)
   - [6. 移动端部署](#6-移动端部署)
   - [7. 最佳实践与常见问题](#7-最佳实践与常见问题)
38. [PyTorch 分布式训练](#pytorch-分布式训练)
   - [1. 分布式训练基础](#1-分布式训练基础)
   - [2. DataParallel 使用指南](#2-dataparallel-使用指南)
   - [3. DistributedDataParallel 详解](#3-distributeddataparallel-详解)
   - [4. 分布式训练中的混合精度](#4-分布式训练中的混合精度)
   - [5. 模型并行与流水线](#5-模型并行与流水线)
   - [6. 分布式训练最佳实践](#6-分布式训练最佳实践)
   - [7. 分布式训练监控与调试](#7-分布式训练监控与调试)
39. [PyTorch 注意力机制](#pytorch-注意力机制)
   - [1. 注意力机制基础](#1-注意力机制基础)
   - [2. PyTorch 注意力模块](#2-pytorch-注意力模块)
   - [3. 注意力机制的变体](#3-注意力机制的变体)
   - [4. 注意力机制的视觉应用](#4-注意力机制的视觉应用)
   - [5. 注意力机制在 NLP 中的应用](#5-注意力机制在-nlp-中的应用)
   - [6. 完整的注意力分类器](#6-完整的注意力分类器)
   - [7. 最佳实践与常见问题](#7-最佳实践与常见问题)

---

# PyTorch 简介

PyTorch 是一个开源的 Python 机器学习库，基于 Torch 库，底层由 C++ 实现，应用于人工智能领域，如计算机视觉和自然语言处理。

PyTorch 最初由 Meta Platforms 的人工智能研究团队开发，现在属 于Linux 基金会的一部分。

许多深度学习软件都是基于 PyTorch 构建的，包括特斯拉自动驾驶、Uber 的 Pyro、Hugging Face 的 Transformers、 PyTorch Lightning 和 Catalyst。

**PyTorch 主要有两大特征：**

-
类似于 NumPy 的张量计算，能在 GPU 或 MPS 等硬件加速器上加速。

-
基于带自动微分系统的深度神经网络。

PyTorch 包括 torch.autograd、torch.nn、torch.optim 等子模块。

PyTorch 包含多种损失函数，包括 MSE（均方误差 = L2 范数）、交叉熵损失和负熵似然损失（对分类器有用）等。

## PyTorch 特性

-

**动态计算图（Dynamic Computation Graphs）**：
            PyTorch 的计算图是动态的，这意味着它们在运行时构建，并且可以随时改变。这为实验和调试提供了极大的灵活性，因为开发者可以逐行执行代码，查看中间结果。

-

**自动微分（Automatic Differentiation）**：
            PyTorch 的自动微分系统允许开发者轻松地计算梯度，这对于训练深度学习模型至关重要。它通过反向传播算法自动计算出损失函数对模型参数的梯度。

-

**张量计算（Tensor Computation）**：
            PyTorch 提供了类似于 NumPy 的张量操作，这些操作可以在 CPU 和 GPU 上执行，从而加速计算过程。张量是 PyTorch 中的基本数据结构，用于存储和操作数据。

-

**丰富的 API**：
            PyTorch 提供了大量的预定义层、损失函数和优化算法，这些都是构建深度学习模型的常用组件。

-

**多语言支持**：
            PyTorch 虽然以 Python 为主要接口，但也提供了 C++ 接口，允许更底层的集成和控制。

### 动态计算图（Dynamic Computation Graph）

PyTorch 最显著的特点之一是其动态计算图的机制。

与 TensorFlow 的静态计算图（graph）不同，PyTorch 在执行时构建计算图，这意味着在每次计算时，图都会根据输入数据的形状自动变化。

**动态计算图的优点：**

- 更加灵活，特别适用于需要条件判断或递归的场景。
- 方便调试和修改，能够直接查看中间结果。
- 更接近 Python 编程的风格，易于上手。

### 张量（Tensor）与自动求导（Autograd）

PyTorch 中的核心数据结构是 **张量（Tensor）**，它是一个多维矩阵，可以在 CPU 或 GPU 上高效地进行计算。张量的操作支持自动求导（Autograd）机制，使得在反向传播过程中自动计算梯度，这对于深度学习中的梯度下降优化算法至关重要。

**张量（Tensor）：**

- 支持在 CPU 和 GPU 之间进行切换。

- 提供了类似 NumPy 的接口，支持元素级运算。

- 支持自动求导，可以方便地进行梯度计算。

**自动求导（Autograd）：**

- PyTorch 内置的自动求导引擎，能够自动追踪所有张量的操作，并在反向传播时计算梯度。

- 通过 `requires_grad` 属性，可以指定张量需要计算梯度。

- 支持高效的反向传播，适用于神经网络的训练。

### 模型定义与训练

PyTorch 提供了 `torch.nn` 模块，允许用户通过继承 `nn.Module` 类来定义神经网络模型。使用 `forward` 函数指定前向传播，自动反向传播（通过 `autograd`）和梯度计算也由 PyTorch 内部处理。

**神经网络模块（torch.nn）：**

- 提供了常用的层（如线性层、卷积层、池化层等）。

- 支持定义复杂的神经网络架构（包括多输入、多输出的网络）。

- 兼容与优化器（如 `torch.optim`）一起使用。

### GPU 加速

PyTorch 完全支持在 GPU 上运行，以加速深度学习模型的训练。通过简单的 `.to(device)` 方法，用户可以将模型和张量转移到 GPU 上进行计算。PyTorch 支持多 GPU 训练，能够利用 NVIDIA CUDA 技术显著提高计算效率。

**GPU 支持：**

- 自动选择 GPU 或 CPU。

- 支持通过 CUDA 加速运算。

- 支持多 GPU 并行计算（`DataParallel` 或 `torch.distributed`）。

### 生态系统与社区支持

PyTorch 作为一个开源项目，拥有一个庞大的社区和生态系统。它不仅在学术界得到了广泛的应用，也在工业界，特别是在计算机视觉、自然语言处理等领域中得到了广泛部署。PyTorch 还提供了许多与深度学习相关的工具和库，如：

- **torchvision**：用于计算机视觉任务的数据集和模型。

- **torchtext**：用于自然语言处理任务的数据集和预处理工具。

- **torchaudio**：用于音频处理的工具包。

- **PyTorch Lightning**：一种简化 PyTorch 代码的高层库，专注于研究和实验的快速迭代。

## 与其他框架的对比

PyTorch 由于其灵活性、易用性和社区支持，已经成为很多深度学习研究者和开发者的首选框架。

### TensorFlow vs PyTorch

- PyTorch 的动态计算图使得它更加灵活，适合快速实验和研究；而 TensorFlow 的静态计算图在生产环境中更具优化空间。

- PyTorch 在调试时更加方便，TensorFlow 则在部署上更加成熟，支持更广泛的硬件和平台。

- 近年来，TensorFlow 也引入了动态图（如 TensorFlow 2.x），使得两者在功能上趋于接近。

- 其他深度学习框架，如 Keras、Caffe 等也有一定应用，但 PyTorch 由于其灵活性、易用性和社区支持，已经成为很多深度学习研究者和开发者的首选框架。

| 特性 | TensorFlow | PyTorch |
| --- | --- | --- |
| 开发公司 | Google | Facebook (FAIR) |
| 计算图类型 | 静态计算图（定义后再执行） | 动态计算图（定义即执行） |
| 灵活性 | 低（计算图在编译时构建，不易修改） | 高（计算图在执行时动态创建，易于修改和调试） |
| 调试 | 较难（需要使用 tf.debugging 或外部工具调试） | 容易（可以直接在 Python 中进行调试） |
| 易用性 | 低（较复杂，API 较多，学习曲线较陡峭） | 高（API 简洁，语法更加接近 Python，容易上手） |
| 部署 | 强（支持广泛的硬件，如 TensorFlow Lite、TensorFlow.js） | 较弱（部署工具和平台相对较少，虽然有 TensorFlow 支持） |
| 社区支持 | 很强（成熟且庞大的社区，广泛的教程和文档） | 很强（社区活跃，特别是在学术界，快速发展的生态） |
| 模型训练 | 支持分布式训练，支持多种设备（如 CPU、GPU、TPU） | 支持分布式训练，支持多 GPU、CPU 和 TPU |
| API 层级 | 高级API：Keras；低级API：TensorFlow Core | 高级API：TorchVision、TorchText 等；低级API：Torch |
| 性能 | 高（优化方面成熟，适合生产环境） | 高（适合研究和原型开发，生产性能也在提升） |
| 自动求导 | 通过 tf.GradientTape 实现动态求导（较复杂） | 通过 autograd 动态求导（更简洁和直观） |
| 调优与可扩展性 | 强（支持在多平台上运行，如 TensorFlow Serving 等） | 较弱（虽然在学术和实验环境中表现优越，但生产环境支持相对较少） |
| 框架灵活性 | 较低（TensorFlow 2.x 引入了动态图特性，但仍不完全灵活） | 高（动态图带来更高的灵活性） |
| 支持多种语言 | 支持多种语言（Python, C++, Java, JavaScript, etc.） | 主要支持 Python（但也有 C++ API） |
| 兼容性与迁移 | TensorFlow 2.x 与旧版本兼容性较好 | 与 TensorFlow 兼容性差，迁移较难 |

### PyTorch vs NumPy

| 特性 | PyTorch | NumPy |
| --- | --- | --- |
| 目标 | 深度学习专用 | 通用科学计算 |
| GPU 支持 | 原生支持 CUDA | 不直接支持 |
| 自动微分 | 内置自动求导 | 需要手动计算梯度 |
| 神经网络 | 丰富的神经网络模块 | 需要从零实现 |
| 学习成本 | 相对较高 | 相对较低 |

## PyTorch 的历史与发展

PyTorch 的前身是 Torch，这是一个基于 Lua 语言的科学计算框架。随着 Python 在机器学习领域的兴起，Facebook 团队决定将 Torch 的核心思想移植到 Python 上，从而诞生了 PyTorch。

- **2016年**：Facebook 发布 PyTorch 0.1 版本

- **2017年**：PyTorch 0.2 引入分布式训练支持

- **2018年**：PyTorch 1.0 发布，增加了生产部署能力

- **2019年**：PyTorch 1.3 引入移动端支持

- **2020年**：PyTorch 1.6 增加了自动混合精度训练

- **2021年**：PyTorch 1.9 引入 TorchScript 和 C++ 前端

- **2022年**：PyTorch 1.12 优化了性能和稳定性

- **2023年**：PyTorch 2.0 发布，引入编译模式大幅提升性能

---

# PyTorch 安装

PyTorch 是一个流行的深度学习框架，支持 CPU 和 GPU 计算。

### 支持的操作系统

- **Windows**：Windows 10 或更高版本（64位）

- **macOS**：macOS 10.15 (Catalina) 或更高版本

- **Linux**：主流发行版（Ubuntu 18.04+、CentOS 7+、RHEL 7+等）

### Python 版本要求

- **推荐版本**：Python 3.8 - 3.11

- **最低要求**：Python 3.7

- **注意**：Python 3.12+ 支持可能有限，建议使用稳定版本

### 硬件要求

- **CPU**：支持 SSE4.2 指令集的 x86_64 处理器

- **内存**：至少 4GB RAM（推荐 8GB+）

- **存储**：至少 3GB 可用空间

- **GPU**（可选）：NVIDIA GPU with CUDA Compute Capability 3.5+

### CUDA 兼容性（GPU 版本）

| PyTorch 版本 | 支持的 CUDA 版本 | 推荐 CUDA 版本 |
| --- | --- | --- |
| 2.1.x | 11.8, 12.1 | 12.1 |
| 2.0.x | 11.7, 11.8 | 11.8 |
| 1.13.x | 11.6, 11.7 | 11.7 |

## 安装前的准备工作

### 检查系统信息

**Windows:**

```python
# 检查 Windows 版本

winver

# 检查 Python 版本

python --version

# 检查是否有 NVIDIA GPU

nvidia-smi
```

**macOS**

```python
# 检查 macOS 版本

sw_vers

# 检查 Python 版本

python3 --version

# 检查是否有兼容的 GPU（Apple Silicon）

system_profiler SPDisplaysDataType
```

**Linux**

```python
# 检查发行版信息

cat /etc/os-release

# 检查 Python 版本

python3 --version

# 检查 NVIDIA GPU

nvidia-smi

# 检查 CUDA 版本（如果已安装）

nvcc --version
```

### Python 环境管理

**使用 Anaconda/Miniconda:**

```python
# 下载并安装 Miniconda

# Windows: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

# macOS: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

# Linux: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 创建专用环境

conda create -n pytorch_env python=3.10

conda activate pytorch_env
```

### 使用 venv（Python 自带）

```python
# 创建虚拟环境

python -m venv pytorch_env

# 激活环境

# Windows

pytorch_env\Scripts\activate

# macOS/Linux

source pytorch_env/bin/activate
```

## 安装 PyTorch

PyTorch 官方提供了几种安装方法，可以通过 pip 或 conda 进行安装。

### CPU 版本安装

**使用 pip 安装 pytorch：**

```python
# 最新稳定版本

pip install torch torchvision torchaudio

# 指定版本

pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0

# 仅 CPU 版本（更小的安装包）

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**使用 conda 安装:**

如果你使用 Anaconda 或 Miniconda 管理 Python 环境，使用 conda 安装 PyTorch 可能会更加简单和高效。

```python
# 从 conda-forge 安装

conda install pytorch torchvision torchaudio cpuonly -c pytorch

# 或从 conda-forge 渠道

conda install pytorch torchvision torchaudio -c conda-forge
```

如果不了解Anaconda，可以参考： [Anaconda 教程](/python-qt/anaconda-tutorial.html)

### 通过 PyTorch 官网安装

访问 PyTorch 的官方网站 [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)，网站提供了一个方便的工具，可以根据你的系统配置（操作系统、包管理器、Python版本以及CUDA版本）推荐安装命令。

### 从源代码安装

如果你需要从源代码安装PyTorch，或者想要尝试最新的开发版本，你可以使用以下命令：

```python
git clone --recursive https://github.com/pytorch/pytorch

cd pytorch

python setup.py install
```

这将从 GitHub 克隆 PyTorch 的源代码，并使用 setup.py 进行安装。

### GPU 版本安装（CUDA）

**安装 CUDA（如果需要）:**

```python
# Ubuntu/Debian

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin

sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-ubuntu2004-12-1-local_12.1.0-530.30.02-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu2004-12-1-local_12.1.0-530.30.02-1_amd64.deb

sudo cp /var/cuda-repo-ubuntu2004-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update

sudo apt-get -y install cuda

# CentOS/RHEL

sudo yum install -y https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-repo-rhel8-12.1.0-1.x86_64.rpm

sudo yum clean all

sudo yum -y install cuda
```

**安装 PyTorch GPU 版本:**

```python
# CUDA 12.1 版本

pip install torch torchvision torchaudio

# CUDA 11.8 版本

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 使用 conda

conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

### macOS 特殊说明

**Apple Silicon (M1/M2) Mac:**

```python
# 使用 Metal Performance Shaders (MPS) 后端

pip install torch torchvision torchaudio

# 验证 MPS 可用性

python -c "import torch; print(torch.backends.mps.is_available())"
```

**Intel Mac:**

```python
# 标准安装

pip install torch torchvision torchaudio
```

### 验证安装

为了确保 PyTorch 已正确安装，我们可以通过执行以下 PyTorch 代码来验证是否安装成功：

## 实例

```python
import torch

# 当前安装的 PyTorch 库的版本

print(torch.__version__)

# 检查 CUDA 是否可用，即你的系统有 NVIDIA 的 GPU

print(torch.cuda.is_available())
```

如果 torch.cuda.is_available() 输出 True，则说明 PyTorch 成功识别到你的 GPU。

一个简单的实例，构建一个随机初始化的张量：

## 实例

```python
import torch

x = torch.rand(5, 3)

print(x)
```

如果安装成功，输出结果类似如下：

```python
tensor([[0.3380, 0.3845, 0.3217],

[0.8337, 0.9050, 0.2650],

[0.2979, 0.7141, 0.9069],

[0.1449, 0.1132, 0.1375],

[0.4675, 0.3947, 0.1426]])
```

---

# PyTorch 基础

PyTorch 是一个开源的深度学习框架，以其灵活性和动态计算图而广受欢迎。

PyTorch 主要有以下几个基础概念：张量（Tensor）、自动求导（Autograd）、神经网络模块（nn.Module）、优化器（optim）等。

- **张量（Tensor）**：PyTorch 的核心数据结构，支持多维数组，并可以在 CPU 或 GPU 上进行加速计算。

- **自动求导（Autograd）**：PyTorch 提供了自动求导功能，可以轻松计算模型的梯度，便于进行反向传播和优化。

- **神经网络（nn.Module）**：PyTorch 提供了简单且强大的 API 来构建神经网络模型，可以方便地进行前向传播和模型定义。

- **优化器（Optimizers）**：使用优化器（如 Adam、SGD 等）来更新模型的参数，使得损失最小化。

- **设备（Device）**：可以将模型和张量移动到 GPU 上以加速计算。

## PyTorch 架构总览

PyTorch 采用模块化设计，由多个相互协作的核心组件构成。理解这些组件的作用和相互关系，是掌握 PyTorch 的关键。

### PyTorch 架构图

```python
┌─────────────────────────────────────────────────────────────┐

│                    PyTorch 生态系统                          │

├─────────────────────────────────────────────────────────────┤

│  torchvision  │  torchtext  │  torchaudio  │  其他专业库     │

├─────────────────────────────────────────────────────────────┤

│                     PyTorch 核心                            │

├───────────────┬─────────────────┬───────────────────────────┤

│   torch.nn    │   torch.optim   │      torch.utils          │

│   (神经网络)   │   (优化器)      │      (工具函数)           │

├───────────────┼─────────────────┼───────────────────────────┤

│               │                 │   torch.utils.data        │

│  torch 核心   │  autograd       │   (数据加载)              │

│  (张量计算)   │  (自动微分)     │                           │

└───────────────┴─────────────────┴───────────────────────────┘
```

PyTorch 采用**分层架构**设计，从上层到底层依次为：

**1、Python API（顶层）**

- `torch`：核心张量计算（类似NumPy，支持GPU）。

- `torch.nn`：神经网络层、损失函数等。

- `torch.autograd`：自动微分（反向传播）。

- 开发者直接调用的接口，简单易用。

**2、C++核心（中层）**

- **ATen**：张量运算核心库（400+操作）。

- **JIT**：即时编译优化模型。

- **Autograd引擎**：自动微分的底层实现。

- 高性能计算，连接Python与底层硬件。

**3、基础库（底层）**

- **TH/THNN**：C语言实现的基础张量和神经网络操作。

- **THC/THCUNN**：对应的CUDA（GPU）版本。

- 直接操作硬件（CPU/GPU），极致优化速度。

**执行流程**：
Python代码 → C++核心计算 → 底层CUDA/C库加速 → 返回结果。
既保持易用性，又确保高性能。

## 张量（Tensor）

张量（Tensor）是 PyTorch 中的核心数据结构，用于存储和操作多维数组。

张量可以视为一个多维数组，支持加速计算的操作。

在 PyTorch 中，张量的概念类似于 NumPy 中的数组，但是 PyTorch 的张量可以运行在不同的设备上，比如 CPU 和 GPU，这使得它们非常适合于进行大规模并行计算，特别是在深度学习领域。

-

**维度（Dimensionality）**：张量的维度指的是数据的多维数组结构。例如，一个标量（0维张量）是一个单独的数字，一个向量（1维张量）是一个一维数组，一个矩阵（2维张量）是一个二维数组，以此类推。

-

**形状（Shape）**：张量的形状是指每个维度上的大小。例如，一个形状为`(3, 4)`的张量意味着它有3行4列。

-

**数据类型（Dtype）**：张量中的数据类型定义了存储每个元素所需的内存大小和解释方式。PyTorch支持多种数据类型，包括整数型（如`torch.int8`、`torch.int32`）、浮点型（如`torch.float32`、`torch.float64`）和布尔型（`torch.bool`）。

**张量创建：**

## 实例

```python
import torch

# 创建一个 2x3 的全 0 张量

a = torch.zeros(2, 3)

print(a)

# 创建一个 2x3 的全 1 张量

b = torch.ones(2, 3)

print(b)

# 创建一个 2x3 的随机数张量

c = torch.randn(2, 3)

print(c)

# 从 NumPy 数组创建张量

import numpy as np

numpy_array = np.array([[1, 2], [3, 4]])

tensor_from_numpy = torch.from_numpy(numpy_array)

print(tensor_from_numpy)

# 在指定设备（CPU/GPU）上创建张量

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

d = torch.randn(2, 3, device=device)

print(d)
```

输出结果类似如下：

```python
tensor([[0., 0., 0.],

[0., 0., 0.]])

tensor([[1., 1., 1.],

[1., 1., 1.]])

tensor([[ 1.0189, -0.5718, -1.2814],

[-0.5865,  1.0855,  1.1727]])

tensor([[1, 2],

[3, 4]])

tensor([[-0.3360,  0.2203,  1.3463],

[-0.5982, -0.2704,  0.5429]])
```

**常用张量操作：**

## 实例

```python
# 张量相加

e = torch.randn(2, 3)

f = torch.randn(2, 3)

print(e + f)

# 逐元素乘法

print(e * f)

# 张量的转置

g = torch.randn(3, 2)

print(g.t())  # 或者 g.transpose(0, 1)

# 张量的形状

print(g.shape)  # 返回形状
```

### 张量与设备

PyTorch 张量可以存在于不同的设备上，包括CPU和GPU，你可以将张量移动到 GPU 上以加速计算：

```python
if torch.cuda.is_available():

tensor_gpu = tensor_from_list.to('cuda')  # 将张量移动到GPU
```

### 梯度和自动微分

PyTorch的张量支持自动微分，这是深度学习中的关键特性。当你创建一个需要梯度的张量时，PyTorch可以自动计算其梯度：

## 实例

```python
# 创建一个需要梯度的张量

tensor_requires_grad = torch.tensor([1.0], requires_grad=True)

# 进行一些操作

tensor_result = tensor_requires_grad * 2

# 计算梯度

tensor_result.backward()

print(tensor_requires_grad.grad)  # 输出梯度
```

### 内存和性能

PyTorch 张量还提供了一些内存管理功能，比如.clone()、.detach() 和 .to() 方法，它们可以帮助你优化内存使用和提高性能。

## 自动求导（Autograd）

自动求导（Automatic Differentiation，简称Autograd）是深度学习框架中的一个核心特性，它允许计算机自动计算数学函数的导数。

在深度学习中，自动求导主要用于两个方面：**一是在训练神经网络时计算梯度**，**二是进行反向传播算法的实现**。

自动求导基于链式法则（Chain Rule），这是一个用于计算复杂函数导数的数学法则。链式法则表明，复合函数的导数是其各个组成部分导数的乘积。在深度学习中，模型通常是由许多层组成的复杂函数，自动求导能够高效地计算这些层的梯度。

**动态图与静态图：**

-

**动态图（Dynamic Graph）**：在动态图中，计算图在运行时动态构建。每次执行操作时，计算图都会更新，这使得调试和修改模型变得更加容易。PyTorch使用的是动态图。

-

**静态图（Static Graph）**：在静态图中，计算图在开始执行之前构建完成，并且不会改变。TensorFlow最初使用的是静态图，但后来也支持动态图。

PyTorch 提供了自动求导功能，通过 autograd 模块来自动计算梯度。

torch.Tensor 对象有一个 requires_grad 属性，用于指示是否需要计算该张量的梯度。

当你创建一个 requires_grad=True 的张量时，PyTorch 会自动跟踪所有对它的操作，以便在之后计算梯度。

创建需要梯度的张量:

## 实例

```python
# 创建一个需要计算梯度的张量

x = torch.randn(2, 2, requires_grad=True)

print(x)

# 执行某些操作

y = x + 2

z = y * y * 3

out = z.mean()

print(out)
```

输出结果类似如下：

```python
tensor([[0., 0., 0.],

[0., 0., 0.]])

tensor([[1., 1., 1.],

[1., 1., 1.]])

tensor([[ 1.0189, -0.5718, -1.2814],

[-0.5865,  1.0855,  1.1727]])

tensor([[1, 2],

[3, 4]])

tensor([[-0.3360,  0.2203,  1.3463],

[-0.5982, -0.2704,  0.5429]])

tianqixin@Mac-mini runoob-test % python3 test.py

tensor([[-0.1908,  0.2811],

[ 0.8068,  0.8002]], requires_grad=True)

tensor(18.1469, grad_fn=<MeanBackward0>)
```

### 反向传播（Backpropagation）

一旦定义了计算图，可以通过 .backward() 方法来计算梯度。

## 实例

```python
# 反向传播，计算梯度

out.backward()

# 查看 x 的梯度

print(x.grad)
```

在神经网络训练中，自动求导主要用于实现反向传播算法。

反向传播是一种通过计算损失函数关于网络参数的梯度来训练神经网络的方法。在每次迭代中，网络的前向传播会计算输出和损失，然后反向传播会计算损失关于每个参数的梯度，并使用这些梯度来更新参数。

### 停止梯度计算

如果你不希望某些张量的梯度被计算（例如，当你不需要反向传播时），可以使用 torch.no_grad() 或设置 requires_grad=False。

## 实例

```python
# 使用 torch.no_grad() 禁用梯度计算

with torch.no_grad():

    y = x * 2
```

## 神经网络（nn.Module）

神经网络是一种模仿人脑神经元连接的计算模型，由多层节点（神经元）组成，用于学习数据之间的复杂模式和关系。

神经网络通过调整神经元之间的连接权重来优化预测结果，这一过程涉及前向传播、损失计算、反向传播和参数更新。

神经网络的类型包括前馈神经网络、卷积神经网络（CNN）、循环神经网络（RNN）和长短期记忆网络（LSTM），它们在图像识别、语音处理、自然语言处理等多个领域都有广泛应用。

PyTorch 提供了一个非常方便的接口来构建神经网络模型，即 torch.nn.Module。

我们可以继承 nn.Module 类并定义自己的网络层。

创建一个简单的神经网络：

## 实例

```python
import torch.nn as nn

import torch.optim as optim

# 定义一个简单的全连接神经网络

class SimpleNN(nn.Module):

    def __init__(self):

        super(SimpleNN, self).__init__()

        self.fc1 = nn.Linear(2, 2)  # 输入层到隐藏层

        self.fc2 = nn.Linear(2, 1)  # 隐藏层到输出层

    

    def forward(self, x):

        x = torch.relu(self.fc1(x))  # ReLU 激活函数

        x = self.fc2(x)

        return x

# 创建网络实例

model = SimpleNN()

# 打印模型结构

print(model)
```

输出结果：

```python
SimpleNN(

(fc1): Linear(in_features=2, out_features=2, bias=True)

(fc2): Linear(in_features=2, out_features=1, bias=True)

)
```

**训练过程：**

-

**前向传播（Forward Propagation）**：
    在前向传播阶段，输入数据通过网络层传递，每层应用权重和激活函数，直到产生输出。

-

**计算损失（Calculate Loss）**：
    根据网络的输出和真实标签，计算损失函数的值。

-

**反向传播（Backpropagation）**：
    反向传播利用自动求导技术计算损失函数关于每个参数的梯度。

-

**参数更新（Parameter Update）**：
    使用优化器根据梯度更新网络的权重和偏置。

-

**迭代（Iteration）**：
    重复上述过程，直到模型在训练数据上的性能达到满意的水平。

### 前向传播与损失计算

## 实例

```python
# 随机输入

x = torch.randn(1, 2)

# 前向传播

output = model(x)

print(output)

# 定义损失函数（例如均方误差 MSE）

criterion = nn.MSELoss()

# 假设目标值为 1

target = torch.randn(1, 1)

# 计算损失

loss = criterion(output, target)

print(loss)
```

### 优化器（Optimizers）

优化器在训练过程中更新神经网络的参数，以减少损失函数的值。

PyTorch 提供了多种优化器，例如 SGD、Adam 等。

使用优化器进行参数更新：

## 实例

```python
# 定义优化器（使用 Adam 优化器）

optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练步骤

optimizer.zero_grad()  # 清空梯度

loss.backward()  # 反向传播

optimizer.step()  # 更新参数
```

## 训练模型

训练模型是机器学习和深度学习中的核心过程，旨在通过大量数据学习模型参数，以便模型能够对新的、未见过的数据做出准确的预测。

训练模型通常包括以下几个步骤：

-

**数据准备**：

- 收集和处理数据，包括清洗、标准化和归一化。

- 将数据分为训练集、验证集和测试集。

-

**定义模型**：

- 选择模型架构，例如决策树、神经网络等。

- 初始化模型参数（权重和偏置）。

-

**选择损失函数**：

- 根据任务类型（如分类、回归）选择合适的损失函数。

-

**选择优化器**：

- 选择一个优化算法，如SGD、Adam等，来更新模型参数。

-

**前向传播**：

- 在每次迭代中，将输入数据通过模型传递，计算预测输出。

-

**计算损失**：

- 使用损失函数评估预测输出与真实标签之间的差异。

-

**反向传播**：

- 利用自动求导计算损失相对于模型参数的梯度。

-

**参数更新**：

- 根据计算出的梯度和优化器的策略更新模型参数。

-

**迭代优化**：

- 重复步骤5-8，直到模型在验证集上的性能不再提升或达到预定的迭代次数。

-

**评估和测试**：

- 使用测试集评估模型的最终性能，确保模型没有过拟合。

-

**模型调优**：

- 根据模型在测试集上的表现进行调参，如改变学习率、增加正则化等。

-

**部署模型**：

- 将训练好的模型部署到生产环境中，用于实际的预测任务。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

# 1. 定义一个简单的神经网络模型

class SimpleNN(nn.Module):

    def __init__(self):

        super(SimpleNN, self).__init__()

        self.fc1 = nn.Linear(2, 2)  # 输入层到隐藏层

        self.fc2 = nn.Linear(2, 1)  # 隐藏层到输出层

    

    def forward(self, x):

        x = torch.relu(self.fc1(x))  # ReLU 激活函数

        x = self.fc2(x)

        return x

# 2. 创建模型实例

model = SimpleNN()

# 3. 定义损失函数和优化器

criterion = nn.MSELoss()  # 均方误差损失函数

optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam 优化器

# 4. 假设我们有训练数据 X 和 Y

X = torch.randn(10, 2)  # 10 个样本，2 个特征

Y = torch.randn(10, 1)  # 10 个目标值

# 5. 训练循环

for epoch in range(100):  # 训练 100 轮

    optimizer.zero_grad()  # 清空之前的梯度

    output = model(X)  # 前向传播

    loss = criterion(output, Y)  # 计算损失

    loss.backward()  # 反向传播

    optimizer.step()  # 更新参数

    

    # 每 10 轮输出一次损失

    if (epoch+1) % 10 == 0:

        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
```

输出结果如下：

```python
Epoch [10/100], Loss: 1.7180

Epoch [20/100], Loss: 1.6352

Epoch [30/100], Loss: 1.5590

Epoch [40/100], Loss: 1.4896

Epoch [50/100], Loss: 1.4268

Epoch [60/100], Loss: 1.3704

Epoch [70/100], Loss: 1.3198

Epoch [80/100], Loss: 1.2747

Epoch [90/100], Loss: 1.2346

Epoch [100/100], Loss: 1.1991
```

在每 10 轮，程序会输出当前的损失值，帮助我们跟踪模型的训练进度。随着训练的进行，损失值应该会逐渐降低，表示模型在不断学习并优化其参数。

训练模型是一个迭代的过程，需要不断地调整和优化，直到达到满意的性能。这个过程涉及到大量的实验和调优，目的是使模型在新的、未见过的数据上也能有良好的泛化能力。

## 设备（Device）

PyTorch 允许你将模型和数据移动到 GPU 上进行加速。

使用 torch.device 来指定计算设备。

将模型和数据移至 GPU:

## 实例

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 将模型移动到设备

model.to(device)

# 将数据移动到设备

X = X.to(device)

Y = Y.to(device)
```

在训练过程中，所有张量和模型都应该移到同一个设备上（要么都在 CPU 上，要么都在 GPU 上）。

---

# PyTorch 张量（Tensor）

张量是一个多维数组，可以是标量、向量、矩阵或更高维度的数据结构。

在 PyTorch 中，张量（Tensor）是数据的核心表示形式，类似于 NumPy 的多维数组，但具有更强大的功能，例如支持 GPU 加速和自动梯度计算。

张量支持多种数据类型（整型、浮点型、布尔型等）。

张量可以存储在 CPU 或 GPU 中，GPU 张量可显著加速计算。

下图展示了不同维度的张量（Tensor）在 PyTorch 中的表示方法：

**说明：**

- **1D Tensor / Vector（一维张量/向量）:** 最基本的张量形式，可以看作是一个数组，图中的例子是一个包含 10 个元素的向量。
-
**2D Tensor / Matrix（二维张量/矩阵）:** 二维数组，通常用于表示矩阵，图中的例子是一个 4x5 的矩阵，包含了 20 个元素。
-
**3D Tensor / Cube（三维张量/立方体）: **三维数组，可以看作是由多个矩阵堆叠而成的立方体，图中的例子展示了一个 3x4x5 的立方体，其中每个 5x5 的矩阵代表立方体的一个"层"。
-
**4D Tensor / Vector of Cubes（四维张量/立方体向量）:** 四维数组，可以看作是由多个立方体组成的向量，图中的例子没有具体数值，但可以理解为一个包含多个 3D 张量的集合。
-
**5D Tensor / Matrix of Cubes（五维张量/立方体矩阵）:** 五维数组，可以看作是由多个4D张量组成的矩阵，图中的例子同样没有具体数值，但可以理解为一个包含多个 4D 张量的集合。

## 创建张量

张量创建的方式有：

| 方法 | 说明 | 示例代码 |
| --- | --- | --- |
| torch.tensor(data) | 从 Python 列表或 NumPy 数组创建张量。 | x = torch.tensor([[1, 2], [3, 4]]) |
| torch.zeros(size) | 创建一个全为零的张量。 | x = torch.zeros((2, 3)) |
| torch.ones(size) | 创建一个全为 1 的张量。 | x = torch.ones((2, 3)) |
| torch.empty(size) | 创建一个未初始化的张量。 | x = torch.empty((2, 3)) |
| torch.rand(size) | 创建一个服从均匀分布的随机张量，值在 [0, 1)。 | x = torch.rand((2, 3)) |
| torch.randn(size) | 创建一个服从正态分布的随机张量，均值为 0，标准差为 1。 | x = torch.randn((2, 3)) |
| torch.arange(start, end, step) | 创建一个一维序列张量，类似于 Python 的 range。 | x = torch.arange(0, 10, 2) |
| torch.linspace(start, end, steps) | 创建一个在指定范围内等间隔的序列张量。 | x = torch.linspace(0, 1, 5) |
| torch.eye(size) | 创建一个单位矩阵（对角线为 1，其他为 0）。 | x = torch.eye(3) |
| torch.from_numpy(ndarray) | 将 NumPy 数组转换为张量。 | x = torch.from_numpy(np.array([1, 2, 3])) |

使用 torch.tensor() 函数，你可以将一个列表或数组转换为张量：

## 实例

```python
import torch

tensor = torch.tensor([1, 2, 3])

print(tensor)
```

输出如下：

```python
tensor([1, 2, 3])
```

如果你有一个 NumPy 数组，可以使用 torch.from_numpy() 将其转换为张量：

## 实例

```python
import numpy as np

np_array = np.array([1, 2, 3])

tensor = torch.from_numpy(np_array)

print(tensor)
```

输出如下：

```python
tensor([1, 2, 3])
```

 创建 2D 张量（矩阵）：

## 实例

```python
import torch

tensor_2d = torch.tensor([

    [-9, 4, 2, 5, 7],

    [3, 0, 12, 8, 6],

    [1, 23, -6, 45, 2],

    [22, 3, -1, 72, 6]

])

print("2D Tensor (Matrix):\n", tensor_2d)

print("Shape:", tensor_2d.shape)  # 形状
```

输出如下：

```python
2D Tensor (Matrix):

tensor([[-9,  4,  2,  5,  7],

[ 3,  0, 12,  8,  6],

[ 1, 23, -6, 45,  2],

[22,  3, -1, 72,  6]])

Shape: torch.Size([4, 5])
```

其他维度的创建：

```python
# 创建 3D 张量（立方体）

tensor_3d = torch.stack([tensor_2d, tensor_2d + 10, tensor_2d - 5])  # 堆叠 3 个 2D 张量

print("3D Tensor (Cube):\n", tensor_3d)

print("Shape:", tensor_3d.shape)  # 形状

# 创建 4D 张量（向量的立方体）

tensor_4d = torch.stack([tensor_3d, tensor_3d + 100])  # 堆叠 2 个 3D 张量

print("4D Tensor (Vector of Cubes):\n", tensor_4d)

print("Shape:", tensor_4d.shape)  # 形状

# 创建 5D 张量（矩阵的立方体）

tensor_5d = torch.stack([tensor_4d, tensor_4d + 1000])  # 堆叠 2 个 4D 张量

print("5D Tensor (Matrix of Cubes):\n", tensor_5d)

print("Shape:", tensor_5d.shape)  # 形状
```

## 张量的属性

张量的属性如下表：

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| .shape | 获取张量的形状 | tensor.shape |
| .size() | 获取张量的形状 | tensor.size() |
| .dtype | 获取张量的数据类型 | tensor.dtype |
| .device | 查看张量所在的设备 (CPU/GPU) | tensor.device |
| .dim() | 获取张量的维度数 | tensor.dim() |
| .requires_grad | 是否启用梯度计算 | tensor.requires_grad |
| .numel() | 获取张量中的元素总数 | tensor.numel() |
| .is_cuda | 检查张量是否在 GPU 上 | tensor.is_cuda |
| .T | 获取张量的转置（适用于 2D 张量） | tensor.T |
| .item() | 获取单元素张量的值 | tensor.item() |
| .is_contiguous() | 检查张量是否连续存储 | tensor.is_contiguous() |

## 实例

```python
import torch

# 创建一个 2D 张量

tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)

# 张量的属性

print("Tensor:\n", tensor)

print("Shape:", tensor.shape)  # 获取形状

print("Size:", tensor.size())  # 获取形状（另一种方法）

print("Data Type:", tensor.dtype)  # 数据类型

print("Device:", tensor.device)  # 设备

print("Dimensions:", tensor.dim())  # 维度数

print("Total Elements:", tensor.numel())  # 元素总数

print("Requires Grad:", tensor.requires_grad)  # 是否启用梯度

print("Is CUDA:", tensor.is_cuda)  # 是否在 GPU 上

print("Is Contiguous:", tensor.is_contiguous())  # 是否连续存储

# 获取单元素值

single_value = torch.tensor(42)

print("Single Element Value:", single_value.item())

# 转置张量

tensor_T = tensor.T

print("Transposed Tensor:\n", tensor_T)
```

输出结果：

```python
Tensor:

tensor([[1., 2., 3.],

[4., 5., 6.]])

Shape: torch.Size([2, 3])

Size: torch.Size([2, 3])

Data Type: torch.float32

Device: cpu

Dimensions: 2

Total Elements: 6

Requires Grad: False

Is CUDA: False

Is Contiguous: True

Single Element Value: 42

Transposed Tensor:

tensor([[1., 4.],

[2., 5.],

[3., 6.]])
```

## 张量的操作

张量操作方法说明如下。

#### 基础操作：

| 操作 | 说明 | 示例代码 |
| --- | --- | --- |
| +, -, *, / | 元素级加法、减法、乘法、除法。 | z = x + y |
| torch.matmul(x, y) | 矩阵乘法。 | z = torch.matmul(x, y) |
| torch.dot(x, y) | 向量点积（仅适用于 1D 张量）。 | z = torch.dot(x, y) |
| torch.sum(x) | 求和。 | z = torch.sum(x) |
| torch.mean(x) | 求均值。 | z = torch.mean(x) |
| torch.max(x) | 求最大值。 | z = torch.max(x) |
| torch.min(x) | 求最小值。 | z = torch.min(x) |
| torch.argmax(x, dim) | 返回最大值的索引（指定维度）。 | z = torch.argmax(x, dim=1) |
| torch.softmax(x, dim) | 计算 softmax（指定维度）。 | z = torch.softmax(x, dim=1) |

#### 形状操作

| 操作 | 说明 | 示例代码 |
| --- | --- | --- |
| x.view(shape) | 改变张量的形状（不改变数据）。 | z = x.view(3, 4) |
| x.reshape(shape) | 类似于 view，但更灵活。 | z = x.reshape(3, 4) |
| x.t() | 转置矩阵。 | z = x.t() |
| x.unsqueeze(dim) | 在指定维度添加一个维度。 | z = x.unsqueeze(0) |
| x.squeeze(dim) | 去掉指定维度为 1 的维度。 | z = x.squeeze(0) |
| torch.cat((x, y), dim) | 按指定维度连接多个张量。 | z = torch.cat((x, y), dim=1) |

## 实例

```python
import torch

# 创建一个 2D 张量

tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)

print("原始张量:\n", tensor)

# 1. **索引和切片操作**

print("\n【索引和切片】")

print("获取第一行:", tensor[0])  # 获取第一行

print("获取第一行第一列的元素:", tensor[0, 0])  # 获取特定元素

print("获取第二列的所有元素:", tensor[:, 1])  # 获取第二列所有元素

# 2. **形状变换操作**

print("\n【形状变换】")

reshaped = tensor.view(3, 2)  # 改变张量形状为 3x2

print("改变形状后的张量:\n", reshaped)

flattened = tensor.flatten()  # 将张量展平成一维

print("展平后的张量:\n", flattened)

# 3. **数学运算操作**

print("\n【数学运算】")

tensor_add = tensor + 10  # 张量加法

print("张量加 10:\n", tensor_add)

tensor_mul = tensor * 2  # 张量乘法

print("张量乘 2:\n", tensor_mul)

tensor_sum = tensor.sum()  # 计算所有元素的和

print("张量元素的和:", tensor_sum.item())

# 4. **与其他张量的操作**

print("\n【与其他张量操作】")

tensor2 = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)

print("另一个张量:\n", tensor2)

tensor_dot = torch.matmul(tensor, tensor2.T)  # 张量矩阵乘法

print("矩阵乘法结果:\n", tensor_dot)

# 5. **条件判断和筛选**

print("\n【条件判断和筛选】")

mask = tensor > 3  # 创建一个布尔掩码

print("大于 3 的元素的布尔掩码:\n", mask)

filtered_tensor = tensor[tensor > 3]  # 筛选出符合条件的元素

print("大于 3 的元素:\n", filtered_tensor)
```

输出结果：

```python
原始张量:

tensor([[1., 2., 3.],

[4., 5., 6.]])

【索引和切片】

获取第一行: tensor([1., 2., 3.])

获取第一行第一列的元素: tensor(1.)

获取第二列的所有元素: tensor([2., 5.])

【形状变换】

改变形状后的张量:

tensor([[1., 2.],

[3., 4.],

[5., 6.]])

展平后的张量:

tensor([1., 2., 3., 4., 5., 6.])

【数学运算】

张量加 10:

tensor([[11., 12., 13.],

[14., 15., 16.]])

张量乘 2:

tensor([[ 2.,  4.,  6.],

[ 8., 10., 12.]])

张量元素的和: 21.0

【与其他张量操作】

另一个张量:

tensor([[1., 1., 1.],

[1., 1., 1.]])

矩阵乘法结果:

tensor([[ 6.,  6.],

[15., 15.]])

【条件判断和筛选】

大于 3 的元素的布尔掩码:

tensor([[False, False, False],

[ True,  True,  True]])

大于 3 的元素:

tensor([4., 5., 6.])
```

## 张量的 GPU 加速

将张量转移到 GPU：

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

x = torch.tensor([1.0, 2.0, 3.0], device=device)
```

检查 GPU 是否可用：

```python
torch.cuda.is_available()  # 返回 True 或 False
```

## 张量与 NumPy 的互操作

张量与 NumPy 的互操作如下表所示：

| 操作 | 说明 | 示例代码 |
| --- | --- | --- |
| torch.from_numpy(ndarray) | 将 NumPy 数组转换为张量。 | x = torch.from_numpy(np_array) |
| x.numpy() | 将张量转换为 NumPy 数组（仅限 CPU 张量）。 | np_array = x.numpy() |

## 实例

```python
import torch

import numpy as np

# 1. NumPy 数组转换为 PyTorch 张量

print("1. NumPy 转为 PyTorch 张量")

numpy_array = np.array([[1, 2, 3], [4, 5, 6]])

print("NumPy 数组:\n", numpy_array)

# 使用 torch.from_numpy() 将 NumPy 数组转换为张量

tensor_from_numpy = torch.from_numpy(numpy_array)

print("转换后的 PyTorch 张量:\n", tensor_from_numpy)

# 修改 NumPy 数组，观察张量的变化（共享内存）

numpy_array[0, 0] = 100

print("修改后的 NumPy 数组:\n", numpy_array)

print("PyTorch 张量也会同步变化:\n", tensor_from_numpy)

# 2. PyTorch 张量转换为 NumPy 数组

print("\n2. PyTorch 张量转为 NumPy 数组")

tensor = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.float32)

print("PyTorch 张量:\n", tensor)

# 使用 tensor.numpy() 将张量转换为 NumPy 数组

numpy_from_tensor = tensor.numpy()

print("转换后的 NumPy 数组:\n", numpy_from_tensor)

# 修改张量，观察 NumPy 数组的变化（共享内存）

tensor[0, 0] = 77

print("修改后的 PyTorch 张量:\n", tensor)

print("NumPy 数组也会同步变化:\n", numpy_from_tensor)

# 3. 注意：不共享内存的情况（需要复制数据）

print("\n3. 使用 clone() 保证独立数据")

tensor_independent = torch.tensor([[13, 14, 15], [16, 17, 18]], dtype=torch.float32)

numpy_independent = tensor_independent.clone().numpy()  # 使用 clone 复制数据

print("原始张量:\n", tensor_independent)

tensor_independent[0, 0] = 0  # 修改张量数据

print("修改后的张量:\n", tensor_independent)

print("NumPy 数组（不会同步变化）:\n", numpy_independent)
```

输出结果：

```python
1. NumPy 转为 PyTorch 张量

NumPy 数组:

[[1 2 3]

[4 5 6]]

转换后的 PyTorch 张量:

tensor([[1, 2, 3],

[4, 5, 6]])

修改后的 NumPy 数组:

[[100   2   3]

[  4   5   6]]

PyTorch 张量也会同步变化:

tensor([[100,   2,   3],

[  4,   5,   6]])

2. PyTorch 张量转为 NumPy 数组

PyTorch 张量:

tensor([[ 7.,  8.,  9.],

[10., 11., 12.]])

转换后的 NumPy 数组:

[[ 7.  8.  9.]

[10. 11. 12.]]

修改后的 PyTorch 张量:

tensor([[77.,  8.,  9.],

[10., 11., 12.]])

NumPy 数组也会同步变化:

[[77.  8.  9.]

[10. 11. 12.]]

3. 使用 clone() 保证独立数据

原始张量:

tensor([[13., 14., 15.],

[16., 17., 18.]])

修改后的张量:

tensor([[ 0., 14., 15.],

[16., 17., 18.]])

NumPy 数组（不会同步变化）:

[[13. 14. 15.]

[16. 17. 18.]]
```

---

# PyTorch 神经网络基础

神经网络是一种模仿人脑处理信息方式的计算模型，它由许多相互连接的节点（神经元）组成，这些节点按层次排列。

神经网络的强大之处在于其能够自动从大量数据中学习复杂的模式和特征，无需人工设计特征提取器。

随着深度学习的发展，神经网络已经成为解决许多复杂问题的关键技术。

### 神经元（Neuron）

神经元是神经网络的基本单元，它接收输入信号，通过加权求和后与偏置（bias）相加，然后通过激活函数处理以产生输出。

神经元的权重和偏置是网络学习过程中需要调整的参数。

 **输入和输出:**

- **输入（Input）**：输入是网络的起始点，可以是特征数据，如图像的像素值或文本的词向量。

- **输出（Output）**：输出是网络的终点，表示模型的预测结果，如分类任务中的类别标签。

神经元接收多个输入（例如x1, x2, ..., xn），如果输入的加权和大于激活阈值（activation potential），则产生二进制输出。

神经元的输出可以看作是输入的加权和加上偏置（bias），神经元的数学表示：

这里，wj 是权重，xj 是输入，而 Bias 是偏置项。

### 层（Layer）

输入层和输出层之间的层被称为隐藏层，层与层之间的连接密度和类型构成了网络的配置。

神经网络由多个层组成，包括：

- **输入层（Input Layer）**：接收原始输入数据。

- **隐藏层（Hidden Layer）**：对输入数据进行处理，可以有多个隐藏层。

- **输出层（Output Layer）**：产生最终的输出结果。

典型的神经网络架构:

### 前馈神经网络（Feedforward Neural Network，FNN）

前馈神经网络（Feedforward Neural Network，FNN）是神经网络家族中的基本单元。

前馈神经网络特点是数据从输入层开始，经过一个或多个隐藏层，最后到达输出层，全过程没有循环或反馈。

**
前馈神经网络的基本结构：**

-

**输入层：** 数据进入网络的入口点。输入层的每个节点代表一个输入特征。

-

**隐藏层：**一个或多个层，用于捕获数据的非线性特征。每个隐藏层由多个神经元组成，每个神经元通过激活函数增加非线性能力。

-

**输出层：**输出网络的预测结果。节点数和问题类型相关，例如分类问题的输出节点数等于类别数。

-

**连接权重与偏置：**每个神经元的输入通过权重进行加权求和，并加上偏置值，然后通过激活函数传递。

### 循环神经网络（Recurrent Neural Network, RNN）

循环神经网络（Recurrent Neural Network, RNN）络是一类专门处理序列数据的神经网络，能够捕获输入数据中时间或顺序信息的依赖关系。

RNN 的特别之处在于它具有"记忆能力"，可以在网络的隐藏状态中保存之前时间步的信息。

循环神经网络用于处理随时间变化的数据模式。

在 RNN 中，相同的层被用来接收输入参数，并在指定的神经网络中显示输出参数。

PyTorch 提供了强大的工具来构建和训练神经网络。

神经网络在 PyTorch 中是通过 torch.nn 模块来实现的。

torch.nn 模块提供了各种网络层（如全连接层、卷积层等）、损失函数和优化器，让神经网络的构建和训练变得更加方便。

在 PyTorch 中，构建神经网络通常需要继承 nn.Module 类。

nn.Module 是所有神经网络模块的基类，你需要定义以下两个部分：

- **`__init__()`**：定义网络层。
- **`forward()`**：定义数据的前向传播过程。

简单的全连接神经网络（Fully Connected Network）：

## 实例

```python
import torch

import torch.nn as nn

# 定义一个简单的神经网络模型

class SimpleNN(nn.Module):

    def __init__(self):

        super(SimpleNN, self).__init__()

        # 定义一个输入层到隐藏层的全连接层

        self.fc1 = nn.Linear(2, 2)  # 输入 2 个特征，输出 2 个特征

        # 定义一个隐藏层到输出层的全连接层

        self.fc2 = nn.Linear(2, 1)  # 输入 2 个特征，输出 1 个预测值

    

    def forward(self, x):

        # 前向传播过程

        x = torch.relu(self.fc1(x))  # 使用 ReLU 激活函数

        x = self.fc2(x)  # 输出层

        return x

# 创建模型实例

model = SimpleNN()

# 打印模型

print(model)
```

输出结果如下：

```python
SimpleNN(

(fc1): Linear(in_features=2, out_features=2, bias=True)

(fc2): Linear(in_features=2, out_features=1, bias=True)

)
```

PyTorch 提供了许多常见的神经网络层，以下是几个常见的：

- **`nn.Linear(in_features, out_features)`**：全连接层，输入 `in_features` 个特征，输出 `out_features` 个特征。
- **`nn.Conv2d(in_channels, out_channels, kernel_size)`**：2D 卷积层，用于图像处理。
- **`nn.MaxPool2d(kernel_size)`**：2D 最大池化层，用于降维。
- **`nn.ReLU()`**：ReLU 激活函数，常用于隐藏层。
- **`nn.Softmax(dim)`**：Softmax 激活函数，通常用于输出层，适用于多类分类问题。

### 激活函数（Activation Function）

激活函数决定了神经元是否应该被激活。它们是非线性函数，使得神经网络能够学习和执行更复杂的任务。常见的激活函数包括：

- Sigmoid：用于二分类问题，输出值在 0 和 1 之间。

- Tanh：输出值在 -1 和 1 之间，常用于输出层之前。

- ReLU（Rectified Linear Unit）：目前最流行的激活函数之一，定义为 `f(x) = max(0, x)`，有助于解决梯度消失问题。

- Softmax：常用于多分类问题的输出层，将输出转换为概率分布。

## 实例

```python
import torch.nn.functional as F

# ReLU 激活

output = F.relu(input_tensor)

# Sigmoid 激活

output = torch.sigmoid(input_tensor)

# Tanh 激活

output = torch.tanh(input_tensor)
```

### 损失函数（Loss Function）

损失函数用于衡量模型的预测值与真实值之间的差异。

常见的损失函数包括：

- **均方误差（MSELoss）**：回归问题常用，计算输出与目标值的平方差。
- **交叉熵损失（CrossEntropyLoss）**：分类问题常用，计算输出和真实标签之间的交叉熵。
- **BCEWithLogitsLoss**：二分类问题，结合了 Sigmoid 激活和二元交叉熵损失。

## 实例

```python
# 均方误差损失

criterion = nn.MSELoss()

# 交叉熵损失

criterion = nn.CrossEntropyLoss()

# 二分类交叉熵损失

criterion = nn.BCEWithLogitsLoss()
```

### 优化器（Optimizer）

优化器负责在训练过程中更新网络的权重和偏置。

常见的优化器包括：

- SGD（随机梯度下降）

- Adam（自适应矩估计）

- RMSprop（均方根传播）

## 实例

```python
import torch.optim as optim

# 使用 SGD 优化器

optimizer = optim.SGD(model.parameters(), lr=0.01)

# 使用 Adam 优化器

optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 训练过程（Training Process）

训练神经网络涉及以下步骤：

- **准备数据**：通过 `DataLoader` 加载数据。
- **定义损失函数和优化器**。
- **前向传播**：计算模型的输出。
- **计算损失**：与目标进行比较，得到损失值。
- **反向传播**：通过 `loss.backward()` 计算梯度。
- **更新参数**：通过 `optimizer.step()` 更新模型的参数。
- **重复上述步骤**，直到达到预定的训练轮数。

## 实例

```python
# 假设已经定义好了模型、损失函数和优化器

# 训练数据示例

X = torch.randn(10, 2)  # 10 个样本，每个样本有 2 个特征

Y = torch.randn(10, 1)  # 10 个目标标签

# 训练过程

for epoch in range(100):  # 训练 100 轮

    model.train()  # 设置模型为训练模式

    optimizer.zero_grad()  # 清除梯度

    output = model(X)  # 前向传播

    loss = criterion(output, Y)  # 计算损失

    loss.backward()  # 反向传播

    optimizer.step()  # 更新权重

    

    if (epoch + 1) % 10 == 0:  # 每 10 轮输出一次损失

        print(f'Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}')
```

### 测试与评估

训练完成后，需要对模型进行测试和评估。

常见的步骤包括：

- **计算测试集的损失**：测试模型在未见过的数据上的表现。
- **计算准确率（Accuracy）**：对于分类问题，计算正确预测的比例。

## 实例

```python
# 假设你有测试集 X_test 和 Y_test

model.eval()  # 设置模型为评估模式

with torch.no_grad():  # 在评估过程中禁用梯度计算

    output = model(X_test)

    loss = criterion(output, Y_test)

    print(f'Test Loss: {loss.item():.4f}')
```

### 神经网络类型

- **前馈神经网络（Feedforward Neural Networks）**：数据单向流动，从输入层到输出层，无反馈连接。

- **卷积神经网络（Convolutional Neural Networks, CNNs）**：适用于图像处理，使用卷积层提取空间特征。

- **循环神经网络（Recurrent Neural Networks, RNNs）**：适用于序列数据，如时间序列分析和自然语言处理，允许信息反馈循环。

- **长短期记忆网络（Long Short-Term Memory, LSTM）**：一种特殊的RNN，能够学习长期依赖关系。

## torch.nn 参考

以下是 PyTorch 中最常用的 `torch.nn` 函数和类：

### 模型定义基础

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Module | 所有神经网络模块的基类 | class Net(nn.Module): ... |
| nn.Sequential | 顺序容器，按顺序执行各层 | nn.Sequential(conv, relu, pool) |
| nn.ModuleList | 将子模块存储在列表中 | self.layers = nn.ModuleList([...]) |
| nn.Parameter | 创建可学习的参数张量 | self.w = nn.Parameter(torch.randn(n)) |

### 卷积层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Conv1d | 一维卷积（文本、音频） | nn.Conv1d(3, 64, 3) |
| nn.Conv2d | 二维卷积（图像） | nn.Conv2d(3, 64, 3, padding=1) |
| nn.Conv3d | 三维卷积（视频） | nn.Conv3d(3, 64, 3) |
| nn.ConvTranspose2d | 转置卷积（解码器、上采样） | nn.ConvTranspose2d(64, 3, 2, stride=2) |

### 池化层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.MaxPool2d | 二维最大池化 | nn.MaxPool2d(2, 2) |
| nn.AvgPool2d | 二维平均池化 | nn.AvgPool2d(2, 2) |
| nn.AdaptiveAvgPool2d | 自适应平均池化（固定输出尺寸） | nn.AdaptiveAvgPool2d((1, 1)) |
| nn.AdaptiveMaxPool2d | 自适应最大池化（固定输出尺寸） | nn.AdaptiveMaxPool2d((1, 1)) |

### 线性层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Linear | 全连接层（线性变换） | nn.Linear(128, 64) |
| nn.Bilinear | 双线性层 | nn.Bilinear(128, 64, 32) |
| 函数 | 描述 | 示例 |
| nn.ReLU | ReLU 激活函数，f(x) = max(0, x) | nn.ReLU() |
| nn.GELU | 高斯误差线性单元（Transformer 默认） | nn.GELU() |
| nn.SiLU | Swish 激活函数 | nn.SiLU() |
| nn.Tanh | 双曲正切 | nn.Tanh() |
| nn.Sigmoid | Sigmoid 激活函数 | nn.Sigmoid() |
| nn.Softmax | Softmax 激活函数 | nn.Softmax(dim=1) |
| nn.LogSoftmax | Log Softmax（数值稳定） | nn.LogSoftmax(dim=1) |
| nn.LeakyReLU | LeakyReLU，允许负值有小幅梯度 | nn.LeakyReLU(0.01) |
| nn.ELU | 指数线性单元 | nn.ELU() |

### 归一化层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.BatchNorm2d | 二维批归一化（卷积网络常用） | nn.BatchNorm2d(64) |
| nn.LayerNorm | 层归一化（Transformer 常用） | nn.LayerNorm(512) |
| nn.GroupNorm | 组归一化（ResNet 等常用） | nn.GroupNorm(4, 64) |
| nn.InstanceNorm2d | 实例归一化（风格迁移常用） | nn.InstanceNorm2d(64) |

### 循环层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.LSTM | LSTM 长短期记忆层 | nn.LSTM(256, 512, 2) |
| nn.GRU | GRU 门控循环单元层 | nn.GRU(256, 512, 2) |
| nn.RNN | 简单 RNN 层 | nn.RNN(256, 512, 2) |

### Transformer 层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Transformer | 完整 Transformer 模型 | nn.Transformer(d_model=512, nhead=8) |
| nn.TransformerEncoder | Transformer 编码器 | nn.TransformerEncoder(layer, num_layers=6) |
| nn.TransformerDecoder | Transformer 解码器 | nn.TransformerDecoder(layer, num_layers=6) |
| nn.TransformerEncoderLayer | Transformer 编码器层 | nn.TransformerEncoderLayer(512, 8) |
| nn.MultiheadAttention | 多头注意力机制 | nn.MultiheadAttention(512, 8) |

### 嵌入层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Embedding | 嵌入层（词汇映射到向量） | nn.Embedding(10000, 256) |
| nn.EmbeddingBag | 嵌入袋（聚合多个嵌入） | nn.EmbeddingBag(10000, 256) |

### Dropout 层

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.Dropout | 随机丢弃（防止过拟合） | nn.Dropout(0.5) |
| nn.Dropout2d | 2D Dropout（按特征图丢弃） | nn.Dropout2d(0.5) |

### 损失函数

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.CrossEntropyLoss | 交叉熵损失（多分类） | nn.CrossEntropyLoss() |
| nn.MSELoss | 均方误差损失（回归） | nn.MSELoss() |
| nn.L1Loss | L1 损失（MAE） | nn.L1Loss() |
| nn.BCEWithLogitsLoss | 带 Sigmoid 的二元交叉熵 | nn.BCEWithLogitsLoss() |
| nn.HuberLoss | Huber 损失（鲁棒回归） | nn.HuberLoss() |
| nn.NLLLoss | 负对数似然损失 | nn.NLLLoss() |

### 功能性函数（nn.functional）

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| F.relu | ReLU 激活 | F.relu(x) |
| F.gelu | GELU 激活 | F.gelu(x) |
| F.sigmoid | Sigmoid 激活 | F.sigmoid(x) |
| F.softmax | Softmax 激活 | F.softmax(x, dim=1) |
| F.dropout | Dropout 操作 | F.dropout(x, 0.5, training) |
| F.conv2d | 二维卷积 | F.conv2d(x, weight, bias) |
| F.linear | 线性变换 | F.linear(x, weight, bias) |
| F.cross_entropy | 交叉熵损失 | F.cross_entropy(logits, targets) |
| F.mse_loss | 均方误差损失 | F.mse_loss(pred, target) |
| F.interpolate | 插值（上/下采样） | F.interpolate(x, scale_factor=2) |
| F.embedding | 嵌入操作 | F.embedding(indices, weight) |

### 工具函数（nn.init）

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.init.xavier_uniform_ | Xavier 均匀初始化 | nn.init.xavier_uniform_(module.weight) |
| nn.init.xavier_normal_ | Xavier 正态初始化 | nn.init.xavier_normal_(module.weight) |
| nn.init.kaiming_uniform_ | Kaiming 均匀初始化（适合 ReLU） | nn.init.kaiming_uniform_(module.weight) |
| nn.init.kaiming_normal_ | Kaiming 正态初始化（适合 ReLU） | nn.init.kaiming_normal_(module.weight) |
| nn.init.zeros_ | 零初始化 | nn.init.zeros_(module.bias) |
| nn.init.normal_ | 正态初始化 | nn.init.normal_(module.weight, 0, 0.01) |

### 工具函数（nn.utils）

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| nn.utils.clip_grad_norm_ | 裁剪梯度范数（防止梯度爆炸） | nn.utils.clip_grad_norm_(model.parameters(), 1.0) |
| nn.utils.weight_norm | 权重归一化 | nn.utils.weight_norm(module, 'weight') |
| nn.utils.spectral_norm | 谱归一化（GAN 常用） | nn.utils.spectral_norm(module, 'weight') |
| nn.utils.rnn.pack_padded_sequence | 打包变长序列 | pack_padded_sequence(x, lengths) |
| nn.utils.rnn.pad_packed_sequence | 解包序列 | pad_packed_sequence(packed) |

---

# PyTorch 第一个神经网络

本章节我们将介绍如何用 PyTorch 实现一个简单的前馈神经网络，完成一个二分类任务。

以下实例展示了如何使用 PyTorch 实现一个简单的神经网络进行二分类任务训练。

网络结构包括输入层、隐藏层和输出层，使用了 ReLU 激活函数和 Sigmoid 激活函数。

采用了均方误差损失函数和随机梯度下降优化器。

训练过程是通过前向传播、计算损失、反向传播和参数更新来逐步调整模型参数。

## 实例

```python
# 导入PyTorch库

import torch

import torch.nn as nn

# 定义输入层大小、隐藏层大小、输出层大小和批量大小

n_in, n_h, n_out, batch_size = 10, 5, 1, 10

# 创建虚拟输入数据和目标数据

x = torch.randn(batch_size, n_in)  # 随机生成输入数据

y = torch.tensor([[1.0], [0.0], [0.0], 

                 [1.0], [1.0], [1.0], [0.0], [0.0], [1.0], [1.0]])  # 目标输出数据

# 创建顺序模型，包含线性层、ReLU激活函数和Sigmoid激活函数

model = nn.Sequential(

   nn.Linear(n_in, n_h),  # 输入层到隐藏层的线性变换

   nn.ReLU(),            # 隐藏层的ReLU激活函数

   nn.Linear(n_h, n_out),  # 隐藏层到输出层的线性变换

   nn.Sigmoid()           # 输出层的Sigmoid激活函数

)

# 定义均方误差损失函数和随机梯度下降优化器

criterion = torch.nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 学习率为0.01

# 执行梯度下降算法进行模型训练

for epoch in range(50):  # 迭代50次

   y_pred = model(x)  # 前向传播，计算预测值

   loss = criterion(y_pred, y)  # 计算损失

   print('epoch: ', epoch, 'loss: ', loss.item())  # 打印损失值

   optimizer.zero_grad()  # 清零梯度

   loss.backward()  # 反向传播，计算梯度

   optimizer.step()  # 更新模型参数
```

输出结果类似如下：

```python
epoch:  0 loss:  0.2591968774795532

epoch:  1 loss:  0.25902628898620605

epoch:  2 loss:  0.25885599851608276

epoch:  3 loss:  0.25868603587150574

epoch:  4 loss:  0.25851646065711975

...
```

定义网络参数：

```python
n_in, n_h, n_out, batch_size = 10, 5, 1, 10
```

- `n_in`：输入层大小为 10，即每个数据点有 10 个特征。
- `n_h`：隐藏层大小为 5，即隐藏层包含 5 个神经元。
- `n_out`：输出层大小为 1，即输出一个标量，表示二分类结果（0 或 1）。
- `batch_size`：每个批次包含 10 个样本。

生成输入数据和目标数据：

```python
x = torch.randn(batch_size, n_in)  # 随机生成输入数据

y = torch.tensor([[1.0], [0.0], [0.0], 

[1.0], [1.0], [1.0], [0.0], [0.0], [1.0], [1.0]])  # 目标输出数据
```

- `x`：随机生成一个形状为 `(10, 10)` 的输入数据矩阵，表示 10 个样本，每个样本有 10 个特征。
- `y`：目标输出数据（标签），表示每个输入样本的类别标签（0 或 1），是一个 10×1 的张量。

定义神经网络模型：

```python
model = nn.Sequential(

nn.Linear(n_in, n_h),  # 输入层到隐藏层的线性变换

nn.ReLU(),            # 隐藏层的ReLU激活函数

nn.Linear(n_h, n_out),  # 隐藏层到输出层的线性变换

nn.Sigmoid()           # 输出层的Sigmoid激活函数

)
```

`nn.Sequential` 用于按顺序定义网络层。

- `nn.Linear(n_in, n_h)`：定义输入层到隐藏层的线性变换，输入特征是 10 个，隐藏层有 5 个神经元。
- `nn.ReLU()`：在隐藏层后添加 ReLU 激活函数，增加非线性。
- `nn.Linear(n_h, n_out)`：定义隐藏层到输出层的线性变换，输出为 1 个神经元。
- `nn.Sigmoid()`：输出层使用 Sigmoid 激活函数，将结果映射到 0 到 1 之间，用于二分类任务。

定义损失函数和优化器：

```python
criterion = torch.nn.MSELoss()  # 使用均方误差损失函数

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 使用随机梯度下降优化器，学习率为 0.01
```

训练循环：

```python
for epoch in range(50):  # 训练50轮

y_pred = model(x)  # 前向传播，计算预测值

loss = criterion(y_pred, y)  # 计算损失

print('epoch: ', epoch, 'loss: ', loss.item())  # 打印损失值

optimizer.zero_grad()  # 清零梯度

loss.backward()  # 反向传播，计算梯度

optimizer.step()  # 更新模型参数
```

- `for epoch in range(50)`：进行 50 次训练迭代。
- `y_pred = model(x)`：进行前向传播，使用当前模型参数计算输入数据 `x` 的预测值。
- `loss = criterion(y_pred, y)`：计算预测值和目标值 `y` 之间的损失。
- `optimizer.zero_grad()`：清除上一轮训练时的梯度值。
- `loss.backward()`：反向传播，计算损失函数相对于模型参数的梯度。
- `optimizer.step()`：根据计算出的梯度更新模型参数。

可视化代码：

## 实例

```python
import torch

import torch.nn as nn

import matplotlib.pyplot as plt

# 定义输入层大小、隐藏层大小、输出层大小和批量大小

n_in, n_h, n_out, batch_size = 10, 5, 1, 10

# 创建虚拟输入数据和目标数据

x = torch.randn(batch_size, n_in)  # 随机生成输入数据

y = torch.tensor([[1.0], [0.0], [0.0], 

                  [1.0], [1.0], [1.0], [0.0], [0.0], [1.0], [1.0]])  # 目标输出数据

# 创建顺序模型，包含线性层、ReLU激活函数和Sigmoid激活函数

model = nn.Sequential(

    nn.Linear(n_in, n_h),  # 输入层到隐藏层的线性变换

    nn.ReLU(),            # 隐藏层的ReLU激活函数

    nn.Linear(n_h, n_out),  # 隐藏层到输出层的线性变换

    nn.Sigmoid()           # 输出层的Sigmoid激活函数

)

# 定义均方误差损失函数和随机梯度下降优化器

criterion = torch.nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 学习率为0.01

# 用于存储每轮的损失值

losses = []

# 执行梯度下降算法进行模型训练

for epoch in range(50):  # 迭代50次

    y_pred = model(x)  # 前向传播，计算预测值

    loss = criterion(y_pred, y)  # 计算损失

    losses.append(loss.item())  # 记录损失值

    print(f'Epoch [{epoch+1}/50], Loss: {loss.item():.4f}')  # 打印损失值

    optimizer.zero_grad()  # 清零梯度

    loss.backward()  # 反向传播，计算梯度

    optimizer.step()  # 更新模型参数

# 可视化损失变化曲线

plt.figure(figsize=(8, 5))

plt.plot(range(1, 51), losses, label='Loss')

plt.xlabel('Epoch')

plt.ylabel('Loss')

plt.title('Training Loss Over Epochs')

plt.legend()

plt.grid()

plt.show()

# 可视化预测结果与实际目标值对比

y_pred_final = model(x).detach().numpy()  # 最终预测值

y_actual = y.numpy()  # 实际值

plt.figure(figsize=(8, 5))

plt.plot(range(1, batch_size + 1), y_actual, 'o-', label='Actual', color='blue')

plt.plot(range(1, batch_size + 1), y_pred_final, 'x--', label='Predicted', color='red')

plt.xlabel('Sample Index')

plt.ylabel('Value')

plt.title('Actual vs Predicted Values')

plt.legend()

plt.grid()

plt.show()
```

显示如下所示：

## 另外一个实例

我们假设有一个二维数据集，目标是根据点的位置将它们分类到两个类别中（例如，红色和蓝色点）。

以下实例展示了如何使用神经网络完成简单的二分类任务，为更复杂的任务奠定了基础，通过 PyTorch 的模块化接口，神经网络的构建、训练和可视化都非常直观。

### 1、数据准备

首先，我们生成一些简单的二维数据：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import matplotlib.pyplot as plt

# 生成一些随机数据

n_samples = 100

data = torch.randn(n_samples, 2)  # 生成 100 个二维数据点

labels = (data[:, 0]**2 + data[:, 1]**2 < 1).float().unsqueeze(1)  # 点在圆内为1，圆外为0

# 可视化数据

plt.scatter(data[:, 0], data[:, 1], c=labels.squeeze(), cmap='coolwarm')

plt.title("Generated Data")

plt.xlabel("Feature 1")

plt.ylabel("Feature 2")

plt.show()
```

**数据说明：**

- `data` 是输入的二维点，每个点有两个特征。
- `labels` 是目标分类，点在圆形区域内为 1，否则为 0。

显示如下：

### 2、定义神经网络

用 PyTorch 创建一个简单的前馈神经网络。

前馈神经网络使用了一层隐藏层，通过简单的线性变换和激活函数捕获数据的非线性模式。

## 实例

```python
class SimpleNN(nn.Module):

    def __init__(self):

        super(SimpleNN, self).__init__()

        # 定义神经网络的层

        self.fc1 = nn.Linear(2, 4)  # 输入层有 2 个特征，隐藏层有 4 个神经元

        self.fc2 = nn.Linear(4, 1)  # 隐藏层输出到 1 个神经元（用于二分类）

        self.sigmoid = nn.Sigmoid()  # 二分类激活函数

    def forward(self, x):

        x = torch.relu(self.fc1(x))  # 使用 ReLU 激活函数

        x = self.sigmoid(self.fc2(x))  # 输出层使用 Sigmoid 激活函数

        return x

# 实例化模型

model = SimpleNN()
```

### 3、定义损失函数和优化器

## 实例

```python
# 定义二分类的损失函数和优化器

criterion = nn.BCELoss()  # 二元交叉熵损失

optimizer = optim.SGD(model.parameters(), lr=0.1)  # 使用随机梯度下降优化器
```

### 4、训练模型

用数据训练模型，让它学会分类。

## 实例

```python
# 训练

epochs = 100

for epoch in range(epochs):

    # 前向传播

    outputs = model(data)

    loss = criterion(outputs, labels)

    # 反向传播

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    # 每 10 轮打印一次损失

    if (epoch + 1) % 10 == 0:

        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')
```

### 5、测试模型并可视化结果

我们测试模型，并在图像上绘制决策边界。

## 实例

```python
# 可视化决策边界

def plot_decision_boundary(model, data):

    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1

    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

    xx, yy = torch.meshgrid(torch.arange(x_min, x_max, 0.1), torch.arange(y_min, y_max, 0.1), indexing='ij')

    grid = torch.cat([xx.reshape(-1, 1), yy.reshape(-1, 1)], dim=1)

    predictions = model(grid).detach().numpy().reshape(xx.shape)

    plt.contourf(xx, yy, predictions, levels=[0, 0.5, 1], cmap='coolwarm', alpha=0.7)

    plt.scatter(data[:, 0], data[:, 1], c=labels.squeeze(), cmap='coolwarm', edgecolors='k')

    plt.title("Decision Boundary")

    plt.show()

plot_decision_boundary(model, data)
```

### 6、完整代码

完整代码如下：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import matplotlib.pyplot as plt

# 生成一些随机数据

n_samples = 100

data = torch.randn(n_samples, 2)  # 生成 100 个二维数据点

labels = (data[:, 0]**2 + data[:, 1]**2 < 1).float().unsqueeze(1)  # 点在圆内为1，圆外为0

# 可视化数据

plt.scatter(data[:, 0], data[:, 1], c=labels.squeeze(), cmap='coolwarm')

plt.title("Generated Data")

plt.xlabel("Feature 1")

plt.ylabel("Feature 2")

plt.show()

# 定义前馈神经网络

class SimpleNN(nn.Module):

    def __init__(self):

        super(SimpleNN, self).__init__()

        # 定义神经网络的层

        self.fc1 = nn.Linear(2, 4)  # 输入层有 2 个特征，隐藏层有 4 个神经元

        self.fc2 = nn.Linear(4, 1)  # 隐藏层输出到 1 个神经元（用于二分类）

        self.sigmoid = nn.Sigmoid()  # 二分类激活函数

    def forward(self, x):

        x = torch.relu(self.fc1(x))  # 使用 ReLU 激活函数

        x = self.sigmoid(self.fc2(x))  # 输出层使用 Sigmoid 激活函数

        return x

# 实例化模型

model = SimpleNN()

# 定义损失函数和优化器

criterion = nn.BCELoss()  # 二元交叉熵损失

optimizer = optim.SGD(model.parameters(), lr=0.1)  # 使用随机梯度下降优化器

# 训练

epochs = 100

for epoch in range(epochs):

    # 前向传播

    outputs = model(data)

    loss = criterion(outputs, labels)

    # 反向传播

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    # 每 10 轮打印一次损失

    if (epoch + 1) % 10 == 0:

        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')

# 可视化决策边界

def plot_decision_boundary(model, data):

    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1

    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

    xx, yy = torch.meshgrid(torch.arange(x_min, x_max, 0.1), torch.arange(y_min, y_max, 0.1), indexing='ij')

    grid = torch.cat([xx.reshape(-1, 1), yy.reshape(-1, 1)], dim=1)

    predictions = model(grid).detach().numpy().reshape(xx.shape)

    plt.contourf(xx, yy, predictions, levels=[0, 0.5, 1], cmap='coolwarm', alpha=0.7)

    plt.scatter(data[:, 0], data[:, 1], c=labels.squeeze(), cmap='coolwarm', edgecolors='k')

    plt.title("Decision Boundary")

    plt.show()

plot_decision_boundary(model, data)
```

训练时的损失输出：

```python
Epoch [10/100], Loss: 0.5247

Epoch [20/100], Loss: 0.3142

...

Epoch [100/100], Loss: 0.0957
```

图中显示了原始数据点（红色和蓝色），以及模型学习到的分类边界。

---

# PyTorch 数据处理与加载

在 PyTorch 中，处理和加载数据是深度学习训练过程中的关键步骤。

为了高效地处理数据，PyTorch 提供了强大的工具，包括 torch.utils.data.Dataset 和 torch.utils.data.DataLoader，帮助我们管理数据集、批量加载和数据增强等任务。

PyTorch 数据处理与加载的介绍：

- **自定义 Dataset**：通过继承 `torch.utils.data.Dataset` 来加载自己的数据集。
- **DataLoader**：`DataLoader` 按批次加载数据，支持多线程加载并进行数据打乱。
- **数据预处理与增强**：使用 `torchvision.transforms` 进行常见的图像预处理和增强操作，提高模型的泛化能力。
- **加载标准数据集**：`torchvision.datasets` 提供了许多常见的数据集，简化了数据加载过程。
- **多个数据源**：通过组合多个 `Dataset` 实例来处理来自不同来源的数据。

## 自定义 Dataset

torch.utils.data.Dataset 是一个抽象类，允许你从自己的数据源中创建数据集。

我们需要继承该类并实现以下两个方法：

- `__len__(self)`：返回数据集中的样本数量。
- `__getitem__(self, idx)`：通过索引返回一个样本。

假设我们有一个简单的 CSV 文件或一些列表数据，我们可以通过继承 Dataset 类来创建自己的数据集。

## 实例

```python
import torch

from torch.utils.data import Dataset

# 自定义数据集类

class MyDataset(Dataset):

    def __init__(self, X_data, Y_data):

        """

        初始化数据集，X_data 和 Y_data 是两个列表或数组

        X_data: 输入特征

        Y_data: 目标标签

        """

        self.X_data = X_data

        self.Y_data = Y_data

    def __len__(self):

        """返回数据集的大小"""

        return len(self.X_data)

    def __getitem__(self, idx):

        """返回指定索引的数据"""

        x = torch.tensor(self.X_data[idx], dtype=torch.float32)  # 转换为 Tensor

        y = torch.tensor(self.Y_data[idx], dtype=torch.float32)

        return x, y

# 示例数据

X_data = [[1, 2], [3, 4], [5, 6], [7, 8]]  # 输入特征

Y_data = [1, 0, 1, 0]  # 目标标签

# 创建数据集实例

dataset = MyDataset(X_data, Y_data)
```

## 使用 DataLoader 加载数据

DataLoader 是 PyTorch 提供的一个重要工具，用于从 Dataset 中按批次（batch）加载数据。

DataLoader 允许我们批量读取数据并进行多线程加载，从而提高训练效率。

## 实例

```python
from torch.utils.data import DataLoader

# 创建 DataLoader 实例，batch_size 设置每次加载的样本数量

dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 打印加载的数据

for epoch in range(1):

    for batch_idx, (inputs, labels) in enumerate(dataloader):

        print(f'Batch {batch_idx + 1}:')

        print(f'Inputs: {inputs}')

        print(f'Labels: {labels}')
```

- **`batch_size`**: 每次加载的样本数量。
- **`shuffle`**: 是否对数据进行洗牌，通常训练时需要将数据打乱。
- **`drop_last`**: 如果数据集中的样本数不能被 `batch_size` 整除，设置为 `True` 时，丢弃最后一个不完整的 batch。

输出：

```python
Batch 1:

Inputs: tensor([[3., 4.], [1., 2.]])

Labels: tensor([0., 1.])

Batch 2:

Inputs: tensor([[7., 8.], [5., 6.]])

Labels: tensor([0., 1.])
```

每次循环中，DataLoader 会返回一个批次的数据，包括输入特征（inputs）和目标标签（labels）。

## 预处理与数据增强

数据预处理和增强对于提高模型的性能至关重要。

PyTorch 提供了 torchvision.transforms 模块来进行常见的图像预处理和增强操作，如旋转、裁剪、归一化等。

常见的图像预处理操作:

## 实例

```python
import torchvision.transforms as transforms

from PIL import Image

# 定义数据预处理的流水线

transform = transforms.Compose([

    transforms.Resize((128, 128)),  # 将图像调整为 128x128

    transforms.ToTensor(),  # 将图像转换为张量

    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化

])

# 加载图像

image = Image.open('image.jpg')

# 应用预处理

image_tensor = transform(image)

print(image_tensor.shape)  # 输出张量的形状
```

- **`transforms.Compose()`**：将多个变换操作组合在一起。
- **`transforms.Resize()`**：调整图像大小。
- **`transforms.ToTensor()`**：将图像转换为 PyTorch 张量，值会被归一化到 `[0, 1]` 范围。
- **`transforms.Normalize()`**：标准化图像数据，通常使用预训练模型时需要进行标准化处理。

### 图像数据增强

数据增强技术通过对训练数据进行随机变换，增加数据的多样性，帮助模型更好地泛化。例如，随机翻转、旋转、裁剪等。

## 实例

```python
transform = transforms.Compose([

    transforms.RandomHorizontalFlip(),  # 随机水平翻转

    transforms.RandomRotation(30),  # 随机旋转 30 度

    transforms.RandomResizedCrop(128),  # 随机裁剪并调整为 128x128

    transforms.ToTensor(),

    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

])
```

这些数据增强方法可以通过 transforms.Compose() 组合使用，保证每个图像在训练时具有不同的变换。

## 加载图像数据集

对于图像数据集，torchvision.datasets 提供了许多常见数据集（如 CIFAR-10、ImageNet、MNIST 等）以及用于加载图像数据的工具。

加载 MNIST 数据集:

## 实例

```python
import torchvision.datasets as datasets

import torchvision.transforms as transforms

# 定义预处理操作

transform = transforms.Compose([

    transforms.ToTensor(),

    transforms.Normalize((0.5,), (0.5,))  # 对灰度图像进行标准化

])

# 下载并加载 MNIST 数据集

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# 创建 DataLoader

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 迭代训练数据

for inputs, labels in train_loader:

    print(inputs.shape)  # 每个批次的输入数据形状

    print(labels.shape)  # 每个批次的标签形状
```

- `datasets.MNIST()` 会自动下载 MNIST 数据集并加载。
- `transform` 参数允许我们对数据进行预处理。
- `train=True` 和 `train=False` 分别表示训练集和测试集。

## 用多个数据源（Multi-source Dataset）

如果你的数据集由多个文件、多个来源（例如多个图像文件夹）组成，可以通过继承 Dataset 类自定义加载多个数据源。

PyTorch 提供了 ConcatDataset 和 ChainDataset 等类来连接多个数据集。

例如，假设我们有多个图像文件夹的数据，可以将它们合并为一个数据集：

## 实例

```python
from torch.utils.data import ConcatDataset

# 假设 dataset1 和 dataset2 是两个 Dataset 对象

combined_dataset = ConcatDataset([dataset1, dataset2])

combined_loader = DataLoader(combined_dataset, batch_size=64, shuffle=True)
```

---

-

# PyTorch 线性回归

线性回归是最基本的机器学习算法之一，用于预测一个连续值。它是一种简单且常见的回归分析方法，目的是通过拟合一个线性函数来预测输出。

对于一个简单的线性回归问题，模型可以表示为：

- y 是预测值（目标值）。

- \(x_1\)，\(x_2\)，\(x_n\) 是输入特征。

- \(w_1\)，\(w_2\)，\(w_n\) 是待学习的权重（模型参数）。

- b 是偏置项。

在 PyTorch 中，线性回归模型可以通过继承 `nn.Module` 类来实现。我们将通过一个简单的示例来详细说明如何使用 PyTorch 实现线性回归模型。

## 数据准备

我们首先准备一些假数据，用于训练我们的线性回归模型。这里，我们可以生成一个简单的线性关系的数据集，其中每个样本有两个特征 \(x_1\)，\(x_2\)。

## 实例

```python
import torch

import numpy as np

import matplotlib.pyplot as plt

# 随机种子，确保每次运行结果一致

torch.manual_seed(42)

# 生成训练数据

X = torch.randn(100, 2)  # 100 个样本，每个样本 2 个特征

true_w = torch.tensor([2.0, 3.0])  # 假设真实权重

true_b = 4.0  # 偏置项

Y = X @ true_w + true_b + torch.randn(100) * 0.1  # 加入一些噪声

# 打印部分数据

print(X[:5])

print(Y[:5])
```

输出结果如下：

```python
tensor([[ 1.9269,  1.4873],

[ 0.9007, -2.1055],

[ 0.6784, -1.2345],

[-0.0431, -1.6047],

[-0.7521,  1.6487]])

tensor([12.4460, -0.4663,  1.7666, -0.9357,  7.4781])
```

这段代码创建了一个带有噪声的线性数据集。

- 输入 X 为 100x2 的矩阵，每个样本有两个特征。

- 输出 Y 由真实的权重和偏置生成，并加上了一些随机噪声。

- 使用 `torch.manual_seed(42)` 确保每次运行结果一致，便于调试和复现。

## 定义线性回归模型

我们可以通过继承 `nn.Module` 来定义一个简单的线性回归模型。在 PyTorch 中，线性回归的核心是 `nn.Linear()` 层，它会自动处理权重和偏置的初始化。

## 实例

```python
import torch.nn as nn

# 定义线性回归模型

class LinearRegressionModel(nn.Module):

    def __init__(self):

        super(LinearRegressionModel, self).__init__()

        # 定义一个线性层，输入为2个特征，输出为1个预测值

        self.linear = nn.Linear(2, 1)  # 输入维度2，输出维度1

    def forward(self, x):

        return self.linear(x)  # 前向传播，返回预测结果

# 创建模型实例

model = LinearRegressionModel()
```

这里的 `nn.Linear(2, 1)` 表示一个线性层，它有 2 个输入特征和 1 个输出。`forward` 方法定义了如何通过这个层进行前向传播。

**注意：** `nn.Linear` 会自动创建权重矩阵和偏置向量，不需要手动定义。

## 定义损失函数与优化器

线性回归的常见损失函数是**均方误差损失（MSELoss）**，用于衡量预测值与真实值之间的差异。PyTorch 中提供了现成的 MSELoss 函数。

我们将使用**SGD（随机梯度下降）**或**Adam**优化器来最小化损失函数。

## 实例

```python
# 损失函数（均方误差）

criterion = nn.MSELoss()

# 优化器（使用 SGD 或 Adam）

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 学习率设置为0.01

# 也可以使用 Adam 优化器

# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
```

| 组件 | 说明 |
| --- | --- |
| MSELoss | 计算预测值与真实值的均方误差，公式为 \(\frac{1}{n}\sum(y_{pred} - y_{true})^2\) |
| SGD | 使用随机梯度下降法更新参数，学习率控制每步更新的幅度 |
| Adam | 自适应学习率优化器，通常收敛更快 |

## 训练模型

在训练过程中，我们将执行以下步骤：

- 使用输入数据 X 进行前向传播，得到预测值。

- 计算损失（预测值与实际值之间的差异）。

- 使用反向传播计算梯度。

- 更新模型参数（权重和偏置）。

我们将训练模型 1000 轮，并在每 100 轮打印一次损失。

## 实例

```python
# 训练模型

num_epochs = 1000  # 训练 1000 轮

for epoch in range(num_epochs):

    model.train()  # 设置模型为训练模式

    # 前向传播

    predictions = model(X)  # 模型输出预测值

    loss = criterion(predictions.squeeze(), Y)  # 计算损失（注意预测值需要压缩为1D）

    # 反向传播

    optimizer.zero_grad()  # 清空之前的梯度

    loss.backward()  # 计算梯度

    optimizer.step()  # 更新模型参数

    # 打印损失

    if (epoch + 1) % 100 == 0:

        print(f'Epoch [{epoch + 1}/1000], Loss: {loss.item():.4f}')
```

- `predictions.squeeze()`：将模型的输出从 2D 张量压缩为 1D，因为目标值 `Y` 是一个一维数组。

- `optimizer.zero_grad()`：每次反向传播前需要清空之前的梯度，否则梯度会累积。

- `loss.backward()`：自动计算所有可训练参数的梯度。

- `optimizer.step()`：根据计算得到的梯度更新权重和偏置。

**训练模式 vs 评估模式：** 在训练循环中调用 `model.train()` 是必要的，虽然本例中没有使用 Dropout 或 BatchNorm，但养成这个习惯对复杂模型很重要。

## 评估模型

训练完成后，我们可以通过查看模型的权重和偏置来评估模型的效果。我们还可以在新的数据上进行预测并与实际值进行比较。

## 实例

```python
# 查看训练后的权重和偏置

print(f'Predicted weight: {model.linear.weight.data.numpy()}')

print(f'Predicted bias: {model.linear.bias.data.numpy()}')

# 在新数据上做预测

with torch.no_grad():  # 评估时不需要计算梯度

    predictions = model(X)

# 可视化预测与实际值

plt.scatter(X[:, 0], Y, color='blue', label='True values')

plt.scatter(X[:, 0], predictions, color='red', label='Predictions')

plt.legend()

plt.show()
```

- `model.linear.weight.data` 和 `model.linear.bias.data`：这些属性存储了模型的权重和偏置。

- `torch.no_grad()`：在评估模式下，不需要计算梯度，可以节省内存并提高推理速度。

## 完整示例代码

下面是上述所有步骤的完整代码，整合在一起可以直接运行：

## 实例

```python
import torch

import torch.nn as nn

import matplotlib.pyplot as plt

# 1. 准备数据

torch.manual_seed(42)

X = torch.randn(100, 2)  # 100 个样本，2 个特征

true_w = torch.tensor([2.0, 3.0])

true_b = 4.0

Y = X @ true_w + true_b + torch.randn(100) * 0.1

# 2. 定义模型

class LinearRegressionModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.linear = nn.Linear(2, 1)

    def forward(self, x):

        return self.linear(x)

model = LinearRegressionModel()

# 3. 定义损失函数和优化器

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4. 训练模型

num_epochs = 1000

for epoch in range(num_epochs):

    model.train()

    predictions = model(X)

    loss = criterion(predictions.squeeze(), Y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if (epoch + 1) % 100 == 0:

        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 5. 评估模型

print(f'\n训练后的权重: {model.linear.weight.data.numpy()}')

print(f'训练后的偏置: {model.linear.bias.data.numpy()}')

print(f'真实权重: {true_w.numpy()}')

print(f'真实偏置: {true_b}')
```

## 运行结果解析

运行上述代码后，你将看到类似以下的输出：

```python
Epoch [100/1000], Loss: 0.0654

Epoch [200/1000], Loss: 0.0398

Epoch [300/1000], Loss: 0.0243

Epoch [400/1000], Loss: 0.0148

Epoch [500/1000], Loss: 0.0090

Epoch [600/1000], Loss: 0.0055

Epoch [700/1000], Loss: 0.0033

Epoch [800/1000], Loss: 0.0020

Epoch [900/1000], Loss: 0.0012

Epoch [1000/1000], Loss: 0.0008

训练后的权重: [[2.0016 2.9973]]

训练后的偏置: [4.0015]

真实权重: [2. 3.]

真实偏置: 4.0
```

可以看到，随着训练轮数的增加，损失值不断下降，最终模型的权重和偏置非常接近真实值，说明模型成功学习到了数据的线性关系。

## 扩展：使用更复杂的优化器

除了 SGD，PyTorch 还提供了许多其他优化器，下面是使用 Adam 优化器的示例：

## 实例

```python
# 使用 Adam 优化器（通常收敛更快）

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 训练模型

for epoch in range(num_epochs):

    model.train()

    predictions = model(X)

    loss = criterion(predictions.squeeze(), Y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if (epoch + 1) % 100 == 0:

        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
```

| 优化器 | 特点 | 适用场景 |
| --- | --- | --- |
| SGD | 简单直接，需要手动调节学习率 | 大数据集，经典场景 |
| Adam | 自适应学习率，收敛快 | 大多数场景，推荐默认选择 |
| RMSprop | 适合递归神经网络 | RNN、LSTM 等序列模型 |

## 常见问题

### 问题一：损失值不下降

如果训练过程中损失值不下降，可能的原因包括：

- 学习率过小，导致参数更新幅度太小。

- 学习率过大，导致跳过最优解。

- 数据存在问题，如特征值范围差异过大。

**解决方案：**

- 尝试调整学习率（从 0.1、0.01、0.001 开始尝试）。

- 对输入数据进行标准化处理。

- 检查数据中是否存在异常值或缺失值。

### 问题二：预测值形状不匹配

如果在计算损失时出现形状不匹配的错误，可能需要使用 `squeeze()` 或 `unsqueeze()` 调整张量形状。

## 实例

```python
# 检查输出形状

predictions = model(X)

print(f'模型输出形状: {predictions.shape}')  # 应该是 [100, 1]

# 压缩为 1D

predictions = predictions.squeeze()

print(f'压缩后形状: {predictions.shape}')  # 应该是 [100]

# 计算损失

loss = criterion(predictions, Y)
```

### 问题三：如何提高模型精度

- 增加训练轮数。

- 调整学习率。

- 使用更复杂的模型结构（如多层神经网络）。

- 增加训练数据量。

---

# PyTorch 卷积神经网络

PyTorch 卷积神经网络 (Convolutional Neural Networks, CNN) 是一类专门用于处理具有网格状拓扑结构数据（如图像）的深度学习模型。

CNN 是计算机视觉任务（如图像分类、目标检测和分割）的核心技术。

下面这张图展示了一个典型的卷积神经网络（CNN）的结构和工作流程，用于图像识别任务。

在图中，CNN 的输出层给出了三个类别的概率：Donald（0.2）、Goofy（0.1）和Tweety（0.7），这表明网络认为输入图像最有可能是 Tweety。

以下是各个部分的简要说明：

-

**输入图像（Input Image）**：网络接收的原始图像数据。

-

**卷积（Convolution）**：使用卷积核（Kernel）在输入图像上滑动，提取特征，生成特征图（Feature Maps）。

-

**池化（Pooling）**：通常在卷积层之后，通过最大池化或平均池化减少特征图的尺寸，同时保留重要特征，生成池化特征图（Pooled Feature Maps）。

-

**特征提取（Feature Extraction）**：通过多个卷积和池化层的组合，逐步提取图像的高级特征。

-

**展平层（Flatten Layer）**：将多维的特征图转换为一维向量，以便输入到全连接层。

-

**全连接层（Fully Connected Layer）**：类似于传统的神经网络层，用于将提取的特征映射到输出类别。

-

**分类（Classification）**：网络的输出层，根据全连接层的输出进行分类。

-

**概率分布（Probabilistic Distribution）**：输出层给出每个类别的概率，表示输入图像属于各个类别的可能性。

### 卷积神经网络的基本结构

**1、输入层（Input Layer）**

接收原始图像数据，图像通常被表示为一个三维数组，其中两个维度代表图像的宽度和高度，第三个维度代表颜色通道（例如，RGB图像有三个通道）。

**2、卷积层（Convolutional Layer）**

用卷积核提取局部特征，如边缘、纹理等。

公式：

- x：输入图像。

-

k：卷积核（权重矩阵）。

-
b：偏置。

应用一组可学习的滤波器（或卷积核）在输入图像上进行卷积操作，以提取局部特征。

每个滤波器在输入图像上滑动，生成一个特征图（Feature Map），表示滤波器在不同位置的激活。

卷积层可以有多个滤波器，每个滤波器生成一个特征图，所有特征图组成一个特征图集合。

### 3、激活函数（Activation Function）

通常在卷积层之后应用非线性激活函数，如 ReLU（Rectified Linear Unit），以引入非线性特性，使网络能够学习更复杂的模式。

ReLU 函数定义为 ：f(x)=max(0,x)，即如果输入小于 0 则输出 0，否则输出输入值。

**4、池化层（Pooling Layer）**

-
用于降低特征图的空间维度，减少计算量和参数数量，同时保留最重要的特征信息。

-
最常见的池化操作是最大池化（Max Pooling）和平均池化（Average Pooling）。

-
最大池化选择区域内的最大值，而平均池化计算区域内的平均值。

**
5、归一化层（Normalization Layer，可选）**

- 例如，局部响应归一化（Local Response Normalization, LRN）或批归一化（Batch Normalization）。

- 这些层有助于加速训练过程，提高模型的稳定性。

**
6、全连接层（Fully Connected Layer）**

-

在 CNN 的末端，将前面层提取的特征图展平（Flatten）成一维向量，然后输入到全连接层。

-
全连接层的每个神经元都与前一层的所有神经元相连，用于综合特征并进行最终的分类或回归。

**
7、输出层（Output Layer）**

根据任务的不同，输出层可以有不同的形式。

对于分类任务，通常使用 Softmax 函数将输出转换为概率分布，表示输入属于各个类别的概率。

**8、损失函数（Loss Function）**

用于衡量模型预测与真实标签之间的差异。

常见的损失函数包括交叉熵损失（Cross-Entropy Loss）用于多分类任务，均方误差（Mean Squared Error, MSE）用于回归任务。

**9、优化器（Optimizer）**

用于根据损失函数的梯度更新网络的权重。常见的优化器包括随机梯度下降（SGD）、Adam、RMSprop等。

**10、正则化（Regularization，可选）**

包括 Dropout、L1/L2 正则化等技术，用于防止模型过拟合。

这些层可以堆叠形成更深的网络结构，以提高模型的学习能力。

CNN 的深度和复杂性可以根据任务的需求进行调整。

## PyTorch 实现一个 CNN 实例

以下示例展示如何用 PyTorch 构建一个简单的 CNN 模型，用于 MNIST 数据集的数字分类。

主要步骤：

- **数据加载与预处理**：使用 `torchvision` 加载和预处理 MNIST 数据。
- **模型构建**：定义卷积层、池化层和全连接层。
- **训练**：通过损失函数和优化器进行模型训练。
- **评估**：测试集上计算模型的准确率。
- **可视化**：展示部分测试样本及其预测结果。

### 1、导入必要库

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import torch.optim as optim
```

### 2、数据加载

使用 torchvision 提供的 MNIST 数据集，加载和预处理数据。

## 实例

```python
transform = transforms.Compose([

    transforms.ToTensor(),  # 转为张量

    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1, 1]

])

# 加载 MNIST 数据集

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)
```

### 3、定义 CNN 模型

使用 nn.Module 构建一个 CNN。

## 实例

```python
class SimpleCNN(nn.Module):

    def __init__(self):

        super(SimpleCNN, self).__init__()

        # 定义卷积层：输入1通道，输出32通道，卷积核大小3x3

        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)

        # 定义卷积层：输入32通道，输出64通道

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)

        # 定义全连接层

        self.fc1 = nn.Linear(64 * 7 * 7, 128)  # 输入大小 = 特征图大小 * 通道数

        self.fc2 = nn.Linear(128, 10)  # 10 个类别

    def forward(self, x):

        x = F.relu(self.conv1(x))  # 第一层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = F.relu(self.conv2(x))  # 第二层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = x.view(-1, 64 * 7 * 7) # 展平操作

        x = F.relu(self.fc1(x))    # 全连接层 + ReLU

        x = self.fc2(x)            # 全连接层输出

        return x

# 创建模型实例

model = SimpleCNN()
```

### 4、定义损失函数与优化器

使用交叉熵损失和随机梯度下降优化器。

```python
criterion = nn.CrossEntropyLoss()  # 多分类交叉熵损失

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)  # 学习率和动量
```

### 5、训练模型

训练模型 5 个 epoch，每个 epoch 后输出训练损失。

## 实例

```python
num_epochs = 5

model.train()  # 设为训练模式

for epoch in range(num_epochs):

    total_loss = 0

    for images, labels in train_loader:

        # 前向传播

        outputs = model(images)

        loss = criterion(outputs, labels)

        

        # 反向传播

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(train_loader):.4f}")
```

### 6、测试模型

在测试集上评估模型的准确率。

## 实例

```python
model.eval()  # 设置为评估模式

correct = 0

total = 0

with torch.no_grad():  # 评估时不需要计算梯度

    for images, labels in test_loader:

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)  # 预测类别

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"Test Accuracy: {accuracy:.2f}%")
```

### 7、完整代码

完整代码如下：

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import torch.optim as optim

from torchvision import datasets, transforms

# 1. 数据加载与预处理

transform = transforms.Compose([

    transforms.ToTensor(),  # 转为张量

    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1, 1]

])

# 加载 MNIST 数据集

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# 2. 定义 CNN 模型

class SimpleCNN(nn.Module):

    def __init__(self):

        super(SimpleCNN, self).__init__()

        # 定义卷积层

        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)  # 输入1通道，输出32通道

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)  # 输入32通道，输出64通道

        # 定义全连接层

        self.fc1 = nn.Linear(64 * 7 * 7, 128)  # 展平后输入到全连接层

        self.fc2 = nn.Linear(128, 10)  # 10 个类别

    def forward(self, x):

        x = F.relu(self.conv1(x))  # 第一层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = F.relu(self.conv2(x))  # 第二层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = x.view(-1, 64 * 7 * 7) # 展平

        x = F.relu(self.fc1(x))    # 全连接层 + ReLU

        x = self.fc2(x)            # 最后一层输出

        return x

# 创建模型实例

model = SimpleCNN()

# 3. 定义损失函数与优化器

criterion = nn.CrossEntropyLoss()  # 多分类交叉熵损失

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# 4. 模型训练

num_epochs = 5

model.train()  # 设置模型为训练模式

for epoch in range(num_epochs):

    total_loss = 0

    for images, labels in train_loader:

        outputs = model(images)  # 前向传播

        loss = criterion(outputs, labels)  # 计算损失

        optimizer.zero_grad()  # 清空梯度

        loss.backward()  # 反向传播

        optimizer.step()  # 更新参数

        total_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(train_loader):.4f}")

# 5. 模型测试

model.eval()  # 设置模型为评估模式

correct = 0

total = 0

with torch.no_grad():  # 关闭梯度计算

    for images, labels in test_loader:

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"Test Accuracy: {accuracy:.2f}%")
```

### 运行结果说明

**1. 输出的训练损失**

代码中每个 epoch 会输出一次平均损失，例如：

```python
Epoch [1/5], Loss: 0.2325

Epoch [2/5], Loss: 0.0526

Epoch [3/5], Loss: 0.0366

Epoch [4/5], Loss: 0.0273

Epoch [5/5], Loss: 0.0221
```

**解释：**损失逐渐下降表明模型在逐步收敛。

**2. 测试集的准确率**

代码在测试集上输出最终的分类准确率，例如：

```python
Test Accuracy: 98.96%
```

**解释：**模型对 MNIST 测试集的分类准确率为 98.96%，对于简单的 CNN 模型来说是一个不错的结果。

### 7、可视化结果

我们可以在测试数据中可视化一些样本及其预测结果。

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import torch.optim as optim

from torchvision import datasets, transforms

import matplotlib.pyplot as plt

# 1. 数据加载与预处理

transform = transforms.Compose([

    transforms.ToTensor(),  # 转为张量

    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1, 1]

])

# 加载 MNIST 数据集

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# 2. 定义 CNN 模型

class SimpleCNN(nn.Module):

    def __init__(self):

        super(SimpleCNN, self).__init__()

        # 定义卷积层

        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)  # 输入1通道，输出32通道

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)  # 输入32通道，输出64通道

        # 定义全连接层

        self.fc1 = nn.Linear(64 * 7 * 7, 128)  # 展平后输入到全连接层

        self.fc2 = nn.Linear(128, 10)  # 10 个类别

    def forward(self, x):

        x = F.relu(self.conv1(x))  # 第一层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = F.relu(self.conv2(x))  # 第二层卷积 + ReLU

        x = F.max_pool2d(x, 2)     # 最大池化

        x = x.view(-1, 64 * 7 * 7) # 展平

        x = F.relu(self.fc1(x))    # 全连接层 + ReLU

        x = self.fc2(x)            # 最后一层输出

        return x

# 创建模型实例

model = SimpleCNN()

# 3. 定义损失函数与优化器

criterion = nn.CrossEntropyLoss()  # 多分类交叉熵损失

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# 4. 模型训练

num_epochs = 5

model.train()  # 设置模型为训练模式

for epoch in range(num_epochs):

    total_loss = 0

    for images, labels in train_loader:

        outputs = model(images)  # 前向传播

        loss = criterion(outputs, labels)  # 计算损失

        optimizer.zero_grad()  # 清空梯度

        loss.backward()  # 反向传播

        optimizer.step()  # 更新参数

        total_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(train_loader):.4f}")

# 5. 模型测试

model.eval()  # 设置模型为评估模式

correct = 0

total = 0

with torch.no_grad():  # 关闭梯度计算

    for images, labels in test_loader:

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"Test Accuracy: {accuracy:.2f}%")

# 6. 可视化测试结果

dataiter = iter(test_loader)

images, labels = next(dataiter)

outputs = model(images)

_, predictions = torch.max(outputs, 1)

fig, axes = plt.subplots(1, 6, figsize=(12, 4))

for i in range(6):

    axes[i].imshow(images[i][0], cmap='gray')

    axes[i].set_title(f"Label: {labels[i]}\nPred: {predictions[i]}")

    axes[i].axis('off')

plt.show()
```

可视化结果展示了 6 个测试样本的实际标签与预测值，例如：

-

图片的左上角是手写数字。

-

标题部分显示了模型的预测值和真实标签。

## 注意几种错误

下载 MNIST 数据集时，由于 SSL 证书验证失败，导致无法下载数据。

```python
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz

Failed to download (trying next):

<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)>

...
```

### 解决办法

打开终端，运行以下命令来安装/更新 SSL 证书：

```python
/Applications/Python\ 3.x/Install\ Certificates.command
```

其中 3.x 替换为你实际安装的 Python 版本。

运行此命令后，重新运行你的 Python 代码，它应该能够成功下载 MNIST 数据集。

---

# PyTorch 循环神经网络（RNN）

-

循环神经网络（Recurrent Neural Networks, RNN）是一类神经网络架构，专门用于处理序列数据，能够捕捉时间序列或有序数据的动态信息，能够处理序列数据，如文本、时间序列或音频。

RNN 在自然语言处理（NLP）、语音识别、时间序列预测等任务中有着广泛的应用。

RNN 的关键特性是其能够保持隐状态（hidden state），使得网络能够记住先前时间步的信息，这对于处理序列数据至关重要。

### RNN 的基本结构

在传统的前馈神经网络（Feedforward Neural Network）中，数据是从输入层流向输出层的，而在 RNN 中，数据不仅沿着网络层级流动，还会在每个时间步骤上传播到当前的隐层状态，从而将之前的信息传递到下一个时间步骤。

**隐状态（Hidden State）：** RNN 通过隐状态来记住序列中的信息。

隐状态是通过上一时间步的隐状态和当前输入共同计算得到的。

循环单元的结构如下：

- 输入（\(x_t\)）：在时间步 \(t\) 的输入向量。

-
隐藏状态（\(h_t\)：在时间步 \(t\) 的隐藏状态向量，用于存储之前时间步的信息。

-
输出（\(y_t\)）：在时间步 \(t\) 的输出向量（可选，取决于具体任务）。

公式：

\[
h_t = f(W_{hh}h_{t-1} + W_{xh}x_t + b_h)
\]

- ht：当前时刻的隐状态。

-
ht-1：前一时刻的隐状态。

-
Xt：当前时刻的输入。

-
Whh、Wxh：权重矩阵。

-
b：偏置项。

-
f：激活函数（如 Tanh 或 ReLU）。

**输出（Output）：** RNN 的输出不仅依赖当前的输入，还依赖于隐状态的历史信息。

公式：

\[
y_t = W_{hy}h_t + b_y
\]

- yt：在时间步 t 的输出向量（可选，取决于具体任务）。

- Why：是隐藏状态到输出的权重矩阵。。

### RNN 如何处理序列数据

循环神经网络（RNN）在处理序列数据时的展开（unfold）视图如下：

RNN 是一种处理序列数据的神经网络，它通过循环连接来处理序列中的每个元素，并在每个时间步传递信息，以下是图中各部分的说明：

-

输入序列（Xt, Xt-1, Xt+1, ...）：图中的粉色圆圈代表输入序列中的各个元素，如Xt表示当前时间步的输入，Xt-1表示前一个时间步的输入，以此类推。

-

隐藏状态（ht, ht-1, ht+1, ...）：绿色矩形代表RNN的隐藏状态，它在每个时间步存储有关序列的信息。ht是当前时间步的隐藏状态，ht-1是前一个时间步的隐藏状态。

-

权重矩阵（U, W, V）：

- `U`：输入到隐藏状态的权重矩阵，用于将输入`Xt`转换为隐藏状态的一部分。

- `W`：隐藏状态到隐藏状态的权重矩阵，用于将前一时间步的隐藏状态`ht-1`转换为当前时间步隐藏状态的一部分。

- `V`：隐藏状态到输出的权重矩阵，用于将隐藏状态`ht`转换为输出`Yt`。

-

输出序列（Yt, Yt-1, Yt+1, ...）：蓝色圆圈代表RNN在每个时间步的输出，如Yt是当前时间步的输出。

-

循环连接：RNN的特点是隐藏状态的循环连接，这允许网络在处理当前时间步的输入时考虑到之前时间步的信息。

-

展开（Unfold）：图中展示了RNN在序列上的展开过程，这有助于理解RNN如何在时间上处理序列数据。在实际的RNN实现中，这些步骤是并行处理的，但在概念上，我们可以将其展开来理解信息是如何流动的。

-

信息流动：信息从输入序列通过权重矩阵U传递到隐藏状态，然后通过权重矩阵W在时间步之间传递，最后通过权重矩阵V从隐藏状态传递到输出序列。

## PyTorch 中的 RNN 基础

在 PyTorch 中，RNN 可以用于构建复杂的序列模型。

PyTorch 提供了几种 RNN 模块，包括：

- `torch.nn.RNN`：基本的RNN单元。

- `torch.nn.LSTM`：长短期记忆单元，能够学习长期依赖关系。

- `torch.nn.GRU`：门控循环单元，是LSTM的简化版本，但通常更容易训练。

使用 RNN 类时，您需要指定输入的维度、隐藏层的维度以及其他一些超参数。

### PyTorch 实现一个简单的 RNN 实例

以下是一个简单的 PyTorch 实现例子，使用 RNN 模型来处理序列数据并进行分类。

**1、导入必要库**

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.utils.data import DataLoader, TensorDataset

import numpy as np
```

**
2、定义 RNN 模型**

## 实例

```python
class SimpleRNN(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):

        super(SimpleRNN, self).__init__()

        # 定义 RNN 层

        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)

        # 定义全连接层

        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):

        # x: (batch_size, seq_len, input_size)

        out, _ = self.rnn(x)  # out: (batch_size, seq_len, hidden_size)

        # 取序列最后一个时间步的输出作为模型的输出

        out = out[:, -1, :]  # (batch_size, hidden_size)

        out = self.fc(out)  # 全连接层

        return out
```

**3、创建训练数据**

为了训练 RNN，我们生成一些随机的序列数据。这里的目标是将每个序列的最后一个值作为分类的目标。

## 实例

```python
# 生成一些随机序列数据

num_samples = 1000

seq_len = 10

input_size = 5

output_size = 2  # 假设二分类问题

# 随机生成输入数据 (batch_size, seq_len, input_size)

X = torch.randn(num_samples, seq_len, input_size)

# 随机生成目标标签 (batch_size, output_size)

Y = torch.randint(0, output_size, (num_samples,))

# 创建数据加载器

dataset = TensorDataset(X, Y)

train_loader = DataLoader(dataset, batch_size=32, shuffle=True)
```

**4、定义损失函数与优化器**

## 实例

```python
# 模型实例化

model = SimpleRNN(input_size=input_size, hidden_size=64, output_size=output_size)

# 定义损失函数和优化器

criterion = nn.CrossEntropyLoss()  # 多分类交叉熵损失

optimizer = optim.Adam(model.parameters(), lr=0.001)
```

**5、训练模型**

## 实例

```python
num_epochs = 10

for epoch in range(num_epochs):

    model.train()  # 设置模型为训练模式

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in train_loader:

        # 前向传播

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        # 反向传播和优化

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        # 计算准确率

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(train_loader):.4f}, Accuracy: {accuracy:.2f}%")
```

**6、测试模型**

训练结束后，我们可以在测试集上评估模型的表现。

## 实例

```python
# 测试模型

model.eval()  # 设置模型为评估模式

with torch.no_grad():

    total = 0

    correct = 0

    for inputs, labels in train_loader:

        outputs = model(inputs)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(f"Test Accuracy: {accuracy:.2f}%")
```

**
7、完整代码如下：**

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import matplotlib.pyplot as plt

import numpy as np

# 数据集：字符序列预测（Hello -> Elloh）

char_set = list("hello")

char_to_idx = {c: i for i, c in enumerate(char_set)}

idx_to_char = {i: c for i, c in enumerate(char_set)}

# 数据准备

input_str = "hello"

target_str = "elloh"

input_data = [char_to_idx[c] for c in input_str]

target_data = [char_to_idx[c] for c in target_str]

# 转换为独热编码

input_one_hot = np.eye(len(char_set))[input_data]

# 转换为 PyTorch Tensor

inputs = torch.tensor(input_one_hot, dtype=torch.float32)

targets = torch.tensor(target_data, dtype=torch.long)

# 模型超参数

input_size = len(char_set)

hidden_size = 8

output_size = len(char_set)

num_epochs = 200

learning_rate = 0.1

# 定义 RNN 模型

class RNNModel(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):

        super(RNNModel, self).__init__()

        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)

        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):

        out, hidden = self.rnn(x, hidden)

        out = self.fc(out)  # 应用全连接层

        return out, hidden

model = RNNModel(input_size, hidden_size, output_size)

# 定义损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 训练 RNN

losses = []

hidden = None  # 初始隐藏状态为 None

for epoch in range(num_epochs):

    optimizer.zero_grad()

    # 前向传播

    outputs, hidden = model(inputs.unsqueeze(0), hidden)

    hidden = hidden.detach()  # 防止梯度爆炸

    # 计算损失

    loss = criterion(outputs.view(-1, output_size), targets)

    loss.backward()

    optimizer.step()

    losses.append(loss.item())

    if (epoch + 1) % 20 == 0:

        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# 测试 RNN

with torch.no_grad():

    test_hidden = None

    test_output, _ = model(inputs.unsqueeze(0), test_hidden)

    predicted = torch.argmax(test_output, dim=2).squeeze().numpy()

    print("Input sequence: ", ''.join([idx_to_char[i] for i in input_data]))

    print("Predicted sequence: ", ''.join([idx_to_char[i] for i in predicted]))
```

**代码解析：**

-
**数据准备**：

- 使用字符序列 `hello`，并将其转化为独热编码。
- 目标序列为 `elloh`，即向右旋转一个字符。

-
**模型构建**：

- 使用 `torch.nn.RNN` 创建循环神经网络。
- 加入全连接层 `torch.nn.Linear` 用于映射隐藏状态到输出。

-
**训练部分**：

- 每一轮都计算损失并反向传播。
- 隐藏状态通过 `hidden.detach()` 防止梯度爆炸。

-
**测试部分**：

- 模型输出字符的预测结果。

-
**可视化**：

- 用 Matplotlib 绘制训练损失的变化趋势。

假设你的模型训练良好，输出可能如下：

```python
Epoch [20/200], Loss: 0.0013

Epoch [40/200], Loss: 0.0003

Epoch [60/200], Loss: 0.0002

Epoch [80/200], Loss: 0.0001

Epoch [100/200], Loss: 0.0001

Epoch [120/200], Loss: 0.0001

Epoch [140/200], Loss: 0.0001

Epoch [160/200], Loss: 0.0001

Epoch [180/200], Loss: 0.0001

Epoch [200/200], Loss: 0.0001

Input sequence:  hello
```

从结果来看，图像显示损失逐渐减少，表明模型训练有效。

**
8、可视化代码：**

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import matplotlib.pyplot as plt

import numpy as np

# 数据集：字符序列预测（Hello -> Elloh）

char_set = list("hello")

char_to_idx = {c: i for i, c in enumerate(char_set)}

idx_to_char = {i: c for i, c in enumerate(char_set)}

# 数据准备

input_str = "hello"

target_str = "elloh"

input_data = [char_to_idx[c] for c in input_str]

target_data = [char_to_idx[c] for c in target_str]

# 转换为独热编码

input_one_hot = np.eye(len(char_set))[input_data]

# 转换为 PyTorch Tensor

inputs = torch.tensor(input_one_hot, dtype=torch.float32)

targets = torch.tensor(target_data, dtype=torch.long)

# 模型超参数

input_size = len(char_set)

hidden_size = 8

output_size = len(char_set)

num_epochs = 200

learning_rate = 0.1

# 定义 RNN 模型

class RNNModel(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):

        super(RNNModel, self).__init__()

        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)

        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):

        out, hidden = self.rnn(x, hidden)

        out = self.fc(out)  # 应用全连接层

        return out, hidden

model = RNNModel(input_size, hidden_size, output_size)

# 定义损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 训练 RNN

losses = []

hidden = None  # 初始隐藏状态为 None

for epoch in range(num_epochs):

    optimizer.zero_grad()

    # 前向传播

    outputs, hidden = model(inputs.unsqueeze(0), hidden)

    hidden = hidden.detach()  # 防止梯度爆炸

    # 计算损失

    loss = criterion(outputs.view(-1, output_size), targets)

    loss.backward()

    optimizer.step()

    losses.append(loss.item())

    if (epoch + 1) % 20 == 0:

        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# 测试 RNN

with torch.no_grad():

    test_hidden = None

    test_output, _ = model(inputs.unsqueeze(0), test_hidden)

    predicted = torch.argmax(test_output, dim=2).squeeze().numpy()

    print("Input sequence: ", ''.join([idx_to_char[i] for i in input_data]))

    print("Predicted sequence: ", ''.join([idx_to_char[i] for i in predicted]))

# 可视化损失

plt.plot(losses, label="Training Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("RNN Training Loss Over Epochs")

plt.legend()

plt.show()
```

执行后，显示图片如下所示：

---

# PyTorch 数据集

在深度学习任务中，数据加载和处理是至关重要的一环。

PyTorch 提供了强大的数据加载和处理工具，主要包括：

-
**`torch.utils.data.Dataset`**：数据集的抽象类，需要自定义并实现 `__len__`（数据集大小）和 `__getitem__`（按索引获取样本）。

-
**`torch.utils.data.TensorDataset`**：基于张量的数据集，适合处理数据-标签对，直接支持批处理和迭代。

-
**`torch.utils.data.DataLoader`**：封装 Dataset 的迭代器，提供批处理、数据打乱、多线程加载等功能，便于数据输入模型训练。

-
**`torchvision.datasets.ImageFolder`**：从文件夹加载图像数据，每个子文件夹代表一个类别，适用于图像分类任务。

### PyTorch 内置数据集

PyTorch 通过 torchvision.datasets 模块提供了许多常用的数据集，例如：

- **MNIST**：手写数字图像数据集，用于图像分类任务。

- **CIFAR**：包含 10 个类别、60000 张 32x32 的彩色图像数据集，用于图像分类任务。

- **COCO**：通用物体检测、分割、关键点检测数据集，包含超过 330k 个图像和 2.5M 个目标实例的大规模数据集。

- **ImageNet**：包含超过 1400 万张图像，用于图像分类和物体检测等任务。

- **STL-10**：包含 100k 张 96x96 的彩色图像数据集，用于图像分类任务。

- **Cityscapes**：包含 5000 张精细注释的城市街道场景图像，用于语义分割任务。

- **SQUAD**：用于机器阅读理解任务的数据集。

以上数据集可以通过 torchvision.datasets 模块中的函数进行加载，也可以通过自定义的方式加载其他数据集。

### torchvision 和 torchtext

- **torchvision**： 一个图形库，提供了图片数据处理相关的 API 和数据集接口，包括数据集加载函数和常用的图像变换。

- **torchtext**： 自然语言处理工具包，提供了文本数据处理和建模的工具，包括数据预处理和数据加载的方式。

## torch.utils.data.Dataset

Dataset 是 PyTorch 中用于数据集抽象的类。

自定义数据集需要继承 torch.utils.data.Dataset 并重写以下两个方法：

- `__len__`：返回数据集的大小。
- `__getitem__`：按索引获取一个数据样本及其标签。

## 实例

```python
import torch

from torch.utils.data import Dataset

# 自定义数据集

class MyDataset(Dataset):

    def __init__(self, data, labels):

        # 数据初始化

        self.data = data

        self.labels = labels

    def __len__(self):

        # 返回数据集大小

        return len(self.data)

    def __getitem__(self, idx):

        # 按索引返回数据和标签

        sample = self.data[idx]

        label = self.labels[idx]

        return sample, label

# 生成示例数据

data = torch.randn(100, 5)  # 100 个样本，每个样本有 5 个特征

labels = torch.randint(0, 2, (100,))  # 100 个标签，取值为 0 或 1

# 实例化数据集

dataset = MyDataset(data, labels)

# 测试数据集

print("数据集大小:", len(dataset))

print("第 0 个样本:", dataset[0])
```

输出结果如下：

```python
数据集大小: 100

第 0 个样本: (tensor([-0.2006,  0.7304, -1.3911, -0.4408,  1.1447]), tensor(0))
```

## torch.utils.data.DataLoader

DataLoader 是 PyTorch 提供的数据加载器，用于批量加载数据集。

提供了以下功能：

- **批量加载**：通过设置 `batch_size`。
- **数据打乱**：通过设置 `shuffle=True`。
- **多线程加速**：通过设置 `num_workers`。
- **迭代访问**：方便地按批次访问数据。

## 实例

```python
import torch

from torch.utils.data import Dataset

from torch.utils.data import DataLoader

# 自定义数据集

class MyDataset(Dataset):

    def __init__(self, data, labels):

        # 数据初始化

        self.data = data

        self.labels = labels

    def __len__(self):

        # 返回数据集大小

        return len(self.data)

    def __getitem__(self, idx):

        # 按索引返回数据和标签

        sample = self.data[idx]

        label = self.labels[idx]

        return sample, label

# 生成示例数据

data = torch.randn(100, 5)  # 100 个样本，每个样本有 5 个特征

labels = torch.randint(0, 2, (100,))  # 100 个标签，取值为 0 或 1

# 实例化数据集

dataset = MyDataset(data, labels)

# 实例化 DataLoader

dataloader = DataLoader(dataset, batch_size=10, shuffle=True, num_workers=0)

# 遍历 DataLoader

for batch_idx, (batch_data, batch_labels) in enumerate(dataloader):

    print(f"批次 {batch_idx + 1}")

    print("数据:", batch_data)

    print("标签:", batch_labels)

    if batch_idx == 2:  # 仅显示前 3 个批次

        break
```

输出结果如下：

```python
批次 1

数据: tensor([[ 0.4689,  0.6666, -1.0234,  0.8948,  0.4503],

[ 0.0273, -0.4684, -0.7762,  0.7963,  0.2168],

[ 1.0677, -0.3502, -0.9594, -1.1318, -0.2196],

[-1.4989,  0.0267,  1.0405, -0.7284,  0.2335],

[-0.5887, -0.4934,  1.6283,  1.4638,  0.0157],

[-1.1047, -0.6550, -0.0381,  0.3617, -1.2792],

[ 0.3592, -0.8264,  0.0231, -1.5508,  0.6833],

[-0.6835,  0.6979,  0.9048, -0.4756,  0.3003],

[ 1.1562, -0.4516, -1.2415,  0.2859,  0.5837],

[ 0.7937,  1.5316, -0.6139,  0.7999,  0.5506]])

标签: tensor([0, 1, 1, 1, 1, 0, 1, 1, 0, 0])

批次 2

数据: tensor([[-0.0388, -0.3658,  0.8993, -1.5027,  1.0738],

[-0.6182,  1.0684, -2.3049,  0.8338,  0.1363],

[-0.5289,  0.1661, -0.0349,  0.2112,  1.4745],

[-0.3304, -1.2114, -0.2982, -0.3006,  0.5252],

[-1.4394, -0.3732,  1.0281,  0.5754,  1.0081],

[ 0.8714, -0.1945, -0.2451, -0.2879, -2.0520],

[ 0.0235,  0.4360,  0.1233,  0.0504,  0.5908],

[ 0.5927,  0.1785, -0.9052, -0.9012,  0.8914],

[ 0.4693,  0.5533, -0.1903,  0.0267,  0.4077],

[-1.1683,  1.6699, -0.4846, -0.7404,  0.3370]])

标签: tensor([1, 1, 0, 1, 0, 1, 1, 0, 1, 1])

批次 3

数据: tensor([[ 0.2103, -0.7839,  1.4899,  2.2749, -0.7548],

[-1.2836,  1.0025, -1.1162, -0.4261,  1.0690],

[-0.7969,  1.0418, -0.7405,  0.8766,  0.2347],

[-1.1071,  1.8560, -1.2979, -0.8364, -0.2925],

[-1.0488,  0.4802, -0.6453,  0.2009,  0.5693],

[ 0.8883,  0.4619, -0.2087,  0.2189, -0.3708],

[-1.4578,  0.3629,  1.8282,  0.5353, -1.1783],

[-1.2813,  0.5129, -0.4598, -0.2131, -1.2804],

[ 1.7831,  1.1730, -0.2305, -0.6550,  0.1197],

[-0.9384, -0.0483,  1.9626,  0.3342,  0.1700]])

标签: tensor([0, 0, 0, 1, 0, 1, 1, 1, 0, 1])
```

## 使用内置数据集

PyTorch 提供了多个常用数据集，存放在 torchvision 中，特别适合图像任务。

加载 MNIST 数据集:

## 实例

```python
import torchvision

import torchvision.transforms as transforms

from torch.utils.data import DataLoader

# 定义数据预处理

transform = transforms.Compose([

    transforms.ToTensor(),  # 转换为张量

    transforms.Normalize((0.5,), (0.5,))  # 标准化

])

# 加载训练数据集

train_dataset = torchvision.datasets.MNIST(

    root='./data', train=True, transform=transform, download=True)

# 使用 DataLoader 加载数据

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# 查看一个批次的数据

data_iter = iter(train_loader)

images, labels = next(data_iter)

print(f"批次图像大小: {images.shape}")  # 输出形状为 [batch_size, 1, 28, 28]

print(f"批次标签: {labels}")
```

输出结果为：

```python
批次图像大小: torch.Size([32, 1, 28, 28])

批次标签: tensor([0, 4, 9, 8, 1, 3, 8, 1, 7, 2, 1, 1, 1, 2, 6, 3, 9, 7, 6, 9, 4, 9, 7, 1,

3, 7, 3, 0, 7, 7, 6, 7])
```

## Dataset 与 DataLoader 的自定义应用

以下是一个将 CSV 文件 作为数据源，并通过自定义 Dataset 和 DataLoader 读取数据。

**CSV 文件内容如下（下载[runoob_pytorch_data.csv](https://static.jyshare.com/download/runoob_pytorch_data.csv)）：**

## 实例

```python
import torch

import pandas as pd

from torch.utils.data import Dataset, DataLoader

# 自定义 CSV 数据集

class CSVDataset(Dataset):

    def __init__(self, file_path):

        # 读取 CSV 文件

        self.data = pd.read_csv(file_path)

    def __len__(self):

        # 返回数据集大小

        return len(self.data)

    def __getitem__(self, idx):

        # 使用 .iloc 明确基于位置索引

        row = self.data.iloc[idx]

        # 将特征和标签分开

        features = torch.tensor(row.iloc[:-1].to_numpy(), dtype=torch.float32)  # 特征

        label = torch.tensor(row.iloc[-1], dtype=torch.float32)  # 标签

        return features, label

# 实例化数据集和 DataLoader

dataset = CSVDataset("runoob_pytorch_data.csv")

dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# 遍历 DataLoader

for features, label in dataloader:

    print("特征:", features)

    print("标签:", label)

    break
```

输出结果为：

```python
特征: tensor([[ 1.2000,  2.1000, -3.0000],

[ 1.0000,  1.1000, -2.0000],

[ 0.5000, -1.2000,  3.3000],

[-0.3000,  0.8000,  1.2000]])

标签: tensor([1., 0., 1., 0.])

tianqixin@Mac-mini runoob-test % python3 test.py

特征: tensor([[ 1.5000,  2.2000, -1.1000],

[ 2.1000, -3.3000,  0.0000],

[-2.3000,  0.4000,  0.7000],

[-0.3000,  0.8000,  1.2000]])

标签: tensor([0., 1., 0., 0.])
```

---

# PyTorch 数据转换

在 PyTorch 中，数据转换（Data Transformation） 是一种在加载数据时对数据进行处理的机制，将原始数据转换成适合模型训练的格式，主要通过 torchvision.transforms 提供的工具完成。

数据转换不仅可以实现基本的数据预处理（如归一化、大小调整等），还能帮助进行数据增强（如随机裁剪、翻转等），提高模型的泛化能力。

### 为什么需要数据转换？

**数据预处理**：

- 调整数据格式、大小和范围，使其适合模型输入。
- 例如，图像需要调整为固定大小、张量格式并归一化到 [0,1]。

**数据增强**：

- 在训练时对数据进行变换，以增加多样性。
- 例如，通过随机旋转、翻转和裁剪增加数据样本的变种，避免过拟合。

**灵活性**：

- 通过定义一系列转换操作，可以动态地对数据进行处理，简化数据加载的复杂度。

在 PyTorch 中，torchvision.transforms 模块提供了多种用于图像处理的变换操作。

### 基础变换操作

| 变换函数名称 | 描述 | 实例 |
| --- | --- | --- |
| transforms.ToTensor() | 将PIL图像或NumPy数组转换为PyTorch张量，并自动将像素值归一化到 [0, 1]。 | transform = transforms.ToTensor() |
| transforms.Normalize(mean, std) | 对图像进行标准化，使数据符合零均值和单位方差。 | transform = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) |
| transforms.Resize(size) | 调整图像尺寸，确保输入到网络的图像大小一致。 | transform = transforms.Resize((256, 256)) |
| transforms.CenterCrop(size) | 从图像中心裁剪指定大小的区域。 | transform = transforms.CenterCrop(224) |

**
1、ToTensor**

将 PIL 图像或 NumPy 数组转换为 PyTorch 张量。

同时将像素值从 [0, 255] 归一化为 [0, 1]。

```python
from torchvision import transforms

transform = transforms.ToTensor()
```

**2、Normalize**

对数据进行标准化，使其符合特定的均值和标准差。

通常用于图像数据，将其像素值归一化为零均值和单位方差。

```python
transform = transforms.Normalize(mean=[0.5], std=[0.5])  # 归一化到 [-1, 1]
```

**3、Resize**

调整图像的大小。

```python
transform = transforms.Resize((128, 128))  # 将图像调整为 128x128
```

**
4、CenterCrop**

从图像中心裁剪指定大小的区域。

```python
transform = transforms.CenterCrop(128)  # 裁剪 128x128 的区域
```

### 数据增强操作

| 变换函数名称 | 描述 | 实例 |
| --- | --- | --- |
| transforms.RandomHorizontalFlip(p) | 随机水平翻转图像。 | transform = transforms.RandomHorizontalFlip(p=0.5) |
| transforms.RandomRotation(degrees) | 随机旋转图像。 | transform = transforms.RandomRotation(degrees=45) |
| transforms.ColorJitter(brightness, contrast, saturation, hue) | 调整图像的亮度、对比度、饱和度和色调。 | transform = transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1) |
| transforms.RandomCrop(size) | 随机裁剪指定大小的区域。 | transform = transforms.RandomCrop(224) |
| transforms.RandomResizedCrop(size) | 随机裁剪图像并调整到指定大小。 | transform = transforms.RandomResizedCrop(224) |

**1、RandomCrop**

从图像中随机裁剪指定大小。

```python
transform = transforms.RandomCrop(128)
```

**2、RandomHorizontalFlip**

以一定概率水平翻转图像。

```python
transform = transforms.RandomHorizontalFlip(p=0.5)  # 50% 概率翻转
```

**3、RandomRotation**

随机旋转一定角度。

```python
transform = transforms.RandomRotation(degrees=30)  # 随机旋转 -30 到 +30 度
```

**4、ColorJitter**

随机改变图像的亮度、对比度、饱和度或色调。

```python
transform = transforms.ColorJitter(brightness=0.5, contrast=0.5)
```

### 组合变换

| 变换函数名称 | 描述 | 实例 |
| --- | --- | --- |
| transforms.Compose() | 将多个变换组合在一起，按照顺序依次应用。 | transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), transforms.Resize((256, 256))]) |

通过 transforms.Compose 将多个变换组合起来。

```python
transform = transforms.Compose([

transforms.Resize((128, 128)),

transforms.RandomHorizontalFlip(p=0.5),

transforms.ToTensor(),

transforms.Normalize(mean=[0.5], std=[0.5])

])
```

### 自定义转换

如果 transforms 提供的功能无法满足需求，可以通过自定义类或函数实现。

## 实例

```python
class CustomTransform:

    def __call__(self, x):

        # 这里可以自定义任何变换逻辑

        return x * 2

transform = CustomTransform()
```

## 实例

### 对图像数据集应用转换

加载 MNIST 数据集，并应用转换。

## 实例

```python
from torchvision import datasets, transforms

from torch.utils.data import DataLoader

# 定义转换

transform = transforms.Compose([

    transforms.Resize((128, 128)),

    transforms.ToTensor(),

    transforms.Normalize(mean=[0.5], std=[0.5])

])

# 加载数据集

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

# 使用 DataLoader

train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)

# 查看转换后的数据

for images, labels in train_loader:

    print("图像张量大小:", images.size())  # [batch_size, 1, 128, 128]

    break
```

输出结果为：

```python
图像张量大小: torch.Size([32, 1, 128, 128])
```

### 可视化转换效果

以下代码展示了原始数据和经过转换后的数据对比。

## 实例

```python
import matplotlib.pyplot as plt

from torchvision import datasets

from torchvision import datasets, transforms

# 原始和增强后的图像可视化

transform_augment = transforms.Compose([

    transforms.RandomHorizontalFlip(),

    transforms.RandomRotation(30),

    transforms.ToTensor()

])

# 加载数据集

dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform_augment)

# 显示图像

def show_images(dataset):

    fig, axs = plt.subplots(1, 5, figsize=(15, 5))

    for i in range(5):

        image, label = dataset[i]

        axs[i].imshow(image.squeeze(0), cmap='gray')  # 将 (1, H, W) 转为 (H, W)

        axs[i].set_title(f"Label: {label}")

        axs[i].axis('off')

    plt.show()

show_images(dataset)
```

显示如下所示：

---

# Pytorch torch 参考手册

PyTorch 软件包包含了用于多维张量的数据结构，并定义了在这些张量上执行的数学运算。此外，它还提供了许多实用工具，用于高效地序列化张量和任意类型的数据，以及其他有用的工具。

它还有一个 CUDA 版本，可以让你在计算能力 >= 3.0 的 NVIDIA GPU 上运行张量计算。

## PyTorch torch  API 手册

### Tensors 类型判断

| 函数 | 描述 |
| --- | --- |
| torch.is_tensor(obj) | 检查 obj 是否为 PyTorch 张量。 |
| torch.is_storage(obj) | 检查 obj 是否为 PyTorch 存储对象。 |
| torch.is_complex(input) | 检查 input 数据类型是否为复数数据类型。 |
| torch.is_conj(input) | 检查 input 是否为共轭张量。 |
| torch.is_floating_point(input) | 检查 input 数据类型是否为浮点数据类型。 |
| torch.is_nonzero(input) | 检查 input 是否为非零单一元素张量。 |
| torch.set_default_dtype(d) | 设置默认浮点数据类型为 d。 |
| torch.get_default_dtype() | 获取当前默认浮点 torch.dtype。 |
| torch.set_default_device(device) | 设置默认 torch.Tensor 分配的设备为 device。 |
| torch.get_default_device() | 获取默认 torch.Tensor 分配的设备。 |
| torch.set_default_tensor_type(tensor_type) | 设置默认张量类型为 tensor_type。 |
| torch.numel(input) | 返回 input 张量中的元素总数。 |
| torch.set_printoptions(...) | 设置张量打印选项。 |

### Tensor 创建

| 函数 | 描述 |
| --- | --- |
| torch.tensor(data, dtype, device, requires_grad) | 从数据创建张量，复制数据，无自动梯度历史。 |
| torch.as_tensor(data, dtype, device) | 将数据转换为张量，共享数据并保留自动梯度历史。 |
| torch.asarray(data, dtype, device) | 将数据转换为张量数组。 |
| torch.from_numpy(ndarray) | 从 NumPy 数组创建张量（共享内存）。 |
| torch.from_dlpack(ext_tensor) | 从 dlpack 张量创建 PyTorch 张量。 |
| torch.frombuffer(buffer, dtype, count, offset) | 从 buffer 创建一维张量。 |
| torch.zeros(*size, dtype, device, requires_grad) | 创建全零张量。 |
| torch.zeros_like(input, dtype, device, requires_grad) | 创建与输入相同形状的全零张量。 |
| torch.ones(*size, dtype, device, requires_grad) | 创建全一张量。 |
| torch.ones_like(input, dtype, device, requires_grad) | 创建与输入相同形状的全一张量。 |
| torch.empty(*size, dtype, device, requires_grad) | 创建未初始化的张量。 |
| torch.empty_like(input, dtype, device, requires_grad) | 创建与输入相同形状的未初始化张量。 |
| torch.empty_strided(size, stride, dtype, device) | 创建具有指定步幅的未初始化张量。 |
| torch.arange(start, end, step, dtype, device, requires_grad) | 创建等差序列张量。 |
| torch.range(start, end, step, dtype, device, requires_grad) | 创建包含 end 值的等差序列张量。 |
| torch.linspace(start, end, steps, dtype, device, requires_grad) | 创建等间隔序列张量。 |
| torch.logspace(start, end, steps, base, dtype, device, requires_grad) | 创建对数间隔序列张量。 |
| torch.eye(n, m, dtype, device, requires_grad) | 创建单位矩阵。 |
| torch.full(size, fill_value, dtype, device, requires_grad) | 创建填充指定值的张量。 |
| torch.full_like(input, fill_value, dtype, device, requires_grad) | 创建与输入相同形状的填充张量。 |
| torch.rand(*size, dtype, device, requires_grad) | 创建均匀分布随机张量（范围 [0, 1)）。 |
| torch.rand_like(input, dtype, device, requires_grad) | 创建与输入相同形状的均匀分布随机张量。 |
| torch.randn(*size, dtype, device, requires_grad) | 创建标准正态分布随机张量。 |
| torch.randn_like(input, dtype, device, requires_grad) | 创建与输入相同形状的标准正态分布随机张量。 |
| torch.randint(low, high, size, dtype, device, requires_grad) | 创建整数随机张量。 |
| torch.randint_like(input, low, high, dtype, device, requires_grad) | 创建与输入相同形状的整数随机张量。 |
| torch.randperm(n, dtype, device, requires_grad) | 创建 0 到 n-1 的随机排列。 |
| torch.sparse_coo_tensor(indices, values, size, dtype, device, requires_grad) | 在指定的 indices 处构造稀疏 COO 张量。 |
| torch.sparse_csr_tensor(crow_indices, col_indices, values, size, dtype, device) | 构造稀疏 CSR 张量。 |
| torch.sparse_csc_tensor(ccol_indices, row_indices, values, size, dtype, device) | 构造稀疏 CSC 张量。 |
| torch.quantize_per_tensor(input, scale, zero_point, dtype) | 创建量化张量（per-tensor）。 |
| torch.quantize_per_channel(input, scales, zero_points, axis, dtype) | 创建量化张量（per-channel）。 |
| torch.dequantize(input) | 反量化张量。 |
| torch.complex(real, imag) | 从实部和虚部创建复数张量。 |
| torch.polar(abs, angle) | 从极坐标创建复数张量。 |
| torch.heaviside(input, values) | 计算 Heaviside 阶跃函数。 |

### 索引、切片、连接、变异操作

| 函数 | 描述 |
| --- | --- |
| torch.cat(tensors, dim, out) | 沿指定维度连接张量。 |
| torch.concat(tensors, dim, out) | 沿指定维度连接张量（同 cat）。 |
| torch.concatenate(tensors, dim, out) | 沿指定维度连接张量（同 cat）。 |
| torch.stack(tensors, dim, out) | 沿新维度堆叠张量。 |
| torch.split(tensor, split_size, dim) | 将张量沿指定维度分割。 |
| torch.chunk(tensor, chunks, dim) | 将张量沿指定维度分块。 |
| torch.reshape(input, shape) | 改变张量的形状。 |
| torch.transpose(input, dim0, dim1) | 交换张量的两个维度。 |
| torch.t(input) | 转置二维张量。 |
| torch.squeeze(input, dim) | 移除大小为 1 的维度。 |
| torch.unsqueeze(input, dim) | 在指定位置插入大小为 1 的维度。 |
| torch.permute(input, dims) | 重新排列张量的维度。 |
| torch.movedim(input, source, destination) | 移动张量的维度到新位置。 |
| torch.moveaxis(input, source, destination) | 移动张量的轴到新位置。 |
| torch.narrow(input, dim, start, length) | 返回张量的切片。 |
| torch.narrow_copy(input, dim, start, length) | 返回张量的切片副本。 |
| torch.select(input, dim, index) | 沿指定维度选择索引对应的切片。 |
| torch.slice_scatter(input, src, dim, start, end) | 将 src 散布到 input 的切片中。 |
| torch.select_scatter(input, src, dim, index) | 将 src 散布到指定索引位置。 |
| torch.diagonal_scatter(input, src, offset, dim1, dim2) | 将值散布到对角线位置。 |
| torch.expand(input, size) | 扩展张量的尺寸（复制视图）。 |
| torch.expand_as(input, other) | 将张量扩展到与 other 相同的尺寸。 |
| torch.masked_select(input, mask) | 根据布尔掩码选择元素。 |
| torch.index_select(input, dim, index) | 沿指定维度选择索引对应的元素。 |
| torch.gather(input, dim, index, sparse_grad) | 沿指定维度收集指定索引的元素。 |
| torch.scatter(input, dim, index, src, reduce) | 将 src 的值散布到 input 的指定位置。 |
| torch.scatter_add(input, dim, index, src) | 将 src 的值加到指定位置。 |
| torch.scatter_reduce(input, dim, index, src, reduce, include_self) | 将 src 的值按指定方式聚合到指定位置。 |
| torch.index_add(input, dim, index, source, alpha) | 将 source 加到 index 指定的位置。 |
| torch.index_copy(input, dim, index, source) | 将 source 复制到 index 指定的位置。 |
| torch.index_reduce(input, dim, index, source, reduce, include_self) | 将 source 按指定方式聚合到 index 指定的位置。 |
| torch.take(input, index) | 获取给定索引位置的元素。 |
| torch.take_along_dim(input, indices, dim) | 沿指定维度获取索引位置的元素。 |
| torch.nonzero(input) | 返回非零元素的索引。 |
| torch.argwhere(input) | 返回满足条件的元素索引。 |
| torch.where(condition, input, other) | 根据条件返回元素。 |
| torch.unbind(tensor, dim) | 沿指定维度分割为元组。 |
| torch.split_with_sizes(tensor, split_sizes, dim) | 按大小分割张量。 |
| torch.tensor_split(tensor, indices_or_sections, dim) | 按索引或段数分割张量。 |
| torch.hsplit(tensor, indices_or_sections) | 水平分割张量。 |
| torch.vsplit(tensor, indices_or_sections) | 垂直分割张量。 |
| torch.dsplit(tensor, indices_or_sections) | 深度分割张量。 |
| torch.hstack(tensors, dim, out) | 水平堆叠张量。 |
| torch.vstack(tensors, out) | 垂直堆叠张量。 |
| torch.dstack(tensors, out) | 深度堆叠张量。 |
| torch.column_stack(tensors, out) | 列堆叠张量。 |
| torch.row_stack(tensors, out) | 行堆叠张量（同 vstack）。 |
| torch.tile(input, dims) | 重复张量多次。 |
| torch.repeat_interleave(input, repeats, dim) | 沿指定维度重复元素。 |
| torch.flip(input, dims) | 沿指定维度翻转张量。 |
| torch.fliplr(input) | 左右翻转张量。 |
| torch.flipud(input) | 上下翻转张量。 |
| torch.rot90(input, k, dims) | 旋转张量 90 度。 |
| torch.linalg.matrix_transpose(input) | 矩阵转置。 |
| torch.adjoint(input) | 返回张量的伴随矩阵。 |
| torch.resolve_conj(input) | 解析共轭张量。 |
| torch.resolve_neg(input) | 解析负张量。 |
| torch.view_as_real(input) | 将复数张量视为实数张量。 |
| torch.view_as_complex(input) | 将实数张量视为复数张量。 |
| torch.unravel_index(indices, shape) | 将展平索引转换为多维索引。 |

### 随机数生成

| 函数 | 描述 |
| --- | --- |
| torch.manual_seed(seed) | 设置随机种子（CPU）。 |
| torch.seed() | 设置随机种子并返回新的种子值。 |
| torch.initial_seed() | 返回当前随机种子。 |
| torch.get_rng_state() | 返回随机数生成器状态。 |
| torch.set_rng_state(state) | 设置随机数生成器状态。 |
| torch.rand(*size, dtype, device, requires_grad) | 创建均匀分布随机张量（范围 [0, 1)）。 |
| torch.rand_like(input, dtype, device, requires_grad) | 创建与输入相同形状的均匀分布随机张量。 |
| torch.randn(*size, dtype, device, requires_grad) | 创建标准正态分布随机张量。 |
| torch.randn_like(input, dtype, device, requires_grad) | 创建与输入相同形状的标准正态分布随机张量。 |
| torch.randint(low, high, size, dtype, device, requires_grad) | 创建整数随机张量。 |
| torch.randint_like(input, low, high, dtype, device, requires_grad) | 创建与输入相同形状的整数随机张量。 |
| torch.randperm(n, dtype, device, requires_grad) | 创建 0 到 n-1 的随机排列。 |
| torch.bernoulli(input, *, generator) | 从伯努利分布生成随机数。 |
| torch.multinomial(input, num_samples, replacement, generator) | 多项式采样。 |
| torch.normal(mean, std, out) | 从正态分布生成随机数。 |
| torch.poisson(input, generator) | 从泊松分布生成随机数。 |

### 序列化

| 函数 | 描述 |
| --- | --- |
| torch.save(obj, f, pickle_module, pickle_protocol) | 保存对象到文件。 |
| torch.load(f, map_location, pickle_module, weights_only) | 从文件加载对象。 |

### 梯度控制

| 函数 | 描述 |
| --- | --- |
| torch.no_grad() | 上下文管理器，禁用梯度计算。 |
| torch.enable_grad() | 上下文管理器，启用梯度计算。 |
| torch.set_grad_enabled(grad) | 设置是否启用梯度计算。 |
| torch.is_grad_enabled() | 检查是否启用梯度计算。 |
| torch.inference_mode() | 上下文管理器，推理模式（禁用梯度和 autograd）。 |
| torch.is_inference_mode_enabled() | 检查是否启用推理模式。 |

### 数学运算 - 点操作

| 函数 | 描述 |
| --- | --- |
| torch.abs(input, out) | 逐元素绝对值。 |
| torch.absolute(input, out) | 逐元素绝对值（同 abs）。 |
| torch.acos(input, out) | 逐元素反余弦。 |
| torch.arccos(input, out) | 逐元素反余弦（同 acos）。 |
| torch.acosh(input, out) | 逐元素反双曲余弦。 |
| torch.arccosh(input, out) | 逐元素反双曲余弦（同 acosh）。 |
| torch.add(input, other, alpha, out) | 逐元素加法（可指定 alpha 缩放）。 |
| torch.addcdiv(input, tensor1, tensor2, value, out) | 执行 input + value * (tensor1 / tensor2)。 |
| torch.addcmul(input, tensor1, tensor2, value, out) | 执行 input + value * (tensor1 * tensor2)。 |
| torch.angle(input, out) | 返回复数张量的相位角。 |
| torch.asin(input, out) | 逐元素反正弦。 |
| torch.arcsin(input, out) | 逐元素反正弦（同 asin）。 |
| torch.asinh(input, out) | 逐元素反双曲正弦。 |
| torch.arcsinh(input, out) | 逐元素反双曲正弦（同 asinh）。 |
| torch.atan(input, out) | 逐元素反正切。 |
| torch.arctan(input, out) | 逐元素反正切（同 atan）。 |
| torch.atan2(input, other, out) | 逐元素二维反正切。 |
| torch.arctan2(input, other, out) | 逐元素二维反正切（同 atan2）。 |
| torch.atanh(input, out) | 逐元素反双曲正切。 |
| torch.arctanh(input, out) | 逐元素反双曲正切（同 atanh）。 |
| torch.bitwise_not(input, out) | 逐元素按位取反。 |
| torch.bitwise_and(input, other, out) | 逐元素按位与。 |
| torch.bitwise_or(input, other, out) | 逐元素按位或。 |
| torch.bitwise_xor(input, other, out) | 逐元素按位异或。 |
| torch.bitwise_left_shift(input, other, out) | 逐元素左移位。 |
| torch.bitwise_right_shift(input, other, out) | 逐元素右移位。 |
| torch.ceil(input, out) | 逐元素向上取整。 |
| torch.clamp(input, min, max, out) | 将张量值限制在指定范围内。 |
| torch.clip(input, min, max, out) | 将张量值限制在指定范围内（同 clamp）。 |
| torch.conj_physical(input, out) | 逐元素计算物理共轭。 |
| torch.copysign(input, other, out) | 逐元素复制符号。 |
| torch.cos(input, out) | 逐元素余弦。 |
| torch.cosh(input, out) | 逐元素双曲余弦。 |
| torch.deg2rad(input, out) | 将角度转换为弧度。 |
| torch.div(input, other, rounding_mode, out) | 逐元素除法。 |
| torch.divide(input, other, rounding_mode, out) | 逐元素除法（同 div）。 |
| torch.digamma(input, out) | 逐元素计算 psi 函数（对数导数）。 |
| torch.erf(input, out) | 逐元素误差函数。 |
| torch.erfc(input, out) | 逐元素互补误差函数。 |
| torch.erfinv(input, out) | 逐元素误差函数逆。 |
| torch.exp(input, out) | 逐元素指数函数。 |
| torch.exp2(input, out) | 逐元素 2 的幂。 |
| torch.expm1(input, out) | 逐元素 exp(x) - 1。 |
| torch.fake_quantize_per_channel_affine(input, scale, zero_point, axis, quant_min, quant_max) | 模拟每通道量化。 |
| torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max) | 模拟每张量量化。 |
| torch.fix(input, out) | 逐元素取整数部分（向零取整）。 |
| torch.float_power(input, exponent, out) | 逐元素浮点幂运算。 |
| torch.floor(input, out) | 逐元素向下取整。 |
| torch.floor_divide(input, other, out) | 逐元素整除。 |
| torch.fmod(input, other, out) | 逐元素取模（余数）。 |
| torch.frac(input, out) | 逐元素取小数部分。 |
| torch.frexp(input, out) | 将浮点数分解为尾数和指数。 |
| torch.gradient(input, dim, spacing, edge_order) | 计算张量的梯度。 |
| torch.imag(input, out) | 返回复数张量的虚部。 |
| torch.ldexp(input, other, out) | 逐元素计算 input * 2**other。 |
| torch.lerp(input, end, weight, out) | 逐元素线性插值。 |
| torch.lgamma(input, out) | 逐元素 gamma 函数的对数。 |
| torch.log(input, out) | 逐元素自然对数。 |
| torch.log10(input, out) | 逐元素以 10 为底的对数。 |
| torch.log1p(input, out) | 逐元素 log(1 + x)。 |
| torch.log2(input, out) | 逐元素以 2 为底的对数。 |
| torch.logaddexp(input, other, out) | 逐元素 log(exp(input) + exp(other))。 |
| torch.logaddexp2(input, other, out) | 逐元素 log2(2**input + 2**other)。 |
| torch.logical_and(input, other, out) | 逐元素逻辑与。 |
| torch.logical_not(input, out) | 逐元素逻辑非。 |
| torch.logical_or(input, other, out) | 逐元素逻辑或。 |
| torch.logical_xor(input, other, out) | 逐元素逻辑异或。 |
| torch.logit(input, eps, out) | 逐元素 logit 函数。 |
| torch.hypot(input, other, out) | 逐元素 hypot 函数 sqrt(input^2 + other^2)。 |
| torch.i0(input, out) | 逐元素修正贝塞尔函数（第一类，0 阶）。 |
| torch.igamma(input, other, out) | 逐元素不完全 gamma 函数。 |
| torch.igammac(input, other, out) | 逐元素互补不完全 gamma 函数。 |
| torch.mul(input, other, out) | 逐元素乘法。 |
| torch.multiply(input, other, out) | 逐元素乘法（同 mul）。 |
| torch.mvlgamma(input, p, out) | 逐元素多元 gamma 函数的对数。 |
| torch.nan_to_num(input, nan, posinf, neginf, out) | 将 NaN 替换为指定值。 |
| torch.neg(input, out) | 逐元素取负。 |
| torch.negative(input, out) | 逐元素取负（同 neg）。 |
| torch.nextafter(input, other, out) | 逐元素返回下一个可表示的浮点数。 |
| torch.polygamma(input, n, out) | 逐元素 polygamma 函数。 |
| torch.positive(input, out) | 逐元素取正。 |
| torch.pow(input, exponent, out) | 逐元素幂运算。 |
| torch.quantized_batch_norm(input, weight, bias, mean, var, eps, output_scale, output_zero_point) | 量化批归一化。 |
| torch.quantized_max_pool1d(input, kernel_size, stride, padding, dilation, ceil_mode) | 量化最大池化（1D）。 |
| torch.quantized_max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode) | 量化最大池化（2D）。 |
| torch.rad2deg(input, out) | 将弧度转换为角度。 |
| torch.real(input, out) | 返回复数张量的实部。 |
| torch.reciprocal(input, out) | 逐元素倒数。 |
| torch.remainder(input, other, out) | 逐元素取余。 |
| torch.round(input, decimals, out) | 逐元素四舍五入。 |
| torch.rsqrt(input, out) | 逐元素平方根倒数。 |
| torch.sigmoid(input, out) | 逐元素 sigmoid 函数。 |
| torch.sign(input, out) | 逐元素返回符号（-1, 0, 1）。 |
| torch.sgn(input, out) | 逐元素返回符号向量。 |
| torch.signbit(input, out) | 逐元素检查符号位。 |
| torch.sin(input, out) | 逐元素正弦。 |
| torch.sinc(input, out) | 逐元素 sinc 函数 sin(pi*x)/(pi*x)。 |
| torch.sinh(input, out) | 逐元素双曲正弦。 |
| torch.softmax(input, dim, dtype) | 逐元素 softmax 函数。 |
| torch.sqrt(input, out) | 逐元素平方根。 |
| torch.square(input, out) | 逐元素平方。 |
| torch.sub(input, other, alpha, out) | 逐元素减法。 |
| torch.subtract(input, other, alpha, out) | 逐元素减法（同 sub）。 |
| torch.tan(input, out) | 逐元素正切。 |
| torch.tanh(input, out) | 逐元素双曲正切。 |
| torch.true_divide(input, other, out) | 逐元素真除法。 |
| torch.trunc(input, out) | 逐元素截断（取整数部分）。 |
| torch.xlogy(input, other, out) | 逐元素计算 input * log(other)。 |

### 数学运算 - 归约操作

| 函数 | 描述 |
| --- | --- |
| torch.argmax(input, dim, keepdim) | 返回沿维度最大值的索引。 |
| torch.argmin(input, dim, keepdim) | 返回沿维度最小值的索引。 |
| torch.amax(input, dim, keepdim, out) | 返回沿维度的最大值。 |
| torch.amin(input, dim, keepdim, out) | 返回沿维度的最小值。 |
| torch.aminmax(input, dim, keepdim, out) | 返回沿维度的最小值和最大值。 |
| torch.all(input, dim, keepdim, out) | 判断是否所有元素都为 True。 |
| torch.any(input, dim, keepdim, out) | 判断是否有元素为 True。 |
| torch.max(input, dim, keepdim, out) | 沿指定维度求最大值。 |
| torch.min(input, dim, keepdim, out) | 沿指定维度求最小值。 |
| torch.dist(input, other, p) | 计算两个张量之间的 p 范数距离。 |
| torch.logsumexp(input, dim, keepdim, out) | 计算 log-sum-exp。 |
| torch.mean(input, dim, keepdim, out) | 沿指定维度求均值。 |
| torch.nanmean(input, dim, keepdim, out) | 沿指定维度求均值（忽略 NaN）。 |
| torch.median(input, dim, keepdim, out) | 沿指定维度求中位数。 |
| torch.nanmedian(input, dim, keepdim, out) | 沿指定维度求中位数（忽略 NaN）。 |
| torch.mode(input, dim, keepdim, out) | 沿指定维度求众数。 |
| torch.norm(input, p, dim, keepdim, out) | 计算 p 范数。 |
| torch.nansum(input, dim, keepdim, out) | 沿指定维度求和（忽略 NaN）。 |
| torch.prod(input, dim, keepdim, dtype, out) | 沿指定维度求积。 |
| torch.quantile(input, q, dim, keepdim, out, method) | 计算分位数。 |
| torch.nanquantile(input, q, dim, keepdim, out, method) | 计算分位数（忽略 NaN）。 |
| torch.std(input, dim, unbiased, keepdim, out) | 计算标准差。 |
| torch.std_mean(input, dim, unbiased, keepdim) | 计算标准差和均值。 |
| torch.sum(input, dim, keepdim, dtype, out) | 沿指定维度求和。 |
| torch.unique(input, sorted, return_inverse, return_counts, dim) | 返回唯一元素。 |
| torch.unique_consecutive(input, sorted, return_inverse, return_counts, dim) | 返回连续唯一元素。 |
| torch.var(input, dim, unbiased, keepdim, out) | 计算方差。 |
| torch.var_mean(input, dim, unbiased, keepdim) | 计算方差和均值。 |
| torch.count_nonzero(input, dim) | 统计非零元素数量。 |
| torch.hash_tensor(input) | 计算张量的哈希值。 |

### 数学运算 - 比较操作

| 函数 | 描述 |
| --- | --- |
| torch.allclose(input, other, rtol, atol, equal_nan) | 检查两个张量是否接近（所有元素）。 |
| torch.argsort(input, dim, descending, stable) | 返回排序后的索引。 |
| torch.eq(input, other, out) | 逐元素相等比较。 |
| torch.equal(input, other) | 检查两个张量是否完全相等。 |
| torch.ge(input, other, out) | 逐元素大于等于比较。 |
| torch.greater_equal(input, other, out) | 逐元素大于等于比较（同 ge）。 |
| torch.gt(input, other, out) | 逐元素大于比较。 |
| torch.greater(input, other, out) | 逐元素大于比较（同 gt）。 |
| torch.isclose(input, other, rtol, atol, equal_nan) | 检查两个张量是否接近（逐元素）。 |
| torch.isfinite(input, out) | 检查是否为有限值。 |
| torch.isin(elements, test_elements, assume_unique, invert) | 检查元素是否在集合中。 |
| torch.isinf(input, out) | 检查是否为无穷值。 |
| torch.isposinf(input, out) | 检查是否为正无穷。 |
| torch.isneginf(input, out) | 检查是否为负无穷。 |
| torch.isnan(input, out) | 检查是否为 NaN。 |
| torch.isreal(input, out) | 检查是否为实数。 |
| torch.kthvalue(input, k, dim, keepdim, out) | 返回第 k 小的元素和索引。 |
| torch.le(input, other, out) | 逐元素小于等于比较。 |
| torch.less_equal(input, other, out) | 逐元素小于等于比较（同 le）。 |
| torch.lt(input, other, out) | 逐元素小于比较。 |
| torch.less(input, other, out) | 逐元素小于比较（同 lt）。 |
| torch.maximum(input, other, out) | 逐元素取最大值。 |
| torch.minimum(input, other, out) | 逐元素取最小值。 |
| torch.fmax(input, other, out) | 逐元素取最大值（忽略 NaN）。 |
| torch.fmin(input, other, out) | 逐元素取最小值（忽略 NaN）。 |
| torch.ne(input, other, out) | 逐元素不等比较。 |
| torch.not_equal(input, other, out) | 逐元素不等比较（同 ne）。 |
| torch.sort(input, dim, descending, stable, out) | 沿指定维度排序。 |
| torch.topk(input, k, dim, largest, sorted, out) | 返回最大的 k 个元素和索引。 |
| torch.msort(input, out) | 沿最后一个维度排序（返回排序后的张量）。 |

### 数学运算 - 谱操作

| 函数 | 描述 |
| --- | --- |
| torch.stft(input, n_fft, hop_length, win_length, window, center, normalized, onesided, return_complex) | 短时傅里叶变换。 |
| torch.istft(input, n_fft, hop_length, win_length, window, center, normalized, onesided, length, return_complex) | 短时傅里叶变换逆。 |
| torch.bartlett_window(window_length, periodic, dtype, device) | Bartlett 窗口。 |
| torch.blackman_window(window_length, periodic, dtype, device) | Blackman 窗口。 |
| torch.hamming_window(window_length, periodic, alpha, beta, dtype, device) | Hamming 窗口。 |
| torch.hann_window(window_length, periodic, dtype, device) | Hann 窗口。 |
| torch.kaiser_window(window_length, periodic, beta, dtype, device) | Kaiser 窗口。 |

### 数学运算 - 其他操作

| 函数 | 描述 |
| --- | --- |
| torch.atleast_1d(*tensors) | 将输入转换为至少 1 维的张量。 |
| torch.atleast_2d(*tensors) | 将输入转换为至少 2 维的张量。 |
| torch.atleast_3d(*tensors) | 将输入转换为至少 3 维的张量。 |
| torch.bincount(input, weights, minlength) | 计算非负整数的出现次数。 |
| torch.block_diag(*tensors) | 从输入张量构建块对角矩阵。 |
| torch.broadcast_tensors(*tensors) | 将输入广播到相同形状。 |
| torch.broadcast_to(input, shape) | 将张量广播到指定形状。 |
| torch.broadcast_shapes(*shapes) | 广播形状以兼容操作。 |
| torch.bucketize(input, boundaries, right) | 将输入映射到桶索引。 |
| torch.cartesian_prod(*tensors) | 计算笛卡尔积。 |
| torch.cdist(x1, x2, p, compute_mode) | 计算成对距离。 |
| torch.clone(input, memory_format) | 返回张量的副本。 |
| torch.combinations(input, r, with_replacement) | 计算组合。 |
| torch.corrcoef(input) | 计算相关系数矩阵。 |
| torch.cov(input, correction, fweights, aweights) | 计算协方差矩阵。 |
| torch.cross(input, dim, out) | 计算叉积。 |
| torch.cummax(input, dim, out) | 沿维度累积最大值。 |
| torch.cummin(input, dim, out) | 沿维度累积最小值。 |
| torch.cumprod(input, dim, out) | 沿维度累积乘积。 |
| torch.cumsum(input, dim, out, dtype) | 沿维度累积和。 |
| torch.diag(input, diagonal, out) | 创建对角矩阵或提取对角线。 |
| torch.diag_embed(input, offset, dim1, dim2, out) | 将输入作为对角线嵌入。 |
| torch.diagflat(input, offset, out) | 创建对角矩阵（扁平输入）。 |
| torch.diagonal(input, offset, dim1, dim2, out) | 提取对角线元素。 |
| torch.diff(input, n, dim, prepend, append, out) | 计算差分。 |
| torch.einsum(equation, *operands) | 爱因斯坦求和约定。 |
| torch.flatten(input, start_dim, end_dim, out) | 展平张量。 |
| torch.ravel(input, out) | 展平为一维张量。 |
| torch.kron(input, other, out) | 计算 Kronecker 积。 |
| torch.meshgrid(*tensors, indexing) | 创建网格。 |
| torch.lcm(input, other, out) | 逐元素最小公倍数。 |
| torch.logcumsumexp(input, dim, out) | 沿维度累积 log-sum-exp。 |
| torch.renorm(input, p, dim, maxnorm, out) | 重归一化到指定范数。 |
| torch.roll(input, shifts, dims) | 滚动张量元素。 |
| torch.searchsorted(sorted_sequence, values, side, sorter) | 在排序序列中搜索位置。 |
| torch.tensordot(a, b, dims) | 计算张量点积。 |
| torch.trace(input, out) | 计算矩阵迹。 |
| torch.tril(input, diagonal, out) | 提取下三角矩阵。 |
| torch.tril_indices(row, column, offset, dtype, device, layout) | 生成下三角索引。 |
| torch.triu(input, diagonal, out) | 提取上三角矩阵。 |
| torch.triu_indices(row, column, offset, dtype, device, layout) | 生成上三角索引。 |
| torch.unflatten(input, dim, sizes) | 展开张量。 |
| torch.vander(x, N, increasing, out) | 创建 Vandermonde 矩阵。 |

### 线性代数 (BLAS 和 LAPACK)

| 函数 | 描述 |
| --- | --- |
| torch.addbmm(input, batch1, batch2, beta, alpha, out) | 批量矩阵乘加。 |
| torch.addmm(input, mat1, mat2, beta, alpha, out) | 矩阵乘加。 |
| torch.addmv(input, mat, vec, beta, alpha, out) | 矩阵向量乘加。 |
| torch.addr(input, vec1, vec2, beta, alpha, out) | 向量外积加。 |
| torch.baddbmm(input, batch1, batch2, beta, alpha, out) | 批量矩阵乘加（bmm + add）。 |
| torch.bmm(input, mat2, out) | 批量矩阵乘法。 |
| torch.chain_matmul(*matrices) | 链式矩阵乘法。 |
| torch.cholesky(input, upper, out) | Cholesky 分解。 |
| torch.cholesky_inverse(input, upper, out) | Cholesky 分解求逆。 |
| torch.cholesky_solve(input, input2, upper, out) | Cholesky 分解求解线性方程。 |
| torch.dot(input, other, out) | 计算两个向量的点积。 |
| torch.geqrf(input, out) | QR 分解（geqrf）。 |
| torch.ger(input, other, out) | 计算向量外积。 |
| torch.inner(input, other, out) | 计算内积。 |
| torch.inverse(input, out) | 计算矩阵的逆。 |
| torch.det(input, out) | 计算矩阵的行列式。 |
| torch.logdet(input, out) | 计算行列式的对数。 |
| torch.slogdet(input, out) | 计算行列式的符号和对数绝对值。 |
| torch.lu(input, pivot, get_infos, out) | LU 分解。 |
| torch.lu_solve(input, LU_data, LU_pivots, out) | LU 分解求解。 |
| torch.lu_unpack(LU_data, LU_pivots, unpack_data, unpack_pivots) | 解包 LU 分解结果。 |
| torch.matmul(input, other, out) | 矩阵乘法（支持不同维度）。 |
| torch.matrix_power(input, n, out) | 矩阵幂运算。 |
| torch.matrix_exp(input, out) | 矩阵指数。 |
| torch.mm(input, mat2, out) | 矩阵乘法（二维）。 |
| torch.mv(input, vec, out) | 矩阵向量乘法。 |
| torch.orgqr(input, q, out) | 从 QR 分解重构 Q。 |
| torch.ormqr(input, mat, vec, left, transpose, out) | ormqr 操作。 |
| torch.outer(input, other, out) | 计算向量外积。 |
| torch.pinverse(input, rcond, out) | 计算Moore-Penrose 伪逆。 |
| torch.qr(input, out) | QR 分解。 |
| torch.svd(input, some, compute_uv, out) | 奇异值分解。 |
| torch.svd_lowrank(input, q, niter, M) | 低秩 SVD 近似。 |
| torch.pca_lowrank(input, q, center, niter) | 低秩 PCA 近似。 |
| torch.lobpcg(input, K, B, X, M, P, max_iter, tol, debug, ortho_iparams, fpfloor) | LOBPCG 特征值求解器。 |
| torch.trapz(y, x, dim, out) | 梯形积分（已废弃，使用 trapezoid）。 |
| torch.trapezoid(y, x, dim, out) | 梯形积分。 |
| torch.cumulative_trapezoid(y, x, dim, out) | 累积梯形积分。 |
| torch.triangular_solve(input, A, upper, transpose, unitriangular, out) | 三角矩阵求解。 |
| torch.vdot(input, other, out) | 计算向量点积（复数感知）。 |

### 设备管理

| 函数 | 描述 |
| --- | --- |
| torch.cuda.is_available() | 检查 CUDA 是否可用。 |
| torch.cuda.device_count() | 返回 CUDA 设备数量。 |
| torch.cuda.current_device() | 返回当前 CUDA 设备索引。 |
| torch.cuda.device(name) | 创建一个设备对象。 |
| torch.cuda.device_context(device) | 创建设备上下文。 |
| torch.device(device) | 创建一个设备对象（如 'cpu' 或 'cuda:0'）。 |
| torch.Tensor.to(device) | 将张量移动到指定设备。 |
| torch.get_device_module(device_type) | 获取设备模块（如 cuda, mps）。 |

### 并行计算

| 函数 | 描述 |
| --- | --- |
| torch.get_num_threads() | 获取用于 CPU 操作的总线程数。 |
| torch.set_num_threads(int) | 设置用于 CPU 操作的线程数。 |
| torch.get_num_interop_threads() | 获取 inter-op 并行线程数。 |
| torch.set_num_interop_threads(int) | 设置 inter-op 并行线程数。 |

### 工具函数

| 函数 | 描述 |
| --- | --- |
| torch.compiled_with_cxx11_abi() | 检查是否使用 C++11 ABI 编译。 |
| torch.result_type(tensor, other) | 返回操作结果的 dtype。 |
| torch.can_cast(from_dtype, to_dtype) | 检查是否可以转换数据类型。 |
| torch.promote_types(type1, type2) | 返回提升后的数据类型。 |
| torch.use_deterministic_algorithms(mode, warn_only) | 启用/禁用确定性算法。 |
| torch.are_deterministic_algorithms_enabled() | 检查是否启用确定性算法。 |
| torch.is_deterministic_algorithms_warn_only_enabled() | 检查确定性算法是否为警告模式。 |
| torch.set_deterministic_debug_mode(debug_mode) | 设置确定性调试模式。 |
| torch.get_deterministic_debug_mode() | 获取确定性调试模式。 |
| torch.set_float32_matmul_precision(precision) | 设置 float32 矩阵乘法的精度。 |
| torch.get_float32_matmul_precision() | 获取 float32 矩阵乘法的精度。 |
| torch.set_warn_always(enabled) | 设置是否始终显示警告。 |
| torch.is_warn_always_enabled() | 检查是否始终显示警告。 |
| torch.vmap(fn, in_dims, out_dims, randomness, chunk_size) | 向量化映射。 |
| torch._assert(condition, message) | 断言检查（内部使用）。 |
| torch.typename(t) | 返回类型的字符串表示。 |

### 编译优化

| 函数 | 描述 |
| --- | --- |
| torch.compile(model, backend, options, dynamic) | 编译 PyTorch 模型进行优化。 |

### 实例

## 实例

```python
import torch

# 创建张量

x = torch.tensor([1, 2, 3])

y = torch.zeros(2, 3)

# 数学运算

z = torch.add(x, 1)  # 逐元素加 1

print(z)

# 索引和切片

mask = x > 1

selected = torch.masked_select(x, mask)

print(selected)

# 设备管理

if torch.cuda.is_available():

    device = torch.device('cuda')

    x = x.to(device)

    print(x.device)

# 矩阵运算

a = torch.randn(3, 4)

b = torch.randn(4, 5)

c = torch.matmul(a, b)

print(c.shape)

# 梯度计算

x = torch.tensor([1., 2., 3.], requires_grad=True)

y = x.sum()

y.backward()

print(x.grad)
```

输出结果：

```python
tensor([2, 3, 4])

tensor([2, 3])
```

如果需要更详细的信息，可以参考 [PyTorch 官方文档](https://pytorch.org/docs/stable/torch.html)。

---

# PyTorch torch.nn 参考手册

PyTorch 的 `torch.nn` 模块是构建和训练神经网络的核心模块，它提供了丰富的类和函数来定义和操作神经网络。

以下是 `torch.nn` 模块的一些关键组成部分及其功能：

**1、nn.Module 类**：

- `nn.Module` 是所有自定义神经网络模型的基类。用户通常会从这个类派生自己的模型类，并在其中定义网络层结构以及前向传播函数（forward pass）。

**2、预定义层（Modules）**：

- 包括各种类型的层组件，例如卷积层（`nn.Conv1d`, `nn.Conv2d`, `nn.Conv3d`）、全连接层（`nn.Linear`）、激活函数（`nn.ReLU`, `nn.Sigmoid`, `nn.Tanh`）等。

**3、容器类**：

- `nn.Sequential`：允许将多个层按顺序组合起来，形成简单的线性堆叠网络。

- `nn.ModuleList` 和 `nn.ModuleDict`：可以动态地存储和访问子模块，支持可变长度或命名的模块集合。

**4、损失函数（Loss Functions）**：

- `torch.nn` 包含了一系列用于衡量模型预测与真实标签之间差异的损失函数，例如均方误差损失（`nn.MSELoss`）、交叉熵损失（`nn.CrossEntropyLoss`）等。

**5、实用函数接口（Functional Interface）**：

- `nn.functional`（通常简写为 `F`），包含了许多可以直接作用于张量上的函数，它们实现了与层对象相同的功能，但不具有参数保存和更新的能力。例如，可以使用 `F.relu()` 直接进行 ReLU 操作，或者 `F.conv2d()` 进行卷积操作。

**6、初始化方法**：

- `torch.nn.init` 提供了一些常用的权重初始化策略，比如 Xavier 初始化 (`nn.init.xavier_uniform_()`) 和 Kaiming 初始化 (`nn.init.kaiming_uniform_()`)，这些对于成功训练神经网络至关重要。

**7、Transformer 层**：

- PyTorch 提供了完整的 Transformer 架构组件，包括 `nn.Transformer`, `nn.TransformerEncoder`, `nn.TransformerDecoder` 以及注意力机制 `nn.MultiheadAttention` 等。

**8、归一化层**：

- 包括批归一化（`BatchNorm`）、层归一化（`LayerNorm`）、组归一化（`GroupNorm`）、实例归一化（`InstanceNorm`）和 RMSNorm 等。

## PyTorch torch.nn 模块参考手册

### 神经网络容器

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Module | 所有神经网络模块的基类。 |
| torch.nn.Sequential(*args) | 按顺序组合多个模块。 |
| torch.nn.ModuleList(modules) | 将子模块存储在列表中。 |
| torch.nn.ModuleDict(modules) | 将子模块存储在字典中。 |
| torch.nn.ParameterList(parameters) | 将参数存储在列表中。 |
| torch.nn.ParameterDict(parameters) | 将参数存储在字典中。 |
| torch.nn.Parameter(data) | 创建一个可学习的参数张量。 |
| torch.nn.Buffer(data) | 创建一个持久化的缓冲区（非学习参数）。 |
| torch.nn.Identity(*args, **kwargs) | 恒等变换层，输入直接输出。 |

### 全局钩子（Global Hooks）

| 函数 | 描述 |
| --- | --- |
| register_module_forward_pre_hook(hook) | 注册前向预钩子。 |
| register_module_forward_hook(hook) | 注册前向钩子。 |
| register_module_backward_hook(hook) | 注册反向钩子。 |
| register_module_full_backward_pre_hook(hook) | 注册完整的反向预钩子。 |
| register_module_full_backward_hook(hook) | 注册完整的反向钩子。 |

### 线性层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Linear(in_features, out_features, bias) | 全连接层（线性变换）。 |
| torch.nn.Bilinear(in1_features, in2_features, out_features, bias) | 双线性层。 |
| torch.nn.LazyLinear(out_features, bias) | 延迟初始化的线性层，第一次前向传播时自动推断输入维度。 |

### 卷积层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Conv1d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode) | 一维卷积层，常用于文本和音频。 |
| torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode) | 二维卷积层，常用于图像。 |
| torch.nn.Conv3d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode) | 三维卷积层，常用于视频和体数据。 |
| torch.nn.ConvTranspose1d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation, padding_mode) | 一维转置卷积（反卷积），用于上采样。 |
| torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation, padding_mode) | 二维转置卷积（反卷积），用于上采样。 |
| torch.nn.ConvTranspose3d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation, padding_mode) | 三维转置卷积（反卷积），用于上采样。 |
| torch.nn.Unfold(kernel_size, dilation, padding, stride) | 将输入张量展开为滑动窗口块。 |
| torch.nn.Fold(output_size, kernel_size, dilation, padding, stride) | 将展开的块重新组合为张量。 |

### 池化层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.MaxPool1d(kernel_size, stride, padding, dilation, return_indices) | 一维最大池化层。 |
| torch.nn.MaxPool2d(kernel_size, stride, padding, dilation, return_indices, ceil_mode) | 二维最大池化层。 |
| torch.nn.MaxPool3d(kernel_size, stride, padding, dilation, return_indices, ceil_mode) | 三维最大池化层。 |
| torch.nn.MaxUnpool1d(kernel_size, stride, padding) | 一维最大反池化层。 |
| torch.nn.MaxUnpool2d(kernel_size, stride, padding) | 二维最大反池化层。 |
| torch.nn.MaxUnpool3d(kernel_size, stride, padding) | 三维最大反池化层。 |
| torch.nn.AvgPool1d(kernel_size, stride, padding) | 一维平均池化层。 |
| torch.nn.AvgPool2d(kernel_size, stride, padding, ceil_mode, count_include_pad) | 二维平均池化层。 |
| torch.nn.AvgPool3d(kernel_size, stride, padding, ceil_mode, count_include_pad) | 三维平均池化层。 |
| torch.nn.AdaptiveMaxPool1d(output_size, return_indices) | 一维自适应最大池化，输出尺寸固定。 |
| torch.nn.AdaptiveMaxPool2d(output_size, return_indices) | 二维自适应最大池化，输出尺寸固定。 |
| torch.nn.AdaptiveMaxPool3d(output_size, return_indices) | 三维自适应最大池化，输出尺寸固定。 |
| torch.nn.AdaptiveAvgPool1d(output_size) | 一维自适应平均池化，输出尺寸固定。 |
| torch.nn.AdaptiveAvgPool2d(output_size) | 二维自适应平均池化，输出尺寸固定。 |
| torch.nn.AdaptiveAvgPool3d(output_size) | 三维自适应平均池化，输出尺寸固定。 |
| torch.nn.LPPool1d(norm_type, kernel_size, stride, padding) | 一维 Lp 池化层。 |
| torch.nn.LPPool2d(norm_type, kernel_size, stride, padding) | 二维 Lp 池化层。 |
| torch.nn.FractionalMaxPool2d(kernel_size, output_size, output_ratio, return_indices) | 二维分数最大池化，使用随机步长。 |
| torch.nn.FractionalMaxPool3d(kernel_size, output_size, output_ratio, return_indices) | 三维分数最大池化，使用随机步长。 |

### 填充层（Padding Layers）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.ReflectionPad1d(padding) | 一维反射填充，沿边界反射复制。 |
| torch.nn.ReflectionPad2d(padding) | 二维反射填充，沿边界反射复制。 |
| torch.nn.ReflectionPad3d(padding) | 三维反射填充，沿边界反射复制。 |
| torch.nn.ReplicationPad1d(padding) | 一维复制填充，沿边界复制边缘值。 |
| torch.nn.ReplicationPad2d(padding) | 二维复制填充，沿边界复制边缘值。 |
| torch.nn.ReplicationPad3d(padding) | 三维复制填充，沿边界复制边缘值。 |
| torch.nn.ZeroPad1d(padding) | 一维零填充。 |
| torch.nn.ZeroPad2d(padding) | 二维零填充。 |
| torch.nn.ZeroPad3d(padding) | 三维零填充。 |
| torch.nn.ConstantPad1d(padding, value) | 一维常量填充，用指定值填充。 |
| torch.nn.ConstantPad2d(padding, value) | 二维常量填充，用指定值填充。 |
| torch.nn.ConstantPad3d(padding, value) | 三维常量填充，用指定值填充。 |
| torch.nn.CircularPad1d(padding) | 一维循环填充。 |
| torch.nn.CircularPad2d(padding) | 二维循环填充。 |
| torch.nn.CircularPad3d(padding) | 三维循环填充。 |

### 激活函数（非线性激活 - 加权求和类）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.ReLU(inplace) | ReLU 激活函数，f(x) = max(0, x)。 |
| torch.nn.ReLU6(inplace) | ReLU6 激活函数，f(x) = min(max(0, x), 6)。 |
| torch.nn.Sigmoid() | Sigmoid 激活函数，f(x) = 1 / (1 + exp(-x))。 |
| torch.nn.Tanh() | Tanh 激活函数，f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))。 |
| torch.nn.LeakyReLU(negative_slope, inplace) | LeakyReLU，允许负值有小的梯度。 |
| torch.nn.PReLU(num_parameters, init) | 参数化 ReLU，可学习的负斜率参数。 |
| torch.nn.ELU(alpha, inplace) | 指数线性单元，负值使用指数函数。 |
| torch.nn.CELU(alpha, inplace) | 连续可微指数线性单元。 |
| torch.nn.SELU(inplace) | 自归一化指数线性单元。 |
| torch.nn.GELU() | 高斯误差线性单元，Transformer 中常用。 |
| torch.nn.SiLU(inplace) | Sigmoid 线性单元（Swish），f(x) = x * sigmoid(x)。 |
| torch.nn.Mish(inplace) | Mish 激活函数，f(x) = x * tanh(softplus(x))。 |
| torch.nn.Hardtanh(min_value, max_value, inplace) | 硬双曲正切，限制输出范围。 |
| torch.nn.Hardswish(inplace) | Hard Swish，ReLU6 的平滑版本。 |
| torch.nn.Hardsigmoid(inplace) | Hard Sigmoid，分段线性近似。 |
| torch.nn.RReLU(lower, upper, inplace) | 随机 LeakyReLU，训练时随机选择负斜率。 |
| torch.nn.Softplus(beta, threshold) | Softplus，ReLU 的平滑近似。 |
| torch.nn.Softshrink(lambda) | Softshrink 激活函数。 |
| torch.nn.Hardshrink(lambda) | Hardshrink 激活函数。 |
| torch.nn.Softsign() | Softsign 激活函数，f(x) = x / (1 + |x|)。 |
| torch.nn.Tanhshrink() | Tanhshrink，f(x) = x - tanh(x)。 |
| torch.nn.LogSigmoid() | Log Sigmoid，f(x) = log(sigmoid(x))。 |
| torch.nn.Threshold(threshold, value, inplace) | 阈值激活函数。 |
| torch.nn.GLU(dim) | 门控线性单元，将输入沿指定维度分成两部分并逐元素相乘。 |

### 激活函数（非线性激活 - 其他）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Softmax(dim) | Softmax 激活函数，将数值转换为概率分布。 |
| torch.nn.Softmax2d() | 对空间维度的 Softmax，用于图像。 |
| torch.nn.LogSoftmax(dim) | Log Softmax，数值稳定版本的 Softmax。 |
| torch.nn.Softmin(dim) | Softmin，与 Softmax 相反。 |
| torch.nn.AdaptiveLogSoftmaxWithLoss(in_features, n_classes, cutoffs, div_value, head_bias) | 自适应 Log Softmax，用于大词汇量分类。 |

### 归一化层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.BatchNorm1d(num_features, eps, momentum, affine, track_running_stats) | 一维批归一化层，对小批量数据进行归一化。 |
| torch.nn.BatchNorm2d(num_features, eps, momentum, affine, track_running_stats) | 二维批归一化层，常用于卷积网络。 |
| torch.nn.BatchNorm3d(num_features, eps, momentum, affine, track_running_stats) | 三维批归一化层，用于视频等三维数据。 |
| torch.nn.LazyBatchNorm1d() | 延迟初始化的一维批归一化。 |
| torch.nn.LazyBatchNorm2d() | 延迟初始化的二维批归一化。 |
| torch.nn.LazyBatchNorm3d() | 延迟初始化的三维批归一化。 |
| torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine) | 层归一化，Transformer 中常用。 |
| torch.nn.GroupNorm(num_groups, num_channels, eps, affine) | 组归一化，将通道分组后归一化。 |
| torch.nn.InstanceNorm1d(num_features, eps, momentum, affine, track_running_stats) | 一维实例归一化，用于风格迁移。 |
| torch.nn.InstanceNorm2d(num_features, eps, momentum, affine, track_running_stats) | 二维实例归一化，用于风格迁移。 |
| torch.nn.InstanceNorm3d(num_features, eps, momentum, affine, track_running_stats) | 三维实例归一化，用于风格迁移。 |
| torch.nn.SyncBatchNorm(num_features, eps, momentum, affine, track_running_stats, process_group) | 同步批归一化，用于多 GPU 分布式训练。 |
| torch.nn.LocalResponseNorm(k, alpha, beta, size) | 局部响应归一化，卷积神经网络中用于横向抑制。 |
| torch.nn.RMSNorm(normalized_shape, eps, elementwise_affine) | RMS 归一化，Transformer 中常用。 |

### 循环神经网络层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.RNN(input_size, hidden_size, num_layers, nonlinearity, bias, batch_first, dropout, bidirectional) | 简单 RNN 层。 |
| torch.nn.LSTM(input_size, hidden_size, num_layers, bias, batch_first, dropout, bidirectional, proj_size) | LSTM（长短期记忆）层。 |
| torch.nn.GRU(input_size, hidden_size, num_layers, bias, batch_first, dropout, bidirectional, proj_size) | GRU（门控循环单元）层。 |
| torch.nn.RNNCell(input_size, hidden_size, bias, nonlinearity) | RNN 单元（单层）。 |
| torch.nn.LSTMCell(input_size, hidden_size, bias) | LSTM 单元（单层）。 |
| torch.nn.GRUCell(input_size, hidden_size, bias) | GRU 单元（单层）。 |

### Transformer 层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Transformer(d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout, activation, custom_encoder, custom_decoder, layer_norm_eps, normalize_before, need_src_mask, need_tgt_mask, need_memory_mask, batch_first, norm_first, bias) | 完整的 Transformer 模型。 |
| torch.nn.TransformerEncoder(encoder_layer, num_layers, norm) | Transformer 编码器。 |
| torch.nn.TransformerDecoder(decoder_layer, num_layers, norm) | Transformer 解码器。 |
| torch.nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation, layer_norm_eps, batch_first, norm_first, bias) | Transformer 编码器层。 |
| torch.nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation, layer_norm_eps, batch_first, norm_first, bias) | Transformer 解码器层。 |
| torch.nn.MultiheadAttention(embed_dim, num_heads, dropout, bias, add_bias_kv, add_zero_attn, kdim, vdim, batch_first) | 多头注意力机制。 |

### 注意力机制（Attention）

| 函数 | 描述 |
| --- | --- |
| torch.nn.functional.scaled_dot_product_attention(query, key, value, attn_mask, dropout_p, is_causal) | 缩放点积注意力，PyTorch 优化的注意力实现。 |
| torch.nn.attention.sdpa_kernel(backends) | 设置 SDP（缩放点积注意力）后端。 |

### 嵌入层（稀疏层）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Embedding(num_embeddings, embedding_dim, padding_idx, max_norm, norm_type, scale_grad_by_freq, sparse) | 嵌入层，将离散索引映射到密集向量。 |
| torch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm, norm_type, scale_grad_by_freq, mode, sparse, per_sample_weights, include_last_offset, padding_idx) | 嵌入袋，对多个嵌入进行聚合。 |

### Dropout 层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Dropout(p, inplace) | Dropout 层，随机置零输入元素。 |
| torch.nn.Dropout1d(p, inplace) | 一维 Dropout，用于一维输入。 |
| torch.nn.Dropout2d(p, inplace) | 二维 Dropout，用于二维特征图。 |
| torch.nn.Dropout3d(p, inplace) | 三维 Dropout，用于三维特征体。 |
| torch.nn.AlphaDropout(p, inplace) | Alpha Dropout，保持自归一化特性。 |
| torch.nn.FeatureAlphaDropout(p, inplace) | 特征 Alpha Dropout。 |

### 视觉层（Vision Layers）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.PixelShuffle(upscale_factor) | 像素重排列，将通道维度转换为空间维度（上采样）。 |
| torch.nn.PixelUnshuffle(downscale_factor) | 像素重排列逆操作，将空间维度转换为通道维度（下采样）。 |
| torch.nn.Upsample(size, scale_factor, mode, align_corners, recompute_scale_factor) | 上采样层。 |
| torch.nn.UpsamplingNearest2d(size, scale_factor) | 二维最近邻上采样。 |
| torch.nn.UpsamplingBilinear2d(size, scale_factor, align_corners) | 二维双线性上采样。 |
| torch.nn.ChannelShuffle(groups) | 通道混排，用于 ChannelShuffle 网络。 |

### 损失函数

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.MSELoss(size_average, reduce, reduction) | 均方误差损失（Mean Squared Error）。 |
| torch.nn.L1Loss(size_average, reduce, reduction) | L1 损失（Mean Absolute Error）。 |
| torch.nn.CrossEntropyLoss(weight, size_average, ignore_index, reduce, reduction, label_smoothing) | 交叉熵损失，用于多分类任务。 |
| torch.nn.NLLLoss(weight, size_average, ignore_index, reduce, reduction) | 负对数似然损失。 |
| torch.nn.BCELoss(weight, size_average, reduce, reduction) | 二元交叉熵损失（二分类）。 |
| torch.nn.BCEWithLogitsLoss(weight, pos_weight, size_average, reduce, reduction, label_smoothing) | 带 Sigmoid 的二元交叉熵损失，数值更稳定。 |
| torch.nn.KLDivLoss(size_average, reduce, reduction, log_target) | KL 散度损失，用于分布匹配。 |
| torch.nn.HuberLoss(delta, size_average, reduce, reduction) | Huber 损失，L1 和 L2 的组合，对异常值更鲁棒。 |
| torch.nn.SmoothL1Loss(beta, size_average, reduce, reduction) | 平滑 L1 损失（Huber 损失的变体）。 |
| torch.nn.CTCLoss(blank, reduction, zero_infinity) | 连接时序分类损失，用于语音识别等序列任务。 |
| torch.nn.PoissonNLLLoss(log_input, full, size_average, reduce, reduction) | 泊松负对数似然损失。 |
| torch.nn.GaussianNLLLoss(full, size_average, reduce, reduction) | 高斯负对数似然损失。 |
| torch.nn.MarginRankingLoss(margin, size_average, reduce, reduction) | 间隔排序损失，用于学习排序。 |
| torch.nn.HingeEmbeddingLoss(margin, size_average, reduce, reduction) | 铰链嵌入损失，用于度量学习。 |
| torch.nn.MultiLabelMarginLoss(size_average, reduce, reduction) | 多标签间隔损失。 |
| torch.nn.SoftMarginLoss(size_average, reduce, reduction) | 软间隔损失。 |
| torch.nn.MultiLabelSoftMarginLoss(weight, size_average, reduce, reduction) | 多标签软间隔损失。 |
| torch.nn.CosineEmbeddingLoss(margin, size_average, reduce, reduction) | 余弦嵌入损失，用于度量学习。 |
| torch.nn.MultiMarginLoss(p, margin, weight, size_average, reduce, reduction) | 多分类间隔损失。 |
| torch.nn.TripletMarginLoss(margin, p, eps, swap, size_average, reduce, reduction) | 三元组损失，用于度量学习和对比学习。 |
| torch.nn.TripletMarginWithDistanceLoss(distance_function, margin, swap, size_average, reduce, reduction) | 带距离函数的三元组损失。 |

### 距离函数

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.PairwiseDistance(p, eps, keepdim) | 成对距离计算。 |
| torch.nn.CosineSimilarity(dim, eps) | 余弦相似度计算。 |

### 并行层（DataParallel）

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.DataParallel(module, device_ids, output_device, dim) | 数据并行，在多个 GPU 上并行运行模型。 |
| torch.nn.parallel.DistributedDataParallel(module, device_ids, broadcast_buffers, bucket_cap_mb, find_unused_parameters, gradient_as_bucket_view, static_graph) | 分布式数据并行，用于多节点分布式训练。 |

### 实用函数（nn.functional）

| 函数 | 描述 |
| --- | --- |
| torch.nn.functional.relu(input, inplace) | 应用 ReLU 激活函数。 |
| torch.nn.functional.sigmoid(input) | 应用 Sigmoid 激活函数。 |
| torch.nn.functional.tanh(input) | 应用 Tanh 激活函数。 |
| torch.nn.functional.softmax(input, dim, dtype) | 应用 Softmax 激活函数。 |
| torch.nn.functional.log_softmax(input, dim, dtype) | 应用 Log Softmax 激活函数。 |
| torch.nn.functional.gelu(input) | 应用 GELU 激活函数。 |
| torch.nn.functional.silu(input) | 应用 SiLU（Swish）激活函数。 |
| torch.nn.functional.mish(input) | 应用 Mish 激活函数。 |
| torch.nn.functional.hardswish(input) | 应用 Hardswish 激活函数。 |
| torch.nn.functional.leaky_relu(input, negative_slope, inplace) | 应用 LeakyReLU 激活函数。 |
| torch.nn.functional.elu(input, alpha, inplace) | 应用 ELU 激活函数。 |
| torch.nn.functional.dropout(input, p, training, inplace) | 应用 Dropout。 |
| torch.nn.functional.conv1d(input, weight, bias, stride, padding, dilation, groups) | 一维卷积操作。 |
| torch.nn.functional.conv2d(input, weight, bias, stride, padding, dilation, groups) | 二维卷积操作。 |
| torch.nn.functional.conv3d(input, weight, bias, stride, padding, dilation, groups) | 三维卷积操作。 |
| torch.nn.functional.max_pool1d(input, kernel_size, stride, padding, dilation, return_indices) | 一维最大池化。 |
| torch.nn.functional.max_pool2d(input, kernel_size, stride, padding, dilation, return_indices, ceil_mode) | 二维最大池化。 |
| torch.nn.functional.avg_pool1d(input, kernel_size, stride, padding, ceil_mode, count_include_pad) | 一维平均池化。 |
| torch.nn.functional.avg_pool2d(input, kernel_size, stride, padding, ceil_mode, count_include_pad) | 二维平均池化。 |
| torch.nn.functional.linear(input, weight, bias) | 线性变换（矩阵乘法）。 |
| torch.nn.functional.cross_entropy(input, target, weight, size_average, ignore_index, reduce, reduction, label_smoothing) | 计算交叉熵损失。 |
| torch.nn.functional.mse_loss(input, target, size_average, reduce, reduction) | 计算均方误差损失。 |
| torch.nn.functional.l1_loss(input, target, size_average, reduce, reduction) | 计算 L1 损失。 |
| torch.nn.functional.binary_cross_entropy(input, target, weight, size_average, reduce, reduction) | 计算二元交叉熵损失。 |
| torch.nn.functional.nll_loss(input, target, weight, size_average, ignore_index, reduce, reduction) | 计算负对数似然损失。 |
| torch.nn.functional.huber_loss(input, target, delta, size_average, reduce, reduction) | 计算 Huber 损失。 |
| torch.nn.functional.batch_norm(input, running_mean, running_var, weight, bias, training, momentum, eps, track_running_stats) | 批归一化操作。 |
| torch.nn.functional.layer_norm(input, normalized_shape, weight, bias, eps) | 层归一化操作。 |
| torch.nn.functional.group_norm(input, num_groups, weight, bias, eps) | 组归一化操作。 |
| torch.nn.functional.interpolate(input, size, scale_factor, mode, align_corners, recompute_scale_factor) | 插值（上/下采样）。 |
| torch.nn.functional.grid_sample(input, grid, mode, padding_mode, align_corners) | 网格采样，用于图像配准和空间变换网络。 |
| torch.nn.functional.affine_grid(theta, size, align_corners) | 仿射网格生成，用于空间变换网络。 |
| torch.nn.functional.pixel_shuffle(input, upscale_factor) | 像素重排列。 |
| torch.nn.functional.pixel_unshuffle(input, downscale_factor) | 像素重排列逆操作。 |
| torch.nn.functional.pad(input, pad, mode, value) | 填充操作。 |
| torch.nn.functional.one_hot(tensor, num_classes) | 将整数转换为独热编码。 |
| torch.nn.functional.embedding(input, weight, padding_idx, max_norm, norm_type, scale_grad_by_freq, sparse) | 嵌入操作。 |
| torch.nn.functional.cosine_similarity(x1, x2, dim, eps) | 余弦相似度计算。 |
| torch.nn.functional.pairwise_distance(x1, x2, p, eps, keepdim) | 成对距离计算。 |

### 工具函数（nn.utils）

| 函数 | 描述 |
| --- | --- |
| torch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type, error_if_nonfinite) | 裁剪梯度范数（原地操作）。 |
| torch.nn.utils.clip_grad_norm(parameters, max_norm, norm_type) | 裁剪梯度范数（非原地）。 |
| torch.nn.utils.clip_grad_value_(parameters, clip_value) | 裁剪梯度值范围。 |
| torch.nn.utils.get_total_norm(parameters, norm_type) | 计算总梯度范数。 |
| torch.nn.utils.weight_norm(module, name, dim) | 对模块参数应用权重归一化。 |
| torch.nn.utils.remove_weight_norm(module, name) | 移除权重归一化。 |
| torch.nn.utils.spectral_norm(module, name, n_power_iterations, eps, bias) | 对模块参数应用谱归一化。 |
| torch.nn.utils.remove_spectral_norm(module, name) | 移除谱归一化。 |
| torch.nn.utils.fuse_conv_bn_eval(conv, bn) | 融合卷积层和批归一化层（推理模式）。 |
| torch.nn.utils.fuse_linear_bn_eval(linear, bn) | 融合线性层和批归一化层（推理模式）。 |
| torch.nn.utils.skip_init(module_class, *args, **kwargs) | 跳过参数初始化。 |
| torch.nn.utils.parameters_to_vector(parameters) | 将参数列表展平为向量。 |
| torch.nn.utils.vector_to_parameters(vector, parameters) | 将向量重塑为参数列表。 |

### 参数初始化（nn.init）

| 函数 | 描述 |
| --- | --- |
| torch.nn.init.zeros_(tensor) | 用零初始化张量。 |
| torch.nn.init.ones_(tensor) | 用一初始化张量。 |
| torch.nn.init.uniform_(tensor, a, b) | 均匀分布初始化。 |
| torch.nn.init.normal_(tensor, mean, std) | 正态分布初始化。 |
| torch.nn.init.constant_(tensor, val) | 常量值初始化。 |
| torch.nn.init.eye_(tensor) | 单位矩阵初始化（仅适用于 2D 方阵）。 |
| torch.nn.init.dirac_(tensor) | Dirac delta 初始化（保留输入通道数）。 |
| torch.nn.init.xavier_uniform_(tensor, gain) | Xavier 均匀分布初始化。 |
| torch.nn.init.xavier_normal_(tensor, gain) | Xavier 正态分布初始化。 |
| torch.nn.init.kaiming_uniform_(tensor, a, mode, nonlinearity) | Kaiming 均匀分布初始化，适合 ReLU 激活。 |
| torch.nn.init.kaiming_normal_(tensor, a, mode, nonlinearity) | Kaiming 正态分布初始化，适合 ReLU 激活。 |
| torch.nn.init.trunc_normal_(tensor, mean, std, a, b) | 截断正态分布初始化。 |
| torch.nn.init.orthogonal_(tensor, gain) | 正交初始化。 |
| torch.nn.init.sparse_(tensor, sparsity, std) | 稀疏初始化（大部分置零）。 |
| torch.nn.init.calculate_gain(nonlinearity, param) | 计算初始化增益值。 |

### RNN 工具函数

| 函数 | 描述 |
| --- | --- |
| torch.nn.utils.rnn.PackedSequence | 打包序列，用于处理变长序列。 |
| torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first, enforce_sorted) | 打包填充序列。 |
| torch.nn.utils.rnn.pad_packed_sequence(input, batch_first, padding_value, total_length) | 解包序列。 |
| torch.nn.utils.rnn.pad_sequence(sequences, batch_first, padding_value) | 填充序列到相同长度。 |
| torch.nn.utils.rnn.pack_sequence(sequences, enforce_sorted) | 直接打包序列列表。 |

### 剪枝函数（Pruning）

| 函数 | 描述 |
| --- | --- |
| torch.nn.utils.prune.random_unstructured(module, name, amount) | 随机非结构化剪枝。 |
| torch.nn.utils.prune.l1_unstructured(module, name, amount) | L1 非结构化剪枝。 |
| torch.nn.utils.prune.global_unstructured(parameters, pruning_method, amount) | 全局非结构化剪枝。 |
| torch.nn.utils.prune.remove(module, name) | 移除剪枝。 |
| torch.nn.utils.prune.is_pruned(module) | 检查模块是否已剪枝。 |

### Flatten 层

| 类/函数 | 描述 |
| --- | --- |
| torch.nn.Flatten(start_dim, end_dim) | 展平张量，将多维张量展平为二维。 |
| torch.nn.Unflatten(dim, unflattened_size) | 解展平，将一维张量重新整形为多维。 |

### 实例

## 实例

```python
import torch

import torch.nn as nn

# 定义一个简单的神经网络

class SimpleNet(nn.Module):

    def __init__(self):

        super(SimpleNet, self).__init__()

        self.fc1 = nn.Linear(10, 20)

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):

        x = self.fc1(x)

        x = self.relu(x)

        x = self.fc2(x)

        return x

# 创建模型和输入

model = SimpleNet()

input = torch.randn(5, 10)

output = model(input)

print(output)
```

## 实例：使用 CNN 进行图像分类

```python
import torch

import torch.nn as nn

class CNN(nn.Module):

    def __init__(self):

        super(CNN, self).__init__()

        # 卷积层

        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)

        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)

        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)

        # 池化层

        self.pool = nn.MaxPool2d(2, 2)

        # 批归一化

        self.bn1 = nn.BatchNorm2d(16)

        self.bn2 = nn.BatchNorm2d(32)

        self.bn3 = nn.BatchNorm2d(64)

        # 激活函数

        self.relu = nn.ReLU()

        # 全连接层

        self.fc1 = nn.Linear(64 * 4 * 4, 256)

        self.fc2 = nn.Linear(256, 10)

        # Dropout

        self.dropout = nn.Dropout(0.5)

    def forward(self, x):

        # Conv -> BN -> ReLU -> Pool

        x = self.pool(self.relu(self.bn1(self.conv1(x))))

        x = self.pool(self.relu(self.bn2(self.conv2(x))))

        x = self.pool(self.relu(self.bn3(self.conv3(x))))

        # Flatten

        x = x.view(x.size(0), -1)

        # FC -> ReLU -> Dropout -> FC

        x = self.dropout(self.relu(self.fc1(x)))

        x = self.fc2(x)

        return x

# 创建模型

model = CNN()

print(model)

# 测试前向传播

input_tensor = torch.randn(1, 3, 32, 32)

output = model(input_tensor)

print("Output shape:", output.shape)
```

## 实例：使用 LSTM 进行文本分类

```python
import torch

import torch.nn as nn

class LSTMClassifier(nn.Module):

    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers, output_dim):

        super(LSTMClassifier, self).__init__()

        # 嵌入层

        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)

        # LSTM 层

        self.lstm = nn.LSTM(

            embedding_dim,

            hidden_dim,

            num_layers=num_layers,

            batch_first=True,

            bidirectional=True,

            dropout=0.5

        )

        # 全连接层

        self.fc = nn.Linear(hidden_dim * 2, output_dim)

        # Dropout

        self.dropout = nn.Dropout(0.5)

    def forward(self, text, text_lengths):

        # 嵌入

        embedded = self.embedding(text)

        # 打包序列以处理变长输入

        packed = nn.utils.rnn.pack_padded_sequence(

            embedded, text_lengths.cpu(), batch_first=True, enforce_sorted=False

        )

        # LSTM

        packed_output, (hidden, cell) = self.lstm(packed)

        # 解包

        output, output_lengths = nn.utils.rnn.pad_packed_sequence(packed_output, batch_first=True)

        # 合并双向的最后隐藏状态

        hidden = torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1)

        # Dropout 和全连接

        hidden = self.dropout(hidden)

        output = self.fc(hidden)

        return output

# 参数

vocab_size = 10000

embedding_dim = 128

hidden_dim = 256

num_layers = 2

output_dim = 5  # 5 分类

# 创建模型

model = LSTMClassifier(vocab_size, embedding_dim, hidden_dim, num_layers, output_dim)

print(model)
```

## 实例：使用 Transformer 编码器

```python
import torch

import torch.nn as nn

class TransformerClassifier(nn.Module):

    def __init__(self, input_dim, d_model, nhead, num_layers, dim_feedforward, output_dim, dropout):

        super(TransformerClassifier, self).__init__()

        # 嵌入层

        self.embedding = nn.Linear(input_dim, d_model)

        # 位置编码

        self.positional_encoding = nn.Parameter(torch.randn(1, 1000, d_model) * 0.1)

        # Transformer 编码器层

        encoder_layer = nn.TransformerEncoderLayer(

            d_model=d_model,

            nhead=nhead,

            dim_feedforward=dim_feedforward,

            dropout=dropout,

            batch_first=True

        )

        # Transformer 编码器

        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        # 分类头

        self.fc = nn.Linear(d_model, output_dim)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        # 添加位置编码

        seq_len = x.size(1)

        x = self.embedding(x) + self.positional_encoding[:, :seq_len, :]

        # Transformer 编码

        x = self.transformer_encoder(x)

        # 使用第一个位置的输出进行分类（类似 CLS token）

        x = x[:, 0, :]

        x = self.dropout(x)

        x = self.fc(x)

        return x

# 参数

input_dim = 512

d_model = 512

nhead = 8

num_layers = 6

dim_feedforward = 2048

output_dim = 10

dropout = 0.1

# 创建模型

model = TransformerClassifier(input_dim, d_model, nhead, num_layers, dim_feedforward, output_dim, dropout)

print(model)

# 测试

x = torch.randn(32, 100, input_dim)  # batch_size=32, seq_len=100

output = model(x)

print("Output shape:", output.shape)  # (32, 10)
```

如果需要更详细的信息，可以参考 [PyTorch 官方文档](https://pytorch.org/docs/stable/nn.html)。

---

# Transformer 模型

-

Transformer 模型是一种基于注意力机制的深度学习模型，最初由 Vaswani 等人在 2017 年的论文《Attention is All You Need》中提出。

Transformer 彻底改变了自然语言处理（NLP）领域，并逐渐扩展到计算机视觉（CV）等领域。

Transformer 的核心思想是完全摒弃传统的循环神经网络（RNN）结构，仅依赖注意力机制来处理序列数据，从而实现更高的并行性和更快的训练速度。

以下是 Transformer 架构图，左边为编码器，右边为解码器。

Transformer 模型由 编码器（Encoder） 和 解码器（Decoder） 两部分组成，每部分都由多层堆叠的相同模块构成。

### 编码器（Encoder）

编码器由 NN 层相同的模块堆叠而成，每层包含两个子层：

- **多头自注意力机制（Multi-Head Self-Attention）：**计算输入序列中每个词与其他词的相关性。

-
**前馈神经网络（Feed-Forward Neural Network）：**对每个词进行独立的非线性变换。

每个子层后面都接有 残差连接（Residual Connection） 和 层归一化（Layer Normalization）。

### 解码器（Decoder）

解码器也由 NN 层相同的模块堆叠而成，每层包含三个子层：

-
**掩码多头自注意力机制（Masked Multi-Head Self-Attention）：**计算输出序列中每个词与前面词的相关性（使用掩码防止未来信息泄露）。

-
**编码器-解码器注意力机制（Encoder-Decoder Attention）：**计算输出序列与输入序列的相关性。

-
**前馈神经网络（Feed-Forward Neural Network）：**对每个词进行独立的非线性变换。

同样，每个子层后面都接有残差连接和层归一化。

在 Transformer 模型出现之前，NLP 领域的主流模型是基于 RNN 的架构，如长短期记忆网络（LSTM）和门控循环单元（GRU）。这些模型通过顺序处理输入数据来捕捉序列中的依赖关系，但存在以下问题：

-
**梯度消失问题**：长距离依赖关系难以捕捉。

-
**顺序计算的局限性**：无法充分利用现代硬件的并行计算能力，训练效率低下。

Transformer 通过引入自注意力机制解决了这些问题，允许模型同时处理整个输入序列，并动态地为序列中的每个位置分配不同的权重。

## Transformer 的核心思想

### 1. 自注意力机制（Self-Attention）

自注意力机制是 Transformer 的核心组件。

自注意力机制允许模型在处理序列时，动态地为每个位置分配不同的权重，从而捕捉序列中任意两个位置之间的依赖关系。

-
**输入表示**：输入序列中的每个词（或标记）通过词嵌入（Embedding）转换为向量表示。

-
**注意力权重计算**：通过计算查询（Query）、键（Key）和值（Value）之间的点积，得到每个词与其他词的相关性权重。

-
**加权求和**：使用注意力权重对值（Value）进行加权求和，得到每个词的上下文表示。

公式如下：

\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

其中：

- \(Q\) 是查询矩阵，\(K\) 是键矩阵，\(V\) 是值矩阵。

- \(d_k\) 是向量的维度，用于缩放点积，防止梯度爆炸。

### 多头注意力（Multi-Head Attention）

为了捕捉更丰富的特征，Transformer 使用多头注意力机制。它将输入分成多个子空间，每个子空间独立计算注意力，最后将结果拼接起来。

-
**多头注意力的优势**：允许模型关注序列中不同的部分，例如语法结构、语义关系等。

-
**并行计算**：多个注意力头可以并行计算，提高效率。

### 位置编码（Positional Encoding）

由于 Transformer 没有显式的序列信息（如 RNN 中的时间步），位置编码被用来为输入序列中的每个词添加位置信息。通常使用正弦和余弦函数生成位置编码：

\[
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
\]
\[
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
\]

其中：

\(pos\) 是词的位置，\(i\) 是维度索引。

### 编码器-解码器架构

Transformer 模型由编码器和解码器两部分组成：

-
**
编码器：**将输入序列转换为一系列隐藏表示。每个编码器层包含一个自注意力机制和一个前馈神经网络。

-
**
解码器：**

根据编码器的输出生成目标序列。每个解码器层包含两个注意力机制（自注意力和编码器-解码器注意力）和一个前馈神经网络。

### 前馈神经网络（Feed-Forward Neural Network）

每个编码器和解码器层都包含一个前馈神经网络，通常由两个全连接层组成，中间使用 ReLU 激活函数。

### 残差连接和层归一化

为了稳定训练过程，每个子层（如自注意力层和前馈神经网络）后面都会接一个残差连接和层归一化（Layer Normalization）。

## Transformer 的优势

-
**并行计算**：Transformer 可以同时处理整个输入序列，充分利用现代硬件的并行计算能力。

-
**长距离依赖**：自注意力机制能够捕捉序列中任意两个位置之间的依赖关系，解决了 RNN 的梯度消失问题。

-
**可扩展性**：Transformer 模型可以通过堆叠更多的层来提升性能，例如 BERT 和 GPT 等模型。

## Transformer 的应用

-
**自然语言处理（NLP）**：

-
机器翻译（如 Google Translate）

-
文本生成（如 GPT 系列模型）

-
文本分类、问答系统等。

-
**计算机视觉（CV）**：

-
图像分类（如 Vision Transformer）

-
目标检测、图像生成等。

-
**多模态任务**：

-
结合文本和图像的任务（如 CLIP、DALL-E）。

## PyTorch 实现 Transformer

以下是一个简单的 PyTorch 实现 Transformer 的示例：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

class TransformerModel(nn.Module):

    def __init__(self, input_dim, model_dim, num_heads, num_layers, output_dim):

        super(TransformerModel, self).__init__()

        self.embedding = nn.Embedding(input_dim, model_dim)

        self.positional_encoding = nn.Parameter(torch.zeros(1, 1000, model_dim))  # 假设序列长度最大为1000

        self.transformer = nn.Transformer(d_model=model_dim, nhead=num_heads, num_encoder_layers=num_layers)

        self.fc = nn.Linear(model_dim, output_dim)

    def forward(self, src, tgt):

        src_seq_length, tgt_seq_length = src.size(1), tgt.size(1)

        src = self.embedding(src) + self.positional_encoding[:, :src_seq_length, :]

        tgt = self.embedding(tgt) + self.positional_encoding[:, :tgt_seq_length, :]

        transformer_output = self.transformer(src, tgt)

        output = self.fc(transformer_output)

        return output

# 超参数

input_dim = 10000  # 词汇表大小

model_dim = 512    # 模型维度

num_heads = 8      # 多头注意力头数

num_layers = 6     # 编码器和解码器层数

output_dim = 10000 # 输出维度（通常与词汇表大小相同）

# 初始化模型、损失函数和优化器

model = TransformerModel(input_dim, model_dim, num_heads, num_layers, output_dim)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.001)

# 假设输入数据

src = torch.randint(0, input_dim, (10, 32))  # (序列长度, 批量大小)

tgt = torch.randint(0, input_dim, (20, 32))  # (序列长度, 批量大小)

# 前向传播

output = model(src, tgt)

# 计算损失

loss = criterion(output.view(-1, output_dim), tgt.view(-1))

# 反向传播和优化

optimizer.zero_grad()

loss.backward()

optimizer.step()

print("Loss:", loss.item())
```

---

# PyTorch 构建 Transformer 模型

Transformer 是现代机器学习中最强大的模型之一。

Transformer 模型是一种基于自注意力机制（Self-Attention） 的深度学习架构，它彻底改变了自然语言处理（NLP）领域，并成为现代深度学习模型（如 BERT、GPT 等）的基础。

Transformer 是现代 NLP 领域的核心架构，凭借其强大的长距离依赖建模能力和高效的并行计算优势，在语言翻译和文本摘要等任务中超越了传统的 长短期记忆 (LSTM) 网络。

如果你还不了解 Transformer，可以参考：[Transformer 模型介绍](/pytorch/transformer-model.html)。

## 使用 PyTorch 构建 Transformer 模型

**构建 Transformer 模型的步骤如下：**

### 1、导入必要的库和模块

导入 PyTorch 核心库、神经网络模块、优化器模块、数据处理工具，以及数学和对象复制模块，为定义模型架构、管理数据和训练过程提供支持。

```python
import torch

import torch.nn as nn

import torch.optim as optim

import torch.utils.data as data

import math

import copy
```

说明：

-
`torch`：PyTorch 的核心库，用于张量操作和自动求导。

-
`torch.nn`：PyTorch 的神经网络模块，包含各种层和损失函数。

-
`torch.optim`：优化算法模块，如 Adam、SGD 等。

-
`math`：数学函数库，用于计算平方根等。

-
`copy`：用于深度复制对象。

### 定义基本构建块：多头注意力、位置前馈网络、位置编码

**多头注意力**通过多个"注意力头"计算序列中每对位置之间的关系，能够捕捉输入序列的不同特征和模式。

MultiHeadAttention 类封装了 Transformer 模型中常用的多头注意力机制，负责将输入拆分成多个注意力头，对每个注意力头施加注意力，然后将结果组合起来，这样模型就可以在不同尺度上捕捉输入数据中的各种关系，提高模型的表达能力。

## 实例

```python
class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, num_heads):

        super(MultiHeadAttention, self).__init__()

        assert d_model % num_heads == 0, "d_model必须能被num_heads整除"

        

        self.d_model = d_model    # 模型维度（如512）

        self.num_heads = num_heads # 注意力头数（如8）

        self.d_k = d_model // num_heads # 每个头的维度（如64）

        

        # 定义线性变换层（无需偏置）

        self.W_q = nn.Linear(d_model, d_model) # 查询变换

        self.W_k = nn.Linear(d_model, d_model) # 键变换

        self.W_v = nn.Linear(d_model, d_model) # 值变换

        self.W_o = nn.Linear(d_model, d_model) # 输出变换

        

    def scaled_dot_product_attention(self, Q, K, V, mask=None):

        """

        计算缩放点积注意力

        输入形状：

            Q: (batch_size, num_heads, seq_length, d_k)

            K, V: 同Q

        输出形状： (batch_size, num_heads, seq_length, d_k)

        """

        # 计算注意力分数（Q和K的点积）

        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        

        # 应用掩码（如填充掩码或未来信息掩码）

        if mask is not None:

            attn_scores = attn_scores.masked_fill(mask == 0, -1e9)

        

        # 计算注意力权重（softmax归一化）

        attn_probs = torch.softmax(attn_scores, dim=-1)

        

        # 对值向量加权求和

        output = torch.matmul(attn_probs, V)

        return output

        

    def split_heads(self, x):

        """

        将输入张量分割为多个头

        输入形状: (batch_size, seq_length, d_model)

        输出形状: (batch_size, num_heads, seq_length, d_k)

        """

        batch_size, seq_length, d_model = x.size()

        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)

        

    def combine_heads(self, x):

        """

        将多个头的输出合并回原始形状

        输入形状: (batch_size, num_heads, seq_length, d_k)

        输出形状: (batch_size, seq_length, d_model)

        """

        batch_size, _, seq_length, d_k = x.size()

        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)

        

    def forward(self, Q, K, V, mask=None):

        """

        前向传播

        输入形状: Q/K/V: (batch_size, seq_length, d_model)

        输出形状: (batch_size, seq_length, d_model)

        """

        # 线性变换并分割多头

        Q = self.split_heads(self.W_q(Q)) # (batch, heads, seq_len, d_k)

        K = self.split_heads(self.W_k(K))

        V = self.split_heads(self.W_v(V))

        

        # 计算注意力

        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)

        

        # 合并多头并输出变换

        output = self.W_o(self.combine_heads(attn_output))

        return output
```

说明：

-
**多头注意力机制**：将输入分割成多个头，每个头独立计算注意力，最后将结果合并。

-
**缩放点积注意力**：计算查询和键的点积，缩放后使用 softmax 计算注意力权重，最后对值进行加权求和。

-
**掩码**：用于屏蔽无效位置（如填充部分）。

### 位置前馈网络（Position-wise Feed-Forward Network）

## 实例

```python
class PositionWiseFeedForward(nn.Module):

    def __init__(self, d_model, d_ff):

        super(PositionWiseFeedForward, self).__init__()

        self.fc1 = nn.Linear(d_model, d_ff)  # 第一层全连接

        self.fc2 = nn.Linear(d_ff, d_model)  # 第二层全连接

        self.relu = nn.ReLU()  # 激活函数

    def forward(self, x):

        # 前馈网络的计算

        return self.fc2(self.relu(self.fc1(x)))
```

**
前馈网络：**由两个全连接层和一个 ReLU 激活函数组成，用于进一步处理注意力机制的输出。

### 位置编码

位置编码用于注入输入序列中每个 token 的位置信息。

使用不同频率的正弦和余弦函数来生成位置编码。

## 实例

```python
class PositionalEncoding(nn.Module):

    def __init__(self, d_model, max_seq_length):

        super(PositionalEncoding, self).__init__()

        pe = torch.zeros(max_seq_length, d_model)  # 初始化位置编码矩阵

        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)

        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))

        pe[:, 0::2] = torch.sin(position * div_term)  # 偶数位置使用正弦函数

        pe[:, 1::2] = torch.cos(position * div_term)  # 奇数位置使用余弦函数

        self.register_buffer('pe', pe.unsqueeze(0))  # 注册为缓冲区

        

    def forward(self, x):

        # 将位置编码添加到输入中

        return x + self.pe[:, :x.size(1)]
```

### 构建编码器块（Encoder Layer）

**编码器层：**包含一个自注意力机制和一个前馈网络，每个子层后接残差连接和层归一化。

## 实例

```python
class EncoderLayer(nn.Module):

    def __init__(self, d_model, num_heads, d_ff, dropout):

        super(EncoderLayer, self).__init__()

        self.self_attn = MultiHeadAttention(d_model, num_heads)  # 自注意力机制

        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)  # 前馈网络

        self.norm1 = nn.LayerNorm(d_model)  # 层归一化

        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)  # Dropout

        

    def forward(self, x, mask):

        # 自注意力机制

        attn_output = self.self_attn(x, x, x, mask)

        x = self.norm1(x + self.dropout(attn_output))  # 残差连接和层归一化

        

        # 前馈网络

        ff_output = self.feed_forward(x)

        x = self.norm2(x + self.dropout(ff_output))  # 残差连接和层归一化

        return x
```

### 构建解码器模块

**解码器层：**包含一个自注意力机制、一个交叉注意力机制和一个前馈网络，每个子层后接残差连接和层归一化。

## 实例

```python
class DecoderLayer(nn.Module):

    def __init__(self, d_model, num_heads, d_ff, dropout):

        super(DecoderLayer, self).__init__()

        self.self_attn = MultiHeadAttention(d_model, num_heads)  # 自注意力机制

        self.cross_attn = MultiHeadAttention(d_model, num_heads)  # 交叉注意力机制

        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)  # 前馈网络

        self.norm1 = nn.LayerNorm(d_model)  # 层归一化

        self.norm2 = nn.LayerNorm(d_model)

        self.norm3 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)  # Dropout

        

    def forward(self, x, enc_output, src_mask, tgt_mask):

        # 自注意力机制

        attn_output = self.self_attn(x, x, x, tgt_mask)

        x = self.norm1(x + self.dropout(attn_output))  # 残差连接和层归一化

        

        # 交叉注意力机制

        attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)

        x = self.norm2(x + self.dropout(attn_output))  # 残差连接和层归一化

        

        # 前馈网络

        ff_output = self.feed_forward(x)

        x = self.norm3(x + self.dropout(ff_output))  # 残差连接和层归一化

        return x
```

### 构建完整的 Transformer 模型

## 实例

```python
class Transformer(nn.Module):

    def __init__(self, src_vocab_size, tgt_vocab_size, d_model, num_heads, num_layers, d_ff, max_seq_length, dropout):

        super(Transformer, self).__init__()

        self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)  # 编码器词嵌入

        self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)  # 解码器词嵌入

        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)  # 位置编码

        # 编码器和解码器层

        self.encoder_layers = nn.ModuleList([EncoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)])

        self.decoder_layers = nn.ModuleList([DecoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)])

        self.fc = nn.Linear(d_model, tgt_vocab_size)  # 最终的全连接层

        self.dropout = nn.Dropout(dropout)  # Dropout

    def generate_mask(self, src, tgt):

        # 源掩码：屏蔽填充符（假设填充符索引为0）

        # 形状：(batch_size, 1, 1, seq_length)

        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)

    

        # 目标掩码：屏蔽填充符和未来信息

        # 形状：(batch_size, 1, seq_length, 1)

        tgt_mask = (tgt != 0).unsqueeze(1).unsqueeze(3)

        seq_length = tgt.size(1)

        # 生成上三角矩阵掩码，防止解码时看到未来信息

        nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool()

        tgt_mask = tgt_mask & nopeak_mask  # 合并填充掩码和未来信息掩码

        return src_mask, tgt_mask

    def forward(self, src, tgt):

        # 生成掩码

        src_mask, tgt_mask = self.generate_mask(src, tgt)

        

        # 编码器部分

        src_embedded = self.dropout(self.positional_encoding(self.encoder_embedding(src)))

        enc_output = src_embedded

        for enc_layer in self.encoder_layers:

            enc_output = enc_layer(enc_output, src_mask)

        

        # 解码器部分

        tgt_embedded = self.dropout(self.positional_encoding(self.decoder_embedding(tgt)))

        dec_output = tgt_embedded

        for dec_layer in self.decoder_layers:

            dec_output = dec_layer(dec_output, enc_output, src_mask, tgt_mask)

        

        # 最终输出

        output = self.fc(dec_output)

        return output
```

说明：

-
**Transformer 模型**：包含编码器和解码器部分，每个部分由多个层堆叠而成。

-
**掩码生成**：用于屏蔽无效位置和未来信息。

-
**前向传播**：依次通过编码器和解码器，最后通过全连接层输出。

模型初始化参数说明：

```python
class Transformer(nn.Module):

def __init__(

self, 

src_vocab_size,  # 源语言词汇表大小（如英文单词数）

tgt_vocab_size,  # 目标语言词汇表大小（如中文单词数）

d_model=512,     # 模型维度（每个词向量的长度）

num_heads=8,     # 多头注意力的头数

num_layers=6,    # 编码器/解码器的堆叠层数

d_ff=2048,       # 前馈网络隐藏层维度

max_seq_length=100, # 最大序列长度（用于位置编码）

dropout=0.1      # Dropout概率

):
```

### 训练 PyTorch Transformer 模型

使用随机数据训练模型，计算损失并更新参数。

## 实例

```python
# 超参数

src_vocab_size = 5000  # 源词汇表大小

tgt_vocab_size = 5000  # 目标词汇表大小

d_model = 512  # 模型维度

num_heads = 8  # 注意力头数量

num_layers = 6  # 编码器和解码器层数

d_ff = 2048  # 前馈网络内层维度

max_seq_length = 100  # 最大序列长度

dropout = 0.1  # Dropout 概率

# 初始化模型

transformer = Transformer(src_vocab_size, tgt_vocab_size, d_model, num_heads, num_layers, d_ff, max_seq_length, dropout)

# 生成随机数据

src_data = torch.randint(1, src_vocab_size, (64, max_seq_length))  # 源序列

tgt_data = torch.randint(1, tgt_vocab_size, (64, max_seq_length))  # 目标序列

# 定义损失函数和优化器

criterion = nn.CrossEntropyLoss(ignore_index=0)  # 忽略填充部分的损失

optimizer = optim.Adam(transformer.parameters(), lr=0.0001, betas=(0.9, 0.98), eps=1e-9)

# 训练循环

transformer.train()

for epoch in range(100):

    optimizer.zero_grad()  # 清空梯度，防止累积

    

    # 输入目标序列时去掉最后一个词（用于预测下一个词）

    output = transformer(src_data, tgt_data[:, :-1])  

    

    # 计算损失时，目标序列从第二个词开始（即预测下一个词）

    # output形状: (batch_size, seq_length-1, tgt_vocab_size)

    # 目标形状: (batch_size, seq_length-1)

    loss = criterion(

        output.contiguous().view(-1, tgt_vocab_size), 

        tgt_data[:, 1:].contiguous().view(-1)

    )

    

    loss.backward()        # 反向传播

    optimizer.step()       # 更新参数

    print(f"Epoch: {epoch+1}, Loss: {loss.item()}")
```

### 模型评估

**评估过程：**在验证数据上计算损失，评估模型性能。

## 实例

```python
transformer.eval()

# 生成验证数据

val_src_data = torch.randint(1, src_vocab_size, (64, max_seq_length))

val_tgt_data = torch.randint(1, tgt_vocab_size, (64, max_seq_length))

# 假设输入为一批英文和对应的中文翻译（已转换为索引）

# 示例数据：

# src_data: [[3, 14, 25, ..., 0, 0], ...]  # 英文句子（0为填充符）

# tgt_data: [[5, 20, 36, ..., 0, 0], ...]  # 中文翻译（0为填充符）

# 注意：实际应用中需对文本进行分词、编码、填充等预处理

with torch.no_grad():

    val_output = transformer(val_src_data, val_tgt_data[:, :-1])

    val_loss = criterion(val_output.contiguous().view(-1, tgt_vocab_size), val_tgt_data[:, 1:].contiguous().view(-1))

    print(f"Validation Loss: {val_loss.item()}")
```

---

# PyTorch torch.optim 优化器模块

优化器是深度学习中的核心组件，负责根据损失函数的梯度调整模型参数，使模型能够逐步逼近最优解。

在 PyTorch 中，torch.optim 模块提供了多种优化算法的实现，是训练神经网络不可或缺的工具。

## 为什么需要优化器

优化器在深度学习中扮演着至关重要的角色，它解决了手动更新参数的繁琐问题。

- **自动化参数更新**：手动计算和更新每个参数非常繁琐，优化器自动完成这一工作

- **加速收敛**：使用优化算法比普通梯度下降更快找到最优解

- **避免局部最优**：某些优化器具有跳出局部最优的能力

## 常见优化器类型

不同优化器适用于不同场景，选择合适的优化器可以显著提升训练效果。

| 优化器名称 | 主要特点 | 适用场景 |
| --- | --- | --- |
| SGD | 简单基础，可带动量 | 基础教学、简单模型、CNN |
| Adam | 自适应学习率 | 大多数深度学习任务 |
| AdamW | Adam + 权重衰减分离 | 需要 L2 正则化的任务 |
| RMSprop | 自适应学习率 | RNN 网络、语音识别 |
| Adagrad | 参数独立学习率 | 稀疏数据、文本处理 |
| Adadelta | 自适应学习率 | 长期训练任务 |

## 优化器核心 API

掌握优化器的基本使用流程是深度学习的第一步。

### 基本使用流程

优化器的使用遵循固定模式：创建实例 → 清空梯度 → 反向传播 → 更新参数。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

# 1. 定义一个简单的模型

class SimpleNet(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc = nn.Linear(784, 10)

    def forward(self, x):

        return self.fc(x)

model = SimpleNet()

# 2. 创建优化器实例

optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. 训练循环

for epoch in range(epochs):

    # 前向传播

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    # 反向传播

    optimizer.zero_grad()  # 清空梯度缓存，避免梯度累积

    loss.backward()        # 计算梯度

    # 参数更新

    optimizer.step()       # 更新参数
```

### 关键方法说明

优化器提供了几个核心方法来管理参数更新过程。

- **zero_grad(set_to_none=True)**：清空参数的梯度缓存。设置为 True 时会将梯度设为 None，比设为 0 更节省显存

- **step()**：执行单次参数更新，根据梯度和学习率更新模型参数

- **state_dict()**：获取优化器状态字典，可用于保存检查点

- **load_state_dict(state_dict)**：加载优化器状态，用于恢复训练

- **add_param_group(param_group)**：动态添加参数组

注意：必须在每次反向传播前调用 zero_grad()，否则梯度会累积，导致训练不稳定。建议使用 zero_grad(set_to_none=True) 以节省显存。

### 保存和加载优化器状态

在恢复训练时，需要同时保存模型和优化器的状态。

## 实例

```python
# 保存检查点（同时保存模型、优化器和调度器）

checkpoint = {

    'epoch': epoch,

    'model_state_dict': model.state_dict(),

    'optimizer_state_dict': optimizer.state_dict(),

    'scheduler_state_dict': scheduler.state_dict(),

    'loss': loss,

}

torch.save(checkpoint, 'checkpoint.pth')

# 加载检查点

checkpoint = torch.load('checkpoint.pth')

model.load_state_dict(checkpoint['model_state_dict'])

optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

scheduler.load_state_dict(checkpoint['scheduler_state_dict'])

start_epoch = checkpoint['epoch'] + 1
```

## 常用优化器详解

### SGD（随机梯度下降）

SGD 是最基础的优化算法，通过计算单个样本或小批量样本的梯度来更新参数。它是深度学习优化的基石，很多高级优化器都是在 SGD 基础上发展而来。

## 实例

```python
# SGD 优化器参数说明

# params: 要优化的参数（通常来自 model.parameters()）

# lr: 学习率，控制参数更新的步长，默认 0.01

# momentum: 动量因子，用于加速收敛和减少震荡，默认 0

# weight_decay: L2 正则化系数，用于防止过拟合，默认 0

# dampening: 动量阻尼，控制动量项的计算，默认 0

# nesterov: 是否使用 Nesterov 动量，默认 False

optimizer = optim.SGD(

    params=model.parameters(),

    lr=0.01,           # 学习率

    momentum=0.9,      # 动量因子

    weight_decay=1e-4, # L2 正则化

    nesterov=True      # 启用 Nesterov 动量

)
```

**核心参数说明：**

- lr (float)：学习率，控制参数更新的步长大小

- momentum (float)：动量因子，用于加速收敛和减少震荡，常用值 0.9

- weight_decay (float)：L2 正则化系数，用于防止过拟合，常用值 1e-4

- nesterov (bool)：是否使用 Nesterov 动量，启用后可减少震荡

**特点：**

- 实现简单，是深度学习优化的基础算法

- 添加动量项可以加速收敛，提高训练稳定性

- 收敛速度较慢，但最终精度可能更高

- 适合作为基准与其他优化器比较

SGD 虽然简单，但在合适的超参数下往往能达到很好的效果，是学习优化算法的良好起点。在图像分类任务中，SGD 配合动量仍是主流选择。

### Adam（自适应矩估计）

Adam 是目前最常用的优化器之一，结合了动量和自适应学习率的优点。它通过计算梯度的一阶和二阶矩估计来自适应调整每个参数的学习率。

## 实例

```python
# Adam 优化器参数说明

# params: 要优化的参数

# lr: 学习率，默认 0.001（推荐值）

# betas: 用于计算梯度和梯度平方的移动平均系数 (beta1, beta2)

#         beta1 控制一阶矩估计（动量），默认 0.9

#         beta2 控制二阶矩估计（方差），默认 0.999

# eps: 数值稳定项，防止除零错误，默认 1e-8

# weight_decay: L2 正则化系数，默认 0

# amsgrad: 是否使用 AMSGrad 变体，默认 False

optimizer = optim.Adam(

    params=model.parameters(),

    lr=0.001,                      # 推荐使用较小的学习率

    betas=(0.9, 0.999),            # 常用的动量参数

    eps=1e-8,                      # 数值稳定项

    weight_decay=1e-4,             # L2 正则化

    amsgrad=False                  # 是否使用 AMSGrad

)
```

**核心参数说明：**

- betas (Tuple[float, float])：控制梯度和梯度平方的指数移动平均

- eps (float)：数值稳定项，防止分母为零

- amsgrad (bool)：是否使用 AMSGrad 变体，使用后可保证收敛性

**特点：**

- 自适应学习率：根据参数的历史梯度自动调整学习率

- 结合动量概念：利用一阶矩估计加速收敛

- 鲁棒性强：对超参数选择相对不敏感

- 收敛速度快，适合快速原型开发

Adam 是大多数深度学习任务的默认选择，但在某些特定场景（如 GAN、强化学习）下可能需要尝试其他优化器。

### AdamW（Adam with Weight Decay）

AdamW 是 Adam 的改进版，将权重衰减与梯度更新解耦，理论上更利于收敛。在实际应用中，AdamW 通常比 Adam 效果更好。

## 实例

```python
# AdamW 优化器

# 与 Adam 的主要区别：weight_decay 的实现方式不同

# AdamW 的权重衰减更正确，不会影响梯度的计算

optimizer = optim.AdamW(

    params=model.parameters(),

    lr=0.001,

    betas=(0.9, 0.999),

    weight_decay=0.01,    # 权重衰减系数，通常比 Adam 设置更大

    amsgrad=False

)

# 推荐的配置：AdamW 通常使用 0.01 的 weight_decay

# 而 Adam 通常使用 0.001
```

如果你的任务需要使用权重衰减（L2 正则化），强烈推荐使用 AdamW 而不是 Adam。

### RMSprop

RMSprop 是一种自适应学习率优化器，特别适合处理非平稳目标和循环神经网络。

## 实例

```python
# RMSprop 优化器

# 通过除以梯度的指数加权平均来归一化学习率

optimizer = optim.RMSprop(

    params=model.parameters(),

    lr=0.01,               # 学习率

    alpha=0.99,            # 平方梯度的指数衰减率

    eps=1e-8,              # 数值稳定项

    weight_decay=0,        # L2 正则化

    momentum=0,            # 动量因子

    centered=False         # 是否对梯度进行中心化

)
```

### Adagrad

Adagrad 适合处理稀疏数据，它会为每个参数自适应调整学习率。

## 实例

```python
# Adagrad 优化器

# 适合稀疏数据的优化，会对频繁更新的参数使用较小的学习率

optimizer = optim.Adagrad(

    params=model.parameters(),

    lr=0.01,               # 学习率

    lr_decay=0,            # 学习率衰减

    weight_decay=0,       # L2 正则化

    initial_accumulator_value=0  # 初始累积值

)
```

## 优化器高级技巧

### 学习率调度

学习率调度允许在训练过程中动态调整学习率，通常可以显著提升模型收敛效果。

## 实例：多种学习率调度器

```python
from torch.optim.lr_scheduler import (

    StepLR,                # 步进衰减

    MultiStepLR,           # 多里程碑衰减

    ExponentialLR,         # 指数衰减

    CosineAnnealingLR,     # 余弦退火

    ReduceLROnPlateau,     # 基于指标自动调整

)

# 方式一：StepLR - 每 30 个 epoch 衰减一次

optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = StepLR(optimizer, step_size=30, gamma=0.1)

# 方式二：MultiStepLR - 在指定 epoch 衰减

optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = MultiStepLR(optimizer, milestones=[30, 60, 80], gamma=0.1)

# 方式三：CosineAnnealingLR - 余弦曲线退火

optimizer = optim.Adam(model.parameters(), lr=0.001)

scheduler = CosineAnnealingLR(optimizer, T_max=50, eta_min=1e-6)

# 方式四：ReduceLROnPlateau - 监控指标自动调整

optimizer = optim.Adam(model.parameters(), lr=0.001)

scheduler = ReduceLROnPlateau(

    optimizer, mode='min',     # 监控 loss

    factor=0.5,                 # 衰减系数

    patience=5,                 # 等待 epoch 数

    verbose=True                # 打印信息

)

# 训练循环

for epoch in range(100):

    train_loss = train(...)

    val_loss = validate(...)

    # StepLR 等调度器

    scheduler.step()

    # ReduceLROnPlateau 需要传入监控的指标

    scheduler.step(val_loss)
```

学习率调度器需要与优化器配合使用，step() 必须在 optimizer.step() 之后调用，否则可能导致学习率更新异常。

### 参数分组优化

参数分组允许为不同层设置不同的学习率，这在迁移学习中特别有用。

## 实例

```python
# 参数分组优化示例

# 为不同层设置不同的学习率

# 通常：主干网络使用较小学习率，分类头使用较大学习率

optimizer = optim.SGD([

    {'params': model.base.parameters(), 'lr': 1e-3},      # 基础层：大学习率

    {'params': model.classifier.parameters(), 'lr': 1e-2} # 分类层：大学习率

], lr=1e-4)  # 全局默认学习率（未指定参数组时使用）

# 实际应用中更常见的写法

optimizer = optim.Adam([

    {'params': model.fc.parameters(), 'lr': 1e-3},       # 分类头

    {'params': [p for n, p in model.named_parameters()    # 主干网络

                if not n.startswith('fc')],

     'lr': 1e-5},

])
```

### 梯度裁剪

梯度裁剪可以防止梯度爆炸，提高训练稳定性。特别是在 RNN、LSTM 等深层网络中非常有用。

## 实例

```python
import torch.nn as nn

# 梯度裁剪示例

# max_norm: 梯度的最大范数，超过此值的梯度会被缩放

# norm_type: 范数类型，默认为 2（二范数）

nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# 在训练循环中的使用位置

for epoch in range(epochs):

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    loss.backward()

    # 在 loss.backward() 之后，optimizer.step() 之前裁剪梯度

    nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    optimizer.step()

# 梯度裁剪的另一种方式：按值裁剪

for param in model.parameters():

    if param.grad is not None:

        param.grad.data.clamp_(min=-1.0, max=1.0)
```

梯度裁剪是训练深度神经网络（尤其是 RNN、LSTM 等）的常用技巧，可以有效防止梯度爆炸导致的训练崩溃。

### 梯度累积

当显存不足时，可以通过梯度累积来模拟大 batch size 的训练效果。

## 实例

```python
# 梯度累积示例

# 实际 batch_size = batch_size * accumulation_steps

accumulation_steps = 4   # 累积 4 个小 batch

optimizer.zero_grad()

for i, (inputs, labels) in enumerate(train_loader):

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    # 将损失除以累积步数，实现平均

    loss = loss / accumulation_steps

    loss.backward()

    # 每累积指定步数后更新一次参数

    if (i + 1) % accumulation_steps == 0:

        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()

        optimizer.zero_grad()

# 处理剩余的梯度

if (i + 1) % accumulation_steps != 0:

    optimizer.step()

    optimizer.zero_grad()
```

## 完整训练示例

以下是一个完整的训练流程，展示了优化器的最佳实践。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.optim.lr_scheduler import CosineAnnealingLR

# 配置

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

EPOCHS = 100

BATCH_SIZE = 32

LR = 1e-3

# 创建模型并移动到设备

model = SimpleNet().to(DEVICE)

# 损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.AdamW(model.parameters(), lr=LR, weight_decay=0.01)

# 学习率调度器（余弦退火）

scheduler = CosineAnnealingLR(optimizer, T_max=EPOCHS, eta_min=1e-6)

# 训练循环

best_acc = 0.0

for epoch in range(EPOCHS):

    model.train()

    total_loss = 0.0

    correct = 0

    for inputs, labels in train_loader:

        inputs = inputs.to(DEVICE)

        labels = labels.to(DEVICE)

        # 清空梯度（推荐使用 set_to_none=True）

        optimizer.zero_grad(set_to_none=True)

        # 前向传播

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        # 反向传播

        loss.backward()

        # 梯度裁剪（防止梯度爆炸）

        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        # 更新参数

        optimizer.step()

        # 统计

        total_loss += loss.item()

        correct += (outputs.argmax(1) == labels).sum().item()

    # 更新学习率

    scheduler.step()

    # 打印训练信息

    avg_loss = total_loss / len(train_loader)

    accuracy = correct / len(train_loader.dataset)

    current_lr = scheduler.get_last_lr()[0]

    print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {avg_loss:.4f} | "

          f"Acc: {accuracy:.4f} | LR: {current_lr:.6f}")

    # 保存最佳模型

    if accuracy > best_acc:

        best_acc = accuracy

        torch.save({

            'epoch': epoch,

            'model_state_dict': model.state_dict(),

            'optimizer_state_dict': optimizer.state_dict(),

            'scheduler_state_dict': scheduler.state_dict(),

            'best_acc': best_acc,

        }, 'best_model.pth')

print(f"训练完成，最佳准确率: {best_acc:.4f}")
```

## 优化器选择指南

选择合适的优化器需要根据具体任务、数据特点和训练阶段来决定。

### 按任务选择

不同任务类型有不同的优化器推荐。

| 任务类型 | 推荐优化器 | 推荐学习率 | 备注 |
| --- | --- | --- | --- |
| 图像分类（CNN） | SGD + Momentum | 0.01 ~ 0.1 | 收敛慢但精度高 |
| 图像分类（CNN） | AdamW | 0.001 | 收敛快 |
| NLP / Transformer | AdamW | 1e-5 ~ 1e-4 | 较小学习率 |
| RNN / LSTM | RMSprop / Adam | 0.001 | 自适应学习率 |
| GAN | Adam (G) / Adam (D) | 0.0001 | 较小学习率 |
| 强化学习 | Adam / RMSprop | 0.0001 ~ 0.001 | 视具体任务 |
| 快速实验 | Adam / AdamW | 0.001 | 收敛快 |

### 性能对比

| 优化器 | 收敛速度 | 内存占用 | 超参数敏感度 | 最终精度 |
| --- | --- | --- | --- | --- |
| SGD + Momentum | 慢 | 低 | 高 | 高 |
| Adam | 快 | 中 | 低 | 中 |
| AdamW | 快 | 中 | 低 | 高 |
| RMSprop | 中 | 中 | 中 | 中 |
| Adagrad | 中 | 高 | 中 | 低 |

### 常见问题与解决

- 训练不稳定（Loss 震荡）：降低学习率，添加梯度裁剪

- 收敛太慢：使用 Adam 或 AdamW，增加学习率

- 过拟合：增加 weight_decay，使用正则化

- 显存不足：减小 batch_size，使用梯度累积

优化器的选择不是绝对的，建议从 Adam 或 AdamW 开始尝试，如果效果不佳再考虑其他优化器。对于特定任务，可能需要通过实验来确定最优选择。

如果需要更详细的信息，可以参考 [PyTorch 官方文档](https://pytorch.org/docs/stable/optim.html)。

---

# PyTorch torchvision 计算机视觉模块

torchvision 是 PyTorch 生态系统中专门用于计算机视觉任务的扩展库，它提供了以下核心功能：

- **预训练模型**：包含经典的 CNN 架构实现（如 ResNet、VGG、AlexNet 等）

- **数据集工具**：内置常用视觉数据集（如 CIFAR10、MNIST、ImageNet 等）

- **图像变换**：提供各种图像预处理和数据增强方法

- **实用工具**：包括视频处理、图像操作等辅助功能

```python
# 安装 torchvision（通常与 PyTorch 一起安装）

pip install torch torchvision
```

## 核心组件解析

### 1. torchvision.models

提供预训练的计算机视觉模型，可直接用于迁移学习：

## 实例

```python
import torchvision.models as models

# 加载预训练模型

resnet18 = models.resnet18(pretrained=True)

alexnet = models.alexnet(pretrained=True)

vgg16 = models.vgg16(pretrained=True)
```

#### 常用模型列表：

| 模型名称 | 适用场景 | 参数量 | Top-1 准确率 |
| --- | --- | --- | --- |
| ResNet | 通用图像分类 | 11M-60M | 69%-80% |
| VGG | 特征提取 | 138M | 71.3% |
| MobileNet | 移动端应用 | 3.4M | 70.6% |
| EfficientNet | 高效模型 | 5M-66M | 77%-84% |

### 2. torchvision.datasets

内置常用计算机视觉数据集，简化数据加载流程：

## 实例

```python
from torchvision import datasets

# 加载 CIFAR10 数据集

train_data = datasets.CIFAR10(

    root='data', 

    train=True,

    download=True,

    transform=transforms.ToTensor()

)

# 加载 MNIST 数据集

test_data = datasets.MNIST(

    root='data',

    train=False,

    download=True

)
```

#### 支持的数据集类型：

## 实例

```python
graph TD

    A[torchvision.datasets] --> B[分类数据集]

    A --> C[检测数据集]

    A --> D[分割数据集]

    B --> B1[CIFAR10/100]

    B --> B2[MNIST/FashionMNIST]

    B --> B3[ImageNet]

    C --> C1[COCO]

    C --> C2[VOC]

    D --> D1[Cityscapes]
```

### 3. torchvision.transforms

图像预处理和数据增强的核心工具：

## 实例

```python
from torchvision import transforms

# 定义图像变换管道

transform = transforms.Compose([

    transforms.Resize(256),          # 调整大小

    transforms.CenterCrop(224),       # 中心裁剪

    transforms.ToTensor(),           # 转为张量

    transforms.Normalize(             # 标准化

        mean=[0.485, 0.456, 0.406],

        std=[0.229, 0.224, 0.225]

    )

])
```

#### 常用变换方法分类：

| 类别 | 方法示例 | 作用 |
| --- | --- | --- |
| 几何变换 | RandomRotation, RandomResizedCrop | 增加位置不变性 |
| 颜色变换 | ColorJitter, Grayscale | 增强颜色鲁棒性 |
| 模糊/噪声 | GaussianBlur, RandomErasing | 防止过拟合 |
| 组合变换 | RandomApply, RandomChoice | 灵活组合策略 |

## 实战示例：图像分类流程

### 1. 数据准备

## 实例

```python
import torch

from torchvision import datasets, transforms

from torch.utils.data import DataLoader

# 定义数据变换

train_transform = transforms.Compose([

    transforms.RandomHorizontalFlip(),

    transforms.RandomRotation(10),

    transforms.ToTensor(),

    transforms.Normalize((0.5,), (0.5,))

])

# 加载数据集

train_set = datasets.CIFAR10(

    root='./data', 

    train=True,

    download=True, 

    transform=train_transform

)

# 创建数据加载器

train_loader = DataLoader(

    train_set, 

    batch_size=32,

    shuffle=True

)
```

### 2. 模型训练

## 实例

```python
import torch.nn as nn

import torch.optim as optim

# 使用预训练模型

model = models.resnet18(pretrained=True)

# 修改最后一层（适应 CIFAR10 的 10 分类）

num_ftrs = model.fc.in_features

model.fc = nn.Linear(num_ftrs, 10)

# 定义损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 训练循环

for epoch in range(10):

    for images, labels in train_loader:

        outputs = model(images)

        loss = criterion(outputs, labels)

        

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()
```

## 高级功能

### 1. 自定义数据集

## 实例

```python
from torchvision.datasets import VisionDataset

class CustomDataset(VisionDataset):

    def __init__(self, root, transform=None):

        super().__init__(root, transform=transform)

        # 实现 __getitem__ 和 __len__

        

    def __getitem__(self, index):

        # 返回 (image, target) 元组

        pass

        

    def __len__(self):

        # 返回数据集大小

        pass
```

### 2. 模型导出与部署

## 实例

```python
# 导出为 ONNX 格式

dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(

    model,

    dummy_input,

    "model.onnx",

    input_names=["input"],

    output_names=["output"]

)
```

## 最佳实践建议

**1、数据增强策略**：

- 训练时使用随机变换增强数据

- 验证/测试时只使用确定性变换

**2、迁移学习技巧**：

## 实例

```python
# 冻结除最后一层外的所有参数

for param in model.parameters():

    param.requires_grad = False

model.fc.requires_grad = True
```

**3、性能优化**：

- 使用 `num_workers` 参数加速数据加载

- 对大数据集考虑使用 `Dataset` 的子集

**4、常见错误**：

- 忘记调用 `zero_grad()`

- 混淆了 `train()` 和 `eval()` 模式

- 图像张量形状不符合模型要求（应为 C×H×W）

---

# PyTorch 模型部署

模型部署是将训练好的机器学习模型投入实际应用的过程。PyTorch 提供了多种工具和方法来实现这一目标。

### 为什么需要模型部署

- **应用集成**：将AI能力整合到Web、移动端或嵌入式系统中

- **性能优化**：针对生产环境优化模型推理速度

- **资源管理**：有效利用计算资源，实现高并发服务

### 部署流程概览

## 模型准备与优化

### 模型导出格式

PyTorch 主要支持以下导出格式：

| 格式 | 特点 | 适用场景 |
| --- | --- | --- |
| TorchScript | PyTorch原生格式，保持动态图特性 | PyTorch生态内部使用 |
| ONNX | 开放标准，跨框架兼容 | 多框架协作环境 |
| Torch-TensorRT | NVIDIA优化格式 | GPU推理加速 |

### 导出为TorchScript

## 实例

```python
import torch

import torchvision

# 加载预训练模型

model = torchvision.models.resnet18(pretrained=True)

model.eval()

# 示例输入

example_input = torch.rand(1, 3, 224, 224)

# 方法1: 通过追踪(tracing)导出

traced_script = torch.jit.trace(model, example_input)

traced_script.save("resnet18_traced.pt")

# 方法2: 通过脚本(scripting)导出

scripted_model = torch.jit.script(model)

scripted_model.save("resnet18_scripted.pt")
```

**注意事项**：

- `torch.jit.trace` 更适合没有控制流的模型

- `torch.jit.script` 能处理包含条件判断等复杂逻辑的模型

- 导出前务必调用 `model.eval()`

## 部署方案选择

### 本地部署方案

#### LibTorch (C++ API)

## 实例

```python
#include <torch/script.h>

int main() {

    // 加载模型

    torch::jit::script::Module module;

    module = torch::jit::load("resnet18.pt");

    

    // 准备输入

    std::vector<torch::jit::IValue> inputs;

    inputs.push_back(torch::ones({1, 3, 224, 224}));

    

    // 执行推理

    auto output = module.forward(inputs).toTensor();

    std::cout << output.slice(/*dim=*/1, /*start=*/0, /*end=*/5) << '\n';

}
```

#### ONNX Runtime

## 实例

```python
import onnxruntime as ort

# 创建推理会话

sess = ort.InferenceSession("model.onnx")

# 准备输入

input_name = sess.get_inputs()[0].name

input_data = np.random.rand(1, 3, 224, 224).astype(np.float32)

# 执行推理

outputs = sess.run(None, {input_name: input_data})
```

### 云端部署方案

#### TorchServe (官方服务框架)

## 实例

```python
# 安装

pip install torchserve torch-model-archiver

# 打包模型

torch-model-archiver --model-name resnet18 \

                     --version 1.0 \

                     --serialized-file model.pth \

                     --extra-files index_to_name.json \

                     --handler image_classifier \

                     --export-path model_store

# 启动服务

torchserve --start --model-store model_store --models resnet18=resnet18.mar
```

#### 使用FastAPI构建REST API

## 实例

```python
from fastapi import FastAPI

from PIL import Image

import io

import torch

app = FastAPI()

model = torch.jit.load("model.pt")

@app.post("/predict")

async def predict(image: UploadFile = File(...)):

    img_data = await image.read()

    img = Image.open(io.BytesIO(img_data))

    # 预处理...

    with torch.no_grad():

        output = model(img_tensor)

    return {"prediction": output.argmax().item()}
```

## 性能优化技巧

### 量化加速

## 实例

```python
# 动态量化

quantized_model = torch.quantization.quantize_dynamic(

    model, {torch.nn.Linear}, dtype=torch.qint8)

# 静态量化

model.qconfig = torch.quantization.get_default_qconfig('fbgemm')

torch.quantization.prepare(model, inplace=True)

# 校准...

torch.quantization.convert(model, inplace=True)
```

### 使用TensorRT加速

## 实例

```python
import torch_tensorrt

# 编译优化

trt_model = torch_tensorrt.compile(model, 

    inputs=[torch_tensorrt.Input((1, 3, 224, 224))],

    enabled_precisions={torch.float32}  # 或 {torch.float16}

)

# 保存优化后模型

torch.jit.save(trt_model, "model_trt.pt")
```

## 常见问题解答

**Q1: 部署时出现版本兼容性问题怎么办？**
A: 建议使用Docker容器固定环境版本，或通过 `conda` 创建专用环境。

**Q2: 如何监控部署模型的性能？**
A: 可以集成Prometheus等监控工具，跟踪延迟、吞吐量和资源使用情况。

**Q3: 模型部署后如何实现热更新？**
A: TorchServe支持模型版本管理和A/B测试，可通过API动态切换模型版本。

---

# PyTorch 模型保存和加载

在深度学习项目中，模型保存和加载是至关重要的环节，主要原因包括：

- **训练中断恢复**：当训练过程意外中断时，可以从保存点继续训练

- **模型部署**：将训练好的模型部署到生产环境

- **模型共享**：方便团队成员之间共享模型成果

- **迁移学习**：保存预训练模型用于其他任务

- **性能评估**：保存不同训练阶段的模型进行比较

## 基本保存和加载方法

### 保存整个模型

这是最简单的方法，保存模型的架构和参数：

## 实例

```python
import torch

import torchvision.models as models

# 创建并训练一个模型

model = models.resnet18(pretrained=True)

# ... 训练代码 ...

# 保存整个模型

torch.save(model, 'model.pth')

# 加载整个模型

loaded_model = torch.load('model.pth')
```

**优点**：

- 代码简单直观

- 保存了完整的模型结构

**缺点**：

- 文件体积较大

- 对模型类的定义有依赖

### 仅保存模型参数（推荐方式）

更推荐的方式是只保存模型的状态字典(state_dict)：

## 实例

```python
# 保存模型参数

torch.save(model.state_dict(), 'model_weights.pth')

# 加载模型参数

model = models.resnet18()  # 必须先创建相同架构的模型

model.load_state_dict(torch.load('model_weights.pth'))

model.eval()  # 设置为评估模式
```

**优点**：

- 文件更小

- 更灵活，可以加载到不同架构中

- 兼容性更好

## 保存和加载训练状态

在实际项目中，我们通常还需要保存优化器状态、epoch等信息：

## 实例

```python
# 保存检查点

checkpoint = {

    'epoch': epoch,

    'model_state_dict': model.state_dict(),

    'optimizer_state_dict': optimizer.state_dict(),

    'loss': loss,

    # 可以添加其他需要保存的信息

}

torch.save(checkpoint, 'checkpoint.pth')

# 加载检查点

checkpoint = torch.load('checkpoint.pth')

model.load_state_dict(checkpoint['model_state_dict'])

optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

epoch = checkpoint['epoch']

loss = checkpoint['loss']

model.eval()  # 或者 model.train() 取决于你的需求
```

## 跨设备加载模型

### CPU/GPU兼容性处理

## 实例

```python
# 保存时指定map_location

torch.save(model.state_dict(), 'model_weights.pth')

# 加载到CPU（当模型是在GPU上训练时）

device = torch.device('cpu')

model.load_state_dict(torch.load('model_weights.pth', map_location=device))

# 加载到GPU

device = torch.device('cuda')

model.load_state_dict(torch.load('model_weights.pth', map_location=device))

model.to(device)
```

### 多GPU训练模型加载

## 实例

```python
# 保存多GPU模型

torch.save(model.module.state_dict(), 'multigpu_model.pth')

# 加载到单GPU

model = ModelClass()

model.load_state_dict(torch.load('multigpu_model.pth'))
```

## 模型转换与兼容性

### PyTorch版本兼容性

## 实例

```python
# 保存时指定_use_new_zipfile_serialization=True以获得更好的兼容性

torch.save(model.state_dict(), 'model.pth', _use_new_zipfile_serialization=True)
```

### 转换为TorchScript

## 实例

```python
# 将模型转换为TorchScript格式

scripted_model = torch.jit.script(model)

torch.jit.save(scripted_model, 'model_scripted.pt')

# 加载TorchScript模型

loaded_script = torch.jit.load('model_scripted.pt')
```

## 最佳实践与常见问题

### 最佳实践

- **命名规范**：使用有意义的文件名，如`resnet18_epoch50.pth`

- **定期保存**：每隔几个epoch保存一次检查点

- **验证加载**：保存后立即测试加载功能

- **文档记录**：记录模型架构和训练参数

- **版本控制**：将模型文件纳入版本控制系统

### 常见问题解决方案

**问题1**：Missing key(s) in state_dict
**解决**：确保模型架构完全匹配，或使用`strict=False`参数：

```python
model.load_state_dict(torch.load('model.pth'), strict=False)
```

**问题2**：CUDA out of memory
**解决**：加载时先放到CPU：

## 实例

```python
model.load_state_dict(torch.load('model.pth', map_location='cpu'))
```

**问题3**：无法加载旧版本模型
**解决**：尝试在不同PyTorch版本中加载，或转换模型格式

## 实际应用示例

### 图像分类模型保存与加载流程

### 完整代码示例

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

# 定义一个简单模型

class SimpleModel(nn.Module):

    def __init__(self):

        super(SimpleModel, self).__init__()

        self.fc = nn.Linear(10, 2)

    

    def forward(self, x):

        return self.fc(x)

# 初始化

model = SimpleModel()

optimizer = optim.SGD(model.parameters(), lr=0.01)

criterion = nn.CrossEntropyLoss()

# 模拟训练过程

for epoch in range(5):

    # 模拟训练步骤

    inputs = torch.randn(32, 10)

    labels = torch.randint(0, 2, (32,))

    

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()

    

    # 每2个epoch保存一次检查点

    if epoch % 2 == 0:

        checkpoint = {

            'epoch': epoch,

            'model_state_dict': model.state_dict(),

            'optimizer_state_dict': optimizer.state_dict(),

            'loss': loss.item(),

        }

        torch.save(checkpoint, f'checkpoint_epoch{epoch}.pth')

        print(f'Checkpoint saved at epoch {epoch}')

# 最终保存

torch.save(model.state_dict(), 'final_model.pth')

# 加载示例

loaded_model = SimpleModel()

loaded_model.load_state_dict(torch.load('final_model.pth'))

loaded_model.eval()

# 测试加载的模型

test_input = torch.randn(1, 10)

with torch.no_grad():

    output = loaded_model(test_input)

print(f'Test output: {output}')
```

---

# PyTorch 实例 - 图像分类项目

图像分类是计算机视觉中最基础的任务之一，其目标是让计算机能够识别图像中的主要内容并将其归类到预定义的类别中。例如，识别一张图片中是猫还是狗。

### 深度学习在图像分类中的应用

深度学习模型，特别是卷积神经网络(CNN)，已成为图像分类任务的主流解决方案。PyTorch作为深度学习框架，提供了构建和训练CNN模型的完整工具链。

### 项目流程概述

一个完整的图像分类项目通常包含以下步骤：

- 数据准备与预处理

- 模型构建

- 模型训练

- 模型评估

- 模型应用

## 环境准备与数据加载

### 安装必要的库

```python
# 安装PyTorch和torchvision

!pip install torch torchvision
```

### 加载常用数据集

PyTorch的torchvision提供了多个常用数据集，如CIFAR-10、MNIST等。

## 实例

```python
import torch

import torchvision

import torchvision.transforms as transforms

# 定义数据转换

transform = transforms.Compose([

    transforms.ToTensor(),  # 将PIL图像转换为Tensor

    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # 归一化

])

# 加载CIFAR-10训练集

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,

                                       download=True, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,

                                         shuffle=True, num_workers=2)

# 加载CIFAR-10测试集

testset = torchvision.datasets.CIFAR10(root='./data', train=False,

                                      download=True, transform=transform)

testloader = torch.utils.data.DataLoader(testset, batch_size=4,

                                        shuffle=False, num_workers=2)

# 定义类别名称

classes = ('plane', 'car', 'bird', 'cat', 'deer', 

           'dog', 'frog', 'horse', 'ship', 'truck')
```

## 构建卷积神经网络模型

### 基本CNN结构

一个典型的CNN包含卷积层、池化层和全连接层。

## 实例

```python
import torch.nn as nn

import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):

        super(Net, self).__init__()

        # 卷积层1：输入3通道(RGB)，输出6通道，5x5卷积核

        self.conv1 = nn.Conv2d(3, 6, 5)

        # 池化层：2x2窗口，步长2

        self.pool = nn.MaxPool2d(2, 2)

        # 卷积层2：输入6通道，输出16通道，5x5卷积核

        self.conv2 = nn.Conv2d(6, 16, 5)

        # 全连接层1：输入16*5*5，输出120

        self.fc1 = nn.Linear(16 * 5 * 5, 120)

        # 全连接层2：输入120，输出84

        self.fc2 = nn.Linear(120, 84)

        # 全连接层3：输入84，输出10(对应10个类别)

        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):

        # 第一层卷积+ReLU+池化

        x = self.pool(F.relu(self.conv1(x)))

        # 第二层卷积+ReLU+池化

        x = self.pool(F.relu(self.conv2(x)))

        # 展平特征图

        x = x.view(-1, 16 * 5 * 5)

        # 全连接层+ReLU

        x = F.relu(self.fc1(x))

        x = F.relu(self.fc2(x))

        # 输出层

        x = self.fc3(x)

        return x

# 实例化网络

net = Net()
```

### 模型结构可视化

## 训练模型

### 定义损失函数和优化器

## 实例

```python
import torch.optim as optim

# 交叉熵损失函数

criterion = nn.CrossEntropyLoss()

# 随机梯度下降优化器

optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
```

### 训练循环

## 实例

```python
for epoch in range(10):  # 训练10个epoch

    running_loss = 0.0

    for i, data in enumerate(trainloader, 0):

        # 获取输入数据

        inputs, labels = data

        

        # 梯度清零

        optimizer.zero_grad()

        

        # 前向传播

        outputs = net(inputs)

        # 计算损失

        loss = criterion(outputs, labels)

        # 反向传播

        loss.backward()

        # 更新权重

        optimizer.step()

        

        # 打印统计信息

        running_loss += loss.item()

        if i % 2000 == 1999:  # 每2000个mini-batch打印一次

            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')

            running_loss = 0.0

print('Finished Training')
```

## 模型评估

### 测试集准确率计算

## 实例

```python
correct = 0

total = 0

with torch.no_grad():  # 不计算梯度

    for data in testloader:

        images, labels = data

        outputs = net(images)

        _, predicted = torch.max(outputs.data, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

print(f'Accuracy on test images: {100 * correct / total:.2f}%')
```

### 各类别准确率分析

## 实例

```python
class_correct = list(0. for i in range(10))

class_total = list(0. for i in range(10))

with torch.no_grad():

    for data in testloader:

        images, labels = data

        outputs = net(images)

        _, predicted = torch.max(outputs, 1)

        c = (predicted == labels).squeeze()

        for i in range(4):

            label = labels[i]

            class_correct[label] += c[i].item()

            class_total[label] += 1

for i in range(10):

    print(f'Accuracy of {classes[i]:5s}: {100 * class_correct[i] / class_total[i]:.2f}%')
```

## 模型保存与加载

### 保存训练好的模型

## 实例

```python
# 保存模型参数

PATH = './cifar_net.pth'

torch.save(net.state_dict(), PATH)
```

### 加载模型进行预测

## 实例

```python
# 加载模型

net = Net()

net.load_state_dict(torch.load(PATH))

# 使用模型进行预测

outputs = net(images)

_, predicted = torch.max(outputs, 1)

print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}' for j in range(4)))
```

---

# PyTorch 实例 - 文本情感分析项目

文本情感分析是自然语言处理(NLP)中的一项基础任务，旨在判断一段文本表达的情感倾向(正面/负面)。本项目将使用PyTorch构建一个深度学习模型，实现对电影评论的情感分类。

### 情感分析的应用场景

- 产品评论分析

- 社交媒体舆情监控

- 客户服务反馈分类

- 市场趋势预测

## 环境准备

### 所需工具和库

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torchtext.data import Field, TabularDataset, BucketIterator

import spacy

import numpy as np
```

### 安装依赖

```python
pip install torch torchtext spacy

python -m spacy download en_core_web_sm
```

## 数据准备

### 数据集介绍

使用IMDB电影评论数据集，包含50,000条带有情感标签(正面/负面)的评论。

### 数据预处理

## 实例

```python
# 定义字段处理

TEXT = Field(tokenize='spacy', 

            tokenizer_language='en_core_web_sm',

            include_lengths=True)

LABEL = Field(sequential=False, use_vocab=False)

# 加载数据集

train_data, test_data = TabularDataset.splits(

    path='./data',

    train='train.csv',

    test='test.csv',

    format='csv',

    fields=[('text', TEXT), ('label', LABEL)]

)

# 构建词汇表

TEXT.build_vocab(train_data, 

                max_size=25000,

                vectors="glove.6B.100d")
```

## 模型构建

### LSTM模型架构

### 4.2 模型实现代码

## 实例

```python
class SentimentLSTM(nn.Module):

    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embedding_dim)

        self.lstm = nn.LSTM(embedding_dim, 

                           hidden_dim, 

                           num_layers=n_layers,

                           bidirectional=True)

        self.fc = nn.Linear(hidden_dim * 2, output_dim)

        self.dropout = nn.Dropout(0.5)

        

    def forward(self, text, text_lengths):

        embedded = self.dropout(self.embedding(text))

        packed_embedded = nn.utils.rnn.pack_padded_sequence(

            embedded, text_lengths.to('cpu'))

        packed_output, (hidden, cell) = self.lstm(packed_embedded)

        hidden = self.dropout(torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1))

        return self.fc(hidden)
```

## 模型训练

### 训练参数设置

## 实例

```python
# 模型参数

INPUT_DIM = len(TEXT.vocab)

EMBEDDING_DIM = 100

HIDDEN_DIM = 256

OUTPUT_DIM = 1

N_LAYERS = 2

# 初始化模型

model = SentimentLSTM(INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM, N_LAYERS)

# 优化器和损失函数

optimizer = optim.Adam(model.parameters())

criterion = nn.BCEWithLogitsLoss()
```

### 训练循环

## 实例

```python
def train(model, iterator, optimizer, criterion):

    epoch_loss = 0

    epoch_acc = 0

    

    model.train()

    

    for batch in iterator:

        text, text_lengths = batch.text

        predictions = model(text, text_lengths).squeeze(1)

        loss = criterion(predictions, batch.label)

        

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        

        epoch_loss += loss.item()

        epoch_acc += accuracy(predictions, batch.label)

        

    return epoch_loss / len(iterator), epoch_acc / len(iterator)
```

## 模型评估

### 评估函数

## 实例

```python
def evaluate(model, iterator, criterion):

    epoch_loss = 0

    epoch_acc = 0

    

    model.eval()

    

    with torch.no_grad():

        for batch in iterator:

            text, text_lengths = batch.text

            predictions = model(text, text_lengths).squeeze(1)

            loss = criterion(predictions, batch.label)

            epoch_loss += loss.item()

            epoch_acc += accuracy(predictions, batch.label)

            

    return epoch_loss / len(iterator), epoch_acc / len(iterator)
```

### 准确率计算

## 实例

```python
def accuracy(preds, y):

    rounded_preds = torch.round(torch.sigmoid(preds))

    correct = (rounded_preds == y).float()

    acc = correct.sum() / len(correct)

    return acc
```

## 模型应用

### 预测新文本

## 实例

```python
def predict_sentiment(model, sentence):

    tokenized = [tok.text for tok in nlp.tokenizer(sentence)]

    indexed = [TEXT.vocab.stoi[t] for t in tokenized]

    length = [len(indexed)]

    tensor = torch.LongTensor(indexed).to(device)

    tensor = tensor.unsqueeze(1)

    length_tensor = torch.LongTensor(length)

    prediction = torch.sigmoid(model(tensor, length_tensor))

    return prediction.item()
```

### 示例预测

## 实例

```python
positive_review = "This movie was fantastic! I really enjoyed it."

negative_review = "The film was terrible and boring."

print(f"Positive review score: {predict_sentiment(model, positive_review):.4f}")

print(f"Negative review score: {predict_sentiment(model, negative_review):.4f}")
```

---

# PyTorch Autograd 自动微分

深度学习的训练本质上是一个反复求梯度、更新参数的过程。

手动推导每一层的梯度既繁琐又容易出错，PyTorch 的 Autograd（自动微分）引擎正是为了解决这个问题而生——它能够**自动计算任意计算图的梯度**，让你专注于模型设计，而不是微积分推导。

## 核心概念

### 1、什么是自动微分

自动微分（Automatic Differentiation）不是数值微分（有限差分法），也不是符号微分（代数推导），而是通过**记录计算过程、反向逐步应用链式法则**来精确计算导数。

PyTorch 的 Autograd 采用**动态计算图**（Define-by-Run）方式：每次前向传播都会实时构建一张有向无环图（DAG），记录每个操作及其输入输出；反向传播时沿图反向遍历，依次计算各节点的梯度。

### 2、requires_grad 属性

Tensor 的 `requires_grad` 属性控制是否需要为该张量追踪梯度：

## 实例

```python
import torch

# 创建一个需要追踪梯度的张量（默认 requires_grad=False）

x = torch.tensor(3.0, requires_grad=True)

print(x)              # tensor(3., requires_grad=True)

print(x.requires_grad)  # True

# 也可以在创建后修改

y = torch.tensor(2.0)

print(y.requires_grad)   # False

y.requires_grad_(True)   # 原地修改（注意末尾有下划线）

print(y.requires_grad)   # True

# 由 requires_grad=True 的张量参与运算的结果，自动继承 requires_grad=True

z = x * y

print(z.requires_grad)   # True
```

### 3、grad_fn 与计算图

每个由运算产生的张量都会记录一个 `grad_fn`，指向创建它的操作节点。这就是计算图的"骨架"：

## 实例

```python
import torch

x = torch.tensor(2.0, requires_grad=True)

y = torch.tensor(3.0, requires_grad=True)

z = x ** 2 + y * 3    # z = x² + 3y

print(z)           # tensor(13., grad_fn=<AddBackward0>)

print(z.grad_fn)   # <AddBackward0 object>

# 追踪创建 z 的操作链

print(z.grad_fn.next_functions)

# ((<PowBackward0 object>, 0), (<MulBackward0 object>, 0))

# 可以看到 z 由一个幂运算和一个乘法运算组合而来
```

## backward() 反向传播

### 1、标量输出调用 backward()

对最终的标量（损失值）调用 `.backward()`，Autograd 会自动沿计算图反向计算所有叶节点的梯度，结果存入各张量的 `.grad` 属性：

## 实例

```python
import torch

x = torch.tensor(2.0, requires_grad=True)

y = torch.tensor(3.0, requires_grad=True)

# 前向传播：z = x² + 3y

z = x ** 2 + y * 3

# 反向传播：自动计算 dz/dx 和 dz/dy

z.backward()

# 查看梯度

print(x.grad)   # tensor(4.)  ← dz/dx = 2x = 2×2 = 4

print(y.grad)   # tensor(3.)  ← dz/dy = 3

# 数学验证：

# z = x² + 3y

# dz/dx = 2x = 2×2 = 4  ✓

# dz/dy = 3             ✓
```

### 2、多次调用 backward() 的累积问题

Autograd 的梯度是**累积**的，不是覆盖。每次调用 `backward()`，梯度会加到 `.grad` 已有的值上。这在训练循环中是最容易踩的坑：

## 实例

```python
import torch

x = torch.tensor(2.0, requires_grad=True)

# 第一次反向传播

loss = x ** 2

loss.backward()

print(x.grad)    # tensor(4.)  ← dL/dx = 2x = 4

# 第二次反向传播（没有清零！）

loss = x ** 2

loss.backward()

print(x.grad)    # tensor(8.)  ← 累积了！不是 4，而是 4+4=8

# &#x2705; 正确做法：每次反向传播前先清零

x.grad.zero_()   # 原地清零（注意下划线）

loss = x ** 2

loss.backward()

print(x.grad)    # tensor(4.)  ← 正确
```

在训练神经网络时，必须在每次 `backward()` 之前调用 `optimizer.zero_grad()` 清零梯度，否则梯度会不断累积，导致参数更新错误。

### 3、非标量输出调用 backward(gradient)

如果输出是一个向量或矩阵而不是标量，`backward()` 需要传入一个与输出形状相同的 `gradient` 参数（即"上游梯度"），本质上是计算向量-雅可比积（VJP）：

## 实例

```python
import torch

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# 前向传播：y 是向量

y = x ** 2   # y = [1, 4, 9]

# 非标量必须传入 gradient 参数（形状与 y 相同）

# gradient 可以理解为"损失对 y 的梯度"

y.backward(gradient=torch.ones_like(y))   # 假设上游梯度全为 1

print(x.grad)

# tensor([2., 4., 6.])  ← dy/dx = 2x，逐元素计算

# 如果上游梯度不是全 1（例如加权）

x.grad.zero_()

y.backward(gradient=torch.tensor([1.0, 0.5, 2.0]))  # 不同权重

# 实际计算：x.grad = 2x * gradient = [2×1, 4×0.5, 6×2]

print(x.grad)

# tensor([2., 2., 12.])

# 更常见的做法：先 sum/mean 变为标量，再 backward()

x.grad.zero_()

loss = (x ** 2).sum()   # 将向量聚合为标量

loss.backward()

print(x.grad)

# tensor([2., 4., 6.])  ← 与第一种写法等价
```

## torch.no_grad() 停止梯度追踪

在模型推理（预测）阶段，不需要计算梯度。使用 `torch.no_grad()` 可以跳过计算图的构建，显著节省内存和计算：

## 实例

```python
import torch

x = torch.tensor(3.0, requires_grad=True)

# 在 no_grad 上下文中，所有运算不会被追踪梯度

with torch.no_grad():

    y = x ** 2

    print(y.requires_grad)  # False ← 不再追踪梯度

    print(y.grad_fn)        # None  ← 没有计算图节点

# 退出 no_grad 上下文后，恢复正常追踪

z = x ** 2

print(z.requires_grad)  # True

# 常见用途：模型评估时包裹整个推理过程

model = torch.nn.Linear(10, 1)

inputs = torch.randn(32, 10)

with torch.no_grad():

    outputs = model(inputs)   # 不构建计算图，速度更快，内存更省
```

### @torch.no_grad() 装饰器写法

也可以用装饰器形式，适合将整个推理函数标记为无梯度：

## 实例

```python
import torch

import torch.nn as nn

model = nn.Linear(10, 1)

@torch.no_grad()

def predict(model, x):

    """推理函数，不需要计算梯度"""

    return model(x)

x = torch.randn(5, 10)

output = predict(model, x)

print(output.requires_grad)   # False
```

## detach() 从计算图中分离

`.detach()` 返回一个与原张量共享数据、但不追踪梯度的新张量。常用于以下场景：

| 场景 | 说明 |
| --- | --- |
| 将中间结果转为 numpy 数组 | numpy 不支持带梯度的张量，必须先 detach() |
| 记录训练损失（日志） | 避免保存整个计算图，防止内存泄漏 |
| 冻结某部分网络的梯度传播 | GAN 训练、迁移学习等场景 |

## 实例

```python
import torch

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

y = x ** 2 + x * 3   # y 有 grad_fn

# detach 后的张量与 y 共享数据，但脱离计算图

y_detached = y.detach()

print(y_detached.requires_grad)  # False

print(y_detached.grad_fn)        # None

# &#x2705; 转为 numpy（带梯度的张量不能直接转）

# y.numpy()           # &#x274c; 报错：RuntimeError

y_detached.numpy()    # &#x2705; 正常

# &#x2705; 记录损失值时应 detach（避免保留计算图消耗内存）

losses = []

for i in range(3):

    loss = (x ** 2).sum()

    losses.append(loss.detach().item())  # .item() 将标量张量转为 Python float

    loss.backward()

    x.grad.zero_()

print(losses)   # [14.0, 14.0, 14.0]
```

## retain_graph 保留计算图

默认情况下，`backward()` 执行后计算图会被**自动释放**（节省内存）。如果需要对同一个计算图多次反向传播（如某些 GAN 训练），需要传入 `retain_graph=True`：

## 实例

```python
import torch

x = torch.tensor(2.0, requires_grad=True)

y = x ** 3   # y = x³

# 第一次 backward（保留计算图）

y.backward(retain_graph=True)

print(x.grad)    # tensor(12.)  ← dy/dx = 3x² = 3×4 = 12

# 第二次 backward（计算图仍然存在）

x.grad.zero_()

y.backward(retain_graph=True)

print(x.grad)    # tensor(12.)  ← 同样结果

# 最后一次不再需要保留

x.grad.zero_()

y.backward()     # 此后计算图被释放

print(x.grad)    # tensor(12.)

# 再次尝试 backward 会报错（计算图已释放）

# y.backward()   # &#x274c; RuntimeError: Trying to backward through the graph a second time
```

不必要地使用 `retain_graph=True` 会导致内存持续增长，因为计算图无法被释放。只在确实需要多次反向传播时才使用。

## 梯度在神经网络训练中的应用

以下是一个完整的使用 Autograd 手动实现梯度下降的示例，展示了 Autograd 在实际训练中的完整流程：

## 实例

```python
import torch

# 构造训练数据：y = 2x + 1 加噪声

torch.manual_seed(42)

X = torch.randn(100, 1)

y_true = 2 * X + 1 + 0.1 * torch.randn(100, 1)

# 初始化模型参数（需要追踪梯度）

w = torch.zeros(1, requires_grad=True)   # 权重

b = torch.zeros(1, requires_grad=True)   # 偏置

lr = 0.1    # 学习率

epochs = 50  # 训练轮数

for epoch in range(epochs):

    # 1. 前向传播：计算预测值

    y_pred = X * w + b

    # 2. 计算损失（均方误差）

    loss = ((y_pred - y_true) ** 2).mean()

    # 3. 反向传播：自动计算 d(loss)/dw 和 d(loss)/db

    loss.backward()

    # 4. 手动更新参数（用 no_grad 包裹，避免更新操作被追踪进计算图）

    with torch.no_grad():

        w -= lr * w.grad

        b -= lr * b.grad

    # 5. 清零梯度（下一轮 backward 前必须清零）

    w.grad.zero_()

    b.grad.zero_()

    if (epoch + 1) % 10 == 0:

        print(f"Epoch {epoch+1:3d} | Loss: {loss.item():.4f} | w={w.item():.3f}, b={b.item():.3f}")

print(f"\n训练完成：w ≈ {w.item():.3f}（真实值 2.0），b ≈ {b.item():.3f}（真实值 1.0）")
```

以上代码执行结果类似如下：

```python
Epoch  10 | Loss: 0.1064 | w=1.587, b=0.805

Epoch  20 | Loss: 0.0281 | w=1.876, b=0.949

Epoch  30 | Loss: 0.0152 | w=1.954, b=0.983

Epoch  40 | Loss: 0.0128 | w=1.978, b=0.993

Epoch  50 | Loss: 0.0122 | w=1.987, b=0.997

训练完成：w ≈ 1.987（真实值 2.0），b ≈ 0.997（真实值 1.0）
```

## 常用 API 速查表

| API | 作用 | 常见场景 |
| --- | --- | --- |
| tensor.requires_grad_(True) | 原地开启梯度追踪 | 对已创建的张量启用 Autograd |
| loss.backward() | 反向传播，计算所有叶节点梯度 | 训练循环中的每次迭代 |
| tensor.grad | 访问张量的梯度值 | 查看或手动更新参数 |
| tensor.grad.zero_() | 原地清零梯度 | 每次 backward() 之前必须清零 |
| torch.no_grad() | 上下文管理器，禁用梯度追踪 | 推理阶段、手动更新参数 |
| tensor.detach() | 返回脱离计算图的新张量 | 转 numpy、记录日志、冻结梯度 |
| tensor.item() | 将标量张量转为 Python 数值 | 打印损失值、记录指标 |
| loss.backward(retain_graph=True) | 保留计算图，允许多次反向传播 | GAN 训练等需要多次 backward 的场景 |

## 常见问题与注意事项

**1、叶节点与非叶节点的区别**

只有**叶节点**（即由用户直接创建、不是运算结果的张量）的梯度才会被保存在 `.grad` 中。中间运算产生的非叶节点默认不保留梯度（节省内存）。如果需要查看中间节点的梯度，需调用 `.retain_grad()`：

## 实例

```python
import torch

x = torch.tensor(2.0, requires_grad=True)   # 叶节点

# 中间节点（非叶节点）

y = x ** 2      # y 是中间节点

y.retain_grad() # 显式声明要保留 y 的梯度

z = y * 3       # z 是最终输出

z.backward()

print(x.grad)   # tensor(12.)  ← 叶节点，正常保存

print(y.grad)   # tensor(3.)   ← 因为 retain_grad()，所以保存了

# 没有 retain_grad() 的中间节点，.grad 为 None
```

**2、原地操作（in-place）可能破坏计算图**

对需要追踪梯度的张量执行原地操作（如 `+=`、`.add_()`）可能导致 Autograd 无法正确反向传播，应尽量避免：

## 实例

```python
import torch

x = torch.tensor([1.0, 2.0], requires_grad=True)

# 危险：对叶节点进行原地操作

# x += 1  # 可能报错：a leaf Variable that requires grad has been used in an in-place operation

# 安全：使用非原地操作

y = x + 1   # 创建新张量，不修改 x

# 在 no_grad 上下文中执行原地操作是安全的（如参数更新）

with torch.no_grad():

    x += 0.01   # 用于手动参数更新，这里是安全的
```

**3、只有浮点型张量支持梯度**

整数类型（如 `torch.int64`）的张量不支持 `requires_grad=True`，只有浮点类型（`float32`、`float64`、`float16`）才能参与自动微分。

---

# PyTorch GPU / CUDA 加速

深度学习的核心操作是大规模矩阵乘法与元素运算。CPU 的设计目标是处理复杂的串行逻辑，核心数通常为 8~64 个；而 GPU 拥有数千个简单并行核心，天然适合这类高度并行的数值计算。PyTorch 通过 NVIDIA 的 CUDA（Compute Unified Device Architecture）框架调用 GPU，可将训练速度提升数十倍乃至百倍。

## 1. CPU 与 GPU 的差异

GPU 训练速度的提升主要来自两方面：其一是并行执行大量相同计算；其二是高带宽显存使得数据搬运速度远快于 CPU 内存。

对于矩阵乘法这类运算密集型操作，加速效果尤为显著。

| 对比项 | CPU | GPU（NVIDIA） |
| --- | --- | --- |
| 核心数量 | 8~64 个大核心 | 数千个小核心（CUDA Cores） |
| 设计目标 | 低延迟串行处理 | 高吞吐并行计算 |
| 内存带宽 | ~50~100 GB/s | ~500~3000 GB/s |
| 矩阵乘法速度 | 基准 | 快 10x~100x |
| PyTorch 接口 | "cpu" | "cuda" |

如果使用 Apple Silicon（M1/M2/M3），PyTorch 通过 `mps` 后端支持 Metal GPU 加速，用法与 CUDA 几乎完全相同，只需将设备改为 `"mps"`。

## 2. 检测 CUDA 环境

使用 GPU 前，需要先确认当前环境是否安装了支持 CUDA 的 PyTorch。

同时需要检查系统上是否存在可用的 GPU 设备。

## 实例

```python
import torch

# 是否支持 CUDA

print("CUDA 可用:", torch.cuda.is_available())

# GPU 设备数量

print("GPU 数量:", torch.cuda.device_count())

# 当前默认 GPU 的索引

print("当前 GPU:", torch.cuda.current_device())

# GPU 型号名称

print("GPU 型号:", torch.cuda.get_device_name(0))

# PyTorch 版本与编译时绑定的 CUDA 版本

print("PyTorch 版本:", torch.__version__)

print("CUDA 版本:", torch.version.cuda)
```

输出示例：

```python
CUDA 可用: True

GPU 数量: 1

当前 GPU: 0

GPU 型号: NVIDIA GeForce RTX 4090

PyTorch 版本: 2.3.0+cu121

CUDA 版本: 12.1
```

### 2.1 动态选择设备（推荐写法）

在代码中硬编码 `"cuda"` 会导致没有 GPU 的机器直接报错。

## 实例

```python
import torch

# 方式一：经典写法，兼容性最好

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 方式二：PyTorch 2.0+ 推荐，自动支持 CUDA / MPS / CPU

device = (

    "cuda" if torch.cuda.is_available()

    else "mps" if torch.backends.mps.is_available()

    else "cpu"

)

print(f"使用设备: {device}")
```

## 3. 张量在设备间移动

PyTorch 中的张量默认在 CPU 上创建。

要使用 GPU 计算，需要显式将张量移动到 GPU，或直接在 GPU 上创建。

### 3.1 基本移动方法

## 实例

```python
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 创建 CPU 张量

cpu_tensor = torch.tensor([1.0, 2.0, 3.0])

print(cpu_tensor.device)   # cpu

# 方式一：.to(device) —— 推荐，通用性最好

gpu_tensor = cpu_tensor.to(device)

# 方式二：.cuda() —— 仅限 CUDA 环境

gpu_tensor = cpu_tensor.cuda()

# 方式三：创建时直接指定设备

gpu_tensor = torch.tensor([1.0, 2.0, 3.0], device=device)

gpu_tensor = torch.randn(3, 4, device=device)

# 移回 CPU（用于打印、numpy 转换、保存等操作）

back_to_cpu = gpu_tensor.cpu()

print(gpu_tensor.device)    # cuda:0

print(back_to_cpu.device)   # cpu
```

GPU 张量转 numpy 时，必须先移回 CPU，且若张量附带梯度还需先 detach：

## 实例

```python
# 普通 GPU 张量转 numpy

arr = gpu_tensor.cpu().numpy()

# 带梯度的 GPU 张量转 numpy

arr = gpu_tensor.detach().cpu().numpy()
```

### 3.2 设备一致性约束

不同设备上的张量不能直接参与同一运算。

否则会抛出 `RuntimeError`：

## 实例

```python
a = torch.randn(3).to("cuda")

b = torch.randn(3)           # 在 CPU 上

# c = a + b    # RuntimeError: Expected all tensors to be on the same device

# 正确做法：先统一设备

c = a + b.to("cuda")
```

查看张量所在设备：

## 实例

```python
x = torch.randn(3, 4).to(device)

print(x.device)           # cuda:0

print(x.is_cuda)          # True

print(x.get_device())     # 0（GPU 索引）
```

### 3.3 速度对比验证

## 实例

```python
import torch

import time

device = torch.device("cuda")

n = 5000

# CPU 矩阵乘法

a_cpu = torch.randn(n, n)

b_cpu = torch.randn(n, n)

start = time.time()

c_cpu = torch.matmul(a_cpu, b_cpu)

print(f"CPU 耗时: {time.time() - start:.3f}s")

# GPU 矩阵乘法

a_gpu = a_cpu.to(device)

b_gpu = b_cpu.to(device)

torch.cuda.synchronize()    # 确保数据已传输完毕再开始计时

start = time.time()

c_gpu = torch.matmul(a_gpu, b_gpu)

torch.cuda.synchronize()    # 等待 GPU 执行完毕再停止计时

print(f"GPU 耗时: {time.time() - start:.3f}s")
```

输出示例：

```python
CPU 耗时: 1.847s

GPU 耗时: 0.021s
```

GPU 计算是异步执行的——Python 调用返回后，GPU 上的运算可能尚未完成。计时时必须调用 `torch.cuda.synchronize()` 等待 GPU 真正结束，否则测量结果不准确。

## 4. 模型移动到 GPU

模型的所有参数（`weight`、`bias`）本质上也是张量。

这些参数同样需要移动到 GPU 才能在 GPU 上执行前向传播和反向传播。

对整个模型调用 `.to(device)` 即可，PyTorch 会自动遍历并移动所有内部参数。

## 实例

```python
import torch

import torch.nn as nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class SimpleNet(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(784, 256),

            nn.ReLU(),

            nn.Linear(256, 128),

            nn.ReLU(),

            nn.Linear(128, 10),

        )

    def forward(self, x):

        return self.net(x)

# 模型移动到 GPU，只需调用一次

model = SimpleNet().to(device)

# 验证参数是否都在 GPU 上

for name, param in model.named_parameters():

    print(f"{name}: {param.device}")

# net.0.weight: cuda:0

# net.0.bias:   cuda:0

# ...

# 输入数据也必须在相同设备上

x = torch.randn(32, 784).to(device)

output = model(x)

print(output.shape)   # torch.Size([32, 10])
```

模型在 GPU 上，但输入数据仍在 CPU 上时，前向传播会报错。务必在 DataLoader 读取每个 batch 之后，将 `inputs` 和 `labels` 都调用 `.to(device)`。

## 5. 完整训练流程

以下是一个包含数据加载、模型训练、验证评估的标准 GPU 训练模板。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.utils.data import DataLoader

from torchvision import datasets, transforms

# 1. 设备配置

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"训练设备: {device}")

# 2. 数据加载

# pin_memory=True：将数据锁定在内存，加快 CPU -> GPU 传输

# num_workers：多进程预加载，减少数据等待时间

transform = transforms.Compose([

    transforms.ToTensor(),

    transforms.Normalize((0.5,), (0.5,)),

])

train_dataset = datasets.MNIST(root="./data", train=True,

                                download=True, transform=transform)

test_dataset  = datasets.MNIST(root="./data", train=False,

                                download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True,

                          num_workers=4, pin_memory=True)

test_loader  = DataLoader(test_dataset,  batch_size=256, shuffle=False,

                          num_workers=4, pin_memory=True)

# 3. 定义模型

class CNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),

        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(64 * 7 * 7, 256), nn.ReLU(), nn.Dropout(0.5),

            nn.Linear(256, 10),

        )

    def forward(self, x):

        return self.classifier(self.features(x))

model     = CNN().to(device)     # 模型移到 GPU

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 4. 训练函数

def train_epoch(model, loader, optimizer, criterion):

    model.train()

    total_loss, correct = 0.0, 0

    for inputs, labels in loader:

        # non_blocking=True：异步传输，CPU 可以继续准备下一批数据

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss    = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item() * inputs.size(0)

        correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

# 5. 验证函数

def eval_epoch(model, loader, criterion):

    model.eval()

    total_loss, correct = 0.0, 0

    with torch.no_grad():

        for inputs, labels in loader:

            inputs = inputs.to(device, non_blocking=True)

            labels = labels.to(device, non_blocking=True)

            outputs = model(inputs)

            loss    = criterion(outputs, labels)

            total_loss += loss.item() * inputs.size(0)

            correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

# 6. 主训练循环

for epoch in range(1, 11):

    train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion)

    val_loss,   val_acc   = eval_epoch(model,  test_loader,  criterion)

    print(f"Epoch {epoch:02d} | "

          f"Train Loss: {train_loss:.4f}, Acc: {train_acc:.4f} | "

          f"Val Loss: {val_loss:.4f}, Acc: {val_acc:.4f}")
```

关键要点：

- `device` 变量在代码最顶部声明，全局统一引用，不硬编码 `"cuda"`

- 模型 `.to(device)` 只需调用一次

- 每个 batch 的 `inputs` 和 `labels` 都要 `.to(device)`

- DataLoader 设置 `pin_memory=True` 和 `non_blocking=True` 加速数据传输

- 验证阶段使用 `torch.no_grad()` 关闭梯度，节省显存

## 6. 多 GPU 训练

当单卡显存不足时，可以考虑使用多 GPU 并行训练。

此外，多 GPU 还能进一步提升训练速度。PyTorch 提供了两种主要方式。

### 6.1 DataParallel

这是最简单的多卡方式。

它采用单进程，将每个 batch 均分到各 GPU，前向传播并行执行，梯度在主卡上汇总更新。使用方便，但主卡负担重，多卡利用率不均衡，适合快速入门。

## 实例

```python
import torch

import torch.nn as nn

model = CNN()

if torch.cuda.device_count() > 1:

    print(f"使用 {torch.cuda.device_count()} 个 GPU")

    model = nn.DataParallel(model)

    # 也可以指定使用哪些 GPU

    # model = nn.DataParallel(model, device_ids=[0, 1])

model = model.to("cuda")

# 之后的训练代码与单卡完全一致

# DataParallel 会自动将 batch 均分到各 GPU，并汇总结果
```

如果需要访问原始模型的属性（如自定义方法），需要通过 `.module` 访问：

## 实例

```python
# model 被 DataParallel 包裹后，原始模型在 model.module 中

print(model.module.classifier)

# 保存模型时建议保存 model.module，方便单卡加载

torch.save(model.module.state_dict(), "model.pth")
```

### 6.2 DistributedDataParallel

这是多进程方式。

每个进程绑定一块 GPU，每张卡持有完整模型，通过 All-Reduce 同步梯度。是生产环境和大规模训练的推荐方案，效率远高于 DataParallel。

## 实例

```python
import torch

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

from torch.utils.data.distributed import DistributedSampler

def main(rank, world_size):

    # 初始化进程组，nccl 后端专为 NVIDIA GPU 优化

    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)

    # 每个进程绑定对应的 GPU

    torch.cuda.set_device(rank)

    device = torch.device(f"cuda:{rank}")

    # 模型移到对应 GPU 后包装 DDP

    model = CNN().to(device)

    model = DDP(model, device_ids=[rank])

    # DataLoader 使用 DistributedSampler，保证各卡数据不重叠

    sampler = DistributedSampler(train_dataset,

                                  num_replicas=world_size, rank=rank)

    loader  = DataLoader(train_dataset, batch_size=64,

                         sampler=sampler, pin_memory=True)

    # 训练逻辑与单卡完全一致

    # ...

    dist.destroy_process_group()

# 启动方式（推荐使用 torchrun）：

# torchrun --nproc_per_node=4 train_ddp.py
```

| 对比项 | DataParallel | DistributedDataParallel |
| --- | --- | --- |
| 进程数量 | 单进程 | 多进程（每卡一个） |
| 通信后端 | Python GIL 限制 | NCCL（高效） |
| 主卡负担 | 重（汇总梯度） | 均衡（All-Reduce） |
| 代码改动 | 极少 | 中等 |
| 适用场景 | 快速实验 | 生产训练 |

## 7. 混合精度训练 AMP

默认训练使用 float32（FP32）精度。

自动混合精度（Automatic Mixed Precision，AMP）让部分计算使用 float16（FP16）或 bfloat16（BF16），在几乎不损失精度的情况下获得显著收益：

- 显存占用减少约 50%

- 训练速度提升 2x~3x（Tensor Core 硬件加速）

- 代码改动极少，只需三处修改

## 实例

```python
from torch.cuda.amp import autocast, GradScaler

model     = CNN().to(device)

optimizer = optim.Adam(model.parameters(), lr=1e-3)

scaler    = GradScaler()    # FP16 梯度缩放器，防止梯度下溢出为零

for epoch in range(num_epochs):

    model.train()

    for inputs, labels in train_loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        # 修改一：autocast 区域内自动选择 FP16/FP32

        with autocast(device_type="cuda"):

            outputs = model(inputs)

            loss    = criterion(outputs, labels)

        # 修改二：用 scaler 缩放 loss 再反向传播

        scaler.scale(loss).backward()

        # 修改三：scaler 更新参数，内部自动处理梯度缩放

        scaler.step(optimizer)

        scaler.update()
```

### 7.1 FP16 与 BF16 的选择

| 格式 | 精度位 | 数值范围位 | 适合硬件 | 特点 |
| --- | --- | --- | --- | --- |
| float16 | 10 位 | 5 位 | RTX 20/30/40 系 | 需要 GradScaler 防溢出 |
| bfloat16 | 7 位 | 8 位 | A100 / H100 / RTX 4090 | 范围与 FP32 相同，训练更稳定 |

如果 GPU 支持 BF16，优先使用，无需 GradScaler：

## 实例

```python
# BF16 写法（PyTorch 2.0+）

with torch.autocast(device_type="cuda", dtype=torch.bfloat16):

    outputs = model(inputs)

    loss    = criterion(outputs, labels)

loss.backward()

optimizer.step()
```

## 8. 性能优化技巧

本节介绍多种优化显存和训练速度的技巧。

### 8.1 显存管理

## 实例

```python
# 查看当前显存使用情况

print(f"已分配: {torch.cuda.memory_allocated() / 1024**2:.1f} MB")

print(f"已缓存: {torch.cuda.memory_reserved()  / 1024**2:.1f} MB")

# 打印详细显存报告

print(torch.cuda.memory_summary())

# 释放缓存池（不释放已分配的显存）

torch.cuda.empty_cache()

# 推理时使用 inference_mode（比 no_grad 更快，彻底禁用梯度引擎）

with torch.inference_mode():

    output = model(x)

# 梯度检查点：以重新计算换显存（大模型训练常用）

from torch.utils.checkpoint import checkpoint

output = checkpoint(model_block, x)
```

### 8.2 DataLoader 优化

## 实例

```python
loader = DataLoader(

    dataset,

    batch_size=256,

    num_workers=4,              # 多进程预加载，建议设为 CPU 核数的 50%

    pin_memory=True,            # 锁页内存，加快 CPU -> GPU 传输

    persistent_workers=True,    # 进程常驻，避免每个 epoch 重新创建进程

    prefetch_factor=2,          # 每个 worker 预取的 batch 数量

)
```

### 8.3 torch.compile 模型编译（PyTorch 2.0+）

一行代码，对计算图进行编译优化，速度提升 30%~200%（取决于模型结构）：

## 实例

```python
# 编译模型，第一次运行时有编译开销，之后的迭代速度显著提升

model = torch.compile(model)

# 不同编译模式的权衡

model = torch.compile(model, mode="default")          # 均衡，适合大多数场景

model = torch.compile(model, mode="reduce-overhead")  # 降低调度开销

model = torch.compile(model, mode="max-autotune")     # 最大优化，编译时间较长
```

### 8.4 梯度累积（模拟大 batch）

显存不足时，可以通过梯度累积模拟更大的 batch size，而无需实际增大显存占用：

## 实例

```python
accumulation_steps = 8    # 每 8 个 batch 更新一次参数，等效 batch_size × 8

for i, (inputs, labels) in enumerate(train_loader):

    inputs = inputs.to(device)

    labels = labels.to(device)

    outputs = model(inputs)

    loss    = criterion(outputs, labels) / accumulation_steps   # 均分 loss

    loss.backward()    # 梯度累积，不清零

    if (i + 1) % accumulation_steps == 0:

        optimizer.step()

        optimizer.zero_grad()    # 只在参数更新后清零
```

### 8.5 显存不足时的应对策略

| 策略 | 方法 | 效果 |
| --- | --- | --- |
| 减小 batch size | 256 -> 64 | 线性减少显存 |
| 混合精度 | AMP + FP16/BF16 | 显存减少约 50% |
| 梯度累积 | 每 N 步更新一次 | 模拟大 batch，不增加显存 |
| 梯度检查点 | torch.utils.checkpoint | 大幅减少显存，训练速度降低 |
| 冻结部分参数 | 迁移学习冻结主干 | 减少反向传播的显存占用 |

## 9. 常见错误与排查

本节汇总了 GPU 训练中最常见的错误及其解决方案。

### 9.1 RuntimeError: Expected all tensors to be on the same device

原因：参与运算的张量分布在不同设备上（一个在 CPU，一个在 GPU）。

## 实例

```python
# 排查方式：打印各张量的 device

print(inputs.device, labels.device, next(model.parameters()).device)

# 解决：确保每个 batch 都执行了 .to(device)

inputs = inputs.to(device)

labels = labels.to(device)
```

### 9.2 RuntimeError: CUDA out of memory

原因：显存不足，常见于 batch size 过大、模型过大，或计算图意外积累。

## 实例

```python
# 常见隐患：循环中 loss 没有调用 .item()，导致计算图不断堆积

# 错误写法

total_loss += loss           # loss 是张量，持有整个计算图

# 正确写法

total_loss += loss.item()    # .item() 取出 Python 标量，释放计算图

# 其他排查步骤：

# 1. 减小 batch_size

# 2. 确认验证循环使用了 torch.no_grad()

# 3. 调用 torch.cuda.empty_cache() 清理缓存

# 4. 使用 torch.cuda.memory_summary() 定位显存占用来源
```

### 9.3 Can't call numpy() on Tensor that requires grad

原因：带梯度的张量不能直接转为 numpy 数组。

## 实例

```python
# 错误写法

arr = gpu_tensor.numpy()

# 正确写法

arr = gpu_tensor.detach().cpu().numpy()
```

### 9.4 CUDA error: device-side assert triggered

原因：通常是标签值越界（如 10 分类但 label 值等于 10），或数组索引越界。报错信息在 GPU 上产生，默认显示位置不准确。

## 实例

```python
# 设置环境变量，让错误在准确的代码行处抛出（会变为同步执行，速度变慢）

import os

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
```

### 9.5 训练速度没有提升（GPU 利用率低）

原因：数据加载成为瓶颈，GPU 大部分时间在等待 CPU 准备数据。

排查步骤：

- 运行 `nvidia-smi` 或 `watch -n 1 nvidia-smi` 观察 GPU 利用率

- 利用率持续低于 80% 说明存在数据瓶颈

- 增大 DataLoader 的 num_workers

- 开启 pin_memory=True

- 将数据预处理移到 GPU（torchvision.transforms 支持 GPU 操作）

- 将小文件数据集预先加载到内存

### 9.6 使用 PyTorch Profiler 精确定位瓶颈

## 实例

```python
from torch.profiler import profile, ProfilerActivity

with profile(

    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],

    record_shapes=True,

) as prof:

    for i, (inputs, labels) in enumerate(train_loader):

        if i >= 10:

            break

        inputs = inputs.to(device)

        labels = labels.to(device)

        loss   = criterion(model(inputs), labels)

        loss.backward()

        optimizer.step()

        optimizer.zero_grad()

# 按 CUDA 耗时排序，打印前 15 项

print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=15))
```

## 10. API 快速参考

以下是常用 PyTorch GPU 相关 API 的速查表。

### 10.1 设备管理

| 操作 | 代码 |
| --- | --- |
| 检测 CUDA 可用 | torch.cuda.is_available() |
| 选择设备 | torch.device("cuda" if ... else "cpu") |
| GPU 数量 | torch.cuda.device_count() |
| GPU 名称 | torch.cuda.get_device_name(0) |
| 设置当前 GPU | torch.cuda.set_device(0) |
| 等待 GPU 完成 | torch.cuda.synchronize() |

### 10.2 张量操作

| 操作 | 代码 |
| --- | --- |
| 张量移到 GPU | tensor.to(device) 或 tensor.cuda() |
| 张量移到 CPU | tensor.cpu() |
| 查看所在设备 | tensor.device |
| 是否在 GPU | tensor.is_cuda |
| GPU 张量转 numpy | tensor.detach().cpu().numpy() |
| 异步传输 | tensor.to(device, non_blocking=True) |

### 10.3 模型操作

| 操作 | 代码 |
| --- | --- |
| 模型移到 GPU | model.to(device) |
| 开启训练模式 | model.train() |
| 开启推理模式 | model.eval() |
| 编译加速 | torch.compile(model) |
| 关闭梯度 | with torch.no_grad(): |
| 推理模式 | with torch.inference_mode(): |

### 10.4 显存管理

| 操作 | 代码 |
| --- | --- |
| 已分配显存 | torch.cuda.memory_allocated() |
| 已缓存显存 | torch.cuda.memory_reserved() |
| 显存报告 | torch.cuda.memory_summary() |
| 清理缓存 | torch.cuda.empty_cache() |

### 10.5 核心原则速记

```python
1. 用 device 变量统一管理，不要硬编码 "cuda"

2. 模型和数据必须在同一设备上，每个 batch 都要 .to(device)

3. 验证和推理时一定使用 torch.no_grad() 或 torch.inference_mode()

4. 生产训练推荐开启 AMP 混合精度，几乎免费获得 2x 加速

5. DataLoader 设置 pin_memory=True 和 num_workers >= 4 减少数据瓶颈

6. PyTorch 2.0+ 可以用 torch.compile(model) 一行提速 30%+

7. GPU 计算是异步的，精确计时需要调用 torch.cuda.synchronize()
```

---

# PyTorch 损失函数

损失函数（Loss Function）衡量模型预测值与真实值之间的差距，是神经网络训练的核心指引——优化器通过最小化损失函数来更新模型参数。

PyTorch 在 `torch.nn` 模块中内置了十余种常用损失函数，覆盖分类、回归、排序等主要任务类型。

## 1. 损失函数基础

### 基本用法

所有 PyTorch 损失函数都是 `nn.Module` 的子类，使用方式统一：

## 实例

```python
import torch

import torch.nn as nn

# 1. 实例化损失函数

criterion = nn.CrossEntropyLoss()

# 2. 计算损失（预测值在前，真实值在后）

loss = criterion(predictions, targets)

# 3. 反向传播

loss.backward()
```

### 预测值的形态约定

不同损失函数对输入的形态要求不同，这是初学者最容易出错的地方：

| 损失函数 | 预测值（input）形态 | 标签（target）形态 |
| --- | --- | --- |
| CrossEntropyLoss | (N, C) 原始 logits | (N,) 整数类别索引 |
| BCELoss | (N,) 经过 Sigmoid 的概率 | (N,) 0/1 浮点数 |
| BCEWithLogitsLoss | (N,) 原始 logits | (N,) 0/1 浮点数 |
| MSELoss | (N,) 任意实数 | (N,) 任意实数 |
| NLLLoss | (N, C) 经过 log_softmax 的概率 | (N,) 整数类别索引 |

**N** = batch size，**C** = 类别数

## 2. 分类任务损失函数

### 2.1 CrossEntropyLoss 交叉熵损失

最常用的多分类损失函数，**内部自动执行 Softmax + 对数 + 负号**，无需手动对模型输出做 Softmax。

**数学公式：**

Loss = -sum(y_c * log(p_c))

其中 p_c = exp(x_c) / sum_j exp(x_j) 是 Softmax 输出。

## 实例

```python
import torch

import torch.nn as nn

criterion = nn.CrossEntropyLoss()

# 模型输出：原始 logits，shape (batch_size, num_classes)

# 不需要提前做 Softmax！

predictions = torch.tensor([

    [2.0, 0.5, 0.3],   # 样本1，最可能是类别 0

    [0.1, 3.0, 0.2],   # 样本2，最可能是类别 1

    [0.2, 0.1, 4.0],   # 样本3，最可能是类别 2

])

# 标签：整数类别索引，shape (batch_size,)

targets = torch.tensor([0, 1, 2])

loss = criterion(predictions, targets)

print(f"Loss: {loss.item():.4f}")  # Loss: 0.1763
```

**支持软标签（Label Smoothing）：**

## 实例

```python
# 标签平滑，缓解过拟合，常用于图像分类竞赛

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

# 也支持直接传入软标签（概率分布）

soft_targets = torch.tensor([

    [0.9, 0.05, 0.05],

    [0.05, 0.9, 0.05],

])

predictions = torch.randn(2, 3)

loss = criterion(predictions, soft_targets)
```

**适用场景：**多分类（猫/狗/鸟）、图像分类、文本分类等所有多分类任务。

### 2.2 BCELoss 二元交叉熵损失

专用于**二分类**或**多标签分类**任务，输入必须是经过 `Sigmoid` 处理后的概率值（0~1）。

**数学公式：**

Loss = -[y * log(p) + (1-y) * log(1-p)]

## 实例

```python
criterion = nn.BCELoss()

# 模型输出必须先经过 Sigmoid，取值范围 (0, 1)

raw_output = torch.tensor([2.0, -1.0, 0.5, -3.0])

predictions = torch.sigmoid(raw_output)   # [0.88, 0.27, 0.62, 0.05]

# 标签：浮点型 0.0 或 1.0

targets = torch.tensor([1.0, 0.0, 1.0, 0.0])

loss = criterion(predictions, targets)

print(f"Loss: {loss.item():.4f}")  # Loss: 0.2824

# 多标签分类（每个样本可属于多个类别）

# predictions shape: (batch_size, num_labels)

predictions_ml = torch.sigmoid(torch.randn(4, 5))

targets_ml     = torch.randint(0, 2, (4, 5)).float()

loss_ml = criterion(predictions_ml, targets_ml)
```

`BCELoss` 要求输入在 (0, 1) 范围内，传入原始 logits 会导致数值不稳定甚至 NaN。推荐使用下方的 `BCEWithLogitsLoss`。

### 2.3 BCEWithLogitsLoss

`BCELoss` 的改进版，**内部自动执行 Sigmoid**，数值更稳定，推荐优先使用。

## 实例

```python
criterion = nn.BCEWithLogitsLoss()

# 直接传入原始 logits，无需手动 Sigmoid

predictions = torch.tensor([2.0, -1.0, 0.5, -3.0])

targets     = torch.tensor([1.0,  0.0, 1.0,  0.0])

loss = criterion(predictions, targets)

print(f"Loss: {loss.item():.4f}")

# 等价于（但数值稳定性更好）：

# loss = BCELoss(Sigmoid(predictions), targets)
```

**带正样本权重（处理类别不平衡）：**

## 实例

```python
# pos_weight：正样本权重，值越大越关注正样本

# 例如负样本是正样本的 10 倍，设 pos_weight=10

pos_weight = torch.tensor([10.0])

criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
```

**适用场景：**二分类（垃圾邮件判断）、多标签分类（文章多标签打标）、目标检测（前景/背景判断）。

### 2.4 NLLLoss 负对数似然损失

需要手动对模型输出做 `log_softmax`，灵活性更高。`CrossEntropyLoss = LogSoftmax + NLLLoss`。

## 实例

```python
criterion = nn.NLLLoss()

# 必须先手动做 log_softmax

raw_output   = torch.randn(4, 3)   # (batch, num_classes)

log_probs    = torch.log_softmax(raw_output, dim=1)

targets = torch.tensor([0, 2, 1, 0])

loss = criterion(log_probs, targets)
```

**使用场景：**需要在中间步骤使用 log 概率时（如 CTC、Beam Search）；其他情况优先用 `CrossEntropyLoss`。

## 3. 回归任务损失函数

### 3.1 MSELoss 均方误差

最经典的回归损失，对**大误差非常敏感**（因为平方会放大大误差的影响）。

**数学公式：**

MSELoss = (1/N) * sum((y_i - y_hat_i)^2)

## 实例

```python
criterion = nn.MSELoss()

predictions = torch.tensor([2.5, 0.5, 2.0, 8.0])

targets     = torch.tensor([3.0, -0.5, 2.0, 7.0])

loss = criterion(predictions, targets)

print(f"MSE Loss: {loss.item():.4f}")  # MSE Loss: 0.3750

# 手动验证

manual = ((predictions - targets) ** 2).mean()

print(f"手动计算: {manual.item():.4f}")  # 0.3750
```

**适用场景：**房价预测、温度预测等连续值回归，数据中没有明显离群点时效果好。

### 3.2 L1Loss 平均绝对误差

对**离群点（outlier）更鲁棒**，因为取绝对值而非平方，大误差不会被过度放大。

**数学公式：**

L1Loss = (1/N) * sum(|y_i - y_hat_i|)

## 实例

```python
criterion = nn.L1Loss()

predictions = torch.tensor([2.5, 0.5, 2.0, 8.0])

targets     = torch.tensor([3.0, -0.5, 2.0, 7.0])

loss = criterion(predictions, targets)

print(f"L1 Loss: {loss.item():.4f}")  # L1 Loss: 0.5000
```

### 3.3 SmoothL1Loss Huber 损失

**融合 MSE 和 L1 的优点**：误差小时用 MSE（平滑，梯度稳定），误差大时用 L1（抗离群点）。目标检测（Faster R-CNN）中的标准损失。

**数学公式：**

SmoothL1(x) = 0.5*x^2 if |x|

## 4. 进阶损失函数

### 4.1 HuberLoss

`SmoothL1Loss` 的通用版，允许自定义切换阈值 `delta`（默认 1.0）。

## 实例

```python
# delta 控制 MSE 和 L1 的切换点

criterion = nn.HuberLoss(delta=1.5)

predictions = torch.randn(10)

targets     = torch.randn(10)

loss = criterion(predictions, targets)
```

### 4.2 KLDivLoss KL 散度

衡量两个概率分布的差异，常用于**知识蒸馏**和**变分自编码器（VAE）**。

**数学公式：**

KL(P || Q) = sum(P(i) * log(P(i) / Q(i)))

## 实例

```python
criterion = nn.KLDivLoss(reduction='batchmean')

# input 必须是 log 概率（对数概率），target 是普通概率

log_predictions = torch.log_softmax(torch.randn(4, 5), dim=1)

targets         = torch.softmax(torch.randn(4, 5), dim=1)

loss = criterion(log_predictions, targets)

print(f"KL Div Loss: {loss.item():.4f}")
```

**知识蒸馏中的典型用法：**

## 实例

```python
temperature = 4.0  # 温度系数，越大越软化

# 教师模型输出

teacher_logits = torch.randn(32, 10)

# 学生模型输出

student_logits = torch.randn(32, 10)

soft_labels = torch.softmax(teacher_logits / temperature, dim=1)

soft_preds  = torch.log_softmax(student_logits / temperature, dim=1)

distill_loss = nn.KLDivLoss(reduction='batchmean')(soft_preds, soft_labels)

distill_loss *= temperature ** 2  # 还原梯度量级
```

### 4.3 MarginRankingLoss 排序损失

判断两个输入的相对顺序，常用于**排序学习**和**相似度学习**。

## 实例

```python
criterion = nn.MarginRankingLoss(margin=0.5)

# x1 应该比 x2 更靠近 target（y=1 表示 x1 > x2）

x1 = torch.tensor([0.8, 0.3, 0.6])

x2 = torch.tensor([0.2, 0.7, 0.5])

y  = torch.tensor([1.0, -1.0, 1.0])  # 1: x1>x2, -1: x1<x2

loss = criterion(x1, x2, y)
```

### 4.4 TripletMarginLoss 三元组损失

用于度量学习，要求 **anchor（锚点）** 与 **positive（同类）** 的距离小于与 **negative（异类）** 的距离。

## 实例

```python
criterion = nn.TripletMarginLoss(margin=1.0)

# 每个向量维度为 embedding_dim

anchor   = torch.randn(32, 128)   # 锚点样本

positive = torch.randn(32, 128)   # 同类样本

negative = torch.randn(32, 128)   # 异类样本

loss = criterion(anchor, positive, negative)

# 目标：dist(anchor, positive) + margin < dist(anchor, negative)
```

**适用场景：**人脸识别、图像检索、Few-Shot Learning。

### 4.5 CTCLoss 序列标注损失

用于**输入与输出长度不对齐**的序列任务，如语音识别（声学序列 -> 文字序列）、手写识别。

## 实例

```python
criterion = nn.CTCLoss(blank=0)  # blank 标签索引

# log_probs: (T, N, C) T=时间步, N=batch, C=类别数

T, N, C = 50, 4, 20

log_probs    = torch.log_softmax(torch.randn(T, N, C), dim=2)

targets      = torch.randint(1, C, (N * 10,))   # 拼接的目标序列

input_lengths  = torch.full((N,), T, dtype=torch.long)

target_lengths = torch.full((N,), 10, dtype=torch.long)

loss = criterion(log_probs, targets, input_lengths, target_lengths)
```

## 5. reduction 参数详解

所有损失函数都支持 `reduction` 参数，控制如何对样本损失进行汇总：

## 实例

```python
predictions = torch.tensor([1.0, 2.0, 3.0, 4.0])

targets     = torch.tensor([1.5, 2.5, 2.0, 5.0])

# 单个样本的误差: [0.25, 0.25, 1.00, 1.00]

# mean（默认）：对所有样本取平均

loss_mean = nn.MSELoss(reduction='mean')(predictions, targets)

print(f"mean:  {loss_mean.item():.4f}")   # 0.6250

# sum：对所有样本求和

loss_sum  = nn.MSELoss(reduction='sum')(predictions, targets)

print(f"sum:   {loss_sum.item():.4f}")    # 2.5000

# none：返回每个样本的独立损失（常用于加权）

loss_none = nn.MSELoss(reduction='none')(predictions, targets)

print(f"none:  {loss_none.tolist()}")     # [0.25, 0.25, 1.0, 1.0]
```

`reduction='none'` 的实际应用——对不同样本加权：

## 实例

```python
# 给误差大的样本更高权重（焦点损失思路）

per_sample_loss = nn.MSELoss(reduction='none')(predictions, targets)

weights = torch.tensor([1.0, 1.0, 2.0, 2.0])   # 手动设置权重

weighted_loss = (per_sample_loss * weights).mean()
```

## 6. 类别权重与样本权重

### 类别权重（处理类别不平衡）

当数据集中某些类别样本极少时，可以给少数类更高的权重：

## 实例

```python
# 假设 3 分类，类别 0 有 1000 个，类别 1 有 100 个，类别 2 有 50 个

# 权重与频率成反比

class_counts = torch.tensor([1000.0, 100.0, 50.0])

weights = 1.0 / class_counts

weights = weights / weights.sum() * len(weights)  # 归一化

criterion = nn.CrossEntropyLoss(weight=weights)
```

### 忽略特定标签

在语义分割等任务中，常需要忽略边界像素（标签为 255）：

## 实例

```python
# ignore_index：计算损失时忽略该标签

criterion = nn.CrossEntropyLoss(ignore_index=255)

# 语义分割场景

predictions = torch.randn(2, 21, 256, 256)   # (N, C, H, W)

targets     = torch.randint(0, 22, (2, 256, 256))

targets[targets == 21] = 255                  # 边界标注为 255

loss = criterion(predictions, targets)
```

## 7. 自定义损失函数

当内置损失函数无法满足需求时，可以通过两种方式自定义：

### 方式一：函数式（简单）

## 实例

```python
import torch

import torch.nn.functional as F

def focal_loss(predictions, targets, gamma=2.0, alpha=0.25):

    """

    Focal Loss：解决目标检测中正负样本严重不平衡问题

    对容易分类的样本降低权重，让模型聚焦于困难样本

    """

    ce_loss = F.cross_entropy(predictions, targets, reduction='none')

    pt = torch.exp(-ce_loss)                          # 预测正确的概率

    focal_weight = alpha * (1 - pt) ** gamma          # 难样本权重更高

    return (focal_weight * ce_loss).mean()

# 使用

predictions = torch.randn(8, 10)

targets     = torch.randint(0, 10, (8,))

loss = focal_loss(predictions, targets)
```

### 方式二：继承 nn.Module（推荐）

## 实例

```python
import torch

import torch.nn as nn

class DiceLoss(nn.Module):

    """

    Dice Loss：常用于图像分割，直接优化 Dice 系数

    对类别不平衡（如小目标分割）比 CrossEntropy 更鲁棒

    """

    def __init__(self, smooth=1.0):

        super().__init__()

        self.smooth = smooth

    def forward(self, predictions, targets):

        # predictions: (N, C, H, W) -> 经过 sigmoid 的概率

        # targets:     (N, C, H, W) -> one-hot 编码标签

        predictions = torch.sigmoid(predictions)

        # 展平到 (N, -1)

        pred_flat   = predictions.view(predictions.size(0), -1)

        target_flat = targets.view(targets.size(0), -1).float()

        intersection = (pred_flat * target_flat).sum(dim=1)

        dice = (2.0 * intersection + self.smooth) / (

            pred_flat.sum(dim=1) + target_flat.sum(dim=1) + self.smooth

        )

        return 1 - dice.mean()

class CombinedLoss(nn.Module):

    """

    组合损失：CrossEntropy + Dice，兼顾像素级分类和区域重叠

    图像分割常用组合

    """

    def __init__(self, ce_weight=0.5, dice_weight=0.5):

        super().__init__()

        self.ce_weight   = ce_weight

        self.dice_weight = dice_weight

        self.ce   = nn.CrossEntropyLoss()

        self.dice = DiceLoss()

    def forward(self, predictions, targets):

        return (self.ce_weight   * self.ce(predictions, targets) +

                self.dice_weight * self.dice(predictions, targets))

# 使用

criterion = CombinedLoss(ce_weight=0.4, dice_weight=0.6)
```

## 8. 损失函数选择指南

### 按任务类型选择

| 任务类型 | 推荐损失函数 | 备注 |
| --- | --- | --- |
| 多分类 | CrossEntropyLoss | 最通用，优先选择 |
| 多分类（类别不平衡） | CrossEntropyLoss(weight=...) | 给少数类加权 |
| 多分类（标签噪声大） | CrossEntropyLoss(label_smoothing=0.1) | 防止过拟合 |
| 二分类 | BCEWithLogitsLoss | 比 BCELoss 更稳定 |
| 多标签分类 | BCEWithLogitsLoss | 每个标签独立判断 |
| 目标检测（分类头） | CrossEntropyLoss / Focal Loss | 正负样本不平衡时用 Focal |
| 目标检测（回归头） | SmoothL1Loss / GIoULoss | 标准做法 |
| 普通回归 | MSELoss | 无离群点时首选 |
| 含离群点的回归 | HuberLoss / SmoothL1Loss | 鲁棒回归 |
| 图像分割 | CrossEntropyLoss + DiceLoss | 组合使用效果更好 |
| 语音识别 | CTCLoss | 序列对齐 |
| 度量学习 / 人脸识别 | TripletMarginLoss | 学习特征空间距离 |
| 知识蒸馏 | KLDivLoss | 学习软标签分布 |

### 常见误用与注意事项

## 实例

```python
# 错误：CrossEntropyLoss 之前手动做了 Softmax

output = torch.softmax(model(x), dim=1)   # 多余的 softmax

loss   = nn.CrossEntropyLoss()(output, targets)  # 内部还会再做一次

# 正确：直接传入 logits

output = model(x)  # 原始 logits

loss   = nn.CrossEntropyLoss()(output, targets)

# 错误：BCELoss 传入未 sigmoid 的原始值

loss = nn.BCELoss()(model(x), targets)    # 可能超出 [0,1]，数值不稳定

# 正确：使用 BCEWithLogitsLoss

loss = nn.BCEWithLogitsLoss()(model(x), targets)

# 错误：标签类型不匹配（整型 vs 浮点型）

targets = torch.tensor([1, 0, 1])                     # int 型

loss    = nn.BCEWithLogitsLoss()(preds, targets)       # 报错！

# 正确：BCEWithLogitsLoss 需要 float 标签

targets = torch.tensor([1.0, 0.0, 1.0])               # float 型

loss    = nn.BCEWithLogitsLoss()(preds, targets)       # 正确

# 错误：loss 没有 .item()，导致计算图不断积累，显存溢出

total_loss += loss      # loss 是张量，持有计算图

# 正确：用 .item() 取出标量

total_loss += loss.item()
```

## 完整训练示例

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 模型 & 损失函数 & 优化器

model     = MyModel().to(device)

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

optimizer = optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(num_epochs):

    model.train()

    total_loss, correct = 0.0, 0

    for inputs, labels in train_loader:

        inputs = inputs.to(device)

        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)          # 原始 logits

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item() * inputs.size(0)    # .item() 取标量

        correct    += (outputs.argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(train_loader.dataset)

    accuracy = correct / len(train_loader.dataset)

    print(f"Epoch {epoch+1} | Loss: {avg_loss:.4f} | Acc: {accuracy:.4f}")
```

---

# PyTorch 学习率调度器

学习率（Learning Rate）是神经网络训练中最重要的超参数之一。学习率过大，训练震荡甚至发散；学习率过小，收敛极慢，容易陷入局部最优。

**学习率调度器（LR Scheduler）** 通过在训练过程中动态调整学习率，兼顾训练初期的快速收敛与后期的精细调优。

## 1. 基础概念与使用模式

### 标准使用流程

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

model     = nn.Linear(10, 1)

optimizer = optim.SGD(model.parameters(), lr=0.1)

# 1. 创建调度器，传入 optimizer

scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

for epoch in range(100):

    # 2. 训练

    train(model, optimizer)

    # 3. 每个 epoch 结束后调用 scheduler.step()

    scheduler.step()

    # 4. 查看当前学习率

    current_lr = scheduler.get_last_lr()[0]

    print(f"Epoch {epoch+1}, LR: {current_lr:.6f}")
```

### step() 的调用时机

## 实例

```python
# 正确：optimizer.step() 在前，scheduler.step() 在后

optimizer.step()

scheduler.step()

# 错误：scheduler.step() 在 optimizer.step() 之前

# PyTorch 1.1.0 之后会产生警告，部分调度器行为异常

scheduler.step()

optimizer.step()
```

注意：`optimizer.step()` 必须在 `scheduler.step()` 之前调用。

### 查看和保存学习率状态

## 实例

```python
# 获取当前学习率

current_lr = optimizer.param_groups[0]['lr']

current_lr = scheduler.get_last_lr()[0]   # 上一次 step() 后的 LR

# 保存检查点（必须同时保存 scheduler 状态）

torch.save({

    'epoch':          epoch,

    'model':          model.state_dict(),

    'optimizer':      optimizer.state_dict(),

    'scheduler':      scheduler.state_dict(),   # 别漏掉这个

}, 'checkpoint.pth')

# 恢复检查点

ckpt = torch.load('checkpoint.pth')

model.load_state_dict(ckpt['model'])

optimizer.load_state_dict(ckpt['optimizer'])

scheduler.load_state_dict(ckpt['scheduler'])
```

## 2. 固定衰减调度器

### 2.1 StepLR 按步衰减

每隔固定 `step_size` 个 epoch，将学习率乘以 `gamma`。是最简单、最常用的调度器之一。

**公式：** lr = lr_base * gamma^(floor(step / step_size))

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = optim.lr_scheduler.StepLR(

    optimizer,

    step_size=30,   # 每 30 个 epoch 衰减一次

    gamma=0.1       # 每次乘以 0.1（即缩小为原来的 1/10）

)

# LR 变化：

# Epoch  0-29:  0.1

# Epoch 30-59:  0.01

# Epoch 60-89:  0.001

# Epoch 90+:    0.0001
```

**适用场景：**训练节奏固定、阶段清晰的任务，如 ResNet 在 ImageNet 上的训练（90 epoch，在第 30、60 epoch 衰减）。

### 2.2 MultiStepLR 多里程碑衰减

在指定的若干个 epoch（里程碑）处衰减学习率，比 StepLR 更灵活。

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = optim.lr_scheduler.MultiStepLR(

    optimizer,

    milestones=[30, 60, 80],   # 在第 30、60、80 epoch 衰减

    gamma=0.1

)

# LR 变化：

# Epoch  0-29:  0.1

# Epoch 30-59:  0.01

# Epoch 60-79:  0.001

# Epoch 80+:    0.0001
```

**适用场景：**已知在哪些 epoch 模型需要精细调整，如分类模型中后期精细收敛阶段。

### 2.3 ExponentialLR 指数衰减

每个 epoch 都衰减，学习率以指数形式持续下降，衰减更平滑。

**公式：** lr = lr_base * gamma^epoch

## 实例

```python
optimizer = optim.Adam(model.parameters(), lr=0.01)

scheduler = optim.lr_scheduler.ExponentialLR(

    optimizer,

    gamma=0.95   # 每个 epoch 乘以 0.95

)

# LR 变化（前 5 个 epoch）：

# Epoch 1: 0.0100

# Epoch 2: 0.0095

# Epoch 3: 0.0090

# Epoch 4: 0.0086

# Epoch 5: 0.0081
```

`gamma` 设置得太小（如 0.5）会导致学习率迅速趋近于零，通常设在 0.9~0.99 之间。

## 3. 自适应调度器

### 3.1 ReduceLROnPlateau 监控指标衰减

**最智能的调度器之一**：监控某个指标（如验证集 loss），当该指标停止改善时自动降低学习率。不需要提前知道在哪个 epoch 衰减。

## 实例

```python
optimizer = optim.Adam(model.parameters(), lr=0.01)

scheduler = optim.lr_scheduler.ReduceLROnPlateau(

    optimizer,

    mode='min',       # 'min': 监控值越小越好（loss）；'max': 越大越好（accuracy）

    factor=0.1,       # 触发时 lr = lr × factor

    patience=10,      # 允许指标停滞的 epoch 数，超过则衰减

    threshold=1e-4,   # 改善幅度小于该值视为未改善

    min_lr=1e-6,      # 学习率下限，不会低于此值

    verbose=True      # 打印衰减信息

)

for epoch in range(100):

    train_loss = train(model, optimizer)

    val_loss   = evaluate(model)

    # 与其他调度器不同，这里传入监控指标

    scheduler.step(val_loss)
```

**监控 Accuracy 的写法：**

## 实例

```python
scheduler = optim.lr_scheduler.ReduceLROnPlateau(

    optimizer,

    mode='max',       # accuracy 越大越好

    factor=0.5,

    patience=5,

)

scheduler.step(val_accuracy)
```

**适用场景：**几乎所有任务的默认首选，尤其是不确定训练多少 epoch、或训练不稳定时。

### 3.2 CosineAnnealingLR 余弦退火

学习率按**余弦曲线**从初始值平滑下降到最小值（`eta_min`），避免了阶梯式衰减的突变。

**公式：** lr_t = eta_min + 0.5 * (eta_max - eta_min) * (1 + cos(t * pi / T_max)

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = optim.lr_scheduler.CosineAnnealingLR(

    optimizer,

    T_max=100,     # 半个周期的长度（通常设为总 epoch 数）

    eta_min=1e-6   # 学习率最小值（默认 0）

)

# LR 变化轨迹（T_max=10 时的示意）：

# 0.1 -> 0.095 -> 0.079 -> 0.055 -> 0.026 -> 0.001

#              （余弦曲线平滑下降）
```

**适用场景：**训练 epoch 数固定的场景，在 Vision Transformer、ResNet 等论文中广泛使用，收敛质量好。

### 3.3 CosineAnnealingWarmRestarts

余弦退火的升级版，支持**周期性重启**（Warm Restarts）：每个周期结束后学习率重置回初始值，开始新一轮余弦衰减。允许模型跳出局部最优。

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.1)

scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(

    optimizer,

    T_0=10,       # 第一个周期的长度（epoch 数）

    T_mult=2,     # 每次重启后周期长度的倍数（1=等长，2=逐渐加长）

    eta_min=1e-6

)

# T_mult=2 时的周期长度：10 -> 20 -> 40 -> 80 ...

# LR 变化（T_0=10, T_mult=1）：

# 0.1 -> ... -> 0 -> 0.1 -> ... -> 0 -> 0.1（每 10 个 epoch 重启一次）
```

**适用场景：**训练大模型、或希望模型从多个收敛点中选最优时，配合 Snapshot Ensemble 使用效果显著。

## 4. 预热调度器

**Warmup（预热）**是指训练开始的若干步内，学习率从一个极小值逐渐升高到目标值。大 batch size 训练、Transformer 类模型几乎都需要预热，否则初期梯度更新过猛，模型难以稳定。

### 4.1 LinearLR 线性调度

在指定 epoch 内线性改变学习率（可用于线性预热或线性衰减）。

## 实例

```python
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 线性预热：前 5 个 epoch 内，lr 从 0.01×0.1=0.001 线性增长到 0.01

warmup_scheduler = optim.lr_scheduler.LinearLR(

    optimizer,

    start_factor=0.1,   # 初始 lr = base_lr × start_factor

    end_factor=1.0,     # 结束 lr = base_lr × end_factor

    total_iters=5       # 经过 5 个 epoch 完成

)

# LR 变化：0.001 -> 0.003 -> 0.005 -> 0.007 -> 0.009 -> 0.01
```

### 4.2 ConstantLR 常数阶段

在指定 epoch 数内，将学习率固定为 `base_lr × factor`，之后恢复原值。

## 实例

```python
# 前 5 个 epoch 使用 base_lr × 0.5，之后恢复正常

scheduler = optim.lr_scheduler.ConstantLR(

    optimizer,

    factor=0.5,

    total_iters=5

)
```

### 4.3 SequentialLR 组合调度

将多个调度器**按顺序串联**，是实现"预热 + 衰减"组合策略的标准做法。

## 实例

```python
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 阶段一：预热（前 5 个 epoch，LR 从 0.001 线性增长到 0.01）

warmup = optim.lr_scheduler.LinearLR(

    optimizer, start_factor=0.1, end_factor=1.0, total_iters=5

)

# 阶段二：余弦退火（剩余 95 个 epoch）

cosine = optim.lr_scheduler.CosineAnnealingLR(

    optimizer, T_max=95, eta_min=1e-6

)

# 组合：先执行 warmup，第 5 个 epoch 后切换到 cosine

scheduler = optim.lr_scheduler.SequentialLR(

    optimizer,

    schedulers=[warmup, cosine],

    milestones=[5]          # 在第 5 个 epoch 切换

)

# 使用方式与普通调度器完全一致

for epoch in range(100):

    train(...)

    scheduler.step()
```

**适用场景：**Transformer 训练的标配（预热 + 余弦退火），BERT、GPT、ViT 的预训练均采用此策略。

## 5. 循环调度器

### 5.1 CyclicLR 循环学习率

学习率在 `base_lr` 和 `max_lr` 之间**周期性循环**，可帮助模型探索更广的参数空间、跳出鞍点。

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.01)

scheduler = optim.lr_scheduler.CyclicLR(

    optimizer,

    base_lr=0.001,          # 学习率下界

    max_lr=0.01,            # 学习率上界

    step_size_up=2000,      # 从 base_lr 上升到 max_lr 的迭代步数

    step_size_down=2000,    # 从 max_lr 下降到 base_lr 的迭代步数（默认等于 step_size_up）

    mode='triangular',      # 三角形循环（等幅）

    # mode='triangular2'    # 每个周期振幅减半

    # mode='exp_range'      # 振幅指数衰减

)

# CyclicLR 按 step（batch）调用，不是按 epoch

for epoch in range(num_epochs):

    for inputs, labels in train_loader:

        optimizer.zero_grad()

        loss = criterion(model(inputs), labels)

        loss.backward()

        optimizer.step()

        scheduler.step()    # 每个 batch 后调用
```

**三种模式对比：**

| mode | 振幅变化 | 特点 |
| --- | --- | --- |
| triangular | 不变 | 稳定探索，适合初期 |
| triangular2 | 每周期减半 | 先探索后收敛 |
| exp_range | 指数衰减 | 最终平稳收敛 |

### 5.2 OneCycleLR 单周期策略

**性能最优的调度器之一**，由 fastai 提出的 1-Cycle Policy。整个训练只有一个周期：学习率先升后降，动量（momentum）反向变化。

训练速度更快，通常只需传统训练的 **1/5~1/10** 的 epoch 数就能达到相同精度。

## 实例

```python
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

steps_per_epoch = len(train_loader)

scheduler = optim.lr_scheduler.OneCycleLR(

    optimizer,

    max_lr=0.1,                              # 学习率最高点

    steps_per_epoch=steps_per_epoch,         # 每个 epoch 的 step 数

    epochs=10,                               # 总 epoch 数

    pct_start=0.3,                           # 前 30% 用于预热上升

    anneal_strategy='cos',                   # 衰减策略（'cos' 或 'linear'）

    div_factor=25,                           # 初始 lr = max_lr / div_factor

    final_div_factor=1e4                     # 最终 lr = max_lr / final_div_factor

)

# 初始 lr = 0.1 / 25 = 0.004

# 峰值 lr = 0.1（在 30% 处）

# 最终 lr = 0.1 / 10000 = 0.00001

# 同样按 batch 调用

for epoch in range(10):

    for inputs, labels in train_loader:

        optimizer.zero_grad()

        loss = criterion(model(inputs), labels)

        loss.backward()

        optimizer.step()

        scheduler.step()    # 每个 batch 后调用
```

**适用场景：**在计算资源有限、需要快速验证想法时首选；`max_lr` 建议通过 LR Finder 工具确定最优值。

## 6. 自定义调度器

### 6.1 LambdaLR 函数式自定义

通过传入一个 Lambda 函数（接受 epoch 数，返回学习率乘数）来完全自定义调度策略。

## 实例

```python
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 示例一：Transformer 经典预热策略

# lr ∝ min(step^-0.5, step × warmup_steps^-1.5)

def transformer_lr(epoch, warmup_epochs=10, d_model=512):

    if epoch == 0:

        return 1e-7 / 0.01          # 避免除零

    step = epoch + 1

    warmup = warmup_epochs

    return (d_model ** -0.5) * min(step ** -0.5, step * warmup ** -1.5) / 0.01

scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=transformer_lr)

# 示例二：多项式衰减（lr 从初始值线性/多项式降到 0）

def polynomial_decay(epoch, total_epochs=100, power=1.0):

    return max((1 - epoch / total_epochs) ** power, 0.0)

scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=polynomial_decay)

# 示例三：分组学习率（不同参数组不同策略）

optimizer = optim.Adam([

    {'params': model.backbone.parameters(), 'lr': 1e-4},

    {'params': model.head.parameters(),     'lr': 1e-3},

])

# 每个参数组一个 lambda 函数

scheduler = optim.lr_scheduler.LambdaLR(

    optimizer,

    lr_lambda=[

        lambda epoch: 0.95 ** epoch,    # backbone：慢衰减

        lambda epoch: 0.85 ** epoch,    # head：快衰减

    ]

)
```

### 6.2 继承 LRScheduler

需要更复杂的逻辑时，继承 `LRScheduler`（PyTorch >= 2.0，旧版为 `_LRScheduler`）实现完全自定义：

## 实例

```python
from torch.optim.lr_scheduler import LRScheduler

import math

class WarmupCosineScheduler(LRScheduler):

    """

    预热 + 余弦退火组合调度器（手动实现版）

    - 前 warmup_epochs 个 epoch 线性预热

    - 之后余弦退火到 min_lr

    """

    def __init__(self, optimizer, warmup_epochs, total_epochs,

                 min_lr=1e-6, last_epoch=-1):

        self.warmup_epochs = warmup_epochs

        self.total_epochs  = total_epochs

        self.min_lr        = min_lr

        super().__init__(optimizer, last_epoch)

    def get_lr(self):

        epoch = self.last_epoch

        # 预热阶段：线性增大

        if epoch < self.warmup_epochs:

            warmup_factor = (epoch + 1) / self.warmup_epochs

            return [base_lr * warmup_factor for base_lr in self.base_lrs]

        # 余弦退火阶段

        progress = (epoch - self.warmup_epochs) / (

            self.total_epochs - self.warmup_epochs

        )

        cosine_factor = 0.5 * (1 + math.cos(math.pi * progress))

        return [

            self.min_lr + (base_lr - self.min_lr) * cosine_factor

            for base_lr in self.base_lrs

        ]

optimizer = optim.Adam(model.parameters(), lr=0.01)

scheduler = WarmupCosineScheduler(

    optimizer,

    warmup_epochs=10,

    total_epochs=100,

    min_lr=1e-6

)
```

## 7. 调度器可视化对比

以下代码可以绘制各调度器的 LR 变化曲线，方便直观对比：

## 实例

```python
import torch

import torch.optim as optim

import matplotlib.pyplot as plt

def simulate_lr(scheduler_fn, epochs=100, steps_per_epoch=None):

    """模拟并记录调度器的学习率变化"""

    model     = torch.nn.Linear(1, 1)

    optimizer = optim.SGD(model.parameters(), lr=0.1)

    scheduler = scheduler_fn(optimizer)

    lrs = []

    if steps_per_epoch:

        # 按 step 调用的调度器

        for _ in range(epochs):

            for _ in range(steps_per_epoch):

                optimizer.step()

                scheduler.step()

                lrs.append(optimizer.param_groups[0]['lr'])

    else:

        # 按 epoch 调用的调度器

        for _ in range(epochs):

            optimizer.step()

            scheduler.step()

            lrs.append(optimizer.param_groups[0]['lr'])

    return lrs

schedulers = {

    'StepLR(step=30, gamma=0.1)':

        lambda opt: optim.lr_scheduler.StepLR(opt, 30, 0.1),

    'CosineAnnealingLR':

        lambda opt: optim.lr_scheduler.CosineAnnealingLR(opt, T_max=100),

    'ExponentialLR(gamma=0.95)':

        lambda opt: optim.lr_scheduler.ExponentialLR(opt, 0.95),

    'CosineWarmRestarts(T0=25)':

        lambda opt: optim.lr_scheduler.CosineAnnealingWarmRestarts(opt, T_0=25),

}

plt.figure(figsize=(12, 5))

for name, fn in schedulers.items():

    plt.plot(simulate_lr(fn), label=name)

plt.xlabel('Epoch')

plt.ylabel('Learning Rate')

plt.title('PyTorch LR Scheduler Comparison')

plt.legend()

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig('lr_schedulers.png', dpi=150)

plt.show()
```

## 8. 完整训练模板

集成了预热 + 余弦退火、模型保存与恢复的生产级训练模板：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.optim.lr_scheduler import SequentialLR, LinearLR, CosineAnnealingLR

# 超参数

EPOCHS       = 100

WARMUP_EPOCHS = 5

BASE_LR      = 1e-3

MIN_LR       = 1e-6

SAVE_PATH    = 'best_model.pth'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 模型 / 优化器 / 调度器

model     = MyModel().to(device)

optimizer = optim.AdamW(model.parameters(), lr=BASE_LR, weight_decay=1e-4)

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

# 预热 5 epoch + 余弦退火 95 epoch

warmup_sched = LinearLR(optimizer, start_factor=0.1, total_iters=WARMUP_EPOCHS)

cosine_sched = CosineAnnealingLR(optimizer, T_max=EPOCHS - WARMUP_EPOCHS, eta_min=MIN_LR)

scheduler    = SequentialLR(optimizer, [warmup_sched, cosine_sched], milestones=[WARMUP_EPOCHS])

# 恢复检查点

start_epoch = 0

best_acc    = 0.0

try:

    ckpt = torch.load(SAVE_PATH, map_location=device)

    model.load_state_dict(ckpt['model'])

    optimizer.load_state_dict(ckpt['optimizer'])

    scheduler.load_state_dict(ckpt['scheduler'])

    start_epoch = ckpt['epoch'] + 1

    best_acc    = ckpt['best_acc']

    print(f"恢复自 Epoch {start_epoch}，最佳准确率 {best_acc:.4f}")

except FileNotFoundError:

    print("从头开始训练")

# 训练循环

history = {'train_loss': [], 'val_acc': [], 'lr': []}

for epoch in range(start_epoch, EPOCHS):

    # 训练

    model.train()

    total_loss = 0.0

    for inputs, labels in train_loader:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        loss = criterion(model(inputs), labels)

        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # 梯度裁剪

        optimizer.step()

        total_loss += loss.item()

    # 验证

    model.eval()

    correct = 0

    with torch.no_grad():

        for inputs, labels in val_loader:

            inputs, labels = inputs.to(device), labels.to(device)

            correct += (model(inputs).argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(train_loader)

    val_acc  = correct / len(val_loader.dataset)

    cur_lr   = scheduler.get_last_lr()[0]

    # 记录 & 打印

    history['train_loss'].append(avg_loss)

    history['val_acc'].append(val_acc)

    history['lr'].append(cur_lr)

    print(f"Epoch {epoch+1:3d}/{EPOCHS} | "

          f"Loss: {avg_loss:.4f} | Acc: {val_acc:.4f} | LR: {cur_lr:.2e}")

    # 调度器更新

    scheduler.step()

    # 保存最优模型

    if val_acc > best_acc:

        best_acc = val_acc

        torch.save({

            'epoch':      epoch,

            'model':      model.state_dict(),

            'optimizer':  optimizer.state_dict(),

            'scheduler':  scheduler.state_dict(),

            'best_acc':   best_acc,

        }, SAVE_PATH)

        print(f"  保存最优模型，Acc: {best_acc:.4f}")

print(f"\n训练完成，最佳验证准确率: {best_acc:.4f}")
```

## 9. 调度器选择指南

### 按任务类型推荐

| 场景 | 推荐调度器 | 理由 |
| --- | --- | --- |
| 快速实验 / 原型验证 | ReduceLROnPlateau | 无需调超参，自适应衰减 |
| 图像分类（固定 epoch） | CosineAnnealingLR | 平滑衰减，收敛质量好 |
| Transformer / BERT | LinearLR + CosineAnnealingLR | 预热必不可少 |
| 资源有限，快速训练 | OneCycleLR | 1/5 时间达同等精度 |
| 大模型精调（fine-tune） | LinearLR（预热） + ConstantLR | 低学习率稳定微调 |
| 不确定 epoch 数 | ReduceLROnPlateau | 自动响应，不依赖固定节奏 |
| 目标检测（YOLO/Faster-RCNN） | MultiStepLR / OneCycleLR | 有明确衰减点或追求速度 |
| 希望跳出局部最优 | CosineAnnealingWarmRestarts | 周期重启探索参数空间 |

### 常见配置组合

## 实例

```python
# 组合一：Warmup + 余弦退火（Transformer 标配）

SequentialLR([LinearLR(5 epochs), CosineAnnealingLR(95 epochs)])

# 组合二：监控验证集 + 自动衰减（通用首选）

ReduceLROnPlateau(mode='min', patience=5, factor=0.5)

# 组合三：OneCycleLR（快速训练首选）

OneCycleLR(max_lr=0.1, total_steps=total_steps, pct_start=0.3)

# 组合四：传统阶梯衰减（CV 经典）

MultiStepLR(milestones=[30, 60, 90], gamma=0.1)
```

### 注意事项速查

| 问题 | 解决方法 |
| --- | --- |
| 调度器没有生效 | 检查 scheduler.step() 是否在 optimizer.step() 之后 调用 |
| CyclicLR / OneCycleLR 没变化 | 这两个按 batch 调用，不是按 epoch |
| ReduceLROnPlateau 不触发 | 检查 mode 是否设对（loss 用 'min'，accuracy 用 'max'） |
| 恢复训练后 LR 不对 | 检查是否保存并加载了 scheduler.state_dict() |
| 多参数组 LR 设置 | 使用 LambdaLR 传入列表，每个参数组一个 lambda |

---

# PyTorch 迁移学习

迁移学习（Transfer Learning）是指将在大规模数据集上预训练好的模型，迁移到新的、数据量较少的任务上进行训练的技术。

它是当今深度学习实践中使用最广泛的技术之一——在大多数情况下，迁移学习比从零开始训练效果更好、速度更快、所需数据更少。

## 1. 迁移学习核心思想

深度神经网络在 ImageNet 上学到的特征具有通用性：

- 浅层网络：学习通用低级特征（边缘、纹理、颜色梯度）

- 中层网络：学习通用中级特征（形状、部件、纹理组合）

- 深层网络：学习任务相关的高级特征（人脸、轮子、文字）

这些低中层特征对绝大部分视觉任务都有效，无需重新学习。

### 什么时候使用迁移学习？

| 数据量 | 与源任务相似度 | 推荐策略 |
| --- | --- | --- |
| 少（ 10000） | 任意 | 全部微调，或考虑从头训练 |

### 三种核心策略对比

预训练模型（如 ResNet50）的层次结构如下：

- Conv Layer 1~3（低级特征：边缘/纹理）：通常冻结

- Conv Layer 4~6（中级特征：形状/部件）：可选冻结

- Conv Layer 7~N（高级特征：语义信息）：微调

- Classifier Head（分类头）：替换并训练

```python
┌─────────────────────────────────────────────────┐

│              预训练模型（如 ResNet50）             │

│  ┌──────────────────────────────────────────┐   │

│  │  Conv Layer 1~3（低级特征：边缘/纹理）      │  ← 通常冻结

│  ├──────────────────────────────────────────┤   │

│  │  Conv Layer 4~6（中级特征：形状/部件）      │  ← 可选冻结

│  ├──────────────────────────────────────────┤   │

│  │  Conv Layer 7~N（高级特征：语义信息）       │  ← 微调

│  ├──────────────────────────────────────────┤   │

│  │  Classifier Head（分类头）                 │  ← 替换 & 训练

│  └──────────────────────────────────────────┘   │

└─────────────────────────────────────────────────┘
```

## 2. 加载预训练模型

PyTorch 通过 torchvision.models 提供了大量官方预训练模型，加载非常简单。

## 实例

```python
import torch

import torchvision.models as models

# 加载预训练模型（自动下载权重）

# PyTorch >= 0.13 推荐新写法：使用 weights 参数

from torchvision.models import ResNet50_Weights

model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)

# 旧写法（仍然有效，但会收到 deprecation 警告）

model = models.resnet50(pretrained=True)

# 不加载预训练权重（仅使用网络结构）

model = models.resnet50(weights=None)
```

### 查看模型结构

## 实例

```python
# 打印完整结构

print(model)

# 只查看最后几层（分类头）

print(model.fc)

# Linear(in_features=2048, out_features=1000, bias=True)

# 统计参数量

total_params    = sum(p.numel() for p in model.parameters())

trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"总参数量:   {total_params:,}")

print(f"可训练参数: {trainable_params:,}")
```

### 各模型分类头的名称

不同模型的分类头属性名不同，迁移时需要替换对应层：

| 模型 | 分类头属性 |
| --- | --- |
| ResNet / RegNet | model.fc |
| VGG / AlexNet | model.classifier[-1] |
| DenseNet | model.classifier |
| EfficientNet | model.classifier[-1] |
| MobileNetV2/V3 | model.classifier[-1] |
| ViT (Vision Transformer) | model.heads.head |
| ConvNeXt | model.classifier[-1] |
| Inception V3 | model.fc |
| Swin Transformer | model.head |

## 3. 三种迁移策略

### 3.1 策略一：特征提取（冻结全部）

冻结预训练模型的全部参数，只训练新替换的分类头。

适合数据量极少（几百张），或任务与源任务高度相似的场景。

## 实例

```python
import torch

import torch.nn as nn

import torchvision.models as models

from torchvision.models import ResNet18_Weights

NUM_CLASSES = 5   # 目标任务的类别数

# Step 1：加载预训练模型

model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

# Step 2：冻结所有参数

for param in model.parameters():

    param.requires_grad = False

# Step 3：替换分类头（这部分参数默认 requires_grad=True）

in_features = model.fc.in_features    # 512

model.fc = nn.Linear(in_features, NUM_CLASSES)

# 验证：只有分类头是可训练的

trainable = [(n, p.shape) for n, p in model.named_parameters() if p.requires_grad]

print(f"可训练层数: {len(trainable)}")

for name, shape in trainable:

    print(f"  {name}: {shape}")

# 输出：

#   fc.weight: torch.Size([5, 512])

#   fc.bias:   torch.Size([5])

# Step 4：优化器只传可训练参数（更高效）

optimizer = torch.optim.Adam(

    filter(lambda p: p.requires_grad, model.parameters()),

    lr=1e-3

)

# 或等价的更清晰写法：

optimizer = torch.optim.Adam(model.fc.parameters(), lr=1e-3)
```

特征提取是最简单也是最常用的迁移学习策略，特别适合数据量较少的场景。

### 3.2 策略二：微调（Fine-tuning）

解冻全部或部分预训练层，使用较小的学习率整体训练。

适合数据量中等，或任务与源任务有所不同的场景。

## 实例

```python
import torch

import torch.nn as nn

import torchvision.models as models

NUM_CLASSES = 10

model = models.resnet50(weights='IMAGENET1K_V2')

# 方式 A：全量微调（解冻所有层）

# 先冻结

for param in model.parameters():

    param.requires_grad = False

# 再解冻（等价于全量微调，此写法常用于逐步解冻场景）

for param in model.parameters():

    param.requires_grad = True

# 替换分类头

model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

# 全量微调：主干用小学习率，头部用大学习率（见策略三）

optimizer = torch.optim.SGD(model.parameters(), lr=1e-4, momentum=0.9)

# 方式 B：解冻最后 N 层（部分微调）

model = models.resnet50(weights='IMAGENET1K_V2')

# 先全部冻结

for param in model.parameters():

    param.requires_grad = False

# 只解冻 layer4 和 fc（ResNet 的最后一个 Block 和分类头）

for param in model.layer4.parameters():

    param.requires_grad = True

model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)  # fc 默认可训练

print("可训练参数:")

for name, param in model.named_parameters():

    if param.requires_grad:

        print(f"  {name}")
```

### 3.3 策略三：分层差异化学习率

主干（backbone）使用小学习率（保留预训练知识），分类头使用大学习率（快速适应新任务）。

这是业界最常用的微调策略，综合效果最好。

## 实例

```python
import torch

import torch.nn as nn

import torchvision.models as models

NUM_CLASSES = 8

model = models.resnet50(weights='IMAGENET1K_V2')

model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

# 方案一：两组学习率（主干 vs 头部）

optimizer = torch.optim.Adam([

    {'params': model.fc.parameters(),  'lr': 1e-3},     # 分类头：大学习率

    {'params': [p for n, p in model.named_parameters()  # 主干：小学习率

                if not n.startswith('fc')],

     'lr': 1e-5},

])

# 方案二：逐层递减学习率（最精细）

# 越靠近输出的层，学习率越大

layer_groups = [

    (model.layer1, 1e-5),    # 最浅层，最小学习率

    (model.layer2, 3e-5),

    (model.layer3, 1e-4),

    (model.layer4, 3e-4),    # 最深主干层

    (model.fc,     1e-3),    # 分类头，最大学习率

]

param_groups = [

    {'params': layer.parameters(), 'lr': lr}

    for layer, lr in layer_groups

]

optimizer = torch.optim.Adam(param_groups)

# 方案三：逐步解冻（Gradual Unfreezing）

# 训练初期只训练头部，逐步解冻更多层（fastai 推荐）

model = models.resnet50(weights='IMAGENET1K_V2')

for param in model.parameters():

    param.requires_grad = False

model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

def unfreeze_layers(model, num_layers):

    """解冻 ResNet 最后 num_layers 个 layer block"""

    layers = [model.layer4, model.layer3, model.layer2, model.layer1]

    for i in range(min(num_layers, len(layers))):

        for param in layers[i].parameters():

            param.requires_grad = True

# Epoch 1-5：只训练分类头

# Epoch 6-10：解冻 layer4

unfreeze_layers(model, num_layers=1)

# Epoch 11+：解冻更多层

unfreeze_layers(model, num_layers=3)
```

## 4. 常用预训练模型

### 4.1 图像分类模型

## 实例

```python
import torchvision.models as models

# ResNet 系列（最经典，适合大多数任务）

resnet18  = models.resnet18(weights='IMAGENET1K_V1')   # 轻量，适合边缘设备

resnet50  = models.resnet50(weights='IMAGENET1K_V2')   # 均衡之选

resnet101 = models.resnet101(weights='IMAGENET1K_V2')  # 更强，更慢

# EfficientNet 系列（精度效率比极高）

effnet_b0 = models.efficientnet_b0(weights='IMAGENET1K_V1')  # 最轻量

effnet_b4 = models.efficientnet_b4(weights='IMAGENET1K_V1')  # 均衡

effnet_b7 = models.efficientnet_b7(weights='IMAGENET1K_V1')  # 最强

# Vision Transformer（大数据量任务首选）

vit_b16 = models.vit_b_16(weights='IMAGENET1K_V1')    # ViT-Base/16

vit_l16 = models.vit_l_16(weights='IMAGENET1K_V1')    # ViT-Large/16

# MobileNet（移动端/嵌入式部署）

mobilenet_v3 = models.mobilenet_v3_small(weights='IMAGENET1K_V1')

# ConvNeXt（CNN 的现代化版本，性能接近 ViT）

convnext_t = models.convnext_tiny(weights='IMAGENET1K_V1')

convnext_b = models.convnext_base(weights='IMAGENET1K_V1')
```

**主流模型性能对比（ImageNet Top-1 Acc）：**

| 模型 | Top-1 Acc | 参数量 | 推理速度 | 适用场景 |
| --- | --- | --- | --- | --- |
| ResNet-18 | 69.8% | 11.7M | 极快 | 资源受限、快速原型 |
| ResNet-50 | 80.9% | 25.6M | 快 | 通用首选 |
| EfficientNet-B4 | 83.4% | 19.3M | 中 | 精度效率均衡 |
| ConvNeXt-Base | 84.1% | 88.6M | 中 | 高精度 CNN |
| ViT-B/16 | 81.1% | 86.6M | 中 | 大数据量场景 |
| ViT-L/16 | 85.1% | 307M | 慢 | 最高精度 |

### 4.2 目标检测模型

## 实例

```python
import torchvision.models.detection as detection

# Faster R-CNN（经典两阶段检测器）

faster_rcnn = detection.fasterrcnn_resnet50_fpn(weights='DEFAULT')

# SSD（单阶段检测器，速度快）

ssd = detection.ssd300_vgg16(weights='DEFAULT')

# RetinaNet

retinanet = detection.retinanet_resnet50_fpn(weights='DEFAULT')

# FCOS

fcos = detection.fcos_resnet50_fpn(weights='DEFAULT')

# 替换 Faster R-CNN 的分类头（适配新类别数）

from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

NUM_CLASSES = 5 + 1   # 5 个目标类 + 1 个背景类

faster_rcnn = detection.fasterrcnn_resnet50_fpn(weights='DEFAULT')

in_features = faster_rcnn.roi_heads.box_predictor.cls_score.in_features

faster_rcnn.roi_heads.box_predictor = FastRCNNPredictor(in_features, NUM_CLASSES)
```

### 4.3 文本模型（HuggingFace）

NLP 任务的迁移学习通常使用 HuggingFace transformers 库：

## 实例

```python
# pip install transformers

from transformers import (

    BertForSequenceClassification,

    RobertaForSequenceClassification,

    AutoModelForSequenceClassification,

    AutoTokenizer,

)

NUM_CLASSES = 3

# BERT（文本分类首选）

model = BertForSequenceClassification.from_pretrained(

    'bert-base-chinese',     # 中文 BERT

    num_labels=NUM_CLASSES

)

tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')

# RoBERTa（BERT 改进版，更强）

model = RobertaForSequenceClassification.from_pretrained(

    'roberta-base',

    num_labels=NUM_CLASSES

)

# 通用加载方式（自动识别模型类型）

model = AutoModelForSequenceClassification.from_pretrained(

    'hfl/chinese-roberta-wwm-ext',    # 中文 RoBERTa

    num_labels=NUM_CLASSES

)
```

## 5. 数据预处理与增强

迁移学习使用 ImageNet 预训练权重时，必须使用与预训练相同的归一化参数，否则特征分布不匹配，效果会大幅下降。

## 实例

```python
from torchvision import transforms

# ImageNet 标准归一化参数（所有 torchvision 预训练模型通用）

IMAGENET_MEAN = [0.485, 0.456, 0.406]

IMAGENET_STD  = [0.229, 0.224, 0.225]

# 训练集：含数据增强

train_transforms = transforms.Compose([

    transforms.RandomResizedCrop(224),          # 随机裁剪并 resize

    transforms.RandomHorizontalFlip(p=0.5),    # 随机水平翻转

    transforms.ColorJitter(                    # 颜色抖动

        brightness=0.2, contrast=0.2,

        saturation=0.2, hue=0.1

    ),

    transforms.RandomRotation(degrees=15),     # 随机旋转

    transforms.ToTensor(),

    transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),

])

# 验证/测试集：不做随机增强

val_transforms = transforms.Compose([

    transforms.Resize(256),                    # 先 resize 到 256

    transforms.CenterCrop(224),                # 再中心裁剪到 224

    transforms.ToTensor(),

    transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),

])

# 数据集加载（目录结构：root/class_name/img.jpg）

from torchvision.datasets import ImageFolder

from torch.utils.data import DataLoader

train_dataset = ImageFolder(root='data/train', transform=train_transforms)

val_dataset   = ImageFolder(root='data/val',   transform=val_transforms)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True,

                          num_workers=4, pin_memory=True)

val_loader   = DataLoader(val_dataset,   batch_size=32, shuffle=False,

                          num_workers=4, pin_memory=True)

print(f"训练样本数: {len(train_dataset)}")

print(f"类别列表:   {train_dataset.classes}")

print(f"类别映射:   {train_dataset.class_to_idx}")
```

### 使用 torchvision 官方推荐预处理

## 实例

```python
# PyTorch >= 0.13：直接从 weights 对象获取标准预处理，无需手动指定参数

from torchvision.models import ResNet50_Weights

weights   = ResNet50_Weights.IMAGENET1K_V2

model     = models.resnet50(weights=weights)

preprocess = weights.transforms()   # 自动返回对应的预处理 pipeline

# preprocess 已包含 Resize(232)、CenterCrop(224)、Normalize 等步骤

# 训练时只需在此基础上追加数据增强
```

必须使用 ImageNet 的归一化参数 [0.485, 0.456, 0.406] 和 [0.229, 0.224, 0.225]，否则预训练特征将无法正确对齐。

## 6. 完整实战：图像二分类

以猫狗分类为例，展示从数据准备到训练评估的完整迁移学习流程：

## 实例

```python
import os

import torch

import torch.nn as nn

import torch.optim as optim

from torch.optim.lr_scheduler import CosineAnnealingLR

from torchvision import models, transforms, datasets

from torch.utils.data import DataLoader, random_split

from torchvision.models import EfficientNet_B0_Weights

# 配置

DEVICE      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

NUM_CLASSES = 2

BATCH_SIZE  = 32

EPOCHS      = 20

BASE_LR     = 1e-3

DATA_DIR    = 'data/cats_and_dogs'

# 数据准备

train_tfm = transforms.Compose([

    transforms.RandomResizedCrop(224),

    transforms.RandomHorizontalFlip(),

    transforms.ColorJitter(brightness=0.3, contrast=0.3),

    transforms.ToTensor(),

    transforms.Normalize([0.485, 0.456, 0.406],

                         [0.229, 0.224, 0.225]),

])

val_tfm = transforms.Compose([

    transforms.Resize(256),

    transforms.CenterCrop(224),

    transforms.ToTensor(),

    transforms.Normalize([0.485, 0.456, 0.406],

                         [0.229, 0.224, 0.225]),

])

full_dataset = datasets.ImageFolder(DATA_DIR, transform=train_tfm)

n_val   = int(len(full_dataset) * 0.2)

n_train = len(full_dataset) - n_val

train_set, val_set = random_split(full_dataset, [n_train, n_val])

val_set.dataset = datasets.ImageFolder(DATA_DIR, transform=val_tfm)  # 替换 val 的 transform

train_loader = DataLoader(train_set, BATCH_SIZE, shuffle=True,

                          num_workers=4, pin_memory=True)

val_loader   = DataLoader(val_set,   BATCH_SIZE, shuffle=False,

                          num_workers=4, pin_memory=True)

# 构建迁移模型

weights = EfficientNet_B0_Weights.IMAGENET1K_V1

model   = models.efficientnet_b0(weights=weights)

# 冻结主干

for param in model.parameters():

    param.requires_grad = False

# 替换分类头（EfficientNet-B0 的头部结构）

in_features = model.classifier[1].in_features  # 1280

model.classifier = nn.Sequential(

    nn.Dropout(p=0.2, inplace=True),

    nn.Linear(in_features, NUM_CLASSES),

)

model = model.to(DEVICE)

# 优化器：分层学习率

optimizer = optim.Adam([

    {'params': model.classifier.parameters(), 'lr': BASE_LR},

    {'params': model.features.parameters(),   'lr': BASE_LR * 0.1},

])

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

scheduler = CosineAnnealingLR(optimizer, T_max=EPOCHS, eta_min=1e-6)

# 训练与验证函数

def train_epoch(model, loader, optimizer, criterion):

    model.train()

    total_loss, correct = 0.0, 0

    for imgs, labels in loader:

        imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()

        outputs = model(imgs)

        loss    = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item() * imgs.size(0)

        correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

def eval_epoch(model, loader, criterion):

    model.eval()

    total_loss, correct = 0.0, 0

    with torch.no_grad():

        for imgs, labels in loader:

            imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

            outputs = model(imgs)

            loss    = criterion(outputs, labels)

            total_loss += loss.item() * imgs.size(0)

            correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

# 分阶段训练

print("=== 阶段一：只训练分类头（Epoch 1-5）===")

best_acc = 0.0

for epoch in range(1, EPOCHS + 1):

    # 第 5 个 epoch 解冻主干，进入全量微调阶段

    if epoch == 6:

        print("\n=== 阶段二：解冻主干全量微调（Epoch 6-20）===")

        for param in model.features.parameters():

            param.requires_grad = True

    train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion)

    val_loss,   val_acc   = eval_epoch(model,  val_loader,   criterion)

    scheduler.step()

    print(f"Epoch {epoch:2d}/{EPOCHS} | "

          f"Train Loss: {train_loss:.4f}, Acc: {train_acc:.4f} | "

          f"Val Loss: {val_loss:.4f}, Acc: {val_acc:.4f} | "

          f"LR: {scheduler.get_last_lr()[0]:.2e}")

    if val_acc > best_acc:

        best_acc = val_acc

        torch.save(model.state_dict(), 'best_model.pth')

        print(f"  ✓ 保存最优模型 Acc={best_acc:.4f}")

print(f"\n训练完成，最佳验证准确率: {best_acc:.4f}")
```

### 推理与预测

## 实例

```python
from PIL import Image

# 加载最优模型

model.load_state_dict(torch.load('best_model.pth', map_location=DEVICE))

model.eval()

# 预测单张图片

def predict(image_path, model, class_names):

    img = Image.open(image_path).convert('RGB')

    tensor = val_tfm(img).unsqueeze(0).to(DEVICE)  # (1, 3, 224, 224)

    with torch.inference_mode():

        logits = model(tensor)

        probs  = torch.softmax(logits, dim=1)[0]

        pred   = probs.argmax().item()

    for cls, prob in zip(class_names, probs.tolist()):

        print(f"  {cls}: {prob:.4f}")

    print(f"预测结果: {class_names[pred]}")

    return class_names[pred]

class_names = train_set.dataset.classes  # ['cat', 'dog']

predict('test_cat.jpg', model, class_names)
```

## 7. 完整实战：文本分类（BERT）

## 实例

```python
# pip install transformers datasets

import torch

import torch.nn as nn

from torch.utils.data import Dataset, DataLoader

from transformers import (

    BertTokenizer,

    BertForSequenceClassification,

    AdamW,

    get_linear_schedule_with_warmup,

)

DEVICE      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

MODEL_NAME  = 'bert-base-chinese'

NUM_CLASSES = 3       # 情感分类：正/中/负

MAX_LEN     = 128

BATCH_SIZE  = 16

EPOCHS      = 5

LR          = 2e-5    # BERT 微调的推荐学习率范围：1e-5 ~ 5e-5

# 自定义 Dataset

class SentimentDataset(Dataset):

    def __init__(self, texts, labels, tokenizer, max_len):

        self.texts     = texts

        self.labels    = labels

        self.tokenizer = tokenizer

        self.max_len   = max_len

    def __len__(self):

        return len(self.texts)

    def __getitem__(self, idx):

        encoding = self.tokenizer(

            self.texts[idx],

            max_length=self.max_len,

            padding='max_length',

            truncation=True,

            return_tensors='pt',

        )

        return {

            'input_ids':      encoding['input_ids'].squeeze(0),

            'attention_mask': encoding['attention_mask'].squeeze(0),

            'label':          torch.tensor(self.labels[idx], dtype=torch.long),

        }

# 加载 BERT 预训练模型

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

model     = BertForSequenceClassification.from_pretrained(

    MODEL_NAME,

    num_labels=NUM_CLASSES,

    hidden_dropout_prob=0.1,

)

model = model.to(DEVICE)

# 冻结底部 N 层（可选）

# BERT-base 有 12 层 Transformer，可以冻结前几层节省计算

FREEZE_LAYERS = 6   # 冻结前 6 层

for i, layer in enumerate(model.bert.encoder.layer):

    if i < FREEZE_LAYERS:

        for param in layer.parameters():

            param.requires_grad = False

print(f"已冻结前 {FREEZE_LAYERS} 层，减少约 {FREEZE_LAYERS/12*100:.0f}% 的参数更新")

# 数据加载

# 示例数据（实际替换为真实数据集）

train_texts  = ["这部电影太棒了！", "服务很差，失望", "一般般，没什么特别"]

train_labels = [2, 0, 1]  # 0:负 1:中 2:正

train_dataset = SentimentDataset(train_texts, train_labels, tokenizer, MAX_LEN)

train_loader  = DataLoader(train_dataset, BATCH_SIZE, shuffle=True)

# 优化器与调度器

# BERT 标配：AdamW + 线性 warmup

no_decay = ['bias', 'LayerNorm.weight']

optimizer_grouped = [

    {'params': [p for n, p in model.named_parameters()

                if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},

    {'params': [p for n, p in model.named_parameters()

                if     any(nd in n for nd in no_decay)], 'weight_decay': 0.0},

]

optimizer = AdamW(optimizer_grouped, lr=LR)

total_steps   = len(train_loader) * EPOCHS

warmup_steps  = int(total_steps * 0.1)   # 10% 的步数用于预热

scheduler = get_linear_schedule_with_warmup(

    optimizer,

    num_warmup_steps=warmup_steps,

    num_training_steps=total_steps,

)

# 训练循环

for epoch in range(1, EPOCHS + 1):

    model.train()

    total_loss, correct = 0.0, 0

    for batch in train_loader:

        input_ids      = batch['input_ids'].to(DEVICE)

        attention_mask = batch['attention_mask'].to(DEVICE)

        labels         = batch['label'].to(DEVICE)

        optimizer.zero_grad()

        outputs = model(input_ids=input_ids,

                        attention_mask=attention_mask,

                        labels=labels)

        loss   = outputs.loss           # BERT 内部已计算 CE Loss

        logits = outputs.logits

        loss.backward()

        # BERT 微调标配：梯度裁剪，防止梯度爆炸

        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()

        scheduler.step()

        total_loss += loss.item()

        correct    += (logits.argmax(1) == labels).sum().item()

    avg_loss = total_loss / len(train_loader)

    acc      = correct / len(train_dataset)

    print(f"Epoch {epoch}/{EPOCHS} | Loss: {avg_loss:.4f} | Acc: {acc:.4f}")

# 推理

def predict_sentiment(text, model, tokenizer, id2label):

    model.eval()

    encoding = tokenizer(text, max_length=MAX_LEN, padding='max_length',

                         truncation=True, return_tensors='pt')

    with torch.inference_mode():

        outputs = model(

            input_ids      = encoding['input_ids'].to(DEVICE),

            attention_mask = encoding['attention_mask'].to(DEVICE),

        )

    pred = outputs.logits.argmax(1).item()

    return id2label[pred]

id2label = {0: '负面', 1: '中性', 2: '正面'}

print(predict_sentiment("这款产品质量真的很好！", model, tokenizer, id2label))
```

## 8. 模型结构修改技巧

### 替换分类头的通用方法

## 实例

```python
import torch.nn as nn

import torchvision.models as models

def build_transfer_model(arch, num_classes, pretrained=True, dropout=0.5):

    """

    通用迁移模型构建函数，自动识别分类头并替换

    支持: resnet, efficientnet, densenet, mobilenet, vit, convnext

    """

    weights = 'IMAGENET1K_V1' if pretrained else None

    model   = getattr(models, arch)(weights=weights)

    name    = arch.lower()

    if 'resnet' in name or 'resnext' in name or 'inception' in name:

        in_f = model.fc.in_features

        model.fc = nn.Sequential(

            nn.Dropout(dropout),

            nn.Linear(in_f, num_classes)

        )

    elif 'efficientnet' in name or 'mobilenet' in name or 'convnext' in name:

        in_f = model.classifier[-1].in_features

        model.classifier[-1] = nn.Sequential(

            nn.Dropout(dropout),

            nn.Linear(in_f, num_classes)

        )

    elif 'densenet' in name:

        in_f = model.classifier.in_features

        model.classifier = nn.Linear(in_f, num_classes)

    elif 'vit' in name or 'swin' in name:

        in_f = model.heads.head.in_features

        model.heads.head = nn.Linear(in_f, num_classes)

    else:

        raise ValueError(f"不支持的架构: {arch}")

    return model

# 使用示例

model_resnet  = build_transfer_model('resnet50',        num_classes=10)

model_effnet  = build_transfer_model('efficientnet_b3', num_classes=10)

model_vit     = build_transfer_model('vit_b_16',        num_classes=10)
```

### 添加中间特征提取层

## 实例

```python
import torch

import torch.nn as nn

import torchvision.models as models

class TransferWithAttention(nn.Module):

    """在预训练主干后接自定义注意力模块和分类头"""

    def __init__(self, num_classes, dropout=0.5):

        super().__init__()

        backbone = models.resnet50(weights='IMAGENET1K_V2')

        # 去掉原始分类头，保留 feature extractor

        self.backbone  = nn.Sequential(*list(backbone.children())[:-1])

        self.feat_dim  = 2048   # ResNet50 特征维度

        # 自定义注意力门控

        self.attention = nn.Sequential(

            nn.Linear(self.feat_dim, 512),

            nn.Tanh(),

            nn.Linear(512, 1),

            nn.Sigmoid()

        )

        # 分类头

        self.classifier = nn.Sequential(

            nn.Dropout(dropout),

            nn.Linear(self.feat_dim, 256),

            nn.ReLU(),

            nn.Linear(256, num_classes),

        )

    def forward(self, x):

        feat   = self.backbone(x).flatten(1)          # (N, 2048)

        weight = self.attention(feat)                  # (N, 1)

        feat   = feat * weight                         # 加权特征

        return self.classifier(feat)
```

## 9. 迁移学习最佳实践

### 学习率选择

## 实例

```python
# 主干（预训练层）学习率

# 通常设为头部学习率的 1/10 ~ 1/100

backbone_lr = 1e-5   # 保守策略，数据量少时推荐

head_lr     = 1e-3   # 新层从随机初始化开始，需要较大学习率

# BERT / ViT 等 Transformer 的学习率

# 这类大模型对学习率极其敏感，超出范围会破坏预训练知识

bert_lr = 2e-5        # 推荐范围：1e-5 ~ 5e-5
```

### 常见问题与解决方案

## 实例

```python
# 问题一：显存不足

# 解法 1：减小 batch size

# 解法 2：使用梯度检查点（以时间换空间）

from torch.utils.checkpoint import checkpoint_sequential

model.features = lambda x: checkpoint_sequential(model.features, 4, x)

# 解法 3：冻结更多层（减少反向传播计算量）

# 问题二：训练集准确率高，验证集低（过拟合）

# 解法 1：增强数据增强

# 解法 2：增大 Dropout

model.classifier = nn.Sequential(nn.Dropout(0.5), nn.Linear(in_f, num_classes))

# 解法 3：使用 Label Smoothing

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

# 解法 4：冻结更多主干层，减少可训练参数

# 问题三：训练不稳定，Loss 震荡

# 解法 1：降低学习率（减半再试）

# 解法 2：添加 warmup 预热

# 解法 3：梯度裁剪

nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# 解法 4：更换优化器（Adam → AdamW）

# 问题四：归一化参数未匹配

# 错误：使用自定义归一化，与预训练不匹配

transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])

# 正确：必须使用 ImageNet 的均值和标准差

transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
```

### 整体策略速查

| 问题 | 推荐做法 |
| --- | --- |
| 数据量  10000 | 全量微调，考虑更大学习率或从头训练 |
| 训练速度慢 | 先冻结训练几轮再解冻；使用 AMP 混合精度 |
| 效果瓶颈 | 换更大/更新的 backbone；尝试 ConvNeXt / ViT |
| 模型要上线部署 | 优先选 EfficientNet-B0 / MobileNetV3 等轻量模型 |
| 中文 NLP 任务 | BERT-base-chinese 或 chinese-roberta-wwm-ext |

### 推荐的完整训练策略

第一阶段（Epoch 1~N/4）：

- 冻结主干，只训练分类头

- 使用较大学习率（1e-3），快速收敛头部参数

第二阶段（Epoch N/4~N）：

- 解冻主干，全量微调

- 主干使用小学习率（1e-5），头部保持（1e-3）

- 配合余弦退火或 ReduceLROnPlateau

保存策略：

- 只保存验证集指标最优的 checkpoint

- 同时保存 model / optimizer / scheduler 状态

---

-

# PyTorch 批归一化与 Dropout

批归一化（Batch Normalization）和 Dropout 是深度神经网络训练中两种最核心的正则化与稳定化技术。前者解决训练过程中的内部协变量偏移问题，让更深的网络变得可训练；后者通过随机丢弃神经元防止过拟合，增强模型泛化能力。两者通常配合使用，是现代神经网络的标配组件。

## 1. 批归一化（Batch Normalization）

### 1.1 基础原理

深层网络在训练时，前一层参数的微小变化会随层数加深而被不断放大，导致后续层的输入分布持续变化——这一现象称为**内部协变量偏移（Internal Covariate Shift）**。批归一化通过在每一层的输出上做标准化，强制将激活值拉回稳定的分布，从而解决这一问题。

**归一化公式：**

\[\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}\]

\[y_i = \gamma \hat{x}_i + \beta\]

其中：

- \(\mu_B\)、\(\sigma_B^2\) 是当前 batch 的均值和方差

- \(\epsilon\) 是防止除零的小常数（默认 `1e-5`）

- \(\gamma\)、\(\beta\) 是可学习的缩放和平移参数，让网络自行决定最终的分布形态

**批归一化带来的好处：**

- 允许使用更大的学习率，加快训练速度

- 降低初始化的敏感性，训练更稳定

- 有一定正则化效果，减轻对 Dropout 的依赖

- 缓解梯度消失/爆炸，使更深的网络可训练

### 1.2 BatchNorm1d / 2d / 3d

PyTorch 根据输入维度提供三个版本，使用方式完全一致，只是处理的数据形状不同。

#### BatchNorm1d：用于全连接层 / 序列数据

## 实例

```python
import torch

import torch.nn as nn

# 输入形状：(N, C) 或 (N, C, L)

# N=batch_size, C=特征数/通道数, L=序列长度

bn1d = nn.BatchNorm1d(

    num_features=128,    # 特征/通道数

    eps=1e-5,            # 防止除零的小常数（默认 1e-5）

    momentum=0.1,        # 滑动平均的动量（默认 0.1）

    affine=True,         # 是否学习 gamma 和 beta（默认 True）

    track_running_stats=True,  # 是否追踪运行时均值/方差（默认 True）

)

# 全连接层后使用

x = torch.randn(32, 128)     # (batch=32, features=128)

out = bn1d(x)

print(out.shape)              # torch.Size([32, 128])

# 序列数据（如 1D 卷积后）

x_seq = torch.randn(32, 128, 50)   # (batch, channels, seq_len)

out_seq = bn1d(x_seq)

print(out_seq.shape)               # torch.Size([32, 128, 50])
```

#### BatchNorm2d：用于 CNN 图像特征图

## 实例

```python
# 输入形状：(N, C, H, W)

# 对每个通道 C 独立做归一化

bn2d = nn.BatchNorm2d(num_features=64)  # 64 个通道

x = torch.randn(32, 64, 28, 28)    # (batch, channels, height, width)

out = bn2d(x)

print(out.shape)                    # torch.Size([32, 64, 28, 28])
```

#### BatchNorm3d：用于 3D 卷积（视频/医学影像）

## 实例

```python
# 输入形状：(N, C, D, H, W)

bn3d = nn.BatchNorm3d(num_features=32)

x = torch.randn(4, 32, 16, 32, 32)    # (batch, channels, depth, h, w)

out = bn3d(x)

print(out.shape)                        # torch.Size([4, 32, 16, 32, 32])
```

#### 查看可学习参数

## 实例

```python
bn = nn.BatchNorm2d(64)

print(f"weight (gamma) shape: {bn.weight.shape}")   # torch.Size([64])

print(f"bias   (beta)  shape: {bn.bias.shape}")     # torch.Size([64])

print(f"running_mean   shape: {bn.running_mean.shape}")  # torch.Size([64])

print(f"running_var    shape: {bn.running_var.shape}")   # torch.Size([64])

# running_mean / running_var 不是可训练参数

# 它们是推理时使用的滑动平均统计量

print(f"可训练参数数量: {sum(p.numel() for p in bn.parameters())}")  # 128（64×2）
```

#### momentum 参数的含义

## 实例

```python
# PyTorch 的 momentum 与通常理解相反：

# running_mean = (1 - momentum) × running_mean + momentum × batch_mean

# 即 momentum 越大，对当前 batch 的统计量权重越大

# 默认 0.1：通常合适

# 小 batch size 时建议调小：momentum=0.01，避免统计量不稳定

bn = nn.BatchNorm2d(64, momentum=0.01)

# momentum=None：使用累积移动平均（CMA），适合非常小的 batch

bn = nn.BatchNorm2d(64, momentum=None)
```

### 1.3 LayerNorm 层归一化

对**单个样本的所有特征**做归一化，不依赖 batch，适合 batch size 小或可变的场景。**Transformer 的标配归一化方式**。

```python
BatchNorm：在 batch 维度计算均值/方差（跨样本，同通道）

LayerNorm：在特征维度计算均值/方差（同样本，跨特征）
```

## 实例

```python
import torch

import torch.nn as nn

# ── 用于全连接/Transformer ────────────────────────

# normalized_shape：对最后几个维度做归一化

ln = nn.LayerNorm(normalized_shape=512)

x = torch.randn(32, 10, 512)   # (batch, seq_len, embed_dim)

out = ln(x)

print(out.shape)                # torch.Size([32, 10, 512])

# ── 对多个维度归一化 ───────────────────────────────

ln_2d = nn.LayerNorm([64, 28, 28])   # 对 C, H, W 三个维度归一化

x = torch.randn(8, 64, 28, 28)

out = ln_2d(x)

# ── Transformer 中的典型用法 ──────────────────────

class TransformerBlock(nn.Module):

    def __init__(self, embed_dim, num_heads, ff_dim):

        super().__init__()

        self.attn  = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)

        self.ff    = nn.Sequential(

            nn.Linear(embed_dim, ff_dim),

            nn.GELU(),

            nn.Linear(ff_dim, embed_dim),

        )

        self.norm1 = nn.LayerNorm(embed_dim)   # ← 每个子层后归一化

        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):

        attn_out, _ = self.attn(x, x, x)

        x = self.norm1(x + attn_out)            # 残差 + 归一化

        x = self.norm2(x + self.ff(x))

        return x
```

### 1.4 GroupNorm 组归一化

将通道分成若干**组**，在每组内做归一化。不依赖 batch size，在小 batch 场景（如目标检测、医学影像分割）效果优于 BatchNorm。

## 实例

```python
# num_groups：将通道分成多少组（必须能整除 num_channels）

# 特殊情况：num_groups=1 等价于 LayerNorm

#           num_groups=num_channels 等价于 InstanceNorm

gn = nn.GroupNorm(

    num_groups=32,       # 分组数（常用：8, 16, 32）

    num_channels=256,    # 通道数

    eps=1e-5,

    affine=True,

)

x = torch.randn(4, 256, 56, 56)    # 小 batch（4 张图），256 通道

out = gn(x)

print(out.shape)                    # torch.Size([4, 256, 56, 56])

# GroupNorm 在 batch=1 时（如推理单张图）效果完全不受影响

x_single = torch.randn(1, 256, 56, 56)

out_single = gn(x_single)           # 完全正常工作
```

### 1.5 InstanceNorm 实例归一化

对**每个样本的每个通道**独立归一化，不涉及 batch 维度。常用于**图像风格迁移**——保留每张图自身的风格信息，不让 batch 内其他图像的统计量干扰。

## 实例

```python
# InstanceNorm2d：对每个 (N, C) 上的 H×W 做归一化

in2d = nn.InstanceNorm2d(

    num_features=64,

    affine=False,    # 默认 False（不学习 gamma/beta）

)

x = torch.randn(8, 64, 128, 128)

out = in2d(x)

print(out.shape)    # torch.Size([8, 64, 128, 128])
```

### 1.6 各归一化方法对比

| 方法 | 归一化维度 | batch 依赖 | 适用场景 |
| --- | --- | --- | --- |
| BatchNorm | 跨 batch（同通道） | 强依赖 | CNN 图像分类（大 batch） |
| LayerNorm | 跨特征（同样本） | 无依赖 | Transformer、NLP、RNN |
| GroupNorm | 组内通道（同样本） | 无依赖 | 小 batch 目标检测、分割 |
| InstanceNorm | 空间维度（同样本同通道） | 无依赖 | 图像风格迁移、生成模型 |

## 选择建议速查

```python
# batch_size >= 16，CNN 图像任务       → BatchNorm2d

# Transformer / BERT / GPT            → LayerNorm

# batch_size < 8，目标检测/分割        → GroupNorm(num_groups=32)

# 图像风格迁移 / CycleGAN             → InstanceNorm2d
```

## 2. Dropout

### 2.1 基础原理

Dropout 在训练时随机将某些神经元的输出置为 0（概率为 `p`），强迫网络不能依赖任何单一神经元，从而学习更鲁棒、分散的特征表示，有效防止过拟合。

**训练时：**

\[y_i = \begin{cases} 0 & \text{以概率 } p \\ \dfrac{x_i}{1-p} & \text{以概率 } 1-p \end{cases}\]

保留的神经元会被放大 \(\frac{1}{1-p}\) 倍，以保持期望值不变（即 Inverted Dropout）。

**推理时：** Dropout **自动关闭**，所有神经元正常参与计算，相当于多个子网络的集成平均。

```python
训练时示意（p=0.5）：

输入:  [1.0,  2.0,  3.0,  4.0,  5.0]

掩码:  [ 1,    0,    1,    0,    1 ]   ← 随机生成

输出:  [2.0,  0.0,  6.0,  0.0, 10.0]  ← 保留的值乘以 1/(1-0.5)=2

推理时：

输出:  [1.0,  2.0,  3.0,  4.0,  5.0]  ← 原样输出
```

### 2.2 Dropout / Dropout2d / Dropout3d

#### Dropout：用于全连接层

## 实例

```python
import torch

import torch.nn as nn

dropout = nn.Dropout(p=0.5)   # p：置零的概率

x = torch.ones(2, 10)

print("训练模式:")

dropout.train()

print(dropout(x))    # 约 50% 的值为 0，保留的值为 2.0

print("\n评估模式:")

dropout.eval()

print(dropout(x))    # 全为 1.0，Dropout 关闭
```

输出示例：

```python
训练模式:

tensor([[2., 0., 2., 0., 2., 0., 0., 2., 2., 0.],

[0., 2., 0., 2., 0., 2., 2., 0., 0., 2.]])

评估模式:

tensor([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],

[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])
```

#### Dropout2d：用于 CNN 特征图（整通道丢弃）

`Dropout2d` 以通道为单位随机丢弃，即整个通道的所有空间位置一起被置零。这比逐点 Dropout 更适合卷积特征，因为相邻像素的激活值高度相关，逐点丢弃效果较弱。

## 实例

```python
dropout2d = nn.Dropout2d(p=0.3)

# 输入：(N, C, H, W)

x = torch.ones(4, 16, 8, 8)    # 4 张图，16 通道

out = dropout2d(x)

print(out.shape)                # torch.Size([4, 16, 8, 8])

# 验证：整通道丢弃

# 第 0 张图的通道丢弃情况（非零 = 保留通道，全零 = 被丢弃通道）

kept_channels = (out[0].sum(dim=(1, 2)) != 0).sum().item()

print(f"第 0 张图保留了 {kept_channels}/16 个通道")
```

#### Dropout3d：用于 3D 卷积

## 实例

```python
# 输入：(N, C, D, H, W)，整个 (D, H, W) 特征体被丢弃

dropout3d = nn.Dropout3d(p=0.2)

x = torch.ones(2, 8, 16, 16, 16)

out = dropout3d(x)

print(out.shape)   # torch.Size([2, 8, 16, 16, 16])
```

#### p 值的选择建议

## 实例

```python
# 全连接层（隐藏层较宽）：较高 Dropout

nn.Dropout(p=0.5)     # 经典值，隐藏层标配

# 全连接层（隐藏层较窄）或小网络：较低 Dropout

nn.Dropout(p=0.2)     # 避免欠拟合

# 卷积层 Dropout2d：一般较低

nn.Dropout2d(p=0.1)   # 卷积层本身已有一定正则效果

# 分类头前的 Dropout（如 EfficientNet / ViT）

nn.Dropout(p=0.3)     # 通常在 0.2~0.5 之间

# Transformer 的注意力 / FFN Dropout

nn.Dropout(p=0.1)     # BERT 默认值，Transformer 通常较小
```

### 2.3 AlphaDropout

专为 **SELU 激活函数**设计的 Dropout 变体，在丢弃神经元后会自动调整均值和方差，保持自归一化（self-normalizing）属性。

## 实例

```python
# 配合 SELU 使用（自归一化网络 SELU + AlphaDropout）

class SelfNormalizingNet(nn.Module):

    def __init__(self, in_dim, hidden_dim, num_classes):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(in_dim, hidden_dim),

            nn.SELU(),

            nn.AlphaDropout(p=0.1),   # ← 配合 SELU 使用

            nn.Linear(hidden_dim, hidden_dim),

            nn.SELU(),

            nn.AlphaDropout(p=0.1),

            nn.Linear(hidden_dim, num_classes),

        )

    def forward(self, x):

        return self.net(x)
```

**注意：** AlphaDropout 仅在使用 SELU 激活函数时有意义，配合其他激活函数时直接用普通 Dropout。

## 3. 训练模式与评估模式

BatchNorm 和 Dropout 的行为在训练和评估时**完全不同**，必须正确切换，这是初学者最常见的错误之一。

### 行为差异对比

| 组件 | model.train() | model.eval() |
| --- | --- | --- |
| BatchNorm | 用当前 batch 的均值/方差归一化；更新 running_mean/var | 用 running_mean/var 归一化；不更新 |
| Dropout | 随机置零（按概率 p） | 关闭，所有神经元正常输出 |

### 正确使用方式

## 实例

```python
import torch

import torch.nn as nn

model = nn.Sequential(

    nn.Linear(128, 256),

    nn.BatchNorm1d(256),

    nn.ReLU(),

    nn.Dropout(0.5),

    nn.Linear(256, 10),

)

# ── 训练阶段 ──────────────────────────────────────

model.train()    # ← 切换到训练模式（默认状态）

for inputs, labels in train_loader:

    optimizer.zero_grad()

    outputs = model(inputs)   # BN 用 batch 统计，Dropout 随机丢弃

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()

# ── 评估/验证阶段 ─────────────────────────────────

model.eval()     # ← 切换到评估模式（非常重要！）

with torch.no_grad():              # 同时关闭梯度计算

    for inputs, labels in val_loader:

        outputs = model(inputs)    # BN 用运行统计，Dropout 关闭

        # ...

# ── 推理单张图片 ──────────────────────────────────

model.eval()

with torch.inference_mode():       # 比 no_grad 更快，推理专用

    output = model(single_input.unsqueeze(0))

    pred   = output.argmax(1).item()
```

### 验证模式切换是否正确

## 实例

```python
# 用这段代码验证 BN 和 Dropout 是否在正确模式下工作

x = torch.randn(8, 128)

model.train()

out_train_1 = model(x)

out_train_2 = model(x)

print("训练模式两次输出相同?", torch.allclose(out_train_1, out_train_2))

# False ← 每次 Dropout 掩码不同，输出不同（正常现象）

model.eval()

out_eval_1 = model(x)

out_eval_2 = model(x)

print("评估模式两次输出相同?", torch.allclose(out_eval_1, out_eval_2))

# True ← Dropout 关闭，BN 使用固定统计量，输出确定（正常现象）
```

## 4. 在网络中的使用位置

### BatchNorm 的放置位置

BatchNorm 的位置存在两种流派，目前均有实践：

## 流派一：激活函数之前（原始论文）

```python
# Conv → BN → ReLU

nn.Sequential(

    nn.Conv2d(32, 64, 3, padding=1),

    nn.BatchNorm2d(64),      # BN 在激活前

    nn.ReLU(inplace=True),

)
```

## 流派二：激活函数之后（部分研究认为效果更好）

```python
# Conv → ReLU → BN

nn.Sequential(

    nn.Conv2d(32, 64, 3, padding=1),

    nn.ReLU(inplace=True),

    nn.BatchNorm2d(64),      # BN 在激活后

)
```

**实际建议：** 遵循你所参考论文的设计；没有特殊要求时，Conv → BN → ReLU 更为主流

### Dropout 的放置位置

## 全连接网络：放在激活函数之后

```python
nn.Sequential(

    nn.Linear(512, 256),

    nn.ReLU(),

    nn.Dropout(0.5),         # 在 ReLU 后

    nn.Linear(256, 128),

    nn.ReLU(),

    nn.Dropout(0.5),

    nn.Linear(128, 10),      # 输出层前通常不加 Dropout

)
```

## CNN：放在 BN 之后（如有 BN 则 Dropout 可省略）

```python
# 注意：BN 本身有正则效果，CNN 中若已有 BN，卷积层不必加 Dropout

# Dropout 通常只加在全连接层或分类头前

nn.Sequential(

    nn.Conv2d(64, 128, 3, padding=1),

    nn.BatchNorm2d(128),

    nn.ReLU(inplace=True),

    # 通常不在这里加 Dropout（BN 已提供正则效果）

)
```

## Transformer：放在 FFN 和注意力层内部

```python
class FeedForward(nn.Module):

    def __init__(self, d_model, d_ff, dropout=0.1):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(d_model, d_ff),

            nn.GELU(),

            nn.Dropout(dropout),  # FFN 内部加 Dropout

            nn.Linear(d_ff, d_model),

            nn.Dropout(dropout),  # 输出前再加一次

        )

    def forward(self, x):

        return self.net(x)
```

### BN 与 Dropout 是否同时使用？

## 全连接网络：可以同时使用

```python
nn.Sequential(

    nn.Linear(512, 256),

    nn.BatchNorm1d(256),

    nn.ReLU(),

    nn.Dropout(0.3),         # BN + Dropout 共存，常见且有效

    nn.Linear(256, 10),

)
```

卷积网络：通常二选一或仅在头部用 Dropout。

原因：BN 的归一化操作与 Dropout 可能产生"方差偏移"问题。即训练时 Dropout 改变了激活值的方差，而推理时 Dropout 关闭，导致 BN 推理时看到的统计量与训练时不一致。

**推荐做法：**

方案 A：卷积层只用 BN，全连接/分类头只用 Dropout

## 实例

```python
class ConvNet(nn.Module):

    def __init__(self, num_classes):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.BatchNorm2d(64),       # 卷积部分：只用 BN

            nn.ReLU(inplace=True),

            nn.Conv2d(64, 128, 3, padding=1),

            nn.BatchNorm2d(128),

            nn.ReLU(inplace=True),

            nn.AdaptiveAvgPool2d(1),

        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(128, 256),

            nn.ReLU(),

            nn.Dropout(0.5),          # 全连接部分：只用 Dropout

            nn.Linear(256, num_classes),

        )

    def forward(self, x):

        return self.classifier(self.features(x))
```

## 5. 完整网络实例

### 实例一：全连接分类网络（BN + Dropout）

## 实例

```python
import torch

import torch.nn as nn

class MLPClassifier(nn.Module):

    """

    带 BatchNorm1d 和 Dropout 的全连接分类器

    适用于表格数据分类任务

    """

    def __init__(self, in_dim, hidden_dims, num_classes, dropout=0.5):

        super().__init__()

        layers = []

        prev_dim = in_dim

        for hidden_dim in hidden_dims:

            layers += [

                nn.Linear(prev_dim, hidden_dim),

                nn.BatchNorm1d(hidden_dim),

                nn.ReLU(inplace=True),

                nn.Dropout(dropout),

            ]

            prev_dim = hidden_dim

        layers.append(nn.Linear(prev_dim, num_classes))

        self.net = nn.Sequential(*layers)

    def forward(self, x):

        return self.net(x)

model = MLPClassifier(

    in_dim=784,

    hidden_dims=[512, 256, 128],

    num_classes=10,

    dropout=0.4

)

# 验证输出形状

x = torch.randn(32, 784)

model.eval()

print(model(x).shape)   # torch.Size([32, 10])
```

### 实例二：CNN 图像分类（BN 为主）

## 实例

```python
class ConvBNBlock(nn.Module):

    """标准卷积块：Conv → BN → ReLU"""

    def __init__(self, in_ch, out_ch, stride=1):

        super().__init__()

        self.block = nn.Sequential(

            nn.Conv2d(in_ch, out_ch, 3, stride=stride, padding=1, bias=False),

            nn.BatchNorm2d(out_ch),    # bias=False：BN 的 beta 已起偏置作用

            nn.ReLU(inplace=True),

        )

    def forward(self, x):

        return self.block(x)

class SmallCNN(nn.Module):

    """用于 CIFAR-10 的小型 CNN"""

    def __init__(self, num_classes=10):

        super().__init__()

        self.features = nn.Sequential(

            ConvBNBlock(3, 32),               # 32×32 → 32×32

            ConvBNBlock(32, 64, stride=2),    # 32×32 → 16×16

            ConvBNBlock(64, 128, stride=2),   # 16×16 → 8×8

            ConvBNBlock(128, 256, stride=2),  # 8×8 → 4×4

            nn.AdaptiveAvgPool2d(1),          # 4×4 → 1×1

        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(256, 128),

            nn.ReLU(),

            nn.Dropout(0.5),                  # 只在全连接层用 Dropout

            nn.Linear(128, num_classes),

        )

    def forward(self, x):

        return self.classifier(self.features(x))

model = SmallCNN(num_classes=10)

x = torch.randn(16, 3, 32, 32)

model.eval()

print(model(x).shape)   # torch.Size([16, 10])
```

### 实例三：完整训练循环

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.optim.lr_scheduler import CosineAnnealingLR

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

EPOCHS = 50

model     = SmallCNN(num_classes=10).to(DEVICE)

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)

scheduler = CosineAnnealingLR(optimizer, T_max=EPOCHS)

def run_epoch(model, loader, optimizer=None, train=True):

    if train:

        model.train()    # ← BN 用 batch 统计，Dropout 激活

    else:

        model.eval()     # ← BN 用 running 统计，Dropout 关闭

    total_loss, correct = 0.0, 0

    ctx = torch.enable_grad() if train else torch.no_grad()

    with ctx:

        for imgs, labels in loader:

            imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)

            if train:

                optimizer.zero_grad()

            outputs = model(imgs)

            loss    = criterion(outputs, labels)

            if train:

                loss.backward()

                optimizer.step()

            total_loss += loss.item() * imgs.size(0)

            correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

best_acc = 0.0

for epoch in range(1, EPOCHS + 1):

    train_loss, train_acc = run_epoch(model, train_loader, optimizer, train=True)

    val_loss,   val_acc   = run_epoch(model, val_loader,   train=False)

    scheduler.step()

    print(f"Epoch {epoch:2d}/{EPOCHS} | "

          f"Train {train_loss:.4f}/{train_acc:.4f} | "

          f"Val {val_loss:.4f}/{val_acc:.4f}")

    if val_acc > best_acc:

        best_acc = val_acc

        torch.save(model.state_dict(), 'best.pth')
```

## 6. 超参数调优指南

### BatchNorm 参数调优

## 实例

```python
# ── momentum（最常需要调整的参数）─────────────────

# 默认值 0.1 在大多数情况下有效

# batch_size 很小（< 8）→ 统计量不稳定 → 减小 momentum

nn.BatchNorm2d(64, momentum=0.01)

# 训练步数很多、数据分布平稳 → 可以适当增大 momentum

nn.BatchNorm2d(64, momentum=0.2)

# ── affine=False（不学习 gamma/beta）──────────────

# 极少使用，通常保持默认 True

# 除非明确不希望 BN 改变特征的缩放和偏移

nn.BatchNorm2d(64, affine=False)

# ── track_running_stats=False ──────────────────────

# 每次推理也用当前 batch 统计（训练和推理行为一致）

# 适合在线学习、流数据等特殊场景

nn.BatchNorm2d(64, track_running_stats=False)
```

### Dropout 调优策略

## 实例

```python
# ── 根据过拟合程度调整 p ───────────────────────────

# 训练 acc 远高于验证 acc（严重过拟合） → 增大 p

# 训练 acc 与验证 acc 接近但都偏低（欠拟合） → 减小 p 或去掉 Dropout

# ── 推荐的 p 值参考 ───────────────────────────────

p_values = {

    '大型全连接隐藏层（> 1024）': 0.5,

    '中型全连接隐藏层（256~1024）': 0.3,

    '小型全连接隐藏层（< 256）': 0.2,

    'CNN 卷积层（Dropout2d）': 0.1,

    '分类头前': 0.3,

    'Transformer FFN': 0.1,

    'Transformer 注意力': 0.1,

}

# ── 动态 Dropout（随训练进程调整）──────────────────

# 某些实践中，训练初期 p 较小，后期增大（模型越来越复杂时加强正则）

class DynamicDropoutNet(nn.Module):

    def __init__(self, initial_p=0.1):

        super().__init__()

        self.dropout = nn.Dropout(initial_p)

        self.fc = nn.Linear(256, 10)

    def set_dropout(self, p):

        self.dropout.p = p

    def forward(self, x):

        return self.fc(self.dropout(x))

model = DynamicDropoutNet(initial_p=0.1)

# 训练到中期，增大 Dropout

model.set_dropout(0.4)
```

## 7. 常见错误与注意事项

### 错误一：忘记切换 eval() 模式

## 错误写法

```python
# 错误：评估时没有调用 model.eval()

model.train()   # 默认状态

for imgs, labels in val_loader:

    with torch.no_grad():

        outputs = model(imgs)   # Dropout 仍然随机丢弃！BN 仍在更新！

        # 结果不确定，准确率虚低，且污染了 running_mean/var
```

## 正确写法

```python
# 正确：评估前明确切换模式

model.eval()

with torch.no_grad():

    outputs = model(imgs)    # 确定性输出
```

### 错误二：Conv 层加了 bias 又接 BN

## 错误写法

```python
# 多余：Conv 的 bias 会被 BN 的 beta 抵消，浪费参数

nn.Conv2d(64, 128, 3, padding=1, bias=True),   # 默认 True

nn.BatchNorm2d(128),
```

## 正确写法

```python
# 正确：Conv 接 BN 时，关闭 bias

nn.Conv2d(64, 128, 3, padding=1, bias=False),  # ← bias=False

nn.BatchNorm2d(128),
```

### 错误三：batch size=1 时使用 BatchNorm

## 错误写法

```python
# 错误：batch=1 时 BN 无法计算方差，训练时会出现 NaN 或 inf

# 单样本推理没问题（使用 running stats），但单样本训练会崩溃

model.train()

x = torch.randn(1, 64, 32, 32)

out = bn2d(x)    # ← 训练模式下 batch=1 会报错或产生 NaN
```

## 解决方案

```python
# 解决方案一：使用 GroupNorm 替代

nn.GroupNorm(num_groups=32, num_channels=64)

# 解决方案二：使用 LayerNorm

nn.LayerNorm([64, 32, 32])

# 解决方案三：推理时切换 eval()，不影响 BN

model.eval()

out = bn2d(x)    # 推理模式下 batch=1 完全正常
```

### 错误四：Dropout 导致 BN 的方差偏移

## 问题

```python
# 问题：Dropout 在训练时改变激活值的方差

# 推理时 Dropout 关闭，BN 用训练时的 running_var（含 Dropout 影响）

# 统计量不匹配，推理结果有偏差

nn.Sequential(

    nn.Conv2d(64, 128, 3),

    nn.Dropout2d(0.5),        # ← 在卷积层用 Dropout

    nn.BatchNorm2d(128),      # ← BN 看到的方差被 Dropout 改变了

)
```

## 解决方案

```python
# 方案一：BN 在前，Dropout 在后

nn.Sequential(

    nn.Conv2d(64, 128, 3),

    nn.BatchNorm2d(128),      # 先 BN（不受 Dropout 影响）

    nn.ReLU(),

    nn.Dropout2d(0.1),        # 后 Dropout

)

# 方案二：卷积层只用 BN，全连接层只用 Dropout（最推荐）
```

### 错误五：在冻结的 BN 层忘记改为 eval 模式

## 错误写法

```python
# 迁移学习中，冻结主干时，预训练 BN 的 running stats 不应被更新

# 否则新数据分布会污染预训练的统计量

# 错误：冻结参数，但 BN 的 running_mean/var 仍在更新

model = models.resnet50(weights='IMAGENET1K_V2')

for param in model.parameters():

    param.requires_grad = False   # 仅冻结可学习参数，BN 统计量仍更新
```

## 正确写法

```python
# 正确方案：将主干的 BN 层也切换为 eval 模式

def freeze_bn(model):

    for module in model.modules():

        if isinstance(module, (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)):

            module.eval()              # 固定 running_mean/var

            for param in module.parameters():

                param.requires_grad = False

model = models.resnet50(weights='IMAGENET1K_V2')

freeze_bn(model)          # 冻结所有 BN

model.fc = nn.Linear(model.fc.in_features, 10)  # 只有新 FC 层可训练
```

### 快速诊断清单

| 现象 | 可能原因 | 检查项 |
| --- | --- | --- |
| 验证 loss 忽高忽低 | 忘记 model.eval() | 确认评估前调用 eval() |
| 训练/验证 acc 差距极大 | Dropout p 过大 | 尝试减小 p 或去掉 Dropout |
| 训练 NaN/inf | batch=1 用了 BatchNorm | 换 GroupNorm 或 LayerNorm |
| 迁移学习效果差 | BN running stats 被污染 | 主干 BN 层调用 eval() |
| 模型推理结果不稳定 | 推理时没切 eval() | 推理前必须 model.eval() |
| Conv 参数量偏多 | Conv+BN 未关 bias | 设置 bias=False |

---

-

# PyTorch LSTM / GRU

循环神经网络（RNN）在处理序列数据时面临梯度消失问题，导致难以学习长距离依赖关系。

长短期记忆网络（Long Short-Term Memory，LSTM）和门控循环单元（Gated Recurrent Unit，GRU）通过引入门控机制解决了这一问题，是处理时间序列、自然语言、语音等序列任务的核心模型。

## 1. RNN 的局限与门控机制

标准 RNN 在每个时间步将当前输入与上一步的隐藏状态合并计算新的隐藏状态：

\[h_t = \tanh(W_h \cdot h_{t-1} + W_x \cdot x_t + b)\]

这一结构存在两个核心问题：

梯度消失：反向传播时梯度需要逐步乘以权重矩阵，序列较长时梯度指数级衰减，导致早期时间步的参数几乎不更新，模型无法学习长距离依赖。

梯度爆炸：当权重矩阵的最大特征值大于 1 时，梯度反向传播过程中指数级增大，训练不稳定（通常用梯度裁剪缓解）。

门控机制的核心思想是引入可学习的"开关"，让网络自主决定：在当前时间步，哪些信息应该被记住，哪些应该被遗忘，哪些新信息应该写入记忆。

LSTM 使用三个门（遗忘门、输入门、输出门）加上一个单独的细胞状态；GRU 将结构简化为两个门（重置门、更新门），参数更少，训练更快。

## 2. LSTM 原理

### 2.1 核心结构与三个门

LSTM 维护两个状态向量在时间步之间传递：

- 细胞状态（Cell State） \(c_t\)：长期记忆的载体，信息可以在其中几乎无损地流动

- 隐藏状态（Hidden State） \(h_t\)：短期记忆，也是当前时间步的输出

三个门均为 Sigmoid 激活的线性变换，输出值在 0~1 之间，起到"阀门"的作用：

```python
遗忘门（Forget Gate）：决定从细胞状态中丢弃哪些信息

输入门（Input Gate）：决定将哪些新信息写入细胞状态

输出门（Output Gate）：决定基于细胞状态输出什么
```

### 2.2 前向计算公式

\[
\begin{aligned}
\text{输入：} & x_t \text{（当前时间步输入）}, h_{t-1} \text{（上一步隐藏状态）}, c_{t-1} \text{（上一步细胞状态）} \\
\text{遗忘门：} & f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \\
\text{输入门：} & i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) \\
\text{候选值：} & \tilde{g}_t = \tanh(W_g \cdot [h_{t-1}, x_t] + b_g) \\
\text{输出门：} & o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) \\
\text{更新细胞状态：} & c_t = f_t \odot c_{t-1} + i_t \odot \tilde{g}_t \\
\text{更新隐藏状态：} & h_t = o_t \odot \tanh(c_t)
\end{aligned}
\]
其中 \(\odot\) 表示逐元素乘法（Hadamard 积），\(\sigma\) 表示 Sigmoid 函数。

计算逻辑解读：

- `f_t ⊙ c_{t-1}`：遗忘门决定保留多少历史记忆，接近 0 则遗忘，接近 1 则保留

- `i_t ⊙ g_t`：输入门决定写入多少新信息，`g_t` 是候选新内容

- `o_t ⊙ tanh(c_t)`：输出门决定从细胞状态中提取什么作为隐藏状态输出

## 3. GRU 原理

### 3.1 核心结构与两个门

GRU 将 LSTM 的遗忘门与输入门合并为更新门，并取消了独立的细胞状态，只保留隐藏状态，结构更加简洁。

```python
重置门（Reset Gate）：决定忽略多少历史状态来计算候选隐藏状态

更新门（Update Gate）：决定保留多少历史状态，写入多少新状态
```

### 3.2 前向计算公式

\[
\begin{aligned}
\text{输入：} & x_t \text{（当前时间步输入）}, h_{t-1} \text{（上一步隐藏状态）} \\
\text{重置门：} & r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r) \\
\text{更新门：} & z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z) \\
\text{候选值：} & \tilde{h}_t = \tanh(W_h \cdot [r_t \odot h_{t-1}, x_t] + b_h) \\
\text{更新隐藏状态：} & h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
\end{aligned}
\]

计算逻辑解读：

- 重置门 `r_t` 接近 0 时，候选状态 `h̃_t` 几乎不依赖历史，相当于重新开始

- 更新门 `z_t` 接近 1 时，新状态更多采用候选值；接近 0 时，更多保留历史状态

- GRU 没有独立的细胞状态，参数量约为 LSTM 的 75%

## 4. PyTorch 中的 LSTM

本节详细介绍 nn.LSTM 的参数、输入输出形状以及隐藏状态初始化方法。

### 4.1 nn.LSTM 参数详解

## 实例

```python
import torch

import torch.nn as nn

lstm = nn.LSTM(

    input_size=64,       # 每个时间步输入向量的维度

    hidden_size=128,     # 隐藏状态（以及细胞状态）的维度

    num_layers=2,        # 堆叠层数，默认为 1

    bias=True,           # 是否使用偏置项，默认 True

    batch_first=False,   # 输入/输出 shape 中 batch 是否在第一维，默认 False

    dropout=0.0,         # 层间 dropout 概率（仅在 num_layers > 1 时生效）

    bidirectional=False, # 是否使用双向 LSTM，默认 False

    proj_size=0,         # 投影层维度（LSTM with projection），默认 0 表示不使用

)

# 查看参数量

total_params = sum(p.numel() for p in lstm.parameters())

print(f"LSTM 参数量: {total_params:,}")

# input_size=64, hidden_size=128, num_layers=2 时约为 197,632
```

参数量估算公式（单层单向）：

\[
\begin{aligned}
\text{每层参数量} & = 4 \times (hidden\_size \times input\_size + hidden\_size \times hidden\_size + hidden\_size) \\
                  & = 4 \times hidden\_size \times (input\_size + hidden\_size + 1)
\end{aligned}
\]
其中 4 对应四组权重矩阵：遗忘门、输入门、候选值、输出门。

### 4.2 输入与输出的形状

这是使用 LSTM 最容易出错的部分，需要特别注意 `batch_first` 参数的影响。

## 实例

```python
import torch

import torch.nn as nn

# ── batch_first=False（默认）────────────────────────

lstm = nn.LSTM(input_size=32, hidden_size=64, batch_first=False)

# 输入形状：(seq_len, batch_size, input_size)

seq_len, batch_size, input_size = 10, 4, 32

x = torch.randn(seq_len, batch_size, input_size)

output, (h_n, c_n) = lstm(x)

print(f"output 形状: {output.shape}")

# torch.Size([10, 4, 64])   → (seq_len, batch_size, hidden_size)

# 每个时间步的隐藏状态输出

print(f"h_n 形状: {h_n.shape}")

# torch.Size([1, 4, 64])    → (num_layers * num_directions, batch_size, hidden_size)

# 最后一个时间步的隐藏状态

print(f"c_n 形状: {c_n.shape}")

# torch.Size([1, 4, 64])    → 同 h_n，最后一个时间步的细胞状态

# ── batch_first=True（推荐，更直观）────────────────

lstm_bf = nn.LSTM(input_size=32, hidden_size=64, batch_first=True)

# 输入形状：(batch_size, seq_len, input_size)

x = torch.randn(batch_size, seq_len, input_size)

output, (h_n, c_n) = lstm_bf(x)

print(f"output 形状: {output.shape}")

# torch.Size([4, 10, 64])   → (batch_size, seq_len, hidden_size)

print(f"h_n 形状: {h_n.shape}")

# torch.Size([1, 4, 64])    → (num_layers, batch_size, hidden_size)

# 注意：h_n 的形状不受 batch_first 影响

# ── 多层双向 LSTM 的输出形状 ──────────────────────

lstm_bd = nn.LSTM(input_size=32, hidden_size=64,

                   num_layers=3, bidirectional=True, batch_first=True)

x = torch.randn(batch_size, seq_len, input_size)

output, (h_n, c_n) = lstm_bd(x)

print(f"output 形状: {output.shape}")

# torch.Size([4, 10, 128])

# hidden_size × 2 = 128，因为双向拼接

print(f"h_n 形状: {h_n.shape}")

# torch.Size([6, 4, 64])

# num_layers × num_directions = 3 × 2 = 6
```

输出形状总结：

| 变量 | batch_first=False | batch_first=True |
| --- | --- | --- |
| output | (seq_len, N, H * D) | (N, seq_len, H * D) |
| h_n | (L * D, N, H) | (L * D, N, H) |
| c_n | (L * D, N, H) | (L * D, N, H) |

\(N\) = batch_size，\(H\) = hidden_size，\(L\) = num_layers，\(D\) = 2（双向）或 1（单向）

### 4.3 隐藏状态的初始化

## 实例

```python
import torch

import torch.nn as nn

lstm = nn.LSTM(input_size=32, hidden_size=64, num_layers=2, batch_first=True)

batch_size = 8

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

lstm = lstm.to(device)

# 方式一：不传入初始状态，PyTorch 自动使用全零初始化

x = torch.randn(batch_size, 10, 32).to(device)

output, (h_n, c_n) = lstm(x)

# 方式二：手动初始化为全零（与方式一等价，但明确显示意图）

num_layers, num_directions = 2, 1

h_0 = torch.zeros(num_layers * num_directions, batch_size, 64).to(device)

c_0 = torch.zeros(num_layers * num_directions, batch_size, 64).to(device)

output, (h_n, c_n) = lstm(x, (h_0, c_0))

# 方式三：有状态（stateful）模式 —— 跨 batch 传递状态

# 适用于超长序列切片（语言模型、长文本生成等）

# 需要调用 detach() 切断与前一 batch 的计算图，防止显存泄漏

h, c = h_0, c_0

for batch_x in data_loader:

    batch_x = batch_x.to(device)

    output, (h, c) = lstm(batch_x, (h, c))

    h = h.detach()    # 切断梯度，只保留数值

    c = c.detach()

# 方式四：使用 Xavier 或正态分布初始化（某些场景收敛更快）

def init_hidden(lstm_module, batch_size, device):

    num_layers = lstm_module.num_layers

    hidden_size = lstm_module.hidden_size

    directions = 2 if lstm_module.bidirectional else 1

    h = torch.zeros(num_layers * directions, batch_size, hidden_size, device=device)

    c = torch.zeros(num_layers * directions, batch_size, hidden_size, device=device)

    nn.init.orthogonal_(h)   # 正交初始化，有助于稳定训练

    return h, c
```

## 5. PyTorch 中的 GRU

GRU 的接口与 LSTM 几乎完全相同，主要区别是没有细胞状态 `c`。

### 5.1 nn.GRU 参数详解

## 实例

```python
import torch.nn as nn

gru = nn.GRU(

    input_size=64,

    hidden_size=128,

    num_layers=2,

    bias=True,

    batch_first=True,    # 推荐设为 True

    dropout=0.3,         # 层间 dropout

    bidirectional=False,

)
```

### 5.2 基本使用示例

## 实例

```python
import torch

import torch.nn as nn

gru = nn.GRU(input_size=32, hidden_size=64, batch_first=True)

batch_size, seq_len = 8, 10

x = torch.randn(batch_size, seq_len, 32)

# GRU 只返回 output 和 h_n，没有 c_n

output, h_n = gru(x)

print(f"output 形状: {output.shape}")

# torch.Size([8, 10, 64])   → (batch_size, seq_len, hidden_size)

print(f"h_n 形状: {h_n.shape}")

# torch.Size([1, 8, 64])    → (num_layers, batch_size, hidden_size)

# 取最后一个时间步的输出（用于分类等任务）

last_hidden = output[:, -1, :]    # (batch_size, hidden_size)

# 或等价地：

last_hidden = h_n.squeeze(0)      # (batch_size, hidden_size)
```

## 6. LSTM 与 GRU 的变体

本节介绍双向、多层堆叠以及带 Dropout 的多层结构。

### 6.1 双向 LSTM / GRU

双向模型同时从序列的正向和反向处理信息，每个时间步的输出包含过去和未来的上下文，适合文本分类、命名实体识别等需要全局上下文的任务。

## 实例

```python
import torch

import torch.nn as nn

# 双向 LSTM

bilstm = nn.LSTM(

    input_size=32,

    hidden_size=64,

    num_layers=2,

    batch_first=True,

    bidirectional=True,    # 开启双向

)

x = torch.randn(8, 10, 32)

output, (h_n, c_n) = bilstm(x)

print(f"output 形状: {output.shape}")

# torch.Size([8, 10, 128])

# 正向 64 维 + 反向 64 维 = 128 维

print(f"h_n 形状: {h_n.shape}")

# torch.Size([4, 8, 64])

# num_layers(2) × num_directions(2) = 4

# 分离正向和反向的最后隐藏状态

# h_n 的排列顺序：[正向layer0, 反向layer0, 正向layer1, 反向layer1]

h_forward  = h_n[-2, :, :]    # (batch_size, hidden_size) 正向最后一层

h_backward = h_n[-1, :, :]    # (batch_size, hidden_size) 反向最后一层

h_combined = torch.cat([h_forward, h_backward], dim=-1)  # (batch_size, 128)

# 双向 GRU 用法完全相同

bigru = nn.GRU(input_size=32, hidden_size=64,

                num_layers=2, batch_first=True, bidirectional=True)

output, h_n = bigru(x)
```

### 6.2 多层堆叠

## 实例

```python
import torch

import torch.nn as nn

# 3 层堆叠 LSTM

deep_lstm = nn.LSTM(

    input_size=32,

    hidden_size=128,

    num_layers=3,          # 堆叠 3 层

    batch_first=True,

)

x = torch.randn(8, 20, 32)

output, (h_n, c_n) = deep_lstm(x)

print(f"output 形状: {output.shape}")

# torch.Size([8, 20, 128])  只包含最顶层的输出

print(f"h_n 形状: {h_n.shape}")

# torch.Size([3, 8, 128])   包含每一层的最终隐藏状态

# 获取各层的最终隐藏状态

h_layer1 = h_n[0]    # (batch_size, hidden_size) 第一层

h_layer2 = h_n[1]    # (batch_size, hidden_size) 第二层

h_layer3 = h_n[2]    # (batch_size, hidden_size) 第三层（最顶层）
```

### 6.3 带 Dropout 的多层结构

`nn.LSTM` 内置的 `dropout` 参数只作用于层与层之间，不作用于最后一层的输出。如需在最后一层后也加 Dropout，需要手动添加：

## 实例

```python
import torch

import torch.nn as nn

class StackedLSTM(nn.Module):

    """

    多层 LSTM + 层间 Dropout + 输出 Dropout

    """

    def __init__(self, input_size, hidden_size, num_layers,

                 num_classes, dropout=0.3):

        super().__init__()

        self.lstm = nn.LSTM(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout if num_layers > 1 else 0.0,

            # num_layers=1 时 dropout 无效，设为 0 避免警告

        )

        self.dropout = nn.Dropout(dropout)    # 最后一层后的 Dropout

        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):

        output, (h_n, c_n) = self.lstm(x)

        # 取最后一个时间步的隐藏状态

        last_output = output[:, -1, :]        # (batch_size, hidden_size)

        last_output = self.dropout(last_output)

        return self.fc(last_output)

model = StackedLSTM(input_size=64, hidden_size=128,

                     num_layers=3, num_classes=5, dropout=0.3)

x = torch.randn(16, 20, 64)

print(model(x).shape)   # torch.Size([16, 5])
```

## 7. 处理变长序列

实际任务中，同一 batch 内的序列长度通常不同。PyTorch 提供了 `pack_padded_sequence` 和 `pad_packed_sequence` 处理这一问题，避免 LSTM 在填充位置（padding）上做无效计算。

### 7.1 pack_padded_sequence

## 实例

```python
import torch

import torch.nn as nn

from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, pad_sequence

# 模拟一个 batch 中的变长序列（已排序，从长到短）

seq1 = torch.randn(5, 32)    # 序列长度 5

seq2 = torch.randn(3, 32)    # 序列长度 3

seq3 = torch.randn(2, 32)    # 序列长度 2

# pad_sequence 自动补零，对齐到最长序列

# batch_first=True 时输出形状为 (batch_size, max_seq_len, input_size)

padded = pad_sequence([seq1, seq2, seq3], batch_first=True, padding_value=0.0)

lengths = torch.tensor([5, 3, 2])

print(f"补零后形状: {padded.shape}")   # torch.Size([3, 5, 32])

# pack_padded_sequence：压缩填充，告诉 LSTM 真实长度

packed = pack_padded_sequence(

    padded,

    lengths=lengths,

    batch_first=True,

    enforce_sorted=True,    # 序列必须按长度降序排列

    # enforce_sorted=False  # 允许任意顺序（内部自动排序），推荐设为 False

)

print(type(packed))         # <class 'torch.nn.utils.rnn.PackedSequence'>
```

### 7.2 pad_packed_sequence

## 实例

```python
lstm = nn.LSTM(input_size=32, hidden_size=64, batch_first=True)

# 将 PackedSequence 传入 LSTM

packed_output, (h_n, c_n) = lstm(packed)

# pad_packed_sequence：还原为补零张量

output, output_lengths = pad_packed_sequence(packed_output, batch_first=True)

print(f"还原后 output 形状: {output.shape}")

# torch.Size([3, 5, 64])    → (batch_size, max_seq_len, hidden_size)

# 补零位置的输出为 0

print(f"各序列实际长度: {output_lengths}")

# tensor([5, 3, 2])
```

### 7.3 完整变长序列处理流程

## 实例

```python
import torch

import torch.nn as nn

from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

class LSTMClassifier(nn.Module):

    def __init__(self, vocab_size, embed_dim, hidden_size, num_classes, padding_idx=0):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=padding_idx)

        self.lstm      = nn.LSTM(embed_dim, hidden_size, batch_first=True)

        self.fc        = nn.Linear(hidden_size, num_classes)

    def forward(self, x, lengths):

        # x: (batch_size, max_seq_len) — 词索引

        embedded = self.embedding(x)   # (batch_size, max_seq_len, embed_dim)

        # 打包

        packed = pack_padded_sequence(

            embedded, lengths.cpu(), batch_first=True, enforce_sorted=False

        )

        # LSTM 前向传播（跳过填充位置）

        packed_output, (h_n, c_n) = self.lstm(packed)

        # 方式一：使用最后一层的 h_n 作为序列表示

        last_hidden = h_n.squeeze(0)    # (batch_size, hidden_size)

        # 方式二：解包后取每个序列真实最后位置的输出（与方式一等价）

        # output, _ = pad_packed_sequence(packed_output, batch_first=True)

        # last_hidden = output[range(len(lengths)), lengths - 1, :]

        return self.fc(last_hidden)

model = LSTMClassifier(vocab_size=10000, embed_dim=128,

                        hidden_size=256, num_classes=5)

# 模拟一个 batch

batch_tokens  = torch.randint(1, 10000, (8, 30))   # (batch_size=8, max_len=30)

batch_lengths = torch.randint(5, 31, (8,))          # 每条序列的真实长度

output = model(batch_tokens, batch_lengths)

print(output.shape)   # torch.Size([8, 5])
```

## 8. 完整实战：文本情感分类

以 IMDB 影评情感二分类为例，展示双向 LSTM 处理文本的完整流程：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.utils.data import Dataset, DataLoader

from torch.nn.utils.rnn import pack_padded_sequence, pad_sequence

from torch.optim.lr_scheduler import ReduceLROnPlateau

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── 模型定义 ──────────────────────────────────────

class BiLSTMClassifier(nn.Module):

    """

    双向 LSTM 文本分类模型

    结构：Embedding -> BiLSTM -> Dropout -> FC

    """

    def __init__(self, vocab_size, embed_dim, hidden_size,

                 num_layers, num_classes, dropout=0.5, padding_idx=0):

        super().__init__()

        self.embedding = nn.Embedding(

            vocab_size, embed_dim, padding_idx=padding_idx

        )

        # 使用预训练词向量时：

        # self.embedding = nn.Embedding.from_pretrained(pretrained_vectors)

        self.lstm = nn.LSTM(

            input_size=embed_dim,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout if num_layers > 1 else 0.0,

            bidirectional=True,

        )

        self.dropout = nn.Dropout(dropout)

        # 双向 LSTM：拼接正向和反向最后隐藏状态

        self.fc = nn.Linear(hidden_size * 2, num_classes)

    def forward(self, x, lengths):

        # x: (batch_size, max_seq_len)

        embedded = self.dropout(self.embedding(x))

        packed = pack_padded_sequence(

            embedded, lengths.cpu(), batch_first=True, enforce_sorted=False

        )

        packed_output, (h_n, c_n) = self.lstm(packed)

        # h_n: (num_layers * 2, batch_size, hidden_size)

        # 取最后一层的正向和反向隐藏状态并拼接

        h_forward  = h_n[-2, :, :]    # (batch_size, hidden_size)

        h_backward = h_n[-1, :, :]    # (batch_size, hidden_size)

        h_combined = torch.cat([h_forward, h_backward], dim=-1)

        # (batch_size, hidden_size * 2)

        out = self.dropout(h_combined)

        return self.fc(out)

# ── 自定义 Dataset ────────────────────────────────

class TextDataset(Dataset):

    def __init__(self, texts, labels, vocab, max_len=200):

        self.data   = texts

        self.labels = labels

        self.vocab  = vocab

        self.max_len = max_len

    def __len__(self):

        return len(self.data)

    def __getitem__(self, idx):

        tokens = self.data[idx][:self.max_len]

        ids    = [self.vocab.get(t, 1) for t in tokens]  # 1 = <UNK>

        return torch.tensor(ids, dtype=torch.long), torch.tensor(self.labels[idx])

def collate_fn(batch):

    """自定义 collate：对变长序列补零，记录真实长度"""

    sequences, labels = zip(*batch)

    lengths = torch.tensor([len(s) for s in sequences])

    padded  = pad_sequence(sequences, batch_first=True, padding_value=0)

    labels  = torch.stack(labels)

    return padded, lengths, labels

# ── 训练与评估函数 ────────────────────────────────

def train_epoch(model, loader, optimizer, criterion):

    model.train()

    total_loss, correct = 0.0, 0

    for texts, lengths, labels in loader:

        texts, labels = texts.to(device), labels.to(device)

        optimizer.zero_grad()

        outputs = model(texts, lengths)

        loss    = criterion(outputs, labels)

        loss.backward()

        # 梯度裁剪：防止 RNN 的梯度爆炸

        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()

        total_loss += loss.item() * len(labels)

        correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

def eval_epoch(model, loader, criterion):

    model.eval()

    total_loss, correct = 0.0, 0

    with torch.no_grad():

        for texts, lengths, labels in loader:

            texts, labels = texts.to(device), labels.to(device)

            outputs = model(texts, lengths)

            loss    = criterion(outputs, labels)

            total_loss += loss.item() * len(labels)

            correct    += (outputs.argmax(1) == labels).sum().item()

    n = len(loader.dataset)

    return total_loss / n, correct / n

# ── 初始化与训练 ──────────────────────────────────

VOCAB_SIZE  = 50000

EMBED_DIM   = 128

HIDDEN_SIZE = 256

NUM_LAYERS  = 2

NUM_CLASSES = 2

DROPOUT     = 0.5

EPOCHS      = 15

model     = BiLSTMClassifier(VOCAB_SIZE, EMBED_DIM, HIDDEN_SIZE,

                              NUM_LAYERS, NUM_CLASSES, DROPOUT).to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

scheduler = ReduceLROnPlateau(optimizer, mode="max",

                               patience=3, factor=0.5)

best_acc = 0.0

for epoch in range(1, EPOCHS + 1):

    train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion)

    val_loss,   val_acc   = eval_epoch(model,  val_loader,   criterion)

    scheduler.step(val_acc)

    print(f"Epoch {epoch:2d}/{EPOCHS} | "

          f"Train Loss: {train_loss:.4f}, Acc: {train_acc:.4f} | "

          f"Val Loss: {val_loss:.4f}, Acc: {val_acc:.4f}")

    if val_acc > best_acc:

        best_acc = val_acc

        torch.save(model.state_dict(), "best_bilstm.pth")

        print(f"  -> 保存最优模型，Val Acc: {best_acc:.4f}")
```

## 9. 完整实战：时间序列预测

以多步时间序列预测为例，使用 LSTM 预测未来 N 步的数值：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import numpy as np

from torch.utils.data import Dataset, DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── 滑动窗口 Dataset ──────────────────────────────

class TimeSeriesDataset(Dataset):

    """

    滑动窗口切割时间序列

    输入：过去 input_len 步

    目标：未来 output_len 步

    """

    def __init__(self, series, input_len, output_len):

        self.data       = torch.tensor(series, dtype=torch.float32)

        self.input_len  = input_len

        self.output_len = output_len

    def __len__(self):

        return len(self.data) - self.input_len - self.output_len + 1

    def __getitem__(self, idx):

        x = self.data[idx : idx + self.input_len]

        y = self.data[idx + self.input_len : idx + self.input_len + self.output_len]

        return x.unsqueeze(-1), y   # x: (input_len, 1), y: (output_len,)

# ── 模型定义 ──────────────────────────────────────

class LSTMForecaster(nn.Module):

    """

    多步时间序列预测模型

    结构：LSTM -> Dropout -> FC

    """

    def __init__(self, input_size, hidden_size, num_layers,

                 output_len, dropout=0.2):

        super().__init__()

        self.lstm = nn.LSTM(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout if num_layers > 1 else 0.0,

        )

        self.dropout = nn.Dropout(dropout)

        self.fc      = nn.Linear(hidden_size, output_len)

    def forward(self, x):

        # x: (batch_size, input_len, input_size)

        output, (h_n, c_n) = self.lstm(x)

        # 取最后一个时间步的输出

        last = output[:, -1, :]            # (batch_size, hidden_size)

        last = self.dropout(last)

        return self.fc(last)               # (batch_size, output_len)

# ── 数据准备（以正弦波为例）──────────────────────

t      = np.linspace(0, 200, 10000)

series = np.sin(t) + 0.1 * np.random.randn(len(t))

INPUT_LEN  = 60     # 使用过去 60 步

OUTPUT_LEN = 10     # 预测未来 10 步

split      = int(len(series) * 0.8)

train_data = series[:split]

val_data   = series[split:]

train_dataset = TimeSeriesDataset(train_data, INPUT_LEN, OUTPUT_LEN)

val_dataset   = TimeSeriesDataset(val_data,   INPUT_LEN, OUTPUT_LEN)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

val_loader   = DataLoader(val_dataset,   batch_size=64, shuffle=False)

# ── 训练 ──────────────────────────────────────────

model     = LSTMForecaster(input_size=1, hidden_size=128,

                            num_layers=2, output_len=OUTPUT_LEN).to(device)

criterion = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

def train_epoch_ts(model, loader, optimizer, criterion):

    model.train()

    total_loss = 0.0

    for x, y in loader:

        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()

        pred = model(x)

        loss = criterion(pred, y)

        loss.backward()

        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()

        total_loss += loss.item() * x.size(0)

    return total_loss / len(loader.dataset)

def eval_epoch_ts(model, loader, criterion):

    model.eval()

    total_loss = 0.0

    with torch.no_grad():

        for x, y in loader:

            x, y = x.to(device), y.to(device)

            pred = model(x)

            total_loss += criterion(pred, y).item() * x.size(0)

    return total_loss / len(loader.dataset)

for epoch in range(1, 31):

    train_loss = train_epoch_ts(model, train_loader, optimizer, criterion)

    val_loss   = eval_epoch_ts(model,  val_loader,   criterion)

    print(f"Epoch {epoch:2d}/30 | Train MSE: {train_loss:.6f} | Val MSE: {val_loss:.6f}")

# ── 多步递归预测（另一种策略）────────────────────

def recursive_forecast(model, init_sequence, steps, device):

    """

    递归预测：每次预测一步，将预测值追加到序列中再预测下一步

    适合 output_len=1 的单步预测模型

    """

    model.eval()

    sequence = list(init_sequence)

    predictions = []

    with torch.inference_mode():

        for _ in range(steps):

            x = torch.tensor(sequence[-INPUT_LEN:], dtype=torch.float32)

            x = x.unsqueeze(0).unsqueeze(-1).to(device)   # (1, input_len, 1)

            pred = model(x).item()

            predictions.append(pred)

            sequence.append(pred)

    return predictions
```

## 10. LSTM 与 GRU 对比及选型

本节对比 LSTM 和 GRU 的结构差异，并提供选型建议。

### 结构对比

| 对比项 | LSTM | GRU |
| --- | --- | --- |
| 门的数量 | 3（遗忘、输入、输出） | 2（重置、更新） |
| 状态向量 | 细胞状态 + 隐藏状态 | 只有隐藏状态 |
| 参数量（相同 hidden_size） | 基准 | 约 75% |
| 训练速度 | 较慢 | 较快 |
| 长序列表现 | 通常更好 | 接近 |
| 短序列表现 | 相近 | 相近 |
| 实现复杂度 | 较高 | 较低 |

### 选型建议

```python
数据量小、训练资源有限

-> 优先选 GRU，参数少，不容易过拟合，训练快

序列较长（> 100 步）、长距离依赖重要

-> 优先选 LSTM，细胞状态更擅长保留远期信息

需要快速实验和基线对比

-> 先用 GRU，效果差再换 LSTM

任务对准确率要求极高，有充足数据

-> 两者都试，结合交叉验证选择

2020 年后的新项目

-> 考虑 Transformer 架构（BERT、GPT），在大数据量下通常优于 LSTM/GRU

LSTM/GRU 仍在边缘设备、低延迟推理、数据量较小的场景中有优势
```

### 常见问题速查

| 问题 | 原因 | 解决方法 |
| --- | --- | --- |
| 训练 Loss 不下降 | 学习率过大或梯度爆炸 | 降低学习率；添加梯度裁剪 clip_grad_norm_ |
| 验证集 Loss 远高于训练集 | 过拟合 | 增大 Dropout；减少层数或 hidden_size |
| 序列尾部预测差 | 梯度消失 | 增加层数；使用双向结构；考虑注意力机制 |
| 显存占用过大 | 序列过长或 batch 过大 | 减小 seq_len 或 batch_size；使用梯度检查点 |
| 有状态训练中 Loss 异常 | 跨 batch 传递状态未 detach | 每个 batch 后调用 h.detach_() |
| 双向 LSTM 拼接维度错误 | h_n 索引理解错误 | 用 h_n[-2]（正向）和 h_n[-1]（反向） |
| PackedSequence 报错 | 序列长度未降序排列 | 设置 enforce_sorted=False |
| batch_first 混淆 | 忘记统一设置 | 推荐全程使用 batch_first=True |

---

-

# PyTorch 词嵌入 (Embedding)

词嵌入是自然语言处理中最基础也是最重要的技术之一。

词嵌入将离散的词符号映射为连续的稠密向量，使机器能够理解和处理文本数据。

PyTorch 提供了 `nn.Embedding` 模块来实现这一功能，是构建各种 NLP 模型的基础。

## 1. 词嵌入基础概念

在计算机中，文本本质上是一串整数序列。每个词被分配一个唯一的索引 ID，但这种离散表示存在一个问题：相似的词在语义上可能很接近，但它们的 ID 却毫无关联。

词嵌入通过学习一个嵌入矩阵来解决这个问题：

\[
E \in \mathbb{R}^{V \times D}
\]

其中 \(V\) 是词表大小，\(D\) 是嵌入维度。每个词 ID 对应嵌入矩阵中的一行，通过查表操作获取其向量表示：

\[
\text{embedding} = E[\text{word\_id}]
\]

词嵌入的优势包括：

- 将高维稀疏的 one-hot 向量转换为低维稠密向量，大幅降低计算开销

- 语义相似的词在向量空间中距离更近，可通过余弦相似度计算词相似度

- 嵌入向量是可学习的参数，可以通过反向传播自动调整

## 2. nn.Embedding 详解

`nn.Embedding` 是 PyTorch 提供的词嵌入层，封装了嵌入矩阵的创建和查表操作。

### 2.1 基本用法

## 实例

```python
import torch

import torch.nn as nn

# 创建词嵌入层

# num_embeddings: 词表大小（vocab_size）

# embedding_dim: 嵌入维度（embedding_dim）

vocab_size = 10000

embedding_dim = 256

embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)

# 查看嵌入矩阵的形状

print(embedding.weight.shape)   # torch.Size([10000, 256])

# 输入词索引（LongTensor），获取嵌入向量

word_ids = torch.tensor([0, 1, 2, 9999])  # 任意词索引

embedded = embedding(word_ids)

print(embedded.shape)           # torch.Size([4, 256])

# 每个词ID对应一个256维的向量
```

### 2.2 nn.Embedding 参数详解

## 实例

```python
import torch.nn as nn

embedding = nn.Embedding(

    num_embeddings=10000,    # 词表大小，必须大于等于输入的最大索引值

    embedding_dim=256,       # 嵌入向量维度，通常为 50, 100, 200, 300 等

    padding_idx=None,        # 填充词的索引，填充词的嵌入向量全为零

    max_norm=None,          # 嵌入向量的最大范数，用于归一化

    norm_type=2.0,          # 归一化类型，通常为 L2 范数

    scale_grad_by_freq=False,# 按词频缩放梯度

    sparse=False,           # 是否使用稀疏梯度（节省显存，但训练较慢）

    _weight=None,           # 预定义权重，用于加载预训练嵌入

)

# 查看参数量

total_params = embedding.num_embeddings * embedding.embedding_dim

print(f"嵌入层参数量: {total_params:,}")

# 10000 * 256 = 2,560,000
```

嵌入层的参数量 = 词表大小 × 嵌入维度，这是一个非常大的矩阵。通常 NLP 模型的嵌入层占模型总参数量的很大比例。

### 2.3 填充索引 padding_idx

在处理变长序列时，需要对短序列进行填充。使用 `padding_idx` 可以将填充词的嵌入向量固定为零向量，避免填充内容对模型产生影响：

## 实例

```python
import torch

import torch.nn as nn

# 设置 padding_idx=0，表示索引0为填充词

embedding = nn.Embedding(num_embeddings=10000, embedding_dim=128, padding_idx=0)

# 初始化权重

nn.init.uniform_(embedding.weight, -0.1, 0.1)

# 索引0的嵌入向量全为0

word_0 = embedding(torch.tensor([0]))

print(f"填充词的嵌入: {word_0}")   # 全为0

# 其他索引正常

word_5 = embedding(torch.tensor([5]))

print(f"词5的嵌入: {word_5}")     # 非零值
```

### 2.4 最大范数归一化

使用 `max_norm` 可以限制嵌入向量的范数，防止训练过程中嵌入向量过大：

## 实例

```python
import torch

import torch.nn as nn

# 设置最大范数为1.0

embedding = nn.Embedding(num_embeddings=1000, embedding_dim=64, max_norm=1.0)

# 输入任意词索引

ids = torch.tensor([1, 2, 3])

embedded = embedding(ids)

# 检查每个向量的L2范数

norms = torch.norm(embedded, p=2, dim=1)

print(f"各向量范数: {norms}")   # 所有值都接近1.0
```

## 3. 加载预训练词嵌入

使用预训练词嵌入可以大幅提升模型性能，尤其是当训练数据较少时。常见的预训练词嵌入包括 Word2Vec、GloVe、FastText 等。

### 3.1 从头训练与加载预训练的区别

| 方式 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| 随机初始化训练 | 完全可定制，适应特定任务 | 需要大量训练数据 | 领域特定词汇多、训练数据充足 |
| 加载预训练嵌入 | 利用大规模语料知识，训练快、效果好 | 词汇覆盖受限，无法处理未登录词 | 通用任务、训练数据有限 |
| 冻结预训练嵌入 | 训练速度快，显存占用小 | 无法微调嵌入 | 训练资源有限、只关注上层模型 |
| 微调预训练嵌入 | 可适应特定任务 | 训练较慢，显存占用大 | 数据量中等、领域有一定差异 |

### 3.2 加载 GloVe 预训练词向量

GloVe 是 Stanford 大学发布的预训练词向量，下面展示如何加载：

## 实例

```python
import torch

import torch.nn as nn

import numpy as np

# 模拟加载 GloVe 词向量（实际需要下载 GloVe 文件）

# 假设已有一个词向量文件，格式为：每行一个词 followed by its vectors

def load_glove_embeddings(path, word2idx, embedding_dim=300):

    """

    加载 GloVe 预训练词向量

    path: 词向量文件路径

    word2idx: 词到索引的映射字典

    embedding_dim: 词向量维度

    """

    embeddings = np.random.randn(len(word2idx), embedding_dim).astype(np.float32)

    word_count = 0

    with open(path, 'r', encoding='utf-8') as f:

        for line in f:

            values = line.strip().split()

            word = values[0]

            if word in word2idx:

                word_idx = word2idx[word]

                embeddings[word_idx] = np.asarray(values[1:], dtype=np.float32)

                word_count += 1

    print(f"已加载 {word_count}/{len(word2idx)} 个词向量")

    return torch.from_numpy(embeddings)

# 假设已有词表

word2idx = {'hello': 0, 'world': 1, 'runoob': 2, 'python': 3}

EMBED_DIM = 300

# 加载预训练嵌入并创建嵌入层

# pretrained_embeddings = load_glove_embeddings('glove.6B.300d.txt', word2idx, EMBED_DIM)

# embedding = nn.Embedding.from_pretrained(pretrained_embeddings, padding_idx=0)

# 简化示例：使用随机初始化的预训练矩阵

pretrained_embeddings = torch.randn(len(word2idx), EMBED_DIM)

embedding = nn.Embedding.from_pretrained(pretrained_embeddings, padding_idx=0)

print(f"嵌入层形状: {embedding.weight.shape}")
```

### 3.3 冻结与微调嵌入层

根据任务需求，可以选择冻结或微调嵌入层：

## 实例

```python
import torch

import torch.nn as nn

embedding = nn.Embedding(num_embeddings=10000, embedding_dim=256)

# 方式一：冻结嵌入层（不参与训练）

embedding.weight.requires_grad = False

# 训练时只有 embedding.weight.requires_grad = False 的参数不会被更新

# 方式二：微调嵌入层（参与训练）

embedding.weight.requires_grad = True

# 方式三：冻结部分词向量（冻结"the", "is"等高频词）

# 假设高频词的索引在 0-99

embedding.weight.requires_grad = True

with torch.no_grad():

    embedding.weight[0:100] *= 0  # 或赋值为固定值

# 在优化器中过滤掉冻结的参数

optimizer = torch.optim.Adam(

    filter(lambda p: p.requires_grad, embedding.parameters()),

    lr=1e-3

)
```

## 4. 嵌入层与 RNN/LSTM 结合

词嵌入是 NLP 模型的第一层，将文本 ID 转换为密集向量后，传入 RNN、LSTM 等序列模型进行处理。

### 4.1 嵌入层 + LSTM 文本分类

## 实例

```python
import torch

import torch.nn as nn

class TextClassifier(nn.Module):

    """

    嵌入层 + LSTM 文本分类模型

    """

    def __init__(self, vocab_size, embed_dim, hidden_size, num_classes, padding_idx=0):

        super().__init__()

        # 词嵌入层

        self.embedding = nn.Embedding(

            num_embeddings=vocab_size,

            embedding_dim=embed_dim,

            padding_idx=padding_idx

        )

        # LSTM 层

        self.lstm = nn.LSTM(

            input_size=embed_dim,

            hidden_size=hidden_size,

            num_layers=2,

            batch_first=True,

            bidirectional=True,

            dropout=0.3

        )

        # 分类器

        self.fc = nn.Linear(hidden_size * 2, num_classes)

    def forward(self, x):

        # x: (batch_size, seq_len) - 词索引

        embedded = self.embedding(x)  # (batch_size, seq_len, embed_dim)

        # LSTM 输出

        output, (h_n, c_n) = self.lstm(embedded)

        # 取最后一个时间步的隐藏状态（双向拼接）

        # 正向最后隐藏状态: h_n[-2]

        # 反向最后隐藏状态: h_n[-1]

        h_combined = torch.cat([h_n[-2], h_n[-1]], dim=-1)

        # 分类

        logits = self.fc(h_combined)

        return logits

# 模型实例化

VOCAB_SIZE = 10000

EMBED_DIM = 128

HIDDEN_SIZE = 128

NUM_CLASSES = 2

model = TextClassifier(VOCAB_SIZE, EMBED_DIM, HIDDEN_SIZE, NUM_CLASSES)

# 模拟输入：batch_size=4, 序列长度=10

batch_input = torch.randint(1, VOCAB_SIZE, (4, 10))

output = model(batch_input)

print(f"输入形状: {batch_input.shape}")      # torch.Size([4, 10])

print(f"输出形状: {output.shape}")           # torch.Size([4, 2])
```

### 4.2 使用预训练词向量

## 实例

```python
import torch

import torch.nn as nn

# 假设已加载预训练词向量

pretrained_vectors = torch.randn(10000, 300)  # 模拟预训练向量

# 创建嵌入层并加载预训练权重

embedding = nn.Embedding.from_pretrained(

    pretrained_vectors,

    padding_idx=0,

    freeze=False  # True: 冻结不训练, False: 微调

)

# 使用 glove 或其他预训练词向量时，通常先冻结训练几轮，再解冻微调

# 前几轮只训练上层模型

embedding.weight.requires_grad = False

# 训练若干轮后，解冻嵌入层进行微调

# embedding.weight.requires_grad = True
```

## 5. 位置编码 (Positional Encoding)

与 RNN/LSTM 不同，Transformer 模型不包含位置信息，需要额外添加位置编码来让模型感知序列中词的顺序。

### 5.1 位置编码原理

位置编码使用正弦和余弦函数生成位置向量：

\[
\begin{aligned}
PE_{(pos, 2i)}   &= \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right) \\
PE_{(pos, 2i+1)} &= \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\end{aligned}
\]

这种编码方式的特点是：不同位置的编码可以通过线性变换相互转换，便于模型学习位置关系。

### 5.2 实现位置编码

## 实例

```python
import torch

import torch.nn as nn

import math

class PositionalEncoding(nn.Module):

    """

    位置编码层

    """

    def __init__(self, d_model, max_len=5000):

        super().__init__()

        # 创建位置编码矩阵

        pe = torch.zeros(max_len, d_model)

        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # 计算除数项

        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        # 偶数索引使用 sin，奇数索引使用 cos

        pe[:, 0::2] = torch.sin(position * div_term)

        pe[:, 1::2] = torch.cos(position * div_term)

        # 添加 batch 维度，并注册为不参与梯度计算的缓冲区

        pe = pe.unsqueeze(0)  # (1, max_len, d_model)

        self.register_buffer('pe', pe)

    def forward(self, x):

        """

        x: (batch_size, seq_len, d_model)

        """

        seq_len = x.size(1)

        # 截取对应长度的位置编码并相加

        x = x + self.pe[:, :seq_len, :]

        return x

# 使用示例

d_model = 256

max_len = 100

pos_encoding = PositionalEncoding(d_model, max_len)

# 模拟输入：batch_size=4, seq_len=20, d_model=256

x = torch.randn(4, 20, d_model)

x = pos_encoding(x)

print(f"输入形状: {x.shape}")   # torch.Size([4, 20, 256])
```

位置编码是 Transformer 架构中的关键组件，它使模型能够区分不同位置的词，即使它们的嵌入向量相同。

### 5.3 可学习的位置编码

除了固定的位置编码，也可以使用可学习的位置编码：

## 实例

```python
import torch

import torch.nn as nn

class LearnablePositionalEncoding(nn.Module):

    """

    可学习的位置编码

    """

    def __init__(self, d_model, max_len=5000):

        super().__init__()

        self.pos_embedding = nn.Embedding(max_len, d_model)

    def forward(self, x):

        batch_size, seq_len, d_model = x.size(1), x.size(1), x.size(2)

        # 创建位置索引 [0, 1, 2, ..., seq_len-1]

        positions = torch.arange(seq_len, device=x.device).unsqueeze(0).expand(batch_size, -1)

        pos_encoded = self.pos_embedding(positions)

        return x + pos_encoded

# 使用示例

pos_encoding = LearnablePositionalEncoding(d_model=256, max_len=100)

x = torch.randn(4, 20, 256)

x = pos_encoding(x)

print(f"输出形状: {x.shape}")   # torch.Size([4, 20, 256])
```

## 6. 嵌入层的进阶技巧

6.1 降低显存占用

当词表非常大时，嵌入层会占用大量显存。可以使用以下技巧优化：

实例

```python
import torch

import torch.nn as nn

# 技巧一：使用稀疏梯度（sparse=True）

embedding = nn.Embedding(

    num_embeddings=100000,

    embedding_dim=256,

    sparse=True  # 梯度以稀疏格式存储，节省显存

)

# 技巧二：使用量化（ quantization）

# 将 float32 转换为 int8 或 float16

embedding_int8 = embedding.to(torch.int8)

# 技巧三：冻结不常用的词向量

# 在大规模词表中，只训练高频词，低频词保持冻结

embedding = nn.Embedding(num_embeddings=100000, embedding_dim=256)

embedding.weight.requires_grad = True

# 冻结索引大于 50000 的词向量

with torch.no_grad():

    embedding.weight[50000:] *= 0

embedding.weight.requires_grad = False

# 只训练高频词

embedding.weight[1:50000].requires_grad = True
```

### 6.2 处理未登录词 (OOV)

测试集中可能出现词表中没有的词（未登录词 / OOV），需要特殊处理：

## 实例

```python
import torch

import torch.nn as nn

class EmbeddingWithOOV(nn.Module):

    """

    支持处理未登录词的嵌入层

    """

    def __init__(self, vocab_size, embed_dim, oov_idx=None):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size + 1, embed_dim, padding_idx=0)

        self.oov_idx = oov_idx if oov_idx is not None else vocab_size  # 最后一个索引作为 OOV

    def forward(self, x):

        # 将 OOV 词的索引替换为 oov_idx

        oov_mask = x >= self.vocab_size

        x = x.clone()

        x[oov_mask] = self.oov_idx

        return self.embedding(x)

# 使用哈希技术处理更大规模的词表

class HashEmbedding(nn.Module):

    """

    使用哈希技术处理任意规模词表的嵌入层

    """

    def __init__(self, num_buckets, embed_dim):

        super().__init__()

        self.num_buckets = num_buckets

        self.embedding = nn.Embedding(num_buckets, embed_dim)

    def forward(self, x):

        # 将词索引哈希到桶中

        # 使用 Python 字典的哈希方式

        hashed = torch.remainder(x, self.num_buckets)

        return self.embedding(hashed)
```

### 6.3 子词嵌入 (Subword Embedding)

对于形态丰富的语言（如德语、俄语），子词嵌入可以有效处理未登录词问题：

## 实例

```python
import torch

import torch.nn as nn

class SubwordEmbedding(nn.Module):

    """

    简化的子词嵌入示例

    实际应使用 BPE、WordPiece 等算法进行分词

    """

    def __init__(self, vocab_size, embed_dim, char_dim=50):

        super().__init__()

        # 字符级嵌入

        self.char_embedding = nn.Embedding(vocab_size, char_dim)

        # 词级嵌入

        self.word_embedding = nn.Embedding(vocab_size, embed_dim - char_dim)

        # 字符级 LSTM，用于组合字符向量

        self.char_lstm = nn.LSTM(

            char_dim, char_dim,

            batch_first=True, bidirectional=True

        )

    def forward(self, word_ids, char_ids):

        """

        word_ids: 词索引 (batch_size, seq_len)

        char_ids: 字符索引 (batch_size, seq_len, max_word_len)

        """

        # 词嵌入

        word_emb = self.word_embedding(word_ids)

        # 字符嵌入 + LSTM

        batch_size, seq_len, max_word_len = char_ids.shape

        char_ids_flat = char_ids.view(-1, max_word_len)  # (batch_size * seq_len, max_word_len)

        char_emb = self.char_embedding(char_ids_flat)    # (batch_size * seq_len, max_word_len, char_dim)

        char_output, (h_n, _) = self.char_lstm(char_emb)

        # 取双向最后隐藏状态拼接

        char_rep = torch.cat([h_n[-2], h_n[-1]], dim=-1)  # (batch_size * seq_len, char_dim * 2)

        char_rep = char_rep.view(batch_size, seq_len, -1)  # (batch_size, seq_len, char_dim * 2)

        # 拼接词嵌入和字符表示

        combined = torch.cat([word_emb, char_rep], dim=-1)

        return combined
```

## 7. 完整实战：文本分类模型

下面是一个完整的文本分类模型示例，包含嵌入层、LSTM 和分类器：

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.utils.data import Dataset, DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── 配置参数 ──────────────────────────────────────

VOCAB_SIZE = 10000

EMBED_DIM = 128

HIDDEN_SIZE = 128

NUM_LAYERS = 2

NUM_CLASSES = 5

DROPOUT = 0.3

MAX_LEN = 200

# ── 模型定义 ──────────────────────────────────────

class TextClassificationModel(nn.Module):

    def __init__(self, vocab_size, embed_dim, hidden_size,

                 num_layers, num_classes, dropout=0.3, padding_idx=0):

        super().__init__()

        # 嵌入层

        self.embedding = nn.Embedding(

            vocab_size,

            embed_dim,

            padding_idx=padding_idx

        )

        # BiLSTM

        self.lstm = nn.LSTM(

            embed_dim,

            hidden_size,

            num_layers=num_layers,

            batch_first=True,

            bidirectional=True,

            dropout=dropout if num_layers > 1 else 0

        )

        # 分类器

        self.dropout = nn.Dropout(dropout)

        self.fc = nn.Linear(hidden_size * 2, num_classes)

    def forward(self, x):

        # x: (batch_size, seq_len)

        embedded = self.embedding(x)  # (batch_size, seq_len, embed_dim)

        # LSTM

        output, (h_n, c_n) = self.lstm(embedded)

        # 双向最后隐藏状态拼接

        h_forward = h_n[-2]   # (batch_size, hidden_size)

        h_backward = h_n[-1]  # (batch_size, hidden_size)

        h_combined = torch.cat([h_forward, h_backward], dim=-1)

        # 分类

        dropped = self.dropout(h_combined)

        logits = self.fc(droped)

        return logits

# ── Dataset ──────────────────────────────────────

class TextDataset(Dataset):

    def __init__(self, texts, labels, vocab, max_len=200):

        self.texts = texts

        self.labels = labels

        self.vocab = vocab

        self.max_len = max_len

    def __len__(self):

        return len(self.texts)

    def __getitem__(self, idx):

        text = self.texts[idx][:self.max_len]

        # 将词转换为索引，未知词用 1（<UNK>）表示

        ids = [self.vocab.get(word, 1) for word in text]

        # 补零到固定长度

        if len(ids) < self.max_len:

            ids += [0] * (self.max_len - len(ids))

        return torch.tensor(ids), torch.tensor(self.labels[idx])

# ── 训练函数 ──────────────────────────────────────

def train_epoch(model, loader, optimizer, criterion, device):

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in loader:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item() * inputs.size(0)

        _, predicted = outputs.max(1)

        correct += predicted.eq(labels).sum().item()

        total += labels.size(0)

    return total_loss / total, correct / total

# ── 初始化与训练 ──────────────────────────────────

# 假设已有词表

word2idx = {'<PAD>': 0, '<UNK>': 1}  # 词表需根据实际语料构建

model = TextClassificationModel(

    VOCAB_SIZE, EMBED_DIM, HIDDEN_SIZE,

    NUM_LAYERS, NUM_CLASSES, DROPOUT

).to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 模拟训练

print("开始训练...")

for epoch in range(10):

    train_loss, train_acc = train_epoch(model, None, optimizer, criterion, device)

    print(f"Epoch {epoch+1}: Loss={train_loss:.4f}, Acc={train_acc:.4f}")
```

## 8. API 快速参考

### 8.1 nn.Embedding 常用操作

| 操作 | 代码 |
| --- | --- |
| 创建嵌入层 | nn.Embedding(num_embeddings, embedding_dim) |
| 加载预训练嵌入 | nn.Embedding.from_pretrained(weights) |
| 查表获取嵌入 | embedding(word_ids) |
| 冻结嵌入 | embedding.weight.requires_grad = False |
| 获取嵌入向量 | embedding.weight[idx] |

### 8.2 预训练词向量资源

| 资源 | 维度 | 特点 |
| --- | --- | --- |
| GloVe | 50, 100, 200, 300 | 词共现统计，训练快 |
| Word2Vec | 50-500 | Google 训练，覆盖广 |
| FastText | 300 | 支持子词，处理 OOV 好 |
| BERT | 768+ | 上下文相关，效果最好 |

### 8.3 嵌入层选型建议

```python
数据量小（< 10K）

-> 使用预训练词向量（GloVe/FastText）+ 冻结或微调

数据量中等（10K ~ 100K）

-> 使用预训练词向量 + 微调

数据量大（> 100K）

-> 可考虑从头训练，或使用大规模预训练模型

领域差异大

-> 使用领域相关预训练模型或增量训练

资源受限

-> 冻结嵌入层，使用较小的嵌入维度
```

---

-

# PyTorch 生成对抗网络 (GAN)

生成对抗网络（Generative Adversarial Network，GAN）是深度学习中最具创意的模型架构之一。它通过让两个神经网络相互对抗、相互学习，最终能够生成非常逼真的数据。GAN 广泛应用于图像生成、风格迁移、数据增强等场景。

## 1. GAN 核心原理

GAN 的核心思想来源于博弈论中的"零和博弈"。它包含两个相互对抗的网络：

- 生成器（Generator）：学习生成假数据，目标是让判别器无法区分生成数据与真实数据

- 判别器（Discriminator）：学习区分真实数据与生成数据，目标是尽可能准确判断

两者在训练过程中相互对抗、不断提升，最终达到纳什均衡状态。

### 1.1 GAN 的目标函数

GAN 的训练目标可以表示为以下minimax游戏：

\[
\min_G \max_D \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\]

其中：

- \(G\) 表示生成器网络

- \(D\) 表示判别器网络

- \(x\) 表示真实数据

- \(z\) 表示随机噪声向量（通常服从标准正态分布）

- \(G(z)\) 表示生成器根据噪声生成的假数据

### 1.2 训练过程解读

GAN 的训练分为两个阶段：

第一阶段：训练判别器

固定生成器，提升判别器的分辨能力：

\[
\max_D \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]
\]

第二阶段：训练生成器

固定判别器，提升生成器的欺骗能力：

\[
\min_G \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]
\]

实际训练中，通常先训练判别器 k 步，再训练生成器 1 步，以保持平衡。

## 2. 基础 GAN 实现

下面实现一个最简单的 GAN——用于生成二维数据点。

### 2.1 定义生成器和判别器

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import matplotlib.pyplot as plt

# 设置随机种子

torch.manual_seed(42)

# ── 生成器网络 ──────────────────────────────────────

class Generator(nn.Module):

    """

    生成器：从随机噪声生成数据

    输入：噪声向量 (batch_size, noise_dim)

    输出：生成数据 (batch_size, data_dim)

    """

    def __init__(self, noise_dim, data_dim, hidden_dim=64):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(noise_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, data_dim),

            # 输出不激活，GAN 会学习合适的分布

        )

    def forward(self, x):

        return self.net(x)

# ── 判别器网络 ──────────────────────────────────────

class Discriminator(nn.Module):

    """

    判别器：区分真实数据与生成数据

    输入：数据点 (batch_size, data_dim)

    输出：真实数据的概率 (batch_size, 1)

    """

    def __init__(self, data_dim, hidden_dim=64):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(data_dim, hidden_dim),

            nn.LeakyReLU(0.2),  # LeakyReLU 防止梯度消失

            nn.Linear(hidden_dim, hidden_dim),

            nn.LeakyReLU(0.2),

            nn.Linear(hidden_dim, 1),

            nn.Sigmoid()  # 输出概率

        )

    def forward(self, x):

        return self.net(x)

# 超参数

NOISE_DIM = 16

DATA_DIM = 2

HIDDEN_DIM = 64

BATCH_SIZE = 128

# 创建网络

generator = Generator(NOISE_DIM, DATA_DIM, HIDDEN_DIM)

discriminator = Discriminator(DATA_DIM, HIDDEN_DIM)

print(f"生成器参数量: {sum(p.numel() for p in generator.parameters()):,}")

print(f"判别器参数量: {sum(p.numel() for p in discriminator.parameters()):,}")
```

### 2.2 训练循环

## 实例

```python
# ── 优化器 ──────────────────────────────────────

lr = 0.001

g_optimizer = optim.Adam(generator.parameters(), lr=lr)

d_optimizer = optim.Adam(discriminator.parameters(), lr=lr)

# 损失函数：二分类交叉熵

criterion = nn.BCELoss()

# ── 训练数据：环形分布 ──────────────────────────

def generate_real_data(batch_size):

    """生成环形分布的真实数据"""

    angles = torch.rand(batch_size) * 2 * torch.pi

    radius = 1.0 + torch.randn(batch_size) * 0.1  # 半径约为 1

    x = radius * torch.cos(angles)

    y = radius * torch.sin(angles)

    return torch.stack([x, y], dim=1)

# ── 训练循环 ──────────────────────────────────────

NUM_EPOCHS = 1000

d_losses = []

g_losses = []

for epoch in range(NUM_EPOCHS):

    # 1. 训练判别器

    # 生成假数据

    noise = torch.randn(BATCH_SIZE, NOISE_DIM)

    fake_data = generator(noise).detach()  # detach 避免计算生成器梯度

    # 生成真实数据

    real_data = generate_real_data(BATCH_SIZE)

    # 判别器损失

    real_pred = discriminator(real_data)

    fake_pred = discriminator(fake_data)

    d_loss = criterion(real_pred, torch.ones_like(real_pred)) + \

             criterion(fake_pred, torch.zeros_like(fake_pred))

    # 更新判别器

    d_optimizer.zero_grad()

    d_loss.backward()

    d_optimizer.step()

    # 2. 训练生成器

    # 生成新一批假数据

    noise = torch.randn(BATCH_SIZE, NOISE_DIM)

    fake_data = generator(noise)

    # 生成器损失：让判别器认为生成的数据是真实的

    fake_pred = discriminator(fake_data)

    g_loss = criterion(fake_pred, torch.ones_like(fake_pred))

    # 更新生成器

    g_optimizer.zero_grad()

    g_loss.backward()

    g_optimizer.step()

    # 记录损失

    d_losses.append(d_loss.item())

    g_losses.append(g_loss.item())

    if (epoch + 1) % 100 == 0:

        print(f"Epoch {epoch+1:4d} | D_loss: {d_loss:.4f} | G_loss: {g_loss:.4f}")

print("训练完成！")
```

### 2.3 可视化生成结果

## 实例

```python
# 生成数据并可视化

def visualize_results(generator, num_samples=1000):

    noise = torch.randn(num_samples, NOISE_DIM)

    generated_data = generator(noise).detach().numpy()

    plt.figure(figsize=(6, 6))

    plt.scatter(generated_data[:, 0], generated_data[:, 1],

                alpha=0.5, s=10, c='blue', label='Generated')

    plt.xlim(-2, 2)

    plt.ylim(-2, 2)

    plt.xlabel('x')

    plt.ylabel('y')

    plt.title('GAN Generated Data')

    plt.legend()

    plt.grid(True, alpha=0.3)

    plt.show()

# 查看生成效果

visualize_results(generator)
```

## 3. DCGAN - 深度卷积 GAN

DCGAN 是将卷积神经网络引入 GAN 的经典架构，大幅提升了图像生成质量。

### 3.1 DCGAN 架构要点

- 使用转置卷积（Transposed Convolution）进行上采样生成图像

- 使用带步长的卷积进行下采样判别图像

- 在生成器和判别器中使用 BatchNorm（但输出层和输入层不使用）

- 生成器使用 ReLU，判别器使用 LeakyReLU

### 3.2 DCGAN 实现

## 实例

```python
import torch

import torch.nn as nn

# ── DCGAN 生成器 ─────────────────────────────────

class DCGenerator(nn.Module):

    """

    DCGAN 生成器：使用转置卷积上采样

    """

    def __init__(self, noise_dim=100, channels=3, features_g=64):

        super().__init__()

        self.noise_dim = noise_dim

        # 输入: noise_dim x 1 x 1

        self.net = nn.Sequential(

            # 转置卷积: (batch, features_g*8, 4, 4)

            nn.ConvTranspose2d(noise_dim, features_g * 8, 4, 1, 0, bias=False),

            nn.BatchNorm2d(features_g * 8),

            nn.ReLU(True),

            # (batch, features_g*4, 8, 8)

            nn.ConvTranspose2d(features_g * 8, features_g * 4, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_g * 4),

            nn.ReLU(True),

            # (batch, features_g*2, 16, 16)

            nn.ConvTranspose2d(features_g * 4, features_g * 2, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_g * 2),

            nn.ReLU(True),

            # (batch, features_g, 32, 32)

            nn.ConvTranspose2d(features_g * 2, features_g, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_g),

            nn.ReLU(True),

            # 输出: (batch, channels, 64, 64)

            nn.ConvTranspose2d(features_g, channels, 4, 2, 1, bias=False),

            nn.Tanh()  # 输出范围 [-1, 1]

        )

    def forward(self, x):

        # x: (batch, noise_dim) -> (batch, noise_dim, 1, 1)

        x = x.view(x.size(0), x.size(1), 1, 1)

        return self.net(x)

# ── DCGAN 判别器 ─────────────────────────────────

class DCDiscriminator(nn.Module):

    """

    DCGAN 判别器：使用卷积下采样

    """

    def __init__(self, channels=3, features_d=64):

        super().__init__()

        # 输入: (batch, channels, 64, 64)

        self.net = nn.Sequential(

            # (batch, features_d, 32, 32)

            nn.Conv2d(channels, features_d, 4, 2, 1, bias=False),

            nn.LeakyReLU(0.2, inplace=True),

            # (batch, features_d*2, 16, 16)

            nn.Conv2d(features_d, features_d * 2, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_d * 2),

            nn.LeakyReLU(0.2, inplace=True),

            # (batch, features_d*4, 8, 8)

            nn.Conv2d(features_d * 2, features_d * 4, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_d * 4),

            nn.LeakyReLU(0.2, inplace=True),

            # (batch, features_d*8, 4, 4)

            nn.Conv2d(features_d * 4, features_d * 8, 4, 2, 1, bias=False),

            nn.BatchNorm2d(features_d * 8),

            nn.LeakyReLU(0.2, inplace=True),

            # 输出: (batch, 1, 1, 1)

            nn.Conv2d(features_d * 8, 1, 4, 1, 0, bias=False),

            nn.Sigmoid()

        )

    def forward(self, x):

        return self.net(x).view(x.size(0), -1)

# 测试网络

noise_dim = 100

generator = DCGenerator(noise_dim=noise_dim, channels=3, features_g=64)

discriminator = DCDiscriminator(channels=3, features_d=64)

# 测试前向传播

noise = torch.randn(2, noise_dim)

fake_images = generator(noise)

print(f"生成图像形状: {fake_images.shape}")  # torch.Size([2, 3, 64, 64])

decision = discriminator(fake_images)

print(f"判别结果形状: {decision.shape}")     # torch.Size([2, 1])
```

### 3.3 完整 DCGAN 训练代码

## 实例

```python
# ── 训练配置 ─────────────────────────────────────

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"使用设备: {device}")

NOISE_DIM = 100

LEARNING_RATE = 0.0002

BETA1 = 0.5  # Adam 参数

# 创建网络

generator = DCGenerator(noise_dim=NOISE_DIM).to(device)

discriminator = DCDiscriminator().to(device)

# 优化器

g_optimizer = optim.Adam(generator.parameters(), lr=LEARNING_RATE, betas=(BETA1, 0.999))

d_optimizer = optim.Adam(discriminator.parameters(), lr=LEARNING_RATE, betas=(BETA1, 0.999))

criterion = nn.BCELoss()

# ── 训练循环 ─────────────────────────────────────

fixed_noise = torch.randn(64, NOISE_DIM, device=device)  # 用于可视化

def train_dcgan(generator, discriminator, g_optimizer, d_optimizer, criterion,

                num_epochs, device, fixed_noise):

    G_losses = []

    D_losses = []

    for epoch in range(num_epochs):

        for batch_idx in range(100):  # 假设每个 epoch 有 100 个 batch

            # 训练判别器

            discriminator.zero_grad()

            # 真实图像（假设已有）

            # real_images = ...

            # 这里用随机噪声模拟

            real_images = torch.randn(32, 3, 64, 64).to(device)

            batch_size = real_images.size(0)

            labels_real = torch.ones(batch_size, 1).to(device)

            labels_fake = torch.zeros(batch_size, 1).to(device)

            # 真实图像损失

            output = discriminator(real_images)

            d_loss_real = criterion(output, labels_real)

            # 生成图像损失

            noise = torch.randn(batch_size, NOISE_DIM).to(device)

            fake_images = generator(noise)

            output = discriminator(fake_images.detach())

            d_loss_fake = criterion(output, labels_fake)

            # 总损失

            d_loss = d_loss_real + d_loss_fake

            d_loss.backward()

            d_optimizer.step()

            # 训练生成器

            generator.zero_grad()

            noise = torch.randn(batch_size, NOISE_DIM).to(device)

            fake_images = generator(noise)

            output = discriminator(fake_images)

            g_loss = criterion(output, labels_real)  # 希望生成图像被判定为真

            g_loss.backward()

            g_optimizer.step()

            # 记录损失

            if batch_idx % 50 == 0:

                G_losses.append(g_loss.item())

                D_losses.append(d_loss.item())

                print(f"[{epoch}/{num_epochs}][{batch_idx}/100] "

                      f"D_loss: {d_loss:.4f} | G_loss: {g_loss:.4f}")

    return G_losses, D_losses

# 开始训练

# G_losses, D_losses = train_dcgan(generator, discriminator, g_optimizer,

#                                   d_optimizer, criterion, 5, device, fixed_noise)

print("DCGAN 架构已定义完成，可以开始训练！")
```

## 4. GAN 的训练技巧

### 4.1 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 模式崩溃（Mode Collapse） | 生成器只生成有限的几种样本 | 使用 WGAN、添加小批量判别、使用标签平滑 |
| 判别器过强 | 生成器梯度消失，无法学习 | 训练生成器多次、降低判别器学习率、使用 LeakyReLU |
| 训练不稳定 | GAN 目标函数非凸，难以收敛 | 使用谱归一化、梯度惩罚、learning rate warmup |
| 生成质量差 | 网络容量不足或训练不足 | 增加网络深度、使用更多训练数据、训练更长时间 |

### 4.2 损失函数改进

原始 GAN 使用 JS 散度，存在梯度消失问题。WGAN 使用 Wasserstein 距离更加稳定：

## 实例

```python
# WGAN 损失函数（替代 BCE）

def wgan_d_loss(real_pred, fake_pred):

    """判别器损失：真实样本得分高，生成样本得分低"""

    return -(torch.mean(real_pred) - torch.mean(fake_pred))

def wgan_g_loss(fake_pred):

    """生成器损失：让生成样本得分高"""

    return -torch.mean(fake_pred)

# 梯度惩罚（Gradient Penalty）- WGAN-GP

def gradient_penalty(discriminator, real_images, fake_images, device):

    """WGAN-GP 梯度惩罚项"""

    batch_size = real_images.size(0)

    alpha = torch.rand(batch_size, 1, 1, 1).to(device)

    # 在真实和生成图像之间插值

    interpolated = alpha * real_images + (1 - alpha) * fake_images

    interpolated.requires_grad = True

    # 计算插值图像的判别器输出

    pred = discriminator(interpolated)

    # 计算梯度

    gradients = torch.autograd.grad(

        outputs=pred,

        inputs=interpolated,

        grad_outputs=torch.ones_like(pred),

        create_graph=True,

        retain_graph=True,

        only_inputs=True

    )[0]

    # 计算梯度范数

    gradients = gradients.view(batch_size, -1)

    gradient_norm = gradients.norm(2, dim=1)

    penalty = ((gradient_norm - 1) ** 2).mean()

    return penalty
```

### 4.3 谱归一化（Spectral Normalization）

谱归一化可以稳定 GAN 训练，控制判别器的 Lipschitz 常数：

## 实例

```python
import torch.nn.utils.spectral_norm as spectral_norm

# 使用谱归一化的判别器

class SNDiscriminator(nn.Module):

    def __init__(self, channels=3, features_d=64):

        super().__init__()

        self.net = nn.Sequential(

            spectral_norm(nn.Conv2d(channels, features_d, 4, 2, 1)),

            nn.LeakyReLU(0.2, inplace=True),

            spectral_norm(nn.Conv2d(features_d, features_d * 2, 4, 2, 1)),

            nn.LeakyReLU(0.2, inplace=True),

            spectral_norm(nn.Conv2d(features_d * 2, features_d * 4, 4, 2, 1)),

            nn.LeakyReLU(0.2, inplace=True),

            spectral_norm(nn.Conv2d(features_d * 4, 1, 4, 1, 0)),

            nn.Sigmoid()

        )

    def forward(self, x):

        return self.net(x).view(x.size(0), -1)
```

## 5. 条件 GAN (cGAN)

条件 GAN 允许指定生成数据的类别标签，实现有条件的生成。

### 5.1 cGAN 架构

## 实例

```python
import torch

import torch.nn as nn

class ConditionalGenerator(nn.Module):

    """条件生成器：同时接收噪声和类别标签"""

    def __init__(self, noise_dim, num_classes, embed_dim, img_channels, features_g=64):

        super().__init__()

        self.label_emb = nn.Embedding(num_classes, embed_dim)

        # 将噪声和标签嵌入拼接

        self.net = nn.Sequential(

            nn.Linear(noise_dim + embed_dim, features_g * 8 * 4 * 4),

            nn.BatchNorm1d(features_g * 8 * 4 * 4),

            nn.ReLU(),

            # 然后接转置卷积（类似 DCGAN）

            # ...

        )

    def forward(self, noise, labels):

        # 将类别标签嵌入到与噪声相同的维度

        label_embedding = self.label_emb(labels)

        # 拼接噪声和标签嵌入

        x = torch.cat([noise, label_embedding], dim=1)

        return self.net(x)

class ConditionalDiscriminator(nn.Module):

    """条件判别器：同时接收图像和类别标签"""

    def __init__(self, img_channels, num_classes, embed_dim, features_d=64):

        super().__init__()

        self.label_emb = nn.Embedding(num_classes, embed_dim)

        # 将图像和标签嵌入拼接

        self.net = nn.Sequential(

            nn.Conv2d(img_channels + embed_dim, features_d, 4, 2, 1),

            nn.LeakyReLU(0.2),

            # ...

        )

    def forward(self, img, labels):

        # 将标签嵌入调整到与图像相同的空间尺寸

        label_embedding = self.label_emb(labels)

        # 调整形状以便拼接

        label_embedding = label_embedding.unsqueeze(2).unsqueeze(3)

        label_embedding = label_embedding.expand(-1, -1, img.size(2), img.size(3))

        # 拼接图像和标签

        x = torch.cat([img, label_embedding], dim=1)

        return self.net(x)
```

## 6. GAN 评估指标

### 6.1 常用评估指标

| 指标 | 描述 | 优点 | 缺点 |
| --- | --- | --- | --- |
| Inception Score (IS) | 使用 Inception v3 评估生成图像的质量和多样性 | 计算简单，与人类判断有一定相关性 | 不评估过拟合，无法检测模式崩溃 |
| Fréchet Inception Distance (FID) | 计算真实图像和生成图像在特征空间的距离 | 对噪声和模式崩溃更敏感 | 需要大量样本，计算较慢 |
| 人工评估 | 人工判断生成图像质量 | 最准确反映人类感知 | 主观、耗时 |

### 6.2 FID 计算实现

## 实例

```python
import numpy as np

from scipy import linalg

def calculate_fid(real_activations, fake_activations):

    """

    计算 Fréchet Inception Distance

    real_activations: 真实图像的特征向量 (N, dim)

    fake_activations: 生成图像的特征向量 (N, dim)

    """

    # 计算均值和协方差

    mu1, sigma1 = real_activations.mean(axis=0), np.cov(real_activations, rowvar=False)

    mu2, sigma2 = fake_activations.mean(axis=0), np.cov(fake_activations, rowvar=False)

    # 计算 FID

    diff = mu1 - mu2

    # 计算协方差矩阵的和

    covmean, _ = linalg.sqrtm(sigma1.dot(sigma2), disp=False)

    # 避免复数

    if np.iscomplexobj(covmean):

        covmean = covmean.real

    fid = diff.dot(diff) + np.trace(sigma1 + sigma2 - 2 * covmean)

    return fid

# 简化示例：使用随机数据

np.random.seed(42)

real_acts = np.random.randn(1000, 2048)  # Inception v3 输出维度

fake_acts = np.random.randn(1000, 2048)

fid_score = calculate_fid(real_acts, fake_acts)

print(f"FID Score: {fid_score:.2f}")

# FID 越低越好，通常小于 50 表示较好的生成质量
```

## 7. 常见 GAN 变体

GAN 发展至今产生了众多变体，适用于不同的应用场景：

| 模型 | 全称 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| DCGAN | Deep Convolutional GAN | 使用卷积网络，生成高质量图像 | 图像生成 |
| WGAN | Wasserstein GAN | 使用 Wasserstein 距离，训练更稳定 | 稳定训练 |
| WGAN-GP | WGAN with Gradient Penalty | 梯度惩罚替代权重裁剪 | 稳定训练 |
| CGAN | Conditional GAN | 加入条件信息，可控生成 | 条件生成 |
| CycleGAN | Cycle-Consistent GAN | 无监督图像转换 | 风格迁移 |
| StyleGAN | Style-Based GAN | 风格控制，高质量人脸生成 | 人脸生成 |
| BigGAN | Big GAN | 大规模、高质量图像生成 | 高分辨率图像 |
| ProGAN | Progressive Growing GAN | 渐进式增大分辨率 | 高分辨率生成 |

---

-

# PyTorch 自编码器 (Autoencoder)

自编码器（Autoencoder，AE）是一种无监督学习的神经网络，通过学习将输入数据压缩到低维潜在空间，再从压缩表示重构原始数据。

自编码器广泛应用于数据降维、特征提取、异常检测、图像去噪、生成模型等场景。

## 1. 自编码器基础原理

自编码器的基本结构包含三个部分：

- 编码器（Encoder）：将输入数据 \(x\) 映射到低维潜在表示 \(z\)

- 潜在空间（Latent Space）：编码器输出的低维向量，也称为瓶颈层

- 解码器（Decoder）：将潜在表示 \(z\) 重构为输出 \(\hat{x}\)

### 1.1 网络结构

自编码器的目标是让输出 \(\hat{x}\) 尽可能接近输入 \(x\)：

\[
\min_{\theta, \phi} \frac{1}{n} \sum_{i=1}^{n} \| x_i - D_\phi(E_\theta(x_i)) \|^2
\]

其中 \(\theta\) 是编码器参数，\(\phi\) 是解码器参数。

### 1.2 降维效果

自编码器通过强制数据通过比输入维度更小的瓶颈层，从而学习数据的压缩表示。这种压缩保留了数据的主要信息。

与主成分分析（PCA）相比，自编码器可以学习非线性降维，能够捕捉更复杂的数据结构。

## 2. 基础自编码器实现

### 2.1 简单自编码器

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.utils.data import DataLoader, TensorDataset

# ── 自编码器模型 ─────────────────────────────────

class Autoencoder(nn.Module):

    """

    基础自编码器：对称结构

    """

    def __init__(self, input_dim, hidden_dim, latent_dim):

        super().__init__()

        # 编码器

        self.encoder = nn.Sequential(

            nn.Linear(input_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, latent_dim),  # 瓶颈层

        )

        # 解码器

        self.decoder = nn.Sequential(

            nn.Linear(latent_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, input_dim),

        )

    def forward(self, x):

        z = self.encoder(x)

        x_recon = self.decoder(z)

        return x_recon

    def encode(self, x):

        """编码：获取潜在表示"""

        return self.encoder(x)

    def decode(self, z):

        """解码：从潜在表示重构"""

        return self.decoder(z)

# ── 使用示例 ──────────────────────────────────────

INPUT_DIM = 784   # 例如 MNIST 图像展开后

HIDDEN_DIM = 256

LATENT_DIM = 32   # 潜在空间维度，远小于输入维度

model = Autoencoder(INPUT_DIM, HIDDEN_DIM, LATENT_DIM)

print(f"输入维度: {INPUT_DIM}")

print(f"潜在维度: {LATENT_DIM}")

print(f"压缩比: {INPUT_DIM / LATENT_DIM:.1f}x")

# 查看参数量

total_params = sum(p.numel() for p in model.parameters())

print(f"总参数量: {total_params:,}")
```

### 2.2 卷积自编码器

对于图像数据，使用卷积层的自编码器效果更好：

## 实例

```python
import torch

import torch.nn as nn

class ConvAutoencoder(nn.Module):

    """

    卷积自编码器：适用于图像

    """

    def __init__(self, channels=3, latent_dim=128):

        super().__init__()

        # 编码器：逐步减小尺寸，增加通道数

        # 输入: (batch, channels, 64, 64)

        self.encoder = nn.Sequential(

            # 32 -> 16

            nn.Conv2d(channels, 32, kernel_size=3, stride=2, padding=1),

            nn.ReLU(),

            # 16 -> 8

            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),

            nn.ReLU(),

            # 8 -> 4

            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),

            nn.ReLU(),

            # 4 -> 2

            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),

            nn.ReLU(),

        )

        # 潜在空间映射

        self.to_latent = nn.AdaptiveAvgPool2d((1, 1))

        # 解码器：逐步增大尺寸

        # 输入: (batch, 256, 2, 2)

        self.from_latent = nn.Sequential(

            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),

            nn.Conv2d(256, 128, kernel_size=3, padding=1),

            nn.ReLU(),

            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),

            nn.Conv2d(128, 64, kernel_size=3, padding=1),

            nn.ReLU(),

            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),

            nn.Conv2d(64, 32, kernel_size=3, padding=1),

            nn.ReLU(),

            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),

            nn.Conv2d(32, channels, kernel_size=3, padding=1),

            nn.Sigmoid()  # 输出 [0, 1]

        )

    def forward(self, x):

        z = self.encode(x)

        x_recon = self.decode(z)

        return x_recon

    def encode(self, x):

        """编码"""

        features = self.encoder(x)

        z = self.to_latent(features)

        z = z.view(z.size(0), -1)  # (batch, 256)

        return z

    def decode(self, z):

        """解码"""

        # 将向量 reshape 为特征图

        batch_size = z.size(0)

        z = z.view(batch_size, 256, 1, 1)

        z = z.expand(-1, -1, 2, 2)  # 上采样到 2x2

        x_recon = self.from_latent(z)

        return x_recon

# 测试

model = ConvAutoencoder(channels=3, latent_dim=128)

x = torch.randn(4, 3, 64, 64)

x_recon = model(x)

print(f"输入形状: {x.shape}")

print(f"输出形状: {x_recon.shape}")

print(f"潜在向量形状: {model.encode(x).shape}")
```

### 2.3 训练与重构

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

# ── 训练配置 ─────────────────────────────────────

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ConvAutoencoder(channels=3, latent_dim=128).to(device)

criterion = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ── 训练循环 ─────────────────────────────────────

def train_autoencoder(model, dataloader, criterion, optimizer, num_epochs=10):

    model.train()

    for epoch in range(num_epochs):

        total_loss = 0

        for batch in dataloader:

            images = batch[0].to(device)

            # 前向传播

            outputs = model(images)

            loss = criterion(outputs, images)

            # 反向传播

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.6f}")

    return model

# 假设已有数据加载器

# train_autoencoder(model, train_loader, criterion, optimizer, num_epochs=10)

print("自编码器训练完成！")
```

## 3. 去噪自编码器 (DAE)

去噪自编码器（Denoising Autoencoder，DAE）在训练时给输入添加噪声，然后学习去除噪声恢复原始输入。这使模型学到更鲁棒的特征表示。

### 3.1 去噪自编码器实现

## 实例

```python
import torch

import torch.nn as nn

class DenoisingAutoencoder(nn.Module):

    """

    去噪自编码器

    """

    def __init__(self, input_dim, hidden_dim, latent_dim):

        super().__init__()

        self.encoder = nn.Sequential(

            nn.Linear(input_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, latent_dim),

        )

        self.decoder = nn.Sequential(

            nn.Linear(latent_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, input_dim),

            nn.Sigmoid()  # 输出 [0, 1]

        )

    def forward(self, x):

        z = self.encode(x)

        return self.decode(z)

    def encode(self, x):

        return self.encoder(x)

    def decode(self, z):

        return self.decoder(z)

def add_noise(x, noise_factor=0.3):

    """

    添加高斯噪声

    """

    noise = torch.randn_like(x) * noise_factor

    noisy_x = x + noise

    return torch.clamp(noisy_x, 0.0, 1.0)

# 训练去噪自编码器

def train_dae(model, dataloader, noise_factor=0.3, lr=1e-3):

    criterion = nn.MSELoss()

    optimizer = optim.Adam(model.parameters(), lr=lr)

    model.train()

    for epoch in range(10):

        for batch in dataloader:

            images = batch[0]

            # 添加噪声

            noisy_images = add_noise(images, noise_factor)

            noisy_images = noisy_images.to(next(model.parameters()).device)

            images = images.to(next(model.parameters()).device)

            # 前向传播

            outputs = model(noisy_images)

            loss = criterion(outputs, images)  # 与原始图像比较，而非噪声图像

            # 反向传播

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

    return model
```

### 3.2 其他噪声类型

## 实例

```python
def salt_pepper_noise(x, prob=0.1):

    """盐椒噪声"""

    random_mask = torch.rand_like(x)

    noisy = x.clone()

    noisy[random_mask < prob / 2] = 0.0

    noisy[random_mask > 1 - prob / 2] = 1.0

    return noisy

def mask_noise(x, prob=0.1):

    """遮挡噪声（随机置零）"""

    mask = torch.rand_like(x) > prob

    return x * mask.float()

def dropout_noise(x, rate=0.2):

    """Dropout 噪声"""

    mask = torch.rand_like(x) > rate

    return x * mask.float() / (1 - rate)
```

## 4. 变分自编码器 (VAE)

变分自编码器（Variational Autoencoder，VAE）是一种生成模型，它将数据编码为潜在空间中的概率分布，而非固定向量。这使得我们可以从潜在空间中采样生成新数据。

### 4.1 VAE 核心原理

VAE 的关键创新是学习潜在变量的概率分布：

- 编码器输出均值 \(\mu\) 和标准差 \(\sigma\)

- 从正态分布 \(\mathcal{N}(\mu, \sigma)\) 中采样得到潜在向量 \(z\)

- 解码器从 \(z\) 重构数据

为了实现可微的采样过程，使用了重参数化技巧（Reparameterization Trick）：

\[
z = \mu + \sigma \cdot \epsilon, \quad \epsilon \sim \mathcal{N}(0, 1)
\]

### 4.2 VAE 实现

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

class VAE(nn.Module):

    """

    变分自编码器

    """

    def __init__(self, input_dim, hidden_dim, latent_dim):

        super().__init__()

        # 编码器：输出均值和方差

        self.encoder = nn.Sequential(

            nn.Linear(input_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

        )

        self.fc_mu = nn.Linear(hidden_dim, latent_dim)

        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        # 解码器

        self.decoder = nn.Sequential(

            nn.Linear(latent_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, input_dim),

            nn.Sigmoid()

        )

    def encode(self, x):

        h = self.encoder(x)

        mu = self.fc_mu(h)

        logvar = self.fc_logvar(h)

        return mu, logvar

    def reparameterize(self, mu, logvar):

        """重参数化技巧"""

        std = torch.exp(0.5 * logvar)

        eps = torch.randn_like(std)

        return mu + eps * std

    def decode(self, z):

        return self.decoder(z)

    def forward(self, x):

        mu, logvar = self.encode(x)

        z = self.reparameterize(mu, logvar)

        x_recon = self.decode(z)

        return x_recon, mu, logvar

def vae_loss(x_recon, x, mu, logvar, beta=1.0):

    """

    VAE 损失函数

    重构损失 + KL 散度

    """

    # 重构损失

    recon_loss = nn.functional.mse_loss(x_recon, x, reduction='sum')

    # KL 散度：-0.5 * sum(1 + log(sigma^2) - mu^2 - sigma^2)

    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    return recon_loss + beta * kl_loss, recon_loss, kl_loss

# 使用示例

INPUT_DIM = 784

HIDDEN_DIM = 256

LATENT_DIM = 2  # 二维潜在空间便于可视化

model = VAE(INPUT_DIM, HIDDEN_DIM, LATENT_DIM)

# 测试

x = torch.randn(32, 784)

x_recon, mu, logvar = model(x)

print(f"输入形状: {x.shape}")

print(f"重构形状: {x_recon.shape}")

print(f"均值形状: {mu.shape}")       # (32, 2)

print(f"方差形状: {logvar.shape}")   # (32, 2)
```

### 4.3 VAE 生成与可视化

## 实例

```python
import matplotlib.pyplot as plt

def visualize_latent_space(model, dataloader, device):

    """可视化潜在空间"""

    model.eval()

    all_mu = []

    all_labels = []

    with torch.no_grad():

        for batch in dataloader:

            images, labels = batch[0].to(device), batch[1]

            mu, _ = model.encode(images)

            all_mu.append(mu.cpu())

            all_labels.append(labels)

    all_mu = torch.cat(all_mu, dim=0).numpy()

    all_labels = torch.cat(all_labels, dim=0).numpy()

    plt.figure(figsize=(10, 8))

    scatter = plt.scatter(all_mu[:, 0], all_mu[:, 1], c=all_labels,

                          cmap='tab10', alpha=0.5, s=10)

    plt.colorbar(scatter)

    plt.xlabel('Latent Dimension 1')

    plt.ylabel('Latent Dimension 2')

    plt.title('VAE Latent Space')

    plt.show()

def generate_from_latent(model, z, device):

    """从潜在向量生成图像"""

    model.eval()

    with torch.no_grad():

        z = z.to(device)

        generated = model.decode(z)

    return generated

def interpolate_latent(model, z1, z2, steps=10, device):

    """潜在空间插值生成"""

    model.eval()

    # 线性插值

    alphas = torch.linspace(0, 1, steps)

    interpolated = []

    with torch.no_grad():

        for alpha in alphas:

            z = z1 * (1 - alpha) + z2 * alpha

            generated = model.decode(z)

            interpolated.append(generated)

    return torch.cat(interpolated, dim=0)

# 生成新图像

def generate_new_images(model, num_images, latent_dim, device):

    """从随机潜在向量生成新图像"""

    model.eval()

    with torch.no_grad():

        # 从标准正态分布采样

        z = torch.randn(num_images, latent_dim).to(device)

        generated = model.decode(z)

    return generated
```

VAE 的潜在空间是连续的，可以在潜在空间中进行插值，生成平滑过渡的图像。但 VAE 生成的图像通常较模糊，这是因为它优化的是下界而非精确的对数似然。

## 5. 稀疏自编码器

稀疏自编码器（Sparse Autoencoder）在损失函数中加入稀疏性约束，限制潜在向量的激活数量。这使模型能够学习更有意义的特征。

### 5.1 稀疏自编码器实现

实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

class SparseAutoencoder(nn.Module):

    """

    稀疏自编码器

    """

    def __init__(self, input_dim, hidden_dim, latent_dim):

        super().__init__()

        # 编码器

        self.encoder = nn.Sequential(

            nn.Linear(input_dim, hidden_dim),

            nn.ReLU(),

        )

        # 潜在层

        self.bottleneck = nn.Linear(hidden_dim, latent_dim)

        # 解码器

        self.decoder = nn.Sequential(

            nn.Linear(latent_dim, hidden_dim),

            nn.ReLU(),

            nn.Linear(hidden_dim, input_dim),

            nn.Sigmoid()

        )

    def forward(self, x):

        h = self.encoder(x)

        z = self.bottleneck(h)

        z_activated = F.relu(z)  # 稀疏激活

        x_recon = self.decoder(z_activated)

        return x_recon, z_activated

def sparse_loss(z, rho=0.05, beta=1.0):

    """

    稀疏损失：KL 散度

    rho: 目标稀疏度（例如 0.05 表示只有 5% 的神经元应该激活）

    beta: 稀疏项权重

    """

    # 计算平均激活

    rho_hat = torch.mean(z, dim=0)

    # KL 散度

    kl = rho * torch.log(rho / (rho_hat + 1e-8)) + \

         (1 - rho) * torch.log((1 - rho) / (1 - rho_hat + 1e-8))

    return beta * torch.sum(kl)

def total_sparse_loss(x_recon, x, z, rho=0.05, beta=1.0):

    """总损失 = 重构损失 + 稀疏损失"""

    recon_loss = F.mse_loss(x_recon, x)

    sparsity = sparse_loss(z, rho, beta)

    return recon_loss + sparsity
```

## 6. 序列到序列自编码器

对于序列数据（如文本、时间序列），使用 RNN/LSTM 作为编码器和解码器。

### 6.1 序列自编码器实现

## 实例

```python
import torch

import torch.nn as nn

class Seq2SeqAutoencoder(nn.Module):

    """

    序列到序列自编码器：用于序列数据

    """

    def __init__(self, input_size, hidden_size, latent_size, num_layers=2):

        super().__init__()

        # 编码器 LSTM

        self.encoder = nn.LSTM(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            bidirectional=True

        )

        # 潜在空间映射

        # 双向 LSTM 输出是 hidden_size * 2

        self.to_latent = nn.Linear(hidden_size * 2, latent_size)

        self.from_latent = nn.Linear(latent_size, hidden_size * 2)

        # 解码器 LSTM

        self.decoder = nn.LSTM(

            input_size=hidden_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            bidirectional=True

        )

        # 输出映射

        self.output_proj = nn.Linear(hidden_size * 2, input_size)

    def forward(self, x):

        # 编码

        _, (h_n, _) = self.encoder(x)

        # 合并双向最后隐藏状态

        # h_n: (num_layers * 2, batch, hidden_size)

        h_forward = h_n[-2]

        h_backward = h_n[-1]

        h_combined = torch.cat([h_forward, h_backward], dim=-1)

        # 映射到潜在空间

        z = self.to_latent(h_combined)

        # 从潜在空间映射回来

        decoder_init = self.from_latent(z)

        decoder_init = decoder_init.view(2, decoder_init.size(0), -1)  # (2, batch, hidden_size*2)

        # 解码（使用原始输入长度）

        decoder_output, _ = self.decoder(

            x,

            (decoder_init, torch.zeros_like(decoder_init))

        )

        # 输出映射

        output = self.output_proj(decoder_output)

        return output, z

# 使用示例

model = Seq2SeqAutoencoder(

    input_size=128,   # 输入特征维度

    hidden_size=256,  # LSTM 隐藏维度

    latent_size=64,   # 潜在空间维度

    num_layers=2

)

# 测试

x = torch.randn(8, 20, 128)  # (batch, seq_len, input_size)

output, z = model(x)

print(f"输入形状: {x.shape}")        # (8, 20, 128)

print(f"输出形状: {output.shape}")  # (8, 20, 128)

print(f"潜在向量形状: {z.shape}")    # (8, 64)
```

## 7. 自编码器的应用场景

### 7.1 异常检测

自编码器可以用于检测异常数据。正常数据的重构误差小，异常数据的重构误差大：

## 实例

```python
import torch

import torch.nn as nn

def detect_anomalies(model, data_loader, threshold=None, device='cpu'):

    """

    使用自编码器检测异常

    """

    model.eval()

    reconstruction_errors = []

    with torch.no_grad():

        for batch in data_loader:

            images = batch[0].to(device)

            outputs = model(images)

            # 计算重构误差（均方误差）

            errors = torch.mean((outputs - images) ** 2, dim=(1, 2, 3))

            reconstruction_errors.extend(errors.cpu().numpy())

    reconstruction_errors = torch.tensor(reconstruction_errors)

    # 如果没有给定阈值，使用统计方法

    if threshold is None:

        # 使用 95% 分位数

        threshold = torch.quantile(reconstruction_errors, 0.95).item()

    # 标记异常

    anomalies = reconstruction_errors > threshold

    return anomalies, reconstruction_errors, threshold

# 训练异常检测模型

def train_anomaly_detector(normal_data_loader):

    """只用正常数据训练自编码器"""

    model = ConvAutoencoder(channels=1, latent_dim=32)

    criterion = nn.MSELoss()

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    model.train()

    for epoch in range(10):

        for batch in normal_data_loader:

            images = batch[0]

            outputs = model(images)

            loss = criterion(outputs, images)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

    return model
```

### 7.2 图像着色与风格迁移

## 实例

```python
class ColorizationAutoencoder(nn.Module):

    """

    图像着色自编码器

    输入：灰度图像 (batch, 1, H, W)

    输出：彩色图像 (batch, 2, H, W) (ab 色彩空间)

    """

    def __init__(self):

        super().__init__()

        # 编码器：逐步提取特征

        self.encoder = nn.Sequential(

            nn.Conv2d(1, 64, kernel_size=4, stride=2, padding=1),   # H/2

            nn.ReLU(),

            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),  # H/4

            nn.BatchNorm2d(128),

            nn.ReLU(),

            nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1), # H/8

            nn.BatchNorm2d(256),

            nn.ReLU(),

        )

        # 解码器：上采样生成颜色

        self.decoder = nn.Sequential(

            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1),

            nn.BatchNorm2d(128),

            nn.ReLU(),

            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),

            nn.BatchNorm2d(64),

            nn.ReLU(),

            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),

            nn.ReLU(),

            nn.Conv2d(32, 2, kernel_size=3, padding=1),  # 输出 ab 通道

            nn.Sigmoid()  # ab 通道范围 [0, 1]

        )

    def forward(self, x):

        z = self.encoder(x)

        color = self.decoder(z)

        return color
```

### 7.3 数据降维可视化

## 实例

```python
import matplotlib.pyplot as plt

def visualize_latent_2d(model, dataloader, device, num_samples=1000):

    """

    使用自编码器将数据降到 2 维进行可视化

    """

    model.eval()

    all_latents = []

    all_labels = []

    with torch.no_grad():

        count = 0

        for batch in dataloader:

            if count >= num_samples:

                break

            images, labels = batch[0], batch[1]

            images = images.to(device)

            # 如果是 2D AE，直接使用

            # 如果维度更高，需要先投影到 2D

            z = model.encode(images)

            all_latents.append(z.cpu())

            all_labels.append(labels)

            count += images.size(0)

    latents = torch.cat(all_latents, dim=0)[:num_samples].numpy()

    labels = torch.cat(all_labels, dim=0)[:num_samples].numpy()

    plt.figure(figsize=(10, 8))

    scatter = plt.scatter(latents[:, 0], latents[:, 1], c=labels,

                          cmap='tab10', alpha=0.6, s=20)

    plt.colorbar(scatter)

    plt.xlabel('Latent Dimension 1')

    plt.ylabel('Latent Dimension 2')

    plt.title('Autoencoder 2D Latent Space Visualization')

    plt.show()
```

## 8. API 快速参考

### 8.1 常见自编码器类型

| 类型 | 特点 | 适用场景 |
| --- | --- | --- |
| 基础自编码器 | 简单对称结构 | 降维、特征提取 |
| 卷积自编码器 | 使用卷积层保留空间结构 | 图像处理 |
| 去噪自编码器 | 学习去除噪声 | 图像去噪、鲁棒特征 |
| 变分自编码器 | 学习概率分布，可生成新数据 | 生成模型、数据生成 |
| 稀疏自编码器 | 稀疏约束，学习可解释特征 | 特征解耦、可解释性 |
| 序列自编码器 | 使用 RNN/LSTM 处理序列 | 文本、时间序列 |

### 8.2 损失函数选择

| 任务 | 推荐损失函数 |
| --- | --- |
| 图像重构 | MSELoss、SSIMLoss |
| 二值图像 | BCELoss、BCEWithLogitsLoss |
| 文本重构 | CrossEntropyLoss |
| VAE | MSE + KL Divergence |
| 异常检测 | MSE、MAE |

### 8.3 潜在维度选择

```python
数据维度低（<100维）

-> 潜在维度设为 2~10

数据维度中等（100~1000维）

-> 潜在维度设为 10~50

数据维度高（>1000维）

-> 潜在维度设为 50~200

生成任务（VAE）

-> 潜在维度 2~32（便于采样和可视化）

异常检测

-> 潜在维度 16~64（保留足够信息检测异常）
```

---

-

# PyTorch 模型评估与调试

深度学习模型的训练和优化需要系统的评估与调试方法。本节介绍如何分析 Loss 曲线、识别过拟合与欠拟合、使用混淆矩阵评估分类模型，以及常见的调试技巧。

## 1. 损失函数 (Loss) 分析

损失函数是训练过程中的核心指标，它反映了模型预测与真实值的差距。正确分析 Loss 曲线是调试模型的关键。

### 1.1 训练与验证 Loss 对比

通过对比训练 Loss 和验证 Loss，可以判断模型的状态：

- 训练 Loss 下降，验证 Loss 下降：正常，表明模型正在学习

- 训练 Loss 下降，验证 Loss 稳定或上升：过拟合，需要正则化

- 训练 Loss 不下降：学习率问题或模型架构问题

- 训练 Loss 震荡：学习率过大或 batch size 过小

### 1.2 Loss 曲线可视化

## 实例

```python
import matplotlib.pyplot as plt

import numpy as np

def plot_training_history(history):

    """

    绘制训练历史

    history: 包含 'train_loss', 'val_loss', 'train_acc', 'val_acc' 的字典

    """

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Loss 曲线

    axes[0].plot(history['train_loss'], label='Train Loss', alpha=0.8)

    axes[0].plot(history['val_loss'], label='Val Loss', alpha=0.8)

    axes[0].set_xlabel('Epoch')

    axes[0].set_ylabel('Loss')

    axes[0].set_title('Training and Validation Loss')

    axes[0].legend()

    axes[0].grid(True, alpha=0.3)

    # Accuracy 曲线

    axes[1].plot(history['train_acc'], label='Train Acc', alpha=0.8)

    axes[1].plot(history['val_acc'], label='Val Acc', alpha=0.8)

    axes[1].set_xlabel('Epoch')

    axes[1].set_ylabel('Accuracy')

    axes[1].set_title('Training and Validation Accuracy')

    axes[1].legend()

    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    plt.show()

# 模拟训练数据

history = {

    'train_loss': np.linspace(2.0, 0.2, 50) + np.random.normal(0, 0.05, 50),

    'val_loss': np.linspace(2.0, 0.3, 50) + np.random.normal(0, 0.08, 50),

    'train_acc': np.linspace(0.3, 0.95, 50),

    'val_acc': np.linspace(0.3, 0.88, 50),

}

plot_training_history(history)
```

### 1.3 识别过拟合

当验证 Loss 开始上升而训练 Loss 继续下降时，就是过拟合的开始。此时模型开始"记忆"训练数据，而非学习通用模式。

## 实例

```python
import matplotlib.pyplot as plt

import numpy as np

def detect_overfitting(history, patience=5):

    """

    检测过拟合

    patience: 连续多少个 epoch 验证 loss 上升才停止训练

    """

    val_loss = history['val_loss']

    best_loss = float('inf')

    best_epoch = 0

    early_stop_epoch = None

    for epoch in range(patience, len(val_loss)):

        # 检查最近 patience 个 epoch

        recent_losses = val_loss[epoch - patience:epoch]

        current_loss = val_loss[epoch]

        # 如果当前 loss 比最近最低 loss 高

        if min(recent_losses) < current_loss:

            early_stop_epoch = epoch

            break

        if current_loss < best_loss:

            best_loss = current_loss

            best_epoch = epoch

    if early_stop_epoch:

        print(f"检测到过拟合！最佳 epoch: {best_epoch}, 应在 epoch {early_stop_epoch} 停止")

    else:

        print("未检测到过拟合")

    return early_stop_epoch, best_epoch

# 过拟合示例

overfitting_history = {

    'train_loss': np.linspace(1.5, 0.1, 30),

    'val_loss': np.concatenate([np.linspace(1.5, 0.3, 15), np.linspace(0.3, 0.8, 15)]),

}

detect_overfitting(overfitting_history)
```

## 2. 过拟合与欠拟合处理

### 2.1 过拟合解决方案

| 方法 | 描述 | 代码实现 |
| --- | --- | --- |
| 增加数据量 | 收集更多训练数据 | 数据增强 |
| Dropout | 随机丢弃神经元 | nn.Dropout(0.5) |
| 权重衰减 | L2 正则化 | weight_decay=1e-4 |
| 早停 (Early Stopping) | 验证 loss 停止下降时停止训练 | patience 参数 |
| 减少模型复杂度 | 减少层数或神经元 | 降低 hidden_size |
| 数据增强 | 随机变换增加数据多样性 | 旋转、翻转、裁剪 |

### 2.2 欠拟合解决方案

| 方法 | 描述 |
| --- | --- |
| 增加模型复杂度 | 增加层数或神经元数量 |
| 训练更久 | 增加训练轮数 |
| 减小正则化 | 降低 Dropout 或 weight_decay |
| 调整学习率 | 尝试更大的学习率 |

### 2.3 早停机制实现

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

class EarlyStopping:

    """

    早停机制：验证 loss 连续不下降时停止训练

    """

    def __init__(self, patience=7, min_delta=0, mode='min'):

        """

        patience: 连续多少个 epoch 没有改善就停止

        min_delta: 被认为是改善的最小变化量

        mode: 'min' 或 'max'，指标是越小越好还是越大越好

        """

        self.patience = patience

        self.min_delta = min_delta

        self.mode = mode

        self.counter = 0

        self.best_score = None

        self.early_stop = False

    def __call__(self, val_loss):

        score = -val_loss if self.mode == 'min' else val_loss

        if self.best_score is None:

            self.best_score = score

        elif score < self.best_score + self.min_delta:

            self.counter += 1

            if self.counter >= self.patience:

                self.early_stop = True

        else:

            self.best_score = score

            self.counter = 0

        return self.early_stop

# 使用早停

def train_with_early_stopping(model, train_loader, val_loader, patience=7):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    early_stopping = EarlyStopping(patience=patience, mode='min')

    best_val_loss = float('inf')

    best_model_state = None

    for epoch in range(100):

        # 训练

        model.train()

        train_loss = 0

        for inputs, labels in train_loader:

            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            train_loss += loss.item()

        # 验证

        model.eval()

        val_loss = 0

        with torch.no_grad():

            for inputs, labels in val_loader:

                inputs, labels = inputs.to(device), labels.to(device)

                outputs = model(inputs)

                loss = criterion(outputs, labels)

                val_loss += loss.item()

        val_loss /= len(val_loader)

        print(f"Epoch {epoch+1}: Train Loss={train_loss:.4f}, Val Loss={val_loss:.4f}")

        # 早停检查

        if early_stopping(val_loss):

            print(f"早停触发！连续 {patience} 个 epoch 验证 loss 未下降")

        # 保存最佳模型

        if val_loss < best_val_loss:

            best_val_loss = val_loss

            best_model_state = model.state_dict().copy()

    # 恢复最佳模型

    model.load_state_dict(best_model_state)

    return model
```

## 3. 混淆矩阵 (Confusion Matrix)

混淆矩阵是评估分类模型的重要工具，它展示了模型预测与真实标签的关系。

### 3.1 混淆矩阵计算

## 实例

```python
import torch

import numpy as np

from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt

import seaborn as sns

def calculate_confusion_matrix(model, dataloader, device, num_classes):

    """

    计算混淆矩阵

    """

    model.eval()

    all_preds = []

    all_labels = []

    with torch.no_grad():

        for inputs, labels in dataloader:

            inputs = inputs.to(device)

            outputs = model(inputs)

            _, preds = torch.max(outputs, 1)

            all_preds.extend(preds.cpu().numpy())

            all_labels.extend(labels.numpy())

    cm = confusion_matrix(all_labels, all_preds)

    return cm

def plot_confusion_matrix(cm, class_names):

    """

    绘制混淆矩阵

    """

    plt.figure(figsize=(10, 8))

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',

                xticklabels=class_names, yticklabels=class_names)

    plt.xlabel('Predicted Label')

    plt.ylabel('True Label')

    plt.title('Confusion Matrix')

    plt.tight_layout()

    plt.show()

# 使用示例

# 假设有 10 个类别

class_names = [f'Class {i}' for i in range(10)]

cm = np.array([

    [45, 1, 0, 0, 0, 0, 2, 1, 1, 0],

    [0, 42, 2, 0, 0, 0, 0, 3, 2, 1],

    [1, 1, 38, 3, 0, 0, 0, 2, 3, 2],

    [0, 0, 1, 41, 2, 1, 0, 1, 1, 3],

    [0, 0, 0, 1, 44, 0, 1, 0, 2, 2],

    [1, 0, 0, 0, 0, 43, 2, 1, 1, 2],

    [2, 1, 0, 0, 1, 1, 39, 2, 2, 2],

    [0, 2, 1, 1, 0, 0, 1, 40, 3, 2],

    [1, 2, 2, 0, 1, 1, 1, 2, 36, 4],

    [0, 1, 1, 2, 2, 2, 2, 1, 2, 37],

])

plot_confusion_matrix(cm, class_names)
```

### 3.2 分类评估指标

从混淆矩阵可以计算多种评估指标：

## 实例

```python
import numpy as np

def classification_metrics(cm):

    """

    从混淆矩阵计算各种评估指标

    """

    # 准确率 (Accuracy)

    accuracy = np.trace(cm) / np.sum(cm)

    # 对每类计算精确率、召回率、F1

    num_classes = cm.shape[0]

    precisions = []

    recalls = []

    f1s = []

    for i in range(num_classes):

        tp = cm[i, i]

        fp = np.sum(cm[:, i]) - tp

        fn = np.sum(cm[i, :]) - tp

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0

        recall = tp / (tp + fn) if (tp + fn) > 0 else 0

        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        precisions.append(precision)

        recalls.append(recall)

        f1s.append(f1)

    # 宏平均 (Macro Average)

    macro_precision = np.mean(precisions)

    macro_recall = np.mean(recalls)

    macro_f1 = np.mean(f1s)

    # 加权平均 (Weighted Average)

    class_counts = np.sum(cm, axis=1)

    weights = class_counts / np.sum(class_counts)

    weighted_precision = np.average(precisions, weights=weights)

    weighted_recall = np.average(recalls, weights=weights)

    weighted_f1 = np.average(f1s, weights=weights)

    return {

        'accuracy': accuracy,

        'macro_precision': macro_precision,

        'macro_recall': macro_recall,

        'macro_f1': macro_f1,

        'weighted_precision': weighted_precision,

        'weighted_recall': weighted_recall,

        'weighted_f1': weighted_f1,

    }

# 计算指标

metrics = classification_metrics(cm)

print("=" * 50)

print("分类评估指标")

print("=" * 50)

print(f"准确率 (Accuracy): {metrics['accuracy']:.4f}")

print(f"宏平均精确率 (Macro Precision): {metrics['macro_precision']:.4f}")

print(f"宏平均召回率 (Macro Recall): {metrics['macro_recall']:.4f}")

print(f"宏平均 F1 (Macro F1): {metrics['macro_f1']:.4f}")

print(f"加权精确率 (Weighted Precision): {metrics['weighted_precision']:.4f}")

print(f"加权召回率 (Weighted Recall): {metrics['weighted_recall']:.4f}")

print(f"加权 F1 (Weighted F1): {metrics['weighted_f1']:.4f}")
```

### 3.3 分类报告

## 实例

```python
from sklearn.metrics import classification_report

# 使用 sklearn 的分类报告

y_true = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 10  # 模拟真实标签

y_pred = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8] * 10  # 模拟预测

report = classification_report(y_true, y_pred, digits=4)

print(report)
```

## 4. 学习率调度

学习率是训练深度学习模型最重要的超参数之一。合适的学习率调度可以显著提升训练效果。

### 4.1 学习率调度策略

| 策略 | 描述 | 适用场景 |
| --- | --- | --- |
| StepLR | 固定步长衰减 | 已知最优学习率时 |
| MultiStepLR | 指定 epoch 衰减 | 非均匀衰减 |
| CosineAnnealingLR | 余弦退火 | 平滑收敛 |
| ReduceLROnPlateau | 验证 loss 不降时衰减 | 自动调优 |
| Warmup | 先增后减 | 稳定训练初期 |

### 4.2 学习率调度实现

## 实例

```python
import torch

import torch.optim as optim

import matplotlib.pyplot as plt

# 模拟训练 epoch

epochs = 50

# 1. Step LR：每 10 个 epoch 衰减一半

scheduler_step = optim.lr_scheduler.StepLR(

    optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1),

    step_size=10, gamma=0.5

)

# 2. MultiStep LR：指定 epoch 衰减

scheduler_multistep = optim.lr_scheduler.MultiStepLR(

    optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1),

    milestones=[15, 30, 45], gamma=0.1

)

# 3. Cosine Annealing

scheduler_cosine = optim.lr_scheduler.CosineAnnealingLR(

    optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1),

    T_max=50

)

# 4. ReduceLROnPlateau

scheduler_plateau = optim.lr_scheduler.ReduceLROnPlateau(

    optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1),

    mode='min', factor=0.5, patience=5

)

# 绘制学习率曲线

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Step LR

lr_history = []

for _ in range(epochs):

    lr_history.append(optimizer.param_groups[0]['lr'])

    scheduler_step.step()

axes[0, 0].plot(lr_history)

axes[0, 0].set_title('Step LR')

# 重新初始化

optimizer = optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1)

scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[15, 30, 45], gamma=0.1)

lr_history = []

for _ in range(epochs):

    lr_history.append(optimizer.param_groups[0]['lr'])

    scheduler.step()

axes[0, 1].plot(lr_history)

axes[0, 1].set_title('MultiStep LR')

# Cosine

optimizer = optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1)

scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)

lr_history = []

for _ in range(epochs):

    lr_history.append(optimizer.param_groups[0]['lr'])

    scheduler.step()

axes[1, 0].plot(lr_history)

axes[1, 0].set_title('Cosine Annealing LR')

# Warmup + Cosine

def warmup_cosine(optimizer, warmup_epochs, total_epochs, min_lr=1e-6):

    def lr_lambda(epoch):

        if epoch < warmup_epochs:

            return epoch / warmup_epochs

        return min_lr + 0.5 * (1 - min_lr) * (1 + np.cos(np.pi * (epoch - warmup_epochs) / (total_epochs - warmup_epochs)))

    return optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

optimizer = optim.SGD(torch.nn.Linear(10, 10).parameters(), lr=0.1)

scheduler = warmup_cosine(optimizer, warmup_epochs=5, total_epochs=50)

lr_history = []

for _ in range(epochs):

    lr_history.append(optimizer.param_groups[0]['lr'])

    scheduler.step()

axes[1, 1].plot(lr_history)

axes[1, 1].set_title('Warmup + Cosine')

for ax in axes.flat:

    ax.set_xlabel('Epoch')

    ax.set_ylabel('Learning Rate')

    ax.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()
```

## 5. 梯度问题诊断

### 5.1 梯度消失与爆炸

实例

```python
import torch

import torch.nn as nn

def analyze_gradients(model):

    """

    分析模型各层梯度

    """

    grad_stats = {}

    for name, param in model.named_parameters():

        if param.grad is not None:

            grad = param.grad

            grad_stats[name] = {

                'mean': grad.mean().item(),

                'std': grad.std().item(),

                'max': grad.abs().max().item(),

                'min': grad.abs().min().item(),

                'norm': grad.norm().item(),

            }

    return grad_stats

def detect_gradient_issues(model):

    """

    检测梯度问题

    """

    issues = []

    grad_norms = []

    for param in model.parameters():

        if param.grad is not None:

            grad_norms.append(param.grad.norm().item())

    avg_grad_norm = sum(grad_norms) / len(grad_norms) if grad_norms else 0

    if avg_grad_norm < 1e-7:

        issues.append("梯度消失：梯度太小，模型可能无法学习")

    elif avg_grad_norm > 100:

        issues.append("梯度爆炸：梯度太大，训练不稳定")

    return issues, avg_grad_norm

# 示例：检测梯度

model = nn.Sequential(

    nn.Linear(100, 50),

    nn.ReLU(),

    nn.Linear(50, 50),

    nn.ReLU(),

    nn.Linear(50, 10)

)

# 模拟前向和反向传播

x = torch.randn(32, 100)

y = model(x)

loss = y.sum()

loss.backward()

issues, avg_norm = detect_gradient_issues(model)

print(f"平均梯度范数: {avg_norm:.6f}")

if issues:

    for issue in issues:

        print(f"警告: {issue}")

else:

    print("梯度状态正常")
```

### 5.2 梯度裁剪

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import torch.nn.utils as utils

# 梯度裁剪示例

def train_with_gradient_clipping(model, dataloader, max_norm=1.0):

    """

    使用梯度裁剪训练

    max_norm: 最大梯度范数，超过此值的梯度会被裁剪

    """

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    model.train()

    for inputs, labels in dataloader:

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        loss.backward()

        # 梯度裁剪：防止梯度爆炸

        utils.clip_grad_norm_(model.parameters(), max_norm=max_norm)

        optimizer.step()

    return model

# 逐元素裁剪（更保守）

def clip_grad_by_value(model, clip_value=1.0):

    """

    按值裁剪梯度

    """

    for param in model.parameters():

        if param.grad is not None:

            param.grad.data.clamp_(min=-clip_value, max=clip_value)
```

## 6. 模型性能分析

### 6.1 计算参数量与 FLOPs

## 实例

```python
import torch

import torch.nn as nn

from thop import profile

def count_parameters(model):

    """计算模型可训练参数数量"""

    total = sum(p.numel() for p in model.parameters())

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)

    return total, trainable

def count_flops(model, input_size=(1, 3, 224, 224)):

    """计算 FLOPs（需要安装 thop 库）"""

    input_tensor = torch.randn(input_size)

    flops, params = profile(model, inputs=(input_tensor,), verbose=False)

    return flops, params

# 示例：统计模型

model = nn.Sequential(

    nn.Conv2d(3, 64, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.MaxPool2d(2),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.MaxPool2d(2),

    nn.Conv2d(128, 256, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.AdaptiveAvgPool2d(1),

    nn.Flatten(),

    nn.Linear(256, 10)

)

total, trainable = count_parameters(model)

print(f"总参数: {total:,}")

print(f"可训练参数: {trainable:,}")

print(f"模型大小: {total * 4 / 1024 / 1024:.2f} MB")

# FLOPs 计算

try:

    flops, _ = count_flops(model)

    print(f"FLOPs: {flops / 1e9:.2f} G")

except ImportError:

    print("请安装 thop 库: pip install thop")
```

### 6.2 推理速度测试

实例

```python
import torch

import time

def measure_inference_speed(model, input_size, device='cuda', num_iterations=100):

    """

    测量推理速度

    """

    model.eval()

    model = model.to(device)

    # 预热

    dummy_input = torch.randn(input_size).to(device)

    with torch.no_grad():

        for _ in range(10):

            _ = model(dummy_input)

    # 计时

    start = time.time()

    with torch.no_grad():

        for _ in range(num_iterations):

            _ = model(dummy_input)

    if device == 'cuda':

        torch.cuda.synchronize()

    end = time.time()

    avg_time = (end - start) / num_iterations * 1000  # ms

    return avg_time

# 使用示例

model = nn.Sequential(

    nn.Conv2d(3, 64, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.Conv2d(64, 64, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.AdaptiveAvgPool2d(1),

    nn.Flatten(),

    nn.Linear(64, 10)

)

# CPU 推理速度

cpu_time = measure_inference_speed(model, (1, 3, 224, 224), device='cpu')

print(f"CPU 推理时间: {cpu_time:.2f} ms/图像")

# GPU 推理速度（如有 CUDA）

if torch.cuda.is_available():

    gpu_time = measure_inference_speed(model, (1, 3, 224, 224), device='cuda')

    print(f"GPU 推理时间: {gpu_time:.2f} ms/图像")
```

### 6.3 显存占用分析

## 实例

```python
import torch

def analyze_memory(model, input_size):

    """

    分析模型显存占用

    """

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model.to(device)

    # 创建输入

    x = torch.randn(input_size).to(device)

    # 清理缓存

    if torch.cuda.is_available():

        torch.cuda.empty_cache()

        torch.cuda.reset_peak_memory_stats()

    # 前向传播

    with torch.no_grad():

        output = model(x)

    # 获取显存统计

    if torch.cuda.is_available():

        allocated = torch.cuda.memory_allocated() / 1024**2  # MB

        reserved = torch.cuda.memory_reserved() / 1024**2

        max_allocated = torch.cuda.max_memory_allocated() / 1024**2

        print(f"当前分配: {allocated:.2f} MB")

        print(f"缓存占用: {reserved:.2f} MB")

        print(f"峰值占用: {max_allocated:.2f} MB")

    else:

        print("需要 CUDA 支持")

    return output

# 使用示例

model = nn.Sequential(

    nn.Conv2d(3, 64, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),

    nn.ReLU(),

    nn.Conv2d(128, 256, kernel_size=3, padding=1),

    nn.ReLU(),

)

analyze_memory(model, (8, 3, 224, 224))
```

## 7. 常见问题与调试技巧

### 7.1 训练问题速查

| 症状 | 可能原因 | 解决方案 |
| --- | --- | --- |
| Loss 不下降 | 学习率过小/过大、梯度问题 | 调整学习率、检查梯度 |
| Loss 震荡 | 学习率过大、batch size 小 | 减小学习率、增大 batch |
| NaN 出现 | 除零、log(0)、梯度爆炸 | 添加 epsilon、梯度裁剪 |
| 过拟合 | 模型复杂、数据不足 | 增加数据、加正则化 |
| 欠拟合 | 模型太简单、训练不足 | 增大模型、训练更久 |
| 显存不足 | batch size 大、模型大 | 减小 batch、梯度累积 |

### 7.2 调试技巧集合

## 实例

```python
import torch

import random

import numpy as np

def set_seed(seed=42):

    """设置随机种子，保证结果可复现"""

    random.seed(seed)

    np.random.seed(seed)

    torch.manual_seed(seed)

    torch.cuda.manual_seed(seed)

    torch.cuda.manual_seed_all(seed)

    torch.backends.cudnn.deterministic = True

    torch.backends.cudnn.benchmark = False

def debug_forward(model, x):

    """调试前向传播，检查各层输出"""

    print("=" * 50)

    print("前向传播调试")

    print("=" * 50)

    for name, layer in model.named_children():

        x = layer(x)

        if hasattr(x, 'shape'):

            print(f"{name}: shape={x.shape}, ", end='')

            if hasattr(x, 'mean'):

                print(f"mean={x.mean().item():.4f}, std={x.std().item():.4f}")

            if torch.isnan(x).any():

                print(f"  &#x26a0;&#xfe0f; 检测到 NaN!")

            if torch.isinf(x).any():

                print(f"  &#x26a0;&#xfe0f; 检测到 Inf!")

    print("=" * 50)

def debug_backward(model):

    """调试反向传播，检查梯度"""

    print("=" * 50)

    print("反向传播调试")

    print("=" * 50)

    for name, param in model.named_parameters():

        if param.grad is not None:

            grad_norm = param.grad.norm().item()

            if torch.isnan(param.grad).any():

                print(f"{name}: &#x26a0;&#xfe0f; 梯度 NaN!")

            elif torch.isinf(param.grad).any():

                print(f"{name}: &#x26a0;&#xfe0f; 梯度 Inf!")

            elif grad_norm > 10:

                print(f"{name}: &#x26a0;&#xfe0f; 梯度爆炸! norm={grad_norm:.2f}")

            elif grad_norm < 1e-7:

                print(f"{name}: &#x26a0;&#xfe0f; 梯度消失! norm={grad_norm:.2e}")

            else:

                print(f"{name}: 正常 norm={grad_norm:.4f}")

    print("=" * 50)

# 使用示例

set_seed(42)

model = nn.Sequential(

    nn.Linear(10, 20),

    nn.ReLU(),

    nn.Linear(20, 20),

    nn.ReLU(),

    nn.Linear(20, 5)

)

x = torch.randn(2, 10)

y = model(x)

debug_forward(model, x)

loss = y.sum()

loss.backward()

debug_backward(model)
```

## 8. PyTorch Profiler 使用

PyTorch Profiler 是官方提供的性能分析工具，可以分析模型各部分的耗时和显存占用。

### 8.1 Profiler 基本使用

## 实例

```python
import torch

import torch.nn as nn

from torch.profiler import profile, ProfilerActivity, schedule

# 简单模型

model = nn.Sequential(

    nn.Conv2d(3, 64, 3, padding=1),

    nn.ReLU(),

    nn.Conv2d(64, 64, 3, padding=1),

    nn.ReLU(),

    nn.AdaptiveAvgPool2d(1),

    nn.Flatten(),

    nn.Linear(64, 10)

).cuda()

optimizer = torch.optim.Adam(model.parameters())

criterion = nn.CrossEntropyLoss()

# 使用 profiler

with profile(

    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],

    schedule=schedule(wait=1, warmup=1, active=3, repeat=1),

    on_trace_ready=torch.profiler.tensorboard_trace_handler('./logs'),

    record_shapes=True,

    profile_memory=True,

    with_stack=True

) as prof:

    for step in range(5):

        inputs = torch.randn(8, 3, 224, 224).cuda()

        labels = torch.randint(0, 10, (8,)).cuda()

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        prof.step()

# 打印结果

print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))
```

### 8.2 可视化 Profiler 结果

## 实例

```python
# 导出 Chrome 跟踪文件

# 生成的 ./logs 目录可以用 Chrome 浏览器打开查看

# 或者直接打印各项指标

print("=" * 80)

print("CPU 时间 Top 10:")

print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))

print("\n" + "=" * 80)

print("CUDA 时间 Top 10:")

print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))

print("\n" + "=" * 80)

print("显存占用 Top 10:")

print(prof.key_averages().table(sort_by="self_cuda_memory_usage", row_limit=10))
```

---

-

# PyTorch torchtext

虽然 PyTorch 生态中有 `torchvision` 处理图像数据、`torchaudio` 处理音频数据，但在文本处理领域，官方曾提供的 `torchtext` 库经历了一些变化。本节介绍如何使用各种方法进行文本数据的预处理、构建词表、数据加载等操作。

注意：torchtext 库经历了一些重构。推荐使用 torchtext.legacy 或自行构建文本处理管线。最新的 torchtext 版本已经回归并提供了更现代的 API。

## 1. 文本数据预处理基础

文本预处理是 NLP 任务的第一步，包括分词、建立词表、编码等操作。

### 1.1 基本文本处理流程

## 实例

```python
import re

from collections import Counter

class SimpleTokenizer:

    """

    简单分词器：按空格和标点分词

    """

    def __init__(self):

        # 标点符号映射

        self.punctuation = str.maketrans('', '', '.,!?;:"\'-()[]{}')

    def tokenize(self, text):

        # 转小写

        text = text.lower()

        # 移除标点

        text = text.translate(self.punctuation)

        # 分词

        tokens = text.split()

        return tokens

class Vocabulary:

    """

    词表构建

    """

    def __init__(self, min_freq=2, max_size=10000):

        self.min_freq = min_freq

        self.max_size = max_size

        self.word2idx = {'<PAD>': 0, '<UNK>': 1}

        self.idx2word = {0: '<PAD>', 1: '<UNK>'}

        self.word_count = Counter()

    def build_vocab(self, texts):

        """从文本列表构建词表"""

        tokenizer = SimpleTokenizer()

        # 统计词频

        for text in texts:

            tokens = tokenizer.tokenize(text)

            self.word_count.update(tokens)

        # 构建词表

        for word, count in self.word_count.most_common(self.max_size):

            if count < self.min_freq:

                break

            if word not in self.word2idx:

                idx = len(self.word2idx)

                self.word2idx[word] = idx

                self.idx2word[idx] = word

        print(f"词表大小: {len(self.word2idx)}")

    def encode(self, text, max_len=50):

        """编码文本为索引序列"""

        tokenizer = SimpleTokenizer()

        tokens = tokenizer.tokenize(text)[:max_len]

        # 编码

        indices = [

            self.word2idx.get(token, self.word2idx['<UNK>'])

            for token in tokens

        ]

        # 补零

        if len(indices) < max_len:

            indices += [self.word2idx['<PAD>']] * (max_len - len(indices))

        return indices

    def decode(self, indices):

        """解码索引序列为文本"""

        tokens = [self.idx2word.get(idx, '<UNK>') for idx in indices]

        return ' '.join(tokens)

# 使用示例

texts = [

    "Hello world",

    "This is a test",

    "PyTorch is great for deep learning",

    "Natural language processing is fun",

    "Deep learning enables many applications",

]

vocab = Vocabulary(min_freq=1, max_size=100)

vocab.build_vocab(texts)

# 编码

encoded = vocab.encode("Hello deep learning world!", max_len=10)

print(f"编码结果: {encoded}")

# 解码

decoded = vocab.decode(encoded)

print(f"解码结果: {decoded}")
```

## 2. 使用 torchtext (Legacy)

如果已安装 torchtext，可以使用 legacy 模块进行文本处理。

### 2.1 安装与导入

## 实例

```python
# 安装 torchtext

# pip install torchtext

# 导入 legacy 模块

try:

    import torchtext

    from torchtext.legacy import data

    from torchtext.legacy import datasets

    print(f"torchtext 版本: {torchtext.__version__}")

    TORCHTEXT_AVAILABLE = True

except ImportError:

    print("torchtext 未安装，使用自定义实现")

    TORCHTEXT_AVAILABLE = False

# 或者尝试新版

try:

    from torchtext import transforms

    from torchtext.datasets import AG_NEWS

    print("新版 torchtext 可用")

except ImportError:

    print("新版 torchtext 不可用")
```

### 2.2 Field 和 Dataset

## 实例

```python
# 使用 torchtext.legacy

from torchtext.legacy import data

from torchtext.legacy import datasets

from torchtext.legacy.data import Field, TabularDataset, BucketIterator

# 定义字段

TEXT = Field(

    tokenize='spacy',           # 使用 spacy 分词

    tokenizer_language='en_core_web_sm',

    lower=True,                 # 转小写

    include_lengths=True,       # 返回序列长度

    batch_first=True            # batch 维度在前

)

LABEL = Field(

    sequential=False,

    use_vocab=False,

    dtype=torch.long

)

# 定义数据集

# 假设有 CSV 文件格式: label,text

# 1,This is a positive review

# 0,This is a negative review

# 或使用内置数据集（如 IMDB）

# train_data, test_data = datasets.IMDB.splits(TEXT, LABEL)

print("Field 和 Dataset 配置完成")
```

### 2.3 词表构建与迭代器

## 实例

```python
# 构建词表

# TEXT.build_vocab(train_data, vectors="glove.6B.100d", max_size=10000)

# 创建迭代器

# train_iterator, test_iterator = BucketIterator.splits(

#     (train_data, test_data),

#     batch_size=32,

#     sort_within_batch=True,

#     device=torch.device('cuda')

# )

# 迭代训练

# for batch in train_iterator:

#     text, lengths = batch.text

#     labels = batch.label

#     # 训练代码

print("词表和迭代器配置完成")
```

### 3. 自定义 NLP 数据管线

推荐使用更灵活的自定义数据处理方式，不依赖 torchtext。

### 3.1 数据集类实现

## 实例

```python
import torch

from torch.utils.data import Dataset, DataLoader

from collections import Counter

import re

class TextDataset(Dataset):

    """

    文本数据集

    """

    def __init__(self, texts, labels, vocab=None, max_len=128, min_freq=2):

        self.texts = texts

        self.labels = labels

        self.max_len = max_len

        # 构建或使用已有词表

        if vocab is None:

            self.vocab = self._build_vocab(texts, min_freq)

        else:

            self.vocab = vocab

    def _build_vocab(self, texts, min_freq):

        """构建词表"""

        word_counts = Counter()

        for text in texts:

            tokens = self._tokenize(text)

            word_counts.update(tokens)

        # 创建词表

        word2idx = {'<PAD>': 0, '<UNK>': 1}

        for word, count in word_counts.items():

            if count >= min_freq:

                word2idx[word] = len(word2idx)

        return word2idx

    def _tokenize(self, text):

        """简单分词"""

        # 转小写

        text = text.lower()

        # 移除特殊字符，保留字母数字和空格

        text = re.sub(r'[^a-z0-9\s]', ' ', text)

        # 分词

        tokens = text.split()

        return tokens

    def _encode(self, text):

        """编码文本"""

        tokens = self._tokenize(text)[:self.max_len]

        indices = [

            self.vocab.get(token, self.vocab['<UNK>'])

            for token in tokens

        ]

        # 补零

        if len(indices) < self.max_len:

            indices += [self.vocab['<PAD>']] * (self.max_len - len(indices))

        return indices

    def __len__(self):

        return len(self.texts)

    def __getitem__(self, idx):

        text = self.texts[idx]

        label = self.labels[idx]

        encoded = self._encode(text)

        return torch.tensor(encoded, dtype=torch.long), torch.tensor(label, dtype=torch.long)

# 使用示例

texts = [

    "This is a great movie",

    "I hated this film",

    "Amazing performance",

    "Terrible acting",

    "Highly recommend",

]

labels = [1, 0, 1, 0, 1]

dataset = TextDataset(texts, labels, max_len=10)

print(f"数据集大小: {len(dataset)}")

print(f"词表大小: {len(dataset.vocab)}")

# 获取样本

text, label = dataset[0]

print(f"文本编码: {text[:5]}...")

print(f"标签: {label}")
```

### 3.2 高级分词器

## 实例

```python
# 使用 spacy 进行高级分词

def tokenize_with_spacy(text):

    """使用 spacy 分词"""

    try:

        import spacy

        nlp = spacy.load("en_core_web_sm")

        doc = nlp(text)

        return [token.text for token in doc]

    except ImportError:

        print("spacy 未安装，使用简单分词")

        return text.lower().split()

# 使用 nltk 进行分词和词干提取

def tokenize_with_nltk(text):

    """使用 nltk 分词"""

    try:

        import nltk

        from nltk.tokenize import word_tokenize

        from nltk.stem import PorterStemmer

        # 分词

        tokens = word_tokenize(text.lower())

        # 可选：词干提取

        stemmer = PorterStemmer()

        tokens = [stemmer.stem(token) for token in tokens if token.isalnum()]

        return tokens

    except ImportError:

        return text.lower().split()

# 使用 SentencePiece 进行子词分词

class SentencePieceTokenizer:

    """

    使用 SentencePiece 进行子词分词

    """

    def __init__(self, model_path=None):

        self.model_path = model_path

        self.sp = None

    def train(self, texts, vocab_size=10000):

        """训练 SentencePiece 模型"""

        try:

            import sentencepiece as spm

            import tempfile

            # 写入临时文件

            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:

                for text in texts:

                    f.write(text + '\n')

                temp_file = f.name

            # 训练

            spm.SentencePieceTrainer.train(

                input=temp_file,

                model_prefix='spm_model',

                vocab_size=vocab_size,

                character_coverage=1.0,

                model_type='unigram',

            )

            self.sp = spm.SentencePieceProcessor()

            self.sp.load('spm_model.model')

        except ImportError:

            print("sentencepiece 未安装")

    def encode(self, text):

        if self.sp:

            return self.sp.encode(text, out_type=str)

        return text.split()

    def decode(self, ids):

        if self.sp:

            return self.sp.decode(ids)

        return ' '.join(ids)
```

### 3.3 完整数据加载器

## 实例

```python
import torch

from torch.utils.data import Dataset, DataLoader

from collections import Counter

class NLPDataset(Dataset):

    """

    完整的 NLP 数据集类

    支持变长序列、词表构建、批量填充

    """

    def __init__(self, texts, labels, min_freq=2, max_vocab=30000):

        self.texts = texts

        self.labels = labels

        self.min_freq = min_freq

        # 构建词表

        self.word2idx, self.idx2word = self._build_vocab(texts, max_vocab)

        self.pad_idx = self.word2idx['<PAD>']

        self.unk_idx = self.word2idx['<UNK>']

    def _tokenize(self, text):

        text = text.lower()

        text = re.sub(r'[^a-z0-9\s]', ' ', text)

        return text.split()

    def _build_vocab(self, texts, max_vocab):

        """构建词表"""

        counter = Counter()

        for text in texts:

            tokens = self._tokenize(text)

            counter.update(tokens)

        # 构建词表

        word2idx = {'<PAD>': 0, '<UNK>': 1}

        idx2word = {0: '<PAD>', 1: '<UNK>'}

        for word, count in counter.most_common(max_vocab):

            if count >= self.min_freq and word not in word2idx:

                idx = len(word2idx)

                word2idx[word] = idx

                idx2word[idx] = word

        return word2idx, idx2word

    def __len__(self):

        return len(self.texts)

    def __getitem__(self, idx):

        text = self.texts[idx]

        tokens = self._tokenize(text)

        indices = [self.word2idx.get(t, self.unk_idx) for t in tokens]

        return {

            'input': indices,

            'label': self.labels[idx],

            'length': len(indices)

        }

def collate_fn(batch, pad_idx=0):

    """

    自定义 collate 函数：处理变长序列

    """

    # 按长度降序排序

    batch.sort(key=lambda x: x['length'], reverse=True)

    texts = [item['input'] for item in batch]

    labels = [item['label'] for item in batch]

    lengths = [item['length'] for item in batch]

    # 填充到相同长度

    max_len = max(lengths)

    padded = [text + [pad_idx] * (max_len - len(text)) for text in texts]

    return {

        'input': torch.tensor(padded, dtype=torch.long),

        'labels': torch.tensor(labels, dtype=torch.long),

        'lengths': torch.tensor(lengths, dtype=torch.long)

    }

# 使用 DataLoader

def create_dataloader(texts, labels, batch_size=32, shuffle=True):

    """创建数据加载器"""

    dataset = NLPDataset(texts, labels)

    pad_idx = dataset.pad_idx

    dataloader = DataLoader(

        dataset,

        batch_size=batch_size,

        shuffle=shuffle,

        collate_fn=lambda b: collate_fn(b, pad_idx)

    )

    return dataloader, dataset

# 模拟数据

texts = [

    "I love this movie",

    "This is a bad movie",

    "Great film",

    "Terrible acting",

    "I recommend this",

    "Not worth watching",

]

labels = [1, 0, 1, 0, 1, 0]

dataloader, dataset = create_dataloader(texts, labels, batch_size=2)

for batch in dataloader:

    print("Input shape:", batch['input'].shape)

    print("Labels:", batch['labels'])

    print("Lengths:", batch['lengths'])

    print("---")
```

## 4. 预训练词向量加载

使用预训练词向量可以提升模型效果。

### 4.1 GloVe 词向量

## 实例

```python
import torch

import numpy as np

def load_glove_vectors(filepath, word2idx, embedding_dim=300):

    """

    加载 GloVe 预训练词向量

    参数:

        filepath: GloVe 文件路径

        word2idx: 词表字典

        embedding_dim: 词向量维度

    """

    print("加载 GloVe 词向量...")

    # 初始化嵌入矩阵

    num_words = len(word2idx)

    embeddings = np.random.randn(num_words, embedding_dim).astype(np.float32)

    embeddings[word2idx['<PAD>']] = np.zeros(embedding_dim)  # PAD 向量置零

    words_loaded = 0

    with open(filepath, 'r', encoding='utf-8') as f:

        for line in f:

            values = line.strip().split()

            word = values[0]

            if word in word2idx:

                idx = word2idx[word]

                vector = np.asarray(values[1:], dtype=np.float32)

                if len(vector) == embedding_dim:

                    embeddings[idx] = vector

                    words_loaded += 1

    print(f"已加载 {words_loaded}/{num_words} 个词向量")

    return torch.from_numpy(embeddings)

# 模拟加载

def create_pretrained_embedding(word2idx, embedding_dim=300, pretrained_path=None):

    """

    创建预训练嵌入层

    """

    if pretrained_path and False:  # 设置为 True 并提供有效路径

        weights = load_glove_vectors(pretrained_path, word2idx, embedding_dim)

    else:

        # 使用随机初始化

        num_words = len(word2idx)

        weights = torch.randn(num_words, embedding_dim) * 0.1

    embedding = torch.nn.Embedding.from_pretrained(weights, padding_idx=0)

    return embedding

# 示例

word2idx = {'<PAD>': 0, '<UNK>': 1, 'hello': 2, 'world': 3, 'test': 4}

embedding = create_pretrained_embedding(word2idx, embedding_dim=100)

print(f"嵌入层形状: {embedding.weight.shape}")
```

### 4.2 使用 gensim 加载 Word2Vec

## 实例

```python
def load_word2vec(word2idx, model_path=None):

    """

    使用 gensim 加载 Word2Vec

    """

    try:

        from gensim.models import KeyedVectors

        # 加载模型

        # model = KeyedVectors.load_word2vec_format(model_path, binary=True)

        # 创建嵌入矩阵

        embedding_dim = 300

        num_words = len(word2idx)

        embeddings = np.random.randn(num_words, embedding_dim).astype(np.float32)

        # 填充词向量

        embeddings[word2idx['<PAD>']] = np.zeros(embedding_dim)

        # 加载词向量

        # for word, idx in word2idx.items():

        #     if word in model:

        #         embeddings[idx] = model[word]

        return torch.from_numpy(embeddings)

    except ImportError:

        print("gensim 未安装")

        return None
```

### 4.3 自定义预训练嵌入

## 实例

```python
import torch

import torch.nn as nn

class PretrainedEmbedding(nn.Module):

    """

    支持加载预训练词向量的嵌入层

    """

    def __init__(self, vocab_size, embed_dim, pretrained_weights=None,

                 padding_idx=0, freeze=False):

        super().__init__()

        self.embedding = nn.Embedding(

            vocab_size,

            embed_dim,

            padding_idx=padding_idx

        )

        # 加载预训练权重

        if pretrained_weights is not None:

            self.embedding.weight.data.copy_(pretrained_weights)

        # 是否冻结

        if freeze:

            self.embedding.weight.requires_grad = False

    def forward(self, x):

        return self.embedding(x)

# 使用示例

vocab_size = 10000

embed_dim = 300

pretrained = torch.randn(vocab_size, embed_dim) * 0.1

embedding_layer = PretrainedEmbedding(

    vocab_size,

    embed_dim,

    pretrained_weights=pretrained,

    padding_idx=0,

    freeze=False  # 设置为 True 冻结嵌入层

)

# 测试

x = torch.tensor([[1, 2, 3], [4, 5, 6]])

output = embedding_layer(x)

print(f"输入形状: {x.shape}")

print(f"输出形状: {output.shape}")
```

## 5. 文本数据增强

数据增强可以提升模型泛化能力。

### 5.1 回译增强

## 实例

```python
# 回译增强需要翻译 API，以下是概念示例

def back_translation_augment(text, translator):

    """

    回译增强：将文本翻译成另一种语言再翻译回来

    """

    # 翻译成目标语言

    translated = translator.translate(text, dest='fr')

    # 翻译回源语言

    back_translated = translator.translate(translated.text, dest='en')

    return back_translated.text

# 使用示例

# from googletrans import Translator

# translator = Translator()

# augmented_text = back_translation_augment("I love this movie", translator)
```

### 5.2 同义词替换

## 实例

```python
import random

def synonym_replacement(text, n=1, stop_words=None):

    """

    同义词替换

    """

    if stop_words is None:

        stop_words = {'a', 'an', 'the', 'is', 'are', 'was', 'were'}

    words = text.lower().split()

    replaceable = [i for i, w in enumerate(words) if w not in stop_words]

    if not replaceable:

        return text

    n = min(n, len(replaceable))

    replace_idx = random.sample(replaceable, n)

    # 简化的同义词映射（实际应使用 WordNet）

    synonym_map = {

        'good': ['great', 'excellent', 'nice'],

        'bad': ['poor', 'terrible', 'awful'],

        'movie': ['film', 'cinema'],

        'loved': ['adored', 'enjoyed'],

    }

    for idx in replace_idx:

        word = words[idx]

        if word in synonym_map:

            words[idx] = random.choice(synonym_map[word])

    return ' '.join(words)

# 使用示例

text = "I loved this good movie"

augmented = synonym_replacement(text, n=2)

print(f"原句: {text}")

print(f"增强: {augmented}")
```

### 5.3 随机插入与删除

## 实例

```python
import random

def random_insertion(text, n=1):

    """

    随机插入：在文本中随机插入词

    """

    words = text.lower().split()

    for _ in range(n):

        if len(words) > 1:

            idx = random.randint(0, len(words) - 1)

            # 简化的插入词

            insert_words = ['really', 'very', 'quite', 'actually']

            words.insert(idx, random.choice(insert_words))

    return ' '.join(words)

def random_deletion(text, p=0.1):

    """

    随机删除：以概率 p 删除词

    """

    words = text.lower().split()

    if len(words) == 1:

        return text

    remaining = [w for w in words if random.random() > p]

    if len(remaining) == 0:

        return random.choice(words)

    return ' '.join(remaining)

def random_swap(text, n=1):

    """

    随机交换：随机交换两个词的位置

    """

    words = text.lower().split()

    if len(words) < 2:

        return text

    for _ in range(n):

        idx1, idx2 = random.sample(range(len(words)), 2)

        words[idx1], words[idx2] = words[idx2], words[idx1]

    return ' '.join(words)

# 使用示例

text = "This is a great movie about love and happiness"

print("原始:", text)

print("插入:", random_insertion(text, n=2))

print("删除:", random_deletion(text, p=0.2))

print("交换:", random_swap(text, n=2))
```

## 6. 常见 NLP 任务示例

### 6.1 文本分类完整流程

## 实例

```python
import torch

import torch.nn as nn

from torch.utils.data import Dataset, DataLoader

# 1. 数据准备

texts = [

    "I love this product, it is amazing!",

    "Terrible quality, waste of money.",

    "Great value for the price.",

    "Not satisfied with the purchase.",

    "Best purchase I have ever made!",

    "Very disappointed with this item.",

]

labels = [1, 0, 1, 0, 1, 0]  # 1: 正面, 0: 负面

# 2. 数据集

class TextClassificationDataset(Dataset):

    def __init__(self, texts, labels, max_len=50):

        self.texts = texts

        self.labels = labels

        self.max_len = max_len

        self.vocab = self._build_vocab(texts)

    def _build_vocab(self, texts):

        vocab = {'<PAD>': 0, '<UNK>': 1}

        for text in texts:

            for word in text.lower().split():

                if word not in vocab:

                    vocab[word] = len(vocab)

        return vocab

    def __len__(self):

        return len(self.texts)

    def __getitem__(self, idx):

        text = self.texts[idx]

        label = self.labels[idx]

        # 简单编码

        tokens = text.lower().split()[:self.max_len]

        indices = [self.vocab.get(t, 1) for t in tokens]

        # 填充

        if len(indices) < self.max_len:

            indices += [0] * (self.max_len - len(indices))

        return torch.tensor(indices, dtype=torch.long), torch.tensor(label, dtype=torch.long)

# 3. 模型

class TextClassifier(nn.Module):

    def __init__(self, vocab_size, embed_dim=128, hidden_dim=64, num_classes=2):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)

        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):

        embedded = self.embedding(x)

        _, (hidden, _) = self.lstm(embedded)

        output = self.fc(hidden.squeeze(0))

        return output

# 4. 训练

dataset = TextClassificationDataset(texts, labels)

dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

model = TextClassifier(vocab_size=len(dataset.vocab))

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 训练几个 epoch

model.train()

for epoch in range(10):

    total_loss = 0

    for texts_batch, labels_batch in dataloader:

        optimizer.zero_grad()

        outputs = model(texts_batch)

        loss = criterion(outputs, labels_batch)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss/len(dataloader):.4f}")

print("训练完成！")
```

### 6.2 序列标注（NER）示例

## 实例

```python
import torch

import torch.nn as nn

from torch.utils.data import Dataset, DataLoader

# 序列标注数据集

class NERDataset(Dataset):

    """

    命名实体识别数据集

    格式: [(word, tag), ...]

    """

    def __init__(self, sentences_tags, word2idx, tag2idx, max_len=50):

        self.sentences_tags = sentences_tags

        self.word2idx = word2idx

        self.tag2idx = tag2idx

        self.max_len = max_len

    def __len__(self):

        return len(self.sentences_tags)

    def __getitem__(self, idx):

        sentence_tags = self.sentences_tags[idx]

        words = [wt[0] for wt in sentence_tags]

        tags = [wt[1] for wt in sentence_tags]

        # 编码

        word_ids = [self.word2idx.get(w.lower(), 1) for w in words[:self.max_len]]

        tag_ids = [self.tag2idx[t] for t in tags[:self.max_len]]

        # 填充

        if len(word_ids) < self.max_len:

            word_ids += [0] * (self.max_len - len(word_ids))

            tag_ids += [0] * (self.max_len - len(tag_ids))

        return {

            'words': torch.tensor(word_ids, dtype=torch.long),

            'tags': torch.tensor(tag_ids, dtype=torch.long)

        }

# NER 模型

class NERModel(nn.Module):

    def __init__(self, vocab_size, tag_size, embed_dim=128, hidden_dim=256):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)

        self.fc = nn.Linear(hidden_dim * 2, tag_size)

    def forward(self, x):

        embedded = self.embedding(x)

        lstm_out, _ = self.lstm(embedded)

        logits = self.fc(lstm_out)

        return logits

# 示例数据

data = [

    [("John", "B-PER"), ("lives", "O"), ("in", "O"), ("New", "B-LOC"), ("York", "I-LOC"), (".", "O")],

    [("Apple", "B-ORG"), ("is", "O"), ("a", "O"), ("company", "O"), (".", "O")],

]

# 构建词表和标签表

word2idx = {'<PAD>': 0, '<UNK>': 1}

tag2idx = {'O': 0, 'B-PER': 1, 'I-PER': 2, 'B-LOC': 3, 'I-LOC': 4, 'B-ORG': 5, 'I-ORG': 6}

for sent in data:

    for word, tag in sent:

        if word.lower() not in word2idx:

            word2idx[word.lower()] = len(word2idx)

print(f"词表大小: {len(word2idx)}")

print(f"标签数: {len(tag2idx)}")
```

## 7. 替代方案推荐

### 7.1 其他文本处理库

| 库名 | 特点 | 适用场景 |
| --- | --- | --- |
| HuggingFace Datasets | 数据加载和处理 | 通用 NLP 任务 |
| spacy | 高级 NLP 工具 | 分词、NER、依存分析 |
| NLTK | 经典 NLP 工具 | 教学、原型开发 |
| textblob | 简单易用 | 快速文本处理 |

### 7.2 HuggingFace Datasets 使用

## 实例

```python
# 使用 HuggingFace Datasets 库

# pip install datasets

from datasets import load_dataset

# 加载数据集

# dataset = load_dataset("imdb")

# dataset = load_dataset("squad")

# 数据预处理

# def preprocess_function(examples):

#     return tokenizer(examples['text'], truncation=True, padding='max_length')

# tokenized_dataset = dataset.map(preprocess_function, batched=True)

print("HuggingFace Datasets 使用示例:")

print("from datasets import load_dataset")

print("dataset = load_dataset('imdb')")
```

## 8. API 快速参考

### 8.1 文本处理常用操作

| 操作 | 方法 |
| --- | --- |
| 分词 | text.split(), spacy, nltk, jieba |
| 词表构建 | Counter, vocab.build_vocab() |
| 编码 | vocab.encode(), tokenizer.encode() |
| 解码 | vocab.decode(), tokenizer.decode() |
| 填充 | pad_sequence, collate_fn |
| 加载词向量 | Gensim, GloVe 直接加载 |

### 8.2 数据增强方法

| 方法 | 描述 |
| --- | --- |
| 同义词替换 | 随机替换词为同义词 |
| 随机插入 | 随机插入词 |
| 随机删除 | 随机删除词 |
| 随机交换 | 随机交换词位置 |
| 回译 | 翻译后再翻译回来 |

### 8.3 推荐的数据处理流程

```python
1. 数据清洗

- 去除 HTML 标签、特殊字符

- 统一编码、大小写

2. 分词

- 英文: spaCy / NLTK

- 中文: jieba / pkuseg

3. 词表构建

- 过滤低频词

- 设定最大词表大小

4. 序列化

- 编码为索引

- 统一长度（填充/截断）

5. 数据增强（可选）

- 同义词替换、回译

6. 批量加载

- DataLoader + 自定义 collate_fn
```

---

# PyTorch 混合精度训练 (AMP)

混合精度训练是深度学习中最重要的性能优化技术之一。它通过同时使用 FP32（单精度）和 FP16（半精度）浮点数进行计算，可以在几乎不损失模型精度的前提下，显著提升训练速度并减少显存占用。本节详细介绍 PyTorch 中的自动混合精度（Automatic Mixed Precision，AMP）技术。

**适用版本：**本文代码基于 PyTorch 1.6+ 的 `torch.cuda.amp` API 编写。PyTorch 2.4+ 推荐使用 `torch.amp.autocast` 和 `torch.amp.GradScaler`，用法基本一致，文中会标注差异。

## 1. 混合精度训练基础

### 1.1 为什么需要混合精度

深度学习模型训练过程中涉及大量的矩阵运算。传统的 FP32（32位浮点）计算精度高，但占用显存大、计算速度慢。FP16（16位浮点）计算速度快、显存占用少，但数值表示范围较小，容易出现梯度下溢（underflow）问题。

混合精度训练的核心理念是：对精度要求高的操作使用 FP32，对精度要求不高的操作使用 FP16。这样既能享受 FP16 的速度优势，又能避免精度问题。

下图展示了三种浮点格式的位布局差异——**指数位**决定数值范围，**尾数位**决定精度：

  浮点数格式位布局对比

    符号位

    指数位

    尾数位

    FP32
    32 bits

    S
    1

    Exponent
    8 bits

    Mantissa
    23 bits

    范围: ±3.4×10³⁸
    精度: ~7 位有效数字

    FP16
    16 bits

    S

    Exp
    5 bits

    Mantissa
    10 bits

    范围: ±65504
    精度: ~3.3 位有效数字

    ⚠ 指数位少，易溢出

    BF16
    16 bits

    S

    Exponent
    8 bits（同 FP32）

    Mantissa
    7 bits

    范围: ±3.4×10³⁸
    精度: ~2.4 位有效数字

    ✓ 范围与 FP32 相同

    BF16 保留了 FP32 的指数位 → 数值范围相同 → 训练更稳定，通常无需 GradScaler

### 1.2 混合精度的优势

| 指标 | 提升效果 | 说明 |
| --- | --- | --- |
| 训练速度 | 提升 2-3 倍 | 依赖 GPU Tensor Core 支持 |
| 显存占用 | 减少约 50% | 激活值和中间结果以 FP16 存储 |
| 内存带宽 | 减少约 50% | 更小的数据体积意味着更少的传输量 |
| 通信开销 | 减少约 50% | 分布式训练中梯度传输量减半 |

### 1.3 Tensor Core 加速原理

NVIDIA 的 Tensor Core 是一种专门用于矩阵运算的硬件单元。它可以在一个时钟周期内完成 4×4 矩阵乘加运算（D = A × B + C），这就是 FP16 训练加速的主要来源。相比普通 CUDA 核心需要多次指令才能完成同样的运算，Tensor Core 将其压缩为单条指令。

支持 Tensor Core 的 GPU 包括：

- **Volta 架构**（V100）— 首代 Tensor Core，仅支持 FP16

- **Turing 架构**（RTX 20 系）— 支持 FP16 / INT8 / INT4

- **Ampere 架构**（RTX 30 系、A100）— 新增 BF16 / TF32 支持

- **Ada Lovelace 架构**（RTX 40 系）— 新增 FP8 支持

- **Hopper 架构**（H100）— 新增 FP8 Transformer Engine

消费级 RTX GPU 同样支持 Tensor Core，如 RTX 3060 及以上型号均可享受 AMP 加速。

## 2. PyTorch AMP 基础用法

### 2.1 autocast 与 GradScaler

PyTorch 的 AMP API 主要包含两个核心组件：

- `autocast`：上下文管理器，自动将区域内的运算切换为 FP16（对精度敏感的操作会自动回退到 FP32）

- `GradScaler`：动态调整梯度缩放系数，放大 FP16 梯度以防止下溢（仅 FP16 需要，BF16 通常不需要）

下图展示了 AMP 训练一个完整 step 的数据流：

  AMP 单步训练流程

    输入数据
    FP32

-

    autocast
    前向传播
    自动选择 FP16/FP32

-

    计算 Loss
    FP32

-

    GradScaler
    缩放 + 反向传播
    loss × scale_factor

-

    Unscale 梯度
    + 梯度裁剪
    grad / scale_factor

-

    优化器更新
    FP32 权重

-

    更新
    Scaler
    调整 scale

    autocast 控制 — 自动选择精度

    GradScaler 控制 — 防止梯度下溢

    FP32 权重更新 — 保持精度

      关键：权重始终以 FP32 存储和更新，仅在计算时临时转换为 FP16

### 2.2 基础使用示例

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.cuda.amp import autocast, GradScaler

# PyTorch 2.4+ 推荐写法：

# from torch.amp import autocast, GradScaler

# 检查 CUDA 是否可用

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"使用设备: {device}")

if torch.cuda.is_available():

    print(f"GPU: {torch.cuda.get_device_name(0)}")

    print(f"支持 BF16: {torch.cuda.is_bf16_supported()}")

# ── 模型定义 ──────────────────────────────────────

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(128, 256),

            nn.ReLU(),

            nn.Linear(256, 256),

            nn.ReLU(),

            nn.Linear(256, 10)

        )

    def forward(self, x):

        return self.net(x)

model = SimpleModel().to(device)

# 损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ── 混合精度训练关键组件 ──────────────────────────

# GradScaler：缩放损失以避免 FP16 梯度下溢

scaler = GradScaler()

# 训练循环

def train_epoch_amp(model, loader, criterion, optimizer, scaler, device):

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        # ── 核心：使用 autocast 上下文管理器 ──────

        # autocast 区域内的运算自动使用 FP16

        # 对精度敏感的操作（如 softmax、loss）会自动回退 FP32

        with autocast(device_type='cuda'):

            outputs = model(inputs)

            loss = criterion(outputs, labels)

        # ── 使用 scaler 进行反向传播 ─────────────

        # 1. 缩放 loss（乘以 scale_factor）

        # 2. 反向传播（在放大的梯度上计算）

        # 3. scaler.step 内部自动反缩放梯度并检查 Inf/NaN

        scaler.scale(loss).backward()

        # 更新参数

        scaler.step(optimizer)

        # 更新 scaler 的缩放因子

        scaler.update()

        # 统计

        total_loss += loss.item() * inputs.size(0)

        _, predicted = outputs.max(1)

        correct += predicted.eq(labels).sum().item()

        total += labels.size(0)

    return total_loss / total, correct / total

# 模拟数据

train_loader = [

    (torch.randn(32, 128), torch.randint(0, 10, (32,))) for _ in range(10)

]

# 开始训练

for epoch in range(3):

    loss, acc = train_epoch_amp(

        model, train_loader, criterion, optimizer, scaler, device

    )

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, Acc={acc:.4f}")

print("混合精度训练完成！")
```

**API 迁移提示：**PyTorch 2.4 将 `torch.cuda.amp.autocast` 标记为 deprecated，推荐使用 `torch.amp.autocast('cuda')`。两者用法完全一致，仅导入路径不同。

### 2.3 BF16 与 FP16 的选择

现代 GPU 支持两种半精度格式，它们的核心区别在于指数位和尾数位的分配策略不同：

| 格式 | 指数位 | 尾数位 | 数值范围 | 精度 | 适用场景 |
| --- | --- | --- | --- | --- | --- |
| FP16 | 5 bits | 10 bits | ±65504 | 较高（~3.3位） | 需要兼容旧 GPU（V100/RTX 20系） |
| BF16 | 8 bits | 7 bits | ±3.4×10³⁸ | 较低（~2.4位） | 追求稳定性（A100/RTX 30系+） |

选择建议：如果硬件支持 BF16，优先使用 BF16。它的数值范围与 FP32 完全相同，训练过程中几乎不会出现溢出问题，且不需要 GradScaler。

## 实例

```python
# ── BF16 写法（PyTorch 1.10+）────────────────────

# BF16 不需要 GradScaler，因为数值范围与 FP32 相同

from torch.cuda.amp import autocast

# 方式一：在 autocast 中指定 dtype

with autocast(device_type='cuda', dtype=torch.bfloat16):

    outputs = model(inputs)

    loss = criterion(outputs, labels)

# 方式二：全局默认启用 BF16（如果硬件支持）

# torch.backends.cuda.matmul.allow_bf16_reduced_precision = True

# torch.backends.cudnn.allow_bf16_reduced_precision = True

# ── 检查硬件支持 ─────────────────────────────────

print(f"硬件支持 BF16: {torch.cuda.is_bf16_supported()}")

print(f"当前 matmul 允许 BF16: {torch.backends.cuda.matmul.allow_bf16}")

print(f"当前 cuDNN 允许 BF16: {torch.backends.cudnn.allow_bf16}")

# ── BF16 完整训练示例（无需 GradScaler）──────────

scaler_bf16 = None  # BF16 不需要 scaler

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda', dtype=torch.bfloat16):

        outputs = model(inputs)

        loss = criterion(outputs, labels)

    # 直接反向传播，无需 scaler

    loss.backward()

    optimizer.step()
```

## 3. 进阶技巧与优化

### 3.1 动态损失缩放

GradScaler 的核心机制是**动态损失缩放**——它会根据训练状态自动调整缩放因子，既能防止梯度下溢，又能在训练稳定时逐步降低缩放以减少精度损失：

  动态损失缩放（Dynamic Loss Scaling）

  Scale × Loss

-

  反向传播

-

  梯度中存在
  Inf / NaN？

-
  是

  缩小 scale
  × backoff
  （默认 0.5）

  跳过本次更新

-
  否

  Unscale + 更新参数
  连续成功 +1

-

  连续成功 ≥ growth_interval？
  （默认 2000 步）

-

  增大 scale × growth

    growth_factor 默认 2.0 · backoff_factor 默认 0.5 · 动态平衡精度与稳定

GradScaler 自动管理上述反馈循环，你只需通过参数微调其行为：

## 实例

```python
from torch.cuda.amp import GradScaler

# 自定义 GradScaler 参数

scaler = GradScaler(

    init_scale=2**16,        # 初始缩放因子，默认 65536

    growth_factor=2.0,       # 缩放因子增长倍数，默认 2.0

    backoff_factor=0.5,      # 缩放因子回退倍数，默认 0.5

    growth_interval=2000,    # 连续多少个 step 成功后才增长

    enabled=True             # 是否启用（可动态开关）

)

# 工作流程：

# 1. 初始 scale = 65536

# 2. 若某 step 出现 Inf/NaN → scale × 0.5（缩小），跳过该 step

# 3. 若连续 2000 个 step 无 Inf/NaN → scale × 2.0（增大）

# 4. 始终在安全范围内寻找最大可用 scale

# 查看当前缩放因子

print(f"当前缩放因子: {scaler.get_scale()}")

# 判断 scaler 是否认为上一步成功

print(f"最近是否成功: {scaler._found_inf.item() == 0}")
```

### 3.2 梯度累积中的 AMP

梯度累积用于在有限显存下模拟更大的 batch size。使用 AMP 时，需要注意每个子 batch 的 loss 必须除以累积步数，否则最终梯度会被放大：

## 实例

```python
# ── 梯度累积 + 混合精度 ──────────────────────────

accumulation_steps = 8

scaler = GradScaler()

model.train()

for batch_idx, (inputs, labels) in enumerate(train_loader):

    inputs, labels = inputs.to(device), labels.to(device)

    with autocast(device_type='cuda'):

        outputs = model(inputs)

        # 关键：每个子 batch 的 loss 除以累积步数

        # 这样累积后的梯度等价于大 batch 的平均梯度

        loss = criterion(outputs, labels) / accumulation_steps

    # 累积缩放后的梯度（注意：此处不清零）

    scaler.scale(loss).backward()

    # 每 accumulation_steps 个 batch 更新一次参数

    if (batch_idx + 1) % accumulation_steps == 0:

        scaler.step(optimizer)

        scaler.update()

        optimizer.zero_grad()

# ── 处理末尾不足一个完整累积周期的梯度 ──────────

remainder = len(train_loader) % accumulation_steps

if remainder != 0:

    # 需要将累积的梯度按实际步数重新缩放

    # 简单做法：仍然执行 step，梯度会偏大但影响通常很小

    scaler.step(optimizer)

    scaler.update()

    optimizer.zero_grad()
```

### 3.3 验证与推理中的 AMP

验证和推理阶段同样推荐使用 AMP。由于不需要反向传播和梯度缩放，代码更加简洁：

## 实例

```python
# ── 推理时使用 autocast ──────────────────────────

@torch.no_grad()

def inference_amp(model, inputs, device):

    model.eval()

    # 推理使用 FP16，无需 GradScaler

    with autocast(device_type='cuda'):

        outputs = model(inputs.to(device))

    return outputs

# ── inference_mode 比 no_grad 更快 ──────────────

# inference_mode 会禁用更多追踪开销，适合纯推理

@torch.inference_mode()

def inference_fast(model, inputs, device):

    model.eval()

    with autocast(device_type='cuda'):

        outputs = model(inputs.to(device))

    return outputs

# ── 批量推理示例 ─────────────────────────────────

def batch_inference(model, dataloader, device):

    model.eval()

    all_outputs = []

    with torch.inference_mode():

        for inputs in dataloader:

            with autocast(device_type='cuda'):

                outputs = model(inputs.to(device))

            all_outputs.append(outputs.cpu())

    return torch.cat(all_outputs, dim=0)
```

## 4. 常见问题与解决方案

### 4.1 训练不稳定

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| Loss 变为 NaN / Inf | 梯度溢出（scale 过大或学习率过高） | 降低 init_scale，添加梯度裁剪，降低学习率 |
| Loss 不下降 / 震荡 | 梯度下溢（scale 过小，梯度被截断为 0） | 提高 init_scale，检查梯度统计，尝试 BF16 |
| 精度下降明显 | 某些层（如 LayerNorm、Softmax）对 FP16 敏感 | 手动将这些层保持 FP32（见 4.2） |
| 训练后期不稳定 | 模型参数值域变化导致 scale 不匹配 | 适当增大 growth_interval，使 scale 调整更保守 |

### 4.2 手动控制精度

某些操作在 FP16 下精度损失较大，需要手动指定使用 FP32。PyTorch 的 autocast 已经内置了对这些操作的保护，但自定义操作可能需要手动处理：

## 实例

```python
# ── 方法一：包裹一个强制 FP32 的损失函数 ────────

class FP32Loss(nn.Module):

    """强制在 FP32 下计算的损失函数包装器"""

    def __init__(self, base_criterion):

        super().__init__()

        self.base_criterion = base_criterion

    def forward(self, input, target):

        # 显式转换为 FP32，脱离 autocast 的影响

        return self.base_criterion(input.float(), target.float())

# ── 方法二：在 autocast 中局部禁用 ──────────────

with autocast(device_type='cuda'):

    outputs = model(inputs)

    # 对精度敏感的操作，临时禁用 autocast

    with autocast(enabled=False):

        loss = criterion(outputs.float(), labels)

# ── 方法三：模型中特定层保持 FP32 ──────────────

class CustomModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.BatchNorm2d(64),  # BN 对精度敏感

            nn.ReLU(),

            nn.Conv2d(64, 128, 3, padding=1),

            nn.BatchNorm2d(128),

            nn.ReLU(),

        )

        self.classifier = nn.Linear(128, 10)

    def forward(self, x):

        x = self.features[0](x)           # Conv: FP16（由 autocast 控制）

        x = self.features[1](x.float())   # BN: 强制 FP32

        x = self.features[2](x)           # ReLU: FP16

        x = self.features[3](x)

        x = self.features[4](x.float())   # BN: 强制 FP32

        x = self.features[5](x)

        x = x.mean(dim=[2, 3])            # Global Average Pooling

        x = self.classifier(x)

        return x
```

**提示：**PyTorch 的 autocast 会自动将以下操作保持在 FP32：softmax、log_softmax、cross_entropy、layer_norm、batch_norm 等。通常只有自定义算子才需要手动处理。

### 4.3 梯度裁剪与 AMP

梯度裁剪必须在 `scaler.step()` 之前、且在 `scaler.unscale_()` 之后执行。这是因为裁剪需要作用在**真实梯度值**上，而非缩放后的梯度：

## 实例

```python
# ── 正确的梯度裁剪顺序 ──────────────────────────

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda'):

        outputs = model(inputs)

        loss = criterion(outputs, labels)

    # Step 1: 缩放 loss 并反向传播

    scaler.scale(loss).backward()

    # Step 2: 反缩放梯度（将梯度从 scale 还原到真实值）

    #         必须在裁剪和 step 之前调用

    scaler.unscale_(optimizer)

    # Step 3: 对真实梯度进行裁剪

    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    # Step 4: 更新参数（内部会检查梯度是否含 Inf/NaN）

    scaler.step(optimizer)

    # Step 5: 更新缩放因子

    scaler.update()

# ── 常见错误：忘记 unscale_ 就裁剪 ──────────────

# 错误！裁剪的是被放大的梯度，阈值会被 scale 干扰

# scaler.scale(loss).backward()

# torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # ← 错误

# scaler.step(optimizer)
```

## 5. 性能对比与最佳实践

### 5.1 性能基准测试

## 实例

```python
import time

def benchmark_training(model, train_loader, device, use_amp=True,

                       dtype=torch.float16, num_iterations=100):

    """对比 FP32 与 AMP 的训练速度"""

    model = model.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    scaler = GradScaler(enabled=use_amp and dtype == torch.float16)

    # ── 预热（前 10 步不计时）────────────────────

    for i, (inputs, labels) in enumerate(train_loader):

        if i >= 10:

            break

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        if use_amp:

            with autocast(device_type='cuda', dtype=dtype):

                outputs = model(inputs)

                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()

            scaler.step(optimizer)

            scaler.update()

        else:

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

    # ── 正式测试 ─────────────────────────────────

    torch.cuda.synchronize()

    start = time.time()

    for i, (inputs, labels) in enumerate(train_loader):

        if i >= num_iterations:

            break

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        if use_amp:

            with autocast(device_type='cuda', dtype=dtype):

                outputs = model(inputs)

                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()

            scaler.step(optimizer)

            scaler.update()

        else:

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

    torch.cuda.synchronize()

    elapsed = time.time() - start

    return elapsed / num_iterations

# ── 运行对比 ─────────────────────────────────────

model = SimpleModel()

fp32_time = benchmark_training(model, train_loader, device, use_amp=False)

fp16_time = benchmark_training(model, train_loader, device, use_amp=True, dtype=torch.float16)

print(f"FP32 平均耗时: {fp32_time*1000:.2f} ms/batch")

print(f"FP16 平均耗时: {fp16_time*1000:.2f} ms/batch")

print(f"加速比: {fp32_time / fp16_time:.2f}x")

# 如果支持 BF16，也测试一下

if torch.cuda.is_bf16_supported():

    bf16_time = benchmark_training(

        model, train_loader, device, use_amp=True, dtype=torch.bfloat16

    )

    print(f"BF16 平均耗时: {bf16_time*1000:.2f} ms/batch")

    print(f"BF16 加速比: {fp32_time / bf16_time:.2f}x")
```

### 5.2 显存对比

## 实例

```python
def compare_memory(model_class, train_loader, device):

    """对比 FP32 与 AMP 的显存占用"""

    def reset():

        torch.cuda.empty_cache()

        torch.cuda.reset_peak_memory_stats()

    # ── FP32 显存测试 ────────────────────────────

    reset()

    model_fp32 = model_class().to(device)

    optimizer_fp32 = optim.Adam(model_fp32.parameters())

    for inputs, labels in list(train_loader)[:5]:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_fp32.zero_grad()

        outputs = model_fp32(inputs)

        loss = nn.CrossEntropyLoss()(outputs, labels)

        loss.backward()

        optimizer_fp32.step()

    fp32_peak = torch.cuda.max_memory_allocated() / 1024**2

    # ── AMP 显存测试 ─────────────────────────────

    reset()

    model_amp = model_class().to(device)

    optimizer_amp = optim.Adam(model_amp.parameters())

    scaler = GradScaler()

    for inputs, labels in list(train_loader)[:5]:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_amp.zero_grad()

        with autocast(device_type='cuda'):

            outputs = model_amp(inputs)

            loss = nn.CrossEntropyLoss()(outputs, labels)

        scaler.scale(loss).backward()

        scaler.step(optimizer_amp)

        scaler.update()

    amp_peak = torch.cuda.max_memory_allocated() / 1024**2

    print(f"FP32 峰值显存: {fp32_peak:.1f} MB")

    print(f"AMP  峰值显存: {amp_peak:.1f} MB")

    print(f"显存节省: {(fp32_peak - amp_peak) / fp32_peak * 100:.1f}%")

compare_memory(SimpleModel, train_loader, device)
```

### 5.3 最佳实践总结

| 场景 | 推荐配置 | 原因 |
| --- | --- | --- |
| A100 / H100 / RTX 40 系 | BF16，不需要 GradScaler | 数值范围与 FP32 相同，最稳定 |
| V100 / RTX 20 系 | FP16 + GradScaler | 硬件不支持 BF16，需要 scaler 防溢出 |
| RTX 30 系 | BF16 优先，FP16 备选 | Ampere 架构支持 BF16 |
| 大模型训练（显存紧张） | AMP + 梯度累积 + 梯度检查点 | 三者叠加可最大化显存利用率 |
| 推理部署 | autocast + inference_mode | 无需 scaler，推理最快 |

PyTorch 2.0+ 已将 AMP 集成到 `torch.compile` 中，可以自动应用混合精度优化。使用 `torch.compile(model)` 时，编译器会自动判断哪些操作适合 FP16。

## 6. 与其他优化技术的结合

### 6.1 AMP + torch.compile

## 实例

```python
# ── PyTorch 2.0+ 结合使用 ───────────────────────

model = model.to(device)

# 方式一：先 compile，再用 AMP 训练

# torch.compile 会自动融合算子、优化内存访问

model_compiled = torch.compile(model, mode="reduce-overhead")

scaler = GradScaler()

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda'):

        outputs = model_compiled(inputs)

        loss = criterion(outputs, labels)

    scaler.scale(loss).backward()

    scaler.step(optimizer)

    scaler.update()

# 方式二：启用 TF32（Ampere+ 架构的额外加速）

# TF32 使用 19 位精度，速度接近 FP16，精度接近 FP32

torch.backends.cuda.matmul.allow_tf32 = True

torch.backends.cudnn.allow_tf32 = True

torch.backends.cudnn.benchmark = True  # 固定输入尺寸时加速卷积
```

### 6.2 AMP + 分布式训练

## 实例

```python
# ── 分布式训练 + 混合精度 ────────────────────────

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):

    dist.init_process_group("nccl", rank=rank, world_size=world_size)

    torch.cuda.set_device(rank)

def train_ddp_amp(rank, world_size):

    setup(rank, world_size)

    device = torch.device(f"cuda:{rank}")

    model = SimpleModel().to(device)

    model = DDP(model, device_ids=[rank])

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    scaler = GradScaler()

    for inputs, labels in train_loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        with autocast(device_type='cuda'):

            outputs = model(inputs)

            loss = criterion(outputs, labels)

        # DDP 会在 backward 中自动同步梯度

        scaler.scale(loss).backward()

        # 梯度裁剪（需先 unscale）

        scaler.unscale_(optimizer)

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        scaler.step(optimizer)

        scaler.update()

    dist.destroy_process_group()
```

## 总结

混合精度训练是当前深度学习训练的**标准实践**。

核心要点：

- **选择精度格式**：硬件支持 BF16 时优先使用，否则使用 FP16 + GradScaler

- **理解 autocast**：它自动管理精度切换，大多数情况下无需手动干预

- **理解 GradScaler**：仅 FP16 需要，通过动态缩放防止梯度下溢

- **注意裁剪顺序**：unscale → clip → step → update，顺序不可颠倒

- **善用组合优化**：AMP 可与 torch.compile、梯度累积、分布式训练无缝结合

---

# PyTorch TorchScript / ONNX 导出

模型训练完成后，需要将模型部署到生产环境。PyTorch 提供了多种模型导出方式，其中 TorchScript 和 ONNX 是最常用的两种格式。

本节详细介绍这两种导出方式的原理、使用方法和最佳实践。

模型导出是将 PyTorch 模型转换为可以在不同平台、不同框架上运行的格式的过程。这对于模型部署、移动端推理、跨框架迁移等场景至关重要。

## 1. TorchScript 基础

### 1.1 什么是 TorchScript

TorchScript 是 PyTorch 的序列化格式，它可以将 Python 代码转换为可以独立运行的 C++ 虚拟机代码。TorchScript 程序可以在没有 Python 解释器的环境中运行。

TorchScript 的主要特点：

- 将动态图转换为静态图

- 支持 Python 子集的语法

- 可以在 C++ 环境中运行

- 保留模型的结构和参数

### 1.2 两种转换方式

TorchScript 提供两种将模型转换为 TorchScript 的方式：

- TorchScript 追踪（Tracing）：通过执行模型记录操作，生成静态计算图

- TorchScript 脚本（Scripting）：直接分析 Python 代码，编译为 TorchScript

## 2. TorchScript 追踪 (Tracing)

### 2.1 基本追踪方法

## 实例

```python
import torch

import torch.nn as nn

# ── 定义模型 ──────────────────────────────────────

class SimpleNet(nn.Module):

    def __init__(self):

        super().__init__()

        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)

        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        self.pool = nn.MaxPool2d(2)

        self.fc = nn.Linear(128 * 8 * 8, 10)

    def forward(self, x):

        x = self.pool(torch.relu(self.conv1(x)))

        x = self.pool(torch.relu(self.conv2(x)))

        x = x.view(x.size(0), -1)

        x = self.fc(x)

        return x

# 创建模型实例

model = SimpleNet()

model.eval()

# 示例输入

example_input = torch.randn(1, 3, 64, 64)

# ── 方式一：torch.jit.trace 追踪 ───────────────────

# 通过运行模型并记录操作来创建 TorchScript

traced_model = torch.jit.trace(model, example_input)

print("追踪后的模型:")

print(traced_model)

# 保存模型

traced_model.save("simple_net_traced.pt")

# 加载模型

loaded_model = torch.jit.load("simple_net_traced.pt")

# 使用加载的模型进行推理

output = loaded_model(example_input)

print(f"输出形状: {output.shape}")
```

### 2.2 追踪的限制

追踪方法有一些限制：

- 只记录实际执行的操作

- 控制流（如 if、for）会被固定

- 动态大小的输入可能有问题

## 实例

```python
# 追踪的限制示例

class DynamicModel(nn.Module):

    def __init__(self):

        super().__init__()

    def forward(self, x):

        # 控制流在追踪时被固定

        if x.sum() > 0:

            return x * 2

        else:

            return x / 2

model = DynamicModel()

model.eval()

# 追踪时，if 分支会被固定为追踪时的路径

example_input = torch.tensor([1.0])

traced = torch.jit.trace(model, example_input)

# 即使输入不同，也会执行相同的分支

print(traced(torch.tensor([1.0])))  # 2

print(traced(torch.tensor([-1.0]))) # 仍然是 2，不是 -0.5
```

对于包含控制流的模型，应该使用 TorchScript 脚本（Scripting）而不是追踪。

## 3. TorchScript 脚本 (Scripting)

### 3.1 基本使用方法

## 实例

```python
import torch

# ── 使用 @torch.jit.script 装饰器 ───────────────

@torch.jit.script

def scripted_function(x: torch.Tensor) -> torch.Tensor:

    """使用脚本方式转换函数"""

    if x.sum() > 0:

        return x * 2

    else:

        return x / 2

# 测试脚本化的函数

input1 = torch.tensor([1.0, 2.0])

input2 = torch.tensor([-1.0, -2.0])

print(scripted_function(input1))  # [2., 4.]

print(scripted_function(input2))    # [-0.5, -1.]

# ── 脚本化模型 ───────────────────────────────────

class ScriptableModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc = nn.Linear(10, 10)

    @torch.jit.export

    def forward(self, x: torch.Tensor) -> torch.Tensor:

        return torch.relu(self.fc(x))

    @torch.jit.export

    def predict(self, x: torch.Tensor) -> torch.Tensor:

        """额外的导出方法"""

        out = self.forward(x)

        return torch.argmax(out, dim=1)

model = ScriptableModel()

# 脚本化模型

scripted_model = torch.jit.script(model)

print(scripted_model)

# 保存

scripted_model.save("scripted_model.pt")
```

### 3.2 复杂模型的脚本化

## 实例

```python
# 更复杂的脚本化示例：带条件的模型

class ConditionModel(nn.Module):

    def __init__(self, num_classes: int):

        super().__init__()

        self.num_classes = num_classes

        self.features = nn.Sequential(

            nn.Conv2d(3, 32, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten()

        )

        self.classifier = nn.Linear(64, num_classes)

    def forward(self, x: torch.Tensor, use_softmax: bool = False) -> torch.Tensor:

        """

        支持动态条件的模型

        """

        features = self.features(x)

        logits = self.classifier(features)

        if use_softmax:

            return torch.softmax(logits, dim=1)

        else:

            return logits

    def get_prediction(self, x: torch.Tensor) -> torch.Tensor:

        """辅助方法"""

        logits = self.forward(x, use_softmax=False)

        return torch.argmax(logits, dim=1)

# 脚本化

model = ConditionModel(num_classes=10)

scripted_model = torch.jit.script(model, example_inputs=(torch.randn(1, 3, 32, 32),))

# 测试

test_input = torch.randn(2, 3, 32, 32)

output1 = scripted_model(test_input, use_softmax=False)

output2 = scripted_model(test_input, use_softmax=True)

print(f"Logits 输出形状: {output1.shape}")

print(f"Softmax 输出形状: {output2.shape}")
```

## 4. ONNX 导出

### 4.1 ONNX 基础

ONNX（Open Neural Network eXchange） 是一个开放的神经网络交换格式，支持在不同的深度学习框架之间转换模型。

ONNX 的优势：

- 跨框架：PyTorch、TensorFlow、Caffe2 等都支持

- 跨平台：支持 CPU、GPU、移动端等多种平台

- 硬件优化：可利用 ONNX Runtime 进行高效推理

- 工具丰富：有大量的优化工具和部署方案

### 4.2 基本 ONNX 导出

## 实例

```python
import torch

import torch.nn as nn

import torchvision

# ── 定义模型 ──────────────────────────────────────

class ImageClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 32, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten()

        )

        self.classifier = nn.Linear(64, 10)

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x

model = ImageClassifier()

model.eval()

# 示例输入

example_input = torch.randn(1, 3, 32, 32)

# ── 导出为 ONNX ──────────────────────────────────

output_path = "image_classifier.onnx"

torch.onnx.export(

    model,

    example_input,

    output_path,

    export_params=True,        # 导出模型参数

    opset_version=14,          # ONNX 版本

    do_constant_folding=True, # 常量折叠优化

    input_names=['input'],     # 输入张量名称

    output_names=['output'],   # 输出张量名称

    dynamic_axes={

        'input': {0: 'batch_size'},    # 动态批次维度

        'output': {0: 'batch_size'}

    }

)

print(f"模型已导出到: {output_path}")

# 验证导出的模型

import onnx

onnx_model = onnx.load(output_path)

onnx.checker.check_model(onnx_model)

print("ONNX 模型验证通过！")
```

### 4.3 导出复杂模型

## 实例

```python
# 导出完整的 ResNet 模型

import torchvision.models as models

# 加载预训练模型

model = models.resnet18(pretrained=True)

model.eval()

# 示例输入（ResNet 标准的 224x224）

example_input = torch.randn(1, 3, 224, 224)

# 导出

torch.onnx.export(

    model,

    example_input,

    "resnet18.onnx",

    export_params=True,

    opset_version=14,

    input_names=['input'],

    output_names=['output'],

    dynamic_axes={

        'input': {0: 'batch_size', 2: 'height', 3: 'width'},

        'output': {0: 'batch_size'}

    }

)

print("ResNet18 已导出")

# 导出时处理特殊的层

# 对于需要特殊处理的层，使用 workaround

class ModelWithSpecialOps(nn.Module):

    def __init__(self):

        super().__init__()

        self.conv = nn.Conv2d(3, 64, 3, padding=1)

    def forward(self, x):

        # 使用 F.interpolate 而不是 nn.functional 的别名

        x = self.conv(x)

        x = torch.nn.functional.interpolate(x, scale_factor=2, mode='bilinear', align_corners=False)

        return x

model = ModelWithSpecialOps()

model.eval()

torch.onnx.export(

    model,

    torch.randn(1, 3, 32, 32),

    "special_ops.onnx",

    input_names=['input'],

    output_names=['output'],

    opset_version=14

)
```

## 5. 导出的验证与优化

### 5.1 验证导出模型

## 实例

```python
import numpy as np

import onnx

import onnxruntime as ort

def verify_onnx_model(onnx_path, pytorch_model, test_input):

    """

    验证 ONNX 模型与 PyTorch 模型的输出一致性

    """

    # 1. 检查 ONNX 模型

    onnx_model = onnx.load(onnx_path)

    onnx.checker.check_model(onnx_model)

    print("✓ ONNX 模型结构验证通过")

    # 2. PyTorch 推理

    pytorch_model.eval()

    with torch.no_grad():

        pytorch_output = pytorch_model(test_input)

    # 3. ONNX Runtime 推理

    ort_session = ort.InferenceSession(onnx_path)

    ort_output = ort_session.run(None, {'input': test_input.numpy()})[0]

    # 4. 对比输出

    diff = np.abs(pytorch_output.numpy() - ort_output).max()

    print(f"✓ 最大输出差异: {diff:.6f}")

    if diff < 1e-5:

        print("✓ 输出验证通过")

        return True

    else:

        print("&#x26a0; 输出差异较大")

        return False

# 使用示例

model = ImageClassifier()

model.eval()

# 先导出

torch.onnx.export(

    model,

    torch.randn(1, 3, 32, 32),

    "test_model.onnx",

    input_names=['input'],

    output_names=['output']

)

# 验证

test_input = torch.randn(2, 3, 32, 32)

verify_onnx_model("test_model.onnx", model, test_input)
```

### 5.2 ONNX Runtime 优化

## 实例

```python
import onnxruntime as ort

from onnxruntime import GraphOptimizationLevel

# 创建推理会话并配置优化

def create_optimized_session(onnx_path, providers=None):

    if providers is None:

        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']

    # 配置会话选项

    sess_options = ort.SessionOptions()

    # 开启图优化

    sess_options.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL

    # 启用其他优化

    sess_options.intra_op_num_threads = 4

    sess_options.inter_op_num_threads = 4

    # 创建会话

    session = ort.InferenceSession(onnx_path, sess_options, providers=providers)

    return session

# 使用优化的会话进行推理

session = create_optimized_session("resnet18.onnx")

# 获取输入输出名称

input_name = session.get_inputs()[0].name

output_name = session.get_outputs()[0].name

# 推理

input_data = np.random.randn(1, 3, 224, 224).astype(np.float32)

output = session.run([output_name], {input_name: input_data})[0]

print(f"推理输出形状: {output.shape}")
```

### 5.3 模型量化

## 实例

```python
# ONNX 模型量化

import onnx

from onnxruntime.quantization import quantize_dynamic, QuantType

def quantize_onnx_model(input_path, output_path):

    """

    动态量化 ONNX 模型

    减少模型大小并加速推理

    """

    # 动态量化（不需要校准数据）

    quantize_dynamic(

        input_path,

        output_path,

        # 指定需要量化的权重类型

        weight_type=QuantType.QInt8

    )

    # 获取文件大小对比

    import os

    original_size = os.path.getsize(input_path) / 1024 / 1024

    quantized_size = os.path.getsize(output_path) / 1024 / 1024

    print(f"原始模型: {original_size:.2f} MB")

    print(f"量化模型: {quantized_size:.2f} MB")

    print(f"压缩比: {original_size/quantized_size:.2f}x")

# 使用

quantize_onnx_model("resnet18.onnx", "resnet18_quantized.onnx")
```

## 6. 移动端部署

### 6.1 导出到移动端格式

## 实例

```python
# 方式一：TorchScript 移动端部署

# 1. 追踪模型

model = ImageClassifier()

model.eval()

example_input = torch.randn(1, 3, 32, 32)

traced_model = torch.jit.trace(model, example_input)

# 2. 优化模型（移动端优化）

optimized_model = torch.jit.optimize_for_inference(traced_model)

# 3. 保存移动端模型

optimized_model.save("mobile_model.pt")

# 方式二：使用 torchmobile（如果可用）

# torchmobile 用于更轻量的移动端部署

# 请参考官方文档进行交叉编译

# 方式三：导出为 ONNX 并使用移动端运行时

# iOS: 使用 Core ML Tools

# Android: 使用 ONNX Runtime Mobile

print("移动端模型已准备")
```

### 6.2 Core ML 导出（iOS）

对于 iOS 平台，可以使用 Core ML Tools 将模型转换为 Core ML 格式。需要先转换为 ONNX 格式，再通过 Core ML Tools 转换。

## 实例

```python
# 需要安装 coremltools

# pip install coremltools

# Core ML 导出步骤

# 注意：这只在 macOS 上可用

# 步骤 1: 先将 PyTorch 模型导出为 ONNX

# from pytorch_example import your_model

# model = your_model()

# model.eval()

# example_input = torch.randn(1, 3, 224, 224)

# torch.onnx.export(

#     model,

#     example_input,

#     "model.onnx",

#     input_names=['input'],

#     output_names=['output']

# )

# 步骤 2: 使用 Core ML Tools 转换为 Core ML 格式

# from coremltools.converters import onnx as onnx_coreml

# coreml_model = onnx_coreml.convert(

#     model="model.onnx",

#     minimum_deployment_target='13',

#     image_input_names=['input']

# )

# coreml_model.save("model.mlmodel")

# 使用示例

print("iOS 部署需要 macOS 环境")

print("详细步骤：1. pip install coremltools  2. 导出 ONNX  3. 使用 coremltools 转换")
```

## 7. 最佳实践与常见问题

### 7.1 导出问题排查

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 导出失败 | 不支持的操作 | 使用 opset_version 更高的版本，或替换操作 |
| 输出不一致 | 动态控制流 | 使用脚本化而非追踪，或固定输入尺寸 |
| ONNX Runtime 错误 | 算子不支持 | 检查 ONNX 支持的操作列表 |

### 7.2 导出格式对比

| 格式 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| TorchScript (.pt) | PyTorch 原生支持 | 跨框架支持差 | 桌面/服务器部署 |
| ONNX (.onnx) | 跨框架、跨平台 | 有些操作不支持 | 通用部署 |

### 7.3 导出检查清单

## 实例

```python
# 导出前检查清单

def export_checklist(model, example_input):

    """导出前的检查"""

    model.eval()

    # 1. 确保模型在推理模式下

    print(f"模型模式: {'eval' if not model.training else 'train'}")

    # 2. 检查输入尺寸

    print(f"示例输入形状: {example_input.shape}")

    # 3. 验证前向传播

    with torch.no_grad():

        output = model(example_input)

    print(f"输出形状: {output.shape}")

    # 4. 检查是否有不可序列化的操作

    # 例如：lambda 函数

    for name, module in model.named_modules():

        if hasattr(module, '__call__'):

            pass  # 检查自定义模块

    print("✓ 导出检查完成")

# 使用示例

model = ImageClassifier()

example_input = torch.randn(1, 3, 32, 32)

export_checklist(model, example_input)
```

### 7.4 完整导出流程

## 实例

```python
# 完整的模型导出流程示例

class ProductionModel(nn.Module):

    """生产级模型"""

    def __init__(self):

        super().__init__()

        self.backbone = nn.Sequential(

            nn.Conv2d(3, 64, 7, stride=2, padding=3),

            nn.BatchNorm2d(64),

            nn.ReLU(),

            nn.MaxPool2d(3, stride=2, padding=1),

            # ... 更多层

        )

        self.head = nn.Linear(512, 10)

    def forward(self, x, return_features=False):

        features = self.backbone(x)

        features = torch.nn.functional.adaptive_avg_pool2d(features, 1).flatten(1)

        if return_features:

            return features

        return self.head(features)

# 完整导出流程

model = ProductionModel()

model.load_state_dict(torch.load("weights.pth"))  # 加载权重

model.eval()

# 准备示例输入

example_input = torch.randn(1, 3, 224, 224)

# 1. 追踪 TorchScript

traced = torch.jit.trace(model, example_input)

traced.save("model_traced.pt")

# 2. 导出 ONNX

torch.onnx.export(

    traced,

    example_input,

    "model.onnx",

    input_names=['input'],

    output_names=['output'],

    dynamic_axes={'input': {0: 'batch'}, 'output': {0: 'batch'}},

    opset_version=14

)

# 3. 优化 ONNX

# 使用 onnx-simplifier 去除冗余操作

# onnxsim model.onnx model_simplified.onnx

print("所有格式导出完成！")
```

---

# PyTorch 分布式训练

当模型越来越大、数据越来越多时，单 GPU 已经无法满足训练需求。

分布式训练通过多 GPU 甚至多台机器并行计算，可以显著缩短训练时间。

本节详细介绍 PyTorch 中的分布式训练技术，包括 DataParallel、DistributedDataParallel 以及混合精度分布式训练。

## 1. 分布式训练基础

### 1.1 为什么需要分布式训练

深度学习模型的规模逐年增长，训练时间也随之增加。分布式训练的核心目标是：将计算任务分散到多个计算单元上，在可接受的时间内完成大规模模型和数据的训练。

分布式训练主要解决两个问题：

- **显存不足**：大模型的参数、优化器状态、梯度需要大量显存

- **训练时间过长**：单 GPU 训练大模型可能需要数周甚至数月

### 1.2 分布式训练的两大模式

分布式训练主要分为两种模式：

| 模式 | 原理 | 适用场景 |
| --- | --- | --- |
| 数据并行（Data Parallel） | 每个计算单元保存完整模型，不同计算单元处理不同数据 | 模型能够装入单卡显存；数据量大，需要加速训练；小团队，机器资源有限 |
| 模型并行（Model Parallel） | 将模型拆分到多个计算单元，每个计算单元只保存部分模型 | 模型超大，单卡放不下；专用集群，多机训练 |

实际生产环境中，数据并行是最常用的方式。PyTorch 提供了 DataParallel 和 DistributedDataParallel 两种实现。

## 2. DataParallel 使用指南

### 2.1 单机多卡：DataParallel

DataParallel（DP） 是 PyTorch 提供的最简便的多 GPU 训练方式。它只需要修改几行代码，就可以利用单机上的多个 GPU 进行训练。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

# ── 模型定义 ──────────────────────────────────────

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(128, 256),

            nn.ReLU(),

            nn.Linear(256, 256),

            nn.ReLU(),

            nn.Linear(256, 10)

        )

    def forward(self, x):

        return self.net(x)

# 检查可用 GPU 数量

print(f"可用 GPU 数量: {torch.cuda.device_count()}")

# 创建模型并移到 GPU

model = SimpleModel()

# ── 方式一：使用 DataParallel（最简方式）───────

if torch.cuda.device_count() > 1:

    model = nn.DataParallel(model)

# 移动到 GPU（如果使用 DataParallel，device_ids 会自动处理）

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

# 损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ── 训练循环 ──────────────────────────────────────

def train_epoch_dp(model, loader, criterion, optimizer, device):

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item() * inputs.size(0)

        _, predicted = outputs.max(1)

        correct += predicted.eq(labels).sum().item()

        total += labels.size(0)

    return total_loss / total, correct / total

# 模拟数据

train_loader = [

    (torch.randn(32, 128), torch.randint(0, 10, (32,))) for _ in range(10)

]

# 开始训练

for epoch in range(3):

    loss, acc = train_epoch_dp(model, train_loader, criterion, optimizer, device)

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, Acc={acc:.4f}")

print("DataParallel 训练完成！")
```

### 2.2 DataParallel 的工作原理

DataParallel 的工作流程如下：

- **模型复制**：将模型复制到每个 GPU 上

- **数据分发**：将 batch 数据均匀分配到各个 GPU

- **并行计算**：每个 GPU 独立计算前向传播

- **梯度聚合**：将所有 GPU 的梯度汇总到主 GPU

- **参数更新**：主 GPU 更新参数后同步到其他 GPU

## 实例

```python
# DataParallel 关键参数说明

model = nn.DataParallel(

    module,                    # 要并行的模型（必填）

    device_ids=[0, 1, 2, 3],   # 使用的 GPU 设备 ID，默认使用所有卡

    output_device=0,            # 输出结果汇总到的设备，默认是第一张卡

    dim=0                      # 数据划分的维度，默认是 batch 维度

)

# 查看当前模型所在的设备

print(f"模型所在设备: {next(model.parameters()).device}")

# 查看实际使用的设备

print(f"使用的 GPU 数量: {model.device_ids if hasattr(model, 'device_ids') else 'N/A'}")
```

DataParallel 简单易用，但存在两个主要问题：1）主 GPU 显存压力大（需要汇总梯度）；2）GPU 之间的通信效率较低。因此，官方推荐使用 DistributedDataParallel。

## 3. DistributedDataParallel 详解

### 3.1 DDP 基础

DistributedDataParallel（DDP） 是 PyTorch 推荐的分布式训练方式。相比 DataParallel，DDP 具有以下优势：

- 每个 GPU 独立计算梯度，无需在主 GPU 汇总

- 使用高效的梯度同步算法（Ring AllReduce）

- 支持多机多卡训练

- 训练速度更快，显存利用更高效

### 3.2 DDP 单机多卡训练

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

import os

# ── 初始化分布式环境 ────────────────────────────

def setup(rank, world_size):

    """设置分布式环境"""

    # 设置当前进程使用的 GPU

    torch.cuda.set_device(rank)

    # 初始化进程组

    dist.init_process_group(

        backend="nccl",           # 使用 NCCL 后端（GPU 推荐）

        init_method="env://",     # 环境变量初始化方式

        world_size=world_size,    # 总进程数

        rank=rank                 # 当前进程排名

    )

def cleanup():

    """清理分布式环境"""

    dist.destroy_process_group()

# ── 数据加载器（支持分布式）───────────────────────

def get_distributed_loader(batch_size, world_size):

    """创建支持分布式的数据加载器"""

    from torch.utils.data import DataLoader, DistributedSampler

    # 模拟数据集

    dataset = torch.utils.data.TensorDataset(

        torch.randn(100, 3, 32, 32),

        torch.randint(0, 10, (100,))

    )

    # DistributedSampler 会自动划分数据

    sampler = DistributedSampler(

        dataset,

        num_replicas=world_size,

        rank=rank,

        shuffle=True

    )

    loader = DataLoader(

        dataset,

        batch_size=batch_size,

        sampler=sampler,

        num_workers=2,

        pin_memory=True

    )

    return loader

# ── 模型定义 ──────────────────────────────────────

class ImageClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 32, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten()

        )

        self.classifier = nn.Linear(64, 10)

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x

# ── DDP 训练函数 ──────────────────────────────────

def train_ddp(rank, world_size, epochs=3):

    """分布式训练主函数"""

    # 初始化

    setup(rank, world_size)

    # 创建模型并移到对应 GPU

    model = ImageClassifier().cuda(rank)

    # 包装为 DDP 模型

    ddp_model = DDP(

        model,

        device_ids=[rank],        # 指定当前进程使用的设备

        output_device=rank,

        find_unused_parameters=False  # 是否检测未使用的参数

    )

    # 损失函数和优化器

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(ddp_model.parameters(), lr=1e-3)

    # 获取数据加载器

    loader = get_distributed_loader(batch_size=16, world_size=world_size)

    # 训练循环

    for epoch in range(epochs):

        # 每个 epoch 开始时设置 epoch 号（用于打乱数据）

        loader.sampler.set_epoch(epoch)

        for batch_idx, (inputs, labels) in enumerate(loader):

            inputs = inputs.cuda(rank, non_blocking=True)

            labels = labels.cuda(rank, non_blocking=True)

            optimizer.zero_grad()

            outputs = ddp_model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            if rank == 0 and batch_idx % 5 == 0:

                print(f"Epoch {epoch+1}, Batch {batch_idx}, Loss: {loss.item():.4f}")

    # 清理

    if rank == 0:

        print("训练完成！")

    cleanup()

# 注意：实际运行时需要通过命令行参数指定 rank 和 world_size

# 此代码需要在每个进程中独立运行
```

### 3.3 启动分布式训练

PyTorch 分布式训练需要通过 torchrun 或 torch.distributed.launch 启动。以下是常用的启动方式：

## 实例

```python
# 方式一：使用 torchrun（推荐，PyTorch 2.0+）

# 文件：train_ddp.py

"""

使用方式：

torchrun --nproc_per_node=4 train_ddp.py

"""

# 方式二：使用 python -m（传统方式）

"""

python -m torch.distributed.launch --nproc_per_node=4 train_ddp.py

"""

# 方式三：多机多卡启动

# 机器 1（主节点）

torchrun --nnodes=2 --nproc_per_node=4 --node_rank=0 --master_addr=192.168.1.1 --master_port=29500 train_ddp.py

# 机器 2（从节点）

torchrun --nnodes=2 --nproc_per_node=4 --node_rank=1 --master_addr=192.168.1.1 --master_port=29500 train_ddp.py

# 参数说明：

# --nproc_per_node: 每个节点的 GPU 数量

# --nnodes: 节点数量

# --node_rank: 当前节点编号（从 0 开始）

# --master_addr: 主节点 IP 地址

# --master_port: 主节点端口号
```

### 3.4 完整的 DDP 训练脚本

## 实例

```python
# 完整的 DDP 训练脚本（保存为 train_ddp.py）

import torch

import torch.nn as nn

import torch.optim as optim

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

from torch.utils.data import DataLoader, DistributedSampler

import argparse

import os

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("--local_rank", type=int, default=-1, help="由 torchrun 自动传递")

    parser.add_argument("--epochs", type=int, default=10)

    parser.add_argument("--batch_size", type=int, default=32)

    parser.add_argument("--lr", type=float, default=1e-3)

    return parser.parse_args()

class TrainModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten(),

            nn.Linear(128, 10)

        )

    def forward(self, x):

        return self.net(x)

def setup(rank, world_size):

    os.environ["MASTER_ADDR"] = "localhost"

    os.environ["MASTER_PORT"] = "12355"

    dist.init_process_group("nccl", rank=rank, world_size=world_size)

    torch.cuda.set_device(rank)

def cleanup():

    dist.destroy_process_group()

def train(rank, world_size, args):

    setup(rank, world_size)

    # 创建模型

    model = TrainModel().cuda(rank)

    model = DDP(model, device_ids=[rank])

    # 优化器和损失函数

    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    criterion = nn.CrossEntropyLoss()

    # 数据集

    dataset = torch.utils.data.TensorDataset(

        torch.randn(1000, 3, 32, 32),

        torch.randint(0, 10, (1000,))

    )

    # DistributedSampler 确保每个进程看到不同的数据

    sampler = DistributedSampler(

        dataset,

        num_replicas=world_size,

        rank=rank,

        shuffle=True

    )

    loader = DataLoader(

        dataset,

        batch_size=args.batch_size,

        sampler=sampler,

        num_workers=2,

        pin_memory=True

    )

    # 训练循环

    for epoch in range(args.epochs):

        # 关键：每个 epoch 都要设置 epoch，打乱数据划分

        sampler.set_epoch(epoch)

        model.train()

        epoch_loss = 0

        for inputs, labels in loader:

            inputs = inputs.cuda(rank, non_blocking=True)

            labels = labels.cuda(rank, non_blocking=True)

            optimizer.zero_grad()

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            epoch_loss += loss.item()

        # 同步所有进程，确保每个进程都完成当前 epoch

        dist.barrier()

        if rank == 0:

            avg_loss = epoch_loss / len(loader)

            print(f"Epoch {epoch+1}/{args.epochs}, Loss: {avg_loss:.4f}")

    cleanup()

if __name__ == "__main__":

    args = parse_args()

    # 从环境变量获取 world_size

    world_size = int(os.environ["WORLD_SIZE"])

    # 从环境变量获取 rank（由 torchrun 自动设置）

    rank = int(os.environ["RANK"])

    if torch.cuda.is_available():

        train(rank, world_size, args)

    else:

        print("需要 CUDA 环境才能运行分布式训练")
```

关键点：每个 epoch 都需要调用 `sampler.set_epoch(epoch)`，确保数据划分被打乱，否则多个进程会看到相同的数据。

## 4. 分布式训练中的混合精度

### 4.1 DDP + AMP 组合

分布式训练与混合精度训练结合，可以进一步提升训练速度。PyTorch 2.0+ 的 DDP 已经与 AMP 完美集成。

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

from torch.cuda.amp import autocast, GradScaler

class AMPModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten(),

            nn.Linear(128, 10)

        )

    def forward(self, x):

        return self.net(x)

def train_ddp_amp(rank, world_size):

    """分布式 + 混合精度训练"""

    # 初始化

    torch.cuda.set_device(rank)

    dist.init_process_group("nccl", rank=rank, world_size=world_size)

    # 创建模型

    model = AMPModel().cuda(rank)

    model = DDP(model, device_ids=[rank])

    # 优化器和 GradScaler

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    scaler = GradScaler()

    criterion = nn.CrossEntropyLoss()

    # 训练循环

    model.train()

    for inputs, labels in loader:

        inputs = inputs.cuda(rank, non_blocking=True)

        labels = labels.cuda(rank, non_blocking=True)

        optimizer.zero_grad()

        # 使用 autocast 自动切换精度

        with autocast(device_type='cuda'):

            outputs = model(inputs)

            loss = criterion(outputs, labels)

        # 使用 scaler 处理梯度缩放

        scaler.scale(loss).backward()

        # 梯度裁剪（需要先 unscale）

        scaler.unscale_(optimizer)

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        scaler.step(optimizer)

        scaler.update()

    dist.destroy_process_group()

# 启动命令

# torchrun --nproc_per_node=4 train_ddp_amp.py
```

### 4.2 分布式训练中的梯度同步

DDP 使用 Ring AllReduce 算法进行梯度同步，其工作原理如下：

- 每个 GPU 将梯度分为 n 份（n 为 GPU 数量）

- 每个 GPU 与相邻 GPU 交换一份梯度

- 重复 n 次后，每个 GPU 拥有完整的梯度

## 实例

```python
# DDP 梯度同步相关配置

# 1. 设置梯度 bucket 的缓冲区大小

model = DDP(

    model,

    device_ids=[rank],

    gradient_as_bucket_view=True,  # 节省显存（PyTorch 1.8+）

    broadcast_buffers=False,        # 不广播 buffers，减少通信

    bucket_cap_mb=25               # 梯度 bucket 大小（MB）

)

# 2. 手动同步模型参数（如需要）

# 在某些场景下，需要手动同步模型参数

def sync_params(model):

    for param in model.parameters():

        dist.broadcast(param, src=0)

# 3. 检查梯度同步状态

# DDP 会自动处理梯度同步，无需手动操作

# 但可以通过以下方式检查

for name, param in model.named_parameters():

    if param.grad is not None:

        print(f"{name}: grad requires_grad={param.grad.requires_grad}")
```

## 5. 模型并行与流水线

### 5.1 简单的模型并行

当模型太大，单个 GPU 无法容纳时，需要将模型拆分到多个 GPU 上。

## 实例

```python
# 模型并行示例：将模型的不同层放到不同 GPU

class ModelParallel(nn.Module):

    def __init__(self, num_gpus=2):

        super().__init__()

        self.num_gpus = num_gpus

        # 第一部分：GPU 0

        self.features1 = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.ReLU(),

            nn.MaxPool2d(2)

        ).to(f"cuda:0")

        # 第二部分：GPU 1

        self.features2 = nn.Sequential(

            nn.Conv2d(64, 128, 3, padding=1),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten()

        ).to(f"cuda:1")

        # 分类器：GPU 0

        self.classifier = nn.Linear(128, 10).to(f"cuda:0")

    def forward(self, x):

        # 数据在不同 GPU 之间传递

        x = x.to("cuda:0")

        x = self.features1(x)

        x = x.to("cuda:1")

        x = self.features2(x)

        x = x.to("cuda:0")

        x = self.classifier(x)

        return x

# 使用

model = ModelParallel(num_gpus=2)

output = model(torch.randn(1, 3, 32, 32))

print(f"输出设备: {output.device}")
```

### 5.2 流水线并行（Pipeline Parallelism）

PyTorch 提供了 torch.distributed.pipeline.sync 模块（PP 包）实现流水线并行，将模型按层拆分，形成计算流水线。

## 实例

```python
# 流水线并行示例（需要安装 torch-pipeline 依赖）

# pip install torch-pipeline

"""

# 注意：PyTorch 原生流水线需要使用特定版本或第三方库

# 这里展示概念，简化实现

from torch.distributed.pipeline.sync import Pipe

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1 = nn.Linear(128, 256)

        self.layer2 = nn.Linear(256, 256)

        self.layer3 = nn.Linear(256, 10)

    def forward(self, x):

        x = torch.relu(self.layer1(x))

        x = torch.relu(self.layer2(x))

        x = self.layer3(x)

        return x

# 将模型按层拆分到不同 GPU

# layer1 -> GPU 0

# layer2 -> GPU 1

# layer3 -> GPU 2

model = SimpleModel()

model.layer1 = model.layer1.cuda(0)

model.layer2 = model.layer2.cuda(1)

model.layer3 = model.layer3.cuda(2)

# 使用 Pipeline 将模型连接

# 注意：实际使用需要安装对应版本的 pipeline 库

# from torch.distributed.pipeline.sync import Pipe

# model = Pipe(model, chunks=4)

"""

print("流水线并行需要额外安装 torch-pipeline 库")

print("pip install torch-pipeline-sync")
```

## 6. 分布式训练最佳实践

### 6.1 性能优化技巧

| 优化项 | 技巧 | 说明 |
| --- | --- | --- |
| 通信优化 | 使用 NCCL 后端 | NCCL 是 GPU 最佳选择；比 Gloo 更快 |
| 数据加载 | 设置 num_workers 和 pin_memory | num_workers 设置为 CPU 核心数；pin_memory 加速 CPU 到 GPU 传输 |
| 梯度同步 | 调整 bucket_cap_mb | 大模型可增大 bucket；小模型可减小以提高响应 |
| 混合精度 | DDP + AMP | 减少通信量；提高训练速度 |

### 6.2 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 通信慢 | 网络带宽不足 | 使用 InfiniBand 或高速网络 |
| 显存不足 | batch size 过大 | 减小 batch size 或使用梯度累积 |
| 负载不均衡 | 模型划分不合理 | 调整层分布，尽量均匀 |
| 同步错误 | 梯度 NaN | 检查梯度裁剪和缩放设置 |

### 6.3 完整的多机多卡训练脚本

## 实例

```python
# 完整的多机多卡训练脚本模板

import torch

import torch.nn as nn

import torch.optim as optim

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

from torch.utils.data import DataLoader, DistributedSampler

import argparse

import os

class TrainingConfig:

    def __init__(self):

        self.local_rank = -1

        self.epochs = 30

        self.batch_size = 32

        self.lr = 1e-3

        self.num_workers = 4

        self.gradient_clip = 1.0

        self.use_amp = True

def init_distributed(config):

    """初始化分布式环境"""

    # 从环境变量获取配置

    local_rank = config.local_rank

    # NCCL 配置

    os.environ["NCCL_DEBUG"] = "WARN"

    torch.cuda.set_device(local_rank)

    dist.init_process_group(backend="nccl")

    return local_rank

def create_dataloader(dataset, config, world_size, rank):

    """创建数据加载器"""

    sampler = DistributedSampler(

        dataset,

        num_replicas=world_size,

        rank=rank,

        shuffle=True,

        drop_last=True

    )

    loader = DataLoader(

        dataset,

        batch_size=config.batch_size,

        sampler=sampler,

        num_workers=config.num_workers,

        pin_memory=True,

        persistent_workers=True

    )

    return loader, sampler

def train_epoch(model, loader, criterion, optimizer, scaler, config, rank):

    """训练一个 epoch"""

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in loader:

        inputs = inputs.cuda(rank, non_blocking=True)

        labels = labels.cuda(rank, non_blocking=True)

        optimizer.zero_grad()

        if config.use_amp and scaler is not None:

            # 混合精度训练

            with torch.cuda.amp.autocast():

                outputs = model(inputs)

                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()

            scaler.unscale_(optimizer)

            torch.nn.utils.clip_grad_norm_(model.parameters(), config.gradient_clip)

            scaler.step(optimizer)

            scaler.update()

        else:

            # 普通训练

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            torch.nn.utils.clip_grad_norm_(model.parameters(), config.gradient_clip)

            optimizer.step()

        total_loss += loss.item() * inputs.size(0)

        _, predicted = outputs.max(1)

        correct += predicted.eq(labels).sum().item()

        total += labels.size(0)

    return total_loss / total, correct / total

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--local_rank", type=int, default=-1)

    args = parser.parse_args()

    config = TrainingConfig()

    config.local_rank = args.local_rank

    rank = init_distributed(config)

    world_size = dist.get_world_size()

    print(f"进程 {rank}/{world_size} 初始化完成")

    # 创建模型

    model = YourModel().cuda(rank)

    model = DDP(model, device_ids=[rank])

    # 优化器

    optimizer = optim.Adam(model.parameters(), lr=config.lr)

    # GradScaler（如果使用混合精度）

    scaler = GradScaler() if config.use_amp else None

    # 数据集（替换为你的数据集）

    dataset = YourDataset()

    loader, sampler = create_dataloader(dataset, config, world_size, rank)

    criterion = nn.CrossEntropyLoss()

    # 训练循环

    for epoch in range(config.epochs):

        sampler.set_epoch(epoch)

        loss, acc = train_epoch(model, loader, criterion, optimizer, scaler, config, rank)

        # 只在 rank 0 打印

        if rank == 0:

            print(f"Epoch {epoch+1}/{config.epochs}: Loss={loss:.4f}, Acc={acc:.4f}")

    dist.destroy_process_group()

# 启动方式：

# torchrun --nnodes=2 --nproc_per_node=4 --node_rank=0 --master_addr=192.168.1.1 --master_port=29500 train.py

# torchrun --nnodes=2 --nproc_per_node=4 --node_rank=1 --master_addr=192.168.1.1 --master_port=29500 train.py
```

分布式训练的关键是：1）选择合适的并行模式（数据并行 vs 模型并行）；2）使用 DDP 代替 DataParallel 以获得更好的性能；3）结合混合精度训练进一步加速；4）合理设置数据加载器和通信参数。

## 7. 分布式训练监控与调试

### 7.1 常用监控工具

## 实例

```python
# 分布式训练监控代码

def monitor_training(rank, world_size):

    """监控分布式训练状态"""

    # 1. 检查进程组状态

    print(f"Rank: {rank}, World Size: {world_size}")

    print(f"Backend: {dist.get_backend()}")

    print(f"Rank: {dist.get_rank()}")

    print(f"CUDA Device: {torch.cuda.current_device()}")

    # 2. 监控显存使用

    if torch.cuda.is_available():

        for i in range(torch.cuda.device_count()):

            allocated = torch.cuda.memory_allocated(i) / 1024**2

            reserved = torch.cuda.memory_reserved(i) / 1024**2

            print(f"GPU {i}: 已分配 {allocated:.1f} MB, 预留 {reserved:.1f} MB")

    # 3. 监控梯度同步

    # DDP 会自动记录同步时间

    # 可以通过设置环境变量启用详细日志

    # os.environ["NCCL_DEBUG"] = "INFO"

# 在训练循环中定期调用

monitor_training(rank, dist.get_world_size())
```

### 7.2 调试技巧

- 先在单机上测试，再扩展到多机

- 使用 `os.environ["NCCL_DEBUG"] = "INFO"` 查看详细通信日志

- 确保所有机器的时间同步（使用 NTP）

- 检查防火墙是否允许 NCCL 通信端口

分布式训练虽然增加了复杂度，但带来的性能提升是显著的。对于大模型训练，几乎是必备的技术手段。

---

-

# PyTorch 注意力机制

注意力机制（Attention Mechanism）是深度学习中最重要的概念之一。

注意力机制让模型学会"关注"输入中最相关的部分，在自然语言处理、计算机视觉等领域取得了巨大成功。

本节详细介绍注意力机制的核心原理、PyTorch 实现以及各种注意力变体。

**适用版本：**本文代码基于 PyTorch 2.0+ 编写。`nn.MultiheadAttention` 的 `batch_first` 参数在 PyTorch 1.9 引入，早期版本需要手动处理维度。

## 1. 注意力机制基础

### 1.1 为什么需要注意力

传统的序列到序列（Seq2Seq）模型存在一个根本问题：Encoder 需要将所有信息压缩到一个固定长度的向量中。对于长序列，这个向量会成为信息瓶颈——句子越长，信息丢失越严重。

注意力机制的核心理念是：让 Decoder 在生成每个输出时，能够"看"到 Encoder 的所有隐藏状态，并根据当前上下文动态地分配不同的注意力权重。这就像人类翻译时，每翻译一个词都会回头去看原文的对应部分。

  Seq2Seq：固定向量 vs 注意力机制

  固定向量（信息瓶颈）

    x₁

    x₂

    x₃

    x₄

-

  c（固定向量）

-

    y₁

    y₂

    y₃

    y₄

  所有解码步共享同一个 c

-

  注意力机制（动态加权）

    h₁

    h₂

    h₃

    h₄

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

    y₁

    y₂

    y₃

    y₄

  每步生成不同的上下文向量 c_t

  线越粗 → 注意力权重越大 → 该位置信息越重要

### 1.2 注意力机制的本质

注意力机制可以看作是一种加权求和操作。给定查询（Query）、键（Key）和值（Value），通过计算 Query 与每个 Key 的相似度来分配权重，再对 Value 进行加权求和：

\[\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\]$$

其中：

- **Q（Query）**：查询向量，表示"我正在寻找什么信息"

- **K（Key）**：键向量，表示"我这里有什么信息"（用于匹配）

- **V（Value）**：值向量，表示"我实际能提供的内容"

- **$$d_k$$**：Key 的维度，$$\sqrt{d_k}$$ 用于缩放，防止点积值过大导致 softmax 梯度消失

为什么要除以 $$\sqrt{d_k}$$？当 $$d_k$$ 较大时，Q 和 K 的点积的方差会随维度线性增长，导致 softmax 的输入值过大，梯度趋近于零。缩放后使方差恢复到 1，保证梯度正常流动。

  Scaled Dot-Product Attention 计算流程

  Q
  [batch, seq_q, d_k]

  K
  [batch, seq_k, d_k]

-

-

  MatMul
  QKᵀ

-

  Scale
  ÷ √d_k

-

  Softmax
  归一化

-

  V
  [batch, seq_k, d_v]

-

  MatMul
  × V

-

  Output

    Mask（可选）
    -∞ 填充

-

    Output = softmax(QKᵀ / √d_k) · V

    输出形状: [batch, seq_q, d_v] — 每个 Query 位置得到一个 d_v 维的上下文向量

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

def scaled_dot_product_attention(Q, K, V, mask=None):

    """

    缩放点积注意力

    参数:

        Q: 查询张量 [batch, n_heads, seq_len_q, d_k]

        K: 键张量 [batch, n_heads, seq_len_k, d_k]

        V: 值张量 [batch, n_heads, seq_len_v, d_v]

        mask: 掩码张量，被掩码位置设为 False/0

    返回:

        output: 注意力输出 [batch, n_heads, seq_len_q, d_v]

        attention_weights: 注意力权重 [batch, n_heads, seq_len_q, seq_len_k]

    """

    d_k = Q.size(-1)

    # 1. 计算 QK^T / sqrt(d_k)

    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)

    # 2. 应用掩码（可选）

    #    掩码位置设为极小值，softmax 后趋近于 0

    if mask is not None:

        scores = scores.masked_fill(mask == 0, -1e9)

    # 3. Softmax 归一化 → 注意力权重

    attention_weights = F.softmax(scores, dim=-1)

    # 4. 加权求和

    output = torch.matmul(attention_weights, V)

    return output, attention_weights

# 测试

batch_size, n_heads = 2, 4

seq_len_q, seq_len_k = 5, 6

d_k, d_v = 8, 16

Q = torch.randn(batch_size, n_heads, seq_len_q, d_k)

K = torch.randn(batch_size, n_heads, seq_len_k, d_k)

V = torch.randn(batch_size, n_heads, seq_len_k, d_v)

output, attn_weights = scaled_dot_product_attention(Q, K, V)

print(f"输出形状: {output.shape}")            # [2, 4, 5, 16]

print(f"注意力权重形状: {attn_weights.shape}")  # [2, 4, 5, 6]

print(f"权重行求和（应为 1.0）: {attn_weights[0, 0, 0].sum().item():.4f}")
```

注意力权重的本质是概率分布——经过 softmax 后，每一行的和为 1。权重越大表示模型对该位置越"关注"。

## 2. PyTorch 注意力模块

### 2.1 Multi-Head Attention

Multi-Head Attention（多头注意力） 允许模型同时关注来自不同位置的不同表示子空间的信息。它将 Q、K、V 分别通过不同的线性投影映射到多个子空间，在每个子空间独立计算注意力，最后拼接结果再做一次线性变换。

这就像让多个人从不同角度同时审视同一段文本——有人关注语法结构，有人关注语义关联，有人关注长距离依赖。多头机制让模型能捕获更丰富的模式。

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$

$$\text{where head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0, "d_model 必须能被 n_heads 整除"

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads  # 每个头的维度

        # Q、K、V 的线性投影（一次计算所有头，更高效）

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        # 输出投影

        self.w_o = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):

        """

        参数:

            query: [batch, seq_len_q, d_model]

            key:   [batch, seq_len_k, d_model]

            value: [batch, seq_len_k, d_model]

            mask:  [batch, 1, 1, seq_len_k] 或 [batch, 1, seq_len_q, seq_len_k]

        """

        batch_size = query.size(0)

        # 1. 线性投影，然后分头

        #    [batch, seq_len, d_model] → [batch, seq_len, n_heads, d_k]

        #    → [batch, n_heads, seq_len, d_k]

        Q = self.w_q(query).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        K = self.w_k(key).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        V = self.w_v(value).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        # 2. 缩放点积注意力

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:

            scores = scores.masked_fill(mask == 0, -1e9)

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 3. 加权求和

        context = torch.matmul(attn_weights, V)

        # 4. 合并多头：[batch, n_heads, seq_len, d_k] → [batch, seq_len, d_model]

        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # 5. 输出投影

        output = self.w_o(context)

        return output, attn_weights

# 测试

d_model, n_heads = 128, 8

seq_len, batch = 10, 4

layer = MultiHeadAttention(d_model, n_heads)

query = torch.randn(batch, seq_len, d_model)

key = torch.randn(batch, seq_len, d_model)

value = torch.randn(batch, seq_len, d_model)

output, attn_weights = layer(query, key, value)

print(f"输出形状: {output.shape}")           # [4, 10, 128]

print(f"注意力权重形状: {attn_weights.shape}") # [4, 8, 10, 10]

print(f"每头维度 d_k = {d_model // n_heads}")
```

### 2.2 PyTorch 内置 MultiheadAttention

PyTorch 提供了经过高度优化的 `nn.MultiheadAttention`，底层使用了融合算子（fused kernels），在大多数场景下比手动实现更快。推荐在生产环境中使用。

## 实例

```python
import torch

import torch.nn as nn

class TransformerAttention(nn.Module):

    """使用 PyTorch 内置 MultiheadAttention 的自注意力层"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        self.attention = nn.MultiheadAttention(

            embed_dim=d_model,

            num_heads=n_heads,

            dropout=dropout,

            batch_first=True,  # 输入格式为 [batch, seq, features]

            # PyTorch 2.0+ 可启用 Flash Attention 后端：

            # attn_implementation="flash_attention_2"  # 需要安装 flash-attn

        )

        self.layernorm = nn.LayerNorm(d_model)

    def forward(self, x, key_padding_mask=None):

        """

        自注意力：Q、K、V 都是 x

        参数:

            x: [batch, seq_len, d_model]

            key_padding_mask: [batch, seq_len]，True 表示该位置是 padding

        """

        attn_output, attn_weights = self.attention(

            x, x, x,  # self-attention

            key_padding_mask=key_padding_mask

        )

        # Pre-Norm 残差连接（比 Post-Norm 训练更稳定）

        output = self.layernorm(x + attn_output)

        return output, attn_weights

# 测试

d_model, n_heads = 128, 8

seq_len, batch = 10, 4

model = TransformerAttention(d_model, n_heads)

x = torch.randn(batch, seq_len, d_model)

# 创建 padding mask：True 表示该位置应被忽略

key_padding_mask = torch.zeros(batch, seq_len, dtype=torch.bool)

key_padding_mask[0, 7:] = True   # 第一个样本的后 3 个位置是 padding

key_padding_mask[1, 5:] = True   # 第二个样本的后 5 个位置是 padding

output, attn_weights = model(x, key_padding_mask=key_padding_mask)

print(f"输出形状: {output.shape}")           # [4, 10, 128]

print(f"注意力权重形状: {attn_weights.shape}") # [4, 10, 10]
```

**注意 mask 类型：**`nn.MultiheadAttention` 的 `key_padding_mask` 使用 **True = 忽略** 的约定，与某些自定义实现中 0 = 忽略的约定相反。使用时务必确认。

## 3. 注意力机制的变体

### 3.1 自注意力（Self-Attention）

自注意力 是注意力机制的一种特殊形式——Q、K、V 都来自同一个输入序列。它让序列中的每个位置都能直接关注到所有其他位置，从而捕获全局依赖关系。这是 Transformer 的核心组件，也是它优于 RNN 的关键所在：RNN 需要逐步传递信息，而自注意力一步到位。

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class SelfAttention(nn.Module):

    """多头自注意力层，支持因果掩码（用于自回归生成）"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        self.out_proj = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def _split_heads(self, x, batch_size):

        """[batch, seq, d_model] → [batch, n_heads, seq, d_k]"""

        return x.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

    def forward(self, x, causal=False):

        """

        自注意力：Q、K、V 都来自同一个输入 x

        参数:

            x: [batch, seq_len, d_model]

            causal: 是否使用因果掩码（防止看到未来位置）

        """

        batch_size, seq_len, _ = x.size()

        # 投影 + 分头

        Q = self._split_heads(self.w_q(x), batch_size)

        K = self._split_heads(self.w_k(x), batch_size)

        V = self._split_heads(self.w_v(x), batch_size)

        # 计算注意力分数

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        # 因果掩码：上三角矩阵设为 -inf，防止看到未来 token

        if causal:

            causal_mask = torch.triu(

                torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),

                diagonal=1

            )

            scores = scores.masked_fill(causal_mask.unsqueeze(0).unsqueeze(0), float('-inf'))

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 加权求和 + 合并多头

        context = torch.matmul(attn_weights, V)

        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

        return self.out_proj(context), attn_weights

# 测试

d_model, n_heads = 256, 8

seq_len, batch = 20, 2

attn = SelfAttention(d_model, n_heads)

x = torch.randn(batch, seq_len, d_model)

# 不使用因果掩码（Encoder 场景）

output_enc, weights_enc = attn(x, causal=False)

print(f"[Encoder] 输出: {output_enc.shape}, 权重: {weights_enc.shape}")

# 使用因果掩码（Decoder / 自回归生成场景）

output_dec, weights_dec = attn(x, causal=True)

print(f"[Decoder] 输出: {output_dec.shape}, 权重: {weights_dec.shape}")

# 验证因果性：第一个 token 不应该关注后面的 token

print(f"causal=True 时，weights[0,0,0,5:]（应全为0）: {weights_dec[0, 0, 0, 5:].tolist()[:5]}")
```

### 3.2 交叉注意力（Cross-Attention）

交叉注意力 中，Q 来自一个序列（如 Decoder），K 和 V 来自另一个序列（如 Encoder）。这是 Encoder-Decoder 架构的桥梁——让 Decoder 在生成每个 token 时，能动态地"查阅"Encoder 的所有输出。

## 实例

```python
import torch

import torch.nn as nn

import torch.nn.functional as F

import math

class CrossAttention(nn.Module):

    """交叉注意力：Q 来自目标序列，K/V 来自源序列"""

    def __init__(self, d_model, n_heads, dropout=0.1):

        super().__init__()

        assert d_model % n_heads == 0

        self.d_model = d_model

        self.n_heads = n_heads

        self.d_k = d_model // n_heads

        self.w_q = nn.Linear(d_model, d_model)

        self.w_k = nn.Linear(d_model, d_model)

        self.w_v = nn.Linear(d_model, d_model)

        self.out_proj = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, target, source, mask=None):

        """

        参数:

            target: 目标序列 [batch, target_len, d_model]  → 提供 Q

            source: 源序列   [batch, source_len, d_model]  → 提供 K, V

            mask:   可选掩码

        """

        batch_size = target.size(0)

        target_len = target.size(1)

        source_len = source.size(1)

        # 投影 + 分头

        Q = self.w_q(target).view(batch_size, target_len, self.n_heads, self.d_k).transpose(1, 2)

        K = self.w_k(source).view(batch_size, source_len, self.n_heads, self.d_k).transpose(1, 2)

        V = self.w_v(source).view(batch_size, source_len, self.n_heads, self.d_k).transpose(1, 2)

        # 注意力计算

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:

            scores = scores.masked_fill(mask == 0, float('-inf'))

        attn_weights = F.softmax(scores, dim=-1)

        attn_weights = self.dropout(attn_weights)

        # 加权求和 + 合并多头

        context = torch.matmul(attn_weights, V)

        context = context.transpose(1, 2).contiguous().view(batch_size, target_len, self.d_model)

        return self.out_proj(context), attn_weights

# 测试

d_model, n_heads = 256, 8

batch = 2

target_len, source_len = 10, 15

cross_attn = CrossAttention(d_model, n_heads)

target = torch.randn(batch, target_len, d_model)  # Decoder 输出

source = torch.randn(batch, source_len, d_model)  # Encoder 输出

output, weights = cross_attn(target, source)

print(f"目标序列形状: {target.shape}")

print(f"源序列形状:   {source.shape}")

print(f"输出形状:     {output.shape}")            # [2, 10, 256]

print(f"权重形状:     {weights.shape}")            # [2, 8, 10, 15]

# 权重含义：每个 target 位置对每个 source 位置的关注程度
```

**自注意力 vs 交叉注意力：**自注意力中 Q/K/V 形状相同（$$seq \times seq$$ 的权重矩阵）；交叉注意力中 Q 长度与 K 长度可以不同（$$target \times source$$ 的权重矩阵）。

### 3.3 位置编码（Positional Encoding）

注意力机制本身具有**置换不变性**——打乱输入顺序不会改变输出。但语言和图像都是有序的，因此需要通过位置编码显式注入位置信息。原始 Transformer 使用正弦/余弦函数生成固定的位置编码：

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right), \quad PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

## 实例

```python
import torch

import torch.nn as nn

import math

class PositionalEncoding(nn.Module):

    """正弦/余弦位置编码（Transformer 原始方案）"""

    def __init__(self, d_model, max_len=5000, dropout=0.1):

        super().__init__()

        self.dropout = nn.Dropout(p=dropout)

        # 预计算位置编码矩阵 [max_len, d_model]

        pe = torch.zeros(max_len, d_model)

        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # div_term: 控制不同频率维度的衰减速度

        div_term = torch.exp(

            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)

        )

        pe[:, 0::2] = torch.sin(position * div_term)  # 偶数维度

        pe[:, 1::2] = torch.cos(position * div_term)  # 奇数维度

        pe = pe.unsqueeze(0)  # [1, max_len, d_model]

        self.register_buffer('pe', pe)  # 不参与训练

    def forward(self, x):

        """

        x: [batch, seq_len, d_model]

        返回: x + positional_encoding

        """

        x = x + self.pe[:, :x.size(1), :]

        return self.dropout(x)

# 测试

d_model = 128

seq_len = 50

batch = 4

pe = PositionalEncoding(d_model)

x = torch.randn(batch, seq_len, d_model)

output = pe(x)

print(f"输入形状: {x.shape}")

print(f"输出形状: {output.shape}")

print(f"位置编码形状: {pe.pe.shape}")  # [1, 5000, 128]
```

## 4. 注意力机制的视觉应用

注意力机制不仅适用于序列数据，在计算机视觉中同样大放异彩。以下介绍三种经典的视觉注意力模块：

### 4.1 通道注意力（Channel Attention）

通道注意力（如 SENet）让网络学习"哪些通道更重要"。它对每个通道进行全局池化压缩空间信息，再通过两层全连接网络学习通道间的依赖关系。

## 实例

```python
import torch

import torch.nn as nn

class SEBlock(nn.Module):

    """Squeeze-and-Excitation Block（通道注意力）"""

    def __init__(self, channels, reduction=16):

        super().__init__()

        self.squeeze = nn.AdaptiveAvgPool2d(1)  # 全局平均池化

        self.excitation = nn.Sequential(

            nn.Linear(channels, channels // reduction, bias=False),

            nn.ReLU(inplace=True),

            nn.Linear(channels // reduction, channels, bias=False),

            nn.Sigmoid()  # 输出 0~1 的通道权重

        )

    def forward(self, x):

        # x: [batch, channels, H, W]

        b, c, _, _ = x.size()

        # Squeeze: [B, C, H, W] → [B, C, 1, 1] → [B, C]

        y = self.squeeze(x).view(b, c)

        # Excitation: 学习通道权重 [B, C]

        y = self.excitation(y).view(b, c, 1, 1)

        # 通道加权：每个通道乘以对应的权重

        return x * y.expand_as(x)

# 测试

se = SEBlock(channels=256, reduction=16)

x = torch.randn(4, 256, 32, 32)

output = se(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 4.2 空间注意力（Spatial Attention）

空间注意力 让网络学习"哪些位置更重要"。它在通道维度上进行压缩（取均值和最大值），然后用卷积学习空间权重图。

## 实例

```python
import torch

import torch.nn as nn

class SpatialAttention(nn.Module):

    """空间注意力模块"""

    def __init__(self, kernel_size=7):

        super().__init__()

        padding = kernel_size // 2

        # 输入 2 个通道（均值 + 最大值），输出 1 个通道（注意力图）

        self.conv = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):

        # x: [batch, channels, H, W]

        # 通道压缩：取均值和最大值 → [B, 1, H, W] 各一个

        avg_out = torch.mean(x, dim=1, keepdim=True)

        max_out, _ = torch.max(x, dim=1, keepdim=True)

        # 拼接 → [B, 2, H, W]

        scale = torch.cat([avg_out, max_out], dim=1)

        # 卷积 + Sigmoid → 空间权重图 [B, 1, H, W]

        scale = self.sigmoid(self.conv(scale))

        # 空间加权

        return x * scale

# 测试

spatial_attn = SpatialAttention(kernel_size=7)

x = torch.randn(4, 256, 32, 32)

output = spatial_attn(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 4.3 CBAM（Convolutional Block Attention Module）

CBAM 将通道注意力和空间注意力**串联**应用：先通过通道注意力选择重要通道，再通过空间注意力选择重要位置。两者互补，效果优于单独使用。

## 实例

```python
import torch

import torch.nn as nn

class CBAM(nn.Module):

    """CBAM: 通道注意力 + 空间注意力"""

    def __init__(self, channels, reduction=16, kernel_size=7):

        super().__init__()

        # 通道注意力

        self.channel_attn = nn.Sequential(

            nn.AdaptiveAvgPool2d(1),

            nn.Flatten(),

            nn.Linear(channels, channels // reduction, bias=False),

            nn.ReLU(inplace=True),

            nn.Linear(channels // reduction, channels, bias=False),

            nn.Sigmoid()

        )

        # 空间注意力

        self.spatial_attn = nn.Sequential(

            nn.Conv2d(2, 1, kernel_size, padding=kernel_size // 2, bias=False),

            nn.Sigmoid()

        )

    def forward(self, x):

        # 1. 通道注意力

        b, c, _, _ = x.size()

        ca = self.channel_attn(x).view(b, c, 1, 1)

        x = x * ca

        # 2. 空间注意力

        avg_out = torch.mean(x, dim=1, keepdim=True)

        max_out, _ = torch.max(x, dim=1, keepdim=True)

        sa = self.spatial_attn(torch.cat([avg_out, max_out], dim=1))

        x = x * sa

        return x

# 测试

cbam = CBAM(channels=256)

x = torch.randn(4, 256, 32, 32)

output = cbam(x)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

## 5. 注意力机制在 NLP 中的应用

### 5.1 Transformer Encoder

Transformer Encoder 由 N 个相同的层堆叠而成，每层包含两个子层：**多头自注意力**和**前馈网络**。每个子层都使用残差连接和层归一化。

## 实例

```python
import torch

import torch.nn as nn

import math

class TransformerEncoderLayer(nn.Module):

    """单层 Transformer Encoder"""

    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):

        super().__init__()

        # 多头自注意力

        self.self_attn = nn.MultiheadAttention(

            d_model, n_heads, dropout=dropout, batch_first=True

        )

        # 前馈网络（两层线性 + 激活）

        self.ffn = nn.Sequential(

            nn.Linear(d_model, d_ff),

            nn.GELU(),  # GELU 比 ReLU 更常用

            nn.Dropout(dropout),

            nn.Linear(d_ff, d_model)

        )

        # 层归一化（Pre-Norm 风格，训练更稳定）

        self.norm1 = nn.LayerNorm(d_model)

        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, key_padding_mask=None):

        # 子层 1: 自注意力

        residual = x

        x = self.norm1(x)  # Pre-Norm

        attn_out, _ = self.self_attn(x, x, x, key_padding_mask=key_padding_mask)

        x = residual + self.dropout(attn_out)

        # 子层 2: 前馈网络

        residual = x

        x = self.norm2(x)  # Pre-Norm

        x = residual + self.dropout(self.ffn(x))

        return x

class TransformerEncoder(nn.Module):

    """多层 Transformer Encoder"""

    def __init__(self, d_model, n_heads, d_ff, num_layers, dropout=0.1):

        super().__init__()

        self.layers = nn.ModuleList([

            TransformerEncoderLayer(d_model, n_heads, d_ff, dropout)

            for _ in range(num_layers)

        ])

        self.final_norm = nn.LayerNorm(d_model)

    def forward(self, x, key_padding_mask=None):

        for layer in self.layers:

            x = layer(x, key_padding_mask)

        return self.final_norm(x)

# 测试

d_model, n_heads, d_ff = 128, 4, 512

num_layers, seq_len, batch = 3, 20, 4

encoder = TransformerEncoder(d_model, n_heads, d_ff, num_layers)

x = torch.randn(batch, seq_len, d_model)

# Padding mask: True = 忽略该位置

key_padding_mask = torch.zeros(batch, seq_len, dtype=torch.bool)

key_padding_mask[0, 15:] = True

output = encoder(x, key_padding_mask=key_padding_mask)

print(f"输入: {x.shape} → 输出: {output.shape}")
```

### 5.2 注意力可视化

可视化注意力权重是理解和调试 Transformer 模型的重要手段。通过热力图可以直观地看到模型在每个位置关注了哪些信息。

## 实例

```python
import torch

import matplotlib.pyplot as plt

import numpy as np

def visualize_attention(attention_weights, tokens=None, save_path=None):

    """

    可视化多头注意力权重

    参数:

        attention_weights: [n_heads, seq_len, seq_len]

        tokens: token 列表（可选）

        save_path: 保存路径（可选）

    """

    n_heads = attention_weights.shape[0]

    seq_len = attention_weights.shape[1]

    fig, axes = plt.subplots(1, n_heads, figsize=(n_heads * 3, 3.5))

    if n_heads == 1:

        axes = [axes]

    for head in range(n_heads):

        ax = axes[head]

        attn = attention_weights[head].detach().cpu().numpy()

        im = ax.imshow(attn, cmap='Blues', aspect='auto', vmin=0, vmax=attn.max())

        ax.set_title(f'Head {head + 1}', fontsize=10, fontweight='bold')

        ax.set_xlabel('Key')

        ax.set_ylabel('Query')

        if tokens is not None:

            ax.set_xticks(range(len(tokens)))

            ax.set_yticks(range(len(tokens)))

            ax.set_xticklabels(tokens, rotation=90, fontsize=8)

            ax.set_yticklabels(tokens, fontsize=8)

    plt.tight_layout()

    if save_path:

        plt.savefig(save_path, dpi=150, bbox_inches='tight')

    plt.show()

# 模拟训练后的注意力权重

n_heads, seq_len = 4, 8

attention_weights = torch.softmax(torch.randn(n_heads, seq_len, seq_len), dim=-1)

tokens = ['The', 'cat', 'sat', 'on', 'the', 'mat', '.', '[PAD]']

visualize_attention(attention_weights, tokens)
```

## 6. 完整的注意力分类器

### 6.1 基于注意力的文本分类

以下是一个完整的文本分类模型：使用 Transformer Encoder 提取特征，再通过注意力池化（Attention Pooling）将变长序列压缩为固定长度的向量，最后送入分类器。

## 实例

```python
import torch

import torch.nn as nn

import math

class AttentionClassifier(nn.Module):

    """基于 Transformer + 注意力池化的文本分类模型"""

    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes,

                 n_heads=4, num_layers=2, dropout=0.1):

        super().__init__()

        self.embed_dim = embed_dim

        # 词嵌入

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.pos_encoding = PositionalEncoding(embed_dim, dropout=dropout)

        # Transformer 编码器

        encoder_layer = nn.TransformerEncoderLayer(

            d_model=embed_dim,

            nhead=n_heads,

            dim_feedforward=hidden_dim,

            dropout=dropout,

            batch_first=True,

            activation='gelu'

        )

        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)

        # 注意力池化：学习每个位置的重要性权重

        self.attn_pool = nn.Sequential(

            nn.Linear(embed_dim, 1)  # 每个位置输出一个标量权重

        )

        # 分类头

        self.classifier = nn.Sequential(

            nn.Linear(embed_dim, hidden_dim),

            nn.GELU(),

            nn.Dropout(dropout),

            nn.Linear(hidden_dim, num_classes)

        )

    def forward(self, x):

        """

        x: [batch, seq_len] — token ids

        返回: logits [batch, num_classes], attn_weights [batch, seq_len]

        """

        # 词嵌入 + 位置编码

        mask = (x == 0)  # padding mask

        x = self.embedding(x) * math.sqrt(self.embed_dim)

        x = self.pos_encoding(x)

        # Transformer 编码

        x = self.transformer(x, src_key_padding_mask=mask)

        # 注意力池化：为每个位置计算权重，加权求和

        scores = self.attn_pool(x).squeeze(-1)          # [batch, seq_len]

        scores = scores.masked_fill(mask, float('-inf'))  # 忽略 padding

        attn_weights = torch.softmax(scores, dim=1)       # [batch, seq_len]

        pooled = torch.bmm(attn_weights.unsqueeze(1), x).squeeze(1)  # [batch, embed_dim]

        # 分类

        logits = self.classifier(pooled)

        return logits, attn_weights

# 测试

model = AttentionClassifier(

    vocab_size=10000, embed_dim=128, hidden_dim=256, num_classes=5

)

# 模拟输入（含 padding）

x = torch.randint(1, 10000, (16, 50))

x[:, -10:] = 0  # 最后 10 个位置是 padding

logits, attn_weights = model(x)

print(f"输入: {x.shape}")

print(f"Logits: {logits.shape}")          # [16, 5]

print(f"注意力权重: {attn_weights.shape}") # [16, 50]
```

### 6.2 常见注意力变体对比

| 类型 | Q 来源 | K/V 来源 | 核心用途 | 典型应用 |
| --- | --- | --- | --- | --- |
| 自注意力（Self-Attention） | 自身 | 自身 | 序列内部全局交互 | Transformer、BERT、ViT |
| 交叉注意力（Cross-Attention） | 目标序列 | 源序列 | 跨序列信息融合 | 机器翻译、图像描述、Stable Diffusion |
| 通道注意力（Channel Attention） | 全局池化特征 | 同上 | 学习通道重要性 | SENet、CBAM |
| 空间注意力（Spatial Attention） | 通道压缩特征 | 同上 | 学习空间位置重要性 | CBAM、Spatial Transformer |
| 稀疏注意力（Sparse Attention） | 部分位置 | 部分位置 | 降低长序列计算复杂度 | Longformer、BigBird |

## 7. 最佳实践与常见问题

### 7.1 使用技巧

- **掩码一致性**：确保 padding mask 和 causal mask 的方向一致（True = 忽略 vs 1 = 保留）。不同 API 约定可能不同。

- **头数选择**：通常设为 $$d_{model}$$ 的因数，常用 8 或 16。头太多会降低每头的维度 $$d_k$$，可能损害性能。

- **残差连接**：注意力层前后务必使用残差连接 + 层归一化，这是训练深层 Transformer 的必要条件。

- **学习率预热**：Transformer 训练初期梯度波动较大，使用 warmup + cosine decay 调度器可显著提升稳定性。

- **Flash Attention**：PyTorch 2.0+ 支持通过 `nn.functional.scaled_dot_product_attention` 自动调用 Flash Attention，显存和速度均有大幅优化。

### 7.2 常见问题

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 注意力权重全为均匀分布 | 输入未归一化或学习率过大 | 检查输入尺度，使用 LayerNorm，降低学习率 |
| 训练 loss 不下降 | 位置编码缺失或 mask 错误 | 确认位置编码已添加，检查 mask 方向 |
| 显存溢出（长序列） | 注意力矩阵 $$O(n^2)$$ 复杂度 | 使用 Flash Attention、梯度检查点或稀疏注意力 |
| 推理时注意力退化 | 训练/推理时 mask 不一致 | 确保 padding mask 在训练和推理时使用相同逻辑 |

注意力机制是现代深度学习的核心技术。从 NLP 到 CV，从语音到蛋白质结构预测，几乎所有前沿模型都以注意力为基础。理解其原理和实现，是掌握 Transformer、ViT、Stable Diffusion、GPT 等模型的关键第一步。
