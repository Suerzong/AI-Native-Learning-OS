# TI 板卡个性化训练课程包

本目录用于训练学习者掌握 LP-MSPM0G3507 / MSPM0G3507 的嵌入式开发能力，并支持一个基于“2 Sigma Problem”的个性化教学 agent 持续运行。

## 使用方式

每次学习会话从 `AGENT.md` 开始。Agent 应先读取：

1. `learner/current-state.md`：当前学习状态
2. `mastery-tracker.md`：各技能掌握度
3. `syllabus.md`：阶段路径
4. `skill-map/`：对应技能地图
5. `materials/examples-map.md`：SDK 例程索引

然后按“诊断 -> 定目标 -> 出训练任务 -> 即时反馈 -> 迁移测试 -> 更新状态 -> 推进或补救”的循环教学。

## 目录结构

| 路径 | 用途 |
|---|---|
| `AGENT.md` | 教学 agent 的总规则和行为协议 |
| `agent/` | 诊断、反馈、出题、晋级规则 |
| `learner/` | 学习者画像、当前状态、学习日志、弱点记录 |
| `skill-map/` | GPIO、UART、ADC 等技能拆解 |
| `materials/` | 官方 SDK、数据手册、板卡资料、例程索引 |
| `code/` | 学习者自己的练习代码 |
| `exercises.md` | 小训练任务库 |
| `labs.md` | 实验任务库 |
| `exams.md` | 阶段考核题 |
| `mistakes.md` | 错题和误区记录 |
| `mastery-tracker.md` | 掌握度追踪表 |

## 个性化修改

修改 `learner/profile.md` 写入学习者背景、目标、时间安排和偏好。每次训练后更新 `learner/current-state.md`、`mastery-tracker.md` 和 `mistakes.md`。
