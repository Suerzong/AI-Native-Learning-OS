[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [12：均值路易](../Lessons/lesson12.html)

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
  2. [12：均值路易](../Lessons/lesson12.html)

# 12：均值漂移聚类

在本课程中，我们首先讨论 CLIP Interrogator，这是一款 Hugging Face Spaces Gradio 应用程序，可生成用于创建 CLIP 嵌入的文本提示。然后，我们回到矩阵乘法，使用爱因斯坦求和符号和 torch.einsum 来简化代码并提高性能。我们探索使用 CUDA 和 Numba 的 GPU 加速，演示如何编写矩阵乘法的内核函数并在 GPU 上启动它。

接下来，我们通过实现均值漂移聚类（一种用于识别数据集中的聚类的技术）来锻炼我们的张量编程技能。我们创建合成数据，解释均值平移算法，并引入高斯核来惩罚远处的点。我们使用 PyTorch 实现均值平移聚类算法，并讨论张量操作操作对于高效 GPU 编程的重要性。

最后，我们使用 PyTorch 和 GPU 优化均值平移算法，演示如何计算权重、矩阵相乘以及对点求和以获得新的数据点。我们探讨了改变批量大小对性能的影响，并鼓励观众研究其他聚类算法。

The lesson concludes with an introduction to calculus, focusing on derivatives and the calculus of infinitesimals.

## 讨论的概念

  * CLIP询问器
  * 逆问题
  * 矩阵乘法
  * 爱因斯坦求和符号和torch.einsum
  * GPU加速和CUDA
  * 努巴
  * 均值漂移聚类
  * 高斯核
  * 规范
  * 欧氏距离
  * 微积分
    * 导数和无穷小数

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-12-official-topic/101702)
  * [CLIP询问器](https://huggingface.co/spaces/pharma/CLIP-Interrogator)
  * [微积分的本质](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3blue1brown)

[__ 11：矩阵乘法](../Lessons/lesson11.html)

[13：逆向传播和MLP__](../Lessons/lesson13.html)
