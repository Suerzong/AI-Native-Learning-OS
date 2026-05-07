# 快速入门指南 {#quick-start-guide}

本教程涵盖了一些基本使用模式和最佳实践，帮助你开始使用 Matplotlib。

```python
import matplotlib.pyplot as plt
import numpy as np
```

## 简单示例 {#a-simple-example}

Matplotlib 将数据绘制在 [`Figure`](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")（例如窗口、Jupyter 小部件等）上，每个 Figure 可以包含一个或多个 [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")（一个可以用 x-y 坐标指定点的区域，在极坐标图中为 theta-r，在 3D 图中为 x-y-z 等）。创建带有 Axes 的 Figure 的最简单方法是使用 [`pyplot.subplots`](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")。然后我们可以使用 [`Axes.plot`](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") 在 Axes 上绘制数据，并使用 [`show`](../../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") 显示图形：

```python
fig, ax = plt.subplots()             # 创建一个包含单个 Axes 的 Figure
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # 在 Axes 上绘制数据
plt.show()                           # 显示 Figure
```

根据你工作的环境，`plt.show()` 可以省略。例如在 Jupyter notebook 中，它会自动显示代码单元格中创建的所有图形。

## Figure 的组成部分 {#parts-of-a-figure}

以下是 Matplotlib Figure 的组件。

### `Figure` {#figure}

**整个**图形。Figure 跟踪所有子 [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")、一组"特殊的" Artist（标题、图例、颜色条等），甚至嵌套的子图。

通常，你会通过以下函数之一创建新的 Figure：

```python
fig = plt.figure()             # 一个没有 Axes 的空 Figure
fig, ax = plt.subplots()       # 一个带有单个 Axes 的 Figure
fig, axs = plt.subplots(2, 2)  # 一个带有 2x2 网格 Axes 的 Figure
# 一个左侧有一个 Axes、右侧有两个的 Figure：
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
```

[`subplots()`](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots") 和 [`subplot_mosaic`](../../api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic") 是便捷函数，会在 Figure 中额外创建 Axes 对象，但你也可以稍后手动添加 Axes。

### `Axes` {#axes}

Axes 是附加到 Figure 上的 Artist，包含用于绘制数据的区域，通常包括两个（或在 3D 情况下三个）[`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") 对象（注意 **Axes** 和 **Axis** 的区别），这些对象提供刻度和刻度标签以为 Axes 中的数据提供标度。每个 [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") 还有一个标题（通过 [`set_title()`](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") 设置）、x 标签（通过 [`set_xlabel()`](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") 设置）和 y 标签（通过 [`set_ylabel()`](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") 设置）。

[`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") 方法是配置图表大部分内容的主要接口（添加数据、控制轴标度和限制、添加标签等）。

### `Axis` {#axis}

这些对象设置标度和限制，生成刻度（Axis 上的标记）和刻度标签（标记刻度的字符串）。刻度的位置由 [`Locator`](../../api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") 对象确定，刻度标签字符串由 [`Formatter`](../../api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter") 格式化。正确的 [`Locator`](../../api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") 和 [`Formatter`](../../api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter") 的组合可以很好地控制刻度位置和标签。

### `Artist` {#artist}

基本上，Figure 上所有可见的东西都是 Artist（甚至 [`Figure`](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")、[`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") 和 [`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") 对象也是如此）。这包括 [`Text`](../../api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") 对象、[`Line2D`](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") 对象、[`collections`](../../api/collections_api.html#module-matplotlib.collections "matplotlib.collections") 对象、[`Patch`](../../api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch") 对象等。当 Figure 被渲染时，所有 Artist 都被绘制到**画布（canvas）**上。大多数 Artist 都绑定到一个 Axes；这样的 Artist 不能被多个 Axes 共享，也不能从一个 Axes 移动到另一个。

## 绘图函数的输入类型 {#types-of-inputs-to-plotting-functions}

绘图函数期望 [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "\(in NumPy v2.4\)") 或 [`numpy.ma.masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "\(in NumPy v2.4\)") 作为输入，或者可以传递给 [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "\(in NumPy v2.4\)") 的对象。类似数组的类（"array-like"），如 [`pandas`](https://pandas.pydata.org/pandas-docs/stable/index.html#module-pandas "\(in pandas v3.0.2\)") 数据对象和 [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "\(in NumPy v2.4\)") 可能无法按预期工作。常见约定是在绘图前将这些转换为 [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "\(in NumPy v2.4\)") 对象。

大多数方法还会解析字符串可索引对象，如*字典*、[结构化 numpy 数组](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays)或 [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.2\)")。Matplotlib 允许你提供 `data` 关键字参数，并生成传递对应于*x*和*y*变量的字符串的图。

## 编程风格 {#coding-styles}

### 面向对象接口 vs pyplot 接口 {#oo-interface-vs-pyplot-interface}

上面，我们使用显式的"面向对象"（OO）风格来创建图形和 Axes，然后调用它们的方法。而使用 pyplot 风格时，pyplot 会隐式地跟踪当前的 Figure 和 Axes，所有 pyplot 函数都应用于当前的 Axes。

```python
# 面向对象风格
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='线性')
ax.plot(x, x**2, label='二次')
ax.plot(x, x**3, label='三次')
ax.set_xlabel('x 轴')
ax.set_ylabel('y 轴')
ax.set_title("简单图例")
ax.legend()
plt.show()
```

```python
# pyplot 风格
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='线性')
plt.plot(x, x**2, label='二次')
plt.plot(x, x**3, label='三次')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.title("简单图例")
plt.legend()
plt.show()
```

> 建议：对于简单的方法调用，两种风格之间的区别很小。对于更复杂的绘图，或者在库中嵌入 Matplotlib 时，OO 风格更受推荐。

### 在函数中绘图 {#making-a-helper-functions}

如果你想在多个不同的数据集上使用相同的绘图，或者想要封装绘图逻辑，可以创建一个函数：

```python
def my_plotter(ax, data1, data2, param_dict):
    """
    一个将数据1和数据2绘制到 Axes 上的辅助函数。
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
```

然后使用它：

```python
fig, ax = plt.subplots(1, 1)
my_plotter(ax, x, x, {'marker': 'x'})
```

## 样式设置 {#styling}

### 使用 `style` 设置 {#using-styles}

Matplotlib 有许多内置的样式表：

```python
plt.style.use('ggplot')
```

可用的样式包括：
- `default`
- `classic`
- `ggplot`
- `seaborn-v0_8`
- `fivethirtyeight`
- `dark_background`
- `bmh`
- 等等

查看所有可用样式：

```python
print(plt.style.available)
```

### 交互模式 {#interactive-mode}

`plt.ion()` 打开交互模式，`plt.ioff()` 关闭它。在交互模式下，图形会在每次绘图命令后自动更新。

## 保存图形 {#saving-figures}

使用 `savefig` 方法可以将图形保存到文件：

```python
fig.savefig('my_figure.png')
fig.savefig('my_figure.pdf')
fig.savefig('my_figure.svg')
```

支持的格式包括：PNG、PDF、SVG、PS、EPS 等。

## 处理日期 {#handling-dates}

Matplotlib 可以处理日期时间数据：

```python
import matplotlib.dates as mdates

fig, ax = plt.subplots()
ax.plot(dates, data)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()  # 自动旋转日期标签
```

## 其他资源 {#further-reading}

- [Matplotlib 教程](../../tutorials/index.html)
- [Matplotlib 示例](../../gallery/index.html)
- [Matplotlib API 参考](../../api/index.html)
