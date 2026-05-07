1-1
分数 1
入门
作者 干红华
单位 浙江大学
将长度分别为m,n的两个单链表合并为一个单链表的时间复杂度为O(m+n)。 

T
F
评测结果
答案错误
得分
0 分

1-2
分数 1
入门
作者 李廷元
单位 中国民用航空飞行学院
线性表采用链式存储表示时，所有结点之间的存储单元地址可以连续也可以不连续。  

T
F
评测结果
答案正确
得分
1 分

1-3
分数 1
入门
作者 李廷元
单位 中国民用航空飞行学院
在单链表中，要访问某个结点，只要知道该结点的指针即可。因此，单链表是一种随机存取结构。   

T
F
评测结果
答案正确
得分
1 分

1-4
分数 1
入门
作者 李廷元
单位 中国民用航空飞行学院
在具有头结点的链式存储结构中，头指针指向链表中的第一个元素结点。     

T
F
评测结果
答案正确
得分
1 分

1-5
分数 1
入门
作者 李廷元
单位 中国民用航空飞行学院
带头结点的单循环链表中，任一结点的后继结点的指针域均不空。 

T
F
评测结果
答案正确
得分
1 分

1-6
分数 1
入门
作者 杨
单位 浙大城市学院
循环链表可以做到从任一结点出发，访问到链表的全部结点。  

T
F
评测结果
答案正确
得分
1 分

1-7
分数 1
简单
作者 ZXM
单位 西南石油大学
在N个结点的顺序表中访问第i（1<=i<=N）个结点和求第i（2<=i<=N）个结点直接前驱的算法时间复杂度均为O(1)。

T
F
评测结果
答案正确
得分
1 分

1-8
分数 1
入门
作者 YJ
单位 西南石油大学
线性表存储于A[1..50]中，删除第30个元素，需要移动20个元素。（   ）

T
F
评测结果
答案正确
得分
1 分

1-9
分数 1
入门
作者 DS课程组
单位 浙江大学
对于顺序存储的长度为N的线性表，访问结点和增加结点的时间复杂度分别对应为O(1)和O(N)。

T
F
评测结果
答案正确
得分
1 分

2-1
分数 2
入门
作者 DS课程组
单位 浙江大学
对于顺序存储的长度为N的线性表，访问结点和增加结点的时间复杂度为：


A.
O(1), O(1)


B.
O(1), O(N)


C.
O(N), O(1)


D.
O(N), O(N)

评测结果
答案正确
得分
2 分

2-2
分数 2
简单
作者 DS课程组
单位 浙江大学
若某线性表最常用的操作是存取任一指定序号的元素和在最后进行插入和删除运算，则利用哪种存储方式最节省时间？


A.
双链表


B.
单循环链表


C.
带头结点的双循环链表


D.
顺序表

评测结果
答案正确
得分
2 分

2-3
分数 2
简单
作者 周治国
单位 东北师范大学
顺序表中第一个元素的存储地址是100，每个元素的长度为2，则第5个元素的地址是（    ）。


A.
100


B.
105


C.
108


D.
110

评测结果
答案正确
得分
2 分

2-4
分数 2
入门
作者 考研真题
单位 浙江大学
下列对顺序存储的有序表（长度为 n）实现给定操作的算法中，平均时间复杂度为 O(1) 的是：


A.
查找包含指定值元素的算法


B.
插入包含指定值元素的算法


C.
删除第 i（1≤i≤n）个元素的算法


D.
获取第 i（1≤i≤n）个元素的算法

评测结果
答案正确
得分
2 分

2-5
分数 2
简单
作者 DS课程组
单位 浙江大学
若某表最常用的操作是在最后一个结点之后插入一个结点或删除最后一个结点。则采用哪种存储方式最节省运算时间？


A.
单链表


B.
双链表


C.
单循环链表


D.
带头结点的双循环链表

评测结果
答案正确
得分
2 分

2-6
分数 2
简单
作者 DS课程组
单位 浙江大学
将线性表La和Lb头尾连接，要求时间复杂度为O(1)，且占用辅助空间尽量小。应该使用哪种结构？


A.
单链表


B.
单循环链表


C.
带尾指针的单循环链表


D.
带头结点的双循环链表

评测结果
答案正确
得分
2 分

2-7
分数 2
简单
作者 DS课程组
单位 浙江大学
带头结点的单链表h为空的判定条件是：


A.
h == NULL;


B.
h->next == NULL;


C.
h->next == h;


D.
h != NULL;

评测结果
答案正确
得分
2 分

2-8
分数 2
简单
作者 DS课程组
单位 浙江大学
对于一非空的循环单链表，h和p分别指向链表的头、尾结点，则有：


A.
p->next == h


