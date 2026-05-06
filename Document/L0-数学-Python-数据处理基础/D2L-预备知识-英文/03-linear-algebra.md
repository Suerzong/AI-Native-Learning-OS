# 2.3. Linear Algebra

By now, we can load datasets into tensors and manipulate these tensors with basic mathematical operations. To start building sophisticated models, we will also need a few tools from linear algebra. This section offers a gentle introduction to the most essential concepts, starting from scalar arithmetic and ramping up to matrix multiplication.

    import torch

    from mxnet import np, npx

    npx.set_np()

    from jax import numpy as jnp

    import tensorflow as tf

## 2.3.1. Scalars

Most everyday mathematics consists of manipulating numbers one at a time. Formally, we call these values _scalars_. For example, the temperature in Palo Alto is a balmy \\(72\\) degrees Fahrenheit. If you wanted to convert the temperature to Celsius you would evaluate the expression \\(c = \frac{5}{9}(f - 32)\\), setting \\(f\\) to \\(72\\). In this equation, the values \\(5\\), \\(9\\), and \\(32\\) are constant scalars. The variables \\(c\\) and \\(f\\) in general represent unknown scalars.

We denote scalars by ordinary lower-cased letters (e.g., \\(x\\), \\(y\\), and \\(z\\)) and the space of all (continuous) _real-valued_ scalars by \\(\mathbb{R}\\). For expedience, we will skip past rigorous definitions of _spaces_ : just remember that the expression \\(x \in \mathbb{R}\\) is a formal way to say that \\(x\\) is a real-valued scalar. The symbol \\(\in\\) (pronounced “in”) denotes membership in a set. For example, \\(x, y \in \\{0, 1\\}\\) indicates that \\(x\\) and \\(y\\) are variables that can only take values \\(0\\) or \\(1\\).

Scalars are implemented as tensors that contain only one element. Below, we assign two scalars and perform the familiar addition, multiplication, division, and exponentiation operations.

    x = torch.tensor(3.0)
    y = torch.tensor(2.0)

    x + y, x * y, x / y, x**y

    (tensor(5.), tensor(6.), tensor(1.5000), tensor(9.))

    x = np.array(3.0)
    y = np.array(2.0)

    x + y, x * y, x / y, x ** y

    [21:50:12] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    (array(5.), array(6.), array(1.5), array(9.))

    x = jnp.array(3.0)
    y = jnp.array(2.0)

    x + y, x * y, x / y, x**y

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

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

## 2.3.2. Vectors

For current purposes, you can think of a vector as a fixed-length array of scalars. As with their code counterparts, we call these scalars the _elements_ of the vector (synonyms include _entries_ and _components_). When vectors represent examples from real-world datasets, their values hold some real-world significance. For example, if we were training a model to predict the risk of a loan defaulting, we might associate each applicant with a vector whose components correspond to quantities like their income, length of employment, or number of previous defaults. If we were studying the risk of heart attack, each vector might represent a patient and its components might correspond to their most recent vital signs, cholesterol levels, minutes of exercise per day, etc. We denote vectors by bold lowercase letters, (e.g., \\(\mathbf{x}\\), \\(\mathbf{y}\\), and \\(\mathbf{z}\\)).

Vectors are implemented as \\(1^{\textrm{st}}\\)-order tensors. In general, such tensors can have arbitrary lengths, subject to memory limitations. Caution: in Python, as in most programming languages, vector indices start at \\(0\\), also known as _zero-based indexing_ , whereas in linear algebra subscripts begin at \\(1\\) (one-based indexing).

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

We can refer to an element of a vector by using a subscript. For example, \\(x_2\\) denotes the second element of \\(\mathbf{x}\\). Since \\(x_2\\) is a scalar, we do not bold it. By default, we visualize vectors by stacking their elements vertically.

(2.3.1)\\[\begin{split}\mathbf{x} =\begin{bmatrix}x_{1} \\\ \vdots \\\x_{n}\end{bmatrix},\end{split}\\]

Here \\(x_1, \ldots, x_n\\) are elements of the vector. Later on, we will distinguish between such _column vectors_ and _row vectors_ whose elements are stacked horizontally. Recall that we access a tensor’s elements via indexing.

    x[2]

    tensor(2)

    x[2]

    array(2.)

    x[2]

    Array(2, dtype=int32)

    x[2]

    <tf.Tensor: shape=(), dtype=int32, numpy=2>

