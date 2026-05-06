# 2.1. Data Manipulation

In order to get anything done, we need some way to store and manipulate data. Generally, there are two important things we need to do with data: (i) acquire them; and (ii) process them once they are inside the computer. There is no point in acquiring data without some way to store it, so to start, let’s get our hands dirty with \\(n\\)-dimensional arrays, which we also call _tensors_. If you already know the NumPy scientific computing package, this will be a breeze. For all modern deep learning frameworks, the _tensor class_ (`ndarray` in MXNet, `Tensor` in PyTorch and TensorFlow) resembles NumPy’s `ndarray`, with a few killer features added. First, the tensor class supports automatic differentiation. Second, it leverages GPUs to accelerate numerical computation, whereas NumPy only runs on CPUs. These properties make neural networks both easy to code and fast to run.

## 2.1.1. Getting Started

To start, we import the PyTorch library. Note that the package name is `torch`.

    import torch

To start, we import the `np` (`numpy`) and `npx` (`numpy_extension`) modules from MXNet. Here, the `np` module includes functions supported by NumPy, while the `npx` module contains a set of extensions developed to empower deep learning within a NumPy-like environment. When using tensors, we almost always invoke the `set_np` function: this is for compatibility of tensor processing by other components of MXNet.

    from mxnet import np, npx

    npx.set_np()

    import jax
    from jax import numpy as jnp

To start, we import `tensorflow`. For brevity, practitioners often assign the alias `tf`.

    import tensorflow as tf

A tensor represents a (possibly multidimensional) array of numerical values. In the one-dimensional case, i.e., when only one axis is needed for the data, a tensor is called a _vector_. With two axes, a tensor is called a _matrix_. With \\(k > 2\\) axes, we drop the specialized names and just refer to the object as a \\(k^\textrm{th}\\)-_order tensor_.

PyTorch provides a variety of functions for creating new tensors prepopulated with values. For example, by invoking `arange(n)`, we can create a vector of evenly spaced values, starting at 0 (included) and ending at `n` (not included). By default, the interval size is \\(1\\). Unless otherwise specified, new tensors are stored in main memory and designated for CPU-based computation.

    x = torch.arange(12, dtype=torch.float32)
    x

    tensor([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])

Each of these values is called an _element_ of the tensor. The tensor `x` contains 12 elements. We can inspect the total number of elements in a tensor via its `numel` method.

    x.numel()

    12

MXNet provides a variety of functions for creating new tensors prepopulated with values. For example, by invoking `arange(n)`, we can create a vector of evenly spaced values, starting at 0 (included) and ending at `n` (not included). By default, the interval size is \\(1\\). Unless otherwise specified, new tensors are stored in main memory and designated for CPU-based computation.

    x = np.arange(12)
    x

    [21:58:20] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])

Each of these values is called an _element_ of the tensor. The tensor `x` contains 12 elements. We can inspect the total number of elements in a tensor via its `size` attribute.

    x.size

    12

    x = jnp.arange(12)
    x

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    Array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11], dtype=int32)

    x.size

    12

TensorFlow provides a variety of functions for creating new tensors prepopulated with values. For example, by invoking `range(n)`, we can create a vector of evenly spaced values, starting at 0 (included) and ending at `n` (not included). By default, the interval size is \\(1\\). Unless otherwise specified, new tensors are stored in main memory and designated for CPU-based computation.

    x = tf.range(12, dtype=tf.float32)
    x

    <tf.Tensor: shape=(12,), dtype=float32, numpy=
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.],
          dtype=float32)>

Each of these values is called an _element_ of the tensor. The tensor `x` contains 12 elements. We can inspect the total number of elements in a tensor via the `size` function.

    tf.size(x)

    <tf.Tensor: shape=(), dtype=int32, numpy=12>

We can access a tensor’s _shape_ (the length along each axis) by inspecting its `shape` attribute. Because we are dealing with a vector here, the `shape` contains just a single element and is identical to the size.

    x.shape

    torch.Size([12])

    x.shape

    (12,)

    x.shape

    (12,)

    x.shape

    TensorShape([12])

