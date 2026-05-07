# 线性代数（`scipy.linalg`） {#linear-algebra-scipy-linalg}

当 SciPy 使用优化的 ATLAS LAPACK 和 BLAS 库构建时，它具有非常快速的线性代数能力。如果你深入挖掘，所有原始的 LAPACK 和 BLAS 库都可供你使用以获得更快的速度。本节描述了一些更易于使用的接口。

所有这些线性代数例程期望一个可以转换为二维数组的对象。这些例程的输出也是二维数组。

## scipy.linalg vs numpy.linalg {#scipy-linalg-vs-numpy-linalg}

[`scipy.linalg`](../reference/linalg.html#module-scipy.linalg "scipy.linalg") 包含 [numpy.linalg](https://www.numpy.org/devdocs/reference/routines.linalg.html) 中的所有函数，加上一些 `numpy.linalg` 中没有的更高级函数。

使用 `scipy.linalg` 而非 `numpy.linalg` 的另一个优势是它始终使用 BLAS/LAPACK 支持编译，而对于 NumPy 这是可选的。因此，SciPy 版本可能更快，具体取决于 NumPy 的安装方式。

因此，除非你不想将 `scipy` 添加为 `numpy` 程序的依赖项，否则请使用 `scipy.linalg` 而非 `numpy.linalg`。

## numpy.matrix vs 二维 numpy.ndarray {#numpy-matrix-vs-2-d-numpy-ndarray}

表示矩阵的类以及基本操作（如矩阵乘法和转置）是 `numpy` 的一部分。为方便起见，我们在此总结 [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "\(in NumPy v2.4\)") 和 [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") 之间的区别。

`numpy.matrix` 是一个矩阵类，对于矩阵操作具有比 `numpy.ndarray` 更方便的接口。此类支持例如通过分号的 MATLAB 风格创建语法，`*` 运算符默认进行矩阵乘法，并包含作为逆和转置快捷方式的 `I` 和 `T` 成员。

尽管方便，但不鼓励使用 `numpy.matrix` 类，因为它没有添加任何不能用二维 `numpy.ndarray` 对象完成的功能，并可能导致混淆使用的是哪个类。

`scipy.linalg` 操作可以同样应用于 `numpy.matrix` 或二维 `numpy.ndarray` 对象。

## 基本例程 {#basic-routines}

### 求逆矩阵 {#finding-the-inverse}

矩阵 \\(\mathbf{A}\\) 的逆是矩阵 \\(\mathbf{B}\\)，使得 \\(\mathbf{AB}=\mathbf{I}\\)，其中 \\(\mathbf{I}\\) 是沿主对角线为 1 的单位矩阵。通常，\\(\mathbf{B}\\) 表示为 \\(\mathbf{B}=\mathbf{A}^{-1}\\)。在 SciPy 中，NumPy 数组 A 的矩阵逆使用 [`linalg.inv`](../reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv") `(A)` 获取，或者如果 `A` 是 Matrix 则使用 `A.I`。

```python
>>> import numpy as np
>>> from scipy import linalg
>>> A = np.array([[1,3,5],[2,5,1],[2,3,8]])
>>> A
array([[1, 3, 5],
      [2, 5, 1],
      [2, 3, 8]])
>>> linalg.inv(A)
array([[-1.48,  0.36,  0.88],
      [ 0.56,  0.08, -0.36],
      [ 0.16, -0.12,  0.04]])
>>> A.dot(linalg.inv(A))  # 双重检查
array([[  1.00000000e+00,  -1.11022302e-16,  -5.55111512e-17],
      [  3.05311332e-16,   1.00000000e+00,   1.87350135e-16],
      [  2.22044605e-16,  -1.11022302e-16,   1.00000000e+00]])
```

### 解线性方程组 {#solving-a-linear-system}

使用 scipy 命令 [`linalg.solve`](../reference/generated/scipy.linalg.solve.html#scipy.linalg.solve "scipy.linalg.solve") 可以直接解线性方程组。此命令期望输入矩阵和右侧向量，然后计算解向量。提供了输入对称矩阵的选项，在适用时可以加快处理速度。

```python
>>> import numpy as np
>>> from scipy import linalg
>>> A = np.array([[1, 2], [3, 4]])
>>> A
array([[1, 2],
      [3, 4]])
>>> b = np.array([[5], [6]])
>>> b
array([[5],
      [6]])
>>> linalg.inv(A).dot(b)  # 慢
array([[-4. ],
      [ 4.5]])
>>> np.linalg.solve(A, b)  # 快
array([[-4. ],
      [ 4.5]])
```

### 计算行列式 {#computing-determinants}

矩阵的行列式是一个经常需要的标量值。SciPy 中使用 [`linalg.det`](../reference/generated/scipy.linalg.det.html#scipy.linalg.det "scipy.linalg.det") 计算。

```python
>>> A = np.array([[1,2],[3,4]])
>>> linalg.det(A)
-2.0
```

### 特征值和特征向量 {#eigenvalues-and-eigenvectors}

特征值-特征向量问题是线性代数中最常见的问题之一。

```python
>>> A = np.array([[1, 2], [3, 4]])
>>> linalg.eig(A)
(array([-0.37228132+0.j,  5.37228132+0.j]),
 array([[-0.82456484, -0.41597356],
        [ 0.56576746, -0.90937671]]))
```

### 奇异值分解（SVD） {#singular-value-decomposition}

SVD 是另一种常见的线性代数操作。

```python
>>> A = np.array([[1,2,3],[4,5,6]])
>>> M, N = A.shape
>>> U, s, Vh = linalg.svd(A)
>>> Sig = linalg.diagsvd(s, M, N)
>>> U, Sig, Vh
```

### LU 分解 {#lu-decomposition}

LU 分解将矩阵分解为下三角矩阵 L 和上三角矩阵 U 的乘积。

```python
>>> A = np.array([[1,2],[3,4]])
>>> P, L, U = linalg.lu(A)
```

### Cholesky 分解 {#cholesky-decomposition}

Cholesky 分解将正定矩阵分解为下三角矩阵及其转置的乘积。

```python
>>> A = np.array([[6, 3], [3, 5]])
>>> L = linalg.cholesky(A)
>>> L
array([[2.44948974, 0.        ],
       [1.22474487, 1.87082869]])
>>> L.dot(L.T)
array([[6., 3.],
       [3., 5.]])
```

### 矩阵函数 {#matrix-functions}

SciPy 提供了各种矩阵函数：

```python
# 矩阵指数
>>> linalg.expm(A)

# 矩阵对数
>>> linalg.logm(A)

# 矩阵平方根
>>> linalg.sqrtm(A)

# 矩阵正弦/余弦
>>> linalg.sinm(A)
>>> linalg.cosm(A)
```

## 特殊矩阵结构 {#special-matrix-structures}

SciPy 中的线性代数函数通常具有利用矩阵特殊结构的选项。

- 对称矩阵
- 正定矩阵
- 带状矩阵
- 三角矩阵
- Toeplitz 矩阵

## 稀疏矩阵的线性代数 {#sparse-linear-algebra}

对于大型稀疏矩阵，`scipy.sparse.linalg` 提供了专门的算法：

```python
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

A = csc_matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
b = np.array([1, 2, 3])
x = spsolve(A, b)
```
