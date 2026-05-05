# 错题与误区记录

本文件只记录会影响后续能力形成的错误，不记录一次性笔误。

## 模板

```md
## YYYY-MM-DD：错误标题

- 所属技能：
- 错误表现：
- 错误原因：
- 正确理解：
- 纠正任务：
- 是否已复测通过：
```

## 常见误区样例

### Conv2d 输出尺寸计算错误

- 所属技能：常用网络层
- 错误表现：用 `(W - K) / S + 1` 算 Conv2d 输出尺寸，忘记 padding
- 错误原因：只记住了核心公式，忽略了 padding 项
- 正确理解：完整公式是 `output = (W - K + 2P) / S + 1`，其中 W 是输入尺寸，K 是 kernel_size，P 是 padding，S 是 stride。padding=1 时两边各补 1 行/列
- 纠正任务：给定输入 (1,3,32,32)、Conv2d(3,16,3,stride=2,padding=1)，手算输出 shape
- 是否已复测通过：否

### CrossEntropyLoss 重复 Softmax

- 所属技能：损失函数
- 错误表现：模型 forward 最后加了 softmax，然后把概率传给 CrossEntropyLoss
- 错误原因：不理解 CrossEntropyLoss 内部已经包含了 log_softmax
- 正确理解：CrossEntropyLoss = log_softmax + NLLLoss，所以模型输出应该是 raw logits，不需要加 softmax。加了 softmax 会导致梯度变小、训练变慢
- 纠正任务：对比"加 softmax"和"不加 softmax"两种写法的训练 loss 曲线
- 是否已复测通过：否

### 验证时忘记 model.eval()

- 所属技能：训练循环
- 错误表现：验证/测试时直接跑 `with torch.no_grad(): output = model(x)` 但没有先 `model.eval()`
- 错误原因：以为 no_grad 就够了，不知道 Dropout 和 BatchNorm 在 eval 模式下的行为不同
- 正确理解：`torch.no_grad()` 只禁用梯度计算，不改变 Dropout（仍然随机置零）和 BatchNorm（仍然用当前 batch 统计量）。`model.eval()` 会切换这些层的行为。两者都需要
- 纠正任务：在有 Dropout 的模型上，对比 no_grad 但不 eval 和 eval + no_grad 的输出差异
- 是否已复测通过：否

### GPU Tensor 直接 .numpy() 报错

- 所属技能：GPU 加速
- 错误表现：对 GPU 上的 tensor 调用 `.numpy()` 报 RuntimeError
- 错误原因：numpy 只能处理 CPU 上的数据
- 正确理解：GPU tensor 必须先 `.cpu()` 再 `.numpy()`：`tensor.cpu().numpy()`
- 纠正任务：写出完整的 GPU → CPU → numpy 转换链
- 是否已复测通过：否

### 梯度不清零导致累加

- 所属技能：自动求导
- 错误表现：训练循环中忘记 zero_grad()，loss 曲线异常
- 错误原因：以为 backward() 会自动覆盖之前的梯度
- 正确理解：backward() 是累加梯度，不是覆盖。每次 backward 前必须 zero_grad() 或 optimizer.zero_grad()
- 纠正任务：故意不 zero_grad 跑 3 个 step，打印梯度值，观察累加效果
- 是否已复测通过：否

### DataLoader shuffle 使用混淆

- 所属技能：Dataset 与 DataLoader
- 错误表现：训练集 DataLoader 没设 shuffle=True，或验证集设了 shuffle=True
- 错误原因：不理解 shuffle 的作用和使用场景
- 正确理解：训练集必须 shuffle（防止模型学习到数据顺序），验证集不需要 shuffle（需要可复现的结果）。测试集绝对不能 shuffle
- 纠正任务：分别创建训练和验证的 DataLoader，明确指定 shuffle 参数
- 是否已复测通过：否

### eval 模式后忘记切回 train

- 所属技能：训练循环
- 错误表现：每个 epoch 的验证阶段用了 model.eval()，但下一个 epoch 训练时没有 model.train()
- 错误原因：以为 eval 是一次性操作
- 正确理解：model.eval() 会改变模型状态，必须在验证结束后 model.train() 切回训练模式
- 纠正任务：写出完整的 train → eval → train 循环模板
- 是否已复测通过：否
