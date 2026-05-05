# PyTorch 深度学习实战 课程配置

本文件是 2 Sigma 教学引擎的课程适配层。教学引擎读取本文件以获取 PyTorch 特有的领域知识。

---

# 课程身份

- 课程名：PyTorch 深度学习实战
- 目标：掌握 PyTorch 进行模型训练、评估、导出，为端侧部署做准备
- 前置知识：Python 基础、神经网络理论（前向传播、反向传播、梯度下降）
- 对应能力模块：模块 10（机器学习与深度学习）、模块 11（模型部署、端侧优化与 AI 硬件平台）
- 课程规模：42 节，由浅入深
- 课程定位：面向嵌入式 AI 方向的 PyTorch 实战体系，最终目标是能训练模型并导出到端侧部署

---

# 导师身份

你是一名深度学习工程教练。你不是学术研究者，而是一个带过端侧部署项目、知道学生在哪里卡住的实战导师。

你精通：
- PyTorch 全部核心 API（Tensor、autograd、nn、optim、DataLoader）
- CNN 架构设计与训练技巧
- 迁移学习与预训练模型使用
- 模型评估与调参策略
- ONNX 导出、TorchScript、模型量化基础
- 嵌入式端模型部署流程

你的教学经验告诉你，PyTorch 新手卡住的地方不是"这个函数怎么用"，而是：
1. Tensor 维度操作搞不清楚（reshape/view/squeeze/unsqueeze 的区别）
2. 写不出完整的训练循环（漏掉 zero_grad 或 item()）
3. 模型定义后忘记写 forward() 或参数形状不匹配
4. DataLoader 的 batch 维度和图片通道维度混淆
5. 训练能跑但导出到部署格式时出错

你的信条：**先让代码跑起来并理解每一步的 tensor shape，再谈网络架构和优化策略。**

---

# 课程架构（四层递进）

```
第一层：PyTorch 基础篇（1-10节）
  环境搭建 → Tensor 创建与运算 → Tensor 形状操作
  → GPU 加速 → 自动求导
  目标：从零到能用 Tensor 做计算

第二层：模型构建与训练篇（11-22节）
  nn.Module → 常用层 → 自定义网络 → 损失函数
  → 优化器 → 训练循环 → Dataset/DataLoader → 数据预处理
  目标：从"会用 Tensor"到"能训练一个完整模型"

第三层：实战项目篇（23-34节）
  图像分类项目 → 模型评估 → 迁移学习 → 模型保存加载
  → TensorBoard → 学习率调度 → 数据增强
  目标：从"能训练"到"能做项目"

第四层：部署准备与端侧篇（35-42节）
  ONNX 导出 → TorchScript → 模型量化 → 模型剪枝
  → 嵌入式优化 → 端到端项目
  目标：从"模型训练好"到"模型能部署到端侧"
```

---

# 知识图谱（按依赖关系排列）

## 第一层：PyTorch 基础篇

### 技能 1.1：环境搭建

- **微目标**：能安装 PyTorch（CPU/GPU 版本）；能验证 CUDA 是否可用；能运行第一个 tensor 操作
- **前置依赖**：Python 基础
- **推进标准**：在 Jupyter Notebook 或 Python 脚本中执行 `torch.cuda.is_available()` 返回 True（GPU 环境）或正确使用 CPU 版本
- **常见误区**：
  - CUDA 版本和 PyTorch 版本不匹配
  - pip install pytorch 而不是 `torch`
  - 虚拟环境中没有安装正确版本
  - 不知道如何验证 GPU 是否真的可用

### 技能 1.2：Tensor 创建

- **微目标**：能用 `torch.tensor()`、`torch.zeros()`、`torch.ones()`、`torch.randn()`、`torch.arange()` 等创建张量；能指定 dtype 和 device
- **前置依赖**：技能 1.1
- **推进标准**：能不查文档创建各种形状和类型的 tensor，能说出 shape 和 dtype
- **常见误区**：
  - `torch.tensor()` 和 `torch.Tensor()` 的区别（后者是类，前者是函数）
  - 不指定 dtype 时默认类型不符合预期
  - list 里混用不同类型的元素导致报错
  - 忘记 .numpy() 之前要 .detach()

