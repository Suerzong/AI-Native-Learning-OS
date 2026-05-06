# 2.2. 数据预处理

到目前为止，我们一直在处理以现成张量形式提供的合成数据。然而，要在实际中应用深度学习，我们必须从以任意格式存储的混乱数据中提取数据，并对其进行预处理以满足我们的需求。幸运的是，_pandas_ [库](https://pandas.pydata.org/) 可以完成大部分繁重的工作。本节虽然不能代替一个合适的 _pandas_ [教程](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)，但会给你一个关于一些最常见操作的速成课程。

## 2.2.1. 读取数据集

逗号分隔值（CSV）文件在存储表格（类似电子表格）数据时无处不在。在其中，每条记录对应一行，由若干个（逗号分隔的）字段组成，例如"Albert Einstein,March 14 1879,Ulm,Federal polytechnic school,field of gravitational physics"。为了演示如何使用 `pandas` 加载 CSV 文件，我们在下面创建了一个 CSV 文件 `../data/house_tiny.csv`。该文件表示一个房屋数据集，其中每行对应一个独立的房屋，各列分别对应房间数（`NumRooms`）、屋顶类型（`RoofType`）和价格（`Price`）。

    import os

    os.makedirs(os.path.join('..', 'data'), exist_ok=True)
    data_file = os.path.join('..', 'data', 'house_tiny.csv')
    with open(data_file, 'w') as f:
        f.write('''NumRooms,RoofType,Price
    NA,NA,127500
    2,NA,106000
    4,Slate,178100
    NA,NA,140000''')

现在让我们导入 `pandas` 并用 `read_csv` 加载数据集。

    import pandas as pd

    data = pd.read_csv(data_file)
    print(data)

       NumRooms RoofType   Price
    0       NaN      NaN  127500
    1       2.0      NaN  106000
    2       4.0    Slate  178100
    3       NaN      NaN  140000

    import pandas as pd

    data = pd.read_csv(data_file)
    print(data)

       NumRooms RoofType   Price
    0       NaN      NaN  127500
    1       2.0      NaN  106000
    2       4.0    Slate  178100
    3       NaN      NaN  140000

    import pandas as pd

    data = pd.read_csv(data_file)
    print(data)

       NumRooms RoofType   Price
    0       NaN      NaN  127500
    1       2.0      NaN  106000
    2       4.0    Slate  178100
    3       NaN      NaN  140000

    import pandas as pd

    data = pd.read_csv(data_file)
    print(data)

       NumRooms RoofType   Price
    0       NaN      NaN  127500
    1       2.0      NaN  106000
    2       4.0    Slate  178100
    3       NaN      NaN  140000

## 2.2.2. 数据准备

在监督学习中，我们训练模型来根据一组_输入_值预测指定的_目标_值。处理数据集的第一步是将对应于输入值和目标值的列分开。我们可以按名称选择列，也可以通过整数位置索引（`iloc`）选择列。

你可能已经注意到，`pandas` 将 CSV 中所有值为 `NA` 的条目替换为特殊的 `NaN`（_非数字_）值。当条目为空时（例如"3,,,270000"）也会发生这种情况。这些被称为_缺失值_（missing values），它们是数据科学中的"臭虫"，是你整个职业生涯中都会遇到的持久威胁。根据上下文，缺失值可以通过_插补_（imputation）或_删除_（deletion）来处理。插补用缺失值的估计值替换它们，而删除则直接丢弃包含缺失值的行或列。

以下是一些常见的插补启发式方法。对于分类输入字段，我们可以将 `NaN` 视为一个类别。由于 `RoofType` 列取值为 `Slate` 和 `NaN`，`pandas` 可以将此列转换为两列 `RoofType_Slate` 和 `RoofType_nan`。屋顶类型为 `Slate` 的行将把 `RoofType_Slate` 和 `RoofType_nan` 的值分别设为 1 和 0。反之亦然，对于 `RoofType` 值缺失的行。

    inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]
    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       NaN           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       NaN           False          True

    inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]
    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       NaN           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       NaN           False          True

    inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]
    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       NaN           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       NaN           False          True

    inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]
    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       NaN           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       NaN           False          True

对于缺失的数值，一种常见的启发式方法是用相应列的均值替换 `NaN` 条目。

    inputs = inputs.fillna(inputs.mean())
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       3.0           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       3.0           False          True

    inputs = inputs.fillna(inputs.mean())
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       3.0           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       3.0           False          True

    inputs = inputs.fillna(inputs.mean())
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       3.0           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       3.0           False          True

    inputs = inputs.fillna(inputs.mean())
    print(inputs)

       NumRooms  RoofType_Slate  RoofType_nan
    0       3.0           False          True
    1       2.0           False          True
    2       4.0            True         False
    3       3.0           False          True