B.
p->next == NULL


C.
p == NULL


D.
p == h

评测结果
答案正确
得分
2 分

2-9
分数 2
中等
作者 DS课程组
单位 浙江大学
在双向循环链表结点p之后插入s的语句是：


A.
p->next=s; s->prior=p; p->next->prior=s ; s->next=p->next;


B.
p->next->prior=s; p->next=s; s->prior=p; s->next=p->next;


C.
s->prior=p; s->next=p->next; p->next=s; p->next->prior=s;


D.
s->prior=p; s->next=p->next; p->next->prior=s; p->next=s;

评测结果
答案正确
得分
2 分

2-10
分数 2
中等
作者 DS课程组
单位 浙江大学
在双向链表存储结构中，删除p所指的结点，相应语句为：


A.
p->prior=p->prior->prior; p->prior->next=p;


B.
p->next->prior=p; p->next=p->next->next;


C.
p->prior->next=p->next; p->next->prior=p->prior;


D.
p->next=p->prior->prior; p->prior=p->next->next;

评测结果
答案正确
得分
2 分

2-11
分数 2
简单
作者 DS课程组
单位 浙江大学
将两个结点数都为N且都从小到大有序的单向链表合并成一个从小到大有序的单向链表，那么可能的最少比较次数是：


A.
1


B.
N


C.
2N


D.
NlogN

评测结果
答案正确
得分
2 分

2-12
分数 2
简单
作者 DS课程组
单位 浙江大学
已知表头元素为c的单链表在内存中的存储状态如下表所示：



现将f存放于1014H处，并插入到单链表中，若f在逻辑上位于a和e之间，则a、e、f的“链接地址”依次

是：


A.
1010H, 1014H, 1004H


B.
1010H, 1004H, 1014H


C.
1014H, 1010H, 1004H


D.
1014H, 1004H, 1010H

评测结果
答案错误
得分
0 分

2-13
分数 2
简单
作者 考研真题
单位 浙江大学
现有非空双向链表 L，其结点结构为：
fig2.jpg，prev 是指向直接前驱结点的指针，next 是指向直接后继结点的指针。若要在 L 中指针 p 所指向的结点（非尾结点）之后插入指针 s 指向的新结点，则在执行了语句序列 s->next = p->next; p->next = s; 后，下列语句序列中还需要执行的是：


A.
s->next->prev = p; s->prev = p;


B.
p->next->prev = s; s->prev = p;


C.
s->prev = s->next->prev; s->next->prev = s;


D.
p->next->prev = s->prev; s->next->prev = p;

评测结果
答案正确
得分
2 分

2-14
分数 2
中等
作者 严冰
单位 浙大城市学院
已知线性表中的元素以值递增有序排列，阅读下列程序，该算法的功能是（）。


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
typedef struct node{
ElemType data;
struct node *next;
}LNode;
void fun4(LNode *h, ElemType min, ElemType max) {
LNode *p=h, *q=NULL;
   while (p!=NULL && p->data<=min ) {
       q=p;  p=p->next;
   }
   while (p!=NULL && p->data<max ) {
       if (p==h) {
           h=p->next;  delete p;  p=h;
 　 }
       else {
           q->next=p->next;  delete p;  p=q->next;
}
   }
}


A.
删除单链表中所有值小于min或大于max的元素


B.
将单链表中值大于min的元素删除


C.
将单链表中值小于max的元素删除


D.
删除单链表中所有值大于min且小于max的元素

评测结果
答案正确
得分
2 分

2-15
分数 2
中等
作者 严冰
单位 浙大城市学院
已知指针ha和hb分别是两个单链表的头指针，下列算法将这两个链表首尾相连在一起，并形成一个循环链表（即ha的最后一个结点链接hb的第一个结点，hb的最后一个结点指向ha），返回ha作为该循环链表的头指针。请将该算法补充完整。


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
typedef struct node{
ElemType data;
    struct node *next;
}LNode;
LNode *merge(LNode *ha, LNode *hb) {
LNode *p=ha;
     if (ha==NULL || hb==NULL) {
cout<<”one or two link lists are empty!”<<endl;
          return NULL;
     }
     while ( p->next!=NULL )
           p=p->next;
     p->next=hb;
     while ( p->next!=NULL )
           p=p->next;
           __________
}


A.
ha=p->next; return ha;


B.
p->next=ha; return ha;


C.
ha=p->next; return p;


D.
p->next=ha; return p;

评测结果
答案正确
得分
2 分