To indicate that a vector contains \\(n\\) elements, we write \\(\mathbf{x} \in \mathbb{R}^n\\). Formally, we call \\(n\\) the _dimensionality_ of the vector. In code, this corresponds to the tensor’s length, accessible via Python’s built-in `len` function.

    len(x)

    3

    len(x)

    3

    len(x)

    3

    len(x)

    3

We can also access the length via the `shape` attribute. The shape is a tuple that indicates a tensor’s length along each axis. Tensors with just one axis have shapes with just one element.

    x.shape

    torch.Size([3])

    x.shape

    (3,)

    x.shape

    (3,)

    x.shape

    TensorShape([3])

Oftentimes, the word “dimension” gets overloaded to mean both the number of axes and the length along a particular axis. To avoid this confusion, we use _order_ to refer to the number of axes and _dimensionality_ exclusively to refer to the number of components.

## 2.3.3. Matrices

Just as scalars are \\(0^{\textrm{th}}\\)-order tensors and vectors are \\(1^{\textrm{st}}\\)-order tensors, matrices are \\(2^{\textrm{nd}}\\)-order tensors. We denote matrices by bold capital letters (e.g., \\(\mathbf{X}\\), \\(\mathbf{Y}\\), and \\(\mathbf{Z}\\)), and represent them in code by tensors with two axes. The expression \\(\mathbf{A} \in \mathbb{R}^{m \times n}\\) indicates that a matrix \\(\mathbf{A}\\) contains \\(m \times n\\) real-valued scalars, arranged as \\(m\\) rows and \\(n\\) columns. When \\(m = n\\), we say that a matrix is _square_. Visually, we can illustrate any matrix as a table. To refer to an individual element, we subscript both the row and column indices, e.g., \\(a_{ij}\\) is the value that belongs to \\(\mathbf{A}\\)’s \\(i^{\textrm{th}}\\) row and \\(j^{\textrm{th}}\\) column:

(2.3.2)\\[\begin{split}\mathbf{A}=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\\ a_{21} & a_{22} & \cdots & a_{2n} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{m1} & a_{m2} & \cdots & a_{mn} \\\ \end{bmatrix}.\end{split}\\]

In code, we represent a matrix \\(\mathbf{A} \in \mathbb{R}^{m \times n}\\) by a \\(2^{\textrm{nd}}\\)-order tensor with shape (\\(m\\), \\(n\\)). We can convert any appropriately sized \\(m \times n\\) tensor into an \\(m \times n\\) matrix by passing the desired shape to `reshape`:

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

Sometimes we want to flip the axes. When we exchange a matrix’s rows and columns, the result is called its _transpose_. Formally, we signify a matrix \\(\mathbf{A}\\)’s transpose by \\(\mathbf{A}^\top\\) and if \\(\mathbf{B} = \mathbf{A}^\top\\), then \\(b_{ij} = a_{ji}\\) for all \\(i\\) and \\(j\\). Thus, the transpose of an \\(m \times n\\) matrix is an \\(n \times m\\) matrix:

(2.3.3)\\[\begin{split}\mathbf{A}^\top = \begin{bmatrix} a_{11} & a_{21} & \dots & a_{m1} \\\ a_{12} & a_{22} & \dots & a_{m2} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{1n} & a_{2n} & \dots & a_{mn} \end{bmatrix}.\end{split}\\]

In code, we can access any matrix’s transpose as follows:

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

Symmetric matrices are the subset of square matrices that are equal to their own transposes: \\(\mathbf{A} = \mathbf{A}^\top\\). The following matrix is symmetric:

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

Matrices are useful for representing datasets. Typically, rows correspond to individual records and columns correspond to distinct attributes.

## 2.3.4. Tensors

While you can go far in your machine learning journey with only scalars, vectors, and matrices, eventually you may need to work with higher-order tensors. Tensors give us a generic way of describing extensions to \\(n^{\textrm{th}}\\)-order arrays. We call software objects of the _tensor class_ “tensors” precisely because they too can have arbitrary numbers of axes. While it may be confusing to use the word _tensor_ for both the mathematical object and its realization in code, our meaning should usually be clear from context. We denote general tensors by capital letters with a special font face (e.g., \\(\mathsf{X}\\), \\(\mathsf{Y}\\), and \\(\mathsf{Z}\\)) and their indexing mechanism (e.g., \\(x_{ijk}\\) and \\([\mathsf{X}]_{1, 2i-1, 3}\\)) follows naturally from that of matrices.

