# 条件、循环、跳转 技能地图

## 目标

学习者能用 C++ 的条件和循环语句编写程序，掌握 C++ 新增的语法糖（range-based for、if 初始化语句），能对比 C 的等价写法。

## 必会概念

- `if` / `else if` / `else`（与 C 相同）
- `if constexpr`（编译期条件，C++17）
- `if` 初始化语句（C++17）
- `switch`（与 C 基本相同）
- `while` / `do-while`（与 C 相同）
- `for`（与 C 相同）
- range-based for（C++11）
- `break` / `continue` / `goto`（与 C 相同）

## 必会语法

```cpp
// if 初始化语句 (C++17)
if (auto x = getValue(); x > 0) {
    std::cout << "positive: " << x << std::endl;
}

// if constexpr (编译期条件)
template<typename T>
void print(T value) {
    if constexpr (std::is_integral_v<T>) {
        std::cout << "int: " << value;
    } else {
        std::cout << "other: " << value;
    }
}

// range-based for
std::vector<int> v = {1, 2, 3, 4, 5};
for (auto x : v) {           // 值拷贝
    std::cout << x << " ";
}
for (auto& x : v) {          // 引用，可修改
    x *= 2;
}
for (const auto& x : v) {    // const 引用，只读且高效
    std::cout << x << " ";
}

// 遍历 string
std::string s = "Hello";
for (char c : s) {
    std::cout << c << " ";
}

// 遍历数组
int arr[] = {1, 2, 3};
for (auto x : arr) {
    std::cout << x << " ";
}
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `for (int i = 0; i < n; i++) printf("%d ", a[i]);` | `for (auto x : a) cout << x << " ";` | 遍历数组 |
| `for (int i = 0; i < n; i++) a[i] *= 2;` | `for (auto& x : a) x *= 2;` | 修改元素 |
| 声明变量再判断 | `if (auto x = f(); x > 0)` | 初始化判断 |

## 常见错误

1. range-based for 中不用引用导致无法修改元素
2. 遍历时增删容器元素导致迭代器失效
3. 以为 `if constexpr` 可以用于运行时条件
4. range-based for 不适用于 C 风格的指针操作

## 训练阶梯

1. **识别**：在已有代码中找到 range-based for 并解释其作用
2. **解释**：解释 `for (auto& x : v)` 和 `for (auto x : v)` 的区别
3. **修改**：将普通 for 循环改写为 range-based for
4. **编写**：用 range-based for 遍历 vector 并统计元素
5. **迁移**：用 `if` 初始化语句改写嵌套判断

## 掌握标准

- 能用 range-based for 遍历数组、vector、string
- 能解释什么时候用值、什么时候用引用
- 能用 `if` 初始化语句简化代码
- 能解释 range-based for 的等价普通 for 写法

## 参考

- runoob.com/cplusplus/cpp-loop-types.html
- runoob.com/cplusplus/cpp-decision-making.html
