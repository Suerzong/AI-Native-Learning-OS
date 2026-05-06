# 前置要求与预习

- Google 的机器学习速成课程为不同机器学习水平的学习者提供灵活的学习体验，包括初学者、希望复习的学习者和有经验的从业者。
- 课程需要预习，例如熟悉 Python、NumPy 和 pandas，并要求具备代数、线性代数、统计学基础，可选地还需要微积分知识，以便充分理解课程概念。
- 课程在聚焦核心 ML 概念的同时，使用 NumPy、pandas 和 Keras 等库进行实践编程练习，但不深入讲解具体的 ML API。
- 鼓励学习者完成预习内容，包括机器学习入门课程以及 NumPy 和 pandas 的教程，以确保做好准备。
- 课程使用 Colaboratory 平台，提供基于浏览器的编程练习，无需任何环境配置，建议在 Chrome 或 Firefox 桌面浏览器上体验。

### 机器学习速成课程适合你吗？

**我几乎没有机器学习背景。**

建议按顺序学习所有内容。

[开始学习](</machine-learning/crash-course/linear-regression>)

**我有一些机器学习背景，但希望获得更全面和最新的理解。**

机器学习速成课程将是很好的复习材料。可以按顺序学习所有模块，也可以只选择感兴趣的模块。

[开始学习](</machine-learning/crash-course/linear-regression>)

**我有将机器学习概念应用于数据处理和模型构建的实践经验。**

虽然机器学习速成课程可以作为基础机器学习概念的复习材料，但你可能还想探索我们的一些高级机器学习课程，这些课程涵盖了在各个领域解决机器学习问题的工具和技术。

[开始学习](</machine-learning/advanced-courses>)

**我在寻找如何使用 Keras 等 ML API 的教程。**

虽然机器学习速成课程包含多个使用 NumPy、pandas 和 Keras 等 ML 库的编程练习，但它主要侧重于教授 ML 概念，不会深入讲解 ML API。如需更多 Keras 资源，请参阅 [Keras 开发者指南](<https://keras.io/guides/>)。

请在开始机器学习速成课程之前阅读以下预习和前置要求部分，以确保你已准备好完成所有模块。

## 预习

在开始机器学习速成课程之前，请完成以下内容：

1. 如果你是机器学习新手，请学习[机器学习简介](</machine-learning/intro-to-ml>)。这个简短的自学课程介绍了基本的机器学习概念。
2. 如果你不熟悉 [NumPy](<https://numpy.org>)，请完成 [NumPy 超快速教程](<https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en>) Colab 练习，它提供了本课程所需的全部 NumPy 信息。
3. 如果你不熟悉 [pandas](<https://pandas.pydata.org/>)，请完成 [pandas 超快速教程](<https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en>) Colab 练习，它提供了本课程所需的全部 pandas 信息。

编程练习使用 [Colaboratory](<https://colab.research.google.com>) 平台直接在浏览器中运行（无需任何环境配置！）。Colaboratory 支持大多数主流浏览器，在 Chrome 和 Firefox 桌面版上经过了最充分的测试。

## 前置要求

机器学习速成课程不要求具备任何机器学习的先验知识。但是，为了理解课程内容并完成练习，建议学习者满足以下前置要求：

- 你必须熟悉变量、线性方程、函数图像、直方图和统计均值。
- 你应具备良好的编程能力。理想情况下，你应有一定的 [Python](<https://www.python.org/>) 编程经验，因为编程练习使用 Python。不过，有经验的非 Python 程序员通常也能完成编程练习。

以下部分提供了有帮助的额外背景资料链接。

### 代数

- [变量](<https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:intro-variables/v/what-is-a-variable>)、[系数](<https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-equivalent-exp/cc-6th-parts-of-expressions/v/expression-terms-factors-and-coefficients>) 和 [函数](<https://www.khanacademy.org/math/algebra-home/alg-functions>)
- [线性方程](<https://wikipedia.org/wiki/Linear_equation>)，如 \\(y = b + w_1x_1 + w_2x_2\\)
- [对数](<https://wikipedia.org/wiki/Logarithm>) 和对数方程，如 \\(y = ln(1+ e^z)\\)
- [Sigmoid 函数](<https://wikipedia.org/wiki/Sigmoid_function>)

### 线性代数

- [张量（Tensor）和张量阶数](<https://www.tensorflow.org/guide/tensor>)
- [矩阵乘法](<https://wikipedia.org/wiki/Matrix_multiplication>)

### 三角函数

- [tanh](<https://reference.wolfram.com/language/ref/Tanh.html>)（作为[激活函数](<https://developers.google.com/machine-learning/glossary#activation-function>)讨论；无需先验知识）

### 统计学

- [均值、中位数、异常值](<https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-center-distributions/v/mean-median-and-mode>) 和 [标准差](<https://wikipedia.org/wiki/Standard_deviation>)
- 能够阅读[直方图](<https://wikipedia.org/wiki/Histogram>)

### 微积分（_可选，用于高级主题_）

- [导数](<https://wikipedia.org/wiki/Derivative>)的概念（你不需要实际计算导数）
- [梯度](<https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/gradient>) 或斜率
- [偏导数](<https://wikipedia.org/wiki/Partial_derivative>)（与梯度密切相关）
- [链式法则](<https://wikipedia.org/wiki/Chain_rule>)（用于充分理解训练神经网络的[反向传播算法](<https://developers.google.com/machine-learning/crash-course/backprop-scroll/>)）

### Python 编程

以下 Python 基础知识在 [Python 教程](<https://docs.python.org/3/tutorial/>) 中有涵盖：

- [定义和调用函数](<https://docs.python.org/3/tutorial/controlflow.html#defining-functions>)，使用位置参数和[关键字参数](<https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments>)
- [字典](<https://docs.python.org/3/tutorial/datastructures.html#dictionaries>)、[列表](<https://docs.python.org/3/tutorial/introduction.html#lists>)、[集合](<https://docs.python.org/3/tutorial/datastructures.html#sets>)（创建、访问和遍历）
- [`for` 循环](<https://docs.python.org/3/tutorial/controlflow.html#for-statements>)、带多个迭代变量的 `for` 循环（例如 `for a, b in [(1,2), (3,4)]`）
- [`if/else` 条件块](<https://docs.python.org/3/tutorial/controlflow.html#if-statements>) 和[条件表达式](<https://docs.python.org/2.5/whatsnew/pep-308.html>)
- [字符串格式化](<https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting>)（例如 `'%.2f' % 3.14`）
- 变量、赋值、[基本数据类型](<https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator>)（`int`、`float`、`bool`、`str`）

部分编程练习使用以下更高级的 Python 概念：

- [列表推导式](<https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>)

### Bash 终端和云端控制台

要在本地机器或云端控制台上运行编程练习，你应该熟悉命令行操作：

- [Bash 参考手册](<https://tiswww.case.edu/php/chet/bash/bashref.html>)
- [Bash 速查表](<https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh>)
- [Learn Shell](<http://www.learnshell.org/>)

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  练习  ](</machine-learning/crash-course/exercises>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
