# 学习资源索引

本文件收集 PyTorch 学习的优质资源，按类别组织。

---

## 官方资源

| 资源 | URL | 用途 |
|------|-----|------|
| PyTorch 官方文档 | https://pytorch.org/docs/stable/ | API 速查 |
| PyTorch 官方教程 | https://pytorch.org/tutorials/ | 系统学习 |
| PyTorch GitHub | https://github.com/pytorch/pytorch | 源码参考 |
| torchvision 文档 | https://pytorch.org/vision/stable/ | 预训练模型、数据集、transforms |
| ONNX 官方 | https://onnx.ai/ | ONNX 格式规范 |
| ONNX Runtime 文档 | https://onnxruntime.ai/ | ONNX 推理引擎 |

## 中文教程

| 资源 | URL | 用途 |
|------|-----|------|
| 菜鸟教程 PyTorch | https://www.runoob.com/pytorch/ | 入门教程（本课程主要参考）|
| PyTorch 中文文档 | https://pytorch.apachecn.org/ | 中文 API 文档 |
| 动手学深度学习 (d2l) | https://zh.d2l.ai/ | 理论 + 代码结合 |
| PyTorch 官方教程中文版 | https://pytorch.apachecn.org/tutorial/ | 官方教程翻译 |

## 视频资源

| 资源 | 平台 | 用途 |
|------|------|------|
| 李沐：动手学深度学习 | B站 | 理论 + PyTorch 实现 |
| PyTorch 官方 YouTube | YouTube | 官方讲解 |
| 3Blue1Brown：神经网络 | B站/YouTube | 直觉理解 |

## 工具

| 工具 | 用途 | 安装 |
|------|------|------|
| Netron | ONNX/模型可视化 | `pip install netron` 或 https://netron.app |
| TensorBoard | 训练可视化 | `pip install tensorboard` |
| ONNX Runtime | ONNX 推理 | `pip install onnxruntime` (CPU) 或 `onnxruntime-gpu` |
| torchsummary | 模型结构摘要 | `pip install torchsummary` |

## 部署相关资源

| 资源 | URL | 用途 |
|------|-----|------|
| NCNN | https://github.com/Tencent/ncnn | 移动端推理框架 |
| MNN | https://github.com/alibaba/MNN | 阿里移动端推理 |
| CMSIS-NN | https://github.com/ARM-software/CMSIS_5 | ARM MCU 神经网络库 |
| tinyml | - | 超轻量 ML 部署概念 |

## PyTorch 版本与安装

### CPU 版本
```bash
pip install torch torchvision
```

### GPU 版本（需要 CUDA）
```bash
# 根据 CUDA 版本选择，参考 https://pytorch.org/get-started/locally/
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### 验证安装
```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # True 表示 GPU 可用
```

## 推荐学习顺序（外部资源配合）

1. **入门**：菜鸟教程 PyTorch → 理解 Tensor 和基本 API
2. **进阶**：PyTorch 官方教程 → 60 分钟入门系列
3. **理论**：李沐 d2l → 深入理解每一步的数学原理
4. **实战**：torchvision 官方示例 → 图像分类参考实现
5. **部署**：ONNX 官方文档 → 模型导出和推理
