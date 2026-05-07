（本页面目前为草稿形式）

## 可视化 ConvNets 学到的内容

文献中已经开发了几种理解和可视化卷积网络的方法，部分是对神经网络中学到的特征不可解释这一常见批评的回应。本节简要介绍其中一些方法和相关工作。

### 可视化激活和第一层权重

**层激活。** 最直接的可视化技术是显示前向传播期间网络的激活。对于 ReLU 网络，激活通常开始时看起来相对斑点状且密集，但随着训练的进行，激活通常变得更稀疏和局部化。一个可以用此可视化轻易注意到的危险陷阱是，某些激活图对许多不同输入可能全为零，这可能指示「死」滤波器。

![](/assets/cnnvis/act1.jpeg) ![](/assets/cnnvis/act2.jpeg)

训练好的 AlexNet 的第一层 CONV（左）和第 5 层 CONV（右）的典型激活。每个框显示对应某个滤波器的激活图。

**Conv/FC 滤波器。** 第二种常见策略是可视化权重。这在直接查看原始像素数据的第一层 CONV 上最易解释。

![](/assets/cnnvis/filt1.jpeg) ![](/assets/cnnvis/filt2.jpeg)

训练好的 AlexNet 的第一层（左）和第二层（右）CONV 的典型滤波器。

### 检索最大程度激活神经元的图像

另一种可视化技术是取大量数据集图像，通过网络馈送它们，跟踪哪些图像最大程度激活某个神经元。

![](/assets/cnnvis/pool5max.jpeg)

AlexNet 某些 POOL5 神经元最大程度激活的图像。

### 使用 t-SNE 嵌入编码

ConvNets 可以解释为逐步将图像转换为线性分类器可分离的表示。我们可以使用 t-SNE 将图像嵌入二维空间来可视化此空间的拓扑。

![](/assets/cnnvis/tsne.jpeg)

基于 CNN 编码的一组图像的 t-SNE 嵌入。

### 遮挡图像的部分

如果 ConvNet 将图像分类为狗，我们如何确定它实际上是在关注图像中的狗，而不是背景或其他杂项对象？通过绘制感兴趣类别概率作为遮挡对象位置的函数。

![](/assets/cnnvis/occlude.jpeg)

### 可视化数据梯度及相关方法

**数据梯度。** [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](http://arxiv.org/abs/1312.6034)

**DeconvNet。** [Visualizing and Understanding Convolutional Networks](http://arxiv.org/abs/1311.2901)

**引导反向传播。** [Striving for Simplicity: The All Convolutional Net](http://arxiv.org/abs/1412.6806)

### 基于 CNN 编码重建原始图像

[Understanding Deep Image Representations by Inverting Them](http://arxiv.org/abs/1412.0035)

### 保留了多少空间信息？

[Do ConvNets Learn Correspondence?](http://papers.nips.cc/paper/5420-do-convnets-learn-correspondence.pdf)（简答：是的）

## 欺骗 ConvNets

[Explaining and Harnessing Adversarial Examples](http://arxiv.org/abs/1412.6572)

## 将 ConvNets 与人类标注者比较

[What I learned from competing against a ConvNet on ImageNet](http://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/)
