[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [9：稳定的扩散](../Lessons/lesson9.html)

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

  * 你需要知道什么
  * 课程概述
  * 讨论的概念
  * 视频
  * 课程资源
  * 课程链接
  * fast.ai 课程的有用背景

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第2部分](../Lessons/part2.html)
  2. [9：稳定的扩散](../Lessons/lesson9.html)

＃9：稳定的扩散

## 你需要知道什么

以下是完成本课程您需要了解的内容：

  * 课程以视频形式呈现，点击右侧目录可直接跳转
  * 每个视频都会经过一个或多个 Jupyter 笔记本，您需要运行和试验这些笔记本才能充分利用课程
  * 完成课程所需的所有信息（包括带有笔记本的存储库的链接）位于课程页面的“课程资源”部分
  * 在课程资源中，您会找到一个“讨论本课程”链接，该链接将带您进入我们论坛上针对该特定课程的问答页面
  * 本课程涵盖的材料包括通常只包含在研究生水平课程中的内容。我们尝试以尽可能清晰的方式呈现它，但您应该努力工作并投入大量时间的学习
  * 我们假设您熟悉本课程第 1 部分中的材料。如果您发现自己对课程中提到的一些基本深度学习想法不确定，我们建议您回去学习第 1 部分中涵盖这些想法的课程
  * 如果我们使用的数学或编码概念让您感到不舒服，请不要害怕寻找其他教程来帮助填补您的空白
  * 在 [论坛.fast.ai](https://forums.fast.ai) 上，您可以与许多其他学生合作，并且许多人正在寻找学习小组或学习伙伴。事实证明，对于大多数人来说，小组学习比单独学习更有效
  * 在许多课程中，我们都会为您提供一个需要完成的挑战，其中一些涉及尝试新颖的研究方向，您将在其中冒险进入学术未知领域。

## 课程概述

本课程首先介绍如何使用扩散器库中的管道来生成图像。 Diffusers（我们认为！）是目前用于图像生成的最佳库。它有很多功能并且非常灵活。我们解释了如何使用其众多功能，并讨论了访问使用该库所需的 GPU 资源的选项。

我们讨论在扩散器中使用稳定扩散时可用的一些巧妙的调整，并展示如何使用它们：引导比例（用于改变提示使用的数量）、负面提示（用于从图像中删除概念）、图像初始化（用于从现有图像开始）、文本反转（用于将您自己的概念添加到生成的图像中）、Dreambooth（文本反转的另一种方法）。

本课程的后半部分涵盖了稳定扩散中涉及的关键概念：

  * CLIP嵌入
  * VAE（变分自动编码器）
  * 使用unet预测噪声
  * 使用调度程序消除噪音

杰里米（Jeremy）使用新颖的解释展示了稳定扩散如何工作的理论基础，该解释显示了该理论易于理解的直觉。他介绍了有限差分和分析导数的概念，使用训练神经网络来识别像素调整以使图像看起来更像手写数字的示例，并描述了此类模型的导数如何提供所需的分数，为生成手写数字的扩散过程提供基础。

本课程还涵盖有限差分、分析导数、自动编码器和 U-Net。 Jeremy 介绍了创建一个模型的概念，该模型可以接受一个句子并返回表示图像的数字向量，使用两个模型：文本编码器和图像编码器。本课程最后讨论了基于扩散的模型和深度学习优化器之间的相似性，并提出了新的研究方向。

## 讨论的概念

  * 稳定的扩散
  * Hugging Face 的扩散器库
  * 预训练管道
  * 指导尺度
  * 负面提示
  * 图像到图像管道
  * 有限差分
  * 解析导数
  * 自动编码器
  * 文本倒置
  * 梦想展位
  * 潜伏者
  * U网
  * 文本编码器和图像编码器
  * 对比损失函数
  * CLIP文本编码器
  * 深度学习优化器
  * 知觉丧失

＃＃ 视频

## 课程资源

  * 其他视频
    * [第 9A 课视频](https://www.youtube.com/watch?v=844LY0vYQhc)—深入探究—来自 @johnowhitaker（附带 [随附的笔记本](https://github.com/fastai/diffusion-nbs/blob/master/Stable%20Diffusion%20Deep%20Dive.ipynb)）
    * [第 9B 课视频](https://youtu.be/mYpjmM7O-30)—扩散数学—来自 @seem 和 @ilovescience
  * Jeremy 的 [课程笔记](https://forums.fast.ai/uploads/short-url/dI0cWOaQQEHFYPKVyM9BkSWY4rQ.pdf)
  * 斋戒书：
    * [已发布版本](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch-ebook-dp-B08C2KM7NR/dp/B08C2KM7NR)
    * [免费笔记本版本](https://github.com/fastai/fastbook)
    * [完整章节示例](https://fastai.github.io/fastbook2e/)
  * 学生笔记 – [课程笔记](https://rekil156.github.io/rekilblog/posts/lesson9_stableDissufion/Lesson9.html) h/t @barnacl

## 课程链接

  * [讨论本课](https://forums.fast.ai/t/lesson-9-official-topic/100562)
  * [课程捐赠](https://github.com/fastai/course22p2)
  * [扩散-nbs回购协议](https://github.com/fastai/diffusion-nbs)
  * [HuggingFace 笔记本电脑](https://github.com/huggingface/notebooks)
  * GPU服务器
    * [拉姆达实验室](https://forums.fast.ai/t/lambda-gpu-cloud-for-deep-learning-a100s-at-1-10-gpu-hr-150-sign-up-credit/100942/2)
    * [纸空间突变](https://www.paperspace.com/gradient)
    * [贾维斯实验室](https://jarvislabs.ai/)
    * [vast.ai - 众包GPU服务](https://vast.ai/)
  * 及时工程
    * [词典](https://lexica.art/)
    * [提示英雄](https://prompthero.com/)
    * [Hexo - 1000 万张图片和提示](https://hexo.ai/)
  * [人工智能艺术的工具和资源](https://pharmapsychotic.com/tools.html)
  * [法斯塔仓库](https://github.com/fastai/fastai)

## fast.ai 课程的有用背景

  * [家庭作业](https://forums.fast.ai/t/did-you-do-the-homework/66034)
  * [摘要 + 杰里米说要做的事 + 问题](../t/podcast-writeup-summaries-things-jeremy-says-to-do-qs/66194)
  * Fastai：深度学习分层 API 论文：[信息杂志](https://www.mdpi.com/2078-2489/11/2/108) 或 [arxiv](https://arxiv.org/abs/2002.04688) 或[快速人工智能](https://www.fast.ai/2020/02/13/fastai-A-Layered-API-for-Deep-Learning/)
  * [提供良好的深度学习教育](https://www.fast.ai/2016/10/08/teaching-philosophy/)：fast.ai教学理念
  * [“如何不做斋戒”](https://medium.com/@init_27/how-not-to-do-fast-ai-or-any-ml-mooc-3d34a7e0ab8c)
  * [《FastAI零课：视频+笔记》](https://www.alexstrick.com/blog/fastai-lesson-zero)

[__ 第 2 部分概述](../Lessons/part2.html)

[10：深入研究__](../Lessons/lesson10.html)
