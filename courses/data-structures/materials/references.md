# 参考资料索引

本文件列出学习数据结构与算法的主要参考资料。教学 agent 在讲解知识点时应优先查阅本地资料。

---

## 本地课件（北京邮电大学 数据结构课程）

路径：`materials/数据结构/slides/`

按章节组织的 PPT 转换 MD，包含课堂讲解内容、图解、代码示例。

| 文件 | 内容 | 对应知识图谱 |
|------|------|-------------|
| ch01-绪论.md | 课程介绍、基本概念、逻辑结构与存储结构 | 技能 1.1 |
| ch02-线性表1-顺序存储.md | 顺序表定义、操作实现、时间复杂度 | 技能 1.2 |
| ch02-线性表2-链式存储(1).md | 单链表定义、头插法尾插法 | 技能 1.3 |
| ch02-线性表2-链式存储(2).md | 单链表操作：查找、插入、删除 | 技能 1.3 |
| ch02-线性表2-链式存储(4).md | 双向链表、循环链表 | 技能 1.4 |
| ch03-栈和队列1-概念与基本实现.md | 栈和队列的定义、顺序/链式实现 | 技能 1.5, 1.6 |
| ch03-栈和队列2-栈与递归.md | 递归概念、栈与递归的关系 | 技能 1.5 |
| ch03-栈和队列4-栈与递归应用.md | 递归应用实例 | 技能 1.5 |
| ch04-树和二叉树.md | 二叉树定义、性质、遍历、存储结构 | 技能 2.2 |

---

## 本地教程

路径：`materials/数据结构/tutorial/菜鸟教程-数据结构.md`

整理自 runoob.com 的数据结构教程，已转为本地 MD。覆盖内容：
- 数据结构与算法概述、时间/空间复杂度
- 数组、链表（单/双/循环）、栈、队列
- 哈希表、二叉树、BST、堆
- 图与遍历、排序算法、查找算法
- 递归/分治、贪心、动态规划

**教学 agent 在讲解任何知识点时，应先查阅此文件获取内容，再补充额外讲解。**

---

## 本地习题库

路径：`materials/数据结构/tasks/`

| 文件 | 内容 | 对应章节 |
|------|------|---------|
| task1.md | 线性表判断题（PTA 格式，含评分） | 第 2 章 |
| task2.md | 栈和队列判断题 | 第 3 章 |
| task3.md | 树和二叉树判断题 | 第 4 章 |
| 数据结构题库.md | 综合题库（判断+选择+填空+应用，含答案和解析） | 全部章节 |

**教学 agent 生成任务时，可从题库中选题，或基于题库风格自行出题。**

---

## 在线参考（备选）

当本地资料不足以覆盖某个知识点时，再查阅以下在线资源。

地址：https://www.runoob.com/datastructures

### 第一层：基础概念与线性结构

| 主题 | 链接 | 对应节号 |
|------|------|---------|
| 数据结构概述 | runoob.com/data-structures | 01 |
| 算法基本概念 | runoob.com/data-structures/basic-algorithm-concept | 02 |
| 时间复杂度 | runoob.com/data-structures/time-complexity | 02 |
| 数组 | runoob.com/data-structures/array | 03 |
| 链表 | runoob.com/data-structures/linked-list | 04-06 |
| 单向链表 | runoob.com/data-structures/linked-list-singly | 04-05 |
| 双向链表 | runoob.com/data-structures/linked-list-doubly | 06 |
| 循环链表 | runoob.com/data-structures/linked-list-circular | 06 |
| 栈 | runoob.com/data-structures/stack | 07-08 |
| 队列 | runoob.com/data-structures/queue | 09-10 |

### 第二层：树与哈希

| 主题 | 链接 | 对应节号 |
|------|------|---------|
| 哈希表 | runoob.com/data-structures/hash | 13-14 |
| 二叉树 | runoob.com/data-structures/binary-tree | 15-17 |
| 二叉树遍历 | runoob.com/data-structures/binary-tree-traversal | 16-17 |
| 二叉搜索树 | runoob.com/data-structures/binary-search-tree | 18-19 |
| 堆 | runoob.com/data-structures/heap | 20-21 |
| 优先队列 | runoob.com/data-structures/priority-queue | 21 |

