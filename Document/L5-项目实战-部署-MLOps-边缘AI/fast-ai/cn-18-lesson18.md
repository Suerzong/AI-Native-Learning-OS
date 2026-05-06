[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [18：加速SGD和ResNet](../Lessons/lesson18.html)

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

    * [ The book](../Resources/book.html)

    * [论坛](../Resources/forums.html)

    * [卡格尔](../Resources/kaggle.html)

    * [感言](../Resources/testimonials.html)

## 在此页面上

  * Concepts discussed
  * 视频
  * Lesson resources

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [18：加速 SGD 和 ResNets](../Lessons/lesson18.html)

#18：加速 SGD 和 ResNet

在本课程中，我们将深入探讨各种随机梯度下降 (SGD) 加速方法，例如动量、RMSProp 和 Adam。我们首先在 Microsoft Excel 中试验这些技术，创建一个简单的线性回归问题并应用不同的方法来解决它。我们还介绍了学习率退火并展示了如何在 Excel 中实现它。接下来，我们探索 PyTorch 中的学习率调度程序，重点关注余弦退火以及如何使用 PyTorch 优化器。我们创建一个具有单批回调的学习器，并拟合模型以获得优化器。然后我们探讨优化器的属性并解释参数组的概念。

我们继续实施 PyTorch 的 OneCycleLR 调度程序，该调度程序在训练期间调整学习率和动量。我们还讨论了如何通过使其更深、更宽来改进神经网络的架构，引入 ResNet 和残差连接的概念。最后，我们探索 PyTorch 图像模型 (timm) 库中的各种 ResNet 架构，并尝试数据增强技术，例如随机擦除和测试时间增强。

## 讨论的概念

  * 随机梯度下降（SGD）加速方法
    * Momentum
    * RMSProp
    * Adam
  * Learning rate annealing
  * PyTorch learning rate schedulers 
    * 余弦退火
    * OneCycleLR
  * Working with PyTorch optimizers
  * 神经网络架构改进
    * 更深更广的网络
    * ResNets
    * 剩余连接
  * 数据增强技术
    * Random erasing
    * Test time augmentation
  * Creating custom schedulers and experimenting with model performance

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-18-official-topic/102750)
  * 课程的[时尚mist挑战](https://forums.fast.ai/t/a-challenge-for-you-all/102656)主题
  * Excel [优化器电子表格](https://github.com/fastai/course22p2/blob/master/xl/graddesc.xlsm)
  * Papers 
    * [训练神经网络的循环学习率](https://arxiv.org/abs/1506.01186)
    * [修复初始化：没有归一化的残差学习](https://arxiv.org/abs/1901.09321)
    * [用于图像识别的残差学习](https://arxiv.org/abs/1512.03385)
  * Fashion-MNIST Benchmark [带有代码的论文](https://paperswithcode.com/sota/image-classification-on-fashion-mnist)

[__ 17：初始化/标准化](../Lessons/lesson17.html)

[19: DDPM 和辍学 __](../Lessons/lesson19.html)