We can change the shape of a tensor without altering its size or values, by invoking `reshape`. For example, we can transform our vector `x` whose shape is (12,) to a matrix `X` with shape (3, 4). This new tensor retains all elements but reconfigures them into a matrix. Notice that the elements of our vector are laid out one row at a time and thus `x[3] == X[0, 3]`.

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

Note that specifying every shape component to `reshape` is redundant. Because we already know our tensor’s size, we can work out one component of the shape given the rest. For example, given a tensor of size \\(n\\) and target shape (\\(h\\), \\(w\\)), we know that \\(w = n/h\\). To automatically infer one component of the shape, we can place a `-1` for the shape component that should be inferred automatically. In our case, instead of calling `x.reshape(3, 4)`, we could have equivalently called `x.reshape(-1, 4)` or `x.reshape(3, -1)`.

Practitioners often need to work with tensors initialized to contain all 0s or 1s. We can construct a tensor with all elements set to 0 and a shape of (2, 3, 4) via the `zeros` function.

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

Similarly, we can create a tensor with all 1s by invoking `ones`.

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

We often wish to sample each element randomly (and independently) from a given probability distribution. For example, the parameters of neural networks are often initialized randomly. The following snippet creates a tensor with elements drawn from a standard Gaussian (normal) distribution with mean 0 and standard deviation 1.

    torch.randn(3, 4)

    tensor([[ 0.1351, -0.9099, -0.2028,  2.1937],
            [-0.3200, -0.7545,  0.8086, -1.8730],
            [ 0.3929,  0.4931,  0.9114, -0.7072]])

    np.random.normal(0, 1, size=(3, 4))

    array([[ 2.2122064 ,  1.1630787 ,  0.7740038 ,  0.4838046 ],
           [ 1.0434403 ,  0.29956347,  1.1839255 ,  0.15302546],
           [ 1.8917114 , -1.1688148 , -1.2347414 ,  1.5580711 ]])

    # Any call of a random function in JAX requires a key to be
    # specified, feeding the same key to a random function will
    # always result in the same sample being generated
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

Finally, we can construct tensors by supplying the exact values for each element by supplying (possibly nested) Python list(s) containing numerical literals. Here, we construct a matrix with a list of lists, where the outermost list corresponds to axis 0, and the inner list corresponds to axis 1.

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

## 2.1.2. Indexing and Slicing

As with Python lists, we can access tensor elements by indexing (starting with 0). To access an element based on its position relative to the end of the list, we can use negative indexing. Finally, we can access whole ranges of indices via slicing (e.g., `X[start:stop]`), where the returned value includes the first index (`start`) _but not the last_ (`stop`). Finally, when only one index (or slice) is specified for a \\(k^\textrm{th}\\)-order tensor, it is applied along axis 0. Thus, in the following code, `[-1]` selects the last row and `[1:3]` selects the second and third rows.

    X[-1], X[1:3]

    (tensor([ 8.,  9., 10., 11.]),
     tensor([[ 4.,  5.,  6.,  7.],
             [ 8.,  9., 10., 11.]]))

Beyond reading them, we can also _write_ elements of a matrix by specifying indices.

    X[1, 2] = 17
    X

    tensor([[ 0.,  1.,  2.,  3.],
            [ 4.,  5., 17.,  7.],
            [ 8.,  9., 10., 11.]])

    X[-1], X[1:3]

    (array([ 8.,  9., 10., 11.]),
     array([[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]]))