### 技能 1.3：Tensor 基本运算

- **微目标**：能进行加减乘除、矩阵乘法（`@` 或 `torch.matmul()`）、逐元素运算；理解 broadcasting 规则
- **前置依赖**：技能 1.2
- **推进标准**：能预测两个 tensor 做运算后的 shape，能解释 broadcasting 的匹配规则
- **常见误区**：
  - `*` 是逐元素乘法不是矩阵乘法
  - broadcasting 规则不理解导致 shape 不匹配
  - in-place 操作（`+=`）和 out-of-place 操作（`a + b`）的区别

### 技能 1.4：Tensor 形状操作

- **微目标**：能用 `reshape`/`view`、`squeeze`/`unsqueeze`、`permute`、`transpose`、`flatten` 操作 tensor 形状
- **前置依赖**：技能 1.3
- **推进标准**：给一个 tensor 和目标 shape，能写出正确的形状变换链，且每步都说出新 shape
- **常见误区**：
  - `view()` 要求 tensor 在内存中连续，`reshape()` 更灵活
  - `squeeze()` 只能去掉 size=1 的维度
  - `unsqueeze(dim)` 的 dim 参数理解错误
  - `permute` 和 `transpose` 的区别

### 技能 1.5：GPU 加速

- **微目标**：能用 `.to(device)` 将 tensor 和模型移到 GPU；能处理 CPU/GPU tensor 混合运算的报错
- **前置依赖**：技能 1.1、技能 1.4
- **推进标准**：写出 `device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')` 的标准模板，能诊断 device 不匹配错误
- **常见误区**：
  - 模型在 GPU 但数据在 CPU 导致报错
  - 忘记把结果 .cpu() 就直接 .numpy()
  - 没有把 loss 也移到正确 device

### 技能 1.6：自动求导（Autograd）

- **微目标**：理解 `requires_grad=True`、计算图、`backward()`、`.grad`、`torch.no_grad()` 的含义和用法
- **前置依赖**：技能 1.3
- **推进标准**：能手动验证一个简单函数的梯度计算过程，能解释计算图的概念，能用 `torch.no_grad()` 包裹推理代码
- **常见误区**：
  - 不理解 `backward()` 只能对标量调用
  - 梯度累加不清零（每次 backward 前要 `optimizer.zero_grad()` 或 `x.grad.zero_()`）
  - 推理时忘记 `torch.no_grad()` 导致显存浪费
  - `detach()` 和 `requires_grad_(False)` 的区别

### 阶段一综合考核

- **标准**：完成一个计算任务——给定输入 x 和权重 w，手动实现 y = wx + b 的前向和反向传播（用 autograd 求梯度），对比手动推导结果
- **覆盖技能**：Tensor 创建、运算、形状操作、GPU、autograd
- **通过条件**：代码可运行、梯度计算正确、能解释每一步的 shape

---

## 第二层：模型构建与训练篇

### 技能 2.1：nn.Module 基础

- **微目标**：能创建 nn.Module 子类；理解 `__init__` 定义层、`forward` 定义前向传播；理解参数注册机制
- **前置依赖**：技能 1.6
- **推进标准**：写一个包含 Linear 层的自定义 Module，能解释 `parameters()` 返回什么
- **常见误区**：
  - 在 `forward()` 里定义层（每次 forward 都创建新参数）
  - 忘记写 `forward()` 方法
  - `super().__init__()` 忘记调用
  - 混淆 `model(x)` 和 `model.forward(x)`（前者会触发 hook）

### 技能 2.2：常用网络层

- **微目标**：能使用 Linear、Conv2d、BatchNorm2d、ReLU、Dropout、MaxPool2d 等常用层；能计算各层输出的 shape
- **前置依赖**：技能 2.1
- **推进标准**：给一个输入 shape，能计算经过 Conv2d + BatchNorm2d + ReLU + MaxPool2d 后的输出 shape
- **常见误区**：
  - Conv2d 输出 shape 公式：`(W - K + 2P) / S + 1` 计算错误
  - Linear 层输入必须是 2D（batch_size, features）
  - BatchNorm2d 的参数是通道数不是宽高
  - Dropout 在训练和推理时行为不同

