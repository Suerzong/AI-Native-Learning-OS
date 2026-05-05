# 模型保存与加载技能地图

## 目标

学习者能正确保存和加载模型，能实现断点续训，能处理跨设备加载问题。

## 必会概念

- state_dict：模型参数的字典（OrderedDict）
- 只保存 state_dict（推荐）vs 保存整个模型
- checkpoint：包含模型参数、优化器状态、epoch 等
- 断点续训：从 checkpoint 恢复继续训练
- 跨设备加载：GPU 训练 → CPU 推理

## 必会 API

| 函数 | 用途 | 示例 |
|------|------|------|
| `model.state_dict()` | 获取参数字典 | `state = model.state_dict()` |
| `model.load_state_dict(state)` | 加载参数 | `model.load_state_dict(state)` |
| `torch.save(obj, path)` | 保存到文件 | `torch.save(model.state_dict(), 'model.pth')` |
| `torch.load(path, map_location=)` | 加载文件 | `torch.load('model.pth', map_location=device)` |
| `model.eval()` | 加载后切换推理模式 | `model.eval()` |

## 代码片段

```python
import torch

# === 推荐方式：只保存 state_dict ===

# 保存
torch.save(model.state_dict(), 'model_weights.pth')

# 加载
model = MyCNN()                          # 先创建同结构模型
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()

# GPU → CPU 加载
model.load_state_dict(
    torch.load('model_weights.pth', map_location='cpu')
)

# === 保存完整 checkpoint（用于断点续训）===

# 保存
checkpoint = {
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}
torch.save(checkpoint, 'checkpoint.pth')

# 加载并续训
checkpoint = torch.load('checkpoint.pth')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
start_epoch = checkpoint['epoch'] + 1
```

## 常见错误

1. 保存整个模型（`torch.save(model, path)`）：不推荐，依赖代码结构
2. 加载时 strict=True 但模型结构不匹配会报错
3. GPU 训练的模型加载到 CPU 没设 map_location
4. 断点续训忘记保存 optimizer 状态
5. 加载后忘记 model.eval()

## 训练阶梯

1. **保存加载 state_dict**：基本保存和加载
2. **跨设备加载**：GPU → CPU
3. **完整 checkpoint**：保存模型 + 优化器 + epoch
4. **断点续训**：从 checkpoint 恢复训练
5. **最佳模型保存**：根据 val_loss 保存最优模型

## 掌握标准

- 能正确保存和加载 state_dict
- 能处理 GPU → CPU 的跨设备加载
- 能实现断点续训
- 能在训练中保存最优模型
- 能解释 state_dict 的内容
