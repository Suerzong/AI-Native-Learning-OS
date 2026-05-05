# 每日诊断短测

每日短测用于判断今天应该训练什么，而不是为了打分。

## 模板

```md
## YYYY-MM-DD

### 诊断题

1. 概念题：
2. API 题：
3. Shape 预测题：
4. 调试题：

### 结果

- 正确率：
- 主要错误：
- 今日训练目标：
- 是否允许推进：
```

## Tensor 基础诊断样例

1. `torch.tensor([1, 2, 3])` 和 `torch.Tensor([1, 2, 3])` 有什么区别？
2. 写出创建一个 (3, 4) 的 float32 全零 tensor 的代码。
3. 给定 `x = torch.randn(2, 3, 4)`，`x.reshape(6, -1)` 的输出 shape 是什么？
4. 如果运行 `a = torch.randn(3, 4).cuda(); b = torch.randn(3, 4); a + b` 会报什么错？

## Autograd 诊断样例

1. `requires_grad=True` 的作用是什么？
2. 写出标准的训练一步的代码顺序（zero_grad → ? → ? → ?）。
3. 如果连续 3 次 backward() 而不 zero_grad()，梯度会怎样？
4. `torch.no_grad()` 的作用是什么？推理时为什么要用它？

## nn.Module 诊断样例

1. nn.Module 子类必须实现哪两个部分？
2. `model.parameters()` 返回什么？
3. `model.train()` 和 `model.eval()` 的区别是什么？分别影响哪些层？
4. 计算 Conv2d(3, 16, 3, padding=1) 对 (1, 3, 32, 32) 输入的输出 shape。

## 训练循环诊断样例

1. 写出 forward → loss → backward → step 的完整 4 行代码。
2. CrossEntropyLoss 的输入应该是 logits 还是概率？为什么？
3. 验证时需要哪两个上下文管理器？
4. `loss.item()` 的作用是什么？为什么不直接用 `loss` 记录？

## DataLoader 诊断样例

1. Dataset 子类必须实现哪两个方法？
2. 训练集的 DataLoader 应该设 `shuffle=True` 还是 `False`？验证集呢？
3. `__getitem__` 返回的数据类型不一致会导致什么问题？
4. `num_workers` 在 Windows 上可能引发什么错误？
