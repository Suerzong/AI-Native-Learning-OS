[跳转到主要内容](#main-content)

__返回顶部 __ `Ctrl`+`K`

[ ![pandas 3.0.2 文档 - 首页](../_static/pandas.svg) ![pandas 3.0.2 文档 - 首页](https://pandas.pydata.org/static/img/pandas_white.svg) ](../index.html)

  * [ 快速入门 ](../getting_started/index.html)
  * [ 用户指南 ](index.html)
  * [ API 参考 ](../reference/index.html)
  * [ 开发 ](../development/index.html)
  * [ 版本更新 ](../whatsnew/index.html)

__ 搜索 `Ctrl`+`K`

选择版本

______

  * [__ GitHub](https://github.com/pandas-dev/pandas "GitHub")
  * [__ X](https://x.com/pandas_dev "X")
  * [__ Mastodon](https://fosstodon.org/@pandas_dev "Mastodon")

__ 搜索 `Ctrl`+`K`

  * [ 快速入门 ](../getting_started/index.html)
  * [ 用户指南 ](index.html)
  * [ API 参考 ](../reference/index.html)
  * [ 开发 ](../development/index.html)
  * [ 版本更新 ](../whatsnew/index.html)

选择版本

______

  * [__ GitHub](https://github.com/pandas-dev/pandas "GitHub")
  * [__ X](https://x.com/pandas_dev "X")
  * [__ Mastodon](https://fosstodon.org/@pandas_dev "Mastodon")

  * [10 分钟入门 pandas](#)
  * [数据结构简介](dsintro.html)
  * [基本功能](basics.html)
  * [IO 工具（文本、CSV、HDF5 等）](io.html)
  * [PyArrow 功能](pyarrow.html)
  * [索引与数据选取](indexing.html)
  * [MultiIndex / 高级索引](advanced.html)
  * [写时复制（Copy-on-Write, CoW）](copy_on_write.html)
  * [合并、连接、拼接与比较](merging.html)
  * [重塑与透视表](reshaping.html)
  * [文本数据处理](text.html)
  * [缺失数据处理](missing_data.html)
  * [重复标签](duplicates.html)
  * [分类数据](categorical.html)
  * [可空整数数据类型](integer_na.html)
  * [可空布尔数据类型](boolean.html)
  * [图表可视化](visualization.html)
  * [表格可视化](style.html)
  * [用户自定义函数（UDF）](user_defined_functions.html)
  * [分组运算：split-apply-combine](groupby.html)
  * [窗口运算](window.html)
  * [时间序列 / 日期功能](timeseries.html)
  * [时间差（Timedelta）](timedeltas.html)
  * [选项与设置](options.html)
  * [性能优化](enhancingperf.html)
  * [大规模数据集处理](scale.html)
  * [稀疏数据结构](sparse.html)
  * [新字符串数据类型迁移指南（pandas 3.0）](migration-3-strings.html)
  * [常见问题（FAQ）](gotchas.html)
  * [实用技巧手册（Cookbook）](cookbook.html)

  * [ __](../index.html)
  * [用户指南](index.html)
  * 10 分钟入门 pandas

# 10 分钟入门 pandas[#](#minutes-to-pandas "Link to this heading")

这是 pandas 的简短介绍，主要面向新用户。你可以在[实用技巧手册（Cookbook）](cookbook.html#cookbook)中查看更多复杂示例。

通常，我们按如下方式导入：

    In [1]: import numpy as np

    In [2]: import pandas as pd

## pandas 中的基本数据结构[#](#basic-data-structures-in-pandas "Link to this heading")

pandas 提供两类用于处理数据的类：

  1. [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")：一种一维（one-dimensional）标签数组，可容纳任意类型的数据，如整数、字符串、Python 对象等。

  2. [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")：一种二维（two-dimensional）数据结构，以类似二维数组或行列表格的形式保存数据。

## 对象创建[#](#object-creation "Link to this heading")

参阅[数据结构简介](dsintro.html#dsintro)部分。

通过传入一组值创建 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")，让 pandas 自动创建默认的 [`RangeIndex`](../reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")：

    In [3]: s = pd.Series([1, 3, 5, np.nan, 6, 8])

    In [4]: s
    Out[4]:
    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64

通过传入 NumPy 数组和日期时间索引（使用 [`date_range()`](../reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")）以及带标签的列，创建 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")：

    In [5]: dates = pd.date_range("20130101", periods=6)

    In [6]: dates
    Out[6]:
    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[us]', freq='D')

    In [7]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    In [8]: df
    Out[8]:
                       A         B         C         D
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401
    2013-01-06 -0.673690  0.113648 -1.478427  0.524988

通过传入字典对象创建 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")，其中键为列标签，值为列值：

    In [9]: df2 = pd.DataFrame(
       ...:     {
       ...:         "A": 1.0,
       ...:         "B": pd.Timestamp("20130102"),
       ...:         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
       ...:         "D": np.array([3] * 4, dtype="int32"),
       ...:         "E": pd.Categorical(["test", "train", "test", "train"]),
       ...:         "F": "foo",
       ...:     }
       ...: )

    In [10]: df2
    Out[10]:
         A          B    C  D      E    F
    0  1.0 2013-01-02  1.0  3   test  foo
    1  1.0 2013-01-02  1.0  3  train  foo
    2  1.0 2013-01-02  1.0  3   test  foo
    3  1.0 2013-01-02  1.0  3  train  foo

结果 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的各列具有不同的[数据类型（dtypes）](basics.html#basics-dtypes)：

    In [11]: df2.dtypes
    Out[11]:
    A           float64
    B    datetime64[us]
    C           float32
    D             int32
    E          category
    F               str
    dtype: object

如果你使用 IPython，列名（以及公共属性）的 Tab 补全会自动启用。以下是会被补全的部分属性：

    In [12]: df2.<TAB>  # noqa: E225, E999
    df2.A                  df2.bool
    df2.abs                df2.boxplot
    df2.add                df2.C
    df2.add_prefix         df2.clip
    df2.add_suffix         df2.columns
    df2.align              df2.copy
    df2.all                df2.count
    df2.any                df2.combine
    df2.append             df2.D
    df2.apply              df2.describe
    df2.B                  df2.duplicated
    df2.diff

如你所见，列 `A`、`B`、`C` 和 `D` 会自动进行 Tab 补全。`E` 和 `F` 也在其中；其余属性为简洁起见已被截断。

## 查看数据[#](#viewing-data "Link to this heading")

参阅[基本功能](basics.html#basics)部分。

使用 [`DataFrame.head()`](../reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head") 和 [`DataFrame.tail()`](../reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail") 分别查看 DataFrame 的顶部和底部行：

    In [13]: df.head()
    Out[13]:
                       A         B         C         D
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401

    In [14]: df.tail(3)
    Out[14]:
                       A         B         C         D
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401
    2013-01-06 -0.673690  0.113648 -1.478427  0.524988

显示 [`DataFrame.index`](../reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index") 或 [`DataFrame.columns`](../reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")：

    In [15]: df.index
    Out[15]:
    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[us]', freq='D')

    In [16]: df.columns
    Out[16]: Index(['A', 'B', 'C', 'D'], dtype='str')

使用 [`DataFrame.to_numpy()`](../reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy") 返回底层数据的 NumPy 表示（不含索引或列标签）：

    In [17]: df.to_numpy()
    Out[17]:
    array([[ 0.4691, -0.2829, -1.5091, -1.1356],
           [ 1.2121, -0.1732,  0.1192, -1.0442],
           [-0.8618, -2.1046, -0.4949,  1.0718],
           [ 0.7216, -0.7068, -1.0396,  0.2719],
           [-0.425 ,  0.567 ,  0.2762, -1.0874],
           [-0.6737,  0.1136, -1.4784,  0.525 ]])

注意

**NumPy 数组的整个数组只有一个 dtype，而 pandas DataFrame 的每列各有一个 dtype**。调用 [`DataFrame.to_numpy()`](../reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy") 时，pandas 会找到能容纳 DataFrame 中*所有* dtype 的 NumPy dtype。如果公共数据类型是 `object`，[`DataFrame.to_numpy()`](../reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy") 将需要复制数据。

    In [18]: df2.dtypes
    Out[18]:
    A           float64
    B    datetime64[us]
    C           float32
    D             int32
    E          category
    F               str
    dtype: object

    In [19]: df2.to_numpy()
    Out[19]:
    array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
          dtype=object)

[`describe()`](../reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe") 显示数据的快速统计摘要：

    In [20]: df.describe()
    Out[20]:
                  A         B         C         D
    count  6.000000  6.000000  6.000000  6.000000
    mean   0.073711 -0.431125 -0.687758 -0.233103
    std    0.843157  0.922818  0.779887  0.973118
    min   -0.861849 -2.104569 -1.509059 -1.135632
    25%   -0.611510 -0.600794 -1.368714 -1.076610
    50%    0.022070 -0.228039 -0.767252 -0.386188
    75%    0.658444  0.041933 -0.034326  0.461706
    max    1.212112  0.567020  0.276232  1.071804

转置数据：

    In [21]: df.T
    Out[21]:
       2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
    A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
    B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
    C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
    D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988

[`DataFrame.sort_index()`](../reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index") 按轴排序：

    In [22]: df.sort_index(axis=1, ascending=False)
    Out[22]:
                       D         C         B         A
    2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
    2013-01-02 -1.044236  0.119209 -0.173215  1.212112
    2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
    2013-01-04  0.271860 -1.039575 -0.706771  0.721555
    2013-01-05 -1.087401  0.276232  0.567020 -0.424972
    2013-01-06  0.524988 -1.478427  0.113648 -0.673690

[`DataFrame.sort_values()`](../reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values") 按值排序：

    In [23]: df.sort_values(by="B")
    Out[23]:
                       A         B         C         D
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-06 -0.673690  0.113648 -1.478427  0.524988
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401

## 选取[#](#selection "Link to this heading")

注意

虽然标准的 Python / NumPy 表达式在选取和设置数据方面很直观，适用于交互式工作，但对于生产代码，我们推荐使用优化的 pandas 数据访问方法：[`DataFrame.at()`](../reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")、[`DataFrame.iat()`](../reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat")、[`DataFrame.loc()`](../reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") 和 [`DataFrame.iloc()`](../reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")。

参阅索引文档[索引与数据选取](indexing.html#indexing)和[MultiIndex / 高级索引](advanced.html#advanced)。

### Getitem（`[]`）[#](#getitem "Link to this heading")

对于 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")，传入单个标签会选取一列，返回 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")：

    In [24]: df["A"]
    Out[24]:
    2013-01-01    0.469112
    2013-01-02    1.212112
    2013-01-03   -0.861849
    2013-01-04    0.721555
    2013-01-05   -0.424972
    2013-01-06   -0.673690
    Freq: D, Name: A, dtype: float64

如果标签仅包含字母、数字和下划线，你也可以使用列名属性来替代：

    In [25]: df.A
    Out[25]:
    2013-01-01    0.469112
    2013-01-02    1.212112
    2013-01-03   -0.861849
    2013-01-04    0.721555
    2013-01-05   -0.424972
    2013-01-06   -0.673690
    Freq: D, Name: A, dtype: float64

传入列标签列表可选取多列，这对于获取子集或重新排列很有用：

    In [26]: df[["B", "A"]]
    Out[26]:
                       B         A
    2013-01-01 -0.282863  0.469112
    2013-01-02 -0.173215  1.212112
    2013-01-03 -2.104569 -0.861849
    2013-01-04 -0.706771  0.721555
    2013-01-05  0.567020 -0.424972
    2013-01-06  0.113648 -0.673690

对于 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")，传入切片 `:` 会选取匹配的行：

    In [27]: df[0:3]
    Out[27]:
                       A         B         C         D
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

    In [28]: df["20130102":"20130104"]
    Out[28]:
                       A         B         C         D
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860

### 按标签选取[#](#selection-by-label "Link to this heading")

参阅[按标签选取](indexing.html#indexing-label)了解更多，使用 [`DataFrame.loc()`](../reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") 或 [`DataFrame.at()`](../reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")。

选取匹配标签的行：

    In [29]: df.loc[dates[0]]
    Out[29]:
    A    0.469112
    B   -0.282863
    C   -1.509059
    D   -1.135632
    Name: 2013-01-01 00:00:00, dtype: float64

选取所有行（`:`）并指定列标签：

    In [30]: df.loc[:, ["A", "B"]]
    Out[30]:
                       A         B
    2013-01-01  0.469112 -0.282863
    2013-01-02  1.212112 -0.173215
    2013-01-03 -0.861849 -2.104569
    2013-01-04  0.721555 -0.706771
    2013-01-05 -0.424972  0.567020
    2013-01-06 -0.673690  0.113648

标签切片时，两端都*包含*在内：

    In [31]: df.loc["20130102":"20130104", ["A", "B"]]
    Out[31]:
                       A         B
    2013-01-02  1.212112 -0.173215
    2013-01-03 -0.861849 -2.104569
    2013-01-04  0.721555 -0.706771

选取单个行和列标签返回一个标量：

    In [32]: df.loc[dates[0], "A"]
    Out[32]: np.float64(0.4691122999071863)

快速获取标量值（等同于上述方法）：

    In [33]: df.at[dates[0], "A"]
    Out[33]: np.float64(0.4691122999071863)

### 按位置选取[#](#selection-by-position "Link to this heading")

参阅[按位置选取](indexing.html#indexing-integer)了解更多，使用 [`DataFrame.iloc()`](../reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc") 或 [`DataFrame.iat()`](../reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat")。

通过传入整数的位置进行选取：

    In [34]: df.iloc[3]
    Out[34]:
    A    0.721555
    B   -0.706771
    C   -1.039575
    D    0.271860
    Name: 2013-01-04 00:00:00, dtype: float64

整数切片的行为类似于 NumPy/Python：

    In [35]: df.iloc[3:5, 0:2]
    Out[35]:
                       A         B
    2013-01-04  0.721555 -0.706771
    2013-01-05 -0.424972  0.567020

整数位置位置列表：

    In [36]: df.iloc[[1, 2, 4], [0, 2]]
    Out[36]:
                       A         C
    2013-01-02  1.212112  0.119209
    2013-01-03 -0.861849 -0.494929
    2013-01-05 -0.424972  0.276232

显式切分行：

    In [37]: df.iloc[1:3, :]
    Out[37]:
                       A         B         C         D
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

显式切分列：

    In [38]: df.iloc[:, 1:3]
    Out[38]:
                       B         C
    2013-01-01 -0.282863 -1.509059
    2013-01-02 -0.173215  0.119209
    2013-01-03 -2.104569 -0.494929
    2013-01-04 -0.706771 -1.039575
    2013-01-05  0.567020  0.276232
    2013-01-06  0.113648 -1.478427

显式获取值：

    In [39]: df.iloc[1, 1]
    Out[39]: np.float64(-0.17321464905330858)

快速获取标量值（等同于上述方法）：

    In [40]: df.iat[1, 1]
    Out[40]: np.float64(-0.17321464905330858)

### 布尔索引[#](#boolean-indexing "Link to this heading")

选取 `df.A` 大于 `0` 的行：

    In [41]: df[df["A"] > 0]
    Out[41]:
                       A         B         C         D
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860

从 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中选取满足布尔条件的值：

    In [42]: df[df > 0]
    Out[42]:
                       A         B         C         D
    2013-01-01  0.469112       NaN       NaN       NaN
    2013-01-02  1.212112       NaN  0.119209       NaN
    2013-01-03       NaN       NaN       NaN  1.071804
    2013-01-04  0.721555       NaN       NaN  0.271860
    2013-01-05       NaN  0.567020  0.276232       NaN
    2013-01-06       NaN  0.113648       NaN  0.524988

使用 [`isin()`](../reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin") 方法进行过滤：

    In [43]: df2 = df.copy()

    In [44]: df2["E"] = ["one", "one", "two", "three", "four", "three"]

    In [45]: df2
    Out[45]:
                       A         B         C         D      E
    2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
    2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
    2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
    2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three

    In [46]: df2[df2["E"].isin(["two", "four"])]
    Out[46]:
                       A         B         C         D     E
    2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
    2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four

### 赋值[#](#setting "Link to this heading")

设置新列会自动按索引对齐数据：

    In [47]: s1 = pd.Series(
       ....:    [1, 2, 3, 4, 5, 6],
       ....:    index=pd.date_range("20130102", periods=6))

    In [48]: s1
    Out[48]:
    2013-01-02    1
    2013-01-03    2
    2013-01-04    3
    2013-01-05    4
    2013-01-06    5
    2013-01-07    6
    Freq: D, dtype: int64

    In [49]: df["F"] = s1

按标签赋值：

    In [50]: df.at[dates[0], "A"] = 0

按位置赋值：

    In [51]: df.iat[0, 1] = 0

通过 NumPy 数组赋值：

    In [52]: df.loc[:, "D"] = np.array([5] * len(df))

上述赋值操作的结果：

    In [53]: df
    Out[53]:
                       A         B         C    D    F
    2013-01-01  0.000000  0.000000 -1.509059  5.0  NaN
    2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0
    2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0
    2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0
    2013-01-05 -0.424972  0.567020  0.276232  5.0  4.0
    2013-01-06 -0.673690  0.113648 -1.478427  5.0  5.0

使用 `where` 操作进行赋值：

    In [54]: df2 = df.copy()

    In [55]: df2[df2 > 0] = -df2

    In [56]: df2
    Out[56]:
                       A         B         C    D    F
    2013-01-01  0.000000  0.000000 -1.509059 -5.0  NaN
    2013-01-02 -1.212112 -0.173215 -0.119209 -5.0 -1.0
    2013-01-03 -0.861849 -2.104569 -0.494929 -5.0 -2.0
    2013-01-04 -0.721555 -0.706771 -1.039575 -5.0 -3.0
    2013-01-05 -0.424972 -0.567020 -0.276232 -5.0 -4.0
    2013-01-06 -0.673690 -0.113648 -1.478427 -5.0 -5.0

## 缺失数据[#](#missing-data "Link to this heading")

对于 NumPy 数据类型，`np.nan` 表示缺失数据。默认情况下不参与计算。参阅[缺失数据](missing_data.html#missing-data)部分。

重建索引（Reindexing）允许你在指定轴上更改/添加/删除索引。这会返回数据的副本：

    In [57]: df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

    In [58]: df1.loc[dates[0] : dates[1], "E"] = 1

    In [59]: df1
    Out[59]:
                       A         B         C    D    F    E
    2013-01-01  0.000000  0.000000 -1.509059  5.0  NaN  1.0
    2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
    2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0  NaN
    2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0  NaN

[`DataFrame.dropna()`](../reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna") 删除任何含有缺失数据的行：

    In [60]: df1.dropna(how="any")
    Out[60]:
                       A         B         C    D    F    E
    2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0

[`DataFrame.fillna()`](../reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna") 填充缺失数据：

    In [61]: df1.fillna(value=5)
    Out[61]:
                       A         B         C    D    F    E
    2013-01-01  0.000000  0.000000 -1.509059  5.0  5.0  1.0
    2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
    2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0  5.0
    2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0  5.0

[`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna") 获取值为 `nan` 的布尔掩码：

    In [62]: pd.isna(df1)
    Out[62]:
                    A      B      C      D      F      E
    2013-01-01  False  False  False  False   True  False
    2013-01-02  False  False  False  False  False  False
    2013-01-03  False  False  False  False  False   True
    2013-01-04  False  False  False  False  False   True

## 运算[#](#operations "Link to this heading")

参阅[二元运算基础](basics.html#basics-binop)部分。

### 统计[#](#stats "Link to this heading")

运算通常*排除*缺失数据。

计算每列的平均值：

    In [63]: df.mean()
    Out[63]:
    A   -0.004474
    B   -0.383981
    C   -0.687758
    D    5.000000
    F    3.000000
    dtype: float64

计算每行的平均值：

    In [64]: df.mean(axis=1)
    Out[64]:
    2013-01-01    0.872735
    2013-01-02    1.431621
    2013-01-03    0.707731
    2013-01-04    1.395042
    2013-01-05    1.883656
    2013-01-06    1.592306
    Freq: D, dtype: float64

与不同索引的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 运算时，结果会按索引或列标签的并集对齐。此外，pandas 会沿指定维度自动广播，并用 `np.nan` 填充未对齐的标签。

    In [65]: s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

    In [66]: s
    Out[66]:
    2013-01-01    NaN
    2013-01-02    NaN
    2013-01-03    1.0
    2013-01-04    3.0
    2013-01-05    5.0
    2013-01-06    NaN
    Freq: D, dtype: float64

    In [67]: df.sub(s, axis="index")
    Out[67]:
                       A         B         C    D    F
    2013-01-01       NaN       NaN       NaN  NaN  NaN
    2013-01-02       NaN       NaN       NaN  NaN  NaN
    2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
    2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
    2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
    2013-01-06       NaN       NaN       NaN  NaN  NaN

### 用户自定义函数[#](#user-defined-functions "Link to this heading")

[`DataFrame.agg()`](../reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg") 和 [`DataFrame.transform()`](../reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform") 分别应用归约或广播结果的用户自定义函数。

    In [68]: df.agg(lambda x: np.mean(x) * 5.6)
    Out[68]:
    A    -0.025054
    B    -2.150294
    C    -3.851445
    D    28.000000
    F    16.800000
    dtype: float64

    In [69]: df.transform(lambda x: x * 101.2)
    Out[69]:
                         A           B           C      D      F
    2013-01-01    0.000000    0.000000 -152.716721  506.0    NaN
    2013-01-02  122.665737  -17.529322   12.063922  506.0  101.2
    2013-01-03  -87.219115 -212.982405  -50.086843  506.0  202.4
    2013-01-04   73.021382  -71.525239 -105.204988  506.0  303.6
    2013-01-05  -43.007200   57.382459   27.954680  506.0  404.8
    2013-01-06  -68.177398   11.501219 -149.616767  506.0  506.0

### 值计数[#](#value-counts "Link to this heading")

参阅[直方图与离散化](basics.html#basics-discretization)了解更多。

    In [70]: s = pd.Series(np.random.randint(0, 7, size=10))

    In [71]: s
    Out[71]:
    0    4
    1    2
    2    1
    3    2
    4    6
    5    4
    6    4
    7    6
    8    4
    9    4
    dtype: int64

    In [72]: s.value_counts()
    Out[72]:
    4    5
    2    2
    6    2
    1    1
    Name: count, dtype: int64

### 字符串方法[#](#string-methods "Link to this heading")

[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 在 `str` 属性中配备了一组字符串处理方法，使得对数组中每个元素的操作变得简单，如以下代码片段所示。参阅[向量化字符串方法](text.html#text-string-methods)了解更多。

    In [73]: s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

    In [74]: s.str.lower()
    Out[74]:
    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5     NaN
    6    caba
    7     dog
    8     cat
    dtype: str

## 合并[#](#merge "Link to this heading")

### 拼接[#](#concat "Link to this heading")

pandas 提供了多种便捷工具，用于将 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 和 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象以各种集合逻辑组合在一起，以及用于连接/合并类型操作的关系代数功能。

参阅[合并](merging.html#merging)部分。

使用 [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 按行拼接 pandas 对象：

    In [75]: df = pd.DataFrame(np.random.randn(10, 4))

    In [76]: df
    Out[76]:
              0         1         2         3
    0 -0.548702  1.467327 -1.015962 -0.483075
    1  1.637550 -1.217659 -0.291519 -1.745505
    2 -0.263952  0.991460 -0.919069  0.266046
    3 -0.709661  1.669052  1.037882 -1.705775
    4 -0.919854 -0.042379  1.247642 -0.009920
    5  0.290213  0.495767  0.362949  1.548106
    6 -1.131345 -0.089329  0.337863 -0.945867
    7 -0.932132  1.956030  0.017587 -0.016692
    8 -0.575247  0.254161 -1.143704  0.215897
    9  1.193555 -0.077118 -0.408530 -0.862495

    # 将其拆分为多块
    In [77]: pieces = [df[:3], df[3:7], df[7:]]

    In [78]: pd.concat(pieces)
    Out[78]:
              0         1         2         3
    0 -0.548702  1.467327 -1.015962 -0.483075
    1  1.637550 -1.217659 -0.291519 -1.745505
    2 -0.263952  0.991460 -0.919069  0.266046
    3 -0.709661  1.669052  1.037882 -1.705775
    4 -0.919854 -0.042379  1.247642 -0.009920
    5  0.290213  0.495767  0.362949  1.548106
    6 -1.131345 -0.089329  0.337863 -0.945867
    7 -0.932132  1.956030  0.017587 -0.016692
    8 -0.575247  0.254161 -1.143704  0.215897
    9  1.193555 -0.077118 -0.408530 -0.862495

注意

向 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 添加列相对较快。然而，添加行需要复制数据，可能代价较高。我们建议将预构建的记录列表传递给 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 构造函数，而不是通过迭代追加记录来构建 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")。

### 连接[#](#join "Link to this heading")

[`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge") 实现了 SQL 风格的连接类型。参阅[数据库风格连接](merging.html#merging-join)部分。

    In [79]: left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

    In [80]: right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

    In [81]: left
    Out[81]:
       key  lval
    0  foo     1
    1  foo     2

    In [82]: right
    Out[82]:
       key  rval
    0  foo     4
    1  foo     5

    In [83]: pd.merge(left, right, on="key")
    Out[83]:
       key  lval  rval
    0  foo     1     4
    1  foo     1     5
    2  foo     2     4
    3  foo     2     5

在唯一键上 [`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge")：

    In [84]: left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})

    In [85]: right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

    In [86]: left
    Out[86]:
       key  lval
    0  foo     1
    1  bar     2

    In [87]: right
    Out[87]:
       key  rval
    0  foo     4
    1  bar     5

    In [88]: pd.merge(left, right, on="key")
    Out[88]:
       key  lval  rval
    0  foo     1     4
    1  bar     2     5

## 分组[#](#grouping "Link to this heading")

"分组（group by）"指的是涉及以下一个或多个步骤的过程：

  * **拆分（Splitting）**：按某种标准将数据拆分为若干组
  * **应用（Applying）**：对每组独立应用函数
  * **合并（Combining）**：将结果合并为数据结构

参阅[分组](groupby.html#groupby)部分。

    In [89]: df = pd.DataFrame(
       ....:     {
       ....:         "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
       ....:         "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
       ....:         "C": np.random.randn(8),
       ....:         "D": np.random.randn(8),
       ....:     }
       ....: )

    In [90]: df
    Out[90]:
         A      B         C         D
    0  foo    one  1.346061 -1.577585
    1  bar    one  1.511763  0.396823
    2  foo    two  1.627081 -0.105381
    3  bar  three -0.990582 -0.532532
    4  foo    two -0.441652  1.453749
    5  bar    two  1.211526  1.208843
    6  foo    one  0.268520 -0.080952
    7  foo  three  0.024580 -0.264610

按列标签分组，选取列标签，然后对结果分组应用 [`DataFrameGroupBy.sum()`](../reference/api/pandas.api.typing.DataFrameGroupBy.sum.html#pandas.api.typing.DataFrameGroupBy.sum "pandas.api.typing.DataFrameGroupBy.sum") 函数：

    In [91]: df.groupby("A")[["C", "D"]].sum()
    Out[91]:
                C         D
    A
    bar  1.732707  1.073134
    foo  2.824590 -0.574779

按多个列标签分组会形成 [`MultiIndex`](../reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")：

    In [92]: df.groupby(["A", "B"]).sum()
    Out[92]:
                      C         D
    A   B
    bar one    1.511763  0.396823
        three -0.990582 -0.532532
        two    1.211526  1.208843
    foo one    1.614581 -1.658537
        three  0.024580 -0.264610
        two    1.185429  1.348368

## 重塑[#](#reshaping "Link to this heading")

参阅[层次化索引](advanced.html#advanced-hierarchical)和[重塑](reshaping.html#reshaping-stacking)部分。

### 堆叠[#](#stack "Link to this heading")

    In [93]: arrays = [
       ....:    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
       ....:    ["one", "two", "one", "two", "one", "two", "one", "two"],
       ....: ]

    In [94]: index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])

    In [95]: df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

    In [96]: df2 = df[:4]

    In [97]: df2
    Out[97]:
                         A         B
    first second
    bar   one    -0.727965 -0.589346
          two     0.339969 -0.693205
    baz   one    -0.339355  0.593616
          two     0.884345  1.591431

[`stack()`](../reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack") 方法"压缩" DataFrame 列中的一个层级：

    In [98]: stacked = df2.stack()

    In [99]: stacked
    Out[99]:
    first  second
    bar    one     A   -0.727965
                   B   -0.589346
           two     A    0.339969
                   B   -0.693205
    baz    one     A   -0.339355
                   B    0.593616
           two     A    0.884345
                   B    1.591431
    dtype: float64

对于"已堆叠"的 DataFrame 或 Series（将 [`MultiIndex`](../reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex") 作为 `index`），[`stack()`](../reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack") 的逆运算是 [`unstack()`](../reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")，默认展开**最后一层**：

    In [100]: stacked.unstack()
    Out[100]:
                         A         B
    first second
    bar   one    -0.727965 -0.589346
          two     0.339969 -0.693205
    baz   one    -0.339355  0.593616
          two     0.884345  1.591431

    In [101]: stacked.unstack(1)
    Out[101]:
    second        one       two
    first
    bar   A -0.727965  0.339969
          B -0.589346 -0.693205
    baz   A -0.339355  0.884345
          B  0.593616  1.591431

    In [102]: stacked.unstack(0)
    Out[102]:
    first          bar       baz
    second
    one    A -0.727965 -0.339355
           B -0.589346  0.593616
    two    A  0.339969  0.884345
           B -0.693205  1.591431

### 透视表[#](#pivot-tables "Link to this heading")

参阅[透视表](reshaping.html#reshaping-pivot)部分。

    In [103]: df = pd.DataFrame(
       .....:     {
       .....:         "A": ["one", "one", "two", "three"] * 3,
       .....:         "B": ["A", "B", "C"] * 4,
       .....:         "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
       .....:         "D": np.random.randn(12),
       .....:         "E": np.random.randn(12),
       .....:     }
       .....: )

    In [104]: df
    Out[104]:
            A  B    C         D         E
    0     one  A  foo -1.202872  0.047609
    1     one  B  foo -1.814470 -0.136473
    2     two  C  foo  1.018601 -0.561757
    3   three  A  bar -0.595447 -1.623033
    4     one  B  bar  1.395433  0.029399
    5     one  C  bar -0.392670 -0.542108
    6     two  A  foo  0.007207  0.282696
    7   three  B  foo  1.928123 -0.087302
    8     one  C  foo -0.055224 -1.575170
    9     one  A  bar  2.395985  1.771208
    10    two  B  bar  1.552825  0.816482
    11  three  C  bar  0.166599  1.100230

[`pivot_table()`](../reference/api/pandas.pivot_table.html#pandas.pivot_table "pandas.pivot_table") 通过指定 `values`、`index` 和 `columns` 对 DataFrame 进行透视：

    In [105]: pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
    Out[105]:
    C             bar       foo
    A     B
    one   A  2.395985 -1.202872
          B  1.395433 -1.814470
          C -0.392670 -0.055224
    three A -0.595447       NaN
          B       NaN  1.928123
          C  0.166599       NaN
    two   A       NaN  0.007207
          B  1.552825       NaN
          C       NaN  1.018601

## 时间序列[#](#time-series "Link to this heading")

pandas 提供了简单、强大且高效的功能，用于在频率转换期间执行重采样操作（例如，将秒级数据转换为 5 分钟数据）。这在金融应用中极为常见，但不限于此。参阅[时间序列](timeseries.html#timeseries)部分。

    In [106]: rng = pd.date_range("1/1/2012", periods=100, freq="s")

    In [107]: ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

    In [108]: ts.resample("5Min").sum()
    Out[108]:
    2012-01-01    24182
    Freq: 5min, dtype: int64

[`Series.tz_localize()`](../reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "pandas.Series.tz_localize") 将时间序列本地化到时区：

    In [109]: rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

    In [110]: ts = pd.Series(np.random.randn(len(rng)), rng)

    In [111]: ts
    Out[111]:
    2012-03-06    1.857704
    2012-03-07   -1.193545
    2012-03-08    0.677510
    2012-03-09   -0.153931
    2012-03-10    0.520091
    Freq: D, dtype: float64

    In [112]: ts_utc = ts.tz_localize("UTC")

    In [113]: ts_utc
    Out[113]:
    2012-03-06 00:00:00+00:00    1.857704
    2012-03-07 00:00:00+00:00   -1.193545
    2012-03-08 00:00:00+00:00    0.677510
    2012-03-09 00:00:00+00:00   -0.153931
    2012-03-10 00:00:00+00:00    0.520091
    Freq: D, dtype: float64

[`Series.tz_convert()`](../reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert "pandas.Series.tz_convert") 将时区感知的时间序列转换为另一个时区：

    In [114]: ts_utc.tz_convert("US/Eastern")
    Out[114]:
    2012-03-05 19:00:00-05:00    1.857704
    2012-03-06 19:00:00-05:00   -1.193545
    2012-03-07 19:00:00-05:00    0.677510
    2012-03-08 19:00:00-05:00   -0.153931
    2012-03-09 19:00:00-05:00    0.520091
    dtype: float64

添加非固定时长（[`BusinessDay`](../reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")）到时间序列：

    In [115]: rng
    Out[115]:
    DatetimeIndex(['2012-03-06', '2012-03-07', '2012-03-08', '2012-03-09',
                   '2012-03-10'],
                  dtype='datetime64[us]', freq='D')

    In [116]: rng + pd.offsets.BusinessDay(5)
    Out[116]:
    DatetimeIndex(['2012-03-13', '2012-03-14', '2012-03-15', '2012-03-16',
                   '2012-03-16'],
                  dtype='datetime64[us]', freq=None)

## 分类数据[#](#categoricals "Link to this heading")

pandas 可以在 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中包含分类数据。完整文档请参阅[分类数据介绍](categorical.html#categorical)和 [API 文档](../reference/arrays.html#api-arrays-categorical)。

    In [117]: df = pd.DataFrame(
       .....:     {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
       .....: )

将原始成绩转换为分类数据类型：

    In [118]: df["grade"] = df["raw_grade"].astype("category")

    In [119]: df["grade"]
    Out[119]:
    0    a
    1    b
    2    b
    3    a
    4    a
    5    e
    Name: grade, dtype: category
    Categories (3, str): ['a', 'b', 'e']

将分类重命名为更有意义的名称：

    In [120]: new_categories = ["very good", "good", "very bad"]

    In [121]: df["grade"] = df["grade"].cat.rename_categories(new_categories)

重新排序分类并同时添加缺失的分类（[`Series.cat()`](../reference/api/pandas.Series.cat.html#pandas.Series.cat "pandas.Series.cat") 下的方法默认返回新的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")）：

    In [122]: df["grade"] = df["grade"].cat.set_categories(
       .....:     ["very bad", "bad", "medium", "good", "very good"]
       .....: )

    In [123]: df["grade"]
    Out[123]:
    0    very good
    1         good
    2         good
    3    very good
    4    very good
    5     very bad
    Name: grade, dtype: category
    Categories (5, str): ['very bad', 'bad', 'medium', 'good', 'very good']

排序按分类的顺序，而非字典顺序：

    In [124]: df.sort_values(by="grade")
    Out[124]:
       id raw_grade      grade
    5   6         e   very bad
    1   2         b       good
    2   3         b       good
    0   1         a  very good
    3   4         a  very good
    4   5         a  very good

使用 `observed=False` 按分类列分组也会显示空分类：

    In [125]: df.groupby("grade", observed=False).size()
    Out[125]:
    grade
    very bad     1
    bad          0
    medium       0
    good         2
    very good    3
    dtype: int64

## 绘图[#](#plotting "Link to this heading")

参阅[绘图](visualization.html#visualization)文档。

我们使用标准约定引用 matplotlib API：

    In [126]: import matplotlib.pyplot as plt

    In [127]: plt.close("all")

`plt.close` 方法用于[关闭](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html)图形窗口：

    In [128]: ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

    In [129]: ts = ts.cumsum()

    In [130]: ts.plot();

![../_images/series_plot_basic.png](../_images/series_plot_basic.png)

注意

使用 Jupyter 时，图表会通过 [`plot()`](../reference/api/pandas.Series.plot.html#pandas.Series.plot "pandas.Series.plot") 显示。否则使用 [matplotlib.pyplot.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) 来显示，或使用 [matplotlib.pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) 写入文件。

[`plot()`](../reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot") 绘制所有列：

    In [131]: df = pd.DataFrame(
       .....:     np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
       .....: )

    In [132]: df = df.cumsum()

    In [133]: plt.figure();

    In [134]: df.plot();

    In [135]: plt.legend(loc='best');

![../_images/frame_plot_basic.png](../_images/frame_plot_basic.png)

## 数据导入与导出[#](#importing-and-exporting-data "Link to this heading")

参阅[IO 工具](io.html#io)部分。

### CSV[#](#csv "Link to this heading")

[写入 CSV 文件：](io.html#io-store-in-csv) 使用 [`DataFrame.to_csv()`](../reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

    In [136]: df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))

    In [137]: df.to_csv("foo.csv")

[从 CSV 文件读取：](io.html#io-read-csv-table) 使用 [`read_csv()`](../reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

    In [138]: pd.read_csv("foo.csv")
    Out[138]:
       Unnamed: 0  0  1  2  3  4
    0           0  4  3  1  1  2
    1           1  1  0  2  3  2
    2           2  1  4  2  1  2
    3           3  0  4  0  2  2
    4           4  4  2  2  3  4
    5           5  4  0  4  3  1
    6           6  2  1  2  0  3
    7           7  4  0  4  4  4
    8           8  4  4  1  0  1
    9           9  0  4  3  0  3

### Parquet[#](#parquet "Link to this heading")

写入 Parquet 文件：

    In [139]: df.to_parquet("foo.parquet")

从 Parquet 文件读取，使用 [`read_parquet()`](../reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")：

    In [140]: pd.read_parquet("foo.parquet")
    Out[140]:
       0  1  2  3  4
    0  4  3  1  1  2
    1  1  0  2  3  2
    2  1  4  2  1  2
    3  0  4  0  2  2
    4  4  2  2  3  4
    5  4  0  4  3  1
    6  2  1  2  0  3
    7  4  0  4  4  4
    8  4  4  1  0  1
    9  0  4  3  0  3

### Excel[#](#excel "Link to this heading")

读写 [Excel](io.html#io-excel)。

使用 [`DataFrame.to_excel()`](../reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel") 写入 Excel 文件：

    In [141]: df.to_excel("foo.xlsx", sheet_name="Sheet1")

使用 [`read_excel()`](../reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel") 从 Excel 文件读取：

    In [142]: pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
    Out[142]:
       Unnamed: 0  0  1  2  3  4
    0           0  4  3  1  1  2
    1           1  1  0  2  3  2
    2           2  1  4  2  1  2
    3           3  0  4  0  2  2
    4           4  4  2  2  3  4
    5           5  4  0  4  3  1
    6           6  2  1  2  0  3
    7           7  4  0  4  4  4
    8           8  4  4  1  0  1
    9           9  0  4  3  0  3

## 注意事项[#](#gotchas "Link to this heading")

如果你尝试对 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 执行布尔操作，可能会看到类似以下异常：

    In [143]: if pd.Series([False, True, False]):
       .....:      print("I was true")
       .....:
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-143-b27eb9c1dfc0> in ?()
    ----> 1 if pd.Series([False, True, False]):
          2      print("I was true")

    ~/work/pandas/pandas/pandas/core/generic.py in ?(self)
       1511     @final
       1512     def __bool__(self) -> NoReturn:
    -> 1513         raise ValueError(
       1514             f"The truth value of a {type(self).__name__} is ambiguous. "
       1515             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
       1516         )

    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

参阅[比较](basics.html#basics-compare)和[注意事项](gotchas.html#gotchas)了解解释及应对方法。

[ __ 上一页 用户指南 ](index.html "previous page") [ 下一页 数据结构简介 __](dsintro.html "next page")

__本页目录

  * [pandas 中的基本数据结构](#basic-data-structures-in-pandas)
  * [对象创建](#object-creation)
  * [查看数据](#viewing-data)
  * [选取](#selection)
    * [Getitem（`[]`）](#getitem)
    * [按标签选取](#selection-by-label)
    * [按位置选取](#selection-by-position)
    * [布尔索引](#boolean-indexing)
    * [赋值](#setting)
  * [缺失数据](#missing-data)
  * [运算](#operations)
    * [统计](#stats)
    * [用户自定义函数](#user-defined-functions)
    * [值计数](#value-counts)
    * [字符串方法](#string-methods)
  * [合并](#merge)
    * [拼接](#concat)
    * [连接](#join)
  * [分组](#grouping)
  * [重塑](#reshaping)
    * [堆叠](#stack)
    * [透视表](#pivot-tables)
  * [时间序列](#time-series)
  * [分类数据](#categoricals)
  * [绘图](#plotting)
  * [数据导入与导出](#importing-and-exporting-data)
    * [CSV](#csv)
    * [Parquet](#parquet)
    * [Excel](#excel)
  * [注意事项](#gotchas)

(C) 2026, pandas via [NumFOCUS, Inc.](https://numfocus.org) Hosted by [OVHcloud](https://www.ovhcloud.com).

Created using [Sphinx](https://www.sphinx-doc.org/) 9.0.4.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.
