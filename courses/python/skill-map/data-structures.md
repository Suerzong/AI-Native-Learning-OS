# skill-map: data-structures — 列表、元组、字典、集合、推导式

## 目标

掌握 Python 四种核心数据结构（list, tuple, dict, set）的操作方法，以及推导式的简洁写法。能根据场景选择合适的数据结构。

## 必知概念

### 列表（list）
- **有序、可变、可重复**
- 创建：`[1, 2, 3]` 或 `list()`
- 常用操作：索引、切片、append、extend、insert、remove、pop、sort、reverse

### 元组（tuple）
- **有序、不可变、可重复**
- 创建：`(1, 2, 3)` 或 `tuple()`
- 单元素元组：`(1,)`（注意逗号）
- 用途：函数返回多值、字典键、不可变数据

### 字典（dict）
- **有序（3.7+）、可变、键不可重复**
- 创建：`{"a": 1}` 或 `dict()`
- 键必须是不可变类型（str, int, tuple 等）
- 常用操作：`d[key]`, `d.get(key)`, `d.keys()`, `d.values()`, `d.items()`

### 集合（set）
- **无序、可变、元素不可重复**
- 创建：`{1, 2, 3}` 或 `set()`
- 用途：去重、集合运算
- 集合运算：`|` 并集, `&` 交集, `-` 差集, `^` 对称差集

### 推导式
| 类型 | 语法 | 示例 |
|------|------|------|
| 列表推导式 | `[expr for x in iterable]` | `[x**2 for x in range(10)]` |
| 带条件 | `[expr for x in iterable if cond]` | `[x for x in lst if x > 0]` |
| 字典推导式 | `{k: v for x in iterable}` | `{x: x**2 for x in range(5)}` |
| 集合推导式 | `{expr for x in iterable}` | `{x % 3 for x in range(10)}` |
| 生成器表达式 | `(expr for x in iterable)` | `(x**2 for x in range(10))` |

## 必知函数/API

| 类型 | 函数 | 用途 |
|------|------|------|
| list | `append(x)` | 末尾添加 |
| list | `extend(lst)` | 扩展列表 |
| list | `insert(i, x)` | 插入 |
| list | `remove(x)` | 删除第一个匹配 |
| list | `pop(i)` | 弹出并返回 |
| list | `sort()` | 原地排序 |
| list | `sorted(lst)` | 返回新列表 |
| list | `reverse()` | 原地反转 |
| list | `index(x)` | 查找索引 |
| list | `count(x)` | 计数 |
| dict | `get(key, default)` | 安全取值 |
| dict | `setdefault(key, default)` | 取值或设置默认 |
| dict | `update(other)` | 更新字典 |
| dict | `pop(key)` | 删除并返回 |
| set | `add(x)` | 添加 |
| set | `discard(x)` | 删除（不存在不报错） |
| 通用 | `len()` | 长度 |
| 通用 | `in` | 成员检查 |
| 通用 | `enumerate()` | 索引+值 |
| 通用 | `zip()` | 打包多个序列 |

## 常见错误

1. **浅拷贝 vs 深拷贝**
   ```python
   a = [[1], [2]]
   b = a[:]       # 浅拷贝！
   b[0].append(9) # a 也变了！
   ```

2. **字典键不存在**
   ```python
   d = {"a": 1}
   print(d["b"])  # KeyError!
   print(d.get("b", 0))  # 安全：返回 0
   ```

3. **集合无序**
   ```python
   s = {3, 1, 2}
   s[0]  # TypeError! 集合不支持索引
   ```

4. **推导式中条件位置**
   ```python
   [x if x > 0 for x in lst]     # 语法错误
   [x for x in lst if x > 0]     # 正确：过滤
   [x if x > 0 else 0 for x in lst]  # 正确：条件表达式
   ```

## 训练阶梯

### Step 1: 列表基础（Level 1→2）
- 创建和访问列表
- 使用 append/remove/pop
- 使用切片操作

### Step 2: 列表进阶（Level 2）
- 排序和反转
- 嵌套列表
- 浅拷贝 vs 深拷贝

### Step 3: 元组和集合（Level 2）
- 创建和使用元组
- 元组解包
- 集合去重和运算

### Step 4: 字典（Level 2→3）
- 创建和访问字典
- 遍历字典（keys/values/items）
- 使用 get/setdefault

### Step 5: 推导式（Level 3）
- 列表推导式
- 条件过滤
- 字典和集合推导式

### Step 6: 数据结构选择（Level 3→4）
- 根据场景选择 list/tuple/dict/set
- 性能考虑（list vs set 的 in 操作）
- 组合使用多种数据结构

### Step 7: 综合运用（Level 4→5）
- 词频统计
- 数据清洗
- 复杂数据结构设计

## 掌握标准

- **Level 3**: 能熟练操作四种数据结构，能写出推导式
- **Level 4**: 能根据场景选择合适的数据结构，理解性能差异
- **Level 5**: 能设计复杂的数据结构组合，能优化数据处理代码

## 参考资料

- 菜鸟教程 Python3 列表：https://www.runoob.com/python3/python3-list.html
- 菜鸟教程 Python3 元组：https://www.runoob.com/python3/python3-tuple.html
- 菜鸟教程 Python3 字典：https://www.runoob.com/python3/python3-dictionary.html
- 菜鸟教程 Python3 集合：https://www.runoob.com/python3/python3-set.html
