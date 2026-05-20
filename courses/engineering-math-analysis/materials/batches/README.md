# 批次处理结果

每个影印照片批次处理后，在本目录生成同名文件夹：

```text
batches/<batch-id>/
  ocr.md
  cleaned.md
  review.md
  provenance.md
```

处理原则：

- 先保存原始识别结果，再清理为 Markdown。
- 不确定内容用 `[待核对]` 标记。
- 保留来源页码和图片文件名。

