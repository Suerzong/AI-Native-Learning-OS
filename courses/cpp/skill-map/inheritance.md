# 继承、多态、虚函数、抽象类 技能地图

## 目标

学习者能用继承和多态组织代码，理解虚函数机制，能设计简单的类继承体系，能对比 C 的函数指针表模拟多态。

## 必会概念

- 继承（单继承、多继承、虚继承）
- 访问控制在继承中的变化（public/protected/private 继承）
- 构造析构顺序
- 组合 vs 继承（"有一个" vs "是一个"）
- 虚函数与 `override`
- 纯虚函数与抽象类
- vtable（虚函数表）基本概念
- 虚析构函数的必要性

## 必会语法

```cpp
// 单继承
class Device {
protected:
    std::string name_;
public:
    Device(const std::string& name) : name_(name) {}
    virtual ~Device() = default;  // 虚析构函数

    virtual void init() = 0;      // 纯虚函数
    virtual int read(char* buf, int len) = 0;
    virtual int write(const char* buf, int len) = 0;

    const std::string& getName() const { return name_; }
};

class UARTDevice : public Device {
public:
    UARTDevice(const std::string& name) : Device(name) {}

    void init() override {
        std::cout << "UART init: " << name_ << std::endl;
    }

    int read(char* buf, int len) override {
        // 模拟实现
        return 0;
    }

    int write(const char* buf, int len) override {
        // 模拟实现
        return len;
    }
};

// 多态使用
void testDevice(Device* dev) {
    dev->init();  // 调用派生类的 init
    // 通过基类指针操作派生类对象
}

// 多继承（慎用）
class A { public: virtual void f() {} };
class B { public: virtual void g() {} };
class C : public A, public B {
    void f() override {}
    void g() override {}
};

// 虚继承（解决菱形问题）
class Base { public: int x; };
class D1 : virtual public Base {};
class D2 : virtual public Base {};
class DD : public D1, public D2 {};  // 只有一份 Base::x
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| struct + 函数指针表模拟多态 | virtual 虚函数 | 多态机制 |
| 手动维护函数指针表 | 编译器自动生成 vtable | 实现细节 |
| 手动传 `this` 指针 | 自动传 `this` 指针 | 成员函数 |
| 没有继承机制 | 语言级继承支持 | 代码复用 |

## 常见错误

1. 基类析构函数没有声明为 virtual——通过基类指针 delete 时派生类析构函数不调用
2. 派生类构造函数没有调用基类构造函数
3. 以为继承可以替代组合——"有一个"关系应该用组合
4. 多继承导致的菱形问题
5. 构造函数中调用虚函数不会多态（对象还没完全构造）
6. 忘记写 `override` 标记

## 训练阶梯

1. **识别**：在代码中找出继承关系和虚函数声明
2. **解释**：解释虚析构函数的必要性
3. **修改**：为已有类添加继承和虚函数
4. **编写**：设计 Device → UARTDevice / SPIDriver 继承体系
5. **迁移**：设计新的抽象基类和派生类

## 掌握标准

- 能设计简单的继承体系
- 能正确使用虚函数和纯虚函数
- 能解释构造析构顺序
- 能解释 vtable 的基本概念
- 能区分什么时候用继承、什么时候用组合

## 参考

- runoob.com/cplusplus/cpp-inheritance.html
- runoob.com/cplusplus/cpp-polymorphism.html
