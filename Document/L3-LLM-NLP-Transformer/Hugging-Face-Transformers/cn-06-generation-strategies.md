[ Hugging Face](/)

Transformers 文档

生成策略

# Transformers

生成策略

解码策略（decoding strategy）决定了模型应如何选择下一个生成的词元。有多种类型的解码策略，选择合适的策略对生成文本的质量有重大影响。

本指南将帮助你了解 Transformers 中可用的不同解码策略以及如何以及何时使用它们。

## [](#basic-decoding-methods) 基本解码方法

这些是成熟的解码方法，应该是你文本生成任务的起点。

### [](#greedy-search) 贪心搜索（Greedy search）

贪心搜索是默认的解码策略。它在每一步选择下一个最可能的词元。除非在 [GenerationConfig](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationConfig) 中指定，否则此策略最多生成 20 个新词元。

贪心搜索适用于输出相对较短且创意不是优先考虑的任务。但是，在生成较长序列时效果不佳，因为它开始重复自身。

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from accelerate import Accelerator

    device = Accelerator().device

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
    inputs = tokenizer("Hugging Face is an open-source company", return_tensors="pt").to(device)

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", dtype=torch.float16).to(device)
    outputs = model.generate(**inputs, max_new_tokens=20)
    tokenizer.batch_decode(outputs, skip_special_tokens=True)
    'Hugging Face is an open-source company that provides a suite of tools and services for building, deploying, and maintaining natural language processing'

### [](#sampling) 采样（Sampling）

采样，或称多项式采样（multinomial sampling），基于整个模型词汇表上的概率分布随机选择词元（与贪心搜索中最可能的词元相反）。这意味着每个具有非零概率的词元都有被选中的机会。采样策略减少重复并可以生成更有创意和多样化的输出。

使用 `do_sample=True` 和 `num_beams=1` 启用多项式采样。

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from accelerate import Accelerator

    device = Accelerator().device

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
    inputs = tokenizer("Hugging Face is an open-source company", return_tensors="pt").to(device)

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", dtype=torch.float16).to(device)
    outputs = model.generate(**inputs, max_new_tokens=50, do_sample=True, num_beams=1)
    tokenizer.batch_decode(outputs, skip_special_tokens=True)

### [](#beam-search) 束搜索（Beam search）

束搜索在每个时间步跟踪多个生成的序列（束）。经过一定步数后，它选择_整体_概率最高的序列。与贪心搜索不同，此策略可以"向前看"并选择整体概率更高的序列，即使初始词元的概率较低。它最适合基于输入的任务，如描述图像或语音识别。你也可以将 `do_sample=True` 与束搜索一起使用以在每一步进行采样，但束搜索仍会在步骤之间贪心地修剪低概率序列。

