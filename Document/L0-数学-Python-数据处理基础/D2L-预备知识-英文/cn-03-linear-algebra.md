# 2.3. 线性代数（Linear Algebra）

到目前为止，我们已经可以将数据集加载到张量（tensor）中，并使用基本的数学运算来操作这些张量。为了开始构建复杂的模型，我们还需要线性代数中的一些工具。本节简要介绍最基本的概念，从标量算术开始，逐步提升到矩阵乘法。

    import torch

    from mxnet import np, npx

    npx.set_np()

    from jax import numpy as jnp

    import tensorflow as tf

## 2.3.1. 标量（Scalars）

大多数日常数学运算由逐个操作数字组成。从形式上来说，我们称这些值为 _标量_（scalar）。例如，帕洛阿尔托的温度是宜人的 \\(72\\) 华氏度。如果你想将温度转换为摄氏度，你需要计算表达式 \\(c = \frac{5}{9}(f - 32)\\)，将 \\(f\\) 设为 \\(72)。在这个等式中，值 \\(5\\)、\\(9\\) 和 \\(32\\) 是常量标量。变量 \\(c\\) 和 \\(f\\) 通常表示未知标量。

我们用普通的小写字母（例如 \\(x\\)、\\(y\\) 和 \\(z\\)）表示标量，并用 \\(\mathbb{R}\\) 表示所有（连续的）_实值_ 标量的空间。为简便起见，我们将跳过 _空间_ 的严格定义：只需记住表达式 \\(x \in \mathbb{R}\\) 是表示 \\(x\\) 是实值标量的正式方式。符号 \\(\in\\)（读作"属于"）表示集合中的成员关系。例如，\\(x, y \in \\{0, 1\\}\\) 表示 \\(x\\) 和 \\(y\\) 是只能取值 \\(0\\) 或 \\(1\\) 的变量。

标量被实现为仅包含一个元素的张量。下面，我们分配两个标量并执行熟悉的加法、乘法、除法和指数运算。

    x = torch.tensor(3.0)
    y = torch.tensor(2.0)

    x + y, x * y, x / y, x**y

    (tensor(5.), tensor(6.), tensor(1.5000), tensor(9.))

    x = np.array(3.0)
    y = np.array(2.0)

    x + y, x * y, x / y, x ** y

    (array(5.), array(6.), array(1.5), array(9.))

    x = jnp.array(3.0)
    y = jnp.array(2.0)

    x + y, x * y, x / y, x**y

    (Array(5., dtype=float32, weak_type=True),
     Array(6., dtype=float32, weak_type=True),
     Array(1.5, dtype=float32, weak_type=True),
     Array(9., dtype=float32, weak_type=True))

    x = tf.constant(3.0)
    y = tf.constant(2.0)

    x + y, x * y, x / y, x**y

    (<tf.Tensor: shape=(), dtype=float32, numpy=5.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=1.5>,
     <tf.Tensor: shape=(), dtype=float32, numpy=9.0>)

## 2.3.2. 向量（Vectors）

就目前而言，你可以将向量视为标量的固定长度数组。与代码中的对应物一样，我们将这些标量称为向量的 _元素_（同义词包括 _条目_ 和 _分量_）。当向量表示来自真实世界数据集的样本时，它们的值具有一定的现实意义。例如，如果我们正在训练一个模型来预测贷款违约风险，我们可能会将每个申请人与一个向量关联，其分量对应于诸如收入、工作年限或先前违约次数等数量。如果我们正在研究心脏病发作的风险，每个向量可能代表一个患者，其分量可能对应于他们最近的生命体征、胆固醇水平、每天运动分钟数等。我们用粗体小写字母表示向量（例如 \\(\mathbf{x}\\)、\\(\mathbf{y}\\) 和 \\(\mathbf{z}\\)）。

向量被实现为 \\(1^{\textrm{st}}\\) 阶张量。一般来说，这样的张量可以具有任意长度（受内存限制）。注意：在 Python 中，与大多数编程语言一样，向量索引从 \\(0\\) 开始，也称为 _零基索引_，而在线性代数中下标从 \\(1\\) 开始（一基索引）。

    x = torch.arange(3)
    x

    tensor([0, 1, 2])

    x = np.arange(3)
    x

    array([0., 1., 2.])

    x = jnp.arange(3)
    x

    Array([0, 1, 2], dtype=int32)

    x = tf.range(3)
    x

    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([0, 1, 2], dtype=int32)>

我们可以通过使用下标来引用向量的元素。例如，\\(x_2\\) 表示 \\(\mathbf{x}\\) 的第二个元素。由于 \\(x_2\\) 是标量，我们不用粗体表示它。默认情况下，我们通过垂直堆叠元素来可视化向量。

(2.3.1)\\[\begin{split}\mathbf{x} =\begin{bmatrix}x_{1} \\\ \vdots \\\x_{n}\end{bmatrix},\end{split}\\]

这里 \\(x_1, \ldots, x_n\\) 是向量的元素。稍后，我们将区分这种 _列向量_ 和元素水平堆叠的 _行向量_。回想一下，我们通过索引访问张量的元素。

    x[2]

    tensor(2)

    x[2]

    array(2.)

    x[2]

    Array(2, dtype=int32)

    x[2]

    <tf.Tensor: shape=(), dtype=int32, numpy=2>

为了表示向量包含 \\(n\\) 个元素，我们写作 \\(\mathbf{x} \in \mathbb{R}^n\\)。从形式上讲，我们称 \\(n\\) 为向量的 _维度_（dimensionality）。在代码中，这对应于张量的长度，可以通过 Python 内置的 `len` 函数访问。

    len(x)

    3

    len(x)

    3

    len(x)

    3

    len(x)

    3

我们也可以通过 `shape` 属性访问长度。形状是一个元组，表示张量沿每个轴的长度。只有一个轴的张量的形状只有一个元素。

    x.shape

    torch.Size([3])

    x.shape

    (3,)

    x.shape

    (3,)

    x.shape

    TensorShape([3])

