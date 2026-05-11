# Tech Intel Cloud Automation

这个方案把每日 AI 晨报迁到 GitHub Actions。只要仓库在 GitHub 上，并且配置好 Secrets，即使本机关机，云端也会在每天早上运行。

## 运行时间

- 北京时间：每天 07:00
- 工作流：`.github/workflows/tech-intel-daily.yml`
- 云端脚本：`tools/tech_intel_cloud.py`
- 生成文件：
  - `tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/email-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/raw-index-YYYY-MM-DD.json`

## 邮件收件人

默认收件人是：

```text
Suerzong@outlook.com
```

如果在 GitHub Secrets 里设置了 `TECH_INTEL_TO`，会优先使用该值。

## 必需 GitHub Secrets

进入 GitHub 仓库：

```text
Settings -> Secrets and variables -> Actions -> New repository secret
```

添加以下值：

```text
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=你的发件 Gmail 地址
SMTP_PASSWORD=你的 Gmail App Password
SMTP_FROM=你的发件 Gmail 地址
TECH_INTEL_TO=Suerzong@outlook.com
```

注意：`SMTP_PASSWORD` 不是 Gmail 登录密码，应该是 Gmail 账号开启两步验证后生成的 App Password。

## 安全规则

- 不把邮箱密码、App Password、API Token 写入仓库。
- `email-YYYY-MM-DD.md` 只保存可发送的正文，不保存凭据。
- 如果 SMTP Secrets 没配，云端仍会生成 Obsidian 报告，但会跳过邮件发送。

## 手动测试

在 GitHub 仓库页面打开：

```text
Actions -> Daily AI Tech Intel -> Run workflow
```

可以不填日期，默认使用北京时间当天。测试成功后，仓库会自动提交当天的 `tech-intel/` 报告，并发送 Outlook 邮件。

## 本地自动化的处理

云端稳定后，可以暂停本机 Codex 的每日 7 点自动化，避免重复发两封。
