Diffusers documentation

Installation

# Diffusers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv0.38.0v0.37.1v0.36.0v0.35.1v0.34.0v0.33.1v0.32.2v0.31.0v0.30.3v0.29.2v0.28.2v0.27.2v0.26.3v0.25.1v0.24.0v0.23.1v0.22.3v0.21.0v0.20.0v0.19.3v0.18.2v0.17.1v0.16.0v0.15.0v0.14.0v0.13.0v0.12.0v0.11.0v0.10.2v0.9.0v0.8.0v0.7.0v0.6.0v0.5.1v0.4.1v0.3.0v0.2.4 ENJAKOPTZH

[ ](https://github.com/huggingface/diffusers)

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

#  Installation

Diffusers is tested on Python 3.8+ and PyTorch 1.4+. Install [PyTorch](https://pytorch.org/get-started/locally/) according to your system and setup.

Create a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for easier management of separate projects and to avoid compatibility issues between dependencies. Use [uv](https://docs.astral.sh/uv/), a Rust-based Python package and project manager, to create a virtual environment and install Diffusers.

Copied
    
    
    uv venv my-env
    source my-env/bin/activate

Install Diffusers with one of the following methods.

pip 

conda 

source 

PyTorch only supports Python 3.8 - 3.11 on Windows.

Copied
    
    
    uv pip install diffusers["torch"] transformers

##  Editable install

An editable install is recommended for development workflows or if you’re using the `main` version of the source code. A special link is created between the cloned repository and the Python library paths. This avoids reinstalling a package after every change.

Clone the repository and install Diffusers with the following commands.

Copied
    
    
    git clone https://github.com/huggingface/diffusers.git
    cd diffusers
    uv pip install -e ".[torch]"

> You must keep the `diffusers` folder if you want to keep using the library with the editable install.

Update your cloned repository to the latest version of Diffusers with the command below.

Copied
    
    
    cd ~/diffusers/
    git pull

##  Cache

Model weights and files are downloaded from the Hub to a cache, which is usually your home directory. Change the cache location with the [HF_HOME](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhome) or [HF_HUB_CACHE](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhubcache) environment variables or configuring the `cache_dir` parameter in methods like [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained).

env variable 

from_pretrained 

Copied
    
    
    export HF_HOME="/path/to/your/cache"
    export HF_HUB_CACHE="/path/to/your/hub/cache"

Cached files allow you to use Diffusers offline. Set the [HF_HUB_OFFLINE](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhuboffline) environment variable to `1` to prevent Diffusers from connecting to the internet.

Copied
    
    
    export HF_HUB_OFFLINE=1

For more details about managing and cleaning the cache, take a look at the [Understand caching](https://huggingface.co/docs/huggingface_hub/guides/manage-cache) guide.

##  Telemetry logging

Diffusers gathers telemetry information during [from_pretrained()](/docs/diffusers/v0.38.0/en/api/pipelines/overview#diffusers.DiffusionPipeline.from_pretrained) requests. The data gathered includes the Diffusers and PyTorch version, the requested model or pipeline class, and the path to a pretrained checkpoint if it is hosted on the Hub.

This usage data helps us debug issues and prioritize new features. Telemetry is only sent when loading models and pipelines from the Hub, and it is not collected if you’re loading local files.

Opt-out and disable telemetry collection with the [HF_HUB_DISABLE_TELEMETRY](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhubdisabletelemetry) environment variable.

Linux/macOS 

Windows 

Copied
    
    
    export HF_HUB_DISABLE_TELEMETRY=1

[ Update on GitHub](https://github.com/huggingface/diffusers/blob/main/docs/source/en/installation.md)

[←Diffusers](/docs/diffusers/index) [Quickstart→](/docs/diffusers/quicktour)
