# 函数、重载、默认参数、引用 技能地图

## 目标

学习者能用 C++ 的函数新特性编写程序，理解引用传参、函数重载、默认参数，能对比 C 的指针传参和宏函数。

## 必会概念

- 引用（`int&`）——变量的别名
- 引用 vs 指针的区别
- 函数重载（同名不同参数）
- 默认参数
- `inline` 函数（替代宏函数）
- `const` 引用传参（高效只读）

## 必会语法

```cpp
// 引用传参（替代指针传参）
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}
// 调用：swap(x, y); 不需要 &

// const 引用（高效只读传参）
void print(const std::string& s) {
    std::cout << s << std::endl;
}

// 默认参数
void greet(const std::string& name = "World") {
    std::cout << "Hello, " << name << std::endl;
}
greet();        // Hello, World
greet("Ethen"); // Hello, Ethen

// 函数重载
int max(int a, int b) { return a > b ? a : b; }
double max(double a, double b) { return a > b ? a : b; }
std::string max(const std::string& a, const std::string& b) {
    return a > b ? a : b;
}

// inline 函数（替代宏函数）
inline int square(int x) { return x * x; }

// 默认参数只能从右向左
void f(int a, int b = 10, int c = 20);  // OK
// void f(int a = 5, int b);  // 错误
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `void swap(int* a, int* b)` + 调用 `swap(&x, &y)` | `void swap(int& a, int& b)` + 调用 `swap(x, y)` | 交换 |
| `#define SQUARE(x) ((x)*(x))` | `inline int square(int x) { return x*x; }` | 平方 |
| `void f(int a, int b)` + `void f_d(int a)` | `void f(int a, int b = 0)` | 默认参数 |
| 不同名函数 `max_int`、`max_double` | 同名重载 `max(int)`、`max(double)` | 重载 |
| `void print(const char* s)` 传指针 | `void print(const string& s)` 传 const 引用 | 只读传参 |

## 引用 vs 指针

| 特性 | 引用 | 指针 |
|------|------|------|
| 必须初始化 | 是 | 否 |
| 可以为 null | 否 | 是 |
| 可以重新绑定 | 否 | 是 |
| 调用处语法 | 直接传变量 | 需要 `&` 取地址 |
| 访问成员 | `r.member` | `p->member` |

## 常见错误

1. 引用没有初始化就使用
2. 以为引用可以重新赋值
3. `void f(int& x)` 调用时传字面量 `f(5)`——编译错误
4. 默认参数从左向右声明
5. 重载只按返回类型不同——编译错误
6. `const` 值参数不算重载——`void f(int x)` 和 `void f(const int x)` 是同一函数

## 训练阶梯

1. **识别**：在代码中找出引用传参的位置，解释为什么比指针传参好
2. **解释**：解释引用和指针的三个区别
3. **修改**：将 C 的指针传参 swap 改为引用传参
4. **编写**：写出一组重载函数 print
5. **迁移**：为自定义函数添加默认参数

## 掌握标准

- 能用引用传参替代指针传参
- 能写出函数重载并解释重载解析规则
- 能写出带默认参数的函数
- 能解释 `const` 引用传参的优势

## 参考

- runoob.com/cplusplus/cpp-functions.html
- runoob.com/cplusplus/cpp-references.html
