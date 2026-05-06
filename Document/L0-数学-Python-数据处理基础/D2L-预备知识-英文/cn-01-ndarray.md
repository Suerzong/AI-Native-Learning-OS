# 2.1. 数据操作

为了完成工作，我们需要某种方式来存储和操作数据。一般来说，我们需要对数据做两件重要的事情：（i）获取数据；（ii）在数据进入计算机后处理它们。如果没有存储数据的方法，获取数据就毫无意义，因此让我们先从 \\(n\\) 维数组（也称为_张量_（tensor））开始动手实践。如果你已经了解 NumPy 科学计算包，那这将轻而易举。对于所有现代深度学习框架，_张量类_（MXNet 中是 `ndarray`，PyTorch 和 TensorFlow 中是 `Tensor`）都类似于 NumPy 的 `ndarray`，并增加了一些关键特性。首先，张量类支持自动微分。其次，它利用 GPU 加速数值计算，而 NumPy 只能在 CPU 上运行。这些特性使得神经网络既易于编码又运行快速。

## 2.1.1. 入门

首先，我们导入 PyTorch 库。注意包名为 `torch`。

    import torch

首先，我们从 MXNet 导入 `np`（`numpy`）和 `npx`（`numpy_extension`）模块。其中 `np` 模块包含 NumPy 支持的函数，而 `npx` 模块包含一组扩展，用于在类似 NumPy 的环境中赋能深度学习。使用张量时，我们几乎总是调用 `set_np` 函数：这是为了与其他 MXNet 组件处理张量时的兼容性。

    from mxnet import np, npx

    npx.set_np()

    import jax
    from jax import numpy as jnp

首先，我们导入 `tensorflow`。为了简洁，从业者通常为其赋予别名 `tf`。

    import tensorflow as tf

张量表示一个（可能是多维的）数值数组。在一维情况下，即只需要一个轴来表示数据时，张量称为_向量_（vector）。对于两个轴，张量称为_矩阵_（matrix）。当 \\(k > 2\\) 个轴时，我们就不再使用专门的名称，而是将该对象称为 \\(k\\) 阶_张量_（\\(k^\textrm{th}\\)-order tensor）。

PyTorch 提供了各种用于创建预填充新张量的函数。例如，通过调用 `arange(n)`，我们可以创建一个从 0（包含）开始到 `n`（不包含）结束的均匀间隔值的向量。默认情况下，间隔大小为 \\(1\\)。除非另有指定，新张量存储在主内存中，并指定用于基于 CPU 的计算。

    x = torch.arange(12, dtype=torch.float32)
    x

    tensor([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])

每个值称为张量的一个_元素_（element）。张量 `x` 包含 12 个元素。我们可以通过 `numel` 方法检查张量中的元素总数。

    x.numel()

    12

MXNet 提供了各种用于创建预填充新张量的函数。例如，通过调用 `arange(n)`，我们可以创建一个从 0（包含）开始到 `n`（不包含）结束的均匀间隔值的向量。默认情况下，间隔大小为 \\(1\\)。除非另有指定，新张量存储在主内存中，并指定用于基于 CPU 的计算。

    x = np.arange(12)
    x

    [21:58:20] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])

每个值称为张量的一个_元素_。张量 `x` 包含 12 个元素。我们可以通过 `size` 属性检查张量中的元素总数。

    x.size

    12

    x = jnp.arange(12)
    x

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    Array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11], dtype=int32)

    x.size

    12

TensorFlow 提供了各种用于创建预填充新张量的函数。例如，通过调用 `range(n)`，我们可以创建一个从 0（包含）开始到 `n`（不包含）结束的均匀间隔值的向量。默认情况下，间隔大小为 \\(1\\)。除非另有指定，新张量存储在主内存中，并指定用于基于 CPU 的计算。

    x = tf.range(12, dtype=tf.float32)
    x

    <tf.Tensor: shape=(12,), dtype=float32, numpy=
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.],
          dtype=float32)>

每个值称为张量的一个_元素_。张量 `x` 包含 12 个元素。我们可以通过 `size` 函数检查张量中的元素总数。

    tf.size(x)

    <tf.Tensor: shape=(), dtype=int32, numpy=12>

