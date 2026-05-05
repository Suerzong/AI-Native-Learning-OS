# PyTorch 深度学习实战 课程大纲

本课程共 42 节，按四层递进结构组织。面向嵌入式 AI 方向的北邮电子工程学生，最终目标是掌握 PyTorch 模型训练并能导出到端侧部署。

---

# 课程架构总览

```
第一层：PyTorch 基础篇（1-10节）     → 从零到能用 Tensor 做计算
第二层：模型构建与训练篇（11-22节）   → 从"会用 Tensor"到"能训练一个完整模型"
第三层：实战项目篇（23-34节）         → 从"能训练"到"能做项目"
第四层：部署准备与端侧篇（35-42节）   → 从"模型训练好"到"模型能部署到端侧"
```

---

# 第一层：PyTorch 基础篇（第 1-10 节）

目标：掌握 Tensor 的创建、运算、形状变换和自动求导，为模型构建打下基础。

| 节号 | 内容 | 核心能力 | 前置依赖 |
|------|------|---------|---------|
| 01 | PyTorch 简介与环境搭建 | 安装 PyTorch、验证 CUDA、理解 PyTorch 生态 | Python 基础 |
| 02 | Tensor 创建 | torch.tensor、zeros、ones、randn、arange、指定 dtype 和 device | 01 |
| 03 | Tensor 基本运算 | 加减乘除、矩阵乘法、逐元素运算、比较运算 | 02 |
| 04 | Broadcasting 机制 | 理解广播规则、预测运算结果 shape | 03 |
| 05 | Tensor 索引与切片 | 基本索引、高级索引、布尔索引、masked_select | 03 |
| 06 | Tensor 形状操作 | reshape/view、squeeze/unsqueeze、permute、transpose、flatten | 05 |
| 07 | Tensor 合并与分割 | cat、stack、split、chunk | 06 |
| 08 | GPU 加速 | CUDA 设备管理、.to(device)、CPU/GPU 数据迁移 | 01 |
| 09 | 自动求导基础 | requires_grad、backward、grad、计算图概念 | 03 |
| 10 | 自动求导进阶 | torch.no_grad、detach、梯度清零、高阶导数 | 09 |

## 阶段一掌握标准

给定输入 x 和权重 w，能手动实现 y = wx + b 的前向和反向传播（用 autograd），对比手动推导结果一致。每一步都能说出 tensor 的 shape。

---

# 第二层：模型构建与训练篇（第 11-22 节）

目标：掌握从定义网络到完成训练循环的全部技能。

| 节号 | 内容 | 核心能力 | 前置依赖 |
|------|------|---------|---------|
| 11 | nn.Module 基础 | 自定义 Module 子类、__init__ 和 forward、parameters() | 10 |
| 12 | 常用网络层（上） | Linear、Conv2d、BatchNorm2d 的参数和输出 shape 计算 | 11 |
| 13 | 常用网络层（下） | ReLU、Dropout、MaxPool2d、AvgPool2d、Flatten | 12 |
| 14 | 自定义网络 | 组合层构建 MLP 和 CNN、处理维度过渡 | 13 |
| 15 | 损失函数 | CrossEntropyLoss、MSELoss、BCELoss 的用法和输入要求 | 14 |
| 16 | 优化器 | SGD、Adam、学习率、momentum、zero_grad/step | 15 |
| 17 | 标准训练循环 | forward → loss → backward → step、train/eval 模式切换 | 16 |
| 18 | 完整训练循环 | 加入验证、记录指标、early stopping 概念 | 17 |
| 19 | Dataset 自定义 | 继承 Dataset、__len__ 和 __getitem__、自定义数据加载 | 18 |
| 20 | DataLoader | batch、shuffle、num_workers、collate_fn、pin_memory | 19 |
| 21 | torchvision.transforms | ToTensor、Normalize、Compose、Resize | 20 |
| 22 | 综合训练：手写数字识别 | MNIST 完整训练流程 | 21 |

## 阶段二掌握标准

独立完成 MNIST 手写数字识别项目：数据加载、CNN 模型定义、训练循环、测试集评估。准确率达到 98%+。能解释每一步的 tensor shape 变化。

---

# 第三层：实战项目篇（第 23-34 节）

目标：掌握模型评估、调参、迁移学习等工程技能。

