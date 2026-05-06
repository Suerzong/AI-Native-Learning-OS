# 嵌入

- 本模块解释如何创建嵌入（Embedding），即稀疏数据（Sparse Data）的低维表示，以解决独热编码（One-Hot Encoding）中大型输入向量和向量之间缺乏有意义关系的问题。
- 独热编码创建大型输入向量，导致神经网络中权重数量巨大，需要更多数据、计算和内存。
- 独热编码向量缺乏有意义的关系，无法捕获项目之间的语义相似性，例如热狗和沙威玛比热狗和沙拉更相似的例子。
- 嵌入通过提供捕获语义关系的稠密向量（Dense Vector）表示来降低数据维度，从而提高机器学习模型的效率和性能。
- 本模块假设熟悉机器学习入门概念，如线性回归、类别数据和神经网络。

假设你正在开发一个食物推荐应用，用户输入他们最喜欢的餐食，应用推荐他们可能喜欢的类似餐食。你想开发一个机器学习（ML）模型来预测食物相似性，以便你的应用可以提供高质量的推荐（"既然你喜欢煎饼，我们推荐可丽饼"）。

为了训练你的模型，你整理了一个包含 5000 种流行餐食项目的数据集，包括罗宋汤、热狗、沙拉、披萨和沙威玛。

![图 1. 五种食物的插图集。从左上角顺时针依次为：罗宋汤、热狗、沙拉、披萨、沙威玛。](/static/machine-learning/crash-course/embeddings/images/food_images.png) **图 1.** 食物数据集中包含的餐食项目样本。

你创建一个 `meal` 特征，包含数据集中每个餐食项目的[**独热编码**](</machine-learning/glossary#one-hot-encoding>)表示。[**编码（Encoding）**](</machine-learning/glossary#encoder>)指的是选择数据的初始数值表示以训练模型的过程。

![图 2. 上：罗宋汤的独热编码可视化。向量 \[1, 0, 0, 0, ..., 0\] 显示在六个方框上方，每个方框从左到右与向量中的一个数字对齐。方框从左到右包含以下图片：罗宋汤、热狗、沙拉、披萨、[空]、沙威玛。中：热狗的独热编码可视化。向量 \[0, 1, 0, 0, ..., 0\] 显示在六个方框上方。方框中的图片与上方罗宋汤的相同。下：沙威玛的独热编码可视化。向量 \[0, 0, 0, 0, ..., 1\] 显示在六个方框上方。方框中的图片与上方罗宋汤和热狗的相同。](/static/machine-learning/crash-course/embeddings/images/food_images_one_hot_encodings.png) **图 2.** 罗宋汤、热狗和沙威玛的独热编码。每个独热编码向量的长度为 5000（数据集中每个菜单项对应一个条目）。图中的省略号表示未显示的 4995 个条目。

## 稀疏数据表示的缺陷

回顾这些独热编码，你注意到这种数据表示方式存在几个问题。

- **权重数量。** 大型输入向量意味着[**神经网络**](</machine-learning/glossary#neural-network>)需要大量[**权重**](</machine-learning/glossary#weight>)。如果你的独热编码有 M 个条目，输入层之后的第一层有 N 个节点，则该层需要训练 M×N 个权重。
- **数据点数量。** 模型中的权重越多，有效训练所需的数据就越多。
- **计算量。** 权重越多，训练和使用模型所需的计算量越大。很容易超出硬件的能力。
- **内存量。** 模型中的权重越多，训练和提供服务的加速器上所需的内存就越多。高效扩展这一点非常困难。
- **支持端侧机器学习（On-Device Machine Learning, ODML）的难度。** 如果你希望在本地设备上运行 ML 模型（而不是在服务器上提供服务），你需要专注于使模型更小，并减少权重数量。

在本模块中，你将学习如何创建**嵌入**——稀疏数据的低维表示，以解决这些问题。

[帮助中心](<https://support.google.com/machinelearningeducation>)

[ 上一页 arrow_back  自测题（10 分钟）  ](</machine-learning/crash-course/neural-networks/test-your-knowledge>)

[ 下一页 嵌入空间与静态嵌入（10 分钟） arrow_forward  ](</machine-learning/crash-course/embeddings/embedding-space>)

除非另有说明，本页面内容根据 [知识共享署名 4.0 许可证](<https://creativecommons.org/licenses/by/4.0/>) 授权，代码示例根据 [Apache 2.0 许可证](<https://www.apache.org/licenses/LICENSE-2.0>) 授权。详情请参阅 [Google 开发者网站政策](<https://developers.google.com/site-policies>)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新于 2025-08-25 UTC。
