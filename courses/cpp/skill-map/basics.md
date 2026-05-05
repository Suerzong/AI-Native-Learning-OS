# 基本语法、输入输出、数据类型 技能地图

## 目标

学习者能编写、编译、运行 C++ 程序，理解 C++ 的基本数据类型和输入输出机制，能对比 C 的等价写法。

## 必会概念

- `#include <iostream>` 的作用
- `std::cout` / `std::cin` / `std::endl`
- `std::string` vs `char[]`
- `bool` 类型
- `auto` 类型推导（编译期）
- `decltype` 类型推导
- `constexpr` 编译期常量
- `nullptr` vs `NULL`
- `const` 在 C++ 中的增强语义
- `using` 类型别名（替代 `typedef`）

## 必会语法

```cpp
// 输出
std::cout << "Hello" << std::endl;
std::cout << "x = " << x << ", y = " << y << std::endl;

// 输入
int n;
std::cin >> n;
std::string name;
std::cin >> name;

// string
std::string s = "Hello";
std::string s2 = s + " World";
s.size();      // 长度
s.empty();     // 是否为空
s.find("ll");  // 查找
s.substr(0, 3); // 截取

// auto
auto x = 42;        // int
auto d = 3.14;      // double
auto s = "hello";   // const char*

// constexpr
constexpr int MAX = 100;
int arr[MAX];  // OK in C++

// nullptr
int* p = nullptr;  // 不是 NULL

// using
using IntVector = std::vector<int>;
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `printf("x=%d\n", x)` | `std::cout << "x=" << x << std::endl` | 输出 |
| `scanf("%d", &x)` | `std::cin >> x` | 输入 |
| `char s[100]` | `std::string s` | 字符串 |
| `#define MAX 100` | `constexpr int MAX = 100` | 常量 |
| `typedef struct { ... } Foo;` | `using Foo = struct { ... };` | 类型别名 |
| `NULL` | `nullptr` | 空指针 |

## 常见错误

1. 忘记 `std::` 前缀
2. 用 `.c` 后缀编译 C++ 文件（应该用 `.cpp`）
3. `<<` 和 `>>` 方向搞反
4. `auto` 不初始化
5. 把 `auto` 当动态类型

## 训练阶梯

1. **识别**：写出 Hello World，识别 `cout`、`cin`、`endl` 的作用
2. **解释**：解释 `auto x = 42;` 的类型推导过程
3. **修改**：将 C 的 `printf` 程序改写为 `cout`
4. **编写**：从零写一个用户输入、计算、输出的程序
5. **迁移**：用 `string` 替换程序中的所有 `char[]`

## 掌握标准

- 能独立编写、编译、运行 C++ 程序
- 能用 `cout`/`cin` 替代 `printf`/`scanf`
- 能解释 `auto`、`constexpr`、`nullptr` 的含义和用途
- 能用 `string` 替代 `char[]`

## 参考

- runoob.com/cplusplus/cpp-basic-syntax.html
- runoob.com/cplusplus/cpp-data-types.html
- runoob.com/cplusplus/cpp-variable-types.html
