# 自动提醒通道策略

## 结论

自动触发的提醒、晨报、睡前复习和灰度测试统一发送到 Outlook 邮箱：`Suerzong@outlook.com`。

微信只保留手动触发场景：当 Ethen 在微信里主动发送 `/chat`、学习命令或自然语言请求时，Agent 继续直接回复微信。系统定时任务、cron、自动报告不再主动调用 `cc-connect send` 发微信，除非 Ethen 明确要求某一次手动转发到微信。

## 邮件链路

默认邮件链路：

- 发件邮箱：Ethen 的 QQ 邮箱
- 收件邮箱：`Suerzong@outlook.com`
- SMTP host：`smtp.qq.com`
- SMTP port：`465`
- 传输方式：SSL
- 认证方式：QQ 邮箱 SMTP 授权码

云端脚本：`tools/email_push.py`。

私密环境变量文件：`~/.config/edge-ai/email.env`

```bash
export SMTP_HOST="smtp.qq.com"
export SMTP_PORT="465"
export SMTP_USER="your@qq.com"
export SMTP_PASSWORD="QQ 邮箱 SMTP 授权码"
export SMTP_FROM="your@qq.com"
export TECH_INTEL_TO="Suerzong@outlook.com"
```

该文件权限设为 `600`，不进入 Git。

Dry run：

```bash
python3 tools/email_push.py --dry-run \
  --subject "[灰度测试] Edge-AI 自动提醒已切换到 Outlook" \
  --body "微信手动触发仍回微信；自动提醒已改为 Outlook 邮件。"
```

真实发送：

```bash
python3 tools/email_push.py \
  --subject "[灰度测试] Edge-AI 自动提醒已切换到 Outlook" \
  --body "微信手动触发仍回微信；自动提醒已改为 Outlook 邮件。"
```

## 触发规则

- 微信手动触发：回复微信。
- 自动触发：发送 Outlook 邮件。
- 科技情报、睡前复习、每日提醒、定时灰度测试：全部属于自动触发。
- 自动任务不得默认调用 `cc-connect send` 给微信。

## 灰度测试

完成清理和脚本验证后，先运行 dry run。确认发件人、收件人、标题、正文正确后，预留约 10 分钟准备窗口，再发送一封真实灰度测试邮件。

如果云端缺少 QQ 邮箱地址或 SMTP 授权码，停止在真实发送前，输出缺失项和可直接重跑的命令，不伪造成功。