通常，"维度"这个词被过度使用，既表示轴的数量，也表示沿特定轴的长度。为避免这种混淆，我们使用 _阶_（order）来表示轴的数量，而 _维度_（dimensionality）专门用于表示分量的数量。

## 2.3.3. 矩阵（Matrices）

正如标量是 \\(0^{\textrm{th}}\\) 阶张量，向量是 \\(1^{\textrm{st}}\\) 阶张量，矩阵是 \\(2^{\textrm{nd}}\\) 阶张量。我们用粗体大写字母（例如 \\(\mathbf{X}\\)、\\(\mathbf{Y}\\) 和 \\(\mathbf{Z}\\)）表示矩阵，并在代码中用具有两个轴的张量表示它们。表达式 \\(\mathbf{A} \in \mathbb{R}^{m \times n}\\) 表示矩阵 \\(\mathbf{A}\\) 包含 \\(m \times n\\) 个实值标量，排列为 \\(m\\) 行和 \\(n\\) 列。当 \\(m = n\\) 时，我们说矩阵是 _方阵_（square）。在视觉上，我们可以将任何矩阵表示为表格。要引用单个元素，我们对行和列索引都使用下标，例如 \\(a_{ij}\\) 是属于 \\(\mathbf{A}\\) 第 \\(i^{\textrm{th}}\\) 行和第 \\(j^{\textrm{th}}\\) 列的值：

(2.3.2)\\[\begin{split}\mathbf{A}=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\\ a_{21} & a_{22} & \cdots & a_{2n} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{m1} & a_{m2} & \cdots & a_{mn} \\\ \end{bmatrix}.\end{split}\\]

在代码中，我们用形状为 (\\(m\\), \\(n\\)) 的 \\(2^{\textrm{nd}}\\) 阶张量表示矩阵 \\(\mathbf{A} \in \mathbb{R}^{m \times n}\\)。我们可以通过将所需形状传递给 `reshape` 来将任何适当大小的 \\(m \times n\\) 张量转换为 \\(m \times n\\) 矩阵：

    A = torch.arange(6).reshape(3, 2)
    A

    tensor([[0, 1],
            [2, 3],
            [4, 5]])

    A = np.arange(6).reshape(3, 2)
    A

    array([[0., 1.],
           [2., 3.],
           [4., 5.]])

    A = jnp.arange(6).reshape(3, 2)
    A

    Array([[0, 1],
           [2, 3],
           [4, 5]], dtype=int32)

    A = tf.reshape(tf.range(6), (3, 2))
    A

    <tf.Tensor: shape=(3, 2), dtype=int32, numpy=
    array([[0, 1],
           [2, 3],
           [4, 5]], dtype=int32)>

有时我们想要翻转轴。当我们交换矩阵的行和列时，结果称为其 _转置_（transpose）。从形式上讲，我们用 \\(\mathbf{A}^\top\\) 表示矩阵 \\(\mathbf{A}\\) 的转置，如果 \\(\mathbf{B} = \mathbf{A}^\top\\)，则对所有 \\(i\\) 和 \\(j\\) 有 \\(b_{ij} = a_{ji}\\)。因此，\\(m \times n\\) 矩阵的转置是 \\(n \times m\\) 矩阵：

(2.3.3)\\[\begin{split}\mathbf{A}^\top = \begin{bmatrix} a_{11} & a_{21} & \dots & a_{m1} \\\ a_{12} & a_{22} & \dots & a_{m2} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{1n} & a_{2n} & \dots & a_{mn} \end{bmatrix}.\end{split}\\]

在代码中，我们可以如下访问任何矩阵的转置：

    A.T

    tensor([[0, 2, 4],
            [1, 3, 5]])

    A.T

    array([[0., 2., 4.],
           [1., 3., 5.]])

    A.T

    Array([[0, 2, 4],
           [1, 3, 5]], dtype=int32)

    tf.transpose(A)

    <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
    array([[0, 2, 4],
           [1, 3, 5]], dtype=int32)>

对称矩阵（symmetric matrices）是等于自身转置的方阵的子集：\\(\mathbf{A} = \mathbf{A}^\top\\)。以下矩阵是对称的：

    A = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
    A == A.T

    tensor([[True, True, True],
            [True, True, True],
            [True, True, True]])

    A = np.array([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
    A == A.T

    array([[ True,  True,  True],
           [ True,  True,  True],
           [ True,  True,  True]])

    A = jnp.array([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
    A == A.T

    Array([[ True,  True,  True],
           [ True,  True,  True],
           [ True,  True,  True]], dtype=bool)

    A = tf.constant([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
    A == tf.transpose(A)

    <tf.Tensor: shape=(3, 3), dtype=bool, numpy=
    array([[ True,  True,  True],
           [ True,  True,  True],
           [ True,  True,  True]])>

矩阵对于表示数据集非常有用。通常，行对应于各个记录，列对应于不同的属性。

## 2.3.4. 张量（Tensors）

虽然在你的机器学习之旅中，仅使用标量、向量和矩阵就可以走得很远，但最终你可能需要处理更高阶的张量。张量为我们提供了一种描述 \\(n^{\textrm{th}}\\) 阶数组扩展的通用方法。我们将 _张量类_ 的软件对象称为"张量"正是因为它们也可以有任意数量的轴。虽然将 _张量_ 一词既用于数学对象又用于其在代码中的实现可能会令人困惑，但从上下文通常可以清楚地理解我们的含义。我们用特殊字体的大写字母（例如 \\(\mathsf{X}\\)、\\(\mathsf{Y}\\) 和 \\(\mathsf{Z}\\)）表示一般张量，它们的索引机制（例如 \\(x_{ijk}\\) 和 \\([\mathsf{X}]_{1, 2i-1, 3}\\)）自然地从矩阵的索引机制继承而来。

当我们开始处理图像时，张量将变得更加重要。每张图像以 \\(3^{\textrm{rd}}\\) 阶张量的形式到达，其轴对应于高度、宽度和 _通道_（channel）。在每个空间位置，每种颜色（红色、绿色和蓝色）的强度沿通道堆叠。此外，一批图像在代码中用 \\(4^{\textrm{th}}\\) 阶张量表示，其中不同的图像沿第一个轴索引。更高阶的张量与向量和矩阵一样，通过增加形状分量的数量来构造。

    torch.arange(24).reshape(2, 3, 4)

    tensor([[[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]],

            [[12, 13, 14, 15],
             [16, 17, 18, 19],
             [20, 21, 22, 23]]])

    np.arange(24).reshape(2, 3, 4)

    array([[[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]],

           [[12., 13., 14., 15.],
            [16., 17., 18., 19.],
            [20., 21., 22., 23.]]])

    jnp.arange(24).reshape(2, 3, 4)

    Array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],

           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]], dtype=int32)

    tf.reshape(tf.range(24), (2, 3, 4))

    <tf.Tensor: shape=(2, 3, 4), dtype=int32, numpy=
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],

           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]], dtype=int32)>

