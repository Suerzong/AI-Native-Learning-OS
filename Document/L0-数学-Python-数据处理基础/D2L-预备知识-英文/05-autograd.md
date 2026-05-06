# 2.5. Automatic Differentiation

Recall from [Section 2.4](calculus.html#sec-calculus) that calculating derivatives is the crucial step in all the optimization algorithms that we will use to train deep networks. While the calculations are straightforward, working them out by hand can be tedious and error-prone, and these issues only grow as our models become more complex.

Fortunately all modern deep learning frameworks take this work off our plates by offering _automatic differentiation_ (often shortened to _autograd_). As we pass data through each successive function, the framework builds a _computational graph_ that tracks how each value depends on others. To calculate derivatives, automatic differentiation works backwards through this graph applying the chain rule. The computational algorithm for applying the chain rule in this fashion is called _backpropagation_.

While autograd libraries have become a hot concern over the past decade, they have a long history. In fact the earliest references to autograd date back over half of a century ([Wengert, 1964](../chapter_references/zreferences.html#id312 "Wengert, R. E. \(1964\). A simple automatic derivative evaluation program. Communications of the ACM, 7\(8\), 463–464.")). The core ideas behind modern backpropagation date to a PhD thesis from 1980 ([Speelpenning, 1980](../chapter_references/zreferences.html#id263 "Speelpenning, B. \(1980\). Compiling fast partial derivatives of functions given by algorithms \(Doctoral dissertation\). University of Illinois at Urbana-Champaign.")) and were further developed in the late 1980s ([Griewank, 1989](../chapter_references/zreferences.html#id98 "Griewank, A. \(1989\). On automatic differentiation. Mathematical Programming: Recent Developments and Applications \(pp. 83–107\). Kluwer.")). While backpropagation has become the default method for computing gradients, it is not the only option. For instance, the Julia programming language employs forward propagation ([Revels _et al._ , 2016](../chapter_references/zreferences.html#id236 "Revels, J., Lubin, M., & Papamarkou, T. \(2016\). Forward-mode automatic differentiation in Julia. ArXiv:1607.07892.")). Before exploring methods, let’s first master the autograd package.

    import torch

    from mxnet import autograd, np, npx

    npx.set_np()

    from jax import numpy as jnp

    import tensorflow as tf

## 2.5.1. A Simple Function

Let’s assume that we are interested in differentiating the function \\(y = 2\mathbf{x}^{\top}\mathbf{x}\\) with respect to the column vector \\(\mathbf{x}\\). To start, we assign `x` an initial value.

    x = torch.arange(4.0)
    x

    tensor([0., 1., 2., 3.])

Before we calculate the gradient of \\(y\\) with respect to \\(\mathbf{x}\\), we need a place to store it. In general, we avoid allocating new memory every time we take a derivative because deep learning requires successively computing derivatives with respect to the same parameters a great many times, and we might risk running out of memory. Note that the gradient of a scalar-valued function with respect to a vector \\(\mathbf{x}\\) is vector-valued with the same shape as \\(\mathbf{x}\\).

    # Can also create x = torch.arange(4.0, requires_grad=True)
    x.requires_grad_(True)
    x.grad  # The gradient is None by default

    x = np.arange(4.0)
    x

    [22:07:05] ../src/storage/storage.cc:196: Using Pooled (Naive) StorageManager for CPU

    array([0., 1., 2., 3.])

Before we calculate the gradient of \\(y\\) with respect to \\(\mathbf{x}\\), we need a place to store it. In general, we avoid allocating new memory every time we take a derivative because deep learning requires successively computing derivatives with respect to the same parameters a great many times, and we might risk running out of memory. Note that the gradient of a scalar-valued function with respect to a vector \\(\mathbf{x}\\) is vector-valued with the same shape as \\(\mathbf{x}\\).

    # We allocate memory for a tensor's gradient by invoking `attach_grad`
    x.attach_grad()
    # After we calculate a gradient taken with respect to `x`, we will be able to
    # access it via the `grad` attribute, whose values are initialized with 0s
    x.grad

    array([0., 0., 0., 0.])

    x = jnp.arange(4.0)
    x

    No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)

    Array([0., 1., 2., 3.], dtype=float32)

    x = tf.range(4, dtype=tf.float32)
    x

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 1., 2., 3.], dtype=float32)>

Before we calculate the gradient of \\(y\\) with respect to \\(\mathbf{x}\\), we need a place to store it. In general, we avoid allocating new memory every time we take a derivative because deep learning requires successively computing derivatives with respect to the same parameters a great many times, and we might risk running out of memory. Note that the gradient of a scalar-valued function with respect to a vector \\(\mathbf{x}\\) is vector-valued with the same shape as \\(\mathbf{x}\\).

    x = tf.Variable(x)

