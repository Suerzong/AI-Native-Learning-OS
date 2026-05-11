# 19类遥感图像识别

本实验采用mobilenet V2的预训练网络。图像resize到 224 X 224。

19类图像，训练集样本总数为904个，验证集样本总数为101个，
10个epoch即可使模型准确率在验证集合上达到98%以上。

模型训练建议使用GPU环境。

可扫码注册使用九章云极（Lab4AI）的H800A(显存80G)免费算力。

<img src="../lab4ai_qr.png" width="200" alt="扫描注册" />

或[点击注册](https://www.lab4ai.cn/register?promoteID=user-rJUY2H2epR)，即可送30元代金券，从而可用其购买算力使用。

![lab4ai](../lab4ai1.png)

![H800A](../lab4ai2.png)


## 数据集准备

数据集下载地址为：

https://aistudio.baidu.com/datasetdetail/51733

数据集下载后，解压缩到dataset目录中，该目录中，每个类别的名称为一个子目录。如：

```
dataset
    |-------Airport
    |-------Beach
    |-------Bridge
    |-------Commercial
    |-------Desert
    |-------..... 
``` 
 
## 实战环境准备

本实验需要pytorch深度学习开发框架，因此需要提先安装。

## 运行代码

直接使用jupyter notebook。

### split.ipynb文件

该文件可以不用执行。其功能是对总的数据集进行拆分，得到训练集、验证集和测试集。
代码中可进行调整比例。当前代码比例为：9:1:0

执行完毕后，会得到各个数据集的文件列表（sattrain.txt、satval.txt、sattest.txt），以及各个类别名称与id的对应。
这些文件已经在该目录中存在，故split.ipynb文件可不必执行。

### train&test.ipynb文件 

该文件包含了训练和测试等功能。训练完成，会生成sat_mobilenet.pt模型文件。

代码中，类别名称和id对应的词典，是split.ipynb文件执行的结果。

若前面重新执行split.ipynb，则对应关系可能变更，需要重新复制到 train&test.ipynb文件，替换原来的original_dict。

该仓库中已经包含了训练得到的sat_mobilenet.pt模型文件，可直接加载后进行模型推理。

## 如何下载？

整个代码仓库下载，可点击本页面右上角的"克隆/下载"，在新打开的页面中点击右上角的"下载 Zip"。

下载到本地后展开压缩包，选择进入到相应目录下，然后运行即可。

自己试一试吧，有任何问题，可在页面中的issues进行提问。请点击页面右上角的star，谢谢。