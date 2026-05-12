# Tech Intel Cloud Automation

云端微信晨报自动化已停用。

## 停用原因

腾讯云服务器访问外网不稳定，OpenAI、Google、Meta 等关键来源经常抓取失败，自动生成的 tech-intel 报告信息密度和可靠性不足。继续每天定时推送会制造噪音，因此不再作为默认方案运行。

## 当前状态

- `cc-connect cron` 中不保留每日 tech-intel 微信晨报任务。
- 本机 Codex 的每日邮箱自动化保持暂停状态。
- `tech-intel/YYYY-MM-DD/` 中已有历史报告保留。
- `tools/tech_intel_cloud.py` 仍可作为手动生成工具，但运行前应确认网络可用，并在报告中明确写出抓取失败的来源。

## 手动方案

需要 tech-intel 时，手动运行 `/tech-intel` 或云端脚本，先检查来源质量，再决定是否保存和提交。不要把微信 token、cc-connect token、邮箱密码、API Token 或任何私人凭据写入仓库。

如果以后要恢复自动化，必须先解决外网访问稳定性，再重新创建定时任务。
