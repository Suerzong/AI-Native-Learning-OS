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

#  ONNX Runtime Execution Providers 

ONNX Runtime works with different hardware acceleration libraries through its extensible **Execution Providers** (EP) framework to optimally execute the ONNX models on the hardware platform. This interface enables flexibility for the AP application developer to deploy their ONNX models in different environments in the cloud and the edge and optimize the execution by taking advantage of the compute capabilities of the platform.

ONNX Runtime works with the execution provider(s) using the `GetCapability()` interface to allocate specific nodes or sub-graphs for execution by the EP library in supported hardware. The EP libraries that are pre-installed in the execution environment process and execute the ONNX sub-graph on the hardware. This architecture abstracts out the details of the hardware specific libraries that are essential to optimize the execution of deep neural networks across hardware platforms like CPU, GPU, FPGA or specialized NPUs.

ONNX Runtime supports many different execution providers today. Some of the EPs are in production for live service, while others are released in preview to enable developers to develop and customize their application using the different options.

##  Summary of supported Execution Providers 

CPU | GPU | IoT/Edge/Mobile | Other  
---|---|---|---  
Default CPU | [NVIDIA CUDA](/docs/execution-providers/CUDA-ExecutionProvider.html) | [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [Rockchip NPU](/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html) (_preview_)  
[Intel DNNL](/docs/execution-providers/oneDNN-ExecutionProvider.html) | [NVIDIA TensorRT](/docs/execution-providers/TensorRT-ExecutionProvider.html) | [Arm Compute Library](/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html) (_preview_) | [Xilinx Vitis-AI](/docs/execution-providers/Vitis-AI-ExecutionProvider.html) (_preview_)  
[TVM](/docs/execution-providers/community-maintained/TVM-ExecutionProvider.html) (_preview_) | [DirectML](/docs/execution-providers/DirectML-ExecutionProvider.html) | [Android Neural Networks API](/docs/execution-providers/NNAPI-ExecutionProvider.html) | [Huawei CANN](/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html) (_preview_)  
[Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [AMD MIGraphX](/docs/execution-providers/MIGraphX-ExecutionProvider.html) | [Arm NN](/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html) (_preview_) | [AZURE](/docs/execution-providers/Azure-ExecutionProvider.html) (_preview_)  
[XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html) | [Intel OpenVINO](/docs/execution-providers/OpenVINO-ExecutionProvider.html) | [CoreML](/docs/execution-providers/CoreML-ExecutionProvider.html) (_preview_) |   
[AMD ROCm](/docs/execution-providers/ROCm-ExecutionProvider.html)(_deprecated_) | [Qualcomm QNN](/docs/execution-providers/QNN-ExecutionProvider.html) | [XNNPACK](/docs/execution-providers/Xnnpack-ExecutionProvider.html) |   
  
##  Add an Execution Provider 

Developers of specialized HW acceleration solutions can integrate with ONNX Runtime to execute ONNX models on their stack. To create an EP to interface with ONNX Runtime you must first identify a unique name for the EP. See: [Add a new execution provider](/docs/execution-providers/add-execution-provider.html) for detailed instructions.

##  Build ONNX Runtime package with EPs 

The ONNX Runtime package can be built with any combination of the EPs along with the default CPU execution provider. **Note** that if multiple EPs are combined into the same ONNX Runtime package then all the dependent libraries must be present in the execution environment. The steps for producing the ONNX Runtime package with different EPs is documented [here](/docs/build/inferencing.html).

##  APIs for Execution Provider 

The same ONNX Runtime API is used across all EPs. This provides the consistent interface for applications to run with different HW acceleration platforms. The APIs to set EP options are available across Python, C/C++/C#, Java and node.js.

**Note** we are updating our API support to get parity across all language binding and will update specifics here.
    
    
    `get_providers`: Return list of registered execution providers.
    `get_provider_options`: Return the registered execution providers' configurations.
    `set_providers`: Register the given list of execution providers. The underlying session is re-created. 
        The list of providers is ordered by Priority. For example ['CUDAExecutionProvider', 'CPUExecutionProvider']
        means execute a node using CUDAExecutionProvider if capable, otherwise execute using CPUExecutionProvider.
    

##  Use Execution Providers 
    
    
    import onnxruntime as rt
    
    #define the priority order for the execution providers
    # prefer CUDA Execution Provider over CPU Execution Provider
    EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']
    
    # initialize the model.onnx
    sess = rt.InferenceSession("model.onnx", providers=EP_list)
    
    # get the outputs metadata as a list of :class:`onnxruntime.NodeArg`
    output_name = sess.get_outputs()[0].name
    
    # get the inputs metadata as a list of :class:`onnxruntime.NodeArg`
    input_name = sess.get_inputs()[0].name
    
    # inference run using image_data as the input to the model 
    detections = sess.run([output_name], {input_name: image_data})[0]
    
    print("Output shape:", detections.shape)
    
    # Process the image to mark the inference points 
    image = post.image_postprocess(original_image, input_size, detections)
    image = Image.fromarray(image)
    image.save("kite-with-objects.jpg")
    
    # Update EP priority to only CPUExecutionProvider
    sess.set_providers(['CPUExecutionProvider'])
    
    cpu_detection = sess.run(...)
    
    

* * *

## Table of contents

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
  * [Add a new provider](/docs/execution-providers/add-execution-provider.html)
  * [EP Context Design](/docs/execution-providers/EP-Context-Design.html)
  * [Plugin Execution Provider Libraries](/docs/execution-providers/plugin-ep-libraries/)

* * *

For documentation questions, please [file an issue](https://github.com/microsoft/onnxruntime/issues/new?assignees=&labels=documentation&projects=&template=02-documentation.yml&title=%5BDocumentation%5D+).

[Edit this page on GitHub](https://github.com/microsoft/onnxruntime/tree/gh-pages/docs/execution-providers/index.md)

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll.
