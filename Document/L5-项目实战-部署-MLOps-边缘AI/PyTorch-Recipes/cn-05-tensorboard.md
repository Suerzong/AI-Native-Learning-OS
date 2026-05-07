# 如何在 PyTorch 中使用 TensorBoard

> 来源：https://docs.pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html

TensorBoard 是一个用于机器学习实验的可视化工具包。TensorBoard 允许跟踪和可视化指标（如损失和准确率）、可视化模型图、查看直方图、显示图像等。在本教程中，我们将介绍 TensorBoard 的安装、与 PyTorch 的基本用法以及如何在 TensorBoard UI 中可视化你记录的数据。

## 安装

需要安装 PyTorch 才能将模型和指标记录到 TensorBoard 日志目录。以下命令通过 Anaconda 安装 PyTorch 1.4+（推荐）：

```bash
conda install pytorch torchvision -c pytorch
```

或使用 pip：

```bash
pip install torch torchvision
```

## 在 PyTorch 中使用 TensorBoard

在记录任何内容之前，我们需要创建一个 `SummaryWriter` 实例。

```python
import torch
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
```

Writer 默认输出到 `./runs/` 目录。

## 记录标量

在机器学习中，了解关键指标（如损失）及其在训练过程中的变化非常重要。标量（Scalar）有助于保存每个训练步骤的损失值或每个 epoch 之后的准确率。

要记录标量值，使用 `add_scalar(tag, scalar_value, global_step=None, walltime=None)`。例如，让我们创建一个简单的线性回归训练，并使用 `add_scalar` 记录损失值：

```python
x = torch.arange(-5, 5, 0.1).view(-1, 1)
y = -5 * x + 0.1 * torch.randn(x.size())

model = torch.nn.Linear(1, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1)

def train_model(iter):
    for epoch in range(iter):
        y1 = model(x)
        loss = criterion(y1, y)
        writer.add_scalar("Loss/train", loss, epoch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

train_model(10)
writer.flush()
```

调用 `flush()` 方法确保所有待处理的事件都已写入磁盘。

如果不再需要 summary writer，调用 `close()` 方法：

```python
writer.close()
```

## 运行 TensorBoard

通过命令行安装 TensorBoard 以可视化你记录的数据：

```bash
pip install tensorboard
```

现在，启动 TensorBoard，指定你上面使用的根日志目录：

```bash
tensorboard --logdir=runs
```

访问它提供的 URL 或 <http://localhost:6006/>

此仪表板显示损失和准确率如何随每个 epoch 变化。你还可以使用它跟踪训练速度、学习率和其他标量值。比较不同训练运行中的这些指标有助于改进你的模型。

## 了解更多

- [torch.utils.tensorboard](https://pytorch.org/docs/stable/tensorboard.html) 文档
- [使用 TensorBoard 可视化模型、数据和训练](https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) 教程
