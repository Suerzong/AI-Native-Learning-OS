[Skip to main content](#main-content)

__Back to top

__ `Ctrl`+`K`

[ ![Matplotlib 3.10.9 documentation - Home](../_static/logo_light.svg) ](https://matplotlib.org/stable/)

  * [Plot types](../plot_types/index.html)
  * [User guide](../users/index.html)
  * [Tutorials](index.html)
  * [Examples](../gallery/index.html)
  * [Reference](../api/index.html)
  * [Contribute](../devel/index.html)
  * [Releases](../users/release_notes.html)

  * [__ Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
  * [__ Discourse](https://discourse.matplotlib.org "Discourse")
  * [__ GitHub](https://github.com/matplotlib/matplotlib "GitHub")
  * [__ Twitter](https://twitter.com/matplotlib/ "Twitter")

  * [Plot types](../plot_types/index.html)
  * [User guide](../users/index.html)
  * [Tutorials](index.html)
  * [Examples](../gallery/index.html)
  * [Reference](../api/index.html)
  * [Contribute](../devel/index.html)
  * [Releases](../users/release_notes.html)

  * [__ Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
  * [__ Discourse](https://discourse.matplotlib.org "Discourse")
  * [__ GitHub](https://github.com/matplotlib/matplotlib "GitHub")
  * [__ Twitter](https://twitter.com/matplotlib/ "Twitter")

Section Navigation

  * [Pyplot tutorial](#)
  * [Coding shortcuts](coding_shortcuts.html)
  * [Image tutorial](images.html)
  * [The Lifecycle of a Plot](lifecycle.html)
  * [Artist tutorial](artists.html)

  * [ __](../index.html)
  * [Tutorials](index.html)
  * Pyplot tutorial

Note

[Go to the end](#sphx-glr-download-tutorials-pyplot-py) to download the full example code.

# Pyplot tutorial[#](#pyplot-tutorial "Link to this heading")

An introduction to the pyplot interface. Please also see [Quick start guide](../users/explain/quick_start.html#quick-start) for an overview of how Matplotlib works and [Matplotlib Application Interfaces (APIs)](../users/explain/figure/api_interfaces.html#api-interfaces) for an explanation of the trade-offs between the supported user APIs.

## Introduction to pyplot[#](#introduction-to-pyplot "Link to this heading")

[`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") is a collection of functions that make matplotlib work like MATLAB. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In [`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current Axes (please note that we use uppercase Axes to refer to the [`Axes`](../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") concept, which is a central [part of a figure](../users/explain/quick_start.html#figure-parts) and not only the plural of _axis_).

Note

The implicit pyplot API is generally less verbose but also not as flexible as the explicit API. Most of the function calls you see here can also be called as methods from an `Axes` object. We recommend browsing the tutorials and examples to see how this works. See [Matplotlib Application Interfaces (APIs)](../users/explain/figure/api_interfaces.html#api-interfaces) for an explanation of the trade-off of the supported user APIs.

Generating visualizations with pyplot is very quick:
    
    
    import matplotlib.pyplot as plt
    
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([1, 2, 3, 4])
    [plt.ylabel](../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")('some numbers')
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_001.png)

You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to [`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot"), matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0; therefore, the x data are `[0, 1, 2, 3]`.

[`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") is a versatile function, and will take an arbitrary number of arguments. For example, to plot x versus y, you can write:
    
    
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([1, 2, 3, 4], [1, 4, 9, 16])
    

![pyplot](../_images/sphx_glr_pyplot_002.png)

### Formatting the style of your plot[#](#formatting-the-style-of-your-plot "Link to this heading")

For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue
    
    
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    [plt.axis](../api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")((0, 6, 0, 20))
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_003.png)

See the [`plot`](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") documentation for a complete list of line styles and format strings. The [`axis`](../api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis") function in the example above takes a list of `[xmin, xmax, ymin, ymax]` and specifies the viewport of the Axes.

If matplotlib were limited to working with lists, it would be fairly useless for numeric processing. Generally, you will use [numpy](https://numpy.org/) arrays. In fact, all sequences are converted to numpy arrays internally. The example below illustrates plotting several lines with different format styles in one function call using arrays.
    
    
    import numpy as np
    
    # evenly sampled time at 200ms intervals
    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0., 5., 0.2)
    
    # red dashes, blue squares and green triangles
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 'r--', [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**2, 'bs', [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")**3, 'g^')
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_004.png)

## Plotting with keyword strings[#](#plotting-with-keyword-strings "Link to this heading")

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with [structured arrays](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays) or [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas v3.0.2\)").

Matplotlib allows you to provide such an object with the `data` keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.
    
    
    [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict") = {'a': [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(50),
            'c': [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")(0, 50, 50),
            'd': [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(50)}
    [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['b'] = [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['a'] + 10 * [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(50)
    [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['d'] = [np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")['d']) * 100
    
    [plt.scatter](../api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")('a', 'b', c='c', [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")='d', [data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")=[data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict"))
    [plt.xlabel](../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")('entry a')
    [plt.ylabel](../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")('entry b')
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_005.png)

## Plotting with categorical variables[#](#plotting-with-categorical-variables "Link to this heading")

It is also possible to create a plot using categorical variables. Matplotlib allows you to pass categorical variables directly to many plotting functions. For example:
    
    
    [names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list") = ['group_a', 'group_b', 'group_c']
    [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list") = [1, 10, 100]
    
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")(figsize=(9, 3))
    
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(131)
    [plt.bar](../api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"), [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"))
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(132)
    [plt.scatter](../api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"), [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"))
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(133)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"), [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list"))
    [plt.suptitle](../api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")('Categorical Plotting')
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![Categorical Plotting](../_images/sphx_glr_pyplot_006.png)

## Controlling line properties[#](#controlling-line-properties "Link to this heading")

Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see [`matplotlib.lines.Line2D`](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"). There are several ways to set line properties

  * Use keyword arguments:
        
        [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), linewidth=2.0)
        

  * Use the setter methods of a `Line2D` instance. `plot` returns a list of `Line2D` objects; e.g., `line1, line2 = plot(x1, y1, x2, y2)`. In the code below we will suppose that we have only one line so that the list returned is of length 1. We use tuple unpacking with `line,` to get the first element of that list:
        
        [line](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), '-')
        [line](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D").set_antialiased(False) # turn off antialiasing
        

  * Use [`setp`](../api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp"). The example below uses a MATLAB-style function to set multiple properties on a list of lines. `setp` works transparently with a list of objects or a single object. You can either use python keyword arguments or MATLAB-style string/value pairs:
        
        lines = [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")(x1, y1, x2, y2)
        # use keyword arguments
        plt.setp(lines, color='r', linewidth=2.0)
        # or MATLAB style string value pairs
        plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
        

Here are the available [`Line2D`](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") properties.

Property | Value Type  
---|---  
alpha | float  
animated | [True | False]  
antialiased or aa | [True | False]  
clip_box | a matplotlib.transform.Bbox instance  
clip_on | [True | False]  
clip_path | a Path instance and a Transform instance, a Patch  
color or c | any matplotlib color  
contains | the hit testing function  
dash_capstyle | [`'butt'` | `'round'` | `'projecting'`]  
dash_joinstyle | [`'miter'` | `'round'` | `'bevel'`]  
dashes | sequence of on/off ink in points  
data | (np.array xdata, np.array ydata)  
figure | a matplotlib.figure.Figure instance  
label | any string  
linestyle or ls | [ `'-'` | `'--'` | `'-.'` | `':'` | `'steps'` | ...]  
linewidth or lw | float value in points  
marker | [ `'+'` | `','` | `'.'` | `'1'` | `'2'` | `'3'` | `'4'` ]  
markeredgecolor or mec | any matplotlib color  
markeredgewidth or mew | float value in points  
markerfacecolor or mfc | any matplotlib color  
markersize or ms | float  
markevery | [ None | integer | (startind, stride) ]  
picker | used in interactive line selection  
pickradius | the line pick selection radius  
solid_capstyle | [`'butt'` | `'round'` | `'projecting'`]  
solid_joinstyle | [`'miter'` | `'round'` | `'bevel'`]  
transform | a matplotlib.transforms.Transform instance  
visible | [True | False]  
xdata | np.array  
ydata | np.array  
zorder | any number  
  
To get a list of settable line properties, call the [`setp`](../api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp") function with a line or lines as argument
    
    
    In [69]: lines = [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([1, 2, 3])
    
    In [70]: plt.setp(lines)
      alpha: float
      animated: [True | False]
      antialiased or aa: [True | False]
      ...snip
    

## Working with multiple figures and Axes[#](#working-with-multiple-figures-and-axes "Link to this heading")

MATLAB, and [`pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot"), have the concept of the current figure and the current Axes. All plotting functions apply to the current Axes. The function [`gca`](../api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca") returns the current Axes (a [`matplotlib.axes.Axes`](../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") instance), and [`gcf`](../api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf") returns the current figure (a [`matplotlib.figure.Figure`](../api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") instance). Normally, you don't have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.
    
    
    def f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")):
        return [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(-[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")) * [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(2*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    
    [t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0.0, 5.0, 0.1)
    [t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0.0, 5.0, 0.02)
    
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")()
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(211)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), f([t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")), 'bo', [t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), f([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")), 'k')
    
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(212)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(2*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")*[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")), 'r--')
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_007.png)

The [`figure`](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure") call here is optional because a figure will be created if none exists, just as an Axes will be created (equivalent to an explicit `subplot()` call) if none exists. The [`subplot`](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot") call specifies `numrows, numcols, plot_number` where `plot_number` ranges from 1 to `numrows*numcols`. The commas in the `subplot` call are optional if `numrows*numcols<10`. So `subplot(211)` is identical to `subplot(2, 1, 1)`.

You can create an arbitrary number of subplots and Axes. If you want to place an Axes manually, i.e., not on a rectangular grid, use [`axes`](../api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes"), which allows you to specify the location as `axes([left, bottom, width, height])` where all values are in fractional (0 to 1) coordinates. See [Axes Demo](../gallery/subplots_axes_and_figures/axes_demo.html) for an example of placing Axes manually and [Multiple subplots](../gallery/subplots_axes_and_figures/subplot.html) for an example with lots of subplots.

You can create multiple figures by using multiple [`figure`](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure") calls with an increasing figure number. Of course, each figure can contain as many Axes and subplots as your heart desires:
    
    
    import matplotlib.pyplot as plt
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")(1)                # the first figure
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(211)             # the first subplot in the first figure
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([1, 2, 3])
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(212)             # the second subplot in the first figure
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([4, 5, 6])
    
    
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")(2)                # a second figure
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([4, 5, 6])          # creates a subplot() by default
    
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")(1)                # first figure current;
                                 # subplot(212) still current
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(211)             # make subplot(211) in the first figure
                                 # current
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('Easy as 1, 2, 3') # subplot 211 title
    

You can clear the current figure with [`clf`](../api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf") and the current Axes with [`cla`](../api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla "matplotlib.pyplot.cla"). If you find it annoying that states (specifically the current image, figure and Axes) are being maintained for you behind the scenes, don't despair: this is just a thin stateful wrapper around an object-oriented API, which you can use instead (see [Artist tutorial](artists.html#artists-tutorial))

If you are making lots of figures, you need to be aware of one more thing: the memory required for a figure is not completely released until the figure is explicitly closed with [`close`](../api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close"). Deleting all references to the figure, and/or using the window manager to kill the window in which the figure appears on the screen, is not enough, because pyplot maintains internal references until [`close`](../api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close") is called.

## Working with text[#](#working-with-text "Link to this heading")

[`text`](../api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text") can be used to add text in an arbitrary location, and [`xlabel`](../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel"), [`ylabel`](../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel") and [`title`](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title") are used to add text in the indicated locations (see [Text in Matplotlib](../users/explain/text/text_intro.html#text-intro) for a more detailed example)
    
    
    [mu](https://docs.python.org/3/library/functions.html#int "builtins.int"), [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int") = 100, 15
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [mu](https://docs.python.org/3/library/functions.html#int "builtins.int") + [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int") * [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")(10000)
    
    # the histogram of the data
    [n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [patches](../api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer") = [plt.hist](../api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), 50, density=True, facecolor='g', alpha=0.75)
    
    
    [plt.xlabel](../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")('Smarts')
    [plt.ylabel](../api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")('Probability')
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('Histogram of IQ')
    [plt.text](../api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")(60, .025, r'$\mu=100,\ \sigma=15$')
    [plt.axis](../api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")([40, 160, 0, 0.03])
    [plt.grid](../api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")(True)
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![Histogram of IQ](../_images/sphx_glr_pyplot_008.png)

All of the [`text`](../api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text") functions return a [`matplotlib.text.Text`](../api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") instance. Just as with lines above, you can customize the properties by passing keyword arguments into the text functions or using [`setp`](../api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp"):
    
    
    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [plt.xlabel](../api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")('my data', fontsize=14, color='red')
    

These properties are covered in more detail in [Text properties and layout](../users/explain/text/text_props.html#text-props).

### Using mathematical expressions in text[#](#using-mathematical-expressions-in-text "Link to this heading")

Matplotlib accepts TeX equation expressions in any text expression. For example to write the expression \\(\sigma_i=15\\) in the title, you can write a TeX expression surrounded by dollar signs:
    
    
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")(r'$\sigma_i=15$')
    

The `r` preceding the title string is important -- it signifies that the string is a _raw_ string and not to treat backslashes as python escapes. matplotlib has a built-in TeX expression parser and layout engine, and ships its own math fonts -- for details see [Writing mathematical expressions](../users/explain/text/mathtext.html#mathtext). Thus, you can use mathematical text across platforms without requiring a TeX installation. For those who have LaTeX and dvipng installed, you can also use LaTeX to format your text and incorporate the output directly into your display figures or saved postscript -- see [Text rendering with LaTeX](../users/explain/text/usetex.html#usetex).

### Annotating text[#](#annotating-text "Link to this heading")

The uses of the basic [`text`](../api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text") function above place text at an arbitrary position on the Axes. A common use for text is to annotate some feature of the plot, and the [`annotate`](../api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate") method provides helper functionality to make annotations easy. In an annotation, there are two points to consider: the location being annotated represented by the argument `xy` and the location of the text `xytext`. Both of these arguments are `(x, y)` tuples.
    
    
    [ax](../api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") = [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")()
    
    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(0.0, 5.0, 0.01)
    [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")(2*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [line](../api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D"), = [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), lw=2)
    
    [plt.annotate](../api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    
    [plt.ylim](../api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")(-2, 2)
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![pyplot](../_images/sphx_glr_pyplot_009.png)

In this basic example, both the `xy` (arrow tip) and `xytext` locations (text location) are in data coordinates. There are a variety of other coordinate systems one can choose -- see [Basic annotation](../users/explain/text/annotations.html#annotations-tutorial) and [Advanced annotation](../users/explain/text/annotations.html#plotting-guide-annotation) for details. More examples can be found in [Annotate plots](../gallery/text_labels_and_annotations/annotation_demo.html).

## Logarithmic and other nonlinear axes[#](#logarithmic-and-other-nonlinear-axes "Link to this heading")

[`matplotlib.pyplot`](../api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot") supports not only linear axis scales, but also logarithmic and logit scales. This is commonly used if data spans many orders of magnitude. Changing the scale of an axis is easy:
    
    
    plt.xscale('log')
    

An example of four plots with the same data and different scales for the y-axis is shown below.
    
    
    # Fixing random state for reproducibility
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")(19680801)
    
    # make up some data in the open interval (0, 1)
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")(loc=0.5, scale=0.4, size=1000)
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") > 0) & ([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") < 1)]
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray").sort()
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") = [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")(len([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")))
    
    # plot with various axes scales
    [plt.figure](../api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")()
    
    # linear
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(221)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [plt.yscale](../api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")('linear')
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('linear')
    [plt.grid](../api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")(True)
    
    # log
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(222)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [plt.yscale](../api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")('log')
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('log')
    [plt.grid](../api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")(True)
    
    # symmetric log
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(223)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") - [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray").mean())
    [plt.yscale](../api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")('symlog', linthresh=0.01)
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('symlog')
    [plt.grid](../api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")(True)
    
    # logit
    [plt.subplot](../api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")(224)
    [plt.plot](../api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"))
    [plt.yscale](../api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")('logit')
    [plt.title](../api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")('logit')
    [plt.grid](../api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")(True)
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    [plt.subplots_adjust](../api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    
    [plt.show](../api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")()
    

![linear, log, symlog, logit](../_images/sphx_glr_pyplot_010.png)

It is also possible to add your own scale, see [`matplotlib.scale`](../api/scale_api.html#module-matplotlib.scale "matplotlib.scale") for details.

**Total running time of the script:** (0 minutes 3.870 seconds)

[`Download Jupyter notebook: pyplot.ipynb`](../_downloads/0e5d53c90d360a55082257e36bfaa2c2/pyplot.ipynb)

[`Download Python source code: pyplot.py`](../_downloads/681f4dd25f8e46fafcfeb15d634a35bf/pyplot.py)

[`Download zipped: pyplot.zip`](../_downloads/953671ad604c4aa1ab001e24866c6505/pyplot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io)

__On this page

  * [Introduction to pyplot](#introduction-to-pyplot)
    * [Formatting the style of your plot](#formatting-the-style-of-your-plot)
  * [Plotting with keyword strings](#plotting-with-keyword-strings)
  * [Plotting with categorical variables](#plotting-with-categorical-variables)
  * [Controlling line properties](#controlling-line-properties)
  * [Working with multiple figures and Axes](#working-with-multiple-figures-and-axes)
  * [Working with text](#working-with-text)
    * [Using mathematical expressions in text](#using-mathematical-expressions-in-text)
    * [Annotating text](#annotating-text)
  * [Logarithmic and other nonlinear axes](#logarithmic-and-other-nonlinear-axes)

© Copyright 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012–2026 The Matplotlib development team.   

Created using [Sphinx](https://www.sphinx-doc.org/) 9.1.0.   

Built from v3.10.9-2-gdf001ac932.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.
