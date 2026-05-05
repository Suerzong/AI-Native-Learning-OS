# skill-map: basics — 变量、数据类型、运算符、输入输出

## 目标

掌握 Python 的基本数据类型、变量声明、类型转换和基本输入输出操作。这是所有后续学习的基础。

## 必知概念

### 变量
- **变量是标签**：Python 变量不是存储数据的盒子，而是贴在对象上的标签
- **动态类型**：不需要声明类型，类型由赋值决定
- **命名规则**：字母/下划线开头，可含数字；大小写敏感
- **命名惯例**：snake_case（如 `student_name`）

### 数据类型
| 类型 | 名称 | 示例 | 可变性 |
|------|------|------|--------|
| int | 整数 | `42`, `-7`, `0` | 不可变 |
| float | 浮点数 | `3.14`, `-0.001` | 不可变 |
| str | 字符串 | `"hello"`, `'world'` | 不可变 |
| bool | 布尔 | `True`, `False` | 不可变 |
| NoneType | 空值 | `None` | 不可变 |

### 类型转换
- `int()` — 转整数（截断小数，不四舍五入）
- `float()` — 转浮点数
- `str()` — 转字符串
- `bool()` — 转布尔（空值为 False，非空为 True）

### 运算符
| 类型 | 运算符 | 说明 |
|------|--------|------|
| 算术 | `+` `-` `*` `/` `//` `%` `**` | 整除 `//`，取模 `%`，幂 `**` |
| 比较 | `==` `!=` `>` `<` `>=` `<=` | 返回 bool |
| 逻辑 | `and` `or` `not` | 短路求值 |
| 赋值 | `=` `+=` `-=` `*=` `/=` | 复合赋值 |
| 身份 | `is` `is not` | 比较对象地址 |
| 成员 | `in` `not in` | 检查是否在序列中 |

### 输入输出
- `print()` — 输出，支持多个参数、`sep`、`end`
- `input()` — 输入，返回字符串，需转换类型
- f-string — 格式化输出：`f"{name} is {age} years old"`

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `print()` | 输出 | `print("hello", end="")` |
| `input()` | 输入 | `name = input("Name: ")` |
| `type()` | 获取类型 | `type(x)` |
| `int()` | 转整数 | `int("42")` |
| `float()` | 转浮点 | `float("3.14")` |
| `str()` | 转字符串 | `str(100)` |
| `bool()` | 转布尔 | `bool(0)` → `False` |
| `id()` | 获取对象地址 | `id(x)` |
| `isinstance()` | 类型检查 | `isinstance(x, int)` |

## 常见错误

1. **input() 返回的是字符串**
   ```python
   age = input("Age: ")    # age 是字符串！
   age = int(input("Age: "))  # 正确：转换为整数
   ```

2. **= vs ==**
   ```python
   if x = 5:    # SyntaxError! = 是赋值
   if x == 5:   # 正确：== 是比较
   ```

3. **float 精度问题**
   ```python
   0.1 + 0.2 == 0.3    # False!
   abs(0.1 + 0.2 - 0.3) < 1e-9  # 正确的比较方式
   ```

4. **is vs ==**
   ```python
   a = 257
   b = 257
   a == b    # True（值相等）
   a is b    # False（不一定是同一个对象）
   ```

## 训练阶梯

### Step 1: 环境搭建（Level 0→1）
- 安装 Python 3.10+
- 在命令行运行 `python --version`
- 运行 `python` 进入 REPL
- 创建并运行第一个 .py 文件

### Step 2: 变量声明与类型（Level 1→2）
- 声明 int/float/str/bool 类型的变量
- 使用 `type()` 检查类型
- 理解动态类型的含义

### Step 3: 类型转换（Level 2）
- 使用 int()/float()/str()/bool() 转换
- 处理 input() 的类型转换
- 理解隐式转换（如 int + float → float）

### Step 4: 运算符（Level 2→3）
- 使用各种运算符
- 理解整除和取模
- 理解短路求值
- 使用链式比较

### Step 5: 输入输出（Level 3）
- 使用 f-string 格式化
- 使用 print() 的 sep/end 参数
- 处理多行输入

### Step 6: 综合运用（Level 3→4）
- 编写温度转换器（摄氏↔华氏）
- 编写 BMI 计算器
- 编写简单的单位换算工具

### Step 7: 迁移运用（Level 4→5）
- 在新场景中选择合适的类型
- 优化代码的可读性
- 处理边界情况和异常输入

## 掌握标准

- **Level 3**: 能独立声明变量、进行类型转换、使用运算符完成计算
- **Level 4**: 能写出清晰的输入输出程序，处理边界情况
- **Level 5**: 能向他人解释动态类型、不可变性等概念，能预判类型相关陷阱

## 参考资料

- 菜鸟教程 Python3 基础语法：https://www.runoob.com/python3/python3-basic-syntax.html
- 菜鸟教程 Python3 变量类型：https://www.runoob.com/python3/python3-variable-types.html
- 菜鸟教程 Python3 运算符：https://www.runoob.com/python3/python3-operator.html
