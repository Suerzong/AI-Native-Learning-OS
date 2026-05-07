# 处理缺失数据 {#working-with-missing-data}

## 被视为"缺失"的值 {#values-considered-missing}

pandas 使用不同的哨兵值（sentinel values）来表示缺失（也称为 NA），具体取决于数据类型。

对于 NumPy 数据类型，使用 `numpy.nan`。使用 NumPy 数据类型的缺点是原始数据类型会被强制转换为 `np.float64` 或 `object`。

```python
In [1]: pd.Series([1, 2], dtype=np.int64).reindex([0, 1, 2])
Out[1]:
0    1.0
1    2.0
2    NaN
dtype: float64

In [2]: pd.Series([True, False], dtype=np.bool_).reindex([0, 1, 2])
Out[2]:
0     True
1    False
2      NaN
dtype: object
```

对于 NumPy `np.datetime64`、`np.timedelta64` 和 [`PeriodDtype`](../reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")，使用 [`NaT`](../reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")。对于类型标注应用，请使用 `api.typing.NaTType`。

```python
In [3]: pd.Series([1, 2], dtype=np.dtype("timedelta64[ns]")).reindex([0, 1, 2])
Out[3]:
0   0 days 00:00:00.000000001
1   0 days 00:00:00.000000002
2                         NaT
dtype: timedelta64[ns]

In [4]: pd.Series([1, 2], dtype=np.dtype("datetime64[ns]")).reindex([0, 1, 2])
Out[4]:
0   1970-01-01 00:00:00.000000001
1   1970-01-01 00:00:00.000000002
2                             NaT
dtype: datetime64[ns]

In [5]: pd.Series(["2020", "2020"], dtype=pd.PeriodDtype("D")).reindex([0, 1, 2])
Out[5]:
0    2020-01-01
1    2020-01-01
2           NaT
dtype: period[D]
```

对于 [`StringDtype`](../reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")、[`Int64Dtype`](../reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")（及其他位宽）、[`Float64Dtype`](../reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "pandas.Float64Dtype")（及其他位宽）、[`BooleanDtype`](../reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype") 和 [`ArrowDtype`](../reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")，使用 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")。这些类型将维护数据的原始数据类型。对于类型标注应用，请使用 `api.typing.NAType`。

```python
In [6]: pd.Series([1, 2], dtype="Int64").reindex([0, 1, 2])
Out[6]:
0       1
1       2
2    <NA>
dtype: Int64

In [7]: pd.Series([True, False], dtype="boolean[pyarrow]").reindex([0, 1, 2])
Out[7]:
0     True
1    False
2     <NA>
dtype: bool[pyarrow]
```

