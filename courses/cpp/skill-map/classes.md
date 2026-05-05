# 类、对象、构造析构、this 指针 技能地图

## 目标

学习者能定义类、创建对象、编写构造函数和析构函数，理解封装的意义，能对比 C 的 struct + 函数模式。

## 必会概念

- class vs struct（默认访问权限不同）
- 访问控制：`public`、`private`、`protected`
- 封装的意义
- 构造函数（默认、带参、拷贝）
- 析构函数
- 初始化列表
- this 指针
- static 成员变量和 static 成员函数
- 对象生命周期（栈对象 vs 堆对象）

## 必会语法

```cpp
// 类定义
class Sensor {
private:
    std::string name_;
    double value_;

public:
    // 默认构造函数
    Sensor() : name_("unknown"), value_(0.0) {}

    // 带参构造函数（初始化列表）
    Sensor(const std::string& name, double value)
        : name_(name), value_(value) {}

    // 析构函数
    ~Sensor() {
        std::cout << "Sensor " << name_ << " destroyed" << std::endl;
    }

    // 成员函数
    void setValue(double v) { value_ = v; }
    double getValue() const { return value_; }
    const std::string& getName() const { return name_; }

    // this 指针
    Sensor& setName(const std::string& name) {
        this->name_ = name;
        return *this;  // 链式调用
    }
};

// 静态成员
class Counter {
private:
    static int count_;  // 类内声明

public:
    Counter() { ++count_; }
    ~Counter() { --count_; }
    static int getCount() { return count_; }  // 静态成员函数
};
int Counter::count_ = 0;  // 类外定义（C++17 允许 inline static）
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `typedef struct { int x; } Foo;` | `class Foo { int x; public: ... };` | 类型定义 |
| `foo_init(&f)` | `Foo f;`（自动调用构造函数） | 初始化 |
| `foo_destroy(&f)` | 对象离开作用域自动析构 | 清理 |
| `foo_get_x(&f)` | `f.getX()` | 访问数据 |
| 全局变量 + 文件作用域 | static 成员变量 | 共享状态 |

## 常见错误

1. 类定义末尾忘记分号
2. 在类外部定义成员函数忘记 `ClassName::` 作用域
3. 构造函数初始化列表顺序和成员声明顺序不一致（有警告）
4. 构造函数忘记初始化所有成员
5. 以为 `private` 成员在类外部可以直接访问
6. `const` 对象只能调用 `const` 成员函数

## 训练阶梯

1. **识别**：在一个类定义中找出 private/public 成员
2. **解释**：解释封装的意义——为什么要 private
3. **修改**：为已有类添加构造函数和析构函数
4. **编写**：从零定义一个完整的 Sensor 类
5. **迁移**：用 this 指针实现链式调用

## 掌握标准

- 能独立定义类，合理使用访问控制
- 能写出带初始化列表的构造函数
- 能解释对象生命周期和析构函数调用时机
- 能用 this 指针实现链式调用
- 能定义和使用 static 成员

## 参考

- runoob.com/cplusplus/cpp-classes-objects.html
- runoob.com/cplusplus/cpp-constructor-destructor.html