Tensors will become more important when we start working with images. Each image arrives as a \\(3^{\textrm{rd}}\\)-order tensor with axes corresponding to the height, width, and _channel_. At each spatial location, the intensities of each color (red, green, and blue) are stacked along the channel. Furthermore, a collection of images is represented in code by a \\(4^{\textrm{th}}\\)-order tensor, where distinct images are indexed along the first axis. Higher-order tensors are constructed, as were vectors and matrices, by growing the number of shape components.

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

## 2.3.5. Basic Properties of Tensor Arithmetic

Scalars, vectors, matrices, and higher-order tensors all have some handy properties. For example, elementwise operations produce outputs that have the same shape as their operands.

    A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
    B = A.clone()  # Assign a copy of A to B by allocating new memory
    A, A + B

    (tensor([[0., 1., 2.],
             [3., 4., 5.]]),
     tensor([[ 0.,  2.,  4.],
             [ 6.,  8., 10.]]))

    A = np.arange(6).reshape(2, 3)
    B = A.copy()  # Assign a copy of A to B by allocating new memory
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
    B = A  # No cloning of A to B by allocating new memory
    A, A + B

    (<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
     array([[0., 1., 2.],
            [3., 4., 5.]], dtype=float32)>,
     <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
     array([[ 0.,  2.,  4.],
            [ 6.,  8., 10.]], dtype=float32)>)

The elementwise product of two matrices is called their _Hadamard product_ (denoted \\(\odot\\)). We can spell out the entries of the Hadamard product of two matrices \\(\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}\\):

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

Adding or multiplying a scalar and a tensor produces a result with the same shape as the original tensor. Here, each element of the tensor is added to (or multiplied by) the scalar.

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

## 2.3.6. Reduction

Often, we wish to calculate the sum of a tensor’s elements. To express the sum of the elements in a vector \\(\mathbf{x}\\) of length \\(n\\), we write \\(\sum_{i=1}^n x_i\\). There is a simple function for it:

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

To express sums over the elements of tensors of arbitrary shape, we simply sum over all its axes. For example, the sum of the elements of an \\(m \times n\\) matrix \\(\mathbf{A}\\) could be written \\(\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}\\).

    A.shape, A.sum()

    (torch.Size([2, 3]), tensor(15.))

    A.shape, A.sum()

    ((2, 3), array(15.))

    A.shape, A.sum()

    ((2, 3), Array(15., dtype=float32))

    A.shape, tf.reduce_sum(A)

    (TensorShape([2, 3]), <tf.Tensor: shape=(), dtype=float32, numpy=15.0>)

By default, invoking the sum function _reduces_ a tensor along all of its axes, eventually producing a scalar. Our libraries also allow us to specify the axes along which the tensor should be reduced. To sum over all elements along the rows (axis 0), we specify `axis=0` in `sum`. Since the input matrix reduces along axis 0 to generate the output vector, this axis is missing from the shape of the output.

    A.shape, A.sum(axis=0).shape

    (torch.Size([2, 3]), torch.Size([3]))

    A.shape, A.sum(axis=0).shape

    ((2, 3), (3,))

    A.shape, A.sum(axis=0).shape

    ((2, 3), (3,))

    A.shape, tf.reduce_sum(A, axis=0).shape

    (TensorShape([2, 3]), TensorShape([3]))

Specifying `axis=1` will reduce the column dimension (axis 1) by summing up elements of all the columns.

    A.shape, A.sum(axis=1).shape

    (torch.Size([2, 3]), torch.Size([2]))

    A.shape, A.sum(axis=1).shape

    ((2, 3), (2,))

    A.shape, A.sum(axis=1).shape

    ((2, 3), (2,))

    A.shape, tf.reduce_sum(A, axis=1).shape

    (TensorShape([2, 3]), TensorShape([2]))

Reducing a matrix along both rows and columns via summation is equivalent to summing up all the elements of the matrix.

    A.sum(axis=[0, 1]) == A.sum()  # Same as A.sum()

    tensor(True)

    A.sum(axis=[0, 1]) == A.sum()  # Same as A.sum()

    array(True)

    A.sum(axis=[0, 1]) == A.sum()  # Same as A.sum()

    Array(True, dtype=bool)

    tf.reduce_sum(A, axis=[0, 1]), tf.reduce_sum(A)  # Same as tf.reduce_sum(A)

    (<tf.Tensor: shape=(), dtype=float32, numpy=15.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=15.0>)

