#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);

    /* 构建链表（尾插法） */
    Node *head = NULL, *tail = NULL;
    for (int i = 0; i < m; i++) {
        int val;
        scanf("%d", &val);
        Node *newNode = (Node *)malloc(sizeof(Node));
        newNode->data = val;
        newNode->next = NULL;
        if (head == NULL) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    /* 快慢指针找倒数第 n 个 */
    Node *fast = head, *slow = head;
    for (int i = 0; i < n; i++) {
        fast = fast->next;
    }
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    /* 从 slow 开始乘 n 个 */
    int product = 1;
    Node *p = slow;
    while (p != NULL) {
        product *= p->data;
        p = p->next;
    }

    printf("%d\n", product);
    return 0;
}
