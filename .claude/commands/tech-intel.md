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

按以下顺序抓取，每个来源用 WebFetch 获取：

1. `https://github.com/trending` — GitHub Trending（重点关注 AI/ML/embedded 方向）
2. `https://huggingface.co/papers` — Hugging Face 最新论文
3. `https://news.ycombinator.com/` — Hacker News 首页
4. `https://arxiv.org/list/cs.LG/recent` — arXiv 机器学习最新论文
5. `https://arxiv.org/list/cs.CV/recent` — arXiv 计算机视觉最新论文

如果某个来源无法访问，跳过并在报告中注明。

## 第 2 步：定向搜索

根据已发现的重点方向，用 WebSearch 追踪一手来源，关键词包括但不限于：

- "Edge AI" OR "edge inference" OR "on-device AI"
- "model quantization" OR "model compression" OR "knowledge distillation"
- "ExecuTorch" OR "TFLite" OR "ONNX Runtime" OR "TensorRT" OR "OpenVINO"
- "ESP32 AI" OR "STM32 AI" OR "Jetson" OR "RK3588"
- "YOLO" OR "object detection" OR "edge vision"
- "AI chip" OR "NPU" OR "edge computing hardware"

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

# 自动推送

文件保存完成后，执行以下 git 操作自动同步到远程仓库：

```bash
git add tech-intel/ && git commit -m "$(cat <<'EOF'
[tech-intel] YYYY-MM-DD 科技情报报告

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)" && git push origin main
```

提交信息格式要求：
- 以 `[tech-intel]` 开头，加上今天的日期
- 简要说明今日最重要的发现

如果 git 操作失败（如网络问题），提示用户但不要中断任务。
