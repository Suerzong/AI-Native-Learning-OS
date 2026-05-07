# 优化（`scipy.optimize`） {#optimization-scipy-optimize}

[`scipy.optimize`](../reference/optimize.html#module-scipy.optimize "scipy.optimize") 包提供了几种常用的优化算法。详细列表可在 [`scipy.optimize`](../reference/optimize.html#module-scipy.optimize "scipy.optimize") 获取（也可以通过 `help(scipy.optimize)` 找到）。

## 多元标量函数的局部最小化（`minimize`） {#local-minimization-of-multivariate-scalar-functions-minimize}

[`minimize`](../reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize "scipy.optimize.minimize") 函数为 [`scipy.optimize`](../reference/optimize.html#module-scipy.optimize "scipy.optimize") 中的多元标量函数的无约束和有约束最小化算法提供了通用接口。为了演示最小化函数，考虑最小化 Rosenbrock 函数的问题：

\\[f\left(\mathbf{x}\right)=\sum_{i=1}^{N-1}100\left(x_{i+1}-x_{i}^{2}\right)^{2}+\left(1-x_{i}\right)^{2}.\\]

该函数的最小值为 0，当 \\(x_{i}=1\\) 时达到。

### 无约束最小化 {#unconstrained-minimization}

#### Nelder-Mead 单纯形算法（`method='Nelder-Mead'`） {#nelder-mead-simplex-algorithm}

```python
>>> import numpy as np
>>> from scipy.optimize import minimize

>>> def rosen(x):
...     """Rosenbrock 函数"""
...     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

>>> x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
>>> res = minimize(rosen, x0, method='nelder-mead',
...                options={'xatol': 1e-8, 'disp': True})
Optimization terminated successfully.
         Current function value: 0.000000
         Iterations: 339
         Function evaluations: 571

>>> print(res.x)
[1. 1. 1. 1. 1.]
```

单纯形算法可能是最小化表现良好的函数的最简单方法。它只需要函数求值，对于简单的最小化问题是一个好的选择。但是，因为它不使用任何梯度求值，找到最小值可能需要更长时间。

#### Broyden-Fletcher-Goldfarb-Shanno 算法（`method='BFGS'`） {#bfgs-algorithm}

BFGS 算法是一种拟牛顿方法，使用梯度信息来加速收敛。

```python
>>> def rosen_der(x):
...     """Rosenbrock 函数的导数"""
...     xm = x[1:-1]
...     xm_m1 = x[:-2]
...     xm_p1 = x[2:]
...     der = np.zeros_like(x)
...     der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
...     der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
...     der[-1] = 200*(x[-1]-x[-2]**2)
...     return der

>>> res = minimize(rosen, x0, method='BFGS', jac=rosen_der,
...                options={'disp': True})
```

#### Newton-Conjugate-Gradient 算法（`method='Newton-CG'`） {#newton-conjugate-gradient}

牛顿共轭梯度算法是一种利用 Hessian 矩阵的二阶方法。

```python
>>> def rosen_hess(x):
...     """Rosenbrock 函数的 Hessian 矩阵"""
...     x = np.asarray(x)
...     H = np.diag(-400*x[:-1],1) - np.diag(400*x[:-1],-1)
...     diagonal = np.zeros_like(x)
...     diagonal[0] = 1200*x[0]**2-400*x[1]+2
...     diagonal[-1] = 200
...     diagonal[1:-1] = 202 + 1200*x[1:-1]**2 - 400*x[2:]
...     H = H + np.diag(diagonal)
...     return H

>>> res = minimize(rosen, x0, method='Newton-CG',
...                jac=rosen_der, hess=rosen_hess,
...                options={'disp': True})
```

### 有约束最小化 {#constrained-minimization}

#### 信赖域约束算法（`method='trust-constr'`） {#trust-region-constrained}

```python
>>> from scipy.optimize import LinearConstraint, NonlinearConstraint

>>> # 线性约束: 1 <= x[0] + x[1] <= 3
>>> linear_constraint = LinearConstraint([[1, 1]], 1, 3)

>>> # 非线性约束
>>> def cons_f(x):
...     return [x[0]**2 + x[1], x[0]**2 - x[1]]
>>> def cons_J(x):
...     return [[2*x[0], 1], [2*x[0], -1]]
>>> nonlinear_constraint = NonlinearConstraint(cons_f, -np.inf, 1, jac=cons_J)

>>> res = minimize(rosen, x0, method='trust-constr',
...                constraints=[linear_constraint, nonlinear_constraint])
```

#### 序列最小二乘规划（SLSQP）算法（`method='SLSQP'`） {#slspp-algorithm}

```python
>>> # 定义约束
>>> cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 2 * x[1] + 2},
...         {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
...         {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

>>> res = minimize(rosen, x0, method='SLSQP',
...                constraints=cons,
...                options={'disp': True})
```

## 全局优化 {#global-optimization}

SciPy 提供了多种全局优化算法：

### 差分进化（`differential_evolution`） {#differential-evolution}

```python
>>> from scipy.optimize import differential_evolution

>>> bounds = [(0, 2), (0, 2)]
>>> result = differential_evolution(rosen, bounds)
```

### 双退火（`dual_annealing`） {#dual-annealing}

```python
>>> from scipy.optimize import dual_annealing

>>> result = dual_annealing(rosen, bounds)
```

### shgo（简单同调全局优化） {#shgo}

```python
>>> from scipy.optimize import shgo

>>> result = shgo(rosen, bounds)
```

## 最小二乘最小化（`least_squares`） {#least-squares-minimization}

[`least_squares`](../reference/generated/scipy.optimize.least_squares.html#scipy.optimize.least_squares "scipy.optimize.least_squares") 函数用于解决非线性最小二乘问题。

```python
>>> from scipy.optimize import least_squares

>>> def fun(x, t, y):
...     return x[0] * np.exp(x[1] * t) - y

>>> t = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
>>> y = np.array([6.0, 4.5, 3.5, 2.8, 2.3, 2.0])
>>> x0 = np.array([1.0, -0.5])
>>> res = least_squares(fun, x0, args=(t, y))
>>> print(res.x)
```

## 单变量函数最小化器（`minimize_scalar`） {#univariate-function-minimizers-minimize-scalar}

对于单变量函数的最小化，使用 [`minimize_scalar`](../reference/generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar "scipy.optimize.minimize_scalar")。

```python
>>> from scipy.optimize import minimize_scalar

>>> def f(x):
...     return (x - 2) ** 2 + 1

>>> res = minimize_scalar(f)
>>> res.x
2.0
>>> res.fun
1.0
```

### 有界最小化（`method='bounded'`） {#bounded-minimization}

```python
>>> res = minimize_scalar(f, bounds=(0, 3), method='bounded')
```

## 求根（Root finding） {#root-finding}

### 标量函数 {#scalar-functions}

使用 [`root_scalar`](../reference/generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar "scipy.optimize.root_scalar") 求标量函数的根。

```python
>>> from scipy.optimize import root_scalar

>>> def f(x):
...     return x ** 2 - 1

>>> root = root_scalar(f, bracket=[0, 3])
>>> root.root
1.0
```

### 方程组 {#sets-of-equations}

使用 [`root`](../reference/generated/scipy.optimize.root.html#scipy.optimize.root "scipy.optimize.root") 求方程组的根。

```python
>>> from scipy.optimize import root

>>> def func(x):
...     return [x[0] * np.cos(x[1]) - 4,
...             x[1]*x[0] - x[1] - 5]

>>> sol = root(func, [1, 1])
>>> sol.x
```

### 不动点求解 {#fixed-point-solving}

使用 [`fixed_point`](../reference/generated/scipy.optimize.fixed_point.html#scipy.optimize.fixed_point "scipy.optimize.fixed_point") 求不动点。

```python
>>> from scipy.optimize import fixed_point

>>> def func(x, c):
...     return x ** 2 + c

>>> result = fixed_point(func, 1.0, args=(1,))
```

## 线性规划（`linprog`） {#linear-programming-linprog}

[`linprog`](../reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog "scipy.optimize.linprog") 用于解决线性规划问题。

```python
>>> from scipy.optimize import linprog

>>> c = [-1, 4]
>>> A = [[-3, 1], [1, 2]]
>>> b = [6, 4]
>>> x0_bounds = (None, None)
>>> x1_bounds = (None, None)
>>> res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
>>> res.x
```

## 分配问题 {#assignment-problems}

使用 [`linear_sum_assignment`](../reference/generated/scipy.optimize.linear_sum_assignment.html#scipy.optimize.linear_sum_assignment "scipy.optimize.linear_sum_assignment") 解决线性和分配问题。

```python
>>> from scipy.optimize import linear_sum_assignment

>>> cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
>>> row_ind, col_ind = linear_sum_assignment(cost)
>>> cost[row_ind, col_ind].sum()
```

## 混合整数线性规划 {#mixed-integer-linear-programming}

使用 [`milp`](../reference/generated/scipy.optimize.milp.html#scipy.optimize.milp "scipy.optimize.milp") 解决混合整数线性规划问题。

```python
>>> from scipy.optimize import milp, LinearConstraint, Bounds

>>> c = -np.ones(2)
>>> constraints = LinearConstraint(np.ones(2), lb=1)
>>> integrality = np.ones(2)
>>> res = milp(c, constraints=constraints, integrality=integrality)
```
