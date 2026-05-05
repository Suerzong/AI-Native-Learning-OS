# PyTorch 混合精度训练

# PyTorch 混合精度训练 (AMP)

混合精度训练是深度学习中最重要的性能优化技术之一。它通过同时使用 FP32（单精度）和 FP16（半精度）浮点数进行计算，可以在几乎不损失模型精度的前提下，显著提升训练速度并减少显存占用。本节详细介绍 PyTorch 中的自动混合精度（Automatic Mixed Precision，AMP）技术。

**适用版本：**本文代码基于 PyTorch 1.6+ 的 `torch.cuda.amp` API 编写。PyTorch 2.4+ 推荐使用 `torch.amp.autocast` 和 `torch.amp.GradScaler`，用法基本一致，文中会标注差异。

## 1. 混合精度训练基础

### 1.1 为什么需要混合精度

深度学习模型训练过程中涉及大量的矩阵运算。传统的 FP32（32位浮点）计算精度高，但占用显存大、计算速度慢。FP16（16位浮点）计算速度快、显存占用少，但数值表示范围较小，容易出现梯度下溢（underflow）问题。

混合精度训练的核心理念是：对精度要求高的操作使用 FP32，对精度要求不高的操作使用 FP16。这样既能享受 FP16 的速度优势，又能避免精度问题。

下图展示了三种浮点格式的位布局差异——**指数位**决定数值范围，**尾数位**决定精度：

  浮点数格式位布局对比

    符号位

    指数位

    尾数位

    FP32
    32 bits

    S
    1

    Exponent
    8 bits

    Mantissa
    23 bits

    范围: ±3.4×10³⁸
    精度: ~7 位有效数字

    FP16
    16 bits

    S

    Exp
    5 bits

    Mantissa
    10 bits

    范围: ±65504
    精度: ~3.3 位有效数字

    ⚠ 指数位少，易溢出

    BF16
    16 bits

    S

    Exponent
    8 bits（同 FP32）

    Mantissa
    7 bits

    范围: ±3.4×10³⁸
    精度: ~2.4 位有效数字

    ✓ 范围与 FP32 相同

    BF16 保留了 FP32 的指数位 → 数值范围相同 → 训练更稳定，通常无需 GradScaler

### 1.2 混合精度的优势

| 指标 | 提升效果 | 说明 |
| --- | --- | --- |
| 训练速度 | 提升 2-3 倍 | 依赖 GPU Tensor Core 支持 |
| 显存占用 | 减少约 50% | 激活值和中间结果以 FP16 存储 |
| 内存带宽 | 减少约 50% | 更小的数据体积意味着更少的传输量 |
| 通信开销 | 减少约 50% | 分布式训练中梯度传输量减半 |

### 1.3 Tensor Core 加速原理

NVIDIA 的 Tensor Core 是一种专门用于矩阵运算的硬件单元。它可以在一个时钟周期内完成 4×4 矩阵乘加运算（D = A × B + C），这就是 FP16 训练加速的主要来源。相比普通 CUDA 核心需要多次指令才能完成同样的运算，Tensor Core 将其压缩为单条指令。

支持 Tensor Core 的 GPU 包括：

- **Volta 架构**（V100）— 首代 Tensor Core，仅支持 FP16

- **Turing 架构**（RTX 20 系）— 支持 FP16 / INT8 / INT4

- **Ampere 架构**（RTX 30 系、A100）— 新增 BF16 / TF32 支持

- **Ada Lovelace 架构**（RTX 40 系）— 新增 FP8 支持

- **Hopper 架构**（H100）— 新增 FP8 Transformer Engine

消费级 RTX GPU 同样支持 Tensor Core，如 RTX 3060 及以上型号均可享受 AMP 加速。

## 2. PyTorch AMP 基础用法

### 2.1 autocast 与 GradScaler

PyTorch 的 AMP API 主要包含两个核心组件：

- `autocast`：上下文管理器，自动将区域内的运算切换为 FP16（对精度敏感的操作会自动回退到 FP32）

- `GradScaler`：动态调整梯度缩放系数，放大 FP16 梯度以防止下溢（仅 FP16 需要，BF16 通常不需要）