A related quantity is the _mean_ , also called the _average_. We calculate the mean by dividing the sum by the total number of elements. Because computing the mean is so common, it gets a dedicated library function that works analogously to `sum`.

    A.mean(), A.sum() / A.numel()

    (tensor(2.5000), tensor(2.5000))

    A.mean(), A.sum() / A.size

    (array(2.5), array(2.5))

    A.mean(), A.sum() / A.size

    (Array(2.5, dtype=float32), Array(2.5, dtype=float32))

    tf.reduce_mean(A), tf.reduce_sum(A) / tf.size(A).numpy()

    (<tf.Tensor: shape=(), dtype=float32, numpy=2.5>,
     <tf.Tensor: shape=(), dtype=float32, numpy=2.5>)

Likewise, the function for calculating the mean can also reduce a tensor along specific axes.

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (tensor([1.5000, 2.5000, 3.5000]), tensor([1.5000, 2.5000, 3.5000]))

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (array([1.5, 2.5, 3.5]), array([1.5, 2.5, 3.5]))

    A.mean(axis=0), A.sum(axis=0) / A.shape[0]

    (Array([1.5, 2.5, 3.5], dtype=float32), Array([1.5, 2.5, 3.5], dtype=float32))

    tf.reduce_mean(A, axis=0), tf.reduce_sum(A, axis=0) / A.shape[0]

    (<tf.Tensor: shape=(3,), dtype=float32, numpy=array([1.5, 2.5, 3.5], dtype=float32)>,
     <tf.Tensor: shape=(3,), dtype=float32, numpy=array([1.5, 2.5, 3.5], dtype=float32)>)

## 2.3.7. Non-Reduction Sum

Sometimes it can be useful to keep the number of axes unchanged when invoking the function for calculating the sum or mean. This matters when we want to use the broadcast mechanism.

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

For instance, since `sum_A` keeps its two axes after summing each row, we can divide `A` by `sum_A` with broadcasting to create a matrix where each row sums up to \\(1\\).

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

If we want to calculate the cumulative sum of elements of `A` along some axis, say `axis=0` (row by row), we can call the `cumsum` function. By design, this function does not reduce the input tensor along any axis.

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

## 2.3.8. Dot Products

So far, we have only performed elementwise operations, sums, and averages. And if this was all we could do, linear algebra would not deserve its own section. Fortunately, this is where things get more interesting. One of the most fundamental operations is the dot product. Given two vectors \\(\mathbf{x}, \mathbf{y} \in \mathbb{R}^d\\), their _dot product_ \\(\mathbf{x}^\top \mathbf{y}\\) (also known as _inner product_ , \\(\langle \mathbf{x}, \mathbf{y} \rangle\\)) is a sum over the products of the elements at the same position: \\(\mathbf{x}^\top \mathbf{y} = \sum_{i=1}^{d} x_i y_i\\).

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

Equivalently, we can calculate the dot product of two vectors by performing an elementwise multiplication followed by a sum:

    torch.sum(x * y)

    tensor(3.)

    np.sum(x * y)

    array(3.)

    jnp.sum(x * y)

    Array(3., dtype=float32)

    tf.reduce_sum(x * y)

    <tf.Tensor: shape=(), dtype=float32, numpy=3.0>

Dot products are useful in a wide range of contexts. For example, given some set of values, denoted by a vector \\(\mathbf{x} \in \mathbb{R}^n\\), and a set of weights, denoted by \\(\mathbf{w} \in \mathbb{R}^n\\), the weighted sum of the values in \\(\mathbf{x}\\) according to the weights \\(\mathbf{w}\\) could be expressed as the dot product \\(\mathbf{x}^\top \mathbf{w}\\). When the weights are nonnegative and sum to \\(1\\), i.e., \\(\left(\sum_{i=1}^{n} {w_i} = 1\right)\\), the dot product expresses a _weighted average_. After normalizing two vectors to have unit length, the dot products express the cosine of the angle between them. Later in this section, we will formally introduce this notion of _length_.

## 2.3.9. Matrix–Vector Products

Now that we know how to calculate dot products, we can begin to understand the _product_ between an \\(m \times n\\) matrix \\(\mathbf{A}\\) and an \\(n\\)-dimensional vector \\(\mathbf{x}\\). To start off, we visualize our matrix in terms of its row vectors

