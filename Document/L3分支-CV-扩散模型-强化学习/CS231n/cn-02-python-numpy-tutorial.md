[ ![Colab Notebook](/assets/badges/colab-open.svg) ](https://colab.research.google.com/github/cs231n/cs231n.github.io/blob/master/python-colab.ipynb)

本教程最初由 [Justin Johnson](http://cs.stanford.edu/people/jcjohns/) 贡献。

本课程的所有作业都将使用 Python 编程语言。Python 本身是一门优秀的通用编程语言，借助几个流行库（numpy、scipy、matplotlib），它就变成了一个强大的科学计算环境。

我们预计你们中许多人已经有一些 Python 和 numpy 的使用经验；对于其他人，本节将作为 Python 编程语言及其在科学计算中应用的快速入门课程。我们还将介绍笔记本（notebooks），这是一种非常方便的 Python 代码实验方式。如果你已有其他编程语言的基础，我们还推荐参考：[NumPy for Matlab users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)、[Python for R users](http://www.data-analysis-in-python.org/python_for_r.html)、以及 [Python for SAS users](https://nbviewer.jupyter.org/github/RandyBetancourt/PythonForSASUsers/tree/master/)。

**目录**

  * Jupyter 和 Colab 笔记本
  * Python
    * Python 版本
    * 基本数据类型
    * 容器
      * 列表（Lists）
      * 字典（Dictionaries）
      * 集合（Sets）
      * 元组（Tuples）
    * 函数（Functions）
    * 类（Classes）
  * Numpy
    * 数组（Arrays）
    * 数组索引
    * 数据类型
    * 数组运算
    * 广播（Broadcasting）
    * Numpy 文档
  * SciPy
    * 图像操作
    * MATLAB 文件
    * 点之间的距离
  * Matplotlib
    * 绘图
    * 子图
    * 图像

## Jupyter 和 Colab 笔记本

在深入 Python 之前，我们先简要介绍「笔记本」（notebooks）。Jupyter 笔记本让你可以在浏览器中**本地**编写和执行 Python 代码。Jupyter 笔记本非常适合分块调试和执行代码，因此在科学计算中被广泛使用。Colab 则是 Google 版本的 Jupyter 笔记本，特别适合机器学习和数据分析，完全在**云端**运行。Colab 相当于加强版的 Jupyter 笔记本：免费、无需配置、预装了许多库、易于分享，并且可以免费使用 GPU 和 TPU 等硬件加速器（有一些限制）。

**在 Colab 中运行教程（推荐）**。如果你想完全在 Colab 中运行本教程，请点击页面顶部的「Open in Colab」徽章。

**在 Jupyter Notebook 中运行教程**。如果你想在本地用 Jupyter 运行笔记本，请确保虚拟环境已正确安装（按照[配置说明](/setup-instructions/)），激活它，然后运行 `pip install notebook` 安装 Jupyter notebook。接下来，[打开笔记本](https://raw.githubusercontent.com/cs231n/cs231n.github.io/master/jupyter-notebook-tutorial.ipynb)，右键点击页面选择「另存为」将其下载到你选择的目录。然后 `cd` 到该目录并运行 `jupyter notebook`。

![](/assets/ipython-tutorial/file-browser.png)

这将在 `http://localhost:8888` 自动启动笔记本服务器。如果一切正常，你应该看到类似这样的界面，显示当前目录中的所有可用笔记本。点击 `jupyter-notebook-tutorial.ipynb` 并按照笔记本中的说明操作。或者，你也可以继续阅读下面的代码片段教程。

## Python

Python 是一种高级、动态类型的多范式编程语言。Python 代码通常被认为几乎像伪代码，因为它允许你用很少的代码行表达非常强大的想法，同时具有很好的可读性。以下是一个用 Python 实现的经典快速排序算法：


    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    print(quicksort([3,6,8,10,1,2,1]))
    # 输出 "[1, 1, 2, 3, 6, 8, 10]"


### Python 版本

自 2020 年 1 月 1 日起，Python 已[正式停止支持](https://www.python.org/doc/sunset-python-2/) `python2`。**本课程所有代码将使用 Python 3.7**。请确保在继续本教程前已完成[配置说明](/setup-instructions/)并正确安装了 `python3` 虚拟环境。你可以在激活环境后在命令行运行 `python --version` 来验证 Python 版本。

### 基本数据类型

与大多数语言一样，Python 有多种基本类型，包括整数（int）、浮点数（float）、布尔值（bool）和字符串（string）。这些数据类型的行为方式与其他编程语言类似。

**数字：** 整数和浮点数的用法与其他语言一致：


    x = 3
    print(type(x)) # 输出 "<class 'int'>"
    print(x)       # 输出 "3"
    print(x + 1)   # 加法；输出 "4"
    print(x - 1)   # 减法；输出 "2"
    print(x * 2)   # 乘法；输出 "6"
    print(x ** 2)  # 乘方；输出 "9"
    x += 1
    print(x)  # 输出 "4"
    x *= 2
    print(x)  # 输出 "8"
    y = 2.5
    print(type(y)) # 输出 "<class 'float'>"
    print(y, y + 1, y * 2, y ** 2) # 输出 "2.5 3.5 5.0 6.25"


注意，与许多语言不同，Python 没有一元自增（`x++`）或自减（`x--`）运算符。

Python 还内置了复数类型；你可以在[文档](https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex)中找到所有细节。

**布尔值：** Python 实现了所有常见的布尔逻辑运算符，但使用英文单词而非符号（`&&`、`||` 等）：


    t = True
    f = False
    print(type(t)) # 输出 "<class 'bool'>"
    print(t and f) # 逻辑与；输出 "False"
    print(t or f)  # 逻辑或；输出 "True"
    print(not t)   # 逻辑非；输出 "False"
    print(t != f)  # 逻辑异或；输出 "True"


**字符串：** Python 对字符串有很好的支持：


    hello = 'hello'    # 字符串可以用单引号
    world = "world"    # 也可以用双引号；效果相同
    print(hello)       # 输出 "hello"
    print(len(hello))  # 字符串长度；输出 "5"
    hw = hello + ' ' + world  # 字符串拼接
    print(hw)  # 输出 "hello world"
    hw12 = '%s %s %d' % (hello, world, 12)  # sprintf 风格的字符串格式化
    print(hw12)  # 输出 "hello world 12"


字符串对象有许多有用的方法，例如：


    s = "hello"
    print(s.capitalize())  # 首字母大写；输出 "Hello"
    print(s.upper())       # 转换为大写；输出 "HELLO"
    print(s.rjust(7))      # 右对齐，用空格填充；输出 "  hello"
    print(s.center(7))     # 居中，用空格填充；输出 " hello "
    print(s.replace('l', '(ell)'))  # 替换所有子串；
                                    # 输出 "he(ell)(ell)o"
    print('  world '.strip())  # 去除首尾空白；输出 "world"


你可以在[文档](https://docs.python.org/3.5/library/stdtypes.html#string-methods)中找到所有字符串方法的列表。

### 容器

Python 包含几种内置容器类型：列表（lists）、字典（dictionaries）、集合（sets）和元组（tuples）。

#### 列表（Lists）

列表是 Python 中等价于数组的数据类型，但可以调整大小且可以包含不同类型的元素：


    xs = [3, 1, 2]    # 创建一个列表
    print(xs, xs[2])  # 输出 "[3, 1, 2] 2"
    print(xs[-1])     # 负数索引从列表末尾开始计数；输出 "2"
    xs[2] = 'foo'     # 列表可以包含不同类型的元素
    print(xs)         # 输出 "[3, 1, 'foo']"
    xs.append('bar')  # 在列表末尾添加新元素
    print(xs)         # 输出 "[3, 1, 'foo', 'bar']"
    x = xs.pop()      # 移除并返回列表末尾的元素
    print(x, xs)      # 输出 "bar [3, 1, 'foo']"


你可以在[文档](https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists)中找到关于列表的所有细节。

**切片（Slicing）：** 除了逐个访问列表元素外，Python 还提供了简洁的语法来访问子列表，称为「切片」：


    nums = list(range(5))     # range 是一个创建整数列表的内置函数
    print(nums)               # 输出 "[0, 1, 2, 3, 4]"
    print(nums[2:4])          # 获取索引 2 到 4（不含）的切片；输出 "[2, 3]"
    print(nums[2:])           # 获取从索引 2 到末尾的切片；输出 "[2, 3, 4]"
    print(nums[:2])           # 获取从开头到索引 2（不含）的切片；输出 "[0, 1]"
    print(nums[:])            # 获取整个列表的切片；输出 "[0, 1, 2, 3, 4]"
    print(nums[:-1])          # 切片索引可以为负数；输出 "[0, 1, 2, 3]"
    nums[2:4] = [8, 9]        # 给切片赋值新的子列表
    print(nums)               # 输出 "[0, 1, 8, 9, 4]"


我们稍后在 numpy 数组中还会看到切片的用法。

**循环（Loops）：** 你可以这样遍历列表的元素：


    animals = ['cat', 'dog', 'monkey']
    for animal in animals:
        print(animal)
    # 输出 "cat"、"dog"、"monkey"，每个各占一行


如果你想在循环体中同时获取每个元素的索引，使用内置的 `enumerate` 函数：


    animals = ['cat', 'dog', 'monkey']
    for idx, animal in enumerate(animals):
        print('#%d: %s' % (idx + 1, animal))
    # 输出 "#1: cat"、"#2: dog"、"#3: monkey"，每个各占一行


**列表推导式（List comprehensions）：** 编程时，我们经常需要将一种数据类型转换为另一种。简单例子：计算平方数。


    nums = [0, 1, 2, 3, 4]
    squares = []
    for x in nums:
        squares.append(x ** 2)
    print(squares)   # 输出 [0, 1, 4, 9, 16]


你可以使用**列表推导式**简化这段代码：


    nums = [0, 1, 2, 3, 4]
    squares = [x ** 2 for x in nums]
    print(squares)   # 输出 [0, 1, 4, 9, 16]


列表推导式也可以包含条件：


    nums = [0, 1, 2, 3, 4]
    even_squares = [x ** 2 for x in nums if x % 2 == 0]
    print(even_squares)  # 输出 "[0, 4, 16]"


#### 字典（Dictionaries）

字典存储（键, 值）对，类似于 Java 中的 `Map` 或 JavaScript 中的对象。用法如下：


    d = {'cat': 'cute', 'dog': 'furry'}  # 创建包含数据的字典
    print(d['cat'])       # 获取字典中的条目；输出 "cute"
    print('cat' in d)     # 检查字典是否包含某个键；输出 "True"
    d['fish'] = 'wet'     # 设置字典中的条目
    print(d['fish'])      # 输出 "wet"
    # print(d['monkey'])  # KeyError: 'monkey' 不是 d 的键
    print(d.get('monkey', 'N/A'))  # 获取元素，带默认值；输出 "N/A"
    print(d.get('fish', 'N/A'))    # 获取元素，带默认值；输出 "wet"
    del d['fish']         # 从字典中删除元素
    print(d.get('fish', 'N/A')) # "fish" 不再是键；输出 "N/A"


你可以在[文档](https://docs.python.org/3.5/library/stdtypes.html#dict)中找到关于字典的所有信息。

**循环：** 遍历字典的键很简单：


    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal in d:
        legs = d[animal]
        print('A %s has %d legs' % (animal, legs))
    # 输出 "A person has 2 legs"、"A cat has 4 legs"、"A spider has 8 legs"


如果你想同时获取键和对应的值，使用 `items` 方法：


    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal, legs in d.items():
        print('A %s has %d legs' % (animal, legs))
    # 输出 "A person has 2 legs"、"A cat has 4 legs"、"A spider has 8 legs"


**字典推导式：** 类似于列表推导式，但用于轻松构造字典：


    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
    print(even_num_to_square)  # 输出 "{0: 0, 2: 4, 4: 16}"


#### 集合（Sets）

集合是无序的不同元素的集合。简单示例：


    animals = {'cat', 'dog'}
    print('cat' in animals)   # 检查元素是否在集合中；输出 "True"
    print('fish' in animals)  # 输出 "False"
    animals.add('fish')       # 向集合中添加元素
    print('fish' in animals)  # 输出 "True"
    print(len(animals))       # 集合中元素的数量；输出 "3"
    animals.add('cat')        # 添加已存在的元素不会有任何效果
    print(len(animals))       # 输出 "3"
    animals.remove('cat')     # 从集合中移除元素
    print(len(animals))       # 输出 "2"


你可以在[文档](https://docs.python.org/3.5/library/stdtypes.html#set)中找到关于集合的所有信息。

**循环：** 遍历集合的语法与遍历列表相同；但由于集合是无序的，你不能对访问元素的顺序做任何假设：


    animals = {'cat', 'dog', 'fish'}
    for idx, animal in enumerate(animals):
        print('#%d: %s' % (idx + 1, animal))
    # 输出 "#1: fish"、"#2: dog"、"#3: cat"


**集合推导式：** 与列表和字典类似，我们可以用集合推导式轻松构造集合：


    from math import sqrt
    nums = {int(sqrt(x)) for x in range(30)}
    print(nums)  # 输出 "{0, 1, 2, 3, 4, 5}"


#### 元组（Tuples）

元组是（不可变的）有序值列表。元组在很多方面与列表相似；最重要的区别之一是元组可以用作字典的键和集合的元素，而列表不能。简单示例：


    d = {(x, x + 1): x for x in range(10)}  # 创建以元组为键的字典
    t = (5, 6)        # 创建元组
    print(type(t))    # 输出 "<class 'tuple'>"
    print(d[t])       # 输出 "5"
    print(d[(1, 2)])  # 输出 "1"


[文档](https://docs.python.org/3.5/tutorial/datastructures.html#tuples-and-sequences)中有更多关于元组的信息。

### 函数（Functions）

Python 函数使用 `def` 关键字定义：


    def sign(x):
        if x > 0:
            return 'positive'
        elif x < 0:
            return 'negative'
        else:
            return 'zero'

    for x in [-1, 0, 1]:
        print(sign(x))
    # 输出 "negative"、"zero"、positive"


我们经常定义带可选关键字参数的函数：


    def hello(name, loud=False):
        if loud:
            print('HELLO, %s!' % name.upper())
        else:
            print('Hello, %s' % name)

    hello('Bob') # 输出 "Hello, Bob"
    hello('Fred', loud=True)  # 输出 "HELLO, FRED!"


关于 Python 函数的更多信息请参阅[文档](https://docs.python.org/3.5/tutorial/controlflow.html#defining-functions)。

### 类（Classes）

Python 中定义类的语法很直观：


    class Greeter(object):

        # 构造函数
        def __init__(self, name):
            self.name = name  # 创建实例变量

        # 实例方法
        def greet(self, loud=False):
            if loud:
                print('HELLO, %s!' % self.name.upper())
            else:
                print('Hello, %s' % self.name)

    g = Greeter('Fred')  # 构造 Greeter 类的实例
    g.greet()            # 调用实例方法；输出 "Hello, Fred"
    g.greet(loud=True)   # 调用实例方法；输出 "HELLO, FRED!"


更多关于 Python 类的信息请参阅[文档](https://docs.python.org/3.5/tutorial/classes.html)。

## Numpy

[Numpy](http://www.numpy.org/) 是 Python 中科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于操作这些数组的工具。如果你已经熟悉 MATLAB，可以参考[此教程](https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html)快速入门 Numpy。

### 数组（Arrays）

numpy 数组是一个值的网格，所有元素类型相同，由非负整数元组索引。维度的数量称为数组的「秩」（rank）；数组的「形状」（shape）是一个整数元组，给出数组在每个维度上的大小。

我们可以从嵌套的 Python 列表初始化 numpy 数组，并使用方括号访问元素：


    import numpy as np

    a = np.array([1, 2, 3])   # 创建秩为 1 的数组
    print(type(a))            # 输出 "<class 'numpy.ndarray'>"
    print(a.shape)            # 输出 "(3,)"
    print(a[0], a[1], a[2])   # 输出 "1 2 3"
    a[0] = 5                  # 修改数组的元素
    print(a)                  # 输出 "[5, 2, 3]"

    b = np.array([[1,2,3],[4,5,6]])    # 创建秩为 2 的数组
    print(b.shape)                     # 输出 "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])   # 输出 "1 2 4"


Numpy 还提供了许多创建数组的函数：


    import numpy as np

    a = np.zeros((2,2))   # 创建全零数组
    print(a)              # 输出 "[[ 0.  0.]
                          #          [ 0.  0.]]"

    b = np.ones((1,2))    # 创建全一数组
    print(b)              # 输出 "[[ 1.  1.]]"

    c = np.full((2,2), 7)  # 创建常量数组
    print(c)               # 输出 "[[ 7.  7.]
                           #          [ 7.  7.]]"

    d = np.eye(2)         # 创建 2x2 单位矩阵
    print(d)              # 输出 "[[ 1.  0.]
                          #          [ 0.  1.]]"

    e = np.random.random((2,2))  # 创建填充随机值的数组
    print(e)                     # 可能输出 "[[ 0.91940167  0.08143941]
                                 #               [ 0.68744134  0.87236687]]"


你可以在[文档](http://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation)中了解其他数组创建方法。

### 数组索引

Numpy 提供了多种索引数组的方法。

**切片：** 与 Python 列表类似，numpy 数组可以被切片。由于数组可能是多维的，你必须为数组的每个维度指定切片：


    import numpy as np

    # 创建以下秩为 2 的数组，形状为 (3, 4)
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

    # 使用切片提取前 2 行和第 1、2 列组成的子数组
    # b 是以下形状为 (2, 2) 的数组：
    # [[2 3]
    #  [6 7]]
    b = a[:2, 1:3]

    # 数组的切片是同一数据的视图，因此修改它
    # 会修改原始数组。
    print(a[0, 1])   # 输出 "2"
    b[0, 0] = 77     # b[0, 0] 与 a[0, 1] 是同一块数据
    print(a[0, 1])   # 输出 "77"


你也可以混合使用整数索引和切片索引。但这样会产生比原始数组秩更低的数组。注意这与 MATLAB 处理数组切片的方式有很大不同：


    import numpy as np

    # 创建以下秩为 2 的数组，形状为 (3, 4)
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

    # 访问数组中间行数据的两种方式
    # 混合整数索引和切片会产生秩更低的数组，
    # 而只使用切片会产生与原始数组相同秩的数组：
    row_r1 = a[1, :]    # a 的第二行的秩 1 视图
    row_r2 = a[1:2, :]  # a 的第二行的秩 2 视图
    print(row_r1, row_r1.shape)  # 输出 "[5 6 7 8] (4,)"
    print(row_r2, row_r2.shape)  # 输出 "[[5 6 7 8]] (1, 4)"

    # 访问数组列时也可以做同样的区分：
    col_r1 = a[:, 1]
    col_r2 = a[:, 1:2]
    print(col_r1, col_r1.shape)  # 输出 "[ 2  6 10] (3,)"
    print(col_r2, col_r2.shape)  # 输出 "[[ 2]
                                 #          [ 6]
                                 #          [10]] (3, 1)"


**整数数组索引：** 当你使用切片索引 numpy 数组时，结果数组视图始终是原始数组的子数组。相比之下，整数数组索引允许你使用另一个数组的数据构造任意数组。示例：


    import numpy as np

    a = np.array([[1,2], [3, 4], [5, 6]])

    # 整数数组索引示例
    # 返回的数组形状为 (3,)
    print(a[[0, 1, 2], [0, 1, 0]])  # 输出 "[1 4 5]"

    # 上面的整数数组索引示例等价于：
    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # 输出 "[1 4 5]"

    # 使用整数数组索引时，可以重复使用
    # 源数组中的同一元素：
    print(a[[0, 0], [1, 1]])  # 输出 "[2 2]"

    # 等价于上一个整数数组索引示例
    print(np.array([a[0, 1], a[0, 1]]))  # 输出 "[2 2]"


整数数组索引的一个有用技巧是选择或修改矩阵每行中的一个元素：


    import numpy as np

    # 创建一个新数组用于选择元素
    a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

    print(a)  # 输出 "array([[ 1,  2,  3],
              #                [ 4,  5,  6],
              #                [ 7,  8,  9],
              #                [10, 11, 12]])"

    # 创建索引数组
    b = np.array([0, 2, 0, 1])

    # 使用 b 中的索引从 a 的每行选择一个元素
    print(a[np.arange(4), b])  # 输出 "[ 1  6  7 11]"

    # 使用 b 中的索引修改 a 的每行中的一个元素
    a[np.arange(4), b] += 10

    print(a)  # 输出 "array([[11,  2,  3],
              #                [ 4,  5, 16],
              #                [17,  8,  9],
              #                [10, 21, 12]])"


**布尔数组索引：** 布尔数组索引让你可以选择数组中的任意元素。这种索引通常用于选择满足某些条件的数组元素。示例：


    import numpy as np

    a = np.array([[1,2], [3, 4], [5, 6]])

    bool_idx = (a > 2)   # 找出 a 中大于 2 的元素；
                         # 返回一个布尔 numpy 数组，形状与 a 相同，
                         # bool_idx 中的每个位置告诉
                         # a 中对应的元素是否 > 2。

    print(bool_idx)      # 输出 "[[False False]
                         #          [ True  True]
                         #          [ True  True]]"

    # 使用布尔数组索引构造一个秩 1 数组
    # 由 bool_idx 中对应 True 值的 a 的元素组成
    print(a[bool_idx])  # 输出 "[3 4 5 6]"

    # 上述所有操作可以用一条简洁语句完成：
    print(a[a > 2])     # 输出 "[3 4 5 6]"


为了简洁，我们省略了许多关于 numpy 数组索引的细节；如果你想了解更多，请[阅读文档](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html)。

### 数据类型（Datatypes）

每个 numpy 数组都是相同类型的元素网格。Numpy 提供了一组大量的数值数据类型用于构造数组。Numpy 在创建数组时会尝试猜测数据类型，但构造数组的函数通常也包含一个可选参数来显式指定数据类型：


    import numpy as np

    x = np.array([1, 2])   # 让 numpy 选择数据类型
    print(x.dtype)         # 输出 "int64"

    x = np.array([1.0, 2.0])   # 让 numpy 选择数据类型
    print(x.dtype)             # 输出 "float64"

    x = np.array([1, 2], dtype=np.int64)   # 强制指定数据类型
    print(x.dtype)                         # 输出 "int64"


你可以在[文档](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)中了解所有 numpy 数据类型。

### 数组运算

基本数学函数对数组进行逐元素操作，既可以通过运算符重载使用，也可以通过 numpy 模块中的函数使用：


    import numpy as np

    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    # 逐元素求和；两种方式都产生
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print(x + y)
    print(np.add(x, y))

    # 逐元素求差；两种方式都产生
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print(x - y)
    print(np.subtract(x, y))

    # 逐元素求积；两种方式都产生
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print(x * y)
    print(np.multiply(x, y))

    # 逐元素除法；两种方式都产生
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print(x / y)
    print(np.divide(x, y))

    # 逐元素平方根；产生
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print(np.sqrt(x))


注意，与 MATLAB 不同，`*` 是逐元素乘法，而不是矩阵乘法。我们使用 `dot` 函数来计算向量的内积、向量与矩阵相乘以及矩阵相乘。`dot` 既可作为 numpy 模块中的函数使用，也可作为数组对象的实例方法使用：


    import numpy as np

    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])

    # 向量内积；两种方式都产生 219
    print(v.dot(w))
    print(np.dot(v, w))

    # 矩阵/向量乘积；两种方式都产生秩 1 数组 [29 67]
    print(x.dot(v))
    print(np.dot(x, v))

    # 矩阵/矩阵乘积；两种方式都产生秩 2 数组
    # [[19 22]
    #  [43 50]]
    print(x.dot(y))
    print(np.dot(x, y))


Numpy 提供了许多对数组执行计算的有用函数；其中最有用的是 `sum`：


    import numpy as np

    x = np.array([[1,2],[3,4]])

    print(np.sum(x))  # 计算所有元素的和；输出 "10"
    print(np.sum(x, axis=0))  # 计算每列的和；输出 "[4 6]"
    print(np.sum(x, axis=1))  # 计算每行的和；输出 "[3 7]"


你可以在[文档](http://docs.scipy.org/doc/numpy/reference/routines.math.html)中找到 numpy 提供的所有数学函数的完整列表。

除了使用数组计算数学函数外，我们经常需要改变数组的形状或以其他方式操作数组数据。这类操作的最简单例子是转置矩阵；要转置矩阵，只需使用数组对象的 `T` 属性：


    import numpy as np

    x = np.array([[1,2], [3,4]])
    print(x)    # 输出 "[[1 2]
                #          [3 4]]"
    print(x.T)  # 输出 "[[1 3]
                #          [2 4]]"

    # 注意转置秩 1 数组没有任何效果：
    v = np.array([1,2,3])
    print(v)    # 输出 "[1 2 3]"
    print(v.T)  # 输出 "[1 2 3]"


Numpy 提供了更多操作数组的函数；你可以在[文档](http://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html)中查看完整列表。

### 广播（Broadcasting）

广播是一种强大的机制，允许 numpy 在执行算术运算时处理不同形状的数组。我们经常有一个较小的数组和一个较大的数组，希望多次使用较小的数组在较大的数组上执行某些操作。

例如，假设我们要将一个常向量加到矩阵的每一行。可以这样做：


    import numpy as np

    # 我们将向量 v 加到矩阵 x 的每一行，
    # 结果存储在矩阵 y 中
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = np.empty_like(x)   # 创建与 x 形状相同的空矩阵

    # 用显式循环将向量 v 加到矩阵 x 的每一行
    for i in range(4):
        y[i, :] = x[i, :] + v

    # 现在 y 是以下矩阵
    # [[ 2  2  4]
    #  [ 5  5  7]
    #  [ 8  8 10]
    #  [11 11 13]]
    print(y)


这可行；但当矩阵 `x` 非常大时，在 Python 中计算显式循环可能很慢。注意将向量 `v` 加到矩阵 `x` 的每一行，等价于将 `v` 的多个副本垂直堆叠形成矩阵 `vv`，然后对 `x` 和 `vv` 进行逐元素求和。实现方式如下：


    import numpy as np

    # 我们将向量 v 加到矩阵 x 的每一行，
    # 结果存储在矩阵 y 中
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    vv = np.tile(v, (4, 1))   # 将 v 垂直堆叠 4 份
    print(vv)                 # 输出 "[[1 0 1]
                              #          [1 0 1]
                              #          [1 0 1]
                              #          [1 0 1]]"
    y = x + vv  # 逐元素相加 x 和 vv
    print(y)  # 输出 "[[ 2  2  4
              #          [ 5  5  7]
              #          [ 8  8 10]
              #          [11 11 13]]"


Numpy 广播允许我们在不实际创建 `v` 的多个副本的情况下执行此计算。使用广播的版本：


    import numpy as np

    # 我们将向量 v 加到矩阵 x 的每一行，
    # 结果存储在矩阵 y 中
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v  # 使用广播将 v 加到 x 的每一行
    print(y)  # 输出 "[[ 2  2  4]
              #          [ 5  5  7]
              #          [ 8  8 10]
              #          [11 11 13]]"


`y = x + v` 这行代码即使 `x` 的形状是 `(4, 3)` 而 `v` 的形状是 `(3,)` 也能工作，这归功于广播；这行代码的效果就像 `v` 的形状实际上是 `(4, 3)`，其中每一行都是 `v` 的副本，然后进行逐元素求和。

两个数组的广播遵循以下规则：

  1. 如果两个数组的秩不同，给秩较低的数组形状前面补 1，直到两个形状长度相同。
  2. 如果两个数组在某个维度上的大小相同，或者其中一个数组在该维度上的大小为 1，则称两个数组在该维度上是「兼容的」。
  3. 如果两个数组在所有维度上都兼容，则可以一起广播。
  4. 广播后，每个数组的行为就像其形状等于两个输入数组形状的逐元素最大值。
  5. 在某个维度上，如果一个数组大小为 1 而另一个数组大小大于 1，则第一个数组的行为就像在该维度上被复制了一样。

如果这个解释不够清楚，请尝试阅读[文档](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)中的解释或[这篇解释](https://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc)。

支持广播的函数称为「通用函数」（universal functions）。你可以在[文档](http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs)中找到所有通用函数的列表。

以下是一些广播的应用：


    import numpy as np

    # 计算向量的外积
    v = np.array([1,2,3])  # v 形状为 (3,)
    w = np.array([4,5])    # w 形状为 (2,)
    # 要计算外积，我们首先将 v 变形为形状为 (3, 1) 的列向量
    # 然后对 w 进行广播，得到形状为 (3, 2) 的输出，即 v 和 w 的外积：
    # [[ 4  5]
    #  [ 8 10]
    #  [12 15]]
    print(np.reshape(v, (3, 1)) * w)

    # 将向量加到矩阵的每一行
    x = np.array([[1,2,3], [4,5,6]])
    # x 形状为 (2, 3)，v 形状为 (3,)，广播到 (2, 3)，
    # 得到以下矩阵：
    # [[2 4 6]
    #  [5 7 9]]
    print(x + v)

    # 将向量加到矩阵的每一列
    # x 形状为 (2, 3)，w 形状为 (2,)
    # 如果我们转置 x，其形状变为 (3, 2)，可以与 w 广播
    # 得到形状为 (3, 2) 的结果；再转置该结果
    # 得到最终形状为 (2, 3) 的矩阵，即矩阵 x 的每一列加上了向量 w：
    # [[ 5  6  7]
    #  [ 9 10 11]]
    print((x.T + w).T)
    # 另一种方法是将 w 变形为形状为 (2, 1) 的列向量
    # 然后直接与 x 广播得到相同的结果
    print(x + np.reshape(w, (2, 1)))

    # 矩阵乘以常数：
    # x 形状为 (2, 3)。Numpy 将标量视为形状为 () 的数组
    # 可以与形状 (2, 3) 广播，产生以下数组：
    # [[ 2  4  6]
    #  [ 8 10 12]]
    print(x * 2)


广播通常使你的代码更简洁、更快，因此你应该尽量使用它。

### Numpy 文档

这个简要概述涵盖了许多你需要了解的关于 numpy 的重要内容，但远非完整。查看 [numpy 参考文档](http://docs.scipy.org/doc/numpy/reference/)了解更多。

## SciPy

Numpy 提供了高性能的多维数组和基本工具来计算和操作这些数组。[SciPy](http://docs.scipy.org/doc/scipy/reference/) 在此基础上构建，提供了大量对 numpy 数组操作的函数，对各种科学和工程应用非常有用。

熟悉 SciPy 的最佳方式是[浏览文档](http://docs.scipy.org/doc/scipy/reference/index.html)。我们将重点介绍 SciPy 中你可能在本课程中用到的部分。

### 图像操作

SciPy 提供了一些基本的图像处理函数。例如，它有从磁盘读取图像到 numpy 数组的函数、将 numpy 数组作为图像写入磁盘的函数，以及调整图像大小的函数。以下是一个展示这些函数的简单示例：


    from scipy.misc import imread, imsave, imresize

    # 读取 JPEG 图像到 numpy 数组
    img = imread('assets/cat.jpg')
    print(img.dtype, img.shape)  # 输出 "uint8 (400, 248, 3)"

    # 我们可以通过用不同的标量常数缩放每个颜色通道来给图像着色
    # 图像形状为 (400, 248, 3)
    # 我们将其乘以形状为 (3,) 的数组 [1, 0.95, 0.9]
    # numpy 广播意味着红色通道保持不变，
    # 绿色和蓝色通道分别乘以 0.95 和 0.9
    img_tinted = img * [1, 0.95, 0.9]

    # 将着色图像调整为 300x300 像素
    img_tinted = imresize(img_tinted, (300, 300))

    # 将着色图像写回磁盘
    imsave('assets/cat_tinted.jpg', img_tinted)


![](/assets/cat.jpg) ![](/assets/cat_tinted.jpg)

左图：原始图像。右图：着色并调整大小后的图像。

### MATLAB 文件

`scipy.io.loadmat` 和 `scipy.io.savemat` 函数允许你读写 MATLAB 文件。你可以在[文档](http://docs.scipy.org/doc/scipy/reference/io.html)中了解它们。

### 点之间的距离

SciPy 定义了一些用于计算点集之间距离的有用函数。

`scipy.spatial.distance.pdist` 函数计算给定集合中所有点对之间的距离：


    import numpy as np
    from scipy.spatial.distance import pdist, squareform

    # 创建以下数组，其中每行是 2D 空间中的一个点：
    # [[0 1]
    #  [1 0]
    #  [2 0]]
    x = np.array([[0, 1], [1, 0], [2, 0]])
    print(x)

    # 计算 x 所有行之间的欧几里得距离
    # d[i, j] 是 x[i, :] 和 x[j, :] 之间的欧几里得距离
    # d 是以下数组：
    # [[ 0.          1.41421356  2.23606798]
    #  [ 1.41421356  0.          1.        ]
    #  [ 2.23606798  1.          0.        ]]
    d = squareform(pdist(x, 'euclidean'))
    print(d)


你可以在[文档](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html)中阅读该函数的所有细节。

一个类似的函数 (`scipy.spatial.distance.cdist`) 计算两个点集之间所有点对的距离；你可以在[文档](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html)中了解它。

## Matplotlib

[Matplotlib](http://matplotlib.org/) 是一个绘图库。本节简要介绍 `matplotlib.pyplot` 模块，它提供了类似于 MATLAB 的绘图系统。

### 绘图

matplotlib 中最重要的函数是 `plot`，它允许你绘制 2D 数据。简单示例：


    import numpy as np
    import matplotlib.pyplot as plt

    # 计算正弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)

    # 使用 matplotlib 绘制点
    plt.plot(x, y)
    plt.show()  # 必须调用 plt.show() 才能显示图形


运行此代码将产生以下图形：

![](/assets/sine.png)

只需很少的额外工作，我们就可以同时绘制多条线，并添加标题、图例和轴标签：


    import numpy as np
    import matplotlib.pyplot as plt

    # 计算正弦和余弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 使用 matplotlib 绘制点
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()


![](/assets/sine_cosine.png)

你可以在[文档](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot)中阅读更多关于 `plot` 函数的信息。

### 子图

你可以使用 `subplot` 函数在同一图形中绘制不同的内容。示例：


    import numpy as np
    import matplotlib.pyplot as plt

    # 计算正弦和余弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 设置一个高度为 2、宽度为 1 的子图网格，
    # 并将第一个子图设置为活动状态
    plt.subplot(2, 1, 1)

    # 绘制第一个图
    plt.plot(x, y_sin)
    plt.title('Sine')

    # 将第二个子图设置为活动状态，绘制第二个图
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    # 显示图形
    plt.show()


![](/assets/sine_cosine_subplot.png)

你可以在[文档](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot)中阅读更多关于 `subplot` 函数的信息。

### 图像

你可以使用 `imshow` 函数显示图像。示例：


    import numpy as np
    from scipy.misc import imread, imresize
    import matplotlib.pyplot as plt

    img = imread('assets/cat.jpg')
    img_tinted = img * [1, 0.95, 0.9]

    # 显示原始图像
    plt.subplot(1, 2, 1)
    plt.imshow(img)

    # 显示着色图像
    plt.subplot(1, 2, 2)

    # imshow 的一个小问题：如果传入的数据不是 uint8 类型，
    # 可能会产生奇怪的结果。为了解决这个问题，
    # 我们在显示图像前显式将其转换为 uint8
    plt.imshow(np.uint8(img_tinted))
    plt.show()


![](/assets/cat_tinted_imshow.png)
