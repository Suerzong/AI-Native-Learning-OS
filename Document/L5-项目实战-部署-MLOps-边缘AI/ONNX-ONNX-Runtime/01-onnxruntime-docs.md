Skip to main content Link Menu Expand (external link) Document Search Copy Copied [ ](/)

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

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll.  Search onnxruntime

  * [ ONNX Runtime ](/)
  * [ Install ](/docs/install/)
  * [ Get Started ](/docs/get-started/)
  * [ Tutorials ](/docs/tutorials/)
  * [ API Docs ](/docs/api/)
  * [ YouTube ](https://www.youtube.com/onnxruntime)
  * [ GitHub ](https://github.com/microsoft/onnxruntime)

#  Welcome to ONNX Runtime 

ONNX Runtime is a cross-platform machine-learning model accelerator, with a flexible interface to integrate hardware-specific libraries. ONNX Runtime can be used with models from PyTorch, Tensorflow/Keras, TFLite, scikit-learn, and other frameworks.

##  How to use ONNX Runtime 

|  [Get started with ORT](./get-started) |  [API Docs](./api)  
---|---  
[Tutorials](./tutorials) |  [Ecosystem](./ecosystem)  
[ONNX Runtime YouTube](https://www.youtube.com/channel/UC_SJk17KdRvDulXz-nc1uFg/featured) |   
  
##  Contribute and Customize 

[Build ORT Packages](./build) | [ONNX Runtime GitHub](https://github.com/microsoft/onnxruntime)  
---|---  
  
* * *

##  QuickStart Template 

[ORT Web JavaScript Site Template](https://github.com/microsoft/onnxruntime-nextjs-template) |  [ORT C# Console App Template](https://github.com/microsoft/onnxruntime-csharp-cv-template)  
---|---  
  
* * *

##  ONNX Runtime for Inferencing 

ONNX Runtime Inference powers machine learning models in key Microsoft products and services across Office, Azure, Bing, as well as dozens of community projects.

Examples use cases for ONNX Runtime Inferencing include:

  * Improve inference performance for a wide variety of ML models
  * Run on different hardware and operating systems
  * Train in Python but deploy into a C#/C++/Java app
  * Train and perform inference with models created in different frameworks

###  How it works 

The premise is simple.

  1. **Get a model.** This can be trained from any framework that supports export/conversion to ONNX format. See the [tutorials](./tutorials) for some of the popular frameworks/libraries.
  2. **Load and run the model with ONNX Runtime.** See the [basic tutorials](./tutorials/api-basics) for running models in different languages.
  3. **_(Optional)_ Tune performance using various runtime configurations or hardware accelerators.** There are lots of options here - see the [Performance section](./performance) as a starting point.

Even without step 3, ONNX Runtime will often provide performance improvements compared to the original framework.

ONNX Runtime applies a number of graph optimizations on the model graph then partitions it into subgraphs based on available hardware-specific accelerators. Optimized computation kernels in core ONNX Runtime provide performance improvements and assigned subgraphs benefit from further acceleration from each [Execution Provider](./execution-providers).

###  Model Validation 

You are responsible for testing and validating any model you use with ONNX Runtime, including its accuracy, performance, and suitability for your intended use case. ONNX Runtime will validate that the model conforms to the [ONNX](https://onnx.ai/onnx/index.html) specification. It is, however, possible to construct a malicious model that, for example, consumes large amounts of memory or compute resources unnecessarily. If you are using a model from an untrusted source, we recommend inspecting the model and testing it in a safe environment before using it in production.

* * *

##  ONNX Runtime for Training 

  * [Large Model Training](/docs/get-started/training-pytorch.html)
  * [On-Device Training](/docs/get-started/training-on-device.html)

* * *

For documentation questions, please [file an issue](https://github.com/microsoft/onnxruntime/issues/new?assignees=&labels=documentation&projects=&template=02-documentation.yml&title=%5BDocumentation%5D+).

[Edit this page on GitHub](https://github.com/microsoft/onnxruntime/tree/gh-pages/docs/index.md)

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll.