## 2.3.5. 张量算术的基本性质

标量、向量、矩阵和更高阶的张量都有一些方便的性质。例如，逐元素运算（elementwise operation）产生的输出与操作数具有相同的形状。

    A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
    B = A.clone()  # 通过分配新内存将 A 的副本分配给 B
    A, A + B

    (tensor([[0., 1., 2.],
             [3., 4., 5.]]),
     tensor([[ 0.,  2.,  4.],
             [ 6.,  8., 10.]]))

    A = np.arange(6).reshape(2, 3)
    B = A.copy()  # 通过分配新内存将 A 的副本分配给 B
    A, A + B

    (array([[0., 1., 2.],
            [3., 4., 5.]]),
     array([[ 0.,  2.,  4.],
            [ 6.,  8., 10.]]))

    A = jnp.arange(6, dtype=jnp.float32).reshape(2, 3)
    B = A
    A, A + B

    (Array([[0., 1., 2.],
            [3., 4., 5.]], dtype=float32),
     Array([[ 0.,  2.,  4.],
            [ 6.,  8., 10.]], dtype=float32))

    A = tf.reshape(tf.range(6, dtype=tf.float32), (2, 3))
    B = A  # 不通过分配新内存将 A 克隆给 B
    A, A + B

    (<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
     array([[0., 1., 2.],
            [3., 4., 5.]], dtype=float32)>,
     <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
     array([[ 0.,  2.,  4.],
            [ 6.,  8., 10.]], dtype=float32)>)

两个矩阵的逐元素乘积称为它们的 _Hadamard 积_（Hadamard product）（记为 \\(\odot\\)）。我们可以写出两个矩阵 \\(\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}\\) 的 Hadamard 积的条目：

(2.3.4)\\[\begin{split}\mathbf{A} \odot \mathbf{B} = \begin{bmatrix} a_{11} b_{11} & a_{12} b_{12} & \dots & a_{1n} b_{1n} \\\ a_{21} b_{21} & a_{22} b_{22} & \dots & a_{2n} b_{2n} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{m1} b_{m1} & a_{m2} b_{m2} & \dots & a_{mn} b_{mn} \end{bmatrix}.\end{split}\\]

    A * B

    tensor([[ 0.,  1.,  4.],
            [ 9., 16., 25.]])

    A * B

    array([[ 0.,  1.,  4.],
           [ 9., 16., 25.]])

    A * B

    Array([[ 0.,  1.,  4.],
           [ 9., 16., 25.]], dtype=float32)

    A * B

    <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
    array([[ 0.,  1.,  4.],
           [ 9., 16., 25.]], dtype=float32)>

将标量与张量相加或相乘，会产生与原始张量形状相同的结果。这里，张量的每个元素都与标量相加（或相乘）。

    a = 2
    X = torch.arange(24).reshape(2, 3, 4)
    a + X, (a * X).shape

    (tensor([[[ 2,  3,  4,  5],
              [ 6,  7,  8,  9],
              [10, 11, 12, 13]],

             [[14, 15, 16, 17],
              [18, 19, 20, 21],
              [22, 23, 24, 25]]]),
     torch.Size([2, 3, 4]))

    a = 2
    X = np.arange(24).reshape(2, 3, 4)
    a + X, (a * X).shape

    (array([[[ 2.,  3.,  4.,  5.],
             [ 6.,  7.,  8.,  9.],
             [10., 11., 12., 13.]],

            [[14., 15., 16., 17.],
             [18., 19., 20., 21.],
             [22., 23., 24., 25.]]]),
     (2, 3, 4))

    a = 2
    X = jnp.arange(24).reshape(2, 3, 4)
    a + X, (a * X).shape

    (Array([[[ 2,  3,  4,  5],
             [ 6,  7,  8,  9],
             [10, 11, 12, 13]],

            [[14, 15, 16, 17],
             [18, 19, 20, 21],
             [22, 23, 24, 25]]], dtype=int32),
     (2, 3, 4))

    a = 2
    X = tf.reshape(tf.range(24), (2, 3, 4))
    a + X, (a * X).shape

    (<tf.Tensor: shape=(2, 3, 4), dtype=int32, numpy=
     array([[[ 2,  3,  4,  5],
             [ 6,  7,  8,  9],
             [10, 11, 12, 13]],

            [[14, 15, 16, 17],
             [18, 19, 20, 21],
             [22, 23, 24, 25]]], dtype=int32)>,
     TensorShape([2, 3, 4]))

## 2.3.6. 降维（Reduction）

