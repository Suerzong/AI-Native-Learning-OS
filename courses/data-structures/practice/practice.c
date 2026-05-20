题 1：写出链队列 DeQueue 的完整代码。函数签名：


int DeQueue(LinkQueue *q, int *x)
{
    if(q->front == q->rear)
    {
        return 0;
    }

    else
    {
        QNode *p = q->front;
        *x = q->front->data
    }
}
// 成功返回 1，队空返回 0
题 2：如果第 1 题写对了，再写链队列 EnQueue 的完整代码：


int EnQueue(LinkQueue *q, int x);
两个操作写完后，用文字解释：EnQueue 和 DeQueue 分别操作的是 front 还是 rear？为什么一个要 malloc，一个要 free？