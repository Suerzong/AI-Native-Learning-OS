# temp/math 转换报告

- 状态：OCR 路线已停用。扫描版教材和图片以后以 `temp/math/visual-latex/` 下的“视觉阅读 + LaTeX 手工整理”为准。
- 保留本目录仅用于已经可直接提取文本的 PDF、JSON、旧试验记录；不要把本目录中的 OCR 结果作为教学材料源稿。

- 生成时间：2026-05-20 15:36:58
- 源目录：`temp/math`
- 输出目录：`temp/math/readable-md`

## 文件转换结果

| 源文件 | 输出文件 | 方法 | 页数/字符 | 备注 |
|---|---|---|---:|---|
| `bump-1.3.2 (1).pdf` | [bump-1.3.2 (1).md](bump-1.3.2 (1).md) | PDF 内嵌文本提取 | 421/421 pages, 353962 chars |  |
| `bump_items.json` | [bump_items.readable.md](bump_items.readable.md) | JSON 索引结构化 | - | 已生成两类试卷清单 |
| `test_page.png` | [test_page.ocr.md](test_page.ocr.md) | RapidOCR 图片识别 | 2903 bytes |  |
| `工科数学分析基础 上册.pdf` | [工科数学分析基础 上册.md](工科数学分析基础 上册.md) | RapidOCR 扫描页识别 | 2/390 pages, 222 chars | 扫描 PDF，公式需人工复核 |
| `工科数学分析基础 下册.pdf` | [工科数学分析基础 下册.md](工科数学分析基础 下册.md) | RapidOCR 扫描页识别 | 2/379 pages, 237 chars | 扫描 PDF，公式需人工复核 |
| `工科数学分析试卷合集.md` | [工科数学分析试卷合集.readable.md](工科数学分析试卷合集.readable.md) | Markdown 排版增强 | 97143 bytes |  |
| `高等数学试卷合集.md` | [高等数学试卷合集.readable.md](高等数学试卷合集.readable.md) | Markdown 排版增强 | 217356 bytes |  |

## 筛选输出

- 高等数学试卷清单：`temp/math/filtered-exams/highmath-index.md`
- 高等数学合并 PDF：`temp/math/filtered-exams/highmath-selected.pdf`
- 工科数学分析 / 数学分析试卷清单：`temp/math/filtered-exams/engineering-math-analysis-index.md`
- 工科数学分析 / 数学分析合并 PDF：`temp/math/filtered-exams/engineering-math-analysis-selected.pdf`
