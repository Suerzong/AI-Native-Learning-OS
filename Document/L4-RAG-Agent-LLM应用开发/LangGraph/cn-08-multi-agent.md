# 多智能体（Multi-Agent）

本概念在[工作流与智能体](./cn-02-agents.md)页面中涵盖。

LangGraph 文档目前没有单独的多智能体页面。
参阅：https://docs.langchain.com/oss/python/langgraph/workflows-agents

多智能体系统涉及多个智能体协作或竞争以完成任务。LangGraph 通过子图（Subgraphs）和智能体间通信支持多智能体架构。主要模式包括：

  * **监督器模式（Supervisor）**：一个监督智能体协调多个工作者智能体
  * **层级模式（Hierarchical）**：智能体按层级组织，上级分配任务给下级
  * **对等模式（Peer-to-peer）**：智能体平等协作，直接通信

详细实现示例请参阅 [LangGraph 官方文档](https://docs.langchain.com/oss/python/langgraph/workflows-agents)。
