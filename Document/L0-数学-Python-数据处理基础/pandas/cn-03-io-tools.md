# IO 工具（文本、CSV、HDF5 等） {#io-tools-text-csv-hdf5}

pandas I/O API 是一组顶层的 `reader` 函数，如 [`pandas.read_csv()`](../reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")，通常返回一个 pandas 对象。相应的 `writer` 函数是对象方法，如 [`DataFrame.to_csv()`](../reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")。以下是包含可用 `reader` 和 `writer` 的表格。

| 格式类型 | 数据描述 | Reader | Writer |
|---------|---------|--------|--------|
| text | [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) | [read_csv](#io-read-csv-table) | [to_csv](#io-store-in-csv) |
| text | 固定宽度文本文件 | [read_fwf](#io-fwf-reader) | NA |
| text | [JSON](https://www.json.org/) | [read_json](#io-json-reader) | [to_json](#io-json-writer) |
| text | [HTML](https://en.wikipedia.org/wiki/HTML) | [read_html](#io-read-html) | [to_html](#io-html) |
| text | [LaTeX](https://en.wikipedia.org/wiki/LaTeX) | NA | [Styler.to_latex](#io-latex) |
| text | [XML](https://www.w3.org/standards/xml/core) | [read_xml](#io-read-xml) | [to_xml](#io-xml) |
| text | 本地剪贴板 | [read_clipboard](#io-clipboard) | [to_clipboard](#io-clipboard) |
| binary | [MS Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) | [read_excel](#io-excel-reader) | [to_excel](#io-excel-writer) |
| binary | [OpenDocument](http://opendocumentformat.org) | [read_excel](#io-ods) | NA |
| binary | [HDF5 格式](https://support.hdfgroup.org/documentation/hdf5/latest/_intro_h_d_f5.html) | [read_hdf](#io-hdf5) | [to_hdf](#io-hdf5) |
| binary | [Feather 格式](https://github.com/wesm/feather) | [read_feather](#io-feather) | [to_feather](#io-feather) |
| binary | [Parquet 格式](https://parquet.apache.org/) | [read_parquet](#io-parquet) | [to_parquet](#io-parquet) |
| binary | [Apache Iceberg](https://iceberg.apache.org/) | [read_iceberg](#io-iceberg) | [to_iceberg](#io-iceberg) |
| binary | [ORC 格式](https://orc.apache.org/) | [read_orc](#io-orc) | [to_orc](#io-orc) |
| binary | [Stata](https://en.wikipedia.org/wiki/Stata) | [read_stata](#io-stata-reader) | [to_stata](#io-stata-writer) |
| binary | [SAS](https://en.wikipedia.org/wiki/SAS_\(software\)) | [read_sas](#io-sas-reader) | NA |
| binary | [SPSS](https://en.wikipedia.org/wiki/SPSS) | [read_spss](#io-spss-reader) | NA |
| binary | [Python Pickle 格式](https://docs.python.org/3/library/pickle.html) | [read_pickle](#io-pickle) | [to_pickle](#io-pickle) |
| SQL | [SQL](https://en.wikipedia.org/wiki/SQL) | [read_sql](#io-sql) | [to_sql](#io-sql) |

[这里](#io-perf)是一些 IO 方法的非正式性能比较。

> 注意：对于使用 `StringIO` 类的示例，请确保在 Python 3 中使用 `from io import StringIO` 导入它。

## CSV 和文本文件 {#csv-text-files}

读取文本文件（也称为平面文件）的主力函数是 [`read_csv()`](../reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")。请参阅[烹饪手册](cookbook.html#cookbook-csv)了解一些高级策略。

### 解析选项 {#parsing-options}

[`read_csv()`](../reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv") 接受以下常用参数：

#### 基本参数 {#basic}

**filepath_or_buffer**：各种类型

文件路径（[`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")、[`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "\(in Python v3.14\)")）、URL（包括 http、ftp 和 S3 位置），或任何具有 `read()` 方法的对象（如打开的文件或 [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "\(in Python v3.14\)")）。

**sep**：str，[`read_csv()`](../reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv") 默认为 `','`，[`read_table()`](../reference/api/pandas.read_table.html#pandas.read_table "pandas.read_table") 默认为 `\t`

使用的分隔符。如果 sep 为 `None`，C 引擎无法自动检测分隔符，但 Python 解析引擎可以，这意味着后者将被使用，并由 Python 内置的嗅探工具 [`csv.Sniffer`](https://docs.python.org/3/library/csv.html#csv.Sniffer "\(in Python v3.14\)") 自动检测分隔符。此外，长度大于 1 且不同于 `'\s+'` 的分隔符将被解释为正则表达式，并强制使用 Python 解析引擎。注意正则表达式分隔符容易忽略带引号的数据。正则表达式示例：`'\\r\\t'`。

**delimiter**：str，默认 `None`

sep 的替代参数名称。

#### 列和索引位置及名称 {#column-and-index-locations-and-names}

**header**：int 或 int 列表，默认 `'infer'`

用作列名的行号，以及数据的开始。默认行为是推断列名：如果未传入名称，行为与 `header=0` 相同，列名从文件第一行推断；如果显式传入列名，行为与 `header=None` 相同。显式传入 `header=0` 可以替换现有名称。

**names**：类数组，默认 `None`

要使用的列名列表。如果文件不包含标题行，则应显式传入 `header=None`。此列表中不允许重复。

**index_col**：int、str、int/str 序列或 False，可选，默认 `None`

用作 DataFrame 行标签的列，以字符串名称或列索引给出。如果给定了 int/str 序列，则使用 MultiIndex。

> 注意：`index_col=False` 可用于强制 pandas *不*使用第一列作为索引，例如当你的文件格式错误，每行末尾有分隔符时。

**usecols**：类列表或可调用对象，默认 `None`

返回列的子集。如果是类列表，所有元素必须是位置（即整数索引）或对应于列名的字符串。如果是可调用对象，该函数将对列名求值，返回求值为 True 的列名。

使用此参数时，使用 C 引擎的解析时间更快，内存使用更低。Python 引擎在决定丢弃哪些列之前先加载数据。

#### 通用解析配置 {#general-parsing-configuration}

**dtype**：类型名称或列 -> 类型的字典，默认 `None`

数据或列的数据类型。例如 `{'a': np.float64, 'b': np.int32, 'c': 'Int64'}`。使用 `str` 或 `object` 配合适当的 `na_values` 设置来保留而不解释 dtype。如果指定了转换器，它们将代替 dtype 转换应用。

**dtype_backend**：{"numpy_nullable", "pyarrow"}，默认为 NumPy 支持的 DataFrame

用于返回 DataFrame 的后端数据类型。

#### NA 值处理 {#na-values-handling}

**na_values**：标量、str、类列表或字典，默认 `None`

附加的识别为 NA/NaN 的值。如果是字典，则指定每列的 NA 值。

**keep_default_na**：bool，默认 `True`

是否包含默认的 NA 值。当 `na_values` 中指定了值时，`keep_default_na=False` 将覆盖默认值。

**na_filter**：bool，默认 `True`

是否检测缺失值标记（空字符串和 `na_values` 中的值）。在没有 NA 的数据中，`na_filter=False` 可以提高读取大文件的性能。

**verbose**：bool，默认 `True`

指示放置在非数值列中的 NA 值的数量。

**skip_blank_lines**：bool，默认 `True`

如果为 True，跳过空行而不是将它们解释为 NaN 值。

#### 解析日期时间 {#parsing-dates}

**parse_dates**：bool 或列表，默认 `False`

- 如果为 True，尝试解析索引。
- 如果为列表或字典，尝试解析每列中的日期。
- 如果使用 `index_col`，可以指定基于列的日期解析。

**date_format**：str 或字典，默认 `None`

用于解析日期的 strftime 格式。

**dayfirst**：bool，默认 `False`

以 DD/MM 格式解析日期。

#### 迭代 {#iteration}

**iterator**：bool，默认 `False`

返回 `TextFileReader` 对象用于迭代。

**chunksize**：int，可选

返回 `TextFileReader` 对象用于迭代。参阅[迭代](#io-chunking)。

#### 引用、压缩和文件格式 {#quoting-compression-format}

**compression**：str 或字典，默认 `'infer'`

用于磁盘上数据的即时解压缩。支持 `'gzip'`、`'bz2'`、`'zip'`、`'xz'`、`'zstd'`、`'tar'`。

**quotechar**：str，默认 `"`

用于引用的字符。

**quoting**：int 或 `csv.QUOTE_*` 实例，默认 `0`

控制字段引用行为。

**doublequote**：bool，默认 `True`

当 `quotechar` 指定且 `quoting` 不是 `QUOTE_NONE` 时，控制一个引号字符的出现是否被解释为两个引号字符。

**escapechar**：str，默认 `None`

用于转义其他字符的字符。

**comment**：str，默认 `None`

表示该行其余部分不应被解析的字符。

**encoding**：str，默认 `None`

读/写的编码。对于 Python 3，使用编码代替 latin-1 的推荐方式。

**encoding_errors**：str，可选，默认 `'strict'`

编码错误的处理方式。

**dialect**：str 或 `csv.Dialect` 实例，默认 `None`

提供 `delimiter`、`doublequote`、`escapechar`、`skipinitialspace`、`quotechar` 和 `quoting` 参数的替代方式。

#### 错误处理 {#error-handling}

**on_bad_lines**：{'error', 'warn', 'skip'} 或可调用对象，默认 `'error'`

指定遇到坏行（字段数过多的行）时的处理方式。

## CSV 文本文件写入 {#io-store-in-csv}

写入 CSV 文件：

```python
In [1]: df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
   ...:                    'mask': ['red', 'purple'],
   ...:                    'weapon': ['sai', 'bo staff']})
   ...: 

In [2]: df.to_csv('out.csv')
```

读回：

```python
In [3]: pd.read_csv('out.csv')
Out[3]:
   Unnamed: 0      name    mask    weapon
0           0   Raphael     red       sai
1           1  Donatello  purple  bo staff
```

## JSON {#json}

### 写入 JSON {#io-json-writer}

将 DataFrame 写入 JSON 字符串：

```python
In [4]: df = pd.DataFrame([['a', 'b'], ['c', 'd']],
   ...:                   index=['row 1', 'row 2'],
   ...:                   columns=['col 1', 'col 2'])
   ...: 

In [5]: df.to_json(orient='split')
Out[5]: '{"columns":["col 1","col 2"],"index":["row 1","row 2"],"data":[["a","b"],["c","d"]]}'
```

### 读取 JSON {#io-json-reader}

读取 JSON 文件或字符串为 DataFrame：

```python
In [6]: df = pd.DataFrame([['a', 'b'], ['c', 'd']],
   ...:                   index=['row 1', 'row 2'],
   ...:                   columns=['col 1', 'col 2'])
   ...: 

In [7]: df_json = df.to_json()

In [8]: pd.read_json(df_json)
Out[8]:
      col 1 col 2
row 1     a     b
row 2     c     d
```

## HTML {#io-read-html}

### 读取 HTML {#io-read-html}

使用 [`read_html()`](../reference/api/pandas.read_html.html#pandas.read_html "pandas.read_html") 从 HTML 页面读取表格数据：

```python
In [9]: url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list'

In [10]: pd.read_html(url)
```

### 写入 HTML {#io-html}

使用 [`DataFrame.to_html()`](../reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html") 将 DataFrame 写入 HTML 表格：

```python
In [11]: df = pd.DataFrame(np.random.randn(2, 2))

In [12]: df.to_html()
```

## Excel 文件 {#excel}

### 读取 Excel 文件 {#io-excel-reader}

```python
In [13]: pd.read_excel('path_to_file.xls', sheet_name='Sheet1')
```

### 写入 Excel 文件 {#io-excel-writer}

```python
In [14]: df.to_excel('path_to_file.xlsx', sheet_name='Sheet1')
```

## HDF5 格式 {#hdf5}

### 写入 HDF5 {#io-hdf5}

```python
In [15]: df.to_hdf('data.h5', key='df')
```

### 读取 HDF5 {#io-hdf5}

```python
In [16]: pd.read_hdf('data.h5', 'df')
```

## Parquet 格式 {#parquet}

Apache Parquet 是一种列式存储格式。

### 写入 Parquet {#io-parquet}

```python
In [17]: df.to_parquet('data.parquet')
```

### 读取 Parquet {#io-parquet}

```python
In [18]: pd.read_parquet('data.parquet')
```

## Feather 格式 {#feather}

Feather 是一种快速、轻量级的二进制格式，适用于数据帧。

### 写入 Feather {#io-feather}

```python
In [19]: df.to_feather('data.feather')
```

### 读取 Feather {#io-feather}

```python
In [20]: pd.read_feather('data.feather')
```

## SQL 数据库 {#sql}

### 读取 SQL {#io-sql}

```python
In [21]: pd.read_sql('SELECT * FROM table_name', connection)
```

### 写入 SQL {#io-sql}

```python
In [22]: df.to_sql('table_name', connection)
```

## 剪贴板 {#clipboard}

### 读取剪贴板 {#io-clipboard}

```python
In [23]: pd.read_clipboard()
```

### 写入剪贴板 {#io-clipboard}

```python
In [24]: df.to_clipboard()
```

## Pickle 格式 {#pickle}

### 写入 Pickle {#io-pickle}

```python
In [25]: df.to_pickle('data.pkl')
```

### 读取 Pickle {#io-pickle}

```python
In [26]: pd.read_pickle('data.pkl')
```

> 警告：Pickle 存在安全风险。仅在你信任的数据源上使用 pickle。

## 性能比较 {#io-perf}

以下是各种 IO 方法的非正式性能比较。实际性能取决于数据集的大小和复杂性。

一般来说：
- **Parquet** 和 **Feather** 提供最快的读取速度，特别是对于大型数据集。
- **HDF5** 提供良好的压缩和快速的随机访问。
- **CSV** 最为通用，但在处理大文件时速度较慢。
- **Pickle** 速度很快，但不适用于长期存储或不同 Python 版本之间的共享。
