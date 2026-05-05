# 学习者状态

## 基本信息

- 姓名：宋恩泽（Ethen）
- 学校：北京邮电大学，电子工程学院
- 长期方向：Edge AI / 嵌入式 AI
- 编程经验：Python、C/C++、嵌入式开发
- 深度学习经验：了解神经网络理论，未系统使用 PyTorch

## 学习风格

- 偏好动手实践，先跑通代码再理解原理
- 有嵌入式背景，对硬件和底层有直觉
- 最终目标导向——所有学习都服务于模型部署到嵌入式端

## 已有基础

| 领域 | 水平 | 备注 |
|------|------|------|
| Python | 中等 | 能独立写脚本 |
| 神经网络理论 | 入门 | 了解前向/反向传播 |
| numpy | 入门 | 基本数组操作 |
| 线性代数 | 入门 | 矩阵乘法、转置 |
| 微积分 | 入门 | 链式法则、偏导数 |
| PyTorch | 零基础 | 尚未使用 |
| CNN 架构 | 理论了解 | 知道卷积、池化的概念 |
| 模型部署 | 零基础 | 尚未接触 |

## 当前阶段

- 阶段：阶段 0：诊断与准备
- 当前技能：环境搭建
- 当前等级：0

## 核心弱点

### Tensor Shape 推理能力弱

- 症状：不能预测 reshape、Conv2d、broadcasting 后的 shape
- 根本原因：对 tensor 的维度含义不直观
- 纠正策略：每步操作后都标注 shape，用"形状追踪"习惯化

### 训练循环步骤遗漏

- 症状：漏掉 zero_grad、漏掉 model.eval()、漏掉 loss.item()
- 根本原因：没有形成标准模板
- 纠正策略：用"训练五步法"口诀：零 → 前 → 失 → 反 → 步

### Device 不匹配错误

- 症状：模型在 GPU、数据在 CPU，报 RuntimeError
- 根本原因：没有建立 device 管理意识
- 纠正策略：从第一天就用 `device = torch.device(...)` 模板

### CrossEntropyLoss 输入格式错误

- 症状：模型输出加了 softmax 再传给 CrossEntropyLoss
- 根本原因：不理解 CrossEntropyLoss 内部已包含 log_softmax
- 纠正策略：每次用 CrossEntropyLoss 时都问"模型输出是什么"

### train/eval 模式混淆

- 症状：验证时忘记 model.eval()，训练时忘记 model.train()
- 根本原因：不理解哪些层受模式影响
- 纠正策略：列出受模式影响的层（Dropout、BatchNorm），建立切换习惯

## 下一步最佳任务

1. 安装 PyTorch（CPU 版本即可开始）
2. 运行 `import torch; print(torch.__version__)` 验证安装
3. 创建第一个 tensor：`x = torch.tensor([1, 2, 3])`
4. 验证 CUDA 是否可用（如有 GPU）
