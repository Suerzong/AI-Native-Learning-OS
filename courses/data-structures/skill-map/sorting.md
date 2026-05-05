# 排序算法 技能地图

## 目标

学习者能手写 6 种常用排序算法，能分析各自的时间/空间复杂度和稳定性，能根据场景选择合适的排序算法。

## 必会概念

- 内排序 vs 外排序
- 稳定排序：相等元素排序后相对位置不变
- 原地排序：不需要额外 O(n) 空间
- 分治：将问题分解为子问题

## 复杂度与稳定性总览

| 算法 | 平均 | 最好 | 最坏 | 空间 | 稳定 |
|------|------|------|------|------|:----:|
| 冒泡排序 | O(n^2) | O(n) | O(n^2) | O(1) | 是 |
| 选择排序 | O(n^2) | O(n^2) | O(n^2) | O(1) | 否 |
| 插入排序 | O(n^2) | O(n) | O(n^2) | O(1) | 是 |
| 快速排序 | O(n log n) | O(n log n) | O(n^2) | O(log n) | 否 |
| 归并排序 | O(n log n) | O(n log n) | O(n log n) | O(n) | 是 |
| 堆排序 | O(n log n) | O(n log n) | O(n log n) | O(1) | 否 |

## 基础排序

### 冒泡排序

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;  // 优化：提前终止
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = 1;
            }
        }
        if (!swapped) break;  // 没有交换说明已有序
    }
}
```

### 选择排序

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx])
                minIdx = j;
        swap(&arr[i], &arr[minIdx]);
    }
}
```

### 插入排序

```c
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];  // 后移
            j--;
        }
        arr[j + 1] = key;  // 插入
    }
}
```

## 高级排序

### 快速排序

```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // 选最右为 pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

最坏情况：已有序数组 + 固定选最右元素为 pivot。优化：随机化 pivot 或三数取中。

### 归并排序

```c
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1, n2 = right - mid;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

## 算法选型指南

| 场景 | 推荐算法 | 原因 |
|------|---------|------|
| 小数据量（n < 20） | 插入排序 | 常数小，对近乎有序数据快 |
| 需要稳定排序 | 归并排序 | O(n log n) 且稳定 |
| 内存受限 | 堆排序 | 原地排序，O(1) 空间 |
| 平均性能最优 | 快速排序 | 常数因子最小 |
| 近乎有序的数据 | 插入排序 / 冒泡排序 | 最好情况 O(n) |

## 常见错误

- 快排分区时 i 和 j 的移动方向
- 快排递归终止条件写错（low < high 还是 low <= high）
- 归并排序合并时忘记处理剩余元素
- 选择排序误认为不稳定（其实"不"稳定）
- 冒泡排序内外循环边界

## 训练阶梯

1. **理解**：解释每种排序的核心思想
2. **冒泡排序**：手写并加优化（提前终止）
3. **选择排序**：手写
4. **插入排序**：手写
5. **快速排序**：手写 partition 和 quickSort
6. **归并排序**：手写 merge 和 mergeSort
7. **对比**：填写复杂度和稳定性对比表
8. **选型**：为 3 个不同场景选择排序算法并说明理由

## 参考

- runoob.com/data-structures/sorting-algorithms.html
