# 处理数值数据

- 本模块侧重于为机器学习模型准备数值数据（Numerical Data），如温度或体重。
- 机器学习从业者在数据准备任务（如清洗和转换）上花费大量时间。
- 本模块涵盖特征缩放（Feature Scaling）、异常值检测（Outlier Detection）和分箱（Binning）等技术，以提高模型训练的数据质量。
- 学习者在开始本模块之前应具备基本的机器学习概念。
- 类别数据（Categorical Data），如邮政编码，由于其独特的特征和处理要求，将在单独的模块中讨论。

ML 从业者在评估、清洗和转换数据上花费的时间远远超过构建模型的时间。数据如此重要，以至于本课程专门安排了三个完整单元来讨论该主题：

- 处理数值数据（本单元）
- [处理类别数据](</machine-learning/crash-course/categorical-data>)
- [数据集、泛化与过拟合](</machine-learning/crash-course/overfitting>)

本单元侧重于[**数值数据**](</machine-learning/glossary#numerical-data>)，即表现为数字的整数或浮点值。也就是说，它们具有可加性、可计数、有序等特性。下一个单元侧重于[**类别数据**](</machine-learning/glossary#categorical-data>)，它可以包含表现为类别的数字。第三个单元侧重于如何准备数据，以确保训练和评估模型时获得高质量结果。

数值数据的例子包括：

- 温度
- 体重
- 在自然保护区越冬的鹿的数量

相比之下，美国邮政编码虽然是五位或九位数字，但其行为不像数字，也不表示数学关系。邮政编码 40004（肯塔基州纳尔逊县）并不是邮政编码 20002（华盛顿特区）的两倍。这些数字代表类别，特别是地理区域，因此被视为类别数据。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/classification/test-your-knowledge>)

[ 下一页 模型如何通过特征向量摄入数据（5 分钟） arrow_forward  ](</machine-learning/crash-course/numerical-data/feature-vectors>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
