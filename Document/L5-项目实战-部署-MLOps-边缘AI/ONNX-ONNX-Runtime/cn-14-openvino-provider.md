# OpenVINO 执行提供者（OpenVINO Execution Provider）

> 来源：https://onnxruntime.ai/docs/execution-providers/OpenVINO-ExecutionProvider.html

使用 Intel OpenVINO 执行提供者在 Intel CPU、GPU、NPU 上加速 ONNX 模型。请参阅[此页面](https://software.intel.com/en-us/openvino-toolkit/hardware)了解支持的 Intel 硬件详情。

## 内容

- 安装
- 要求
- 构建
- 使用
- 配置选项
- 配置描述
  - `device_type`
  - `precision`
  - `num_of_threads` 和 `num_streams`
  - `cache_dir`
  - `load_config`
    - 概述
    - JSON 配置格式
    - 常用 OpenVINO 属性
    - 属性参考文档
  - `enable_qdq_optimizer`
  - `disable_dynamic_shapes`
  - `reshape_input`
  - `model_priority`
  - `layout`
- 示例
  - Python
    - 使用带有 JSON 字符串的 load_config
    - 用于 CPU 的 load_config
    - 用于 GPU 的 load_config
  - Python API
  - C/C++ API 2.0
  - C/C++ 旧版 API
  - ONNX Runtime 图级优化
    - Python API
    - C/C++ API
- 支持覆盖
  - 拓扑支持
