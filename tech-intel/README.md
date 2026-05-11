# tech-intel

`tech-intel/` 是 Ethen 的每日 AI 科技情报目录，也是 Obsidian 自动读取的知识库入口。不要再新增单独的 Obsidian 导出目录。

## 目录结构

```text
tech-intel/
  sources.yaml                         # 信息源配置
  README.md
  YYYY-MM-DD/
    tech-intel-YYYY-MM-DD.md           # Obsidian 主报告
    email-YYYY-MM-DD.md                # 邮件短版
    raw-index-YYYY-MM-DD.json          # 原始抓取索引
```

## 运行流程

每天运行 `/tech-intel` 时，agent 应按以下流程工作：

1. 读取 `profile.md`、`learning-progress.md`、`plan/daily-plan.md` 和最近的日报。
2. 从 `tech-intel/sources.yaml` 读取信息源。
3. 抓取、解析、去重和评分。
4. 先输出草稿，不直接写正式文件。
5. 根据 Ethen 的反馈迭代。
6. 确认满意后写入主报告、邮件短版和 raw-index。

## 云端自动化

本地 Codex 自动化依赖电脑开机。若需要电脑关机时也能发送晨报，使用 GitHub Actions 云端方案：

- 工作流：`.github/workflows/tech-intel-daily.yml`
- 云端脚本：`tools/tech_intel_cloud.py`
- 配置说明：`tech-intel/cloud-automation.md`
- 默认收件人：`Suerzong@outlook.com`

云端方案会在北京时间每天 07:00 生成 Obsidian 主报告、邮件版和 raw-index，并在 SMTP Secrets 配置完成后发送邮件。

## 迭代确认机制

`/tech-intel` 必须按“模拟运行 -> 询问意见 -> 修改 -> 再模拟”的方式工作。

每一版草稿后，agent 都应主动询问：

- 内容是否太少或太多？
- 一手来源是否足够？
- 正文速读是否抓到了重点？
- 本科生可读解释是否清楚？
- 今日行动是否贴合当天学习主线？
- 邮件版是否适合手机邮箱阅读？

只有当 Ethen 明确说“满意”“可以”“定稿”“写入正式文件”等确认时，才写入正式文件。否则继续迭代。

## 内容密度

日报默认不是极简新闻卡片，而是“前沿视野 + 学习过滤器”：

- Obsidian 主报告默认保留 5 条最重要信息。
- 总候选信号应覆盖 10-20 条，按一手官方、论文代码、开源社区、产品创业、中文线索分层。
- 重要条目要尽量抓正文，并输出“正文速读”，让 Ethen 在 Obsidian 里能读懂要点。
- 邮件短版仍然保持短，只保留 Top 3、今日建议和关键链接。

## Obsidian 主报告

主报告路径：

```text
tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md
```

主报告必须适合 Obsidian 阅读和检索：

- 使用 YAML frontmatter。
- 使用稳定标题层级。
- 保留原始链接。
- 可使用内部链接，如 `[[learning-progress]]`、`[[plan/daily-plan]]`。
- 每条重点信息都说明“本科生可读解释”和“和我当前阶段的关系”。
- 重要条目增加“正文速读”和“关键原文短摘”；不要只给标题和链接。
- 只给 1-3 个今日行动，避免干扰当天主线学习。

推荐 frontmatter：

```yaml
---
title: "Daily Tech Intelligence Report - YYYY-MM-DD"
date: YYYY-MM-DD
type: tech-intel
tags:
  - tech-intel
  - edge-ai
  - ai-news
aliases:
  - "YYYY-MM-DD AI 科技情报"
top_topics:
  - Edge AI
status: final
---
```

## 邮件短版

邮件短版路径：

```text
tech-intel/YYYY-MM-DD/email-YYYY-MM-DD.md
```

邮件短版用于未来定时发送到邮箱。它只负责提供适合发送的 Markdown 内容，不包含 SMTP、邮箱 token 或任何私人凭据。邮件应适合 iPhone 早读：比极简摘要更丰富，但不替代 Obsidian 完整日报。

邮件短版必须包含：

```markdown
<!-- EMAIL_SUBJECT -->
YYYY-MM-DD AI晨报：{当天核心趋势}
<!-- EMAIL_BODY_START -->

# YYYY-MM-DD AI 科技情报

Ethen，早上好！

## 今日一句话总览

一句话说清今天最重要的技术/产业信号。

## 5 行摘要

- ...
- ...
- ...
- ...
- ...

## Top 5 简报

1. ...
2. ...
3. ...
4. ...
5. ...

## 今日时代动向

- 2-3 条趋势判断，说明对学习和就业方向的影响。

## 今天建议

1. ...

## 关键链接

- ...

## 抓取异常

- 无 / arXiv 限速 / WebSearch 不可用 / 官方 HTML 解析失败

## Obsidian 全文

`tech-intel/YYYY-MM-DD/tech-intel-YYYY-MM-DD.md`

<!-- EMAIL_BODY_END -->
```

## 报告内容

每日科技情报报告覆盖：

1. 今日摘要
2. 今日最重要的 5 条信息
3. 官方源：模型、产品、API 与开发者生态
4. 论文与代码：技术趋势源头
5. Edge AI / 嵌入式 AI 动态
6. GitHub 开源项目与工程信号
7. 新产品、创业与产业信号
8. 中文信息源二次筛选
9. 会议、课程与长期资源
10. 今日行动建议
11. 可写入知识库的条目
12. 时代动向分析：对学习与就业方向的启发
13. 附录 A：抓取状态
14. 附录 B：一手信号总览
15. 附录 C：低价值/不建议看的信息

抓取状态、一手信号总览和低价值信息默认放在文末。它们用于回溯和质量控制，不应打断正文阅读。

“时代动向分析”放在正文末尾、附录之前，用来把当天信息抽象为学习路线和就业方向判断。它必须具体、可执行，不能写成泛泛鼓励。

## 失败处理

普通失败不打断生成：

- 单个来源超时
- arXiv 限速
- 某个 GitHub topic 返回 0 条
- 官方 HTML 页面结构变化

关键失败必须询问 Ethen：

- 一级来源大面积失败
- Top 3 只能来自低可信来源
- 重要结论找不到原始来源
- 报告质量不足以指导学习安排

## 重要原则

- 不编造新闻、论文、链接或抓取结果。
- 不把计划写成已经完成的能力提升。
- 不覆盖旧日报，除非 Ethen 明确确认。
- 优先服务 Edge AI / 嵌入式 AI 长期成长，而不是追热点。
