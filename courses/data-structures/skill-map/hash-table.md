# 哈希表 技能地图

## 目标

学习者理解哈希函数和冲突处理原理，能用 C++ 实现链地址法的哈希表，能分析负载因子和扩容的影响。

## 必会概念

- 哈希函数：将 key 映射到数组下标的函数
- 哈希冲突：不同 key 映射到同一位置
- 链地址法（Separate Chaining）：每个位置用链表存储冲突元素
- 开放寻址法（Open Addressing）：冲突时探测下一个空位
- 负载因子（Load Factor）：元素数 / 容量
- 扩容：负载因子超过阈值时增大容量并重新哈希

## 操作复杂度

| 操作 | 平均 | 最坏（所有 key 冲突） | 说明 |
|------|------|---------------------|------|
| 插入 put | O(1) | O(n) | 链地址法平均 O(1) |
| 查找 get | O(1) | O(n) | 最坏退化为链表查找 |
| 删除 remove | O(1) | O(n) | 需要在链表中找到并删除 |
| 扩容 resize | O(n) | O(n) | 重新哈希所有元素 |

## 哈希函数设计

```c
// 简单的取模哈希
int hash(int key, int capacity) {
    return key % capacity;
}

// 字符串哈希（DJB2 简化版）
unsigned int hashString(const char* str, int capacity) {
    unsigned int hash = 5381;
    while (*str)
        hash = ((hash << 5) + hash) + *str++;
    return hash % capacity;
}
```

## 链地址法实现结构

```
hashTable[0] -> (key1, val1) -> (key2, val2) -> NULL
hashTable[1] -> NULL
hashTable[2] -> (key3, val3) -> NULL
hashTable[3] -> (key4, val4) -> (key5, val5) -> NULL
...
```

## C++ 实现要点

```cpp
class HashTable {
    struct Entry {
        int key;
        int val;
        Entry* next;
    };
    vector<Entry*> table;
    int capacity;
    int size_;
    double loadFactorThreshold;

    int hash(int key) { return key % capacity; }

    void resize() {
        // 容量翻倍，重新哈希所有元素
        // 注意：容量最好取质数
    }
public:
    void put(int key, int val);
    int get(int key);
    void remove(int key);
};
```

## 开放寻址法

| 探测方式 | 公式 | 特点 |
|---------|------|------|
| 线性探测 | `(hash + i) % capacity` | 简单，但有聚集问题 |
| 二次探测 | `(hash + i*i) % capacity` | 缓解聚集 |
| 双重哈希 | `(hash1 + i * hash2) % capacity` | 分布最均匀 |

开放寻址法的删除需要使用"墓碑标记"，不能直接置空。

## 容量选择

- 最好选择质数作为容量（减少哈希冲突）
- 常见选择：17, 37, 67, 131, 257, 521...
- 扩容时取下一个质数

## 常见错误

- key 已存在时 put 应更新 value 而不是新增
- 删除时忘记维护 size
- 扩容后忘记重新哈希所有元素
- 开放寻址法删除时没有用墓碑标记
- 哈希函数取模时 key 为负数

## 嵌入式场景考量

- 哈希表需要动态分配，在嵌入式中可能受限
- 固定大小的哈希表（不扩容）可以使用
- 简单场景可用数组+线性查找代替

## 训练阶梯

1. **理解**：解释哈希函数如何将 key 映射到下标
2. **冲突处理**：画出链地址法的结构图
3. **基本实现**：实现 put/get/remove
4. **扩容**：实现负载因子检测和自动扩容
5. **字符串哈希**：实现字符串 key 的哈希表
6. **开放寻址**：用线性探测实现简单哈希表

## 参考

- runoob.com/data-structures/hash-table.html