下图展示了 AMP 训练一个完整 step 的数据流：

  AMP 单步训练流程

    输入数据
    FP32

-

    autocast
    前向传播
    自动选择 FP16/FP32

-

    计算 Loss
    FP32

-

    GradScaler
    缩放 + 反向传播
    loss × scale_factor

-

    Unscale 梯度
    + 梯度裁剪
    grad / scale_factor

-

    优化器更新
    FP32 权重

-

    更新
    Scaler
    调整 scale

    autocast 控制 — 自动选择精度

    GradScaler 控制 — 防止梯度下溢

    FP32 权重更新 — 保持精度

      关键：权重始终以 FP32 存储和更新，仅在计算时临时转换为 FP16

### 2.2 基础使用示例

## 实例

```python
import torch

import torch.nn as nn

import torch.optim as optim

from torch.cuda.amp import autocast, GradScaler

# PyTorch 2.4+ 推荐写法：

# from torch.amp import autocast, GradScaler

# 检查 CUDA 是否可用

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"使用设备: {device}")

if torch.cuda.is_available():

    print(f"GPU: {torch.cuda.get_device_name(0)}")

    print(f"支持 BF16: {torch.cuda.is_bf16_supported()}")

# ── 模型定义 ──────────────────────────────────────

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(128, 256),

            nn.ReLU(),

            nn.Linear(256, 256),

            nn.ReLU(),

            nn.Linear(256, 10)

        )

    def forward(self, x):

        return self.net(x)

model = SimpleModel().to(device)

# 损失函数和优化器

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ── 混合精度训练关键组件 ──────────────────────────

# GradScaler：缩放损失以避免 FP16 梯度下溢

scaler = GradScaler()

# 训练循环

def train_epoch_amp(model, loader, criterion, optimizer, scaler, device):

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for inputs, labels in loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        # ── 核心：使用 autocast 上下文管理器 ──────

        # autocast 区域内的运算自动使用 FP16

        # 对精度敏感的操作（如 softmax、loss）会自动回退 FP32

        with autocast(device_type='cuda'):

            outputs = model(inputs)

            loss = criterion(outputs, labels)

        # ── 使用 scaler 进行反向传播 ─────────────

        # 1. 缩放 loss（乘以 scale_factor）

        # 2. 反向传播（在放大的梯度上计算）

        # 3. scaler.step 内部自动反缩放梯度并检查 Inf/NaN

        scaler.scale(loss).backward()

        # 更新参数

        scaler.step(optimizer)

        # 更新 scaler 的缩放因子

        scaler.update()

        # 统计

        total_loss += loss.item() * inputs.size(0)

        _, predicted = outputs.max(1)

        correct += predicted.eq(labels).sum().item()

        total += labels.size(0)

    return total_loss / total, correct / total

# 模拟数据

train_loader = [

    (torch.randn(32, 128), torch.randint(0, 10, (32,))) for _ in range(10)

]

# 开始训练

for epoch in range(3):

    loss, acc = train_epoch_amp(

        model, train_loader, criterion, optimizer, scaler, device

    )

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, Acc={acc:.4f}")

print("混合精度训练完成！")
```

**API 迁移提示：**PyTorch 2.4 将 `torch.cuda.amp.autocast` 标记为 deprecated，推荐使用 `torch.amp.autocast('cuda')`。两者用法完全一致，仅导入路径不同。

### 2.3 BF16 与 FP16 的选择

现代 GPU 支持两种半精度格式，它们的核心区别在于指数位和尾数位的分配策略不同：

| 格式 | 指数位 | 尾数位 | 数值范围 | 精度 | 适用场景 |
| --- | --- | --- | --- | --- | --- |
| FP16 | 5 bits | 10 bits | ±65504 | 较高（~3.3位） | 需要兼容旧 GPU（V100/RTX 20系） |
| BF16 | 8 bits | 7 bits | ±3.4×10³⁸ | 较低（~2.4位） | 追求稳定性（A100/RTX 30系+） |

选择建议：如果硬件支持 BF16，优先使用 BF16。它的数值范围与 FP32 完全相同，训练过程中几乎不会出现溢出问题，且不需要 GradScaler。

## 实例

