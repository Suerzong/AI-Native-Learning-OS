# 数学资料视觉 LaTeX 转写

- 更新时间：2026-05-20 16:25:24
- 原则：不使用 OCR；先渲染页图，再由视觉阅读整理为 LaTeX Markdown。
- 不确定的公式、页码、题号统一标记 `[待核对]`。

## PDF 资料目录

- [工科数学分析基础 上册](工科数学分析基础 上册/index.md)
- [工科数学分析基础 下册](工科数学分析基础 下册/index.md)

## 照片批次目录

- [standalone-images](manual-batches/standalone-images/index.md)

## 使用方式

```powershell
python tools\math_visual_latex_pipeline.py --pdf '工科数学分析基础 上册.pdf' --start 18 --end 24 --zoom 2.0
python tools\math_visual_latex_pipeline.py --image-dir 'temp\math\new-photos' --batch-name '2026-05-20-绪论'
```