We now calculate our function of `x` and assign the result to `y`.

    y = 2 * torch.dot(x, x)
    y

    tensor(28., grad_fn=<MulBackward0>)

We can now take the gradient of `y` with respect to `x` by calling its `backward` method. Next, we can access the gradient via `x`’s `grad` attribute.

    y.backward()
    x.grad

    tensor([ 0.,  4.,  8., 12.])

    # Our code is inside an `autograd.record` scope to build the computational
    # graph
    with autograd.record():
        y = 2 * np.dot(x, x)
    y

    array(28.)

We can now take the gradient of `y` with respect to `x` by calling its `backward` method. Next, we can access the gradient via `x`’s `grad` attribute.

    y.backward()
    x.grad

    [22:07:05] ../src/base.cc:48: GPU context requested, but no GPUs found.

    array([ 0.,  4.,  8., 12.])

    y = lambda x: 2 * jnp.dot(x, x)
    y(x)

    Array(28., dtype=float32)

We can now take the gradient of `y` with respect to `x` by passing through the `grad` transform.

    from jax import grad

    # The `grad` transform returns a Python function that
    # computes the gradient of the original function
    x_grad = grad(y)(x)
    x_grad

    Array([ 0.,  4.,  8., 12.], dtype=float32)

    # Record all computations onto a tape
    with tf.GradientTape() as t:
        y = 2 * tf.tensordot(x, x, axes=1)
    y

    <tf.Tensor: shape=(), dtype=float32, numpy=28.0>

We can now calculate the gradient of `y` with respect to `x` by calling the `gradient` method.

    x_grad = t.gradient(y, x)
    x_grad

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([ 0.,  4.,  8., 12.], dtype=float32)>

We already know that the gradient of the function \\(y = 2\mathbf{x}^{\top}\mathbf{x}\\) with respect to \\(\mathbf{x}\\) should be \\(4\mathbf{x}\\). We can now verify that the automatic gradient computation and the expected result are identical.

    x.grad == 4 * x

    tensor([True, True, True, True])

Now let’s calculate another function of `x` and take its gradient. Note that PyTorch does not automatically reset the gradient buffer when we record a new gradient. Instead, the new gradient is added to the already-stored gradient. This behavior comes in handy when we want to optimize the sum of multiple objective functions. To reset the gradient buffer, we can call `x.grad.zero_()` as follows:

    x.grad.zero_()  # Reset the gradient
    y = x.sum()
    y.backward()
    x.grad

    tensor([1., 1., 1., 1.])

    x.grad == 4 * x

    array([ True,  True,  True,  True])

Now let’s calculate another function of `x` and take its gradient. Note that MXNet resets the gradient buffer whenever we record a new gradient.

    with autograd.record():
        y = x.sum()
    y.backward()
    x.grad  # Overwritten by the newly calculated gradient

    array([1., 1., 1., 1.])

    x_grad == 4 * x

    Array([ True,  True,  True,  True], dtype=bool)

    y = lambda x: x.sum()
    grad(y)(x)

    Array([1., 1., 1., 1.], dtype=float32)

    x_grad == 4 * x

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

Now let’s calculate another function of `x` and take its gradient. Note that TensorFlow resets the gradient buffer whenever we record a new gradient.

    with tf.GradientTape() as t:
        y = tf.reduce_sum(x)
    t.gradient(y, x)  # Overwritten by the newly calculated gradient

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([1., 1., 1., 1.], dtype=float32)>

## 2.5.2. Backward for Non-Scalar Variables

When `y` is a vector, the most natural representation of the derivative of `y` with respect to a vector `x` is a matrix called the _Jacobian_ that contains the partial derivatives of each component of `y` with respect to each component of `x`. Likewise, for higher-order `y` and `x`, the result of differentiation could be an even higher-order tensor.

While Jacobians do show up in some advanced machine learning techniques, more commonly we want to sum up the gradients of each component of `y` with respect to the full vector `x`, yielding a vector of the same shape as `x`. For example, we often have a vector representing the value of our loss function calculated separately for each example among a _batch_ of training examples. Here, we just want to sum up the gradients computed individually for each example.

