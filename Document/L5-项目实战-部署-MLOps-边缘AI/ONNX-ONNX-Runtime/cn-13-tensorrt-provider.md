# TensorRT 执行提供者（TensorRT Execution Provider）

> 来源：https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.html

使用 TensorRT 执行提供者，ONNX Runtime 在相同硬件上比通用 GPU 加速提供更好的推理性能。

ONNX Runtime 中的 TensorRT 执行提供者利用 NVIDIA 的 [TensorRT](https://developer.nvidia.com/tensorrt) 深度学习推理引擎来加速其 GPU 系列上的 ONNX 模型。Microsoft 和 NVIDIA 密切合作，将 TensorRT 执行提供者与 ONNX Runtime 集成。

## 内容

- 安装
- 从源码构建
- 要求
- 使用
  - C/C++
  - Python
- 配置
  - Python API 示例
  - C++ API 示例
  - 场景
  - 执行提供者选项
  - 环境变量（已弃用）
- TensorRT EP 缓存
  - 缓存可以将会话创建时间从分钟减少到秒
  - 如何设置缓存
  - 关于嵌入式引擎模型 / EPContext 模型的更多信息
- 性能调优
  - TensorRT 子图的形状推断
  - TensorRT 插件支持
  - 计时缓存
  - 动态形状输入的显式形状范围
  - 数据相关形状（DDS）操作
- 示例
- 已知问题

## 安装

请选择 GPU（CUDA/TensorRT）版本的 ONNX Runtime：https://onnxruntime.ai/docs/install。Jetpack 的预构建包和 Docker 镜像可在 [Jetson Zoo](https://elinux.org/Jetson_Zoo#ONNX_Runtime) 获取。
