# skill-map: functions — 函数、参数、作用域、lambda、装饰器

## 目标

掌握 Python 函数的定义、调用、参数传递、作用域规则，以及闭包、lambda 和装饰器等高级特性。

## 必知概念

### 函数定义
- **def 语句**：`def function_name(parameters):`
- **文档字符串**：函数定义后的第一个字符串
- **return 语句**：返回值（无 return 则返回 None）
- **函数是对象**：可以赋值给变量、作为参数传递

### 参数类型
| 类型 | 语法 | 说明 |
|------|------|------|
| 位置参数 | `def f(a, b):` | 按顺序传递 |
| 关键字参数 | `f(b=2, a=1)` | 按名称传递 |
| 默认值 | `def f(a=10):` | 不传时使用默认值 |
| *args | `def f(*args):` | 收集位置参数为元组 |
| **kwargs | `def f(**kwargs):` | 收集关键字参数为字典 |
| 仅限关键字 | `def f(*, a):` | a 只能用关键字传递 |

### 作用域（LEGB 规则）
- **Local**：函数内部
- **Enclosing**：外层函数（闭包场景）
- **Global**：模块级别
- **Built-in**：Python 内置

### 闭包
- 内层函数引用了外层函数的变量
- 外层函数返回内层函数
- 内层函数"记住"了外层函数的变量

### Lambda
- 匿名函数：`lambda 参数: 表达式`
- 常配合 `sorted()`, `filter()`, `map()` 使用

### 装饰器
- 接受函数、返回函数的函数
- `@decorator` 语法糖
- `functools.wraps` 保留元信息

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `def` | 定义函数 | `def f(x):` |
| `return` | 返回值 | `return x * 2` |
| `lambda` | 匿名函数 | `lambda x: x * 2` |
| `sorted()` | 排序 | `sorted(lst, key=lambda x: x[1])` |
| `filter()` | 过滤 | `filter(lambda x: x > 0, lst)` |
| `map()` | 映射 | `map(lambda x: x**2, lst)` |
| `functools.wraps` | 保留装饰器元信息 | `@wraps(func)` |

## 常见错误

1. **可变默认参数**
   ```python
   def f(lst=[]):    # 错误！
       lst.append(1)
       return lst
   ```

2. **不理解 *args 和 **kwargs**
   ```python
   def f(*args, **kwargs):
       print(args)     # 元组
       print(kwargs)   # 字典
   ```

3. **闭包变量延迟绑定**
   ```python
   funcs = [lambda: i for i in range(5)]
   [f() for f in funcs]  # 全是 4！
   # 修复：lambda i=i: i
   ```

4. **装饰器丢失元信息**
   ```python
   def decorator(func):
       def wrapper(*args):
           return func(*args)
       return wrapper
   # wrapper 的 __name__ 是 "wrapper"，不是原函数名
   ```

## 训练阶梯

### Step 1: 基本函数（Level 1→2）
- 定义和调用函数
- 使用 return 返回值
- 添加文档字符串

### Step 2: 参数（Level 2）
- 使用位置参数和关键字参数
- 使用默认值
- 使用 *args 和 **kwargs

### Step 3: 作用域（Level 2→3）
- 理解 LEGB 规则
- 使用 global 和 nonlocal
- 避免作用域陷阱

### Step 4: 闭包（Level 3）
- 编写闭包函数
- 理解自由变量
- 解决延迟绑定问题

### Step 5: Lambda（Level 3）
- 编写 lambda 表达式
- 配合 sorted/filter/map 使用

### Step 6: 装饰器（Level 3→4）
- 编写简单装饰器
- 使用 @语法糖
- 使用 functools.wraps
- 编写带参数的装饰器

### Step 7: 综合运用（Level 4→5）
- 设计函数 API
- 使用装饰器实现日志、计时、缓存
- 编写高阶函数

## 掌握标准

- **Level 3**: 能独立定义函数、使用各种参数类型、理解作用域
- **Level 4**: 能编写闭包和装饰器，能使用 lambda 配合内置函数
- **Level 5**: 能设计优雅的函数 API，能编写复杂的高阶函数

## 参考资料

- 菜鸟教程 Python3 函数：https://www.runoob.com/python3/python3-function.html