我们可以通过检查张量的 `shape` 属性来访问其_形状_（shape）（沿每个轴的长度）。因为我们这里处理的是向量，所以 `shape` 只包含一个元素，与大小相同。

    x.shape

    torch.Size([12])

    x.shape

    (12,)

    x.shape

    (12,)

    x.shape

    TensorShape([12])

我们可以在不改变张量大小或值的情况下更改其形状，通过调用 `reshape`。例如，我们可以把形状为 (12,) 的向量 `x` 转换为形状为 (3, 4) 的矩阵 `X`。这个新张量保留了所有元素，但将它们重新配置为一个矩阵。注意，向量的元素是逐行排列的，因此 `x[3] == X[0, 3]`。

    X = x.reshape(3, 4)
    X

    tensor([[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]])

    X = x.reshape(3, 4)
    X

    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  6.,  7.],
           [ 8.,  9., 10., 11.]])

    X = x.reshape(3, 4)
    X

    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    X = tf.reshape(x, (3, 4))
    X

    <tf.Tensor: shape=(3, 4), dtype=float32, numpy=
    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  6.,  7.],
           [ 8.,  9., 10., 11.]], dtype=float32)>

注意，指定 `reshape` 的每个形状分量是冗余的。因为我们已经知道张量的大小，所以可以利用其余分量推算出一个分量。例如，给定一个大小为 \\(n\\) 的张量和目标形状 (\\(h\\), \\(w\\))，我们知道 \\(w = n/h\\)。为了自动推断形状的一个分量，我们可以用 `-1` 来表示应该被自动推断的形状分量。在我们的例子中，我们可以等价地调用 `x.reshape(-1, 4)` 或 `x.reshape(3, -1)` 来代替 `x.reshape(3, 4)`。

实践者通常需要使用初始化为全 0 或全 1 的张量。我们可以通过 `zeros` 函数创建一个所有元素都设置为 0 且形状为 (2, 3, 4) 的张量。

    torch.zeros((2, 3, 4))

    tensor([[[0., 0., 0., 0.],
             [0., 0., 0., 0.],
             [0., 0., 0., 0.]],

            [[0., 0., 0., 0.],
             [0., 0., 0., 0.],
             [0., 0., 0., 0.]]])

    np.zeros((2, 3, 4))

    array([[[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]],

           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]])

    jnp.zeros((2, 3, 4))

    Array([[[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]],

           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]], dtype=float32)

    tf.zeros((2, 3, 4))

    <tf.Tensor: shape=(2, 3, 4), dtype=float32, numpy=
    array([[[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]],

           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]], dtype=float32)>

类似地，我们可以通过调用 `ones` 创建一个全为 1 的张量。

    torch.ones((2, 3, 4))

    tensor([[[1., 1., 1., 1.],
             [1., 1., 1., 1.],
             [1., 1., 1., 1.]],

            [[1., 1., 1., 1.],
             [1., 1., 1., 1.],
             [1., 1., 1., 1.]]])

    np.ones((2, 3, 4))

    array([[[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]],

           [[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]]])

    jnp.ones((2, 3, 4))

    Array([[[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]],

           [[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]]], dtype=float32)

    tf.ones((2, 3, 4))

    <tf.Tensor: shape=(2, 3, 4), dtype=float32, numpy=
    array([[[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]],

           [[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]]], dtype=float32)>