(2.3.5)\\[\begin{split}\mathbf{A}= \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_m \\\ \end{bmatrix},\end{split}\\]

where each \\(\mathbf{a}^\top_{i} \in \mathbb{R}^n\\) is a row vector representing the \\(i^\textrm{th}\\) row of the matrix \\(\mathbf{A}\\).

The matrix–vector product \\(\mathbf{A}\mathbf{x}\\) is simply a column vector of length \\(m\\), whose \\(i^\textrm{th}\\) element is the dot product \\(\mathbf{a}^\top_i \mathbf{x}\\):

(2.3.6)\\[\begin{split}\mathbf{A}\mathbf{x} = \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_m \\\ \end{bmatrix}\mathbf{x} = \begin{bmatrix} \mathbf{a}^\top_{1} \mathbf{x} \\\ \mathbf{a}^\top_{2} \mathbf{x} \\\ \vdots\\\ \mathbf{a}^\top_{m} \mathbf{x}\\\ \end{bmatrix}.\end{split}\\]

We can think of multiplication with a matrix \\(\mathbf{A}\in \mathbb{R}^{m \times n}\\) as a transformation that projects vectors from \\(\mathbb{R}^{n}\\) to \\(\mathbb{R}^{m}\\). These transformations are remarkably useful. For example, we can represent rotations as multiplications by certain square matrices. Matrix–vector products also describe the key calculation involved in computing the outputs of each layer in a neural network given the outputs from the previous layer.

To express a matrix–vector product in code, we use the `mv` function. Note that the column dimension of `A` (its length along axis 1) must be the same as the dimension of `x` (its length). Python has a convenience operator `@` that can execute both matrix–vector and matrix–matrix products (depending on its arguments). Thus we can write `A@x`.

    A.shape, x.shape, torch.mv(A, x), A@x

    (torch.Size([2, 3]), torch.Size([3]), tensor([ 5., 14.]), tensor([ 5., 14.]))

To express a matrix–vector product in code, we use the same `dot` function. The operation is inferred based on the type of the arguments. Note that the column dimension of `A` (its length along axis 1) must be the same as the dimension of `x` (its length).

    A.shape, x.shape, np.dot(A, x)

    ((2, 3), (3,), array([ 5., 14.]))

    A.shape, x.shape, jnp.matmul(A, x)

    ((2, 3), (3,), Array([ 5., 14.], dtype=float32))

To express a matrix–vector product in code, we use the `matvec` function. Note that the column dimension of `A` (its length along axis 1) must be the same as the dimension of `x` (its length).

    A.shape, x.shape, tf.linalg.matvec(A, x)

    (TensorShape([2, 3]),
     TensorShape([3]),
     <tf.Tensor: shape=(2,), dtype=float32, numpy=array([ 5., 14.], dtype=float32)>)

## 2.3.10. Matrix–Matrix Multiplication

Once you have gotten the hang of dot products and matrix–vector products, then _matrix–matrix multiplication_ should be straightforward.

Say that we have two matrices \\(\mathbf{A} \in \mathbb{R}^{n \times k}\\) and \\(\mathbf{B} \in \mathbb{R}^{k \times m}\\):

(2.3.7)\\[\begin{split}\mathbf{A}=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1k} \\\ a_{21} & a_{22} & \cdots & a_{2k} \\\ \vdots & \vdots & \ddots & \vdots \\\ a_{n1} & a_{n2} & \cdots & a_{nk} \\\ \end{bmatrix},\quad \mathbf{B}=\begin{bmatrix} b_{11} & b_{12} & \cdots & b_{1m} \\\ b_{21} & b_{22} & \cdots & b_{2m} \\\ \vdots & \vdots & \ddots & \vdots \\\ b_{k1} & b_{k2} & \cdots & b_{km} \\\ \end{bmatrix}.\end{split}\\]

Let \\(\mathbf{a}^\top_{i} \in \mathbb{R}^k\\) denote the row vector representing the \\(i^\textrm{th}\\) row of the matrix \\(\mathbf{A}\\) and let \\(\mathbf{b}_{j} \in \mathbb{R}^k\\) denote the column vector from the \\(j^\textrm{th}\\) column of the matrix \\(\mathbf{B}\\):

