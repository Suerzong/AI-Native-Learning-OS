[![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Hugging Face](</>)

  * [ 模型 ](</models>)
  * [ 数据集 ](</datasets>)
  * [ Spaces ](</spaces>)
  * [ Buckets 新功能](</storage>)
  * [ 文档 ](</docs>)
  * [ 企业版 ](</enterprise>)
  * [定价](</pricing>)
  *   * * * *

  * [登录](</login>)
  * [注册](</join>)

Agents 课程文档

什么是工具？

# Agents 课程

🏡 查看所有资源Agents 课程音频课程社区计算机视觉课程深度强化学习课程扩散模型课程LLM 课程MCP 课程3D 机器学习课程游戏机器学习课程开源 AI 食谱机器人课程a smol course

搜索文档

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. 欢迎来到课程

Live 1. 课程说明与答疑

Unit 1. Agent 基础介绍

[简介](</learn/agents-course/unit1/introduction>)[什么是 Agent？](</learn/agents-course/unit1/what-are-agents>)[快速测验 1](</learn/agents-course/unit1/quiz1>)[什么是 LLM？](</learn/agents-course/unit1/what-are-llms>)[消息与特殊标记](</learn/agents-course/unit1/messages-and-special-tokens>)[什么是工具？](</learn/agents-course/unit1/tools>)[快速测验 2](</learn/agents-course/unit1/quiz2>)[通过思考-行动-观察循环理解 AI Agent](</learn/agents-course/unit1/agent-steps-and-structure>)[思考：内部推理与 ReAct 方法](</learn/agents-course/unit1/thoughts>)[行动：让 Agent 与环境交互](</learn/agents-course/unit1/actions>)[观察：整合反馈以反思和适应](</learn/agents-course/unit1/observations>)[Dummy Agent 库](</learn/agents-course/unit1/dummy-agent-library>)[使用 smolagents 创建我们的第一个 Agent](</learn/agents-course/unit1/tutorial>)[Unit 1 最终测验](</learn/agents-course/unit1/final-quiz>)[总结](</learn/agents-course/unit1/conclusion>)

Unit 2. AI Agent 框架

Unit 2.1 smolagents 框架

Unit 2.2 LlamaIndex 框架

Unit 2.3 LangGraph 框架

Unit 3. Agentic RAG 应用案例

Unit 4. 最终项目 - 创建、测试并认证你的 Agent

Bonus Unit 1. 面向函数调用的 LLM 微调

Bonus Unit 2. Agent 可观测性与评估

Bonus Unit 3. 游戏中的 Agent（Pokemon）

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

加入 Hugging Face 社区

获取增强文档体验

在模型、数据集和 Spaces 上协作

通过加速推理获得更快的示例

切换文档主题

[注册](</join>)

开始使用

复制页面

# [](<#what-are-tools>) 什么是工具？

![Unit 1 规划](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/whiteboard-check-2.jpg)

AI Agent 的一个关键方面是它们的**行动**能力。正如我们所看到的，这是通过使用**工具（Tools）**来实现的。

在本节中，我们将学习什么是工具、如何有效地设计工具，以及如何通过系统消息（System Message）将它们集成到你的 Agent 中。

通过为你的 Agent 提供正确的工具，并清晰地描述这些工具的工作方式，你可以显著提升 AI 的能力。让我们开始吧！

## [](<#what-are-ai-tools>) 什么是 AI 工具？

**工具（Tool）是赋予 LLM 的一个函数**。这个函数应该实现一个**明确的目标**。

以下是一些 AI Agent 中常用的工具：

工具 | 描述
---|---
网络搜索 | 允许 Agent 从互联网获取最新信息。
图像生成 | 根据文本描述创建图像。
检索 | 从外部来源检索信息。
API 接口 | 与外部 API 交互（GitHub、YouTube、Spotify 等）。

这些只是示例，实际上你可以为任何用例创建工具！

一个好的工具应该是**补充 LLM 能力**的东西。

例如，如果你需要执行算术运算，给 LLM 提供一个**计算器工具**会比依赖模型的原生能力获得更好的结果。

此外，**LLM 基于其训练数据预测提示的补全**，这意味着它们的内部知识仅包括训练之前的事件。因此，如果你的 Agent 需要最新数据，你必须通过某种工具提供。

例如，如果你直接问 LLM（没有搜索工具）今天的天气，LLM 可能会随机幻觉出天气信息。

![天气](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/weather.jpg)

  * 一个工具应包含：

    * **函数功能的文本描述**。
    * 一个_可调用对象（Callable）_（用于执行操作）。
    * 带类型的_参数（Arguments）_。
    * （可选）带类型的输出。

## [](<#how-do-tools-work>) 工具是如何工作的？

正如我们所看到的，LLM 只能接收文本输入并生成文本输出。它们无法自行调用工具。当我们说向 Agent 提供工具时，我们的意思是让 LLM 了解这些工具的存在，并指示它在需要时生成基于文本的调用。

例如，如果我们提供一个从互联网检查某个地点天气的工具，然后询问 LLM 巴黎的天气，LLM 将识别这是一个使用"天气"工具的机会。LLM 不会自己检索天气数据，而是会生成表示工具调用的文本，例如 `call weather_tool('Paris')`。

然后，**Agent** 读取这个响应，识别出需要进行工具调用，代表 LLM 执行工具，并检索实际的天气数据。

工具调用步骤通常不会显示给用户：Agent 将它们作为新消息附加，然后将更新后的对话再次传递给 LLM。LLM 处理这个额外的上下文，并为用户生成听起来自然的响应。从用户的角度来看，看起来好像是 LLM 直接与工具交互了，但实际上，是 Agent 在后台处理了整个执行过程。

我们将在未来的课程中更多地讨论这个过程。

## [](<#how-do-we-give-tools-to-an-llm>) 我们如何给 LLM 提供工具？

完整的答案可能看起来很复杂，但我们本质上是使用系统提示（system prompt）来向模型提供可用工具的文本描述：

![工具的系统提示](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/Agent_system_prompt.png)

为了让这奏效，我们必须非常精确和准确地说明：

  1. **工具的功能**
  2. **它期望的确切输入**

这就是为什么工具描述通常使用富有表现力但精确的结构来提供，例如计算机语言或 JSON。并不是_必须_这样做，任何精确且连贯的格式都可以工作。

如果这看起来太理论化了，让我们通过一个具体例子来理解。

我们将实现一个简化的**计算器**工具，它只是将两个整数相乘。这是我们的 Python 实现：

Copied

    def calculator(a: int, b: int) -> int:
        """Multiply two integers."""
        return a * b

所以我们的工具叫做 `calculator`，它**将两个整数相乘**，需要以下输入：

  * **`a`** (_int_)：一个整数。
  * **`b`** (_int_)：一个整数。

工具的输出是另一个整数，我们可以这样描述：

  * (_int_)：`a` 和 `b` 的乘积。

所有这些细节都很重要。让我们将它们组合成一个文本字符串来向 LLM 描述我们的工具。

Copied

    Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int

> **提醒：**这个文本描述是_我们希望 LLM 了解的关于工具的信息_。

当我们将上述字符串作为 LLM 输入的一部分传递时，模型将把它识别为一个工具，并知道它需要传递什么输入以及期望什么输出。

如果我们想提供更多的工具，我们必须保持一致，始终使用相同的格式。这个过程可能是脆弱的，我们可能会不小心忽略一些细节。

有更好的方法吗？

### [](<#auto-formatting-tool-sections>) 自动格式化工具部分

我们的工具是用 Python 编写的，实现已经提供了我们需要的一切：

  * 描述性的名称：`calculator`
  * 更长的描述，由函数的 docstring 注释提供：`Multiply two integers.`
  * 输入及其类型：函数明确期望两个 `int`。
  * 输出的类型。

人们使用编程语言是有原因的：它们富有表现力、简洁且精确。

我们可以提供 Python 源代码作为工具的_规范_，但工具的实现方式并不重要。重要的是它的名称、功能、期望的输入和提供的输出。

我们将利用 Python 的内省（introspection）功能来利用源代码并自动构建工具描述。我们需要的只是工具实现使用类型提示（type hints）、文档字符串（docstrings）和合理的函数名。我们将编写一些代码来从源代码中提取相关部分。

完成后，我们只需要使用一个 Python 装饰器（decorator）来指示 `calculator` 函数是一个工具：

Copied

    @tool
    def calculator(a: int, b: int) -> int:
        """Multiply two integers."""
        return a * b

    print(calculator.to_string())

注意函数定义前的 `@tool` 装饰器。

通过我们接下来将看到的实现，我们将能够通过装饰器提供的 `to_string()` 函数从源代码自动检索以下文本：

Copied

    Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int

如你所见，这和我们之前手动写的一样！

### [](<#generic-tool-implementation>) 通用工具实现

我们创建一个通用的 `Tool` 类，可以在需要使用工具时复用。

> **免责声明：**此示例实现是虚构的，但与大多数库中的真实实现非常相似。

Copied

    from typing import Callable

    class Tool:
        """
        表示可复用代码片段（工具）的类。

        属性：
            name (str): 工具名称。
            description (str): 工具功能的文本描述。
            func (callable): 此工具包装的函数。
            arguments (list): 参数列表。
            outputs (str or list): 被包装函数的返回类型。
        """
        def __init__(self,
                     name: str,
                     description: str,
                     func: Callable,
                     arguments: list,
                     outputs: str):
            self.name = name
            self.description = description
            self.func = func
            self.arguments = arguments
            self.outputs = outputs

        def to_string(self) -> str:
            """
            返回工具的字符串表示，
            包括其名称、描述、参数和输出。
            """
            args_str = ", ".join([
                f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments
            ])

            return (
                f"Tool Name: {self.name},"
                f" Description: {self.description},"
                f" Arguments: {args_str},"
                f" Outputs: {self.outputs}"
            )

        def __call__(self, *args, **kwargs):
            """
            使用提供的参数调用底层函数（可调用对象）。
            """
            return self.func(*args, **kwargs)

这可能看起来很复杂，但如果我们慢慢分析，就能理解它的作用。我们定义了一个 **`Tool`** 类，包含：

  * **`name`** (_str_)：工具的名称。
  * **`description`** (_str_)：工具功能的简要描述。
  * **`function`** (_callable_)：工具执行的函数。
  * **`arguments`** (_list_)：期望的输入参数。
  * **`outputs`** (_str_ 或 _list_)：工具的期望输出。
  * **`__call__()`**：当工具实例被调用时调用该函数。
  * **`to_string()`**：将工具属性转换为文本表示。

我们可以使用以下代码通过此类创建一个工具：

Copied

    calculator_tool = Tool(
        "calculator",                   # 名称
        "Multiply two integers.",       # 描述
        calculator,                     # 要调用的函数
        [("a", "int"), ("b", "int")],   # 输入（名称和类型）
        "int",                          # 输出
    )

但我们也可以使用 Python 的 `inspect` 模块来为我们检索所有信息！这就是 `@tool` 装饰器的功能。

> 如果你感兴趣，可以展开以下部分查看装饰器实现。

装饰器代码

Copied

    import inspect

    def tool(func):
        """
        从给定函数创建 Tool 实例的装饰器。
        """
        # 获取函数签名
        signature = inspect.signature(func)

        # 提取输入的 (参数名, 参数注解) 对
        arguments = []
        for param in signature.parameters.values():
            annotation_name = (
                param.annotation.__name__
                if hasattr(param.annotation, '__name__')
                else str(param.annotation)
            )
            arguments.append((param.name, annotation_name))

        # 确定返回注解
        return_annotation = signature.return_annotation
        if return_annotation is inspect._empty:
            outputs = "No return annotation"
        else:
            outputs = (
                return_annotation.__name__
                if hasattr(return_annotation, '__name__')
                else str(return_annotation)
            )

        # 使用函数的 docstring 作为描述（如果为 None 则使用默认值）
        description = func.__doc__ or "No description provided."

        # 函数名成为工具名称
        name = func.__name__

        # 返回新的 Tool 实例
        return Tool(
            name=name,
            description=description,
            func=func,
            arguments=arguments,
            outputs=outputs
        )

再次强调，有了这个装饰器，我们可以这样实现我们的工具：

Copied

    @tool
    def calculator(a: int, b: int) -> int:
        """Multiply two integers."""
        return a * b

    print(calculator.to_string())

然后我们可以使用 `Tool` 的 `to_string` 方法自动获取适合用作 LLM 工具描述的文本：

Copied

    Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int

描述被**注入**到系统提示中。以本节开头的例子为例，替换 `tools_description` 后的系统提示如下：

![工具的系统提示](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/Agent_system_prompt_tools.png)

在[行动](<actions>)部分，我们将了解更多关于 Agent 如何**调用**我们刚刚创建的工具。

### [](<#model-context-protocol-mcp-a-unified-tool-interface>) 模型上下文协议（MCP）：统一的工具接口

模型上下文协议（MCP）是一个**开放协议**，它标准化了应用程序**向 LLM 提供工具的方式**。MCP 提供：

  * 一个不断增长的预构建集成列表，你的 LLM 可以直接使用
  * 在 LLM 提供商和供应商之间切换的灵活性
  * 在你的基础设施内保护数据的最佳实践

这意味着**任何实现 MCP 的框架都可以利用协议中定义的工具**，无需为每个框架重新实现相同的工具接口。

如果你想更深入了解 MCP，可以查看我们的[免费 MCP 课程](<https://huggingface.co/learn/mcp-course/>)。

* * *

工具在增强 AI Agent 能力方面发挥着至关重要的作用。

总结一下，我们学习了：

  * _什么是工具_：赋予 LLM 额外能力的函数，例如执行计算或访问外部数据。

  * _如何定义工具_：通过提供清晰的文本描述、输入、输出和可调用函数。

  * _为什么工具至关重要_：它们使 Agent 能够克服静态模型训练的限制，处理实时任务并执行专业操作。

现在，我们可以继续学习 [Agent 工作流程](<agent-steps-and-structure>)，在那里你将看到 Agent 如何观察、思考和行动。这**将我们目前涵盖的所有内容整合在一起**，为你创建自己的功能齐全的 AI Agent 奠定基础。

但首先，是时候进行另一个简短的测验了！

[ 在 GitHub 上更新](<https://github.com/huggingface/agents-course/blob/main/units/en/unit1/tools.mdx>)

[←消息与特殊标记](</learn/agents-course/unit1/messages-and-special-tokens>) [快速测验 2→](</learn/agents-course/unit1/quiz2>)

[什么是工具？](<#what-are-tools>)[什么是 AI 工具？](<#what-are-ai-tools>)[工具是如何工作的？](<#how-do-tools-work>)[我们如何给 LLM 提供工具？](<#how-do-we-give-tools-to-an-llm>)[自动格式化工具部分](<#auto-formatting-tool-sections>)[通用工具实现](<#generic-tool-implementation>)[模型上下文协议（MCP）：统一的工具接口](<#model-context-protocol-mcp-a-unified-tool-interface>)
