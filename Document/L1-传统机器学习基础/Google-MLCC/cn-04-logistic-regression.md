# 逻辑回归

- 本模块介绍逻辑回归（Logistic Regression），一种用于预测结果概率的模型，不同于预测连续数值的线性回归。
- 逻辑回归使用 Sigmoid 函数计算概率，并采用对数损失（Log Loss）作为其损失函数。
- 在训练逻辑回归模型时，正则化（Regularization）对于防止过拟合（Overfitting）和改善泛化能力至关重要。
- 本模块涵盖线性回归与逻辑回归的比较，并探讨逻辑回归的使用场景。
- 本模块时长约 35 分钟，要求具备机器学习入门和线性回归概念的基础知识。

在[线性回归模块](</machine-learning/crash-course/linear-regression>)中，你学习了如何构建模型来进行连续数值预测，例如汽车的燃油效率。但如果你想构建一个回答"今天会下雨吗？"或"这封邮件是垃圾邮件吗？"这样的问题的模型呢？

本模块介绍一种新型回归模型，称为[**逻辑回归**](</machine-learning/glossary#logistic_regression>)，它被设计用于预测给定结果的概率。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/linear-regression/test-your-knowledge>)

[ 下一页 计算概率（10 分钟） arrow_forward  ](</machine-learning/crash-course/logistic-regression/sigmoid-function>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
