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
  * 概述
本页内容

# MLflow：面向 LLM 和智能体的 AI 工程平台

MLflow 是最大的开源**[面向智能体和 LLM 的 AI 工程平台](https://mlflow.org/genai)**。MLflow 使各种规模的团队都能够调试、评估、[监控](https://mlflow.org/ai-monitoring)和优化生产级 AI 应用，同时控制成本并管理对模型和数据的访问。凭借每月超过 3000 万次下载，数千个组织每天依赖 MLflow 将 AI 信心十足地部署到生产环境。MLflow 面向智能体和 LLM 应用的全面功能集包括生产级[可观测性](/docs/latest/genai/tracing/)、[评估](/docs/latest/genai/eval-monitor/)、[提示词管理](/docs/latest/genai/prompt-registry/)、用于管理成本和模型访问的 [AI 网关](https://mlflow.org/ai-gateway)等。

#### 开源（Open Source）

加入数千个使用 MLflow 构建智能体和 LLM 应用的团队——拥有 20K+ GitHub Stars 和 5000 万+ 月下载量。作为 Linux 基金会的一部分，MLflow 确保你的 AI 基础设施保持开放且供应商中立。

#### OpenTelemetry 兼容

MLflow Tracing（追踪）完全兼容 OpenTelemetry，原生支持 GenAI 语义约定（Semantic Conventions），避免供应商锁定，并可轻松与现有可观测性技术栈集成。

#### 一体化平台

管理从原型到生产的完整 AI 开发流程。在一个平台上追踪提示词、评估质量、部署 AI 智能体并监控性能。

#### 完整可观测性

通过全面的追踪深入了解每一次 AI 决策，捕获提示词、检索、工具调用和 LLM 响用。自信地调试复杂的工作流。

#### 评估与监控

使用 LLM 评判器（LLM-as-a-Judge）和自定义指标取代手动测试。系统化地评估每一次变更，确保 AI 应用的持续改进。

#### 框架集成

使用任何智能体框架或 LLM 提供商。凭借 100+ 集成和可扩展 API，MLflow 适配你的技术栈，而非相反。

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

## 可观测性

使用 MLflow 的[追踪](https://mlflow.org/llm-tracing)功能调试和迭代智能体及 LLM 应用，它捕获应用的完整执行过程，包括提示词、检索和工具调用。MLflow 的开源、OpenTelemetry 兼容的追踪 SDK 有助于避免供应商锁定。[可观测性快速入门 →

* * *

本快速入门将引导你在智能体中启用追踪并发送第一个追踪到 MLflow。](/docs/latest/genai/tracing/quickstart/)

## 评估

通过利用 [LLM-as-a-Judge](https://mlflow.org/llm-evaluation) 指标来准确测量自由格式语言，模拟人类专业知识以评估和提升智能体质量。使用预构建的评判器处理常见指标（如幻觉或相关性），或开发适合你业务需求和专家洞察的自定义评判器。[评估快速入门 →

* * *

本快速入门将引导你准备数据集、配置评分器（Scorer），并在几个步骤内运行你的第一次评估。](/docs/latest/genai/eval-monitor/quickstart/)

## 提示词管理与优化

通过 MLflow UI 直接对提示词模板进行版本管理、比较、迭代和发现。在智能体或应用代码的多个版本中复用提示词，并查看详细的血缘关系，了解哪些版本正在使用每个提示词。使用[自动提示词优化](https://mlflow.org/prompt-optimization)加速开发，它通过数据驱动的算法改进提示词，无需手动反复试验。[提示词管理快速入门 →

* * *

本快速入门将引导你为智能体或 LLM 应用创建、编辑和版本化提示词。](/docs/latest/genai/prompt-registry/create-and-edit-prompts/)

* * *

## 在任何环境中运行

MLflow 可在多种环境中使用，包括本地环境、本地集群、云平台和托管服务。作为开源平台，MLflow 是**供应商中立**的；无论你是在构建 AI 智能体、LLM 应用还是 ML 模型，你都可以使用 MLflow 的核心能力——追踪、评估、实验追踪、部署等。

## 向 AI 咨询 MLflow 相关问题

## 社区

与其他构建者交流、提问并获取最新动态——加入我们在 Slack、GitHub、LinkedIn 等平台的活跃 MLflow 社区！了解如何参与并在[社区页面](/docs/latest/community/)发现我们的所有渠道。[下一篇实时演示](/docs/latest/genai/demo/)

  * 可观测性
  * 评估
  * 提示词管理与优化
  * 在任何环境中运行
  * 向 AI 咨询 MLflow 相关问题
  * 社区
