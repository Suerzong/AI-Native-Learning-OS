# skill-map: modules — 模块、包、标准库、pip

## 目标

掌握 Python 的模块和包系统，能组织代码结构，能使用 pip 管理第三方包，为后续项目开发和库使用打下基础。

## 必知概念

### 模块
- **定义**：一个 `.py` 文件就是一个模块
- **导入方式**：
  ```python
  import module
  from module import func
  from module import func as f
  from module import *  # 不推荐
  ```
- **__name__**：直接运行时为 `"__main__"`，被导入时为模块名
- **模块搜索路径**：当前目录 → PYTHONPATH → 标准库 → site-packages

### 包
- **定义**：包含 `__init__.py` 的目录
- **__init__.py**：可以为空，也可以包含初始化代码
- **相对导入**：`from . import sibling`，`from ..parent import func`
- **绝对导入**：`from mypackage.submodule import func`

### pip
| 命令 | 用途 |
|------|------|
| `pip install package` | 安装包 |
| `pip install package==1.0` | 安装指定版本 |
| `pip uninstall package` | 卸载 |
| `pip list` | 列出已安装 |
| `pip freeze > requirements.txt` | 导出依赖 |
| `pip install -r requirements.txt` | 从文件安装 |
| `pip show package` | 查看包信息 |

### 常用标准库
| 模块 | 用途 |
|------|------|
| `os` | 操作系统接口 |
| `sys` | 系统参数 |
| `math` | 数学函数 |
| `random` | 随机数 |
| `datetime` | 日期时间 |
| `json` | JSON 处理 |
| `re` | 正则表达式 |
| `collections` | 高级数据结构 |
| `itertools` | 迭代器工具 |
| `functools` | 函数工具 |
| `pathlib` | 路径操作 |

## 常见错误

1. **循环导入**
   ```python
   # a.py
   from b import func_b
   # b.py
   from a import func_a  # ImportError!
   ```

2. **相对导入在顶层运行**
   ```python
   # 直接运行包内的模块时，相对导入会报错
   # 使用 python -m package.module 代替
   ```

3. **shadowing 标准库**
   ```python
   # 不要把自己的模块命名为 random.py, math.py 等
   # 会覆盖同名的标准库模块
   ```

4. **忘记 __init__.py**
   ```python
   # Python 3.3+ 支持没有 __init__.py 的"命名空间包"
   # 但传统包仍然建议包含 __init__.py
   ```

## 训练阶梯

### Step 1: 导入基础（Level 2→3）
- 使用 import 和 from...import
- 理解模块搜索路径
- 编写和导入自己的模块

### Step 2: 包结构（Level 3）
- 创建包和 __init__.py
- 使用相对和绝对导入
- 理解 __name__ == "__main__"

### Step 3: pip 使用（Level 3）
- 安装和卸载包
- 使用 requirements.txt
- 管理依赖

### Step 4: 标准库（Level 3→4）
- 熟悉常用标准库模块
- 能在文档中查找用法
- 合理选择标准库 vs 第三方库

### Step 5: 项目结构（Level 4）
- 设计合理的目录结构
- 配置 setup.py / pyproject.toml
- 使用虚拟环境

## 掌握标准

- **Level 3**: 能创建和导入模块/包，能使用 pip 管理依赖
- **Level 4**: 能设计项目结构，熟悉常用标准库
- **Level 5**: 能发布自己的包，能解决复杂的导入问题

## 参考资料

- 菜鸟教程 Python3 模块：https://www.runoob.com/python3/python3-module.html
