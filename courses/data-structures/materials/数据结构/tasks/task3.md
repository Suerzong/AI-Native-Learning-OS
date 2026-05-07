1-1
分数 1
作者 李祥
单位 湖北经济学院
队列是先进先出的线性表。

T
F

1-2
分数 1
作者 朱晓龙
单位 西安邮电大学
链栈和顺序栈相比，比较明显的优点是通常不会出现栈满的情况。 

T
F

1-3
分数 1
作者 朱晓龙
单位 西安邮电大学
链栈的插入在栈顶，删除在栈底。  

T
F

1-4
分数 1
作者 陈越
单位 浙江大学
堆栈适合解决处理顺序与输入顺序相反的问题。

T
F

1-5
分数 1
作者 DS课程组
单位 浙江大学
所谓“循环队列”是指用单向循环链表或者循环数组表示的队列。

T
F

1-6
分数 1
作者 DS课程组
单位 浙江大学
在用数组表示的循环队列中，front值一定小于等于rear值。

T
F

1-7
分数 1
作者 anrorvv
单位 集美大学诚毅学院
循环队列也存在空间溢出的问题。

T
F

1-8
分数 1
作者 李廷元
单位 中国民用航空飞行学院
栈和队列的存储方式，既可以是顺序方式，也可以是链式方式。  

T
F

1-9
分数 1
作者 ZXM
单位 西南石油大学
序列{1,2,3,4,5}依次入栈，则不可能得到{3,4,1,2,5}的出栈序列。   

T
F

1-10
分数 1
作者 鲁法明
单位 山东科技大学
采用顺序存储结构的循环队列，出队操作会引起其余元素的移动。  

T
F

2-1
分数 2
作者 DS课程组
单位 浙江大学
线性表、堆栈、队列的主要区别是什么？


A.
线性表用指针，堆栈和队列用数组


B.
堆栈和队列都是插入、删除受到约束的线性表


C.
线性表和队列都可以用循环链表实现，但堆栈不能


D.
堆栈和队列都不是线性结构，而线性表是


2-2
分数 2
作者 DS课程组
单位 西南石油大学
循环队列的引入，目的是为了克服(  )。   


A.
假溢出问题


B.
真溢出问题


C.
空间不够用


D.
操作不方便


2-3
分数 2
作者 赵玉霞
单位 山东航空学院
栈在 （   ）中有所应用。


A.
递归调用


B.
函数调用


C.
表达式求值


D.
前三个选项都有


2-4
分数 2
作者 陈越
单位 浙江大学
检查表达式中的括号是否匹配的问题需要借助________来解决。


A.
队列


B.
堆栈


C.
二叉搜索树


D.
有向无环图


2-5
分数 2
作者 DS课程组
单位 浙江大学
为解决计算机主机与打印机之间速度不匹配问题，通常设置一个打印数据缓冲区，主机将要输出的数据依次写入该缓冲区，而打印机则依次从该缓冲区中取出数据。该缓冲区的逻辑结构应该是？


A.
堆栈


B.
队列


C.
树


D.
图


2-6
分数 2
作者 DS课程组
单位 浙江大学
设栈S和队列Q的初始状态均为空，元素a、b、c、d、e、f、g依次进入栈S。若每个元素出栈后立即进入队列Q，且7个元素出队的顺序是b、d、c、f、e、a、g，则栈S的容量至少是：


A.
1


B.
2


C.
3


D.
4


2-7
分数 2
作者 DS课程组
单位 浙江大学
假设有5个整数以1、2、3、4、5的顺序被压入堆栈，且出栈顺序为3、5、4、2、1，那么为了获得这样的输出，堆栈大小至少为：


A.
2


B.
3


C.
4


D.
5


2-8
分数 2
作者 DS课程组
单位 浙江大学
从栈顶指针为ST的链栈中删除一个结点且用X保存被删结点的值，则执行：


A.
X= ST->data;


