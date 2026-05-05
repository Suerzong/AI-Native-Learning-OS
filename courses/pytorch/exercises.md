# 训练任务库

训练任务用于 10-30 分钟内完成一个明确技能点。

## 任务模板

```md
## 任务名称

- 目标技能：
- 前置知识：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 反馈重点：
```

---

## Tensor-01：创建指定形状的 Tensor

- 目标技能：使用 torch API 创建各种 tensor
- 前置知识：无
- 任务要求：不查文档，写出以下代码：
  1. 创建一个 3x4 的全零 float32 tensor
  2. 创建一个 2x3x4 的标准正态分布随机 tensor
  3. 创建一个从 0 到 9（不含 10）的一维 int64 tensor
  4. 创建一个和已知 tensor `x` 形状相同但全为 1 的 tensor
  5. 创建一个 5x5 的单位矩阵
- 限制条件：必须指定正确的 dtype 和 shape
- 成功标准：5 个 tensor 全部创建成功，shape 和 dtype 正确
- 常见错误：
  - `torch.zeros()` 忘记指定 dtype
  - `torch.randn()` 参数是 shape 而不是单个数字
  - `torch.eye()` 和 `torch.ones()` 混淆
  - `torch.tensor([0,1,2])` 默认是 int64 不是 float32
- 反馈重点：每个 API 的参数含义和默认行为

## Tensor-02：Tensor 运算与 Shape 预测

- 目标技能：预测 tensor 运算后的 shape
- 前置知识：Tensor 创建、基本运算、broadcasting
- 任务要求：不运行代码，预测以下运算的输出 shape：
  1. `(3,4) + (4,)` → ?
  2. `(2,3,4) * (1,4)` → ?
  3. `(5,1,3) + (3,1)` → ?
  4. `torch.matmul((2,3,4), (2,4,5))` → ?
  5. `(2,3) @ (4,3).T` → ?
- 限制条件：必须写出 broadcasting 的匹配过程
- 成功标准：5 个 shape 全部预测正确
- 常见错误：
  - broadcasting 从右向左匹配搞错
  - matmul 和 * 的区别不理解
  - 不理解 `.T` 会交换最后两个维度
- 反馈重点：broadcasting 规则的可视化解释

## Tensor-03：reshape 练习

- 目标技能：使用 reshape/view 改变 tensor 形状
- 前置知识：Tensor shape 操作
- 任务要求：给定 `x = torch.randn(2, 3, 4)`，写出代码完成：
  1. 将 x 变形为 (6, 4)
  2. 将 x 变形为 (2, 12)
  3. 在第 1 维（从 0 开始计数）增加一个维度，变成 (2, 1, 3, 4)
  4. 去掉所有 size=1 的维度（如果有）
  5. 将 x 转置为 (4, 3, 2)
- 限制条件：第 3 题只能用 unsqueeze，第 5 题只能用 permute
- 成功标准：5 个操作后的 shape 完全正确
- 常见错误：
  - unsqueeze 的 dim 参数从 0 开始计数
  - permute 的参数是维度索引的排列
  - reshape 的总元素数必须和原始一致
- 反馈重点：每步操作后的 shape 标注

## Autograd-01：手动验证梯度

- 目标技能：理解 requires_grad 和 backward 的机制
- 前置知识：自动求导基础
- 任务要求：
  1. 创建 `x = torch.tensor([2.0], requires_grad=True)`
  2. 计算 `y = x ** 2 + 3 * x + 1`
  3. 调用 `y.backward()`
  4. 打印 `x.grad` 的值
  5. 手动推导 dy/dx 的值，和代码结果对比
- 限制条件：不能直接运行代码——必须先手动计算，再用代码验证
- 成功标准：手动推导 dy/dx = 2x + 3 = 7，代码结果也是 7
- 常见错误：
  - 忘记 requires_grad=True
  - backward() 对非标量报错
  - 手动推导时忘记链式法则
- 反馈重点：计算图的概念——每个运算如何连接成图

## Autograd-02：梯度清零的必要性

- 目标技能：理解梯度累加和 zero_grad 的作用
- 前置知识：自动求导
- 任务要求：
  1. 创建 `w = torch.tensor([1.0], requires_grad=True)`
  2. 连续做 3 次 `loss = w * 2; loss.backward()`（不 zero_grad）
  3. 打印 `w.grad`，观察值是多少
  4. 解释为什么是这个值
  5. 在第 2、3 次 backward 前加入 `w.grad.zero_()`，再次观察
