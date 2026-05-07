# 结构化输出（Structured Output）

结构化输出允许你要求模型以特定格式返回响应，这对于确保输出可以被轻松解析和在后续处理中使用非常有用。

## 基本用法

使用 `with_structured_output` 方法让模型返回结构化数据：

    from pydantic import BaseModel, Field

    class Movie(BaseModel):
        """电影详情。"""
        title: str = Field(description="电影标题")
        year: int = Field(description="上映年份")
        director: str = Field(description="导演")
        rating: float = Field(description="评分（满分 10 分）")

    model_with_structure = model.with_structured_output(Movie)
    response = model_with_structure.invoke("Provide details about the movie Inception")
    print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)

## 支持的模式类型

  * **Pydantic**：提供最丰富的功能集，包括字段验证、描述和嵌套结构
  * **TypedDict**：Pydantic 的简单替代方案，不需要运行时验证
  * **JSON Schema**：提供最大控制和互操作性

## 智能体中的结构化输出

通过 `response_format` 参数让智能体以特定格式返回输出：

    from langchain.agents import create_agent
    from langchain.agents.structured_output import ToolStrategy

    class ContactInfo(BaseModel):
        name: str
        email: str
        phone: str

    agent = create_agent(
        model="gpt-5.4-mini",
        tools=[search_tool],
        response_format=ToolStrategy(ContactInfo)
    )

    result = agent.invoke({
        "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com"}]
    })
    result["structured_response"]  # ContactInfo(name='John Doe', ...)

## 输出策略

  * `ToolStrategy`：使用人工工具调用生成结构化输出，适用于任何支持工具调用的模型
  * `ProviderStrategy`：使用模型提供商的原生结构化输出生成，更可靠但仅适用于支持的提供商

## 高级选项

  * `include_raw=True`：同时获取解析后的输出和原始 AI 消息
  * 嵌套结构：模式可以嵌套
  * 验证：Pydantic 模型提供自动验证
