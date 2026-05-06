[编码员实用深度学习](../index.html)

  * [无](https://github.com/fastai/course22)

[无](“切换阅读器模式”)

__

  1. [第2部分](../Lessons/part2.html)
  2. [11：矩阵乘法](../Lessons/lesson11.html)

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
  2. [11：矩阵乘法](../Lessons/lesson11.html)

#11：矩阵乘法

在本课中，我们讨论了学生在论坛上分享的各种技术和实验，例如在视觉上吸引人的过渡提示之间进行插值，改进文本到图像生成的更新过程，以及在图像生成过程中减少引导比例的新颖方法。然后我们深入研究一篇名为 DiffEdit 的新论文，该论文重点关注使用文本条件扩散模型进行语义图像编辑。我们会贯穿阅读和理解论文的过程，强调抓住主要思想而不是陷入每个细节的重要性。

然后，我们开始使用 Python 深入探索矩阵乘法，将 APL 与 PyTorch 进行比较，并介绍 Frobenius 范数的概念。我们还讨论了强大的广播概念，它允许在不同形状的张量之间进行运算，并展示其在加速矩阵乘法方面的效率。本课程中介绍的技术使我们能够将初始 Python 实现速度加快约 500 万倍，包括利用 GPU 实现大规模并行！

## 讨论的概念

  * 扩散改进
    * 在提示之间进行插值以实现视觉上吸引人的过渡
    * 改进文本到图像生成的更新过程
    * 减小图像生成过程中的引导比例
  * 理解研究论文
  * 使用 Python 和 Numba 进行矩阵乘法
  * APL 与 PyTorch 的比较
  * 弗罗贝尼乌斯范数
  * 深度学习和机器学习代码中的广播

＃＃ 视频

## 课程资源

  * [讨论本课](https://forums.fast.ai/t/lesson-11-official-topic/101508)
  * [DiffEdit：具有阻抗引导的基于肿瘤的图像编辑](https://arxiv.org/abs/2210.11427)
  * 数学符号
    * [希腊字母](https://en.wikipedia.org/wiki/Greek_alphabet)
    * [一本数学备忘单](https://ourway.keybase.pub/mathematics_cheat_sheet.pdf) (PDF)
    * [数学符号词汇表](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols#Other_brackets) (wikipedia)
    * [像素2tex](https://github.com/lukas-blecher/LaTeX-OCR)（开源）或[数学像素](https://mathpix.com/)（商业）
    * [深度学习的希腊字母](https://ankiweb.net/shared/info/2118139507) \- Anki 甲板包含与 fastai 相关的希腊字母
    * [解毒](https://detexify.kirelabs.org/classify.html) 绘制数学符号

[__ 10：深入研究](../Lessons/lesson10.html)

[12：均值相等__](../Lessons/lesson12.html)
