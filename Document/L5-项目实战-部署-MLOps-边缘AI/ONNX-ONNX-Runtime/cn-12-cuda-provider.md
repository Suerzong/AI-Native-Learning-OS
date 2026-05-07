# CUDA 执行提供者（CUDA Execution Provider）

> 来源：https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html

CUDA 执行提供者在 NVIDIA CUDA 启用的 GPU 上实现硬件加速计算。

## 内容

- 安装
- 从源码构建
- 要求
  - CUDA 12.x
  - CUDA 11.x
  - CUDA 10.x
- 构建
- 与 PyTorch 的兼容性
- 预加载 DLL
- 配置选项
  - device_id
  - user_compute_stream
  - do_copy_in_default_stream
  - use_ep_level_unified_stream
  - gpu_mem_limit
  - arena_extend_strategy
  - cudnn_conv_algo_search
  - cudnn_conv_use_max_workspace
  - cudnn_conv1d_pad_to_nc1d
  - enable_cuda_graph
  - enable_skip_layer_norm_strict_mode
  - use_tf32
  - gpu_external_[alloc|free|empty_cache]
  - prefer_nhwc
- 性能调优
  - 卷积密集型模型
  - 卷积输入填充
  - 使用 CUDA Graph（预览）
- 示例
  - Python
  - C/C++
