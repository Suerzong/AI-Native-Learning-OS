# 弱点追踪

记录影响后续能力形成的核心弱点。只有同一弱点出现 2 次以上才记录。

## 模板

```md
### 弱点标题

- 首次出现：YYYY-MM-DD
- 最近出现：YYYY-MM-DD
- 出现次数：
- 症状描述：
- 根本原因：
- 纠正策略：
- 是否已解决：
```

---

## 常见弱点库（预防性记录）

以下弱点是 PyTorch 初学者最高发的，在教学中需要优先关注。

### Tensor Shape 推理能力弱

- 症状：不能预测 reshape、Conv2d、broadcasting 后的 shape
- 根本原因：对 tensor 的维度含义不直观
- 纠正策略：每步操作后都标注 shape，用"形状追踪"习惯化
- 是否已解决：否

### 训练循环步骤遗漏

- 症状：漏掉 zero_grad、漏掉 model.eval()、漏掉 loss.item()
- 根本原因：没有形成标准模板
- 纠正策略：用"训练五步法"口诀：零 → 前 → 失 → 反 → 步
- 是否已解决：否

### Device 不匹配错误

- 症状：模型在 GPU、数据在 CPU，报 RuntimeError
- 根本原因：没有建立 device 管理意识
- 纠正策略：从第一天就用 `device = torch.device(...)` 模板
- 是否已解决：否

### CrossEntropyLoss 输入格式错误

- 症状：模型输出加了 softmax 再传给 CrossEntropyLoss
- 根本原因：不理解 CrossEntropyLoss 内部已包含 log_softmax
- 纠正策略：每次用 CrossEntropyLoss 时都问"模型输出是什么"
- 是否已解决：否

### train/eval 模式混淆

- 症状：验证时忘记 model.eval()，训练时忘记 model.train()
- 根本原因：不理解哪些层受模式影响
- 纠正策略：列出受模式影响的层（Dropout、BatchNorm），建立切换习惯
- 是否已解决：否

---

（以上为预防性记录，实际训练中出现的弱点会更新到具体条目）
