[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [17：初始化/标准化](../Lessons/lesson17.html)

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
  * 课程论文

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [17：初始化/标准化](../Lessons/lesson17.html)

# 17：初始化/标准化

在本课程中，我们讨论神经网络中权重初始化的重要性，并探索改进训练的各种技术。我们首先介绍对 miniai 库的更改，并演示如何使用 HooksCallback 和 ActivationStats 来实现更好的可视化。然后，我们深入探讨神经网络中零均值和单位标准差的重要性，并介绍 Glorot (Xavier) 初始化。

我们还介绍了方差、标准差和协方差，以及它们在理解数据点之间关系方面的重要性。我们创建了一种新颖的广义 ReLU 激活函数，并讨论了用于初始化任何神经网络的逐层序列单元方差 (LSUV) 技术。我们探索归一化技术，例如层归一化和批量归一化，并简要提及其他归一化方法，例如实例归一化和组归一化。

最后，我们尝试使用不同的批量大小、学习率和 Accelerated SGD、RMSProp 和 Adam 等优化器来提高性能。

## 讨论的概念

  * Callback class and TrainLearner subclass
  * HooksCallback 和 ActivationStats
  * Glorot（Xavier）初始化
  * 方差、标准差和协方差
  * 通用ReLU激活函数
  * 逐层序列单位方差 (LSUV)
  * 层归一化和批量归一化
  * 实例范数和组范数
  * 加速 SGD、RMSProp 和 Adam 优化器
  * 试验批量大小和学习率

＃＃ 视频

## 课程论文

  * [讨论本课](https://forums.fast.ai/t/lesson-17-official-topic/102602)
  * [了解训练深度前馈神经网络的难度 - Xavier Glorot、Yoshua Bengio](http://proceedings.mlr.press/v9/glorot10a)
  * [深入研究修正器：在ImageNet分类上超越人类水平的表现 - Kaiming He 等人](https://arxiv.org/abs/1502.01852)
  * [LSUV - 您所需要的只是一个好的初始化 - Dmytro Mishkin、Jiri Matas](https://arxiv.org/abs/1511.06422)
  * [批量归一化：通过减少内部协变量偏移加速深度网络训练 - Sergey Ioffe、Christian Szegedy](https://arxiv.org/abs/1502.03167)
  * [层归一化 - Ba、Kiros、Hinton](https://arxiv.org/abs/1607.06450)

[__ 16：学习者框架](../Lessons/lesson16.html)

[18：加速SGD和ResNets__](../Lessons/lesson18.html)