2-16
分数 2
中等
作者 严冰
单位 浙大城市学院
已知单链表中的元素以值递增有序排列，下列算法删除单链表中所有值相同的元素，同时释放被删结点空间。请将该算法补充完整。


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
typedef struct node{
ElemType data;
    struct node *next;
}LNode;
void delete_equal(LNode *h){
LNode *p=h, *q;
     if (h==NULL)  return;
    while (p->next!=NULL) {
        q=p->next;
        if (p->data!=q->data)
             p=q;
        else  //相邻两元素值相等，则循环删除后继等值结点
             while (q!=NULL && q->data==p->data) {
             __________________________
             }
    }
}


A.
p->next=q->next; delete q;


B.
q->next=p->next; delete q; q=p->next;


C.
p->next=q->next; delete q; q= p->next;


D.
p->next=q->next; delete q; q=p;

评测结果
答案正确
得分
2 分

2-17
分数 2
中等
作者 严冰
单位 浙大城市学院
设有一个双向循环链表，每个结点中除有left、data和right三个域外，还增设了一个访问频度域freq，freq 的初值为零。每当链表进行一次查找操作后，被访问结点的频度域值便增1，同时调整链表中结点的次序，使链表按结点频度值非递增有序的次序排列。下列算法是符合上述要求的查找算法，请将该算法补充完整。


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
typedef struct Node{
ElemType  data;
   struct Node *left;
   struct Node *right;
intfreq;
} DNode;
DNode *locate_DList(DNode *&L, ElemType x)
{ //在表L中查找元素x，查找成功则调整结点频度域值及结点位置，并返回结点地址；
//查找不成功则返回NULL
DNode *p=L, *q;
   if (L==NULL)  return NULL;
   while (p->data!=x && p->right!=L)  p=p->right;
   if (p->data!=x)  return NULL;
   p->freq++;
   q=p->left;
   while (q!=L && q->freq<=p->freq)  q=q->left;  //查找插入位置
   if (q==L && q->freq<=p->freq) {  //需将p结点插在头结点L前
//将p结点先从链表中摘下来
p->left->right=p->right;
      p->right->left=p->left;
               //将p结点插在L结点前
      p->right=L;
      p->left=L->left;
      L->left->right=p;
      L->left=p;
      L=p;
   }
   else if (q!=p->left ) {  //若q不是p的前驱，则需调整结点位置，将p结点插在q结点后
//将p结点先从链表中摘下来
      p->left->right=p->right;
      p->right->left=p->left;
      ______________ //将p结点插在q结点后
   }
   return p;
}


A.
p->left=q; p->right=q->right;


B.
p->left=q; q->right=p;


C.
p->left=q; p->right=q->right; q->right->left=p; q->right=p;


D.
p->left=q; q->right=p; p->right=q->right; q->right->left=p;

评测结果
答案正确
得分
2 分

2-18
分数 2
简单
作者 考研真题
单位 浙江大学
已知带头结点的非空单链表 L 的头指针为 h，结点结构为 data | next，其中 next 是指向直接后继结点的指针。现有指针 p 和 q，若 p 指向 L 中非首且非尾的任意一个结点，则执行语句序列 q = p->next; p->next = q->next; q->next = h->next; h->next = q; 的结果是


A.
在 p 所指结点后插入 q 所指结点


B.
在 q 所指结点后插入 p 所指结点


C.
将 p 所指结点移动到 L 的头结点之后


D.
将 q 所指结点移动到 L 的头结点之后

评测结果
答案正确
得分
2 分

6-1 求链表的倒数第m个元素
分数 10
简单

全屏浏览

切换布局
作者 DS课程组
单位 浙江大学
请设计时间和空间上都尽可能高效的算法，在不改变链表的前提下，求链式存储的线性表的倒数第m（>0）个元素。

函数接口定义：
[ C++ ]

复制内容

格式

全屏
1
ElementType Find( List L, int m );
其中List结构定义如下：

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
▾
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data; /* 存储结点数据 */
    PtrToNode   Next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */
L是给定的带头结点的单链表；函数Find要将L的倒数第m个元素返回，并不改变原链表。如果这样的元素不存在，则返回一个错误标志ERROR。

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
▾
▾
#include <stdio.h>
#include <stdlib.h>

#define ERROR -1

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data;
    PtrToNode   Next;
};
typedef PtrToNode List;

List Read(); /* 细节在此不表 */
void Print( List L ); /* 细节在此不表 */

ElementType Find( List L, int m );