(2.3.8)\\[\begin{split}\mathbf{A}= \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_n \\\ \end{bmatrix}, \quad \mathbf{B}=\begin{bmatrix} \mathbf{b}_{1} & \mathbf{b}_{2} & \cdots & \mathbf{b}_{m} \\\ \end{bmatrix}.\end{split}\\]

To form the matrix product \\(\mathbf{C} \in \mathbb{R}^{n \times m}\\), we simply compute each element \\(c_{ij}\\) as the dot product between the \\(i^{\textrm{th}}\\) row of \\(\mathbf{A}\\) and the \\(j^{\textrm{th}}\\) column of \\(\mathbf{B}\\), i.e., \\(\mathbf{a}^\top_i \mathbf{b}_j\\):

(2.3.9)\\[\begin{split}\mathbf{C} = \mathbf{AB} = \begin{bmatrix} \mathbf{a}^\top_{1} \\\ \mathbf{a}^\top_{2} \\\ \vdots \\\ \mathbf{a}^\top_n \\\ \end{bmatrix} \begin{bmatrix} \mathbf{b}_{1} & \mathbf{b}_{2} & \cdots & \mathbf{b}_{m} \\\ \end{bmatrix} = \begin{bmatrix} \mathbf{a}^\top_{1} \mathbf{b}_1 & \mathbf{a}^\top_{1}\mathbf{b}_2& \cdots & \mathbf{a}^\top_{1} \mathbf{b}_m \\\ \mathbf{a}^\top_{2}\mathbf{b}_1 & \mathbf{a}^\top_{2} \mathbf{b}_2 & \cdots & \mathbf{a}^\top_{2} \mathbf{b}_m \\\ \vdots & \vdots & \ddots &\vdots\\\ \mathbf{a}^\top_{n} \mathbf{b}_1 & \mathbf{a}^\top_{n}\mathbf{b}_2& \cdots& \mathbf{a}^\top_{n} \mathbf{b}_m \end{bmatrix}.\end{split}\\]

We can think of the matrix–matrix multiplication \\(\mathbf{AB}\\) as performing \\(m\\) matrix–vector products or \\(m \times n\\) dot products and stitching the results together to form an \\(n \times m\\) matrix. In the following snippet, we perform matrix multiplication on `A` and `B`. Here, `A` is a matrix with two rows and three columns, and `B` is a matrix with three rows and four columns. After multiplication, we obtain a matrix with two rows and four columns.

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

The term _matrix–matrix multiplication_ is often simplified to _matrix multiplication_ , and should not be confused with the Hadamard product.

## 2.3.11. Norms

Some of the most useful operators in linear algebra are _norms_. Informally, the norm of a vector tells us how _big_ it is. For instance, the \\(\ell_2\\) norm measures the (Euclidean) length of a vector. Here, we are employing a notion of _size_ that concerns the magnitude of a vector’s components (not its dimensionality).

A norm is a function \\(\| \cdot \|\\) that maps a vector to a scalar and satisfies the following three properties:

  1. Given any vector \\(\mathbf{x}\\), if we scale (all elements of) the vector by a scalar \\(\alpha \in \mathbb{R}\\), its norm scales accordingly:

(2.3.10)\\[\|\alpha \mathbf{x}\| = |\alpha| \|\mathbf{x}\|.\\]

  2. For any vectors \\(\mathbf{x}\\) and \\(\mathbf{y}\\): norms satisfy the triangle inequality:

(2.3.11)\\[\|\mathbf{x} + \mathbf{y}\| \leq \|\mathbf{x}\| + \|\mathbf{y}\|.\\]

  3. The norm of a vector is nonnegative and it only vanishes if the vector is zero:

(2.3.12)\\[\|\mathbf{x}\| > 0 \textrm{ for all } \mathbf{x} \neq 0.\\]

Many functions are valid norms and different norms encode different notions of size. The Euclidean norm that we all learned in elementary school geometry when calculating the hypotenuse of a right triangle is the square root of the sum of squares of a vector’s elements. Formally, this is called the \\(\ell_2\\) _norm_ and expressed as

(2.3.13)\\[\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}.\\]

The method `norm` calculates the \\(\ell_2\\) norm.

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

The \\(\ell_1\\) norm is also common and the associated measure is called the Manhattan distance. By definition, the \\(\ell_1\\) norm sums the absolute values of a vector’s elements:

