# 时间序列 / 日期功能 {#time-series-date-functionality}

pandas 包含用于处理所有领域时间序列数据的广泛能力和特性。使用 NumPy `datetime64` 和 `timedelta64` 数据类型，pandas 整合了来自其他 Python 库（如 `scikits.timeseries`）的大量特性，并为处理时间序列数据创建了大量新功能。

例如，pandas 支持：

从各种来源和格式解析时间序列信息：

```python
In [1]: import datetime

In [2]: dti = pd.to_datetime(
   ...:     ["1/1/2018", np.datetime64("2018-01-01"), datetime.datetime(2018, 1, 1)]
   ...: )
   ...: 

In [3]: dti
Out[3]: DatetimeIndex(['2018-01-01', '2018-01-01', '2018-01-01'], dtype='datetime64[us]', freq=None)
```

生成固定频率的日期和时间跨度序列：

```python
In [4]: dti = pd.date_range("2018-01-01", periods=3, freq="h")

In [5]: dti
Out[5]: 
DatetimeIndex(['2018-01-01 00:00:00', '2018-01-01 01:00:00',
               '2018-01-01 02:00:00'],
              dtype='datetime64[us]', freq='h')
```

使用时区信息操作和转换日期时间：

```python
In [6]: dti = dti.tz_localize("UTC")

In [7]: dti
Out[7]: 
DatetimeIndex(['2018-01-01 00:00:00+00:00', '2018-01-01 01:00:00+00:00',
               '2018-01-01 02:00:00+00:00'],
              dtype='datetime64[us, UTC]', freq='h')

In [8]: dti.tz_convert("US/Pacific")
Out[8]: 
DatetimeIndex(['2017-12-31 16:00:00-08:00', '2017-12-31 17:00:00-08:00',
               '2017-12-31 18:00:00-08:00'],
              dtype='datetime64[us, US/Pacific]', freq='h')
```

重采样或将时间序列转换为特定频率：

```python
In [9]: idx = pd.date_range("2018-01-01", periods=5, freq="h")

In [10]: ts = pd.Series(range(len(idx)), index=idx)

In [11]: ts
Out[11]: 
2018-01-01 00:00:00    0
2018-01-01 01:00:00    1
2018-01-01 02:00:00    2
2018-01-01 03:00:00    3
2018-01-01 04:00:00    4
Freq: h, dtype: int64

In [12]: ts.resample("2h").mean()
Out[12]: 
2018-01-01 00:00:00    0.5
2018-01-01 02:00:00    2.5
2018-01-01 04:00:00    4.0
Freq: 2h, dtype: float64
```

使用绝对或相对时间增量执行日期和时间算术：

```python
In [13]: friday = pd.Timestamp("2018-01-05")

In [14]: friday.day_name()
Out[14]: 'Friday'

# 加 1 天
In [15]: saturday = friday + pd.Timedelta("1 day")

In [16]: saturday.day_name()
Out[16]: 'Saturday'

# 加 1 个工作日（周五 --> 周一）
In [17]: monday = friday + pd.offsets.BDay()

In [18]: monday.day_name()
Out[18]: 'Monday'
```

pandas 提供了一套相对紧凑且自包含的工具来执行上述任务等。

## 概述 {#overview}

pandas 捕获 4 个一般时间相关概念：

1. **日期时间（Date times）**：具有时区支持的特定日期和时间。类似于标准库中的 `datetime.datetime`。

2. **时间增量（Time deltas）**：绝对时间持续。类似于标准库中的 `datetime.timedelta`。

3. **时间跨度（Time spans）**：由时间点及其关联频率定义的一段时间。

4. **日期偏移（Date offsets）**：遵循日历算术的相对时间持续。类似于 `dateutil` 包中的 `dateutil.relativedelta.relativedelta`。

| 概念 | 标量类 | 数组类 | pandas 数据类型 | 主要创建方法 |
|------|--------|--------|----------------|------------|
| 日期时间 | `Timestamp` | `DatetimeIndex` | `datetime64[ns]` 或 `datetime64[ns, tz]` | `to_datetime` 或 `date_range` |
| 时间增量 | `Timedelta` | `TimedeltaIndex` | `timedelta64[ns]` | `to_timedelta` 或 `timedelta_range` |
| 时间跨度 | `Period` | `PeriodIndex` | `period[freq]` | `Period` 或 `period_range` |
| 日期偏移 | `DateOffset` | `None` | `None` | `DateOffset` |

