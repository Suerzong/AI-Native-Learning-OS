# 数据结构入门 {#intro-to-data-structures}

我们将快速、非全面地介绍 pandas 中的基本数据结构，帮助你快速上手。数据类型、索引（index）、轴标签（axis labeling）和对齐（alignment）等基本行为在所有对象中都是通用的。首先，导入 NumPy 并加载 pandas：

```python
In [1]: import numpy as np

In [2]: import pandas as pd
```

从根本上说，**数据对齐是内在的（intrinsic）**。标签与数据之间的链接不会被打破，除非你显式地这样做。

我们将简要介绍数据结构，然后在其他章节中考虑所有大类别的功能和方法。

## Series {#series}

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 是一种一维带标签的数组，能够容纳任何数据类型（整数、字符串、浮点数、Python 对象等）。轴标签统称为**索引（index）**。创建 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的基本方法是调用：

```python
s = pd.Series(data, index=index)
```

这里，`data` 可以是多种不同的形式：

- 一个 Python 字典（dict）
- 一个 ndarray
- 一个标量值（如 5）

传入的**索引（index）**是一个轴标签列表。构造函数的行为取决于**数据（data）**的类型：

**从 ndarray 创建**

如果 `data` 是一个 ndarray，则**索引（index）**必须与**数据（data）**长度相同。如果没有传入索引，将创建一个值为 `[0, ..., len(data) - 1]` 的索引。

```python
In [3]: s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

In [4]: s
Out[4]:
a    0.469112
b   -0.282863
c   -1.509059
d   -1.135632
e    1.212112
dtype: float64

In [5]: s.index
Out[5]: Index(['a', 'b', 'c', 'd', 'e'], dtype='str')

In [6]: pd.Series(np.random.randn(5))
Out[6]:
0   -0.173215
1    0.119209
2   -1.044236
3   -0.861849
4   -2.104569
dtype: float64
```

> 注意：pandas 支持非唯一的索引值。如果尝试执行不支持重复索引值的操作，届时将引发异常。

**从字典创建**

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 可以从字典实例化：

```python
In [7]: d = {"b": 1, "a": 0, "c": 2}

In [8]: pd.Series(d)
Out[8]:
b    1
a    0
c    2
dtype: int64
```

如果传入了索引，将从数据中提取与索引中标签对应的值。

```python
In [9]: d = {"a": 0.0, "b": 1.0, "c": 2.0}

In [10]: pd.Series(d)
Out[10]:
a    0.0
b    1.0
c    2.0
dtype: float64

In [11]: pd.Series(d, index=["b", "c", "d", "a"])
Out[11]:
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
```

> 注意：NaN（Not a Number，非数字）是 pandas 中使用的标准缺失数据标记。

**从标量值创建**

如果 `data` 是一个标量值，该值将被重复以匹配**索引（index）**的长度。如果未提供**索引（index）**，则默认为 `RangeIndex(1)`。

```python
In [12]: pd.Series(5.0, index=["a", "b", "c", "d", "e"])
Out[12]:
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64
```

### Series 类似 ndarray {#series-is-ndarray-like}

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的行为与 [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)") 非常相似，是大多数 NumPy 函数的有效参数。但是，切片等操作也会同时切片索引。

```python
In [13]: s.iloc[0]
Out[13]: np.float64(0.4691122999071863)

In [14]: s.iloc[:3]
Out[14]:
a    0.469112
b   -0.282863
c   -1.509059
dtype: float64

In [15]: s[s > s.median()]
Out[15]:
a    0.469112
e    1.212112
dtype: float64

In [16]: s.iloc[[4, 3, 1]]
Out[16]:
e    1.212112
d   -1.135632
b   -0.282863
dtype: float64

In [17]: np.exp(s)
Out[17]:
a    1.598575
b    0.753623
c    0.221118
d    0.321219
e    3.360575
dtype: float64
```