(2.3.14)\\[\|\mathbf{x}\|_1 = \sum_{i=1}^n \left|x_i \right|.\\]

Compared to the \\(\ell_2\\) norm, it is less sensitive to outliers. To compute the \\(\ell_1\\) norm, we compose the absolute value with the sum operation.

    torch.abs(u).sum()

    tensor(7.)

    np.abs(u).sum()

    array(7.)

    jnp.linalg.norm(u, ord=1) # same as jnp.abs(u).sum()

    Array(7., dtype=float32)

    tf.reduce_sum(tf.abs(u))

    <tf.Tensor: shape=(), dtype=float32, numpy=7.0>

Both the \\(\ell_2\\) and \\(\ell_1\\) norms are special cases of the more general \\(\ell_p\\) _norms_ :

(2.3.15)\\[\|\mathbf{x}\|_p = \left(\sum_{i=1}^n \left|x_i \right|^p \right)^{1/p}.\\]

In the case of matrices, matters are more complicated. After all, matrices can be viewed both as collections of individual entries _and_ as objects that operate on vectors and transform them into other vectors. For instance, we can ask by how much longer the matrix–vector product \\(\mathbf{X} \mathbf{v}\\) could be relative to \\(\mathbf{v}\\). This line of thought leads to what is called the _spectral_ norm. For now, we introduce the _Frobenius norm_ , which is much easier to compute and defined as the square root of the sum of the squares of a matrix’s elements:

(2.3.16)\\[\|\mathbf{X}\|_\textrm{F} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n x_{ij}^2}.\\]

The Frobenius norm behaves as if it were an \\(\ell_2\\) norm of a matrix-shaped vector. Invoking the following function will calculate the Frobenius norm of a matrix.

    torch.norm(torch.ones((4, 9)))

    tensor(6.)

    np.linalg.norm(np.ones((4, 9)))

    array(6.)

    jnp.linalg.norm(jnp.ones((4, 9)))

    Array(6., dtype=float32)

    tf.norm(tf.ones((4, 9)))

    <tf.Tensor: shape=(), dtype=float32, numpy=6.0>

While we do not want to get too far ahead of ourselves, we already can plant some intuition about why these concepts are useful. In deep learning, we are often trying to solve optimization problems: _maximize_ the probability assigned to observed data; _maximize_ the revenue associated with a recommender model; _minimize_ the distance between predictions and the ground truth observations; _minimize_ the distance between representations of photos of the same person while _maximizing_ the distance between representations of photos of different people. These distances, which constitute the objectives of deep learning algorithms, are often expressed as norms.

## 2.3.12. Discussion

In this section, we have reviewed all the linear algebra that you will need to understand a significant chunk of modern deep learning. There is a lot more to linear algebra, though, and much of it is useful for machine learning. For example, matrices can be decomposed into factors, and these decompositions can reveal low-dimensional structure in real-world datasets. There are entire subfields of machine learning that focus on using matrix decompositions and their generalizations to high-order tensors to discover structure in datasets and solve prediction problems. But this book focuses on deep learning. And we believe you will be more inclined to learn more mathematics once you have gotten your hands dirty applying machine learning to real datasets. So while we reserve the right to introduce more mathematics later on, we wrap up this section here.