对于时间序列数据，通常将时间成分表示在 [`Series`](../reference/api/pandas.Series.html#pandas.Series "pandas.Series") 或 [`DataFrame`](../reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 的索引中，以便可以针对时间元素执行操作。

```python
In [19]: pd.Series(range(3), index=pd.date_range("2000", freq="D", periods=3))
Out[19]: 
2000-01-01    0
2000-01-02    1
2000-01-03    2
Freq: D, dtype: int64
```

## 时间戳（Timestamp）vs 时间段（Period） {#timestamp-vs-period}

Timestamp 表示时间轴上的一个点。Period 表示时间轴上的一个间隔。

```python
In [20]: pd.Timestamp(datetime.datetime(2012, 5, 1))
Out[20]: Timestamp('2012-05-01 00:00:00')

In [21]: pd.Timestamp('2012-05-01')
Out[21]: Timestamp('2012-05-01 00:00:00')

In [22]: pd.Timestamp(2012, 5, 1)
Out[22]: Timestamp('2012-05-01 00:00:00')
```

## DatetimeIndex {#datetimeindex}

`DatetimeIndex` 是 pandas 中时间序列的核心数据结构。它提供了许多专门用于处理时间序列的方法。

### 创建 DatetimeIndex {#creating-datetimeindex}

```python
# 使用 date_range
In [23]: pd.date_range('2000-01-01', periods=3, freq='D')
Out[23]: DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='datetime64[us]', freq='D')

# 使用 to_datetime
In [24]: pd.to_datetime(['2000-01-01', '2000-01-02', '2000-01-03'])
Out[24]: DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='datetime64[us]', freq=None)
```

### 日期范围生成 {#date-range-generation}

`date_range` 是创建 `DatetimeIndex` 的主要方式：

```python
In [25]: pd.date_range(start='1/1/2018', end='1/08/2018')
Out[25]: DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
              dtype='datetime64[us]', freq='D')

In [26]: pd.date_range(start='1/1/2018', periods=8)
Out[26]: DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
              dtype='datetime64[us]', freq='D')
```

### 频率（Frequency） {#frequency}

pandas 支持多种频率别名：

| 别名 | 描述 |
|------|------|
| `D` | 日历日 |
| `B` | 工作日 |
| `h` | 小时 |
| `min` | 分钟 |
| `s` | 秒 |
| `ms` | 毫秒 |
| `M` | 月末 |
| `MS` | 月初 |
| `Q` | 季度末 |
| `QS` | 季度初 |
| `A` | 年末 |
| `AS` | 年初 |
| `W` | 周 |

## 时区处理 {#time-zone-handling}

### 本地化（Localization） {#localization}

使用 `tz_localize` 为朴素时间戳添加时区信息：

```python
In [27]: ts = pd.Series(range(3), index=pd.date_range('2000', periods=3, freq='D'))

In [28]: ts_utc = ts.tz_localize('UTC')
```

### 转换（Conversion） {#conversion}

使用 `tz_convert` 在不同时区之间转换：

```python
In [29]: ts_utc.tz_convert('US/Pacific')
```

## 重采样（Resampling） {#resampling}

重采样是指将时间序列从一个频率转换为另一个频率的过程。`resample` 方法类似于 `groupby`，但专门用于时间序列。

### 降采样（Downsampling） {#downsampling}

将高频数据转换为低频数据：

```python
In [30]: ts = pd.Series(range(24), index=pd.date_range('2000-01-01', periods=24, freq='h'))

In [31]: ts.resample('D').mean()
Out[31]: 
2000-01-01    5.5
2000-01-01   17.5
Freq: D, dtype: float64
```

### 升采样（Upsampling） {#upsampling}

将低频数据转换为高频数据：

```python
In [32]: ts = pd.Series([1, 2], index=pd.date_range('2000-01-01', periods=2, freq='D'))

In [33]: ts.resample('12h').ffill()
Out[33]: 
2000-01-01 00:00:00    1
2000-01-01 12:00:00    1
2000-01-02 00:00:00    2
Freq: 12h, dtype: int64
```

## 时间增量（Timedelta） {#timedelta}

时间增量表示两个日期或时间之间的持续时间。

```python
In [34]: pd.Timedelta('1 days')
Out[34]: Timedelta('1 days 00:00:00')

In [35]: pd.Timedelta('1 days 2 hours 3 minutes')
Out[35]: Timedelta('1 days 02:03:00')

In [36]: pd.Timedelta(days=1, hours=2, minutes=3)
Out[36]: Timedelta('1 days 02:03:00')
```

### 时间增量范围 {#timedelta-range}

```python
In [37]: pd.timedelta_range(start='1 day', periods=5, freq='D')
Out[37]: TimedeltaIndex(['1 days', '2 days', '3 days', '4 days', '5 days'], dtype='timedelta64[ns]', freq='D')
```

## 时间跨度（Period） {#period}

Period 表示一个时间间隔，如某天、某月或某年。

```python
In [38]: pd.Period('2012-01', freq='M')
Out[38]: Period('2012-01', 'M')

In [39]: pd.period_range('2012-01', periods=5, freq='M')
Out[39]: PeriodIndex(['2012-01', '2012-02', '2012-03', '2012-04', '2012-05'], dtype='period[M]')
```

## 日期偏移（Date Offset） {#date-offset}

日期偏移遵循日历算术，可用于执行复杂的日期计算：

```python
In [40]: ts = pd.Timestamp('2020-03-28')

In [41]: ts + pd.DateOffset(months=1)
Out[41]: Timestamp('2020-04-28 00:00:00')
```

常用的日期偏移类：

| 类 | 描述 |
|-----|------|
| `BDay` | 工作日 |
| `MonthEnd` | 月末 |
| `MonthBegin` | 月初 |
| `QuarterEnd` | 季度末 |
| `QuarterBegin` | 季度初 |
| `YearEnd` | 年末 |
| `YearBegin` | 年初 |
| `Hour` | 小时 |
| `Minute` | 分钟 |
| `Second` | 秒 |

## 窗口函数 {#window-functions}

pandas 提供了滚动窗口（rolling）和扩展窗口（expanding）函数，用于时间序列分析：

### 滚动窗口 {#rolling}

```python
In [42]: ts = pd.Series(range(10), index=pd.date_range('2000', periods=10, freq='D'))

In [43]: ts.rolling(window=3).mean()
Out[43]: 
2000-01-01    NaN
2000-01-02    NaN
2000-01-03    1.0
2000-01-04    2.0
2000-01-05    3.0
2000-01-06    4.0
2000-01-07    5.0
2000-01-08    6.0
2000-01-09    7.0
2000-01-10    8.0
Freq: D, dtype: float64
```

### 扩展窗口 {#expanding}

```python
In [44]: ts.expanding().mean()
```

## 滞后和前导 {#lagging-and-leading}

使用 `shift` 方法可以移动数据：

```python
In [45]: ts.shift(1)  # 滞后 1 期
In [46]: ts.shift(-1)  # 前导 1 期
```

## 日期时间属性访问器 {#datetime-properties}

DatetimeIndex 和 Timestamp 对象提供了许多属性来访问日期时间的各个部分：

```python
In [47]: dti = pd.date_range('2000-01-01', periods=5, freq='D')

In [48]: dti.year
Out[48]: Index([2000, 2000, 2000, 2000, 2000], dtype='int32')

In [49]: dti.month
Out[49]: Index([1, 1, 1, 1, 1], dtype='int32')

In [50]: dti.day
Out[50]: Index([1, 2, 3, 4, 5], dtype='int32')

In [51]: dti.day_name()
Out[51]: Index(['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'], dtype='object')
```

## 处理缺失时间数据 {#missing-time-data}

NaT（Not a Time）是 pandas 中表示缺失时间数据的特殊值：

```python
In [52]: pd.Series([pd.Timestamp('2020-01-01'), pd.NaT, pd.Timestamp('2020-01-03')])
Out[52]: 
0   2020-01-01
1          NaT
2   2020-01-03
dtype: datetime64[us]
```
