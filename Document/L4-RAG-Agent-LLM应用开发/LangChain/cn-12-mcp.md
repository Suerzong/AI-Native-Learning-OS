# 模型上下文协议（MCP）

模型上下文协议（Model Context Protocol, MCP）是一个开放协议，标准化了应用程序如何向 LLM 提供上下文。MCP 为 AI 模型与外部工具和数据源的交互提供了统一的接口。

## 什么是 MCP？

MCP 是一个客户端-服务器架构，允许 AI 应用程序连接到各种数据源和工具。它类似于 USB-C 接口——为 AI 模型提供了一种标准方式来连接外部系统。

MCP 的核心组件：

  * **MCP 服务器（Server）**——提供工具和数据源的服务器
  * **MCP 客户端（Client）**——连接到 MCP 服务器的 AI 应用程序
  * **工具（Tools）**——模型可以调用的函数
  * **资源（Resources）**——模型可以访问的数据
  * **提示（Prompts）**——预定义的提示模板

## 在 LangChain 中使用 MCP

LangChain 支持将 MCP 服务器作为工具集成到智能体中。这允许智能体使用 MCP 生态系统中的任何工具服务器。

### 连接 MCP 服务器

LangChain 提供了 MCP 集成，允许你将 MCP 服务器的工具暴露给智能体：

    from langchain_mcp import MCPToolkit

    # 连接到 MCP 服务器
    toolkit = MCPToolkit(server_command=["npx", "-y", "@modelcontextprotocol/server-filesystem"])

    # 获取工具
    tools = toolkit.get_tools()

    # 在智能体中使用
    agent = create_agent(model="gpt-5.4", tools=tools)

### MCP 的优势

  * **标准化**——统一的工具和数据访问接口
  * **可组合**——可以连接多个 MCP 服务器
  * **生态系统**——丰富的预构建 MCP 服务器可用
  * **安全性**——细粒度的权限控制

## MCP 资源

  * [MCP 官方文档](https://modelcontextprotocol.io/)
  * [MCP GitHub 仓库](https://github.com/modelcontextprotocol)
  * [MCP 服务器列表](https://github.com/modelcontextprotocol/servers)