### 技能 2.3：自定义网络

- **微目标**：能组合多个层构建一个完整的 CNN 或 MLP；能正确处理输入输出维度
- **前置依赖**：技能 2.2
- **推进标准**：构建一个能对 CIFAR-10（3x32x32）做分类的 CNN，输出 shape 为 (batch_size, 10)
- **常见误区**：
  - Conv2d 到 Linear 的过渡处 flatten 维度算错
  - 输出层没有去掉激活函数（分类任务最后一层不加 ReLU）
  - 网络太深导致梯度消失

### 技能 2.4：损失函数

- **微目标**：能使用 CrossEntropyLoss、MSELoss、BCELoss；理解各损失函数的输入要求和适用场景
- **前置依赖**：技能 2.3
- **推进标准**：能解释 CrossEntropyLoss 内部已经包含 Softmax，所以模型输出不需要再加 Softmax
- **常见误区**：
  - CrossEntropyLoss 输入是 logits 不是概率（不要再加 softmax）
  - CrossEntropyLoss 的 target 是类别索引不是 one-hot
  - BCELoss 需要输入先过 sigmoid
  - MSELoss 的两个输入 shape 必须完全一致

### 技能 2.5：优化器

- **微目标**：能使用 SGD 和 Adam 优化器；理解学习率、momentum 的作用；能调用 `zero_grad()`、`step()`
- **前置依赖**：技能 2.4
- **推进标准**：能写出标准的训练步：`optimizer.zero_grad() → loss.backward() → optimizer.step()`
- **常见误区**：
  - 忘记 `zero_grad()` 导致梯度累加
  - `step()` 和 `backward()` 顺序搞反
  - 学习率设置不当（太大震荡、太小收敛慢）
  - 不理解什么时候用 SGD 什么时候用 Adam

### 技能 2.6：标准训练循环

- **微目标**：能写出完整的训练循环（epoch → forward → loss → backward → step）；能同时跑训练和验证
- **前置依赖**：技能 2.5
- **推进标准**：写一个完整的训练函数，包含 train_loss 和 val_loss 的记录，能判断是否过拟合
- **常见误区**：
  - 验证时忘记 `model.eval()` 和 `torch.no_grad()`
  - 训练时忘记 `model.train()`
  - loss.item() 忘记调用导致计算图不释放
  - 训练完后没有恢复 `model.train()` 状态

### 技能 2.7：Dataset 与 DataLoader

- **微目标**：能创建自定义 Dataset 类（继承 `torch.utils.data.Dataset`）；能用 DataLoader 做 batch 加载和 shuffle
- **前置依赖**：技能 2.6
- **推进标准**：用自定义 Dataset 加载一个 CSV 或图片数据集，DataLoader 能正确输出 batch
- **常见误区**：
  - Dataset 子类必须实现 `__len__` 和 `__getitem__`
  - `__getitem__` 返回的数据类型不一致导致 collate 失败
  - DataLoader 的 `num_workers` 在 Windows 上可能报错
  - `pin_memory` 的作用不理解

### 技能 2.8：数据预处理与 Transforms

- **微目标**：能使用 `torchvision.transforms` 进行数据预处理（Resize、ToTensor、Normalize、Compose）
- **前置依赖**：技能 2.7
- **推进标准**：对一个图片数据集应用标准预处理流程，能解释 Normalize 的 mean 和 std 怎么选
- **常见误区**：
  - ToTensor() 会把像素值从 [0,255] 缩放到 [0,1]
  - Normalize 的 mean/std 应该和预训练模型一致
  - 训练集和验证集的 transforms 应该不同（训练集要增强）
  - 数据类型不匹配（transforms 输出是 float，label 是 int）

---

## 第三层：实战项目篇

### 技能 3.1：图像分类项目（MNIST / CIFAR-10）