| 节号 | 内容 | 核心能力 | 前置依赖 |
|------|------|---------|---------|
| 23 | CIFAR-10 图像分类 | 3 通道图像的 CNN 设计、训练和调参 | 22 |
| 24 | 模型评估指标 | accuracy、precision、recall、F1、混淆矩阵 | 23 |
| 25 | 过拟合与正则化 | Dropout、L2 正则化、weight_decay、早停 | 24 |
| 26 | 数据增强 | RandomCrop、RandomFlip、ColorJitter、数据增强策略 | 25 |
| 27 | 学习率调度 | StepLR、CosineAnnealingLR、ReduceLROnPlateau | 26 |
| 28 | 模型保存与加载 | state_dict、torch.save/load、checkpoint、断点续训 | 23 |
| 29 | TensorBoard 可视化 | add_scalar、add_graph、add_image、实时监控 | 28 |
| 30 | 迁移学习（上） | torchvision.models、加载预训练模型、冻结层 | 28 |
| 31 | 迁移学习（下） | fine-tune 策略、学习率分层设置 | 30 |
| 32 | GPU 多卡训练 | DataParallel 基础 | 31 |
| 33 | 调参实战 | 超参数搜索策略、实验记录方法 | 32 |
| 34 | 综合项目：自定义数据集分类 | 从零到完成一个自定义图像分类项目 | 33 |

## 阶段三掌握标准

在自定义数据集上完成图像分类项目：数据收集 → 标注 → 训练 → 评估 → 可视化。能用 TensorBoard 分析训练过程，能用迁移学习提升小数据集效果。

---

# 第四层：部署准备与端侧篇（第 35-42 节）

目标：掌握模型导出、量化、优化等部署前准备。

| 节号 | 内容 | 核心能力 | 前置依赖 |
|------|------|---------|---------|
| 35 | ONNX 导出 | torch.onnx.export、dynamic_axes、Netron 可视化 | 34 |
| 36 | ONNX Runtime 推理 | onnxruntime 加载模型、推理验证 | 35 |
| 37 | TorchScript | torch.jit.script、torch.jit.trace、区别和选择 | 35 |
| 38 | 模型量化基础 | 动态量化、静态量化、量化感知训练概念 | 37 |
| 39 | 模型剪枝 | torch.nn.utils.prune、结构化 vs 非结构化剪枝 | 38 |
| 40 | 嵌入式部署流程 | PyTorch → ONNX → NCNN/MNN/TFLite → 嵌入式设备 | 39 |
| 41 | 端侧优化技巧 | 模型大小优化、推理速度优化、内存优化 | 40 |
| 42 | 端到端项目 | 训练 → 优化 → 导出 → 部署验证完整流程 | 41 |

## 阶段四掌握标准

完成端到端项目：训练一个图像分类模型 → 导出 ONNX → 量化优化 → 在 PC 端用 ONNX Runtime 验证 → 说明在嵌入式端（如 STM32 + CMSIS-NN 或 TI + 深度学习加速器）部署的后续步骤。

---

# 推荐学习顺序（按依赖关系）

```
 1.  PyTorch 简介与环境搭建 (01)
 2.  Tensor 创建 (02)
 3.  Tensor 基本运算 (03)
 4.  Broadcasting 机制 (04)
 5.  Tensor 索引与切片 (05)
 6.  Tensor 形状操作 (06)
 7.  Tensor 合并与分割 (07)
 8.  GPU 加速 (08)
 9.  自动求导基础 (09)
10.  自动求导进阶 (10)
11.  nn.Module 基础 (11)
12.  常用网络层上 (12)
13.  常用网络层下 (13)
14.  自定义网络 (14)
15.  损失函数 (15)
16.  优化器 (16)
17.  标准训练循环 (17)
18.  完整训练循环 (18)
19.  Dataset 自定义 (19)
20.  DataLoader (20)
21.  transforms (21)
22.  MNIST 综合训练 (22)
23.  CIFAR-10 图像分类 (23)
24.  模型评估指标 (24)
25.  过拟合与正则化 (25)
26.  数据增强 (26)
27.  学习率调度 (27)
28.  模型保存与加载 (28)
29.  TensorBoard (29)
30.  迁移学习上 (30)
31.  迁移学习下 (31)
32.  GPU 多卡 (32)
33.  调参实战 (33)
34.  综合项目 (34)
35.  ONNX 导出 (35)
36.  ONNX Runtime (36)
37.  TorchScript (37)
38.  模型量化 (38)
39.  模型剪枝 (39)
40.  嵌入式部署流程 (40)
41.  端侧优化 (41)
42.  端到端项目 (42)
```
