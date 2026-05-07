# 消息（Messages）

消息是 LangChain 中模型上下文的基本单元。它们表示模型的输入和输出，承载与 LLM 交互时所需的内容和元数据。消息对象包含：

  * **角色（Role）**——标识消息类型（如 `system`、`user`）
  * **内容（Content）**——表示消息的实际内容（如文本、图像、音频、文档等）
  * **元数据（Metadata）**——可选字段，如响应信息、消息 ID 和 token 使用量

LangChain 提供跨所有模型提供商工作的标准消息类型。

## 基本用法

    from langchain.messages import HumanMessage, AIMessage, SystemMessage

    system_msg = SystemMessage("You are a helpful assistant.")
    human_msg = HumanMessage("Hello, how are you?")
    messages = [system_msg, human_msg]
    response = model.invoke(messages)  # 返回 AIMessage

也可以使用字典格式（OpenAI 聊天补全格式）：

    messages = [
        {"role": "system", "content": "You are a poetry expert"},
        {"role": "user", "content": "Write a haiku about spring"},
    ]

## 消息类型

### 系统消息（System Message）

`SystemMessage` 表示初始指令集，引导模型的行为。可以设置语气、定义模型角色和建立响应指南。

### 人消息（Human Message）

`HumanMessage` 表示用户输入和交互。可以包含文本、图像、音频、文件等多种模态内容。

### AI 消息（AI Message）

`AIMessage` 表示模型调用的输出。可以包含多模态数据、工具调用和提供商特定元数据。

关键属性：
  * `text`——消息的文本内容
  * `content_blocks`——标准化的内容块
  * `tool_calls`——模型做出的工具调用
  * `id`——消息的唯一标识符
  * `usage_metadata`——token 使用量元数据

### 工具消息（Tool Message）

`ToolMessage` 用于将单个工具执行的结果传递回模型。

    tool_message = ToolMessage(
        content=weather_result,
        tool_call_id="call_123"  # 必须匹配调用 ID
    )

`artifact` 字段存储补充数据，不会发送给模型，但可以通过编程方式访问。

## 消息内容

消息的 `content` 属性支持：
  1. 字符串
  2. 提供商原生格式的内容块列表
  3. LangChain 标准内容块列表

LangChain 提供标准内容块类型，跨提供商工作：
  * `TextContentBlock`——标准文本输出
  * `ReasoningContentBlock`——模型推理步骤
  * `ImageContentBlock`——图像数据
  * `AudioContentBlock`——音频数据
  * `VideoContentBlock`——视频数据
  * `FileContentBlock`——通用文件（PDF 等）
  * `ToolCall`——函数调用
  * `ServerToolCall`/`ServerToolResult`——服务端工具执行
  * `NonStandardContentBlock`——提供商特定的逃生舱

## 多模态（Multimodal）

LangChat 聊天模型可以接受多模态数据作为输入并生成多模态数据作为输出：

    # 图像输入
    message = {
        "role": "user",
        "content": [
            {"type": "text", "text": "描述此图像的内容。"},
            {"type": "image", "url": "https://example.com/image.jpg"},
        ]
    }

支持图像、PDF 文档、音频和视频输入。并非所有模型支持所有文件类型。
