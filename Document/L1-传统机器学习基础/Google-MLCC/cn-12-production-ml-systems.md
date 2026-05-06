# 机器学习生产系统

- 本模块探讨机器学习生产系统的更广泛生态系统，强调模型本身只是整个系统的一小部分。
- 你将学习根据具体需求选择合适的训练和推理范式（静态或动态）。
- 本模块涵盖机器学习生产系统的关键方面，包括测试、识别潜在缺陷以及监控系统组件。
- 作为前提条件，要求熟悉基础机器学习概念，包括线性回归、数据类型和过拟合。
- 在之前模块的基础上，本内容将焦点转向在实际场景中部署和维护 ML 模型的实践方面。

到目前为止，本课程一直侧重于构建机器学习（ML）模型。然而，正如图 1 所示，真实的机器学习生产系统是庞大的生态系统，模型只是一个相对较小的部分。

![图 1. ML 系统图包含以下组件：数据收集、特征提取、流程管理工具、数据验证、配置、机器资源管理、监控、服务基础设施和 ML 模型代码。图中 ML 模型代码部分与其他九个组件相比显得很小。](/static/machine-learning/crash-course/images/MlSystem.png) **图 1.** 一个真实的机器学习生产系统包含许多组件。

真实机器学习生产系统的核心是 ML 模型代码，但它通常只占系统总代码库的 5% 或更少。这不是印刷错误；它比你预期的要少得多。注意，ML 生产系统在输入数据上投入了大量资源：收集数据、验证数据和从中提取特征。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/llm/test-your-knowledge>)

[ 下一页 静态训练与动态训练（10 分钟） arrow_forward  ](</machine-learning/crash-course/production-ml-systems/static-vs-dynamic-training>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
