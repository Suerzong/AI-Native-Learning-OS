# 快速开始指南

> 目标：从零搭建 AI-Native-Learning-OS 并完成首次运行。

---

## 前提条件

| 组件 | 最低要求 | 备注 |
|------|---------|------|
| Python | 3.10+ | 运行所有自动化脚本 |
| Git | 2.x | 版本控制和云同步 |
| Claude Code | 最新版 | AI Agent 编排中枢 |
| cc-connect | 最新版 | WeChat ↔ CLI 通信网关 |
| 云服务器 | Ubuntu 20.04+ | 24h 运行 cron 任务（推荐腾讯云 ECS） |
| QQ 邮箱 | — | SMTP 推送（或替换为其他 SMTP 服务） |

---

## 第一步：克隆仓库

```bash
git clone https://github.com/Suerzong/AI-Native-Learning-OS.git
cd AI-Native-Learning-OS
```

---

## 第二步：安装 Python 依赖

```bash
pip install -r tools/requirements.txt
```

> 如果 `requirements.txt` 尚未创建，核心依赖包括：
> ```bash
> pip install requests beautifulsoup4 pyyaml markdown lxml
> ```

---

## 第三步：配置 Claude Code

```bash
# 复制配置模板
cp claude/settings.example.json .claude/settings.local.json

# 编辑配置文件
# 填入你的 Claude API 凭证和权限配置
```

`.claude/settings.local.json` 包含个人 API 密钥和权限设置，**不能提交到 Git**（已在 `.gitignore` 中排除）。

---

## 第四步：配置 WeChat 接入

1. 按照 [cc-connect](https://github.com/cc-connect) 文档完成安装
2. 在 cc-connect 中配置命令转发规则：

```json
{
  "forward": {
    "/start-day": "claude /start-day",
    "/end-day": "claude /end-day",
    "/mastery-learn": "claude /mastery-learn",
    "/update-progress": "claude /update-progress",
    "/tech-intel": "claude /tech-intel",
    "/life-chat": "claude /life-chat"
  }
}
```

3. 测试 WeChat → CLI 连通性：在微信中发送任意消息，确认 cc-connect 已转发

---

## 第五步：配置云服务器

### 5.1 同步代码到云端

```bash
# 在云服务器上
git clone https://github.com/Suerzong/AI-Native-Learning-OS.git
cd AI-Native-Learning-OS
pip install -r tools/requirements.txt
```

### 5.2 设置 cron 定时任务

```bash
crontab -e
```

添加以下行：

```cron
# 学习伴侣 tick（每 5 分钟检查一次）
*/5 * * * * cd /path/to/AI-Native-Learning-OS && python3 tools/companion.py tick >> /var/log/companion.log 2>&1

# 每日技术情报（早上 7:00）
0 7 * * * cd /path/to/AI-Native-Learning-OS && python3 tools/tech_intel_cloud.py >> /var/log/tech-intel.log 2>&1
```

### 5.3 配置邮件发送

在 `tools/` 目录下创建 `.env` 文件：

```bash
SMTP_SERVER=smtp.qq.com
SMTP_PORT=587
SMTP_USERNAME=your_email@qq.com
SMTP_PASSWORD=your_smtp_password
RECIPIENT_EMAIL=your_outlook@outlook.com
```

---

## 第六步：初始化学习档案

### 6.1 编辑个人信息

```bash
# 填写你的基本信息
vim profile.md
```

### 6.2 设定学习方向

```bash
# 根据你的专业方向编辑 12 模块能力框架
vim plan/ability-framework.md
```

### 6.3 添加课程

```bash
# 在 courses/ 下为每门课创建目录
mkdir -p courses/your-course-name
# 放入教材 Markdown 文件
```

---

## 第七步：首次运行

```bash
# 生成今日学习计划
claude /start-day

# 开始一节掌握学习
claude /mastery-learn your-course-name

# 手动触发科技情报
claude /tech-intel
```

或者通过 WeChat 发送相同命令（如果已完成 cc-connect 配置）。

---

## 验证安装

成功运行后，你应该收到：

1. **一封"晨间启动"邮件**（如果 cron 已运行，或手动触发 `/start-day`）
2. **WeChat 中的回复**（如果 cc-connect 已配置）
3. **`plan/daily-plan.md` 已生成**（可在终端查看）

---

## 目录结构确认

安装完成后，你的目录结构应包含以下关键文件：

```
AI-Native-Learning-OS/
├── CLAUDE.md              ✅ Agent 行为契约
├── AGENTS.md              ✅ Agent 协调中枢
├── profile.md             ✅ 已填写个人信息
├── .claude/
│   └── settings.local.json ✅ 已配置 API 凭证
├── tools/
│   ├── companion.py        ✅ 学习伴侣
│   ├── review_system.py    ✅ 复习系统
│   └── .env                ✅ 邮件配置
├── plan/
│   └── ability-framework.md ✅ 已设定学习方向
└── courses/
    └── your-course/        ✅ 已添加至少一门课
```

---

## 常见问题

### Q: cc-connect 无法转发 WeChat 消息

检查 cc-connect 是否正常运行、命令转发规则 JSON 格式是否正确、防火墙是否阻止了 WebSocket 连接。

### Q: 邮件未收到

检查 `.env` 中的 SMTP 配置。QQ 邮箱需要使用授权码而非登录密码。确认云服务器的 587 端口未被屏蔽。

### Q: companion.py tick 未生效

检查 cron 日志（`/var/log/companion.log`）。确认 Python 路径正确（使用 `which python3` 检查）。确认工作目录正确（cron 中需使用绝对路径）。

### Q: Claude Code 无法读取 Agent 定义

确认 `.claude/` 配置目录结构正确。Agent 定义文件需放在 `agents/` 或 `.github/agents/` 目录下。

---

## 下一步

- 阅读 [架构详解](architecture.md) 理解系统设计
- 阅读 [Agent 设计哲学](agent-design.md) 了解如何定制 Agent 行为
- 查看 WECHAT_COMMANDS.md 了解完整命令列表
