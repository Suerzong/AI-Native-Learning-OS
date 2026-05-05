# 训练循环技能地图

## 目标

学习者能写出标准、完整的训练循环，包含损失函数、优化器、train/eval 切换、指标记录。

## 必会概念

- 损失函数（Loss Function）：衡量预测和真实值的差距
- 优化器（Optimizer）：根据梯度更新参数
- 学习率（Learning Rate）：控制参数更新步长
- epoch：遍历整个数据集一次
- batch：一个 mini-batch 的数据
- 前向传播 → 计算损失 → 反向传播 → 参数更新
- train/eval 模式切换

## 必会 API

### 损失函数

| 类 | 用途 | 输入要求 |
|------|------|---------|
| `nn.CrossEntropyLoss()` | 多分类 | input: (N, C) logits, target: (N,) 类别索引 |
| `nn.MSELoss()` | 回归 | input 和 target shape 相同 |
| `nn.BCELoss()` | 二分类 | input: (N) 经过 sigmoid, target: (N) 0/1 |
| `nn.BCEWithLogitsLoss()` | 二分类（含 sigmoid） | input: (N) logits, target: (N) 0/1 |

### 优化器

| 类 | 用途 | 关键参数 |
|------|------|---------|
| `torch.optim.SGD(params, lr=, momentum=)` | SGD | lr, momentum, weight_decay |
| `torch.optim.Adam(params, lr=)` | Adam | lr, betas, weight_decay |
| `optimizer.zero_grad()` | 清零梯度 | - |
| `optimizer.step()` | 参数更新 | - |

## 代码片段

```python
# 标准训练循环
model = MyCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(num_epochs):
    # 训练阶段
    model.train()
    train_loss = 0.0
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()          # 1. 清零梯度
        outputs = model(inputs)         # 2. 前向传播
        loss = criterion(outputs, labels)  # 3. 计算损失
        loss.backward()                 # 4. 反向传播
        optimizer.step()                # 5. 参数更新

        train_loss += loss.item()

    # 验证阶段
    model.eval()
    val_loss = 0.0
    correct = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()

    print(f"Epoch {epoch+1}: train_loss={train_loss/len(train_loader):.4f}, "
          f"val_loss={val_loss/len(val_loader):.4f}, "
          f"accuracy={correct/len(val_dataset)*100:.2f}%")
```

## 训练五步法口诀

```
零 → 前 → 失 → 反 → 步
zero_grad → forward → loss → backward → step
```

## 常见错误

1. 顺序错误：先 step 再 backward
2. 忘记 zero_grad：梯度累加
3. 验证时忘记 model.eval() + torch.no_grad()
4. loss.item() 忘记调用，直接用 loss tensor 累加
5. 验证后忘记切回 model.train()
6. CrossEntropyLoss 输入加了 softmax（重复了）
7. device 不一致

## 训练阶梯

1. **五步法**：能默写 zero_grad → forward → loss → backward → step
2. **单步训练**：能用随机数据跑一个 step 并打印 loss
3. **多 epoch 训练**：加入 epoch 循环
4. **加入验证**：train/eval 切换 + 验证集评估
5. **完整训练函数**：封装成 train() 和 validate() 函数
6. **加入指标记录**：记录 loss 和 accuracy 曲线

## 掌握标准

- 能不看代码写出完整的训练循环
- 能解释每一步的作用
- 能正确使用 CrossEntropyLoss（输入是 logits）
- 能正确切换 train/eval 模式
- 能判断训练是否过拟合（train_loss 下降但 val_loss 上升）
