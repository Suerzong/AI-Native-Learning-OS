# 动手学深度学习（Dive into Deep Learning）

[![](_images/front-cup.jpg)](https://www.amazon.com/Dive-into-Learning-Aston-Zhang/dp/1009389432/)

## 动手学深度学习

**交互式**深度学习教材，包含代码、数学和讨论

基于 **PyTorch**、**NumPy/MXNet**、**JAX** 和 **TensorFlow** 实现

已被全球 70 个国家的 500 所高校采用

[Star](https://github.com/d2l-ai/d2l-en)

[关注 @D2L_ai](https://twitter.com/D2L_ai?ref_src=twsrc%5Etfw)

  * [2023年2月] 本书即将由剑桥大学出版社出版（[订购](https://www.amazon.com/Dive-into-Learning-Aston-Zhang/dp/1009389432/)）。中文版是中国最大在线书店的[畅销书](https://raw.githubusercontent.com/d2l-ai/d2l-zh/master/static/frontpage/_images/sales/jd-2023020304-all-ai-zh-4.png)。请关注 D2L 的[开源项目](https://github.com/d2l-ai/d2l-en)以获取最新更新。
  * [2022年12月] JAX 实现已上线！新增[强化学习](chapter_reinforcement-learning/index.html)、[高斯过程](chapter_gaussian-processes/index.html)和[超参数优化](chapter_hyperparameter-optimization/index.html)等主题！
  * [2022年7月] 查看我们的[新 API](chapter_linear-regression/oo-design.html) 用于实现，以及[分类](chapter_linear-classification/generalization-classification.html)和[深度学习](chapter_multilayer-perceptrons/generalization-deep.html)中的泛化、[ResNeXt](chapter_convolutional-modern/resnet.html)、[CNN 设计空间](chapter_convolutional-modern/cnn-design.html)、用于[视觉](chapter_attention-mechanisms-and-transformers/vision-transformer.html)和[大规模预训练](chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html)的 Transformer 等新主题。
  * [2022年5月] 加入[我们](https://github.com/d2l-ai)，改进正在进行的[葡萄牙语](https://pt.d2l.ai/)、[土耳其语](https://tr.d2l.ai/)、[越南语](https://d2l.aivivn.com/)、[韩语](https://ko.d2l.ai/)和[日语](https://ja.d2l.ai/)翻译。
  * [2021年12月] 我们新增了一个免费[运行本书](#jupyter)的选项：查看 [SageMaker Studio Lab](https://studiolab.sagemaker.aws/import/github/d2l-ai/d2l-pytorch-sagemaker-studio-lab/blob/main/GettingStarted-D2L.ipynb)。
  * [2021年5月] Berkeley 课程的幻灯片、Jupyter 笔记本、作业和视频可在[课程大纲页面](https://courses.d2l.ai/berkeley-stat-157/syllabus.html)找到。

## 作者

![](./_images/aston.jpg)

### [Aston Zhang](https://www.astonzhang.com/)

Amazon

![](./_images/zack.jpg)

### [Zack C. Lipton](http://zacklipton.com/)

CMU and Amazon

![](./_images/mu.jpg)

### [Mu Li](https://www.cs.cmu.edu/~muli/)

Amazon

![](./_images/alex.jpg)

### [Alex J. Smola](https://alex.smola.org/)

Amazon

## 第二卷章节作者

![](./_images/pratik.jpg)

### [Pratik Chaudhari](https://pratikac.github.io/)

UPenn and Amazon
 _[强化学习](chapter_reinforcement-learning/index.html)_

![](./_images/rasool.jpg)

### [Rasool Fakoor](https://sites.google.com/site/rfakoor)

Amazon
 _[强化学习](chapter_reinforcement-learning/index.html)_

![](./_images/kavosh.jpg)

### [Kavosh Asadi](https://cs.brown.edu/~kasadiat/)

Amazon
 _[强化学习](chapter_reinforcement-learning/index.html)_

![](./_images/andrew.jpg)

### [Andrew Gordon Wilson](https://cims.nyu.edu/~andrewgw/)

NYU and Amazon
 _[高斯过程](chapter_gaussian-processes/index.html)_

![](./_images/aaron.jpg)

### [Aaron Klein](https://aaronkl.github.io/)

Amazon
 _[超参数优化](chapter_hyperparameter-optimization/index.html)_

![](./_images/matthias.jpg)

### [Matthias Seeger](https://mseeger.github.io/)

Amazon
 _[超参数优化](chapter_hyperparameter-optimization/index.html)_

![](./_images/cedric.png)

### [Cedric Archambeau](http://www0.cs.ucl.ac.uk/staff/c.archambeau/)

Amazon
 _[超参数优化](chapter_hyperparameter-optimization/index.html)_

![](./_images/shuai.jpg)

### [Shuai Zhang](https://shuaizhang.tech/)

Amazon
_[推荐系统](chapter_recommender-systems/index.html)_

![](./_images/yi.jpg)

### [Yi Tay](https://vanzytay.github.io/)

Google
_[推荐系统](chapter_recommender-systems/index.html)_

![](./_images/brent.jpg)

### [Brent Werness](https://www.linkedin.com/in/brent-werness-1506471b7/)

Amazon
 _[深度学习的数学](chapter_appendix-mathematics-for-deep-learning/index.html)_

![](./_images/rachel.jpeg)

### [Rachel Hu](https://www.linkedin.com/in/rachelsonghu/)

Amazon
 _[深度学习的数学](chapter_appendix-mathematics-for-deep-learning/index.html)_

## 框架适配作者

![](./_images/anirudh.jpg)

### [Anirudh Dagar](https://github.com/AnirudhDagar)

Amazon
 _PyTorch 适配_
 _JAX 适配_

![](./_images/yuan.jpg)

### [Yuan Tang](https://terrytangyuan.github.io/about/)

Akuity
 _TensorFlow 适配_

### 感谢所有[社区贡献者](https://github.com/d2l-ai/d2l-en/graphs/contributors)让这本开源书变得更好。

#### [为本书做贡献](https://d2l.ai/chapter_appendix-tools-for-deep-learning/contributing.html)

## 每一节都是一个可执行的 Jupyter 笔记本

你可以修改代码、调整超参数，获得即时反馈，从而积累深度学习的实践经验。

[ ![](./_images/laptop_jupyter.png) 本地运行 ](./chapter_installation/index.html)

[ ![](./_images/logos/sagemaker-studio-lab.png) Amazon SageMaker
Studio Lab ](https://studiolab.sagemaker.aws/import/github/d2l-ai/d2l-pytorch-sagemaker-studio-lab/blob/main/GettingStarted-D2L.ipynb)

[ ![](./_images/logos/sagemaker.png) Amazon
SageMaker ](./chapter_appendix-tools-for-deep-learning/sagemaker.html)

[ ![](./_images/logos/colab.png) Google
Colab ](./chapter_appendix-tools-for-deep-learning/colab.html)

![](_images/notebook.gif)

## 数学 + 图 + 代码

我们提供交互式学习体验，融合数学、图形、代码、文本和讨论，通过在真实数据集上的实验来阐释和实现概念与技术。

![](_images/eq.jpg)

![](_images/figure.jpg)

![](_images/code.jpg)

![](_images/forum.gif)

## 活跃的[社区](https://discuss.d2l.ai/c/5)支持

你可以通过每节提供的链接，在社区中与数千名同行讨论和学习。

## D2L 作为教材或参考书

![](./_images/logos/logoimg1.png)

![](./_images/logos/logoimg2.png)

![](./_images/logos/logoimg3.png)

![](./_images/logos/logoimg4.png)

![](./_images/logos/logoimg5.png)

![](./_images/logos/logoimg6.png)

![](./_images/logos/logoimg7.png)

![](./_images/map.png)

[+] _点击此处显示不完整列表。_

（此处省略大学列表，保留原文件中的完整列表）

### 引用本书的 BibTeX 条目

```
@book{zhang2023dive,
    title={Dive into Deep Learning},
    author={Zhang, Aston and Lipton, Zachary C. and Li, Mu and Smola, Alexander J.},
    publisher={Cambridge University Press},
    note={\url{https://D2L.ai}},
    year={2023}
}
```

[ __ 上一页 前言 ](chapter_preface/index.html) [ __ 下一页 1. 引言 ](chapter_introduction/index.html)
