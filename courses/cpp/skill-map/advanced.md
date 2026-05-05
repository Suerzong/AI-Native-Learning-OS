# 异常处理、命名空间、文件 I/O、多线程基础 技能地图

## 目标

学习者能用异常处理错误、用命名空间组织代码、用文件 I/O 读写数据、用多线程实现并发，能对比 C 的等价机制。

## 必会概念

- `try` / `catch` / `throw`
- 标准异常类（`std::exception` 及其派生类）
- 异常安全（嵌入式环境下通常禁用异常）
- `namespace` 命名空间
- 匿名命名空间
- `ifstream` / `ofstream` / `fstream`
- `std::thread` 创建和管理线程
- `std::mutex` 互斥锁
- `std::lock_guard` RAII 锁管理
- 竞态条件和死锁

## 必会语法

```cpp
// ===== 异常处理 =====
try {
    std::ifstream file("data.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Cannot open file");
    }
    // 处理文件
} catch (const std::runtime_error& e) {
    std::cerr << "Error: " << e.what() << std::endl;
} catch (const std::exception& e) {
    std::cerr << "Exception: " << e.what() << std::endl;
}

// ===== 命名空间 =====
namespace sensor {
    class Temperature {
        // ...
    };
    void init() { /* ... */ }
}

// 使用
sensor::Temperature temp;
sensor::init();

// using 声明
using sensor::Temperature;
Temperature t;

// 匿名命名空间（替代 C 的 static）
namespace {
    void helperFunction() { /* 仅本文件可见 */ }
}

// ===== 文件 I/O =====
// 写文件
std::ofstream out("log.txt");
out << "Temperature: " << 25.5 << std::endl;
out.close();

// 读文件
std::ifstream in("data.txt");
std::string line;
while (std::getline(in, line)) {
    std::cout << line << std::endl;
}

// 二进制读写
std::ofstream bin_out("data.bin", std::ios::binary);
int value = 42;
bin_out.write(reinterpret_cast<char*>(&value), sizeof(value));

// ===== 多线程 =====
#include <thread>
#include <mutex>

std::mutex mtx;

void threadFunction(int id) {
    std::lock_guard<std::mutex> lock(mtx);
    std::cout << "Thread " << id << " running" << std::endl;
}

// 创建线程
std::thread t1(threadFunction, 1);
std::thread t2(threadFunction, 2);
t1.join();
t2.join();

// Lambda 线程
std::thread t3([]() {
    std::cout << "Lambda thread" << std::endl;
});
t3.join();
```

## C vs C++ 对比

| C | C++ | 说明 |
|---|-----|------|
| 返回值/errno 检查错误 | try/catch/throw | 错误处理 |
| 函数名前缀避免冲突 | namespace | 命名空间 |
| `fopen`/`fclose`/`fprintf` | `ifstream`/`ofstream`/`<<`/`>>` | 文件 I/O |
| `pthread_create`/`pthread_join` | `std::thread`/`join()` | 多线程 |
| `pthread_mutex_lock/unlock` | `std::lock_guard<std::mutex>` | 锁 |

## 常见错误

1. 异常处理中捕获值而不是引用（导致切片）
2. 析构函数中抛出异常
3. 头文件中使用 `using namespace std`
4. 创建 thread 后忘记 join 或 detach
5. 不用 lock_guard 手动 lock/unlock（容易忘记 unlock）
6. 死锁——按固定顺序加锁避免

## 训练阶梯

1. **识别**：在代码中找出异常处理和命名空间使用
2. **解释**：解释 try/catch 的执行流程
3. **修改**：用命名空间重组代码
4. **编写**：实现多线程安全的数据读写
5. **迁移**：用 CMake 管理多文件多线程项目

## 掌握标准

- 能用异常处理常见错误场景
- 能用命名空间组织项目代码
- 能用 ifstream/ofstream 读写文件
- 能用 thread + mutex 实现线程安全
- 能解释嵌入式环境下异常和多线程的约束

## 参考

- runoob.com/cplusplus/cpp-exceptions-handling.html
- runoob.com/cplusplus/cpp-namespaces.html
- runoob.com/cplusplus/cpp-files-streams.html
