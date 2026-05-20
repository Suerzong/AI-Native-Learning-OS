# 键盘输入数学公式约定

本课程允许学生用普通键盘输入数学表达式，不强制完整 LaTeX。

## 极限

| 数学写法 | 可输入 |
|---|---|
| lim x->0 f(x) | `lim x->0 f(x)` |
| lim n->inf a_n | `lim n->inf a_n` |
| x -> a+ | `x->a+` |
| x -> a- | `x->a-` |

## 求导与微分

| 数学写法 | 可输入 |
|---|---|
| dy/dx | `dy/dx` |
| d/dx f(x) | `d/dx f(x)` |
| f'(x), f''(x) | `f'(x)`, `f''(x)` |
| partial f / partial x | `df/dx` 或 `partial f/partial x` |
| 全微分 | `df = f_x dx + f_y dy` |

## 积分

| 数学写法 | 可输入 |
|---|---|
| int f(x) dx | `int f(x) dx` |
| int_0^1 x^2 dx | `int_0^1 x^2 dx` |
| double integral over D | `intint_D f(x,y) dA` |
| line integral | `int_C f ds` 或 `int_C P dx + Q dy` |

## 级数

| 数学写法 | 可输入 |
|---|---|
| sum n=1..inf a_n | `sum n=1..inf a_n` |
| sum n=0..inf c_n (x-a)^n | `sum n=0..inf c_n (x-a)^n` |
| 收敛半径 | `R` |

## 常用符号

| 含义 | 可输入 |
|---|---|
| 无穷大 | `inf` |
| 属于 | `in` |
| 不属于 | `notin` |
| 任意 | `forall` |
| 存在 | `exists` |
| 小于等于 | `<=` |
| 大于等于 | `>=` |
| 不等于 | `!=` |

## 作答格式

推荐使用：

```text
方法：先判断...
条件：需要...
计算：
1. ...
2. ...
结论：...
```

如果不会完整计算，可以先写“方法 + 定理条件 + 卡住的位置”。教学 agent 应先纠正思路，再处理计算。

