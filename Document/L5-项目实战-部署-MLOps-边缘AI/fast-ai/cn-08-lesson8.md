[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第 1 部分](../Lessons/lesson1.html)
  2. [8：心血管（CNN）](../Lessons/lesson8.html)

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

    * [ 19：DDPM 和辍学](../Lessons/lesson19.html)

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

  * 视频
  * 资源

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第 1 部分](../Lessons/lesson1.html)
  2. [8：心血管（CNN）](../Lessons/lesson8.html)

# 8：卷积（CNN）

今天，我们通过仔细研究“嵌入”（许多深度学习算法的关键构建块）来完成对协同过滤的研究。然后我们将深入研究_卷积神经网络_（CNN）并了解它们的实际工作原理。我们在本课程中使用了大量的 CNN，但我们还没有深入了解它们内部到底发生了什么。除了了解它们最基本的构建块_卷积_之外，我们还将了解池化、dropout 等。

＃＃ 视频

本课程部分基于[书](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527)的[第13章](https://github.com/fastai/fastbook/blob/master/13_volvings.ipynb)。

＃＃ 资源

  * 本课笔记本
    * [良好过滤深入研究](https://www.kaggle.com/code/jhoward/collaborative-filtering-deep-dive/notebook)
  * 本课的[电子表格](https://github.com/fastai/course22/tree/master/xl)
    * [良好的过滤和嵌入](https://github.com/fastai/course22/blob/master/xl/collab_filter.xlsx)
    * [Formai](https://github.com/fastai/course22/blob/master/xl/conv-example.xlsx)
  * 本课程的其他资源
    * 请将您希望 Jeremy 回答的任何问题添加到 [阿玛线程](https://forums.fast.ai/t/jeremy-ama/97238) – 并为您感兴趣的任何问题投票
    *特别额外：【数据伦理】(https://www.youtube.com/krIVOb23EH8)课程
  * [解决方案](https://forums.fast.ai/t/fastbook-chapter-8-questionnaire-solutions-wiki/69926)到书中第8章调查问卷

[__7：良好过滤](../Lessons/lesson7.html)

[奖励：数据道德__](../Lessons/lesson8a.html)
