# 迁移学习技能地图

## 目标

学习者能加载预训练模型，能替换最后一层做 fine-tuning，能在小数据集上获得比从零训练更好的效果。

## 必会概念

- 迁移学习：利用在大数据集（ImageNet）上预训练的模型
- Feature Extraction：冻结预训练层，只训练新分类头
- Fine-tuning：解冻部分或全部预训练层，用小学习率微调
- 预训练模型：在 ImageNet 上训练好的模型（ResNet、VGG、MobileNet 等）
- 冻结层：设置 `param.requires_grad = False`

## 必会 API

| 函数/属性 | 用途 | 示例 |
|-----------|------|------|
| `torchvision.models.resnet18(pretrained=True)` | 加载预训练 ResNet18 | 见代码 |
| `torchvision.models.mobilenet_v2(pretrained=True)` | 加载 MobileNetV2 | 轻量级模型，适合端侧 |
| `model.fc = nn.Linear(512, num_classes)` | 替换最后一层 | ResNet 系列 |
| `param.requires_grad_(False)` | 冻结参数 | Feature Extraction |
| `torchvision.models.ResNet18_Weights.DEFAULT` | 新版权重加载方式 | PyTorch >= 0.13 |

## 代码片段

```python
import torch
import torch.nn as nn
import torchvision.models as models

# === 方式一：Feature Extraction（冻结所有预训练层）===
model = models.resnet18(pretrained=True)

# 冻结所有参数
for param in model.parameters():
    param.requires_grad = False

# 替换最后一层（默认 1000 类 → 自定义类别数）
num_classes = 10
model.fc = nn.Linear(model.fc.in_features, num_classes)

# 只有 fc 层的参数会训练
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

# === 方式二：Fine-tuning（解冻最后几层）===
model = models.resnet18(pretrained=True)

# 冻结前面的层
for name, param in model.named_parameters():
    if 'layer4' not in name and 'fc' not in name:
        param.requires_grad = False

# 替换最后一层
model.fc = nn.Linear(model.fc.in_features, num_classes)

# 对预训练层和新层用不同学习率
optimizer = torch.optim.Adam([
    {'params': model.layer4.parameters(), 'lr': 0.0001},  # 小学习率
    {'params': model.fc.parameters(), 'lr': 0.001},       # 大学习率
])

# === 方式三：新版 API（推荐）===
from torchvision.models import ResNet18_Weights
model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
```

## 何时用迁移学习

| 场景 | 推荐做法 |
|------|---------|
| 数据量小（< 1000 张/类） | Feature Extraction |
| 数据量中等（1000-10000 张/类） | Fine-tuning |
| 数据量大（> 10000 张/类） | 从零训练或微调 |
| 数据和 ImageNet 差异大 | 冻结前几层，微调后面 |
| 需要快速部署 | 用 MobileNet 等轻量模型 |

## 常见错误

1. 忘记替换最后一层（输出 1000 类而不是自己的类别数）
2. 冻结后 optimizer 还包含冻结层的参数（浪费计算）
3. 对预训练层用太大的学习率（破坏特征）
4. 数据预处理的 mean/std 和预训练模型不一致
5. 不理解 requires_grad=False 的影响

## 训练阶梯

1. **加载预训练模型**：打印模型结构，理解最后一层
2. **替换最后一层**：修改 fc 层
3. **Feature Extraction**：冻结所有层，只训练新头
4. **Fine-tuning**：解冻最后几层
5. **对比实验**：从零训练 vs 迁移学习的准确率差异

## 掌握标准

- 能加载预训练模型并替换最后一层
- 能正确冻结/解冻参数
- 能用不同学习率微调不同层
- 能对比迁移学习和从零训练的效果
- 理解什么时候用 feature extraction、什么时候用 fine-tuning