Because deep learning frameworks vary in how they interpret gradients of non-scalar tensors, PyTorch takes some steps to avoid confusion. Invoking `backward` on a non-scalar elicits an error unless we tell PyTorch how to reduce the object to a scalar. More formally, we need to provide some vector \\(\mathbf{v}\\) such that `backward` will compute \\(\mathbf{v}^\top \partial_{\mathbf{x}} \mathbf{y}\\) rather than \\(\partial_{\mathbf{x}} \mathbf{y}\\). This next part may be confusing, but for reasons that will become clear later, this argument (representing \\(\mathbf{v}\\)) is named `gradient`. For a more detailed description, see Yang Zhang’s [Medium post](https://zhang-yang.medium.com/the-gradient-argument-in-pytorchs-backward-function-explained-by-examples-68f266950c29).

    x.grad.zero_()
    y = x * x
    y.backward(gradient=torch.ones(len(y)))  # Faster: y.sum().backward()
    x.grad

    tensor([0., 2., 4., 6.])

MXNet handles this problem by reducing all tensors to scalars by summing before computing a gradient. In other words, rather than returning the Jacobian \\(\partial_{\mathbf{x}} \mathbf{y}\\), it returns the gradient of the sum \\(\partial_{\mathbf{x}} \sum_i y_i\\).

    with autograd.record():
        y = x * x
    y.backward()
    x.grad  # Equals the gradient of y = sum(x * x)

    array([0., 2., 4., 6.])

    y = lambda x: x * x
    # grad is only defined for scalar output functions
    grad(lambda x: y(x).sum())(x)

    Array([0., 2., 4., 6.], dtype=float32)

By default, TensorFlow returns the gradient of the sum. In other words, rather than returning the Jacobian \\(\partial_{\mathbf{x}} \mathbf{y}\\), it returns the gradient of the sum \\(\partial_{\mathbf{x}} \sum_i y_i\\).

    with tf.GradientTape() as t:
        y = x * x
    t.gradient(y, x)  # Same as y = tf.reduce_sum(x * x)

    <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 2., 4., 6.], dtype=float32)>

## 2.5.3. Detaching Computation

Sometimes, we wish to move some calculations outside of the recorded computational graph. For example, say that we use the input to create some auxiliary intermediate terms for which we do not want to compute a gradient. In this case, we need to _detach_ the respective computational graph from the final result. The following toy example makes this clearer: suppose we have `z = x * y` and `y = x * x` but we want to focus on the _direct_ influence of `x` on `z` rather than the influence conveyed via `y`. In this case, we can create a new variable `u` that takes the same value as `y` but whose _provenance_ (how it was created) has been wiped out. Thus `u` has no ancestors in the graph and gradients do not flow through `u` to `x`. For example, taking the gradient of `z = x * u` will yield the result `u`, (not `3 * x * x` as you might have expected since `z = x * x * x`).

    x.grad.zero_()
    y = x * x
    u = y.detach()
    z = u * x

    z.sum().backward()
    x.grad == u

    tensor([True, True, True, True])

    with autograd.record():
        y = x * x
        u = y.detach()
        z = u * x
    z.backward()
    x.grad == u

    array([ True,  True,  True,  True])

    import jax

    y = lambda x: x * x
    # jax.lax primitives are Python wrappers around XLA operations
    u = jax.lax.stop_gradient(y(x))
    z = lambda x: u * x

    grad(lambda x: z(x).sum())(x) == y(x)

    Array([ True,  True,  True,  True], dtype=bool)

    # Set persistent=True to preserve the compute graph.
    # This lets us run t.gradient more than once
    with tf.GradientTape(persistent=True) as t:
        y = x * x
        u = tf.stop_gradient(y)
        z = u * x

    x_grad = t.gradient(z, x)
    x_grad == u

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

Note that while this procedure detaches `y`’s ancestors from the graph leading to `z`, the computational graph leading to `y` persists and thus we can calculate the gradient of `y` with respect to `x`.

    x.grad.zero_()
    y.sum().backward()
    x.grad == 2 * x

    tensor([True, True, True, True])

    y.backward()
    x.grad == 2 * x

    array([ True,  True,  True,  True])

    grad(lambda x: y(x).sum())(x) == 2 * x

    Array([ True,  True,  True,  True], dtype=bool)

    t.gradient(y, x) == 2 * x

    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True,  True,  True,  True])>

## 2.5.4. Gradients and Python Control Flow

So far we reviewed cases where the path from input to output was well defined via a function such as `z = x * x * x`. Programming offers us a lot more freedom in how we compute results. For instance, we can make them depend on auxiliary variables or condition choices on intermediate results. One benefit of using automatic differentiation is that even if building the computational graph of a function required passing through a maze of Python control flow (e.g., conditionals, loops, and arbitrary function calls), we can still calculate the gradient of the resulting variable. To illustrate this, consider the following code snippet where the number of iterations of the `while` loop and the evaluation of the `if` statement both depend on the value of the input `a`.

    def f(a):
        b = a * 2
        while b.norm() < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while np.linalg.norm(b) < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while jnp.linalg.norm(b) < 1000:
            b = b * 2
        if b.sum() > 0:
            c = b
        else:
            c = 100 * b
        return c

    def f(a):
        b = a * 2
        while tf.norm(b) < 1000:
            b = b * 2
        if tf.reduce_sum(b) > 0:
            c = b
        else:
            c = 100 * b
        return c

