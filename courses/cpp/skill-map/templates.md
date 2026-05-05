# 函数模板、类模板 技能地图

## 目标

学习者能编写函数模板和类模板，理解模板实例化，能对比 C 的宏实现泛型方式。

## 必会概念

- 函数模板的定义和实例化
- 类模板的定义和实例化
- 模板参数推导
- 模板特化（全特化和偏特化）
- 模板定义放在头文件中的必要性
- SFINAE 基本概念（替换失败不是错误）
- 可变参数模板

## 必会语法

```cpp
// 函数模板
template<typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// 使用
int x = max(3, 5);         // T 推导为 int
double d = max(3.14, 2.71); // T 推导为 double

// 显式指定类型
auto s = max<std::string>("hello", "world");

// 函数模板特化
template<>
const char* max<const char*>(const char* a, const char* b) {
    return (strcmp(a, b) > 0) ? a : b;
}

// 类模板
template<typename T>
class Stack {
private:
    std::vector<T> data_;
public:
    void push(const T& value) { data_.push_back(value); }
    void pop() { data_.pop_back(); }
    T& top() { return data_.back(); }
    bool empty() const { return data_.empty(); }
    size_t size() const { return data_.size(); }
};

// 使用
Stack<int> si;
si.push(42);
Stack<std::string> ss;
ss.push("hello");

// 类模板特化
template<typename T>
class Printer {
public:
    void print(const T& value) { std::cout << value; }
};

template<>
class Printer<std::vector<int>> {
public:
    void print(const std::vector<int>& v) {
        for (auto x : v) std::cout << x << " ";
    }
};
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `#define MAX(a,b) ((a)>(b)?(a):(b))` | `template<T> T max(T a, T b)` | 泛型最大值 |
| `void*` + 类型转换 | `T` 类型安全的模板参数 | 类型安全 |
| 手写 `int_stack_push`、`double_stack_push` | `Stack<int>`、`Stack<double>` | 泛型容器 |

## 常见错误

1. 模板定义放在 `.cpp` 文件中——链接时报 undefined reference
2. 模板编译错误信息非常长
3. 以为模板可以处理任何类型——某些类型不支持 `>` 运算符
4. 类模板的成员函数定义必须在头文件中
5. 混淆全特化和偏特化的语法

## 训练阶梯

1. **识别**：在标准库源码中找到模板使用
2. **解释**：解释模板实例化过程
3. **修改**：为已有函数模板添加特化版本
4. **编写**：从零实现 `Stack<T>` 类模板
5. **迁移**：实现 `Pair<T1, T2>` 类模板

## 掌握标准

- 能独立编写函数模板和类模板
- 能解释模板实例化的概念
- 能写出简单的模板特化
- 能理解为什么模板定义要放头文件

## 参考

- runoob.com/cplusplus/cpp-templates.html
