# 运算符重载 技能地图

## 目标

学习者能为自定义类重载常用运算符，理解重载的规则和限制，能用友元函数重载流运算符。

## 必会概念

- 运算符重载的规则（不能创建新运算符、不能改变优先级）
- 成员函数重载 vs 友元函数重载
- 可重载的运算符列表
- 只能用成员函数重载的运算符（`=`、`()`、`[]`、`->`）
- 流运算符 `<<` 和 `>>` 通常用友元函数重载

## 必会语法

```cpp
class Vector2D {
private:
    double x_, y_;
public:
    Vector2D(double x = 0, double y = 0) : x_(x), y_(y) {}

    // 成员函数重载：二元运算符（左操作数是 this）
    Vector2D operator+(const Vector2D& rhs) const {
        return Vector2D(x_ + rhs.x_, y_ + rhs.y_);
    }

    Vector2D operator-(const Vector2D& rhs) const {
        return Vector2D(x_ - rhs.x_, y_ - rhs.y_);
    }

    // 成员函数重载：一元运算符
    Vector2D operator-() const {
        return Vector2D(-x_, -y_);
    }

    // 成员函数重载：比较运算符
    bool operator==(const Vector2D& rhs) const {
        return x_ == rhs.x_ && y_ == rhs.y_;
    }

    // 成员函数重载：赋值运算符
    Vector2D& operator=(const Vector2D& rhs) {
        if (this != &rhs) {
            x_ = rhs.x_;
            y_ = rhs.y_;
        }
        return *this;
    }

    // 下标运算符
    double& operator[](int i) {
        return (i == 0) ? x_ : y_;
    }

    // 友元函数重载：流运算符
    friend std::ostream& operator<<(std::ostream& os, const Vector2D& v) {
        os << "(" << v.x_ << ", " << v.y_ << ")";
        return os;
    }
};

// 使用
Vector2D a(1, 2), b(3, 4);
Vector2D c = a + b;
std::cout << c << std::endl;  // (4, 6)
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `vector2d_add(&a, &b, &c)` | `c = a + b` | 向量加法 |
| `vector2d_equal(&a, &b)` | `a == b` | 比较 |
| `printf("(%f, %f)", v.x, v.y)` | `cout << v` | 输出 |

## 常见错误

1. `<<` 和 `>>` 用成员函数重载（应该用友元函数，因为左操作数是 stream）
2. 忘记检查自赋值 `if (this != &rhs)`
3. 返回引用而不是值（对于 `+` 应该返回新对象）
4. 重载太多运算符导致代码难以理解

## 训练阶梯

1. **识别**：在代码中找出运算符重载的定义
2. **解释**：解释 `operator<<` 为什么要用友元函数
3. **修改**：为已有类添加 `==` 和 `<` 运算符重载
4. **编写**：从零为 Vector2D 类重载 `+`、`-`、`<<`
5. **迁移**：为自定义类重载 `[]` 和 `()`

## 掌握标准

- 能为自定义类重载常用运算符
- 能正确使用友元函数重载流运算符
- 能解释成员函数和友元函数重载的区别
- 能解释运算符重载的限制

## 参考

- runoob.com/cplusplus/cpp-overloading.html
