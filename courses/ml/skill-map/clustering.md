# skill-map: clustering — 聚类分析（K-Means、层次聚类、DBSCAN）

## 目标

掌握无监督学习中的聚类算法，能用 sklearn 对数据进行分群并评估聚类质量。

## 必知概念

### K-Means
- **核心思想**：将数据分成 K 个簇，使每个点到其所属簇质心的距离之和最小
- **算法步骤**：
  1. 随机初始化 K 个质心
  2. 将每个点分配到最近的质心
  3. 重新计算每个簇的质心
  4. 重复 2-3 直到收敛
- **肘部法则**：绘制不同 K 值的 inertia 曲线，找拐点
- **轮廓系数**：衡量聚类质量，范围 [-1, 1]，越大越好
- **缺点**：需要预设 K，对初始质心敏感，只能发现球形簇
- **sklearn**：`KMeans(n_clusters=k)`

### 层次聚类（Hierarchical Clustering）
- **凝聚式**：自底向上，每次合并最近的两个簇
- **分裂式**：自顶向下，每次将一个簇分成两个
- **树状图（Dendrogram）**：展示聚类过程
- **优点**：不需要预设 K，能发现层次结构
- **缺点**：计算复杂度高，不适合大数据
- **sklearn**：`AgglomerativeClustering()`

### DBSCAN
- **核心思想**：基于密度的聚类，能发现任意形状的簇
- **关键参数**：
  - eps：邻域半径
  - min_samples：成为核心点的最小邻居数
- **点的分类**：
  - 核心点：eps 邻域内有 >= min_samples 个点
  - 边界点：在核心点的邻域内，但自身不是核心点
  - 噪声点：既不是核心点也不是边界点
- **优点**：不需要预设 K，能发现任意形状的簇，能识别噪声
- **缺点**：对参数敏感，不适合密度差异大的数据
- **sklearn**：`DBSCAN(eps=0.5, min_samples=5)`

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `KMeans()` | K-Means 聚类 | `KMeans(n_clusters=3)` |
| `.inertia_` | 惯性（SSE） | `model.inertia_` |
| `.cluster_centers_` | 簇中心 | `model.cluster_centers_` |
| `.labels_` | 聚类标签 | `model.labels_` |
| `silhouette_score()` | 轮廓系数 | `silhouette_score(X, labels)` |
| `AgglomerativeClustering()` | 层次聚类 | `AgglomerativeClustering(n_clusters=3)` |
| `dendrogram()` | 树状图 | `dendrogram(linkage_matrix)` |
| `DBSCAN()` | 密度聚类 | `DBSCAN(eps=0.5, min_samples=5)` |

## 常见错误

1. **混淆 inertia 和轮廓系数**
   ```python
   # inertia 越小越好（误差和）
   model.inertia_

   # 轮廓系数越大越好（[-1, 1]）
   silhouette_score(X, model.labels_)
   ```

2. **在原始标签上计算轮廓系数**
   ```python
   # 错误：用真实标签
   silhouette_score(X, y_true)  # 这不是聚类评估

   # 正确：用聚类标签
   silhouette_score(X, model.labels_)
   ```

3. **DBSCAN 参数选择不当**
   ```python
   # eps 太小：大部分点都是噪声
   model = DBSCAN(eps=0.01, min_samples=5)

   # eps 太大：所有点都在一个簇里
   model = DBSCAN(eps=100, min_samples=5)
   ```

## 训练阶梯

### Step 1: K-Means 基础（Level 0→2）
- 理解 K-Means 算法步骤
- 用 sklearn 训练 K-Means
- 可视化聚类结果

### Step 2: 选择 K（Level 2→3）
- 使用肘部法则
- 计算轮廓系数
- 比较不同 K 的结果

### Step 3: 层次聚类（Level 3）
- 绘制树状图
- 理解凝聚式聚类
- 与 K-Means 对比

### Step 4: DBSCAN（Level 3→4）
- 理解核心点、边界点、噪声
- 调节 eps 和 min_samples
- 发现任意形状的簇

### Step 5: 聚类评估（Level 4）
- 综合使用多种评估方法
- 选择最优算法和参数
- 将聚类结果用于下游任务

## 掌握标准

- **Level 3**: 能用 sklearn 进行聚类，能用肘部法则和轮廓系数评估
- **Level 4**: 能根据数据特点选择聚类算法，能调节参数优化结果
- **Level 5**: 能从零实现 K-Means，能将聚类用于实际项目（如客户分群）

## 参考资料

- materials/noob/033_ml-cluster-analysis.md
- scikit-learn 聚类文档：https://scikit-learn.org/stable/modules/clustering.html
