# 2.7. Documentation

While we cannot possibly introduce every single PyTorch function and class (and the information might become outdated quickly), the [API documentation](https://pytorch.org/docs/stable/index.html) and additional [tutorials](https://pytorch.org/tutorials/beginner/basics/intro.html) and examples provide such documentation. This section provides some guidance for how to explore the PyTorch API.

    import torch

While we cannot possibly introduce every single MXNet function and class (and the information might become outdated quickly), the [API documentation](https://mxnet.apache.org/versions/1.8.0/api) and additional [tutorials](https://mxnet.apache.org/versions/1.8.0/api/python/docs/tutorials/) and examples provide such documentation. This section provides some guidance for how to explore the MXNet API.

    from mxnet import np

    import jax

While we cannot possibly introduce every single TensorFlow function and class (and the information might become outdated quickly), the [API documentation](https://www.tensorflow.org/api_docs) and additional [tutorials](https://www.tensorflow.org/tutorials) and examples provide such documentation. This section provides some guidance for how to explore the TensorFlow API.

    import tensorflow as tf

## 2.7.1. Functions and Classes in a Module

To know which functions and classes can be called in a module, we invoke the `dir` function. For instance, we can query all properties in the module for generating random numbers:

    print(dir(torch.distributions))

    ['AbsTransform', 'AffineTransform', 'Bernoulli', 'Beta', 'Binomial', 'CatTransform', 'Categorical', 'Cauchy', 'Chi2', 'ComposeTransform', 'ContinuousBernoulli', 'CorrCholeskyTransform', 'CumulativeDistributionTransform', 'Dirichlet', 'Distribution', 'ExpTransform', 'Exponential', 'ExponentialFamily', 'FisherSnedecor', 'Gamma', 'Geometric', 'Gumbel', 'HalfCauchy', 'HalfNormal', 'Independent', 'IndependentTransform', 'Kumaraswamy', 'LKJCholesky', 'Laplace', 'LogNormal', 'LogisticNormal', 'LowRankMultivariateNormal', 'LowerCholeskyTransform', 'MixtureSameFamily', 'Multinomial', 'MultivariateNormal', 'NegativeBinomial', 'Normal', 'OneHotCategorical', 'OneHotCategoricalStraightThrough', 'Pareto', 'Poisson', 'PositiveDefiniteTransform', 'PowerTransform', 'RelaxedBernoulli', 'RelaxedOneHotCategorical', 'ReshapeTransform', 'SigmoidTransform', 'SoftmaxTransform', 'SoftplusTransform', 'StackTransform', 'StickBreakingTransform', 'StudentT', 'TanhTransform', 'Transform', 'TransformedDistribution', 'Uniform', 'VonMises', 'Weibull', 'Wishart', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'bernoulli', 'beta', 'biject_to', 'binomial', 'categorical', 'cauchy', 'chi2', 'constraint_registry', 'constraints', 'continuous_bernoulli', 'dirichlet', 'distribution', 'exp_family', 'exponential', 'fishersnedecor', 'gamma', 'geometric', 'gumbel', 'half_cauchy', 'half_normal', 'identity_transform', 'independent', 'kl', 'kl_divergence', 'kumaraswamy', 'laplace', 'lkj_cholesky', 'log_normal', 'logistic_normal', 'lowrank_multivariate_normal', 'mixture_same_family', 'multinomial', 'multivariate_normal', 'negative_binomial', 'normal', 'one_hot_categorical', 'pareto', 'poisson', 'register_kl', 'relaxed_bernoulli', 'relaxed_categorical', 'studentT', 'transform_to', 'transformed_distribution', 'transforms', 'uniform', 'utils', 'von_mises', 'weibull', 'wishart']

    print(dir(np.random))

    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_mx_nd_np', 'beta', 'chisquare', 'choice', 'exponential', 'gamma', 'gumbel', 'logistic', 'lognormal', 'multinomial', 'multivariate_normal', 'normal', 'pareto', 'power', 'rand', 'randint', 'randn', 'rayleigh', 'shuffle', 'uniform', 'weibull']

    print(dir(jax.random))

    ['KeyArray', 'PRNGKey', 'PRNGKeyArray', '_PRNGKeyArray', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ball', 'bernoulli', 'beta', 'bits', 'categorical', 'cauchy', 'chisquare', 'choice', 'default_prng_impl', 'dirichlet', 'double_sided_maxwell', 'exponential', 'f', 'fold_in', 'gamma', 'generalized_normal', 'geometric', 'gumbel', 'key', 'key_data', 'laplace', 'loggamma', 'logistic', 'maxwell', 'multivariate_normal', 'normal', 'orthogonal', 'pareto', 'permutation', 'poisson', 'rademacher', 'randint', 'random_gamma_p', 'rayleigh', 'rbg_key', 'shuffle', 'split', 't', 'threefry2x32_key', 'threefry2x32_p', 'threefry_2x32', 'truncated_normal', 'typing', 'uniform', 'unsafe_rbg_key', 'wald', 'weibull_min']

    print(dir(tf.random))

    ['Algorithm', 'Generator', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_sys', 'all_candidate_sampler', 'categorical', 'create_rng_state', 'experimental', 'fixed_unigram_candidate_sampler', 'fold_in', 'gamma', 'get_global_generator', 'learned_unigram_candidate_sampler', 'log_uniform_candidate_sampler', 'normal', 'poisson', 'set_global_generator', 'set_seed', 'shuffle', 'split', 'stateless_binomial', 'stateless_categorical', 'stateless_gamma', 'stateless_normal', 'stateless_parameterized_truncated_normal', 'stateless_poisson', 'stateless_truncated_normal', 'stateless_uniform', 'truncated_normal', 'uniform', 'uniform_candidate_sampler']

Generally, we can ignore functions that start and end with `__` (special objects in Python) or functions that start with a single `_`(usually internal functions). Based on the remaining function or attribute names, we might hazard a guess that this module offers various methods for generating random numbers, including sampling from the uniform distribution (`uniform`), normal distribution (`normal`), and multinomial distribution (`multinomial`).

## 2.7.2. Specific Functions and Classes

For specific instructions on how to use a given function or class, we can invoke the `help` function. As an example, let’s explore the usage instructions for tensors’ `ones` function.

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

From the documentation, we can see that the `ones` function creates a new tensor with the specified shape and sets all the elements to the value of 1. Whenever possible, you should run a quick test to confirm your interpretation:

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

In the Jupyter notebook, we can use `?` to display the document in another window. For example, `list?` will create content that is almost identical to `help(list)`, displaying it in a new browser window. In addition, if we use two question marks, such as `list??`, the Python code implementing the function will also be displayed.

The official documentation provides plenty of descriptions and examples that are beyond this book. We emphasize important use cases that will get you started quickly with practical problems, rather than completeness of coverage. We also encourage you to study the source code of the libraries to see examples of high-quality implementations of production code. By doing this you will become a better engineer in addition to becoming a better scientist.

[Discussions](https://discuss.d2l.ai/t/39)

[Discussions](https://discuss.d2l.ai/t/38)

[Discussions](https://discuss.d2l.ai/t/17972)

[Discussions](https://discuss.d2l.ai/t/199)

Table Of Contents

  * 2.7. Documentation
    * 2.7.1. Functions and Classes in a Module
    * 2.7.2. Specific Functions and Classes

