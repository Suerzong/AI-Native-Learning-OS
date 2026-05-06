[Skip to main content](#main-content)

__Back to top

__ `Ctrl`+`K`

[ ![Matplotlib 3.10.9 documentation - Home](../../_static/logo_light.svg) ](https://matplotlib.org/stable/)

  * [Plot types](../../plot_types/index.html)
  * [User guide](../index.html)
  * [Tutorials](../../tutorials/index.html)
  * [Examples](../../gallery/index.html)
  * [Reference](../../api/index.html)
  * [Contribute](../../devel/index.html)
  * [Releases](../release_notes.html)

  * [__ Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
  * [__ Discourse](https://discourse.matplotlib.org "Discourse")
  * [__ GitHub](https://github.com/matplotlib/matplotlib "GitHub")
  * [__ Twitter](https://twitter.com/matplotlib/ "Twitter")

  * [Plot types](../../plot_types/index.html)
  * [User guide](../index.html)
  * [Tutorials](../../tutorials/index.html)
  * [Examples](../../gallery/index.html)
  * [Reference](../../api/index.html)
  * [Contribute](../../devel/index.html)
  * [Releases](../release_notes.html)

  * [__ Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
  * [__ Discourse](https://discourse.matplotlib.org "Discourse")
  * [__ GitHub](https://github.com/matplotlib/matplotlib "GitHub")
  * [__ Twitter](https://twitter.com/matplotlib/ "Twitter")

Section Navigation

  * [Quick start guide](#)

  * [Frequently Asked Questions](../faq.html)

  * [Figures and backends](figure/index.html) __
    * [Introduction to figures](figure/figure_intro.html)
    * [Output backends](figure/backends.html)
    * [Matplotlib Application Interfaces (APIs)](figure/api_interfaces.html)
    * [Interacting with figures](figure/interactive.html)
    * [Interactive figures and asynchronous programming](figure/interactive_guide.html)
    * [Event handling](figure/event_handling.html)
    * [Writing a backend -- the pyplot interface](figure/writing_a_backend_pyplot_interface.html)

  * [Axes and subplots](axes/index.html) __
    * [Introduction to Axes (or Subplots)](axes/axes_intro.html)
    * [Arranging multiple Axes in a Figure](axes/arranging_axes.html)
    * [Placing colorbars](axes/colorbar_placement.html)
    * [Autoscaling axes](axes/autoscale.html)
    * [Axis scales](axes/axes_scales.html)
    * [Axis ticks](axes/axes_ticks.html)
    * [Plotting dates and strings](axes/axes_units.html)
    * [Legends](axes/legend_guide.html)
    * [Subplot mosaic](axes/mosaic.html)
    * [Constrained layout guide](axes/constrainedlayout_guide.html)
    * [Tight layout guide (mildly discouraged)](axes/tight_layout_guide.html)

  * [Artists](artists/index.html) __
    * [Introduction to Artists](artists/artist_intro.html)
    * [Automated color cycle](artists/color_cycle.html)
    * [Optimizing Artists for performance](artists/performance.html)
    * [Paths](artists/paths.html)
    * [Path effects guide](artists/patheffects_guide.html)
    * [Understanding the extent keyword argument of imshow](artists/imshow_extent.html)
    * [Transformations Tutorial](artists/transforms_tutorial.html)

  * [Customizing Matplotlib with style sheets and rcParams](customizing.html)

  * [Colors](colors/index.html) __
    * [Specifying colors](colors/colors.html)
    * [Customized Colorbars Tutorial](colors/colorbar_only.html)
    * [Creating Colormaps in Matplotlib](colors/colormap-manipulation.html)
    * [Colormap normalization](colors/colormapnorms.html)
    * [Choosing Colormaps in Matplotlib](colors/colormaps.html)

  * [Text](text/index.html) __
    * [Text in Matplotlib](text/text_intro.html)
    * [Text properties and layout](text/text_props.html)
    * [Annotations](text/annotations.html)
    * [Fonts in Matplotlib](text/fonts.html)
    * [Writing mathematical expressions](text/mathtext.html)
    * [Text rendering with XeLaTeX/LuaLaTeX via the `pgf` backend](text/pgf.html)
    * [Text rendering with LaTeX](text/usetex.html)

  * [Animations using Matplotlib](animations/index.html) __
    * [Animations using Matplotlib](animations/animations.html)
    * [Faster rendering by using blitting](animations/blitting.html)

  * [User Toolkits](toolkits/index.html) __
    * [The axisartist toolkit](toolkits/axisartist.html)
    * [The axes_grid1 toolkit](toolkits/axes_grid.html)
    * [The mplot3d toolkit](toolkits/mplot3d.html)

  * [Getting started](../getting_started/index.html)
  * [Installation](../../install/index.html) __
    * [Environment variables](../../install/environment_variables_faq.html)
    * [Dependencies](../../install/dependencies.html)

  * [ __](../../index.html)
  * Quick start guide

Note

[Go to the end](#sphx-glr-download-users-explain-quick-start-py) to download the full example code.

# Quick start guide[#](#quick-start-guide "Link to this heading")

This tutorial covers some basic usage patterns and best practices to help you get started with Matplotlib.
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    

## A simple example[#](#a-simple-example "Link to this heading")

Matplotlib graphs your data on [`Figure`](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")s (e.g., windows, Jupyter widgets, etc.), each of which can contain one or more [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), an area where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.). The simplest way of creating a Figure with an Axes is using [`pyplot.subplots`](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots"). We can then use [`Axes.plot`](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") to draw some data on the Axes, and [`show`](../../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") to display the figure:
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")()             # Create a figure containing a single Axes.
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    [plt.show](../../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()                           # Show the figure.
    

![quick start](../../_images/sphx_glr_quick_start_001.png)

Depending on the environment you are working in, `plt.show()` can be left out. This is for example the case with Jupyter notebooks, which automatically show all figures created in a code cell.

## Parts of a Figure[#](#parts-of-a-figure "Link to this heading")

Here are the components of a Matplotlib Figure.

![../../_images/anatomy.png](../../_images/anatomy.png)

### [`Figure`](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")[#](#figure "Link to this heading")

The **whole** figure. The Figure keeps track of all the child [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), a group of 'special' Artists (titles, figure legends, colorbars, etc.), and even nested subfigures.

Typically, you'll create a new Figure through one of the following functions:
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") = [plt.figure](../../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")()             # an empty figure with no Axes
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")()       # a figure with a single Axes
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(2, 2)  # a figure with a 2x2 grid of Axes
    # a figure with one Axes on the left, and two on the right:
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.subplot_mosaic](../../api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")([['left', 'right_top'],
                                   ['left', 'right_bottom']])
    

[`subplots()`](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots") and [`subplot_mosaic`](../../api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic") are convenience functions that additionally create Axes objects inside the Figure, but you can also manually add Axes later on.

For more on Figures, including panning and zooming, see [Introduction to Figures](figure/figure_intro.html#figure-intro).

### [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")[#](#axes "Link to this heading")

An Axes is an Artist attached to a Figure that contains a region for plotting data, and usually includes two (or three in the case of 3D) [`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects (be aware of the difference between **Axes** and **Axis**) that provide ticks and tick labels to provide scales for the data in the Axes. Each [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") also has a title (set via [`set_title()`](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")), an x-label (set via [`set_xlabel()`](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")), and a y-label set via [`set_ylabel()`](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")).

The [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") methods are the primary interface for configuring most parts of your plot (adding data, controlling axis scales and limits, adding labels etc.).

### [`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")[#](#axis "Link to this heading")

These objects set the scale and limits and generate ticks (the marks on the Axis) and ticklabels (strings labeling the ticks). The location of the ticks is determined by a [`Locator`](../../api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") object and the ticklabel strings are formatted by a [`Formatter`](../../api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter"). The combination of the correct [`Locator`](../../api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") and [`Formatter`](../../api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter") gives very fine control over the tick locations and labels.

### [`Artist`](../../api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")[#](#artist "Link to this heading")

Basically, everything visible on the Figure is an Artist (even [`Figure`](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [`Axes`](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), and [`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects). This includes [`Text`](../../api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") objects, [`Line2D`](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") objects, [`collections`](../../api/collections_api.html#module-matplotlib.collections "matplotlib.collections") objects, [`Patch`](../../api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch") objects, etc. When the Figure is rendered, all of the Artists are drawn to the **canvas**. Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another.

## Types of inputs to plotting functions[#](#types-of-inputs-to-plotting-functions "Link to this heading")

Plotting functions expect [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "\(in NumPy v2.4\)") or [`numpy.ma.masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "\(in NumPy v2.4\)") as input, or objects that can be passed to [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "\(in NumPy v2.4\)"). Classes that are similar to arrays ('array-like') such as [`pandas`](https://pandas.pydata.org/pandas-docs/stable/index.html#module-pandas "\(in pandas v3.0.2\)") data objects and [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "\(in NumPy v2.4\)") may not work as intended. Common convention is to convert these to [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "\(in NumPy v2.4\)") objects prior to plotting. For example, to convert a [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "\(in NumPy v2.4\)")
    
    
    b = np.matrix([[1, 2], [3, 4]])
    b_asarray = np.asarray(b)
    

Most methods will also parse a string-indexable object like a _dict_ , a [structured numpy array](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays), or a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.2\)"). Matplotlib allows you to provide the `data` keyword argument and generate plots passing the strings corresponding to the _x_ and _y_ variables.
    
    
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")(19680801)  # seed the random number generator.
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = {'a': [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(50),
            'c': [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")(0, 50, 50),
            'd': [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(50)}
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")['b'] = [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")['a'] + 10 * [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(50)
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")['d'] = [np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")['d']) * 100
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7), layout='constrained')
    [ax.scatter](../../api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")('a', 'b', c='c', [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")='d', [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")=[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [ax.set_xlabel](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")('entry a')
    [ax.set_ylabel](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")('entry b')
    

![quick start](../../_images/sphx_glr_quick_start_002.png)

## Coding styles[#](#coding-styles "Link to this heading")

### The explicit and the implicit interfaces[#](#the-explicit-and-the-implicit-interfaces "Link to this heading")

As noted above, there are essentially two ways to use Matplotlib:

  * Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").

  * Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.

See [Matplotlib Application Interfaces (APIs)](figure/api_interfaces.html#api-interfaces) for an explanation of the tradeoffs between the implicit and explicit interfaces.

So one can use the OO-style
    
    
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")(0, 2, 100)  # Sample data.
    
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7), layout='constrained')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), label='linear')  # Plot some data on the Axes.
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2, label='quadratic')  # Plot more data on the Axes...
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**3, label='cubic')  # ... and some more.
    [ax.set_xlabel](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")('x label')  # Add an x-label to the Axes.
    [ax.set_ylabel](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")('y label')  # Add a y-label to the Axes.
    [ax.set_title](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")("Simple Plot")  # Add a title to the Axes.
    [ax.legend](../../api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")()  # Add a legend.
    

![Simple Plot](../../_images/sphx_glr_quick_start_003.png)

or the pyplot-style:
    
    
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")(0, 2, 100)  # Sample data.
    
    [plt.figure](../../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")(figsize=(5, 2.7), layout='constrained')
    [plt.plot](../../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), label='linear')  # Plot some data on the (implicit) Axes.
    [plt.plot](../../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2, label='quadratic')  # etc.
    [plt.plot](../../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**3, label='cubic')
    [plt.xlabel](../../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")('x label')
    [plt.ylabel](../../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")('y label')
    [plt.title](../../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")("Simple Plot")
    [plt.legend](../../api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")()
    

![Simple Plot](../../_images/sphx_glr_quick_start_004.png)

(In addition, there is a third approach, for the case when embedding Matplotlib in a GUI application, which completely drops pyplot, even for figure creation. See the corresponding section in the gallery for more info: [Embedding Matplotlib in graphical user interfaces](../../gallery/user_interfaces/index.html#user-interfaces).)

Matplotlib's documentation and examples use both the OO and the pyplot styles. In general, we suggest using the OO style, particularly for complicated plots, and functions and scripts that are intended to be reused as part of a larger project. However, the pyplot style can be very convenient for quick interactive work.

Note

You may find older examples that use the `pylab` interface, via `from pylab import *`. This approach is strongly deprecated.

### Making a helper functions[#](#making-a-helper-functions "Link to this heading")

If you need to make the same plots over and over again with different data sets, or want to easily wrap Matplotlib methods, use the recommended signature function below.
    
    
    def my_plotter([ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), param_dict):
        """
        A helper function to make a graph.
        """
        out = [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), **param_dict)
        return out
    

which you would then use twice to populate two subplots:
    
    
    [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(4, 100)  # make 4 random data sets
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), ([ax1](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), [ax2](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")) = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(1, 2, figsize=(5, 2.7))
    my_plotter([ax1](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), {'marker': 'x'})
    my_plotter([ax2](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), [data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), {'marker': 'o'})
    

![quick start](../../_images/sphx_glr_quick_start_005.png)

Note that if you want to install these as a python package, or any other customizations you could use one of the many templates on the web; Matplotlib has one at [mpl-cookiecutter](https://github.com/matplotlib/matplotlib-extension-cookiecutter)

## Styling Artists[#](#styling-artists "Link to this heading")

Most plotting methods have styling options for the Artists, accessible either when a plotting method is called, or from a "setter" on the Artist. In the plot below we manually set the _color_ , _linewidth_ , and _linestyle_ of the Artists created by [`plot`](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot"), and we set the linestyle of the second line after the fact with [`set_linestyle`](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle").
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7))
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")))
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")), color='blue', linewidth=3, linestyle='--')
    [l](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")([data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")), color='orange', linewidth=2)
    [l.set_linestyle](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")(':')
    

![quick start](../../_images/sphx_glr_quick_start_006.png)

### Colors[#](#colors "Link to this heading")

Matplotlib has a very flexible array of colors that are accepted for most Artists; see [allowable color definitions](colors/colors.html#colors-def) for a list of specifications. Some Artists will take multiple colors. i.e. for a [`scatter`](../../api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") plot, the edge of the markers can be different colors from the interior:
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7))
    [ax.scatter](../../api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")=50, facecolor='C0', edgecolor='k')
    

![quick start](../../_images/sphx_glr_quick_start_007.png)

### Linewidths, linestyles, and markersizes[#](#linewidths-linestyles-and-markersizes "Link to this heading")

Line widths are typically in typographic points (1 pt = 1/72 inch) and available for Artists that have stroked lines. Similarly, stroked lines can have a linestyle. See the [linestyles example](../../gallery/lines_bars_and_markers/linestyles.html).

Marker size depends on the method being used. [`plot`](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") specifies markersize in points, and is generally the "diameter" or width of the marker. [`scatter`](../../api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") specifies markersize as approximately proportional to the visual area of the marker. There is an array of markerstyles available as string codes (see [`markers`](../../api/markers_api.html#module-matplotlib.markers "matplotlib.markers")), or users can define their own [`MarkerStyle`](../../api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle") (see [Marker reference](../../gallery/lines_bars_and_markers/marker_reference.html)):
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7))
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 'o', label='data1')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 'd', label='data2')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 'v', label='data3')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([data4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 's', label='data4')
    [ax.legend](../../api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")()
    

![quick start](../../_images/sphx_glr_quick_start_008.png)

## Labelling plots[#](#labelling-plots "Link to this heading")

### Axes labels and text[#](#axes-labels-and-text "Link to this heading")

[`set_xlabel`](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel"), [`set_ylabel`](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel"), and [`set_title`](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") are used to add text in the indicated locations (see [Text in Matplotlib](text/text_intro.html#text-intro) for more discussion). Text can also be directly added to plots using [`text`](../../api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text"):
    
    
    [mu](https://docs.python.org/3/library/functions.html#int "builtins.int"), [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int") = 115, 15
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [mu](https://docs.python.org/3/library/functions.html#int "builtins.int") + [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int") * [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(10000)
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7), layout='constrained')
    # the histogram of the data
    [n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [patches](../../api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer") = [ax.hist](../../api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 50, density=True, facecolor='C0', alpha=0.75)
    
    [ax.set_xlabel](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")('Length [cm]')
    [ax.set_ylabel](../../api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")('Probability')
    [ax.set_title](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")('Aardvark lengths\n (not really)')
    [ax.text](../../api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")(75, .025, r'$\mu=115,\ \sigma=15$')
    [ax.axis](../../api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")([55, 175, 0, 0.03])
    [ax.grid](../../api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")(True)
    

![Aardvark lengths  \(not really\)](../../_images/sphx_glr_quick_start_009.png)

All of the [`text`](../../api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text") functions return a [`matplotlib.text.Text`](../../api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") instance. Just as with lines above, you can customize the properties by passing keyword arguments into the text functions:
    
    
    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [ax.set_xlabel](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")('my data', fontsize=14, color='red')
    

These properties are covered in more detail in [Text properties and layout](text/text_props.html#text-props).

### Using mathematical expressions in text[#](#using-mathematical-expressions-in-text "Link to this heading")

Matplotlib accepts TeX equation expressions in any text expression. For example to write the expression \\(\sigma_i=15\\) in the title, you can write a TeX expression surrounded by dollar signs:
    
    
    [ax.set_title](../../api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")(r'$\sigma_i=15$')
    

where the `r` preceding the title string signifies that the string is a _raw_ string and not to treat backslashes as python escapes. Matplotlib has a built-in TeX expression parser and layout engine, and ships its own math fonts – for details see [Writing mathematical expressions](text/mathtext.html#mathtext). You can also use LaTeX directly to format your text and incorporate the output directly into your display figures or saved postscript – see [Text rendering with LaTeX](text/usetex.html#usetex).

### Annotations[#](#annotations "Link to this heading")

We can also annotate points on a plot, often by connecting an arrow pointing to _xy_ , to a piece of text at _xytext_ :
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7))
    
    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0.0, 5.0, 0.01)
    [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(2 * [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float") * [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [line](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), lw=2)
    
    [ax.annotate](../../api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05))
    
    [ax.set_ylim](../../api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")(-2, 2)
    

![quick start](../../_images/sphx_glr_quick_start_010.png)

In this basic example, both _xy_ and _xytext_ are in data coordinates. There are a variety of other coordinate systems one can choose -- see [Basic annotation](text/annotations.html#annotations-tutorial) and [Advanced annotation](text/annotations.html#plotting-guide-annotation) for details. More examples also can be found in [Annotate plots](../../gallery/text_labels_and_annotations/annotation_demo.html).

### Legends[#](#legends "Link to this heading")

Often we want to identify lines or markers with a [`Axes.legend`](../../api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend"):
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7))
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))), [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), label='data1')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), label='data2')
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))), [data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 'd', label='data3')
    [ax.legend](../../api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")()
    

![quick start](../../_images/sphx_glr_quick_start_011.png)

Legends in Matplotlib are quite flexible in layout, placement, and what Artists they can represent. They are discussed in detail in [Legend guide](axes/legend_guide.html#legend-guide).

## Axis scales and ticks[#](#axis-scales-and-ticks "Link to this heading")

Each Axes has two (or three) [`Axis`](../../api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects representing the x- and y-axis. These control the _scale_ of the Axis, the tick _locators_ and the tick _formatters_. Additional Axes can be attached to display further Axis objects.

### Scales[#](#scales "Link to this heading")

In addition to the linear scale, Matplotlib supplies non-linear scales, such as a log-scale. Since log-scales are used so much there are also direct methods like [`loglog`](../../api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog"), [`semilogx`](../../api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx"), and [`semilogy`](../../api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy"). There are a number of scales (see [Scales overview](../../gallery/scales/scales.html) for other examples). Here we set the scale manually:
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(1, 2, figsize=(5, 2.7), layout='constrained')
    [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")))  # make an ordinal for this
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = 10**[data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].set_yscale('log')
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    

![quick start](../../_images/sphx_glr_quick_start_012.png)

The scale sets the mapping from data values to spacing along the Axis. This happens in both directions, and gets combined into a _transform_ , which is the way that Matplotlib maps from data coordinates to Axes, Figure, or screen coordinates. See [Transformations Tutorial](artists/transforms_tutorial.html#transforms-tutorial).

### Tick locators and formatters[#](#tick-locators-and-formatters "Link to this heading")

Each Axis has a tick _locator_ and _formatter_ that choose where along the Axis objects to put tick marks. A simple interface to this is [`set_xticks`](../../api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks"):
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(2, 1, layout='constrained')
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0].set_title('Automatic ticks')
    
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].set_xticks([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0, 100, 30), ['zero', '30', 'sixty', '90'])
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1].set_title('Manual ticks')
    

![Automatic ticks, Manual ticks](../../_images/sphx_glr_quick_start_013.png)

Different scales can have different locators and formatters; for instance the log-scale above uses [`LogLocator`](../../api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator") and [`LogFormatter`](../../api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter"). See [Tick locators](../../gallery/ticks/tick-locators.html) and [Tick formatters](../../gallery/ticks/tick-formatters.html) for other formatters and locators and information for writing your own.

### Plotting dates and strings[#](#plotting-dates-and-strings "Link to this heading")

Matplotlib can handle plotting arrays of dates and arrays of strings, as well as floating point numbers. These get special locators and formatters as appropriate. For dates:
    
    
    from matplotlib.dates import [ConciseDateFormatter](../../api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7), layout='constrained')
    [dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")('2021-11-15'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")('2021-12-25'),
                      [np.timedelta64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")(1, 'h'))
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(len([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))))
    [ax.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [ax.xaxis.set_major_formatter](../../api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")([ConciseDateFormatter](../../api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")([ax.xaxis.get_major_locator](../../api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")()))
    

![quick start](../../_images/sphx_glr_quick_start_014.png)

For more information see the date examples (e.g. [Date tick labels](../../gallery/text_labels_and_annotations/date.html))

For strings, we get categorical plotting (see: [Plotting categorical variables](../../gallery/lines_bars_and_markers/categorical_variables.html)).
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(figsize=(5, 2.7), layout='constrained')
    [categories](https://docs.python.org/3/library/stdtypes.html#list "builtins.list") = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
    
    [ax.bar](../../api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")([categories](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"), [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")(len([categories](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"))))
    

![quick start](../../_images/sphx_glr_quick_start_015.png)

One caveat about categorical plotting is that some methods of parsing text files return a list of strings, even if the strings all represent numbers or dates. If you pass 1000 strings, Matplotlib will think you meant 1000 categories and will add 1000 ticks to your plot!

### Additional Axis objects[#](#additional-axis-objects "Link to this heading")

Plotting data of different magnitude in one chart may require an additional y-axis. Such an Axis can be created by using [`twinx`](../../api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx") to add a new Axes with an invisible x-axis and a y-axis positioned at the right (analogously for [`twiny`](../../api/_as_gen/matplotlib.axes.Axes.twiny.html#matplotlib.axes.Axes.twiny "matplotlib.axes.Axes.twiny")). See [Plots with different scales](../../gallery/subplots_axes_and_figures/two_scales.html) for another example.

Similarly, you can add a [`secondary_xaxis`](../../api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis") or [`secondary_yaxis`](../../api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib.axes.Axes.secondary_yaxis "matplotlib.axes.Axes.secondary_yaxis") having a different scale than the main Axis to represent the data in different scales or units. See [Secondary Axis](../../gallery/subplots_axes_and_figures/secondary_axis.html) for further examples.
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), ([ax1](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), [ax3](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")) = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(1, 2, figsize=(7, 2.7), layout='constrained')
    [l1](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [ax1.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [ax2](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [ax1.twinx](../../api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")()
    [l2](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [ax2.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), range(len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))), 'C1')
    [ax2.legend](../../api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")([[l1](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), [l2](../../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")], ['Sine (left)', 'Straight (right)'])
    
    [ax3.plot](../../api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [ax3.set_xlabel](../../api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")('Angle [rad]')
    ax4 = [ax3.secondary_xaxis](../../api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")('top', ([np.rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc"), [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")))
    ax4.set_xlabel('Angle [°]')
    

![quick start](../../_images/sphx_glr_quick_start_016.png)

## Color mapped data[#](#color-mapped-data "Link to this heading")

Often we want to have a third dimension in a plot represented by colors in a colormap. Matplotlib has a number of plot types that do this:
    
    
    from matplotlib.colors import [LogNorm](../../api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
    
    [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")(-3, 3, 128), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")(-3, 3, 128))
    [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = (1 - [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")/2 + [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**5 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**3) * [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2 - [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2)
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.subplots](../../api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")(2, 2, layout='constrained')
    [pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection") = [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 0].pcolormesh([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), vmin=-1, vmax=1, cmap='RdBu_r')
    [fig.colorbar](../../api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")([pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 0])
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 0].set_title('pcolormesh()')
    
    [co](../../api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet") = [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 1].contourf([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), levels=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")(-1.25, 1.25, 11))
    [fig.colorbar](../../api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")([co](../../api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 1])
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[0, 1].set_title('contourf()')
    
    [pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection") = [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 0].imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2 * 100, cmap='plasma', norm=[LogNorm](../../api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")(vmin=0.01, vmax=100))
    [fig.colorbar](../../api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")([pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 0], extend='both')
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 0].set_title('imshow() with LogNorm()')
    
    [pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection") = [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 1].scatter([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), c=[data3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), cmap='RdBu_r')
    [fig.colorbar](../../api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")([pc](../../api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection"), [ax](../../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 1], extend='both')
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[1, 1].set_title('scatter()')
    

![pcolormesh\(\), contourf\(\), imshow\(\) with LogNorm\(\), scatter\(\)](../../_images/sphx_glr_quick_start_017.png)

### Colormaps[#](#colormaps "Link to this heading")

These are all examples of Artists that derive from [`ScalarMappable`](../../api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable") objects. They all can set a linear mapping between _vmin_ and _vmax_ into the colormap specified by _cmap_. Matplotlib has many colormaps to choose from ([Choosing Colormaps in Matplotlib](colors/colormaps.html#colormaps)) you can make your own ([Creating Colormaps in Matplotlib](colors/colormap-manipulation.html#colormap-manipulation)) or download as [third-party packages](https://matplotlib.org/mpl-third-party/#colormaps-and-styles).

### Normalizations[#](#normalizations "Link to this heading")

Sometimes we want a non-linear mapping of the data to the colormap, as in the `LogNorm` example above. We do this by supplying the ScalarMappable with the _norm_ argument instead of _vmin_ and _vmax_. More normalizations are shown at [Colormap normalization](colors/colormapnorms.html#colormapnorms).

### Colorbars[#](#colorbars "Link to this heading")

Adding a [`colorbar`](../../api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar") gives a key to relate the color back to the underlying data. Colorbars are figure-level Artists, and are attached to a ScalarMappable (where they get their information about the norm and colormap) and usually steal space from a parent Axes. Placement of colorbars can be complex: see [Placing colorbars](axes/colorbar_placement.html#colorbar-placement) for details. You can also change the appearance of colorbars with the _extend_ keyword to add arrows to the ends, and _shrink_ and _aspect_ to control the size. Finally, the colorbar will have default locators and formatters appropriate to the norm. These can be changed as for other Axis objects.

## Working with multiple Figures and Axes[#](#working-with-multiple-figures-and-axes "Link to this heading")

You can open multiple Figures with multiple calls to `fig = plt.figure()` or `fig2, ax = plt.subplots()`. By keeping the object references you can add Artists to either Figure.

Multiple Axes can be added a number of ways, but the most basic is `plt.subplots()` as used above. One can achieve more complex layouts, with Axes objects spanning columns or rows, using [`subplot_mosaic`](../../api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic").
    
    
    [fig](../../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict") = [plt.subplot_mosaic](../../api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")([['upleft', 'right'],
                                   ['lowleft', 'right']], layout='constrained')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['upleft'].set_title('upleft')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['lowleft'].set_title('lowleft')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['right'].set_title('right')
    

![upleft, right, lowleft](../../_images/sphx_glr_quick_start_018.png)

Matplotlib has quite sophisticated tools for arranging Axes: See [Arranging multiple Axes in a Figure](axes/arranging_axes.html#arranging-axes) and [Complex and semantic figure composition (subplot_mosaic)](axes/mosaic.html#mosaic).

## More reading[#](#more-reading "Link to this heading")

For more plot types see [Plot types](../../plot_types/index.html) and the [API reference](../../api/index.html), in particular the [Axes API](../../api/axes_api.html).

**Total running time of the script:** (0 minutes 8.308 seconds)

[`Download Jupyter notebook: quick_start.ipynb`](../../_downloads/19637872c4a7dbe872e23f74038df260/quick_start.ipynb)

[`Download Python source code: quick_start.py`](../../_downloads/43dac8ab08924b9b18dd7e7874d69d6c/quick_start.py)

[`Download zipped: quick_start.zip`](../../_downloads/780c8d7b1587e6267d615cfc1adb0408/quick_start.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io)

__On this page

  * [A simple example](#a-simple-example)
  * [Parts of a Figure](#parts-of-a-figure)
    * [`Figure`](#figure)
    * [`Axes`](#axes)
    * [`Axis`](#axis)
    * [`Artist`](#artist)
  * [Types of inputs to plotting functions](#types-of-inputs-to-plotting-functions)
  * [Coding styles](#coding-styles)
    * [The explicit and the implicit interfaces](#the-explicit-and-the-implicit-interfaces)
    * [Making a helper functions](#making-a-helper-functions)
  * [Styling Artists](#styling-artists)
    * [Colors](#colors)
    * [Linewidths, linestyles, and markersizes](#linewidths-linestyles-and-markersizes)
  * [Labelling plots](#labelling-plots)
    * [Axes labels and text](#axes-labels-and-text)
    * [Using mathematical expressions in text](#using-mathematical-expressions-in-text)
    * [Annotations](#annotations)
    * [Legends](#legends)
  * [Axis scales and ticks](#axis-scales-and-ticks)
    * [Scales](#scales)
    * [Tick locators and formatters](#tick-locators-and-formatters)
    * [Plotting dates and strings](#plotting-dates-and-strings)
    * [Additional Axis objects](#additional-axis-objects)
  * [Color mapped data](#color-mapped-data)
    * [Colormaps](#colormaps)
    * [Normalizations](#normalizations)
    * [Colorbars](#colorbars)
  * [Working with multiple Figures and Axes](#working-with-multiple-figures-and-axes)
  * [More reading](#more-reading)

© Copyright 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2026 The Matplotlib development team.   

Created using [Sphinx](https://www.sphinx-doc.org/) 9.1.0.   

Built from v3.10.9-2-gdf001ac932.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.
