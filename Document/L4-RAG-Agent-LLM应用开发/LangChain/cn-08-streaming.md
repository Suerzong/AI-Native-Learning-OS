# 流式传输（Streaming）

流式传输允许你实时查看智能体的中间进度，而不是等待完整响应。这对改善用户体验至关重要，特别是对于较长的响应。

## 基本流式传输

使用 `stream` 方法流式返回智能体的消息：

    from langchain.messages import AIMessage, HumanMessage

    for chunk in agent.stream({
        "messages": [{"role": "user", "content": "Search for AI news and summarize the findings"}]
    }, stream_mode="values"):
        latest_message = chunk["messages"][-1]
        if latest_message.content:
            if isinstance(latest_message, HumanMessage):
                print(f"User: {latest_message.content}")
            elif isinstance(latest_message, AIMessage):
                print(f"Agent: {latest_message.content}")
        elif latest_message.tool_calls:
            print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")

## 流式模式

LangGraph 支持多种流式模式：

  * `values`——流式传输每个步骤后的完整状态值
  * `updates`——流式传输每个步骤后的状态更新
  * `messages`——流式传输来自图中任何节点的完整消息和消息块
  * `custom`——流式传输自定义数据
  * `debug`——流式传输调试信息

## 流式传输 Token

要流式传输模型生成的个别 token，使用 `messages` 流式模式：

    for msg, metadata in agent.stream(
        {"messages": [{"role": "user", "content": "Tell me a joke"}]},
        stream_mode="messages"
    ):
        if hasattr(msg, 'content') and msg.content:
            print(msg.content, end="|", flush=True)

## 工具中的流式传输

工具可以使用 `runtime.stream_writer` 发出自定义流式更新：

    @tool
    def get_weather(city: str, runtime: ToolRuntime) -> str:
        """获取指定城市的天气。"""
        writer = runtime.stream_writer
        writer(f"Looking up data for city: {city}")
        return f"It's always sunny in {city}!"

## 事件流

使用 `astream_events` 方法获取更详细的流式事件：

    async for event in agent.astream_events(
        {"messages": [{"role": "user", "content": "Hello"}]},
        version="v2"
    ):
        if event["event"] == "on_chat_model_stream":
            print(event["data"]["chunk"].content, end="|")