Beyond reading them, we can also _write_ elements of a matrix by specifying indices.

    X[1, 2] = 17
    X

    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5., 17.,  7.],
           [ 8.,  9., 10., 11.]])

    X[-1], X[1:3]

    (Array([ 8,  9, 10, 11], dtype=int32),
     Array([[ 4,  5,  6,  7],
            [ 8,  9, 10, 11]], dtype=int32))

    # JAX arrays are immutable. jax.numpy.ndarray.at index
    # update operators create a new array with the corresponding
    # modifications made
    X_new_1 = X.at[1, 2].set(17)
    X_new_1

    Array([[ 0,  1,  2,  3],
           [ 4,  5, 17,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    X[-1], X[1:3]

    (<tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 8.,  9., 10., 11.], dtype=float32)>,
     <tf.Tensor: shape=(2, 4), dtype=float32, numpy=
     array([[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]], dtype=float32)>)

`Tensors` in TensorFlow are immutable, and cannot be assigned to. `Variables` in TensorFlow are mutable containers of state that support assignments. Keep in mind that gradients in TensorFlow do not flow backwards through `Variable` assignments.

Beyond assigning a value to the entire `Variable`, we can write elements of a `Variable` by specifying indices.

    X_var = tf.Variable(X)
    X_var[1, 2].assign(9)
    X_var

    <tf.Variable 'Variable:0' shape=(3, 4) dtype=float32, numpy=
    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  9.,  7.],
           [ 8.,  9., 10., 11.]], dtype=float32)>

If we want to assign multiple elements the same value, we apply the indexing on the left-hand side of the assignment operation. For instance, `[:2, :]` accesses the first and second rows, where `:` takes all the elements along axis 1 (column). While we discussed indexing for matrices, this also works for vectors and for tensors of more than two dimensions.

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

## 2.1.3. Operations

Now that we know how to construct tensors and how to read from and write to their elements, we can begin to manipulate them with various mathematical operations. Among the most useful of these are the _elementwise_ operations. These apply a standard scalar operation to each element of a tensor. For functions that take two tensors as inputs, elementwise operations apply some standard binary operator on each pair of corresponding elements. We can create an elementwise function from any function that maps from a scalar to a scalar.

In mathematical notation, we denote such _unary_ scalar operators (taking one input) by the signature \\(f: \mathbb{R} \rightarrow \mathbb{R}\\). This just means that the function maps from any real number onto some other real number. Most standard operators, including unary ones like \\(e^x\\), can be applied elementwise.

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

Likewise, we denote _binary_ scalar operators, which map pairs of real numbers to a (single) real number via the signature \\(f: \mathbb{R}, \mathbb{R} \rightarrow \mathbb{R}\\). Given any two vectors \\(\mathbf{u}\\) and \\(\mathbf{v}\\) _of the same shape_ , and a binary operator \\(f\\), we can produce a vector \\(\mathbf{c} = F(\mathbf{u},\mathbf{v})\\) by setting \\(c_i \gets f(u_i, v_i)\\) for all \\(i\\), where \\(c_i, u_i\\), and \\(v_i\\) are the \\(i^\textrm{th}\\) elements of vectors \\(\mathbf{c}, \mathbf{u}\\), and \\(\mathbf{v}\\). Here, we produced the vector-valued \\(F: \mathbb{R}^d, \mathbb{R}^d \rightarrow \mathbb{R}^d\\) by _lifting_ the scalar function to an elementwise vector operation. The common standard arithmetic operators for addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`**`) have all been _lifted_ to elementwise operations for identically-shaped tensors of arbitrary shape.

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

