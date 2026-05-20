# 影印资料来源清单

本文件记录教材、教辅、试题和照片批次来源。所有由影印照片转成的 Markdown 都必须能追溯到批次、页码和来源。

## 固定入口

照片放置路径：

```text
courses/engineering-math-analysis/materials/inbox/scans/<batch-id>/
```

推荐批次命名：

```text
YYYY-MM-DD-chapter-section-source
```

示例：

```text
2026-05-20-ch01-sec01-textbook
2026-05-20-ch01-exercise-tutor
```

## 批次产物

每个批次处理后，在以下目录生成：

```text
courses/engineering-math-analysis/materials/batches/<batch-id>/
  ocr.md
  cleaned.md
  review.md
  provenance.md
```

| 文件 | 内容 |
|---|---|
| `ocr.md` | 原始 OCR / 模型识别结果 |
| `cleaned.md` | 清理后的可读 Markdown |
| `review.md` | 待核对公式、题号、页码、疑点 |
| `provenance.md` | 图片文件名、页码、来源、处理时间 |

## 归档规则

- 教材内容归档到 `materials/textbook/`。
- 教辅内容归档到 `materials/tutor-book/`。
- 历年题、阶段测试、模拟题归档到 `materials/past-exams/`。
- 不确定的公式、页码、题号必须保留 `[待核对]`。
- 不得把不同章节的题目提前归入未到达章节。

## 当前资料状态

| 来源 | 状态 | 说明 |
|---|---|---|
| 教材影印版（上册 PDF） | 处理中 | 原件：`temp/math/工科数学分析基础 上册.pdf`；视觉 LaTeX 转写入口：`temp/math/visual-latex/工科数学分析基础 上册/`；已转写绪论页 1-6 与第 1 章开头 |
| 教材影印版（下册 PDF） | 待视觉转写 | 原件：`temp/math/工科数学分析基础 下册.pdf` |
| 教学辅导书影印版 | 待提交 | 教辅作为训练主材料 |
| 历年试题 | 已筛选 | 高等数学与工科数学分析试卷筛选结果：`temp/math/filtered-exams/`；仅用于阶段训练和考试训练 |

## 当前视觉转写规则

- OCR 路线已停用；扫描教材、照片批次统一使用“读图 + LaTeX 手工整理”。
- `temp/math/visual-latex/` 用于处理当前临时资料；课程正式归档仍按 `materials/textbook/`、`materials/tutor-book/`、`materials/past-exams/` 分类。
- 每页必须保留原始页图链接、PDF 页码/教材页码、转写状态。
- 不确定的公式、题号、页码必须标记 `[待核对]`。
