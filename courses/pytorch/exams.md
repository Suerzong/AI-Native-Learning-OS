# 阶段考核

阶段考核用于判断是否形成稳定能力，而不是检查是否背过答案。

## 考核模板

```md
## 阶段名称

- 覆盖技能：
- 考核时间：
- 允许资料：
- 任务：
- 评分标准：
- 晋级条件：
```

---

## 第一层考核：Tensor 与自动求导

- 覆盖技能：Tensor 创建、运算、形状操作、broadcasting、autograd
- 考核时间：45 分钟
- 允许资料：PyTorch 官方文档、自己的笔记
- 任务：
  1. 给定一个线性模型 y = wx + b，手动实现前向传播和反向传播（用 autograd），对比手动推导的梯度结果
  2. 给定复杂的 tensor 形状变换链，预测每一步的 shape
  3. 解释 broadcasting 在两个不等 shape tensor 相加时的工作过程
  4. 写出一个使用 `torch.no_grad()` 的推理代码片段，并解释为什么推理时不需要梯度
- 评分标准：
  - 代码能运行且梯度正确（40%）
  - Shape 预测全部正确（30%）
  - 能解释 broadcasting 规则（15%）
  - 能解释 no_grad 的作用（15%）
- 晋级条件：
  - 正确率不低于 80%
  - 每一步都能说出 tensor shape
  - 能解释计算图的概念

---

## 第二层考核：模型构建与训练

- 覆盖技能：nn.Module、常用层、损失函数、优化器、训练循环、Dataset/DataLoader
- 考核时间：90 分钟
- 允许资料：PyTorch 官方文档、自己的笔记
- 任务：
  1. 从零定义一个 CNN 模型（包含 Conv2d、BatchNorm2d、ReLU、MaxPool2d、Linear），用于 MNIST 分类
  2. 写出完整的训练循环（含 train/eval 切换、zero_grad、loss 记录）
  3. 创建自定义 Dataset 和 DataLoader
  4. 训练 5 个 epoch，报告训练 loss 和测试准确率
  5. 解释 CrossEntropyLoss 为什么不需要在模型输出处加 softmax
- 评分标准：
  - 模型定义正确且能运行（30%）
  - 训练循环完整无遗漏（30%）
  - DataLoader 正确创建（15%）
  - MNIST 准确率达到 95%+（15%）
  - 能解释 softmax 问题（10%）
- 晋级条件：
  - 准确率不低于 95%
  - 训练循环中无遗漏步骤
  - 能正确切换 train/eval 模式
  - 没有未纠正的关键误区

---

## 第三层考核：实战项目

- 覆盖技能：CIFAR-10 分类、模型评估、迁移学习、保存加载、数据增强、学习率调度
- 考核时间：120 分钟（可分 2 次完成）
- 允许资料：PyTorch 官方文档、torchvision 文档
- 任务：
  1. 在 CIFAR-10 上训练一个 CNN，达到 75%+ 准确率
  2. 使用 torchvision.models 加载预训练 ResNet18，替换最后一层做 fine-tune，达到 85%+
  3. 计算测试集的 classification_report（precision、recall、F1）
  4. 使用 TensorBoard 记录训练过程
  5. 保存最优模型的 state_dict，并加载验证
  6. 使用数据增强和学习率调度提升准确率
- 评分标准：
  - CNN 准确率 75%+（20%）
  - 迁移学习准确率 85%+（20%）
  - 分类报告正确生成（15%）
  - TensorBoard 有完整曲线（10%）
  - 模型保存加载正确（15%）
  - 数据增强和 LR 调度有合理使用（20%）
- 晋级条件：
  - 迁移学习准确率不低于 85%
  - 能解释过拟合现象并说明应对策略
  - 能独立完成完整项目

---

## 第四层考核：部署准备

- 覆盖技能：ONNX 导出、TorchScript、量化、部署流程
- 考核时间：90 分钟
- 允许资料：PyTorch 官方文档、ONNX 文档
- 任务：
  1. 将第三层训练的模型导出为 ONNX 格式（设置正确的 dynamic_axes）
  2. 用 ONNX Runtime 加载并推理，对比 PyTorch 和 ONNX 的输出差异
  3. 用 torch.jit.trace 导出 TorchScript 模型
  4. 对模型做动态量化，对比模型大小和精度变化
  5. 画出从 PyTorch 到嵌入式端的完整部署流程图
- 评分标准：
  - ONNX 导出成功且推理结果一致（30%）
  - TorchScript 导出成功（20%）
  - 量化后模型大小和精度变化正确分析（20%）
  - 部署流程图完整准确（20%）
  - 能解释各步骤的精度损失来源（10%）
- 晋级条件：
  - ONNX 推理输出与 PyTorch 差异在 1e-5 内
  - 能说清 ONNX → Runtime → 嵌入式的完整流程
  - 理解量化对精度的影响