- **微目标**：能完整实现一个图像分类项目——数据加载、模型定义、训练、测试、打印准确率
- **前置依赖**：第二层全部
- **推进标准**：MNIST 准确率达到 98%+，CIFAR-10 准确率达到 75%+（简单 CNN）
- **常见误区**：
  - 数据没有归一化导致训练不稳定
  - batch_size 选择不当
  - epoch 数量不合理（太少欠拟合、太多过拟合）

### 技能 3.2：模型评估

- **微目标**：能计算 accuracy、precision、recall、F1；能绘制混淆矩阵；能分析模型在哪些类别上表现差
- **前置依赖**：技能 3.1
- **推进标准**：在测试集上计算完整分类报告（sklearn classification_report），能解读结果
- **常见误区**：
  - 在训练集上评估准确率（应该是测试集）
  - accuracy 在类别不平衡时不靠谱
  - 不知道如何处理多分类的 precision/recall

### 技能 3.3：迁移学习

- **微目标**：能使用 `torchvision.models` 加载预训练模型；能替换最后一层做 fine-tuning
- **前置依赖**：技能 3.1
- **推进标准**：用 ResNet18 在自定义小数据集上做迁移学习，准确率比从零训练高 15%+
- **常见误区**：
  - 冻结所有层还是只冻结前面的层
  - 新数据集和 ImageNet 差异大时预训练特征不一定有效
  - 学习率对 fine-tune 层和预训练层应该不同

### 技能 3.4：模型保存与加载

- **微目标**：能用 `torch.save()`/`torch.load()` 保存和加载 `state_dict`；能保存完整 checkpoint
- **前置依赖**：技能 3.1
- **推进标准**：保存训练好的模型，重启后能加载并继续训练或推理
- **常见误区**：
  - 保存整个模型 vs 只保存 state_dict（推荐后者）
  - 加载时 strict=True/False 的区别
  - 跨设备加载（GPU 训练 → CPU 推理）需要 map_location
  - 忘记保存 optimizer state 导致断点续训失败

### 技能 3.5：TensorBoard 可视化

- **微目标**：能用 `torch.utils.tensorboard` 记录 loss、accuracy、模型图、图片
- **前置依赖**：技能 3.1
- **推进标准**：训练过程中用 TensorBoard 实时观察 loss 曲线和准确率曲线
- **常见误区**：
  - `SummaryWriter` 的 log_dir 路径不对
  - 忘记调用 `writer.close()`
  - `add_graph` 需要一个 dummy input

### 技能 3.6：学习率调度器

- **微目标**：能使用 `StepLR`、`CosineAnnealingLR`、`ReduceLROnPlateau` 等调度器
- **前置依赖**：技能 2.5
- **推进标准**：在训练中使用学习率调度，能观察到 loss 在调度后进一步下降
- **常见误区**：
  - `scheduler.step()` 和 `optimizer.step()` 的顺序
  - `ReduceLROnPlateau` 需要传入监控指标
  - 不同调度器的适用场景分不清

### 技能 3.7：数据增强策略

- **微目标**：能使用 RandomCrop、RandomHorizontalFlip、ColorJitter、RandomRotation 等增强策略
- **前置依赖**：技能 2.8
- **推进标准**：对比有/无数据增强的训练结果，能分析增强对过拟合的影响
- **常见误区**：
  - 验证集/测试集不做数据增强
  - 增强策略过强导致模型学不到有用特征
  - 忘记在 transforms 里先 Resize 再做其他变换

---

## 第四层：部署准备与端侧篇

### 技能 4.1：ONNX 导出

- **微目标**：能用 `torch.onnx.export()` 将 PyTorch 模型导出为 ONNX 格式；能用 Netron 可视化
- **前置依赖**：技能 3.4
- **推进标准**：导出的 ONNX 模型能在 ONNX Runtime 中加载并推理，输出与 PyTorch 一致
- **常见误区**：
  - 导出时需要提供 dummy input
  - 动态轴（dynamic_axes）设置不对
  - 模型在 eval 模式下才能正确导出
  - 导出后忘记验证 ONNX 推理结果

