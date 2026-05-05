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
