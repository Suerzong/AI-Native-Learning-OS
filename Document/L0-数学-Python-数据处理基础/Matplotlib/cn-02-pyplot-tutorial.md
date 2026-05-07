# Pyplot 教程 {#pyplot-tutorial}

pyplot 接口介绍。请同时参阅[快速入门指南](../users/explain/quick_start.html#quick-start)了解 Matplotlib 工作原理的概述，以及 [Matplotlib 应用接口（APIs）](../users/explain/figure/api_interfaces.html#api-interfaces)了解支持的用户 API 之间的权衡。

## pyplot 简介 {#introduction-to-pyplot}

[`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") 是一个使 matplotlib 类似于 MATLAB 工作的函数集合。每个 `pyplot` 函数对图形做一些更改：例如，创建图形、在图形中创建绘图区域、在绘图区域中绘制一些线条、用标签装饰图形等。

在 [`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") 中，各种状态在函数调用之间被保留，因此它跟踪当前图形和绘图区域等，绘图函数被定向到当前的 Axes（请注意我们使用大写的 Axes 来引用 [`Axes`](../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") 概念，它是图形的中心[组成部分](../users/explain/quick_start.html#figure-parts)，而不仅仅是 *axis* 的复数形式）。

> 注意：隐式 pyplot API 通常不那么冗长，但也不如显式 API 灵活。你在这里看到的大多数函数调用也可以作为 `Axes` 对象的方法调用。我们建议浏览教程和示例以了解其工作原理。

使用 pyplot 生成可视化非常快速：

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('一些数字')
plt.show()
```

你可能想知道为什么 x 轴的范围是 0-3，y 轴是 1-4。如果你向 [`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") 提供单个列表或数组，matplotlib 假设它是 y 值序列，并自动生成 x 值。由于 Python 范围从 0 开始，默认的 x 向量与 y 长度相同但从 0 开始；因此 x 数据是 `[0, 1, 2, 3]`。

[`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") 是一个多功能函数，可以接受任意数量的参数。例如，要绘制 x 与 y 的关系，你可以写：

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

### 设置绘图样式 {#formatting-the-style-of-your-plot}

对于每对 x, y 参数，有一个可选的第三个参数，即指示绘图颜色和线型的格式字符串。格式字符串的字母和符号来自 MATLAB，你将颜色字符串与线型字符串连接起来。默认格式字符串是 'b-'，即实心蓝线。例如，要用红色圆圈绘制上面的图，你可以写：

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis((0, 6, 0, 20))
plt.show()
```

请参阅 [`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") 文档获取线型和格式字符串的完整列表。

如果 matplotlib 限于处理列表，那对数值处理来说就相当没用了。通常，你会使用 [numpy](https://numpy.org/) 数组。实际上，所有序列在内部都会转换为 numpy 数组。下面的示例说明了在一个函数调用中使用数组绘制具有不同格式样式的多条线。

```python
import numpy as np

# 以 200ms 间隔均匀采样的时间
t = np.arange(0., 5., 0.2)

# 红色虚线、蓝色方块和绿色三角形
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

## 使用关键字字符串绘图 {#plotting-with-keyword-strings}

有些情况下，你拥有的数据格式允许你用字符串访问特定变量。例如，使用[结构化数组](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays)或 [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.2\)")。

Matplotlib 允许你通过 `data` 关键字参数提供这样的对象。如果提供了，那么你可以用这些变量对应的字符串生成图。

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('条目 a')
plt.ylabel('条目 b')
plt.show()
```

## 使用分类变量绘图 {#plotting-with-categorical-variables}

也可以使用分类变量创建图。Matplotlib 允许你将分类变量直接传递给许多绘图函数。例如：

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('分类绘图')
plt.show()
```

## 控制线条属性 {#controlling-line-properties}

线条有许多你可以设置的属性：线宽、虚线样式、抗锯齿等；参见 [`matplotlib.lines.Line2D`](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")。有几种设置线条属性的方法：

- 使用关键字参数：

```python
plt.plot(x, y, linewidth=2.0)
```

- 使用 `Line2D` 实例的 setter 方法。`plot` 返回 `Line2D` 对象的列表：

```python
line, = plt.plot(x, y, '-')
line.set_antialiased(False)  # 关闭抗锯齿
```

- 使用 [`setp`](../api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")。以下示例使用 MATLAB 风格的函数在一组线条上设置多个属性：

```python
lines = plt.plot(x1, y1, x2, y2)
# 使用关键字参数
plt.setp(lines, color='r', linewidth=2.0)
# 或 MATLAB 风格的字符串/值对
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
```

## 在同一图形上处理多个图形和轴 {#working-with-multiple-figures-and-axes}

MATLAB 和 pyplot 都有当前图形和当前轴的概念。所有绘图函数都应用于当前轴。[`gca()`](../api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca") 返回当前轴（[`matplotlib.axes.Axes`](../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") 实例），[`gcf()`](../api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf") 返回当前图形（[`matplotlib.figure.Figure`](../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") 实例）。通常，这对你来说是隐藏的。

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

[`clf()`](../api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf") 和 [`cla()`](../api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla "matplotlib.pyplot.cla") 分别用于清除当前图形和当前轴。

## 添加文本 {#working-with-text}

[`text()`](../api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text") 可以在任意位置添加文本，[`xlabel()`](../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")、[`ylabel()`](../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel") 和 [`title()`](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title") 分别用于在指定位置添加文本。

```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# 直方图
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('智商')
plt.ylabel('概率')
plt.title('智商直方图')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

### 添加注释 {#annotating-text}

[`annotate()`](../api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate") 方法可以在图中的任意位置添加注释，同时可以添加箭头指示注释指向的位置。

```python
ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('局部最大值', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
```

## 对数轴和其他非线性轴 {#logarithmic-and-other-nonlinear-axes}

[`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") 不仅支持线性轴刻度，还支持对数和 logit 刻度。如果数据跨越多个数量级，这通常很有用。更改轴刻度很容易：

```python
plt.xscale('log')
plt.yscale('log')
```

示例：

```python
# 修复随机状态以确保可重现性
np.random.seed(19680801)

# 创建一些数据
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# 带对数轴的图
plt.figure()
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('线性')
plt.grid(True)

plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('对数')
plt.grid(True)

plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('对称对数')
plt.grid(True)

plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit')
plt.grid(True)

plt.show()
```
