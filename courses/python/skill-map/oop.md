# skill-map: oop — 类、继承、多态、魔法方法

## 目标

掌握 Python 面向对象编程，能设计类、实现继承、使用魔法方法，为后续框架使用和库扩展打下基础。

## 必知概念

### 类与对象
- **类**：对象的蓝图，定义属性和方法
- **对象/实例**：类的具体实例
- **self**：实例方法的第一个参数，指向调用者
- **实例属性**：每个对象独有的数据
- **类属性**：所有对象共享的数据

### 方法类型
| 类型 | 装饰器 | 第一个参数 | 调用方式 |
|------|--------|-----------|----------|
| 实例方法 | 无 | self | `obj.method()` |
| 类方法 | @classmethod | cls | `Class.method()` |
| 静态方法 | @staticmethod | 无 | `Class.method()` |
| 属性方法 | @property | self | `obj.prop` |

### 继承
- **单继承**：`class Child(Parent):`
- **多继承**：`class Child(P1, P2, P3):`
- **MRO**：方法解析顺序（C3 线性化）
- **super()**：调用父类方法
- **方法重写**：子类重新定义父类方法

### 多态
- 不同类的对象对同一方法有不同的实现
- 鸭子类型："如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子"

### 魔法方法
| 方法 | 触发时机 | 用途 |
|------|----------|------|
| `__init__` | 创建实例 | 初始化属性 |
| `__str__` | print(obj) | 用户友好的字符串 |
| `__repr__` | repr(obj) | 开发者友好的字符串 |
| `__len__` | len(obj) | 定义长度 |
| `__eq__` | obj == other | 相等比较 |
| `__lt__` | obj < other | 小于比较 |
| `__add__` | obj + other | 加法 |
| `__getitem__` | obj[key] | 索引访问 |
| `__setitem__` | obj[key] = val | 索引赋值 |
| `__contains__` | x in obj | 成员检查 |
| `__iter__` | for x in obj | 迭代 |
| `__call__` | obj() | 使对象可调用 |
| `__enter__/__exit__` | with obj: | 上下文管理 |

## 常见错误

1. **忘记 self**
   ```python
   class Dog:
       def bark():      # 缺少 self 参数
           print("woof")
   Dog().bark()  # TypeError
   ```

2. **__init__ 忘记返回 None**
   ```python
   class Foo:
       def __init__(self):
           return 42  # TypeError! __init__ 必须返回 None
   ```

3. **类属性 vs 实例属性混淆**
   ```python
   class Foo:
       lst = []       # 类属性，所有实例共享
   a = Foo()
   b = Foo()
   a.lst.append(1)
   print(b.lst)  # [1]！b 也被影响了
   ```

4. **super() 在多继承中的使用**
   ```python
   # 不要跳过中间类
   class A: pass
   class B(A): pass
   class C(A): pass
   class D(B, C): pass
   # D 的 MRO: D → B → C → A → object
   ```

## 训练阶梯

### Step 1: 类与对象基础（Level 2→3）
- 定义类和创建实例
- 添加实例属性和方法
- 理解 self 的含义

### Step 2: 构造方法（Level 3）
- 使用 __init__ 初始化
- 区分实例属性和类属性
- 使用 @property

### Step 3: 继承（Level 3）
- 实现单继承
- 使用 super()
- 方法重写

### Step 4: 多继承（Level 3→4）
- 理解 MRO
- 使用多继承
- 处理菱形继承

### Step 5: 魔法方法（Level 3→4）
- 重写 __str__/__repr__
- 重写比较运算符
- 重写 __getitem__

### Step 6: 设计模式基础（Level 4）
- 数据类设计
- 迭代器类
- 上下文管理器类

### Step 7: 综合运用（Level 4→5）
- 设计一个数据处理类层级
- 实现序列化/反序列化
- 设计可扩展的类结构

## 掌握标准

- **Level 3**: 能定义类、实现继承、重写基本魔法方法
- **Level 4**: 能设计类层级、理解 MRO、使用高级魔法方法
- **Level 5**: 能运用 OOP 设计复杂系统，理解鸭子类型

## 参考资料

- 菜鸟教程 Python3 面向对象：https://www.runoob.com/python3/python3-class.html
