# 工作流与智能体（Workflows + Agents）

本页面内容与 [cn-02-agents.md](./cn-02-agents.md) 相同，涵盖了 LangGraph 的工作流和智能体模式。

主要内容包括：

  * **提示链（Prompt Chaining）**：每个 LLM 调用处理前一个调用的输出
  * **并行化（Parallelization）**：LLM 同时工作，拆分子任务或多次运行以增加置信度
  * **路由（Routing）**：处理输入后引导到特定上下文任务
  * **编排器-工作者（Orchestrator-Worker）**：编排器分解任务、委派给工作者、合成最终结果
  * **评估器-优化器（Evaluator-Optimizer）**：一个 LLM 创建响应，另一个评估，迭代直到可接受
  * **智能体（Agents）**：动态、自主的 LLM，使用工具在反馈循环中运行

每种模式都提供了 Graph API 和 Functional API 两种实现方式的代码示例。

完整示例和详细代码请参阅 [LangGraph 官方文档](https://docs.langchain.com/oss/python/langgraph/workflows-agents)。
