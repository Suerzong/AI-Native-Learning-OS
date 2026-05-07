Diffusers 文档

调度器（Schedulers）

# Schedulers

调度器是一种算法，为去噪过程提供指令，例如在某个步骤中应去除多少噪声。它接收步骤 _t_ 的模型预测，并应用更新来计算步骤 _t-1_ 的下一个样本。不同的调度器产生不同的结果；有些更快，有些更精确。

Diffusers 支持许多调度器，并允许你修改它们的时间步调度、时间步间距等，以在更少的步骤中生成高质量图像。

本指南将展示如何加载和自定义调度器。

## 加载调度器

调度器没有任何参数，定义在配置文件中。访问 Pipeline 的 `.scheduler` 属性查看配置。

使用 `from_pretrained()` 加载不同的调度器，指定 `subfolder` 参数将配置文件加载到 Pipeline 仓库的正确子文件夹中。将新调度器传递给现有 Pipeline。

## 时间步调度

时间步或噪声调度决定噪声在去噪过程中如何分布。调度可以是线性的，也可以更集中在开始或结束处。它是从调度器默认配置生成的噪声级别预计算序列，但可以自定义使用其他调度。

下面的示例使用 [Align Your Steps (AYS)](https://research.nvidia.com/labs/toronto-ai/AlignYourSteps/) 调度，可以在 10 步中生成高质量图像，显著加速生成并减少计算时间。

### 重新缩放调度

去噪应从纯噪声开始，信噪比（SNR）应为零。但有些模型实际上并非从纯噪声开始，这使得在亮度极端处生成图像变得困难。要修复此问题，模型必须使用 `v_prediction` 训练。

在调度器中启用以下参数：
- 设置 `rescale_betas_zero_snr=True` 将噪声调度重新缩放到最后一个时间步，使其恰好为零 SNR
- 设置 `timestep_spacing="trailing"` 强制从纯噪声的最后一个时间步开始采样

## 时间步间距

时间步间距指从调度中采样的特定步骤 _t_。Diffusers 提供三种间距类型：

间距策略 | 间距计算
---|---
`leading` | 均匀间距的步骤
`linspace` | 包含首尾步骤并均匀分割中间步骤
`trailing` | 包含最后一步并从末尾开始均匀分割中间步骤

`trailing` 策略通常在更少的步骤中产生更高质量和更多细节的图像。

## Sigmas

Sigmas 是衡量某个步骤中样本噪声程度的指标。使用自定义 `sigmas` 时，`timesteps` 从这些值计算，而非默认调度器配置。

### Karras Sigmas

Karras sigmas 重新采样噪声调度以实现更高效的采样，在结构重建关键的序列中间更密集地聚集 sigmas，同时在开始和结束处使用更少的 sigmas。

设置 `use_karras_sigmas=True` 启用。

## 选择调度器

尝试不同的调度器以找到最适合用例的非常重要。以下是一些建议：
- DPM++ 2M SDE Karras 通常是很好的通用选择
- TCDScheduler 适用于蒸馏模型
- FlowMatchEulerDiscreteScheduler 适用于 FlowMatch 模型
- EulerDiscreteScheduler 或 EulerAncestralDiscreteScheduler 适用于生成动漫风格图像
