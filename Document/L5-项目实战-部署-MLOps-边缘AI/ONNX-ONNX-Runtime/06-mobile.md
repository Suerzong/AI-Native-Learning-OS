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

  1. [Tutorials](/docs/tutorials/)
  2. Deploy on mobile

#  How to develop a mobile application with ONNX Runtime 

ONNX Runtime gives you a variety of options to add machine learning to your mobile application. This page outlines the flow through the development process. You can also check out the tutorials in this section:

  * [Build an objection detection application on iOS](/docs/tutorials/mobile/deploy-ios.html)
  * [Build an image classification application on Android](/docs/tutorials/mobile/deploy-android.html)
  * [Build an super resolution application on iOS](/docs/tutorials/mobile/superres.html#ios-app)
  * [Build an super resolution application on Android](/docs/tutorials/mobile/superres.html#android-app)

##  ONNX Runtime mobile application development flow 

###  Obtain a model 

The first step in developing your mobile machine learning application is to obtain a model.

You need to understand your mobile app’s scenario and get an ONNX model that is appropriate for that scenario. For example, does the app classify images, do object detection in a video stream, summarize or predict text, or do numerical prediction.

To run on ONNX Runtime mobile, the model is required to be in ONNX format. ONNX models can be obtained from the [ONNX model zoo](https://github.com/onnx/models). If your model is not already in ONNX format, you can convert it to ONNX from PyTorch, TensorFlow and other formats using one of the converters.

Because the model is loaded and run on device, the model must fit on the device disk and be able to be loaded into the device’s memory.

###  Develop the application 

Once you have a model, you can load and run it using the ONNX Runtime API.

Which language bindings and runtime package you use depends on your chosen development environment and the target(s) you are developing for.

  * Android Java/C/C++: onnxruntime-android package
  * iOS C/C++: onnxruntime-c package
  * iOS Objective-C: onnxruntime-objc package
  * Android and iOS C# in MAUI/Xamarin: [Microsoft.ML.OnnxRuntime](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime/) and [Microsoft.ML.OnnxRuntime.Managed](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.Managed/)

See the [install guide](https://onnxruntime.ai/docs/install/#install-on-web-and-mobile) for package specific instructions.

The above packages all contain the full ONNX Runtime feature and operator set and support for the ONNX format. We recommend you start with these to develop your application. Further optimizations may be required. These are detailed below.

You have a choice of hardware accelerators to use in your app, depending on the target platform:

  * All targets have support for CPU and this is the default
  * Applications that run on Android also have support for NNAPI and XNNPACK
  * Applications that run on iOS also have support for CoreML and XNNPACK

Accelerators are called Execution Providers in ONNX Runtime.

If the model is quantized, start with the CPU Execution Provider. If the model is not quantized start with XNNPACK. These are the simplest and most consistent as everything is running on CPU.

If CPU/XNNPACK do not meet the application’s performance results, then try NNAPI/CoreML. Performance with these execution providers is device and model specific. If the model is broken into multiple partitions due to the model using operators that the execution provider doesn’t support (e.g., due to older NNAPI versions), performance may degrade.

Specific execution providers are configured in the SessionOptions, when the ONNXRuntime session is created and the model is loaded. For more detail, see your language [API docs](../../api).

###  Measure the application’s performance 

Measure the application’s performance against the requirements of your target platform. This includes:

  * application binary size
  * model size
  * application latency
  * power consumption

If the application does not meet its requirements, there are optimizations that can be applied.

###  Optimize your application 

####  Reduce model size 

One method of reducing model size is to quantize the model. This reduces an original model with 32-bit weights by approximately a factor of 4, as the weights are reduced to 8-bit. See the ONNX Runtime [quantization guide](/docs/performance/model-optimizations/quantization.html) for instructions on how to do this.

Another way of reducing the model size is to find a new model with the same inputs, outputs and architecture that has already been optimized for mobile. For example: MobileNet and MobileBert.

####  Reduce application binary size 

To reduce the ONNX Runtime binary size, you can build a custom runtime based on your model(s).

Refer to the process to build a [custom runtime](/docs/build/custom.html).

One of the outputs of the ORT format conversion is a build configuration file, containing a list of operators from your model(s) and their types. You can use this configuration file as input to the custom runtime binary build.

To give an idea of the binary size difference between the pre-built package and a custom build:

File | 1.18.0 pre-built package size (bytes) | 1.18.0 custom build size (bytes)  
---|---|---  
AAR | 24415212 | 7532309  
`jni/arm64-v8a/libonnxruntime.so`, uncompressed | 16276832 | 3962832  
`jni/x86_64/libonnxruntime.so`, uncompressed | 18222208 | 4240864  
  
This custom build supports the operators needed to run a ResNet50 model. It requires the use of ORT format models (as it was built with `--minimal_build=extended`). It has support for the NNAPI and XNNPACK execution providers.

* * *

## Table of contents

  * [Object detection and pose estimation with YOLOv8](/docs/tutorials/mobile/pose-detection.html)
  * [Mobile image recognition on Android](/docs/tutorials/mobile/deploy-android.html)
  * [Improve image resolution on mobile](/docs/tutorials/mobile/superres.html)
  * [Mobile objection detection on iOS](/docs/tutorials/mobile/deploy-ios.html)
  * [ORT Mobile Model Export Helpers](/docs/tutorials/mobile/helpers/)

* * *

For documentation questions, please [file an issue](https://github.com/microsoft/onnxruntime/issues/new?assignees=&labels=documentation&projects=&template=02-documentation.yml&title=%5BDocumentation%5D+).

[Edit this page on GitHub](https://github.com/microsoft/onnxruntime/tree/gh-pages/docs/tutorials/mobile/index.md)

This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll.
