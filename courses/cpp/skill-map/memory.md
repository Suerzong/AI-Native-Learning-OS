# 指针、引用、智能指针、动态内存 技能地图

## 目标

学习者能正确管理 C++ 中的动态内存，理解 RAII 原则，能用智能指针替代裸指针，能对比 C 的 malloc/free。

## 必会概念

- `new` / `delete` vs `malloc` / `free`
- `new[]` / `delete[]`
- 引用 vs 指针
- RAII（Resource Acquisition Is Initialization）原则
- `unique_ptr`：独占所有权
- `shared_ptr`：共享所有权（引用计数）
- `weak_ptr`：弱引用，解决循环引用
- 循环引用问题

## 必会语法

```cpp
// new / delete
int* p = new int(42);        // 分配并初始化
delete p;                     // 释放

int* arr = new int[100];     // 分配数组
delete[] arr;                 // 释放数组

// unique_ptr（独占所有权）
auto p1 = std::make_unique<int>(42);
std::cout << *p1 << std::endl;

// unique_ptr 管理对象
auto sensor = std::make_unique<Sensor>("temp", 25.0);
sensor->setValue(30.0);

// unique_ptr 不能拷贝，只能移动
auto p2 = std::move(p1);  // p1 变为 nullptr

// shared_ptr（共享所有权，引用计数）
auto sp1 = std::make_shared<int>(42);
auto sp2 = sp1;  // 引用计数 +1
std::cout << sp1.use_count() << std::endl;  // 2
sp2.reset();     // 引用计数 -1
std::cout << sp1.use_count() << std::endl;  // 1

// weak_ptr（解决循环引用）
class Node {
public:
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // 用 weak_ptr 打破循环
    ~Node() { std::cout << "Node destroyed" << std::endl; }
};

// RAII 示例
class FileHandler {
private:
    FILE* fp_;
public:
    FileHandler(const char* filename) : fp_(fopen(filename, "r")) {
        if (!fp_) throw std::runtime_error("Cannot open file");
    }
    ~FileHandler() { if (fp_) fclose(fp_); }

    // 禁止拷贝
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| `malloc(sizeof(int))` | `new int` | 分配 |
| `free(p)` | `delete p` | 释放 |
| `malloc(n * sizeof(int))` | `new int[n]` | 分配数组 |
| `free(arr)` | `delete[] arr` | 释放数组 |
| 手动 malloc/free 配对 | 智能指针自动管理 | 内存管理 |
| 可能忘记 free（内存泄漏） | RAII 自动释放 | 安全性 |

## 常见错误

1. `new` 分配的用 `free` 释放（未定义行为）
2. `new[]` 分配的用 `delete` 释放（未定义行为）
3. 忘记 `delete` 导致内存泄漏
4. `shared_ptr` 的循环引用（用 `weak_ptr` 解决）
5. 不要用裸 `new` 初始化多个 `shared_ptr`
6. `unique_ptr` 不能赋值（只能移动）

## 训练阶梯

1. **识别**：在代码中找出 new/delete 配对
2. **解释**：解释 RAII 原则
3. **修改**：将裸指针代码改为 unique_ptr
4. **编写**：用 shared_ptr 实现共享数据
5. **迁移**：解决循环引用问题

## 掌握标准

- 能正确使用 new/delete 配对
- 能用 unique_ptr 管理独占资源
- 能用 shared_ptr 管理共享资源
- 能解释循环引用问题并用 weak_ptr 解决
- 能理解 RAII 原则

## 参考

- runoob.com/cplusplus/cpp-dynamic-memory.html
