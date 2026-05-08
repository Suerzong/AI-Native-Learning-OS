# mistakes.md — Python 错误记录

## 错误记录模板

```
### [日期] 错误 #编号
- **相关技能**: [skill-map 中的技能]
- **错误代码**:
```python
# 学生写的错误代码
```
- **错误类型**: 语法错误 / 逻辑错误 / 概念错误 / 类型错误
- **错误描述**: [发生了什么错误]
- **错误原因**: [为什么会犯这个错误]
- **正确做法**:
```python
# 正确的代码
```
- **要点总结**: [一句话总结]
- **是否已掌握**: 否
```

---

## 错误记录

### 2026-05-05 错误 #001
- **相关技能**: basics — 可变默认参数
- **错误代码**:
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  —— 预期是 [2]！
```
- **错误类型**: 概念错误
- **错误描述**: 使用列表作为函数默认参数，多次调用后列表累积了所有之前添加的元素
- **错误原因**: Python 的默认参数在函数定义时求值一次，之后所有调用共享同一个列表对象
- **正确做法**:
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```
- **要点总结**: 永远不要使用可变对象（list, dict, set）作为函数默认参数
- **是否已掌握**: 否

---

### 2026-05-05 错误 #002
- **相关技能**: control-flow — 循环中修改列表
- **错误代码**:
```python
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)  # [1, 3, 5] 看起来对了？

numbers2 = [2, 4, 6, 8]
for n in numbers2:
    if n % 2 == 0:
        numbers2.remove(n)
print(numbers2)  # [4, 8] —— 不对！
```
- **错误类型**: 逻辑错误
- **错误描述**: 在 for 循环中删除列表元素，导致某些元素被跳过
- **错误原因**: for 循环通过索引遍历列表，删除元素后索引偏移，下一个元素被跳过
- **正确做法**:
```python
# 方法1：列表推导式创建新列表
numbers = [n for n in numbers if n % 2 != 0]

# 方法2：倒序遍历
numbers = [2, 4, 6, 8]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)

# 方法3：切片赋值
numbers[:] = [n for n in numbers if n % 2 != 0]
```
- **要点总结**: 不要在遍历列表的同时修改它（增/删元素）。要么创建新列表，要么倒序遍历
- **是否已掌握**: 否

---

