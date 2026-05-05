# 学习者状态

## 基本信息

- 姓名：宋恩泽（Ethen）
- 学校：北京邮电大学，电子工程学院
- 长期方向：Edge AI / 嵌入式 AI
- 编程经验：Python、C/C++、嵌入式开发
- 深度学习经验：了解神经网络理论，可能已学过 PyTorch 基础

## 学习风格

- 偏好动手实践，先跑通代码再理解原理
- 有嵌入式背景，对硬件和底层有直觉
- 最终目标导向——所有学习都服务于模型部署到嵌入式端
- 已有 PyTorch 经验，对 TensorFlow 的学习可以通过对比加深理解

## 已有基础

| 领域 | 水平 | 备注 |
|------|------|------|
| Python | 中等 | 能独立写脚本 |
| 神经网络理论 | 入门+ | 了解前向/反向传播、损失函数、优化器 |
| numpy | 入门+ | 基本数组操作 |
| 线性代数 | 入门 | 矩阵乘法、转置 |
| 微积分 | 入门 | 链式法则、偏导数 |
| PyTorch | 入门 | 可能已有基础（视学习进度） |
| TensorFlow | 零基础 | 尚未系统使用 |
| CNN 架构 | 理论了解 | 知道卷积、池化的概念 |
| 模型部署 | 入门 | 了解 ONNX/TF Lite 概念 |

## 当前阶段

- 阶段：阶段 0：诊断与准备
- 当前技能：TF-L101（TensorFlow 概述与生态）
- 当前等级：0

## 核心弱点

### TensorFlow API 不熟悉

- 症状：不知道 TF 的 API 命名和 PyTorch 的区别
- 根本原因：缺乏 TensorFlow 使用经验
- 纠正策略：建立 TF-PyTorch 对照表，逐步迁移已有知识

### Keras API 选择困难

- 症状：不清楚什么时候用 Sequential，什么时候用 Functional API
- 根本原因：不了解两种 API 的适用场景和限制
- 纠正策略：先掌握 Sequential（简单场景），再学 Functional API（复杂场景）

### tf.data Pipeline 概念弱

- 症状：不知道各操作（map/batch/shuffle/prefetch）的顺序和原因
- 根本原因：没有数据工程的直觉
- 纠正策略：从简单 pipeline 开始，逐步理解每个操作的作用

### GradientTape 使用不熟

- 症状：不知道什么时候需要手写训练循环 vs 用 fit()
- 根本原因：对 TF 的自动微分机制不熟悉
- 纠正策略：先用 fit() 完成所有训练，再学 GradientTape 做自定义训练

### TF Lite 转换流程不清

- 症状：不知道从训练到端侧部署的完整步骤
- 根本原因：缺乏端到端部署经验
- 纠正策略：跟随教程完成一次完整的 训练→保存→转换→推理 流程

## 下一步最佳任务

1. 安装 TensorFlow（`pip install tensorflow`）
2. 运行 `import tensorflow as tf; print(tf.__version__)` 验证安装
3. 创建第一个 tensor：`x = tf.constant([1, 2, 3])`
4. 了解 TensorFlow 和 PyTorch 的主要 API 对照关系
