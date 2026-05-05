# skill-map: advanced — 生成器、迭代器、上下文管理器、并发基础

## 目标

掌握 Python 的高级特性，包括惰性求值（生成器）、迭代器协议、上下文管理器和基本并发概念。这些是高效 Python 编程和数据处理的基础。

## 必知概念

### 生成器（Generator）
- **惰性求值**：按需生成值，不一次性占用内存
- **yield**：暂停函数并返回值，下次调用时继续
- **生成器函数**：包含 yield 的函数
- **生成器表达式**：`(x for x in iterable)`，类似列表推导式但返回生成器
- **send()**：向生成器发送值
- **StopIteration**：生成器耗尽时自动抛出

### 迭代器（Iterator）
- **迭代器协议**：实现 `__iter__()` 和 `__next__()` 方法
- **可迭代对象**：实现 `__iter__()` 的对象
- **iter()**：将可迭代对象转为迭代器
- **next()**：获取下一个值

### 上下文管理器（Context Manager）
- **with 语句**：自动管理资源的进入和退出
- **__enter__**：进入 with 块时调用
- **__exit__**：退出 with 块时调用（无论是否异常）
- **contextlib.contextmanager**：装饰器简化编写

### 并发基础
- **GIL**：Global Interpreter Lock，限制同一时刻只有一个线程执行 Python 字节码
- **threading**：线程，适用于 I/O 密集型任务
- **multiprocessing**：进程，适用于 CPU 密集型任务
- **concurrent.futures**：高级并发接口（ThreadPoolExecutor, ProcessPoolExecutor）

### 常用 itertools 函数
| 函数 | 用途 | 示例 |
|------|------|------|
| `chain()` | 连接多个迭代器 | `chain([1,2], [3,4])` → 1,2,3,4 |
| `islice()` | 切片迭代器 | `islice(range(10), 2, 8, 2)` → 2,4,6 |
| `product()` | 笛卡尔积 | `product([1,2], ['a','b'])` |
| `permutations()` | 排列 | `permutations([1,2,3], 2)` |
| `combinations()` | 组合 | `combinations([1,2,3], 2)` |
| `groupby()` | 分组 | `groupby(sorted_data, key)` |
| `cycle()` | 无限循环 | `cycle([1,2,3])` → 1,2,3,1,2,3,... |
| `repeat()` | 重复 | `repeat(5, 3)` → 5,5,5 |

## 常见错误

1. **生成器只能遍历一次**
   ```python
   gen = (x for x in range(5))
   list(gen)  # [0, 1, 2, 3, 4]
   list(gen)  # [] ！已经耗尽了
   ```

2. **混淆生成器和列表**
   ```python
   gen = (x for x in range(1000000))
   len(gen)  # TypeError! 生成器没有长度
   gen[0]    # TypeError! 生成器不支持索引
   ```

3. **yield vs return**
   ```python
   def gen():
       yield 1
       yield 2
       return 3  # return 在生成器中表示结束，值是 StopIteration 的 value

   g = gen()
   next(g)  # 1
   next(g)  # 2
   next(g)  # StopIteration: 3
   ```

4. **GIL 的误解**
   ```python
   # threading 不会加速 CPU 密集型任务！
   import threading
   def cpu_work():
       total = 0
       for i in range(10**7):
           total += i
   # 多线程跑 cpu_work 不会比单线程快
   # 应该用 multiprocessing
   ```

5. **上下文管理器忘记处理异常**
   ```python
   class MyContext:
       def __exit__(self, exc_type, exc_val, exc_tb):
           return True  # 吞掉所有异常！
   ```

## 训练阶梯

### Step 1: 生成器基础（Level 3→4）
- 编写生成器函数（使用 yield）
- 理解惰性求值
- 使用生成器表达式

### Step 2: 迭代器协议（Level 4）
- 实现 __iter__/__next__
- 理解可迭代对象 vs 迭代器
- 使用 iter() 和 next()

### Step 3: 上下文管理器（Level 4）
- 使用 with 语句
- 编写 __enter__/__exit__
- 使用 contextlib.contextmanager

### Step 4: itertools（Level 4）
- 使用 chain/islice/product
- 使用 combinations/permutations
- 使用 groupby

### Step 5: 并发基础（Level 4→5）
- 理解 GIL 的影响
- 使用 threading（I/O 密集型）
- 使用 multiprocessing（CPU 密集型）
- 使用 concurrent.futures

### Step 6: 综合运用（Level 5）
- 处理大文件（生成器逐行读取）
- 实现自定义迭代器
- 设计上下文管理器管理资源
- 并行处理数据

## 掌握标准

- **Level 4**: 能编写生成器和上下文管理器，理解迭代器协议
- **Level 5**: 能设计高效的惰性数据处理流程，能合理使用并发

## 参考资料

- 菜鸟教程 Python3 生成器：https://www.runoob.com/python3/python3-iterator-generator.html
- Python 官方文档 itertools：https://docs.python.org/3/library/itertools.html
- Python 官方文档 concurrent.futures：https://docs.python.org/3/library/concurrent.futures.html
