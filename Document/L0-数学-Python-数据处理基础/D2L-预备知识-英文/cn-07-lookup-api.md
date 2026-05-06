# 2.7. 查阅文档

虽然我们不可能介绍每一个 PyTorch 函数和类（而且这些信息可能很快就会过时），但 [API 文档](https://pytorch.org/docs/stable/index.html)以及额外的 [教程](https://pytorch.org/tutorials/beginner/basics/intro.html) 和示例提供了这样的文档。本节将提供一些关于如何探索 PyTorch API 的指导。

    import torch

虽然我们不可能介绍每一个 MXNet 函数和类（而且这些信息可能很快就会过时），但 [API 文档](https://mxnet.apache.org/versions/1.8.0/api)以及额外的 [教程](https://mxnet.apache.org/versions/1.8.0/api/python/docs/tutorials/) 和示例提供了这样的文档。本节将提供一些关于如何探索 MXNet API 的指导。

    from mxnet import np

    import jax

虽然我们不可能介绍每一个 TensorFlow 函数和类（而且这些信息可能很快就会过时），但 [API 文档](https://www.tensorflow.org/api_docs)以及额外的 [教程](https://www.tensorflow.org/tutorials) 和示例提供了这样的文档。本节将提供一些关于如何探索 TensorFlow API 的指导。

    import tensorflow as tf

## 2.7.1. 模块中的函数和类

要知道一个模块中可以调用哪些函数和类，我们可以调用 `dir` 函数。例如，我们可以查询生成随机数的模块中的所有属性：

    print(dir(torch.distributions)

    ['AbsTransform', 'AffineTransform', 'Bernoulli', 'Beta', 'Binomial', 'CatTransform', 'Categorical', 'Cauchy', 'Chi2', 'ComposeTransform', 'ContinuousBernoulli', 'CorrCholeskyTransform', 'CumulativeDistributionTransform', 'Dirichlet', 'Distribution', 'ExpTransform', 'Exponential', 'ExponentialFamily', 'FisherSnedecor', 'Gamma', 'Geometric', 'Gumbel', 'HalfCauchy', 'HalfNormal', 'Independent', 'IndependentTransform', 'Kumaraswamy', 'LKJCholesky', 'Laplace', 'LogNormal', 'LogisticNormal', 'LowRankMultivariateNormal', 'LowerCholeskyTransform', 'MixtureSameFamily', 'Multinomial', 'MultivariateNormal', 'NegativeBinomial', 'Normal', 'OneHotCategorical', 'OneHotCategoricalStraightThrough', 'Pareto', 'Poisson', 'PositiveDefiniteTransform', 'PowerTransform', 'RelaxedBernoulli', 'RelaxedOneHotCategorical', 'ReshapeTransform', 'SigmoidTransform', 'SoftmaxTransform', 'SoftplusTransform', 'StackTransform', 'StickBreakingTransform', 'StudentT', 'TanhTransform', 'Transform', 'TransformedDistribution', 'Uniform', 'VonMises', 'Weibull', 'Wishart', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'bernoulli', 'beta', 'biject_to', 'binomial', 'categorical', 'cauchy', 'chi2', 'constraint_registry', 'constraints', 'continuous_bernoulli', 'dirichlet', 'distribution', 'exp_family', 'exponential', 'fishersnedecor', 'gamma', 'geometric', 'gumbel', 'half_cauchy', 'half_normal', 'identity_transform', 'independent', 'kl', 'kl_divergence', 'kumaraswamy', 'laplace', 'lkj_cholesky', 'log_normal', 'logistic_normal', 'lowrank_multivariate_normal', 'mixture_same_family', 'multinomial', 'multivariate_normal', 'negative_binomial', 'normal', 'one_hot_categorical', 'pareto', 'poisson', 'register_kl', 'relaxed_bernoulli', 'relaxed_categorical', 'studentT', 'transform_to', 'transformed_distribution', 'transforms', 'uniform', 'utils', 'von_mises', 'weibull', 'wishart']

    print(dir(np.random))

    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_mx_nd_np', 'beta', 'chisquare', 'choice', 'exponential', 'gamma', 'gumbel', 'logistic', 'lognormal', 'multinomial', 'multivariate_normal', 'normal', 'pareto', 'power', 'rand', 'randint', 'randn', 'rayleigh', 'shuffle', 'uniform', 'weibull']

    print(dir(jax.random))

    ['KeyArray', 'PRNGKey', 'PRNGKeyArray', '_PRNGKeyArray', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ball', 'bernoulli', 'beta', 'bits', 'categorical', 'cauchy', 'chisquare', 'choice', 'default_prng_impl', 'dirichlet', 'double_sided_maxwell', 'exponential', 'f', 'fold_in', 'gamma', 'generalized_normal', 'geometric', 'gumbel', 'key', 'key_data', 'laplace', 'loggamma', 'logistic', 'maxwell', 'multivariate_normal', 'normal', 'orthogonal', 'pareto', 'permutation', 'poisson', 'rademacher', 'randint', 'random_gamma_p', 'rayleigh', 'rbg_key', 'shuffle', 'split', 't', 'threefry2x32_key', 'threefry2x32_p', 'threefry_2x32', 'truncated_normal', 'typing', 'uniform', 'unsafe_rbg_key', 'wald', 'weibull_min']

    print(dir(tf.random))

    ['Algorithm', 'Generator', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_sys', 'all_candidate_sampler', 'categorical', 'create_rng_state', 'experimental', 'fixed_unigram_candidate_sampler', 'fold_in', 'gamma', 'get_global_generator', 'learned_unigram_candidate_sampler', 'log_uniform_candidate_sampler', 'normal', 'poisson', 'set_global_generator', 'set_seed', 'shuffle', 'split', 'stateless_binomial', 'stateless_categorical', 'stateless_gamma', 'stateless_normal', 'stateless_parameterized_truncated_normal', 'stateless_poisson', 'stateless_truncated_normal', 'stateless_uniform', 'truncated_normal', 'uniform', 'uniform_candidate_sampler']

通常，我们可以忽略以 `__` 开头和结尾的函数（Python 中的特殊对象）或以单个 `_` 开头的函数（通常是内部函数）。根据剩余的函数或属性名称，我们可以大致猜测出该模块提供了各种生成随机数的方法，包括从均匀分布（`uniform`）、正态分布（`normal`）和多项分布（`multinomial`）中采样。

## 2.7.2. 特定函数和类

要了解如何使用特定的函数或类，我们可以调用 `help` 函数。例如，让我们探索张量的 `ones` 函数的使用说明。

    help(torch.ones)

    Help on built-in function ones in module torch:

    ones(...)
        ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) -> Tensor

        Returns a tensor filled with the scalar value 1, with the shape defined
        by the variable argument size.

        Args:
            size (int...): a sequence of integers defining the shape of the output tensor.
                Can be a variable number of arguments or a collection like a list or tuple.

        Keyword arguments:
            out (Tensor, optional): the output tensor.
            dtype (torch.dtype, optional): the desired data type of returned tensor.
                Default: if None, uses a global default (see torch.set_default_tensor_type()).
            layout (torch.layout, optional): the desired layout of returned Tensor.
                Default: torch.strided.
            device (torch.device, optional): the desired device of returned tensor.
                Default: if None, uses the current device for the default tensor type
                (see torch.set_default_tensor_type()). device will be the CPU
                for CPU tensor types and the current CUDA device for CUDA tensor types.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: False.

        Example::

            >>> torch.ones(2, 3)
            tensor([[ 1.,  1.,  1.],
                    [ 1.,  1.,  1.]])

            >>> torch.ones(5)
            tensor([ 1.,  1.,  1.,  1.,  1.])

    help(np.ones)

    Help on function ones in module mxnet.numpy:

    ones(shape, dtype=<class 'numpy.float32'>, order='C', ctx=None)
        Return a new array of given shape and type, filled with ones.
        This function currently only supports storing multi-dimensional data
        in row-major (C-style).

        Parameters
        ----------
        shape : int or tuple of int
            The shape of the empty array.
        dtype : str or numpy.dtype, optional
            An optional value type. Default is numpy.float32. Note that this
            behavior is different from NumPy's ones function where float64
            is the default value, because float32 is considered as the default
            data type in deep learning.
        order : {'C'}, optional, default: 'C'
            How to store multi-dimensional data in memory, currently only row-major
            (C-style) is supported.
        ctx : Context, optional
            An optional device context (default is the current default context).

        Returns
        -------
        out : ndarray
            Array of ones with the given shape, dtype, and ctx.

        Examples
        --------
        >>> np.ones(5)
        array([1., 1., 1., 1., 1.])

        >>> np.ones((5,), dtype=int)
        array([1, 1, 1, 1, 1], dtype=int64)

        >>> np.ones((2, 1))
        array([[1.],
               [1.]])

        >>> s = (2,2)
        >>> np.ones(s)
        array([[1., 1.],
               [1., 1.]])

    help(jax.numpy.ones)

    Help on function ones in module jax._src.numpy.lax_numpy:

    ones(shape: Any, dtype: Union[Any, str, numpy.dtype, jax._src.SupportsDType, NoneType] = None) -> jax.Array
        Return a new array of given shape and type, filled with ones.

        LAX-backend implementation of numpy.ones().

        _Original docstring below._

        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the new array, e.g., (2, 3) or 2.
        dtype : data-type, optional
            The desired data-type for the array, e.g., numpy.int8.  Default is
            numpy.float64.

        Returns
        -------
        out : ndarray
            Array of ones with the given shape, dtype, and order.

    help(tf.ones)

    Help on function ones in module tensorflow.python.ops.array_ops:

    ones(shape, dtype=tf.float32, name=None)
        Creates a tensor with all elements set to one (1).

        See also tf.ones_like, tf.zeros, tf.fill, tf.eye.

        This operation returns a tensor of type dtype with shape shape and
        all elements set to one.

        >>> tf.ones([3, 4], tf.int32)
        <tf.Tensor: shape=(3, 4), dtype=int32, numpy=
        array([[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]], dtype=int32)>

        Args:
          shape: A list of integers, a tuple of integers, or
            a 1-D Tensor of type int32.
          dtype: Optional DType of an element in the resulting Tensor. Default is
            tf.float32.
          name: Optional string. A name for the operation.

        Returns:
          A Tensor with all elements set to one (1).

从文档中我们可以看到，`ones` 函数创建一个指定形状的新张量，并将所有元素设置为 1。只要有可能，你应该运行一个快速测试来确认你的理解：

    torch.ones(4)

    tensor([1., 1., 1., 1.])

    np.ones(4)

    [22:07:42] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    array([1., 1., 1., 1.])

    jax.numpy.ones(4)

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    Array([1., 1., 1., 1.], dtype=float32)

    tf.ones(4)

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([1., 1., 1., 1.], dtype=float32)>

在 Jupyter 笔记本中，我们可以使用 `?` 在另一个窗口中显示文档。例如，`list?` 将创建与 `help(list)` 几乎相同的内容，并在新的浏览器窗口中显示。此外，如果我们使用两个问号，例如 `list??`，那么实现该函数的 Python 代码也会被显示出来。

官方文档提供了大量本书未涵盖的描述和示例。我们强调重要的用例，以便你能快速上手实际问题，而不是追求全面覆盖。我们也鼓励你研究库的源代码，以查看生产代码的高质量实现示例。通过这样做，你不仅能成为更好的科学家，还能成为更好的工程师。

[Discussions](https://discuss.d2l.ai/t/39)

[Discussions](https://discuss.d2l.ai/t/38)

[Discussions](https://discuss.d2l.ai/t/17972)

[Discussions](https://discuss.d2l.ai/t/199)

目录

  * 2.7. 查阅文档
    * 2.7.1. 模块中的函数和类
    * 2.7.2. 特定函数和类