In addition to elementwise computations, we can also perform linear algebraic operations, such as dot products and matrix multiplications. We will elaborate on these in [Section 2.3](linear-algebra.html#sec-linear-algebra).

We can also _concatenate_ multiple tensors, stacking them end-to-end to form a larger one. We just need to provide a list of tensors and tell the system along which axis to concatenate. The example below shows what happens when we concatenate two matrices along rows (axis 0) instead of columns (axis 1). We can see that the first output’s axis-0 length (\\(6\\)) is the sum of the two input tensors’ axis-0 lengths (\\(3 + 3\\)); while the second output’s axis-1 length (\\(8\\)) is the sum of the two input tensors’ axis-1 lengths (\\(4 + 4\\)).

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

Sometimes, we want to construct a binary tensor via _logical statements_. Take `X == Y` as an example. For each position `i, j`, if `X[i, j]` and `Y[i, j]` are equal, then the corresponding entry in the result takes value `1`, otherwise it takes value `0`.

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

Summing all the elements in the tensor yields a tensor with only one element.

    X.sum()

    tensor(66.)

    X.sum()

    array(66.)

    X.sum()

    Array(66., dtype=float32)

    tf.reduce_sum(X)

    <tf.Tensor: shape=(), dtype=float32, numpy=66.0>

## 2.1.4. Broadcasting

By now, you know how to perform elementwise binary operations on two tensors of the same shape. Under certain conditions, even when shapes differ, we can still perform elementwise binary operations by invoking the _broadcasting mechanism_. Broadcasting works according to the following two-step procedure: (i) expand one or both arrays by copying elements along axes with length 1 so that after this transformation, the two tensors have the same shape; (ii) perform an elementwise operation on the resulting arrays.

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

Since `a` and `b` are \\(3\times1\\) and \\(1\times2\\) matrices, respectively, their shapes do not match up. Broadcasting produces a larger \\(3\times2\\) matrix by replicating matrix `a` along the columns and matrix `b` along the rows before adding them elementwise.

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

## 2.1.5. Saving Memory

Running operations can cause new memory to be allocated to host results. For example, if we write `Y = X + Y`, we dereference the tensor that `Y` used to point to and instead point `Y` at the newly allocated memory. We can demonstrate this issue with Python’s `id()` function, which gives us the exact address of the referenced object in memory. Note that after we run `Y = Y + X`, `id(Y)` points to a different location. That is because Python first evaluates `Y + X`, allocating new memory for the result and then points `Y` to this new location in memory.

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

This might be undesirable for two reasons. First, we do not want to run around allocating memory unnecessarily all the time. In machine learning, we often have hundreds of megabytes of parameters and update all of them multiple times per second. Whenever possible, we want to perform these updates _in place_. Second, we might point at the same parameters from multiple variables. If we do not update in place, we must be careful to update all of these references, lest we spring a memory leak or inadvertently refer to stale parameters.

Fortunately, performing in-place operations is easy. We can assign the result of an operation to a previously allocated array `Y` by using slice notation: `Y[:] = <expression>`. To illustrate this concept, we overwrite the values of tensor `Z`, after initializing it, using `zeros_like`, to have the same shape as `Y`.

    Z = torch.zeros_like(Y)
    print('id(Z):', id(Z))
    Z[:] = X + Y
    print('id(Z):', id(Z))

    id(Z): 140381179266448
    id(Z): 140381179266448

If the value of `X` is not reused in subsequent computations, we can also use `X[:] = X + Y` or `X += Y` to reduce the memory overhead of the operation.

    before = id(X)
    X += Y
    id(X) == before

    True

Fortunately, performing in-place operations is easy. We can assign the result of an operation to a previously allocated array `Y` by using slice notation: `Y[:] = <expression>`. To illustrate this concept, we overwrite the values of tensor `Z`, after initializing it, using `zeros_like`, to have the same shape as `Y`.

    Z = np.zeros_like(Y)
    print('id(Z):', id(Z))
    Z[:] = X + Y
    print('id(Z):', id(Z))

    id(Z): 139767554095872
    id(Z): 139767554095872

If the value of `X` is not reused in subsequent computations, we can also use `X[:] = X + Y` or `X += Y` to reduce the memory overhead of the operation.

    before = id(X)
    X += Y
    id(X) == before

    True

    # JAX arrays do not allow in-place operations

`Variables` are mutable containers of state in TensorFlow. They provide a way to store your model parameters. We can assign the result of an operation to a `Variable` with `assign`. To illustrate this concept, we overwrite the values of `Variable` `Z` after initializing it, using `zeros_like`, to have the same shape as `Y`.

    Z = tf.Variable(tf.zeros_like(Y))
    print('id(Z):', id(Z))
    Z.assign(X + Y)
    print('id(Z):', id(Z))

    id(Z): 139652041257360
    id(Z): 139652041257360

Even once you store state persistently in a `Variable`, you may want to reduce your memory usage further by avoiding excess allocations for tensors that are not your model parameters. Because TensorFlow `Tensors` are immutable and gradients do not flow through `Variable` assignments, TensorFlow does not provide an explicit way to run an individual operation in-place.

However, TensorFlow provides the `tf.function` decorator to wrap computation inside of a TensorFlow graph that gets compiled and optimized before running. This allows TensorFlow to prune unused values, and to reuse prior allocations that are no longer needed. This minimizes the memory overhead of TensorFlow computations.

    @tf.function
    def computation(X, Y):
        Z = tf.zeros_like(Y)  # This unused value will be pruned out
        A = X + Y  # Allocations will be reused when no longer needed
        B = A + Y
        C = B + Y
        return C + Y

    computation(X, Y)

    <tf.Tensor: shape=(3, 4), dtype=float32, numpy=
    array([[ 8.,  9., 26., 27.],
           [24., 33., 42., 51.],
           [56., 57., 58., 59.]], dtype=float32)>

## 2.1.6. Conversion to Other Python Objects

Converting to a NumPy tensor (`ndarray`), or vice versa, is easy. The torch tensor and NumPy array will share their underlying memory, and changing one through an in-place operation will also change the other.

    A = X.numpy()
    B = torch.from_numpy(A)
    type(A), type(B)

    (numpy.ndarray, torch.Tensor)

Converting to a NumPy tensor (`ndarray`), or vice versa, is easy. The converted result does not share memory. This minor inconvenience is actually quite important: when you perform operations on the CPU or on GPUs, you do not want to halt computation, waiting to see whether the NumPy package of Python might want to be doing something else with the same chunk of memory.

    A = X.asnumpy()
    B = np.array(A)
    type(A), type(B)

    (numpy.ndarray, mxnet.numpy.ndarray)

    A = jax.device_get(X)
    B = jax.device_put(A)
    type(A), type(B)

    (numpy.ndarray, jaxlib.xla_extension.ArrayImpl)

Converting to a NumPy tensor (`ndarray`), or vice versa, is easy. The converted result does not share memory. This minor inconvenience is actually quite important: when you perform operations on the CPU or on GPUs, you do not want to halt computation, waiting to see whether the NumPy package of Python might want to be doing something else with the same chunk of memory.

    A = X.numpy()
    B = tf.constant(A)
    type(A), type(B)

    (numpy.ndarray, tensorflow.python.framework.ops.EagerTensor)

To convert a size-1 tensor to a Python scalar, we can invoke the `item` function or Python’s built-in functions.

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

## 2.1.7. Summary

The tensor class is the main interface for storing and manipulating data in deep learning libraries. Tensors provide a variety of functionalities including construction routines; indexing and slicing; basic mathematics operations; broadcasting; memory-efficient assignment; and conversion to and from other Python objects.

## 2.1.8. Exercises

  1. Run the code in this section. Change the conditional statement `X == Y` to `X < Y` or `X > Y`, and then see what kind of tensor you can get.

  2. Replace the two tensors that operate by element in the broadcasting mechanism with other shapes, e.g., 3-dimensional tensors. Is the result the same as expected?

[Discussions](https://discuss.d2l.ai/t/27)

[Discussions](https://discuss.d2l.ai/t/26)

[Discussions](https://discuss.d2l.ai/t/17966)

[Discussions](https://discuss.d2l.ai/t/187)

Table Of Contents

  * 2.1. Data Manipulation
    * 2.1.1. Getting Started
    * 2.1.2. Indexing and Slicing
    * 2.1.3. Operations
    * 2.1.4. Broadcasting
    * 2.1.5. Saving Memory
    * 2.1.6. Conversion to Other Python Objects
    * 2.1.7. Summary
    * 2.1.8. Exercises

