# iOS 快速入门

> 来源：https://ai.google.dev/edge/litert/ios/quickstart

LiteRT 让你可以在 iOS 应用中运行 TensorFlow、PyTorch 和 JAX 模型。LiteRT 系统提供了预构建和可自定义的执行环境，用于在 iOS 上快速高效地运行模型，具有额外的版本管理灵活性和可选的委托（如 CoreML 和 Metal）以增强性能。

有关使用 LiteRT 的示例 iOS 应用，请参阅 [LiteRT 示例](https://github.com/google-ai-edge/litert-samples/tree/main/examples)仓库。

## 将 LiteRT 添加到你的 Swift 或 Objective-C 项目

LiteRT 提供用 [Swift](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/swift) 和 [Objective-C](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/objc) 编写的原生 iOS 库。

以下部分演示如何将 LiteRT Swift 或 Objective-C 添加到你的项目：

### CocoaPods 开发者

在你的 `Podfile` 中添加 LiteRT pod，然后运行 `pod install`。

#### Swift

```ruby
use_frameworks!
pod 'TensorFlowLiteSwift'
```

#### Objective-C

```ruby
pod 'TensorFlowLiteObjC'
```

#### 指定版本

`TensorFlowLiteSwift` 和 `TensorFlowLiteObjC` pod 都有稳定版本和每夜版本可用。如果你不指定版本约束，CocoaPods 默认拉取最新的稳定版本。

你也可以指定版本约束。例如，如果你希望依赖 2.10.0 版本：

```ruby
pod 'TensorFlowLiteSwift', '~> 2.10.0'
```

如果你希望依赖每夜版本：

```ruby
pod 'TensorFlowLiteSwift', '~> 0.0.1-nightly'
```

从 2.4.0 版本和最新每夜版本开始，默认情况下 [GPU](https://ai.google.dev/edge/litert/performance/gpu) 和 [Core ML 委托](https://ai.google.dev/edge/litert/ios/coreml)从 pod 中排除以减小二进制大小。你可以通过指定子规范来包含它们：

```ruby
pod 'TensorFlowLiteSwift', '~> 0.0.1-nightly', :subspecs => ['CoreML', 'Metal']
```

### Bazel 开发者

在你的 `BUILD` 文件中，将 `TensorFlowLite` 依赖添加到目标。

#### Swift

```python
swift_library(
  deps = [
      "//tensorflow/lite/swift:TensorFlowLite",
  ],
)
```

#### Objective-C

```python
objc_library(
  deps = [
      "//tensorflow/lite/objc:TensorFlowLite",
  ],
)
```

#### C/C++ API

或者，你可以使用 [C API](https://www.tensorflow.org/code/tensorflow/lite/c/c_api.h) 或 [C++ API](https://ai.google.dev/edge/api/tflite/cc)：

```python
# 直接使用 C API
objc_library(
  deps = [
      "//tensorflow/lite/c:c_api",
  ],
)

# 直接使用 C++ API
objc_library(
  deps = [
      "//tensorflow/lite:framework",
  ],
)
```

### 导入库

对于 Swift 文件，导入 LiteRT 模块：

```swift
import TensorFlowLite
```

对于 Objective-C 文件，导入 umbrella header：

```objective-c
#import "TFLTensorFlowLite.h"
```

或者，如果你在 Xcode 项目中设置了 `CLANG_ENABLE_MODULES = YES`，则导入模块：

```objective-c
@import TFLTensorFlowLite;
```

**注意：** 对于想要导入 Objective-C TensorFlow Lite 模块的 CocoaPods 开发者，你还必须在 `Podfile` 中包含 `use_frameworks!`。
