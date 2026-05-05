# skill-map: dimensionality-reduction — 降维（PCA、t-SNE）

## 目标

掌握降维技术的原理和应用，能用 PCA 做特征压缩和可视化，能用 t-SNE 做高维数据可视化。

## 必知概念

### PCA（主成分分析）
- **核心思想**：找到数据方差最大的方向（主成分），将数据投影到低维空间
- **数学基础**：
  - 协方差矩阵：C = 1/n * X^T X
  - 特征值分解：C = V * Lambda * V^T
  - 主成分：特征值最大的特征向量
- **方差贡献率**：每个主成分解释的方差比例
- **累积方差**：前 k 个主成分的方差贡献率之和
- **应用**：
  - 特征压缩：减少特征数量，保留主要信息
  - 可视化：降到 2D/3D 后绘制
  - 去噪：去掉方差小的成分（可能是噪声）
- **缺点**：线性变换，可能丢失非线性结构
- **sklearn**：`PCA(n_components=k)`

### t-SNE（t-分布随机邻域嵌入）
- **核心思想**：在高维空间保持局部邻域关系的同时，将数据映射到 2D/3D
- **关键特点**：
  - 非线性降维
  - 保留局部结构（相似的点在低维中仍然相似）
  - 不保留全局距离
- **关键参数**：
  - perplexity（困惑度）：控制局部 vs 全局结构的平衡，通常 5-50
  - learning_rate：学习率
  - n_iter：迭代次数
- **缺点**：计算慢，每次运行结果不同，不能用于新数据
- **sklearn**：`TSNE(n_components=2)`

### PCA vs t-SNE

| 特性 | PCA | t-SNE |
|------|-----|-------|
| 线性/非线性 | 线性 | 非线性 |
| 速度 | 快 | 慢 |
| 可解释性 | 强（主成分有明确含义） | 弱 |
| 全局结构 | 保留 | 不保证 |
| 局部结构 | 不保证 | 保留 |
| 新数据 | 可以 transform | 不能（需要重新计算） |
| 用途 | 特征压缩、去噪 | 可视化 |

## 必知函数/API

| 函数 | 用途 | 示例 |
|------|------|------|
| `PCA(n_components=k)` | PCA 降维 | `pca.fit_transform(X)` |
| `.explained_variance_ratio_` | 方差贡献率 | `pca.explained_variance_ratio_` |
| `.components_` | 主成分方向 | `pca.components_` |
| `.transform()` | 降维 | `pca.transform(X_new)` |
| `.inverse_transform()` | 还原 | `pca.inverse_transform(X_low)` |
| `TSNE(n_components=2)` | t-SNE 降维 | `tsne.fit_transform(X)` |

## 常见错误

1. **PCA 前忘记标准化**
   ```python
   # 错误：不同量纲的特征直接 PCA
   pca = PCA(n_components=2)
   X_pca = pca.fit_transform(X)  # 大数值特征主导主成分

   # 正确：先标准化
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   X_pca = pca.fit_transform(X_scaled)
   ```

2. **t-SNE 用于新数据**
   ```python
   # 错误：t-SNE 没有 transform 方法
   tsne = TSNE(n_components=2)
   X_embedded = tsne.fit_transform(X_train)
   X_test_embedded = tsne.transform(X_test)  # AttributeError!

   # t-SNE 只能用于可视化，不能用于特征工程
   ```

3. **忽略方差贡献率**
   ```python
   # 不检查保留了多少信息
   pca = PCA(n_components=2)
   X_pca = pca.fit_transform(X)

   # 应该检查
   print(pca.explained_variance_ratio_)
   # 如果总和只有 0.5，说明丢失了 50% 的信息
   ```

## 训练阶梯

### Step 1: PCA 基础（Level 0→2）
- 理解主成分的含义
- 用 sklearn 做 PCA
- 查看方差贡献率

### Step 2: PCA 可视化（Level 2→3）
- 降到 2D 后绘制散点图
- 用颜色区分不同类别
- 分析不同类别在主成分空间的分布

### Step 3: PCA 特征压缩（Level 3）
- 选择保留 95% 方差的主成分数
- 比较降维前后的模型性能
- 理解降维加速的效果

### Step 4: t-SNE（Level 3→4）
- 理解 t-SNE 的非线性特性
- 调节 perplexity 参数
- 与 PCA 可视化对比

### Step 5: 综合运用（Level 4→5）
- PCA 用于特征工程，t-SNE 用于可视化
- 在实际项目中选择合适的降维方法
- 理解降维对模型性能的影响

## 掌握标准

- **Level 3**: 能用 PCA 降维和可视化，能解释方差贡献率
- **Level 4**: 能用 t-SNE 可视化高维数据，能调节参数
- **Level 5**: 能在实际项目中选择合适的降维策略

## 参考资料

- materials/noob/034_ml-dimensionality-reduction.md
- scikit-learn 分解文档：https://scikit-learn.org/stable/modules/decomposition.html
- scikit-learn 流形学习：https://scikit-learn.org/stable/modules/manifold.html
