# syllabus.md — Python 课程大纲（40 课时）

## 课程总览

- **总课时：** 40 课时
- **每课时：** 60-90 分钟
- **分层：** 4 层，每层 10 课时
- **掌握标准：** 每个技能达到 Level 3（初步掌握）方可进入下一技能

---

## Layer 1: Python 基础（Lesson 1-10）

**目标：能用 Python 写出基本的数据处理脚本**
**掌握标准：** 能独立完成包含变量、条件、循环、数据结构的基本程序

| 课时 | 主题 | 内容 | 预计时长 | 掌握标准 |
|------|------|------|----------|----------|
| L01 | 环境搭建与第一个程序 | 安装 Python、IDLE 使用、命令行运行、print/input、注释 | 60min | 能独立配置环境并运行 .py 文件 |
| L02 | 变量、数据类型与类型转换 | int/float/str/bool/None、动态类型、type()、类型转换 | 60min | 能正确声明变量并进行类型转换 |
| L03 | 运算符 | 算术、比较、逻辑、赋值、位运算、短路求值 | 60min | 能正确使用各类运算符 |
| L04 | 字符串操作与格式化 | 索引、切片、常用方法、f-string、format() | 75min | 能灵活操作字符串 |
| L05 | 条件语句 | if/elif/else、嵌套条件、三元表达式、truthy/falsy | 60min | 能写出复杂条件逻辑 |
| L06 | 循环 | for/while、range()、break/continue、else 子句、enumerate | 75min | 能用循环处理序列数据 |
| L07 | 列表操作 | 创建、索引、切片、增删改查、排序、嵌套列表、浅/深拷贝 | 75min | 能熟练操作列表 |
| L08 | 元组与集合 | 元组不可变性、解包、集合去重、集合运算 | 60min | 能正确选用元组和集合 |
| L09 | 字典操作 | 创建、增删改查、遍历、嵌套字典、setdefault/update | 75min | 能用字典组织数据 |
| L10 | 推导式 | 列表推导式、条件过滤、字典/集合推导式、生成器表达式简介 | 60min | 能写出简洁的推导式 |

---

## Layer 2: 函数与面向对象（Lesson 11-20）

**目标：能写出有结构的、可复用的 Python 代码**
**掌握标准：** 能设计类、使用装饰器、写出模块化的代码

| 课时 | 主题 | 内容 | 预计时长 | 掌握标准 |
|------|------|------|----------|----------|
| L11 | 函数定义与调用 | def、文档字符串、return、调用机制 | 60min | 能定义带文档字符串的函数 |
| L12 | 参数类型 | 位置、关键字、默认值、*args、**kwargs、参数解包 | 75min | 能灵活使用各种参数形式 |
| L13 | 返回值与作用域 | 多返回值、global/nonlocal、LEGB 规则 | 60min | 理解并正确使用作用域 |
| L14 | 闭包与 lambda | 闭包概念、自由变量、lambda、配合 sorted/filter/map | 75min | 能写出闭包和 lambda 表达式 |
| L15 | 装饰器 | 装饰器原理、@语法糖、带参数的装饰器、functools.wraps | 90min | 能写简单装饰器 |
| L16 | 类与对象基础 | class、实例属性、实例方法、self | 60min | 能定义和使用基本类 |
| L17 | 属性与方法 | 类属性、静态方法、类方法、property | 75min | 能区分不同类型的属性和方法 |
| L18 | 继承与多态 | 单继承、多继承、MRO、方法重写、super() | 75min | 能设计继承体系 |
| L19 | 魔法方法 | __init__/__str__/__repr__/__len__/__eq__/__lt__/__getitem__ 等 | 90min | 能重写魔法方法 |
| L20 | 综合练习 | 设计一个数据处理类（含继承、魔法方法、装饰器） | 90min | 能综合运用 OOP 特性 |

---

## Layer 3: 实用技能（Lesson 21-30）

**目标：能用 Python 完成文件处理、数据读写、自动化脚本**
**掌握标准：** 能独立完成文件读写、数据解析、异常处理的脚本

