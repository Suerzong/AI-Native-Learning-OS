跳转到主要内容 [](/docs/latest/)LLM 与智能体

  * [LLM 与智能体](/docs/latest/genai/)
  * [机器学习](/docs/latest/ml/)
[API 参考](https://mlflow.org/docs/latest/api_reference/index.html)[自托管](/docs/latest/self-hosting/)[社区](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)搜索

  * [概述](/docs/latest/genai/)
  * [实时演示](/docs/latest/genai/demo/)
  * **快速入门**
  * [ 设置 MLflow 服务器](/docs/latest/genai/getting-started/connect-environment/)
  * [开始追踪（Tracing）](/docs/latest/genai/tracing/quickstart/)
  * [评估 LLM 和智能体](/docs/latest/genai/eval-monitor/quickstart/)
  * [试用 MLflow AI 助手](/docs/latest/genai/getting-started/try-assistant/)
  * [自动问题检测](/docs/latest/genai/eval-monitor/ai-insights/detect-issues/)
  * **核心组件**
  * [ 追踪（可观测性）](/docs/latest/genai/tracing/)
  * [评估与监控](/docs/latest/genai/eval-monitor/)
    * [快速入门](/docs/latest/genai/eval-monitor/quickstart/)
    * [自动问题检测](/docs/latest/genai/eval-monitor/ai-insights/detect-issues/)
    * [运行评估](/docs/latest/genai/eval-monitor/running-evaluation/eval-examples/)
    * [自动评估](/docs/latest/genai/eval-monitor/automatic-evaluations/)
    * [评判器与评分器](/docs/latest/genai/eval-monitor/scorers/)
    * [评估数据集](/docs/latest/genai/datasets/)
    * [标注](/docs/latest/genai/assessments/feedback/)
    * [AI 洞察](/docs/latest/genai/eval-monitor/ai-insights/ai-issue-discovery/)
    * [从 MLflow 2 LLM 评估迁移](/docs/latest/genai/eval-monitor/legacy-llm-evaluation/)
    * [常见问题](/docs/latest/genai/eval-monitor/faq/)
  * [提示词管理与优化](/docs/latest/genai/prompt-registry/)
  * [AI 网关](/docs/latest/genai/governance/ai-gateway/)
  * **更多功能**
  * [ 版本追踪](/docs/latest/genai/version-tracking/)
  * [打包与部署](/docs/latest/genai/flavors/)
  * [MCP](/docs/latest/genai/mcp/)
  * [智能体服务](/docs/latest/genai/serving/agent-server/)
  * **参考**
  * [ 概念](/docs/latest/genai/concepts/trace/)
  * [功能请求](/docs/latest/genai/references/request-features/)
  * [托管 MLflow](/docs/latest/genai/getting-started/databricks-trial/)

  * [](/docs/latest/)
  * 评估与监控
本页内容

# 使用 MLflow 评估 LLM 和智能体

MLflow 的评估和监控能力帮助你系统化地衡量、改进和维护 LLM 应用和 AI 智能体在整个生命周期（从开发到生产）中的质量。

**试用 MLflow LLM 与智能体演示**

了解 MLflow 在 LLM 和 AI 智能体方面应用的最快方式是试用演示。**点击启动演示 ↓**

#### **公开演示**

访问 **[demo.mlflow.org](https://demo.mlflow.org/#/experiments/1/overview)** 探索预加载了示例数据的公开托管 MLflow 实例。

#### **从 UI 启动**

要启动演示，点击 MLflow UI 顶部页面的 "Start Demo" 按钮。

#### **从 CLI 启动**

或者，你可以使用 `mlflow demo` 命令从命令行启动演示。此选项不需要你运行 MLflow 服务器。

```bash
uvx mlflow demo
```

MLflow 评估能力的一个核心理念是**评估驱动开发（Evaluation-Driven Development）**。这是一种新兴实践，用于应对构建高质量 LLM/智能体应用的挑战。MLflow 是一个开源 AI 工程平台，旨在支持这种实践，帮助你快速构建生产级 AI 智能体和 LLM 应用。

## 核心能力

  * 数据集管理
  * 人工反馈
  * LLM-as-a-Judge（LLM 评判器）
  * 系统化评估
  * 生产监控

#### 创建和维护高质量数据集

在评估 LLM 应用或 AI 智能体之前，你需要测试数据。**评估数据集（Evaluation Datasets）**提供了一个集中化的仓库，用于大规模管理测试用例、真实标签（ground truth）和评估数据。将评估数据集视为你的"测试数据库"——评估 AI 系统所需的所有数据的单一事实来源。它们将临时测试转化为系统化的质量保障。[了解更多 →](/docs/latest/genai/datasets/)

#### 追踪标注和人工反馈

人工反馈对于构建满足用户期望的高质量 LLM 应用和 AI 智能体至关重要。MLflow 支持收集、管理和利用来自终端用户和领域专家的反馈。反馈会附加到追踪记录上并记录元数据，包括用户、时间戳、修订记录等。[了解更多 →](/docs/latest/genai/assessments/feedback/)

#### 通过自动化扩展质量评估

质量评估是构建高质量 LLM 应用和 AI 智能体的关键环节，但它通常耗时且需要人类专业知识。LLM 是自动化质量评估的强大工具。MLflow 提供多种内置的 [LLM-as-a-Judge](https://mlflow.org/llm-evaluation) 评分器来帮助自动化这一过程，以及一套灵活的工具集，让你轻松构建自己的 LLM 评判器。[了解更多 →](/docs/latest/genai/eval-monitor/)

#### 评估和提升质量

系统化地评估和改进 LLM 应用和 AI 智能体的质量是一项挑战。MLflow 提供了一套全面的工具来帮助你评估和提升应用质量。作为业界最受信赖的面向智能体和 LLM 应用的开源 [AI 工程平台](https://mlflow.org/genai)，MLflow 为追踪评估结果和团队高效协作提供了坚实基础。[了解更多 →](/docs/latest/genai/eval-monitor/quickstart/)

#### 在生产环境中监控应用

理解和优化 LLM 应用及 AI 智能体的性能对于高效运营至关重要。[MLflow Tracing（追踪）](https://mlflow.org/llm-tracing)捕获每个步骤的关键指标（如延迟和 token 使用量）以及各种质量指标，帮助你识别瓶颈、监控效率并发现优化机会。[了解更多 →](/docs/latest/genai/tracing/prod-tracing/)

## 运行评估

每次评估由三个组件定义：

| 组件 | 示例 |
|------|------|
| **数据集（Dataset）** —— 输入和期望值（可选包含预生成的输出和追踪） | `[{"inputs": {"question": "2+2"}, "expectations": {"answer": "4"}},{"inputs": {"question": "2+3"}, "expectations": {"answer": "5"}}]` |
| **评分器（Scorer）** —— 评估标准 | `@scorer`<br>`def exact_match(expectations, outputs):`<br>`    return expectations == outputs` |
| **预测函数（Predict Function）** —— 为数据集生成输出 | `def predict_fn(question: str) -> str:`<br>`    response = client.chat.completions.create(`<br>`        model="gpt-4o-mini",`<br>`        messages=[{"role": "user", "content": question}]`<br>`    )`<br>`    return response.choices[0].message.content` |

以下示例展示了一个简单的问答数据集评估：

```python
import os
import openai
import mlflow
from mlflow.genai.scorers import Correctness, Guidelines

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. 定义一个简单的问答数据集
dataset = [
    {
        "inputs": {"question": "Can MLflow manage prompts?"},
        "expectations": {"expected_response": "Yes!"},
    },
    {
        "inputs": {"question": "Can MLflow create a taco for my lunch?"},
        "expectations": {"expected_response": "No, unfortunately, MLflow is not a taco maker."},
    },
]


# 2. 定义预测函数以生成响应
def predict_fn(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content


# 3. 运行评估
results = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=predict_fn,
    scorers=[
        # 内置 LLM 评判器
        Correctness(),
        # 使用 LLM 评判器的自定义标准
        Guidelines(name="is_english", guidelines="The answer must be in English"),
    ],
)
```

## 查看结果

打开 MLflow UI 查看评估结果。你可以使用以下命令启动 UI：

```bash
mlflow server --port 5000
```

你会看到在 "Runs" 标签下创建了一个新的评估运行。点击运行名称查看评估结果。

## 下一步

### [快速入门在实践中学习 MLflow 的评估工作流。开始评估 →](/docs/latest/genai/eval-monitor/quickstart/)### [评估智能体使用专门的技术和自定义评分器评估 AI 智能体。评估智能体 →](/docs/latest/genai/eval-monitor/running-evaluation/agents/)### [构建评分器开始使用 MLflow 强大的评分器来评估质量。了解评分器 →](/docs/latest/genai/eval-monitor/scorers/)[上一篇常见问题](/docs/latest/genai/tracing/faq/)[下一篇快速入门](/docs/latest/genai/eval-monitor/quickstart/)

  * 核心能力
  * 运行评估
  * 查看结果
  * 下一步
