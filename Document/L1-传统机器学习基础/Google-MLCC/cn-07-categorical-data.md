# 处理类别数据

- 本模块侧重于在机器学习中区分类别数据（Categorical Data）和数值数据（Numerical Data）。
- 你将学习如何使用独热向量（One-Hot Vector）表示类别数据，并解决与之相关的常见问题。
- 本模块涵盖将类别数据转换为适合模型训练的数值向量的编码（Encoding）技术。
- 还讨论了特征交叉（Feature Cross），一种组合类别特征以捕获交互关系的方法。
- 假设你已具备机器学习入门和处理数值数据的先验知识。

[**类别数据**](</machine-learning/glossary#categorical-data>)具有_一组特定的_可能值。例如：

- 国家公园中不同种类的动物
- 特定城市的街道名称
- 邮件是否为垃圾邮件
- 房屋外墙涂刷的颜色
- 分箱后的数字，在[处理数值数据](</machine-learning/crash-course/numerical-data>)模块中有描述

## 数字也可以是类别数据

真正的[**数值数据**](</machine-learning/glossary#numerical-data>)可以有意义地进行乘法运算。例如，考虑一个根据房屋面积预测房屋价值的模型。注意，用于评估房价的有用模型通常依赖数百个特征。但假设其他条件相同，200 平方米的房屋价值大约应是 100 平方米相同房屋的两倍。

通常，你应该将包含整数值的特征表示为类别数据，而不是数值数据。例如，考虑一个邮政编码特征，其值为整数。如果你以数值方式而非类别方式表示此特征，就是在要求模型找出不同邮政编码之间的数值关系。也就是说，你在告诉模型将邮政编码 20004 视为邮政编码 10002 的两倍（或一半）大小的信号。将邮政编码表示为类别数据可以让模型单独对每个邮政编码进行加权。

## 编码

**编码（Encoding）** 意味着将类别数据或其他数据转换为模型可以训练的数值向量。这种转换是必要的，因为模型只能训练浮点值；模型无法训练字符串，如 `"dog"` 或 `"maple"`。本模块解释了类别数据的不同编码方法。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  结论（2 分钟）  ](</machine-learning/crash-course/numerical-data/conclusion>)

[ 下一页 词汇表与独热编码（10 分钟） arrow_forward  ](</machine-learning/crash-course/categorical-data/one-hot-encoding>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
