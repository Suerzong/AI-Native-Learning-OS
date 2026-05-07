# 快速开始

本快速入门演示如何使用 LangGraph Graph API 或 Functional API 构建一个计算器智能体。

## 设置

安装依赖：

    pip install langchain_core langchain-anthropic langgraph

设置 API 密钥：

    export ANTHROPIC_API_KEY="your-api-key"

## 使用 Graph API

### 1. 定义工具和模型

    from langchain.tools import tool
    from langchain.chat_models import init_chat_model

    model = init_chat_model("claude-sonnet-4-6", temperature=0)

    @tool
    def multiply(a: int, b: int) -> int:
        """将 a 和 b 相乘。"""
        return a * b

    @tool
    def add(a: int, b: int) -> int:
        """将 a 和 b 相加。"""
        return a + b

    @tool
    def divide(a: int, b: int) -> float:
        """将 a 除以 b。"""
        return a / b

    tools = [add, multiply, divide]
    tools_by_name = {tool.name: tool for tool in tools}
    model_with_tools = model.bind_tools(tools)

### 2. 定义状态

    from langchain.messages import AnyMessage
    from typing_extensions import TypedDict, Annotated
    import operator

    class MessagesState(TypedDict):
        messages: Annotated[list[AnyMessage], operator.add]
        llm_calls: int

### 3. 定义模型节点

    def llm_call(state: dict):
        """LLM 决定是否调用工具"""
        return {
            "messages": [model_with_tools.invoke([...])],
            "llm_calls": state.get('llm_calls', 0) + 1
        }

### 4. 定义工具节点

    def tool_node(state: dict):
        """执行工具调用"""
        result = []
        for tool_call in state["messages"][-1].tool_calls:
            tool = tools_by_name[tool_call["name"]]
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
        return {"messages": result}

### 5. 定义结束逻辑

    def should_continue(state) -> Literal["tool_node", END]:
        if state["messages"][-1].tool_calls:
            return "tool_node"
        return END

### 6. 构建并编译智能体

    agent_builder = StateGraph(MessagesState)
    agent_builder.add_node("llm_call", llm_call)
    agent_builder.add_node("tool_node", tool_node)
    agent_builder.add_edge(START, "llm_call")
    agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
    agent_builder.add_edge("tool_node", "llm_call")
    agent = agent_builder.compile()

    messages = [HumanMessage(content="Add 3 and 4.")]
    messages = agent.invoke({"messages": messages})

## 使用 Functional API

Functional API 允许你用标准控制流逻辑编写智能体，无需显式定义节点和边：

    from langgraph.func import entrypoint, task

    @task
    def call_llm(messages):
        return model_with_tools.invoke([...])

    @task
    def call_tool(tool_call):
        tool = tools_by_name[tool_call["name"]]
        return tool.invoke(tool_call)

    @entrypoint()
    def agent(messages):
        model_response = call_llm(messages).result()
        while model_response.tool_calls:
            tool_results = [call_tool(tc).result() for tc in model_response.tool_calls]
            messages = add_messages(messages, [model_response, *tool_results])
            model_response = call_llm(messages).result()
        return add_messages(messages, model_response)
