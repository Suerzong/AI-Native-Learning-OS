---
description: 运行科技情报分析 Agent，生成今日 Daily Tech Intelligence Report
---

请执行"每日科技情报分析"任务。

$ARGUMENTS

你必须先读取以下文件：

- `.github/agents/tech-intel.agent.md` — 完整的 agent 指令（关注方向、信息源优先级、评分标准、输出格式）
- `profile.md` — 了解背景和学习方向
- `learning-progress.md` — 了解当前能力状态，用于判断信息的行动价值

如果某个文件不存在，请明确说明缺失文件，并在不编造信息的前提下继续完成任务。

---

# 任务目标

根据 tech-intel agent 的完整指令，从一手信息源搜集、筛选、评分并输出结构化的每日科技情报报告。

---

# 工作流程

## 第 1 步：抓取信息源

**必须使用 curl + API 方式**（WebFetch 和 WebSearch 在当前环境不可用）。

按以下顺序用 curl 抓取，中间文件保存到 `temp/` 目录：

1. GitHub Search API — 量化/推理、YOLO、Edge AI、模型压缩、本月新 ML 项目
2. Hacker News Algolia API — `https://hn.algolia.com/api/v1/search?tags=front_page`
3. arXiv API — cs.LG 分类下 edge AI / quantization / model compression 论文
4. HuggingFace Papers API（可选，可能超时）

详细命令参见 `.github/agents/tech-intel.agent.md` 的"执行说明"部分。

**注意事项：**
- 用 `python`（非 `python3`）解析 JSON
- 中间文件用 `temp/` 目录（非 `/tmp/`）
- 必须 `sys.stdout.reconfigure(encoding='utf-8')` 处理编码
- curl 输出重定向到文件，不要管道到 python

## 第 3 步：筛选与评分

对每条信息按照 tech-intel agent 中的评分标准打分：

- 重要性评分（1-5 分）
- 相关性评分（1-5 分）
- 行动价值分类

## 第 4 步：输出报告

按照 tech-intel agent 定义的完整格式输出报告，包含 8 个板块：

1. 今日最重要的 3 条信息
2. AI / LLM 动态（表格）
3. Edge AI / 嵌入式 AI 动态（表格）
4. GitHub 开源项目（表格）
5. 论文与研究（表格）
6. 今日噪音信息
7. 今日行动建议
8. 可写入知识库的条目

---

# 文件保存要求

1. 检查 `tech-intel/YYYY-MM-DD/` 文件夹是否存在（YYYY-MM-DD 为今天日期），不存在则创建
2. 将完整报告保存为 `tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md`
3. 报告开头注明日期和信息源覆盖范围

---

# GitHub 备份与微信晨报

文件保存完成后，先检查 Git 状态，再把当天生成的 `tech-intel/YYYY-MM-DD/` 自动同步到远程私有仓库。不要暂存或提交密钥、token、`.cc-connect/`、`.claude/profiles/`、`.claude/settings.local.json` 等本机凭据。

```bash
git status --short
git add tech-intel/YYYY-MM-DD/
git commit -m "$(cat <<'EOF'
[tech-intel] YYYY-MM-DD AI 微信晨报

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)" && git push origin main
```

提交信息格式要求：
- 以 `[tech-intel]` 开头，加上今天的日期
- 简要说明今日最重要的发现

如果没有变化，不要创建空提交。如果 git 操作失败（如网络问题或 GitHub 权限问题），提示用户但不要中断任务。

GitHub 备份完成后，写入适合手机阅读的 `email-YYYY-MM-DD.md` 短版，并明确写出：

- Obsidian 全文路径
- GitHub 备份状态：已推送 / 无变化 / 失败需检查
- 抓取异常摘要

云端微信定时晨报已停用。不要自动调用 `cc-connect send`，除非 Ethen 明确要求临时手动发送。
