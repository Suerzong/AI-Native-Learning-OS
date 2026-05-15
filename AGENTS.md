# AGENTS.md — Agent 指令总纲

本文件是所有 Agent 的共享规则入口。项目结构、能力模块、文件操作规则等详见 `CLAUDE.md`。

## 必读文件

每个 Agent 在执行任务前，必须先读取：
1. `CLAUDE.md` — 项目结构、核心规则、能力模块、文件操作规则
2. `learning-progress.md` — 用户当前能力画像
3. `course-index.md` — 课程资料索引

## 间隔复习策略

所有教学和复盘类 agent 必须读取 `plan/spaced-review-policy.md` 中的复习规则。各课程 `course-config.md` 只负责课程领域知识，不重复写入复习规则。

## 生活伴侣策略

生活聊天类 agent 必须读取 `plan/life-companion-policy.md`。聊天记录写入 `personal/` 目录，默认不进入 Git，不记录密码、地址等敏感信息。

## 自动化系统

- **学习伴侣**：`tools/companion.py` — 晨间/午间/晚间邮件推送，`wechat-companion/` 存储状态
- **间隔复习**：`tools/review_system.py` — 错题收集、反馈处理、复习报告，`review/` 存储队列
- **邮件推送**：`tools/email_push.py` — SMTP 发送到 Outlook
- **定时任务**：cron 每 5 分钟运行 `companion.py tick`，自动派发各时段任务

## 云服务器模型切换

- 唯一入口：`/usr/local/bin/ccswitch`
- 常用命令：`ccswitch current`、`ccswitch list`、`ccswitch sw <branch>`
- 当前采用 Git 分支式 Claude 配置，配置目录为 `/home/ubuntu/.claude`
- 不要使用旧的 `cc-switch`、`ai-model` 或旧 `set-ccswitch-profile` 入口

## 教学引擎

掌握学习教学由 `.github/agents/mastery-learn.agent.md` 驱动，包含 8 步教学循环、错误分类、掌握度判断。`/mastery-learn` 和 `/teach-course` 均加载此引擎。

## 不可修改

- `plan/ability-framework.md` — 十二大能力模块标准定义
- `profile.md` — 个人基本信息
- `.github/` — Copilot 配置（除非明确要求）
