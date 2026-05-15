Mistakes 复测：3 道快速题
从 mistakes.md 中挑 3 个未复测通过且最容易在考试翻车的：

M1：countValue — 节点 vs 节点值


// 统计链表中值为 target 的节点个数
int countValue(ListNode* head, int target) {
    int count = 0;
    ListNode* curr = head;
    while (curr != NULL) {
        if (curr == target) count++;   // ← 这行哪里错了？
        curr = curr->next;
    }
    return count;
}

错误点：curr->val
M2：循环队列空满判断

循环队列用数组实现，front 指向队头，rear 指向队尾的下一个位置。只说一种方法：怎么区分队空和队满？
队空：front == rear
队满：（rear + 1）% maxsize == front

M3：链表插入 — 顺序

在 p 节点后面插入新节点 s，下面哪个顺序正确？

A. s->next = p->next; p->next = s;
B. p->next = s; s->next = p->next;

A
三道题发上来。