今年推荐通过 [Google Colaboratory](https://colab.research.google.com/) 完成作业。不过，如果你已有 GPU 硬件设备并希望在本地工作，我们也提供了虚拟环境配置指南。

  * 在 Google Colaboratory 上远程工作
  * 在本地机器上工作
    * Anaconda 虚拟环境
    * Python venv
    * 安装依赖包

### 在 Google Colaboratory 上远程工作

Google Colaboratory 本质上是 Jupyter Notebook 和 Google Drive 的结合体。它完全在云端运行，预装了许多常用库（如 PyTorch 和 TensorFlow），因此每个人都可以使用相同的依赖环境。更棒的是，Colab 提供免费的硬件加速器（如 K80、P100 GPU 和 TPU），这对作业 2 和 3 尤其有用。

**使用要求**。使用 Colab 需要拥有一个关联 Google Drive 的 Google 账号。如果你已有账号，可按以下步骤将 Colab 连接到你的 Drive：

  1. 点击右上角齿轮图标，选择「设置」。
  2. 点击「管理应用」标签。
  3. 在顶部选择「连接更多应用」，将弹出「GSuite Marketplace」窗口。
  4. 搜索 **Colab**，然后点击「添加」。

**工作流程**。每次作业都提供一个 zip 文件的下载链接，其中包含 Colab 笔记本和 Python 起始代码。你可以将文件夹上传到 Drive，用 Colab 打开笔记本进行工作，然后将进度保存回 Drive。我们建议你观看下方教程视频，它以作业 1 为例演示了推荐的工作流程。

**最佳实践**。使用 Colab 时需注意以下几点。首先，资源并非保证可用（这是免费使用的代价）。如果你空闲一段时间或总连接时间超过上限（约 12 小时），Colab 虚拟机将断开连接，这意味着未保存的进度将丢失。**因此，请养成在作业过程中频繁保存代码的习惯。** 要了解更多 Colab 资源限制，请阅读其 [FAQ](https://research.google.com/colaboratory/faq.html)。

**使用 GPU**。使用 GPU 只需在 Colab 中切换运行时类型。具体操作：点击「运行时 -> 更改运行时类型 -> 硬件加速器 -> GPU」，你的 Colab 实例将自动获得 GPU 计算支持。

如果你想了解更多关于 Colab 的信息，建议访问以下资源：

  * [Google Colab 入门](https://www.youtube.com/watch?v=inN8seMm7UI)
  * [欢迎使用 Colab](https://colab.research.google.com/notebooks/intro.ipynb)
  * [Colab 功能概览](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)

### 在本地机器上工作

如果你希望在本地工作，应使用虚拟环境。可通过 Anaconda（推荐）或 Python 原生的 `venv` 模块安装。请确保使用 Python 3.7，因为**我们不再支持 Python 2**。

#### Anaconda 虚拟环境

我们强烈推荐使用免费的 [Anaconda Python 发行版](https://www.anaconda.com/download/)，它提供了一种便捷的方式来管理包依赖。请务必下载 Python 3 版本（当前安装 Python 3.7）。Anaconda 的优点在于它默认自带 [MKL 优化](https://docs.anaconda.com/mkl-optimizations/)，这意味着你的 `numpy` 和 `scipy` 代码无需修改即可获得显著的速度提升。

安装 Anaconda 后，建议为本课程创建一个虚拟环境。如果你选择不使用虚拟环境（强烈不推荐！），你需要自行确保所有依赖都在全局环境中安装。要创建名为 `cs231n` 的虚拟环境，在终端运行：


    # 这将在 'path/to/anaconda3/envs/' 下
    # 创建一个名为 cs231n 的 anaconda 环境
    conda create -n cs231n python=3.7


激活并进入环境，运行 `conda activate cs231n`。退出环境，运行 `conda deactivate cs231n` 或关闭终端。注意，每次做作业时都需要重新运行 `conda activate cs231n`。


    # 激活后检查 python 路径
    # 是否与 anaconda 环境匹配
    which python
    # 例如，在我的机器上输出
    # $ '/Users/kevin/anaconda3/envs/sci/bin/python'


你可以参考[此页面](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)获取关于使用 Anaconda 管理虚拟环境的更详细说明。

**注意：** 如果你选择了 Anaconda 方案，可以跳过下一节，直接前往「安装依赖包」部分。

#### Python venv

自 Python 3.3 起，Python 原生自带一个轻量级虚拟环境模块 [venv](https://docs.python.org/3/library/venv.html)。每个虚拟环境都包含独立的 Python 包集合，与系统级 Python 包隔离，并使用创建时对应的 Python 版本。要创建名为 `cs231n` 的虚拟环境，在终端运行：


    # 这将在你的主目录下
    # 创建一个名为 cs231n 的虚拟环境
    python3.7 -m venv ~/cs231n


激活并进入环境，运行 `source ~/cs231n/bin/activate`。退出环境，运行 `deactivate` 或关闭终端。注意，每次做作业时都需要重新运行 `source ~/cs231n/bin/activate`。


    # 激活后检查 python 路径
    # 是否与虚拟环境匹配
    which python
    # 例如，在我的机器上输出
    # $ '/Users/kevin/cs231n/bin/python'


#### 安装依赖包

**设置**并**激活**虚拟环境后（通过 `conda` 或 `venv`），你需要使用 `pip` 安装运行作业所需的库。运行：


    # 再次确保虚拟环境（conda 或 venv）
    # 已在运行以下命令前激活
    cd assignment1  # 进入作业目录

    # 安装作业依赖
    # 由于虚拟环境已激活，
    # 此 pip 关联的是
    # 环境的 python 二进制文件
    pip install -r requirements.txt
