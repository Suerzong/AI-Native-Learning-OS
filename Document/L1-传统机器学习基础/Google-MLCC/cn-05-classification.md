# 分类

- 本模块侧重于将逻辑回归模型转换为二元分类（Binary Classification）模型，用于预测类别而非概率。
- 你将学习如何确定分类的最佳阈值（Threshold）、计算和选择合适的评估指标，以及解读 ROC 和 AUC。
- 本模块涵盖二元分类，并简要介绍多类别分类（Multi-Class Classification），建立在机器学习、线性回归和逻辑回归的先验知识之上。
- 内容探讨了评估分类模型预测质量的方法，并将其应用于实际场景。

在[逻辑回归模块](</machine-learning/crash-course/logistic-regression>)中，你学习了如何使用[**Sigmoid 函数**](</machine-learning/glossary#sigmoid-function>)将原始模型输出转换为 0 到 1 之间的值以进行概率预测——例如，预测某封邮件有 75% 的概率是垃圾邮件。但如果你的目标不是输出概率而是输出类别呢——例如，预测某封邮件是"垃圾邮件"还是"非垃圾邮件"？

[**分类**](</machine-learning/glossary#classification-model>)是预测某个样本属于一组[**类别**](</machine-learning/glossary#class>)中哪一个的任务。在本模块中，你将学习如何将预测概率的逻辑回归模型转换为预测两个类别之一的[**二元分类**](</machine-learning/glossary#binary-classification>)模型。你还将学习如何选择和计算适当的指标来评估分类模型的预测质量。最后，你将简要了解[**多类别分类**](</machine-learning/glossary#multi-class>)问题，课程后续将对此进行更深入的讨论。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/logistic-regression/test-your-knowledge>)

[ 下一页 阈值与混淆矩阵（12 分钟） arrow_forward  ](</machine-learning/crash-course/classification/thresholding>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
