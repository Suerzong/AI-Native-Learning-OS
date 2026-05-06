# NumPy 快速入门

## 前置知识

你需要了解一些 Python 基础。如需复习，请参阅 [Python 教程](https://docs.python.org/tutorial/)。

要运行示例，除了 NumPy 外还需要安装 `matplotlib`。

**学习者概览**

本文对 NumPy 中的数组（Array）进行了快速概览，展示了 n 维（\\(n>=2\\）数组的表示和操作方式。特别是，如果你不知道如何将常用函数应用于 n 维数组（而不使用 for 循环），或者想理解 n 维数组的轴（axis）和形状（shape）属性，本文会有所帮助。

**学习目标**

阅读后，你应该能够：

- 理解 NumPy 中一维、二维和 n 维数组的区别；
- 理解如何在不使用 for 循环的情况下，将一些线性代数运算应用于 n 维数组；
- 理解 n 维数组的轴和形状属性。

## 基础

NumPy 的主要对象是同构多维数组（homogeneous multidimensional array）。它是一个元素表（通常是数字），所有元素类型相同，由非负整数元组索引。在 NumPy 中，维度称为 _轴（axes）_。

例如，3D 空间中一个点的坐标数组 `[1, 2, 1]` 有一个轴，该轴有 3 个元素，因此我们说它的长度为 3。在下面的例子中，数组有 2 个轴，第一个轴长度为 2，第二个轴长度为 3。

```python
[[1., 0., 0.],
 [0., 1., 2.]]
```

NumPy 的数组类称为 `ndarray`，也被称为别名 `array`。注意 `numpy.array` 与 Python 标准库中的 `array.array` 不同，后者只处理一维数组且功能较少。`ndarray` 对象的重要属性有：

**ndarray.ndim** -- 数组的轴（维度）数量。

**ndarray.shape** -- 数组的维度。这是一个整数元组，表示每个维度中数组的大小。对于一个 _n_ 行 _m_ 列的矩阵，`shape` 为 `(n,m)`。因此 `shape` 元组的长度就是轴的数量 `ndim`。

**ndarray.size** -- 数组元素的总数。等于 `shape` 各元素的乘积。

**ndarray.dtype** -- 描述数组中元素类型的对象。可以使用标准 Python 类型创建或指定 dtype。此外 NumPy 提供了自己的类型，如 numpy.int32、numpy.int16 和 numpy.float64。

**ndarray.itemsize** -- 数组每个元素的字节大小。例如，`float64` 类型的数组 `itemsize` 为 8（=64/8），而 `complex32` 类型的 `itemsize` 为 4（=32/8）。等价于 `ndarray.dtype.itemsize`。

**ndarray.data** -- 包含数组实际元素的缓冲区。通常不需要使用此属性，因为我们将通过索引方式访问数组元素。

### 示例

```python
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>
```

### 数组创建

有几种创建数组的方法。

例如，可以使用 `array` 函数从 Python 列表或元组创建数组，结果数组的类型由序列中元素的类型推断而来。

```python
>>> import numpy as np
>>> a = np.array([2, 3, 4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
```

常见错误是用多个参数调用 `array`，而不是提供单个序列作为参数。

```python
>>> a = np.array(1, 2, 3, 4)    # 错误
Traceback (most recent call last):
  ...
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
>>> a = np.array([1, 2, 3, 4])  # 正确
```

`array` 将序列的序列转换为二维数组，序列的序列的序列转换为三维数组，以此类推。

```python
>>> b = np.array([(1.5, 2, 3), (4, 5, 6)])
>>> b
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```

也可以在创建时显式指定数组类型：

```python
>>> c = np.array([[1, 2], [3, 4]], dtype=complex)
>>> c
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

通常数组的元素最初是未知的，但其大小是已知的。因此 NumPy 提供了几个函数来创建带有初始占位内容的数组，以尽量减少数组增长这一昂贵操作的必要性。

函数 `zeros` 创建全零数组，`ones` 创建全一数组，`empty` 创建初始内容随机且取决于内存状态的数组。默认 dtype 为 `float64`，但可以通过关键字参数 `dtype` 指定。

```python
>>> np.zeros((3, 4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((2, 3, 4), dtype=np.int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> np.empty((2, 3))
array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # 可能不同
       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
```

要创建数字序列，NumPy 提供了 `arange` 函数，类似于 Python 内置的 `range`，但返回数组。

```python
>>> np.arange(10, 30, 5)
array([10, 15, 20, 25])
>>> np.arange(0, 2, 0.3)  # 接受浮点参数
array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
```

当 `arange` 使用浮点参数时，由于浮点精度有限，通常无法预测获得的元素数量。因此通常最好使用 `linspace` 函数，它接收所需元素数量作为参数，而不是步长：

```python
>>> from numpy import pi
>>> np.linspace(0, 2, 9)                   # 从 0 到 2 的 9 个数
array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
>>> x = np.linspace(0, 2 * pi, 100)        # 在大量点上计算函数值很有用
>>> f = np.sin(x)
```

### 打印数组

打印数组时，NumPy 的显示方式类似于嵌套列表，但有以下布局规则：

- 最后一个轴从左到右打印
- 倒数第二个轴从上到下打印
- 其余轴也从上到下打印，每个切片之间用空行分隔

一维数组打印为行，二维打印为矩阵，三维打印为矩阵列表。

```python
>>> a = np.arange(6)                    # 一维数组
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4, 3)     # 二维数组
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2, 3, 4)  # 三维数组
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

如果数组太大无法打印，NumPy 会自动跳过中间部分，只打印角落：

```python
>>> print(np.arange(10000))
[   0    1    2 ... 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100, 100))
[[   0    1    2 ...   97   98   99]
 [ 100  101  102 ...  197  198  199]
 ...
 [9900 9901 9902 ... 9997 9998 9999]]
```

要禁用此行为并强制 NumPy 打印整个数组，可以使用 `set_printoptions` 更改打印选项。

```python
>>> np.set_printoptions(threshold=sys.maxsize)  # 需要导入 sys 模块
```

### 基本运算

数组上的算术运算符是 _逐元素（elementwise）_ 的。创建新数组并填充结果。

```python
>>> a = np.array([20, 30, 40, 50])
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False])
```

与许多矩阵语言不同，NumPy 数组中的乘法运算符 `*` 是逐元素运算。矩阵乘积可以使用 `@` 运算符（Python >=3.5）或 `dot` 函数/方法：

```python
>>> A = np.array([[1, 1],
...               [0, 1]])
>>> B = np.array([[2, 0],
...               [3, 4]])
>>> A * B     # 逐元素乘积
array([[2, 0],
       [0, 4]])
>>> A @ B     # 矩阵乘积
array([[5, 4],
       [3, 4]])
>>> A.dot(B)  # 另一种矩阵乘积
array([[5, 4],
       [3, 4]])
```

某些运算如 `+=` 和 `*=` 是就地修改现有数组，而不是创建新数组。

```python
>>> rg = np.random.default_rng(1)  # 创建默认随机数生成器实例
>>> a = np.ones((2, 3), dtype=int)
>>> b = rg.random((2, 3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[3.51182162, 3.9504637 , 3.14415961],
       [3.94864945, 3.31183145, 3.42332645]])
>>> a += b  # b 不会自动转换为整数类型
Traceback (most recent call last):
    ...
numpy._core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

当对不同类型的数组进行运算时，结果数组的类型对应于更通用或更精确的类型（称为向上转型）。

```python
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0, pi, 3)
>>> b.dtype.name
'float64'
>>> c = a + b
>>> c
array([1.        , 2.57079633, 4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c * 1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
```

许多一元运算（如计算数组所有元素之和）作为 `ndarray` 类的方法实现。

```python
>>> a = rg.random((2, 3))
>>> a
array([[0.82770259, 0.40919914, 0.54959369],
       [0.02755911, 0.75351311, 0.53814331]])
>>> a.sum()
3.1057109529998157
>>> a.min()
0.027559113243068367
>>> a.max()
0.8277025938204418
```

默认情况下，这些运算将数组视为数字列表，不管其形状如何。但是通过指定 `axis` 参数，可以沿数组的指定轴执行运算：

```python
>>> b = np.arange(12).reshape(3, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)     # 每列的和
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)     # 每行的最小值
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)  # 沿每行的累积和
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```

### 通用函数（Universal Functions）

NumPy 提供了熟悉的数学函数，如 sin、cos 和 exp。在 NumPy 中，这些称为"通用函数"（`ufunc`）。在 NumPy 内部，这些函数对数组逐元素运算，产生数组作为输出。

```python
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(B)
array([0.        , 1.        , 1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([2., 0., 6.])
```

### 索引、切片和迭代

**一维**数组可以被索引、切片和迭代，就像列表和其他 Python 序列一样。

```python
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> # 等价于 a[0:6:2] = 1000;
>>> # 从起始到位置 6（不含），每隔 2 个元素设为 1000
>>> a[:6:2] = 1000
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
>>> a[::-1]  # 反转 a
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
>>> for i in a:
...     print(i**(1 / 3.))
...
9.999999999999998  # 可能不同
1.0
9.999999999999998
3.0
9.999999999999998
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
```

**多维**数组每个轴可以有一个索引，这些索引以逗号分隔的元组给出：

```python
>>> def f(x, y):
...     return 10 * x + y
...
>>> b = np.fromfunction(f, (5, 4), dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2, 3]
23
>>> b[0:5, 1]  # b 的第二列每一行
array([ 1, 11, 21, 31, 41])
>>> b[:, 1]    # 等价于上面的例子
array([ 1, 11, 21, 31, 41])
>>> b[1:3, :]  # b 的第二和第三行每一列
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

当提供的索引少于轴的数量时，缺失的索引被视为完整切片 `:`。

```python
>>> b[-1]   # 最后一行。等价于 b[-1, :]
array([40, 41, 42, 43])
```

`b[i]` 中括号内的表达式被视为 `i` 后跟表示剩余轴所需的尽可能多的 `:`。NumPy 也允许你用点号写作 `b[i, ...]`。

**省略号**（`...`）代表生成完整索引元组所需的尽可能多的冒号。例如，如果 `x` 是一个 5 轴数组：

- `x[1, 2, ...]` 等价于 `x[1, 2, :, :, :]`
- `x[..., 3]` 等价于 `x[:, :, :, :, 3]`
- `x[4, ..., 5, :]` 等价于 `x[4, :, :, 5, :]`

```python
>>> c = np.array([[[  0,  1,  2],  # 一个 3D 数组（两个堆叠的 2D 数组）
...                [ 10, 12, 13]],
...               [[100, 101, 102],
...                [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
>>> c[1, ...]  # 等价于 c[1, :, :] 或 c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[..., 2]  # 等价于 c[:, :, 2]
array([[  2,  13],
       [102, 113]])
```

**迭代**多维数组是沿第一个轴进行的：

```python
>>> for row in b:
...     print(row)
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

如果想对数组中每个元素执行操作，可以使用 `flat` 属性，它是数组所有元素的[迭代器](https://docs.python.org/tutorial/classes.html#iterators)：

```python
>>> for element in b.flat:
...     print(element)
...
0
1
2
3
10
11
...
```

## 形状操作

### 改变数组形状

数组的形状由每个轴的元素数量给出：

```python
>>> a = np.floor(10 * rg.random((3, 4)))
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.shape
(3, 4)
```

可以用各种命令改变数组的形状。注意以下三个命令都返回修改后的数组，但不改变原始数组：

```python
>>> a.ravel()  # 返回展平的数组
array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
>>> a.reshape(6, 2)  # 返回修改形状后的数组
array([[3., 7.],
       [3., 4.],
       [1., 4.],
       [2., 2.],
       [7., 2.],
       [4., 9.]])
>>> a.T  # 返回转置数组
array([[3., 1., 7.],
       [7., 4., 2.],
       [3., 2., 4.],
       [4., 2., 9.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

`ravel` 产生的数组中元素的顺序通常是"C 风格"，即最右边的索引"变化最快"，因此 `a[0, 0]` 之后的元素是 `a[0, 1]`。如果将数组重塑为其他形状，数组仍被视为"C 风格"。NumPy 通常按此顺序创建数组，因此 `ravel` 通常不需要复制其参数。但如果数组是通过切片另一个数组或用不寻常的选项创建的，可能需要复制。`ravel` 和 `reshape` 函数也可以通过可选参数指定使用 FORTRAN 风格数组，其中最左边的索引变化最快。

[`reshape`](../reference/generated/numpy.reshape.html) 函数返回修改形状后的参数，而 [`ndarray.resize`](../reference/generated/numpy.ndarray.resize.html) 方法直接修改数组本身：

```python
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.resize((2, 6))
>>> a
array([[3., 7., 3., 4., 1., 4.],
       [2., 2., 7., 2., 4., 9.]])
```

如果在重塑操作中某个维度指定为 `-1`，则其他维度会自动计算：

```python
>>> a.reshape(3, -1)
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
```

### 将不同数组堆叠在一起

可以沿不同轴将多个数组堆叠在一起：

```python
>>> a = np.floor(10 * rg.random((2, 2)))
>>> a
array([[9., 7.],
       [5., 2.]])
>>> b = np.floor(10 * rg.random((2, 2)))
>>> b
array([[1., 9.],
       [5., 1.]])
>>> np.vstack((a, b))
array([[9., 7.],
       [5., 2.],
       [1., 9.],
       [5., 1.]])
>>> np.hstack((a, b))
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
```

函数 [`column_stack`](../reference/generated/numpy.column_stack.html) 将一维数组作为列堆叠到二维数组中。对于二维数组，它等价于 [`hstack`](../reference/generated/numpy.hstack.html)：

```python
>>> from numpy import newaxis
>>> np.column_stack((a, b))  # 对二维数组
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
>>> a = np.array([4., 2.])
>>> b = np.array([3., 8.])
>>> np.column_stack((a, b))  # 返回二维数组
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a, b))        # 结果不同
array([4., 2., 3., 8.])
>>> a[:, newaxis]  # 将 a 视为二维列向量
array([[4.],
       [2.]])
>>> np.column_stack((a[:, newaxis], b[:, newaxis]))
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a[:, newaxis], b[:, newaxis]))  # 结果相同
array([[4., 3.],
       [2., 8.]])
```

一般来说，对于两个以上维度的数组，[`hstack`](../reference/generated/numpy.hstack.html) 沿第二个轴堆叠，[`vstack`](../reference/generated/numpy.vstack.html) 沿第一个轴堆叠，[`concatenate`](../reference/generated/numpy.concatenate.html) 允许可选参数指定拼接的轴号。

**注意**：在复杂情况下，[`r_`](../reference/generated/numpy.r_.html) 和 [`c_`](../reference/generated/numpy.c_.html) 对于沿一个轴堆叠数字来创建数组很有用，它们允许使用范围字面量 `:`。

```python
>>> np.r_[1:4, 0, 4]
array([1, 2, 3, 0, 4])
```

### 将一个数组拆分为多个较小的数组

使用 [`hsplit`](../reference/generated/numpy.hsplit.html)，可以沿水平轴拆分数组，通过指定要返回的等形数组数量或指定分割发生的列：

```python
>>> a = np.floor(10 * rg.random((2, 12)))
>>> a
array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
       [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
>>> # 将 a 拆分为 3 个
>>> np.hsplit(a, 3)
[array([[6., 7., 6., 9.],
       [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
       [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
       [1., 8., 1., 0.]])]
>>> # 在第三列和第四列之后拆分 a
>>> np.hsplit(a, (3, 4))
[array([[6., 7., 6.],
       [8., 5., 5.]]), array([[9.],
       [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
       [1., 8., 6., 7., 1., 8., 1., 0.]])]
```

[`vsplit`](../reference/generated/numpy.vsplit.html) 沿垂直轴拆分，[`array_split`](../reference/generated/numpy.array_split.html) 允许指定沿哪个轴拆分。

## 副本和视图

在操作和操作数组时，数据有时会被复制到新数组中，有时不会。这常常是初学者困惑的来源。有三种情况：

### 完全不复制

简单赋值不会复制对象或其数据。

```python
>>> a = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])
>>> b = a            # 不创建新对象
>>> b is a           # a 和 b 是同一 ndarray 对象的两个名称
True
```

Python 以引用方式传递可变对象，因此函数调用也不复制。

```python
>>> def f(x):
...     print(id(x))
...
>>> id(a)  # id 是对象的唯一标识符
148293216  # 可能不同
>>> f(a)
148293216  # 可能不同
```

### 视图或浅拷贝

不同的数组对象可以共享相同的数据。`view` 方法创建一个查看相同数据的新数组对象。

```python
>>> c = a.view()
>>> c is a
False
>>> c.base is a            # c 是 a 拥有数据的视图
True
>>> c.flags.owndata
False
>>>
>>> c = c.reshape((2, 6))  # a 的形状不变，重新赋值的 c 仍然是 a 的视图
>>> a.shape
(3, 4)
>>> c[0, 4] = 1234         # a 的数据改变
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
```

对数组切片返回其视图：

```python
>>> s = a[:, 1:3]
>>> s[:] = 10  # s[:] 是 s 的视图。注意 s = 10 和 s[:] = 10 的区别
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

### 深拷贝

`copy` 方法对数组及其数据进行完整复制。

```python
>>> d = a.copy()  # 创建一个带有新数据的新数组对象
>>> d is a
False
>>> d.base is a  # d 与 a 不共享任何数据
False
>>> d[0, 0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

有时如果不再需要原始数组，应在切片后调用 `copy`。例如，假设 `a` 是一个巨大的中间结果，而最终结果 `b` 只包含 `a` 的一小部分，在用切片构造 `b` 时应进行深拷贝：

```python
>>> a = np.arange(int(1e8))
>>> b = a[:100].copy()
>>> del a  # 可以释放 a 的内存。
```

如果使用 `b = a[:100]` 代替，`a` 被 `b` 引用，即使执行 `del a` 也会在内存中持续存在。

### 函数和方法概览

以下是按类别排列的一些有用的 NumPy 函数和方法名称列表。

**数组创建**：`arange`, `array`, `copy`, `empty`, `empty_like`, `eye`, `fromfile`, `fromfunction`, `identity`, `linspace`, `logspace`, `mgrid`, `ogrid`, `ones`, `ones_like`, `r_`, `zeros`, `zeros_like`

**类型转换**：`ndarray.astype`, `atleast_1d`, `atleast_2d`, `atleast_3d`

**操作**：`array_split`, `column_stack`, `concatenate`, `diagonal`, `dsplit`, `dstack`, `hsplit`, `hstack`, `ndarray.item`, `newaxis`, `ravel`, `repeat`, `reshape`, `resize`, `squeeze`, `swapaxes`, `take`, `transpose`, `vsplit`, `vstack`

**查询**：`all`, `any`, `nonzero`, `where`

**排序**：`argmax`, `argmin`, `argsort`, `max`, `min`, `ptp`, `searchsorted`, `sort`

**运算**：`choose`, `compress`, `cumprod`, `cumsum`, `inner`, `ndarray.fill`, `imag`, `prod`, `put`, `putmask`, `real`, `sum`

**基本统计**：`cov`, `mean`, `std`, `var`

**基本线性代数**：`cross`, `dot`, `outer`, `linalg.svd`, `vdot`

## 进阶内容

### 广播规则（Broadcasting Rules）

广播允许通用函数以有意义的方式处理不具有完全相同形状的输入。

广播的第一条规则是，如果所有输入数组不具有相同的维度数，则将"1"重复前置到较小数组的形状中，直到所有数组具有相同的维度数。

广播的第二条规则确保沿特定维度大小为 1 的数组表现得像沿该维度具有最大形状的数组一样。对于"广播"数组，该维度上数组元素的值被认为是相同的。

应用广播规则后，所有数组的大小必须匹配。更多详情请参阅 [Broadcasting](basics.broadcasting.html)。

## 高级索引和索引技巧

NumPy 提供了比常规 Python 序列更多的索引功能。除了之前看到的整数和切片索引外，还可以用整数数组和布尔数组进行索引。

### 用索引数组索引

```python
>>> a = np.arange(12)**2  # 前 12 个平方数
>>> i = np.array([1, 1, 3, 8, 5])  # 索引数组
>>> a[i]  # a 在位置 i 处的元素
array([ 1,  1,  9, 64, 25])
>>>
>>> j = np.array([[3, 4], [9, 7]])  # 二维索引数组
>>> a[j]  # 与 j 形状相同
array([[ 9, 16],
       [81, 49]])
```

### 用布尔数组索引

当用布尔数组索引时，我们显式选择数组中想要和不想要的元素。最自然的方式是使用与原始数组 _形状相同_ 的布尔数组：

```python
>>> a = np.arange(12).reshape(3, 4)
>>> b = a > 4
>>> b  # b 是与 a 形状相同的布尔数组
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> a[b]  # 包含选定元素的一维数组
array([ 5,  6,  7,  8,  9, 10, 11])
```

这个特性在赋值时非常有用：

```python
>>> a[b] = 0  # a 中所有大于 4 的元素变为 0
>>> a
array([[0, 1, 2, 3],
       [4, 0, 0, 0],
       [0, 0, 0, 0]])
```

### ix_() 函数

[`ix_`](../reference/generated/numpy.ix_.html) 函数可以组合不同向量以获得每个 n 元组的结果。例如，如果你想计算从向量 a、b、c 中各取一个元素的所有 a+b*c：

```python
>>> a = np.array([2, 3, 4, 5])
>>> b = np.array([8, 5, 4])
>>> c = np.array([5, 4, 6, 8, 3])
>>> ax, bx, cx = np.ix_(a, b, c)
>>> result = ax + bx * cx
>>> result[3, 2, 4]
17
>>> a[3] + b[2] * c[4]
17
```

## 实用技巧

### "自动"重塑

要更改数组的维度，可以省略其中一个大小，它将被自动推断：

```python
>>> a = np.arange(30)
>>> b = a.reshape((2, -1, 3))  # -1 表示"根据需要"
>>> b.shape
(2, 5, 3)
```

### 向量堆叠

如何从等长行向量列表构造二维数组？在 MATLAB 中这很简单：如果 `x` 和 `y` 是两个等长向量，只需 `m=[x;y]`。在 NumPy 中，这通过 `column_stack`、`dstack`、`hstack` 和 `vstack` 函数实现，取决于堆叠的维度：

```python
>>> x = np.arange(0, 10, 2)
>>> y = np.arange(5)
>>> m = np.vstack([x, y])
>>> m
array([[0, 2, 4, 6, 8],
       [0, 1, 2, 3, 4]])
>>> xy = np.hstack([x, y])
>>> xy
array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])
```

### 直方图

NumPy 的 `histogram` 函数应用于数组时返回一对向量：数组的直方图和分箱边界的向量。注意：`matplotlib` 也有构建直方图的函数（称为 `hist`，与 Matlab 中相同），它与 NumPy 中的不同。主要区别在于 `pylab.hist` 自动绘制直方图，而 `numpy.histogram` 只生成数据。

```python
>>> import numpy as np
>>> rg = np.random.default_rng(1)
>>> import matplotlib.pyplot as plt
>>> # 构建 10000 个正态偏差的向量，方差 0.5^2，均值 2
>>> mu, sigma = 2, 0.5
>>> v = rg.normal(mu, sigma, 10000)
>>> # 绘制 50 个分箱的归一化直方图
>>> plt.hist(v, bins=50, density=True)       # matplotlib 版本（绘图）
>>> # 用 numpy 计算直方图然后绘制
>>> (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy 版本（不绘图）
>>> plt.plot(.5 * (bins[1:] + bins[:-1]), n)
```

使用 Matplotlib >=3.4 时也可以用 `plt.stairs(n, bins)`。

## 延伸阅读

- [Python 教程](https://docs.python.org/tutorial/)
- [NumPy 参考手册](../reference/index.html)
- [SciPy 教程](https://docs.scipy.org/doc/scipy/tutorial/index.html)
- [SciPy 讲义](https://scipy-lectures.org)
- [matlab, R, IDL, NumPy/SciPy 对照表](https://mathesaurus.sourceforge.net/)
- [tutorial-svd](https://numpy.org/numpy-tutorials/tutorial-svd)
