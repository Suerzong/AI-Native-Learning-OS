# Tech Intel Cloud Automation

当前稳定方案把每日 AI 晨报迁到腾讯云服务器，通过 cc-connect 在微信发送。GitHub Actions 邮箱方案只作为历史备选，不再作为默认发送方式。

## 运行时间

- 北京时间：每天 07:00
- 运行位置：`/home/ubuntu/Edge-AI`
- 定时器：`cc-connect cron`
- 推送方式：个人微信
- 云端脚本：`tools/tech_intel_cloud.py`
- 生成文件：
  - `tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/email-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/raw-index-YYYY-MM-DD.json`

## 微信推送

晨报发送到当前 cc-connect 绑定的个人微信会话。不要把微信 token、cc-connect token、个人账号 ID 或任何凭据写入仓库。

## GitHub 备份

每日生成后，云服务器必须把 `tech-intel/YYYY-MM-DD/` 提交并推送到 GitHub 私有仓库。超过普通 Git 限制的大文件走 Git LFS；密钥、token、`.cc-connect/`、`.claude/profiles/` 和 `.claude/settings.local.json` 不进入仓库。

## 安全规则

- 不把邮箱密码、App Password、API Token、微信 token 写入仓库。
- `email-YYYY-MM-DD.md` 只保存可发送到微信的正文，不保存凭据。
- 如果 GitHub push 失败，仍保存本地报告，并在微信晨报里提示需要手动检查。

## 手动测试

使用云服务器测试：

```bash
cc-connect cron list
cc-connect send -p Edge-AI -m "云端微信晨报通道测试"
```

测试成功后，微信会收到提示；次日 07:00 自动运行正式晨报。

## 本地自动化的处理

云端稳定后，保持本机 Codex 的每日 7 点邮箱自动化为暂停状态，避免重复发送。
