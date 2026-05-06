Skip to main content[](/docs/latest/)Machine Learning

  * [LLMs & Agents](/docs/latest/genai/)
  * [Machine Learning](/docs/latest/ml/)
[API Reference](https://mlflow.org/docs/latest/api_reference/index.html)[Self-Hosting](/docs/latest/self-hosting/)[Community](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)Search

  * [Overview](/docs/latest/ml/)
  * [Getting Started](/docs/latest/ml/getting-started/)
  * [Machine Learning](/docs/latest/ml/traditional-ml/)
    * [Traditional ML](/docs/latest/ml/traditional-ml/)
    * [Deep Learning](/docs/latest/ml/deep-learning/)
  * [Build ](/docs/latest/ml/tracking/)
    * [MLflow Tracking](/docs/latest/ml/tracking/)
    * [MLflow Model](/docs/latest/ml/model/)
    * [MLflow Datasets](/docs/latest/ml/dataset/)
  * [Evaluate](/docs/latest/ml/evaluation/)
  * [Deploy](/docs/latest/ml/model-registry/)
    * [MLflow Model Registry](/docs/latest/ml/model-registry/)
    * [MLflow Serving](/docs/latest/ml/deployment/)
      * [Deploy MLflow Model as a Local Inference Server](/docs/latest/ml/deployment/deploy-model-locally/)
      * [Deploy MLflow Model to Kubernetes](/docs/latest/ml/deployment/deploy-model-to-kubernetes/)
      * [Deploy MLflow Model to Amazon SageMaker](/docs/latest/ml/deployment/deploy-model-to-sagemaker/)
      * [Deploy MLflow Model to Modal](/docs/latest/ml/deployment/deploy-model-to-modal/)
    * [Docker](/docs/latest/ml/docker/)
  * [Team Collaboration](/docs/latest/self-hosting/)
  * [API References](https://mlflow.org/docs/latest/api_reference/python_api/index.html)
  * [MLflow 3 Migration Guide](/docs/latest/ml/mlflow-3/)
  * [More](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.md)

  * [](/docs/latest/)
  * Deploy
  * MLflow Serving
On this page

# MLflow Serving

After training your machine learning model and ensuring its performance, the next step is deploying it to a production environment. This process can be complex, but MLflow simplifies it by offering an easy toolset for deploying your ML models to various targets, including local environments, cloud services, and Kubernetes clusters. By using MLflow deployment toolset, you can enjoy the following benefits:

  * **Effortless Deployment** : MLflow provides a simple interface for deploying models to various targets, eliminating the need to write boilerplate code.
  * **Dependency and Environment Management** : MLflow ensures that the deployment environment mirrors the training environment, capturing all dependencies. This guarantees that models run consistently, regardless of where they're deployed.
  * **Packaging Models and Code** : With MLflow, not just the model, but any supplementary code and configurations are packaged along with the deployment container. This ensures that the model can be executed seamlessly without any missing components.
  * **Avoid Vendor Lock-in** : MLflow provides a standard format for packaging models and unified APIs for deployment. You can easily switch between deployment targets without having to rewrite your code.

## Concepts​

### [MLflow Model](/docs/latest/ml/model/)​

[MLflow Model](/docs/latest/ml/model/) is a standard format that packages a machine learning model with its metadata, such as dependencies and inference schema. You typically create a model as a result of training execution using the [MLflow Tracking APIs](/docs/latest/ml/tracking/), for instance, [`mlflow.pyfunc.log_model()`](/docs/latest/api_reference/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model). Alternatively, models can be registered and retrieved via the [MLflow Model Registry](/docs/latest/ml/model-registry/). To use MLflow deployment, you must first create a model.

### Container​

Container plays a critical role for simplifying and standardizing the model deployment process. MLflow uses Docker containers to package models with their dependencies, enabling deployment to various destinations without environment compatibility issues. See [Building a Docker Image for MLflow Model](/docs/latest/ml/deployment/deploy-model-to-kubernetes/#build-docker-for-deployment) for more details on how to deploy your model as a container. If you're new to Docker, you can start learning at ["What is a Container"](https://www.docker.com/resources/what-container).

### Deployment Target​

Deployment target refers to the destination environment for your model. MLflow supports various targets, including local environments, cloud services (AWS, Azure), Kubernetes clusters, and others.

## How it works​

An [MLflow Model](/docs/latest/ml/model/) already packages your model and its dependencies, hence MLflow can create either a virtual environment (for local deployment) or a Docker container image containing everything needed to run your model. Subsequently, MLflow launches an inference server with REST endpoints using frameworks like [FastAPI](https://fastapi.tiangolo.com/), preparing it for deployment to various destinations to handle inference requests. Detailed information about the server and endpoints is available in [Inference Server Specification](/docs/latest/ml/deployment/deploy-model-locally/#local-inference-server-spec). MLflow provides CLI commands and Python APIs to facilitate the deployment process. The required commands differ based on the deployment target, so please continue reading to the next section for more details about your specific target.

## Supported Deployment Targets​

MLflow offers support for a variety of deployment targets. For detailed information and tutorials on each, please follow the respective links below. [Deploying a Model LocallyDeploying a model locally as an inference server is straightforward with MLflow, requiring just a single command `mlflow models serve`.](/docs/latest/ml/deployment/deploy-model-locally/)[Amazon SageMaker is a fully managed service for scaling ML inference containers. MLflow simplifies the deployment process with easy-to-use commands, eliminating the need to write container definitions.](/docs/latest/ml/deployment/deploy-model-to-sagemaker/)[MLflow integrates seamlessly with Azure ML. You can deploy MLflow Model to the Azure ML managed online/batch endpoints, or to Azure Container Instances (ACI) / Azure Kubernetes Service (AKS).](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models)[Databricks Model Serving offers a fully managed service for serving MLflow models at scale, with added benefits of performance optimizations and monitoring capabilities.](https://docs.databricks.com/en/mlflow/models.html)[MLflow Deployment integrates with Kubernetes-native ML serving frameworks such as Seldon Core and KServe (formerly KFServing).](/docs/latest/ml/deployment/deploy-model-to-kubernetes/)[Modal is a serverless cloud platform for AI/ML with on-demand GPU access (T4 to H200), auto-scaling, and one-command deployment via the mlflow-modal-deploy plugin.](/docs/latest/ml/deployment/deploy-model-to-modal/)[Community Supported TargetsMLflow also supports more deployment targets such as Ray Serve, Redis AI, Torch Serve, Oracle Cloud Infrastructure (OCI), through community-supported plugins.](/docs/latest/ml/plugins/)

## API References​

### Command Line Interface​

Deployment-related commands are primarily categorized under two modules:

  * [mlflow models](/docs/latest/api_reference/cli.html#mlflow-models) \- typically used for local deployment.
  * [mlflow deployments](/docs/latest/api_reference/cli.html#mlflow-deployments) \- typically used for deploying to custom targets.

Note that these categories are not strictly separated and may overlap. Furthermore, certain targets require custom modules or plugins, for example, [mlflow sagemaker](/docs/latest/api_reference/cli.html#mlflow-sagemaker) is used for Amazon SageMaker deployments, and the [azureml-mlflow](https://pypi.org/project/azureml-mlflow) library is required for Azure ML. Therefore, it is advisable to consult the specific documentation for your chosen target to identify the appropriate commands.

### Python APIs​

Almost all functionalities available in MLflow deployment can also be accessed via Python APIs. For more details, refer to the following API references:

  * [mlflow.models](/docs/latest/api_reference/python_api/mlflow.models.html#mlflow.models)
  * [mlflow.deployments](/docs/latest/api_reference/python_api/mlflow.deployments.html#mlflow.deployments)
  * [mlflow.sagemaker](/docs/latest/api_reference/python_api/mlflow.sagemaker.html#mlflow.sagemaker)

## FAQ​

If you encounter any dependency issues during model deployment, please refer to [Model Dependencies FAQ](/docs/latest/ml/model/dependencies/#model-dependencies-troubleshooting) for guidance on how to troubleshoot and validate fixes.[PreviousWorkflow](/docs/latest/ml/model-registry/workflow/)[NextDeploy MLflow Model as a Local Inference Server](/docs/latest/ml/deployment/deploy-model-locally/)

  * Concepts
    * MLflow Model
    * Container
    * Deployment Target
  * How it works
  * Supported Deployment Targets
  * API References
    * Command Line Interface
    * Python APIs
  * FAQ
© 2025 MLflow Project, a Series of LF Projects, LLC.[Components](https://mlflow.org)[Releases](https://mlflow.org/releases)[Blog](https://mlflow.org/blog)[Docs](/docs/latest/)[Ambassador Program](https://mlflow.org/ambassadors)
