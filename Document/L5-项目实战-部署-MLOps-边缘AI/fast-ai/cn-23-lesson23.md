[ 给程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [Part 2](../Lessons/part2.html)
  2. [23: 超分辨率](../Lessons/lesson23.html)

  * [ 实用深度学习 ](../index.html)

  * Part 1 __

    * [ 1: 入门 ](../Lessons/lesson1.html)

    * [ 2: 部署 ](../Lessons/lesson2.html)

    * [ 3: 神经网络基础 ](../Lessons/lesson3.html)

    * [ 4: 自然语言处理（NLP）](../Lessons/lesson4.html)

    * [ 5: 从零构建模型 ](../Lessons/lesson5.html)

    * [ 6: 随机森林 ](../Lessons/lesson6.html)

    * [ 7: 协同过滤 ](../Lessons/lesson7.html)

    * [ 8: 卷积（CNN）](../Lessons/lesson8.html)

    * [ 附加: 数据伦理 ](../Lessons/lesson8a.html)

    * 课程小结 __

      * [ 第 1 课 ](../Lessons/Summaries/lesson1.html)

      * [ 第 2 课 ](../Lessons/Summaries/lesson2.html)

      * [ 第 3 课 ](../Lessons/Summaries/lesson3.html)

      * [ 第 4 课 ](../Lessons/Summaries/lesson4.html)

      * [ 第 5 课 ](../Lessons/Summaries/lesson5.html)

      * [ 第 6 课 ](../Lessons/Summaries/lesson6.html)

      * [ 第 7 课 ](../Lessons/Summaries/lesson7.html)

      * [ 第 8 课 ](../Lessons/Summaries/lesson8.html)

  * Part 2 __

    * [ Part 2 概览 ](../Lessons/part2.html)

    * [ 9: Stable Diffusion ](../Lessons/lesson9.html)

    * [ 10: 深入探索 ](../Lessons/lesson10.html)

    * [ 11: 矩阵乘法 ](../Lessons/lesson11.html)

    * [ 12: 均值漂移聚类 ](../Lessons/lesson12.html)

    * [ 13: 反向传播与 MLP ](../Lessons/lesson13.html)

    * [ 14: 反向传播 ](../Lessons/lesson14.html)

    * [ 15: 自编码器 ](../Lessons/lesson15.html)

    * [ 16: Learner 框架 ](../Lessons/lesson16.html)

    * [ 17: 初始化与归一化 ](../Lessons/lesson17.html)

    * [ 18: 加速 SGD 与 ResNet ](../Lessons/lesson18.html)

    * [ 19: DDPM 与 Dropout ](../Lessons/lesson19.html)

    * [ 20: 混合精度 ](../Lessons/lesson20.html)

    * [ 21: DDIM ](../Lessons/lesson21.html)

    * [ 22: Karras 等人（2022）](../Lessons/lesson22.html)

    * [ 23: 超分辨率 ](../Lessons/lesson23.html)

    * [ 24: 注意力与 Transformer ](../Lessons/lesson24.html)

    * [ 25: 潜在扩散 ](../Lessons/lesson25.html)

    * [ 附加: 第 9a 课 ](https://youtu.be/0_BBRNYInx8)

    * [ 附加: 第 9b 课 ](https://youtu.be/mYpjmM7O-30)

  * 资源 __

    * [ 书籍 ](../Resources/book.html)

    * [ 论坛 ](../Resources/forums.html)

    * [ Kaggle ](../Resources/kaggle.html)

    * [ 用户评价 ](../Resources/testimonials.html)

## 本页内容

  * 讨论的概念
  * 视频
  * 课程资源

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [23: 超分辨率](../Lessons/lesson23.html)

# 23: 超分辨率（Super-resolution）

在本课中，我们使用 Tiny Imagenet 数据集创建了一个超分辨率 U-Net 模型，讨论了数据集创建、预处理和数据增强。超分辨率的目标是将低分辨率图像放大到更高分辨率。我们使用 AdamW 优化器和混合精度训练模型，达到了近 60% 的准确率。我们还通过 Papers with Code 网站查看了其他模型在 Tiny Imagenet 上的结果，探索了改进的可能性。

我们讨论了使用卷积神经网络进行图像超分辨率的局限性，并引入了 U-net 的概念，这是一种更适合此任务的架构。我们实现了感知损失（perceptual loss），即在预训练分类器模型的中间层比较输出图像和目标图像的特征。使用新的损失函数训练 U-net 模型后，输出图像更清晰，与目标图像更加相似。

最后，我们讨论了比较不同模型及其输出的挑战。我们展示了感知损失如何显著改善了结果，但也指出目前没有一个明确的度量标准来进行比较。然后我们转向逐步解冻预训练网络，这是 fast.ai 最喜爱的技巧之一。我们将预训练模型的权重复制到我们的模型中，并冻结下采样路径的权重训练一个 epoch。这导致了损失的显著降低。

## 讨论的概念

  * Tiny Imagenet 数据集
  * 创建超分辨率 U-Net 模型
  * 数据预处理与增强
  * 感知损失（perceptual loss）
  * 逐步解冻预训练网络
  * 在 U-net 中尝试交叉连接

## 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-23-official-topic/103965)
  * [TrivialAugment: 无需调参的先进数据增强](https://arxiv.org/pdf/2103.10158.pdf)
  * [深度残差网络中的恒等映射](https://arxiv.org/abs/1603.05027)

[ __ 22: Karras 等人（2022） ](../Lessons/lesson22.html)

[ 24: 注意力与 Transformer __ ](../Lessons/lesson24.html)