Below, we call this function, passing in a random value, as input. Since the input is a random variable, we do not know what form the computational graph will take. However, whenever we execute `f(a)` on a specific input, we realize a specific computational graph and can subsequently run `backward`.

    a = torch.randn(size=(), requires_grad=True)
    d = f(a)
    d.backward()

    a = np.random.normal()
    a.attach_grad()
    with autograd.record():
        d = f(a)
    d.backward()

    from jax import random

    a = random.normal(random.PRNGKey(1), ())
    d = f(a)
    d_grad = grad(f)(a)

    a = tf.Variable(tf.random.normal(shape=()))
    with tf.GradientTape() as t:
        d = f(a)
    d_grad = t.gradient(d, a)
    d_grad

    <tf.Tensor: shape=(), dtype=float32, numpy=2048.0>

Even though our function `f` is, for demonstration purposes, a bit contrived, its dependence on the input is quite simple: it is a _linear_ function of `a` with piecewise defined scale. As such, `f(a) / a` is a vector of constant entries and, moreover, `f(a) / a` needs to match the gradient of `f(a)` with respect to `a`.

    a.grad == d / a

    tensor(True)

    a.grad == d / a

    array(True)

    d_grad == d / a

    Array(True, dtype=bool)

    d_grad == d / a

    <tf.Tensor: shape=(), dtype=bool, numpy=True>

Dynamic control flow is very common in deep learning. For instance, when processing text, the computational graph depends on the length of the input. In these cases, automatic differentiation becomes vital for statistical modeling since it is impossible to compute the gradient _a priori_.

## 2.5.5. Discussion

You have now gotten a taste of the power of automatic differentiation. The development of libraries for calculating derivatives both automatically and efficiently has been a massive productivity booster for deep learning practitioners, liberating them so they can focus on less menial. Moreover, autograd lets us design massive models for which pen and paper gradient computations would be prohibitively time consuming. Interestingly, while we use autograd to _optimize_ models (in a statistical sense) the _optimization_ of autograd libraries themselves (in a computational sense) is a rich subject of vital interest to framework designers. Here, tools from compilers and graph manipulation are leveraged to compute results in the most expedient and memory-efficient manner.

For now, try to remember these basics: (i) attach gradients to those variables with respect to which we desire derivatives; (ii) record the computation of the target value; (iii) execute the backpropagation function; and (iv) access the resulting gradient.

## 2.5.6. Exercises

  1. Why is the second derivative much more expensive to compute than the first derivative?

  2. After running the function for backpropagation, immediately run it again and see what happens. Investigate.

  3. In the control flow example where we calculate the derivative of `d` with respect to `a`, what would happen if we changed the variable `a` to a random vector or a matrix? At this point, the result of the calculation `f(a)` is no longer a scalar. What happens to the result? How do we analyze this?

  4. Let \\(f(x) = \sin(x)\\). Plot the graph of \\(f\\) and of its derivative \\(f'\\). Do not exploit the fact that \\(f'(x) = \cos(x)\\) but rather use automatic differentiation to get the result.

  5. Let \\(f(x) = ((\log x^2) \cdot \sin x) + x^{-1}\\). Write out a dependency graph tracing results from \\(x\\) to \\(f(x)\\).

  6. Use the chain rule to compute the derivative \\(\frac{df}{dx}\\) of the aforementioned function, placing each term on the dependency graph that you constructed previously.

  7. Given the graph and the intermediate derivative results, you have a number of options when computing the gradient. Evaluate the result once starting from \\(x\\) to \\(f\\) and once from \\(f\\) tracing back to \\(x\\). The path from \\(x\\) to \\(f\\) is commonly known as _forward differentiation_ , whereas the path from \\(f\\) to \\(x\\) is known as backward differentiation.

  8. When might you want to use forward, and when backward, differentiation? Hint: consider the amount of intermediate data needed, the ability to parallelize steps, and the size of matrices and vectors involved.

[Discussions](https://discuss.d2l.ai/t/35)

[Discussions](https://discuss.d2l.ai/t/34)

[Discussions](https://discuss.d2l.ai/t/17970)

[Discussions](https://discuss.d2l.ai/t/200)

Table Of Contents

  * 2.5. Automatic Differentiation
    * 2.5.1. A Simple Function
    * 2.5.2. Backward for Non-Scalar Variables
    * 2.5.3. Detaching Computation
    * 2.5.4. Gradients and Python Control Flow
    * 2.5.5. Discussion
    * 2.5.6. Exercises

