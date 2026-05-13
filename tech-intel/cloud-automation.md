# Tech Intel Cloud Automation

每日 AI 晨报和自动提醒统一走 Outlook 邮件。微信只用于 Ethen 主动发消息触发 Agent 的场景，自动任务不得默认调用 `cc-connect send` 主动发微信。

## 运行策略

- 默认收件人：`Suerzong@outlook.com`
- 发件方式：QQ 邮箱 SMTP，`smtp.qq.com:465`，SSL
- 运行位置：`/home/ubuntu/Edge-AI`
- 云端脚本：`tools/tech_intel_cloud.py` 或 `tools/email_push.py`
- 生成文件：
  - `tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/email-YYYY-MM-DD.md`
  - `tech-intel/YYYY-MM-DD/raw-index-YYYY-MM-DD.json`

## 邮件配置

QQ 邮箱 SMTP 配置只放在云端私密文件，不写入仓库：

```bash
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=<qq-mail-address>
SMTP_PASSWORD=<qq-mail-authorization-code>
SMTP_FROM=<qq-mail-address>
TECH_INTEL_TO=Suerzong@outlook.com
```

云服务器默认私密配置文件为 `~/.config/edge-ai/email.env`，权限应为 `600`。

## 安全规则

- 不把邮箱密码、SMTP 授权码、OAuth token、API Token、微信 token 写入仓库。
- `email-YYYY-MM-DD.md` 只保存可发送的邮件正文，不保存凭据。
- 如果邮件发送失败，保留本地报告并输出 SMTP 错误。

## 手动测试

```bash
python3 tools/email_push.py --dry-run \
  --subject "[灰度测试] Edge-AI 自动提醒已切换到 Outlook" \
  --body "微信手动触发仍回微信；自动提醒已改为 Outlook 邮件。"
```

dry run 通过且 QQ 邮箱授权码可用后，再去掉 `--dry-run` 发送真实测试邮件。
