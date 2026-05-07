# 工作流与智能体（Workflows + Agents）

本指南介绍常见的工作流和智能体模式。

  * **工作流（Workflows）**具有预定的代码路径，设计为按特定顺序运行。
  * **智能体（Agents）**是动态的，定义自己的流程和工具使用方式。

LangGraph 在构建智能体和工作流时提供多种优势，包括[持久化](https://docs.langchain.com/oss/python/langgraph/persistence)、[流式传输](https://docs.langchain.com/oss/python/langgraph/streaming)以及对调试和[部署](https://docs.langchain.com/oss/python/langgraph/deploy)的支持。

## LLM 与增强

工作流和智能体系统基于 LLM 以及你添加的各种增强。[工具调用](https://docs.langchain.com/oss/python/langchain/tools)、[结构化输出](https://docs.langchain.com/oss/python/langchain/structured-output)和[短期记忆](https://docs.langchain.com/oss/python/langchain/short-term-memory)是定制 LLM 的几种方式。

## 提示链（Prompt Chaining）

提示链中，每个 LLM 调用处理前一个调用的输出。常用于执行可分解为较小、可验证步骤的任务。例如：
  * 将文档翻译为不同语言
  * 验证生成内容的一致性

## 并行化（Parallelization）

LLM 同时处理任务。用于：
  * 拆分子任务并并行运行，提高速度
  * 多次运行同一任务以检查不同输出，增加置信度

## 路由（Routing）

路由工作流处理输入，然后将其引导到特定上下文的任务。允许为复杂任务定义专门的流程。

## 编排器-工作者（Orchestrator-Worker）

编排器将任务分解为子任务，委派给工作者，并将工作者输出合成为最终结果。LangGraph 的 `Send` API 支持动态创建工作者节点。

## 评估器-优化器（Evaluator-Optimizer）

一个 LLM 调用创建响应，另一个评估该响应。如果需要改进，则提供反馈并重新创建，直到生成可接受的响应。

## 智能体（Agents）

智能体通常由使用[工具](https://docs.langchain.com/oss/python/langchain/tools)执行操作的 LLM 实现。它们在连续的反馈循环中运行，用于问题和解决方案不可预测的情况。智能体比工作流有更多自主权，可以决定使用哪些工具以及如何解决问题。
