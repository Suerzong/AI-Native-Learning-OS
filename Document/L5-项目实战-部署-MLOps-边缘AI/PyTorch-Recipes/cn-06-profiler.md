# PyTorch Profiler（性能分析器）

> 来源：https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html

本教程介绍如何使用 PyTorch Profiler 测量模型操作符的时间和内存消耗。

## 简介

PyTorch 包含一个简单的 Profiler API，当用户需要确定模型中最昂贵的操作符时非常有用。

在本教程中，我们将使用一个简单的 ResNet 模型来演示如何使用 Profiler 分析模型性能。

## 前置条件

- `torch >= 2.3.0`

## 步骤

1. 导入所有必要的库
2. 实例化一个简单的 ResNet 模型
3. 使用 Profiler 分析执行时间
4. 使用 Profiler 分析内存消耗
5. 使用追踪功能
6. 检查堆栈追踪
7. 使用 Profiler 分析长时间运行的任务

### 1. 导入所需库

```python
import torch
import torchvision.models as models
from torch.profiler import profile, ProfilerActivity, record_function
```

### 2. 实例化一个简单的 ResNet 模型

```python
model = models.resnet18()
inputs = torch.randn(5, 3, 224, 224)
```

### 3. 使用 Profiler 分析执行时间

PyTorch Profiler 通过上下文管理器启用，接受多个参数，其中最有用的包括：

- `activities` — 要分析的活动列表：
  - `ProfilerActivity.CPU` — PyTorch 操作符、TorchScript 函数和用户定义的代码标签
  - `ProfilerActivity.CUDA` — 设备上的 CUDA 内核
  - `ProfilerActivity.XPU` — 设备上的 XPU 内核
- `record_shapes` — 是否记录操作符输入的形状
- `profile_memory` — 是否报告模型张量消耗的内存量

```python
with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
    with record_function("model_inference"):
        model(inputs)

print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))
```

我们可以使用 `record_function` 上下文管理器用用户提供的名称标记任意代码范围。

输出示例（省略部分列）：

```
---------------------------------  ------------  ------------  ------------  ------------
                                Name      Self CPU     CPU total  CPU time avg    # of Calls
---------------------------------  ------------  ------------  ------------  ------------
                      model_inference       5.509ms      57.503ms      57.503ms             1
                         aten::conv2d     231.000us      31.931ms       1.597ms            20
                    aten::convolution     250.000us      31.700ms       1.585ms            20
```

可以看到，如预期的那样，大部分时间花在卷积上。注意 self CPU 时间和 CPU 时间的区别——操作符可以调用其他操作符，self CPU 时间不包括子操作符调用的时间，而总 CPU 时间包括。

### 4. 使用 Profiler 分析内存消耗

PyTorch Profiler 还可以显示在模型操作符执行期间分配（或释放）的内存量（由模型张量使用）。

```python
model = models.resnet18()
inputs = torch.randn(5, 3, 224, 224)

with profile(
    activities=[ProfilerActivity.CPU], profile_memory=True, record_shapes=True
) as prof:
    model(inputs)

print(prof.key_averages().table(sort_by="self_cpu_memory_usage", row_limit=10))
```

### 5. 使用追踪功能

分析结果可以输出为 `.json` 追踪文件：

```python
with profile(activities=activities) as prof:
    model(inputs)

prof.export_chrome_trace("trace.json")
```

你可以在 Chrome 追踪查看器（`chrome://tracing`）中检查已分析的操作符和 CUDA/XPU 内核的序列。

### 6. 检查堆栈追踪

Profiler 可用于分析 Python 和 TorchScript 堆栈追踪：

```python
with profile(
    activities=activities,
    with_stack=True,
    experimental_config=torch._C._profiler._ExperimentalConfig(verbose=True),
) as prof:
    model(inputs)

print(prof.key_averages(group_by_stack_n=5).table(sort_by=sort_by_keyword, row_limit=2))
```

（警告：堆栈追踪会增加额外的分析开销。）

### 7. 使用 Profiler 分析长时间运行的任务

PyTorch Profiler 提供了一个额外的 API 来处理长时间运行的任务（如训练循环）。追踪所有执行可能很慢并产生非常大的追踪文件。使用可选参数来避免这一点：

- `schedule` — 指定一个接受整数参数（步骤号）作为输入并返回 Profiler 操作的函数
- `on_trace_ready` — 指定一个接受 Profiler 引用作为输入的函数，每次新追踪准备好时由 Profiler 调用

```python
from torch.profiler import schedule

my_schedule = schedule(skip_first=10, wait=5, warmup=1, active=3, repeat=2)

def trace_handler(p):
    output = p.key_averages().table(sort_by=sort_by_keyword, row_limit=10)
    print(output)
    p.export_chrome_trace("/tmp/trace_" + str(p.step_num) + ".json")

with profile(
    activities=activities,
    schedule=torch.profiler.schedule(wait=1, warmup=1, active=2),
    on_trace_ready=trace_handler,
) as p:
    for idx in range(8):
        model(inputs)
        p.step()
```

## 了解更多

- [PyTorch Benchmark](https://pytorch.org/tutorials/recipes/recipes/benchmark.html)
- [使用 TensorBoard 可视化模型、数据和训练](https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) 教程