```python
# ── BF16 写法（PyTorch 1.10+）────────────────────

# BF16 不需要 GradScaler，因为数值范围与 FP32 相同

from torch.cuda.amp import autocast

# 方式一：在 autocast 中指定 dtype

with autocast(device_type='cuda', dtype=torch.bfloat16):

    outputs = model(inputs)

    loss = criterion(outputs, labels)

# 方式二：全局默认启用 BF16（如果硬件支持）

# torch.backends.cuda.matmul.allow_bf16_reduced_precision = True

# torch.backends.cudnn.allow_bf16_reduced_precision = True

# ── 检查硬件支持 ─────────────────────────────────

print(f"硬件支持 BF16: {torch.cuda.is_bf16_supported()}")

print(f"当前 matmul 允许 BF16: {torch.backends.cuda.matmul.allow_bf16}")

print(f"当前 cuDNN 允许 BF16: {torch.backends.cudnn.allow_bf16}")

# ── BF16 完整训练示例（无需 GradScaler）──────────

scaler_bf16 = None  # BF16 不需要 scaler

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda', dtype=torch.bfloat16):

        outputs = model(inputs)

        loss = criterion(outputs, labels)

    # 直接反向传播，无需 scaler

    loss.backward()

    optimizer.step()
```

## 3. 进阶技巧与优化

### 3.1 动态损失缩放

GradScaler 的核心机制是**动态损失缩放**——它会根据训练状态自动调整缩放因子，既能防止梯度下溢，又能在训练稳定时逐步降低缩放以减少精度损失：

  动态损失缩放（Dynamic Loss Scaling）

  Scale × Loss

-

  反向传播

-

  梯度中存在
  Inf / NaN？

-
  是

  缩小 scale
  × backoff
  （默认 0.5）

  跳过本次更新

-
  否

  Unscale + 更新参数
  连续成功 +1

-

  连续成功 ≥ growth_interval？
  （默认 2000 步）

-

  增大 scale × growth

    growth_factor 默认 2.0 · backoff_factor 默认 0.5 · 动态平衡精度与稳定

GradScaler 自动管理上述反馈循环，你只需通过参数微调其行为：

## 实例

```python
from torch.cuda.amp import GradScaler

# 自定义 GradScaler 参数

scaler = GradScaler(

    init_scale=2**16,        # 初始缩放因子，默认 65536

    growth_factor=2.0,       # 缩放因子增长倍数，默认 2.0

    backoff_factor=0.5,      # 缩放因子回退倍数，默认 0.5

    growth_interval=2000,    # 连续多少个 step 成功后才增长

    enabled=True             # 是否启用（可动态开关）

)

# 工作流程：

# 1. 初始 scale = 65536

# 2. 若某 step 出现 Inf/NaN → scale × 0.5（缩小），跳过该 step

# 3. 若连续 2000 个 step 无 Inf/NaN → scale × 2.0（增大）

# 4. 始终在安全范围内寻找最大可用 scale

# 查看当前缩放因子

print(f"当前缩放因子: {scaler.get_scale()}")

# 判断 scaler 是否认为上一步成功

print(f"最近是否成功: {scaler._found_inf.item() == 0}")
```

### 3.2 梯度累积中的 AMP

梯度累积用于在有限显存下模拟更大的 batch size。使用 AMP 时，需要注意每个子 batch 的 loss 必须除以累积步数，否则最终梯度会被放大：

## 实例

```python
# ── 梯度累积 + 混合精度 ──────────────────────────

accumulation_steps = 8

scaler = GradScaler()

model.train()

for batch_idx, (inputs, labels) in enumerate(train_loader):

    inputs, labels = inputs.to(device), labels.to(device)

    with autocast(device_type='cuda'):

        outputs = model(inputs)

        # 关键：每个子 batch 的 loss 除以累积步数

        # 这样累积后的梯度等价于大 batch 的平均梯度

        loss = criterion(outputs, labels) / accumulation_steps

    # 累积缩放后的梯度（注意：此处不清零）

    scaler.scale(loss).backward()

    # 每 accumulation_steps 个 batch 更新一次参数

    if (batch_idx + 1) % accumulation_steps == 0:

        scaler.step(optimizer)

        scaler.update()

        optimizer.zero_grad()

# ── 处理末尾不足一个完整累积周期的梯度 ──────────

remainder = len(train_loader) % accumulation_steps

if remainder != 0:

    # 需要将累积的梯度按实际步数重新缩放

    # 简单做法：仍然执行 step，梯度会偏大但影响通常很小

    scaler.step(optimizer)

    scaler.update()

    optimizer.zero_grad()
```

