# 2.5. 自动微分（Automatic Differentiation）

回顾[第 2.4 节](calculus.html#sec-calculus)，计算导数是我们将用来训练深度网络的所有优化算法中的关键步骤。虽然计算本身很直接，但手动推导它们可能很繁琐且容易出错，而且随着模型变得越来越复杂，这些问题只会加剧。

幸运的是，所有现代深度学习框架都通过提供 _自动微分_（automatic differentiation，通常缩写为 _autograd_）来将这项工作从我们手中接管。当我们将数据通过每个连续的函数传递时，框架会构建一个 _计算图_（computational graph），跟踪每个值如何依赖于其他值。为了计算导数，自动微分通过这个图反向应用链式法则。以这种方式应用链式法则的计算算法称为 _反向传播_（backpropagation）。

虽然 autograd 库在过去十年中成为热门关注点，但它们有着悠久的历史。事实上，最早的 autograd 参考文献可以追溯到半个世纪以前（[Wengert, 1964](../chapter_references/zreferences.html#id312 "Wengert, R. E. \(1964\). A simple automatic derivative evaluation program. Communications of the ACM, 7\(8\), 463–464.")）。现代反向传播的核心思想源于 1980 年的一篇博士论文（[Speelpenning, 1980](../chapter_references/zreferences.html#id263 "Speelpenning, B. \(1980\). Compiling fast partial derivatives of functions given by algorithms \(Doctoral dissertation\). University of Illinois at Urbana-Champaign.")），并在 1980 年代后期进一步发展（[Griewank, 1989](../chapter_references/zreferences.html#id98 "Griewank, A. \(1989\). On automatic differentiation. Mathematical Programming: Recent Developments and Applications \(pp. 83–107\). Kluwer.")）。虽然反向传播已成为计算梯度的默认方法，但它并不是唯一的选择。例如，Julia 编程语言采用前向传播（[Revels _et al._, 2016](../chapter_references/zreferences.html#id236 "Revels, J., Lubin, M., & Papamarkou, T. \(2016\). Forward-mode automatic differentiation in Julia. ArXiv:1607.07892.")）。在探索方法之前，让我们首先掌握 autograd 包。

    import torch

    from mxnet import autograd, np, npx

    npx.set_np()

    from jax import numpy as jnp

    import tensorflow as tf

## 2.5.1. 一个简单的函数

假设我们有兴趣对函数 \\(y = 2\mathbf{x}^{\top}\mathbf{x\\) 相对于列向量 \\(\mathbf{x}\\) 进行求导。首先，我们为 `x` 分配一个初始值。

    x = torch.arange(4.0)
    x

    tensor([0., 1., 2., 3.])

在计算 \\(y\\) 相对于 \\(\mathbf{x}\\) 的梯度之前，我们需要一个地方来存储它。通常，我们避免在每次求导时都分配新内存，因为深度学习需要对同一参数连续计算很多次导数，我们可能会面临内存耗尽的风险。请注意，标量值函数相对于向量 \\(\mathbf{x}\\) 的梯度是与 \\(\mathbf{x}\\) 形状相同的向量值。

    # 也可以创建 x = torch.arange(4.0, requires_grad=True)
    x.requires_grad_(True)
    x.grad  # 默认梯度为 None

    x = np.arange(4.0)
    x

    array([0., 1., 2., 3.])

在计算 \\(y\\) 相对于 \\(\mathbf{x}\\) 的梯度之前，我们需要一个地方来存储它。

    # 我们通过调用 `attach_grad` 为张量的梯度分配内存
    x.attach_grad()
    # 在我们计算相对于 `x` 的梯度后，我们可以通过 `grad` 属性访问它，其值初始化为 0
    x.grad

    array([0., 0., 0., 0.])

    x = jnp.arange(4.0)
    x

    Array([0., 1., 2., 3.], dtype=float32)

    x = tf.range(4, dtype=tf.float32)
    x

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 1., 2., 3.], dtype=float32)>

在计算 \\(y\\) 相对于 \\(\mathbf{x}\\) 的梯度之前，我们需要一个地方来存储它。

    x = tf.Variable(x)

我们现在计算 `x` 的函数并将结果分配给 `y`。

    y = 2 * torch.dot(x, x)
    y

    tensor(28., grad_fn=<MulBackward0>)

我们现在可以通过调用其 `backward` 方法来计算 `y` 相对于 `x` 的梯度。接下来，我们可以通过 `x` 的 `grad` 属性访问梯度。

    y.backward()
    x.grad

    tensor([ 0.,  4.,  8., 12.])

    # 我们的代码在 `autograd.record` 作用域内以构建计算图
    with autograd.record():
        y = 2 * np.dot(x, x)
    y

    array(28.)

我们现在可以通过调用其 `backward` 方法来计算 `y` 相对于 `x` 的梯度。接下来，我们可以通过 `x` 的 `grad` 属性访问梯度。

    y.backward()
    x.grad

    array([ 0.,  4.,  8., 12.])

    y = lambda x: 2 * jnp.dot(x, x)
    y(x)

    Array(28., dtype=float32)

我们现在可以通过 `grad` 变换来计算 `y` 相对于 `x` 的梯度。

    from jax import grad

    # `grad` 变换返回一个计算原始函数梯度的 Python 函数
    x_grad = grad(y)(x)
    x_grad

    Array([ 0.,  4.,  8., 12.], dtype=float32)

    # 将所有计算记录到磁带上
    with tf.GradientTape() as t:
        y = 2 * tf.tensordot(x, x, axes=1)
    y

    <tf.Tensor: shape=(), dtype=float32, numpy=28.0>

我们现在可以通过调用 `gradient` 方法计算 `y` 相对于 `x` 的梯度。

    x_grad = t.gradient(y, x)
    x_grad

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 0.,  4.,  8., 12.], dtype=float32)>