### 第三层：图与排序

| 主题 | 链接 | 对应节号 |
|------|------|---------|
| 图 | runoob.com/data-structures/graph | 23-24 |
| 图的遍历 | runoob.com/data-structures/graph-traversal | 25-26 |
| 排序算法 | runoob.com/data-structures/sorting-algorithm | 27-31 |
| 冒泡排序 | runoob.com/data-structures/bubble-sort | 27 |
| 选择排序 | runoob.com/data-structures/selection-sort | 28 |
| 插入排序 | runoob.com/data-structures/insertion-sort | 28 |
| 快速排序 | runoob.com/data-structures/quick-sort | 29 |
| 归并排序 | runoob.com/data-structures/merge-sort | 30 |
| 堆排序 | runoob.com/data-structures/heap-sort | 31 |
| 二分查找 | runoob.com/data-structures/binary-search | 32-33 |

### 第四层：算法思维

| 主题 | 链接 | 对应节号 |
|------|------|---------|
| 递归 | runoob.com/data-structures/recursion | 35 |
| 分治算法 | runoob.com/data-structures/divide-and-conquer | 35 |
| 贪心算法 | runoob.com/data-structures/greedy-algorithm | 36 |
| 动态规划 | runoob.com/data-structures/dynamic-programming | 37-38 |

---

## 推荐书籍

| 书名 | 适用阶段 | 说明 |
|------|---------|------|
| 《数据结构（C 语言版）》严蔚敏 | 第一~三层 | 国内经典教材 |
| 《算法导论》CLRS | 第三~四层 | 进阶参考，理论深入 |
| 《大话数据结构》 | 第一~二层 | 入门读物，图多易懂 |
| 《算法图解》Grokking Algorithms | 第一~三层 | 图解为主，适合入门 |

## LeetCode 推荐刷题顺序

### 第一阶段：线性结构（先打基础）

| 题号 | 题名 | 知识点 |
|------|------|--------|
| 206 | Reverse Linked List | 链表反转 |
| 21 | Merge Two Sorted Lists | 链表合并 |
| 141 | Linked List Cycle | 快慢指针 |
| 20 | Valid Parentheses | 栈 |
| 155 | Min Stack | 栈设计 |
| 232 | Implement Queue using Stacks | 栈队列互转 |

### 第二阶段：树与哈希

| 题号 | 题名 | 知识点 |
|------|------|--------|
| 94 | Binary Tree Inorder Traversal | 中序遍历 |
| 102 | Binary Tree Level Order Traversal | 层序遍历 |
| 104 | Maximum Depth of Binary Tree | 递归 |
| 236 | LCA of a Binary Tree | BST |
| 1 | Two Sum | 哈希表 |
| 242 | Valid Anagram | 哈希表 |

### 第三阶段：排序与查找

| 题号 | 题名 | 知识点 |
|------|------|--------|
| 912 | Sort an Array | 快排/归并 |
| 75 | Sort Colors | 荷兰国旗 |
| 347 | Top K Frequent Elements | 堆/桶排序 |
| 33 | Search in Rotated Sorted Array | 二分变体 |
| 34 | Find First and Last Position | 二分边界 |

### 第四阶段：算法思维

| 题号 | 题名 | 知识点 |
|------|------|--------|
| 70 | Climbing Stairs | DP 入门 |
| 198 | House Robber | DP |
| 322 | Coin Change | DP |
| 55 | Jump Game | 贪心 |
| 46 | Permutations | 回溯/递归 |

---

## 在线工具

| 工具 | 链接 | 用途 |
|------|------|------|
| Visualgo | visualgo.net | 算法可视化 |
| LeetCode | leetcode.cn | 刷题练习 |
| 代码随想录 | programmercarl.com | 刷题路线 |
| CS-Notes | CyC2018/CS-Notes (GitHub) | 面试复习 |
