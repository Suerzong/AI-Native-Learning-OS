[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [15：自动编码器](../Lessons/lesson15.html)

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
  2. [15：自动编码器](../Lessons/lesson15.html)

#15：自动编码器

我们首先深入研究卷积自动编码器并探索卷积的概念。卷积有助于神经网络理解问题的结构，使其更容易解决。我们学习如何使用内核将卷积应用于图像，并讨论 im2col、padding 和 stride 等技术。我们还使用序列模型从头开始创建 CNN，并在 GPU 上对其进行训练。

然后，我们尝试构建一个自动编码器，但面临速度和准确性问题。为了解决这些问题，我们引入了一个概念`Learner`，这样可以更快地进行实验并更好地了解模型的性能。我们创建一个简单的`Learner`并演示其在多层感知器 (MLP) 模型中的使用。

最后，我们讨论了理解 Python 概念（例如 try- except 块、装饰器、getattr 和调试）的重要性，以减少学习正在构建的框架时的认知负担。

## 讨论的概念

  * 卷积自动编码器
  * 卷积和核
  * Im2col 技术
  * CNN 中的填充和跨步
  * 感受野
  * 从头开始​​构建 CNN
  * 创建学习器以加快实验速度
  * Python 概念：try- except 块、装饰器、getattr 和调试
  * 学习中的认知负荷理论

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-15-official-topic/102322)
  * [Excel簿工作](https://github.com/fastai/course22/tree/master/xl)

[__ 14：逆向传播](../Lessons/lesson14.html)

[16：学习者框架__](../Lessons/lesson16.html)