If you are eager to learn more linear algebra, there are many excellent books and online resources. For a more advanced crash course, consider checking out Strang ([1993](../chapter_references/zreferences.html#id266 "Strang, G. \(1993\). Introduction to Linear Algebra. Wellesley–Cambridge Press.")), Kolter ([2008](../chapter_references/zreferences.html#id152 "Kolter, Z. \(2008\). Linear algebra review and reference. Available online: http://cs229.stanford.edu/section/cs229-linalg.pdf.")), and Petersen and Pedersen ([2008](../chapter_references/zreferences.html#id216 "Petersen, K. B., & Pedersen, M. S. \(2008\). The Matrix Cookbook. Technical University of Denmark.")).

To recap:

  * Scalars, vectors, matrices, and tensors are the basic mathematical objects used in linear algebra and have zero, one, two, and an arbitrary number of axes, respectively.

  * Tensors can be sliced or reduced along specified axes via indexing, or operations such as `sum` and `mean`, respectively.

  * Elementwise products are called Hadamard products. By contrast, dot products, matrix–vector products, and matrix–matrix products are not elementwise operations and in general return objects having shapes that are different from the the operands.

  * Compared to Hadamard products, matrix–matrix products take considerably longer to compute (cubic rather than quadratic time).

  * Norms capture various notions of the magnitude of a vector (or matrix), and are commonly applied to the difference of two vectors to measure their distance apart.

  * Common vector norms include the \\(\ell_1\\) and \\(\ell_2\\) norms, and common matrix norms include the _spectral_ and _Frobenius_ norms.

## 2.3.13. Exercises

  1. Prove that the transpose of the transpose of a matrix is the matrix itself: \\((\mathbf{A}^\top)^\top = \mathbf{A}\\).

  2. Given two matrices \\(\mathbf{A}\\) and \\(\mathbf{B}\\), show that sum and transposition commute: \\(\mathbf{A}^\top + \mathbf{B}^\top = (\mathbf{A} + \mathbf{B})^\top\\).

  3. Given any square matrix \\(\mathbf{A}\\), is \\(\mathbf{A} + \mathbf{A}^\top\\) always symmetric? Can you prove the result by using only the results of the previous two exercises?

  4. We defined the tensor `X` of shape (2, 3, 4) in this section. What is the output of `len(X)`? Write your answer without implementing any code, then check your answer using code.

  5. For a tensor `X` of arbitrary shape, does `len(X)` always correspond to the length of a certain axis of `X`? What is that axis?

  6. Run `A / A.sum(axis=1)` and see what happens. Can you analyze the results?

  7. When traveling between two points in downtown Manhattan, what is the distance that you need to cover in terms of the coordinates, i.e., in terms of avenues and streets? Can you travel diagonally?

  8. Consider a tensor of shape (2, 3, 4). What are the shapes of the summation outputs along axes 0, 1, and 2?

  9. Feed a tensor with three or more axes to the `linalg.norm` function and observe its output. What does this function compute for tensors of arbitrary shape?

  10. Consider three large matrices, say \\(\mathbf{A} \in \mathbb{R}^{2^{10} \times 2^{16}}\\), \\(\mathbf{B} \in \mathbb{R}^{2^{16} \times 2^{5}}\\) and \\(\mathbf{C} \in \mathbb{R}^{2^{5} \times 2^{14}}\\), initialized with Gaussian random variables. You want to compute the product \\(\mathbf{A} \mathbf{B} \mathbf{C}\\). Is there any difference in memory footprint and speed, depending on whether you compute \\((\mathbf{A} \mathbf{B}) \mathbf{C}\\) or \\(\mathbf{A} (\mathbf{B} \mathbf{C})\\). Why?

  11. Consider three large matrices, say \\(\mathbf{A} \in \mathbb{R}^{2^{10} \times 2^{16}}\\), \\(\mathbf{B} \in \mathbb{R}^{2^{16} \times 2^{5}}\\) and \\(\mathbf{C} \in \mathbb{R}^{2^{5} \times 2^{16}}\\). Is there any difference in speed depending on whether you compute \\(\mathbf{A} \mathbf{B}\\) or \\(\mathbf{A} \mathbf{C}^\top\\)? Why? What changes if you initialize \\(\mathbf{C} = \mathbf{B}^\top\\) without cloning memory? Why?

  12. Consider three matrices, say \\(\mathbf{A}, \mathbf{B}, \mathbf{C} \in \mathbb{R}^{100 \times 200}\\). Construct a tensor with three axes by stacking \\([\mathbf{A}, \mathbf{B}, \mathbf{C}]\\). What is the dimensionality? Slice out the second coordinate of the third axis to recover \\(\mathbf{B}\\). Check that your answer is correct.

[Discussions](https://discuss.d2l.ai/t/31)

[Discussions](https://discuss.d2l.ai/t/30)

[Discussions](https://discuss.d2l.ai/t/17968)

[Discussions](https://discuss.d2l.ai/t/196)

Table Of Contents

  * 2.3. Linear Algebra
    * 2.3.1. Scalars
    * 2.3.2. Vectors
    * 2.3.3. Matrices
    * 2.3.4. Tensors
    * 2.3.5. Basic Properties of Tensor Arithmetic
    * 2.3.6. Reduction
    * 2.3.7. Non-Reduction Sum
    * 2.3.8. Dot Products
    * 2.3.9. Matrix–Vector Products
    * 2.3.10. Matrix–Matrix Multiplication
    * 2.3.11. Norms
    * 2.3.12. Discussion
    * 2.3.13. Exercises

