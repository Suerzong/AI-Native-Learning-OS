# Tools

## Domain File Agent

`domain_file_agent.py` 用于在指定域名内搜索并下载相关文件。它会从起始 URL 开始爬取 HTML 页面，只保留同域名链接，并按文件扩展名与关键词筛选下载目标。

常用命令：

```powershell
python tools/domain_file_agent.py https://example.com --ext pdf,zip --keyword edge-ai --dry-run
python tools/domain_file_agent.py https://example.com/docs/ --ext pdf,docx,pptx --output downloads/example
```

参数说明：

- `url`: 起始域名或页面，例如 `https://example.com/docs/`
- `--ext`: 文件扩展名，逗号分隔；默认包含 `pdf/docx/pptx/xlsx/zip/md/txt` 等常见资料格式
- `--keyword`: 文件 URL 中必须包含的关键词，可重复传入多个
- `--output`: 下载目录，默认 `downloads/domain-files`
- `--max-pages`: 最多扫描多少个 HTML 页面，默认 `300`
- `--include-subdomains`: 允许扫描子域名
- `--dry-run`: 只预览匹配文件，不下载

下载完成后，工具会在输出目录生成 `download_manifest.tsv`，记录文件名、原始 URL、来源页面和扩展名。

## WeChat Template Push

`wechat_template_push.py` sends a WeChat Official Account or test-account template message for private study reminders. It reads credentials from environment variables and does not store secrets in the repository.

Required private environment variables: `WECHAT_MP_APPID`, `WECHAT_MP_SECRET`, `WECHAT_MP_OPENID`, `WECHAT_MP_TEMPLATE_ID`.

Dry run:

```bash
python3 tools/wechat_template_push.py --dry-run --content "Evening review reminder"
```

