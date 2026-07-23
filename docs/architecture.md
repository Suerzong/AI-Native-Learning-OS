# 系统架构详解

> 目标读者：想理解 AI-Native-Learning-OS 设计理念的开发者、Agent 系统设计者。

---

## 概述

AI-Native-Learning-OS 不是一个"在 App 里嵌入 AI 聊天"的系统。它的架构设计围绕一个核心假设：**AI Agent 可以成为个人学习的操作系统，而不只是偶尔求助的工具。**

这个假设驱动了以下架构决策：
- 文件即状态（而非数据库）
- 约束优先于自由生成（Hook + 枚举）
- 多 Agent 分工（而非单一全能 Agent）
- 日常通讯工具作为交互入口（而非独立 Web UI）

---

## 四层架构

```
交互入口层 ──→ 通信网关层 ──→ Agent 执行层 ──→ 数据与存储层
```

### 层 1：交互入口层

系统的所有交互入口都是用户已有的日常工具：

| 入口 | 使用场景 | 技术链路 |
|------|---------|---------|
| **WeChat** | 发送命令、学习对话、日常闲聊 | cc-connect → CLI |
| **Outlook** | 接收每日计划、复习报告、AI 晨报 | SMTP 推送 |
| **GitHub** | 触发定时任务、存储版本历史 | GitHub Actions |
| **终端 CLI** | 开发调试、直接控制 | 本地执行 |

设计原则：**零额外 App**。用户不需要安装新工具，所有交互嵌入现有工作流。

### 层 2：通信网关层

这一层只有 Claude Code。它承担三个职责：

1. **协议转换**：将来自 WeChat、GitHub Actions、CLI 的不同格式请求统一为内部 Agent 调用
2. **行为契约执行**：读取 `CLAUDE.md` 中的规则，确保 Agent 行为不越界
3. **Hook 触发**：在关键操作（文件写入、状态变更）前后执行验证脚本

Claude Code 不直接执行具体任务——它只做编排和路由。

### 层 3：Agent 执行层

三个 Agent 各司其职，互不耦合：

| Agent | 文件 | 触发方式 | 核心逻辑 |
|-------|------|---------|---------|
| Mastery-Learn | `agents/mastery-learn.agent.md` | WeChat 命令 | 8 步教学闭环 → 错题入库 → 间隔复习 |
| Companion |（内嵌于 Claude Code 行为规则） | cron + WeChat | 5 段日循环 → 计划/复盘 → 日记 |
| Tech-Intel | `agents/tech-intel.agent.md` | GitHub Actions cron | 50+ 源抓取 → 分级过滤 → 邮件推送 |

Agent 之间不直接通信。它们通过共享文件交换信息：
- Mastery-Learn 写入 `review/mistakes.md` → Companion 的睡前复习读取
- Companion 写入 `plan/daily-plan.md` → Mastery-Learn 参考当前学习进度
- Tech-Intel 写入 `tech-intel/` → Companion 的晨间推送引用

### 层 4：数据与存储层

**核心原则：文件即状态。**

不使用 MySQL、PostgreSQL、SQLite 或任何数据库。所有数据存储在 Markdown（人类可读）和 JSON（结构化状态）文件中。

为什么：
1. AI Agent 可以直接读取和写入文件，不需要额外的 API 层
2. Markdown 文件可以被 Git 版本控制
3. 人类可以直接打开文件查看、编辑、调试
4. Agent 会话之间通过文件恢复上下文——消除了 "chatbot 失忆" 问题

---

## Agent 行为约束模型

### 三层约束

```
契约层（CLAUDE.md）
  ↓ 定义不可绕过的行为规则
验证层（Python Hook）
  ↓ 在 Write/Edit 操作前后自动执行
枚举层（固定枚举值）
  ↓ 掌握度等级、出题权限、错误类型
```

### 契约层

`CLAUDE.md` 是 Agent 的"宪法"。它定义了：
- 允许的源文件范围（源隔离——禁止引用外部知识）
- 教学会话的必读顺序
- 响应格式要求
- 禁止的行为（如跳过诊断直接讲解、替用户写代码等）

