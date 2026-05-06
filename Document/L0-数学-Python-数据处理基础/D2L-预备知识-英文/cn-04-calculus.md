# 2.4. 微积分

长期以来，如何计算圆的面积一直是个谜。后来，在古希腊，数学家阿基米德想出了一个巧妙的方法：在圆内内接一系列顶点数递增的多边形（图 2.4.1）。对于一个有 \\(n\\) 个顶点的多边形，我们得到 \\(n\\) 个三角形。当我们更精细地划分圆时，每个三角形的高度趋近于半径 \\(r\\)。同时，它的底边趋近于 \\(2 \pi r/n\\)，因为对于大量的顶点，弧与弦的比率趋近于 1。因此，多边形的面积趋近于 \\(n \cdot r \cdot \frac{1}{2} (2 \pi r/n) = \pi r^2\\)。

![../_images/polygon-circle.svg](../_images/polygon-circle.svg)

图 2.4.1 将圆的面积作为极限过程来求解。

这种极限过程是_微分学_（differential calculus）和_积分学_（integral calculus）的根基。前者可以告诉我们如何通过操纵函数的参数来增大或减小函数值。这对我们在深度学习中面临的_优化问题_非常有用，在这些问题中，我们反复更新参数以降低损失函数。优化涉及如何将模型拟合到训练数据，而微积分是其关键前提。然而，不要忘记我们的最终目标是在_先前未见过的_数据上表现良好。这个问题称为_泛化_（generalization），将是其他章节的重点。

    %matplotlib inline
    import numpy as np
    from matplotlib_inline import backend_inline
    from d2l import torch as d2l

    %matplotlib inline
    from matplotlib_inline import backend_inline
    from mxnet import np, npx
    from d2l import mxnet as d2l

    npx.set_np()

    %matplotlib inline
    import numpy as np
    from matplotlib_inline import backend_inline
    from d2l import jax as d2l

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    %matplotlib inline
    import numpy as np
    from matplotlib_inline import backend_inline
    from d2l import tensorflow as d2l

## 2.4.1. 导数与微分

简而言之，_导数_（derivative）是函数相对于其参数变化的变化率。导数可以告诉我们，如果我们对每个参数进行无穷小量的增大或减小，损失函数会增加或减少多少。在正式术语中，对于从标量映射到标量的函数 \\(f: \mathbb{R} \rightarrow \mathbb{R}\\)，\\(f\\) 在点 \\(x\\) 处的_导数_定义为

