跳转到主要内容 [](/docs/latest/)机器学习

  * [LLM 与智能体](/docs/latest/genai/)
  * [机器学习](/docs/latest/ml/)
[API 参考](https://mlflow.org/docs/latest/api_reference/index.html)[自托管](/docs/latest/self-hosting/)[社区](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)搜索

  * [概述](/docs/latest/ml/)
  * [快速入门](/docs/latest/ml/getting-started/)
  * [机器学习](/docs/latest/ml/traditional-ml/)
    * [传统机器学习](/docs/latest/ml/traditional-ml/)
    * [深度学习](/docs/latest/ml/deep-learning/)
  * [构建](/docs/latest/ml/tracking/)
    * [MLflow Tracking（实验追踪）](/docs/latest/ml/tracking/)
    * [MLflow Model（模型）](/docs/latest/ml/model/)
    * [MLflow Datasets（数据集）](/docs/latest/ml/dataset/)
  * [评估](/docs/latest/ml/evaluation/)
  * [部署](/docs/latest/ml/model-registry/)
    * [MLflow Model Registry（模型注册表）](/docs/latest/ml/model-registry/)
    * [MLflow Serving（模型服务）](/docs/latest/ml/deployment/)
      * [将 MLflow 模型部署为本地推理服务器](/docs/latest/ml/deployment/deploy-model-locally/)
      * [将 MLflow 模型部署到 Kubernetes](/docs/latest/ml/deployment/deploy-model-to-kubernetes/)
      * [将 MLflow 模型部署到 Amazon SageMaker](/docs/latest/ml/deployment/deploy-model-to-sagemaker/)
      * [将 MLflow 模型部署到 Modal](/docs/latest/ml/deployment/deploy-model-to-modal/)
    * [Docker](/docs/latest/ml/docker/)
  * [团队协作](/docs/latest/self-hosting/)
  * [API 参考](https://mlflow.org/docs/latest/api_reference/python_api/index.html)
  * [MLflow 3 迁移指南](/docs/latest/ml/mlflow-3/)
  * [更多](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.md)

  * [](/docs/latest/)
  * 部署
  * MLflow Serving（模型服务）
本页内容

# MLflow Serving（模型服务）

在训练好机器学习模型并确认其性能之后，下一步就是将其部署到生产环境。这个过程可能很复杂，但 MLflow 通过提供一套便捷的工具集简化了部署流程，支持将 ML 模型部署到各种目标环境，包括本地环境、云服务和 Kubernetes 集群。使用 MLflow 部署工具集，你可以享受以下优势：

  * **轻松部署**：MLflow 提供了简洁的接口用于将模型部署到各种目标环境，无需编写模板代码。
  * **依赖与环境管理**：MLflow 确保部署环境与训练环境一致，捕获所有依赖项。这保证了模型在任何部署位置都能一致运行。
  * **模型与代码打包**：使用 MLflow，不仅是模型，任何辅助代码和配置都会随部署容器一起打包。这确保模型可以无缝执行，不会缺少任何组件。
  * **避免供应商锁定**：MLflow 提供了标准的模型打包格式和统一的部署 API。你可以轻松在不同部署目标之间切换，而无需重写代码。

## 核心概念

### [MLflow Model（模型）](/docs/latest/ml/model/)

[MLflow Model](/docs/latest/ml/model/) 是一种标准格式，将机器学习模型与其元数据（如依赖项和推理模式）一起打包。通常通过 [MLflow Tracking API](/docs/latest/ml/tracking/) 在训练执行过程中创建模型，例如 [`mlflow.pyfunc.log_model()`](/docs/latest/api_reference/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model)。也可以通过 [MLflow Model Registry（模型注册表）](/docs/latest/ml/model-registry/) 注册和检索模型。要使用 MLflow 部署功能，你必须先创建一个模型。

### 容器（Container）

容器在简化和标准化模型部署过程中扮演着关键角色。MLflow 使用 Docker 容器将模型及其依赖项一起打包，从而能够部署到各种目标环境而不会出现环境兼容性问题。有关如何将模型部署为容器的更多详情，请参阅[为 MLflow 模型构建 Docker 镜像](/docs/latest/ml/deployment/deploy-model-to-kubernetes/#build-docker-for-deployment)。如果你是 Docker 新手，可以从[「什么是容器」](https://www.docker.com/resources/what-container)开始学习。

### 部署目标（Deployment Target）

部署目标指的是模型的目标运行环境。MLflow 支持多种目标，包括本地环境、云服务（AWS、Azure）、Kubernetes 集群等。

## 工作原理

[MLflow Model](/docs/latest/ml/model/) 已经将模型及其依赖项打包在一起，因此 MLflow 可以创建虚拟环境（用于本地部署）或包含运行模型所需一切的 Docker 容器镜像。随后，MLflow 使用 [FastAPI](https://fastapi.tiangolo.com/) 等框架启动具有 REST 端点的推理服务器，准备好部署到各种目标环境以处理推理请求。有关服务器和端点的详细信息，请参阅[推理服务器规范](/docs/latest/ml/deployment/deploy-model-locally/#local-inference-server-spec)。MLflow 提供 CLI 命令和 Python API 来简化部署过程。不同部署目标所需的命令有所不同，请继续阅读下一节以了解你所选目标的详情。

## 支持的部署目标

MLflow 支持多种部署目标。有关每个目标的详细信息和教程，请点击以下相应链接。[本地部署模型使用 MLflow 将模型部署为本地推理服务器非常简单，只需一条命令 `mlflow models serve`。](/docs/latest/ml/deployment/deploy-model-locally/)[Amazon SageMaker 是一项用于扩展 ML 推理容器的全托管服务。MLflow 通过易用的命令简化了部署过程，无需编写容器定义。](/docs/latest/ml/deployment/deploy-model-to-sagemaker/)[MLflow 与 Azure ML 无缝集成。你可以将 MLflow 模型部署到 Azure ML 托管的在线/批量端点，或部署到 Azure Container Instances (ACI) / Azure Kubernetes Service (AKS)。](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models)[Databricks Model Serving 提供全托管服务，用于大规模部署 MLflow 模型，并具有性能优化和监控能力的额外优势。](https://docs.databricks.com/en/mlflow/models.html)[MLflow 部署与 Kubernetes 原生 ML 服务框架（如 Seldon Core 和 KServe（原 KFServing））集成。](/docs/latest/ml/deployment/deploy-model-to-kubernetes/)[Modal 是一个面向 AI/ML 的无服务器云平台，提供按需 GPU 访问（T4 到 H200）、自动扩缩容和通过 mlflow-modal-deploy 插件的一键部署。](/docs/latest/ml/deployment/deploy-model-to-modal/)[社区支持的目标MLflow 还通过社区支持的插件支持更多部署目标，如 Ray Serve、Redis AI、Torch Serve、Oracle Cloud Infrastructure (OCI) 等。](/docs/latest/ml/plugins/)

## API 参考

### 命令行接口（CLI）

部署相关命令主要分为两个模块：

  * [mlflow models](/docs/latest/api_reference/cli.html#mlflow-models) —— 通常用于本地部署。
  * [mlflow deployments](/docs/latest/api_reference/cli.html#mlflow-deployments) —— 通常用于部署到自定义目标。

请注意，这些分类并非严格划分，可能存在交叉。此外，某些目标需要自定义模块或插件，例如，[mlflow sagemaker](/docs/latest/api_reference/cli.html#mlflow-sagemaker) 用于 Amazon SageMaker 部署，[azureml-mlflow](https://pypi.org/project/azureml-mlflow) 库则用于 Azure ML。因此，建议查阅你所选目标的具体文档以确定合适的命令。

### Python API

MLflow 部署中几乎所有功能也可以通过 Python API 访问。更多详情请参考以下 API 文档：

  * [mlflow.models](/docs/latest/api_reference/python_api/mlflow.models.html#mlflow.models)
  * [mlflow.deployments](/docs/latest/api_reference/python_api/mlflow.deployments.html#mlflow.deployments)
  * [mlflow.sagemaker](/docs/latest/api_reference/python_api/mlflow.sagemaker.html#mlflow.sagemaker)

## 常见问题（FAQ）

如果在模型部署过程中遇到任何依赖问题，请参阅[模型依赖常见问题](/docs/latest/ml/model/dependencies/#model-dependencies-troubleshooting)以获取故障排除和验证修复的指导。[上一篇工作流](/docs/latest/ml/model-registry/workflow/)[下一篇将 MLflow 模型部署为本地推理服务器](/docs/latest/ml/deployment/deploy-model-locally/)

  * 核心概念
    * MLflow Model（模型）
    * 容器（Container）
    * 部署目标（Deployment Target）
  * 工作原理
  * 支持的部署目标
  * API 参考
    * 命令行接口（CLI）
    * Python API
  * 常见问题（FAQ）
