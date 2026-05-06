# MLflow Models

> Source: https://mlflow.org/docs/latest/ml/models/index.html
> Note: This page could not be automatically fetched (S3 AccessDenied). Please visit the URL directly.

## Overview

MLflow Models provide a standard format for packaging machine learning models that can be used in a variety of downstream tools.

### Key Concepts

- **Model Format**: A standard format for ML models
- **Model Signature**: Schema for model inputs and outputs
- **Model Flavors**: Different serialization formats (sklearn, pytorch, tensorflow, etc.)
- **Model Loading**: Unified API for loading models in different frameworks

### Model Flavors

MLflow supports multiple model flavors:

- `python_function` (pyfunc) - Generic Python function model
- `sklearn` - Scikit-learn models
- `pytorch` - PyTorch models
- `tensorflow` - TensorFlow models
- `keras` - Keras models
- `xgboost` - XGBoost models
- `lightgbm` - LightGBM models
- `spark` - Spark MLlib models
- `h2o` - H2O models
- `statsmodels` - Statsmodels
- `prophet` - Prophet models

### Sub-pages

- [Model Overview](https://mlflow.org/docs/latest/ml/models/index.html)
- [Model Signatures and Input Examples](https://mlflow.org/docs/latest/ml/model/signatures/)
- [Model API Reference](https://mlflow.org/docs/latest/python_api/mlflow.models.html)
