[ 给程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [Part 2](../Lessons/part2.html)
  2. [24: 注意力与 Transformer](../Lessons/lesson24.html)

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

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [24: 注意力与 Transformer](../Lessons/lesson24.html)

# 24: 注意力与 Transformer

在本课中，我们完成了对无条件 stable diffusion 模型的探索。然后我们实现了无条件模型，在 Fashion MNIST 上进行训练，并讨论了时间嵌入（time embedding）的重要性。我们还在 stable diffusion 的背景下深入研究了正弦和余弦嵌入（sine/cosine embeddings）、注意力机制（attention mechanism）、自注意力（self-attention）和多头注意力（multi-headed attention）。我们讨论了 `rearrange` 函数、Transformer 及其在视觉任务中的潜在用途。最后，我们通过向 UNet 模型的输入添加标签来创建条件模型，使其能够生成特定类别的图像。

## 讨论的概念

  * 实现无条件 stable diffusion 模型
  * 时间嵌入与正弦/余弦嵌入
  * 自注意力与多头注意力
  * Rearrange 函数
  * Transformer
  * 创建条件 stable diffusion 模型

## 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-24-official-topic/104358)

[ __ 23: 超分辨率 ](../Lessons/lesson23.html)

[ 25: 潜在扩散 __ ](../Lessons/lesson25.html)
