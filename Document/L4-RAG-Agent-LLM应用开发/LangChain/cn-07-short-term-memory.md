# 短期记忆（Short-term Memory）

短期记忆是智能体在当前对话中存在的状态。它包含消息历史和你在[图状态](https://docs.langchain.com/oss/python/langgraph/graph-api#state)中定义的任何自定义字段。

## 基本概念

LangChain 智能体通过消息状态自动维护对话历史。每次调用智能体时，它会看到整个对话历史，从而能够引用之前的消息并维护上下文。

## 管理对话历史

在长时间对话中，消息历史可能会变得很长，超出模型的上下文窗口。LangChain 提供了管理上下文窗口的策略：

  * **消息修剪（Trimming）**——删除较旧的消息以适应上下文窗口
  * **消息摘要（Summarizing）**——将较长的对话历史压缩为较短的摘要

## 使用检查点（Checkpointer）

LangGraph 提供检查点功能，允许智能体在多次调用之间保持状态：

    from langgraph.checkpoint.memory import InMemorySaver

    checkpointer = InMemorySaver()

    agent = create_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer,
    )

    # 使用 thread_id 维护对话状态
    config = {"configurable": {"thread_id": "1"}}
    result = agent.invoke({"messages": [{"role": "user", "content": "Hi!"}]}, config=config)

在生产环境中，使用持久化检查点器将消息历史保存到数据库。参见 [PostgresSaver](https://docs.langchain.com/oss/python/langgraph/add-memory#manage-short-term-memory) 等实现。

## 自定义状态

可以通过中间件或 `state_schema` 参数定义自定义状态模式来记住对话期间的附加信息：

    from langchain.agents import AgentState

    class CustomState(AgentState):
        user_preferences: dict

    agent = create_agent(model=model, tools=tools, state_schema=CustomState)
