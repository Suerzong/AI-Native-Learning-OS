目录：

  * 生成数据
  * 训练 Softmax 线性分类器
    * 初始化参数
    * 计算类别得分
    * 计算损失
    * 使用反向传播计算解析梯度
    * 执行参数更新
    * 整合：训练 Softmax 分类器
  * 训练神经网络
  * 总结

在本节中，我们将用一个 2 维玩具数据集完成一个完整的神经网络实现。

## 生成数据

生成一个不易线性分离的分类数据集——螺旋数据集：


    N = 100 # 每类点数
    D = 2 # 维度
    K = 3 # 类别数
    X = np.zeros((N*K,D))
    y = np.zeros(N*K, dtype='uint8')
    for j in range(K):
      ix = range(N*j,N*(j+1))
      r = np.linspace(0.0,1,N)
      t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.2
      X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
      y[ix] = j
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
    plt.show()


![](/assets/eg/spiral_raw.png)

三个类别（蓝、红、黄）的玩具螺旋数据，不是线性可分的。

## 训练 Softmax 线性分类器

### 初始化参数

    W = 0.01 * np.random.randn(D,K)
    b = np.zeros((1,K))

### 计算类别得分

    scores = np.dot(X, W) + b

### 计算损失

Softmax 分类器损失：\\(L_i = -\log\left(\frac{e^{f_{y_i}}}{ \sum_j e^{f_j} }\right)\\)


    num_examples = X.shape[0]
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    correct_logprobs = -np.log(probs[range(num_examples),y])
    data_loss = np.sum(correct_logprobs)/num_examples
    reg_loss = 0.5*reg*np.sum(W*W)
    loss = data_loss + reg_loss

### 使用反向传播计算解析梯度

梯度推导结果非常简洁：\\(\frac{\partial L_i }{ \partial f_k } = p_k - \mathbb{1}(y_i = k)\\)


    dscores = probs
    dscores[range(num_examples),y] -= 1
    dscores /= num_examples

    dW = np.dot(X.T, dscores)
    db = np.sum(dscores, axis=0, keepdims=True)
    dW += reg*W

### 执行参数更新

    W += -step_size * dW
    b += -step_size * db

### 整合：训练 Softmax 分类器


    W = 0.01 * np.random.randn(D,K)
    b = np.zeros((1,K))
    step_size = 1e-0
    reg = 1e-3
    num_examples = X.shape[0]
    for i in range(200):
      scores = np.dot(X, W) + b
      exp_scores = np.exp(scores)
      probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
      correct_logprobs = -np.log(probs[range(num_examples),y])
      data_loss = np.sum(correct_logprobs)/num_examples
      reg_loss = 0.5*reg*np.sum(W*W)
      loss = data_loss + reg_loss
      if i % 10 == 0:
        print "iteration %d: loss %f" % (i, loss)
      dscores = probs
      dscores[range(num_examples),y] -= 1
      dscores /= num_examples
      dW = np.dot(X.T, dscores)
      db = np.sum(dscores, axis=0, keepdims=True)
      dW += reg*W
      W += -step_size * dW
      b += -step_size * db


训练准确率 **49%**。线性分类器无法学习螺旋数据集。

![](/assets/eg/spiral_linear.png)

## 训练神经网络

添加一个隐藏层：


    h = 100 # 隐藏层大小
    W = 0.01 * np.random.randn(D,h)
    b = np.zeros((1,h))
    W2 = 0.01 * np.random.randn(h,K)
    b2 = np.zeros((1,K))


前向传播变化：


    hidden_layer = np.maximum(0, np.dot(X, W) + b) # ReLU 激活
    scores = np.dot(hidden_layer, W2) + b2


反向传播：


    dW2 = np.dot(hidden_layer.T, dscores)
    db2 = np.sum(dscores, axis=0, keepdims=True)
    dhidden = np.dot(dscores, W2.T)
    dhidden[hidden_layer <= 0] = 0 # ReLU 反向传播
    dW = np.dot(X.T, dhidden)
    db = np.sum(dhidden, axis=0, keepdims=True)


完整训练循环收敛到 **98%** 准确率！

![](/assets/eg/spiral_net.png)

神经网络分类器碾压螺旋数据集。

## 总结

我们使用了一个 2D 玩具数据集，训练了线性网络和 2 层神经网络。从线性分类器到神经网络的转变只需要很少的代码修改：得分函数形式变化（1 行代码差异），反向传播形式变化（需要多执行一轮反向传播通过隐藏层到第一层）。
