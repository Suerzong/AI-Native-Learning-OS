# 计算机视觉迁移学习教程

**作者：** [Sasank Chilamkurthy](https://chsasank.github.io)

在本教程中，你将学习如何使用迁移学习训练卷积神经网络进行图像分类。你可以在 [cs231n 笔记](https://cs231n.github.io/transfer-learning/)中阅读更多关于迁移学习的内容。

引用这些笔记：

> 在实践中，很少有人从头训练整个卷积网络（使用随机初始化），因为拥有足够大的数据集相对罕见。相反，通常在一个非常大的数据集（例如 ImageNet，包含 120 万张图像和 1000 个类别）上预训练卷积网络，然后将卷积网络用作感兴趣任务的初始化或固定特征提取器。

这两种主要的迁移学习场景如下：

  * **微调卷积网络：** 不使用随机初始化，而是使用预训练网络（如在 ImageNet 1000 数据集上训练的网络）初始化网络。其余的训练看起来像往常一样。
  * **卷积网络作为固定特征提取器：** 在这里，我们将冻结除最终全连接层之外的所有网络权重。最后一个全连接层被替换为一个具有随机权重的新层，并且只训练这一层。

## 加载数据

我们将使用 torchvision 和 torch.utils.data 包来加载数据。

今天我们要解决的问题是训练一个模型来分类**蚂蚁**和**蜜蜂**。我们有大约 120 张蚂蚁和蜜蜂的训练图像。每个类别有 75 张验证图像。通常，如果从头训练，这是一个非常小的数据集，难以泛化。由于我们使用迁移学习，我们应该能够合理地泛化。

这个数据集是 ImageNet 的一个非常小的子集。

> 从[此处](https://download.pytorch.org/tutorial/hymenoptera_data.zip)下载数据并解压到当前目录。

### 可视化一些图像

让我们可视化一些训练图像以理解数据增强。

    def imshow(inp, title=None):
        inp = inp.numpy().transpose((1, 2, 0))
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        inp = std * inp + mean
        inp = np.clip(inp, 0, 1)
        plt.imshow(inp)
        if title is not None:
            plt.title(title)
        plt.pause(0.001)

## 训练模型

现在，让我们编写一个通用函数来训练模型。这里我们将说明：

  * 学习率调度
  * 保存最佳模型

### 可视化模型预测

显示一些图像预测的通用函数

## 微调卷积网络

加载预训练模型并重置最终全连接层。

    model_ft = models.resnet18(weights='IMAGENET1K_V1')
    num_ftrs = model_ft.fc.in_features
    model_ft.fc = nn.Linear(num_ftrs, 2)

    model_ft = model_ft.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)

    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)

### 训练和评估

在 CPU 上大约需要 15-25 分钟。在 GPU 上，不到一分钟。

### 训练结果

    训练在 0m 36s 内完成
    最佳验证准确率: 0.960784

## 卷积网络作为固定特征提取器

在这里，我们需要冻结除最后一层之外的所有网络。我们需要设置 `requires_grad = False` 来冻结参数，以便在 `backward()` 中不计算梯度。

### 训练和评估

在 CPU 上，这大约需要之前场景的一半时间。这是因为不需要为大部分网络计算梯度。但是，仍然需要计算前向传播。

    训练在 0m 27s 内完成
    最佳验证准确率: 0.954248

## 在自定义图像上推理

使用训练好的模型对自定义图像进行预测，并将预测的类别标签与图像一起可视化。

## 进一步学习

如果你想了解更多关于迁移学习的应用，请查看我们的[量化迁移学习计算机视觉教程](https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html)。
