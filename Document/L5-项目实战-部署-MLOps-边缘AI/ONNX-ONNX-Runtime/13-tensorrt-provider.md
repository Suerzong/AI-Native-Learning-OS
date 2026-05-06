Skip to main content Link Menu Expand (external link) Document Search Copy Copied

[ ](/)

  * [ONNX Runtime](/docs/)
  * [Install ONNX Runtime](/docs/install/)
  * [Get Started](/docs/get-started/)
    * [Python](/docs/get-started/with-python.html)
    * [C++](/docs/get-started/with-cpp.html)
    * [C](/docs/get-started/with-c.html)
    * [C#](/docs/get-started/with-csharp.html)
    * [Java](/docs/get-started/with-java.html)
    * [JavaScript](/docs/get-started/with-javascript/)
      * [Web](/docs/get-started/with-javascript/web.html)
      * [Node.js binding](/docs/get-started/with-javascript/node.html)
      * [React Native](/docs/get-started/with-javascript/react-native.html)
    * [Objective-C](/docs/get-started/with-obj-c.html)
    * [Julia, Ruby and Rust APIs](/docs/get-started/community-projects.html)
    * [Windows](/docs/get-started/with-windows.html)
    * [Mobile](/docs/get-started/with-mobile.html)
    * [On-Device Training](/docs/get-started/training-on-device.html)
    * [Large Model Training](/docs/get-started/training-pytorch.html)
  * [Tutorials](/docs/tutorials/)
    * [API Basics](/docs/tutorials/api-basics.html)
    * [Accelerate PyTorch](/docs/tutorials/accelerate-pytorch/)
      * [PyTorch Inference](/docs/tutorials/accelerate-pytorch/pytorch.html)
      * [Inference on multiple targets](/docs/tutorials/accelerate-pytorch/resnet-inferencing.html)
      * [Accelerate PyTorch Training](/docs/tutorials/accelerate-pytorch/ort-training.html)
    * [Accelerate TensorFlow](/docs/tutorials/tensorflow.html)
    * [Accelerate Hugging Face](/docs/tutorials/huggingface.html)
    * [Deploy on AzureML](/docs/tutorials/azureml.html)
    * [Deploy on mobile](/docs/tutorials/mobile/)
      * [Object detection and pose estimation with YOLOv8](/docs/tutorials/mobile/pose-detection.html)
      * [Mobile image recognition on Android](/docs/tutorials/mobile/deploy-android.html)
      * [Improve image resolution on mobile](/docs/tutorials/mobile/superres.html)
      * [Mobile objection detection on iOS](/docs/tutorials/mobile/deploy-ios.html)
      * [ORT Mobile Model Export Helpers](/docs/tutorials/mobile/helpers/)
    * [Web](/docs/tutorials/web/)
      * [Build a web app with ONNX Runtime](/docs/tutorials/web/build-web-app.html)
      * [The 'env' Flags and Session Options](/docs/tutorials/web/env-flags-and-session-options.html)
      * [Using WebGPU](/docs/tutorials/web/ep-webgpu.html)
      * [Using WebNN](/docs/tutorials/web/ep-webnn.html)
      * [Working with Large Models](/docs/tutorials/web/large-models.html)
      * [Performance Diagnosis](/docs/tutorials/web/performance-diagnosis.html)
      * [Deploying ONNX Runtime Web](/docs/tutorials/web/deploy.html)
      * [Troubleshooting](/docs/tutorials/web/trouble-shooting.html)
      * [Classify images with ONNX Runtime and Next.js](/docs/tutorials/web/classify-images-nextjs-github-template.html)
      * [Custom Excel Functions for BERT Tasks in JavaScript](/docs/tutorials/web/excel-addin-bert-js.html)
    * [Deploy on IoT and edge](/docs/tutorials/iot-edge/)
      * [IoT Deployment on Raspberry Pi](/docs/tutorials/iot-edge/rasp-pi-cv.html)
    * [Deploy traditional ML](/docs/tutorials/traditional-ml.html)
    * [Inference with C#](/docs/tutorials/csharp/)
      * [Basic C# Tutorial](/docs/tutorials/csharp/basic_csharp.html)
      * [Inference BERT NLP with C#](/docs/tutorials/csharp/bert-nlp-csharp-console-app.html)
      * [Configure CUDA for GPU with C#](/docs/tutorials/csharp/csharp-gpu.html)
      * [Image recognition with ResNet50v2 in C#](/docs/tutorials/csharp/resnet50_csharp.html)
      * [Stable Diffusion with C#](/docs/tutorials/csharp/stable-diffusion-csharp.html)
      * [Object detection in C# using OpenVINO](/docs/tutorials/csharp/yolov3_object_detection_csharp.html)
      * [Object detection with Faster RCNN in C#](/docs/tutorials/csharp/fasterrcnn_csharp.html)
    * [On-Device Training](/docs/tutorials/on-device-training/)
      * [Building an Android Application](/docs/tutorials/on-device-training/android-app.html)
      * [Building an iOS Application](/docs/tutorials/on-device-training/ios-app.html)
  * [API Docs](/docs/api/)
  * [Build ONNX Runtime](/docs/build/)
    * [Build for inferencing](/docs/build/inferencing.html)
    * [Build for training](/docs/build/training.html)
    * [Build with different EPs](/docs/build/eps.html)
    * [Build for web](/docs/build/web.html)
    * [Build for Android](/docs/build/android.html)
    * [Build for iOS](/docs/build/ios.html)
    * [Custom build](/docs/build/custom.html)
  * [Execution Providers](/docs/execution-providers/)
    * [NVIDIA - CUDA](/docs/execution-providers/CUDA-ExecutionProvider.html)
    * [NVIDIA - TensorRT](/docs/execution-providers/TensorRT-ExecutionProvider.html)
    * [NVIDIA - TensorRT RTX](/docs/execution-providers/TensorRTRTX-ExecutionProvider.html)
    * [Intel - OpenVINO™](/docs/execution-providers/OpenVINO-ExecutionProvider.html)
    * [Intel - oneDNN](/docs/execution-providers/oneDNN-ExecutionProvider.html)
    * [Windows - DirectML](/docs/execution-providers/DirectML-ExecutionProvider.html)
    * [Qualcomm - QNN](/docs/execution-providers/QNN-ExecutionProvider.html)
    * [Android - NNAPI](/docs/execution-providers/NNAPI-ExecutionProvider.html)
    * [Apple - CoreML](/docs/execution-providers/CoreML-ExecutionProvider.html)
    * [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html)
    * [AMD - ROCm](/docs/execution-providers/ROCm-ExecutionProvider.html)
    * [AMD - MIGraphX](/docs/execution-providers/MIGraphX-ExecutionProvider.html)
    * [AMD - Vitis AI](/docs/execution-providers/Vitis-AI-ExecutionProvider.html)
    * [Cloud - Azure](/docs/execution-providers/Azure-ExecutionProvider.html)
    * [Community-maintained](/docs/execution-providers/community-maintained/)
      * [Arm - ACL](/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html)
      * [Arm - Arm NN](/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html)
      * [Apache - TVM](/docs/execution-providers/community-maintained/TVM-ExecutionProvider.html)
      * [Rockchip - RKNPU](/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html)
      * [Huawei - CANN](/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html)
    * [Add a new provider](/docs/execution-providers/add-execution-provider.html)
    * [EP Context Design](/docs/execution-providers/EP-Context-Design.html)
    * [Plugin Execution Provider Libraries](/docs/execution-providers/plugin-ep-libraries/)
      * [Usage](/docs/execution-providers/plugin-ep-libraries/usage.html)
      * [Development](/docs/execution-providers/plugin-ep-libraries/development.html)
      * [Testing](/docs/execution-providers/plugin-ep-libraries/testing.html)
      * [Packaging](/docs/execution-providers/plugin-ep-libraries/packaging.html)
  * [Generate API (Preview)](/docs/genai/)
    * [Tutorials](/docs/genai/tutorials/)
      * [Phi-3.5 vision tutorial](/docs/genai/tutorials/phi3-v.html)
      * [Phi-3 tutorial](/docs/genai/tutorials/phi3-python.html)
      * [Phi-2 tutorial](/docs/genai/tutorials/phi2-python.html)
      * [Run with LoRA adapters](/docs/genai/tutorials/finetune.html)
      * [DeepSeek-R1-Distill tutorial](/docs/genai/tutorials/deepseek-python.html)
      * [Run on Snapdragon devices](/docs/genai/tutorials/snapdragon.html)
    * [API docs](/docs/genai/api/)
      * [Python API](/docs/genai/api/python.html)
      * [C# API](/docs/genai/api/csharp.html)
      * [C API](/docs/genai/api/c.html)
      * [C++ API](/docs/genai/api/cpp.html)
      * [Java API](/docs/genai/api/java.html)
    * [How to](/docs/genai/howto/)
      * [Install](/docs/genai/howto/install.html)
      * [Build from source](/docs/genai/howto/build-from-source.html)
      * [Build models](/docs/genai/howto/build-model.html)
      * [Build models for Snapdragon](/docs/genai/howto/build-models-for-snapdragon.html)
      * [Troubleshoot](/docs/genai/howto/troubleshoot.html)
      * [Migrate](/docs/genai/howto/migrate.html)
      * [Past present share buffer](/docs/genai/howto/past-present-share-buffer.html)
    * [Reference](/docs/genai/reference/)
      * [Config reference](/docs/genai/reference/config.html)
      * [Adapter file spec](/docs/genai/reference/adapter.html)
  * [Extensions](/docs/extensions/)
    * [Add Operators](/docs/extensions/add-op.html)
    * [Build](/docs/extensions/build.html)
  * [Performance](/docs/performance/)
    * [Tune performance](/docs/performance/tune-performance/)
      * [Profiling tools](/docs/performance/tune-performance/profiling-tools.html)
      * [Logging & Tracing](/docs/performance/tune-performance/logging_tracing.html)
      * [Memory consumption](/docs/performance/tune-performance/memory.html)
      * [Thread management](/docs/performance/tune-performance/threading.html)
      * [I/O Binding](/docs/performance/tune-performance/iobinding.html)
      * [Troubleshooting](/docs/performance/tune-performance/troubleshooting.html)
    * [Model optimizations](/docs/performance/model-optimizations/)
      * [Quantize ONNX models](/docs/performance/model-optimizations/quantization.html)
      * [Float16 and mixed precision models](/docs/performance/model-optimizations/float16.html)
      * [Graph optimizations](/docs/performance/model-optimizations/graph-optimizations.html)
      * [ORT model format](/docs/performance/model-optimizations/ort-format-models.html)
      * [ORT model format runtime optimization](/docs/performance/model-optimizations/ort-format-model-runtime-optimization.html)
    * [Transformers optimizer](/docs/performance/transformers-optimization.html)
    * [End to end optimization with Olive](/docs/performance/olive.html)
    * [Device tensors](/docs/performance/device-tensor.html)
  * [Ecosystem](/docs/ecosystem/)
    * [Azure Container for PyTorch (ACPT)](/docs/ecosystem/acpt.html)
  * [Reference](/docs/reference/)
    * [Releases](/docs/reference/releases-servicing.html)
    * [Compatibility](/docs/reference/compatibility.html)
    * [Operators](/docs/reference/operators/)
      * [Operator kernels](/docs/reference/operators/OperatorKernels.html)
      * [Contrib operators](/docs/reference/operators/ContribOperators.html)
      * [Custom operators](/docs/reference/operators/add-custom-op.html)
      * [Reduced operator config file](/docs/reference/operators/reduced-operator-config-file.html)
    * [Architecture](/docs/reference/high-level-design.html)
    * [Citing ONNX Runtime](/docs/reference/citing.html)
  * [Dependency Management in ONNX Runtime](/docs/build/dependencies.html)

  * [ ONNX Runtime Docs on GitHub ](https://github.com/microsoft/onnxruntime/tree/gh-pages)

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll. 

Search onnxruntime

  * [ ONNX Runtime ](/)
  * [ Install ](/docs/install/)
  * [ Get Started ](/docs/get-started/)
  * [ Tutorials ](/docs/tutorials/)
  * [ API Docs ](/docs/api/)
  * [ YouTube ](https://www.youtube.com/onnxruntime)
  * [ GitHub ](https://github.com/microsoft/onnxruntime)

  1. [Execution Providers](/docs/execution-providers/)
  2. NVIDIA - TensorRT

#  TensorRT Execution Provider 

With the TensorRT execution provider, the ONNX Runtime delivers better inferencing performance on the same hardware compared to generic GPU acceleration.

The TensorRT execution provider in the ONNX Runtime makes use of NVIDIA’s [TensorRT](https://developer.nvidia.com/tensorrt) Deep Learning inferencing engine to accelerate ONNX model in their family of GPUs. Microsoft and NVIDIA worked closely to integrate the TensorRT execution provider with ONNX Runtime.

##  Contents 

  * Install
  * Build from source
  * Requirements
  * Usage
    * C/C++
    * Python
  * Configurations
    * Click below for Python API example:
    * Click below for C++ API example:
    * Scenario
    * Execution Provider Options
    * Environment Variables(deprecated)
  * TensorRT EP Caches
    * Caches can help reduce session creation time from minutes to seconds
    * How to set caches
    * More about Embedded engine model / EPContext model
  * Performance Tuning
    * Shape Inference for TensorRT Subgraphs
    * TensorRT Plugins Support
    * Timing cache
    * Explicit shape range for dynamic shape input
    * Data-dependant shape (DDS) ops
  * Samples
  * Known Issues

##  Install 

Please select the GPU (CUDA/TensorRT) version of Onnx Runtime: https://onnxruntime.ai/docs/install. Pre-built packages and Docker images are available for Jetpack in the [Jetson Zoo](https://elinux.org/Jetson_Zoo#ONNX_Runtime).

##  Build from source 

See [Build instructions](/docs/build/eps.html#tensorrt).

##  Requirements 

Note:

Starting with version 1.19, **CUDA 12** becomes the default version when distributing ONNX Runtime GPU packages.

Starting with ORT 1.22, only CUDA 12 GPU packages are released.

ONNX Runtime | TensorRT | CUDA  
---|---|---  
main | 10.9 | **12.0-12.8**  
1.22 | 10.9 | **12.0-12.8**  
1.21 | 10.8 | **12.0-12.8** , 11.8  
1.20 | 10.4 | **12.0-12.6** , 11.8  
1.19 | 10.2 | **12.0-12.6** , 11.8  
1.18 | 10.0 | 11.8, 12.0-12.6  
1.17 | 8.6 | 11.8, 12.0-12.6  
1.16 | 8.6 | 11.8  
1.15 | 8.6 | 11.8  
1.14 | 8.5 | 11.6  
1.12-1.13 | 8.4 | 11.4  
1.11 | 8.2 | 11.4  
1.10 | 8.0 | 11.4  
1.9 | 8.0 | 11.4  
1.7-1.8 | 7.2 | 11.0.3  
1.5-1.6 | 7.1 | 10.2  
1.2-1.4 | 7.0 | 10.1  
1.0-1.1 | 6.0 | 10.0  
  
For more details on CUDA/cuDNN versions, please see [CUDA EP requirements](/docs/execution-providers/CUDA-ExecutionProvider.html#requirements).

##  Usage 

###  C/C++ 
    
    
    Ort::Env env = Ort::Env{ORT_LOGGING_LEVEL_ERROR, "Default"};
    Ort::SessionOptions sf;
    int device_id = 0;
    Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_Tensorrt(sf, device_id));
    Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_CUDA(sf, device_id));
    Ort::Session session(env, model_path, sf);
    

The C API details are [here](/docs/get-started/with-c.html).

###  Python 

To use TensorRT execution provider, you must explicitly register TensorRT execution provider when instantiating the `InferenceSession`. Note that it is recommended you also register `CUDAExecutionProvider` to allow Onnx Runtime to assign nodes to CUDA execution provider that TensorRT does not support.
    
    
    import onnxruntime as ort
    # set providers to ['TensorrtExecutionProvider', 'CUDAExecutionProvider'] with TensorrtExecutionProvider having the higher priority.
    sess = ort.InferenceSession('model.onnx', providers=['TensorrtExecutionProvider', 'CUDAExecutionProvider'])
    

##  Configurations 

There are two ways to configure TensorRT settings, either by [TensorRT Execution Provider Session Option](/docs/execution-providers/TensorRT-ExecutionProvider.html#execution-provider-options) or [Environment Variables(deprecated)](/docs/execution-providers/TensorRT-ExecutionProvider.html#environment-variablesdeprecated).

Here are examples and different [scenarios](/docs/execution-providers/TensorRT-ExecutionProvider.html#scenario) to set TensorRT EP session options:

####  Click below for Python API example: 
    
    
    import onnxruntime as ort
    
    model_path = '<path to model>'
    
    # note: for bool type options in python API, set them as False/True
    providers = [
        ('TensorrtExecutionProvider', {
            'device_id': 0,                       # Select GPU to execute
            'trt_max_workspace_size': 2147483648, # Set GPU memory usage limit
            'trt_fp16_enable': True,              # Enable FP16 precision for faster inference  
        }),
        ('CUDAExecutionProvider', {
            'device_id': 0,
            'arena_extend_strategy': 'kNextPowerOfTwo',
            'gpu_mem_limit': 2 * 1024 * 1024 * 1024,
            'cudnn_conv_algo_search': 'EXHAUSTIVE',
            'do_copy_in_default_stream': True,
        })
    ]
    
    sess_opt = ort.SessionOptions()
    sess = ort.InferenceSession(model_path, sess_options=sess_opt, providers=providers)
    

####  Click below for C++ API example: 
    
    
    Ort::SessionOptions session_options;
    
    const auto& api = Ort::GetApi();
    OrtTensorRTProviderOptionsV2* tensorrt_options;
    Ort::ThrowOnError(api.CreateTensorRTProviderOptions(&tensorrt_options));
    
    std::vector<const char*> option_keys = {
        "device_id",
        "trt_max_workspace_size",
        "trt_max_partition_iterations",
        "trt_min_subgraph_size",
        "trt_fp16_enable",
        "trt_int8_enable",
        "trt_int8_use_native_calibration_table",
        "trt_dump_subgraphs",
        // below options are strongly recommended !
        "trt_engine_cache_enable",
        "trt_engine_cache_path",
        "trt_timing_cache_enable",
        "trt_timing_cache_path",
    };
    std::vector<const char*> option_values = {
        "1",
        "2147483648",
        "10",
        "5",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "/path/to/cache",
        "1",
        "/path/to/cache", // can be same as the engine cache folder
    };
    
    Ort::ThrowOnError(api.UpdateTensorRTProviderOptions(tensorrt_options,
                                                        option_keys.data(), option_values.data(), option_keys.size()));
    
    
    cudaStream_t cuda_stream;
    cudaStreamCreate(&cuda_stream);
    // this implicitly sets "has_user_compute_stream"
    Ort::ThrowOnError(api.UpdateTensorRTProviderOptionsWithValue(cuda_options, "user_compute_stream", cuda_stream))
    
    session_options.AppendExecutionProvider_TensorRT_V2(*tensorrt_options);
    /// below code can be used to print all options
    OrtAllocator* allocator;
    char* options;
    Ort::ThrowOnError(api.GetAllocatorWithDefaultOptions(&allocator));
    Ort::ThrowOnError(api.GetTensorRTProviderOptionsAsString(tensorrt_options,          allocator, &options));
    
    

###  Scenario 

Scenario | TensorRT EP Session Option | Type  
---|---|---  
**Device and Compute Configuration** |  |   
Specify GPU id for execution | [device_id](/docs/execution-providers/TensorRT-ExecutionProvider.html#device_id) | int  
Set custom compute stream for GPU operations | [user_compute_stream](/docs/execution-providers/TensorRT-ExecutionProvider.html#user_compute_stream) | string  
|  |   
**Engine Caching and Compatibility** |  |   
Enable caching of TensorRT engines | [trt_engine_cache_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_engine_cache_enable) | bool  
Set path to store cached TensorRT engines | [trt_engine_cache_path](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_engine_cache_path) | string  
Set prefix for cached engine files | [trt_engine_cache_prefix](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_engine_cache_prefix) | string  
Maximize engine compatibility across Ampere+ GPUs | [trt_engine_hw_compatible](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_engine_hw_compatible) | bool  
|  |   
**Precision and Performance** |  |   
Set TensorRT EP GPU memory usage limit | [trt_max_workspace_size](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_max_workspace_size) | int  
Enable FP16 precision for faster performance | [trt_fp16_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_fp16_enable) | bool  
Enable INT8 precision for quantized inference | [trt_int8_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_int8_enable) | bool  
Name INT8 calibration table for non-QDQ models | [trt_int8_calibration_table_name](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_int8_calibration_table_name) | string  
Use native TensorRT calibration tables | [trt_int8_use_native_calibration_table](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_int8_use_native_calibration_table) | bool  
Use heuristics to speed up engine builds | [trt_build_heuristics_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_build_heuristics_enable) | bool  
Enable sparsity to leverage zero values | [trt_sparsity_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_sparsity_enable) | bool  
Enable Deep Learning Accelerator (DLA) on edge SoC | [trt_dla_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_dla_enable) | bool  
Specify which DLA core to use | [trt_dla_core](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_dla_core) | int  
|  |   
**Subgraph and Graph Optimization** |  |   
Limit partitioning iterations for model conversion | [trt_max_partition_iterations](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_max_partition_iterations) | int  
Set minimum size for subgraphs in partitioning | [trt_min_subgraph_size](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_min_subgraph_size) | int  
Dump optimized subgraphs for debugging | [trt_dump_subgraphs](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_dump_subgraphs) | bool  
Force sequential engine builds under multi-GPU | [trt_force_sequential_engine_build](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_force_sequential_engine_build) | bool  
Exclude specific op types from running on TRT | [trt_op_types_to_exclude](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_op_types_to_exclude) | string  
|  |   
**Advanced Configuration and Profiling** |  |   
Enable sharing of context memory between subgraphs | [trt_context_memory_sharing_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_context_memory_sharing_enable) | bool  
Force layer norm calculations to FP32 | [trt_layer_norm_fp32_fallback](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_layer_norm_fp32_fallback) | bool  
Capture CUDA graph for reduced launch overhead | [trt_cuda_graph_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_cuda_graph_enable) | bool  
Set optimization level for TensorRT builder | [trt_builder_optimization_level](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_builder_optimization_level) | int  
Set number of auxiliary streams for computation | [trt_auxiliary_streams](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_auxiliary_streams) | int  
Specify tactics sources for TensorRT | [trt_tactic_sources](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_tactic_sources) | string  
Add additional plugin library paths for TensorRT | [trt_extra_plugin_lib_paths](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_extra_plugin_lib_paths) | string  
Enable detailed logging of build steps | [trt_detailed_build_log](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_detailed_build_log) | bool  
|  |   
**Timing cache** |  |   
Enable use of timing cache to speed up builds | [trt_timing_cache_enable](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_timing_cache_enable) | bool  
Set path for storing timing cache | [trt_timing_cache_path](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_timing_cache_path) | string  
Force use of timing cache regardless of GPU match | [trt_force_timing_cache](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_force_timing_cache) | bool  
|  |   
**Dynamic Shape Profiling** |  |   
Define min shapes | [trt_profile_min_shapes](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_profile_min_shapes) | string  
Define max shapes | [trt_profile_max_shapes](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_profile_max_shapes) | string  
Define optimal shapes | [trt_profile_opt_shapes](/docs/execution-providers/TensorRT-ExecutionProvider.html#trt_profile_opt_shapes) | string  
  
> Note: for bool type options, assign them with **True** /**False** in python, or **1** /**0** in C++.

###  Execution Provider Options 

TensorRT configurations can be set by execution provider options. It’s useful when each model and inference session have their own configurations. In this case, execution provider option settings will override any environment variable settings. All configurations should be set explicitly, otherwise default value will be taken.

#####  device_id 

  * Description: GPU device ID.
  * Default value: 0

#####  user_compute_stream 

  * Description: define the compute stream for the inference to run on. It implicitly sets the `has_user_compute_stream` option. It cannot be set through `UpdateTensorRTProviderOptions`, but rather `UpdateTensorRTProviderOptionsWithValue`.

  * This cannot be used in combination with an external allocator.

  * This can also be set using the python API.

    * i.e The cuda stream captured from pytorch can be passed into ORT-TRT. Click below to check sample code:
          
          import onnxruntime as ort
          import torch
          ...
          sess = ort.InferenceSession('model.onnx')
          if torch.cuda.is_available():
              s = torch.cuda.Stream()
              option = {"user_compute_stream": str(s.cuda_stream)}
              sess.set_providers(["TensorrtExecutionProvider"], [option])
              options = sess.get_provider_options()
              
              assert "TensorrtExecutionProvider" in options
              assert options["TensorrtExecutionProvider"].get("user_compute_stream", "") == str(s.cuda_stream)
              assert options["TensorrtExecutionProvider"].get("has_user_compute_stream", "") == "1"
          ...
          

  * To take advantage of user compute stream, it is recommended to use [I/O Binding](https://onnxruntime.ai/docs/api/python/api_summary.html#data-on-device) to bind inputs and outputs to tensors in device.

#####  trt_max_workspace_size 

  * Description: maximum workspace size for TensorRT engine.

  * Default value: 1073741824 (1GB).

#####  trt_max_partition_iterations 

  * Description: maximum number of iterations allowed in model partitioning for TensorRT.
  * If target model can’t be successfully partitioned when the maximum number of iterations is reached, the whole model will fall back to other execution providers such as CUDA or CPU.
  * Default value: 1000.

#####  trt_min_subgraph_size 

  * Description: minimum node size in a subgraph after partitioning.

  * Subgraphs with smaller size will fall back to other execution providers.
  * Default value: 1.

#####  trt_fp16_enable 

  * Description: enable FP16 mode in TensorRT.

> Note: not all Nvidia GPUs support FP16 precision.

#####  trt_int8_enable 

  * Description: enable INT8 mode in TensorRT.

> Note: not all Nvidia GPUs support INT8 precision.

#####  trt_int8_calibration_table_name 

  * Description: specify INT8 calibration table file for non-QDQ models in INT8 mode.

> Note: calibration table should not be provided for QDQ model because TensorRT doesn’t allow calibration table to be loded if there is any Q/DQ node in the model. By default the name is empty.

#####  trt_int8_use_native_calibration_table 

  * Description: select what calibration table is used for non-QDQ models in INT8 mode.

    * If `True`, native TensorRT generated calibration table is used;
    * If `False`, ONNXRUNTIME tool generated calibration table is used.

> Note: Please copy up-to-date calibration table file to `trt_engine_cache_path` before inference. Calibration table is specific to models and calibration data sets. Whenever new calibration table is generated, old file in the path should be cleaned up or be replaced.

#####  trt_dla_enable 

  * Description: enable DLA (Deep Learning Accelerator).

> Note: Not all Nvidia GPUs support DLA.

#####  trt_dla_core 

  * Description: specify DLA core to execute on. Default value: 0.

#####  trt_engine_cache_enable 

  * Description: enable TensorRT engine caching.

  * The purpose of using engine caching is to save engine build time in the case that TensorRT may take long time to optimize and build engine.

  * Engine will be cached when it’s built for the first time so next time when new inference session is created the engine can be loaded directly from cache. In order to validate that the loaded engine is usable for current inference, engine profile is also cached and loaded along with engine. If current input shapes are in the range of the engine profile, the loaded engine can be safely used. Otherwise if input shapes are out of range, profile cache will be updated to cover the new shape and engine will be recreated based on the new profile (and also refreshed in the engine cache).

    * Note each engine is created for specific settings such as model path/name, precision (FP32/FP16/INT8 etc), workspace, profiles etc, and specific GPUs and it’s not portable, so it’s essential to make sure those settings are not changing, otherwise the engine needs to be rebuilt and cached again.

> **Warning: Please clean up any old engine and profile cache files (.engine and .profile) if any of the following changes:**
> 
>     * Model changes (if there are any changes to the model topology, opset version, operators etc.)
>     * ORT version changes (i.e. moving from ORT version 1.8 to 1.9)
>     * TensorRT version changes (i.e. moving from TensorRT 7.0 to 8.0)

#####  trt_engine_cache_path 

  * Description: specify path for TensorRT engine and profile files if `trt_engine_cache_enable` is `True`, or path for INT8 calibration table file if `trt_int8_enable` is `True`.

#####  trt_engine_cache_prefix 

  * Description: customize engine cache prefix when `trt_engine_cache_enable` is `True`. 
    * ORT-TRT will only reuse existing engine cache with customized prefix if the same prefix is assigned in `trt_engine_cache_prefix`. If this option is empty, new engine cache with default prefix will be generated.

#####  trt_dump_subgraphs 

  * Description: dumps the subgraphs that are transformed into TRT engines in onnx format to the filesystem. 
    * This can help debugging subgraphs, e.g. by using `trtexec --onnx my_model.onnx` and check the outputs of the parser.

#####  trt_force_sequential_engine_build 

  * Description: sequentially build TensorRT engines across provider instances in multi-GPU environment.

#####  trt_context_memory_sharing_enable 

  * Description: share execution context memory between TensorRT subgraphs.

#####  trt_layer_norm_fp32_fallback 

  * Description: force Pow + Reduce ops in layer norm to FP32.

#####  trt_timing_cache_enable 

  * Description: enable TensorRT timing cache. 
    * Check Timing cache for details.

#####  trt_timing_cache_path 

  * Description: specify path for TensorRT timing cache if `trt_timing_cache_enable` is `True`. 
    * Not specifying a `trt_timing_cache_path` will result in using the working directory

#####  trt_force_timing_cache 

  * Description: force the TensorRT timing cache to be used even if device profile does not match. 
    * A perfect match is only the exact same GPU model as the on that produced the timing cache.

#####  trt_detailed_build_log 

  * Description: enable detailed build step logging on TensorRT EP with timing for each engine build.

#####  trt_build_heuristics_enable 

  * Description: build engine using heuristics to reduce build time.

#####  trt_cuda_graph_enable 

  * Description: this will capture a [CUDA graph](https://developer.nvidia.com/blog/cuda-graphs/) which can drastically help for a network with many small layers as it reduces launch overhead on the CPU.

#####  trt_sparsity_enable 

  * Description: control if sparsity can be used by TRT. 
    * Check `--sparsity` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

#####  trt_builder_optimization_level 

  * Description: set the builder optimization level.

> WARNING: levels below 3 do not guarantee good engine performance, but greatly improve build time. Default 3, valid range [0-5]. Check `--builderOptimizationLevel` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

#####  trt_auxiliary_streams 

  * Description: set maximum number of auxiliary streams per inference stream. 
    * Setting this value to 0 will lead to optimal memory usage.
    * Default -1 = heuristics.
    * Check `--maxAuxStreams` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

#####  trt_tactic_sources 

  * Description: specify the tactics to be used by adding (+) or removing (-) tactics from the default tactic sources (default = all available tactics) 
    * e.g. “-CUDNN,+CUBLAS” available keys: “CUBLAS”, “CUBLAS_LT”, “CUDNN” or “EDGE_MASK_CONVOLUTIONS”.

#####  trt_extra_plugin_lib_paths 

  * Description: specify extra TensorRT plugin library paths. 
    * ORT TRT by default supports any TRT plugins registered in TRT registry in TRT plugin library (i.e., `libnvinfer_plugin.so`).
    * Moreover, if users want to use other TRT plugins that are not in TRT plugin library, 
      * for example, FasterTransformer has many TRT plugin implementations for different models, user can specify like this `ORT_TENSORRT_EXTRA_PLUGIN_LIB_PATHS=libvit_plugin.so;libvit_int8_plugin.so`.

#####  trt_profile_min_shapes 

#####  trt_profile_max_shapes 

#####  trt_profile_opt_shapes 

  * Description: build with dynamic shapes using a profile with the min/max/opt shapes provided. 
    * The format of the profile shapes is `input_tensor_1:dim_1xdim_2x...,input_tensor_2:dim_3xdim_4x...,...`
      * These three flags should all be provided in order to enable explicit profile shapes feature.
    * Check Explicit shape range for dynamic shape input and TRT doc [optimization profiles](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#opt_profiles) for more details.

#####  trt_engine_hw_compatible 

  * Description: enable Ampere+ hardware compatibility if `trt_engine_cache_enable` is enabled 
    * Hardware-compatible engines can be reused across all Ampere+ GPU environments (may have lower throughput and/or higher latency).
    * Engines will be generated and loaded with `sm80+` name suffix, instead of actual compute capacity.
    * Turing and former Nvidia GPU architecture and Nvidia Jetson Orin platform are not eligble to this option.

#####  trt_op_types_to_exclude 

  * Description: exclude specific op types from running on TRT. (Available in ORT 1.21.0) 
    * The format is `op_type_1,op_type_2,op_type_3...`
    * One use case is to mitigate the performance issue mentioned [below](https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.html#known-issues), it allows users to prevent DDS ops from running on TensorRT, ensuring they are executed by CUDA EP or CPU EP instead: 
          
          ./onnxruntime_perf_test -r 1 -e tensorrt -i "trt_op_types_to_exclude|NonMaxSuppression,NonZero,RoiAlign" /path/to/onnx/your_model.onnx
          

    * Another use case is experimenting assigning ops to CUDA EP vs TRT EP

###  Environment Variables(deprecated) 

Following environment variables can be set for TensorRT execution provider. Click below for more details.

  * `ORT_TENSORRT_MAX_WORKSPACE_SIZE`: maximum workspace size for TensorRT engine. Default value: 1073741824 (1GB).

  * `ORT_TENSORRT_MAX_PARTITION_ITERATIONS`: maximum number of iterations allowed in model partitioning for TensorRT. If target model can’t be successfully partitioned when the maximum number of iterations is reached, the whole model will fall back to other execution providers such as CUDA or CPU. Default value: 1000.

  * `ORT_TENSORRT_MIN_SUBGRAPH_SIZE`: minimum node size in a subgraph after partitioning. Subgraphs with smaller size will fall back to other execution providers. Default value: 1.

  * `ORT_TENSORRT_FP16_ENABLE`: Enable FP16 mode in TensorRT. 1: enabled, 0: disabled. Default value: 0. Note not all Nvidia GPUs support FP16 precision.

  * `ORT_TENSORRT_INT8_ENABLE`: Enable INT8 mode in TensorRT. 1: enabled, 0: disabled. Default value: 0. Note not all Nvidia GPUs support INT8 precision.

  * `ORT_TENSORRT_INT8_CALIBRATION_TABLE_NAME`: Specify INT8 calibration table file for non-QDQ models in INT8 mode. Note calibration table should not be provided for QDQ model because TensorRT doesn’t allow calibration table to be loded if there is any Q/DQ node in the model. By default the name is empty.

  * `ORT_TENSORRT_INT8_USE_NATIVE_CALIBRATION_TABLE`: Select what calibration table is used for non-QDQ models in INT8 mode. If 1, native TensorRT generated calibration table is used; if 0, ONNXRUNTIME tool generated calibration table is used. Default value: 0. 
    * **Note: Please copy up-to-date calibration table file to`ORT_TENSORRT_CACHE_PATH` before inference. Calibration table is specific to models and calibration data sets. Whenever new calibration table is generated, old file in the path should be cleaned up or be replaced.**
  * `ORT_TENSORRT_DLA_ENABLE`: Enable DLA (Deep Learning Accelerator). 1: enabled, 0: disabled. Default value: 0. Note not all Nvidia GPUs support DLA.

  * `ORT_TENSORRT_DLA_CORE`: Specify DLA core to execute on. Default value: 0.

  * `ORT_TENSORRT_ENGINE_CACHE_ENABLE`: Enable TensorRT engine caching. The purpose of using engine caching is to save engine build time in the case that TensorRT may take long time to optimize and build engine. Engine will be cached when it’s built for the first time so next time when new inference session is created the engine can be loaded directly from cache. In order to validate that the loaded engine is usable for current inference, engine profile is also cached and loaded along with engine. If current input shapes are in the range of the engine profile, the loaded engine can be safely used. Otherwise if input shapes are out of range, profile cache will be updated to cover the new shape and engine will be recreated based on the new profile (and also refreshed in the engine cache). Note each engine is created for specific settings such as model path/name, precision (FP32/FP16/INT8 etc), workspace, profiles etc, and specific GPUs and it’s not portable, so it’s essential to make sure those settings are not changing, otherwise the engine needs to be rebuilt and cached again. 1: enabled, 0: disabled. Default value: 0. 
    * **Warning: Please clean up any old engine and profile cache files (.engine and .profile) if any of the following changes:**
      * Model changes (if there are any changes to the model topology, opset version, operators etc.)
      * ORT version changes (i.e. moving from ORT version 1.8 to 1.9)
      * TensorRT version changes (i.e. moving from TensorRT 7.0 to 8.0)
      * Hardware changes. (Engine and profile files are not portable and optimized for specific Nvidia hardware)
  * `ORT_TENSORRT_CACHE_PATH`: Specify path for TensorRT engine and profile files if `ORT_TENSORRT_ENGINE_CACHE_ENABLE` is 1, or path for INT8 calibration table file if ORT_TENSORRT_INT8_ENABLE is 1.

  * `ORT_TENSORRT_DUMP_SUBGRAPHS`: Dumps the subgraphs that are transformed into TRT engines in onnx format to the filesystem. This can help debugging subgraphs, e.g. by using `trtexec --onnx my_model.onnx` and check the outputs of the parser. 1: enabled, 0: disabled. Default value: 0.

  * `ORT_TENSORRT_FORCE_SEQUENTIAL_ENGINE_BUILD`: Sequentially build TensorRT engines across provider instances in multi-GPU environment. 1: enabled, 0: disabled. Default value: 0.

  * `ORT_TENSORRT_CONTEXT_MEMORY_SHARING_ENABLE`: Share execution context memory between TensorRT subgraphs. Default 0 = false, nonzero = true.

  * `ORT_TENSORRT_LAYER_NORM_FP32_FALLBACK`: Force Pow + Reduce ops in layer norm to FP32. Default 0 = false, nonzero = true.

  * `ORT_TENSORRT_TIMING_CACHE_ENABLE`: Enable TensorRT timing cache. Default 0 = false, nonzero = true. Check Timing cache for details.

  * `ORT_TENSORRT_FORCE_TIMING_CACHE_ENABLE`: Force the TensorRT timing cache to be used even if device profile does not match. Default 0 = false, nonzero = true.

  * `ORT_TENSORRT_DETAILED_BUILD_LOG_ENABLE`: Enable detailed build step logging on TensorRT EP with timing for each engine build. Default 0 = false, nonzero = true.

  * `ORT_TENSORRT_BUILD_HEURISTICS_ENABLE`: Build engine using heuristics to reduce build time. Default 0 = false, nonzero = true.

  * `ORT_TENSORRT_SPARSITY_ENABLE`: Control if sparsity can be used by TRT. Default 0 = false, 1 = true. Check `--sparsity` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

  * `ORT_TENSORRT_BUILDER_OPTIMIZATION_LEVEL`: Set the builder optimization level. WARNING: levels below 3 do not guarantee good engine performance, but greatly improve build time. Default 3, valid range [0-5]. Check `--builderOptimizationLevel` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

  * `ORT_TENSORRT_AUXILIARY_STREAMS`: Set maximum number of auxiliary streams per inference stream. Setting this value to 0 will lead to optimal memory usage. Default -1 = heuristics. Check `--maxAuxStreams` in `trtexec` command-line flags for [details](https://docs.nvidia.com/deeplearning/tensorrt/latest/reference/command-line-programs.html#commonly-used-command-line-flags).

  * `ORT_TENSORRT_TACTIC_SOURCES`: Specify the tactics to be used by adding (+) or removing (-) tactics from the default tactic sources (default = all available tactics) e.g. “-CUDNN,+CUBLAS” available keys: “CUBLAS”, “CUBLAS_LT”, “CUDNN” or “EDGE_MASK_CONVOLUTIONS”.

  * `ORT_TENSORRT_EXTRA_PLUGIN_LIB_PATHS`: Specify extra TensorRT plugin library paths. ORT TRT by default supports any TRT plugins registered in TRT registry in TRT plugin library (i.e., `libnvinfer_plugin.so`). Moreover, if users want to use other TRT plugins that are not in TRT plugin library, for example, FasterTransformer has many TRT plugin implementations for different models, user can specify like this `ORT_TENSORRT_EXTRA_PLUGIN_LIB_PATHS=libvit_plugin.so;libvit_int8_plugin.so`.

  * `ORT_TENSORRT_PROFILE_MIN_SHAPES`, `ORT_TENSORRT_PROFILE_MAX_SHAPES` and `ORT_TENSORRT_PROFILE_OPT_SHAPES` : Build with dynamic shapes using a profile with the min/max/opt shapes provided. The format of the profile shapes is “input_tensor_1:dim_1xdim_2x…,input_tensor_2:dim_3xdim_4x…,…” and these three flags should all be provided in order to enable explicit profile shapes feature. Check Explicit shape range for dynamic shape input and TRT doc [optimization profiles](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#opt_profiles) for more details.

One can override default values by setting environment variables. e.g. on Linux:
    
    
    # Override default max workspace size to 2GB
    export ORT_TENSORRT_MAX_WORKSPACE_SIZE=2147483648
    
    # Override default maximum number of iterations to 10
    export ORT_TENSORRT_MAX_PARTITION_ITERATIONS=10
    
    # Override default minimum subgraph node size to 5
    export ORT_TENSORRT_MIN_SUBGRAPH_SIZE=5
    
    # Enable FP16 mode in TensorRT
    export ORT_TENSORRT_FP16_ENABLE=1
    
    # Enable INT8 mode in TensorRT
    export ORT_TENSORRT_INT8_ENABLE=1
    
    # Use native TensorRT calibration table
    export ORT_TENSORRT_INT8_USE_NATIVE_CALIBRATION_TABLE=1
    
    # Enable TensorRT engine caching
    export ORT_TENSORRT_ENGINE_CACHE_ENABLE=1
    # Please Note warning above. This feature is experimental.
    # Engine cache files must be invalidated if there are any changes to the model, ORT version, TensorRT version or if the underlying hardware changes. Engine files are not portable across devices.
    
    # Specify TensorRT cache path
    export ORT_TENSORRT_CACHE_PATH="/path/to/cache"
    
    # Dump out subgraphs to run on TensorRT
    export ORT_TENSORRT_DUMP_SUBGRAPHS=1
    
    # Enable context memory sharing between TensorRT subgraphs. Default 0 = false, nonzero = true
    export ORT_TENSORRT_CONTEXT_MEMORY_SHARING_ENABLE=1
    

##  TensorRT EP Caches 

There are three major TRT EP caches:

  * TRT timing cache
  * TRT engine cache
  * Embedded engine model / EPContext model

###  Caches can help reduce session creation time from minutes to seconds 

Following numbers are measured from initializing session with TRT EP for SD UNet model.

  * No cache (default) – 384 seconds 
    * The first run (warmup) can be very long because building engine involves exhaustive profiling for every kernels to select the optimal one.
  * Timing cache used – 42 seconds 
    * Keep layer-profiling information and reuse them to expedite build time
    * Timing cache can be shared across multiple models if layers are the same
  * Engine cache used – 9 seconds 
    * Serialize engine from memory to disk for later use
    * Skip entire engine build and deserialize engine cache to memory
  * Embedded engine used (no builder instantiation) - 1.9 seconds 
    * The serialized engine cache is wrapped inside an ONNX model
    * No builder will be instantiated, nor engine will be built
    * Quickly load engine with less processes needed

###  How to set caches 

  * Use Timing cache (.timing): 
    * `trt_timing_cache_enable = true`
    * `trt_timing_cache_path = .\`
    * `trt_force_timing_cache = true (accept slight GPU mismatch within CC)`
  * Use Engine Cache (.engine): 
    * `trt_engine_cache_enable = true`
    * `trt_engine_cache_path = .\trt_engines`
  * Use Embed Engine (_ctx.onnx): 
    * Get the embed engine model via warmup run with the original model
    * `trt_engine_cache_enable = true`
    * `trt_dump_ep_context_model = true`
    * `trt_ep_context_file_path = .\`
    * Will be generated with inputs/outputs identical to original model
    * Run the embed engine model as the original model !

The folder structure of the caches:

With the following command, the embedded engine model (`model_ctx.onnx`) will be generated along with the engine cache in the same directory.

Note: The example does not specify `trt_engine_cache_path` because `onnxruntime_perf_test` requires a specific folder structure to run the inference. However, we still recommend specifying `trt_engine_cache_path` to better organize the caches.
    
    
    $./onnxruntime_perf_test -e tensorrt -r 1 -i "trt_engine_cache_enable|true trt_dump_ep_context_model|true" /model_database/transformer_model/model.onnx
    

Once the inference is complete, the embedded engine model is saved to disk. User can then run this model just like the original one, but with a significantly quicker session creation time.
    
    
    $./onnxruntime_perf_test -e tensorrt -r 1 /model_database/transformer_model/model_ctx.onnx
    

###  More about Embedded engine model / EPContext model 

  * One constraint is that the entire model needs to be TRT eligible
  * When running the embedded engine model, the default setting is `trt_ep_context_embed_mode=0`, where the engine cache path is embedded and TRT EP will look for the engine cache on the disk. Alternatively, users can set `trt_ep_context_embed_mode=1`, embedding the entire engine binary data as a string in the model. However, this mode increases initialization time due to ORT graph optimization hashing the long string. Therefore, we recommend using `trt_ep_context_embed_mode=0`.
  * The default name of an embedded engine model will have `_ctx.onnx` appended to the end. Users can specify `trt_ep_context_file_path=my_ep_context_model.onnx` to overwrite this default name.
  * If an embedded engine is used the library **`nvinfer_builder_resource` of TensorRT is not required**, which is by far the largest library. This enables the case of shipping a minimal set of libraries in the case that a fixed set of models is used which are packaged as precompield engine.
  * Besides everything that embedded engines enable to accelerate the load time, they also **enable packaging an externally compiled engine** using e.g. `trtexec`. A [python script](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/tensorrt/gen_trt_engine_wrapper_onnx_model.py) that is capable of packaging such a precompiled engine into an ONNX file is included in the python tools.

##  Performance Tuning 

For performance tuning, please see guidance on this page: [ONNX Runtime Perf Tuning](/docs/performance/tune-performance/)

When/if using [onnxruntime_perf_test](https://github.com/microsoft/onnxruntime/tree/main/onnxruntime/test/perftest#onnxruntime-performance-test), use the flag `-e tensorrt`. Check below for sample.

###  Shape Inference for TensorRT Subgraphs 

If some operators in the model are not supported by TensorRT, ONNX Runtime will partition the graph and only send supported subgraphs to TensorRT execution provider. Because TensorRT requires that all inputs of the subgraphs have shape specified, ONNX Runtime will throw error if there is no input shape info. In this case please run shape inference for the entire model first by running script [here](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/symbolic_shape_infer.py) (Check below for sample).

###  TensorRT Plugins Support 

ORT TRT can leverage the TRT plugins which come with TRT plugin library in official release. To use TRT plugins, firstly users need to create the custom node (a one-to-one mapping to TRT plugin) with a registered plugin name and `trt.plugins` domain in the ONNX model. So, ORT TRT can recognize this custom node and pass the node together with the subgraph to TRT. Please see following python example to create a new custom node in the ONNX model:

Click below for Python API example:
    
    
    from onnx import TensorProto, helper
    
    def generate_model(model_name):
        nodes = [
            helper.make_node(
                "DisentangledAttention_TRT", # The registered name is from https://github.com/NVIDIA/TensorRT/blob/main/plugin/disentangledAttentionPlugin/disentangledAttentionPlugin.cpp#L36
                ["input1", "input2", "input3"],
                ["output"],
                "DisentangledAttention_TRT",
                domain="trt.plugins", # The domain has to be "trt.plugins"
                factor=0.123,
                span=128,
            ),
        ]
    
        graph = helper.make_graph(
            nodes,
            "trt_plugin_custom_op",
            [  # input
                helper.make_tensor_value_info("input1", TensorProto.FLOAT, [12, 256, 256]),
                helper.make_tensor_value_info("input2", TensorProto.FLOAT, [12, 256, 256]),
                helper.make_tensor_value_info("input3", TensorProto.FLOAT, [12, 256, 256]),
            ],
            [  # output
                helper.make_tensor_value_info("output", TensorProto.FLOAT, [12, 256, 256]),
            ],
        )
    
        model = helper.make_model(graph)
        onnx.save(model, model_name)
    

Note: If users want to use TRT plugins that are not in the TRT plugin library in official release, please see the ORT TRT provider option `trt_extra_plugin_lib_paths` for more details.

###  Timing cache 

Enabling `trt_timing_cache_enable` will enable ORT TRT to use TensorRT timing cache to accelerate engine build time on a device with the same compute capability. This will work across models as it simply stores kernel latencies for specific configurations and cubins (TRT 9.0+). Those files are usually very small (only a few KB or MB) which makes them very easy to ship with an application to accelerate the build time on the user end.

_Note:_ A timing cache can be used across one [GPU compute capability](https://developer.nvidia.com/cuda-gpus) similar to an engine. Nonetheless the preferred way is to use one per GPU model, but practice shows that sharing across one compute capability works well in most cases.

The following examples shows build time reduction with timing cache:

Model | no Cache | with Cache  
---|---|---  
efficientnet-lite4-11 | 34.6 s | 7.7 s  
yolov4 | 108.62 s | 9.4 s  
  
Click below for Python example:
    
    
    import onnxruntime as ort
    
    ort.set_default_logger_severity(0) # Turn on verbose mode for ORT TRT
    sess_options = ort.SessionOptions()
    
    trt_ep_options = {
        "trt_timing_cache_enable": True,
    }
    
    sess = ort.InferenceSession(
        "my_model.onnx",
        providers=[
            ("TensorrtExecutionProvider", trt_ep_options),
            "CUDAExecutionProvider",
        ],
    )
    
    # Once inference session initialization is done (assume no dynamic shape input, otherwise you must wait until inference run is done)
    # you can find timing cache is saved in the 'trt_engine_cache_path' directory, e.g., TensorrtExecutionProvider_cache_cc75.timing, please note
    # that the name contains information of compute capability.
    
    sess.run(
        None,
        {"input_ids": np.zeros((1, 77), dtype=np.int32)}
    )
    

###  Explicit shape range for dynamic shape input 

ORT TRT lets you explicitly specify min/max/opt shapes for each dynamic shape input through three provider options, `trt_profile_min_shapes`, `trt_profile_max_shapes` and `trt_profile_opt_shapes`. If these three provider options are not specified and model has dynamic shape input, ORT TRT will determine the min/max/opt shapes for the dynamic shape input based on incoming input tensor. The min/max/opt shapes are required for TRT optimization profile (An optimization profile describes a range of dimensions for each TRT network input and the dimensions that the auto-tuner will use for optimization. When using runtime dimensions, you must create at least one optimization profile at build time.)

To use the engine cache built with optimization profiles specified by explicit shape ranges, user still needs to provide those three provider options as well as engine cache enable flag. ORT TRT will firstly compare the shape ranges of those three provider options with the shape ranges saved in the .profile file, and then rebuild the engine if the shape ranges don’t match.

Click below for Python example:
    
    
    import onnxruntime as ort
    
    ort.set_default_logger_severity(0) # Turn on verbose mode for ORT TRT
    sess_options = ort.SessionOptions()
    
    trt_ep_options = {
        "trt_fp16_enable": True,
        "trt_engine_cache_enable": True,
        "trt_profile_min_shapes": "sample:2x4x64x64,encoder_hidden_states:2x77x768",
        "trt_profile_max_shapes": "sample:32x4x64x64,encoder_hidden_states:32x77x768",
        "trt_profile_opt_shapes": "sample:2x4x64x64,encoder_hidden_states:2x77x768",
    }
    
    sess = ort.InferenceSession(
        "my_model.onnx",
        providers=[
            ("TensorrtExecutionProvider", trt_ep_options),
            "CUDAExecutionProvider",
        ],
    )
    
    batch_size = 1
    unet_dim = 4
    max_text_len = 77
    embed_dim = 768
    latent_height = 64
    latent_width = 64
    
    args = {
        "sample": np.zeros(
            (2 * batch_size, unet_dim, latent_height, latent_width), dtype=np.float32
        ),
        "timestep": np.ones((1,), dtype=np.float32),
        "encoder_hidden_states": np.zeros(
            (2 * batch_size, max_text_len, embed_dim),
            dtype=np.float32,
        ),
    }
    sess.run(None, args)
    # you can find engine cache and profile cache are saved in the 'trt_engine_cache_path' directory, e.g.
    # TensorrtExecutionProvider_TRTKernel_graph_torch_jit_1843998305741310361_0_0_fp16.engine and TensorrtExecutionProvider_TRTKernel_graph_torch_jit_1843998305741310361_0_0_fp16.profile.
    
    

Please note that there is a constraint of using this explicit shape range feature, i.e., all the dynamic shape inputs should be provided with corresponding min/max/opt shapes.

###  Data-dependant shape (DDS) ops 

The DDS operations — _NonMaxSuppression_ , _NonZero_ , and _RoiAlign_ — have output shapes that are only determined at runtime.

To ensure DDS ops are executed by TRT-EP/TRT instead of CUDA EP or CPU EP, please check the following:

  * For TensorRT < 10.7: Build ORT with [onnx-tensorrt OSS parser](https://github.com/onnx/onnx-tensorrt) and use `10.X-GA-ORT-DDS` branch.
  * For TensorRT >= 10.7: By default, DDS ops will be executed by TRT.
  * For ORT: By default, ORT relies on the TRT parser to decide if DDS ops run with TRT. However, note that ORT 1.20.1 and 1.20.2 will **not** run DDS ops with TRT due to a [known performance issue](https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.html#known-issues).

##  Samples 

This example shows how to run the Faster R-CNN model on TensorRT execution provider.

  1. Download the Faster R-CNN onnx model from the ONNX model zoo [here](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/faster-rcnn).

  2. Infer shapes in the model by running the [shape inference script](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/symbolic_shape_infer.py)
         
         python symbolic_shape_infer.py --input /path/to/onnx/model/model.onnx --output /path/to/onnx/model/new_model.onnx --auto_merge
         

  3. To test model with sample input and verify the output, run `onnx_test_runner` under ONNX Runtime build directory.

> Models and test_data_set_ folder need to be stored under the same path. `onnx_test_runner` will test all models under this path.
         
         ./onnx_test_runner -e tensorrt /path/to/onnx/model/
         

  4. To test on model performance, run `onnxruntime_perf_test` on your shape-inferred Faster-RCNN model

> Download sample test data with model from [model zoo](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/faster-rcnn), and put test_data_set folder next to your inferred model
         
         # e.g.
          # -r: set up test repeat time
          # -e: set up execution provider
          # -i: set up params for execution provider options
          ./onnxruntime_perf_test -r 1 -e tensorrt -i "trt_fp16_enable|true" /path/to/onnx/your_inferred_model.onnx
         

Please see [this Notebook](https://github.com/microsoft/onnxruntime/blob/main/docs/python/notebooks/onnx-inference-byoc-gpu-cpu-aks.ipynb) for an example of running a model on GPU using ONNX Runtime through Azure Machine Learning Services.

##  Known Issues 

  * TensorRT 8.6 built-in parser and TensorRT oss parser behaves differently. Namely built-in parser cannot recognize some custom plugin ops while OSS parser can. See [EfficientNMS_TRT missing attribute class_agnostic w/ TensorRT 8.6 ](https://github.com/microsoft/onnxruntime/issues/16121).
  * There is a performance issue for TensorRT versions 10.0 to 10.5 when running models, such as Faster-RCNN, that: 
    * contain data-dependent shape (DDS) operations, like NonMaxSuppression, NonZero, and RoiAlign, and
    * DDS ops are executed with TRT

* * *

For documentation questions, please [file an issue](https://github.com/microsoft/onnxruntime/issues/new?assignees=&labels=documentation&projects=&template=02-documentation.yml&title=%5BDocumentation%5D+).

[Edit this page on GitHub](https://github.com/microsoft/onnxruntime/tree/gh-pages/docs/execution-providers/TensorRT-ExecutionProvider.md)

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll.
