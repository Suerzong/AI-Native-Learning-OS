Diffusers 文档

训练概览

# 训练概览

Diffusers 提供了一系列训练脚本，供你训练自己的扩散模型。所有训练脚本可在 [diffusers/examples](https://github.com/huggingface/diffusers/tree/main/examples) 中找到。

每个训练脚本具有以下特点：

- **自包含**：训练脚本不依赖任何本地文件，运行脚本所需的所有包都从 `requirements.txt` 安装。
- **易于调整**：训练脚本是针对特定任务训练扩散模型的示例，不会对所有训练场景开箱即用。你可能需要根据具体用例调整脚本。
- **对初学者友好**：训练脚本设计为对初学者友好且易于理解。
- **单一目的**：每个训练脚本专为单一任务设计。

当前训练脚本包括：

训练任务 | SDXL 支持 | LoRA 支持
---|---|---
无条件图像生成（unconditional image generation） | |
文本到图像（text-to-image） | 👍 | 👍
文本反演（textual inversion） | |
DreamBooth | 👍 | 👍
ControlNet | 👍 |
InstructPix2Pix | 👍 |
Custom Diffusion | |
T2I-Adapters | 👍 |

## 安装

在新的虚拟环境中从源码安装库：

    git clone https://github.com/huggingface/diffusers
    cd diffusers
    pip install .

然后导航到训练脚本的文件夹并安装 `requirements.txt` 文件。

要加速训练并减少内存使用，推荐：
- 使用 PyTorch 2.0 或更高版本自动使用缩放点积注意力
- 安装 xFormers 以启用内存高效注意力
