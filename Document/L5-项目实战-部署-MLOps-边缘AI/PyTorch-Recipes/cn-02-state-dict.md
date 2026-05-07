# PyTorch 中的 state_dict 是什么

> 来源：https://docs.pytorch.org/tutorials/recipes/recipes/what_is_state_dict.html

在 PyTorch 中，`torch.nn.Module` 模型的可学习参数（即权重和偏置）包含在模型的参数中（通过 `model.parameters()` 访问）。`state_dict` 是一个简单的 Python 字典对象，它将每一层映射到其参数张量。

## 简介

`state_dict` 是如果你有兴趣从 PyTorch 保存或加载模型的不可或缺的实体。因为 `state_dict` 对象是 Python 字典，它们可以很容易地保存、更新、修改和恢复，为 PyTorch 模型和优化器增加了大量的模块化。请注意，只有具有可学习参数的层（卷积层、线性层等）和注册的缓冲区（如 batchnorm 的 running_mean）在模型的 `state_dict` 中有条目。优化器对象（`torch.optim`）也有一个 `state_dict`，其中包含有关优化器状态以及使用的超参数的信息。

## 步骤

1. 导入加载数据所需的所有库
2. 定义并初始化神经网络
3. 初始化优化器
4. 访问模型和优化器的 `state_dict`

### 1. 导入所需库

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
```

### 2. 定义并初始化神经网络

```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
print(net)
```

### 3. 初始化优化器

```python
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
```

### 4. 访问模型和优化器的 `state_dict`

```python
# 打印模型的 state_dict
print("Model's state_dict:")
for param_tensor in net.state_dict():
    print(param_tensor, "\t", net.state_dict()[param_tensor].size())

print()

# 打印优化器的 state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])
```

这些信息对于保存和加载模型及优化器以供将来使用非常重要。

恭喜！你已成功在 PyTorch 中使用了 `state_dict`。

## 了解更多

- [在 PyTorch 中保存和加载模型进行推理](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_models_for_inference.html)
- [在 PyTorch 中保存和加载通用检查点](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html)