我们常常希望计算张量元素的总和。为了表示长度为 \\(n\\) 的向量 \\(\mathbf{x}\\) 中元素的总和，我们写作 \\(\sum_{i=1}^n x_i\\)。有一个简单的函数可以做到这一点：

    x = torch.arange(3, dtype=torch.float32)
    x, x.sum()

    (tensor([0., 1., 2.]), tensor(3.))

    x = np.arange(3)
    x, x.sum()

    (array([0., 1., 2.]), array(3.))

    x = jnp.arange(3, dtype=jnp.float32)
    x, x.sum()

    (Array([0., 1., 2.], dtype=float32), Array(3., dtype=float32))

    x = tf.range(3, dtype=tf.float32)
    x, tf.reduce_sum(x)

    (<tf.Tensor: shape=(3,), dtype=float32, numpy=array([0., 1., 2.], dtype=float32)>,
     <tf.Tensor: shape=(), dtype=float32, numpy=3.0>)

为了表示任意形状张量的元素之和，我们只需对所有轴求和。例如，\\(m \times n\\) 矩阵 \\(\mathbf{A}\\) 的元素之和可以写作 \\(\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}\\)。

    A.shape, A.sum()

    (torch.Size([2, 3]), tensor(15.))

    A.shape, A.sum()

    ((2, 3), array(15.))

    A.shape, A.sum()

    ((2, 3), Array(15., dtype=float32))

    A.shape, tf.reduce_sum(A)

    (TensorShape([2, 3]), <tf.Tensor: shape=(), dtype=float32, numpy=15.0>)

默认情况下，调用求和函数会沿张量的所有轴 _降维_（reduce），最终产生一个标量。我们的库也允许指定沿哪些轴进行降维。要对行（轴 0）上的所有元素求和，我们在 `sum` 中指定 `axis=0`。由于输入矩阵沿轴 0 降维以生成输出向量，因此输出形状中缺少该轴。

    A.shape, A.sum(axis=0).shape

    (torch.Size([2, 3]), torch.Size([3]))

    A.shape, A.sum(axis=0).shape

    ((2, 3), (3,))

    A.shape, A.sum(axis=0).shape

    ((2, 3), (3,))

    A.shape, tf.reduce_sum(A, axis=0).shape

    (TensorShape([2, 3]), TensorShape([3]))

指定 `axis=1` 将通过对所有列的元素求和来缩减列维度（轴 1）。

    A.shape, A.sum(axis=1).shape

    (torch.Size([2, 3]), torch.Size([2]))

    A.shape, A.sum(axis=1).shape

    ((2, 3), (2,))

    A.shape, A.sum(axis=1).shape

    ((2, 3), (2,))

    A.shape, tf.reduce_sum(A, axis=1).shape

    (TensorShape([2, 3]), TensorShape([2]))

沿行和列对矩阵求和等同于对矩阵的所有元素求和。

    A.sum(axis=[0, 1]) == A.sum()  # 等同于 A.sum()

    tensor(True)

    A.sum(axis=[0, 1]) == A.sum()  # 等同于 A.sum()

    array(True)

    A.sum(axis=[0, 1]) == A.sum()  # 等同于 A.sum()

    Array(True, dtype=bool)

    tf.reduce_sum(A, axis=[0, 1]), tf.reduce_sum(A)  # 等同于 tf.reduce_sum(A)

    (<tf.Tensor: shape=(), dtype=float32, numpy=15.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=15.0>)

一个相关的量是 _均值_（mean），也称为 _平均值_（average）。我们通过将总和除以元素总数来计算均值。由于计算均值非常常见，因此它有一个专门的库函数，其工作方式类似于 `sum`。

    A.mean(), A.sum() / A.numel()

    (tensor(2.5000), tensor(2.5000))

    A.mean(), A.sum() / A.size

    (array(2.5), array(2.5))

    A.mean(), A.sum() / A.size

    (Array(2.5, dtype=float32), Array(2.5, dtype=float32))

    tf.reduce_mean(A), tf.reduce_sum(A) / tf.size(A).numpy()

    (<tf.Tensor: shape=(), dtype=float32, numpy=2.5>,
     <tf.Tensor: shape=(), dtype=float32, numpy=2.5>)

同样，计算均值的函数也可以沿特定轴对张量进行降维。

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (tensor([1.5000, 2.5000, 3.5000]), tensor([1.5000, 2.5000, 3.5000]))

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (array([1.5, 2.5, 3.5]), array([1.5, 2.5, 3.5]))

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (Array([1.5, 2.5, 3.5], dtype=float32), Array([1.5, 2.5, 3.5], dtype=float32))

    tf.reduce_mean(A, axis=0), tf.reduce_sum(A, axis=0) / A.shape[0]

    (<tf.Tensor: shape=(3,), dtype=float32, numpy=array([1.5, 2.5, 3.5], dtype=float32)>,
     <tf.Tensor: shape=(3,), dtype=float32, numpy=array([1.5, 2.5, 3.5], dtype=float32)>)

## 2.3.7. 非降维求和（Non-Reduction Sum）

有时，在调用求和或均值函数时保持轴数不变是有用的。这在我们想要使用广播机制时很重要。

    sum_A = A.sum(axis=1, keepdims=True)
    sum_A, sum_A.shape

    (tensor([[ 3.],
             [12.]]),
     torch.Size([2, 1]))

    sum_A = A.sum(axis=1, keepdims=True)
    sum_A, sum_A.shape

    (array([[ 3.],
            [12.]]),
     (2, 1))

    sum_A = A.sum(axis=1, keepdims=True)
    sum_A, sum_A.shape

    (Array([[ 3.],
            [12.]], dtype=float32),
     (2, 1))

    sum_A = tf.reduce_sum(A, axis=1, keepdims=True)
    sum_A, sum_A.shape

    (<tf.Tensor: shape=(2, 1), dtype=float32, numpy=
     array([[ 3.],
            [12.]], dtype=float32)>,
     TensorShape([2, 1]))

