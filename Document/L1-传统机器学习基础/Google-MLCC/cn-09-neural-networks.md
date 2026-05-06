# 神经网络

- 本模块探讨神经网络（Neural Network），一种旨在自动识别数据中非线性（Nonlinear）模式的模型架构，无需手动进行特征交叉实验。
- 你将学习深度神经网络（Deep Neural Network）的基本组件，包括节点（Node）、隐藏层（Hidden Layer）和激活函数（Activation Function），以及它们如何参与预测。
- 本模块涵盖神经网络的训练过程，使用反向传播算法（Backpropagation）优化预测并最小化损失。
- 此外，你将了解神经网络如何使用一对多（One-vs-All）和一对一（One-vs-One）方法处理多类别分类问题。
- 本模块建立在机器学习概念的先验知识之上，如线性回归、逻辑回归、分类以及处理数值和类别数据。

你可能还记得[类别数据模块](</machine-learning/crash-course/categorical-data>)中的[特征交叉练习](</machine-learning/crash-course/categorical-data/feature-cross-exercises>)，以下分类问题是非线性的：

![图 1. 笛卡尔坐标平面分为四个象限，每个象限填充了形状类似正方形的随机点。右上和左下象限的点为蓝色，左上和右下象限的点为橙色。](/static/machine-learning/crash-course/neural-networks/images/nonlinear_simple.png) **图 1.** 非线性分类问题。线性函数无法干净地将所有蓝点与橙点分开。

"非线性"意味着你无法用 \\(b + w_1x_1 + w_2x_2\\) 形式的模型准确预测标签。换句话说，"决策面（Decision Surface）"不是一条直线。

但是，如果对特征 $x_1$ 和 $x_2$ 进行特征交叉，我们就可以使用[**线性模型**](</machine-learning/glossary#linear-model>)来表示两个特征之间的非线性关系：$b + w_1x_1 + w_2x_2 + w_3x_3$，其中 $x_3$ 是 $x_1$ 和 $x_2$ 之间的特征交叉：

![图 2. 与图 1 相同的蓝点和橙点笛卡尔坐标平面。但这次在网格上方绘制了一条白色双曲线，将右上和左下象限（现在以蓝色背景着色）的蓝点与左上和右下象限（现在以橙色背景着色）的橙点分开。](/static/machine-learning/crash-course/neural-networks/images/nonlinear_simple_feature_cross.png) **图 2.** 通过添加特征交叉 _x_1_x_2，线性模型可以学习一个将蓝点与橙点分开的双曲线形状。

现在考虑以下数据集：

![图 3. 笛卡尔坐标平面分为四个象限。原点中心有一个圆形的蓝色点簇，周围环绕着一圈橙色点。](/static/machine-learning/crash-course/neural-networks/images/nonlinear_complex.png) **图 3.** 一个更困难的非线性分类问题。

你可能还记得在[特征交叉练习](</machine-learning/crash-course/categorical-data/feature-cross-exercises>)中，确定正确的特征交叉以使线性模型拟合这些数据需要更多的努力和实验。

但如果你不必自己完成所有这些实验呢？[**神经网络**](</machine-learning/glossary#neural_network>)是一类旨在发现数据中[**非线性**](</machine-learning/glossary#nonlinear>)模式的模型架构。在神经网络的训练过程中，[**模型**](</machine-learning/glossary#model>)自动学习应对输入数据执行的最优特征交叉，以最小化损失。

在以下部分中，我们将更详细地了解神经网络的工作原理。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/overfitting/test-your-knowledge>)

[ 下一页 节点与隐藏层（15 分钟） arrow_forward  ](</machine-learning/crash-course/neural-networks/nodes-hidden-layers>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
