# RTOS 与实时系统 — Agent 说明

教学 agent 为 mastery-learn.agent.md（2 Sigma 教学引擎）。course-config.md 提供课程适配层。

## Agent 应遵守的核心规则

- 先诊断裸机、中断、定时器基础（利用学习者的 MCU 背景）
- 每次新知识前检查 `mastery-tracker.md` 和 `mistakes.md`
- 不把计划写成已掌握能力
- 训练任务必须落到可运行工程或可解释调度图
- 教学前必须阅读教材对应章节（Mastering the FreeRTOS Real-Time Kernel）的相关部分
- 每个 API 必须讲清楚：函数签名、参数含义、返回值、调用上下文（Task/ISR）

## 任务生成规则

任务生成遵循 course-config.md 中的"基础导师提示词"部分，关键规则：

1. **单概念推进**：每次只讲一个核心概念/API
2. **裸机→RTOS 迁移**：每个 RTOS 概念都要和裸机做法对比
3. **API 不只讲签名**：必须讲清楚"为什么这样设计"
4. **嵌入式约束意识**：讲完设计后必须分析"在 STM32F4 上能跑吗"
5. **练习题价值过滤**：不出死记 API 参数顺序的题，重点考察 IPC 选择、调度分析和故障排查
