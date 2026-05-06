Skip to main content[](/docs/latest/)LLMs & Agents

  * [LLMs & Agents](/docs/latest/genai/)
  * [Machine Learning](/docs/latest/ml/)
[API Reference](https://mlflow.org/docs/latest/api_reference/index.html)[Self-Hosting](/docs/latest/self-hosting/)[Community](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)Search

  * [Overview](/docs/latest/genai/)
  * [Live Demo](/docs/latest/genai/demo/)
  * **Getting Started**
  * [ Set Up MLflow Server](/docs/latest/genai/getting-started/connect-environment/)
  * [Start Tracing](/docs/latest/genai/tracing/quickstart/)
  * [Evaluate LLMs and Agents](/docs/latest/genai/eval-monitor/quickstart/)
  * [Try MLflow's AI Assistant](/docs/latest/genai/getting-started/try-assistant/)
  * [Automatic Issue Detection](/docs/latest/genai/eval-monitor/ai-insights/detect-issues/)
  * **Core Components**
  * [ Tracing (Observability)](/docs/latest/genai/tracing/)
  * [Evaluation & Monitoring](/docs/latest/genai/eval-monitor/)
  * [Prompt Management & Optimization](/docs/latest/genai/prompt-registry/)
  * [AI Gateway](/docs/latest/genai/governance/ai-gateway/)
  * **More Features**
  * [ Version Tracking](/docs/latest/genai/version-tracking/)
  * [Packaging & Deployment](/docs/latest/genai/flavors/)
  * [MCP](/docs/latest/genai/mcp/)
  * [Agent Serving](/docs/latest/genai/serving/agent-server/)
  * **References**
  * [ Concepts](/docs/latest/genai/concepts/trace/)
  * [Request Features](/docs/latest/genai/references/request-features/)
  * [Managed MLflow](/docs/latest/genai/getting-started/databricks-trial/)

  * [](/docs/latest/)
  * Overview
On this page

# MLflow: AI Engineering Platform for LLMs and Agents

MLflow is the largest open source **[AI engineering platform for agents and LLMs](https://mlflow.org/genai)**. MLflow enables teams of all sizes to debug, evaluate, [monitor](https://mlflow.org/ai-monitoring), and optimize production-quality AI applications, while controlling costs and managing access to models and data. With over 30 million monthly downloads, thousands of organizations rely on MLflow each day to ship AI to production with confidence. MLflow's comprehensive feature set for agents and LLM applications includes production-grade [observability](/docs/latest/genai/tracing/), [evaluation](/docs/latest/genai/eval-monitor/), [prompt management](/docs/latest/genai/prompt-registry/), an [AI Gateway](https://mlflow.org/ai-gateway) for managing costs and model access, and much more.

#### Open Source

Join thousands of teams building agents and LLM applications with MLflow - with 20K+ GitHub Stars and 50M+ monthly downloads. As part of the Linux Foundation, MLflow ensures your AI infrastructure remains open and vendor-neutral.

#### OpenTelemetry

MLflow Tracing is fully compatible with OpenTelemetry with native support for GenAI Semantic Conventions, making it free from vendor lock-in and easy to integrate with your existing observability stack.

#### All-in-one Platform

Manage the complete AI development journey from prototype to production. Track prompts, evaluate quality, deploy AI agents, and monitor performance in one platform.

#### Complete Observability

See inside every AI decision with comprehensive tracing that captures prompts, retrievals, tool calls, and LLM responses. Debug complex workflows with confidence.

#### Evaluation & Monitoring

Stop manual testing with LLM judges and custom metrics. Systematically evaluate every change to ensure consistent improvements in your AI applications.

#### Framework Integration

Use any agent framework or LLM provider. With 100+ integrations and extensible APIs, MLflow adapts to your tech stack, not the other way around.   
**Try the MLflow LLMs and Agents Demo**  
The quickest way to learn about MLflow for LLMs and AI Agents is to try the demo. **Click to launch the demo ↓**

#### **Public Demo**​

Visit **[demo.mlflow.org](https://demo.mlflow.org/#/experiments/1/overview)** to explore a publicly hosted MLflow instance pre-loaded with sample data.

#### **Starting from UI**​

To start the demo, click on the "Start Demo" button on the top page of the MLflow UI.

#### **Starting from CLI**​

Alternatively, you can start the demo from the command line using the `mlflow demo` command. This option does not require you to have a running MLflow server.bash
    
    
    uvx mlflow demo  
    

## Observability​

Debug and iterate on agents and LLM applications using MLflow's [tracing](https://mlflow.org/llm-tracing), which captures your app's entire execution, including prompts, retrievals and tool calls. MLflow's open-source, OpenTelemetry-compatible tracing SDK helps avoid vendor lock-in. [Observability Quickstart →

* * *

This quickstart will guide you through enabling tracing in your agent and sending your first trace to MLflow.](/docs/latest/genai/tracing/quickstart/)

## Evaluations​

Accurately measure free-form language with LLM judges by utilizing [LLM-as-a-judge](https://mlflow.org/llm-evaluation) metrics, mimicking human expertise, to assess and enhance agent quality. Access pre-built judges for common metrics like hallucination or relevance, or develop custom judges tailored to your business needs and expert insights. [Evaluations Quickstart →

* * *

This quickstart will walk you through preparing a dataset, configuring a scorer, and running your first evaluation in just a few steps.](/docs/latest/genai/eval-monitor/quickstart/)

## Prompt Management & Optimization​

Version, compare, iterate on, and discover prompt templates directly through the MLflow UI. Reuse prompts across multiple versions of your agent or application code, and view rich lineage identifying which versions are using each prompt. Accelerate development with [automated prompt optimization](https://mlflow.org/prompt-optimization) that uses data-driven algorithms to improve your prompts without manual trial-and-error. [Prompt Management Quickstart →

* * *

This quickstart will guide you through creating, editing and versioning prompts for your agent or LLM application.](/docs/latest/genai/prompt-registry/create-and-edit-prompts/)

* * *

## Running Anywhere​

MLflow can be used in a variety of environments, including your local environment, on-premises clusters, cloud platforms, and managed services. Being an open-source platform, MLflow is **vendor-neutral** ; whether you're building AI agents, LLM applications, or ML models, you have access to MLflow's core capabilities — tracing, evaluation, experiment tracking, deployment, and more. [](https://docs.databricks.com/aws/en/mlflow3/genai/)[](https://aws.amazon.com/sagemaker-ai/experiments/)[](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow?view=azureml-api-2)[](https://nebius.com/services/managed-mlflow)[](/docs/latest/ml/tracking/)

## Ask AI About MLflow​

## Community​

Connect with fellow builders, ask questions, and stay up to date — join our vibrant MLflow community on Slack, GitHub, LinkedIn, and more! Learn how to get involved and discover all our channels on the [Community Page](/docs/latest/community/).[NextLive Demo](/docs/latest/genai/demo/)

  * Observability
  * Evaluations
  * Prompt Management & Optimization
  * Running Anywhere
  * Ask AI About MLflow
  * Community
© 2025 MLflow Project, a Series of LF Projects, LLC.[Components](https://mlflow.org)[Releases](https://mlflow.org/releases)[Blog](https://mlflow.org/blog)[Docs](/docs/latest/)[Ambassador Program](https://mlflow.org/ambassadors)