例如，由于 `sum_A` 在对每行求和后保持了两个轴，我们可以通过广播将 `A` 除以 `sum_A`，创建一个每行之和为 \\(1\\) 的矩阵。

    A / sum_A

    tensor([[0.0000, 0.3333, 0.6667],
            [0.2500, 0.3333, 0.4167]])

    A / sum_A

    array([[0.        , 0.33333334, 0.6666667 ],
           [0.25      , 0.33333334, 0.41666666]])

    A / sum_A

    Array([[0.        , 0.33333334, 0.6666667 ],
           [0.25      , 0.33333334, 0.41666666]], dtype=float32)

    A / sum_A

    <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
    array([[0.        , 0.33333334, 0.6666667 ],
           [0.25      , 0.33333334, 0.41666666]], dtype=float32)>

如果我们想沿某个轴（如 `axis=0`）计算 `A` 元素的累积和（cumulative sum），我们可以调用 `cumsum` 函数。在设计上，这个函数不会沿任何轴对输入张量进行降维。

    A.cumsum(axis=0)

    tensor([[0., 1., 2.],
            [3., 5., 7.]])

    A.cumsum(axis=0)

    array([[0., 1., 2.],
           [3., 5., 7.]])

    A.cumsum(axis=0)

    Array([[0., 1., 2.],
           [3., 5., 7.]], dtype=float32)

    tf.cumsum(A, axis=0)

    <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
    array([[0., 1., 2.],
           [3., 5., 7.]], dtype=float32)>

## 2.3.8. 点积（Dot Products）

到目前为止，我们只执行了逐元素运算、求和和均值运算。如果这就是我们能做的全部，线性代数就不值得拥有自己的章节了。幸运的是，事情从这里开始变得更加有趣。最基本的运算之一是点积。给定两个向量 \\(\mathbf{x}, \mathbf{y} \in \mathbb{R}^d\\)，它们的 _点积_ \\(\mathbf{x}^\top \mathbf{y}\\)（也称为 _内积_，\\(\langle \mathbf{x}, \mathbf{y} \rangle\\)）是对相同位置元素乘积的求和：\\(\mathbf{x}^\top \mathbf{y} = \sum_{i=1}^{d} x_i y_i\\)。

    y = torch.ones(3, dtype = torch.float32)
    x, y, torch.dot(x, y)

    (tensor([0., 1., 2.]), tensor([1., 1., 1.]), tensor(3.))

    y = np.ones(3)
    x, y, np.dot(x, y)

    (array([0., 1., 2.]), array([1., 1., 1.]), array(3.))

    y = jnp.ones(3, dtype = jnp.float32)
    x, y, jnp.dot(x, y)

    (Array([0., 1., 2.], dtype=float32),
     Array([1., 1., 1.], dtype=float32),
     Array(3., dtype=float32))

    y = tf.ones(3, dtype=tf.float32)
    x, y, tf.tensordot(x, y, axes=1)

    (<tf.Tensor: shape=(3,), dtype=float32, numpy=array([0., 1., 2.], dtype=float32)>,
     <tf.Tensor: shape=(3,), dtype=float32, numpy=array([1., 1., 1.], dtype=float32)>,
     <tf.Tensor: shape=(), dtype=float32, numpy=3.0>)

等价地，我们可以通过执行逐元素乘法然后求和来计算两个向量的点积：

    torch.sum(x * y)

    tensor(3.)

    np.sum(x * y)

    array(3.)

    jnp.sum(x * y)

    Array(3., dtype=float32)

    tf.reduce_sum(x * y)

    <tf.Tensor: shape=(), dtype=float32, numpy=3.0>

点积在广泛的上下文中都很有用。例如，给定一组值，用向量 \\(\mathbf{x} \in \mathbb{R}^n\\) 表示，和一组权重，用 \\(\mathbf{w} \in \mathbb{R}^n\\) 表示，\\(\mathbf{x}\\) 中的值根据权重 \\(\mathbf{w}\\) 的加权和可以表示为点积 \\(\mathbf{x}^\top \mathbf{w}\\)。当权重非负且总和为 \\(1\\) 时（即 \\(\left(\sum_{i=1}^{n} {w_i} = 1\right)\\)），点积表示 _加权平均_。在将两个向量归一化为单位长度后，点积表示它们之间夹角的余弦。在本节后面，我们将正式介绍这种 _长度_ 的概念。

## 2.3.9. 矩阵-向量乘积（Matrix-Vector Products）

既然我们知道了如何计算点积，我们就可以开始理解 \\(m \times n\\) 矩阵 \\(\mathbf{A}\\) 和 \\(n\\) 维向量 \\(\mathbf{x}\\) 之间的 _乘积_。首先，我们将矩阵可视化为其行向量：

(2.3.5)\\[\begin{split}\mathbf{A}= \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_m \\\ \end{bmatrix},\end{split}\\]

其中每个 \\(\mathbf{a}^\top_{i} \in \mathbb{R}^n\\) 是表示矩阵 \\(\mathbf{A}\\) 第 \\(i^\textrm{th}\\) 行的行向量。

矩阵-向量乘积 \\(\mathbf{A}\mathbf{x}\\) 简单来说是一个长度为 \\(m\\) 的列向量，其第 \\(i^\textrm{th}\\) 个元素是点积 \\(\mathbf{a}^\top_i \mathbf{x}\\)：

(2.3.6)\\[\begin{split}\mathbf{A}\mathbf{x} = \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_m \\\ \end{bmatrix}\mathbf{x} = \begin{bmatrix} \mathbf{a}^\top_{1} \mathbf{x} \\\ \mathbf{a}^\top_{2} \mathbf{x} \\\ \vdots\\\ \mathbf{a}^\top_{m} \mathbf{x}\\\ \end{bmatrix}.\end{split}\\]

我们可以将与矩阵 \\(\mathbf{A}\in \mathbb{R}^{m \times n}\\) 的乘法视为将向量从 \\(\mathbb{R}^{n}\\) 投影到 \\(\mathbb{R}^{m}\\) 的变换。这些变换非常有用。例如，我们可以将旋转表示为与某些方阵的乘法。矩阵-向量乘积还描述了在给定前一层输出的情况下计算神经网络中每一层输出所涉及的关键计算。

