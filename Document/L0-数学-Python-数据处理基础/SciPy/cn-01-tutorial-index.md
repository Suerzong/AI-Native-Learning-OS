[跳过主要内容](#main-content)

__返回顶部 __ `Ctrl`+`K`

[ ![](../_static/logo.svg) ![](../_static/logo.svg) SciPy ](../index.html)

  * [ 安装 ](https://scipy.org/install/)
  * [ 用户指南 ](#)
  * [ API 参考 ](../reference/index.html)
  * [ 从源码构建 ](../building/index.html)
  * [ 开发 ](../dev/index.html)
  * [ 发布说明 ](../release.html)

选择版本

______

  * [__ GitHub](https://github.com/scipy/scipy "GitHub")
  * [__ Scientific Python 论坛](https://discuss.scientific-python.org/c/contributor/scipy/ "Scientific Python 论坛")

  * [ 安装 ](https://scipy.org/install/)
  * [ 用户指南 ](#)
  * [ API 参考 ](../reference/index.html)
  * [ 从源码构建 ](../building/index.html)
  * [ 开发 ](../dev/index.html)
  * [ 发布说明 ](../release.html)

选择版本

______

  * [__ GitHub](https://github.com/scipy/scipy "GitHub")
  * [__ Scientific Python 论坛](https://discuss.scientific-python.org/c/contributor/scipy/ "Scientific Python 论坛")

__ 搜索 `Ctrl`+`K`

章节导航

用户指南

  * [傅里叶变换 (`scipy.fft`)](fft.html)
  * [积分 (`scipy.integrate`)](integrate.html)
  * [插值 (`scipy.interpolate`)](interpolate.html)
  * [文件 IO (`scipy.io`)](io.html)
  * [线性代数 (`scipy.linalg`)](linalg.html)
  * [多维图像处理 (`scipy.ndimage`)](ndimage.html)
  * [优化 (`scipy.optimize`)](optimize.html)
  * [信号处理 (`scipy.signal`)](signal.html)
  * [稀疏数组 (`scipy.sparse`)](sparse.html)
  * [空间数据结构与算法 (`scipy.spatial`)](spatial.html)
  * [特殊函数 (`scipy.special`)](special.html)
  * [统计 (`scipy.stats`)](stats.html)
  * [使用 ARPACK 的稀疏特征值问题](arpack.html)
  * [压缩稀疏图例程 (`scipy.sparse.csgraph`)](csgraph.html)
  * [SciPy 中的并行执行支持](parallel_execution.html)
  * [SciPy 中的线程安全性](thread_safety.html)

  * [ __](../index.html)
  * SciPy 用户指南

# SciPy 用户指南[#](#scipy-user-guide "链接到此标题")

SciPy 是建立在 [NumPy](https://numpy.org) 之上的数学算法和便捷函数的集合。它通过提供用于操作和可视化数据的高级命令和类，为 Python 增添了强大的功能。

## 子包与用户指南[#](#subpackages-and-user-guides "链接到此标题")

SciPy 按照不同的科学计算领域组织为若干子包。下表对这些子包进行了汇总，并在"描述与用户指南"列中提供了用户指南的链接（如果可用）：

子包 | 描述与用户指南
---|---
`cluster` | 聚类算法
`constants` | 物理与数学常数
`differentiate` | 有限差分微分工具
`fft` | [傅里叶变换 (scipy.fft)](fft.html)
`fftpack` | 快速傅里叶变换例程（旧版）
`integrate` | [积分 (scipy.integrate)](integrate.html)
`interpolate` | [插值 (scipy.interpolate)](interpolate.html)
`io` | [文件 IO (scipy.io)](io.html)
`linalg` | [线性代数 (scipy.linalg)](linalg.html)
`ndimage` | [多维图像处理 (scipy.ndimage)](ndimage.html)
`odr` | 正交距离回归
`optimize` | [优化 (scipy.optimize)](optimize.html)
`signal` | [信号处理 (scipy.signal)](signal.html)
`sparse` | [稀疏数组 (scipy.sparse)](sparse.html)
`spatial` | [空间数据结构与算法 (scipy.spatial)](spatial.html)
`special` | [特殊函数 (scipy.special)](special.html)
`stats` | [统计 (scipy.stats)](stats.html)

还有一些额外的用户指南涵盖以下主题：

  * [使用 ARPACK 的稀疏特征值问题](arpack.html) - 使用迭代方法的特征值问题求解器

  * [压缩稀疏图例程 (scipy.sparse.csgraph)](csgraph.html) - 压缩稀疏图例程

关于组织和导入 SciPy 子包函数的指导，请参阅[从 SciPy 导入函数的指南](https://scipy.github.io/devdocs/reference/index.html#guidelines-for-importing-functions-from-scipy)。

有关并行执行支持和线程安全性的信息，请参阅[SciPy 中的并行执行支持](parallel_execution.html#scipy-parallel-execution)和[SciPy 中的线程安全性](thread_safety.html#scipy-thread-safety)。

[ __ 上一页 SciPy 文档 ](../index.html "上一页") [ 下一页 傅里叶变换 (`scipy.fft`) __](fft.html "下一页")

__本页内容

  * [子包与用户指南](#subpackages-and-user-guides)

版权所有 2008，The SciPy 社区。

使用 [Sphinx](https://www.sphinx-doc.org/) 8.1.3 创建。

使用 [PyData Sphinx 主题](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1 构建。