- 限制条件：必须先预测结果再运行
- 成功标准：不 zero_grad 时梯度累加到 6.0，zero_grad 后每次是 2.0
- 常见错误：
  - 不理解梯度是累加的不是覆盖的
  - `zero_grad()` 和 `grad.zero_()` 的区别不理解
- 反馈重点：为什么训练循环里每次 backward 前要 zero_grad

## Module-01：自定义 Linear 层

- 目标技能：创建 nn.Module 子类
- 前置知识：nn.Module 基础
- 任务要求：
  1. 创建一个名为 `MyLinear` 的类，继承 `nn.Module`
  2. 在 `__init__` 中定义一个 `nn.Linear(10, 5)` 层
  3. 在 `forward` 中返回该层的输出
  4. 实例化并传入一个 (2, 10) 的随机 tensor，验证输出 shape 为 (2, 5)
- 限制条件：不能使用 nn.Sequential
- 成功标准：自定义 Module 能正确运行，输出 shape 正确
- 常见错误：
  - 忘记调用 `super().__init__()`
  - 在 forward 中用 `model.forward(x)` 而不是 `model(x)`
  - 不理解 `self.linear = nn.Linear(...)` 会自动注册参数
- 反馈重点：参数注册机制——__init__ 中赋值的 nn.Module 会自动注册参数

## Training-01：完整训练循环骨架

- 目标技能：写出标准训练循环
- 前置知识：损失函数、优化器
- 任务要求：不参考任何代码，写出以下训练循环骨架：
  1. 5 个 epoch 的训练循环
  2. 每个 epoch 中：zero_grad → forward → loss → backward → step
  3. 打印每个 epoch 的 loss
- 限制条件：模型和数据可以用随机数据代替，但训练循环结构必须完整
- 成功标准：循环能运行，loss 在下降（即使是随机数据也至少能看到 loss 变化）
- 常见错误：
  - 顺序错误：先 step 再 backward
  - 忘记 zero_grad
  - 忘记 loss.item() 直接打印 tensor
- 反馈重点：训练循环的 5 步必须形成肌肉记忆

## Training-02：train/eval 模式切换

- 目标技能：理解 model.train() 和 model.eval() 的区别
- 前置知识：训练循环、Dropout、BatchNorm
- 任务要求：
  1. 创建一个包含 Dropout(0.5) 的模型
  2. 在 model.train() 模式下，同一个输入跑 3 次，记录输出
  3. 在 model.eval() 模式下，同一个输入跑 3 次，记录输出
  4. 解释为什么 train 模式下输出不同，eval 模式下输出相同
- 限制条件：必须用 torch.no_grad() 包裹 eval 部分
- 成功标准：train 模式输出 3 次不同，eval 模式输出 3 次相同
- 常见错误：
  - eval 时忘记 torch.no_grad()（不影响本题结果但浪费显存）
  - 混淆 Dropout 的训练/推理行为
- 反馈重点：哪些层受 train/eval 影响（Dropout、BatchNorm）

## CNN-01：Conv2d 输出尺寸计算

- 目标技能：计算卷积层输出 shape
- 前置知识：Conv2d 的参数含义
- 任务要求：不运行代码，计算以下 Conv2d 的输出 shape：
  1. 输入 (1,3,32,32)，Conv2d(3, 16, kernel_size=3, padding=1) → ?
  2. 输入 (1,16,32,32)，Conv2d(16, 32, kernel_size=3, stride=2, padding=1) → ?
  3. 输入 (1,32,16,16)，Conv2d(32, 64, kernel_size=5, stride=2, padding=0) → ?
  4. 在第 3 题的基础上再加 MaxPool2d(kernel_size=2) → ?
- 限制条件：必须写出计算公式 `(W - K + 2P) / S + 1`
- 成功标准：4 个 shape 全部正确
- 常见错误：
  - 公式记错
  - 忘记 stride 不为 1 时需要除以 S
  - MaxPool2d 用同样的公式计算
- 反馈重点：Conv2d 输出公式和 MaxPool2d 输出公式的推导
