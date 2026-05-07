[ Hugging Face](/)

Transformers 文档

安装

# Transformers

安装

Transformers 与 [PyTorch](https://pytorch.org/get-started/locally/) 一起工作。已在 Python 3.10+ 和 PyTorch 2.4+ 上测试。

## [](#virtual-environment) 虚拟环境

[uv](https://docs.astral.sh/uv/) 是一个极快的基于 Rust 的 Python 包和项目管理器，默认需要[虚拟环境](https://docs.astral.sh/uv/pip/environments/)来管理不同项目并避免依赖之间的兼容性问题。

它可以作为 [pip](https://pip.pypa.io/en/stable/) 的直接替代品使用，但如果你更喜欢使用 pip，请从以下命令中移除 `uv`。

> 参考 uv [安装](https://docs.astral.sh/uv/guides/install-python/)文档安装 uv。

创建虚拟环境以在其中安装 Transformers。

    uv venv .env
    source .env/bin/activate

## [](#python) Python

使用以下命令安装 Transformers。

[uv](https://docs.astral.sh/uv/) 是一个快速的基于 Rust 的 Python 包和项目管理器。

    uv pip install transformers

对于 GPU 加速，为 [PyTorch](https://pytorch.org/get-started/locally) 安装适当的 CUDA 驱动程序。

运行以下命令检查你的系统是否检测到 NVIDIA GPU。

    nvidia-smi

要安装仅 CPU 版本的 Transformers，运行以下命令。

    uv pip install torch --index-url https://download.pytorch.org/whl/cpu
    uv pip install transformers

使用以下命令测试安装是否成功。它应为提供的文本返回标签和分数。

    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('hugging face is the best'))"
    [{'label': 'POSITIVE', 'score': 0.9998704791069031}]

### [](#source-install) 源码安装

从源码安装会安装库的_最新_版本而不是_稳定_版本。它确保你拥有 Transformers 中最新的更改，这对于尝试最新功能或修复尚未在稳定版本中正式发布的错误非常有用。

缺点是最新版本可能并不总是稳定的。如果你遇到任何问题，请提交 [GitHub Issue](https://github.com/huggingface/transformers/issues)，以便我们尽快修复。

使用以下命令从源码安装。

    uv pip install git+https://github.com/huggingface/transformers

使用以下命令检查安装是否成功。它应为提供的文本返回标签和分数。

    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('hugging face is the best'))"
    [{'label': 'POSITIVE', 'score': 0.9998704791069031}]

### [](#editable-install) 可编辑安装

如果你正在本地使用 Transformers 进行开发，[可编辑安装](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)非常有用。它将你的本地 Transformers 副本链接到 Transformers [仓库](https://github.com/huggingface/transformers)而不是复制文件。文件被添加到 Python 的导入路径中。

    git clone https://github.com/huggingface/transformers.git
    cd transformers
    uv pip install -e .

> 你必须保留本地 Transformers 文件夹以继续使用它。

使用以下命令将本地版本的 Transformers 更新为最新更改。

    cd ~/transformers/
    git pull

## [](#conda) conda

[conda](https://docs.conda.io/projects/conda/en/stable/#) 是一个语言无关的包管理器。在你新创建的虚拟环境中从 [conda-forge](https://anaconda.org/conda-forge/transformers) 频道安装 Transformers。

    conda install conda-forge::transformers

## [](#set-up) 配置

安装后，你可以配置 Transformers 缓存位置或设置库以供离线使用。

### [](#cache-directory) 缓存目录

当你使用 [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 加载预训练模型时，模型会从 Hub 下载并在本地缓存。

每次加载模型时，它都会检查缓存的模型是否是最新的。如果相同，则加载本地模型。如果不同，则下载更新的模型并缓存。

由 shell 环境变量 `HF_HUB_CACHE` 给出的默认目录是 `~/.cache/huggingface/hub`。在 Windows 上，默认目录是 `C:\Users\username\.cache\huggingface\hub`。

通过更改以下 shell 环境变量中的路径（按优先级列出）将模型缓存到不同的目录。

  1. [HF_HUB_CACHE](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#hfhubcache)（默认）
  2. [HF_HOME](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#hfhome)
  3. [XDG_CACHE_HOME](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#xdgcachehome) + `/huggingface`（仅在未设置 `HF_HOME` 时）

### [](#offline-mode) 离线模式

在离线或有防火墙的环境中使用 Transformers 需要提前下载并缓存文件。使用 `snapshot_download` 方法从 Hub 下载模型仓库。

> 参考 [从 Hub 下载文件](https://hf.co/docs/huggingface_hub/guides/download)指南了解从 Hub 下载文件的更多选项。你可以从特定修订版下载文件、从 CLI 下载，甚至过滤从仓库下载的文件。

    from huggingface_hub import snapshot_download

    snapshot_download(repo_id="meta-llama/Llama-2-7b-hf", repo_type="model")

设置环境变量 `HF_HUB_OFFLINE=1` 以在加载模型时阻止对 Hub 的 HTTP 调用。

    HF_HUB_OFFLINE=1 \
    python examples/pytorch/language-modeling/run_clm.py --model_name_or_path meta-llama/Llama-2-7b-hf --dataset_name wikitext ...

仅加载缓存文件的另一个选项是在 [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 中设置 `local_files_only=True`。

    from transformers import LlamaForCausalLM

    model = LlamaForCausalLM.from_pretrained("./path/to/local/directory", local_files_only=True)

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/installation.md)

[←Transformers](/docs/transformers/index) [快速入门→](/docs/transformers/quicktour)

[安装](#installation)[虚拟环境](#virtual-environment)[Python](#python)[源码安装](#source-install)[可编辑安装](#editable-install)[conda](#conda)[配置](#set-up)[缓存目录](#cache-directory)[离线模式](#offline-mode)