我们已经知道函数 \\(y = 2\mathbf{x}^{\top}\mathbf{x}\\) 相对于 \\(\mathbf{x}\\) 的梯度应该是 \\(4\mathbf{x}\\)。我们现在可以验证自动梯度计算与预期结果是否相同。

    x.grad == 4 * x

    tensor([True, True, True, True])

现在让我们计算 `x` 的另一个函数并取其梯度。请注意，PyTorch 在我们记录新梯度时不会自动重置梯度缓冲区。相反，新梯度会添加到已存储的梯度中。当我们想要优化多个目标函数的总和时，这种行为很有用。要重置梯度缓冲区，我们可以调用 `x.grad.zero_()`，如下所示：

    x.grad.zero_()  # 重置梯度
    y = x.sum()
    y.backward()
    x.grad

    tensor([1., 1., 1., 1.])

    x.grad == 4 * x

    array([ True,  True,  True,  True])

现在让我们计算 `x` 的另一个函数并取其梯度。请注意，MXNet 在我们记录新梯度时会重置梯度缓冲区。

    with autograd.record():
        y = x.sum()
    y.backward()
    x.grad  # 被新计算的梯度覆盖

    array([1., 1., 1., 1.])

    x_grad == 4 * x

    Array([ True,  True,  True,  True], dtype=bool)

    y = lambda x: x.sum()
    grad(y)(x)

    Array([1., 1., 1., 1.], dtype=float32)

    x_grad == 4 * x

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

现在让我们计算 `x` 的另一个函数并取其梯度。请注意，TensorFlow 在我们记录新梯度时会重置梯度缓冲区。

    with tf.GradientTape() as t:
        y = tf.reduce_sum(x)
    t.gradient(y, x)  # 被新计算的梯度覆盖

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([1., 1., 1., 1.], dtype=float32)>

## 2.5.2. 非标量变量的反向传播

当 `y` 是向量时，`y` 相对于向量 `x` 的导数的最自然表示是一个称为 _雅可比矩阵_（Jacobian）的矩阵，它包含 `y` 的每个分量相对于 `x` 的每个分量的偏导数。同样，对于更高阶的 `y` 和 `x`，微分的结果可能是更高阶的张量。

虽然雅可比矩阵确实出现在一些高级机器学习技术中，但更常见的是我们想要对 `y` 的每个分量相对于完整向量 `x` 的梯度求和，产生与 `x` 形状相同的向量。例如，我们经常有一个向量，表示在一批训练样本中分别计算的每个样本的损失函数值。在这里，我们只想对为每个样本单独计算的梯度求和。