### 2026-05-07 错误 #003
- **相关技能**: PY-B02 — 负数整除与取模
- **错误代码**:
```python
a = -10 // 3   # 用户预期 -3
b = -10 % 3    # 用户预期不确定
```
- **错误类型**: 概念错误
- **错误描述**: 将 C 的"向零截断"套用到 Python 的 `//`，认为 -10//3 = -3；对负数取模规则不理解
- **错误原因**: Python 的 `//` 是向下取整（往更小的方向），不是 C 的向零截断。`%` 和 `//` 配对，结果符号与除数相同
- **正确做法**:
```python
-10 // 3  # → -4（向下取整）
-10 % 3   # → 2（因为 -10 == -4*3 + 2）
```
- **要点总结**: Python `//` 向下取整，`%` 结果符号和除数一致。用公式 a == (a//b)*b + (a%b) 验证
- **是否已掌握**: 是（经复测确认）

### 2026-05-07 错误 #004
- **相关技能**: PY-B02 — 字符串切片右边界
- **错误代码**:
```python
s = "Python"
print(s[2:5])  # 用户预期 "thon"
```
- **错误类型**: 概念错误
- **错误描述**: 将切片 `s[2:5]` 理解为"第 2 到第 5 个字符"，实际是左闭右开 [2,5)
- **错误原因**: 不熟悉 Python 左闭右开的设计规则（切片、range、迭代器统一遵循此规则）
- **正确做法**:
```python
s[2:5]  # 索引 2,3,4 → "tho"
s[2:6]  # 索引 2,3,4,5 → "thon"
```
- **要点总结**: Python 切片 `s[start:stop]` 包含 start，不包含 stop。和 range(n) 从 0 到 n-1 是同一套规则
- **是否已掌握**: 是（经复测确认）

### 2026-05-07 错误 #005
- **相关技能**: PY-B02 — bool 与 int 运算
- **错误代码**:
```python
print(True + False)  # 用户预期 True
```
- **错误类型**: 概念错误
- **错误描述**: 认为 bool 运算返回 bool，实际返回 int
- **错误原因**: bool 是 int 的子类（True=1, False=0），算术运算结果是 int 类型
- **正确做法**:
```python
True + False   # → 1 (int)
type(True + False)  # <class 'int'>
```
- **要点总结**: bool 参与算术运算时，结果总是 int 类型
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #006
- **相关技能**: PY-F06 — 装饰器 wrapper 省略参数
- **错误代码**:
```python
def timer(func):
    def wrapper():          # ← 没有参数
        print("开始执行")
        func()              # ← 无法接收外部传入的参数
        print("执行完毕")
    return wrapper
```
- **错误类型**: 概念错误
- **错误描述**: wrapper 没有使用 `*args, **kwargs`，导致被装饰函数无法接收参数
- **错误原因**: 不理解 wrapper 的职责是"透传"——接收原函数的所有参数并转发
- **正确做法**:
```python
def timer(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        result = func(*args, **kwargs)
        print("执行完毕")
        return result
    return wrapper
```
- **要点总结**: 装饰器的 wrapper 必须用 `*args, **kwargs` 接收任意参数，调用原函数并返回结果
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #007
- **相关技能**: PY-F06 — 使用不存在的 dunder 属性
- **错误代码**:
```python
print(f"调用 {__self__.name}{args}")   # __self__ 不存在
```
- **错误类型**: 概念错误
- **错误描述**: 使用 `__self__.name` 获取函数名，但 `__self__` 是绑定方法的属性，装饰器中不存在
- **正确做法**:
```python
print(f"调用 {func.__name__}{args}")
```
- **要点总结**: 获取函数名字用 `func.__name__`，不要混淆其他 dunder 属性
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #008
- **相关技能**: PY-F06 — C 语言习惯残留
- **错误代码**:
```python
printf("开始执行")      # ← printf 是 C 的
return wrapper;         # ← 分号是 C 的
```
- **错误类型**: 语法错误
- **错误描述**: 将 C 语言的 `printf` 和分号语法带入 Python
- **正确做法**:
```python
print("开始执行")
return wrapper
```
- **要点总结**: Python 用 `print()`（不是 printf），不需要分号
- **是否已掌握**: 否（需持续注意）

### 2026-05-08 错误 #009
- **相关技能**: PY-F07 — 类关键字和 dunder 大小写
- **错误代码**:
```python
Class Dog:              # Class 大写
    def __Init__(self): # __Init__ 大写 I
```
- **错误类型**: 语法错误
- **错误描述**: `Class` 和 `__Init__` 首字母大写，导致 NameError/SyntaxError
- **正确做法**:
```python
class Dog:
    def __init__(self):
```
- **要点总结**: Python 关键字（class, def, if, for 等）和 dunder 方法（__init__, __str__ 等）全部小写
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #010
- **相关技能**: PY-F07 — 实例方法中访问属性缺少 self.
- **错误代码**:
```python
def bark(self):
    print(f"{sound}")   # 直接用 sound，没有 self.
```
- **错误类型**: 概念错误
- **错误描述**: 在实例方法中直接使用变量名而非 `self.属性名`，导致 NameError
- **错误原因**: 不理解实例属性必须通过 `self` 访问，`__init__` 的参数是局部变量，方法间不共享
- **正确做法**:
```python
def bark(self):
    print(f"{self.sound}")
```
- **要点总结**: 实例属性存在对象身上，访问时必须用 `self.属性名`
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #011
- **相关技能**: PY-F08 — 类属性访问缺少限定
- **错误代码**:
```python
class Dog:
    count = 0
    def __init__(self, name):
        count += 1          # ← 裸写 count
    @classmethod
    def get_count(cls):
        return class.count  # ← class 是关键字
```
- **错误类型**: 概念错误
- **错误描述**: 类属性在方法中裸写会导致 NameError；`class` 是 Python 关键字，不能作为变量名
- **正确做法**:
```python
    def __init__(self, name):
        Dog.count += 1         # 实例方法中用类名
    @classmethod
    def get_count(cls):
        return cls.count       # classmethod 中用 cls
```
- **要点总结**: 类属性必须通过类名（`Dog.count`）或 `cls`（仅在 classmethod 中）访问，不能裸写
- **是否已掌握**: 是（经复测确认）

### 2026-05-08 错误 #012
- **相关技能**: PY-F08 — C 语言语法混入 Python
- **错误代码**:
```python
count++     # C 的自增运算符
```
- **错误类型**: 语法错误
- **错误描述**: Python 没有 `++` 运算符
- **正确做法**:
```python
count += 1
```
- **要点总结**: Python 没有 `++` 和 `--`，用 `+= 1` 和 `-= 1` 替代
- **是否已掌握**: 否（C 习惯残留，需持续注意）

### 2026-05-08 错误 #013
- **相关技能**: PY-F10 — __str__ 返回值包含多余文字
- **错误代码**:
```python
def __str__(self):
    return f"Dog({self.name}({self.age}岁))"
```
- **错误类型**: 概念错误
- **错误描述**: __str__ 返回值中硬编码了 "Dog(" 前缀，导致输出为 `Dog(Tom(3岁))` 而非要求的 `Tom(3岁)`
- **错误原因**: 不理解 __str__ 返回什么就打印什么，把类名当作必须包含的内容
- **正确做法**:
```python
def __str__(self):
    return f"{self.name}({self.age}岁)"
```
- **要点总结**: __str__ 的返回值就是 print 的输出，按题目要求的格式写，不要自动添加多余内容
- **是否已掌握**: 是（经复测确认）
