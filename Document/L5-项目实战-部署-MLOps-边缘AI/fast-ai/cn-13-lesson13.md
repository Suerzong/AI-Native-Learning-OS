[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [13：逆向传播和MLP](../Lessons/lesson13.html)

  * [实用深度学习](../index.html)

  * 第 1 部分 __

    * [1：入门](../Lessons/lesson1.html)

    * [2：部署](../Lessons/lesson2.html)

    * [3：神经网络基础](../Lessons/lesson3.html)

    * [4：自然语言（NLP）](../Lessons/lesson4.html)

    * [5：从头开始模型](../Lessons/lesson5.html)

    * [6：随机森林](../Lessons/lesson6.html)

    * [7：良好过滤](../Lessons/lesson7.html)

    * [8：心血管（CNN）](../Lessons/lesson8.html)

    * [奖励：道德数据](../Lessons/lesson8a.html)

    * 摘要__

      * [第 1 课](../Lessons/Summaries/lesson1.html)

      * [第2课](../Lessons/Summaries/lesson2.html)

      * [第三课](../Lessons/Summaries/lesson3.html)

      * [第 4 课](../Lessons/Summaries/lesson4.html)

      * [第五课](../Lessons/Summaries/lesson5.html)

      * [第 6 课](../Lessons/Summaries/lesson6.html)

      * [第7课](../Lessons/Summaries/lesson7.html)

      * [第8课](../Lessons/Summaries/lesson8.html)

  * 第 2 部分 __

    * [第 2 部分概述](../Lessons/part2.html)

    * [9：稳定的扩散](../Lessons/lesson9.html)

    * [10：深入研究](../Lessons/lesson10.html)

    * [11：矩阵乘法](../Lessons/lesson11.html)

    * [12：均值可靠性](../Lessons/lesson12.html)

    * [13：逆向传播和MLP](../Lessons/lesson13.html)

    * [14：逆向传播](../Lessons/lesson14.html)

    * [15：自动编码器](../Lessons/lesson15.html)

    * [16：学习者框架](../Lessons/lesson16.html)

    * [17：初始化/标准化](../Lessons/lesson17.html)

    * [18：加速SGD和ResNet](../Lessons/lesson18.html)

    * [19: DDPM 和休学](../Lessons/lesson19.html)

    * [20：混合精度](../Lessons/lesson20.html)

    * [21：DDIM](../Lessons/lesson21.html)

    * [22：卡拉斯等人 (2022)](../Lessons/lesson22.html)

    * [23：超分辨率](../Lessons/lesson23.html)

    * [24：注意力和变形金刚](../Lessons/lesson24.html)

    * [25: 潜在扩散](../Lessons/lesson25.html)

    * [奖励：第9a课](https://youtu.be/0_BBRNYInx8)

    * [奖励：第 9b 课](https://youtu.be/mYpjmM7O-30)

  * 资源 __

    * [本书](../Resources/book.html)

    * [论坛](../Resources/forums.html)

    * [卡格尔](../Resources/kaggle.html)

    * [感言](../Resources/testimonials.html)

## 在此页面上

  * 讨论的概念
  * 视频
  * 课程资源

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [13：逆向传播和MLP](../Lessons/lesson13.html)

# 13：反向传播和 MLP

在本课程中，我们将深入研究反向传播和简单的多层感知器 (MLP) 神经网络的创建。我们首先回顾基本的神经网络及其架构，然后继续从头开始实现一个简单的 MLP。我们重点了解神经网络背景下的链式法则和反向传播，并演示如何使用 Python 和 SimPy 库计算导数。

我们还讨论了链式法则在计算应用于模型的均方误差 (MSE) 梯度时的重要性，并演示了如何使用 PyTorch 计算导数并通过为 ReLU 和线性函数创建类来简化过程。然后，我们探讨浮点数学的问题，并引入对数和指数技巧来克服这些问题。最后，我们为简单的神经网络创建一个训练循环。

## 讨论的概念

  * 基本神经网络架构
  * 多层感知器（MLP）实现
  * 梯度和导数
  * 链式法则和反向传播
  * Python 调试器 (pdb)
  * PyTorch 用于计算导数
  * ReLU和线性函数类
  * 对数和指数技巧
  * `log_softmax()` function and cross entropy loss
  * 简单神经网络的训练循环

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-13-official-topic/101876)
  * [链式法则的观察概念](https://webspace.ship.edu/msrenault/geogebracalculus/derivative_intuitive_chain_rule.html)
  * [深度学习所需的矩阵微积分](https://explained.ai/matrix-calculus/)
  * [第1部分Excel工作簿](https://github.com/fastai/course22/tree/master/xl)
  * [微积分帮助主题](https://forums.fast.ai/t/calculus-help-topic/102020)
  * [简单神经网络后向传递](https://nasheqlbrm.github.io/blog/posts/2021-11-13-backward-pass.html)

[__ 12：均值路易](../Lessons/lesson12.html)

[14：逆向传播__](../Lessons/lesson14.html)
