# 流式传输（Streaming）

LangGraph 实现了流式系统来展示实时更新。流式传输对于增强基于 LLM 的应用程序的响应性至关重要，通过在完整响应准备好之前逐步显示输出来改善用户体验。

## 基本用法

LangGraph 图暴露 `stream`（同步）和 `astream`（异步）方法来生成流式输出：

    for chunk in graph.stream(
        {"topic": "ice cream"},
        stream_mode=["updates", "custom"],
        version="v2",
    ):
        if chunk["type"] == "updates":
            for node_name, state in chunk["data"].items():
                print(f"Node {node_name} updated: {state}")
        elif chunk["type"] == "custom":
            print(f"Status: {chunk['data']['status']}")

## 流模式（Stream Modes）

模式 | 说明
---|---
`values` | 每步后的完整状态
`updates` | 每步后的状态更新
`messages` | LLM 调用的 2 元组（token, metadata）
`custom` | 通过 `get_stream_writer` 从节点发出的自定义数据
`checkpoints` | 检查点事件
`tasks` | 任务开始/完成事件
`debug` | 所有可用信息

## 图状态流

  * `updates` 流式传输每个步骤后状态的**更新**
  * `values` 流式传输每个步骤后状态的**完整值**

## LLM Token 流

使用 `messages` 流模式逐个 token 地流式传输 LLM 输出：

    for chunk in graph.stream(inputs, stream_mode="messages", version="v2"):
        if chunk["type"] == "messages":
            message_chunk, metadata = chunk["data"]
            if message_chunk.content:
                print(message_chunk.content, end="|", flush=True)

## 自定义数据

使用 `get_stream_writer` 从节点或工具内部发送自定义数据：

    from langgraph.config import get_stream_writer

    def node(state):
        writer = get_stream_writer()
        writer({"custom_key": "Generating custom data"})
        return {"answer": "some data"}

## 子图输出

设置 `subgraphs=True` 以在流式输出中包含子图的输出：

    for chunk in graph.stream(inputs, subgraphs=True, stream_mode="updates", version="v2"):
        print(chunk["ns"])  # () for root, ("node_name:task_id",) for subgraph

## 多模式同时使用

    for chunk in graph.stream(inputs, stream_mode=["updates", "custom"], version="v2"):
        if chunk["type"] == "updates":
            ...
        elif chunk["type"] == "custom":
            ...

## 使用任意 LLM

使用 `stream_mode="custom"` 从任何 LLM API 流式传输数据，即使该 API 不实现 LangChain 聊天模型接口。
