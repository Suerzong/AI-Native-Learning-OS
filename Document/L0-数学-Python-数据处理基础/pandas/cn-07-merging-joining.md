# 合并、连接、拼接和比较 {#merge-join-concatenate-and-compare}

pandas 提供了各种用于组合和比较 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的方法。

- [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat")：沿共享索引或列拼接多个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象
- [`DataFrame.join()`](../reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join")：沿列合并多个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象
- [`DataFrame.combine_first()`](../reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "pandas.DataFrame.combine_first")：用相同位置的非缺失值更新缺失值
- [`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge")：使用 SQL 风格的连接组合两个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象
- [`merge_ordered()`](../reference/api/pandas.merge_ordered.html#pandas.merge_ordered "pandas.merge_ordered")：沿有序轴组合两个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象
- [`merge_asof()`](../reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof")：通过近似匹配键组合两个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象
- [`Series.compare()`](../reference/api/pandas.Series.compare.html#pandas.Series.compare "pandas.Series.compare") 和 [`DataFrame.compare()`](../reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "pandas.DataFrame.compare")：显示两个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象之间的值差异

## `concat()` {#concat}

[`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 函数沿某个轴拼接任意数量的 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象，同时对其他轴上的索引执行可选的集合逻辑（并集或交集）。与 `numpy.concatenate` 类似，[`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 接受同类型对象的列表或字典并拼接它们。

> 注意：[`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 会完整复制数据，迭代重用 [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 会创建不必要的副本。在使用 [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat") 之前，将所有 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 对象收集到列表中。

```python
frames = [process_your_file(f) for f in files]
result = pd.concat(frames)
```

### 结果轴的连接逻辑 {#joining-logic-of-the-resulting-axis}

`join` 关键字指定如何处理第一个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中不存在的轴值。

`join='outer'` 取所有轴值的并集。

```python
In [7]: df4 = pd.DataFrame(
   ...:     {
   ...:         "B": ["B2", "B3", "B6", "B7"],
   ...:         "D": ["D2", "D3", "D6", "D7"],
   ...:         "F": ["F2", "F3", "F6", "F7"],
   ...:     },
   ...:     index=[2, 3, 6, 7],
   ...: )
   ...: 

In [8]: result = pd.concat([df1, df4], axis=1)
```

`join='inner'` 取轴值的交集。

```python
In [10]: result = pd.concat([df1, df4], axis=1, join="inner")
```

### 忽略拼接轴上的索引 {#ignoring-indexes-on-the-concatenation-axis}

对于没有有意义索引的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象，`ignore_index` 忽略重叠的索引。

```python
In [14]: result = pd.concat([df1, df4], ignore_index=True, sort=False)
```

### 拼接 `Series` 和 `DataFrame` {#concatenating-series-and-dataframe-together}

你可以拼接 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 和 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的混合对象。[`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 将被转换为 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")，列名为 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 的名称。

### 结果键（keys） {#resulting-keys}

`keys` 参数为结果索引或列添加另一个轴级别（创建 [`MultiIndex`](../reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")），将特定键与每个原始 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 关联。

```python
In [24]: result = pd.concat(frames, keys=["x", "y", "z"])
```

你也可以将字典传递给 [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat")，在这种情况下，字典键将用于 `keys` 参数（除非指定了其他 `keys` 参数）。

### 向 `DataFrame` 追加行 {#appending-rows-to-a-dataframe}

如果你有一个 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 想要作为单行追加到 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")，可以将该行转换为 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 并使用 [`concat()`](../reference/api/pandas.concat.html#pandas.concat "pandas.concat")。

```python
In [41]: s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])

In [42]: result = pd.concat([df1, s2.to_frame().T], ignore_index=True)
```

## `merge()` {#merge}

[`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge") 执行类似于关系数据库（如 SQL）的连接操作。熟悉 SQL 但不熟悉 pandas 的用户可以参考[与 SQL 的比较](../getting_started/comparison/comparison_with_sql.html#compare-with-sql-join)。

### 合并类型 {#merge-types}

[`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge") 实现常见的 SQL 风格连接操作。

- **一对一（one-to-one）**：在两个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象的索引上连接，索引必须包含唯一值。
- **多对一（many-to-one）**：将唯一索引连接到不同 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中的一个或多个列。
- **多对多（many-to-many）**：列对列的连接。

> 注意：当列对列连接时（可能是多对多连接），传入的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 对象上的任何索引**将被丢弃**。

对于**多对多**连接，如果键组合在两个表中都出现多次，则 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 将具有关联数据的**笛卡尔积**。

`how` 参数指定结果表中包含哪些键。下表总结了 `how` 选项及其 SQL 等效名称：

| 合并方法 | SQL 连接名称 | 描述 |
|---------|------------|------|
| `left` | `LEFT OUTER JOIN` | 仅使用左表的键 |
| `right` | `RIGHT OUTER JOIN` | 仅使用右表的键 |
| `outer` | `FULL OUTER JOIN` | 使用两表键的并集 |
| `inner` | `INNER JOIN` | 使用两表键的交集 |
| `cross` | `CROSS JOIN` | 创建两表行的笛卡尔积 |

### 合并键唯一性 {#merge-key-uniqueness}

`validate` 参数检查合并键的唯一性。在合并操作之前检查键的唯一性，可以防止内存溢出和意外的键重复。

```python
In [71]: result = pd.merge(left, right, on="B", how="outer", validate="one_to_one")
# 如果右表中的键不唯一，将引发 MergeError
```

### 合并结果指示器 {#merge-result-indicator}

[`merge()`](../reference/api/pandas.merge.html#pandas.merge "pandas.merge") 接受 `indicator` 参数。如果为 `True`，将在输出对象中添加一个名为 `_merge` 的 Categorical 类型列，其值为：

| 观测来源 | `_merge` 值 |
|---------|------------|
| 合并键仅在左表中 | `left_only` |
| 合并键仅在右表中 | `right_only` |
| 合并键在两表中 | `both` |

```python
In [75]: pd.merge(df1, df2, on="col1", how="outer", indicator=True)
```

### 重叠的值列 {#overlapping-value-columns}

合并 `suffixes` 参数接受一个字符串元组或列表，用于附加到输入 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中重叠的列名，以消除结果列的歧义。

```python
In [81]: result = pd.merge(left, right, on="k", suffixes=("_l", "_r"))
```

## `DataFrame.join()` {#dataframe-join}

[`DataFrame.join()`](../reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join") 将多个可能具有不同索引的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列合并为单个结果 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")。

```python
In [85]: result = left.join(right)
```

[`DataFrame.join()`](../reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join") 默认执行左连接（left join），仅使用调用 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中的键。可以使用 `how` 指定其他连接类型。

### 将单个索引连接到 MultiIndex {#joining-a-single-index-to-a-multiindex}

你可以将带有 [`Index`](../reference/api/pandas.Index.html#pandas.Index "pandas.Index") 的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 在某个级别上连接到带有 [`MultiIndex`](../reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex") 的 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")。

### 连接两个 `MultiIndex` {#joining-with-two-multiindex}

输入参数的 [`MultiIndex`](../reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex") 必须在连接中完全使用，并且是左参数中索引的子集。

### 在列和索引级别的组合上合并 {#merging-on-a-combination-of-columns-and-index-levels}

作为 `on`、`left_on` 和 `right_on` 参数传递的字符串可以引用列名或索引级别名。这使得可以在不重置索引的情况下，在索引级别和列的组合上合并 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 实例。

### 连接多个 `DataFrame` {#joining-multiple-dataframe}

[`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的列表或元组也可以传递给 [`join()`](../reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join")，以在它们的索引上连接。

### `DataFrame.combine_first()` {#dataframe-combine-first}

[`DataFrame.combine_first()`](../reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "pandas.DataFrame.combine_first") 用另一个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中对应位置的非缺失值更新一个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中的缺失值。

```python
In [132]: result = df1.combine_first(df2)
```

## `merge_ordered()` {#merge-ordered}

[`merge_ordered()`](../reference/api/pandas.merge_ordered.html#pandas.merge_ordered "pandas.merge_ordered") 合并有序数据（如数值或时间序列数据），并可通过 `fill_method` 可选地填充缺失数据。

```python
In [136]: pd.merge_ordered(left, right, fill_method="ffill", left_by="s")
```

## `merge_asof()` {#merge-asof}

[`merge_asof()`](../reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof") 类似于有序左连接，不同之处在于匹配是在最近的键上而不是相等的键上。对于 `left` [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中的每一行，在 `right` [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中选择 `on` 键小于左表键的最后一行。两个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 都必须按键排序。

可选地，[`merge_asof()`](../reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof") 可以通过在 `on` 键的最近匹配之外匹配 `by` 键来执行分组合并。

```python
In [141]: pd.merge_asof(trades, quotes, on="time", by="ticker")
```

在报价时间和交易时间之间 `2ms` 内使用 [`merge_asof()`](../reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof")：

```python
In [142]: pd.merge_asof(trades, quotes, on="time", by="ticker", tolerance=pd.Timedelta("2ms"))
```

## `compare()` {#compare}

[`Series.compare()`](../reference/api/pandas.Series.compare.html#pandas.Series.compare "pandas.Series.compare") 和 [`DataFrame.compare()`](../reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "pandas.DataFrame.compare") 方法分别允许比较两个 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 或 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series")，并汇总它们的差异。

```python
In [150]: df.compare(df2)
Out[150]:
  col1       col3      
  self other self other
0    a     c  NaN   NaN
2  NaN   NaN  3.0   4.0
```

默认情况下，如果两个对应值相等，它们将显示为 `NaN`。此外，如果整行/列的所有值都相等，则该行/列将从结果中省略。其余差异将在列上对齐。

在行上堆叠差异：

```python
In [151]: df.compare(df2, align_axis=0)
```

使用 `keep_shape=True` 保留所有原始行和列：

```python
In [152]: df.compare(df2, keep_shape=True)
```

即使值相等，也保留所有原始值：

```python
In [153]: df.compare(df2, keep_shape=True, keep_equal=True)
```
