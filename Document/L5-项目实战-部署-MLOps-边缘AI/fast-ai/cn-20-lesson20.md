[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [20：混合精度](../Lessons/lesson20.html)

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
  2. [20：混合精度](../Lessons/lesson20.html)

#20：混合精度

在本课程中，我们将深入研究混合精度训练并尝试各种技术。我们引入了 PyTorch 的 MixedPrecision 回调，并探索 HuggingFace 的 Accelerate 库来加速训练循环。我们还学习了一个更快的数据加载和增强的技巧。

然后，Johno 讨论了使用神经网络进行风格迁移、从预训练网络的不同层中提取特征，并介绍了内容损失和 Gram 矩阵。他演示了如何结合内容损失和风格损失来执行风格迁移，从而实现广泛的实验和艺术效果。

最后，约翰受到康威生命游戏和自然界中发现的自组织系统的启发，探索了神经细胞自动机。他使用硬编码滤波器和具有密集线性层和卷积层的神经网络来实现细胞自动机。他使用风格损失和溢出损失来训练模型，并尝试使用不同的模型大小和损失函数以获得更复杂和更具创造性的结果。

## 讨论的概念

  * 混合精准训练
  * 从 HuggingFace 加速库
  * 校对功能
  * 更快的数据加载
  * 预训练的神经网络
  * 风格转移
  * Content loss
  * 克矩阵
  * 神经细胞自动机
  * 圆形填充
  * 梯度归一化

＃＃ 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-20-official-topic/103322)

[__ 19：DDPM 和辍学](../Lessons/lesson19.html)

[21：DDIM__](../Lessons/lesson21.html)
