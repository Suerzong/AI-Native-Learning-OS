# MLflow Models（模型）

> 来源：https://mlflow.org/docs/latest/ml/models/index.html
> 注意：此页面无法自动抓取（S3 AccessDenied），请直接访问原文链接。

## 概述

MLflow Models 为机器学习模型提供了一种标准打包格式，可在各种下游工具中使用。

### 核心概念

- **模型格式（Model Format）**：ML 模型的标准格式
- **模型签名（Model Signature）**：模型输入和输出的模式定义
- **模型风格（Model Flavors）**：不同的序列化格式（sklearn、pytorch、tensorflow 等）
- **模型加载（Model Loading）**：用于在不同框架中加载模型的统一 API

### 模型风格

MLflow 支持多种模型风格：

- `python_function`（pyfunc）—— 通用 Python 函数模型
- `sklearn` —— Scikit-learn 模型
- `pytorch` —— PyTorch 模型
- `tensorflow` —— TensorFlow 模型
- `keras` —— Keras 模型
- `xgboost` —— XGBoost 模型
- `lightgbm` —— LightGBM 模型
- `spark` —— Spark MLlib 模型
- `h2o` —— H2O 模型
- `statsmodels` —— Statsmodels 模型
- `prophet` —— Prophet 模型

### 子页面

- [模型概述](https://mlflow.org/docs/latest/ml/models/index.html)
- [模型签名与输入示例](https://mlflow.org/docs/latest/ml/model/signatures/)
- [模型 API 参考](https://mlflow.org/docs/latest/python_api/mlflow.models.html)