由于深度学习框架对非标量张量梯度的解释方式不同，PyTorch 采取了一些步骤来避免混淆。在非标量上调用 `backward` 会引发错误，除非我们告诉 PyTorch 如何将对象缩减为标量。更正式地说，我们需要提供某个向量 \\(\mathbf{v}\\)，使得 `backward` 将计算 \\(\mathbf{v}^\top \partial_{\mathbf{x}} \mathbf{y}\\) 而不是 \\(\partial_{\mathbf{x}} \mathbf{y}\\)。接下来的部分可能令人困惑，但由于稍后会变得清晰的原因，这个参数（表示 \\(\mathbf{v}\\)）被命名为 `gradient`。更详细的描述请参阅 Yang Zhang 的 [Medium 文章](https://zhang-yang.medium.com/the-gradient-argument-in-pytorchs-backward-function-explained-by-examples-68f266950c29)。

    x.grad.zero_()
    y = x * x
    y.backward(gradient=torch.ones(len(y)))  # 更快: y.sum().backward()
    x.grad

    tensor([0., 2., 4., 6.])

MXNet 通过在计算梯度之前将所有张量缩减为标量（通过求和）来处理这个问题。换句话说，它不返回雅可比矩阵 \\(\partial_{\mathbf{x}} \mathbf{y}\\)，而是返回和的梯度 \\(\partial_{\mathbf{x}} \sum_i y_i\\)。

    with autograd.record():
        y = x * x
    y.backward()
    x.grad  # 等于 y = sum(x * x) 的梯度

    array([0., 2., 4., 6.])

    y = lambda x: x * x
    # grad 仅对标量输出函数定义
    grad(lambda x: y(x).sum())(x)

    Array([0., 2., 4., 6.], dtype=float32)

默认情况下，TensorFlow 返回和的梯度。换句话说，它不返回雅可比矩阵 \\(\partial_{\mathbf{x}} \mathbf{y}\\)，而是返回和的梯度 \\(\partial_{\mathbf{x}} \sum_i y_i\\)。

    with tf.GradientTape() as t:
        y = x * x
    t.gradient(y, x)  # 等同于 y = tf.reduce_sum(x * x)

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 2., 4., 6.], dtype=float32)>

## 2.5.3. 分离计算

有时，我们希望将某些计算移出记录的计算图。例如，假设我们使用输入创建一些辅助中间项，而我们不想对这些项计算梯度。在这种情况下，我们需要将相应的计算图从最终结果中 _分离_（detach）出来。下面的简单例子使这一点更清楚：假设我们有 `z = x * y` 和 `y = x * x`，但我们想关注 `x` 对 `z` 的 _直接_ 影响，而不是通过 `y` 传达的影响。在这种情况下，我们可以创建一个新变量 `u`，它与 `y` 具有相同的值，但其 _来源_（它是如何创建的）已被抹去。因此 `u` 在图中没有祖先，梯度不会通过 `u` 流向 `x`。例如，取 `z = x * u` 的梯度将产生结果 `u`（而不是你可能预期的 `3 * x * x`，因为 `z = x * x * x`）。

    x.grad.zero_()
    y = x * x
    u = y.detach()
    z = u * x

    z.sum().backward()
    x.grad == u

    tensor([True, True, True, True])

    with autograd.record():
        y = x * x
        u = y.detach()
        z = u * x
    z.backward()
    x.grad == u

    array([ True,  True,  True,  True])

    import jax

    y = lambda x: x * x
    # jax.lax 原语是 XLA 操作的 Python 包装器
    u = jax.lax.stop_gradient(y(x))
    z = lambda x: u * x

    grad(lambda x: z(x).sum())(x) == y(x)

    Array([ True,  True,  True,  True], dtype=bool)

    # 设置 persistent=True 以保留计算图。
    # 这允许我们多次运行 t.gradient
    with tf.GradientTape(persistent=True) as t:
        y = x * x
        u = tf.stop_gradient(y)
        z = u * x

    x_grad = t.gradient(z, x)
    x_grad == u

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

请注意，虽然此过程将 `y` 的祖先从通向 `z` 的图中分离出来，但通向 `y` 的计算图仍然存在，因此我们可以计算 `y` 相对于 `x` 的梯度。

    x.grad.zero_()
    y.sum().backward()
    x.grad == 2 * x

    tensor([True, True, True, True])

    y.backward()
    x.grad == 2 * x

    array([ True,  True,  True,  True])

    grad(lambda x: y(x).sum())(x) == 2 * x

    Array([ True,  True,  True,  True], dtype=bool)

    t.gradient(y, x) == 2 * x

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

## 2.5.4. 梯度与 Python 控制流

到目前为止，我们回顾了从输入到输出的路径通过函数（如 `z = x * x * x`）明确定义的情况。编程为我们提供了更多的计算结果自由度。例如，我们可以使结果依赖于辅助变量，或者根据中间结果进行条件选择。使用自动微分的一个好处是，即使构建函数的计算图需要通过 Python 控制流的迷宫（例如条件、循环和任意函数调用），我们仍然可以计算最终变量的梯度。为了说明这一点，请考虑以下代码片段，其中 `while` 循环的迭代次数和 `if` 语句的求值都取决于输入 `a` 的值。

    def f(a):
        b = a * 2
        while b.norm() < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while np.linalg.norm(b) < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while jnp.linalg.norm(b) < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while tf.norm(b) < 1000:
            b = b * 2
        if tf.reduce_sum(b) > 0:
            c = b
        else:
            c = 100 * b
        return c