### 3.3 验证与推理中的 AMP

验证和推理阶段同样推荐使用 AMP。由于不需要反向传播和梯度缩放，代码更加简洁：

## 实例

```python
# ── 推理时使用 autocast ──────────────────────────

@torch.no_grad()

def inference_amp(model, inputs, device):

    model.eval()

    # 推理使用 FP16，无需 GradScaler

    with autocast(device_type='cuda'):

        outputs = model(inputs.to(device))

    return outputs

# ── inference_mode 比 no_grad 更快 ──────────────

# inference_mode 会禁用更多追踪开销，适合纯推理

@torch.inference_mode()

def inference_fast(model, inputs, device):

    model.eval()

    with autocast(device_type='cuda'):

        outputs = model(inputs.to(device))

    return outputs

# ── 批量推理示例 ─────────────────────────────────

def batch_inference(model, dataloader, device):

    model.eval()

    all_outputs = []

    with torch.inference_mode():

        for inputs in dataloader:

            with autocast(device_type='cuda'):

                outputs = model(inputs.to(device))

            all_outputs.append(outputs.cpu())

    return torch.cat(all_outputs, dim=0)
```

## 4. 常见问题与解决方案

### 4.1 训练不稳定

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| Loss 变为 NaN / Inf | 梯度溢出（scale 过大或学习率过高） | 降低 init_scale，添加梯度裁剪，降低学习率 |
| Loss 不下降 / 震荡 | 梯度下溢（scale 过小，梯度被截断为 0） | 提高 init_scale，检查梯度统计，尝试 BF16 |
| 精度下降明显 | 某些层（如 LayerNorm、Softmax）对 FP16 敏感 | 手动将这些层保持 FP32（见 4.2） |
| 训练后期不稳定 | 模型参数值域变化导致 scale 不匹配 | 适当增大 growth_interval，使 scale 调整更保守 |

### 4.2 手动控制精度

某些操作在 FP16 下精度损失较大，需要手动指定使用 FP32。PyTorch 的 autocast 已经内置了对这些操作的保护，但自定义操作可能需要手动处理：

## 实例

```python
# ── 方法一：包裹一个强制 FP32 的损失函数 ────────

class FP32Loss(nn.Module):

    """强制在 FP32 下计算的损失函数包装器"""

    def __init__(self, base_criterion):

        super().__init__()

        self.base_criterion = base_criterion

    def forward(self, input, target):

        # 显式转换为 FP32，脱离 autocast 的影响

        return self.base_criterion(input.float(), target.float())

# ── 方法二：在 autocast 中局部禁用 ──────────────

with autocast(device_type='cuda'):

    outputs = model(inputs)

    # 对精度敏感的操作，临时禁用 autocast

    with autocast(enabled=False):

        loss = criterion(outputs.float(), labels)

# ── 方法三：模型中特定层保持 FP32 ──────────────

class CustomModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),

            nn.BatchNorm2d(64),  # BN 对精度敏感

            nn.ReLU(),

            nn.Conv2d(64, 128, 3, padding=1),

            nn.BatchNorm2d(128),

            nn.ReLU(),

        )

        self.classifier = nn.Linear(128, 10)

    def forward(self, x):

        x = self.features[0](x)           # Conv: FP16（由 autocast 控制）

        x = self.features[1](x.float())   # BN: 强制 FP32

        x = self.features[2](x)           # ReLU: FP16

        x = self.features[3](x)

        x = self.features[4](x.float())   # BN: 强制 FP32

        x = self.features[5](x)

        x = x.mean(dim=[2, 3])            # Global Average Pooling

        x = self.classifier(x)

        return x
```

**提示：**PyTorch 的 autocast 会自动将以下操作保持在 FP32：softmax、log_softmax、cross_entropy、layer_norm、batch_norm 等。通常只有自定义算子才需要手动处理。

### 4.3 梯度裁剪与 AMP

