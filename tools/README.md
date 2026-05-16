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

## Email Push

`email_push.py` sends automatic reminders and reports through QQ Mail SMTP to Outlook. Manual requests from WeChat still reply in WeChat; cron and other automatic triggers should use email instead of `cc-connect send`.

Private config lives in `~/.config/edge-ai/email.env`:

```bash
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=<qq-mail-address>
SMTP_PASSWORD=<qq-mail-authorization-code>
SMTP_FROM=<qq-mail-address>
TECH_INTEL_TO=Suerzong@outlook.com
```

Dry run:

```bash
python3 tools/email_push.py --dry-run --body "Evening review reminder"
```

`graph_email_push.py` remains as a Microsoft Graph OAuth option, but it requires Azure app registration.

Microsoft Graph dry run:

```bash
python3 tools/graph_email_push.py --dry-run --body "Evening review reminder"
```

## UCloud Task Scraper

`ucloud_task_scraper.py` 抓取 BUPT 教学平台（UCloud）上的所有待办任务，输出 JSON + Obsidian Markdown 到 `ucloud-tasks/YYYY-MM-DD.*`。

### 架构

UCloud 是 BladeX 微服务 SPA（Vue.js + CAS 认证）。脚本不爬页面 HTML，而是直接调用后端 API：

| API 端点 | 说明 |
| --- | --- |
| `/ykt-site/site/student/undone` | 未完成教学活动 |
| `/ykt-site/assignment/student/list/sort` | 作业 |
| `/ykt-activity/survey/page/student/todo` | 问卷 |
| `/ykt-site/evaluate-student/taskPage` | 互评任务 |
| `/ykt-site/examination/list-stu` | 考试 |

API base: `https://apiucloud.bupt.edu.cn`

Auth: cookies（`token` / `refresh_token` / `identity`），通过 `Blade-Auth` header 传递，`refresh_token` grant 自动续期。

### 首次使用

```bash
# 1. 在浏览器登录 https://ucloud.bupt.edu.cn/uclass/
# 2. 从浏览器自动提取 cookies
python3 tools/ucloud_cookie_helper.py

# 如果自动提取失败，手动粘贴（DevTools > Application > Cookies > ucloud.bupt.edu.cn）：
python3 tools/ucloud_cookie_helper.py --manual

# 3. 抓取待办任务
python3 tools/ucloud_task_scraper.py
```

### 日常使用

```bash
python3 tools/ucloud_task_scraper.py                    # 输出到 ucloud-tasks/
python3 tools/ucloud_task_scraper.py --print-report     # 终端打印
python3 tools/ucloud_task_scraper.py --date 2026-05-20  # 指定日期
```

### Cookie 过期

Blade-Auth token 约 2 小时过期，脚本自动用 `refresh_token` 续期。如 refresh_token 也失效，重新运行 `ucloud_cookie_helper.py`。

### 输出示例

```
ucloud-tasks/
  2026-05-16.json    # 结构化数据（可用于自动化）
  2026-05-16.md      # Obsidian 可读报告
```

### 集成到 Daily Workflow

可以加入 GitHub Actions cron 或本地 cron，每天定时抓取：

```bash
# crontab: 每天 8:00、12:00、18:00 抓取
0 8,12,18 * * * cd ~/Edge-AI && python3 tools/ucloud_task_scraper.py
```