B.
X= ST; ST = ST->next;


C.
X= ST->data; ST = ST->next;


D.
ST = ST->next; X= ST->data;


2-9
分数 2
作者 DS课程组
单位 浙江大学
若栈采用顺序存储方式存储，现两栈共享空间V[m]：top[i]代表第i（i=1或2）个栈的栈顶；栈1的底在V[0]，栈2的底在V[m-1]，则栈满的条件是：


A.
|top[2]-top[1]|==0


B.
top[1]+top[2]==m


C.
top[1]==top[2]


D.
top[1]+1==top[2]


2-10
分数 2
作者 DS课程组
单位 浙江大学
若已知一队列用单向链表表示，该单向链表的当前状态（含3个对象）是：1->2->3，其中x->y表示x的下一节点是y。此时，如果将对象4入队，然后队列头的对象出队，则单向链表的状态是：


A.
1->2->3


B.
2->3->4


C.
4->1->2


D.
答案不唯一


2-11
分数 2
作者 DS课程组
单位 浙江大学
若用大小为6的数组来实现循环队列，且当前front和rear的值分别为0和4。当从队列中删除两个元素，再加入两个元素后，front和rear的值分别为多少？


A.
2和0


B.
2和2


C.
2和4


D.
2和6


2-12
分数 2
作者 DS课程组
单位 浙江大学
如果循环队列用大小为m的数组表示，且用队头指针front和队列元素个数size代替一般循环队列中的front和rear指针来表示队列的范围，那么这样的循环队列可以容纳的元素个数最多为：


A.
m-1


B.
m


C.
m+1


D.
不能确定


2-13
分数 2
作者 严冰
单位 浙大城市学院
循环顺序队列中是否可以插入下一个元素（）。


A.
与队头指针和队尾指针的值有关


B.
只与队尾指针的值有关，与队头指针的值无关


C.
只与数组大小有关，与队首指针和队尾指针的值无关


D.
与曾经进行过多少次插入操作有关


2-14
分数 2
作者 严冰
单位 浙江大学
最不适合用作链队的链表是（）。


A.
只带队头指针的非循环双链表


B.
只带队头指针的循环双链表


C.
只带队尾指针的循环双链表


D.
只带队尾指针的循环单链表



6-1 递归计算Ackermenn函数
分数 15

全屏浏览

切换布局
作者 C课程组
单位 浙江大学
本题要求实现Ackermenn函数的计算，其函数定义如下：



函数接口定义：
[ C++ ]

复制内容

格式

全屏
1
int Ack( int m, int n );
其中m和n是用户传入的非负整数。函数Ack返回Ackermenn函数的相应值。题目保证输入输出都在长整型

范围内。

