# 容器、算法、迭代器 技能地图

## 目标

学习者能熟练使用 STL 容器和算法，能根据场景选择合适的容器，能用迭代器遍历和操作容器。

## 必会容器

| 容器 | 底层结构 | 特点 | 适用场景 |
|------|---------|------|---------|
| `vector` | 动态数组 | 随机访问 O(1)，尾部插入 O(1)，中间插入 O(n) | 最常用，数据量已知或大致已知 |
| `list` | 双向链表 | 任意位置插入删除 O(1)，不支持随机访问 | 频繁中间插入删除 |
| `deque` | 分段数组 | 两端插入删除 O(1)，随机访问 O(1) | 需要两端操作 |
| `map` | 红黑树 | 有序，查找 O(log n) | 需要有序键值对 |
| `unordered_map` | 哈希表 | 无序，平均查找 O(1) | 高性能键值查找 |
| `set` | 红黑树 | 有序，元素唯一 | 去重、有序集合 |
| `unordered_set` | 哈希表 | 无序，元素唯一 | 快速去重 |

## 必会算法

```cpp
#include <algorithm>
#include <numeric>
#include <vector>

std::vector<int> v = {5, 3, 1, 4, 2};

// sort
std::sort(v.begin(), v.end());                // 升序
std::sort(v.begin(), v.end(), std::greater<int>()); // 降序
std::sort(v.begin(), v.end(), [](int a, int b) {    // Lambda 比较
    return a > b;
});

// find
auto it = std::find(v.begin(), v.end(), 3);
if (it != v.end()) {
    std::cout << "Found: " << *it << std::endl;
}

// find_if
auto it2 = std::find_if(v.begin(), v.end(), [](int x) {
    return x > 3;
});

// count / count_if
int cnt = std::count(v.begin(), v.end(), 3);
int cnt2 = std::count_if(v.begin(), v.end(), [](int x) { return x > 2; });

// for_each
std::for_each(v.begin(), v.end(), [](int& x) { x *= 2; });

// transform
std::vector<int> result(v.size());
std::transform(v.begin(), v.end(), result.begin(), [](int x) { return x * x; });

// accumulate
int sum = std::accumulate(v.begin(), v.end(), 0);

// min_element / max_element
auto min_it = std::min_element(v.begin(), v.end());
auto max_it = std::max_element(v.begin(), v.end());
```

## 必会迭代器

```cpp
// 获取迭代器
auto it = v.begin();   // 指向第一个元素
auto it2 = v.end();    // 指向最后一个元素的下一个位置

// 迭代器操作
*it            // 解引用
++it           // 前进
--it           // 后退（双向迭代器以上）
it1 == it2     // 比较

// 迭代器种类
// 输入迭代器：只能读，只能前进
// 输出迭代器：只能写
// 前进迭代器：可读写，只能前进（forward_list）
// 双向迭代器：可读写，可前进后退（list, map, set）
// 随机访问迭代器：可读写，可跳跃（vector, deque, array）
```

## 常见错误

1. `find` 返回 `end()` 表示没找到（不是 -1 或 null）
2. `sort` 需要随机访问迭代器（`list` 不能用，用 `list::sort()`）
3. `vector::push_back` 可能导致迭代器失效
4. `map` 的 `[]` 运算符会插入不存在的 key
5. 遍历时删除元素要用返回的迭代器

## 训练阶梯

1. **识别**：选择合适的容器存储特定数据
2. **解释**：解释 vector 和 list 的性能差异
3. **修改**：用 sort + Lambda 排序自定义结构体
4. **编写**：用 map 统计单词出现频率
5. **迁移**：用 find_if + transform 实现数据过滤和变换

## 掌握标准

- 能根据场景选择合适的容器
- 能用 sort、find、for_each、transform 完成常见操作
- 能解释迭代器失效问题
- 能用 Lambda 配合 STL 算法

## 参考

- runoob.com/cplusplus/cpp-stl-tutorial.html