梯度裁剪必须在 `scaler.step()` 之前、且在 `scaler.unscale_()` 之后执行。这是因为裁剪需要作用在**真实梯度值**上，而非缩放后的梯度：

## 实例

```python
# ── 正确的梯度裁剪顺序 ──────────────────────────

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda'):

        outputs = model(inputs)

        loss = criterion(outputs, labels)

    # Step 1: 缩放 loss 并反向传播

    scaler.scale(loss).backward()

    # Step 2: 反缩放梯度（将梯度从 scale 还原到真实值）

    #         必须在裁剪和 step 之前调用

    scaler.unscale_(optimizer)

    # Step 3: 对真实梯度进行裁剪

    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    # Step 4: 更新参数（内部会检查梯度是否含 Inf/NaN）

    scaler.step(optimizer)

    # Step 5: 更新缩放因子

    scaler.update()

# ── 常见错误：忘记 unscale_ 就裁剪 ──────────────

# 错误！裁剪的是被放大的梯度，阈值会被 scale 干扰

# scaler.scale(loss).backward()

# torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # ← 错误

# scaler.step(optimizer)
```

## 5. 性能对比与最佳实践

### 5.1 性能基准测试

## 实例

```python
import time

def benchmark_training(model, train_loader, device, use_amp=True,

                       dtype=torch.float16, num_iterations=100):

    """对比 FP32 与 AMP 的训练速度"""

    model = model.to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    scaler = GradScaler(enabled=use_amp and dtype == torch.float16)

    # ── 预热（前 10 步不计时）────────────────────

    for i, (inputs, labels) in enumerate(train_loader):

        if i >= 10:

            break

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        if use_amp:

            with autocast(device_type='cuda', dtype=dtype):

                outputs = model(inputs)

                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()

            scaler.step(optimizer)

            scaler.update()

        else:

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

    # ── 正式测试 ─────────────────────────────────

    torch.cuda.synchronize()

    start = time.time()

    for i, (inputs, labels) in enumerate(train_loader):

        if i >= num_iterations:

            break

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        if use_amp:

            with autocast(device_type='cuda', dtype=dtype):

                outputs = model(inputs)

                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()

            scaler.step(optimizer)

            scaler.update()

        else:

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

    torch.cuda.synchronize()

    elapsed = time.time() - start

    return elapsed / num_iterations

# ── 运行对比 ─────────────────────────────────────

model = SimpleModel()

fp32_time = benchmark_training(model, train_loader, device, use_amp=False)

fp16_time = benchmark_training(model, train_loader, device, use_amp=True, dtype=torch.float16)

print(f"FP32 平均耗时: {fp32_time*1000:.2f} ms/batch")

print(f"FP16 平均耗时: {fp16_time*1000:.2f} ms/batch")

print(f"加速比: {fp32_time / fp16_time:.2f}x")

# 如果支持 BF16，也测试一下

if torch.cuda.is_bf16_supported():

    bf16_time = benchmark_training(

        model, train_loader, device, use_amp=True, dtype=torch.bfloat16

    )

    print(f"BF16 平均耗时: {bf16_time*1000:.2f} ms/batch")

    print(f"BF16 加速比: {fp32_time / bf16_time:.2f}x")
```

### 5.2 显存对比

## 实例

```python
def compare_memory(model_class, train_loader, device):

    """对比 FP32 与 AMP 的显存占用"""

    def reset():

        torch.cuda.empty_cache()

        torch.cuda.reset_peak_memory_stats()

    # ── FP32 显存测试 ────────────────────────────

    reset()

    model_fp32 = model_class().to(device)

    optimizer_fp32 = optim.Adam(model_fp32.parameters())

    for inputs, labels in list(train_loader)[:5]:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_fp32.zero_grad()

        outputs = model_fp32(inputs)

        loss = nn.CrossEntropyLoss()(outputs, labels)

        loss.backward()

        optimizer_fp32.step()

    fp32_peak = torch.cuda.max_memory_allocated() / 1024**2

    # ── AMP 显存测试 ─────────────────────────────

    reset()

    model_amp = model_class().to(device)

    optimizer_amp = optim.Adam(model_amp.parameters())

    scaler = GradScaler()

    for inputs, labels in list(train_loader)[:5]:

        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_amp.zero_grad()

        with autocast(device_type='cuda'):

            outputs = model_amp(inputs)

            loss = nn.CrossEntropyLoss()(outputs, labels)

        scaler.scale(loss).backward()

        scaler.step(optimizer_amp)

        scaler.update()

    amp_peak = torch.cuda.max_memory_allocated() / 1024**2

    print(f"FP32 峰值显存: {fp32_peak:.1f} MB")

    print(f"AMP  峰值显存: {amp_peak:.1f} MB")

    print(f"显存节省: {(fp32_peak - amp_peak) / fp32_peak * 100:.1f}%")

compare_memory(SimpleModel, train_loader, device)
```