我们通常希望从给定的概率分布中随机（且独立地）采样每个元素。例如，神经网络的参数通常会随机初始化。以下代码片段创建一个元素从均值为 0、标准差为 1 的标准高斯（正态）分布中抽取的张量。

    torch.randn(3, 4)

    tensor([[ 0.1351, -0.9099, -0.2028,  2.1937],
            [-0.3200, -0.7545,  0.8086, -1.8730],
            [ 0.3929,  0.4931,  0.9114, -0.7072]])

    np.random.normal(0, 1, size=(3, 4))

    array([[ 2.2122064 ,  1.1630787 ,  0.7740038 ,  0.4838046 ],
           [ 1.0434403 ,  0.29956347,  1.1839255 ,  0.15302546],
           [ 1.8917114 , -1.1688148 , -1.2347414 ,  1.5580711 ]])

    # JAX 中任何随机函数的调用都需要指定一个 key，
    # 给随机函数传入相同的 key 将始终产生相同的样本
    jax.random.normal(jax.random.PRNGKey(0), (3, 4))

    Array([[ 1.1901639 , -1.0996888 ,  0.44367844,  0.5984697 ],
           [-0.39189556,  0.69261974,  0.46018356, -2.068578  ],
           [-0.21438177, -0.9898306 , -0.6789304 ,  0.27362573]],      dtype=float32)

    tf.random.normal(shape=[3, 4])

    <tf.Tensor: shape=(3, 4), dtype=float32, numpy=
    array([[ 0.7826548 , -0.46305087,  0.02664557,  0.46879977],
           [ 0.7448125 , -0.3040165 ,  0.36592638,  1.3140978 ],
           [-0.2799254 , -0.5550206 ,  0.43767878,  0.80542797]],
          dtype=float32)>

最后，我们可以通过提供每个元素的精确值来构造张量，方法是提供包含数值字面量的（可能是嵌套的）Python 列表。这里，我们用一个列表的列表构造一个矩阵，其中最外层的列表对应轴 0，内部列表对应轴 1。

    torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

    tensor([[2, 1, 4, 3],
            [1, 2, 3, 4],
            [4, 3, 2, 1]])

    np.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

    array([[2., 1., 4., 3.],
           [1., 2., 3., 4.],
           [4., 3., 2., 1.]])

    jnp.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

    Array([[2, 1, 4, 3],
           [1, 2, 3, 4],
           [4, 3, 2, 1]], dtype=int32)

    tf.constant([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

    <tf.Tensor: shape=(3, 4), dtype=int32, numpy=
    array([[2, 1, 4, 3],
           [1, 2, 3, 4],
           [4, 3, 2, 1]], dtype=int32)>

## 2.1.2. 索引与切片

与 Python 列表一样，我们可以通过索引（从 0 开始）访问张量元素。要根据元素相对于列表末尾的位置来访问元素，我们可以使用负索引。最后，我们可以通过切片（例如 `X[start:stop]`）来访问索引的整个范围，其中返回值包含第一个索引（`start`）_但不包含最后一个_（`stop`）。最后，当只对 \\(k\\) 阶张量指定一个索引（或切片）时，它沿轴 0 应用。因此，在下面的代码中，`[-1]` 选择最后一行，`[1:3]` 选择第二行和第三行。

    X[-1], X[1:3]

    (tensor([ 8.,  9., 10., 11.]),
     tensor([[ 4.,  5.,  6.,  7.],
             [ 8.,  9., 10., 11.]]))

除了读取，我们还可以通过指定索引来_写入_矩阵的元素。

    X[1, 2] = 17
    X

    tensor([[ 0.,  1.,  2.,  3.],
            [ 4.,  5., 17.,  7.],
            [ 8.,  9., 10., 11.]])

    X[-1], X[1:3]

    (array([ 8.,  9., 10., 11.]),
     array([[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]]))

除了读取，我们还可以通过指定索引来_写入_矩阵的元素。

    X[1, 2] = 17
    X

    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5., 17.,  7.],
           [ 8.,  9., 10., 11.]])

    X[-1], X[1:3]

    (Array([ 8,  9, 10, 11], dtype=int32),
     Array([[ 4,  5,  6,  7],
            [ 8,  9, 10, 11]], dtype=int32))

    # JAX 数组是不可变的。jax.numpy.ndarray.at 索引
    # 更新操作符会创建一个包含相应修改的新数组
    X_new_1 = X.at[1, 2].set(17)
    X_new_1

    Array([[ 0,  1,  2,  3],
           [ 4,  5., 17,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    X[-1], X[1:3]

    (<tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 8.,  9., 10., 11.], dtype=float32)>,
     <tf.Tensor: shape=(2, 4), dtype=float32, numpy=
     array([[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]], dtype=float32)>)

TensorFlow 中的 `Tensors` 是不可变的，不能被赋值。TensorFlow 中的 `Variables` 是可变的状态容器，支持赋值。请记住，TensorFlow 中的梯度不会通过 `Variable` 赋值反向流动。

除了给整个 `Variable` 赋值外，我们还可以通过指定索引来写入 `Variable` 的元素。

    X_var = tf.Variable(X)
    X_var[1, 2].assign(9)
    X_var

    <tf.Variable 'Variable:0' shape=(3, 4) dtype=float32, numpy=
    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  9.,  7.],
           [ 8.,  9., 10., 11.]], dtype=float32)>

