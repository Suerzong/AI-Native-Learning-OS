[ Hugging Face](/)

  * [ Models ](/models)
  * [ Datasets ](/datasets)
  * [ Spaces ](/spaces)
  * [ Buckets new](/storage)
  * [ Docs ](/docs)
  * [ Enterprise ](/enterprise)
  * [Pricing](/pricing)
  *   * * * *

  * [Log In](/login)
  * [Sign Up](/join)

Transformers documentation

Installation

# Transformers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv5.8.0v5.7.0v5.6.2v5.5.4v5.4.0v5.3.0v5.2.0v5.1.0v5.0.0v4.57.6v4.56.2v4.55.4v4.53.3v4.52.3v4.51.3v4.50.0v4.49.0v4.48.2v4.47.1v4.46.3v4.45.2v4.44.2v4.43.4v4.42.4v4.41.2v4.40.2v4.39.3v4.38.2v4.37.2v4.36.1v4.35.2v4.34.1v4.33.3v4.32.1v4.31.0v4.30.0v4.29.1v4.28.1v4.27.2v4.26.1v4.25.1v4.24.0v4.23.1v4.22.2v4.21.3v4.20.1v4.19.4v4.18.0v4.17.0v4.16.2v4.15.0v4.14.1v4.13.0v4.12.5v4.11.3v4.10.1v4.9.2v4.8.2v4.7.0v4.6.0v4.5.1v4.4.2v4.3.3v4.2.2v4.1.1v4.0.1v3.5.1v3.4.0v3.3.1v3.2.0v3.1.0v3.0.2v2.11.0v2.10.0v2.9.1v2.8.0v2.7.0v2.6.0v2.5.1v2.4.1v2.3.0v2.2.2v2.1.1v2.0.0v1.2.0v1.1.0v1.0.0doc-builder-html ARDEENESFRHIITJAKOPTTRZH