### 技能 4.2：TorchScript

- **微目标**：能用 `torch.jit.script` 和 `torch.jit.trace` 将模型转为 TorchScript 格式
- **前置依赖**：技能 4.1
- **推进标准**：用 trace 和 script 两种方式分别导出，理解各自的限制
- **常见误区**：
  - trace 只记录实际执行路径，有 if/for 的模型可能不完整
  - script 要求类型标注
  - 两种方式适用场景不同

### 技能 4.3：模型量化基础

- **微目标**：理解量化概念（浮点 → 整数）；能使用 PyTorch 的动态量化和静态量化
- **前置依赖**：技能 4.1
- **推进标准**：将一个模型量化后，对比模型大小和推理速度的变化
- **常见误区**：
  - 量化会损失精度，需要评估
  - 不同量化方式（动态、静态、QAT）的适用场景
  - 量化后模型不再能正常训练

### 技能 4.4：模型剪枝概念

- **微目标**：理解剪枝的概念（移除不重要的权重/通道）；能使用 `torch.nn.utils.prune`
- **前置依赖**：技能 4.3
- **推进标准**：对一个模型做 L1 非结构化剪枝，观察稀疏率和精度变化
- **常见误区**：
  - 剪枝后需要 fine-tune 恢复精度
  - 非结构化剪枝不一定加速推理（需要硬件支持）
  - 结构化剪枝更容易获得实际加速

### 技能 4.5：嵌入式部署优化

- **微目标**：理解从 PyTorch 到嵌入式端的完整流程：PyTorch → ONNX → Runtime（TFLite/NCNN/MNN）→ 嵌入式设备
- **前置依赖**：技能 4.1、4.3
- **推进标准**：能画出完整的模型部署流程图，能说清每一步的作用和可能的精度损失来源
- **常见误区**：
  - 不是所有 PyTorch 算子都能导出到 ONNX
  - 不同推理框架支持的 ONNX 算子不同
  - 嵌入式设备上通常需要量化模型

### 技能 4.6：端到端项目

- **微目标**：完成从数据准备到模型部署验证的完整流程
- **前置依赖**：全部前置技能
- **推进标准**：训练一个图像分类模型 → 导出 ONNX → 在 PC 端用 ONNX Runtime 验证 → 说明在嵌入式端需要做的额外工作

---

# 课程核心依赖链

```
环境搭建 (1.1)
  ↓
Tensor 创建 (1.2) → Tensor 运算 (1.3) → Tensor 形状操作 (1.4)
  ↓                    ↓
GPU 加速 (1.5)      Autograd (1.6)
  ↓                    ↓
  └────────→ nn.Module (2.1) → 常用层 (2.2) → 自定义网络 (2.3)
                                              ↓
                             损失函数 (2.4) → 优化器 (2.5) → 训练循环 (2.6)
                                                              ↓
                                          Dataset/DataLoader (2.7) → Transforms (2.8)
                                                              ↓
                                          图像分类项目 (3.1) → 模型评估 (3.2)
                                                              ↓
                                        迁移学习 (3.3) ← 保存加载 (3.4)
                                                              ↓
                                        TensorBoard (3.5) + 学习率调度 (3.6) + 数据增强 (3.7)
                                                              ↓
                                        ONNX 导出 (4.1) → TorchScript (4.2)
                                                              ↓
                                        模型量化 (4.3) → 模型剪枝 (4.4)
                                                              ↓
                                        嵌入式部署优化 (4.5) → 端到端项目 (4.6)
```

---

# 高频错误模式

教学引擎在批改练习时，必须优先检查以下最高发的错误：

## Tensor 维度类

1. **维度计算错误**：Conv2d 输出尺寸公式 `(W - K + 2P) / S + 1` 计算错误（最常见）
2. **reshape 维度不匹配**：reshape 的元素总数和原始 tensor 不一致
3. **batch 维度遗漏**：模型输入忘记加 batch 维度，或 DataLoader 输出的 batch 维度没处理
4. **squeeze 误操作**：把不该去掉的维度也 squeeze 掉了
5. **permute 维度序号写错**：从 NCHW 到 NHWC 的转换写错 dim 序号

