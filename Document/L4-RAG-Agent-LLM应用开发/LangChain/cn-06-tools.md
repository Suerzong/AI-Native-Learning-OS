# 工具（Tools）

工具扩展了[智能体](https://docs.langchain.com/oss/python/langchain/agents)的能力——让它们可以获取实时数据、执行代码、查询外部数据库并在世界上执行操作。工具本质上是具有明确定义的输入和输出的可调用函数，传递给[聊天模型](https://docs.langchain.com/oss/python/langchain/models)。模型根据对话上下文决定何时调用工具以及提供什么输入参数。

## 创建工具

### 基本定义

创建工具最简单的方式是使用 `@tool` 装饰器。函数的文档字符串默认成为工具的描述：

    from langchain.tools import tool

    @tool
    def search_database(query: str, limit: int = 10) -> str:
        """搜索客户数据库中匹配查询的记录。"""
        return f"Found {limit} results for '{query}'"

类型提示是**必需的**，因为它们定义了工具的输入模式。

### 自定义工具属性

**自定义名称**：

    @tool("web_search")
    def search(query: str) -> str:
        """搜索网页获取信息。"""
        return f"Results for: {query}"

**自定义描述**：

    @tool("calculator", description="执行算术计算。用于任何数学问题。")
    def calc(expression: str) -> str:
        return str(eval(expression))

### 高级模式定义

使用 Pydantic 模型或 JSON Schema 定义复杂输入：

    from pydantic import BaseModel, Field

    class WeatherInput(BaseModel):
        location: str = Field(description="城市名称或坐标")
        units: str = Field(default="celsius", description="温度单位偏好")

    @tool(args_schema=WeatherInput)
    def get_weather(location: str, units: str = "celsius") -> str:
        """获取当前天气。"""
        return f"Weather in {location}: 22 degrees"

### 保留参数名

以下参数名是保留的，不能用作工具参数：
  * `config`——用于内部传递 `RunnableConfig`
  * `runtime`——用于 `ToolRuntime` 参数（访问状态、上下文、存储）

## 访问上下文

工具可以通过 `ToolRuntime` 参数访问运行时信息：

| 组件 | 说明 |
|------|------|
| **State** | 短期记忆——当前对话中存在的可变数据 |
| **Context** | 不可变配置——调用时传递的用户 ID、会话信息等 |
| **Store** | 长期记忆——跨对话持久保存的数据 |
| **Stream Writer** | 在工具执行期间发出实时更新 |
| **Execution Info** | 当前执行的线程 ID、运行 ID、重试信息 |
| **Config** | 执行的 `RunnableConfig` |

### 短期记忆（State）

    @tool
    def get_last_user_message(runtime: ToolRuntime) -> str:
        """获取用户最近的消息。"""
        messages = runtime.state["messages"]
        for message in reversed(messages):
            if isinstance(message, HumanMessage):
                return message.content
        return "No user messages found"

### 更新状态

使用 `Command` 更新智能体状态：

    @tool
    def set_user_name(new_name: str, runtime: ToolRuntime) -> Command:
        """设置用户名。"""
        return Command(update={"user_name": new_name, "messages": [...]})

### 上下文（Context）

    @tool
    def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
        """获取当前用户的账户信息。"""
        user_id = runtime.context.user_id
        return f"User: {user_id}"

### 长期记忆（Store）

    @tool
    def save_user_info(user_id: str, info: dict, runtime: ToolRuntime) -> str:
        """保存用户信息。"""
        runtime.store.put(("users",), user_id, info)
        return "Saved."

## 工具返回值

  * **返回字符串**——用于人类可读的结果
  * **返回对象**——用于模型应解析的结构化数据
  * **返回 Command**——需要写入状态时使用

## ToolNode

`ToolNode` 是 LangGraph 工作流中执行工具的预构建节点。它自动处理并行工具执行、错误处理和状态注入。

## 预构建工具

LangChain 提供大量预构建工具和工具包，用于网页搜索、代码解释、数据库访问等常见任务。

## 服务端工具使用

某些聊天模型具有内置工具（网页搜索、代码解释器），由模型提供商在服务端执行。