### 验证层

Python 脚本在 Agent 每次 Write 操作时自动触发（通过 Claude Code PreToolUse Hook），验证：
- 教学内容是否包含必填字段（`原文定位`、`知识点分层`、`教学轮次`）
- 段落引用是否落在教材范围内
- 掌握度变更是否合法（只能升级，不能跳级）

### 枚举层

以下值在系统中有固定枚举，Agent 不得自由发挥：

| 枚举类型 | 可选值 |
|---------|--------|
| 掌握度等级 | 0-5（未开始 → 识别 → 复述 → 使用 → 掌握 → 串联） |
| 出题权限 | 仅教材段落内容、禁止引入外部知识、禁止代码实现题 |
| 错误类型 | 概念误解、计算错误、公式误用、遗漏步骤 |
| 学习事件类型 | teach、practice、diagnose、remediate、review |

---

## 5 段式日循环

companion.py 的 tick 机制在云服务器上以 cron 持续运行。每次 tick 检查当前时间并执行对应动作：

```
tick() 被 cron 调用（每 5 分钟）
  ↓
检查当前时间窗口
  ↓
┌─ 5:00-5:30  →  generate_morning_plan()
├─ 7:00-7:30  →  send_morning_email()
├─ 12:30-13:00 → reorient_afternoon()
├─ 21:30-22:00 → trigger_evening_review()
└─ 23:00-23:30 → trigger_sleep_review()
```

每个动作执行后记录时间戳，防止同一天内重复执行。

---

## 通信协议

### WeChat → Agent 链路

```
User types "/start-day" in WeChat
  → cc-connect receives the message
    → Forwards to local CLI: claude /start-day
      → Claude Code reads CLAUDE.md, AGENTS.md
        → Routes to Companion behavior
          → Reads plan/ability-framework.md, plan/roadmap.md, courses/*/index.md
            → Generates daily-plan.md
              → Returns summary to CLI
                → cc-connect sends back to WeChat
```

### 邮件推送链路

```
companion.py generates report as Markdown
  → Converts to HTML via markdown-to-email template
    → SMTP (QQ Mail) sends to Outlook
      → User receives formatted email
```

---

## 数据模型

### 核心文件

| 文件 | 格式 | 写入者 | 读取者 | 内容 |
|------|------|--------|--------|------|
| `learning-progress.md` | Markdown | Companion（自动） | 所有 Agent | 12 模块 × 6 级掌握度的能力矩阵 |
| `plan/daily-plan.md` | Markdown | Companion | Mastery-Learn, Companion | 当日计划、三件事、最低完成线 |
| `review/mistakes.md` | Markdown | Mastery-Learn | Companion（睡前复习） | 错题列表，按课程和错误类型分类 |
| `review/queue.json` | JSON | review_system.py | review_system.py | 间隔复习排期队列 |
| `plan/ability-framework.md` | Markdown | 手动 | 所有 Agent | 12 模块能力标准定义（不可变） |
| `tech-intel/YYYY-MM-DD/` | Markdown | tech_intel_cloud.py | Companion | 每日科技情报报告 |

---

## 安全设计

### 密钥管理

- API 密钥通过环境变量传入，由 `write_local_claude_settings.py` 写入本地配置文件
- 配置文件（`.claude/settings.local.json`）在 `.gitignore` 中排除
- 所有进度文件和日志不会包含明文密钥

### 隐私数据隔离

- `personal/`、`Bills/`、`inbox/` 等目录完全排除在 Git 之外
- 每日 review 记录（`plan/record/daily/`）不进入公开仓库
- WeChat 聊天记录存储在 `personal/chat/`，不公开

---

## 扩展性

当前架构支持以下扩展方向（未实现）：

1. **新 Agent 接入**：只需在 `AGENTS.md` 中注册，在 `claude/commands/` 中添加命令定义
2. **新通信渠道**：在网关层添加新的协议适配器（如 Telegram Bot、Slack App）
3. **新数据格式**：数据层的 Markdown/JSON 可扩展为其他格式，Agent 只需更新读取逻辑
