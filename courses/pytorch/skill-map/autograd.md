# 自动求导（Autograd）技能地图

## 目标

学习者能理解 PyTorch 自动求导机制，能手动验证梯度计算，能在训练循环中正确使用梯度相关 API。

## 必会概念

- requires_grad：标记 tensor 需要梯度
- 计算图（Computational Graph）：记录运算关系的有向图
- 前向传播：沿计算图正向计算
- 反向传播（backward）：沿计算图反向传播梯度
- 梯度累加：backward 是累加而非覆盖
- 梯度清零（zero_grad）
- torch.no_grad()：推理时禁用梯度计算
- detach：从计算图中分离

## 必会 API

| 函数/属性 | 用途 | 示例 |
|-----------|------|------|
| `requires_grad_(True)` | 原地设置需要梯度 | `x.requires_grad_(True)` |
| `x.grad` | 获取梯度值 | `print(w.grad)` |
| `loss.backward()` | 反向传播 | `loss.backward()` |
| `w.grad.zero_()` | 清零梯度 | `w.grad.zero_()` |
| `torch.no_grad()` | 禁用梯度上下文 | `with torch.no_grad(): ...` |
| `x.detach()` | 从计算图分离 | `x.detach()` |
| `x.requires_grad_(False)` | 关闭梯度追踪 | `x.requires_grad_(False)` |
| `optimizer.zero_grad()` | 优化器清零梯度 | `optimizer.zero_grad()` |

## 代码片段

```python
import torch

# 基本自动求导
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2 + 3 * x + 1       # y = x^2 + 3x + 1
y.backward()                  # 反向传播
print(x.grad)                 # dy/dx = 2x + 3 = 7.0

# 梯度清零的重要性
w = torch.tensor([1.0], requires_grad=True)
for i in range(3):
    loss = w * 2
    loss.backward()
    print(f"Step {i}: grad = {w.grad}")  # 2.0, 4.0, 6.0 (累加！)
    w.grad.zero_()                        # 清零

# torch.no_grad() 推理
model.eval()
with torch.no_grad():
    output = model(input)     # 不构建计算图，节省显存
```

## 常见错误

1. 忘记 `requires_grad=True` 导致梯度为 None
2. `backward()` 对非标量报错（需要传入 gradient 参数）
3. 不 zero_grad 导致梯度累加
4. 推理时不用 `no_grad()` 浪费显存
5. `detach()` 后的 tensor 不再有梯度

## 训练阶梯

1. **创建带梯度的 tensor**：理解 requires_grad
2. **简单函数求导**：验证 y = x^2 的梯度
3. **复合函数求导**：用链式法则手动验证
4. **梯度累加实验**：故意不 zero_grad 观察效果
5. **no_grad 实践**：在推理代码中正确使用

## 掌握标准

- 能手动推导简单函数的梯度并用 autograd 验证
- 能解释计算图的构建过程
- 能解释为什么每次 backward 前要 zero_grad
- 能在推理代码中正确使用 no_grad
- 能理解 detach 的作用和使用场景