要在代码中表示矩阵-向量乘积，我们使用 `mv` 函数。请注意，`A` 的列维度（沿轴 1 的长度）必须与 `x` 的维度（其长度）相同。Python 有一个方便的运算符 `@`，可以执行矩阵-向量和矩阵-矩阵乘积（取决于其参数）。因此我们可以写 `A@x`。

    A.shape, x.shape, torch.mv(A, x), A@x

    (torch.Size([2, 3]), torch.Size([3]), tensor([ 5., 14.]), tensor([ 5., 14.]))

要在代码中表示矩阵-向量乘积，我们使用相同的 `dot` 函数。操作根据参数类型来推断。请注意，`A` 的列维度（沿轴 1 的长度）必须与 `x` 的维度（其长度）相同。

    A.shape, x.shape, np.dot(A, x)

    ((2, 3), (3,), array([ 5., 14.]))

    A.shape, x.shape, jnp.matmul(A, x)

    ((2, 3), (3,), Array([ 5., 14.], dtype=float32))

要在代码中表示矩阵-向量乘积，我们使用 `matvec` 函数。请注意，`A` 的列维度（沿轴 1 的长度）必须与 `x` 的维度（其长度）相同。

    A.shape, x.shape, tf.linalg.matvec(A, x)

    (TensorShape([2, 3]),
     TensorShape([3]),
     <tf.Tensor: shape=(2,), dtype=float32, numpy=array([ 5., 14.], dtype=float32)>)

## 2.3.10. 矩阵-矩阵乘法（Matrix-Matrix Multiplication）

一旦你掌握了点积和矩阵-向量乘积，_矩阵-矩阵乘法_ 应该就很简单了。

假设我们有两个矩阵 \\(\mathbf{A} \in \mathbb{R}^{n \times k}\\) 和 \\(\mathbf{B} \in \mathbb{R}^{k \times m}\\)：

(2.3.7)\\[\begin{split}\mathbf{A}=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1k} \\\ a_{21} & a_{22} & \cdots & a_{2k} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{n1} & a_{n2} & \cdots & a_{nk} \\\ \end{bmatrix},\quad \mathbf{B}=\begin{bmatrix} b_{11} & b_{12} & \cdots & b_{1m} \\\ b_{21} & b_{22} & \cdots & b_{2m} \\\ \vdots & \vdots & \ddots & \vdots \\\ b_{k1} & b_{k2} & \cdots & b_{km} \\\ \end{bmatrix}.\end{split}\\]

设 \\(\mathbf{a}^\top_{i} \in \mathbb{R}^k\\) 表示矩阵 \\(\mathbf{A}\\) 第 \\(i^\textrm{th}\\) 行的行向量，设 \\(\mathbf{b}_{j} \in \mathbb{R}^k\\) 表示矩阵 \\(\mathbf{B}\\) 第 \\(j^\textrm{th}\\) 列的列向量：

(2.3.8)\\[\begin{split}\mathbf{A}= \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_n \\\ \end{bmatrix}, \quad \mathbf{B}=\begin{bmatrix} \mathbf{b}_{1} & \mathbf{b}_{2} & \cdots & \mathbf{b}_{m} \\\ \end{bmatrix}.\end{split}\\]

为了形成矩阵乘积 \\(\mathbf{C} \in \mathbb{R}^{n \times m}\\)，我们只需将每个元素 \\(c_{ij}\\) 计算为 \\(\mathbf{A}\\) 的第 \\(i^{\textrm{th}}\\) 行与 \\(\mathbf{B}\\) 的第 \\(j^{\textrm{th}}\\) 列的点积，即 \\(\mathbf{a}^\top_i \mathbf{b}_j\\)：

(2.3.9)\\[\begin{split}\mathbf{C} = \mathbf{AB} = \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_n \\\ \end{bmatrix} \begin{bmatrix} \mathbf{b}_{1} & \mathbf{b}_{2} & \cdots & \mathbf{b}_{m} \\\ \end{bmatrix} = \begin{bmatrix} \mathbf{a}^\top_{1} \mathbf{b}_1 & \mathbf{a}^\top_{1}\mathbf{b}_2& \cdots & \mathbf{a}^\top_{1} \mathbf{b}_m \\\ \mathbf{a}^\top_{2}\mathbf{b}_1 & \mathbf{a}^\top_{2} \mathbf{b}_2 & \cdots & \mathbf{a}^\top_{2} \mathbf{b}_m \\\ \vdots & \vdots & \ddots &\vdots\\\ \mathbf{a}^\top_{n} \mathbf{b}_1 & \mathbf{a}^\top_{n}\mathbf{b}_2& \cdots& \mathbf{a}^\top_{n} \mathbf{b}_m \end{bmatrix}.\end{split}\\]

我们可以将矩阵-矩阵乘法 \\(\mathbf{AB}\\) 视为执行 \\(m\\) 次矩阵-向量乘积或 \\(m \times n\\) 次点积，并将结果缝合在一起形成 \\(n \times m\\) 矩阵。在以下代码片段中，我们在 `A` 和 `B` 上执行矩阵乘法。这里，`A` 是一个有两行三列的矩阵，`B` 是一个有三行四列的矩阵。相乘后，我们得到一个两行四列的矩阵。

    B = torch.ones(3, 4)
    torch.mm(A, B), A@B

    (tensor([[ 3.,  3.,  3.,  3.],
             [12., 12., 12., 12.]]),
     tensor([[ 3.,  3.,  3.,  3.],
             [12., 12., 12., 12.]]))

    B = np.ones(shape=(3, 4))
    np.dot(A, B)

    array([[ 3.,  3.,  3.,  3.],
           [12., 12., 12., 12.]])

    B = jnp.ones((3, 4))
    jnp.matmul(A, B)

    Array([[ 3.,  3.,  3.,  3.],
           [12., 12., 12., 12.]], dtype=float32)

    B = tf.ones((3, 4), tf.float32)
    tf.matmul(A, B)

    <tf.Tensor: shape=(2, 4), dtype=float32, numpy=
    array([[ 3.,  3.,  3.,  3.],
           [12., 12., 12., 12.]], dtype=float32)>

