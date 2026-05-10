# CLAUDE.md

这是宋恩泽（Ethen）的 Edge AI / 嵌入式 AI 学习工作区。

## 核心身份

- 姓名：宋恩泽（Ethen）
- 学校：北京邮电大学，电子工程学院
- 长期方向：Edge AI / 嵌入式 AI
- 目标：本科四年成长为具备工程能力和科研潜力的嵌入式 AI 工程师

## 项目结构

```
profile.md              # 个人信息
course-index.md         # 课程资料索引
learning-progress.md    # 12 大模块完整能力画像（核心文件）
plan/
  ability-framework.md  # 12 大能力模块标准定义（不可随意修改）
  roadmap.md            # 长期学习路线
  school-calendar.md    # 校历（含节次时间）
  timetable.md          # 课程表
  schedule.md           # 综合日程
  daily-plan.md         # 今日计划
  record/
    daily/              # 每日复盘 YYYY-MM-DD.md
courses/                # 课程资料
  circuit-analysis/
  matlab-simulation/
  stm32/
  ti-board/             # TI 板子学习
projects/               # 工程项目
resources/              # 学习资源索引
tech-intel/             # 每日科技情报报告（YYYY-MM-DD/ 子文件夹归档）
```

## 核心规则

### 12 大能力模块（不可修改）

所有学习记录、计划、复盘必须围绕以下 12 个模块展开：

1. 数学与理论基础
2. 编程语言与软件基础
3. 计算机系统基础
4. 电子电路与硬件基础
5. 单片机与裸机开发
6. 传感器、通信与外设接口
7. RTOS 与实时系统
8. 嵌入式 Linux 系统
9. 信号处理与计算机视觉
10. 机器学习与深度学习
11. 模型部署、端侧优化与 AI 硬件平台
12. 工程项目、机器人系统与科研能力

### 能力状态分级

- 已了解：看过或听过，知道基本概念
- 已学习：系统学过，但不一定能独立完成
- 已实践：跟随资料完成过代码、仿真、调试或项目
- 初步掌握：能在参考资料较少时完成基本复现和解释
- 已掌握：能不看教程独立复现、调试、修改并解释原理
- 已应用：已用于完整项目、课程设计、竞赛或科研任务

### 文件操作规则

**不可随意修改的文件：**
- `plan/ability-framework.md` — 十二大能力模块标准定义
- `profile.md` — 个人基本信息
- `course-index.md` — 课程索引

**谨慎修改的文件：**
- `learning-progress.md` — 仅在用户确实形成学习成果、完成实验、通过测试或明确要求时修改。不要把计划、突发事件、未完成任务写成能力提升。必须保持完整 12 模块结构，增量更新 + 全量输出
- `plan/roadmap.md` — 仅在用户明确要求调整长期路线时修改

**可修改的文件：**
- `plan/daily-plan.md` — 今日计划，每日更新
- `plan/record/daily/YYYY-MM-DD.md` — 每日复盘记录
- `courses/ti-board/exercises.md`
- `courses/ti-board/labs.md`
- `courses/ti-board/mistakes.md`
- `courses/ti-board/mastery-tracker.md`
- `courses/ti-board/daily-tests.md`
- `courses/ti-board/exams.md`

### 不要编造

- 课程资料不足时，必须明确说明缺少哪些文件或内容，不要编造
- 不要夸大用户能力
- 不要把"看过资料"写成"已掌握"
- 不要把计划中的任务写成已完成的能力

### 学习记录原则

- 用户说"学完某章"默认记录为"已学习"，不是"已掌握"
- 用户明确说明完成实验/代码/仿真/项目/独立复现，才记录为"已实践"或更高
- 每次更新 learning-progress.md 必须输出完整的 12 模块能力画像
- 不要覆盖已有记录，在原有基础上补充合并

## GitHub Copilot 配置

本仓库已有 `.github/copilot-instructions.md` 和 `.github/prompts/`、`.github/agents/` 配置。Claude Code 配置文件（CLAUDE.md、.claude/）与 Copilot 配置互不干扰，不要修改 `.github/` 下的 Copilot 配置。
