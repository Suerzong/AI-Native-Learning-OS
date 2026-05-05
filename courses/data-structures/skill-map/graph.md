# 图 技能地图

## 目标

学习者理解图的基本概念，能用邻接矩阵和邻接表存储图，能实现 DFS 和 BFS 遍历，能解决连通性和路径问题。

## 必会概念

- 有向图 / 无向图
- 权值（Weight）：边的权重
- 度（Degree）：与顶点相连的边数（入度/出度）
- 连通图 / 连通分量
- 路径 / 最短路径
- 邻接矩阵 / 邻接表

## 存储方式对比

| 方式 | 空间 | 判断边是否存在 | 遍历邻居 | 适用场景 |
|------|------|---------------|---------|---------|
| 邻接矩阵 | O(V^2) | O(1) | O(V) | 稠密图 |
| 邻接表 | O(V+E) | O(degree) | O(degree) | 稀疏图 |

## 邻接矩阵实现

```c
#define MAX_V 100
int graph[MAX_V][MAX_V];  // graph[i][j] = 1 表示有边
int V;  // 顶点数

void addEdge(int u, int v) {
    graph[u][v] = 1;
    graph[v][u] = 1;  // 无向图
}
```

## 邻接表实现

```c
// 链表方式
typedef struct AdjNode {
    int dest;
    struct AdjNode* next;
} AdjNode;

AdjNode* adjList[MAX_V];

void addEdge(int u, int v) {
    // u -> v
    AdjNode* node = (AdjNode*)malloc(sizeof(AdjNode));
    node->dest = v;
    node->next = adjList[u];
    adjList[u] = node;
}
```

```cpp
// C++ vector 方式
vector<vector<int>> adj(V);
void addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);  // 无向图
}
```

## DFS 深度优先搜索

```c
int visited[MAX_V];

void dfs(int u) {
    visited[u] = 1;
    printf("%d ", u);
    for (int v = 0; v < V; v++) {
        if (graph[u][v] && !visited[v])
            dfs(v);
    }
}
```

DFS 适用场景：连通分量、拓扑排序、环检测、路径搜索。

## BFS 广度优先搜索

```c
void bfs(int start) {
    int visited[MAX_V] = {0};
    int queue[MAX_V], front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;
    while (front < rear) {
        int u = queue[front++];
        printf("%d ", u);
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !visited[v]) {
                visited[v] = 1;
                queue[rear++] = v;
            }
        }
    }
}
```

BFS 适用场景：无权图最短路径、层序遍历、社交网络中的"六度分隔"。

## DFS vs BFS

| 维度 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈（递归或显式） | 队列 |
| 空间 | O(V)（递归栈深） | O(V)（队列宽） |
| 最短路径 | 不保证 | 无权图中保证 |
| 遍历顺序 | 深度优先 | 广度优先 |

## 复杂度

| 操作 | 邻接矩阵 | 邻接表 |
|------|---------|--------|
| DFS/BFS | O(V^2) | O(V+E) |
| 空间 | O(V^2) | O(V+E) |

## 常见错误

- DFS 忘记标记 visited 导致死循环
- 无向图添加边只加了 u->v，忘记加 v->u
- BFS 用了栈而不是队列
- 邻接矩阵遍历邻居时遍历了所有 V 个顶点（应该只看有边的）
- 有向图和无向图的度数计算搞混

## 训练阶梯

1. **画图**：画出一个有 5 个顶点 7 条边的无向图
2. **邻接矩阵**：用邻接矩阵存储图
3. **邻接表**：用邻接表存储图
4. **DFS**：实现 DFS 遍历并打印访问顺序
5. **BFS**：实现 BFS 遍历并打印访问顺序
6. **连通分量**：用 DFS 计算图的连通分量数
7. **最短路径**：用 BFS 求无权图两点间最短路径

## 参考

- runoob.com/data-structures/graph.html
