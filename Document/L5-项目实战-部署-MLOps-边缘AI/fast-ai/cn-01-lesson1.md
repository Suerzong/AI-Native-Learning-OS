[ 面向程序员的实用深度学习 ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "切换阅读模式")

__

  1. [第一部分](../Lessons/lesson1.html)
  2. [1: 入门](../Lessons/lesson1.html)

  * [ 实用深度学习](../index.html)

  * 第一部分 __

    * [ 1: 入门](../Lessons/lesson1.html)

    * [ 2: 部署](../Lessons/lesson2.html)

    * [ 3: 神经网络基础](../Lessons/lesson3.html)

    * [ 4: 自然语言处理（NLP）](../Lessons/lesson4.html)

    * [ 5: 从零构建模型](../Lessons/lesson5.html)

    * [ 6: 随机森林](../Lessons/lesson6.html)

    * [ 7: 协同过滤](../Lessons/lesson7.html)

    * [ 8: 卷积（CNN）](../Lessons/lesson8.html)

    * [ 附加: 数据伦理](../Lessons/lesson8a.html)

    * 课程摘要 __

      * [ 第 1 课](../Lessons/Summaries/lesson1.html)

      * [ 第 2 课](../Lessons/Summaries/lesson2.html)

      * [ 第 3 课](../Lessons/Summaries/lesson3.html)

      * [ 第 4 课](../Lessons/Summaries/lesson4.html)

      * [ 第 5 课](../Lessons/Summaries/lesson5.html)

      * [ 第 6 课](../Lessons/Summaries/lesson6.html)

      * [ 第 7 课](../Lessons/Summaries/lesson7.html)

      * [ 第 8 课](../Lessons/Summaries/lesson8.html)

  * 第二部分 __

    * [ 第二部分概览](../Lessons/part2.html)

    * [ 9: Stable Diffusion](../Lessons/lesson9.html)

    * [ 10: 深入探索](../Lessons/lesson10.html)

    * [ 11: 矩阵乘法](../Lessons/lesson11.html)

    * [ 12: 均值漂移聚类](../Lessons/lesson12.html)

    * [ 13: 反向传播与 MLP](../Lessons/lesson13.html)

    * [ 14: 反向传播](../Lessons/lesson14.html)

    * [ 15: 自编码器](../Lessons/lesson15.html)

    * [ 16: Learner 框架](../Lessons/lesson16.html)

    * [ 17: 初始化/归一化](../Lessons/lesson17.html)

    * [ 18: 加速 SGD 与 ResNet](../Lessons/lesson18.html)

    * [ 19: DDPM 与 Dropout](../Lessons/lesson19.html)

    * [ 20: 混合精度训练](../Lessons/lesson20.html)

    * [ 21: DDIM](../Lessons/lesson21.html)

    * [ 22: Karras 等人（2022）](../Lessons/lesson22.html)

    * [ 23: 超分辨率](../Lessons/lesson23.html)

    * [ 24: 注意力机制与 Transformer](../Lessons/lesson24.html)

    * [ 25: 潜在扩散](../Lessons/lesson25.html)

    * [ 附加: 第 9a 课](https://youtu.be/0_BBRNYInx8)

    * [ 附加: 第 9b 课](https://youtu.be/mYpjmM7O-30)

  * 资源 __

    * [ 书籍](../Resources/book.html)

    * [ 论坛](../Resources/forums.html)

    * [ Kaggle](../Resources/kaggle.html)

    * [ 学员评价](../Resources/testimonials.html)

## 页面目录

  * 视频
  * 如何完成第 1 课
  * 资源
  * 链接
  * 如果需要帮助

  * [__报告问题](https://github.com/fastai/course22-web/issues/new)

  1. [第一部分](../Lessons/lesson1.html)
  2. [1: 入门](../Lessons/lesson1.html)

# 1: 入门

在本课中，你将快速上手——在前五分钟内，你将看到一个完整的端到端示例，训练和使用一个在 2015 年被认为是研究前沿的高级模型。

那么，让我们开始吧！

## 视频

点击下方视频播放。播放后，右下角会出现一个小方框——点击它可以全屏播放。按 `Esc` 退出全屏视图。按 `c` 开启/关闭字幕。

本课部分基于[书籍](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527)的[第 1 章](https://github.com/fastai/fastbook/blob/master/01_intro.ipynb)。

## 如何完成第 1 课

每节课都包含大量动手练习供你尝试。其中大多数在交互式 Notebook 中运行，所有 Notebook 都可以在 [Kaggle](../Resources/kaggle.html) 上找到。如果你不亲自运行这些 Notebook，你将无法从本课程中获得应有的收获——这意味着你需要在 Kaggle 上进行设置。我们有一个页面帮助你在 Kaggle 上入门：[点击这里](../Resources/kaggle.html)前往。除了使用 Kaggle，另一个很好的选择是 [Paperspace Gradient](https://gradient.run/notebooks)。如果你还没有 Paperspace 账户，请使用[此链接](https://console.paperspace.com/signup?R=lg6rnx)注册可获得 10 美元积分（我们也会获得积分）。

设置好 Kaggle 账户后，你需要熟悉 [Jupyter Notebook](https://jupyter.org/)，这是我们本课程大部分内容使用的平台（也是大多数深度学习研究人员和工程师使用的工具）。Jupyter 是用 Python 进行数据科学的最流行工具，这是有充分理由的。它功能强大、灵活且易于使用。我们认为你会喜欢它的！因为学习深度学习最重要的事情是编写代码和实验，所以拥有一个优秀的代码实验平台非常重要。如果你以前没有使用过，我们提供了这个帮助你入门：[Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101)。

好的，现在你有了 Kaggle 账户并知道如何使用 Jupyter，你已经准备好打开本课的 Notebook 了：[在这里](https://www.kaggle.com/code/jhoward/is-it-a-bird-creating-a-model-from-your-own-data)。对于每节课，你可以在课程网页的 _资源_ 部分找到所有使用的 Notebook 链接。例如，对于第 1 课，你会在本节下面看到该部分。

除了观看视频和运行 Notebook 之外，你还应该阅读 fast.ai 书籍《面向程序员的实用深度学习》的相关章节。每节课会在视频下方告诉你需要阅读哪一章。对于本课，是第 1 章。有几种方式可以阅读本书——你可以购买纸质书或 Kindle 电子书，或者免费阅读 Jupyter Notebook 版本。整本书都是用 Jupyter Notebook 编写的，所以你也可以自己执行书中的所有代码。要前往任何章节的交互式 Jupyter 版本，请点击左侧边栏中的[书籍](../Resources/book.html)，在那里你会找到章节链接列表。你还可以在那里找到每章的只读版本。

## 资源

  * 本课的 [Kaggle](../Resources/kaggle.html) Notebook：
    * [这是一只鸟吗？用你自己的数据创建模型](https://www.kaggle.com/code/jhoward/is-it-a-bird-creating-a-model-from-your-own-data)
    * [Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101)
  * fastai 书籍：
    * [出版版本](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch-ebook-dp-B08C2KM7NR/dp/B08C2KM7NR)
    * [免费 Notebook 版本](https://github.com/fastai/fastbook)
    * 第 1 章 [Notebook](https://github.com/fastai/fastbook/blob/master/01_intro.ipynb)
  * 包含[所有课程 Notebook](https://github.com/fastai/course22) 的仓库
  * 书中第 1 章问题的[解答](https://forums.fast.ai/t/fastbook-chapter-1-questionnaire-solutions-wiki/65647)

## 链接

你会发现 fast.ai 的教学方式与你在大学接受的技术学位教育非常不同。大学中几乎所有技术科目都是"自下而上"教授的：从基础开始，逐步推进到解决现实问题的完整方案。但我们是"自上而下"的：从解决现实问题的完整方案开始，逐步深入到基础原理。教育专家推荐这种方法以实现更有效的学习。更多信息，请查看这篇讨论 fast.ai 教学理念的文章：[提供优质的深度学习教育](https://www.fast.ai/2016/10/08/teaching-philosophy/)。

  * 如何学习——fast.ai 学生强烈推荐的书籍
    * [元学习](https://radekosmulski.gumroad.com/l/learn_deep_learning)
    * [一位数学家的挽歌](https://www.maa.org/external_archive/devlin/LockhartsLament.pdf)，Paul Lockhart 著
    * [让学习变得完整](http://www.pz.harvard.edu/resources/making-learning-whole-how-seven-principles-of-teaching-can-transform-education)，David Perkins 著
  * Jupyter
    * 演示：[RISE](https://rise.readthedocs.io/en/stable/)
    * 博客：[fastpages](https://github.com/fastai/fastpages)
    * 用于创建 [fastai 库](https://github.com/fastai/fastai/tree/master/nbs) 的 Notebook
    * [nbdev](https://nbdev.fast.ai/) \- 我们构建的用于使用 Jupyter 创建 Python 库的系统
  * Fastai：深度学习分层 API 论文：[Information Journal](https://www.mdpi.com/2078-2489/11/2/108) 或 [arxiv](https://arxiv.org/abs/2002.04688) 或 [fast.ai](https://www.fast.ai/2020/02/13/fastai-A-Layered-API-for-Deep-Learning/)
  * [用 DALL-E 2 画 Twitter 个人简介](https://twitter.com/nickcammarata/status/1511861061988892675)
  * [timm](https://timm.fast.ai)：PyTorch 图像模型

## 如果需要帮助

[fast.ai 论坛](https://forums.fast.ai/c/p1v5/54)上有很多乐于助人的人，也有许多过去问题的有用答案。有专门针对初学者问题的帮助主题，以确保你的问题不会被遗漏：

  * [帮助：环境设置](https://forums.fast.ai/t/help-setup/95289)
  * [帮助：创建数据集和使用 Gradio / Spaces](https://forums.fast.ai/t/help-creating-a-dataset-and-using-gradio-spaces/96281)
  * [帮助：使用 Colab 或 Kaggle](https://forums.fast.ai/t/help-using-colab-or-kaggle/96280)
  * [帮助：Python、git、bash 等](https://forums.fast.ai/t/help-python-git-bash-etc/96282)
  * [帮助：SGD 和神经网络基础](https://forums.fast.ai/t/help-sgd-and-neural-net-foundations/96286)
  * [帮助：fastai、PyTorch、numpy 等基础](https://forums.fast.ai/t/help-basics-of-fastai-pytorch-numpy-etc/96285)
  * [帮助：不适合其他分类的初学者问题](https://forums.fast.ai/t/help-beginner-questions-that-dont-fit-elsewhere/96284)

[ __ 实用深度学习 ](../index.html)

[ 2: 部署 __](../Lessons/lesson2.html)
