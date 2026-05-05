# 数组与动态数组 技能地图

## 目标

学习者理解数组的内存布局和随机访问原理，能用 C 实现动态数组，能分析各操作的复杂度，能比较数组和链表的差异。

## 必会概念

- 数组：连续内存存储的固定大小元素集合
- 随机访问：通过下标直接计算地址，O(1)
- 动态数组：可自动扩容的数组（C++ vector 底层实现）
- 扩容策略：容量不足时分配 2 倍新空间，复制旧数据

## 操作复杂度

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 按索引访问 `arr[i]` | O(1) | 随机访问 |
| 按索引修改 `arr[i] = val` | O(1) | 随机访问 |
| 尾部插入 | O(1) 均摊 | 动态数组可能触发扩容 O(n) |
| 尾部删除 | O(1) | |
| 中间插入 | O(n) | 需要移动后续元素 |
| 中间删除 | O(n) | 需要移动后续元素 |
| 线性查找 | O(n) | 无序数组 |
| 二分查找 | O(log n) | 有序数组 |

## C 语言实现要点

```c
// 动态数组结构体
typedef struct {
    int* data;      // 数据指针
    int size;       // 当前元素个数
    int capacity;   // 当前容量
} DynamicArray;

// 关键操作
void init(DynamicArray* arr, int capacity);     // 初始化
void push_back(DynamicArray* arr, int val);     // 尾部插入
void pop_back(DynamicArray* arr);               // 尾部删除
int get(DynamicArray* arr, int index);          // 按索引访问
void set(DynamicArray* arr, int index, int val);// 按索引修改
void destroy(DynamicArray* arr);                // 释放内存
```

## 扩容机制

```
初始 capacity = 4
size = 4, 插入第 5 个元素：
1. 新 capacity = 4 * 2 = 8
2. malloc(8 * sizeof(int))
3. 将旧数据 memcpy 到新空间
4. free(旧 data)
5. data = 新指针
6. 插入新元素，size = 5
```

## 嵌入式场景考量

- 数组访问对 CPU 缓存友好（连续内存）
- 动态数组的扩容在嵌入式中可能不可用（无 malloc）
- 固定大小数组是嵌入式首选
- 环形缓冲区是数组在嵌入式中最常见的变体

## 常见错误

- 数组越界（C 不检查越界，导致未定义行为）
- 动态数组扩容后忘记 free 旧内存
- 将 capacity 和 size 混淆
- 忘记在 push_back 前检查是否需要扩容

## 训练阶梯

1. **识别**：画出数组在内存中的布局（连续字节）
2. **理解**：解释为什么 `arr[i]` 是 O(1)
3. **基本操作**：实现 init、push_back、get、set
4. **扩容**：实现自动扩容（2 倍策略）
5. **插入删除**：实现在中间位置插入和删除
6. **对比**：和链表做复杂度对比表

## 参考

- runoob.com/data-structures/array.html
