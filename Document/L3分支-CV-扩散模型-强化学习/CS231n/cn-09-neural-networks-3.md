目录：

  * 梯度检验
  * 合理性检查
  * 监控学习过程
    * 损失函数
    * 训练/验证准确率
    * 权重:更新比率
    * 每层激活/梯度分布
    * 可视化
  * 参数更新
    * 一阶（SGD）、动量、Nesterov 动量
    * 学习率退火
    * 二阶方法
    * 每参数自适应学习率（Adagrad、RMSProp）
  * 超参数优化
  * 评估
    * 模型集成
  * 总结
  * 参考资料

## 学习

在前面的章节中，我们讨论了神经网络的静态部分：如何设置网络连接、数据和损失函数。本节致力于动态部分，即学习参数和寻找良好超参数的过程。

### 梯度检验

在理论上，执行梯度检验就是将解析梯度与数值梯度进行比较。在实践中，这个过程要复杂得多且容易出错。

**使用中心公式。** 使用中心差分公式：\\(\frac{df(x)}{dx} = \frac{f(x + h) - f(x - h)}{2h}\\)，其误差为 \\(O(h^2)\\)（二阶近似）。

**使用相对误差进行比较。** 比较数值梯度 \\(f'_n\\) 和解析梯度 \\(f'_a\\) 时，使用相对误差：

\\[\frac{\mid f'_a - f'_n \mid}{\max(\mid f'_a \mid, \mid f'_n \mid)}\\]

实际标准：
  * 相对误差 > 1e-2 通常意味着梯度可能错误
  * 1e-2 > 相对误差 > 1e-4 应让你感到不安
  * 1e-4 > 相对误差 对有折点的目标通常可以
  * 1e-7 及以下应该满意

**使用双精度。** 使用单精度浮点可能导致高相对误差。

**注意目标中的折点。** 折点指目标函数的不可微部分，由 ReLU（\\(max(0,x)\\)）、SVM 损失等引入。

**只使用少量数据点。** 包含折点的损失函数（如 ReLU）使用更少的数据点时折点更少。

**小心步长 h。** 并非越小越好，因为 h 太小可能导致数值精度问题。

**在「特征性」操作模式下进行梯度检验。** 最好使用短暂的「预热」时间，让网络学习，然后在损失开始下降后执行梯度检验。

**不要让正则化压倒数据。** 首先关闭正则化，单独检查数据损失，然后独立检查正则化项。

**记住关闭 dropout/数据增强。** 执行梯度检验时，关闭网络中的任何非确定性效果。

**只检查少数维度。** 梯度可能有数百万参数大小，实际中只能检查部分维度。

### 学习前的合理性检查

  * **在随机性能下检查正确损失。** 确保初始化小参数时获得预期损失。例如 CIFAR-10 上 Softmax 分类器初始损失应为 2.302（-ln(0.1)）。
  * **过拟合一小部分数据。** 最重要的是，在完整数据集上训练前，尝试在很小部分数据（例如 20 个样本）上训练并确保能达到零代价。

### 监控学习过程

#### 损失函数

训练期间跟踪的第一个有用量是损失。

![](/assets/nn3/learningrates.jpeg) ![](/assets/nn3/loss.jpeg)

损失的「抖动」量与批量大小相关。

#### 训练/验证准确率

![](/assets/nn3/accuracies.jpeg)

训练和验证准确率之间的差距指示过拟合程度。

#### 权重:更新比率

你可能想跟踪的是更新幅度与值幅度的比率。粗略启发式是此比率应在 1e-3 左右。

#### 每层激活/梯度分布

不正确的初始化可能减慢甚至完全停止学习过程。绘制所有层的激活/梯度直方图有助于诊断。

#### 第一层可视化

![](/assets/nn3/weights.jpeg) ![](/assets/nn3/cnnweights.jpg)

### 参数更新

#### SGD 及其改进

**原始更新：** `x += - learning_rate * dx`

**动量更新：**
    v = mu * v - learning_rate * dx
    x += v

动量参数通常设为 [0.5, 0.9, 0.95, 0.99]。

**Nesterov 动量：** 在「前瞻」位置计算梯度。

![](/assets/nn3/nesterov.jpeg)

#### 学习率退火

  * **阶梯退火：** 每隔几个 epoch 将学习率降低一定因子
  * **指数退火：** \\(\alpha = \alpha_0 e^{-k t}\\)
  * **1/t 退火：** \\(\alpha = \alpha_0 / (1 + k t )\\)

#### 二阶方法

基于[牛顿法](http://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)：\\(x \leftarrow x - [H f(x)]^{-1} \nabla f(x)\\)

海森矩阵计算和求逆代价高昂，L-BFGS 是最流行的近似方法。

#### 每参数自适应学习率方法

**Adagrad：**
    cache += dx**2
    x += - learning_rate * dx / (np.sqrt(cache) + eps)

**RMSprop：**
    cache = decay_rate * cache + (1 - decay_rate) * dx**2
    x += - learning_rate * dx / (np.sqrt(cache) + eps)

**Adam：**
    m = beta1*m + (1-beta1)*dx
    v = beta2*v + (1-beta2)*(dx**2)
    x += - learning_rate * m / (np.sqrt(v) + eps)

![](/assets/nn3/opt2.gif) ![](/assets/nn3/opt1.gif)

### 超参数优化

  * 在对数尺度上搜索超参数
  * 随机搜索优于网格搜索
  * 从粗到细分阶段搜索

![](/assets/nn3/gridsearchbad.jpeg)

### 模型集成

  * **相同模型，不同初始化**
  * **交叉验证中发现的顶级模型**
  * **单一模型的不同检查点**
  * **训练期间参数的运行平均值**

集成的一个缺点是测试时评估时间更长。

## 总结

训练神经网络：
  * 用小批量数据进行梯度检验
  * 作为合理性检查，确保初始损失合理
  * 训练期间监控损失、训练/验证准确率
  * 推荐使用 SGD+Nesterov 动量 或 Adam
  * 在训练期间退火学习率
  * 使用随机搜索寻找好的超参数
  * 形成模型集成以获得额外性能

## 参考资料

  * [SGD](http://research.microsoft.com/pubs/192769/tricks-2012.pdf) 技巧（Leon Bottou）
  * [Efficient BackProp](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)（Yann LeCun）
  * [Practical Recommendations for Gradient-Based Training of Deep Architectures](http://arxiv.org/pdf/1206.5533v2.pdf)（Yoshua Bengio）