如果我们想为多个元素分配相同的值，我们在赋值操作的左侧应用索引。例如，`[:2, :]` 访问第一行和第二行，其中 `:` 沿着轴 1（列）选取所有元素。虽然我们讨论的是矩阵的索引，但这也适用于向量和超过两个维度的张量。

    X[:2, :] = 12
    X

    tensor([[12., 12., 12., 12.],
            [12., 12., 12., 12.],
            [ 8.,  9., 10., 11.]])

    X[:2, :] = 12
    X

    array([[12., 12., 12., 12.],
           [12., 12., 12., 12.],
           [ 8.,  9., 10., 11.]])

    X_new_2 = X_new_1.at[:2, :].set(12)
    X_new_2

    Array([[12, 12, 12, 12],
           [12, 12, 12, 12],
           [ 8,  9, 10, 11]], dtype=int32)

    X_var = tf.Variable(X)
    X_var[:2, :].assign(tf.ones(X_var[:2,:].shape, dtype=tf.float32) * 12)
    X_var

    <tf.Variable 'Variable:0' shape=(3, 4) dtype=float32, numpy=
    array([[12., 12., 12., 12.],
           [12., 12., 12., 12.],
           [ 8.,  9., 10., 11.]], dtype=float32)>

## 2.1.3. 运算

现在我们知道了如何构造张量以及如何读取和写入它们的元素，我们可以开始使用各种数学运算来操作它们了。其中最有用的是_逐元素_（elementwise）运算。这些运算将标准标量运算应用于张量的每个元素。对于以两个张量作为输入的函数，逐元素运算对每对对应元素应用一些标准二元运算符。我们可以从任何将标量映射到标量的函数创建逐元素函数。

在数学符号中，我们将这样的_一元_标量算符（接受一个输入）表示为 \\(f: \mathbb{R} \rightarrow \mathbb{R}\\)。这仅意味着该函数将任意实数映射到某个其他实数。大多数标准算符，包括像 \\(e^x\\) 这样的一元算符，都可以逐元素应用。

    torch.exp(x)

    tensor([162754.7969, 162754.7969, 162754.7969, 162754.7969, 162754.7969,
            162754.7969, 162754.7969, 162754.7969,   2980.9580,   8103.0840,
             22026.4648,  59874.1406])

    np.exp(x)

    array([1.0000000e+00, 2.7182817e+00, 7.3890562e+00, 2.0085537e+01,
           5.4598148e+01, 1.4841316e+02, 4.0342880e+02, 1.0966332e+03,
           2.9809580e+03, 8.1030840e+03, 2.2026465e+04, 5.9874141e+04])

    jnp.exp(x)

    Array([1.0000000e+00, 2.7182817e+00, 7.3890562e+00, 2.0085537e+01,
           5.4598152e+01, 1.4841316e+02, 4.0342880e+02, 1.0966332e+03,
           2.9809580e+03, 8.1030840e+03, 2.2026465e+04, 5.9874141e+04],      dtype=float32)

    tf.exp(x)

    <tf.Tensor: shape=(12,), dtype=float32, numpy=
    array([1.0000000e+00, 2.7182817e+00, 7.3890562e+00, 2.0085537e+01,
           5.4598148e+01, 1.4841316e+02, 4.0342877e+02, 1.0966332e+03,
           2.9809580e+03, 8.1030835e+03, 2.2026465e+04, 5.9874141e+04],
          dtype=float32)>

