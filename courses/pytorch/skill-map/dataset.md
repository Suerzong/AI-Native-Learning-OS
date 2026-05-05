# Dataset 与 DataLoader 技能地图

## 目标

学习者能创建自定义 Dataset，能正确配置 DataLoader，能处理各种数据格式（图片、CSV、自定义格式）。

## 必会概念

- Dataset：数据集的抽象，定义"怎么取一个样本"
- DataLoader：数据加载器，定义"怎么取一个 batch"
- `__len__`：返回数据集大小
- `__getitem__`：返回第 i 个样本（data, label）
- collate_fn：如何将多个样本组成一个 batch
- shuffle：是否打乱顺序
- num_workers：并行加载的进程数
- pin_memory：是否使用锁页内存加速 GPU 传输

## 必会 API

| 类/函数 | 用途 | 来源 |
|---------|------|------|
| `torch.utils.data.Dataset` | 自定义数据集基类 | torch.utils.data |
| `torch.utils.data.DataLoader` | 数据加载器 | torch.utils.data |
| `torchvision.datasets.MNIST` | MNIST 数据集 | torchvision.datasets |
| `torchvision.datasets.CIFAR10` | CIFAR-10 数据集 | torchvision.datasets |
| `torchvision.datasets.ImageFolder` | 按文件夹分类的图片数据集 | torchvision.datasets |

## 代码片段

```python
import torch
from torch.utils.data import Dataset, DataLoader

# 自定义 Dataset
class MyDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx]
        y = self.labels[idx]
        if self.transform:
            x = self.transform(x)
        return x, y

# 使用
dataset = MyDataset(train_data, train_labels)
loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,        # 训练集必须 shuffle
    num_workers=0,       # Windows 上先设 0
    pin_memory=True      # 有 GPU 时建议开启
)

for batch_x, batch_y in loader:
    # batch_x: (32, ...)
    # batch_y: (32,)
    output = model(batch_x)
    ...
```

```python
# 内置数据集
import torchvision
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

trainset = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
```

## 常见错误

1. 不实现 `__len__` 或 `__getitem__` 导致 TypeError
2. `__getitem__` 返回类型不一致导致 collate 失败
3. 训练集没 shuffle、验证集 shuffle 了
4. num_workers > 0 在 Windows 上可能报 multiprocessing 错误
5. 数据类型不匹配（图片是 float，label 是 long）

## 训练阶梯

1. **使用内置数据集**：加载 MNIST/CIFAR-10
2. **理解 DataLoader**：调整 batch_size 和 shuffle
3. **自定义 Dataset**：从 numpy 数组创建
4. **自定义数据格式**：从 CSV 或图片文件夹创建
5. **完整流程**：Dataset → DataLoader → 训练循环

## 掌握标准

- 能从零创建自定义 Dataset 类
- 能正确配置 DataLoader 参数
- 能处理图片和表格数据
- 能解释 shuffle 和 num_workers 的作用
- 能处理 collate_fn 的自定义需求