| 课时 | 主题 | 内容 | 预计时长 | 掌握标准 |
|------|------|------|----------|----------|
| L21 | 模块与包 | import 机制、__init__.py、相对/绝对导入、__name__=="__main__" | 60min | 能创建和使用自定义包 |
| L22 | pip 与包管理 | pip install/uninstall/upgrade、PyPI、requirements.txt、虚拟环境简介 | 60min | 能管理项目依赖 |
| L23 | 文件读写 | open()、with 语句、读写模式（r/w/a/b）、read/readline/readlines | 75min | 能安全读写文本文件 |
| L24 | CSV 文件处理 | csv 模块、DictReader/DictWriter、pandas 读取简介 | 60min | 能读写 CSV 数据 |
| L25 | JSON 数据处理 | json.dumps/loads、dump/load、处理嵌套结构 | 60min | 能序列化/反序列化 JSON |
| L26 | 异常处理 | try/except/else/finally、常见异常类型、自定义异常、raise | 75min | 能合理处理异常 |
| L27 | 正则表达式 | re 模块、match/search/findall/sub、常用模式、分组 | 90min | 能进行基本的模式匹配 |
| L28 | 系统操作 | os 模块、pathlib、文件/目录操作、环境变量 | 60min | 能进行文件系统操作 |
| L29 | 时间处理 | datetime、time、格式化、时间计算、时区 | 60min | 能处理时间相关任务 |
| L30 | 工具库 | collections（Counter/defaultdict/deque）、itertools（chain/product/combinations） | 75min | 能使用常用工具库 |

---

## Layer 4: 进阶与 AI 准备（Lesson 31-40）

**目标：具备使用 Python 进行数据科学和深度学习的基础能力**
**掌握标准：** 能使用 NumPy/Pandas 处理数据，理解深度学习常用 Python 模式

| 课时 | 主题 | 内容 | 预计时长 | 掌握标准 |
|------|------|------|----------|----------|
| L31 | 生成器与 yield | 生成器函数、yield、惰性求值、生成器表达式、send() | 75min | 能写生成器函数 |
| L32 | 迭代器协议 | __iter__/__next__、可迭代对象、itertools 高级用法 | 60min | 理解迭代器协议 |
| L33 | 上下文管理器 | __enter__/__exit__、contextlib.contextmanager、with 语句原理 | 60min | 能写上下文管理器 |
| L34 | 并发基础 | GIL 概念、threading、multiprocessing、concurrent.futures | 90min | 理解并发基本概念 |
| L35 | 虚拟环境与项目管理 | venv、项目目录结构、.gitignore、打包基础 | 60min | 能管理 Python 项目 |
| L36 | NumPy 基础 | ndarray、索引/切片、广播、向量化操作、常用函数 | 90min | 能用 NumPy 做数值计算 |
| L37 | Pandas 基础 | Series/DataFrame、读取 CSV/Excel、筛选、分组、合并 | 90min | 能用 Pandas 处理表格数据 |
| L38 | 数据可视化 | matplotlib 基础（plot/bar/scatter/hist）、子图、样式 | 75min | 能绘制基本图表 |
| L39 | 深度学习 Python 模式 | 数据加载/预处理、批处理迭代、模型保存/加载（pickle/torch.save）、日志记录 | 75min | 理解 DL 项目中的 Python 模式 |
| L40 | 综合项目 | 数据分析流水线：读取 → 清洗 → 分析 → 可视化 → 输出 | 120min | 能独立完成端到端数据处理 |

---

## 推荐学习顺序

### 快速通道（如果已有编程基础）
直接从 Layer 1 测试开始，Level ≥ 2 的技能跳过，重点学习：
- L10 推导式
- L14-15 闭包与装饰器
- L19 魔法方法
- L31-32 生成器与迭代器
- L36-38 NumPy/Pandas/matplotlib

### 标准通道（从零开始）
按 L01 → L40 顺序学习，每 5 课时做一次阶段测试。

### AI 工程重点通道
优先学习与深度学习直接相关的技能：
1. L01-L04（环境与基础）
2. L07-L10（数据结构与推导式）
3. L11-L15（函数与装饰器）
4. L21-L22（模块与包管理）
5. L26（异常处理）
6. L31-L32（生成器与迭代器）
7. L35-L40（虚拟环境、NumPy、Pandas、可视化、DL 模式）

---

## 阶段考试安排

| 考试 | 覆盖范围 | 通过标准 |
|------|----------|----------|
| 阶段考试 1 | Layer 1（L01-L10） | 平均 Level ≥ 2 |
| 阶段考试 2 | Layer 2（L11-L20） | 平均 Level ≥ 2 |
| 阶段考试 3 | Layer 3（L21-L30） | 平均 Level ≥ 2 |
| 阶段考试 4 | Layer 4（L31-L40） | 平均 Level ≥ 2 |
| 综合考试 | 全部 40 课时 | 平均 Level ≥ 3 |
