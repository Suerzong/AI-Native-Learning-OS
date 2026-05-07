# 安装

Diffusers 在 Python 3.8+ 和 PyTorch 1.4+ 上测试通过。请根据你的系统和设置安装 [PyTorch](https://pytorch.org/get-started/locally/)。

创建一个[虚拟环境](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)以便更轻松地管理独立项目并避免依赖之间的兼容性问题。使用 [uv](https://docs.astral.sh/uv/)（一个基于 Rust 的 Python 包和项目管理器）来创建虚拟环境并安装 Diffusers。

    uv venv my-env
    source my-env/bin/activate

使用以下方法之一安装 Diffusers。

pip / conda / source

    uv pip install diffusers["torch"] transformers

> PyTorch 在 Windows 上仅支持 Python 3.8 - 3.11。

## 可编辑安装

对于开发工作流或使用源码的 `main` 版本，推荐使用可编辑安装。这会在克隆的仓库和 Python 库路径之间创建一个特殊的链接，避免每次更改后重新安装包。

克隆仓库并使用以下命令安装 Diffusers：

    git clone https://github.com/huggingface/diffusers.git
    cd diffusers
    uv pip install -e ".[torch]"

> 如果你想继续使用可编辑安装的库，必须保留 `diffusers` 文件夹。

使用以下命令将克隆的仓库更新到最新版本：

    cd ~/diffusers/
    git pull

## 缓存

模型权重和文件从 Hub 下载到缓存目录，通常是你的主目录。可以通过 [HF_HOME](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhome) 或 [HF_HUB_CACHE](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhubcache) 环境变量更改缓存位置，或在 [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained) 等方法中配置 `cache_dir` 参数。

    export HF_HOME="/path/to/your/cache"
    export HF_HUB_CACHE="/path/to/your/hub/cache"

缓存文件允许你在离线状态下使用 Diffusers。将 [HF_HUB_OFFLINE](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhuboffline) 环境变量设置为 `1` 可阻止 Diffusers 连接到互联网。

    export HF_HUB_OFFLINE=1

有关管理和清理缓存的更多详情，请参阅[理解缓存](https://huggingface.co/docs/huggingface_hub/guides/manage-cache)指南。

## 遥测日志

Diffusers 在 [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained) 请求期间收集遥测信息。收集的数据包括 Diffusers 和 PyTorch 版本、请求的模型或流水线类，以及托管在 Hub 上的预训练检查点路径。

此使用数据帮助我们调试问题和优先安排新功能。遥测仅在从 Hub 加载模型和流水线时发送，加载本地文件时不收集。

使用 [HF_HUB_DISABLE_TELEMETRY](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhubdisabletelemetry) 环境变量选择退出并禁用遥测收集。

    export HF_HUB_DISABLE_TELEMETRY=1
