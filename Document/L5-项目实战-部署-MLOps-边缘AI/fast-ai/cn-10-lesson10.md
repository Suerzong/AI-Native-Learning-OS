[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [10：深入研究](../Lessons/lesson10.html)

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
  * 课程链接

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [10：深入研究](../Lessons/lesson10.html)

＃10：深入研究

本课程从底层组件创建完整的 Diffusers 管道：VAE、unet、调度程序和标记器。通过手动将它们组合在一起，您可以灵活地完全自定义推理过程的各个方面。

我们还讨论了上周发布的三篇重要的新论文，它们将推理性能提高了 10 倍以上，并且允许通过仅描述新图片应显示的内容来“编辑”任何照片。

在课程的后半部分，杰里米开始“从头开始”实施稳定扩散。他介绍了学生在课程中创建的“miniai”库，并讨论了组织和简化代码。本课程讨论 Python 数据模型、张量和随机数生成。 Jeremy 介绍了 Wickman-Hill 随机数生成算法，并比较了自定义随机数生成器和 Pytorch 内置随机数生成器的性能。本课程最后以使用张量创建线性分类器作为结束。

## 讨论的概念

  * 论文：
    * 用于扩散模型快速采样的渐进式蒸馏
    * 关于引导扩散模型的蒸馏
    * 意象
  * 对输入文本进行标记
  * 用于嵌入的 CLIP 编码器
  * 用于噪声确定的调度程序
  * 组织和简化代码
  * 负面提示和回调
  * Python 中的迭代器和生成器
  * 矩阵的自定义类
  * 邓德方法
  * Python数据模型
  * 张量
  * 伪随机数生成
    * Wickman-Hill算法
    * 深度学习中的随机状态
  * 使用张量的线性分类器

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-10-official-topic/101171)
  * [纸质演练视频](https://www.youtube.com/watch?v=ZXuK6IRJlnk) 作者：@johnowhitaker，涵盖_扩散模型快速采样的渐进式蒸馏_
  * [扩散-nbs回购协议](https://github.com/fastai/diffusion-nbs)（我们继续遍历`stable_diffusion.ipynb`我们上次提到过）
  * 本课程的[Fashion-MNIST 重新实现](https://mlops.systems/computervision/fastai/parttwo/2022/10/24/foundations-mnist-basics.html)，附有注释，作者：@strickvl

## 课程链接

  * [课程 2022p2 存储库](https://github.com/fastai/course22p2)
  * [用于扩散模型快速采样的渐进增量](https://arxiv.org/abs/2202.00512)
  * [意象纸](https://arxiv.org/abs/2210.09276)。几个小时内[稳定的扩散版本](https://twitter.com/Buntworthy/status/1582307817884889088?s=20&t=BAiIP4MoZXt6ptq2kp9Xug) 就出现了。
  * APL: [ 数据库编程 - fast.ai 课程论坛](https://forums.fast.ai/c/array-programming/56)

[__ 9：稳定扩散](../Lessons/lesson9.html)

[11: 矩阵乘法__](../Lessons/lesson11.html)
