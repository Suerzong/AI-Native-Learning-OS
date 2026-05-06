[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [14：逆向传播](../Lessons/lesson14.html)

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

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [14：逆向传播](../Lessons/lesson14.html)

#14：反向传播

在本课中，我们将深入探讨使用反向传播在神经网络训练中实现链式法则。我们重构代码，使其更加高效和灵活，并探索 PyTorch 的`nn.Module`和`nn.Sequential`。我们还创建自定义 PyTorch 模块，构建我们自己的实现`nn.Module`，并了解优化器、数据加载器和数据集。我们展示了如何使用 Hugging Face 数据集，并介绍 nbdev 库。

我们看看如何将上一课的代码映射到反向传播背后的数学。接下来，我们使用 PyTorch 重构我们的代码`nn.Module`，自动跟踪图层和参数。我们还使用创建一个顺序模型`nn.Sequential`并演示如何创建自定义 PyTorch 模块。然后我们引入优化器的概念，它简化了基于梯度和学习率更新参数的过程。我们从头开始创建一个自定义 SGD 优化器，并探索 PyTorch 的内置 DataLoader。我们还使用 PyTorch DataLoader 创建适当的训练循环。

在整个课程中，我们强调理解底层代码而不是仅仅依赖其他人的代码的重要性。这使得在构建定制解决方案时具有更大的灵活性和创造力。我们还讨论了使用`**kwargs`以及 Python 数据模型中 fastcore、回调和 dunder 方法中的委托。

## 讨论的概念

  * 反向传播和链式法则
  * 重构代码以提高效率和灵活性
  * PyTorch 的`nn.Module`和`nn.Sequential`
  * 创建自定义 PyTorch 模块
  * 实现优化器、数据加载器和数据集
  * 使用拥抱面部数据集
  * 使用 nbdev 从 Jupyter Notebook 创建 Python 模块
  * `**kwargs` and delegates
  * Python数据模型中的回调和dunder方法
  * 使用 PyTorch DataLoader 构建适当的训练循环

＃＃ 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-14-official-topic/102018)

[__ 13：逆向传播和MLP](../Lessons/lesson13.html)

[15：自动编码器__](../Lessons/lesson15.html)
