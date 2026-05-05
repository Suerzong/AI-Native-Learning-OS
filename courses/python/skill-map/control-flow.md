# skill-map: control-flow — 条件、循环、异常处理

## 目标

掌握 Python 的条件语句、循环结构和基本异常处理，能控制程序的执行流程。

## 必知概念

### 条件语句
- **if/elif/else**：条件分支
- **缩进**：Python 用缩进定义代码块（4 个空格）
- **条件表达式**：必须是布尔值或可转换为布尔值
- **Truthy/Falsy**：
  - Falsy: `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None`, `False`
  - 其他所有值均为 Truthy
- **三元表达式**：`x if condition else y`
- **链式比较**：`1 < x < 10`

### 循环
- **for 循环**：遍历可迭代对象
- **while 循环**：条件为 True 时重复执行
- **range()**：生成整数序列
  - `range(stop)` — 0 到 stop-1
  - `range(start, stop)` — start 到 stop-1
  - `range(start, stop, step)` — 指定步长
- **break**：跳出当前循环
- **continue**：跳到下一次迭代
- **else 子句**：循环正常结束（非 break）时执行
- **enumerate()**：同时获取索引和值

### 异常处理基础
- **try/except**：捕获异常
- **try/except/else**：else 在无异常时执行
- **try/except/finally**：finally 始终执行
- **常见异常**：ValueError, TypeError, IndexError, KeyError, ZeroDivisionError

## 必知函数/API

| 函数/语句 | 用途 | 示例 |
|-----------|------|------|
| `if/elif/else` | 条件分支 | `if x > 0:` |
| `for` | 遍历循环 | `for i in range(10):` |
| `while` | 条件循环 | `while x > 0:` |
| `range()` | 整数序列 | `range(0, 10, 2)` |
| `enumerate()` | 索引+值 | `for i, v in enumerate(lst):` |
| `break` | 跳出循环 | |
| `continue` | 跳过本次 | |
| `try/except` | 异常捕获 | `except ValueError:` |

## 常见错误

1. **range() 起止值错误**
   ```python
   for i in range(10):  # 0,1,2,...,9 （不含 10！）
   ```

2. **在循环中修改列表**
   ```python
   for x in lst:
       lst.remove(x)  # 可能跳过元素
   ```

3. **except 过于宽泛**
   ```python
   try:
       risky()
   except:      # 不好：捕获所有异常，包括 KeyboardInterrupt
       pass
   ```

4. **while 死循环**
   ```python
   while x > 0:
       print(x)  # 忘记修改 x，导致无限循环
   ```

## 训练阶梯

### Step 1: 简单条件（Level 1→2）
- 编写 if/else 判断
- 使用比较运算符

### Step 2: 复杂条件（Level 2）
- 使用 elif 多分支
- 使用 and/or 组合条件
- 使用三元表达式

### Step 3: for 循环（Level 2）
- 使用 range() 遍历
- 遍历列表/字符串
- 使用 enumerate()

### Step 4: while 循环（Level 2→3）
- 编写条件循环
- 使用 break/continue
- 避免死循环

### Step 5: 嵌套循环（Level 3）
- 编写嵌套 for 循环
- 打印九九乘法表
- 理解循环的 else 子句

### Step 6: 异常处理（Level 3）
- 使用 try/except 捕获特定异常
- 使用 finally 确保资源释放
- 处理用户输入异常

### Step 7: 综合运用（Level 3→4）
- 编写猜数字游戏
- 编写菜单驱动程序
- 编写带异常处理的数据验证

## 掌握标准

- **Level 3**: 能独立编写条件判断和循环，能处理常见异常
- **Level 4**: 能选择合适的循环类型，能合理使用异常处理
- **Level 5**: 能预判边界情况，能编写健壮的控制流代码

## 参考资料

- 菜鸟教程 Python3 条件控制：https://www.runoob.com/python3/python3-conditioanal.html
- 菜鸟教程 Python3 循环语句：https://www.runoob.com/python3/python3-loop.html
