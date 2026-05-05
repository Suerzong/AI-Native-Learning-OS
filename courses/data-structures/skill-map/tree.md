# 二叉树与 BST 技能地图

## 目标

学习者理解二叉树的递归定义，能实现二叉树的四种遍历和 BST 的增删查操作，能分析递归操作的复杂度。

## 必会概念

- 二叉树：每个节点最多两个子节点（left, right）
- 满二叉树：每层节点数最多的二叉树
- 完全二叉树：除最后一层外都是满的，最后一层靠左排列
- 二叉搜索树 BST：左 < 根 < 右的二叉树
- 遍历顺序：前序（根左右）、中序（左根右）、后序（左右根）、层序（逐层）

## 操作复杂度

### 二叉树

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 遍历（递归） | O(n) | 每个节点访问一次 |
| 层序遍历 | O(n) | 需要队列辅助 |
| 求高度 | O(n) | 递归求左右子树最大高度 |
| 求节点数 | O(n) | |

### 二叉搜索树 BST

| 操作 | 平均 | 最坏（退化为链表） | 说明 |
|------|------|-------------------|------|
| 查找 | O(log n) | O(n) | |
| 插入 | O(log n) | O(n) | |
| 删除 | O(log n) | O(n) | 最复杂，分三种情况 |
| 中序遍历 | O(n) | O(n) | 输出有序序列 |

## C 语言节点定义

```c
typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;
```

## 必会遍历（递归实现）

```c
// 前序遍历：根 -> 左 -> 右
void preorder(TreeNode* root) {
    if (root == NULL) return;
    printf("%d ", root->val);  // 访问根
    preorder(root->left);      // 遍历左子树
    preorder(root->right);     // 遍历右子树
}

// 中序遍历：左 -> 根 -> 右
void inorder(TreeNode* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}

// 后序遍历：左 -> 右 -> 根
void postorder(TreeNode* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->val);
}
```

## 层序遍历（BFS）

```c
void levelOrder(TreeNode* root) {
    if (root == NULL) return;
    // 用队列实现
    TreeNode* queue[1000];
    int front = 0, rear = 0;
    queue[rear++] = root;
    while (front < rear) {
        TreeNode* node = queue[front++];
        printf("%d ", node->val);
        if (node->left) queue[rear++] = node->left;
        if (node->right) queue[rear++] = node->right;
    }
}
```

## BST 删除（最复杂的操作）

分三种情况：
1. **叶节点**：直接删除，父节点指针置 NULL
2. **只有一个子节点**：用子节点替换当前节点
3. **有两个子节点**：找中序后继（右子树最小值）或中序前驱（左子树最大值），用其值替换当前节点，然后删除后继/前驱

```
删除 5：
      5                    6
     / \                  / \
    3   8     ->         3   8
       / \                  / \
      6   9                7   9
       \
        7
```

## 由遍历序列重建二叉树

- 前序 + 中序 可以唯一确定一棵二叉树
- 后序 + 中序 可以唯一确定一棵二叉树
- 前序 + 后序 不能唯一确定（除非是满二叉树）

## 常见错误

- 递归终止条件写成 `if (root == NULL) return;` 但忘记处理空树
- BST 删除有两个子节点时，找后继但忘记处理后继的右子树
- 不理解为什么 BST 的中序遍历是有序的
- 用有序数组构建 BST 时没有选择中间元素作为根

## 训练阶梯

1. **画图**：画出一棵有 7 个节点的完全二叉树
2. **递归遍历**：手写前序、中序、后序遍历
3. **层序遍历**：用队列实现层序遍历
4. **BST 插入**：实现 BST 的插入操作
5. **BST 查找**：实现 BST 的查找操作
6. **BST 删除**：实现 BST 的删除操作（重点练）
7. **有序数组转 BST**：将有序数组转换为平衡 BST

## 参考

- runoob.com/data-structures/binary-tree.html
- runoob.com/data-structures/binary-search-tree.html
