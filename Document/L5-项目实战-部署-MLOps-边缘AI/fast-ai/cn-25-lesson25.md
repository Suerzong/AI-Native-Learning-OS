[ 给程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [Part 2](../Lessons/part2.html)
  2. [25: 潜在扩散](../Lessons/lesson25.html)

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

  * 视频
  * 课程资源

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [25: 潜在扩散](../Lessons/lesson25.html)

# 25: 潜在扩散（Latent diffusion）

在本系列的最后一课中，Johno 首先向我们展示了如何将声音转换为图像，然后利用本课程中学到的知识来生成音频！他使用这种方法构建并演示了一个非常有效的鸟鸣生成器。

然后 Jeremy 通过展示如何使用变分编码器（variational encoder）中的潜在变量（latents）作为常规扩散模型中的"像素"，完成了"从零开始的 Stable Diffusion"系列。他还描述了一个值得学生跟进的新想法：如果将潜在变量用于其他目的，例如分类模型会怎样？也许这将打开一个全新的可能性世界，例如 latents-FID、latents-perceptual-loss 以及扩散引导的新方法！

## 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-25-official-topic/104573)
  * [02_diffusion for audio.pynb](https://github.com/huggingface/diffusion-models-class/blob/main/unit4/02_diffusion_for_audio.ipynb)
  * Riffusion: [演示](https://www.riffusion.com/) | [仓库](https://github.com/riffusion/riffusion)
  * 讨论的笔记本: [nb 29](https://github.com/fastai/course22p2/blob/master/nbs/29_vae.ipynb) | [nb 30](https://github.com/fastai/course22p2/blob/master/nbs/30_lsun_diffusion-latents.ipynb) | [nb 31](https://github.com/fastai/course22p2/blob/master/nbs/31_imgnet_latents-widish.ipynb) | [Johno 的简易音频扩散](https://colab.research.google.com/drive/1b3CeZB2FfRGr5NPYDVvk34hyZFBtgub5?usp=sharing)

[ __ 24: 注意力与 Transformer ](../Lessons/lesson24.html)

[ 书籍 __ ](../Resources/book.html)
