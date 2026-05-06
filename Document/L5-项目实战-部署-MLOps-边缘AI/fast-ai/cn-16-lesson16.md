[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [16：学习者框架](../Lessons/lesson16.html)

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
  2. [16：学习者框架](../Lessons/lesson16.html)

#16：学习者框架

在第 16 课中，我们将深入构建一个称为学习器的灵活培训框架。我们从基本的回调学习器开始，这是迈向灵活学习器的中间步骤。我们介绍回调，它们是在训练过程中的特定点调用的函数或类，并演示了简单回调的创建。我们还介绍了 CancelFitException、CancelEpochException 和 CancelBatchException 的概念。

接下来，我们探索指标并创建 MetricsCB 回调以在训练期间打印出指标。我们引入 torcheval 库并创建一个 DeviceCB 回调来处理将模型和数据移动到适当的设备。我们使用上下文管理器重构代码，以简化代码并使将来更容易维护和添加回调。

然后，我们专注于研究模型内部，以诊断和修复训练期间的问题。我们引入set_seed函数并训练一个具有0.6的高学习率的模型来测试训练的稳定性。最后，我们讨论通过查看每层激活的平均值和标准差、使用 PyTorch 挂钩并创建激活的直方图来分析训练过程。

## 讨论的概念

  * 建立灵活的培训框架
  * 基本回调学习者
  * 回调和异常（CancelFitException、CancelEpochException、CancelBatchException）
  * Metrics和MetricsCB回调
  * 火炬图书馆
  * 设备CB回调
  * 使用上下文管理器重构代码
  * 设置种子函数
  * 分析训练过程
  * PyTorch 钩子
  * 激活的直方图

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-16-official-topic/102472)
  * [训练神经网络的循环学习率 - Leslie Smith](https://arxiv.org/abs/1506.01186)
  * [神经网络超参数的规范方法：第1部分 - 学习率、批量大小、动量和权重衰减 - Leslie Smith](https://arxiv.org/abs/1803.09820)
  * [自动学习率查找器的方法 - Zach Mueller](https://www.novetta.com/2021/03/learning-rate/)

[__ 15：自动编码器](../Lessons/lesson15.html)

[17:初始化/标准化__](../Lessons/lesson17.html)