术语 _矩阵-矩阵乘法_ 通常简化为 _矩阵乘法_（matrix multiplication），不应与 Hadamard 积混淆。

## 2.3.11. 范数（Norms）

线性代数中一些最有用的运算符是 _范数_（norms）。非正式地说，范数告诉我们向量有多 _大_。例如，\\(\ell_2\\) 范数衡量向量的（欧几里得）长度。在这里，我们使用的是与向量分量大小（而非其维度）有关的 _大小_ 概念。

范数是将向量映射到标量的函数 \\(\| \cdot \|\\)，并满足以下三个性质：

1. 给定任意向量 \\(\mathbf{x}\\)，如果我们用标量 \\(\alpha \in \mathbb{R}\\) 缩放（向量的所有元素），则其范数也相应缩放：

(2.3.10)\\[\|\alpha \mathbf{x}\| = |\alpha| \|\mathbf{x}\|.\\]

2. 对于任意向量 \\(\mathbf{x}\\) 和 \\(\mathbf{y}\\)：范数满足三角不等式：

(2.3.11)\\[\|\mathbf{x} + \mathbf{y}\| \leq \|\mathbf{x}\| + \|\mathbf{y}\|.\\]

3. 向量的范数是非负的，只有当向量为零时才为零：

(2.3.12)\\[\|\mathbf{x}\| > 0 \textrm{ 对所有 } \mathbf{x} \neq 0.\\]

许多函数都是有效的范数，不同的范数编码了不同的大小概念。我们在小学几何中学到的欧几里得范数（用于计算直角三角形的斜边）是向量元素平方和的平方根。从形式上讲，这被称为 \\(\ell_2\\) _范数_，表示为

(2.3.13)\\[\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}.\\]

方法 `norm` 计算 \\(\ell_2\\) 范数。

    u = torch.tensor([3.0, -4.0])
    torch.norm(u)

    tensor(5.)

    u = np.array([3, -4])
    np.linalg.norm(u)

    array(5.)

    u = jnp.array([3.0, -4.0])
    jnp.linalg.norm(u)

    Array(5., dtype=float32)

    u = tf.constant([3.0, -4.0])
    tf.norm(u)

    <tf.Tensor: shape=(), dtype=float32, numpy=5.0>

\\(\ell_1\\) 范数也很常见，其相关的度量称为曼哈顿距离（Manhattan distance）。根据定义，\\(\ell_1\\) 范数对向量元素的绝对值求和：

(2.3.14)\\[\|\mathbf{x}\|_1 = \sum_{i=1}^n \left|x_i \right|.\\]

与 \\(\ell_2\\) 范数相比，它对异常值不太敏感。为了计算 \\(\ell_1\\) 范数，我们将绝对值与求和操作组合。

    torch.abs(u).sum()

    tensor(7.)

    np.abs(u).sum()

    array(7.)

    jnp.linalg.norm(u, ord=1) # 等同于 jnp.abs(u).sum()

    Array(7., dtype=float32)

    tf.reduce_sum(tf.abs(u))

    <tf.Tensor: shape=(), dtype=float32, numpy=7.0>

\\(\ell_2\\) 和 \\(\ell_1\\) 范数都是更一般的 \\(\ell_p\\) _范数_ 的特殊情况：

(2.3.15)\\[\|\mathbf{x}\|_p = \left(\sum_{i=1}^n \left|x_i \right|^p \right)^{1/p}.\\]

对于矩阵来说，情况更复杂。毕竟，矩阵既可以被视为单个条目的集合，也可以被视为作用于向量并将其变换为其他向量的对象。例如，我们可以问矩阵-向量乘积 \\(\mathbf{X} \mathbf{v}\\) 相对于 \\(\mathbf{v}\\) 可以长多少。这种思路引出了所谓的 _谱范数_（spectral norm）。现在，我们介绍 _Frobenius 范数_，它更容易计算，定义为矩阵元素平方和的平方根：

(2.3.16)\\[\|\mathbf{X}\|_\textrm{F} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n x_{ij}^2}.\\]

Frobenius 范数的行为就像矩阵形状向量的 \\(\ell_2\\) 范数一样。调用以下函数将计算矩阵的 Frobenius 范数。

    torch.norm(torch.ones((4, 9)))

    tensor(6.)

    np.linalg.norm(np.ones((4, 9)))

    array(6.)

    jnp.linalg.norm(jnp.ones((4, 9)))

    Array(6., dtype=float32)

    tf.norm(tf.ones((4, 9)))

    <tf.Tensor: shape=(), dtype=float32, numpy=6.0>

虽然我们不想太过超前，但我们已经可以种下一些关于这些概念为何有用的直觉。在深度学习中，我们经常尝试解决优化问题：_最大化_ 分配给观测数据的概率；_最大化_ 与推荐模型相关的收入；_最小化_ 预测与真实观测之间的距离；_最小化_ 同一人照片表示之间的距离，同时 _最大化_ 不同人照片表示之间的距离。这些距离构成了深度学习算法的目标，通常表示为范数。

## 2.3.12. 讨论

在本节中，我们回顾了理解现代深度学习重要部分所需的所有线性代数知识。不过，线性代数还有很多内容，其中许多对机器学习很有用。例如，矩阵可以分解为因子，这些分解可以揭示真实世界数据集中的低维结构。机器学习中有整个子领域专注于使用矩阵分解及其对高阶张量的推广来发现数据集中的结构并解决预测问题。但本书专注于深度学习。我们相信，一旦你动手将机器学习应用于真实数据集，你会更倾向于学习更多数学知识。因此，虽然我们保留稍后引入更多数学知识的权利，但我们在此结束本节。

