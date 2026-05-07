[跳过主要内容](#main-content)

__返回顶部 __ `Ctrl`+`K`

[ ![NumPy v2.4 手册 - 首页](../../_static/numpylogo.svg) ![NumPy v2.4 手册 - 首页](../../_static/numpylogo_dark.svg) ](../../index.html)

  * [ 用户指南 ](../../user/index.html)
  * [ API 参考 ](../index.html)
  * [ 从源码构建 ](../../building/index.html)
  * [ 开发 ](../../dev/index.html)
  * [ 发布说明 ](../../release.html)
  * [ 学习 ](https://numpy.org/numpy-tutorials/)
  * 更多
    * [ NEPs ](https://numpy.org/neps)

__

______

选择版本

  * [__ GitHub](https://github.com/numpy/numpy "GitHub")

  * [ 用户指南 ](../../user/index.html)
  * [ API 参考 ](../index.html)
  * [ 从源码构建 ](../../building/index.html)
  * [ 开发 ](../../dev/index.html)
  * [ 发布说明 ](../../release.html)
  * [ 学习 ](https://numpy.org/numpy-tutorials/)
  * [ NEPs ](https://numpy.org/neps)

__

______

选择版本

  * [__ GitHub](https://github.com/numpy/numpy "GitHub")

章节导航

  * [NumPy 的模块结构](../module_structure.html)

  * [数组对象](../arrays.html)

  * [通用函数 (`ufunc`)](../ufuncs.html)

  * [按主题分类的例程与对象](../routines.html) __
    * [常数](../constants.html)
    * [数组创建例程](../routines.array-creation.html)
    * [数组操作例程](../routines.array-manipulation.html)
    * [位运算](../routines.bitwise.html)
    * [字符串功能](../routines.strings.html)
    * [日期时间支持函数](../routines.datetime.html)
    * [数据类型例程](../routines.dtype.html)
    * [具有自动定义域的数学函数](../routines.emath.html)
    * [浮点错误处理](../routines.err.html)
    * [异常与警告](../routines.exceptions.html)
    * [离散傅里叶变换](../routines.fft.html)
    * [函数式编程](../routines.functional.html)
    * [输入与输出](../routines.io.html)
    * [索引例程](../routines.indexing.html)
    * [线性代数](../routines.linalg.html)
    * [逻辑函数](../routines.logic.html)
    * [掩码数组操作](../routines.ma.html)
    * [数学函数](../routines.math.html)
    * [其他例程](../routines.other.html)
    * [多项式](../routines.polynomials.html)
    * [随机采样](#) __
      * [随机 `Generator`](generator.html)
      * [旧版生成器 (RandomState)](legacy.html)
      * [位生成器](bit_generators/index.html)
      * [使用 PCG64DXSM 升级 PCG64](upgrading-pcg64.html)
      * [兼容性策略](compatibility.html)
      * [并行应用](parallel.html)
      * [多线程生成](multithreading.html)
      * [新增或变更内容](new-or-different.html)
      * [性能比较](performance.html)
      * [随机的 C API](c-api.html)
      * [使用 Numba、Cython、CFFI 的示例](extending.html)
    * [集合例程](../routines.set.html)
    * [排序、搜索与计数](../routines.sort.html)
    * [统计](../routines.statistics.html)
    * [测试支持](../routines.testing.html)
    * [窗函数](../routines.window.html)

  * [类型标注 (`numpy.typing`)](../typing.html)
  * [打包](../distutils.html)

  * [NumPy C-API](../c-api/index.html)

  * [Array API 标准兼容性](../array_api.html)
  * [CPU/SIMD 优化](../simd/index.html)
  * [线程安全性](../thread_safety.html)
  * [全局配置选项](../global_state.html)
  * [NumPy 安全性](../security.html)
  * [测试指南](../testing.html)
  * [`numpy.distutils` 的状态与迁移建议](../distutils_status_migration.html)
  * [`numpy.distutils` 用户指南](../distutils_guide.html)
  * [NumPy 与 SWIG](../swig.html)

  * [ __](../../index.html)
  * [NumPy 参考](../index.html)
  * [NumPy 的模块结构](../module_structure.html)
  * 随机采样

# 随机采样[#](#random-sampling "链接到此标题")

## 快速入门[#](#quick-start "链接到此标题")

[`numpy.random`](#module-numpy.random "numpy.random") 模块实现了伪随机数生成器（PRNG 或简称 RNG），能够从各种概率分布中抽取样本。通常，用户将使用 [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 创建一个 [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 实例，然后调用其上的各种方法来从不同分布获取样本。

在浏览器中尝试！

    >>> import numpy as np
    >>> rng = np.random.default_rng()

生成一个在区间 \\([0, 1)\\) 上均匀分布的随机浮点数：

    >>> rng.random()
    0.06369197489564249  # 可能不同

根据单位高斯分布生成包含 10 个数的数组：

    >>> rng.standard_normal(10)
    array([-0.31018314, -1.8922078 , -0.3628523 , -0.63526532,  0.43181166,  # 可能不同
            0.51640373,  1.25693945,  0.07779185,  0.84090247, -2.13406828])

在区间 \\([0, 10)\\) 上均匀生成包含 5 个整数的数组：

    >>> rng.integers(low=0, high=10, size=5)
    array([8, 7, 6, 2, 0])  # 可能不同

返回在新标签页中打开

我们的 RNG 是确定性序列，可以通过指定种子整数来推导其初始状态来进行重现。默认情况下，如果不提供种子，[`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 将从操作系统的非确定性数据中为 RNG 设定种子，因此每次都会生成不同的数字。伪随机序列在所有实际目的上都是独立的，至少在我们的伪随机性最初适用的那些目的上是如此。

在浏览器中尝试！

    >>> import numpy as np
    >>> rng1 = np.random.default_rng()
    >>> rng1.random()
    0.6596288841243357  # 可能不同
    >>> rng2 = np.random.default_rng()
    >>> rng2.random()
    0.11885628817151628  # 可能不同

返回在新标签页中打开

警告

本模块中实现的伪随机数生成器是为统计建模和模拟而设计的。它们不适用于安全或加密目的。对于此类用例，请参阅标准库中的 [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "\(in Python v3.14\)") 模块。

种子应为大的正整数。[`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 可以接受任意大小的正整数。我们建议使用非常大且唯一的数字，以确保您的种子与其他人的不同。这是确保您的结果在统计上独立于他人结果的良好实践（除非您有意 _试图_ 重现他们的结果）。获取此类种子数字的便捷方法是使用 [`secrets.randbits`](https://docs.python.org/3/library/secrets.html#secrets.randbits "\(in Python v3.14\)") 获取任意 128 位整数。

在浏览器中尝试！

    >>> import numpy as np
    >>> import secrets
    >>> secrets.randbits(128)
    122807528840384100672342137672332424406  # 可能不同
    >>> rng1 = np.random.default_rng(122807528840384100672342137672332424406)
    >>> rng1.random()
    0.5363922081269535
    >>> rng2 = np.random.default_rng(122807528840384100672342137672332424406)
    >>> rng2.random()
    0.5363922081269535

返回在新标签页中打开

有关在特殊场景中控制种子的更高级选项，请参阅 [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 和 [`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence") 的文档。

[`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 及其相关基础设施是在 NumPy 1.17.0 版本中引入的。目前仍有很多代码在使用旧的 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 和 [`numpy.random`](#module-numpy.random "numpy.random") 中的函数。虽然目前没有移除它们的计划，但我们建议尽可能过渡到 [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator")。这些算法更快、更灵活，并且将来会获得更多改进。在大多数情况下，[`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 可以作为 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 的替代品。有关旧版基础设施的信息请参阅[旧版随机生成](legacy.html#legacy)，有关过渡的信息请参阅[新增或变更内容](new-or-different.html#new-or-different)，有关过渡原因的一些推理请参阅 [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html#nep19 "\(in NumPy Enhancement Proposals\)")。

## 设计[#](#design "链接到此标题")

用户主要与 [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 实例交互。每个 [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 实例拥有一个 [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") 实例，该实例实现核心 RNG 算法。[`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") 的职责有限。它管理状态并提供生成随机双精度数和随机无符号 32 位及 64 位值的函数。

[`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 接受位生成器提供的流，并将它们转换为更有用的分布，例如模拟的正态随机值。这种结构允许使用替代的位生成器，而代码重复很少。

NumPy 实现了几个不同的 [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") 类，实现了不同的 RNG 算法。[`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 目前使用 [`PCG64`](bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64") 作为默认的 [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")。与旧版 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 中使用的 [`MT19937`](bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937") 算法相比，它具有更好的统计属性和性能。有关支持的位生成器的更多详细信息，请参阅[位生成器](bit_generators/index.html#random-bit-generators)。

[`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") 和位生成器在内部将种子到 RNG 状态的转换委托给 [`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")。[`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence") 实现了一种复杂的算法，在用户的输入和每个 [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") 算法的内部实现细节之间进行中介，每个算法的状态可能需要不同数量的位。重要的是，它允许您使用任意大小的整数和此类整数的任意序列来混合到 RNG 状态中。这是构建[灵活的并行 RNG 流模式](parallel.html#seedsequence-spawn)的有用原语。

为了向后兼容，我们仍然维护旧的 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 类。它继续默认使用 [`MT19937`](bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937") 算法，旧的种子继续重现相同的结果。便捷的 [numpy.random 中的函数](legacy.html#functions-in-numpy-random) 仍然是单个全局 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 实例上方法的别名。完整细节请参阅[旧版随机生成](legacy.html#legacy)。有关 [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") 和 [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") 之间的详细比较，请参阅[新增或变更内容](new-or-different.html#new-or-different)。

### 并行生成[#](#parallel-generation "链接到此标题")

包含的生成器可以通过多种方式用于并行分布式应用：

  * [SeedSequence 生成](parallel.html#seedsequence-spawn)

  * [整数种子序列](parallel.html#sequence-of-seeds)

  * [独立流](parallel.html#independent-streams)

  * [跳转位生成器状态](parallel.html#parallel-jumped)

具有大量并行性的用户应参阅[使用 PCG64DXSM 升级 PCG64](upgrading-pcg64.html#upgrading-pcg64)。

## 概念[#](#concepts "链接到此标题")

  * [随机 `Generator`](generator.html)
  * [旧版生成器 (RandomState)](legacy.html)
  * [位生成器](bit_generators/index.html)
  * [种子与熵](bit_generators/index.html#seeding-and-entropy)
  * [使用 PCG64DXSM 升级 PCG64](upgrading-pcg64.html)
  * [兼容性策略](compatibility.html)

## 特性[#](#features "链接到此标题")

  * [并行应用](parallel.html)
    * [`SeedSequence` 生成](parallel.html#seedsequence-spawning)
    * [整数种子序列](parallel.html#sequence-of-integer-seeds)
    * [独立流](parallel.html#independent-streams)
    * [跳转位生成器状态](parallel.html#jumping-the-bitgenerator-state)
  * [多线程生成](multithreading.html)
  * [新增或变更内容](new-or-different.html)
  * [性能比较](performance.html)
    * [推荐](performance.html#recommendation)
    * [计时](performance.html#timings)
    * [不同操作系统上的性能](performance.html#performance-on-different-operating-systems)
  * [随机的 C API](c-api.html)
  * [使用 Numba、Cython、CFFI 的示例](extending.html)
    * [Numba](extending.html#numba)
    * [Cython](extending.html#cython)
    * [CFFI](extending.html#id2)
    * [新的位生成器](extending.html#new-bitgenerators)
    * [示例](extending.html#examples)

### 生成器与位生成器的原始来源[#](#original-source-of-the-generator-and-bitgenerators "链接到此标题")

此包独立于 NumPy 开发，并在 1.17.0 版本中集成。原始仓库位于 [bashtage/randomgen](https://github.com/bashtage/randomgen)。

[ __ 上一页 numpy.polynomial.set_default_printstyle ](../generated/numpy.polynomial.set_default_printstyle.html "上一页") [ 下一页 随机 `Generator` __](generator.html "下一页")

__本页内容

  * [快速入门](#quick-start)
  * [设计](#design)
    * [并行生成](#parallel-generation)
  * [概念](#concepts)
  * [特性](#features)
    * [生成器与位生成器的原始来源](#original-source-of-the-generator-and-bitgenerators)

版权所有 2008-2025，NumPy 开发者。

使用 [Sphinx](https://www.sphinx-doc.org/) 7.2.6 创建。

使用 [PyData Sphinx 主题](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1 构建。
