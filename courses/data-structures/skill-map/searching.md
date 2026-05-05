# 查找算法 技能地图

## 目标

学习者能实现线性查找和二分查找（迭代+递归），能处理二分查找的各种变体，能分析查找算法的复杂度。

## 必会概念

- 线性查找（顺序查找）：逐个比较，O(n)
- 二分查找：在有序数组中折半查找，O(log n)
- 查找左边界：第一个 >= target 的位置
- 查找右边界：最后一个 <= target 的位置
- lower_bound / upper_bound

## 复杂度

| 算法 | 最好 | 平均 | 最坏 | 空间 | 前提 |
|------|------|------|------|------|------|
| 线性查找 | O(1) | O(n) | O(n) | O(1) | 无 |
| 二分查找（迭代） | O(1) | O(log n) | O(log n) | O(1) | 有序 |
| 二分查找（递归） | O(1) | O(log n) | O(log n) | O(log n) | 有序 |

## 线性查找

```c
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++)
        if (arr[i] == target)
            return i;
    return -1;
}
```

## 二分查找（标准）

### 迭代实现

```c
int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  // 防溢出
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
```

### 递归实现

```c
int binarySearchRec(int arr[], int left, int right, int target) {
    if (left > right) return -1;
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target)
        return binarySearchRec(arr, mid + 1, right, target);
    return binarySearchRec(arr, left, mid - 1, target);
}
```

## 二分查找变体

### 查找左边界（第一个等于 target 的位置）

```c
int lowerBound(int arr[], int n, int target) {
    int left = 0, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid;  // 注意：不是 mid - 1
    }
    return left;
}
```

### 查找右边界（最后一个等于 target 的位置）

```c
int upperBound(int arr[], int n, int target) {
    int left = 0, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] <= target)
            left = mid + 1;  // 注意：不是 mid
        else
            right = mid;
    }
    return left - 1;
}
```

### 旋转排序数组中搜索

```c
int searchRotated(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[left] <= arr[mid]) {  // 左半有序
            if (arr[left] <= target && target < arr[mid])
                right = mid - 1;
            else
                left = mid + 1;
        } else {  // 右半有序
            if (arr[mid] < target && target <= arr[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    return -1;
}
```

## 边界条件的两种写法

| 写法 | left right 初始 | 循环条件 | mid 更新 | 适用 |
|------|----------------|---------|---------|------|
| 闭区间 | `[0, n-1]` | `left <= right` | `left = mid+1` / `right = mid-1` | 标准查找 |
| 左闭右开 | `[0, n)` | `left < right` | `left = mid+1` / `right = mid` | lower_bound |

## 常见错误

- `mid = (left + right) / 2` 溢出（应用 `left + (right - left) / 2`）
- 循环条件 `left < right` 但更新写成 `right = mid - 1`（丢失中间元素）
- `left <= right` 和 `left < right` 的边界写法混用
- 旋转数组中判断有序半边的条件写错
- lower_bound 返回后没有检查是否真的等于 target

## 训练阶梯

1. **理解**：解释二分查找为什么是 O(log n)
2. **基本实现**：手写标准二分查找
3. **递归实现**：手写递归版二分查找
4. **左边界**：实现 lower_bound
5. **右边界**：实现 upper_bound
6. **旋转数组**：在旋转排序数组中搜索
7. **应用**：用二分查找求平方根（浮点二分）

## 参考

- runoob.com/data-structures/binary-search.html
