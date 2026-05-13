# 睡前复习与遗忘曲线系统

## 概述

基于类艾宾浩斯遗忘曲线的自动复习系统。每天北京时间 23:00 自动从学习记录中提取知识点，生成 15 分钟复习报告，通过邮件发送到 Outlook。

## 使用方式

```bash
# 手动收集知识卡片
python3 tools/review_system.py ingest

# 生成复习报告（打印到终端）
python3 tools/review_system.py generate --output

# 发送复习报告（邮件）
python3 tools/review_system.py send

# 试运行（不真正发送）
python3 tools/review_system.py send --dry-run

# 查看系统状态
python3 tools/review_system.py status

# 调整推送时间（例如改到 22:30）
python3 tools/review_system.py set-time 22:30

# 定时检查（由 cron 每 5 分钟调用）
python3 tools/review_system.py tick
```

## 复习间隔

默认复习间隔为：当天、1天、3天、7天、14天、30天。

优先级规则（从高到低）：
1. `mistakes.md` 中未复测通过的错误
2. `mastery-tracker.md` 中正确率低于 80% 的技能
3. 最近 1-7 天刚学过的知识点
4. 已掌握但到达长期巩固节点的内容

## 数据来源

- `courses/*/mastery-tracker.md` — 各课程掌握度追踪表
- `courses/*/mistakes.md` — 各课程错题与误区记录
- `plan/record/daily/*.md` — 每日复盘学习收获

## 配置文件

- `review/config.json` — 推送时间、时区、强度等配置
- `review/queue.json` — 复习卡片队列
- `review/daily/YYYY-MM-DD.md` — 每日复习报告归档
- `review/send_log.json` — 发送记录

## 复习反馈

收到报告后回复格式：
```
复习反馈：反向传播=2，循环队列=1
```

评分标准：1=完全忘了，2=模糊，3=基本记得，4=清晰

## 安全说明

- 不读取、不提交微信 token、cc-connect token、私钥或 `.cc-connect/` 配置
- 邮件凭据存储在 `~/.config/edge-ai/email.env`，权限 600
- 复习归档和队列状态可提交到私有 GitHub 仓库