(2.4.1)\\[f'(x) = \lim_{h \rightarrow 0} \frac{f(x+h) - f(x)}{h}.\\]

右边的项称为_极限_（limit），它告诉我们当指定变量趋近某个特定值时，表达式的值会发生什么变化。这个极限告诉我们，当我们把扰动 \\(h\\) 的大小缩小到零时，它与函数值变化 \\(f(x + h) - f(x)\\) 之间的比率趋近于什么。

当 \\(f'(x)\\) 存在时，\\(f\\) 在 \\(x\\) 处被称为_可微_（differentiable）的；当 \\(f'(x)\\) 在集合（例如区间 \\([a,b]\\)）上的所有 \\(x\\) 处都存在时，我们说 \\(f\\) 在该集合上是可微的。并非所有函数都是可微的，包括许多我们希望优化的函数，如准确率和受试者工作特征曲线下面积（AUC）。然而，由于计算损失函数的导数在几乎所有训练深度神经网络的算法中都是关键步骤，我们通常优化一个可微的_替代_函数。

我们可以将导数 \\(f'(x)\\) 解释为 \\(f(x)\\) 相对于 \\(x\\) 的_瞬时_变化率。让我们通过一个例子来培养一些直觉。定义 \\(u = f(x) = 3x^2-4x\\)。

    def f(x):
        return 3 * x ** 2 - 4 * x

    def f(x):
        return 3 * x ** 2 - 4 * x

    def f(x):
        return 3 * x ** 2 - 4 * x

    def f(x):
        return 3 * x ** 2 - 4 * x

令 \\(x=1\\)，我们看到 \\(\frac{f(x+h) - f(x)}{h}\\) 在 \\(h\\) 趋近于 \\(0\\) 时趋近于 \\(2\\)。虽然这个实验缺乏数学证明的严谨性，但我们可以快速看出确实 \\(f'(1) = 2\\)。

    for h in 10.0**np.arange(-1, -6, -1):
        print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')

    h=0.10000, numerical limit=2.30000
    h=0.01000, numerical limit=2.03000
    h=0.00100, numerical limit=2.00300
    h=0.00010, numerical limit=2.00030
    h=0.00001, numerical limit=2.00003

    for h in 10.0**np.arange(-1, -6, -1):
        print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')

    h=0.10000, numerical limit=2.30000
    h=0.01000, numerical limit=2.02999
    h=0.00100, numerical limit=2.00295
    h=0.00010, numerical limit=2.00033
    h=0.00001, numerical limit=2.00272
    [21:50:15] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    for h in 10.0**np.arange(-1, -6, -1):
        print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')

    h=0.10000, numerical limit=2.30000
    h=0.01000, numerical limit=2.03000
    h=0.00100, numerical limit=2.00300
    h=0.00010, numerical limit=2.00030
    h=0.00001, numerical limit=2.00003

    for h in 10.0**np.arange(-1, -6, -1):
        print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')

    h=0.10000, numerical limit=2.30000
    h=0.01000, numerical limit=2.03000
    h=0.00100, numerical limit=2.00300
    h=0.00010, numerical limit=2.00030
    h=0.00001, numerical limit=2.00003

导数有几种等价的符号约定。给定 \\(y = f(x)\\)，以下表达式是等价的：

(2.4.2)\\[f'(x) = y' = \frac{dy}{dx} = \frac{df}{dx} = \frac{d}{dx} f(x) = Df(x) = D_x f(x),\\]

其中符号 \\(\frac{d}{dx}\\) 和 \\(D\\) 是_微分运算符_（differentiation operator）。下面我们列出一些常见函数的导数：

(2.4.3)\\[\begin{split}\begin{aligned} \frac{d}{dx} C & = 0 && \textrm{对任意常数 $C$} \\\ \frac{d}{dx} x^n & = n x^{n-1} && \textrm{对 } n \neq 0 \\\ \frac{d}{dx} e^x & = e^x \\\ \frac{d}{dx} \ln x & = x^{-1}. \end{aligned}\end{split}\\]

由可微函数组成的函数通常本身也是可微的。以下规则在处理任意可微函数 \\(f\\) 和 \\(g\\) 以及常数 \\(C\\) 的复合时很方便。

(2.4.4)\\[\begin{split}\begin{aligned} \frac{d}{dx} [C f(x)] & = C \frac{d}{dx} f(x) && \textrm{常数倍法则} \\\ \frac{d}{dx} [f(x) + g(x)] & = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) && \textrm{加法法则} \\\ \frac{d}{dx} [f(x) g(x)] & = f(x) \frac{d}{dx} g(x) + g(x) \frac{d}{dx} f(x) && \textrm{乘法法则} \\\ \frac{d}{dx} \frac{f(x)}{g(x)} & = \frac{g(x) \frac{d}{dx} f(x) - f(x) \frac{d}{dx} g(x)}{g^2(x)} && \textrm{除法法则} \end{aligned}\end{split}\\]

利用这些法则，我们可以求 \\(3 x^2 - 4x\\) 的导数：

(2.4.5)\\[\frac{d}{dx} [3 x^2 - 4x] = 3 \frac{d}{dx} x^2 - 4 \frac{d}{dx} x = 6x - 4.\\]

代入 \\(x = 1\\) 可以看出，导数确实在该位置等于 \\(2\\)。注意导数告诉我们函数在特定位置的_斜率_（slope）。

## 2.4.2. 可视化工具

我们可以使用 `matplotlib` 库可视化函数的斜率。我们需要定义几个函数。顾名思义，`use_svg_display` 告诉 `matplotlib` 以 SVG 格式输出图形，以获得更清晰的图像。注释 `#@save` 是一个特殊修饰符，允许我们将任何函数、类或其他代码块保存到 `d2l` 包中，以便稍后可以调用它而无需重复代码，例如通过 `d2l.use_svg_display()`。

    def use_svg_display():  #@save
        """Use the svg format to display a plot in Jupyter."""
        backend_inline.set_matplotlib_formats('svg')

我们可以用 `set_figsize` 方便地设置图形大小。由于 `from matplotlib import pyplot as plt` 导入语句在 `d2l` 包中通过 `#@save` 标记过，我们可以调用 `d2l.plt`。

    def set_figsize(figsize=(3.5, 2.5)):  #@save
        """Set the figure size for matplotlib."""
        use_svg_display()
        d2l.plt.rcParams['figure.figsize'] = figsize

`set_axes` 函数可以为坐标轴关联属性，包括标签、范围和刻度。

    #@save
    def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
        """Set the axes for matplotlib."""
        axes.set_xlabel(xlabel), axes.set_ylabel(ylabel)
        axes.set_xscale(xscale), axes.set_yscale(yscale)
        axes.set_xlim(xlim),     axes.set_ylim(ylim)
        if legend:
            axes.legend(legend)
        axes.grid()

有了这三个函数，我们可以定义一个 `plot` 函数来叠加多条曲线。这里的大部分代码只是为了确保输入的大小和形状匹配。

    #@save
    def plot(X, Y=None, xlabel=None, ylabel=None, legend=[], xlim=None,
             ylim=None, xscale='linear', yscale='linear',
             fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
        """Plot data points."""

        def has_one_axis(X):  # True if X (tensor or list) has 1 axis
            return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                    and not hasattr(X[0], "__len__"))

        if has_one_axis(X): X = [X]
        if Y is None:
            X, Y = [[]] * len(X), X
        elif has_one_axis(Y):
            Y = [Y]
        if len(X) != len(Y):
            X = X * len(Y)

        set_figsize(figsize)
        if axes is None:
            axes = d2l.plt.gca()
        axes.cla()
        for x, y, fmt in zip(X, Y, fmts):
            axes.plot(x,y,fmt) if len(x) else axes.plot(y,fmt)
        set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

现在我们可以绘制函数 \\(u = f(x)\\) 及其在 \\(x=1\\) 处的切线 \\(y = 2x - 3\\)，其中系数 \\(2\\) 是切线的斜率。

    x = np.arange(0, 3, 0.1)
    plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

![../_images/output_calculus_7e7694_56_0.svg](../_images/output_calculus_7e7694_56_0.svg)

    x = np.arange(0, 3, 0.1)
    plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

![../_images/output_calculus_7e7694_59_0.svg](../_images/output_calculus_7e7694_59_0.svg)

    x = np.arange(0, 3, 0.1)
    plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

![../_images/output_calculus_7e7694_62_0.svg](../_images/output_calculus_7e7694_62_0.svg)

    x = np.arange(0, 3, 0.1)
    plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

![../_images/output_calculus_7e7694_65_0.svg](../_images/output_calculus_7e7694_65_0.svg)

## 2.4.3. 偏导数与梯度

到目前为止，我们一直在对只有一个变量的函数求微分。在深度学习中，我们还需要处理具有_多个_变量的函数。我们简要介绍适用于此类_多元_（multivariate）函数的导数概念。

令 \\(y = f(x_1, x_2, \ldots, x_n)\\) 是一个具有 \\(n\\) 个变量的函数。\\(y\\) 关于其第 \\(i\\) 个参数 \\(x_i\\) 的_偏导数_（partial derivative）为

(2.4.6)\\[\frac{\partial y}{\partial x_i} = \lim_{h \rightarrow 0} \frac{f(x_1, \ldots, x_{i-1}, x_i+h, x_{i+1}, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}.\\]

为了计算 \\(\frac{\partial y}{\partial x_i}\\)，我们可以将 \\(x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n\\) 视为常数，并计算 \\(y\\) 关于 \\(x_i\\) 的导数。偏导数的以下符号约定都很常见，且含义相同：

(2.4.7)\\[\frac{\partial y}{\partial x_i} = \frac{\partial f}{\partial x_i} = \partial_{x_i} f = \partial_i f = f_{x_i} = f_i = D_i f = D_{x_i} f.\\]

我们可以将多元函数关于其所有变量的偏导数连接起来，得到一个称为该函数_梯度_（gradient）的向量。假设函数 \\(f: \mathbb{R}^n \rightarrow \mathbb{R}\\) 的输入是 \\(n\\) 维向量 \\(\mathbf{x} = [x_1, x_2, \ldots, x_n]^\top\\)，输出是标量。函数 \\(f\\) 关于 \\(\mathbf{x}\\) 的梯度是 \\(n\\) 个偏导数组成的向量：

(2.4.8)\\[\nabla_{\mathbf{x}} f(\mathbf{x}) = \left[\partial_{x_1} f(\mathbf{x}), \partial_{x_2} f(\mathbf{x}), \ldots \partial_{x_n} f(\mathbf{x})\right]^\top.\\]

在没有歧义时，\\(\nabla_{\mathbf{x}} f(\mathbf{x})\\) 通常简写为 \\(\nabla f(\mathbf{x})\\)。以下规则在对多元函数求微分时很方便：

  * 对所有 \\(\mathbf{A} \in \mathbb{R}^{m \times n}\\)，有 \\(\nabla_{\mathbf{x}} \mathbf{A} \mathbf{x} = \mathbf{A}^\top\\) 和 \\(\nabla_{\mathbf{x}} \mathbf{x}^\top \mathbf{A} = \mathbf{A}\\)。

  * 对于方阵 \\(\mathbf{A} \in \mathbb{R}^{n \times n}\\)，有 \\(\nabla_{\mathbf{x}} \mathbf{x}^\top \mathbf{A} \mathbf{x} = (\mathbf{A} + \mathbf{A}^\top)\mathbf{x}\\)，特别地，\\(\nabla_{\mathbf{x}} \|\mathbf{x} \|^2 = \nabla_{\mathbf{x}} \mathbf{x}^\top \mathbf{x} = 2\mathbf{x}\\)。

类似地，对于任何矩阵 \\(\mathbf{X}\\)，有 \\(\nabla_{\mathbf{X}} \|\mathbf{X} \|_\textrm{F}^2 = 2\mathbf{X}\\)。

## 2.4.4. 链式法则

在深度学习中，关注的梯度通常很难计算，因为我们处理的是深度嵌套的函数（函数的函数……）。幸运的是，_链式法则_（chain rule）可以解决这个问题。回到单变量函数，假设 \\(y = f(g(x))\\)，且底层函数 \\(y=f(u)\\) 和 \\(u=g(x)\\) 都是可微的。链式法则表明

(2.4.9)\\[\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}.\\]

回到多元函数，假设 \\(y = f(\mathbf{u})\\) 有变量 \\(u_1, u_2, \ldots, u_m\\)，其中每个 \\(u_i = g_i(\mathbf{x})\\) 有变量 \\(x_1, x_2, \ldots, x_n\\)，即 \\(\mathbf{u} = g(\mathbf{x})\\)。那么链式法则表明

(2.4.10)\\[\frac{\partial y}{\partial x_{i}} = \frac{\partial y}{\partial u_{1}} \frac{\partial u_{1}}{\partial x_{i}} + \frac{\partial y}{\partial u_{2}} \frac{\partial u_{2}}{\partial x_{i}} + \ldots + \frac{\partial y}{\partial u_{m}} \frac{\partial u_{m}}{\partial x_{i}} \ \textrm{ 因此 } \ \nabla_{\mathbf{x}} y = \mathbf{A} \nabla_{\mathbf{u}} y,\\]

其中 \\(\mathbf{A} \in \mathbb{R}^{n \times m}\\) 是包含向量 \\(\mathbf{u}\\) 关于向量 \\(\mathbf{x}\\) 导数的_矩阵_。因此，计算梯度需要计算向量-矩阵乘积。这是线性代数成为构建深度学习系统不可或缺的基石的关键原因之一。

## 2.4.5. 讨论

虽然我们只是触及了一个深奥话题的表面，但一些概念已经浮现出来：首先，微分的组合规则可以例行应用，使我们能够_自动_计算梯度。这项任务不需要创造力，因此我们可以将认知能力集中在其他地方。其次，计算向量值函数的导数需要我们在从输出到输入追踪变量的依赖图时进行矩阵乘法。特别是，当我们求值函数时，这个图是_正向_遍历的，而当我们计算梯度时是_反向_遍历的。后面的章节将正式介绍反向传播，一种应用链式法则的计算过程。

从优化的角度来看，梯度使我们能够确定如何移动模型参数以降低损失，本书中使用的优化算法的每一步都需要计算梯度。

## 2.4.6. 练习

  1. 到目前为止，我们认为导数的规则是理所当然的。使用定义和极限证明以下函数的性质：（i）\\(f(x) = c\\)，（ii）\\(f(x) = x^n\\)，（iii）\\(f(x) = e^x\\) 和 （iv）\\(f(x) = \log x\\)。

  2. 同样，从基本原理出发证明乘法法则、加法法则和除法法则。

  3. 证明常数倍法则是乘法法则的特例。

  4. 计算 \\(f(x) = x^x\\) 的导数。

  5. 对于某些 \\(x\\)，\\(f'(x) = 0\\) 意味着什么？给出一个函数 \\(f\\) 和位置 \\(x\\) 的例子，使这种情况成立。

  6. 绘制函数 \\(y = f(x) = x^3 - \frac{1}{x}\\) 及其在 \\(x = 1\\) 处的切线。

  7. 求函数 \\(f(\mathbf{x}) = 3x_1^2 + 5e^{x_2}\\) 的梯度。

  8. 函数 \\(f(\mathbf{x}) = \|\mathbf{x}\|_2\\) 的梯度是什么？当 \\(\mathbf{x} = \mathbf{0}\\) 时会发生什么？

  9. 你能写出当 \\(u = f(x, y, z)\\) 且 \\(x = x(a, b)\\)、\\(y = y(a, b)\\) 和 \\(z = z(a, b)\\) 时的链式法则吗？

  10. 给定可逆函数 \\(f(x)\\)，计算其反函数 \\(f^{-1}(x)\\) 的导数。这里有 \\(f^{-1}(f(x)) = x\\)，反过来 \\(f(f^{-1}(y)) = y\\)。提示：在推导中使用这些性质。

[Discussions](https://discuss.d2l.ai/t/33)

[Discussions](https://discuss.d2l.ai/t/32)

[Discussions](https://discuss.d2l.ai/t/17969)

[Discussions](https://discuss.d2l.ai/t/197)

目录

  * 2.4. 微积分
    * 2.4.1. 导数与微分
    * 2.4.2. 可视化工具
    * 2.4.3. 偏导数与梯度
    * 2.4.4. 链式法则
    * 2.4.5. 讨论
    * 2.4.6. 练习