> 注意：我们将在[索引章节](indexing.html#indexing)中讨论类似 `s.iloc[[4, 3, 1]]` 的基于数组的索引。

与 NumPy 数组类似，pandas [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 也有单一的 [`dtype`](../reference/api/pandas.Series.dtype.html#pandas.Series.dtype "pandas.Series.dtype")。

```python
In [18]: s.dtype
Out[18]: dtype('float64')
```

这通常是 NumPy dtype。但是，pandas 和第三方库在某些地方扩展了 NumPy 的类型系统，在这种情况下 dtype 将是 [`ExtensionDtype`](../reference/api/pandas.api.extensions.ExtensionDtype.html#pandas.api.extensions.ExtensionDtype "pandas.api.extensions.ExtensionDtype")。pandas 中的一些示例包括[分类数据](categorical.html#categorical)和[可空整数数据类型](integer_na.html#integer-na)。更多信息请参阅 [dtypes](basics.html#basics-dtypes)。

如果你需要 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 背后的实际数组，请使用 [`Series.array`](../reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")。

```python
In [19]: s.array
Out[19]:
<NumpyExtensionArray>
[ 0.4691122999071863, -0.2828633443286633, -1.5090585031735124,
 -1.1356323710171934,  1.2121120250208506]
Length: 5, dtype: float64
```

当你需要在没有索引的情况下执行某些操作（例如禁用[自动对齐](#dsintro-alignment)）时，访问数组会很有用。

[`Series.array`](../reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array") 将始终是一个 [`ExtensionArray`](../reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")。简而言之，ExtensionArray 是围绕一个或多个*具体*数组（如 [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.4\)")）的轻量级包装器。pandas 知道如何获取 [`ExtensionArray`](../reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray") 并将其存储在 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列中。更多信息请参阅 [dtypes](basics.html#basics-dtypes)。

虽然 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 类似 ndarray，但如果你需要一个*实际的* ndarray，则请使用 [`Series.to_numpy()`](../reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")。

```python
In [20]: s.to_numpy()
Out[20]: array([ 0.4691, -0.2829, -1.5091, -1.1356,  1.2121])
```

即使 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 由 [`ExtensionArray`](../reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray") 支持，[`Series.to_numpy()`](../reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy") 也会返回一个 NumPy ndarray。

### Series 类似字典 {#series-is-dict-like}

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 也类似于固定大小的字典，你可以通过索引标签获取和设置值：

```python
In [21]: s["a"]
Out[21]: np.float64(0.4691122999071863)

In [22]: s["e"] = 12.0

In [23]: s
Out[23]:
a     0.469112
b    -0.282863
c    -1.509059
d    -1.135632
e    12.000000
dtype: float64

In [24]: "e" in s
Out[24]: True

In [25]: "f" in s
Out[25]: False
```

如果索引中不包含某个标签，将引发异常。

使用 [`Series.get()`](../reference/api/pandas.Series.get.html#pandas.Series.get "pandas.Series.get") 方法，缺失的标签将返回 None 或指定的默认值：

```python
In [27]: s.get("f")

In [28]: s.get("f", np.nan)
Out[28]: nan
```

这些标签也可以通过[属性](indexing.html#indexing-attribute-access)访问。

### Series 的向量化运算与标签对齐 {#vectorized-operations-and-label-alignment-with-series}

在使用原始 NumPy 数组时，通常不需要逐值循环。在 pandas 中使用 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 也是如此。[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 也可以传入大多数期望 ndarray 的 NumPy 方法。

```python
In [29]: s + s
Out[29]:
a     0.938225
b    -0.565727
c    -3.018117
d    -2.271265
e    24.000000
dtype: float64

In [30]: s * 2
Out[30]:
a     0.938225
b    -0.565727
c    -3.018117
d    -2.271265
e    24.000000
dtype: float64

In [31]: np.exp(s)
Out[31]:
a         1.598575
b         0.753623
c         0.221118
d         0.321219
e    162754.791419
dtype: float64
```

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 和 ndarray 之间的一个关键区别是，[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 之间的操作会根据标签自动对齐数据。因此，你可以编写计算而不必考虑涉及的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 是否具有相同的标签。

```python
In [32]: s.iloc[1:] + s.iloc[:-1]
Out[32]:
a         NaN
b   -0.565727
c   -3.018117
d   -2.271265
e         NaN
dtype: float64
```

未对齐的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 之间操作的结果将具有所涉及索引的**并集（union）**。如果某个标签在一个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或另一个中找不到，则结果将标记为缺失 `NaN`。能够在不进行任何显式数据对齐的情况下编写代码，为交互式数据分析和研究提供了巨大的自由度和灵活性。pandas 数据结构的集成数据对齐功能使 pandas 与大多数处理标签数据的相关工具区分开来。

> 注意：通常，我们选择使不同索引对象之间操作的默认结果产生索引的**并集**，以避免信息丢失。虽然数据缺失，但拥有索引标签通常是作为计算一部分的重要信息。你当然可以通过 **dropna** 函数删除带有缺失数据的标签。

### name 属性 {#name-attribute}

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 还有一个 `name` 属性：

```python
In [33]: s = pd.Series(np.random.randn(5), name="something")

In [34]: s
Out[34]:
0   -0.494929
1    1.071804
2    0.721555
3   -0.706771
4   -1.039575
Name: something, dtype: float64

In [35]: s.name
Out[35]: 'something'
```

在许多情况下，[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的 `name` 会被自动分配，特别是从 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中选择单个列时，`name` 将被分配为列标签。

你可以使用 [`pandas.Series.rename()`](../reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename") 方法重命名 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")。

```python
In [36]: s2 = s.rename("different")

In [37]: s2.name
Out[37]: 'different'
```

注意 `s` 和 `s2` 引用的是不同的对象。

## DataFrame {#dataframe}

[`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 是一个二维带标签的数据结构，各列可能具有不同的类型。你可以将其想象为电子表格或 SQL 表，或者是 Series 对象的字典。它通常是最常用的 pandas 对象。与 Series 类似，DataFrame 接受多种不同类型的输入：

- 一维 ndarray、列表、字典或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的字典
- 二维 numpy.ndarray
- [结构化或记录](https://numpy.org/doc/stable/user/basics.rec.html) ndarray
- 一个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")
- 另一个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

除了数据之外，你还可以选择传入**索引（index）**（行标签）和**列（columns）**（列标签）参数。如果你传入了索引和/或列，则保证结果 DataFrame 的索引和/或列。因此，Series 的字典加上特定的索引将丢弃所有与传入索引不匹配的数据。

如果没有传入轴标签，它们将根据输入数据按照常识规则构建。

### 从 Series 或字典的字典创建 {#from-dict-of-series-or-dicts}

结果的**索引（index）**将是各个 Series 索引的**并集（union）**。如果有任何嵌套的字典，它们将首先被转换为 Series。如果没有传入列，则列将是字典键的有序列表。

```python
In [38]: d = {
   ....:     "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
   ....:     "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
   ....: }
   ....:

In [39]: df = pd.DataFrame(d)

In [40]: df
Out[40]:
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0

In [41]: pd.DataFrame(d, index=["d", "b", "a"])
Out[41]:
   one  two
d  NaN  4.0
b  2.0  2.0
a  1.0  1.0

In [42]: pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
Out[42]:
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
```

行标签和列标签可以分别通过访问 **index** 和 **columns** 属性获取。

> 注意：当传入一组特定的列与数据字典一起使用时，传入的列会覆盖字典中的键。

```python
In [43]: df.index
Out[43]: Index(['a', 'b', 'c', 'd'], dtype='str')

In [44]: df.columns
Out[44]: Index(['one', 'two'], dtype='str')
```

### 从 ndarray/列表的字典创建 {#from-dict-of-ndarrays-lists}

所有 ndarray 必须具有相同的长度。如果传入了索引，它也必须与数组长度相同。如果没有传入索引，结果将是 `range(n)`，其中 `n` 是数组长度。

```python
In [45]: d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}

In [46]: pd.DataFrame(d)
Out[46]:
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0

In [47]: pd.DataFrame(d, index=["a", "b", "c", "d"])
Out[47]:
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0
```

### 从结构化或记录数组创建 {#from-structured-or-record-array}

这种情况的处理方式与数组的字典完全相同。

```python
In [48]: data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])

In [49]: data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

In [50]: pd.DataFrame(data)
Out[50]:
   A    B         C
0  1  2.0  b'Hello'
1  2  3.0  b'World'

In [51]: pd.DataFrame(data, index=["first", "second"])
Out[51]:
        A    B         C
first   1  2.0  b'Hello'
second  2  3.0  b'World'

In [52]: pd.DataFrame(data, columns=["C", "A", "B"])
Out[52]:
          C  A    B
0  b'Hello'  1  2.0
1  b'World'  2  3.0
```

> 注意：DataFrame 并非旨在完全像二维 NumPy ndarray 那样工作。

### 从字典列表创建 {#from-a-list-of-dicts}

```python
In [53]: data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]

In [54]: pd.DataFrame(data2)
Out[54]:
   a   b     c
0  1   2   NaN
1  5  10  20.0

In [55]: pd.DataFrame(data2, index=["first", "second"])
Out[55]:
        a   b     c
first   1   2   NaN
second  5  10  20.0

In [56]: pd.DataFrame(data2, columns=["a", "b"])
Out[56]:
   a   b
0  1   2
1  5  10
```

### 从元组字典创建 {#from-a-dict-of-tuples}

你可以通过传入元组字典来自动创建 MultiIndexed 数据框。

```python
In [57]: pd.DataFrame(
   ....:     {
   ....:         ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
   ....:         ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
   ....:         ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
   ....:         ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
   ....:         ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
   ....:     }
   ....: )
   ....:
Out[57]:
       a              b
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
```

### 从 Series 创建 {#from-a-series}

结果将是一个与输入 Series 具有相同索引的 DataFrame，并且有一列，其名称是 Series 的原始名称（仅在未提供其他列名称时）。

```python
In [58]: ser = pd.Series(range(3), index=list("abc"), name="ser")

In [59]: pd.DataFrame(ser)
Out[59]:
   ser
a    0
b    1
c    2
```

### 从命名元组列表创建 {#from-a-list-of-namedtuples}

列表中第一个 `namedtuple` 的字段名称决定 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列。其余的命名元组（或元组）将被简单地解包，它们的值被送入 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的行中。如果其中任何元组比第一个 `namedtuple` 短，则对应行中后面的列将被标记为缺失值。如果其中任何元组长于第一个 `namedtuple`，则会引发 `ValueError`。

```python
In [60]: from collections import namedtuple

In [61]: Point = namedtuple("Point", "x y")

In [62]: pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
Out[62]:
   x  y
0  0  0
1  0  3
2  2  3

In [63]: Point3D = namedtuple("Point3D", "x y z")

In [64]: pd.DataFrame([Point3D(0, 0, 0), Point3D(0, 3, 5), Point(2, 3)])
Out[64]:
   x  y    z
0  0  0  0.0
1  0  3  5.0
2  2  3  NaN
```

### 从数据类列表创建 {#from-a-list-of-dataclasses}

如 [PEP557](https://www.python.org/dev/peps/pep-0557) 中引入的数据类（Data Classes），可以传入 DataFrame 构造函数。传入数据类列表等同于传入字典列表。

请注意，列表中的所有值都应该是数据类，在列表中混合类型将导致 `TypeError`。

```python
In [65]: from dataclasses import make_dataclass

In [66]: Point = make_dataclass("Point", [("x", int), ("y", int)])

In [67]: pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
Out[67]:
   x  y
0  0  0
1  0  3
2  2  3
```

**缺失数据**

要构建带有缺失数据的 DataFrame，我们使用 `np.nan` 来表示缺失值。或者，你可以将 `numpy.MaskedArray` 作为数据参数传递给 DataFrame 构造函数，其被掩蔽的条目将被视为缺失。更多信息请参阅[缺失数据](missing_data.html#missing-data)。

### 替代构造函数 {#alternate-constructors}

**DataFrame.from_dict**

[`DataFrame.from_dict()`](../reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict") 接受字典的字典或类数组序列的字典，并返回 DataFrame。它的操作类似于 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 构造函数，除了 `orient` 参数默认为 `'columns'`，但可以设置为 `'index'` 以使用字典键作为行标签。

```python
In [68]: pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))
Out[68]:
   A  B
0  1  4
1  2  5
2  3  6
```

如果你传入 `orient='index'`，键将成为行标签。在这种情况下，你还可以传入所需的列名：

```python
In [69]: pd.DataFrame.from_dict(
   ....:     dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]),
   ....:     orient="index",
   ....:     columns=["one", "two", "three"],
   ....: )
   ....:
Out[69]:
   one  two  three
A    1    2      3
B    4    5      6
```

**DataFrame.from_records**

[`DataFrame.from_records()`](../reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records") 接受元组列表或具有结构化 dtype 的 ndarray。它的工作方式类似于普通的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 构造函数，不同之处在于结果 DataFrame 的索引可以是结构化 dtype 的特定字段。

### 列的选择、添加、删除 {#column-selection-addition-deletion}

你可以在语义上将 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 视为具有相同索引的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 对象的字典。获取、设置和删除列的工作方式与类似的字典操作使用相同的语法。

列可以像字典一样被删除或弹出。

当插入标量值时，它将自然地被传播以填充整列。

当插入的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 与 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的索引不同时，它将被调整为 DataFrame 的索引。

你可以插入原始 ndarray，但它们的长度必须匹配 DataFrame 索引的长度。

默认情况下，列被插入到末尾。[`DataFrame.insert()`](../reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert "pandas.DataFrame.insert") 可以在列的特定位置插入。

### 在方法链中分配新列 {#assigning-new-columns-in-method-chains}

受 [dplyr 的](https://dplyr.tidyverse.org/reference/mutate.html) `mutate` 动词启发，DataFrame 有一个 [`assign()`](../reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign") 方法，允许你轻松创建可能从现有列派生的新列。

[`assign()`](../reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign") **总是**返回数据的副本，原始 DataFrame 保持不变。

传递可调用对象而不是实际要插入的值，在你手头没有 DataFrame 引用时很有用。这在使用 [`assign()`](../reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign") 进行操作链时很常见。

[`assign()`](../reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign") 的函数签名就是 `**kwargs`。键是新字段的列名，值要么是要插入的值（例如 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 NumPy 数组），要么是在 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 上调用的单参数函数。返回原始 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的*副本*，其中插入了新值。

`**kwargs` 的顺序是保留的。这允许*依赖*赋值，其中 `**kwargs` 中后面的表达式可以引用在同一 [`assign()`](../reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign") 中前面创建的列。

### 索引 / 选择 {#indexing-selection}

索引的基本操作如下：

| 操作 | 语法 | 结果 |
|------|------|------|
| 选择列 | `df[col]` | Series |
| 按标签选择行 | `df.loc[label]` | Series |
| 按整数位置选择行 | `df.iloc[loc]` | Series |
| 切片行 | `df[5:10]` | DataFrame |
| 按布尔向量选择行 | `df[bool_vec]` | DataFrame |

例如，行选择返回一个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")，其索引是 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列。

有关复杂的基于标签的索引和切片的详尽处理，请参阅[索引章节](indexing.html#indexing)。我们将在[重新索引章节](basics.html#basics-reindexing)中讨论重新索引/符合新标签集的基础知识。

### 数据对齐与算术 {#data-alignment-and-arithmetic}

[`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象之间的数据对齐会自动在**列和索引（行标签）**上同时对齐。同样，结果对象将具有列标签和行标签的并集。

当在 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 和 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 之间执行操作时，默认行为是将 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的**索引**与 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的**列**对齐，从而按行[广播](https://numpy.org/doc/stable/user/basics.broadcasting.html)。

有关匹配和广播行为的显式控制，请参阅[灵活二元运算](basics.html#basics-binop)章节。

与标量的算术运算是按元素进行的。

布尔运算符也是按元素操作的。

### 转置 {#transposing}

要转置，访问 `T` 属性或 [`DataFrame.transpose()`](../reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "pandas.DataFrame.transpose")，类似于 ndarray。

### DataFrame 与 NumPy 函数的互操作性 {#dataframe-interoperability-with-numpy-functions}

大多数 NumPy 函数可以直接在 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 和 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 上调用。

[`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 并非旨在成为 ndarray 的直接替代品，因为其索引语义和数据模型在某些地方与 n 维数组有很大不同。

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 实现了 `__array_ufunc__`，这使得它可以与 NumPy 的[通用函数（universal functions）](https://numpy.org/doc/stable/reference/ufuncs.html)一起工作。

ufunc 被应用于 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 中的底层数组。

当多个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 被传递给 ufunc 时，它们会在执行操作之前进行对齐。

与库的其他部分类似，pandas 会自动将带标签的输入对齐，作为具有多个输入的 ufunc 的一部分。

像往常一样，取两个索引的并集，非重叠的值用缺失值填充。

当二元 ufunc 应用于 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 和 [`Index`](../reference/api/pandas.Index.html#pandas.Index "pandas.Index") 时，[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 实现优先，并返回 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")。

NumPy ufunc 可以安全地应用于由非 ndarray 数组支持的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")，例如 [`arrays.SparseArray`](../reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")（参阅[稀疏计算](sparse.html#sparse-calculation)）。如果可能，ufunc 将在不将底层数据转换为 ndarray 的情况下应用。

### 控制台显示 {#console-display}

非常大的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 将被截断以在控制台中显示。你也可以使用 [`info()`](../reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info") 获取摘要。

然而，使用 [`DataFrame.to_string()`](../reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string") 将以表格形式返回 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的字符串表示，尽管它并不总是适合控制台宽度。

宽 DataFrame 默认将在多行上打印。

你可以通过设置 `display.width` 选项来更改单行上打印的内容。

你可以通过设置 `display.max_colwidth` 来调整各个列的最大宽度。

你也可以通过 `expand_frame_repr` 选项禁用此功能。这将以一个整体块打印表格。

### DataFrame 列属性访问和 IPython 补全 {#dataframe-column-attribute-access-and-ipython-completion}

如果 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列标签是有效的 Python 变量名，则可以像属性一样访问该列。

这些列也连接到 [IPython](https://ipython.org) 补全机制，因此可以进行 Tab 补全。
