# 索引和选择数据 {#indexing-and-selecting-data}

pandas 对象中的轴标签信息有多种用途：

- 使用已知指标标识数据（即提供*元数据*），对分析、可视化和交互式控制台显示非常重要。
- 启用自动和显式的数据对齐。
- 允许直观地获取和设置数据集的子集。

在本节中，我们将重点讨论最后一点：即如何切片、切割以及一般性地获取和设置 pandas 对象的子集。主要焦点将放在 Series 和 DataFrame 上，因为它们在这方面得到了更多的开发关注。

> 注意：Python 和 NumPy 索引运算符 `[]` 和属性运算符 `.` 提供了对 pandas 数据结构快速简便的访问，适用于广泛的用例。这使得交互式工作直观，因为如果你已经知道如何处理 Python 字典和 NumPy 数组，就几乎不需要学习新东西。但是，由于要访问的数据类型事先未知，直接使用标准运算符存在一些优化限制。对于生产代码，我们建议你利用本章中介绍的优化的 pandas 数据访问方法。

请参阅 [MultiIndex / 高级索引](advanced.html#advanced)获取 `MultiIndex` 和更高级的索引文档。

请参阅[烹饪手册](cookbook.html#cookbook-selection)了解一些高级策略。

## 索引的不同选择 {#different-choices-for-indexing}

对象选择经历了许多用户请求的添加，以支持更明确的基于位置的索引。pandas 现在支持三种类型的多轴索引。

- `.loc` 主要基于标签，但也可以与布尔数组一起使用。当找不到项目时，`.loc` 将引发 `KeyError`。允许的输入是：
  - 单个标签，例如 `5` 或 `'a'`（注意 `5` 被解释为索引的*标签*，**不是**沿索引的整数位置。）
  - 标签列表或数组 `['a', 'b', 'c']`
  - 带标签的切片对象 `'a':'f'`（注意与通常的 Python 切片不同，当存在于索引中时，**起始和结束都包含在内！**）
  - 布尔数组（任何 `NA` 值将被视为 `False`）
  - 具有一个参数（调用的 Series 或 DataFrame）并返回有效索引输出的 `callable` 函数
  - 行（和列）索引的元组，其元素是上述输入之一

- `.iloc` 主要基于整数位置（从 `0` 到轴的 `length-1`），但也可以与布尔数组一起使用。如果请求的索引器超出范围，`.iloc` 将引发 `IndexError`，*切片*索引器除外（这符合 Python/NumPy *切片*语义）。允许的输入是：
  - 整数，例如 `5`
  - 整数列表或数组 `[4, 3, 0]`
  - 带整数的切片对象 `1:7`
  - 布尔数组（任何 `NA` 值将被视为 `False`）
  - 具有一个参数（调用的 Series 或 DataFrame）并返回有效索引输出的 `callable` 函数
  - 行（和列）索引的元组，其元素是上述输入之一

- `.loc`、`.iloc` 和 `[]` 索引都可以接受 `callable` 作为索引器。

> 注意：在应用 callable *之前*会先将元组键解构为行（和列）索引，因此你不能从 callable 返回元组来同时索引行和列。

使用多轴选择从对象获取值使用以下表示法（以 `.loc` 为例，但以下也适用于 `.iloc`）。任何轴访问器都可以是空切片 `:`。未在规范中指定的轴被假定为 `:`，例如 `p.loc['a']` 等价于 `p.loc['a', :]`。

```python
In [1]: ser = pd.Series(range(5), index=list("abcde"))

In [2]: ser.loc[["a", "c", "e"]]
Out[2]:
a    0
c    2
e    4
dtype: int64

In [3]: df = pd.DataFrame(np.arange(25).reshape(5, 5), index=list("abcde"), columns=list("abcde"))

In [4]: df.loc[["a", "c", "e"], ["b", "d"]]
Out[4]:
    b   d
a   1   3
c  11  13
e  21  23
```

## 基础知识 {#basics}

如上一节介绍数据结构时所述，使用 `[]`（对熟悉 Python 类行为实现的人来说也称为 `__getitem__`）进行索引的主要功能是选择低维切片。下表显示了使用 `[]` 索引 pandas 对象时的返回类型值：

| 对象类型 | 选择方式 | 返回值类型 |
|---------|---------|-----------|
| Series | `series[label]` | 标量值 |
| DataFrame | `frame[colname]` | 对应于 colname 的 `Series` |

我们构建一个简单的时间序列数据集来说明索引功能：

```python
In [5]: dates = pd.date_range('1/1/2000', periods=8)

In [6]: df = pd.DataFrame(np.random.randn(8, 4),
   ...:                   index=dates, columns=['A', 'B', 'C', 'D'])
   ...: 

In [7]: df
Out[7]:
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
```

> 注意：除非特别说明，否则所有索引功能都不是时间序列特定的。

因此，如上所述，我们有使用 `[]` 的最基本索引：

```python
In [8]: s = df['A']

In [9]: s[dates[5]]
Out[9]: np.float64(-0.6736897080883706)
```

## 按标签选择 {#indexing-label}

使用 `.loc` 可以按标签选择数据。这是 pandas 中推荐的基于标签的索引方法。

```python
In [10]: df.loc[:, 'A']
Out[10]:
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64
```

按标签切片：

```python
In [11]: df.loc['2000-01-01':'2000-01-05', ['A', 'B']]
Out[11]:
                   A         B
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
2000-01-04  0.721555 -0.706771
2000-01-05 -0.424972  0.567020
```

减少返回对象的维度：

```python
In [12]: df.loc['2000-01-01', 'A']
Out[12]: np.float64(0.4691122999071863)
```

## 按位置选择 {#indexing-integer}

使用 `.iloc` 可以按整数位置选择数据。

```python
In [13]: df.iloc[0:3, 0:2]
Out[13]:
                   A         B
2000-01-01  0.469112 -0.282863
2000-01-02  1.212112 -0.173215
2000-01-03 -0.861849 -2.104569
```

按位置切片：

```python
In [14]: df.iloc[[0, 2, 4], [0, 2]]
Out[14]:
                   A         C
2000-01-01  0.469112 -1.509059
2000-01-03 -0.861849 -0.494929
2000-01-05 -0.424972  0.276232
```

## 使用 callable 索引 {#indexing-callable}

`.loc`、`.iloc` 和 `[]` 索引都可以接受一个 callable 作为索引器。callable 必须以 pandas 对象（Series 或 DataFrame）作为唯一参数，并返回有效的索引输出。

```python
In [15]: df.loc[lambda df: df['A'] > 0, :]
Out[15]:
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
```

## 使用布尔索引 {#indexing-boolean}

使用布尔向量可以过滤数据。

```python
In [16]: df[df['A'] > 0]
Out[16]:
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
```

组合多个条件：

```python
In [17]: df[(df['A'] > 0) & (df['B'] < 0)]
Out[17]:
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
```

## 属性访问 {#indexing-attribute-access}

如果 DataFrame 的列名是有效的 Python 标识符，可以使用属性方式访问：

```python
In [18]: df.A
Out[18]:
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64
```

> 注意：属性访问不支持赋值。对于赋值操作，请使用 `.loc` 或 `.iloc`。

## 重新索引 {#reindexing}

[`reindex()`](../reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex") 是 pandas 中重要的基本方法，用于符合新索引集的数据。它用于实现大多数涉及标签对齐的操作。`reindex` 意味着使数据符合一组给定的标签，沿特定轴。

```python
In [19]: s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

In [20]: s
Out[20]:
a    1.695320
b   -1.156883
c   -0.385767
d    0.326457
e    0.167581
dtype: float64

In [21]: s.reindex(['e', 'b', 'f', 'd'])
Out[21]:
e    0.167581
b   -1.156883
f         NaN
d    0.326457
dtype: float64
```

对于 DataFrame，你可以同时在行和列上重新索引：

```python
In [22]: df.reindex(index=['c', 'f', 'b'], columns=['C', 'B', 'A'])
Out[22]:
          C         B         A
c -0.385767 -1.156883  1.695320
f       NaN       NaN       NaN
b -0.385767 -1.156883  1.695320
```

## 使用 `take` 进行选择 {#take}

[`take()`](../reference/api/pandas.DataFrame.take.html#pandas.DataFrame.take "pandas.DataFrame.take") 方法沿轴返回给定位置的元素。

```python
In [23]: s.take([0, 3, 4])
Out[23]:
a    1.695320
d    0.326457
e    0.167581
dtype: float64
```

> 注意：`take` 方法不适用于布尔索引。请使用 `.loc` 或 `.iloc` 代替。

## 索引细节 {#indexing-details}

### 设置与重置索引 {#set-reset-index}

使用 [`set_index()`](../reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index") 将列设置为索引：

```python
In [24]: df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})

In [25]: df.set_index('a')
Out[25]:
   b
a   
1  a
2  b
3  c
```

使用 [`reset_index()`](../reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index") 重置索引：

```python
In [26]: df.set_index('a').reset_index()
Out[26]:
   a  b
0  1  a
1  2  b
2  3  c
```

### 链式索引警告 {#chained-indexing}

避免链式索引（如 `df['A']['B']`），因为它可能产生不可预测的结果。始终使用 `.loc` 或 `.iloc` 进行单次索引操作。

```python
# 不推荐
df['A']['B'] = 1

# 推荐
df.loc[:, ('A', 'B')] = 1
```

## 索引对象 {#index-objects}

pandas 的 [`Index`](../reference/api/pandas.Index.html#pandas.Index "pandas.Index") 类负责存储轴标签和其他元数据（如轴名称或标签）。

### 索引的基本属性 {#index-basic-properties}

```python
In [27]: idx = pd.Index(['a', 'b', 'c'])

In [28]: idx
Out[28]: Index(['a', 'b', 'c'], dtype='object')

In [29]: 'a' in idx
Out[29]: True
```

### 索引的方法 {#index-methods}

索引对象支持集合操作，如并集、交集和差集：

```python
In [30]: idx_a = pd.Index([1, 2, 3, 4])

In [31]: idx_b = pd.Index([3, 4, 5, 6])

In [32]: idx_a.union(idx_b)
Out[32]: Index([1, 2, 3, 4, 5, 6], dtype='int64')

In [33]: idx_a.intersection(idx_b)
Out[33]: Index([3, 4], dtype='int64')

In [34]: idx_a.difference(idx_b)
Out[34]: Index([1, 2], dtype='int64')
```

## MultiIndex（多层次索引） {#multiindex}

MultiIndex 是 pandas 中处理高维数据的强大工具。详见 [MultiIndex / 高级索引](advanced.html#advanced) 章节。