同样，我们将_二元_标量算符（将实数对映射为（单个）实数）表示为 \\(f: \mathbb{R}, \mathbb{R} \rightarrow \mathbb{R}\\)。给定任意两个_相同形状_的向量 \\(\mathbf{u}\\) 和 \\(\mathbf{v}\\)，以及一个二元算符 \\(f\\)，我们可以通过设置 \\(c_i \gets f(u_i, v_i)\\)（对所有 \\(i\\)）来产生一个向量 \\(\mathbf{c} = F(\mathbf{u},\mathbf{v})\\)，其中 \\(c_i, u_i\\) 和 \\(v_i\\) 分别是向量 \\(\mathbf{c}, \mathbf{u}\\) 和 \\(\mathbf{v}\\) 的第 \\(i\\) 个元素。这里，我们通过_提升_标量函数为逐元素向量运算，产生了向量值的 \\(F: \mathbb{R}^d, \mathbb{R}^d \rightarrow \mathbb{R}^d\\)。加法（`+`）、减法（`-`）、乘法（`*`）、除法（`/`）和幂运算（`**`）等常见标准算术运算符都已被_提升_为任意形状的同形张量的逐元素运算。

    x = torch.tensor([1.0, 2, 4, 8])
    y = torch.tensor([2, 2, 2, 2])
    x + y, x - y, x * y, x / y, x ** y

    (tensor([ 3.,  4.,  6., 10.]),
     tensor([-1.,  0.,  2.,  6.]),
     tensor([ 2.,  4.,  8., 16.]),
     tensor([0.5000, 1.0000, 2.0000, 4.0000]),
     tensor([ 1.,  4., 16., 64.]))

    x = np.array([1, 2, 4, 8])
    y = np.array([2, 2, 2, 2])
    x + y, x - y, x * y, x / y, x ** y

    (array([ 3.,  4.,  6., 10.]),
     array([-1.,  0.,  2.,  6.]),
     array([ 2.,  4.,  8., 16.]),
     array([0.5, 1. , 2. , 4. ]),
     array([ 1.,  4., 16., 64.]))

    x = jnp.array([1.0, 2, 4, 8])
    y = jnp.array([2, 2, 2, 2])
    x + y, x - y, x * y, x / y, x ** y

    (Array([ 3.,  4.,  6., 10.], dtype=float32),
     Array([-1.,  0.,  2.,  6.], dtype=float32),
     Array([ 2.,  4.,  8., 16.], dtype=float32),
     Array([0.5, 1. , 2. , 4. ], dtype=float32),
     Array([ 1.,  4., 16., 64.], dtype=float32))

    x = tf.constant([1.0, 2, 4, 8])
    y = tf.constant([2.0, 2, 2, 2])
    x + y, x - y, x * y, x / y, x ** y

    (<tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 3.,  4.,  6., 10.], dtype=float32)>,
     <tf.Tensor: shape=(4,), dtype=float32, numpy=array([-1.,  0.,  2.,  6.], dtype=float32)>,
     <tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 2.,  4.,  8., 16.], dtype=float32)>,
     <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0.5, 1. , 2. , 4. ], dtype=float32)>,
     <tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 1.,  4., 16., 64.], dtype=float32)>)

