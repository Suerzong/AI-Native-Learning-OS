# 栈与队列 技能地图

## 目标

学习者能用数组和链表两种方式实现栈和队列，能分析各操作的复杂度，能用栈/队列解决经典问题（括号匹配、表达式求值、层序遍历）。

## 必会概念

- 栈（Stack）：LIFO（后进先出），只在一端操作
- 队列（Queue）：FIFO（先进先出），一端入一端出
- 循环队列：用数组+取模实现固定大小队列
- 双端队列（Deque）：两端都可插入和删除
- 单调栈：栈内元素保持单调性

## 栈操作复杂度

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| push | O(1) | 栈顶插入 |
| pop | O(1) | 栈顶删除 |
| top/peek | O(1) | 查看栈顶 |
| isEmpty | O(1) | 判断空 |
| size | O(1) | 若维护了计数器 |

## 队列操作复杂度

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| enqueue（入队） | O(1) | 尾部插入 |
| dequeue（出队） | O(1) | 头部删除 |
| front/peek | O(1) | 查看队首 |
| isEmpty | O(1) | 判断空 |

## 栈的数组实现

```c
#define MAX_SIZE 1000
typedef struct {
    int data[MAX_SIZE];
    int top;  // 栈顶下标，-1 表示空
} Stack;

void push(Stack* s, int val) {
    if (s->top < MAX_SIZE - 1)
        s->data[++(s->top)] = val;
}
int pop(Stack* s) {
    if (s->top >= 0)
        return s->data[(s->top)--];
    return -1; // error
}
```

## 队列的循环数组实现

```c
#define MAX_SIZE 1000
typedef struct {
    int data[MAX_SIZE];
    int front;  // 队首下标
    int rear;   // 队尾下标（下一个入队位置）
    int size;   // 当前元素个数
} Queue;

void enqueue(Queue* q, int val) {
    if (q->size < MAX_SIZE) {
        q->data[q->rear] = val;
        q->rear = (q->rear + 1) % MAX_SIZE;
        q->size++;
    }
}
int dequeue(Queue* q) {
    if (q->size > 0) {
        int val = q->data[q->front];
        q->front = (q->front + 1) % MAX_SIZE;
        q->size--;
        return val;
    }
    return -1; // error
}
```

## 经典应用

| 应用 | 使用结构 | 说明 |
|------|---------|------|
| 括号匹配 | 栈 | 遇左括号入栈，遇右括号匹配栈顶 |
| 表达式求值 | 栈（两个） | 操作数栈 + 运算符栈 |
| 单调栈 | 栈 | 求"下一个更大元素" |
| 层序遍历二叉树 | 队列 | BFS 的核心数据结构 |
| 用栈实现队列 | 两个栈 | 一个入栈一个出栈 |
| 用队列实现栈 | 两个队列 | 入队时翻转顺序 |

## 循环队列的空/满判断

三种常用方法：
1. **浪费一个位置**：`(rear + 1) % capacity == front` 表示满
2. **size 计数器**：`size == capacity` 表示满，`size == 0` 表示空
3. **flag 标记**：区分最后一次操作是入队还是出队

## 常见错误

- 数组栈忘记检查满栈就 push
- 队列出队忘记移动 front 指针
- 循环队列忘记取模
- 循环队列空和满的判断条件混淆
- pop 后忘记释放内存（链表实现）
- 单调栈的应用中，忘记处理相等元素

## 训练阶梯

1. **识别**：理解 LIFO 和 FIFO 的区别
2. **数组栈**：实现 push/pop/top
3. **链表栈**：用链表实现栈
4. **循环队列**：实现 enqueue/dequeue
5. **括号匹配**：用栈判断括号字符串是否有效
6. **两个栈实现队列**：理解两个数据结构的组合
7. **单调栈**：解决"下一个更大元素"问题

## 参考

- runoob.com/data-structures/stack.html
- runoob.com/data-structures/queue.html