[ ](https://github.com/huggingface/transformers)

Get started

[Transformers](/docs/transformers/index)[Installation](/docs/transformers/installation)[Quickstart](/docs/transformers/quicktour)

Base classes

Models

Preprocessors

Inference

Pipeline API

Generate API

Optimization

Chat with models

Serving

Training

Get started

Customization

[Parameter-efficient fine-tuning](/docs/transformers/peft)

Performance

Distributed training

Hardware

Quantization

Ecosystem integrations

Resources

API

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#installation) Installation

Transformers works with [PyTorch](https://pytorch.org/get-started/locally/). It has been tested on Python 3.10+ and PyTorch 2.4+.

## [](#virtual-environment) Virtual environment

[uv](https://docs.astral.sh/uv/) is an extremely fast Rust-based Python package and project manager and requires a [virtual environment](https://docs.astral.sh/uv/pip/environments/) by default to manage different projects and avoids compatibility issues between dependencies.

It can be used as a drop-in replacement for [pip](https://pip.pypa.io/en/stable/), but if you prefer to use pip, remove `uv` from the commands below.

> Refer to the uv [installation](https://docs.astral.sh/uv/guides/install-python/) docs to install uv.

Create a virtual environment to install Transformers in.

Copied


    uv venv .env
    source .env/bin/activate

## [](#python) Python

Install Transformers with the following command.

[uv](https://docs.astral.sh/uv/) is a fast Rust-based Python package and project manager.

Copied


    uv pip install transformers

For GPU acceleration, install the appropriate CUDA drivers for [PyTorch](https://pytorch.org/get-started/locally).

Run the command below to check if your system detects an NVIDIA GPU.

Copied


    nvidia-smi

To install a CPU-only version of Transformers, run the following command.

Copied


    uv pip install torch --index-url https://download.pytorch.org/whl/cpu
    uv pip install transformers

Test whether the install was successful with the following command. It should return a label and score for the provided text.

Copied


    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('hugging face is the best'))"
    [{'label': 'POSITIVE', 'score': 0.9998704791069031}]

### [](#source-install) Source install

Installing from source installs the _latest_ version rather than the _stable_ version of the library. It ensures you have the most up-to-date changes in Transformers and it’s useful for experimenting with the latest features or fixing a bug that hasn’t been officially released in the stable version yet.

The downside is that the latest version may not always be stable. If you encounter any problems, please open a [GitHub Issue](https://github.com/huggingface/transformers/issues) so we can fix it as soon as possible.

Install from source with the following command.

Copied


    uv pip install git+https://github.com/huggingface/transformers

Check if the install was successful with the command below. It should return a label and score for the provided text.

Copied


    python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('hugging face is the best'))"
    [{'label': 'POSITIVE', 'score': 0.9998704791069031}]

### [](#editable-install) Editable install

An [editable install](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs) is useful if you’re developing locally with Transformers. It links your local copy of Transformers to the Transformers [repository](https://github.com/huggingface/transformers) instead of copying the files. The files are added to Python’s import path.

Copied


    git clone https://github.com/huggingface/transformers.git
    cd transformers
    uv pip install -e .

> You must keep the local Transformers folder to keep using it.

Update your local version of Transformers with the latest changes in the main repository with the following command.

Copied


    cd ~/transformers/
    git pull

## [](#conda) conda

[conda](https://docs.conda.io/projects/conda/en/stable/#) is a language-agnostic package manager. Install Transformers from the [conda-forge](https://anaconda.org/conda-forge/transformers) channel in your newly created virtual environment.

Copied


    conda install conda-forge::transformers

## [](#set-up) Set up

After installation, you can configure the Transformers cache location or set up the library for offline usage.

### [](#cache-directory) Cache directory

When you load a pretrained model with [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained), the model is downloaded from the Hub and locally cached.

Every time you load a model, it checks whether the cached model is up-to-date. If it’s the same, then the local model is loaded. If it’s not the same, the newer model is downloaded and cached.

The default directory given by the shell environment variable `HF_HUB_CACHE` is `~/.cache/huggingface/hub`. On Windows, the default directory is `C:\Users\username\.cache\huggingface\hub`.

Cache a model in a different directory by changing the path in the following shell environment variables (listed by priority).

  1. [HF_HUB_CACHE](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#hfhubcache) (default)
  2. [HF_HOME](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#hfhome)
  3. [XDG_CACHE_HOME](https://hf.co/docs/huggingface_hub/package_reference/environment_variables#xdgcachehome) \+ `/huggingface` (only if `HF_HOME` is not set)

### [](#offline-mode) Offline mode

To use Transformers in an offline or firewalled environment requires the downloaded and cached files ahead of time. Download a model repository from the Hub with the `snapshot_download` method.

> Refer to the [Download files from the Hub](https://hf.co/docs/huggingface_hub/guides/download) guide for more options for downloading files from the Hub. You can download files from specific revisions, download from the CLI, and even filter which files to download from a repository.

Copied


    from huggingface_hub import snapshot_download

    snapshot_download(repo_id="meta-llama/Llama-2-7b-hf", repo_type="model")

Set the environment variable `HF_HUB_OFFLINE=1` to prevent HTTP calls to the Hub when loading a model.

Copied


    HF_HUB_OFFLINE=1 \
    python examples/pytorch/language-modeling/run_clm.py --model_name_or_path meta-llama/Llama-2-7b-hf --dataset_name wikitext ...

Another option for only loading cached files is to set `local_files_only=True` in [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained).

Copied


    from transformers import LlamaForCausalLM

    model = LlamaForCausalLM.from_pretrained("./path/to/local/directory", local_files_only=True)

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/installation.md)

[←Transformers](/docs/transformers/index) [Quickstart→](/docs/transformers/quicktour)

[Installation](#installation)[Virtual environment](#virtual-environment)[Python](#python)[Source install](#source-install)[Editable install](#editable-install)[conda](#conda)[Set up](#set-up)[Cache directory](#cache-directory)[Offline mode](#offline-mode)