要检测这些缺失值，请使用 [`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna") 或 [`notna()`](../reference/api/pandas.notna.html#pandas.notna "pandas.notna") 方法。

```python
In [8]: ser = pd.Series([pd.Timestamp("2020-01-01"), pd.NaT])

In [9]: ser
Out[9]:
0   2020-01-01
1          NaT
dtype: datetime64[us]

In [10]: pd.isna(ser)
Out[10]:
0    False
1     True
dtype: bool
```

> 注意：[`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna") 或 [`notna()`](../reference/api/pandas.notna.html#pandas.notna "pandas.notna") 也会将 `None` 视为缺失值。

```python
In [11]: ser = pd.Series([1, None], dtype=object)

In [12]: ser
Out[12]:
0       1
1    None
dtype: object

In [13]: pd.isna(ser)
Out[13]:
0    False
1     True
dtype: bool
```

> 警告：`np.nan`、[`NaT`](../reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT") 和 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 之间的相等比较行为与 `None` 不同。

```python
In [14]: None == None  # noqa: E711
Out[14]: True

In [15]: np.nan == np.nan
Out[15]: False

In [16]: pd.NaT == pd.NaT
Out[16]: False

In [17]: pd.NA == pd.NA
Out[17]: <NA>
```

因此，[`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 与这些缺失值之一的相等比较不提供与 [`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna") 或 [`notna()`](../reference/api/pandas.notna.html#pandas.notna "pandas.notna") 相同的信息。

## [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 语义 {#na-semantics}

> 警告：实验性的：[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 的行为可能在不发出警告的情况下发生变化。

从 pandas 1.0 开始，提供了一个实验性的 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 值（单例）来表示标量缺失值。[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 的目标是提供一个可以在所有数据类型中一致使用的"缺失"指示器（而不是根据数据类型使用 `np.nan`、`None` 或 `pd.NaT`）。

例如，当在具有可空整数 dtype 的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 中存在缺失值时，它将使用 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")：

```python
In [21]: s = pd.Series([1, 2, None], dtype="Int64")

In [22]: s
Out[22]:
0       1
1       2
2    <NA>
dtype: Int64

In [23]: s[2]
Out[23]: <NA>

In [24]: s[2] is pd.NA
Out[24]: True
```

目前，pandas 默认不在 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 中使用这些支持 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 的数据类型，因此你需要显式指定 dtype。转换为这些 dtype 的简单方法在[转换章节](#missing-data-na-conversion)中说明。

### 算术和比较运算中的传播 {#propagation-in-arithmetic-and-comparison-operations}

通常，缺失值在涉及 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 的操作中会*传播*。当操作数之一未知时，操作的结果也是未知的。

例如，[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 在算术运算中传播，类似于 `np.nan`：

```python
In [25]: pd.NA + 1
Out[25]: <NA>

In [26]: "a" * pd.NA
Out[26]: <NA>
```

在某些特殊情况下，即使操作数之一是 `NA`，结果也是已知的。

```python
In [27]: pd.NA ** 0
Out[27]: 1

In [28]: 1 ** pd.NA
Out[28]: 1
```

在相等性和比较运算中，[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 也会传播。这与 `np.nan` 的行为不同，与 `np.nan` 的比较总是返回 `False`。

```python
In [29]: pd.NA == 1
Out[29]: <NA>

In [30]: pd.NA == pd.NA
Out[30]: <NA>

In [31]: pd.NA < 2.5
Out[31]: <NA>
```

要检查一个值是否等于 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")，请使用 [`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna")。

```python
In [32]: pd.isna(pd.NA)
Out[32]: True
```

> 注意：这个基本传播规则的一个例外是*归约操作*（如均值或最小值），pandas 默认跳过缺失值。更多信息请参阅[计算章节](#missing-data-calculations)。

### 逻辑运算 {#logical-operations}

对于逻辑运算，[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 遵循[三值逻辑](https://en.wikipedia.org/wiki/Three-valued_logic)（或 *Kleene 逻辑*，类似于 R、SQL 和 Julia）的规则。这种逻辑意味着仅在逻辑上需要时才传播缺失值。

例如，对于逻辑"或"运算（`|`），如果操作数之一为 `True`，我们已经知道结果将是 `True`，无论另一个值是什么（因此无论缺失值是 `True` 还是 `False`）。在这种情况下，[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 不会传播：

```python
In [33]: True | False
Out[33]: True

In [34]: True | pd.NA
Out[34]: True

In [35]: pd.NA | True
Out[35]: True
```

另一方面，如果操作数之一是 `False`，结果取决于另一个操作数的值。因此，在这种情况下 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 会传播：

```python
In [36]: False | True
Out[36]: True

In [37]: False | False
Out[37]: False

In [38]: False | pd.NA
Out[38]: <NA>
```

逻辑"与"运算（`&`）的行为可以使用类似的逻辑推导（在这种情况下，如果操作数之一已经是 `False`，[`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 将不会传播）：

```python
In [39]: False & True
Out[39]: False

In [40]: False & False
Out[40]: False

In [41]: False & pd.NA
Out[41]: False

In [42]: True & True
Out[42]: True

In [43]: True & False
Out[43]: False

In [44]: True & pd.NA
Out[44]: <NA>
```

### 布尔上下文中的 `NA` {#na-in-a-boolean-context}

由于 NA 的实际值是未知的，将 NA 转换为布尔值是模糊的。

```python
In [45]: bool(pd.NA)
TypeError: boolean value of NA is ambiguous
```

这也意味着 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 不能在被评估为布尔值的上下文中使用，例如 `if condition: ...`，其中 `condition` 可能是 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")。在这种情况下，可以使用 [`isna()`](../reference/api/pandas.isna.html#pandas.isna "pandas.isna") 检查 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")，或者例如事先填充缺失值以避免 `condition` 为 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA")。

在 `if` 语句中使用 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象时会出现类似情况，请参阅[在 pandas 中使用 if/true 语句](gotchas.html#gotchas-truth)。

### NumPy ufuncs {#numpy-ufuncs}

[`pandas.NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 实现了 NumPy 的 `__array_ufunc__` 协议。大多数 ufunc 可以与 `NA` 一起工作，通常返回 `NA`：

```python
In [46]: np.log(pd.NA)
Out[46]: <NA>

In [47]: np.add(pd.NA, 1)
Out[47]: <NA>
```

> 警告：目前，涉及 ndarray 和 `NA` 的 ufunc 将返回填充了 NA 值的对象 dtype。

```python
In [48]: a = np.array([1, 2, 3])

In [49]: np.greater(a, pd.NA)
Out[49]: array([<NA>, <NA>, <NA>], dtype=object)
```

这里的返回类型将来可能会更改为返回不同的数组类型。

有关 ufunc 的更多信息，请参阅 [DataFrame 与 NumPy 函数的互操作性](dsintro.html#dsintro-numpy-interop)。

#### 转换 {#conversion}

如果你有使用 `np.nan` 的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")，[`DataFrame.convert_dtypes()`](../reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "pandas.DataFrame.convert_dtypes") 和 [`Series.convert_dtypes()`](../reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes") 将分别将你的数据转换为支持 [`NA`](../reference/api/pandas.NA.html#pandas.NA "pandas.NA") 的可空数据类型，例如 [`Int64Dtype`](../reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype") 或 [`ArrowDtype`](../reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")。这在从推断数据类型的 IO 方法读入数据集后特别有用。

```python
In [50]: import io

In [51]: data = io.StringIO("a,b\n,True\n2,")

In [52]: df = pd.read_csv(data)

In [53]: df.dtypes
Out[53]:
a    float64
b     object
dtype: object

In [54]: df_conv = df.convert_dtypes()

In [55]: df_conv
Out[55]:
      a     b
0  <NA>  True
1     2  <NA>

In [56]: df_conv.dtypes
Out[56]:
a      Int64
b    boolean
dtype: object
```

## 插入缺失数据 {#inserting-missing-data}

你可以通过简单地赋值给 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 来插入缺失值。使用的缺失值哨兵将根据 dtype 选择。

```python
In [57]: ser = pd.Series([1., 2., 3.])

In [58]: ser.loc[0] = None

In [59]: ser
Out[59]:
0    NaN
1    2.0
2    3.0
dtype: float64

In [60]: ser = pd.Series([pd.Timestamp("2021"), pd.Timestamp("2021")])

In [61]: ser.iloc[0] = np.nan

In [62]: ser
Out[62]:
0          NaT
1   2021-01-01
dtype: datetime64[us]

In [63]: ser = pd.Series([True, False], dtype="boolean[pyarrow]")

In [64]: ser.iloc[0] = None

In [65]: ser
Out[65]:
0     <NA>
1    False
dtype: bool[pyarrow]
```

对于 `object` 类型，pandas 将使用给定的值：

```python
In [66]: s = pd.Series(["a", "b", "c"], dtype=object)

In [67]: s.loc[0] = None

In [68]: s.loc[1] = np.nan

In [69]: s
Out[69]:
0    None
1     NaN
2       c
dtype: object
```

## 缺失数据的计算 {#calculations-with-missing-data}

缺失值通过 pandas 对象之间的算术运算传播。

```python
In [70]: ser1 = pd.Series([np.nan, np.nan, 2, 3])

In [71]: ser2 = pd.Series([np.nan, 1, np.nan, 4])

In [72]: ser1
Out[72]:
0    NaN
1    NaN
2    2.0
3    3.0
dtype: float64

In [73]: ser2
Out[73]:
0    NaN
1    1.0
2    NaN
3    4.0
dtype: float64

In [74]: ser1 + ser2
Out[74]:
0    NaN
1    NaN
2    NaN
3    7.0
dtype: float64
```

[数据结构概述](basics.html#basics-stats)中讨论的描述性统计和计算方法（以及[此处](../reference/series.html#api-series-stats)和[此处](../reference/frame.html#api-dataframe-stats)列出的）都会考虑缺失数据。

对数据求和时，NA 值或空数据将被视为零。

```python
In [75]: pd.Series([np.nan]).sum()
Out[75]: np.float64(0.0)

In [76]: pd.Series([], dtype="float64").sum()
Out[76]: np.float64(0.0)
```

求乘积时，NA 值或空数据将被视为 1。

```python
In [77]: pd.Series([np.nan]).prod()
Out[77]: np.float64(1.0)

In [78]: pd.Series([], dtype="float64").prod()
Out[78]: np.float64(1.0)
```

累积方法如 [`cumsum()`](../reference/api/pandas.DataFrame.cumsum.html#pandas.DataFrame.cumsum "pandas.DataFrame.cumsum") 和 [`cumprod()`](../reference/api/pandas.DataFrame.cumprod.html#pandas.DataFrame.cumprod "pandas.DataFrame.cumprod") 默认忽略 NA 值，但会在结果数组中保留它们。要覆盖此行为并在计算中包含 NA 值，请使用 `skipna=False`。

```python
In [79]: ser = pd.Series([1, np.nan, 3, np.nan])

In [80]: ser
Out[80]:
0    1.0
1    NaN
2    3.0
3    NaN
dtype: float64

In [81]: ser.cumsum()
Out[81]:
0    1.0
1    NaN
2    4.0
3    NaN
dtype: float64

In [82]: ser.cumsum(skipna=False)
Out[82]:
0    1.0
1    NaN
2    NaN
3    NaN
dtype: float64
```

## 删除缺失数据 {#dropping-missing-data}

[`dropna()`](../reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna") 删除带有缺失数据的行或列。

```python
In [83]: df = pd.DataFrame([[np.nan, 1, 2], [1, 2, np.nan], [1, 2, 3]])

In [84]: df
Out[84]:
     0  1    2
0  NaN  1  2.0
1  1.0  2  NaN
2  1.0  2  3.0

In [85]: df.dropna()
Out[85]:
     0  1    2
2  1.0  2  3.0

In [86]: df.dropna(axis=1)
Out[86]:
   1
0  1
1  2
2  2

In [87]: ser = pd.Series([1, pd.NA], dtype="int64[pyarrow]")

In [88]: ser.dropna()
Out[88]:
0    1
dtype: int64[pyarrow]
```

## 填充缺失数据 {#filling-missing-data}

### 按值填充 {#filling-by-value}

[`fillna()`](../reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna") 用非 NA 数据替换 NA 值。

用标量值替换 NA：

```python
In [89]: data = {"np": [1.0, np.nan, np.nan, 2], "arrow": pd.array([1.0, pd.NA, pd.NA, 2], dtype="float64[pyarrow]")}

In [90]: df = pd.DataFrame(data)

In [91]: df
Out[91]:
    np  arrow
0  1.0    1.0
1  NaN   <NA>
2  NaN   <NA>
3  2.0    2.0

In [92]: df.fillna(0)
Out[92]:
    np  arrow
0  1.0    1.0
1  0.0    0.0
2  0.0    0.0
3  2.0    2.0
```

向前或向后填充缺口：

```python
In [104]: df.ffill()
Out[104]:
    np  arrow
0  1.0    1.0
1  1.0    1.0
2  1.0    1.0
3  2.0    2.0

In [105]: df.bfill()
Out[105]:
    np  arrow
0  1.0    1.0
1  2.0    2.0
2  2.0    2.0
3  2.0    2.0
```

限制填充的 NA 值数量：

```python
In [106]: df.ffill(limit=1)
Out[106]:
    np  arrow
0  1.0    1.0
1  1.0    1.0
2  NaN   <NA>
3  2.0    2.0
```

NA 值可以用来自 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的对应值替换，其中原始对象和填充对象之间的索引和列是对齐的。

> 注意：[`DataFrame.where()`](../reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where") 也可用于填充 NA 值。结果与上面相同。

### 插值 {#interpolation}

[`DataFrame.interpolate()`](../reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "pandas.DataFrame.interpolate") 和 [`Series.interpolate()`](../reference/api/pandas.Series.interpolate.html#pandas.Series.interpolate "pandas.Series.interpolate") 使用各种插值方法填充 NA 值。

```python
In [114]: df = pd.DataFrame(
   .....:     {
   .....:         "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
   .....:         "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
   .....:     }
   .....: )
   .....:

In [115]: df
Out[115]:
     A      B
0  1.0   0.25
1  2.1    NaN
2  NaN    NaN
3  4.7   4.00
4  5.6  12.20
5  6.8  14.40

In [116]: df.interpolate()
Out[116]:
     A      B
0  1.0   0.25
1  2.1   1.50
2  3.4   2.75
3  4.7   4.00
4  5.6  12.20
5  6.8  14.40
```

通过设置 `method="time"`，可以使用 [`DatetimeIndex`](../reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex") 中 [`Timestamp`](../reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp") 的相对时间进行插值。

对于浮点索引，使用 `method='values'`。

如果你安装了 [scipy](https://scipy.org/)，可以将一维插值例程的名称传递给 `method`，如 scipy 插值[文档](https://docs.scipy.org/doc/scipy/reference/interpolate.html#univariate-interpolation)和参考[指南](https://docs.scipy.org/doc/scipy/tutorial/interpolate.html)中所指定。适当的插值方法取决于数据类型。

> 提示：
> - 如果处理增长速度递增的时间序列，使用 `method='barycentric'`。
> - 如果有近似累积分布函数的值，使用 `method='pchip'`。
> - 为平滑绘图填充缺失值时，使用 `method='akima'`。

通过多项式或样条近似进行插值时，还必须指定近似的次数或阶数：

```python
In [139]: df.interpolate(method="spline", order=2)
Out[139]:
          A          B
0  1.000000   0.250000
1  2.100000  -0.428598
2  3.404545   1.206900
3  4.700000   4.000000
4  5.600000  12.200000
5  6.800000  14.400000

In [140]: df.interpolate(method="polynomial", order=2)
Out[140]:
          A          B
0  1.000000   0.250000
1  2.100000  -2.703846
2  3.451351  -1.453846
3  4.700000   4.000000
4  5.600000  12.200000
5  6.800000  14.400000
```

#### 插值限制 {#interpolation-limits}

[`interpolate()`](../reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "pandas.DataFrame.interpolate") 接受 `limit` 关键字参数，以限制自上次有效观测值以来填充的连续 `NaN` 值的数量。

默认情况下，`NaN` 值按 `forward`（向前）方向填充。使用 `limit_direction` 参数可以按 `backward`（向后）或 `both`（双向）方向填充。

默认情况下，无论 `NaN` 值是被现有有效值包围还是在现有有效值之外，都会被填充。`limit_area` 参数将填充限制为内部或外部值。

### 替换值 {#replacing-values}

[`Series.replace()`](../reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace") 和 [`DataFrame.replace()`](../reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace") 可以类似于 [`Series.fillna()`](../reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna") 和 [`DataFrame.fillna()`](../reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna") 的方式使用，来替换或插入缺失值。

```python
In [162]: df = pd.DataFrame(np.eye(3))

In [163]: df
Out[163]:
     0    1    2
0  1.0  0.0  0.0
1  0.0  1.0  0.0
2  0.0  0.0  1.0

In [164]: df_missing = df.replace(0, np.nan)

In [165]: df_missing
Out[165]:
     0    1    2
0  1.0  NaN  NaN
1  NaN  1.0  NaN
2  NaN  NaN  1.0

In [166]: df_filled = df_missing.replace(np.nan, 2)

In [167]: df_filled
Out[167]:
     0    1    2
0  1.0  2.0  2.0
1  2.0  1.0  2.0
2  2.0  2.0  1.0
```

通过传入列表可以替换多个值。

使用映射字典进行替换。

#### 正则表达式替换 {#regular-expression-replacement}

> 注意：以 `r` 字符为前缀的 Python 字符串，如 `r'hello world'`，是[原始字符串](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)。它们在反斜杠方面具有与没有此前缀的字符串不同的语义。原始字符串中的反斜杠将被解释为转义的反斜杠，例如 `r'\' == '\\'`。

用 `NaN` 替换 '.'：

```python
In [170]: d = {"a": list(range(4)), "b": list("ab.."), "c": ["a", "b", np.nan, "d"]}

In [171]: df = pd.DataFrame(d)

In [172]: df.replace(".", np.nan)
Out[172]:
   a    b    c
0  0    a    a
1  1    b    b
2  2  NaN  NaN
3  3  NaN    d
```

使用正则表达式替换，移除周围空白：

```python
In [173]: df.replace(r"\s*\.\s*", np.nan, regex=True)
Out[173]:
   a    b    c
0  0    a    a
1  1    b    b
2  2  NaN  NaN
3  3  NaN    d
```

使用正则表达式列表进行替换。

使用映射字典中的正则表达式进行替换。

传递嵌套的正则表达式字典。

传递正则表达式列表，将匹配替换为标量。

所有正则表达式示例也可以将 `to_replace` 参数作为 `regex` 参数传递。在这种情况下，`value` 参数必须显式传递，或者 `regex` 必须是嵌套字典。

> 注意：`re.compile` 的正则表达式对象也是有效的输入。
