跳转到主要内容

[](/docs/latest/)

机器学习

  * [大语言模型与智能体](/docs/latest/genai/)
  * [机器学习](/docs/latest/ml/)

[API 参考](https://mlflow.org/docs/latest/api_reference/index.html)[自托管](/docs/latest/self-hosting/)[社区](/docs/latest/community/)

[GitHub](https://github.com/mlflow/mlflow)

搜索

  * [概览](/docs/latest/ml/)
  * [入门指南](/docs/latest/ml/getting-started/)

  * [机器学习](/docs/latest/ml/traditional-ml/)

    * [传统机器学习](/docs/latest/ml/traditional-ml/)

    * [深度学习](/docs/latest/ml/deep-learning/)

  * [构建](/docs/latest/ml/tracking/)

    * [MLflow Tracking](/docs/latest/ml/tracking/)

      * [快速入门](/docs/latest/ml/tracking/quickstart/)
      * [自动日志记录](/docs/latest/ml/tracking/autolog/)
      * [Tracking Server](/docs/latest/self-hosting/architecture/tracking-server/)
      * [搜索](/docs/latest/ml/search/search-models/)

      * [系统指标](/docs/latest/ml/tracking/system-metrics/)
      * [Tracking API](/docs/latest/ml/tracking/tracking-api/)
    * [MLflow Model](/docs/latest/ml/model/)

    * [MLflow 数据集](/docs/latest/ml/dataset/)
  * [评估](/docs/latest/ml/evaluation/)
  * [部署](/docs/latest/ml/model-registry/)

  * [团队协作](/docs/latest/self-hosting/)

  * [API 参考](https://mlflow.org/docs/latest/api_reference/python_api/index.html)

  * [MLflow 3 迁移指南](/docs/latest/ml/mlflow-3/)
  * [更多](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.md)

  * [](/docs/latest/)
  * 构建
  * MLflow Tracking

本页内容

# MLflow Tracking

MLflow Tracking 是一个 API 和 UI，用于在运行机器学习代码时记录参数、代码版本、指标和输出文件，并用于后续结果可视化。MLflow Tracking 提供 [Python](/docs/latest/api_reference/python_api/index.html#) 、[REST](/docs/latest/api_reference/rest-api.html#) 、[R](/docs/latest/api_reference/R-api.html#) 和 [Java](/docs/latest/api_reference/java_api/index.html#) API。

MLflow Tracking UI 截图，展示模型训练期间验证损失指标的图表。

## 快速入门

如果你之前没有使用过 MLflow Tracking，我们强烈建议你完成以下快速入门教程。

[MLflow Tracking 快速入门学习 MLflow Tracking 基础知识的绝佳起点！在 5 分钟内学习如何记录、注册和加载模型进行推理。](/docs/latest/ml/tracking/quickstart/)

## 核心概念

### 运行（Runs）

MLflow Tracking 围绕**运行**（runs）的概念组织，运行是某段数据科学代码的执行记录，例如单次 `python train.py` 执行。每个运行记录元数据（关于运行的各种信息，如指标、参数、开始和结束时间）和产物（运行的输出文件，如模型权重、图像等）。

### 模型（Models）

模型代表运行过程中产生的已训练机器学习产物。记录的模型包含与运行类似的元数据和产物。

### 实验（Experiments）

实验将针对特定任务的运行和模型分组在一起。你可以使用 CLI、API 或 UI 创建实验。MLflow API 和 UI 还允许你创建和搜索实验。参阅[将运行组织到实验中](/docs/latest/ml/tracking/tracking-api/#experiment-organization)了解如何将运行组织到实验中的更多细节。

## 跟踪运行

[MLflow Tracking API](/docs/latest/ml/tracking/tracking-api/) 提供了一组函数来跟踪你的运行。例如，你可以调用 [`mlflow.start_run()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.start_run) 启动一个新运行，然后调用[记录函数](/docs/latest/ml/tracking/tracking-api/)如 [`mlflow.log_param()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.log_param) 和 [`mlflow.log_metric()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.log_metric) 分别记录参数和指标。请访问 [Tracking API 文档](/docs/latest/ml/tracking/tracking-api/) 了解更多关于使用这些 API 的细节。

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("lr", 0.001)
    # 你的机器学习代码
    ...
    mlflow.log_metric("val_loss", val_loss)
```

或者，[自动日志记录](/docs/latest/ml/tracking/autolog/)（Auto-logging）提供了一种超快速的 MLflow Tracking 设置方式。这个强大的功能允许你无需显式日志语句即可记录指标、参数和模型——你只需在训练代码之前调用 [`mlflow.autolog()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog)。自动日志记录支持 [Scikit-learn](/docs/latest/ml/tracking/autolog/#autolog-sklearn)、[XGBoost](/docs/latest/ml/tracking/autolog/#autolog-xgboost)、[PyTorch](/docs/latest/ml/tracking/autolog/#autolog-pytorch)、[Keras](/docs/latest/ml/tracking/autolog/#autolog-keras)、[Spark](/docs/latest/ml/tracking/autolog/#autolog-spark) 等流行库。参阅[自动日志记录文档](/docs/latest/ml/tracking/autolog/)了解支持的库及如何使用。

```python
import mlflow

mlflow.autolog()

# 你的训练代码...
```

> 注意：默认情况下，没有任何特殊的服务器/数据库配置，MLflow Tracking 会将数据记录到本地 `mlruns` 目录。如果你想将运行记录到不同的位置（如远程数据库和云存储），以便与团队共享结果，请按照设置 MLflow Tracking 环境部分的说明操作。

### 以编程方式搜索已记录的模型

MLflow 3 通过 [`mlflow.search_logged_models()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_logged_models) 引入了强大的模型搜索功能。该 API 允许你使用类 SQL 语法跨实验查找基于性能指标、参数和模型属性的特定模型。

```python
import mlflow

# 跨实验查找高性能模型
top_models = mlflow.search_logged_models(
    experiment_ids=["1", "2"],
    filter_string="metrics.accuracy > 0.95 AND params.model_type = 'RandomForest'",
    order_by=[{"field_name": "metrics.f1_score", "ascending": False}],
    max_results=5,
)

# 获取用于部署的最佳模型
best_model = mlflow.search_logged_models(
    experiment_ids=["1"],
    filter_string="metrics.accuracy > 0.9",
    max_results=1,
    order_by=[{"field_name": "metrics.accuracy", "ascending": False}],
    output_format="list",
)[0]

# 直接加载最佳模型
loaded_model = mlflow.pyfunc.load_model(f"models:/{best_model.model_id}")
```

**主要特性：**

  * **类 SQL 过滤**：使用 `metrics.`、`params.` 和属性前缀构建复杂查询
  * **数据集感知搜索**：基于特定数据集过滤指标，实现公平的模型比较
  * **灵活排序**：按多个标准排序以找到最佳模型
  * **直接模型加载**：使用新的 `models:/<model_id>` URI 格式实现即时模型访问

有关全面的示例和高级搜索模式，请参阅[搜索已记录模型指南](/docs/latest/ml/search/search-models/)。

### 以编程方式查询运行

你还可以通过 [MlflowClient](/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient) 以编程方式访问 Tracking UI 中的所有功能。

例如，以下代码片段搜索实验中所有运行中验证损失最佳的运行。

```python
client = mlflow.tracking.MlflowClient()
experiment_id = "0"
best_run = client.search_runs(experiment_id, order_by=["metrics.val_loss ASC"], max_results=1)[0]
print(best_run.info)
# {'run_id': '...', 'metrics': {'val_loss': 0.123}, ...}
```

## 跟踪模型

MLflow 3 引入了增强的模型跟踪功能，允许你在单个运行中记录多个模型检查点，并跟踪它们在不同数据集上的性能。这对于深度学习工作流特别有用，你可以在不同训练阶段保存和比较模型检查点。

### 记录模型检查点

你可以在训练过程中使用模型记录函数的 `step` 参数记录不同步骤的模型检查点。每个记录的模型都有唯一的模型 ID，你可以在以后引用它。

```python
import mlflow
import mlflow.pytorch

with mlflow.start_run() as run:
    for epoch in range(100):
        # 训练模型
        train_model(model, epoch)

        # 每 10 个 epoch 记录一次模型检查点
        if epoch % 10 == 0:
            model_info = mlflow.pytorch.log_model(
                pytorch_model=model,
                name=f"checkpoint-epoch-{epoch}",
                step=epoch,
                input_example=sample_input,
            )

            # 记录链接到此特定模型检查点的指标
            accuracy = evaluate_model(model, validation_data)
            mlflow.log_metric(
                key="accuracy",
                value=accuracy,
                step=epoch,
                model_id=model_info.model_id,  # 将指标链接到特定模型
                dataset=validation_dataset,
            )
```

### 将指标链接到模型和数据集

MLflow 3 允许你将指标链接到特定的模型检查点和数据集，提供更好的模型性能可追溯性：

```python
# 创建数据集引用
train_dataset = mlflow.data.from_pandas(train_df, name="training_data")

# 记录带有模型和数据集链接的指标
mlflow.log_metric(
    key="f1_score",
    value=0.95,
    step=epoch,
    model_id=model_info.model_id,  # 链接到特定模型检查点
    dataset=train_dataset,  # 链接到特定数据集
)
```

### 搜索和排序模型检查点

使用 [`mlflow.search_logged_models()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_logged_models) 基于性能指标搜索和排序模型检查点：

```python
# 搜索运行中的所有模型，按准确率排序
ranked_models = mlflow.search_logged_models(
    filter_string=f"source_run_id='{run.info.run_id}'",
    order_by=[{"field_name": "metrics.accuracy", "ascending": False}],
    output_format="list",
)

# 获取性能最佳的模型
best_model = ranked_models[0]
print(f"最佳模型: {best_model.name}")
print(f"准确率: {best_model.metrics[0].value}")

# 加载最佳模型进行推理
loaded_model = mlflow.pyfunc.load_model(f"models:/{best_model.model_id}")
```

### MLflow 3 中的模型 URI

MLflow 3 引入了一种新的模型 URI 格式，使用模型 ID 代替运行 ID，提供更直接的模型引用方式：

```python
# 新的 MLflow 3 模型 URI 格式
model_uri = f"models:/{model_info.model_id}"
loaded_model = mlflow.pyfunc.load_model(model_uri)

# 这取代了旧的基于运行的 URI 格式：
# model_uri = f"runs:/{run_id}/model_path"
```

这种新方法提供了几个优势：

  * **直接模型引用**：无需知道运行 ID 和产物路径
  * **更好的模型生命周期管理**：每个模型检查点都有自己的唯一标识符
  * **改进的模型比较**：轻松比较同一运行中的不同检查点
  * **增强的可追溯性**：模型、指标和数据集之间的清晰链接

## 跟踪数据集

MLflow 提供了跟踪与模型训练事件相关联的数据集的能力。这些与数据集关联的元数据可以通过 [`mlflow.log_input()`](/docs/latest/api_reference/python_api/mlflow.html#mlflow.log_input) API 存储。要了解更多信息，请访问 [MLflow 数据文档](/docs/latest/ml/dataset/) 查看此 API 的可用功能。

## 探索运行、模型和结果

### Tracking UI

Tracking UI 让你可以可视化地探索实验、运行和模型，如本页顶部所示。

  * 基于实验的运行列表和比较（包括跨多个实验的运行比较）
  * 按参数或指标值搜索运行
  * 可视化运行指标
  * 下载运行结果（产物和元数据）

这些功能同样适用于模型，如下所示。

MLflow Tracking UI 模型标签页截图，展示实验下的模型列表。

如果你将运行记录到本地 `mlruns` 目录，请在其上层目录运行以下命令，然后在浏览器中访问 <http://127.0.0.1:5000>。

```bash
mlflow server --port 5000
```

或者，MLflow Tracking Server 提供相同的 UI，并支持运行产物的远程存储。在这种情况下，你可以从任何能连接到 Tracking Server 的机器上在 `http://<你的 MLflow Tracking Server IP 地址>:5000` 查看 UI。

## 设置 MLflow Tracking 环境

> 注意：如果你只想将实验数据和模型记录到本地文件，可以跳过此部分。

MLflow Tracking 支持开发工作流的多种不同场景。本节将指导你如何为特定用例设置 MLflow Tracking 环境。从宏观来看，MLflow Tracking 环境包含以下组件。

### 组件

#### [MLflow Tracking API](/docs/latest/ml/tracking/tracking-api/)

你可以在 ML 代码中调用 MLflow Tracking API 来记录运行，并在必要时与 MLflow Tracking Server 通信。

#### [后端存储](/docs/latest/self-hosting/architecture/backend-store/)

后端存储持久化每个运行的各种元数据，如运行 ID、开始和结束时间、参数、指标等。MLflow 支持两种类型的后端存储：**基于文件系统**（如本地文件）和**基于数据库**（如 PostgreSQL）。

此外，如果你正在使用托管服务（如 Databricks 或 Azure Machine Learning），你将与一个基于 REST 的外部管理后端存储交互，该存储不直接可访问。

#### [产物存储](/docs/latest/self-hosting/architecture/artifact-store/)

产物存储持久化每个运行的（通常较大的）产物，如模型权重（例如 pickled scikit-learn 模型）、图像（例如 PNG）、模型和数据文件（例如 [Parquet](https://parquet.apache.org) 文件）。MLflow 默认将产物存储在本地文件（`mlruns`）中，但也支持不同的存储选项，如 Amazon S3 和 Azure Blob Storage。

对于记录为 MLflow 产物的模型，你可以通过格式为 `models:/<model_id>` 的模型 URI 引用模型，其中 'model_id' 是分配给记录模型的唯一标识符。这取代了旧的 `runs:/<run_id>/<artifact_path>` 格式，提供了更直接的模型引用方式。

如果模型已在 [MLflow Model Registry](/docs/latest/ml/model-registry/) 中注册，你还可以通过格式为 `models:/<model-name>/<model-version>` 的模型 URI 引用模型，详见 [MLflow Model Registry](/docs/latest/ml/model-registry/)。

#### [MLflow Tracking Server](/docs/latest/self-hosting/architecture/tracking-server/)（可选）

MLflow Tracking Server 是一个独立的 HTTP 服务器，提供用于访问后端和/或产物存储的 REST API。Tracking Server 还提供灵活的配置选项，用于管理要提供哪些数据、访问控制、版本控制等。阅读 [MLflow Tracking Server 文档](/docs/latest/self-hosting/) 了解更多详情。

### 常见配置方案

通过正确配置这些组件，你可以创建适合团队开发工作流的 MLflow Tracking 环境。下图和表格展示了 MLflow Tracking 环境的几种常见配置方案。

| 1. 本地主机（默认）| 2. 本地 Tracking + 本地数据库| 3. 使用 MLflow Tracking Server 的远程 Tracking |
| 场景| 个人开发| 个人开发| 团队开发 |
| 用例| 默认情况下，MLflow 将每次运行的元数据和产物记录到本地目录 `mlruns`。这是开始使用 MLflow Tracking 最简单的方式，无需设置任何外部服务器、数据库和存储。| MLflow 客户端可以与 SQLAlchemy 兼容的数据库（如 SQLite、PostgreSQL、MySQL）对接[后端](/docs/latest/self-hosting/architecture/backend-store/)。将元数据保存到数据库可以更清晰地管理实验数据，同时省去设置服务器的工作。| MLflow Tracking Server 可以配置产物 HTTP 代理，通过 Tracking Server 传递产物请求来存储和检索产物，而无需与底层对象存储服务交互。这对于团队开发场景特别有用，你希望将产物和实验元数据存储在具有适当访问控制的共享位置。 |
| 教程| [快速入门](/docs/latest/ml/tracking/quickstart/)| [使用本地数据库跟踪实验](/docs/latest/ml/tracking/tutorials/local-database/)| [使用 MLflow Tracking Server 进行远程实验跟踪](/docs/latest/ml/tracking/tutorials/remote-server/) |

## MLflow Tracking Server 的其他配置

MLflow Tracking Server 为其他特殊用例提供可定制性。请按照[使用 MLflow Tracking Server 进行远程实验跟踪](/docs/latest/ml/tracking/tutorials/remote-server/)学习基本设置，然后继续阅读以下材料以满足你的高级配置需求。

  * 本地 Tracking Server
  * 仅产物模式
  * 产物直接访问

#### 在本地使用 MLflow Tracking Server

你当然可以在本地运行 MLflow Tracking Server。虽然这与直接使用本地文件或数据库相比没有太大额外好处，但对于在本地测试团队开发工作流或在容器环境中运行机器学习代码可能很有用。

#### 以仅产物模式运行 MLflow Tracking Server

MLflow Tracking Server 有一个 `--artifacts-only` 选项，允许服务器专门处理（代理）产物，而不允许处理元数据。这在大型组织中或训练超大模型时特别有用。在这些场景中，你可能有很高的产物传输量，可以将产物服务的流量分离出来以不影响 Tracking 功能。请阅读[可选地使用 Tracking Server 实例专门处理产物](/docs/latest/self-hosting/architecture/tracking-server/#tracking-server-artifacts-only)了解更多关于如何使用此模式的详情。

#### 禁用产物代理以允许直接访问产物

MLflow Tracking Server 默认同时提供产物和元数据服务。但在某些情况下，你可能希望允许直接访问远程产物存储，以避免代理的开销，同时保留元数据跟踪功能。这可以通过使用 `--no-serve-artifacts` 选项启动服务器来禁用产物代理实现。参考[在不代理产物访问的情况下使用 Tracking Server](/docs/latest/self-hosting/architecture/tracking-server/#tracking-server-no-proxy) 了解如何设置。

## 常见问题

### 可以并行启动多个运行吗？

可以，MLflow 支持并行启动多个运行，例如多进程/多线程。参阅[在一个程序中启动多个运行](/docs/latest/ml/tracking/tracking-api/#parallel-execution-strategies)了解更多详情。

### 如何整齐地组织大量 MLflow 运行？

MLflow 提供了几种组织运行的方式：

  * [将运行组织到实验中](/docs/latest/ml/tracking/tracking-api/#experiment-organization) - 实验是运行的逻辑容器。你可以使用 CLI、API 或 UI 创建实验。
  * [创建子运行](/docs/latest/ml/tracking/tracking-api/#hierarchical-runs-with-parent-child-relationships) - 你可以在单个父运行下创建子运行以将它们分组。例如，你可以在交叉验证实验中为每个折创建一个子运行。
  * [为运行添加标签](/docs/latest/ml/tracking/tracking-api/#smart-tagging-for-organization) - 你可以为每个运行关联任意标签，这允许你基于标签过滤和搜索运行。

### 不运行 Tracking Server 可以直接访问远程存储吗？

可以，虽然在团队开发工作流中将 MLflow Tracking Server 作为产物访问的代理是最佳实践，但如果你将其用于个人项目或测试，则可能不需要。你可以通过以下方式实现：

  1. 设置产物配置（如凭据和端点），就像为 MLflow Tracking Server 所做的那样。参阅[配置产物存储](/docs/latest/self-hosting/architecture/artifact-store/#artifacts-store-supported-storages)了解更多详情。
  2. 创建具有显式产物位置的实验：

```python
experiment_name = "your_experiment_name"
mlflow.create_experiment(experiment_name, artifact_location="s3://your-bucket")
mlflow.set_experiment(experiment_name)
```

此实验下的运行将直接将产物记录到远程存储。

#### 如何将 MLflow Tracking 与 [Model Registry](/docs/latest/ml/model-registry/) 集成？

要将 Model Registry 功能与 MLflow Tracking 结合使用，你**必须使用数据库支持的存储**（如 PostgreSQL），并使用相应模型 flavor 的 `log_model` 方法记录模型。记录模型后，你可以通过 UI 或 API 在 Model Registry 中添加、修改、更新或删除模型。参阅[后端存储](/docs/latest/self-hosting/architecture/backend-store/)和[常见配置方案](/docs/latest/self-hosting/architecture/overview/#common-setups)了解如何为你的工作流正确配置后端存储。

#### 如何包含关于运行的附加描述文本？

系统标签 `mlflow.note.content` 可用于添加关于此运行的描述性备注。虽然其他[系统标签](/docs/latest/ml/tracking/tracking-api/#system-tags-reference)是自动设置的，但此标签**默认不设置**，用户可以覆盖它以包含关于运行的附加信息。内容将显示在运行页面的"备注"部分。[上一页spaCy](/docs/latest/ml/deep-learning/spacy/)[下一页快速入门](/docs/latest/ml/tracking/quickstart/)

  * 快速入门
  * 核心概念
    * 运行（Runs）
    * 模型（Models）
    * 实验（Experiments）
  * 跟踪运行
    * 以编程方式搜索已记录的模型
    * 以编程方式查询运行
  * 跟踪模型
    * 记录模型检查点
    * 将指标链接到模型和数据集
    * 搜索和排序模型检查点
    * MLflow 3 中的模型 URI
  * 跟踪数据集
  * 探索运行、模型和结果
    * Tracking UI
  * 设置 MLflow Tracking 环境
    * 组件
    * 常见配置方案
  * MLflow Tracking Server 的其他配置
  * 常见问题
    * 可以并行启动多个运行吗？
    * 如何整齐地组织大量 MLflow 运行？
    * 不运行 Tracking Server 可以直接访问远程存储吗？

© 2025 MLflow 项目，LF Projects, LLC 旗下产品。[组件](https://mlflow.org)[发布](https://mlflow.org/releases)[博客](https://mlflow.org/blog)[文档](/docs/latest/)[大使计划](https://mlflow.org/ambassadors)
