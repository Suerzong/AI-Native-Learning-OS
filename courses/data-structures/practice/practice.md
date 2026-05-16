练习（按考试格式）
写出顺序表的定义（结构体）和 Insert 函数（在第 i 个位置插入 x）。
#define MAXSIZE 100
typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

int Insert(SqList *sq, int i, int x)
{
    if (i < 1 || i > sq->length + 1 || sq->length == MAXSIZE)
    {
        return -1;
    }

    else
    {
        for (int j = sq->length; j >= i; j--)
        {
           sq->data[j] = sq->data[j-1]; 
        }

        sq->data[i - 1] = x;
        sq->length++;
        return 0;
    }
}
写出双向链表节点定义和 Delete 函数（删除第 i 个节点）。
typedef struct DuLNode {
    ElemType data;
    struct DuLNode *prior;  // 前驱
    struct DuLNode *next;   // 后继
} DuLNode, *DuLinkList;

int Delete(DuLinkList du, int i)
{
    if (i < 1)
    {
        return -1;
    }

    else
    {
        DuLinkList curr = du->next;
        for(int j = 1; j < i; j++)
        {
            if (curr == NULL)
            {
                return -1;
            }
            curr = curr->next;
        }

        curr->prior->next = curr->next;
        if (curr->next != NULL)
        {
            curr->next->prior = curr->prior;
        }
        free(curr);
        return 0;
    }
}


写出链队的初始化、入队、出队（不看上面，独立手写）。

typedef struct QNode
{
    ElemType data;
    struct QNode *next;
} QNode;

typedef struct
{
    QNode *front;
    QNode *rear;
}LinkQueue;

void InitQueue(LinkQueue *q) 
{
    q->front = q->rear = NULL;
}

void EnQueue(LinkQueue *q, ElemType val)
{
    QNode *s = (QNode*)malloc(sizeof(QNode));
    s->data = val;
    s->next = NULL;

    if (q->rear == NULL)      // 空队
    {
        q->front = s;
        q->rear  = s;
    }
    else                      // 非空队
    {
        q->rear->next = s;
        q->rear = s;
    }
}

int DeQueue(LinkQueue *q, int *return_val)
{
    if(q->front == NULL)
    {
        return -1;
    }

    else
    {
        LinkQueue *temp = q;
        *return_val = q->front->data;
        q->front = q->front->next;
        if(q->front == NULL)
        {
            q->rear = NULL;
        }
        free(q);
        return 0;

    }
}