裁判测试程序样例：
[ C++ ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
▾
#include <stdio.h>

int Ack( int m, int n );

int main()
{
    int m, n;
    
    scanf("%d %d", &m, &n);
    printf("%d\n", Ack(m, n));
    
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
[ in ]

复制内容

格式

全屏
1
2 3
输出样例：
[ out ]

复制内容

格式

全屏
1
9
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB


6-2 仅有头指针的队列
分数 18

全屏浏览

切换布局
作者 陈越
单位 浙江大学
如果用一个循环数组表示队列，且只有一个队列头指针 front，不设队列尾指针 rear，而设置计数器 count 用以记录队列中结点的个数。请编写算法实现队列的三个基本运算：判空、入队、出队。

函数接口定义：
[ C++ ]

复制内容

格式

全屏

收起
1
2
3
bool IsEmpty(Queue queue);
void EnQueue(Queue queue, QElemSet x);
void DeQueue(Queue queue);
其中顺序队列 Queue 的定义如下：

[ C++ ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
8
▾
typedef int Position; /* 整型下标，表示元素的位置 */
typedef struct QueueNode *Queue;
struct QueueNode {
    int capacity;     /* 顺序队列的容量 */
    Position front;   /* 顺序队列的队首指针，初始化为0 */
    int count;        /* 顺序队队列中结点的个数，初始化为0 */
    QElemSet *data;   /* 存储数据的数组 */
};
函数接口定义中，QElemSet 是用户定义的数据类型，例如 int、double 或者 char 等。函数 IsEmpty 的功能是判断 queue 是否为空队，若是则返回 true，否则返回 false；函数 EnQueue 将元素 x 插入队尾；函数 DeQueue 将队首元素删除。
当调用 EnQueue 但队列已满，或调用 DeQueue 但队列为空时，应该在一行中输出错误信息 ERROR。

裁判测试程序样例：
[ C++ ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
▾
▾
▾
▾
▾
▾
#include <stdio.h>
#include <stdlib.h>

typedef enum {false, true} bool;
typedef int QElemSet;
#define NIL -1
typedef int Position; /* 整型下标，表示元素的位置 */
typedef struct QueueNode *Queue;
struct QueueNode {
    int capacity;     /* 顺序队列的容量 */
    Position front;   /* 顺序队列的队首指针，初始化为0 */
    int count;        /* 顺序队队列中结点的个数，初始化为0 */
    QElemSet *data;   /* 存储数据的数组 */
};
/* 裁判实现的函数，实现细节省略 */
void InitQueue(Queue queue, int kSize); /* 初始化一个大小为kSize的顺序队列 */
bool IsFull(Queue queue);               /* 判断队列是否已满 */
QElemSet GetFront(Queue queue);         /* 取队首元素 */
void DestroyQueue(Queue queue);         /* 销毁队列 */
/* 裁判实现的函数 结束 */

bool IsEmpty(Queue queue);
void EnQueue(Queue queue, QElemSet x);
void DeQueue(Queue queue);

int main(void)
{
    int i, n, x;
    char cmd;
    Queue queue;
    
    queue = (Queue)malloc(sizeof(struct QueueNode));
    scanf("%d\n", &n);
    InitQueue(queue, n);
    scanf("%c ", &cmd);
    while (cmd != 'E') {
        if (cmd == 'I') {
            scanf("%d\n", &x);
            EnQueue(queue, x);
        }
        else {
            x = GetFront(queue);
            if (x != NIL)
                printf("%d\n", x);
            DeQueue(queue);    
        }
        scanf("%c ", &cmd);
    }
    DestroyQueue(queue);
    
    return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
[ in ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
8
9
10
11
12
3
I 1
I 2
I 3
I 4
O
I 5
O
O
O
O
E
输出样例：
[ out ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
ERROR
1
2
3
5
ERROR
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB
6-3 在一个数组中实现两个栈
分数 19

全屏浏览

切换布局
作者 陈越
单位 浙江大学
试在一个长度为 n 的数组中实现两个栈，使得二者在元素的总数目为 n 之前都不溢出，并保证 Push 和 TopPop 操作的时间代价为 O(1)。

函数接口定义：
[ C++ ]

复制内容

格式

全屏

收起
1
2
3
4
void InitStack(Stack stack, int n);
bool Push (Stack stack, int tag, SElemSet x);
bool IsEmpty(Stack stack, int tag);
SElemSet TopPop (Stack stack, int tag);
其中 Stack 数据类型的定义如下：

[ C++ ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
▾
typedef int Position;    /* 整型下标，表示元素的位置 */
typedef struct StackNode *Stack;
struct StackNode {
    int capacity;        /* 两个顺序栈的总容量 */
    Position top1, top2; /* 两个顺序栈的栈顶指针 */
    SElemSet *data;      /* 存储数据的数组 */
};
函数接口定义中，SElemSet 是用户定义的数据类型，例如 int、double 或者 char 等；n 是数组的长度，也就是两个栈的总容量；tag 是栈的编号，为 1 时表示对 top1 所指的栈顶进行操作，为 2 时表示对 top2 所指的栈顶进行操作。

InitStack 需要将 stack 进行初始化，即将 n 赋值给 capacity，为 n 个元素声明数组空间，并且定义两个栈顶指针的初值。

Push 函数将 x 插入第 tag 个栈。注意：如果栈已满，Push 函数必须输出 Stack Full 并且返回 false。成功插入则返回 true。

IsEmpty 函数判断第 tag 个栈是否为空，空则返回 true，否则返回 false。

TopPop 函数是标准栈函数 Top 和 Pop 的组合，需要将第 tag 个栈的栈顶元素从该栈中移除，并返回其值。如果第 tag 个栈是空的，则 Pop 函数必须返回 ERROR。

裁判测试程序样例：
[ C++ ]

复制内容

格式

全屏

收起
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
▾
▾
▾
▾
▾
▾
▾
▾
▾
#include <stdio.h>
{ /* 判断输入的操作类型 */
    char op[5]; /* 操作最长4个字符 */
    Operation ret; 
    
    scanf(" %s ", op);
    switch (op[1]) { /* 用第2个字母区分操作 */
        case 'u': ret = push; break;
        case 'o': ret = pop; break;
        case 'n': ret = end; break;
        default: break;
    }
    return ret;
}

void PrintStack (Stack stack, int tag)
{
    printf("Pop from Stack %d:", tag);
    while (!IsEmpty(stack, tag)) {
        printf(" %d", TopPop(stack, tag));
    }
    printf("\n");
}

int main(void)
{
    int n, tag, x;
    Stack stack;
    bool done;
    stack = (Stack)malloc(sizeof(struct StackNode));
    scanf("%d", &n);
    InitStack(stack, n); /* 初始化栈空间 */
    done = false; /* 初始化结束标识 */
    while ( done == false ) {
        switch( GetOp() ) {
            case push: /* 执行入栈操作 */
                scanf("%d %d\n", &tag, &x);
                if (Push(stack, tag, x) == false) {
                    printf("%d is not in Stack %d\n", x, tag);
                }
                break;
            case pop: /* 执行出栈操作 */
                scanf("%d\n", &tag);
                x = TopPop(stack, tag);
                if (x == ERROR) {
                    printf("Stack %d is Empty\n", tag);
                }
                break;
            case end: /* 输入结束，打印栈元素 */
                PrintStack(stack, 1);
                PrintStack(stack, 2);
                done = true;
                break;
            default: break;
        }
    }
    return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
[ in ]

复制内容

格式

全屏

收起
1
2
3
4
5
6
7
8
9
10
11
12
5
Push 1 1
Pop 2
Push 2 11
Push 1 2
Push 2 12
Pop 1
Push 2 13
Push 2 14
Push 1 3
Pop 2
End
输出样例：
[ out ]

复制内容

格式

全屏

收起
1
2
3
4
5
Stack 2 is Empty
Stack Full
3 is not in Stack 1
Pop from Stack 1: 1
Pop from Stack 2: 13 12 11
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB

8-1 简述以下三个算法的功能
分数 10

全屏浏览
作者 wzl
单位 北京邮电大学
分别说明以下三个算法的功能

Status a1go1(Stack S){

 int i,n, A[255];

 n=0;

 while(!StackEmpty(S)){n++; Pop(S, A[n]);};

 for(i=1; i<=n; i++) Push(S,A[i]);

}

Status algo2(Stack S, int e){

 Stack T; int d;

 InitStack(T);

 while(!StackEmpty(S)){

 Pop(S,d);

 if(d!=e) Push(T,d);

 }

 while(!StackEmpty(T)){

 Pop(T, d);

 Push(S,d);

 }

}

void algo3(Queue &Q){

 Stack S; int d;

 InitStack(S);

 while(!QeueuEmpty(Q)){

 DeQueue(Q,d);

 Push(S,d);

 }

 while(!StackEmpty(S)){

 Pop(S,d);

 EnQueue(Q,d);

 }

}
