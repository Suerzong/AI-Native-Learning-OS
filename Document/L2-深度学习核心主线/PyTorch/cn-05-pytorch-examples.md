# 通过示例学习 PyTorch

**作者：** [Justin Johnson](https://github.com/jcjohnson/pytorch-examples)

> 这是我们较早的 PyTorch 教程之一。你可以在[学习基础知识](https://pytorch.org/tutorials/beginner/basics/intro.html)中查看我们最新的初学者内容。

本教程通过自包含的示例介绍 [PyTorch](https://github.com/pytorch/pytorch) 的基本概念。

PyTorch 的核心提供两个主要特性：

  * 一个 n 维张量（Tensor），类似于 numpy 但可以在 GPU 上运行
  * 用于构建和训练神经网络的自动微分

我们将使用拟合 \\(y=\\sin(x)\\) 的三次多项式问题作为运行示例。网络将有四个参数，并通过梯度下降进行训练，通过最小化网络输出和真实输出之间的欧几里得距离来拟合随机数据。

> 你可以在此页面底部浏览单独的示例。

要运行下面的教程，请确保你已安装 [torch](https://github.com/pytorch/pytorch) 和 [numpy](https://github.com/numpy/numpy) 包。

## 张量

### 热身：numpy

在介绍 PyTorch 之前，我们将首先使用 numpy 实现网络。

Numpy 提供了一个 n 维数组对象，以及许多操作这些数组的函数。Numpy 是用于科学计算的通用框架；它不了解计算图或深度学习或梯度。然而，通过使用 numpy 操作手动实现网络的前向和反向传播，我们可以很容易地使用 numpy 来拟合正弦函数的三次多项式：

    import numpy as np
    import math

    # 创建随机输入和输出数据
    x = np.linspace(-math.pi, math.pi, 2000)
    y = np.sin(x)

    # 随机初始化权重
    a = np.random.randn()
    b = np.random.randn()
    c = np.random.randn()
    d = np.random.randn()

    learning_rate = 1e-6
    for t in range(2000):
        # 前向传播：计算预测的 y
        # y = a + b x + c x^2 + d x^3
        y_pred = a + b * x + c * x ** 2 + d * x ** 3

        # 计算并打印损失
        loss = np.square(y_pred - y).sum()
        if t % 100 == 99:
            print(t, loss)

        # 反向传播计算 a, b, c, d 关于损失的梯度
        grad_y_pred = 2.0 * (y_pred - y)
        grad_a = grad_y_pred.sum()
        grad_b = (grad_y_pred * x).sum()
        grad_c = (grad_y_pred * x ** 2).sum()
        grad_d = (grad_y_pred * x ** 3).sum()

        # 更新权重
        a -= learning_rate * grad_a
        b -= learning_rate * grad_b
        c -= learning_rate * grad_c
        d -= learning_rate * grad_d

    print(f'结果: y = {a} + {b} x + {c} x^2 + {d} x^3')

### PyTorch 张量

Numpy 是一个优秀的框架，但它不能利用 GPU 加速其数值计算。对于现代深度神经网络，GPU 通常提供 [50 倍或更大的加速](https://github.com/jcjohnson/cnn-benchmarks)，所以不幸的是 numpy 不足以用于现代深度学习。

这里我们介绍最基本的 PyTorch 概念：**张量（Tensor）**。PyTorch 张量在概念上与 numpy 数组相同：张量是一个 n 维数组，PyTorch 提供了许多操作这些张量的函数。在底层，张量可以跟踪计算图和梯度，但它们也可作为科学计算的通用工具。

与 numpy 不同，PyTorch 张量可以利用 GPU 加速其数值计算。要在 GPU 上运行 PyTorch 张量，你只需指定正确的设备。

这里我们使用 PyTorch 张量来拟合正弦函数的三次多项式。像上面的 numpy 示例一样，我们需要手动实现网络的前向和反向传播：

    import torch
    import math

    dtype = torch.float
    device = torch.device("cpu")
    # device = torch.device("cuda:0") # 取消注释以在 GPU 上运行

    # 创建随机输入和输出数据
    x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
    y = torch.sin(x)

    # 随机初始化权重
    a = torch.randn((), device=device, dtype=dtype)
    b = torch.randn((), device=device, dtype=dtype)
    c = torch.randn((), device=device, dtype=dtype)
    d = torch.randn((), device=device, dtype=dtype)

    learning_rate = 1e-6
    for t in range(2000):
        # 前向传播：计算预测的 y
        y_pred = a + b * x + c * x ** 2 + d * x ** 3

        # 计算并打印损失
        loss = (y_pred - y).pow(2).sum().item()
        if t % 100 == 99:
            print(t, loss)

        # 反向传播计算 a, b, c, d 关于损失的梯度
        grad_y_pred = 2.0 * (y_pred - y)
        grad_a = grad_y_pred.sum()
        grad_b = (grad_y_pred * x).sum()
        grad_c = (grad_y_pred * x ** 2).sum()
        grad_d = (grad_y_pred * x ** 3).sum()

        # 使用梯度下降更新权重
        a -= learning_rate * grad_a
        b -= learning_rate * grad_b
        c -= learning_rate * grad_c
        d -= learning_rate * grad_d

    print(f'结果: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')

## 自动微分（Autograd）

### PyTorch 张量和自动微分

在上面的示例中，我们必须手动实现神经网络的前向和反向传播。手动实现反向传播对于小型两层网络来说不是什么大事，但对于大型复杂网络来说会很快变得非常棘手。

幸运的是，我们可以使用[自动微分](https://en.wikipedia.org/wiki/Automatic_differentiation)来自动化神经网络中反向传播的计算。PyTorch 中的 **autograd** 包正好提供了这个功能。使用 autograd 时，网络的前向传播将定义一个**计算图**；图中的节点是张量，边是从输入张量产生输出张量的函数。通过这个图进行反向传播可以让你轻松计算梯度。

这听起来很复杂，但在实践中使用起来相当简单。每个张量代表计算图中的一个节点。如果 `x` 是一个张量且 `x.requires_grad=True`，那么 `x.grad` 是另一个张量，保存 `x` 关于某个标量值的梯度。

这里我们使用 PyTorch 张量和 autograd 来实现用三次多项式拟合正弦波的例子；现在我们不再需要手动实现网络的反向传播：

    import torch
    import math

    # 我们希望能够在加速器上训练模型，如 CUDA、MTIA 或 MPS
    # 如果当前加速器可用，我们将使用它。否则，我们使用 CPU。
    dtype = torch.float
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"使用 {device} 设备")
    torch.set_default_device(device)

    # 创建张量来保存输入和输出。
    # 默认情况下，requires_grad=False，表示我们不需要在反向传播中计算这些张量的梯度。
    x = torch.linspace(-1, 1, 2000, dtype=dtype)
    y = torch.exp(x)

    # 为权重创建随机张量。对于三次多项式，我们需要 4 个权重：
    # y = a + b x + c x^2 + d x^3
    # 设置 requires_grad=True 表示我们希望在反向传播中计算这些张量的梯度。
    a = torch.randn((), dtype=dtype, requires_grad=True)
    b = torch.randn((), dtype=dtype, requires_grad=True)
    c = torch.randn((), dtype=dtype, requires_grad=True)
    d = torch.randn((), dtype=dtype, requires_grad=True)

    initial_loss = 1.
    learning_rate = 1e-5
    for t in range(5000):
        # 前向传播：使用张量操作计算预测的 y
        y_pred = a + b * x + c * x ** 2 + d * x ** 3

        # 使用张量操作计算并打印损失
        loss = (y_pred - y).pow(2).sum()

        if t==0:
            initial_loss=loss.item()

        if t % 100 == 99:
            print(f'迭代 t = {t:4d}  loss(t)/loss(0) = {round(loss.item()/initial_loss, 6):10.6f}  a = {a.item():10.6f}  b = {b.item():10.6f}  c = {c.item():10.6f}  d = {d.item():10.6f}')

        # 使用 autograd 计算反向传播
        loss.backward()

        # 使用梯度下降手动更新权重
        with torch.no_grad():
            a -= learning_rate * a.grad
            b -= learning_rate * b.grad
            c -= learning_rate * c.grad
            d -= learning_rate * d.grad

            # 更新权重后手动清零梯度
            a.grad = None
            b.grad = None
            c.grad = None
            d.grad = None

    print(f'结果: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')

### 定义新的自动微分函数

在底层，每个原始自动微分算子实际上是两个操作张量的函数。**前向**函数从输入张量计算输出张量。**反向**函数接收输出张量关于某个标量值的梯度，并计算输入张量关于同一标量值的梯度。

在 PyTorch 中，我们可以通过定义 `torch.autograd.Function` 的子类并实现 `forward` 和 `backward` 函数来轻松定义自己的自动微分算子。然后我们可以像调用函数一样构造实例并调用它，传递包含输入数据的张量。

在这个例子中，我们将模型定义为 \\(y=a+b P_3(c+dx)\\) 而不是 \\(y=a+bx+cx^2+dx^3\\)，其中 \\(P_3(x)=\\frac{1}{2}(5x^3-3x)\\) 是三次[勒让德多项式](https://en.wikipedia.org/wiki/Legendre_polynomials)。我们编写自己的自定义自动微分函数来计算 \\(P_3\\) 的前向和反向传播：

    class LegendrePolynomial3(torch.autograd.Function):
        @staticmethod
        def forward(ctx, input):
            ctx.save_for_backward(input)
            return 0.5 * (5 * input ** 3 - 3 * input)

        @staticmethod
        def backward(ctx, grad_output):
            input, = ctx.saved_tensors
            return grad_output * 1.5 * (5 * input ** 2 - 1)

## nn 模块

### PyTorch nn

计算图和自动微分是定义复杂算子并自动求导的非常强大的范式；然而，对于大型神经网络来说，原始的自动微分可能有点太底层了。

在构建神经网络时，我们经常考虑将计算安排成**层**，其中一些层有**可学习的参数**，在学习过程中会被优化。

在 PyTorch 中，`nn` 包服务于相同的目的。`nn` 包定义了一组**模块（Modules）**，大致相当于神经网络层。模块接收输入张量并计算输出张量，但也可以保存内部状态，如包含可学习参数的张量。`nn` 包还定义了一组在训练神经网络时常用的有用损失函数。

在这个例子中，我们使用 `nn` 包来实现我们的多项式模型网络：

    model = torch.nn.Sequential(
        torch.nn.Linear(3, 1),
        torch.nn.Flatten(0, 1)
    )

    loss_fn = torch.nn.MSELoss(reduction='sum')

    learning_rate = 1e-6
    for t in range(2000):
        y_pred = model(xx)
        loss = loss_fn(y_pred, y)
        if t % 100 == 99:
            print(t, loss.item())

        model.zero_grad()
        loss.backward()

        with torch.no_grad():
            for param in model.parameters():
                param -= learning_rate * param.grad

### PyTorch 优化器（optim）

到目前为止，我们通过使用 `torch.no_grad()` 手动修改保存可学习参数的张量来更新模型的权重。对于像随机梯度下降这样的简单优化算法来说，这不是很大的负担，但在实践中，我们经常使用更复杂的优化器（如 `AdaGrad`、`RMSProp`、`Adam` 等）来训练神经网络。

PyTorch 中的 `optim` 包抽象了优化算法的思想，并提供了常用优化算法的实现。

在这个例子中，我们将使用 `nn` 包像之前一样定义模型，但我们将使用 `optim` 包提供的 `RMSprop` 算法来优化模型：

    learning_rate = 1e-3
    optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
    for t in range(2000):
        y_pred = model(xx)
        loss = loss_fn(y_pred, y)
        if t % 100 == 99:
            print(t, loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

### 自定义 nn 模块

有时你会想要指定比现有模块序列更复杂的模型；对于这些情况，你可以通过子类化 `nn.Module` 并定义一个接收输入张量并使用其他模块或张量上的其他自动微分操作产生输出张量的 `forward` 来定义自己的模块。

在这个例子中，我们将三次多项式实现为自定义模块子类：

    class Polynomial3(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.a = torch.nn.Parameter(torch.randn(()))
            self.b = torch.nn.Parameter(torch.randn(()))
            self.c = torch.nn.Parameter(torch.randn(()))
            self.d = torch.nn.Parameter(torch.randn(()))

        def forward(self, x):
            return self.a + self.b * x + self.c * x ** 2 + self.d * x ** 3

        def string(self):
            return f'y = {self.a.item()} + {self.b.item()} x + {self.c.item()} x^2 + {self.d.item()} x^3'

### 控制流和权重共享

作为动态图和权重共享的一个例子，我们实现一个非常奇怪的模型：一个三到五次多项式，在每次前向传播中选择 3 到 5 之间的随机数，并使用该数量的阶数，重用相同的权重多次计算四次和五次。

    class DynamicNet(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.a = torch.nn.Parameter(torch.randn(()))
            self.b = torch.nn.Parameter(torch.randn(()))
            self.c = torch.nn.Parameter(torch.randn(()))
            self.d = torch.nn.Parameter(torch.randn(()))
            self.e = torch.nn.Parameter(torch.randn(()))

        def forward(self, x):
            y = self.a + self.b * x + self.c * x ** 2 + self.d * x ** 3
            for exp in range(4, random.randint(4, 6)):
                y = y + self.e * x ** exp
            return y

        def string(self):
            return f'y = {self.a.item()} + {self.b.item()} x + {self.c.item()} x^2 + {self.d.item()} x^3 + {self.e.item()} x^4 ? + {self.e.item()} x^5 ?'
