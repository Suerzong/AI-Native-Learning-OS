[跳过主要内容](#main-content)

__返回顶部 __ `Ctrl`+`K`

[ ![](../_static/logo.svg) ![](../_static/logo.svg) SciPy ](../index.html)

  * [ 安装 ](https://scipy.org/install/)
  * [ 用户指南 ](index.html)
  * [ API 参考 ](../reference/index.html)
  * [ 从源码构建 ](../building/index.html)
  * [ 开发 ](../dev/index.html)
  * [ 发布说明 ](../release.html)

选择版本

______

  * [__ GitHub](https://github.com/scipy/scipy "GitHub")
  * [__ Scientific Python 论坛](https://discuss.scientific-python.org/c/contributor/scipy/ "Scientific Python 论坛")

  * [ 安装 ](https://scipy.org/install/)
  * [ 用户指南 ](index.html)
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
  * [统计 (`scipy.stats`)](#)
  * [使用 ARPACK 的稀疏特征值问题](arpack.html)
  * [压缩稀疏图例程 (`scipy.sparse.csgraph`)](csgraph.html)
  * [SciPy 中的并行执行支持](parallel_execution.html)
  * [SciPy 中的线程安全性](thread_safety.html)

  * [ __](../index.html)
  * [SciPy 用户指南](index.html)
  * 统计 (`scipy.stats`)

# 统计 ([`scipy.stats`](../reference/stats.html#module-scipy.stats "scipy.stats"))[#](#statistics-scipy-stats "链接到此标题")

在本教程中，我们将讨论 `scipy.stats` 的许多（但绝非全部）特性。本文旨在为用户提供该包的实用知识。更多细节请参考[参考手册](../reference/stats.html#statsrefmanual)。

注意：本文档仍在编写中。

目录

  * [概率分布](stats/probability_distributions.html)
    * [连续统计分布](stats/continuous.html)
    * [离散统计分布](stats/discrete.html)
    * [获取帮助](stats/probability_distributions.html#getting-help)
    * [常用方法](stats/probability_distributions.html#common-methods)
    * [随机数生成](stats/probability_distributions.html#random-number-generation)
    * [平移与缩放](stats/probability_distributions.html#shifting-and-scaling)
    * [形状参数](stats/probability_distributions.html#shape-parameters)
    * [冻结分布](stats/probability_distributions.html#freezing-a-distribution)
    * [广播](stats/probability_distributions.html#broadcasting)
    * [离散分布的具体要点](stats/probability_distributions.html#specific-points-for-discrete-distributions)
    * [拟合分布](stats/probability_distributions.html#fitting-distributions)
    * [性能问题与注意事项](stats/probability_distributions.html#performance-issues-and-cautionary-remarks)
    * [遗留问题](stats/probability_distributions.html#remaining-issues)
    * [构建特定分布](stats/probability_distributions.html#building-specific-distributions)
  * [随机变量转换指南](stats/rv_infrastructure.html)
    * [背景](stats/rv_infrastructure.html#background)
    * [基础](stats/rv_infrastructure.html#basics)
    * [新增与高级特性](stats/rv_infrastructure.html#new-and-advanced-features)
    * [结论](stats/rv_infrastructure.html#conclusion)
  * [SciPy 中的通用非均匀随机数采样](stats/sampling.html)
    * [简介](stats/sampling.html#introduction)
    * [接口的基本概念](stats/sampling.html#basic-concepts-of-the-interface)
    * [`scipy.stats.sampling` 中的生成器](stats/sampling.html#generators-in-scipy-stats-sampling)
    * [参考文献](stats/sampling.html#references)
  * [核密度估计](stats/kernel_density_estimation.html)
    * [单变量估计](stats/kernel_density_estimation.html#univariate-estimation)
    * [多变量估计](stats/kernel_density_estimation.html#multivariate-estimation)
  * [多尺度图相关 (MGC)](stats/multiscale_graphcorr.html)
  * [拟蒙特卡罗](stats/quasi_monte_carlo.html)
    * [计算偏差](stats/quasi_monte_carlo.html#calculate-the-discrepancy)
    * [使用 QMC 引擎](stats/quasi_monte_carlo.html#using-a-qmc-engine)
    * [制作 QMC 引擎，即子类化 `QMCEngine`](stats/quasi_monte_carlo.html#making-a-qmc-engine-i-e-subclassing-qmcengine)
    * [QMC 使用指南](stats/quasi_monte_carlo.html#guidelines-on-using-qmc)
  * [修剪与缩尾处理转换指南](stats/outliers.html)
    * [动机](stats/outliers.html#motivation)
    * [识别阈值](stats/outliers.html#identifying-the-threshold)
    * [修剪与缩尾](stats/outliers.html#trimming-and-winsorizing)
    * [计算统计量](stats/outliers.html#computing-the-statistic)
    * [方案](stats/outliers.html#recipes)

样本统计量与假设检验

  * [分析单个样本](stats/analysing_one_sample.html)
    * [描述性统计](stats/analysing_one_sample.html#descriptive-statistics)
    * [T 检验与 KS 检验](stats/analysing_one_sample.html#t-test-and-ks-test)
    * [分布尾部](stats/analysing_one_sample.html#tails-of-the-distribution)
    * [正态分布的特殊检验](stats/analysing_one_sample.html#special-tests-for-normal-distributions)
  * [比较两个样本](stats/comparing_two_samples.html)
    * [比较均值](stats/comparing_two_samples.html#comparing-means)
    * [两个样本的 Kolmogorov-Smirnov 检验 ks_2samp](stats/comparing_two_samples.html#kolmogorov-smirnov-test-for-two-samples-ks-2samp)
  * [重采样与蒙特卡罗方法](stats/resampling.html)
    * [简介](stats/resampling.html#introduction)
    * [重采样与蒙特卡罗方法教程](stats/resampling.html#resampling-and-monte-carlo-methods-tutorials)
  * [假设检验](stats/hypothesis_tests.html)
    * [Bartlett 方差齐性检验](stats/hypothesis_bartlett.html)
    * [卡方检验](stats/hypothesis_chisquare.html)
    * [列联表中变量独立性的卡方检验](stats/hypothesis_chi2_contingency.html)
    * [Dunnett 检验](stats/hypothesis_dunnett.html)
    * [Fisher 精确检验](stats/hypothesis_fisher_exact.html)
    * [Fligner-Killeen 方差齐性检验](stats/hypothesis_fligner.html)
    * [重复样本的 Friedman 检验](stats/hypothesis_friedmanchisquare.html)
    * [Jarque-Bera 拟合优度检验](stats/hypothesis_jarque_bera.html)
    * [Kendall's tau 检验](stats/hypothesis_kendalltau.html)
    * [峰度检验](stats/hypothesis_kurtosistest.html)
    * [Levene 方差齐性检验](stats/hypothesis_levene.html)
    * [正态性检验](stats/hypothesis_normaltest.html)
    * [列联表的优势比](stats/hypothesis_odds_ratio.html)
    * [Pearson 相关系数](stats/hypothesis_pearsonr.html)
    * [Shapiro-Wilk 正态性检验](stats/hypothesis_shapiro.html)
    * [偏度检验](stats/hypothesis_skewtest.html)
    * [Spearman 相关系数](stats/hypothesis_spearmanr.html)

[ __ 上一页 特殊函数 (`scipy.special`) ](special.html "上一页") [ 下一页 概率分布 __](stats/probability_distributions.html "下一页")

版权所有 2008，The SciPy 社区。

使用 [Sphinx](https://www.sphinx-doc.org/) 8.1.3 创建。

使用 [PyData Sphinx 主题](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1 构建。
