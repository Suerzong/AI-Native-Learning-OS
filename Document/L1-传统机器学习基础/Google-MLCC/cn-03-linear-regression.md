# 线性回归

- 本模块介绍线性回归（Linear Regression），一种用于根据特征预测标签值的统计方法。
- 线性回归模型使用方程（y' = b + w₁x₁ + ...）来表示特征与标签之间的关系。
- 在训练过程中，模型调整其偏置（Bias, b）和权重（Weight, w）以最小化预测值与实际值之间的差异。
- 线性回归可应用于具有多个特征的模型，每个特征具有单独的权重，以提高预测精度。
- 梯度下降（Gradient Descent）和超参数调优（Hyperparameter Tuning）是优化线性回归模型性能的关键技术。

本模块介绍**线性回归**概念。

[**线性回归**](</machine-learning/glossary#linear-regression>)是一种用于发现变量之间关系的统计技术。在 ML 语境中，线性回归找出[**特征**](</machine-learning/glossary#feature>)与[**标签**](</machine-learning/glossary#label>)之间的关系。

例如，假设我们想根据汽车的重量来预测其燃油效率（以每加仑英里数表示），我们有以下数据集：

重量（千磅）（特征） | 每加仑英里数（标签）
---|---
3.5 | 18
3.69 | 15
3.44 | 18
3.43 | 16
4.34 | 15
4.42 | 14
2.37 | 24

如果我们将这些点绘制出来，会得到以下图表：

![图 1. 数据点呈从左到右下降趋势。](/static/machine-learning/crash-course/linear-regression/images/car-data-points.png)

**图 1**. 汽车重量（磅）与每加仑英里数评分的关系。随着汽车变重，其每加仑英里数评分通常会降低。

我们可以通过在数据点之间绘制一条最佳拟合线来创建自己的模型：

![图 2. 数据点之间绘制了代表模型的最佳拟合线。](/static/machine-learning/crash-course/linear-regression/images/car-data-points-with-model.png)

**图 2**. 在上图数据点之间绘制的最佳拟合线。

## 线性回归方程

从代数角度来看，模型定义为 $ y = mx + b $，其中：

- $ y $ 是每加仑英里数——我们要预测的值。
- $ m $ 是直线的斜率。
- $ x $ 是重量——我们的输入值。
- $ b $ 是 y 轴截距。

在 ML 中，我们将线性回归模型的方程写为：

$$ y' = b + w_1x_1 $$

其中：

- $ y' $ 是预测标签——输出值。
- $ b $ 是模型的[**偏置**](</machine-learning/glossary#bias-math-or-bias-term>)。偏置与直线代数方程中的 y 轴截距是同一概念。在 ML 中，偏置有时也称为 $ w_0 $。偏置是模型的[**参数**](</machine-learning/glossary#parameter>)，在训练过程中计算得出。
- $ w_1 $ 是特征的[**权重**](</machine-learning/glossary#weight>)。权重与直线代数方程中的斜率 $ m $ 是同一概念。权重是模型的[**参数**](</machine-learning/glossary#parameter>)，在训练过程中计算得出。
- $ x_1 $ 是一个[**特征**](</machine-learning/glossary#feature>)——输入值。

在训练过程中，模型计算产生最佳模型的权重和偏置。

![图 3. 方程 y' = b + w1x1，每个组成部分标注了其用途。](/static/machine-learning/crash-course/linear-regression/images/equation.png)

**图 3**. 线性模型的数学表示。

在我们的示例中，我们从绘制的直线计算权重和偏置。偏置为 34（直线与 y 轴的交点），权重为 –4.6（直线的斜率）。模型定义为 $ y' = 34 + (-4.6)(x_1) $，我们可以用它来进行预测。例如，使用此模型，一辆 4000 磅的汽车的预测燃油效率为每加仑 15.6 英里。

![图 4. 与图 2 相同的图表，突出显示了点 (4, 15.6)。](/static/machine-learning/crash-course/linear-regression/images/model-prediction.png)

**图 4**. 使用该模型，一辆 4000 磅的汽车的预测燃油效率为每加仑 15.6 英里。

### 具有多个特征的模型

虽然本节示例仅使用了一个特征——汽车的重量，但更复杂的模型可能依赖多个特征，每个特征具有单独的权重（$ w_1 $、$ w_2 $ 等）。例如，依赖五个特征的模型可以写为：

$ y' = b + w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + w_5x_5 $

例如，预测油耗的模型还可以使用以下特征：

- 发动机排量
- 加速度
- 气缸数
- 马力

该模型写为：

![图 5. 具有五个特征的线性回归方程。](/static/machine-learning/crash-course/linear-regression/images/equation-multiple-features.png)

**图 5**. 用于预测汽车每加仑英里数的五特征模型。

通过绘制其中几个附加特征的图表，我们可以看到它们与标签（每加仑英里数）之间也存在线性关系：

![图 6. 以立方厘米为单位的排量与每加仑英里数的图表，呈负线性关系。](/static/machine-learning/crash-course/linear-regression/images/displacement.png)

**图 6**. 汽车排量（立方厘米）与每加仑英里数评分的关系。随着发动机排量增大，每加仑英里数评分通常会降低。

![图 7. 从零加速到六十英里每小时的秒数与每加仑英里数的图表，呈正线性关系。](/static/machine-learning/crash-course/linear-regression/images/acceleration.png)

**图 7**. 汽车加速度与每加仑英里数评分的关系。加速度所需时间越长，每加仑英里数评分通常越高。

### 练习：检验理解

线性回归方程的哪些部分在训练过程中会更新？

**偏置和权重**

在训练过程中，模型会更新偏置和权重。

**预测值**

预测值不会在训练过程中更新。

**特征值**

特征值是数据集的一部分，不会在训练过程中更新。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  练习  ](</machine-learning/crash-course/exercises>)

[ 下一页 损失函数（10 分钟） arrow_forward  ](</machine-learning/crash-course/linear-regression/loss>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-12-09 UTC。
