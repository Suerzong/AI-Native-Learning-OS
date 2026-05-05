# 链表 技能地图

## 目标

学习者能用 C/C++ 实现单链表、双向链表和循环链表的全部核心操作（增删查改），能画出内存状态图，能分析每个操作的复杂度。

## 必会概念

- 节点（Node）：数据 + 指针的结构体
- 头指针（head）：指向第一个节点的指针
- 哨兵节点 / 哑节点（dummy head）：简化边界处理
- 空链表：head == NULL
- 指针操作顺序：先接后断

## 操作复杂度（单链表）

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 头部插入 | O(1) | 直接修改 head |
| 尾部插入 | O(n) | 需要遍历到尾部（有尾指针则 O(1)） |
| 已知节点后插入 | O(1) | 直接修改指针 |
| 头部删除 | O(1) | 直接修改 head |
| 尾部删除 | O(n) | 需要找到倒数第二个节点 |
| 按值查找 | O(n) | 需要遍历 |
| 按索引访问 | O(n) | 需要遍历计数 |

## C 语言节点定义

```c
// 单链表节点
typedef struct Node {
    int val;
    struct Node* next;
} Node;

// 双向链表节点
typedef struct DNode {
    int val;
    struct DNode* prev;
    struct DNode* next;
} DNode;
```

## 必会操作（单链表）

### 头插法
```c
void insertAtHead(Node** head, int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    newNode->next = *head;
    *head = newNode;
}
```

### 尾插法
```c
void insertAtTail(Node** head, int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    newNode->next = NULL;
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node* curr = *head;
    while (curr->next != NULL)
        curr = curr->next;
    curr->next = newNode;
}
```

### 反转链表（迭代）
```c
Node* reverse(Node* head) {
    Node *prev = NULL, *curr = head, *next;
    while (curr != NULL) {
        next = curr->next;   // 保存后继
        curr->next = prev;   // 反转指针
        prev = curr;         // prev 前进
        curr = next;         // curr 前进
    }
    return prev;
}
```

## 必会操作（双向链表）

关键差异：需要同时维护 prev 和 next 两个指针。

### 插入（在给定节点后）
```c
void insertAfter(DNode* node, int val) {
    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    newNode->val = val;
    newNode->prev = node;
    newNode->next = node->next;
    if (node->next != NULL)
        node->next->prev = newNode;
    node->next = newNode;
}
```

### 删除（删除给定节点）
```c
void deleteNode(DNode** head, DNode* node) {
    if (node->prev != NULL)
        node->prev->next = node->next;
    else
        *head = node->next;  // 删除的是头节点
    if (node->next != NULL)
        node->next->prev = node->prev;
    free(node);
}
```

## 循环链表

- 尾节点的 next 指向 head（单循环）或 head 的 prev 指向尾节点（双循环）
- 遍历终止条件：`curr != head`（而不是 `curr != NULL`）
- 应用场景：约瑟夫环、轮转调度

## 常见错误

1. **断链**：插入/删除时指针赋值顺序错误
2. **空指针解引用**：没有检查 `curr->next != NULL` 就访问
3. **内存泄漏**：删除节点后忘记 free
4. **双重指针**：函数参数用 `Node*` 而不是 `Node**`，导致修改不生效
5. **循环链表死循环**：终止条件写错

## 训练阶梯

1. **画图**：画出 1->2->3 的内存布局
2. **头插法**：实现头部插入并遍历打印
3. **尾插法**：实现尾部插入
4. **按值删除**：删除第一个值为 val 的节点
5. **反转**：迭代法反转单链表
6. **快慢指针**：判断链表是否有环
7. **双链表**：实现双向链表的插入和删除
8. **循环链表**：实现约瑟夫环问题

## 参考

- runoob.com/data-structures/linked-list.html
