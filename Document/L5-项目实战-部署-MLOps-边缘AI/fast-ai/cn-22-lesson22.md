[ 给程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [Part 2](../Lessons/part2.html)
  2. [22: Karras 等人（2022）](../Lessons/lesson22.html)

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
  2. [22: Karras 等人（2022）](../Lessons/lesson22.html)

# 22: Karras 等人（2022）

Jeremy 首先讨论了对 DDPM/DDIM 实现的改进。他探索了移除整数步数的概念，使过程更加连续。然后深入研究了在不将时间步作为输入的情况下预测图像中的噪声量，并修改了 DDIM 步骤以使用每个图像的预测 alpha bar。

本课的重点是研究和实现 Karras 等人 2022 年的论文 [Elucidating the Design Space of Diffusion-Based Generative Models](https://arxiv.org/abs/2206.00364)（阐明基于扩散的生成模型的设计空间）。该论文使用*预处理*（pre-conditioning）来确保模型的输入和目标被缩放至单位方差。模型根据输入中存在的噪声量，预测干净图像和噪声的插值版本。

课程涵盖了各种采样技术，如 Euler 采样器（Euler sampler）、Ancestral Euler 采样器和 Heun 方法（Heun's method）。Jeremy 解释了这些方法背后的概念，并演示了如何使用它们来改进采样过程。他强调了理解研究论文中底层概念和技术的重要性，并展示了如何将这些应用于改善模型性能。

## 讨论的概念

  * DDPM/DDIM 改进
  * 预测图像中的噪声量
  * 扩散模型的噪声调度
  * 缩放输入和输出图像
  * 单位方差输入输出的重要性
  * 不同采样器的实现和性能
    * Euler 采样器
    * Ancestral Euler 采样器
    * Heun 方法
    * LMS 采样器

## 视频

  * [讨论本课](https://forums.fast.ai/t/lesson-22-official-topic/103586)

[ __ 21: DDIM ](../Lessons/lesson21.html)

[ 23: 超分辨率 __ ](../Lessons/lesson23.html)