下面，我们调用这个函数，传入一个随机值作为输入。由于输入是随机变量，我们不知道计算图会是什么形式。然而，每当我们对特定输入执行 `f(a)` 时，我们都会实现一个特定的计算图，随后可以运行 `backward`。

    a = torch.randn(size=(), requires_grad=True)
    d = f(a)
    d.backward()

    a = np.random.normal()
    a.attach_grad()
    with autograd.record():
        d = f(a)
    d.backward()

    from jax import random

    a = random.normal(random.PRNGKey(1), ())
    d = f(a)
    d_grad = grad(f)(a)

    a = tf.Variable(tf.random.normal(shape=()))
    with tf.GradientTape() as t:
        d = f(a)
    d_grad = t.gradient(d, a)
    d_grad

    <tf.Tensor: shape=(), dtype=float32, numpy=2048.0>

尽管我们的函数 `f` 为了演示目的有点刻意，但它对输入的依赖关系相当简单：它是 `a` 的 _线性_ 函数，具有分段定义的比例。因此，`f(a) / a` 是一个常量条目的向量，而且 `f(a) / a` 需要与 `f(a)` 相对于 `a` 的梯度匹配。

    a.grad == d / a

    tensor(True)

    a.grad == d / a

    array(True)

    d_grad == d / a

    Array(True, dtype=bool)

    d_grad == d / a

    <tf.Tensor: shape=(), dtype=bool, numpy=True>

动态控制流在深度学习中非常常见。例如，在处理文本时，计算图取决于输入的长度。在这些情况下，自动微分对于统计建模变得至关重要，因为事先不可能计算梯度。

## 2.5.5. 讨论

你现在已经体验到了自动微分的力量。自动高效计算导数的库的发展极大地提高了深度学习从业者的生产力，使他们能够专注于不那么琐碎的事情。此外，autograd 使我们能够设计大型模型，而对于这些模型，手动计算梯度将耗费大量时间。有趣的是，虽然我们使用 autograd 来 _优化_（optimize）模型（在统计意义上），但 autograd 库本身的 _优化_（在计算意义上）是一个对框架设计者至关重要的丰富课题。在这里，利用编译器和图操作工具以最便捷和内存高效的方式计算结果。

现在，尝试记住这些基础：(i) 将梯度附加到我们希望求导的那些变量上；(ii) 记录目标值的计算；(iii) 执行反向传播函数；(iv) 访问所得梯度。

## 2.5.6. 练习

1. 为什么二阶导数比一阶导数的计算成本高得多？

2. 运行反向传播函数后，立即再次运行它，看看会发生什么。请研究原因。

3. 在我们计算 `d` 相对于 `a` 的导数的控制流示例中，如果我们将变量 `a` 改为随机向量或矩阵会发生什么？此时，计算结果 `f(a)` 不再是标量。结果会怎样？我们如何分析这种情况？

4. 设 \\(f(x) = \sin(x)\\)。绘制 \\(f\\) 及其导数 \\(f'\\) 的图形。不要利用 \\(f'(x) = \cos(x)\\) 这一事实，而是使用自动微分来获得结果。

5. 设 \\(f(x) = ((\log x^2) \cdot \sin x) + x^{-1}\\)。写出从 \\(x\\) 到 \\(f(x)\\) 追踪结果的依赖图。

6. 使用链式法则计算上述函数的导数 \\(\frac{df}{dx}\\)，将每个项放在你之前构造的依赖图上。

7. 给定图和中间导数结果，计算梯度时你有多个选项。从 \\(x\\) 到 \\(f\\) 求值一次，从 \\(f\\) 追溯到 \\(x\\) 求值一次。从 \\(x\\) 到 \\(f\\) 的路径通常称为 _前向微分_（forward differentiation），而从 \\(f\\) 到 \\(x\\) 的路径称为反向微分（backward differentiation）。

8. 你什么时候想使用前向微分，什么时候想使用反向微分？提示：考虑所需的中间数据量、步骤并行化的能力以及涉及的矩阵和向量的大小。

[讨论](https://discuss.d2l.ai/t/35)

[讨论](https://discuss.d2l.ai/t/34)

[讨论](https://discuss.d2l.ai/t/17970)

[讨论](https://discuss.d2l.ai/t/200)

目录

  * 2.5. 自动微分
    * 2.5.1. 一个简单的函数
    * 2.5.2. 非标量变量的反向传播
    * 2.5.3. 分离计算
    * 2.5.4. 梯度与 Python 控制流
    * 2.5.5. 讨论
    * 2.5.6. 练习
