# 堆与优先队列 技能地图

## 目标

学习者理解堆的性质和数组存储方式，能实现最大堆/最小堆的插入和删除，能用堆实现优先队列和堆排序。

## 必会概念

- 堆：完全二叉树 + 堆序性质
- 最大堆：父节点 >= 子节点
- 最小堆：父节点 <= 子节点
- 数组存储：下标 i 的父节点是 (i-1)/2，左子是 2*i+1，右子是 2*i+2
- 上浮（sift up / bubble up）：插入后向上调整
- 下沉（sift down / heapify）：删除堆顶后向下调整
- 建堆（heapify）：从最后一个非叶节点开始，逐个下沉

## 操作复杂度

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 插入 | O(log n) | 上浮操作，最多到根 |
| 删除堆顶 | O(log n) | 下沉操作，最多到叶 |
| 查看堆顶 | O(1) | 直接访问 arr[0] |
| 建堆（自底向上） | O(n) | 不是 O(n log n) |
| 堆排序 | O(n log n) | 建堆 O(n) + n 次删除 O(log n) |

## 数组存储映射

```
完全二叉树：        数组存储：
      0              [0] = 10
     / \             [1] = 8,  [2] = 7
    8   7            [3] = 5,  [4] = 6, [5] = 3, [6] = 4
   / \ / \
  5  6 3  4

父节点：parent(i) = (i - 1) / 2
左子节点：left(i) = 2 * i + 1
右子节点：right(i) = 2 * i + 2
```

## 核心操作实现

### 上浮（插入时）

```c
void siftUp(int arr[], int i) {
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (arr[i] <= arr[parent]) break;  // 最大堆
        swap(&arr[i], &arr[parent]);
        i = parent;
    }
}
```

### 下沉（删除堆顶时）

```c
void siftDown(int arr[], int n, int i) {
    while (2 * i + 1 < n) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < n && arr[left] > arr[largest])
            largest = left;
        if (right < n && arr[right] > arr[largest])
            largest = right;
        if (largest == i) break;
        swap(&arr[i], &arr[largest]);
        i = largest;
    }
}
```

### 建堆

```c
void buildHeap(int arr[], int n) {
    // 从最后一个非叶节点开始下沉
    for (int i = n / 2 - 1; i >= 0; i--)
        siftDown(arr, n, i);
}
```

为什么建堆是 O(n)：叶节点不需要下沉，第 k 层有 n/2^k 个节点，每层下沉最多 k 次，总操作次数 < n。

## 堆排序

```c
void heapSort(int arr[], int n) {
    buildHeap(arr, n);           // O(n)
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);  // 最大值放到末尾
        siftDown(arr, i, 0);     // 对剩余部分重新堆化
    }
}
```

## 优先队列

| 操作 | 最大堆实现 |
|------|-----------|
| push(val) | 插入数组末尾 + siftUp |
| pop() | 返回 arr[0]，用 arr[n-1] 替换 arr[0]，siftDown |
| top() | 返回 arr[0] |
| isEmpty() | return n == 0 |

## 常见错误

- 下标从 0 开始还是 1 开始搞混（父子公式不同）
- siftDown 的终止条件写错（应该检查子节点是否存在）
- 建堆误认为 O(n log n)
- 堆排序后忘记数组已变为升序（最大堆排序后是升序）
- 优先队列 pop 空堆时没有检查

## 嵌入式场景考量

- 堆用数组存储，对缓存友好
- 优先队列是任务调度的核心数据结构
- 固定大小的堆在嵌入式中很实用（不需要动态分配）

## 训练阶梯

1. **画图**：画出一个最大堆，标注每个节点的下标
2. **上浮**：在已有堆中插入新元素
3. **下沉**：删除堆顶并重新调整
4. **建堆**：从无序数组构建最大堆
5. **堆排序**：实现完整的堆排序
6. **优先队列**：实现优先队列的 push/pop/top
7. **应用**：用优先队列找数组中第 K 大元素

## 参考

- runoob.com/data-structures/heap.html
