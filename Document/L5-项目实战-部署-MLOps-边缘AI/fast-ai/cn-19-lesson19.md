[编码员实用深度学习](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [19：DDPM和辍学](../Lessons/lesson19.html)

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
  2. [19: DDPM 和辍学](../Lessons/lesson19.html)

#19：DDPM 和 Dropout

在本课程中，Jeremy 介绍了 Dropout，一种提高模型性能的技术，并与特邀嘉宾 Tanishq 和 Johno 讨论了去噪扩散概率模型 (DDPM)，这是扩散模型的基础方法。本课程涵盖 DDPM 中涉及的正向和反向过程，以及使用神经网络实现噪声预测模型。该团队还展示了另一种实施方法，并讨论了提高训练速度的方法。

## 讨论的概念

  * 用于提高模型性能的 Dropout 技术
  * 用于测量模型置信度的测试时间 dropout 回调
  * 用于生成建模的去噪扩散概率模型 (DDPM)
  * DDPM中的正向和反向过程
  * 使用神经网络实现噪声预测模型
  * DDPM中的训练循环和损失函数计算
  * 可视化不同时间步长的噪声图像
  * 用于改进 DDPM 性能的替代噪声表
  * 继承Callback和UNet2DModel作为替代实现
  * 尝试初始化技术和优化器
  * 引入混合精度以加快训练速度

＃＃ 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-19-official-topic/103201)

[__ 18：加速SGD和ResNet](../Lessons/lesson18.html)

[20：混合精度__](../Lessons/lesson20.html)
