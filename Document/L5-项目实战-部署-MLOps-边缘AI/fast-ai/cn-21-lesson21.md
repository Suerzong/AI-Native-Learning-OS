[ 给程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [Part 2](../Lessons/part2.html)
  2. [21: DDIM](../Lessons/lesson21.html)

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
  2. [21: DDIM](../Lessons/lesson21.html)

# 21: DDIM（去噪扩散隐式模型）

在本课中，Jeremy、Johno 和 Tanishq 讨论了他们在 Fashion-MNIST 数据集和 CIFAR-10 数据集上的实验。CIFAR-10 是图像分类和生成建模中常用的经典数据集。他们引入了 Weights and Biases（W&B），这是一个实验跟踪和日志记录工具，可以帮助管理和可视化实验进度。课程介绍了 Fréchet Inception Distance（FID，弗雷歇起始距离）指标来衡量生成图像的质量，Jeremy 演示了如何使用自定义的 Fashion-MNIST 模型计算 FID。课程还涵盖了用于比较图像分布的 FID 和 Kernel Inception Distance（KID，核起始距离）指标。

Jeremy 探索了在不牺牲质量的前提下加速模型的方法。Denoising Diffusion Implicit Model（DDIM，去噪扩散隐式模型）被引入作为 DDPM 的更快替代方案，Jeremy 演示了如何从零开始构建自定义 DDIM。课程最后讨论了 DDPM 和 DDIM 之间的差异，以及使用 DDIM 进行快速采样的优势。

## 讨论的概念

  * 使用 Weights and Biases（W&B）进行实验跟踪
  * Fréchet Inception Distance（FID）指标
  * Kernel Inception Distance（KID）指标
  * 去噪扩散隐式模型（DDIM）

## 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-21-official-topic/103528)

[ __ 20: 混合精度 ](../Lessons/lesson20.html)

[ 22: Karras 等人（2022） __ ](../Lessons/lesson22.html)
