# 图像数据处理技能地图

## 目标

学习者能用 TensorFlow 的 tf.image 和 tf.keras.layers 完成图像的加载、预处理、数据增强，能构建从文件系统到模型输入的完整图像数据管道。

## 必会概念

- 图像在 TensorFlow 中表示为 Tensor：(height, width, channels) 或 (batch, height, width, channels)
- channels_last（默认）vs channels_first 的数据格式
- uint8 [0,255] vs float32 [0,1] 的转换
- 数据增强（Data Augmentation）只用于训练集
- 预处理层（Preprocessing Layers）可直接嵌入模型

## 必会 API

### 图像加载

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.io.read_file(path)` | 读取文件为字符串 | `tf.io.read_file('image.jpg')` |
| `tf.image.decode_jpeg(contents)` | 解码 JPEG | `tf.image.decode_jpeg(img_raw)` |
| `tf.image.decode_png(contents)` | 解码 PNG | `tf.image.decode_png(img_raw)` |
| `tf.image.decode_image(contents)` | 自动识别格式解码 | `tf.image.decode_image(img_raw)` |
| `tf.keras.utils.load_img(path)` | Keras 方式加载 | `tf.keras.utils.load_img('image.jpg')` |
| `tf.io.parse_single_example()` | 解析 TFRecord | 从 TFRecord 加载 |

### 图像预处理

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.image.resize(image, size)` | 调整大小 | `tf.image.resize(img, [224, 224])` |
| `tf.image.resize_with_pad()` | 保持比例调整 | `tf.image.resize_with_pad(img, 224, 224)` |
| `tf.image.central_crop(img, 0.5)` | 中心裁剪 | 裁剪中心 50% |
| `tf.cast(image, tf.float32) / 255.0` | 归一化到 [0,1] | 像素值缩放 |
| `tf.image.per_image_standardization()` | 标准化（减均值除标准差）| 每张图标准化 |

### 数据增强

| 函数 | 用途 | 示例 |
|------|------|------|
| `tf.image.random_flip_left_right(img)` | 随机水平翻转 | 50% 概率翻转 |
| `tf.image.random_flip_up_down(img)` | 随机垂直翻转 | 50% 概率翻转 |
| `tf.image.random_brightness(img, 0.2)` | 随机亮度调整 | 最大偏移 0.2 |
| `tf.image.random_contrast(img, 0.8, 1.2)` | 随机对比度 | 范围 [0.8, 1.2] |
| `tf.image.random_saturation(img, 0.8, 1.2)` | 随机饱和度 | 范围 [0.8, 1.2] |
| `tf.image.random_hue(img, 0.1)` | 随机色相 | 最大偏移 0.1 |
| `tf.image.random_crop(img, size)` | 随机裁剪 | 需指定裁剪尺寸 |

### Keras 预处理层（推荐）

```python
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
    tf.keras.layers.RandomContrast(0.1),
])
```

## 完整 Pipeline 示例

```python
import tensorflow as tf

def load_and_preprocess_image(path, label):
    # 读取文件
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    # 调整大小
    image = tf.image.resize(image, [224, 224])
    # 归一化
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

def augment(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, 0.1)
    image = tf.clip_by_value(image, 0.0, 1.0)  # 确保值在 [0,1]
    return image, label

# 训练 pipeline
train_ds = tf.data.Dataset.from_tensor_slices((file_paths, labels))
train_ds = (train_ds
    .map(load_and_preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)
    .map(augment, num_parallel_calls=tf.data.AUTOTUNE)
    .shuffle(1000)
    .batch(32)
    .prefetch(tf.data.AUTOTUNE)
)

# 验证 pipeline（不含增强）
val_ds = tf.data.Dataset.from_tensor_slices((val_paths, val_labels))
val_ds = (val_ds
    .map(load_and_preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)
    .batch(32)
    .prefetch(tf.data.AUTOTUNE)
)
```

## 常见错误

1. decode 后的图像是 uint8，模型通常需要 float32
2. 数据增强应用在了验证集/测试集上
3. resize 没有保持宽高比导致图片变形
4. random_crop 的尺寸大于图片尺寸导致报错
5. 增强后的值超出 [0,1] 范围（需要 clip_by_value）
6. 忘记 normalize 导致训练不稳定

## 训练阶梯

1. **图像加载**：能用 tf.io + tf.image 加载和解码图片
2. **基本预处理**：能 resize 和 normalize 图片
3. **数据增强**：能用 tf.image 或 Keras 层做数据增强
4. **完整 pipeline**：能构建从文件到 batch 的完整管道
5. **TFRecord**：能用 TFRecord 格式高效存储和加载大量图片

## 掌握标准

- 能从文件系统构建图像数据管道
- 能正确区分训练集（含增强）和验证集（不含增强）的 pipeline
- 理解 uint8 → float32 的转换必要性
- 能用 Keras 预处理层或 tf.image 实现数据增强
- 能将预处理层嵌入模型实现端到端推理
