# teaching-loop.md — Python 8 步教学循环

## 循环概览

```
┌─────────────────────────────────────────────────────────────┐
│                    Python 掌握学习循环                        │
│                                                             │
│  ① 诊断 ──→ ② 目标 ──→ ③ 知识教学 ──→ ④ 任务练习         │
│      ↑                                          │           │
│      │                                          ▼           │
│  ⑧ 推进/补救 ←── ⑦ 状态更新 ←── ⑥ 迁移测试 ←── ⑤ 即时反馈 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 1: 诊断（Diagnostic）

**目标**：确定学生的当前水平和起点

**输入**：
- `learner/current-state.md` — 历史状态
- `mastery-tracker.md` — 技能掌握度

**流程**：
1. 如果是新技能，进行前测（5 题概念 + 3 题代码）
2. 如果是复习，快速提问 2-3 题确认水平
3. 确定当前 Level

**输出**：
- 当前 Level（0-5）
- 前置技能是否满足
- 主要弱点识别

**Python 特化**：
- 前测全部可以通过运行代码验证
- 不需要硬件、不需要理论推导
- 诊断时间短（5-10 分钟）

---

## Step 2: 目标设定（Goal Setting）

**目标**：明确本次学习要达到的 Level 和能力

**流程**：
1. 确定目标 Level（当前 Level + 1）
2. 定义该 Level 的具体能力（参考 promotion-rules.md）
3. 设定可衡量的学习成果

**示例**：
```
当前 Level: 0（变量与数据类型 未学习）
目标 Level: 2（已学习）
学习成果：
- 能解释 int/float/str/bool/None 的区别
- 能正确声明变量并进行类型转换
- 能使用 type() 检查类型
- 能写出包含 3 种以上类型的程序
```

---

## Step 3: 知识教学（Knowledge Teaching）

**目标**：讲解概念和代码，建立直觉理解

**Python Code-First 流程**：

**3a. 展示可运行代码**
```python
# 先看这段代码
name = "Ethen"
age = 20
gpa = 3.85
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(gpa))       # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

**3b. 让学生运行并观察**
- "请将这段代码保存为 test.py 并运行"
- "观察输出，你看到了什么？"

**3c. 逐行解释**
- "name 是一个 str 类型的变量..."
- "type() 函数返回变量的类型..."

**3d. 引导修改**
- "如果把 name = 'Ethen' 改成 name = 123，type(name) 会输出什么？"
- "试试看，然后告诉我结果。"

**3e. 提供知识卡片**

---

## 知识卡片模板

```
## [技能名称]

### 核心概念
[用 2-3 句话解释]

### 语法/用法
```python
[代码示例]
```

### 常见用法
```python
[更多示例]
```

### 注意事项
- [常见陷阱 1]
- [常见陷阱 2]

### 对比表（如适用）
| A | B | 区别 |
|---|---|------|
| ... | ... | ... |
```

**示例 — 变量与数据类型知识卡片**：

```
## 变量与数据类型

### 核心概念
Python 是动态类型语言，变量不需要声明类型，类型由赋值决定。
主要数据类型：int（整数）、float（浮点数）、str（字符串）、bool（布尔）、None（空值）。

### 语法
```python
# 变量赋值
name = "Ethen"        # str
age = 20              # int
gpa = 3.85            # float
is_student = True     # bool
data = None           # NoneType

# 类型检查
print(type(name))     # <class 'str'>

# 类型转换
x = int("42")         # str → int
y = float("3.14")     # str → float
z = str(100)          # int → str
```

### 注意事项
- None 用 `is None` 判断，不用 `== None`
- bool() 的 falsy 值：0, 0.0, '', [], {}, None, False
- float 精度问题：0.1 + 0.2 != 0.3
```

---

## Step 4: 任务练习（Task Practice）

**目标**：通过练习巩固理解

**任务分配规则**：
1. 从 Level 0+1 的任务类型开始
2. 每次给 1-2 题
3. 学生提交代码后进入 Step 5

**Python 特化**：
- 所有任务都可以立即运行验证
- 鼓励学生先运行、再理解、再修改
- 不需要等待编译或烧录

---

## Step 5: 即时反馈（Immediate Feedback）

**目标**：对学生的代码进行评估和反馈

**流程**（参考 feedback-rubric.md）：
1. 确认正确部分
2. 指出错误
3. 解释原因
4. 给出修正任务
5. 迁移测试

**Python 特化**：
- 可以直接运行学生的代码验证
- 错误信息是即时的（不需要等硬件响应）
- 调试手段多样（print()、断言、pdb）

---

## Step 6: 迁移测试（Transfer Test）

**目标**：验证学生是否真正理解（而非只是记住了答案）

**迁移类型**：
- **情境迁移**：同样的代码，不同的输入
- **方法迁移**：同样的逻辑，不同的实现方式
- **组合迁移**：将当前技能与其他技能组合

**Python 特化**：
- 可以给真实的数据集让学生处理
- 可以要求优化代码（效率、可读性）
- 可以要求用不同的方法实现

---

## Step 7: 状态更新（State Update）

**目标**：记录学习成果和状态变化

**更新文件**：
1. `mastery-tracker.md` — 更新技能 Level
2. `mistakes.md` — 记录犯过的错误
3. `learner/current-state.md` — 更新当前状态
4. `learner/learning-log.md` — 记录本次学习内容

**更新规则**：
- 只在学生确实完成任务后更新 Level
- 不要把计划写成完成
- 保持完整的 12 模块结构（在 learning-progress.md 中）

---

## Step 8: 推进/补救（Advance/Remediate）

**目标**：根据学习结果决定下一步

**推进条件**（全部满足）：
- 当前技能 Level ≥ 目标 Level
- 迁移测试通过
- 前置技能 Level 足够

**推进动作**：
- 进入下一个技能的 Step 1
- 更新 daily-plan.md

**补救条件**（任一满足）：
- 当前技能 Level < 目标 Level
- 迁移测试未通过
- 连续犯同一类型错误

**补救动作**：
- 回到 Step 3 重新讲解（换一种方式）
- 提供更多示例
- 降低任务难度
- 再次测试
- 如果连续 3 次未通过，标记为"需要特殊关注"

---

## 单次会话示例

```
主题：列表推导式
当前 Level：1（了解概念，未独立写过）
目标 Level：3（已实践）

Step 1 诊断：
  Q: "什么是列表推导式？"
  A: "一种用一行代码创建列表的方法。" → Level 1 确认

Step 2 目标：
  能独立写出列表推导式，包括带条件过滤的情况

Step 3 知识教学：
  展示代码：
  squares = [x**2 for x in range(10)]
  evens = [x for x in range(20) if x % 2 == 0]
  逐行解释，让学生运行

Step 4 任务：
  "将以下 for 循环改写为列表推导式：
   result = []
   for word in words:
       if len(word) > 3:
           result.append(word.upper())"

Step 5 反馈：
  学生提交：result = [word.upper() for word in words if len(word) > 3]
  "完全正确！条件过滤和方法调用的位置都对了。"

Step 6 迁移：
  "现在试试字典推导式：给定 words 列表，
   创建一个字典，键是单词，值是单词长度。"

Step 7 更新：
  Level: 1 → 3
  记录到 mastery-tracker.md

Step 8 推进：
  进入下一个技能：元组与集合
```