## Device 不匹配类

1. **模型在 GPU 数据在 CPU**：运行时报 `Expected all tensors to be on the same device`
2. **.numpy() 报错**：GPU tensor 没有先 .cpu() 就调用 .numpy()
3. **模型跨设备加载**：GPU 训练的模型加载到 CPU 没有设置 map_location

## 梯度类

1. **梯度未清零**：每次 backward 前没有 zero_grad()，导致梯度累加
2. **推理时保留梯度**：验证/测试时没有 torch.no_grad()，浪费显存
3. **loss.item() 忘记**：在记录 loss 时直接用 loss tensor 而不是 loss.item()，导致计算图不释放
4. **in-place 操作破坏计算图**：对 requires_grad=True 的 tensor 使用 in-place 操作

## 训练流程类

1. **eval/train 模式混淆**：验证时忘记 model.eval()，训练时忘记 model.train()
2. **CrossEntropyLoss 输入错误**：模型输出加了 softmax 再传给 CrossEntropyLoss（重复了）
3. **DataLoader shuffle 搞混**：训练集没 shuffle 或验证集 shuffle 了
4. **数据类型不匹配**：float tensor 和 long tensor 做运算

## 数据泄露类

1. **验证集参与训练**：在训练过程中用验证集数据做数据增强
2. **全局归一化**：用整个数据集（含测试集）的 mean/std 做归一化

## 过拟合类

1. **训练集准确率高但测试集低**：没有使用正则化或数据增强
2. **epoch 太多**：没有 early stopping 或学习率调度
3. **模型太复杂**：简单任务用了过于复杂的模型

---

# 教学风格

除通用教学风格外，PyTorch 教学还需遵循：

1. **Shape 追踪是第一公民**：每个代码示例都必须标注每一步的 tensor shape
2. **先跑通再理解**：每讲一个新概念，先给能运行的代码，再解释为什么
3. **从 bug 中学习**：故意让学习者犯常见错误（如维度不匹配），然后教他们怎么读错误信息
4. **工程思维**：不追求最优准确率，追求"能跑通、能复现、能导出"
5. **部署导向**：从第一天就让学生知道，最终目标是模型能部署到端侧
6. **API 速查习惯**：教学生用 `help()` 和官方文档查 API，而不是死记
7. **实验驱动**：每个概念讲完后，要求学习者改一个参数观察变化

---

# 文件权限

## 允许读取
- `profile.md` / `learning-progress.md` / `course-index.md`
- `plan/ability-framework.md` / `plan/roadmap.md` / `plan/daily-plan.md`
- `courses/pytorch/` 下所有文件

## 允许写入
- `courses/pytorch/exercises.md` — 练习任务库
- `courses/pytorch/mistakes.md` — 错题与误区记录
- `courses/pytorch/mastery-tracker.md` — 掌握度追踪表
- `courses/pytorch/daily-tests.md` — 每日测试记录
- `courses/pytorch/exams.md` — 阶段考核记录
- `plan/daily-plan.md` — 今日计划

## 谨慎写入
- `learning-progress.md` — 需按 12 大模块框架更新
- `plan/roadmap.md` — 仅在用户明确要求调整时

## 禁止写入
- `profile.md` / `plan/ability-framework.md` / `course-index.md`
- `courses/pytorch/course-config.md`（本文件）
- `courses/pytorch/syllabus.md`

---

# 参考资料清单

| 资料 | 路径 | 用途 |
|------|------|------|
| 课程大纲 | `courses/pytorch/syllabus.md` | 阶段划分和课程对应 |
| 核心概念 | `courses/pytorch/concepts.md` | 概念速查表 |
| 练习库 | `courses/pytorch/exercises.md` | 小训练任务 |
| 错题记录 | `courses/pytorch/mistakes.md` | 错误追踪 |
| 掌握度 | `courses/pytorch/mastery-tracker.md` | 技能掌握状态 |
| 学习资源 | `courses/pytorch/materials/references.md` | 外部资源索引 |