除了逐元素计算，我们还可以执行线性代数运算，如点积和矩阵乘法。我们将在 [第 2.3 节](linear-algebra.html#sec-linear-algebra)中详细介绍这些内容。

我们还可以_拼接_（concatenate）多个张量，将它们首尾相连以形成更大的张量。我们只需提供一个张量列表并告诉系统沿哪个轴拼接。下面的示例展示了当我们沿行（轴 0）而非列（轴 1）拼接两个矩阵时会发生什么。我们可以看到第一个输出的轴 0 长度（\\(6\\)）是两个输入张量轴 0 长度的和（\\(3 + 3\\)）；而第二个输出的轴 1 长度（\\(8\\)）是两个输入张量轴 1 长度的和（\\(4 + 4\\)）。

    X = torch.arange(12, dtype=torch.float32).reshape((3,4))
    Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)

    (tensor([[ 0.,  1.,  2.,  3.],
             [ 4.,  5.,  6.,  7.],
             [ 8.,  9., 10., 11.],
             [ 2.,  1.,  4.,  3.],
             [ 1.,  2.,  3.,  4.],
             [ 4.,  3.,  2.,  1.]]),
     tensor([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
             [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
             [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]]))

    X = np.arange(12).reshape(3, 4)
    Y = np.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    np.concatenate([X, Y], axis=0), np.concatenate([X, Y], axis=1)

    (array([[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.],
            [ 2.,  1.,  4.,  3.],
            [ 1.,  2.,  3.,  4.],
            [ 4.,  3.,  2.,  1.]]),
     array([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
            [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
            [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]]))

    X = jnp.arange(12, dtype=jnp.float32).reshape((3, 4))
    Y = jnp.array([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    jnp.concatenate((X, Y), axis=0), jnp.concatenate((X, Y), axis=1)

    (Array([[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.],
            [ 2.,  1.,  4.,  3.],
            [ 1.,  2.,  3.,  4.],
            [ 4.,  3.,  2.,  1.]], dtype=float32),
     Array([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
            [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
            [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]], dtype=float32))

    X = tf.reshape(tf.range(12, dtype=tf.float32), (3, 4))
    Y = tf.constant([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    tf.concat([X, Y], axis=0), tf.concat([X, Y], axis=1)

    (<tf.Tensor: shape=(6, 4), dtype=float32, numpy=
     array([[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.],
            [ 2.,  1.,  4.,  3.],
            [ 1.,  2.,  3.,  4.],
            [ 4.,  3.,  2.,  1.]], dtype=float32)>,
     <tf.Tensor: shape=(3, 8), dtype=float32, numpy=
     array([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
            [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
            [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]], dtype=float32)>)

有时，我们想通过_逻辑语句_构造二元张量。以 `X == Y` 为例。对于每个位置 `i, j`，如果 `X[i, j]` 和 `Y[i, j]` 相等，则结果中对应的条目取值为 `1`，否则为 `0`。

    X == Y

    tensor([[False,  True, False,  True],
            [False, False, False, False],
            [False, False, False, False]])

    X == Y

    array([[False,  True, False,  True],
           [False, False, False, False],
           [False, False, False, False]])

    X == Y

    Array([[False,  True, False,  True],
           [False, False, False, False],
           [False, False, False, False]], dtype=bool)

    X == Y

    <tf.Tensor: shape=(3, 4), dtype=bool, numpy=
    array([[False,  True, False,  True],
           [False, False, False, False],
           [False, False, False, False]])>

对张量中所有元素求和会产生一个只有一个元素的张量。

    X.sum()

    tensor(66.)

    X.sum()

    array(66.)

    X.sum()

    Array(66., dtype=float32)

    tf.reduce_sum(X)

    <tf.Tensor: shape=(), dtype=float32, numpy=66.0>

## 2.1.4. 广播

到目前为止，你知道了如何对两个相同形状的张量执行逐元素二元运算。在某些条件下，即使形状不同，我们仍然可以通过调用_广播机制_（broadcasting）来执行逐元素二元运算。广播机制按照以下两步进行：（i）通过沿长度为 1 的轴复制元素来扩展一个或两个数组，使变换后两个张量具有相同的形状；（ii）对结果数组执行逐元素运算。

    a = torch.arange(3).reshape((3, 1))
    b = torch.arange(2).reshape((1, 2))
    a, b

    (tensor([[0],
             [1],
             [2]]),
     tensor([[0, 1]]))

    a = np.arange(3).reshape(3, 1)
    b = np.arange(2).reshape(1, 2)
    a, b

    (array([[0.],
            [1.],
            [2.]]),
     array([[0., 1.]]))

    a = jnp.arange(3).reshape((3, 1))
    b = jnp.arange(2).reshape((1, 2))
    a, b

    (Array([[0],
            [1],
            [2]], dtype=int32),
     Array([[0, 1]], dtype=int32))

    a = tf.reshape(tf.range(3), (3, 1))
    b = tf.reshape(tf.range(2), (1, 2))
    a, b

    (<tf.Tensor: shape=(3, 1), dtype=int32, numpy=
     array([[0],
            [1],
            [2]], dtype=int32)>,
     <tf.Tensor: shape=(1, 2), dtype=int32, numpy=array([[0, 1]], dtype=int32)>)

由于 `a` 和 `b` 分别是 \\(3\times1\\) 和 \\(1\times2\\) 矩阵，它们的形状不匹配。广播通过将矩阵 `a` 沿列复制、矩阵 `b` 沿行复制，生成一个更大的 \\(3\times2\\) 矩阵，然后再逐元素相加。

    a + b

    tensor([[0, 1],
            [1, 2],
            [2, 3]])

    a + b

    array([[0., 1.],
           [1., 2.],
           [2., 3.]])

    a + b

    Array([[0, 1],
           [1, 2],
           [2, 3]], dtype=int32)

    a + b

    <tf.Tensor: shape=(3, 2), dtype=int32, numpy=
    array([[0, 1],
           [1, 2],
           [2, 3]], dtype=int32)>

## 2.1.5. 节省内存

运行操作可能会导致为结果分配新的内存。例如，如果我们写 `Y = X + Y`，我们会取消 `Y` 原来指向的张量的引用，转而将 `Y` 指向新分配的内存。我们可以用 Python 的 `id()` 函数来演示这个问题，它给我们提供了引用对象在内存中的确切地址。注意，在我们运行 `Y = Y + X` 之后，`id(Y)` 指向了不同的位置。这是因为 Python 首先计算 `Y + X`，为结果分配新的内存，然后将 `Y` 指向内存中的这个新位置。

    before = id(Y)
    Y = Y + X
    id(Y) == before

    False

    before = id(Y)
    Y = Y + X
    id(Y) == before

    False

    before = id(Y)
    Y = Y + X
    id(Y) == before

    False

    before = id(Y)
    Y = Y + X
    id(Y) == before

    False

这可能出于两个原因而不希望发生。首先，我们不希望总是不必要地到处分配内存。在机器学习中，我们通常有数百兆字节的参数，并且每秒要多次更新所有参数。只要可能，我们就希望_原地_执行这些更新。其次，我们可能有多个变量指向相同的参数。如果我们不原地更新，就必须小心地更新所有这些引用，以免造成内存泄漏或无意中引用了过时的参数。

幸运的是，执行原地操作很容易。我们可以使用切片表示法将操作的结果赋给先前分配的数组 `Y`：`Y[:] = <expression>`。为了说明这个概念，我们使用 `zeros_like`（使 `Z` 的形状与 `Y` 相同）初始化张量 `Z` 后，再覆盖其值。

    Z = torch.zeros_like(Y)
    print('id(Z):', id(Z))
    Z[:] = X + Y
    print('id(Z):', id(Z))

    id(Z): 140381179266448
    id(Z): 140381179266448

如果 `X` 的值在后续计算中不会被重用，我们也可以使用 `X[:] = X + Y` 或 `X += Y` 来减少操作的内存开销。

    before = id(X)
    X += Y
    id(X) == before

    True

幸运的是，执行原地操作很容易。我们可以使用切片表示法将操作的结果赋给先前分配的数组 `Y`：`Y[:] = <expression>`。为了说明这个概念，我们使用 `zeros_like` 初始化张量 `Z`，使其形状与 `Y` 相同，然后覆盖其值。

    Z = np.zeros_like(Y)
    print('id(Z):', id(Z))
    Z[:] = X + Y
    print('id(Z):', id(Z))

    id(Z): 139767554095872
    id(Z): 139767554095872

如果 `X` 的值在后续计算中不会被重用，我们也可以使用 `X[:] = X + Y` 或 `X += Y` 来减少操作的内存开销。

    before = id(X)
    X += Y
    id(X) == before

    True

    # JAX 数组不允许原地操作

TensorFlow 中的 `Variables` 是可变的状态容器。它们提供了一种存储模型参数的方法。我们可以用 `assign` 将操作的结果赋给 `Variable`。为了说明这个概念，我们使用 `zeros_like` 初始化 `Variable` `Z`，使其形状与 `Y` 相同，然后覆盖其值。

    Z = tf.Variable(tf.zeros_like(Y))
    print('id(Z):', id(Z))
    Z.assign(X + Y)
    print('id(Z):', id(Z))

    id(Z): 139652041257360
    id(Z): 139652041257360

即使你将状态持久地存储在 `Variable` 中，你也可能希望通过避免为不是模型参数的张量分配额外的内存来进一步减少内存使用。由于 TensorFlow 的 `Tensors` 是不可变的，并且梯度不会通过 `Variable` 赋值流动，因此 TensorFlow 没有提供显式的方式来原地执行单个操作。

然而，TensorFlow 提供了 `tf.function` 装饰器，将计算包装在 TensorFlow 图中，在运行前进行编译和优化。这使得 TensorFlow 能够剪枝未使用的值，并重用不再需要的先前分配。这最大限度地减少了 TensorFlow 计算的内存开销。

    @tf.function
    def computation(X, Y):
        Z = tf.zeros_like(Y)  # 这个未使用的值将被剪枝掉
        A = X + Y  # 当不再需要时，分配将被重用
        B = A + Y
        C = B + Y
        return C + Y

    computation(X, Y)

    <tf.Tensor: shape=(3, 4), dtype=float32, numpy=
    array([[ 8.,  9., 26., 27.],
           [24., 33., 42., 51.],
           [56., 57., 58., 59.]], dtype=float32)>

## 2.1.6. 转换为其他 Python 对象

转换为 NumPy 张量（`ndarray`）或反之亦然很容易。torch 张量和 NumPy 数组将共享它们的底层内存，通过原地操作更改其中一个也会改变另一个。

    A = X.numpy()
    B = torch.from_numpy(A)
    type(A), type(B)

    (numpy.ndarray, torch.Tensor)

转换为 NumPy 张量（`ndarray`）或反之亦然很容易。转换后的结果不共享内存。这个小麻烦实际上相当重要：当你在 CPU 或 GPU 上执行操作时，你不希望停止计算，等待查看 Python 的 NumPy 包是否想对同一块内存做其他事情。

    A = X.asnumpy()
    B = np.array(A)
    type(A), type(B)

    (numpy.ndarray, mxnet.numpy.ndarray)

    A = jax.device_get(X)
    B = jax.device_put(A)
    type(A), type(B)

    (numpy.ndarray, jaxlib.xla_extension.ArrayImpl)

转换为 NumPy 张量（`ndarray`）或反之亦然很容易。转换后的结果不共享内存。这个小麻烦实际上相当重要：当你在 CPU 或 GPU 上执行操作时，你不希望停止计算，等待查看 Python 的 NumPy 包是否想对同一块内存做其他事情。

    A = X.numpy()
    B = tf.constant(A)
    type(A), type(B)

    (numpy.ndarray, tensorflow.python.framework.ops.EagerTensor)

要将大小为 1 的张量转换为 Python 标量，我们可以调用 `item` 函数或 Python 的内置函数。

    a = torch.tensor([3.5])
    a, a.item(), float(a), int(a)

    (tensor([3.5000]), 3.5, 3.5, 3)

    a = np.array([3.5])
    a, a.item(), float(a), int(a)

    (array([3.5]), 3.5, 3.5, 3)

    a = jnp.array([3.5])
    a, a.item(), float(a), int(a)

    (Array([3.5], dtype=float32), 3.5, 3.5, 3)

    a = tf.constant([3.5]).numpy()
    a, a.item(), float(a), int(a)

    (array([3.5], dtype=float32), 3.5, 3.5, 3)

## 2.1.7. 小结

张量类是深度学习库中存储和操作数据的主要接口。张量提供了多种功能，包括构造例程、索引与切片、基本数学运算、广播、节省内存的赋值以及与其他 Python 对象的相互转换。

## 2.1.8. 练习

  1. 运行本节中的代码。将条件语句 `X == Y` 改为 `X < Y` 或 `X > Y`，看看能得到什么样的张量。

  2. 将广播机制中进行逐元素运算的两个张量替换为其他形状，例如三维张量。结果是否与预期相同？

[Discussions](https://discuss.d2l.ai/t/27)

[Discussions](https://discuss.d2l.ai/t/26)

[Discussions](https://discuss.d2l.ai/t/17966)

[Discussions](https://discuss.d2l.ai/t/187)

目录

  * 2.1. 数据操作
    * 2.1.1. 入门
    * 2.1.2. 索引与切片
    * 2.1.3. 运算
    * 2.1.4. 广播
    * 2.1.5. 节省内存
    * 2.1.6. 转换为其他 Python 对象
    * 2.1.7. 小结
    * 2.1.8. 练习