### 5.3 最佳实践总结

| 场景 | 推荐配置 | 原因 |
| --- | --- | --- |
| A100 / H100 / RTX 40 系 | BF16，不需要 GradScaler | 数值范围与 FP32 相同，最稳定 |
| V100 / RTX 20 系 | FP16 + GradScaler | 硬件不支持 BF16，需要 scaler 防溢出 |
| RTX 30 系 | BF16 优先，FP16 备选 | Ampere 架构支持 BF16 |
| 大模型训练（显存紧张） | AMP + 梯度累积 + 梯度检查点 | 三者叠加可最大化显存利用率 |
| 推理部署 | autocast + inference_mode | 无需 scaler，推理最快 |

PyTorch 2.0+ 已将 AMP 集成到 `torch.compile` 中，可以自动应用混合精度优化。使用 `torch.compile(model)` 时，编译器会自动判断哪些操作适合 FP16。

## 6. 与其他优化技术的结合

### 6.1 AMP + torch.compile

## 实例

```python
# ── PyTorch 2.0+ 结合使用 ───────────────────────

model = model.to(device)

# 方式一：先 compile，再用 AMP 训练

# torch.compile 会自动融合算子、优化内存访问

model_compiled = torch.compile(model, mode="reduce-overhead")

scaler = GradScaler()

for inputs, labels in train_loader:

    inputs, labels = inputs.to(device), labels.to(device)

    optimizer.zero_grad()

    with autocast(device_type='cuda'):

        outputs = model_compiled(inputs)

        loss = criterion(outputs, labels)

    scaler.scale(loss).backward()

    scaler.step(optimizer)

    scaler.update()

# 方式二：启用 TF32（Ampere+ 架构的额外加速）

# TF32 使用 19 位精度，速度接近 FP16，精度接近 FP32

torch.backends.cuda.matmul.allow_tf32 = True

torch.backends.cudnn.allow_tf32 = True

torch.backends.cudnn.benchmark = True  # 固定输入尺寸时加速卷积
```

### 6.2 AMP + 分布式训练

## 实例

```python
# ── 分布式训练 + 混合精度 ────────────────────────

import torch.distributed as dist

from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):

    dist.init_process_group("nccl", rank=rank, world_size=world_size)

    torch.cuda.set_device(rank)

def train_ddp_amp(rank, world_size):

    setup(rank, world_size)

    device = torch.device(f"cuda:{rank}")

    model = SimpleModel().to(device)

    model = DDP(model, device_ids=[rank])

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    scaler = GradScaler()

    for inputs, labels in train_loader:

        inputs = inputs.to(device, non_blocking=True)

        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        with autocast(device_type='cuda'):

            outputs = model(inputs)

            loss = criterion(outputs, labels)

        # DDP 会在 backward 中自动同步梯度

        scaler.scale(loss).backward()

        # 梯度裁剪（需先 unscale）

        scaler.unscale_(optimizer)

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        scaler.step(optimizer)

        scaler.update()

    dist.destroy_process_group()
```

## 总结

混合精度训练是当前深度学习训练的**标准实践**。

核心要点：

- **选择精度格式**：硬件支持 BF16 时优先使用，否则使用 FP16 + GradScaler

- **理解 autocast**：它自动管理精度切换，大多数情况下无需手动干预

- **理解 GradScaler**：仅 FP16 需要，通过动态缩放防止梯度下溢

- **注意裁剪顺序**：unscale → clip → step → update，顺序不可颠倒

- **善用组合优化**：AMP 可与 torch.compile、梯度累积、分布式训练无缝结合
