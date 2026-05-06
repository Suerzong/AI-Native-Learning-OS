[Skip to main content](#main-content)

__Back to top __ `Ctrl`+`K`

[ ![NumPy v2.4 Manual - Home](../../_static/numpylogo.svg) ![NumPy v2.4 Manual - Home](../../_static/numpylogo_dark.svg) ](../../index.html)

  * [ User Guide ](../../user/index.html)
  * [ API reference ](../index.html)
  * [ Building from source ](../../building/index.html)
  * [ Development ](../../dev/index.html)
  * [ Release notes ](../../release.html)
  * [ Learn ](https://numpy.org/numpy-tutorials/)
  * More 
    * [ NEPs ](https://numpy.org/neps)

__

______

Choose version 

  * [__ GitHub](https://github.com/numpy/numpy "GitHub")

  * [ User Guide ](../../user/index.html)
  * [ API reference ](../index.html)
  * [ Building from source ](../../building/index.html)
  * [ Development ](../../dev/index.html)
  * [ Release notes ](../../release.html)
  * [ Learn ](https://numpy.org/numpy-tutorials/)
  * [ NEPs ](https://numpy.org/neps)

__

______

Choose version 

  * [__ GitHub](https://github.com/numpy/numpy "GitHub")

Section Navigation

  * [NumPy’s module structure](../module_structure.html)

  * [Array objects](../arrays.html)

  * [Universal functions (`ufunc`)](../ufuncs.html)

  * [Routines and objects by topic](../routines.html) __
    * [Constants](../constants.html)
    * [Array creation routines](../routines.array-creation.html)
    * [Array manipulation routines](../routines.array-manipulation.html)
    * [Bit-wise operations](../routines.bitwise.html)
    * [String functionality](../routines.strings.html)
    * [Datetime support functions](../routines.datetime.html)
    * [Data type routines](../routines.dtype.html)
    * [Mathematical functions with automatic domain](../routines.emath.html)
    * [Floating point error handling](../routines.err.html)
    * [Exceptions and Warnings](../routines.exceptions.html)
    * [Discrete Fourier Transform](../routines.fft.html)
    * [Functional programming](../routines.functional.html)
    * [Input and output](../routines.io.html)
    * [Indexing routines](../routines.indexing.html)
    * [Linear algebra](../routines.linalg.html)
    * [Logic functions](../routines.logic.html)
    * [Masked array operations](../routines.ma.html)
    * [Mathematical functions](../routines.math.html)
    * [Miscellaneous routines](../routines.other.html)
    * [Polynomials](../routines.polynomials.html)
    * [Random sampling](#) __
      * [Random `Generator`](generator.html)
      * [Legacy Generator (RandomState)](legacy.html)
      * [Bit generators](bit_generators/index.html)
      * [Upgrading PCG64 with PCG64DXSM](upgrading-pcg64.html)
      * [Compatibility policy](compatibility.html)
      * [Parallel Applications](parallel.html)
      * [Multithreaded Generation](multithreading.html)
      * [What’s new or different](new-or-different.html)
      * [Comparing Performance](performance.html)
      * [C API for random](c-api.html)
      * [Examples of using Numba, Cython, CFFI](extending.html)
    * [Set routines](../routines.set.html)
    * [Sorting, searching, and counting](../routines.sort.html)
    * [Statistics](../routines.statistics.html)
    * [Test support](../routines.testing.html)
    * [Window functions](../routines.window.html)

  * [Typing (`numpy.typing`)](../typing.html)
  * [Packaging](../distutils.html)

  * [NumPy C-API](../c-api/index.html)

  * [Array API standard compatibility](../array_api.html)
  * [CPU/SIMD optimizations](../simd/index.html)
  * [Thread Safety](../thread_safety.html)
  * [Global Configuration Options](../global_state.html)
  * [NumPy security](../security.html)
  * [Testing guidelines](../testing.html)
  * [Status of `numpy.distutils` and migration advice](../distutils_status_migration.html)
  * [`numpy.distutils` user guide](../distutils_guide.html)
  * [NumPy and SWIG](../swig.html)

  * [ __](../../index.html)
  * [NumPy reference](../index.html)
  * [NumPy’s module structure](../module_structure.html)
  * Random sampling

# Random sampling[#](#random-sampling "Link to this heading")

## Quick start[#](#quick-start "Link to this heading")

The [`numpy.random`](#module-numpy.random "numpy.random") module implements pseudo-random number generators (PRNGs or RNGs, for short) with the ability to draw samples from a variety of probability distributions. In general, users will create a [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") instance with [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") and call the various methods on it to obtain samples from different distributions.

Try it in your browser!
    
    
    >>> import numpy as np
    >>> rng = np.random.default_rng()
    

Generate one random float uniformly distributed over the range \\([0, 1)\\):
    
    
    >>> rng.random()  
    0.06369197489564249  # may vary
    

Generate an array of 10 numbers according to a unit Gaussian distribution:
    
    
    >>> rng.standard_normal(10)  
    array([-0.31018314, -1.8922078 , -0.3628523 , -0.63526532,  0.43181166,  # may vary
            0.51640373,  1.25693945,  0.07779185,  0.84090247, -2.13406828])
    

Generate an array of 5 integers uniformly over the range \\([0, 10)\\):
    
    
    >>> rng.integers(low=0, high=10, size=5)  
    array([8, 7, 6, 2, 0])  # may vary
    

Go BackOpen In Tab

Our RNGs are deterministic sequences and can be reproduced by specifying a seed integer to derive its initial state. By default, with no seed provided, [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") will seed the RNG from nondeterministic data from the operating system and therefore generate different numbers each time. The pseudo-random sequences will be independent for all practical purposes, at least those purposes for which our pseudo-randomness was good for in the first place.

Try it in your browser!
    
    
    >>> import numpy as np
    >>> rng1 = np.random.default_rng()
    >>> rng1.random()  
    0.6596288841243357  # may vary
    >>> rng2 = np.random.default_rng()
    >>> rng2.random()  
    0.11885628817151628  # may vary
    

Go BackOpen In Tab

Warning

The pseudo-random number generators implemented in this module are designed for statistical modeling and simulation. They are not suitable for security or cryptographic purposes. See the [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "\(in Python v3.14\)") module from the standard library for such use cases.

Seeds should be large positive integers. [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") can take positive integers of any size. We recommend using very large, unique numbers to ensure that your seed is different from anyone else’s. This is good practice to ensure that your results are statistically independent from theirs unless you are intentionally _trying_ to reproduce their result. A convenient way to get such a seed number is to use [`secrets.randbits`](https://docs.python.org/3/library/secrets.html#secrets.randbits "\(in Python v3.14\)") to get an arbitrary 128-bit integer.

Try it in your browser!
    
    
    >>> import numpy as np
    >>> import secrets
    >>> secrets.randbits(128)  
    122807528840384100672342137672332424406  # may vary
    >>> rng1 = np.random.default_rng(122807528840384100672342137672332424406)
    >>> rng1.random()
    0.5363922081269535
    >>> rng2 = np.random.default_rng(122807528840384100672342137672332424406)
    >>> rng2.random()
    0.5363922081269535
    

Go BackOpen In Tab

See the documentation on [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") and [`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence") for more advanced options for controlling the seed in specialized scenarios.

[`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") and its associated infrastructure was introduced in NumPy version 1.17.0. There is still a lot of code that uses the older [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") and the functions in [`numpy.random`](#module-numpy.random "numpy.random"). While there are no plans to remove them at this time, we do recommend transitioning to [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") as you can. The algorithms are faster, more flexible, and will receive more improvements in the future. For the most part, [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") can be used as a replacement for [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState"). See [Legacy random generation](legacy.html#legacy) for information on the legacy infrastructure, [What’s new or different](new-or-different.html#new-or-different) for information on transitioning, and [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html#nep19 "\(in NumPy Enhancement Proposals\)") for some of the reasoning for the transition.

## Design[#](#design "Link to this heading")

Users primarily interact with [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") instances. Each [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") instance owns a [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") instance that implements the core RNG algorithm. The [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") has a limited set of responsibilities. It manages state and provides functions to produce random doubles and random unsigned 32- and 64-bit values.

The [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") takes the bit generator-provided stream and transforms them into more useful distributions, e.g., simulated normal random values. This structure allows alternative bit generators to be used with little code duplication.

NumPy implements several different [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") classes implementing different RNG algorithms. [`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") currently uses [`PCG64`](bit_generators/pcg64.html#numpy.random.PCG64 "numpy.random.PCG64") as the default [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator"). It has better statistical properties and performance than the [`MT19937`](bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937") algorithm used in the legacy [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState"). See [Bit generators](bit_generators/index.html#random-bit-generators) for more details on the supported BitGenerators.

[`default_rng`](generator.html#numpy.random.default_rng "numpy.random.default_rng") and BitGenerators delegate the conversion of seeds into RNG states to [`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence") internally. [`SeedSequence`](bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence") implements a sophisticated algorithm that intermediates between the user’s input and the internal implementation details of each [`BitGenerator`](bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator") algorithm, each of which can require different amounts of bits for its state. Importantly, it lets you use arbitrary-sized integers and arbitrary sequences of such integers to mix together into the RNG state. This is a useful primitive for constructing a [flexible pattern for parallel RNG streams](parallel.html#seedsequence-spawn).

For backward compatibility, we still maintain the legacy [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") class. It continues to use the [`MT19937`](bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937") algorithm by default, and old seeds continue to reproduce the same results. The convenience [Functions in numpy.random](legacy.html#functions-in-numpy-random) are still aliases to the methods on a single global [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState") instance. See [Legacy random generation](legacy.html#legacy) for the complete details. See [What’s new or different](new-or-different.html#new-or-different) for a detailed comparison between [`Generator`](generator.html#numpy.random.Generator "numpy.random.Generator") and [`RandomState`](legacy.html#numpy.random.RandomState "numpy.random.RandomState").

### Parallel Generation[#](#parallel-generation "Link to this heading")

The included generators can be used in parallel, distributed applications in a number of ways:

  * [SeedSequence spawning](parallel.html#seedsequence-spawn)

  * [Sequence of integer seeds](parallel.html#sequence-of-seeds)

  * [Independent streams](parallel.html#independent-streams)

  * [Jumping the BitGenerator state](parallel.html#parallel-jumped)

Users with a very large amount of parallelism will want to consult [Upgrading PCG64 with PCG64DXSM](upgrading-pcg64.html#upgrading-pcg64).

## Concepts[#](#concepts "Link to this heading")

  * [Random `Generator`](generator.html)
  * [Legacy Generator (RandomState)](legacy.html)
  * [Bit generators](bit_generators/index.html)
  * [Seeding and entropy](bit_generators/index.html#seeding-and-entropy)
  * [Upgrading PCG64 with PCG64DXSM](upgrading-pcg64.html)
  * [Compatibility policy](compatibility.html)

## Features[#](#features "Link to this heading")

  * [Parallel Applications](parallel.html)
    * [`SeedSequence` spawning](parallel.html#seedsequence-spawning)
    * [Sequence of integer seeds](parallel.html#sequence-of-integer-seeds)
    * [Independent streams](parallel.html#independent-streams)
    * [Jumping the BitGenerator state](parallel.html#jumping-the-bitgenerator-state)
  * [Multithreaded Generation](multithreading.html)
  * [What’s new or different](new-or-different.html)
  * [Comparing Performance](performance.html)
    * [Recommendation](performance.html#recommendation)
    * [Timings](performance.html#timings)
    * [Performance on different operating systems](performance.html#performance-on-different-operating-systems)
  * [C API for random](c-api.html)
  * [Examples of using Numba, Cython, CFFI](extending.html)
    * [Numba](extending.html#numba)
    * [Cython](extending.html#cython)
    * [CFFI](extending.html#id2)
    * [New BitGenerators](extending.html#new-bitgenerators)
    * [Examples](extending.html#examples)

### Original Source of the Generator and BitGenerators[#](#original-source-of-the-generator-and-bitgenerators "Link to this heading")

This package was developed independently of NumPy and was integrated in version 1.17.0. The original repo is at [bashtage/randomgen](https://github.com/bashtage/randomgen).

[ __ previous numpy.polynomial.set_default_printstyle ](../generated/numpy.polynomial.set_default_printstyle.html "previous page") [ next Random `Generator` __](generator.html "next page")

__On this page

  * [Quick start](#quick-start)
  * [Design](#design)
    * [Parallel Generation](#parallel-generation)
  * [Concepts](#concepts)
  * [Features](#features)
    * [Original Source of the Generator and BitGenerators](#original-source-of-the-generator-and-bitgenerators)

© Copyright 2008-2025, NumPy Developers.   

Created using [Sphinx](https://www.sphinx-doc.org/) 7.2.6.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.
