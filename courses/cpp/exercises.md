# 训练任务库

训练任务用于 10-30 分钟内完成一个明确技能点。

## 任务模板

```md
## 任务名称

- 目标技能：
- 起始文件：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 反馈重点：
```

---

## BASICS-01：Hello World 与编译

- 目标技能：编写、编译、运行第一个 C++ 程序
- 起始文件：无（从零写）
- 任务要求：
  1. 编写一个 `hello.cpp`，输出 `Hello, C++!`
  2. 用 g++ 编译并运行
  3. 修改程序，让用户输入姓名，输出 `Hello, <姓名>!`
- 限制条件：使用 `std::cout` 和 `std::cin`，不能用 `printf`/`scanf`
- 成功标准：编译零错误，运行正确，能解释 `#include <iostream>`、`std::cout`、`std::cin` 的作用
- 常见错误：忘记 `std::` 前缀、用 `.c` 后缀编译、`<<` 和 `>>` 方向搞反
- 反馈重点：C++ 的流操作符 vs C 的格式化字符串

---

## BASICS-02：auto 与 constexpr

- 目标技能：理解 C++ 的类型推导和编译期常量
- 起始文件：无
- 任务要求：
  1. 用 `auto` 声明一个 `int` 变量、一个 `double` 变量、一个 `std::string` 变量
  2. 用 `constexpr` 定义一个数组大小常量，并声明一个数组
  3. 用 `decltype` 推导一个表达式的类型
- 限制条件：每个 `auto` 变量必须有初始化表达式
- 成功标准：能解释 `auto` 是编译期推导不是动态类型，能解释 `constexpr` 和 `const` 的区别
- 常见错误：`auto` 不初始化、把 `auto` 当动态类型、`constexpr` 函数忘记 `return`
- 反馈重点：`auto` 的推导规则和 `constexpr` 的编译期语义

---

## BASICS-03：new/delete vs malloc/free

- 目标技能：理解 C++ 动态内存分配与 C 的区别
- 起始文件：无
- 任务要求：
  1. 用 `malloc`/`free` 分配一个 `int` 并赋值打印（C 写法）
  2. 用 `new`/`delete` 做同样的事情（C++ 写法）
  3. 用 `new` 分配一个数组，用 `delete[]` 释放
  4. 写一段代码演示 `new` 调用构造函数、`malloc` 不调用构造函数（用一个自定义类）
- 限制条件：不能混用 `new`/`free` 或 `malloc`/`delete`
- 成功标准：能解释 `new` 和 `malloc` 的三个区别（构造函数、返回类型、失败行为）
- 常见错误：`new` 分配的数组用 `delete` 而不是 `delete[]`、混用 `new`/`free`
- 反馈重点：构造函数调用时机和内存管理正确配对

---

## BASICS-04：引用传参替代指针传参

- 目标技能：理解引用的语义并用引用替代指针传参
- 起始文件：以下 C 代码
  ```c
  void swap(int* a, int* b) {
      int temp = *a;
      *a = *b;
      *b = temp;
  }
  int main() {
      int x = 10, y = 20;
      swap(&x, &y);
      // 打印 x, y
  }
  ```
- 任务要求：
  1. 将 `swap` 函数改写为引用传参版本
  2. 将调用处的 `&x, &y` 改为直接传 `x, y`
  3. 再写一个函数 `increment(int& n)`，将参数加 1
  4. 尝试用 `const int&` 传参给一个只读函数，理解为什么比值传递高效
- 限制条件：不能使用指针
- 成功标准：能解释引用和指针的三个区别（必须初始化、不能为 null、不能重新绑定）
- 常见错误：`void f(int& x)` 调用时传字面量 `f(5)`（编译错误）、引用没有取地址
- 反馈重点：引用是别名不是指针，调用处不需要任何额外语法

---

## BASICS-05：函数重载

- 目标技能：理解函数重载的规则和用途
- 起始文件：无
- 任务要求：
  1. 写三个重载函数 `print`：一个接受 `int`，一个接受 `double`，一个接受 `std::string`
  2. 写两个重载函数 `max`：一个接受两个 `int`，一个接受两个 `double`
  3. 尝试写两个参数类型相同但返回类型不同的重载，观察编译器报什么错误
  4. 尝试写 `void f(int x)` 和 `void f(const int x)`，观察是否能重载
- 限制条件：不能使用模板
- 成功标准：能解释重载解析按参数类型和数量，不是按返回类型；`const` 值参数不算重载
- 常见错误：以为返回类型不同就能重载、以为 `const` 值参数能区分重载
- 反馈重点：重载的判定规则——参数类型、数量、顺序（不含返回类型）

---

## BASICS-06：std::string 基本操作

- 目标技能：掌握 std::string 的常用操作
- 起始文件：无
- 任务要求：
  1. 创建 string 对象，用 `+` 拼接，用 `+=` 追加
  2. 用 `find` 查找子串，用 `substr` 截取子串
  3. 用 `replace` 替换子串
  4. 用 `size()` / `length()` 获取长度，用 `empty()` 判断是否为空
  5. `string` 和 `const char*` 互相转换
- 限制条件：不能使用 C 的 `strcat`、`strcpy`、`strlen`
- 成功标准：能用 string 完成字符串拼接、查找、替换，能解释和 C 字符串函数的区别
- 常见错误：`find` 返回 `string::npos` 表示未找到（不是 -1）、`substr` 的参数是起始位置和长度
- 反馈重点：string 自动管理内存，不需要手动分配和释放

---

## BASICS-07：range-based for 循环

- 目标技能：掌握基于范围的 for 循环
- 起始文件：无
- 任务要求：
  1. 用普通 for 循环遍历数组 `int arr[] = {1, 2, 3, 4, 5}`
  2. 用 range-based for 重写
  3. 用 `auto` 简化 range-based for
  4. 用 `for (auto& x : arr)` 修改数组元素（每个元素乘以 2）
  5. 尝试用 range-based for 遍历 `std::string` 的每个字符
- 限制条件：至少使用一次 `auto` 和一次引用
- 成功标准：能解释 range-based for 的等价普通 for 写法，能解释什么时候必须用引用
- 常见错误：遍历时修改容器大小、不用引用导致无法修改元素
- 反馈重点：range-based for 是语法糖，编译器展开为迭代器或指针操作

---

## BASICS-08：const 与类型安全

- 目标技能：理解 C++ 中 const 的增强语义
- 起始文件：无
- 任务要求：
  1. 声明 `const int MAX = 100;`，用它作为数组大小（验证 C++ 的 const 是编译期常量）
  2. 声明 `const int* p`、`int* const p`、`const int* const p`，分别解释含义
  3. 写一个函数 `void print(const std::string& s)`，解释为什么用 `const` 引用
  4. 尝试修改 `const` 变量，观察编译错误
- 限制条件：不能使用 `const_cast`
- 成功标准：能区分三种 const 指针的含义，能解释 const 引用的优势（避免拷贝 + 防止修改）
- 常见错误：`const int*` 和 `int* const` 搞混、以为 `const` 引用可以延长临时对象的生命周期（可以但要知道规则）
- 反馈重点：`const` 在左边是值不可变，在右边是指针不可变
