# 模型部署技能地图

## 目标

学习者能将训练好的模型保存为 SavedModel 格式，能转换为 TF Lite 格式用于端侧部署，能用 TF Serving 部署为 REST API 服务。

## 必会概念

- SavedModel 是 TensorFlow 的标准保存格式（包含模型结构+权重+计算图）
- HDF5 是 Keras 的传统保存格式（.h5 文件）
- TF Lite 是 TensorFlow 的端侧推理引擎
- 量化可以减小模型大小并加速推理
- TF Serving 是 TensorFlow 的生产级模型服务框架
- 模型部署流程：训练 → 保存 → 转换（可选量化）→ 部署

## 保存与加载 API

| 函数 | 用途 | 示例 |
|------|------|------|
| `model.save(path)` | 保存 SavedModel 格式 | `model.save('my_model')` |
| `model.save('file.h5')` | 保存 HDF5 格式 | `model.save('model.h5')` |
| `tf.keras.models.load_model(path)` | 加载模型 | `tf.keras.models.load_model('my_model')` |
| `model.save_weights(path)` | 只保存权重 | `model.save_weights('weights')` |
| `model.load_weights(path)` | 加载权重 | `model.load_weights('weights')` |
| `tf.saved_model.save(model, path)` | 保存 SavedModel（低级 API）| `tf.saved_model.save(model, 'model')` |
| `tf.saved_model.load(path)` | 加载 SavedModel（低级 API）| `tf.saved_model.load('model')` |

## SavedModel vs HDF5

| 特性 | SavedModel | HDF5 |
|------|-----------|------|
| 文件结构 | 目录（含多个文件）| 单个 .h5 文件 |
| 自定义层 | 支持 | 需要 custom_objects |
| TF Serving | 支持 | 不支持 |
| TF Lite | 支持 | 支持 |
| 计算图 | 保存完整计算图 | 只保存权重+配置 |
| 推荐使用 | 生产部署首选 | 简单保存备用 |

## TF Lite 转换 API

```python
import tensorflow as tf

# 从 SavedModel 转换
converter = tf.lite.TFLiteConverter.from_saved_model('my_model')
tflite_model = converter.convert()

# 保存 .tflite 文件
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

# 从 Keras 模型转换
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

## TF Lite 推理 API

```python
import tensorflow as tf
import numpy as np

# 加载模型
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

# 获取输入/输出信息
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 准备输入数据
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)

# 推理
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
```

## TF Serving 基本用法

```bash
# Docker 运行 TF Serving
docker run -p 8501:8501 \
  --mount type=bind,source=/path/to/my_model,target=/models/my_model \
  -e MODEL_NAME=my_model \
  tensorflow/serving

# REST API 请求
curl -d '{"instances": [[1.0, 2.0, 3.0]]}' \
  -X POST http://localhost:8501/v1/models/my_model:predict
```

## 量化选项

| 量化方式 | 模型大小 | 推理速度 | 精度损失 | 额外要求 |
|---------|---------|---------|---------|---------|
| Dynamic range | 4x 减小 | 2-3x 加速 | 小 | 无 |
| Float16 | 2x 减小 | GPU 加速 | 很小 | GPU 支持 |
| Full integer | 4x 减小 | 最快加速 | 中等 | representative dataset |
| Quantization-aware training | 4x 减小 | 最快加速 | 最小 | 训练时修改模型 |

```python
# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_saved_model('my_model')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Full integer quantization
converter = tf.lite.TFLiteConverter.from_saved_model('my_model')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
def representative_dataset():
    for _ in range(100):
        yield [np.random.random((1, 224, 224, 3)).astype(np.float32)]
converter.representative_dataset = representative_dataset
tflite_model = converter.convert()
```

## 常见错误

1. SavedModel 路径是目录不是文件
2. HDF5 格式加载自定义层需要 custom_objects
3. TF Lite 不支持某些 TF 算子（需要注册或替换）
4. 量化时忘记提供 representative_dataset
5. Interpreter 推理前忘记 allocate_tensors()
6. 输入数据的 dtype 和 shape 必须与模型一致

## 训练阶梯

1. **保存加载**：能用 SavedModel 格式保存和加载模型
2. **基本转换**：能将模型转为 TF Lite 格式
3. **TF Lite 推理**：能用 Interpreter 加载和推理
4. **量化**：能应用基本量化减小模型大小
5. **端到端部署**：完成训练 → 保存 → 转换 → 推理的完整流程

## 掌握标准

- 能不查文档写出 SavedModel 保存和加载代码
- 能完成 SavedModel → TF Lite 转换并验证推理结果
- 能应用至少一种量化方式
- 能画出完整的模型部署流程图
- 理解 SavedModel、HDF5、TF Lite 三种格式的关系
