# skill-map: file-io — 文件读写、CSV、JSON

## 目标

掌握 Python 文件读写操作，能处理文本文件、CSV 和 JSON 格式的数据。这是数据处理和自动化的基础技能。

## 必知概念

### 文件操作基础
- **open()**：打开文件，返回文件对象
- **with 语句**：自动管理资源，确保文件正确关闭
- **文件模式**：
  | 模式 | 说明 |
  |------|------|
  | `r` | 只读（默认） |
  | `w` | 写入（覆盖，文件不存在则创建） |
  | `a` | 追加 |
  | `r+` | 读写 |
  | `b` | 二进制模式（可组合，如 `rb`, `wb`） |

### 文件读取方法
| 方法 | 说明 |
|------|------|
| `read()` | 读取全部内容为字符串 |
| `readline()` | 读取一行 |
| `readlines()` | 读取所有行为列表 |
| `for line in file:` | 逐行迭代（推荐大文件） |

### 文件写入方法
| 方法 | 说明 |
|------|------|
| `write(s)` | 写入字符串 |
| `writelines(lst)` | 写入字符串列表（不自动加换行） |

### CSV 处理
- **csv.reader**：读取 CSV 为列表
- **csv.writer**：写入 CSV
- **csv.DictReader**：读取 CSV 为字典
- **csv.DictWriter**：用字典写入 CSV

### JSON 处理
- **json.dumps()**：Python 对象 → JSON 字符串
- **json.loads()**：JSON 字符串 → Python 对象
- **json.dump()**：Python 对象 → JSON 文件
- **json.load()**：JSON 文件 → Python 对象

### pathlib（现代路径操作）
- **Path**：路径对象
- **Path.exists()**：文件是否存在
- **Path.read_text()**：读取文本
- **Path.write_text()**：写入文本
- **Path.glob()**：模式匹配
- **Path.iterdir()**：遍历目录

## 常见错误

1. **忘记使用 with 语句**
   ```python
   f = open("data.txt")
   data = f.read()
   # 忘记 f.close()！资源泄漏
   ```

2. **编码问题**
   ```python
   open("data.txt")  # 默认编码取决于系统
   open("data.txt", encoding="utf-8")  # 明确指定编码
   ```

3. **w 模式覆盖文件**
   ```python
   with open("data.txt", "w") as f:  # 清空文件！
       f.write("new content")
   # 应该用 "a" 追加，或先读取再写入
   ```

4. **JSON 序列化不可序列化对象**
   ```python
   import json
   data = {"time": datetime.now()}
   json.dumps(data)  # TypeError: 不可序列化
   # 需要先转换为字符串
   ```

## 训练阶梯

### Step 1: 文本文件读取（Level 2→3）
- 使用 with open() 读取文件
- 使用 read()/readlines()
- 逐行迭代

### Step 2: 文本文件写入（Level 3）
- 使用 write() 写入
- 理解 w vs a 模式
- 处理编码

### Step 3: CSV 处理（Level 3）
- 使用 csv.reader/writer
- 使用 DictReader/DictWriter
- 处理中文

### Step 4: JSON 处理（Level 3）
- 序列化和反序列化
- 处理嵌套结构
- 处理日期等特殊类型

### Step 5: pathlib（Level 3→4）
- 使用 Path 对象
- 遍历目录
- 模式匹配

### Step 6: 综合运用（Level 4）
- 读取 → 处理 → 写入流水线
- 配置文件管理（JSON/YAML）
- 日志文件解析

## 掌握标准

- **Level 3**: 能安全地读写文本文件，能处理 CSV 和 JSON
- **Level 4**: 能设计文件处理流程，能处理各种编码和格式
- **Level 5**: 能处理大文件，能设计高效的文件 I/O 方案

## 参考资料

- 菜鸟教程 Python3 文件 I/O：https://www.runoob.com/python3/python3-file-io.html
- Python 官方文档 csv 模块：https://docs.python.org/3/library/csv.html
- Python 官方文档 json 模块：https://docs.python.org/3/library/json.html
