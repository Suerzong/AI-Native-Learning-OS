[跳转到主要内容](#main-content)

__返回顶部

__ `Ctrl`+`K`

评价此页面

★ ★ ★ ★ ★

beginner/blitz/tensor_tutorial

![](../../_static/img/pytorch-colab.svg) 在 Google Colab 中运行 Colab ![](../../_static/img/pytorch-download.svg) 下载 Notebook Notebook ![](../../_static/img/pytorch-github.svg) 在 GitHub 上查看 GitHub

提示

[跳转到页面底部](#sphx-glr-download-beginner-blitz-tensor-tutorial-py)下载完整示例代码。

# 张量[#](#tensors "Link to this heading")

创建日期：2017 年 3 月 24 日 | 最后更新：2024 年 1 月 16 日 | 最后验证：2024 年 11 月 5 日

张量（Tensor）是一种专门的数据结构，与数组和矩阵非常相似。在 PyTorch 中，我们使用张量来编码模型的输入和输出，以及模型的参数。

张量类似于 NumPy 的 ndarray，不同之处在于张量可以在 GPU 或其他专用硬件上运行以加速计算。如果你熟悉 ndarray，那么你会对张量 API 得心应手。如果不熟悉，请跟着这个快速 API 概览来学习。


    import torch
    import numpy as np


## 张量初始化[#](#tensor-initialization "Link to this heading")

张量可以通过多种方式初始化。请看以下示例：

**直接从数据创建**

张量可以直接从数据创建，数据类型会被自动推断。


    data = [[1, 2], [3, 4]]
    x_data = torch.tensor(data)


**从 NumPy 数组创建**

张量可以从 NumPy 数组创建（反之亦然——参见[与 NumPy 的桥接](#bridge-to-np-label)）。


    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)


**从另一个张量创建：**

新张量保留参数张量的属性（形状、数据类型），除非被显式覆盖。


    x_ones = torch.ones_like(x_data) # 保留 x_data 的属性
    print(f"全 1 张量: \n {x_ones} \n")

    x_rand = torch.rand_like(x_data, dtype=torch.float) # 覆盖 x_data 的数据类型
    print(f"随机张量: \n {x_rand} \n")



    全 1 张量:
     tensor([[1, 1],
            [1, 1]])

    随机张量:
     tensor([[0.8461, 0.1849],
            [0.8453, 0.2983]])


**使用随机值或常量值：**

`shape` 是张量维度的元组。在下面的函数中，它决定了输出张量的维度。


    shape = (2, 3,)
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    print(f"随机张量: \n {rand_tensor} \n")
    print(f"全 1 张量: \n {ones_tensor} \n")
    print(f"全 0 张量: \n {zeros_tensor}")



    随机张量:
     tensor([[0.6388, 0.6338, 0.1391],
            [0.5276, 0.7904, 0.1924]])

    全 1 张量:
     tensor([[1., 1., 1.],
            [1., 1., 1.]])

    全 0 张量:
     tensor([[0., 0., 0.],
            [0., 0., 0.]])


* * *

## 张量属性[#](#tensor-attributes "Link to this heading")

张量属性描述了它们的形状、数据类型以及存储所在的设备。


    tensor = torch.rand(3, 4)

    print(f"张量的形状: {tensor.shape}")
    print(f"张量的数据类型: {tensor.dtype}")
    print(f"张量存储所在的设备: {tensor.device}")



    张量的形状: torch.Size([3, 4])
    张量的数据类型: torch.float32
    张量存储所在的设备: cpu


* * *

## 张量操作[#](#tensor-operations "Link to this heading")

超过 100 种张量操作，包括转置、索引、切片、数学运算、线性代数、随机采样等，详见[此处](https://pytorch.org/docs/stable/torch.html)。

每种操作都可以在 GPU 上运行（通常比在 CPU 上更快）。如果你使用 Colab，请通过 编辑 > Notebook 设置 来分配 GPU。


    # 如果可用的话，将张量移动到 GPU
    if torch.cuda.is_available():
      tensor = tensor.to('cuda')
      print(f"张量存储所在的设备: {tensor.device}")



    张量存储所在的设备: cuda:0


试试列表中的一些操作。如果你熟悉 NumPy API，你会发现张量 API 用起来很轻松。

**标准的类 NumPy 索引和切片：**


    tensor = torch.ones(4, 4)
    tensor[:,1] = 0
    print(tensor)



    tensor([[1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.]])


**拼接张量** 你可以使用 `torch.cat` 沿给定维度拼接一系列张量。另请参阅 [torch.stack](https://pytorch.org/docs/stable/generated/torch.stack.html)，这是另一种与 `torch.cat` 有微妙不同的张量拼接操作。


    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print(t1)



    tensor([[1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.]])


**张量乘法**


    # 计算逐元素乘积
    print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
    # 另一种语法:
    print(f"tensor * tensor \n {tensor * tensor}")



    tensor.mul(tensor)
     tensor([[1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.]])

    tensor * tensor
     tensor([[1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.]])


计算两个张量之间的矩阵乘法


    print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
    # 另一种语法:
    print(f"tensor @ tensor.T \n {tensor @ tensor.T}")



    tensor.matmul(tensor.T)
     tensor([[3., 3., 3., 3.],
            [3., 3., 3., 3.],
            [3., 3., 3., 3.],
            [3., 3., 3., 3.]])

    tensor @ tensor.T
     tensor([[3., 3., 3., 3.],
            [3., 3., 3., 3.],
            [3., 3., 3., 3.],
            [3., 3., 3., 3.]])


**就地操作（In-place Operations）** 带有 `_` 后缀的操作是就地操作。例如：`x.copy_(y)`、`x.t_()` 会改变 `x`。


    print(tensor, "\n")
    tensor.add_(5)
    print(tensor)



    tensor([[1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.]])

    tensor([[6., 5., 6., 6.],
            [6., 5., 6., 6.],
            [6., 5., 6., 6.],
            [6., 5., 6., 6.]])


提示

就地操作可以节省一些内存，但在计算导数时可能会出现问题，因为历史记录会立即丢失。因此，不鼓励使用就地操作。

* * *

## 与 NumPy 的桥接[#](#bridge-with-numpy "Link to this heading")

CPU 上的张量和 NumPy 数组可以共享底层内存位置，改变其中一个会同时改变另一个。

### 张量转 NumPy 数组[#](#tensor-to-numpy-array "Link to this heading")


    t = torch.ones(5)
    print(f"t: {t}")
    n = t.numpy()
    print(f"n: {n}")



    t: tensor([1., 1., 1., 1., 1.])
    n: [1. 1. 1. 1. 1.]


张量的变化会反映在 NumPy 数组中。


    t.add_(1)
    print(f"t: {t}")
    print(f"n: {n}")



    t: tensor([2., 2., 2., 2., 2.])
    n: [2. 2. 2. 2. 2.]


### NumPy 数组转张量[#](#numpy-array-to-tensor "Link to this heading")


    n = np.ones(5)
    t = torch.from_numpy(n)


NumPy 数组的变化会反映在张量中。


    np.add(n, 1, out=n)
    print(f"t: {t}")
    print(f"n: {n}")



    t: tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
    n: [2. 2. 2. 2. 2.]


**脚本总运行时间：**（0 分钟 0.435 秒）

## 文档

访问 PyTorch 的综合开发者文档

[查看文档](https://docs.pytorch.org/docs/stable/index.html)

## 教程

获取面向初学者和高级开发者的深入教程

[查看教程](https://docs.pytorch.org/tutorials)

## 资源

查找开发资源并获得问题解答

[查看资源](https://pytorch.org/resources)

为分析流量和优化你的体验，我们在本网站上使用 Cookie。通过点击或导航，你同意允许我们使用 Cookie。作为本网站的当前维护者，适用 Facebook 的 Cookie 政策。了解更多，包括可用的控制选项：[Cookie 政策](https://opensource.fb.com/legal/cookie-policy)。
