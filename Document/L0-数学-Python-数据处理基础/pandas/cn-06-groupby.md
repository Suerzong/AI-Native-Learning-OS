# GroupBy：分组-应用-合并 {#group-by-split-apply-combine}

"分组（group by）"指的是涉及以下一个或多个步骤的过程：

- **拆分（Splitting）**：根据某些标准将数据拆分为若干组。
- **应用（Applying）**：独立地对每组应用函数。
- **合并（Combining）**：将结果合并为一个数据结构。

其中，拆分步骤是最直接的。在应用步骤中，我们可能希望执行以下操作之一：

- **聚合（Aggregation）**：为每组计算一个汇总统计量（或多个统计量）。例如：
  - 计算组的总和或均值。
  - 计算组的大小/计数。

- **转换（Transformation）**：执行一些特定于组的计算并返回类似索引的对象。例如：
  - 在组内标准化数据（zscore）。
  - 使用从每组派生的值填充组内的 NA。

- **过滤（Filtration）**：根据评估为 True 或 False 的逐组计算，丢弃某些组。例如：
  - 丢弃属于成员很少的组的数据。
  - 根据组总和或均值过滤数据。

其中许多操作在 GroupBy 对象上定义。这些操作类似于[聚合 API](basics.html#basics-aggregate)、[窗口 API](window.html#window-overview) 和[重采样 API](timeseries.html#timeseries-aggregate) 中的操作。

可能某些操作不属于上述类别或是它们的组合。在这种情况下，可以使用 GroupBy 的 `apply` 方法来计算操作。

> 注意：使用内置 GroupBy 操作分成多个步骤的操作比使用用户定义 Python 函数的 `apply` 方法更高效。

GroupBy 这个名称对于使用过基于 SQL 的工具（或 `itertools`）的人来说应该很熟悉，在 SQL 中你可以编写如下代码：

```sql
SELECT Column1, Column2, mean(Column3), sum(Column4)
FROM SomeTable
GROUP BY Column1, Column2
```

我们的目标是使用 pandas 让这样的操作自然且易于表达。

## 将对象拆分为组 {#splitting-an-object-into-groups}

分组的抽象定义是提供标签到组名的映射。要创建 GroupBy 对象，你可以执行以下操作：

```python
In [1]: speeds = pd.DataFrame(
   ...:     [
   ...:         ("bird", "Falconiformes", 389.0),
   ...:         ("bird", "Psittaciformes", 24.0),
   ...:         ("mammal", "Carnivora", 80.2),
   ...:         ("mammal", "Primates", np.nan),
   ...:         ("mammal", "Carnivora", 58),
   ...:     ],
   ...:     index=["falcon", "parrot", "lion", "monkey", "leopard"],
   ...:     columns=("class", "order", "max_speed"),
   ...: )
   ...: 

In [2]: speeds
Out[2]:
          class           order  max_speed
falcon     bird   Falconiformes      389.0
parrot     bird  Psittaciformes       24.0
lion     mammal       Carnivora       80.2
monkey   mammal        Primates        NaN
leopard  mammal       Carnivora       58.0

In [3]: grouped = speeds.groupby("class")

In [4]: grouped = speeds.groupby(["class", "order"])
```

映射可以通过多种方式指定：

- 一个 Python 函数，在每个索引标签上调用。
- 一个与索引长度相同的列表或 NumPy 数组。
- 一个字典或 `Series`，提供 `label -> group name` 的映射。
- 对于 `DataFrame` 对象，一个字符串指示要用于分组的列名或索引级别名。
- 上述任何内容的列表。

我们将分组对象统称为**键（keys）**。

> 注意：传递给 `groupby` 的字符串可以引用列或索引级别。如果字符串同时匹配列名和索引级别名，将引发 `ValueError`。

```python
In [5]: df = pd.DataFrame(
   ...:     {
   ...:         "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
   ...:         "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
   ...:         "C": np.random.randn(8),
   ...:         "D": np.random.randn(8),
   ...:     }
   ...: )
   ...: 

In [6]: df
Out[6]:
     A      B         C         D
0  foo    one  0.469112 -0.861849
1  bar    one -0.282863 -2.104569
2  foo    two -1.509059 -0.494929
3  bar  three -1.135632  1.071804
4  foo    two  1.212112  0.721555
5  bar    two -0.173215 -0.706771
6  foo    one  0.119209 -1.039575
7  foo  three -1.044236  0.271860
```

## 聚合 {#aggregation}

使用 [`agg()`](../reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html#pandas.core.groupby.DataFrameGroupBy.agg "pandas.core.groupby.DataFrameGroupBy.agg") 方法可以一次应用多个聚合函数：

```python
In [7]: df.groupby('A').agg(['sum', 'mean', 'std'])
Out[7]:
        C                       D                
      sum      mean       std sum      mean       std
A                                                    
bar -1.591710 -0.530570  0.491278 -1.500636 -0.500212  1.611429
foo  0.348248  0.069650  1.088074 -1.388156 -0.277631  0.775775
```

你也可以使用命名聚合来为输出列指定自定义名称：

```python
In [8]: df.groupby('A').agg(
   ...:     C_sum=('C', 'sum'),
   ...:     D_mean=('D', 'mean'),
   ...: )
   ...: 
Out[8]:
        C_sum    D_mean
A                      
bar -1.591710 -1.500636
foo  0.348248 -1.388156
```

## 转换 {#transformation}

使用 [`transform()`](../reference/api/pandas.core.groupby.DataFrameGroupBy.transform.html#pandas.core.groupby.DataFrameGroupBy.transform "pandas.core.groupby.DataFrameGroupBy.transform") 方法对每组进行转换：

```python
In [9]: df.groupby('A')['C'].transform('mean')
Out[9]:
0   -0.530570
1   -0.530570
2    0.069650
3   -0.530570
4    0.069650
5   -0.530570
6    0.069650
7    0.069650
dtype: float64
```

## 过滤 {#filtration}

使用 [`filter()`](../reference/api/pandas.core.groupby.DataFrameGroupBy.filter.html#pandas.core.groupby.DataFrameGroupBy.filter "pandas.core.groupby.DataFrameGroupBy.filter") 方法过滤组：

```python
In [10]: df.groupby('A').filter(lambda x: x['C'].mean() > 0)
Out[10]:
     A      B         C         D
0  foo    one  0.469112 -0.861849
2  foo    two -1.509059 -0.494929
4  foo    two  1.212112  0.721555
6  foo    one  0.119209 -1.039575
7  foo  three -1.044236  0.271860
```

## 应用任意函数 {#apply}

使用 [`apply()`](../reference/api/pandas.core.groupby.DataFrameGroupBy.apply.html#pandas.core.groupby.DataFrameGroupBy.apply "pandas.core.groupby.DataFrameGroupBy.apply") 方法对每组应用任意函数：

```python
In [11]: df.groupby('A').apply(lambda x: x.describe())
Out[11]:
                  C         D
A                             
bar count  3.000000  3.000000
    mean  -0.530570 -0.500212
    std    0.491278  1.611429
    min   -1.135632 -2.104569
    25%   -0.861849 -1.401103
    50%   -0.282863 -0.706771
    75%   -0.228039  0.182545
    max    0.119209  1.071804
foo count  5.000000  5.000000
    mean   0.069650 -0.277631
    std    1.088074  0.775775
    min   -1.509059 -1.039575
    25%   -1.044236 -0.861849
    50%    0.119209 -0.494929
    75%    0.469112  0.271860
    max    1.212112  0.721555
```

## 按多列分组 {#groupby-multi}

按多列分组时，结果是一个 MultiIndex：

```python
In [12]: df.groupby(['A', 'B']).sum()
Out[12]:
                  C         D
A   B                         
bar one   -0.282863 -2.104569
    three -1.135632  1.071804
    two   -0.173215 -0.706771
foo one    0.588321 -1.901424
    three -1.044236  0.271860
    two   -0.296947  0.226626
```

## 遍历组 {#groupby-iteration}

GroupBy 对象支持迭代，生成组名和数据的元组：

```python
In [13]: for name, group in df.groupby('A'):
   ....:     print(f"Group: {name}")
   ....:     print(group)
   ....:     print()
   ....: 
Group: bar
     A      B         C         D
1  bar    one -0.282863 -2.104569
3  bar  three -1.135632  1.071804
5  bar    two -0.173215 -0.706771

Group: foo
     A      B         C         D
0  foo    one  0.469112 -0.861849
2  foo    two -1.509059 -0.494929
4  foo    two  1.212112  0.721555
6  foo    one  0.119209 -1.039575
7  foo  three -1.044236  0.271860
```

## 排除分组键 {#groupby-attributes}

默认情况下，分组键包含在结果中。使用 `group_keys=False` 可以排除它们：

```python
In [14]: df.groupby('A', group_keys=False).apply(lambda x: x.head(2))
Out[14]:
     A      B         C         D
1  bar    one -0.282863 -2.104569
3  bar  three -1.135632  1.071804
0  foo    one  0.469112 -0.861849
2  foo    two -1.509059 -0.494929
```

## 处理缺失数据 {#groupby-missing-data}

默认情况下，分组时会排除 NA 值。使用 `dropna=False` 可以包含 NA 值作为分组键：

```python
In [15]: df_with_nan = df.copy()
In [16]: df_with_nan.loc[0, 'A'] = np.nan
In [17]: df_with_nan.groupby('A', dropna=False).sum()
```

## 常见聚合方法速查 {#groupby-common-methods}

| 方法 | 描述 |
|------|------|
| `count()` | 非 NA 值的数量 |
| `sum()` | 值的总和 |
| `mean()` | 值的均值 |
| `median()` | 值的中位数 |
| `std()` | 值的标准差 |
| `var()` | 值的方差 |
| `min()` | 最小值 |
| `max()` | 最大值 |
| `prod()` | 值的乘积 |
| `first()` | 组中的第一个值 |
| `last()` | 组中的最后一个值 |
