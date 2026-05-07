# PyTorch Recipes 索引

> 来源：https://docs.pytorch.org/tutorials/recipes/recipes_index.html

## 什么是 PyTorch Recipes？

PyTorch Recipes 是关于如何使用特定 PyTorch 功能的小而实用的示例。

## Recipe 分类

### 基础
- 定义神经网络
- PyTorch 中的 `state_dict` 是什么
- 保存和加载模型进行推理
- 保存和加载通用检查点（Checkpoint）
- 在一个文件中保存和加载多个模型
- 使用来自不同模型的参数热启动模型
- 使用 ONNX 进行跨平台部署

### 生产与优化
- PyTorch 性能分析（Profiling）
- 使用 Tune 进行超参数调优
- 剪枝教程
- LSTM 词语言模型的动态量化
- BERT 的动态量化
- 计算机视觉的量化迁移学习
- PyTorch 中使用 Eager 模式的静态量化
- （Beta）使用 SCAFFOLD 实现高性能 Transformers
- （Beta）使用 FX 构建简单的 CPU 性能分析器

### 数据
- 数据集加载教程
- 使用 DataParallel 进行并行训练
- （Beta）使用 FX 构建简单的 CUDA 性能分析器
- 前向/后向钩子（Hook）

### 分布式训练
- 分布式数据并行入门
- 分布式 RPC 框架入门
- 使用异步执行实现批处理 RPC
- 将 DistributedDataParallel 与分布式 RPC 框架结合使用

### 其他
- TorchScript 和 Autograd
- 使用 TensorBoard 和 PyTorch
- 使用 TensorBoard 可视化模型、数据和训练
- 面向 Former Torch 用户的 PyTorch
- 使用 PyTorch 编写分布式应用
- 使用 Grad-CAM 定位 TorchVision 模型
- 免费融合 Conv+BN