int main()
{
    List L;
    int m;
    L = Read();
    scanf("%d", &m);
    printf("%d\n", Find(L,m));
    Print(L);
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
5
1 2 4 5 6
3
输出样例：
[ out ]

复制内容

格式

全屏
1
2
4
1 2 4 5 6 
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB

6-2 线性表元素的区间删除
分数 10
简单

全屏浏览

切换布局
作者 DS课程组
单位 浙江大学
给定一个顺序存储的线性表，请设计一个函数删除所有值大于min而且小于max的元素。删除后表中剩余元素保持顺序存储，并且相对位置不能改变。

函数接口定义：
[ C++ ]

复制内容

格式

全屏
1
List Delete( List L, ElementType minD, ElementType maxD );
其中List结构定义如下：

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
▾
typedef int Position;
typedef struct LNode *List;
struct LNode {
    ElementType Data[MAXSIZE];
    Position Last; /* 保存线性表中最后一个元素在数组中的位置 */
};
L是用户传入的一个线性表，其中ElementType元素可以通过>、==、<进行比较；minD和maxD分别为待删除元素的值域的下、上界。函数Delete应将Data[]中所有值大于minD而且小于maxD的元素删除，同时保证表中剩余元素保持顺序存储，并且相对位置不变，最后返回删除后的表。

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
▾
▾
#include <stdio.h>

#define MAXSIZE 20
typedef int ElementType;

typedef int Position;
typedef struct LNode *List;
struct LNode {
    ElementType Data[MAXSIZE];
    Position Last; /* 保存线性表中最后一个元素的位置 */
};

List ReadInput(); /* 裁判实现，细节不表。元素从下标0开始存储 */
void PrintList( List L ); /* 裁判实现，细节不表 */
List Delete( List L, ElementType minD, ElementType maxD );

int main()
{
    List L;
    ElementType minD, maxD;
    int i;

    L = ReadInput();
    scanf("%d %d", &minD, &maxD);
    L = Delete( L, minD, maxD );
    PrintList( L );

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
10
4 -8 2 12 1 5 9 3 3 10
0 4
输出样例：
[ out ]

复制内容

格式

全屏
1
4 -8 12 5 9 10 
代码长度限制
16 KB
时间限制
200 ms
内存限制
64 MB

6-3 单链表逆转
分数 10
简单

全屏浏览

切换布局
作者 陈越
单位 浙江大学
本题要求实现一个函数，将给定的单链表逆转。

函数接口定义：
[ C++ ]

复制内容

格式

全屏
1
List Reverse( List L );
其中List结构定义如下：

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
▾
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data; /* 存储结点数据 */
    PtrToNode   Next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */
L是给定单链表，函数Reverse要返回被逆转后的链表。

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
▾
▾
#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data;
    PtrToNode   Next;
};
typedef PtrToNode List;

List Read(); /* 细节在此不表 */
void Print( List L ); /* 细节在此不表 */

List Reverse( List L );

int main()
{
    List L1, L2;
    L1 = Read();
    L2 = Reverse(L1);
    Print(L1);
    Print(L2);
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
[ in ]

复制内容

格式

全屏
1
2
5
1 3 4 5 2
输出样例：
[ out ]

复制内容

格式

全屏
1
2
1
2 5 4 3 1
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB

7-1 数组循环左移
分数 20
简单

全屏浏览

切换布局
作者 DS课程组
单位 浙江大学
本题要求实现一个对数组进行循环左移的简单函数：一个数组a中存有n（>0）个整数，在不允许使用另外数组的前提下，将每个整数循环向左移m（≥0）个位置，即将a中的数据由（a 
0
​
 a 
1
​
 ⋯a 
n−1
​
 ）变换为（a 
m
​
 ⋯a 
n−1
​
 a 
0
​
 a 
1
​
 ⋯a 
m−1
​
 ）（最前面的m个数循环移至最后面的m个位置）。如果还需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

输入格式:
输入第1行给出正整数n（≤100）和整数m（≥0）；第2行给出n个整数，其间以空格分隔。 

输出格式:
在一行中输出循环左移m位以后的整数序列，之间用空格分隔，序列结尾不能有多余空格。

输入样例：
[ in ]

复制内容

格式

全屏
1
2
8 3
1 2 3 4 5 6 7 8
输出样例：
[ out ]

复制内容

格式

全屏
1
4 5 6 7 8 1 2 3
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB
栈限制
8192 KB

8-1 线性表--简述以下算法的功能
分数 5
入门

全屏浏览
作者 wzl
单位 北京邮电大学
简述以下算法的功能

[ C ]

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
▾
▾
▾
▾
//算法1
Status A(LinkedList &L){// L是无头结点的单链表
    if(L && L->next){
        Q = L; L = L->next; P = L;
        while(P->next) P = P->next;
        P->next = Q; Q->next = NULL;
    }
    return OK;
}

//算法2
void BB(LNode *s, LNode *q){
    p = s;
    while(p->next !=q) p = p->next;
    p->next = s;
}//BB

void AA(LNode *pa, LNode *pb){
    //pa和pb分别指向不带头结点单循环链表中的两个结点
    BB(pa，pb);
    BB（pb, pa);
}//AA