> 查看[束搜索可视化工具](https://huggingface.co/spaces/m-ric/beam_search_visualizer)了解束搜索的工作原理。

使用 `num_beams` 参数启用束搜索（应大于 1，否则等同于贪心搜索）。

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from accelerate import Accelerator

    device = Accelerator().device

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
    inputs = tokenizer("Hugging Face is an open-source company", return_tensors="pt").to(device)

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", dtype=torch.float16).to(device)
    outputs = model.generate(**inputs, max_new_tokens=50, num_beams=2)
    tokenizer.batch_decode(outputs, skip_special_tokens=True)

## [](#custom-generation-methods) 自定义生成方法

自定义生成方法支持特殊行为，例如：

  * 如果模型不确定，让模型继续思考；
  * 如果模型卡住，回滚生成；
  * 使用自定义逻辑处理特殊词元；
  * 使用专门的 KV 缓存；

我们通过模型仓库启用自定义生成方法，假设特定的模型标签和文件结构（参见下面的小节）。此功能是[自定义建模代码](./models#custom-models)的扩展，与之类似，需要设置 `trust_remote_code=True`。

如果模型仓库包含自定义生成方法，最简单的尝试方式是加载模型并使用它进行生成：

    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("transformers-community/custom_generate_example")
    model = AutoModelForCausalLM.from_pretrained(
        "transformers-community/custom_generate_example", device_map="auto", trust_remote_code=True
    )

    inputs = tokenizer(["The quick brown"], return_tensors="pt").to(model.device)
    gen_out = model.generate(**inputs)
    print(tokenizer.batch_decode(gen_out, skip_special_tokens=True))
    'The quick brown fox jumps over a lazy dog, and the dog is a type of animal. Is'

具有自定义生成方法的模型仓库有一个特殊属性：它们的生成方法可以通过 [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) 的 `custom_generate` 参数从**任何**模型加载。这意味着任何人都可以创建和共享他们的自定义生成方法，以潜在地与任何 Transformers 模型一起工作，而无需用户安装额外的 Python 包。

    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct", device_map="auto")

    inputs = tokenizer(["The quick brown"], return_tensors="pt").to(model.device)
    gen_out = model.generate(**inputs, custom_generate="transformers-community/custom_generate_example", trust_remote_code=True)
    print(tokenizer.batch_decode(gen_out, skip_special_tokens=True)[0])
    'The quick brown fox jumps over a lazy dog, and the dog is a type of animal. Is'

### [](#creating-a-custom-generation-method) 创建自定义生成方法

要创建新的生成方法，你需要创建一个新的 [**模型**](https://huggingface.co/new)仓库并向其中推送几个文件。

  1. 你设计生成方法所用的模型。
  2. `custom_generate/generate.py`，包含自定义生成方法的所有逻辑。
  3. `custom_generate/requirements.txt`，用于可选地添加新的 Python 依赖和/或锁定特定版本以正确使用你的方法。
  4. `README.md`，你应该在此添加 `custom_generate` 标签并在此记录你的自定义方法的任何新参数或输出类型差异。

添加所有必需文件后，你的仓库应如下所示

    your_repo/
    ├── README.md          # 包含 'custom_generate' 标签
    ├── config.json
    ├── ...
    └── custom_generate/
        ├── generate.py
        └── requirements.txt

#### [](#generatepy) generate.py

这是你生成方法的核心。它_必须_包含一个名为 `generate` 的方法，且此方法_必须_包含一个 `model` 参数作为其第一个参数。`model` 是模型实例，这意味着你可以访问模型中的所有属性和方法，包括在 [GenerationMixin](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin) 中定义的那些（如基础的 `generate` 方法）。

> `generate.py` 必须放在名为 `custom_generate` 的文件夹中，而不是仓库的根级别。此功能的文件路径是硬编码的。

你的自定义 `generate` 方法可以从 `custom_generate` 文件夹中相对导入代码。例如，如果你有一个 `utils.py` 文件，可以这样导入：

    from .utils import some_function

### [](#finding-custom-generation-methods) 查找自定义生成方法

你可以通过[搜索自定义标签](https://huggingface.co/models?other=custom_generate) `custom_generate` 来找到所有自定义生成方法。除了标签外，我们还策划了两个 `custom_generate` 方法集合：

  * [自定义生成方法 - 社区](https://huggingface.co/collections/transformers-community/custom-generation-methods-community-6888fb1da0efbc592d3a8ab6) — 由社区贡献的强大方法集合；
  * [自定义生成方法 - 教程](https://huggingface.co/collections/transformers-community/custom-generation-methods-tutorials-6823589657a94940ea02cfec) — 以前是 `transformers` 一部分的方法的参考实现集合，以及 `custom_generate` 的教程。

## [](#resources) 资源

阅读[如何生成文本：使用 Transformers 进行语言生成的不同解码方法](https://huggingface.co/blog/how-to-generate)博客文章，了解常见解码策略的工作原理说明。

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/generation_strategies.md)

[←文本生成](/docs/transformers/llm_tutorial) [生成特性→](/docs/transformers/generation_features)

[生成策略](#generation-strategies)[基本解码方法](#basic-decoding-methods)[贪心搜索](#greedy-search)[采样](#sampling)[束搜索](#beam-search)[自定义生成方法](#custom-generation-methods)[创建自定义生成方法](#creating-a-custom-generation-method)[generate.py](#generatepy)[查找自定义生成方法](#finding-custom-generation-methods)[资源](#resources)