如果你渴望学习更多线性代数，有许多优秀的书籍和在线资源。对于更高级的速成课程，请考虑查看 Strang ([1993](../chapter_references/zreferences.html#id266 "Strang, G. \(1993\). Introduction to Linear Algebra. Wellesley–Cambridge Press."))、Kolter ([2008](../chapter_references/zreferences.html#id152 "Kolter, Z. \(2008\). Linear algebra review and reference. Available online: http://cs229.stanford.edu/section/cs229-linalg.pdf.")) 以及 Petersen 和 Pedersen ([2008](../chapter_references/zreferences.html#id216 "Petersen, K. B., & Pedersen, M. S. \(2008\). The Matrix Cookbook. Technical University of Denmark."))。

总结：

  * 标量、向量、矩阵和张量是线性代数中使用的基本数学对象，分别具有零个、一个、两个和任意多个轴。

  * 张量可以通过索引沿指定轴进行切片或降维（通过 `sum` 和 `mean` 等运算）。

  * 逐元素乘积称为 Hadamard 积。相比之下，点积、矩阵-向量乘积和矩阵-矩阵乘积不是逐元素运算，通常返回形状与操作数不同的对象。

  * 与 Hadamard 积相比，矩阵-矩阵乘积的计算时间要长得多（三次方而非二次方时间）。

  * 范数捕获向量（或矩阵）大小的各种概念，通常应用于两个向量的差值以衡量它们之间的距离。

  * 常见的向量范数包括 \\(\ell_1\\) 和 \\(\ell_2\\) 范数，常见的矩阵范数包括 _谱范数_ 和 _Frobenius 范数_。

## 2.3.13. 练习

1. 证明矩阵转置的转置是矩阵本身：\\((\mathbf{A}^\top)^\top = \mathbf{A}\\)。

2. 给定两个矩阵 \\(\mathbf{A}\\) 和 \\(\mathbf{B}\\)，证明加法和转置可交换：\\(\mathbf{A}^\top + \mathbf{B}^\top = (\mathbf{A} + \mathbf{B})^\top\\)。

3. 给定任意方阵 \\(\mathbf{A}\\)，\\(\mathbf{A} + \mathbf{A}^\top\\) 总是对称的吗？你能仅用前两个练习的结果证明这个结论吗？

4. 我们在本节中定义了形状为 (2, 3, 4) 的张量 `X`。`len(X)` 的输出是什么？在不实现任何代码的情况下写下你的答案，然后用代码检查你的答案。

5. 对于任意形状的张量 `X`，`len(X)` 是否总是对应于 `X` 的某个轴的长度？那是哪个轴？

6. 运行 `A / A.sum(axis=1)` 并查看结果。你能分析结果吗？

7. 在曼哈顿市中心两点之间旅行时，按坐标来说你需要覆盖的距离是多少，即按大道和街道来说？你能对角线旅行吗？

8. 考虑一个形状为 (2, 3, 4) 的张量。沿轴 0、1 和 2 的求和输出的形状是什么？

9. 将具有三个或更多轴的张量输入 `linalg.norm` 函数，并观察其输出。这个函数对任意形状的张量计算什么？

10. 考虑三个大矩阵，例如 \\(\mathbf{A} \in \mathbb{R}^{2^{10} \times 2^{16}}\\)、\\(\mathbf{B} \in \mathbb{R}^{2^{16} \times 2^{5}}\\) 和 \\(\mathbf{C} \in \mathbb{R}^{2^{5} \times 2^{14}}\\)，用高斯随机变量初始化。你想计算乘积 \\(\mathbf{A} \mathbf{B} \mathbf{C}\\)。根据你计算 \\((\mathbf{A} \mathbf{B}) \mathbf{C}\\) 还是 \\(\mathbf{A} (\mathbf{B} \mathbf{C})\\)，在内存占用和速度上是否有差异？为什么？

11. 考虑三个大矩阵，例如 \\(\mathbf{A} \in \mathbb{R}^{2^{10} \times 2^{16}}\\)、\\(\mathbf{B} \in \mathbb{R}^{2^{16} \times 2^{5}}\\) 和 \\(\mathbf{C} \in \mathbb{R}^{2^{5} \times 2^{16}}\\)。根据你计算 \\(\mathbf{A} \mathbf{B}\\) 还是 \\(\mathbf{A} \mathbf{C}^\top\\)，在速度上是否有差异？为什么？如果不克隆内存就初始化 \\(\mathbf{C} = \mathbf{B}^\top\\) 会有什么变化？为什么？

12. 考虑三个矩阵，例如 \\(\mathbf{A}, \mathbf{B}, \mathbf{C} \in \mathbb{R}^{100 \times 200}\\)。通过堆叠 \\([\mathbf{A}, \mathbf{B}, \mathbf{C}]\\) 构造一个具有三个轴的张量。维度是多少？切出第三个轴的第二个坐标以恢复 \\(\mathbf{B}\\)。检查你的答案是否正确。

[讨论](https://discuss.d2l.ai/t/31)

[讨论](https://discuss.d2l.ai/t/30)

[讨论](https://discuss.d2l.ai/t/17968)

[讨论](https://discuss.d2l.ai/t/196)

目录

  * 2.3. 线性代数
    * 2.3.1. 标量
    * 2.3.2. 向量
    * 2.3.3. 矩阵
    * 2.3.4. 张量
    * 2.3.5. 张量算术的基本性质
    * 2.3.6. 降维
    * 2.3.7. 非降维求和
    * 2.3.8. 点积
    * 2.3.9. 矩阵-向量乘积
    * 2.3.10. 矩阵-矩阵乘法
    * 2.3.11. 范数
    * 2.3.12. 讨论
    * 2.3.13. 练习
