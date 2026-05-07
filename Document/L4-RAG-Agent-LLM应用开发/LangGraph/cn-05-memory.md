# 记忆（Memory）

记忆是记住先前交互信息的系统。对于 AI 智能体，记忆至关重要，因为它让他们记住先前的交互、从反馈中学习并适应用户偏好。

## 短期记忆（Short-term Memory）

短期记忆或线程范围的记忆，通过在会话中维护消息历史来跟踪持续的对话。LangGraph 将短期记忆作为智能体[状态](https://docs.langchain.com/oss/python/langgraph/graph-api#state)的一部分进行管理。状态通过[检查点器](https://docs.langchain.com/oss/python/langgraph/persistence#checkpoints)持久化到数据库，因此线程可以随时恢复。

### 管理短期记忆

对话历史是短期记忆最常见的形式。完整历史可能不适合 LLM 的上下文窗口，导致不可恢复的错误。管理技术包括：

  * **消息修剪**——删除较旧的消息以适应上下文窗口
  * **消息摘要**——将较长的对话历史压缩为摘要
  * **过滤**——基于条件选择性保留消息

## 长期记忆（Long-term Memory）

长期记忆在不同对话或会话之间保留信息。与短期记忆不同，长期记忆保存在自定义"命名空间"中。

### 记忆类型

记忆类型 | 存储内容 | 人类示例 | 智能体示例
---|---|---|---
语义记忆（Semantic） | 事实 | 在学校学到的东西 | 关于用户的事实
情景记忆（Episodic） | 经验 | 做过的事情 | 过去的智能体行为
程序记忆（Procedural） | 指令 | 本能或技能 | 智能体系统提示

### 语义记忆

语义记忆涉及保留特定事实和概念。对于 AI 智能体，语义记忆常用于通过记住过去交互中的事实来个性化应用。

语义记忆可以用两种方式管理：
  * **档案（Profile）**——单一、持续更新的 JSON 文档，包含用户的键值对信息
  * **集合（Collection）**——持续更新和扩展的文档集合，每个记忆更窄范围

### 情景记忆

情景记忆涉及回忆过去的事件或行动。常用于帮助智能体记住如何完成任务，通常通过 few-shot 示例提示实现。

### 程序记忆

程序记忆涉及记住执行任务的规则。对于 AI 智能体，程序记忆是模型权重、智能体代码和智能体提示的组合。

## 写入记忆

两种主要方法：
  * **在关键路径中**——在运行时创建记忆，实时更新但可能增加延迟
  * **在后台**——作为独立后台任务创建，消除主应用延迟但需要决定触发时机

## 记忆存储

LangGraph 将长期记忆作为 JSON 文档存储在 [Store](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store) 中。每个记忆组织在自定义 `namespace`（类似文件夹）和唯一 `key`（类似文件名）下。

    from langgraph.store.memory import InMemoryStore
    store = InMemoryStore(index={"embed": embed, "dims": 2})
    store.put(("user_id", "context"), "key", {"data": "value"})
    item = store.search(("user_id", "context"), query="search term")