## 2.2.3. 转换为张量格式

现在 `inputs` 和 `targets` 中的所有条目都是数值型的，我们可以将它们加载到张量中（回顾 [第 2.1 节](ndarray.html#sec-ndarray)）。

    import torch

    X = torch.tensor(inputs.to_numpy(dtype=float))
    y = torch.tensor(targets.to_numpy(dtype=float))
    X, y

    (tensor([[3., 0., 1.],
             [2., 0., 1.],
             [4., 1., 0.],
             [3., 0., 1.]], dtype=torch.float64),
     tensor([127500., 106000., 178100., 140000.], dtype=torch.float64))

    from mxnet import np

    X, y = np.array(inputs.to_numpy(dtype=float)), np.array(targets.to_numpy(dtype=float))
    X, y

    [22:09:02] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    (array([[3., 0., 1.],
            [2., 0., 1.],
            [4., 1., 0.],
            [3., 0., 1.]], dtype=float64),
     array([127500., 106000., 178100., 140000.], dtype=float64))

    from jax import numpy as jnp

    X = jnp.array(inputs.to_numpy(dtype=float))
    y = jnp.array(targets.to_numpy(dtype=float))
    X, y

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    (Array([[3., 0., 1.],
            [2., 0., 1.],
            [4., 1., 0.],
            [3., 0., 1.]], dtype=float32),
     Array([127500., 106000., 178100., 140000.], dtype=float32))

    import tensorflow as tf

    X = tf.constant(inputs.to_numpy(dtype=float))
    y = tf.constant(targets.to_numpy(dtype=float))
    X, y

    (<tf.Tensor: shape=(4, 3), dtype=float64, numpy=
     array([[3., 0., 1.],
            [2., 0., 1.],
            [4., 1., 0.],
            [3., 0., 1.]])>,
     <tf.Tensor: shape=(4,), dtype=float64, numpy=array([127500., 106000., 178100., 140000.])>)

## 2.2.4. 讨论

你现在知道了如何划分数据列、插补缺失变量以及将 `pandas` 数据加载到张量中。在 [第 5.7 节](../chapter_multilayer-perceptrons/kaggle-house-price.html#sec-kaggle-house)中，你将学到更多的数据处理技能。虽然本节速成课程保持了简洁，但数据处理可能会变得复杂。例如，我们的数据集可能不是来自单个 CSV 文件，而是分散在从关系数据库中提取的多个文件中。例如，在电子商务应用中，客户地址可能存储在一个表中，而购买数据存储在另一个表中。此外，从业者面临的数据类型远不止分类和数值，例如文本字符串、图像、音频数据和点云。通常需要高级工具和高效算法来防止数据处理成为机器学习流水线中最大的瓶颈。这些问题在我们进入计算机视觉和自然语言处理时将会出现。最后，我们必须关注数据质量。现实世界的数据集常常受到异常值、传感器故障测量和记录错误的困扰，在将数据输入任何模型之前必须解决这些问题。数据可视化工具如 [seaborn](https://seaborn.pydata.org/)、[Bokeh](https://docs.bokeh.org/) 或 [matplotlib](https://matplotlib.org/) 可以帮助你手动检查数据并建立关于你可能需要解决的问题类型的直觉。

## 2.2.5. 练习

  1. 尝试加载数据集，例如来自 [UCI 机器学习库](https://archive.ics.uci.edu/ml/datasets.php) 的鲍鱼数据集，并检查其属性。其中有多少比例有缺失值？变量中有多大比例是数值型、分类型或文本型的？

  2. 尝试按名称而非列号索引和选择数据列。pandas 文档中的 [索引](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) 部分有更多详细信息。

  3. 你认为用这种方式可以加载多大的数据集？可能存在哪些限制？提示：考虑读取数据的时间、表示、处理和内存占用。在你的笔记本电脑上试试看。如果在服务器上尝试会怎样？

  4. 你将如何处理具有大量类别的数据？如果类别标签都是唯一的呢？你应该包含后者吗？

  5. 你能想到 pandas 的哪些替代方案？比如 [从文件加载 NumPy 张量](https://numpy.org/doc/stable/reference/generated/numpy.load.html)？查看 [Pillow](https://python-pillow.org/)，Python 图像处理库。

[Discussions](https://discuss.d2l.ai/t/29)

[Discussions](https://discuss.d2l.ai/t/28)

[Discussions](https://discuss.d2l.ai/t/17967)

[Discussions](https://discuss.d2l.ai/t/195)

目录

  * 2.2. 数据预处理
    * 2.2.1. 读取数据集
    * 2.2.2. 数据准备
    * 2.2.3. 转换为张量格式
    * 2.2.4. 讨论
    * 2.2.5. 练习
