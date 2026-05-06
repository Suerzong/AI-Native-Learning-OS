跳转到主要内容[](/docs/latest/)机器学习

  * [大语言模型与智能体](/docs/latest/genai/)
  * [机器学习](/docs/latest/ml/)
[API 参考](https://mlflow.org/docs/latest/api_reference/index.html)[自托管](/docs/latest/self-hosting/)[社区](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)搜索

  * [概览](/docs/latest/ml/)
  * [入门指南](/docs/latest/ml/getting-started/)
  * [机器学习](/docs/latest/ml/traditional-ml/)
    * [传统机器学习](/docs/latest/ml/traditional-ml/)
    * [深度学习](/docs/latest/ml/deep-learning/)
  * [构建](/docs/latest/ml/tracking/)
    * [MLflow Tracking](/docs/latest/ml/tracking/)
    * [MLflow Model](/docs/latest/ml/model/)
    * [MLflow 数据集](/docs/latest/ml/dataset/)
  * [评估](/docs/latest/ml/evaluation/)
  * [部署](/docs/latest/ml/model-registry/)
    * [MLflow Model Registry](/docs/latest/ml/model-registry/)
      * [概览](/docs/latest/ml/model-registry/)
      * [教程](/docs/latest/ml/model-registry/tutorial/)
      * [工作流](/docs/latest/ml/model-registry/workflow/)
    * [MLflow Serving](/docs/latest/ml/deployment/)
    * [Docker](/docs/latest/ml/docker/)
  * [团队协作](/docs/latest/self-hosting/)
  * [API 参考](https://mlflow.org/docs/latest/api_reference/python_api/index.html)
  * [MLflow 3 迁移指南](/docs/latest/ml/mlflow-3/)
  * [更多](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.md)

  * [](/docs/latest/)
  * 部署
  * MLflow Model Registry
本页内容

# MLflow Model Registry

MLflow Model Registry 是一个集中式的模型存储库、一组 API 和一个 UI，旨在协作管理机器学习模型的完整生命周期。它提供溯源信息（即哪个 MLflow 实验和运行产生了该模型）、版本控制、别名、元数据标签和注释支持，确保你在从开发到生产部署的每个阶段都拥有完整的信息。

## 为什么需要 Model Registry？

随着机器学习项目复杂性和规模的增长，在不同环境、团队和迭代之间手动管理模型变得越来越容易出错且低效。MLflow Model Registry 通过提供一个集中化、结构化的系统来组织和治理整个生命周期中的 ML 模型来解决这一挑战。使用 Model Registry 有以下好处：

  * **版本控制**：注册表自动跟踪每个模型的版本，允许团队比较迭代、回滚到先前状态以及并行管理多个版本（例如 staging 与 production）。
  * **模型溯源与可追溯性**：每个注册的模型版本都链接到产生它的 MLflow 运行、记录的模型或笔记本，实现完全可复现性。你可以追溯模型的确切训练方式、使用的数据和参数。
  * **生产就绪的工作流**：模型别名（如 @champion）和标签等功能使部署工作流更易于管理，以受控和可审计的方式将模型提升到实验、暂存或生产环境。
  * **治理与合规**：通过结构化元数据、标签和基于角色的访问控制（当与 Databricks 后端或托管 MLflow 服务一起使用时），Model Registry 支持企业级 ML 操作所必需的治理要求。

无论你是独立数据科学家还是大型 ML 平台团队的一员，Model Registry 都是扩展可靠和可维护机器学习系统的基础组件。

## 核心概念

Model Registry 引入了几个概念来描述和促进 MLflow 模型的完整生命周期。

| 概念 | 描述 |
| 模型（Model）| MLflow 模型使用模型 flavor 的 **`mlflow.<model_flavor>.log_model()`** 方法之一创建，或自 MLflow 3 起使用 **[`mlflow.create_external_model()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.create_external_model)** API 创建。记录后，该模型可以在 Model Registry 中注册。|
| 已注册模型（Registered Model）| MLflow 模型可以在 Model Registry 中注册。已注册模型具有唯一名称，包含版本、别名、标签和其他元数据。|
| 模型版本（Model Version）| 每个已注册模型可以有一个或多个版本。当新模型添加到 Model Registry 时，它作为版本 1 添加。注册到同一模型名称的每个新模型**递增版本号**。模型版本具有标签，可用于跟踪模型版本的属性（例如 _`pre_deploy_checks: "PASSED"`_）|
| 模型 URI | 你可以使用此格式的 URI 引用已注册模型：`models:/<model-name>/<model-version>`，例如，如果你有一个名为 "MyModel" 且版本为 1 的已注册模型，引用该模型的 URI 为：`models:/MyModel/1`。|
| 模型别名（Model Alias）| 模型别名允许你为已注册模型的特定版本分配一个可变的命名引用。通过为特定模型版本分配别名，你可以使用该别名通过模型 URI 或模型注册表 API 引用该模型版本。例如，你可以创建名为 **`champion`** 的别名指向名为 **`MyModel`** 的模型的版本 1。然后你可以使用 URI **`models:/MyModel@champion`** 引用 **`MyModel`** 的版本 1。别名对于部署模型特别有用。例如，你可以将 **`champion`** 别名分配给用于生产流量的模型版本，并在生产工作负载中定位此别名。然后，你可以通过将 **`champion`** 别名重新分配给不同的模型版本来更新提供生产流量的模型。|
| 标签（Tags）| 标签是你与已注册模型和模型版本关联的键值对，允许你按功能或状态标记和分类它们。例如，你可以将键为 **`"task"`**、值为 **`"question-answering"`**（在 UI 中显示为 **`task:question-answering`**）的标签应用于用于问答任务的已注册模型。在模型版本级别，你可以用 **`validation_status:pending`** 标记正在进行部署前验证的版本，用 **`validation_status:approved`** 标记已通过验证可部署的版本。|
| 注释和描述 | 你可以使用 Markdown 对顶级模型和每个版本单独注释，包括描述和对团队有用的任何相关信息，如算法描述、使用的数据集或特定版本建模方法的整体方法论。|

## 实践中的 Model Registry

MLflow Model Registry 在开源（OSS）MLflow 和 Databricks 等托管平台中都可用。根据环境不同，注册表提供不同级别的集成、治理和协作功能。

### OSS MLflow 中的 Model Registry

在 ML 模型的开源版本 MLflow 中，Model Registry 提供 UI 和 API 用于版本控制和管理 ML 模型。你可以注册模型、跟踪版本、添加标签和描述，以及在 Staging 和 Production 等阶段之间转换模型。

在 MLflow 中注册模型

  * Python API
  * MLflow UI

#### 使用 MLflow Python API 注册模型

MLflow 提供了多种注册模型版本的方式

```python
# 选项 1：在记录模型时指定 `registered_model_name` 参数
mlflow.<flavor>.log_model(..., registered_model_name="<你的模型名称>")

# 选项 2：注册已记录的模型
mlflow.register_model(model_uri="<你的模型 URI>", name="<你的模型名称>")
```

注册模型后，你可以使用模型名称和版本加载它

```python
mlflow.<flavor>.load_model("models:/<你的模型名称>/<你的模型版本>")
```

#### 在 MLflow UI 上注册模型

  1. 打开包含你要注册的 MLflow 模型的 MLflow 运行详情页面。在**产物**部分选择包含目标 MLflow 模型的模型文件夹。
  2. 点击**注册模型**按钮，将弹出一个模态表单。
  3. 在表单的**模型**下拉菜单中，你可以选择"创建新模型"（这将创建一个新的已注册模型，你的 MLflow 模型作为其初始版本）或选择现有的已注册模型（这将你的模型作为新版本注册到其下）。以下截图演示了将 MLflow 模型注册到名为 `"iris_model_testing"` 的新已注册模型。

要了解有关 OSS Model Registry 的更多信息，请参阅[模型注册表教程](/docs/latest/ml/model-registry/tutorial/)。

### Databricks 中的 Model Registry

Databricks 通过将 Model Registry 与 Unity Catalog 集成来扩展 MLflow 的功能，实现集中治理、细粒度访问控制和跨工作区协作。Unity Catalog 集成的主要优势包括：

  * **增强治理**：对模型资产应用访问策略和权限控制。
  * **跨工作区访问**：注册一次模型，即可在多个 Databricks 工作区中访问。
  * **模型溯源**：跟踪用于创建每个模型的笔记本、数据集和实验。
  * **发现与复用**：从共享目录中浏览和复用生产级模型。

在 Databricks UC 中注册模型

  * Python API
  * Databricks UI

#### 使用 MLflow Python API 将模型注册到 Databricks UC

**前提条件**：将 tracking uri 设置为 Databricks

```python
import mlflow

mlflow.set_registry_uri("databricks-uc")
```

使用 MLflow API 注册模型

```python
# 选项 1：在记录模型时指定 `registered_model_name` 参数
mlflow.<flavor>.log_model(..., registered_model_name="<你的模型名称>")

# 选项 2：注册已记录的模型
mlflow.register_model(model_uri="<你的模型 URI>", name="<你的模型名称>")
```

> 警告：UC 中的 ML 模型版本必须具有[模型签名](/docs/latest/ml/model/signatures/)。如果你想对已记录或已保存的模型设置签名，可以使用 [`mlflow.models.set_signature()`](/docs/latest/api_reference/python_api/mlflow.models.html#mlflow.models.set_signature) API。

注册模型后，你可以使用模型名称和版本加载它

```python
mlflow.<flavor>.load_model("models:/<你的模型名称>/<你的模型版本>")
```

#### 在 Databricks UI 上注册模型

  1. 从实验运行页面或模型页面，点击 UI 右上角的"注册模型"。
  2. 在对话框中，选择 Unity Catalog，然后从下拉列表中选择目标模型。
  3. 点击"注册"。

注册模型可能需要一些时间。要监控进度，请导航到 Unity Catalog 中的目标模型并定期刷新。更多信息，请参阅 Databricks 关于[管理模型生命周期](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle)的文档。[上一页评估](/docs/latest/ml/evaluation/)[下一页教程](/docs/latest/ml/model-registry/tutorial/)

  * 为什么需要 Model Registry？
  * 核心概念
  * 实践中的 Model Registry
    * OSS MLflow 中的 Model Registry
      * 使用 MLflow Python API 注册模型
      * 在 MLflow UI 上注册模型
    * Databricks 中的 Model Registry
      * 使用 MLflow Python API 将模型注册到 Databricks UC
      * 在 Databricks UI 上注册模型

© 2025 MLflow 项目，LF Projects, LLC 旗下产品。[组件](https://mlflow.org)[发布](https://mlflow.org/releases)[博客](https://mlflow.org/blog)[文档](/docs/latest/)[大使计划](https://mlflow.org/ambassadors)
