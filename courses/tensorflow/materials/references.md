# 学习资源索引

本文件收集 TensorFlow 学习的优质资源，按类别组织。

---

## 官方资源

| 资源 | URL | 用途 |
|------|-----|------|
| TensorFlow 官方文档 | https://www.tensorflow.org/api_docs | API 速查 |
| TensorFlow 官方教程 | https://www.tensorflow.org/tutorials | 系统学习 |
| Keras 官方文档 | https://keras.io/api/ | Keras API 详细参考 |
| TensorFlow GitHub | https://github.com/tensorflow/tensorflow | 源码参考 |
| TF Lite 官方文档 | https://www.tensorflow.org/lite | 端侧部署 |
| TF Lite 示例 | https://www.tensorflow.org/lite/examples | 端侧部署实例 |
| TF.js 官方文档 | https://www.tensorflow.org/js | 浏览器端部署 |
| TF Hub | https://tfhub.dev/ | 预训练模型库 |
| TF Serving 文档 | https://www.tensorflow.org/tfx/guide/serving | 生产部署 |

## 中文教程

| 资源 | URL | 用途 |
|------|-----|------|
| 菜鸟教程 TensorFlow | https://www.runoob.com/tensorflow2/ | 入门教程（本课程主要参考）|
| TensorFlow 中文社区 | https://www.tensorflow.org/community/ | 中文社区 |
| 动手学深度学习 (d2l) | https://zh.d2l.ai/ | 理论 + 代码结合 |
| Keras 中文文档 | https://keras.io/zh/ | Keras 中文参考 |

## 本课程材料索引

| 教程文件 | 对应技能 | 主题 |
|---------|---------|------|
| `materials/noob/001_tensorflow-tutorial.md` | TF-L101 | TensorFlow 入门教程 |
| `materials/noob/002_tensorflow-intro.md` | TF-L101 | TensorFlow 简介 |
| `materials/noob/003_tensorflow-core-concepts.md` | TF-L102 | 核心概念 |
| `materials/noob/004_tensorflow-setup.md` | TF-L103 | 环境搭建 |
| `materials/noob/005_tensorflow-tensor-operations.md` | TF-L104/105/106 | Tensor 操作 |
| `materials/noob/006_tensorflow-api-keras.md` | TF-L107 | Keras API |
| `materials/noob/007_keras-neural-network.md` | TF-L107 | 神经网络 |
| `materials/noob/008_keras-layer.md` | TF-L108 | 常用层 |
| `materials/noob/009_tensorflow-ata-processing-and-pipelines.md` | TF-L201 | 数据处理流程 |
| `materials/noob/010_tensorflow-data-api.md` | TF-L202 | tf.data API |
| `materials/noob/011_tensorflow-image-data-processing.md` | TF-L203 | 图像数据处理 |
| `materials/noob/012_tensorflow-text-data-processing.md` | TF-L204 | 文本数据处理 |
| `materials/noob/013_tensorflow-model-training.md` | TF-L205/206 | 模型训练 |
| `materials/noob/014_tensorflow-model-evaluation-and-monitoring.md` | TF-L207 | 模型评估 |
| `materials/noob/015_tensorflow-model-tuning.md` | TF-L208 | 超参调优 |
| `materials/noob/016_tensorflow-image-classification.md` | TF-L209/301 | 图像分类 |
| `materials/noob/017_tensorflow-text-classification.md` | TF-L302 | 文本分类 |
| `materials/noob/018_tensorflow-regression.md` | TF-L303 | 回归问题 |
| `materials/noob/019_tensorflow-save-load.md` | TF-L304 | 保存与加载 |
| `materials/noob/020_tensorflow-conversion-and-optimization.md` | TF-L305 | 转换与优化 |
| `materials/noob/021_tensorflow-production.md` | TF-L306 | 生产部署 |
| `materials/noob/022_tensorflow-distributed-training.md` | TF-L307 | 分布式训练 |
| `materials/noob/023_tensorflow-ecosystem.md` | TF-L308/401 | 生态工具 |
| `materials/noob/024_tensorflow-custom-components.md` | TF-L404/405 | 自定义组件 |
| `materials/noob/TensorFlow_完整教程.md` | 全部 | 全局概览 |

## 视频资源

| 资源 | 平台 | 用途 |
|------|------|------|
| 李沐：动手学深度学习 | B站 | 理论 + 框架实现 |
| TensorFlow 官方 YouTube | YouTube | 官方讲解 |
| 3Blue1Brown：神经网络 | B站/YouTube | 直觉理解 |
| deeplizard TensorFlow 系列 | YouTube | 英文入门教程 |

## 工具

| 工具 | 用途 | 安装 |
|------|------|------|
| TensorBoard | 训练可视化 | 随 TensorFlow 附带 |
| Netron | 模型结构可视化 | `pip install netron` 或 https://netron.app |
| TF Lite Interpreter | TF Lite 推理 | 随 TensorFlow 附带 |
| Colab | 免费 GPU 环境 | https://colab.research.google.com |
| KerasTuner | 超参数搜索 | `pip install keras-tuner` |

## 端侧部署相关资源

| 资源 | URL | 用途 |
|------|-----|------|
| TF Lite 官方示例 | https://www.tensorflow.org/lite/examples | Android/iOS/嵌入式示例 |
| TF Lite Micro | https://www.tensorflow.org/lite/microcontrollers | MCU 端部署 |
| TF Lite Model Maker | https://www.tensorflow.org/lite/tutorials/model_maker | 自定义模型训练+转换 |
| Edge Impulse | https://www.edgeimpulse.com/ | 嵌入式 ML 平台 |
| NCNN | https://github.com/Tencent/ncnn | 腾讯移动端推理框架 |
| MNN | https://github.com/alibaba/MNN | 阿里移动端推理框架 |
| CMSIS-NN | https://github.com/ARM-software/CMSIS_5 | ARM MCU 神经网络库 |

## TensorFlow 版本与安装

### CPU 版本
```bash
pip install tensorflow
```

### GPU 版本（需要 CUDA + cuDNN）
```bash
# TensorFlow 2.10+ 在 Windows 上需要 WSL2
# 参考 https://www.tensorflow.org/install/pip
pip install tensorflow[and-cuda]
```

### 验证安装
```python
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))  # 返回 GPU 设备列表表示成功
```

### 常见安装问题
- Windows 上 TensorFlow 2.10+ 原生不支持 GPU，需要 WSL2
- CUDA 版本必须与 TensorFlow 版本匹配
- 如果 CPU 不支持 AVX 指令集，需要安装 `tensorflow-cpu` 或从源码编译

## 推荐学习顺序（外部资源配合）

1. **入门**：本课程 materials/noob/ 教程 → 理解 TensorFlow 基本概念和 API
2. **Keras**：Keras 官方文档 → 掌握高级 API
3. **实战**：TensorFlow 官方教程 → 图像/文本分类示例
4. **理论**：李沐 d2l → 深入理解数学原理
5. **部署**：TF Lite 官方文档 → 模型转换和端侧推理
