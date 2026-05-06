Diffusers documentation

Overview

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

#  Overview

🤗 Diffusers provides a collection of training scripts for you to train your own diffusion models. You can find all of our training scripts in [diffusers/examples](https://github.com/huggingface/diffusers/tree/main/examples).

Each training script is:

  * **Self-contained** : the training script does not depend on any local files, and all packages required to run the script are installed from the `requirements.txt` file.
  * **Easy-to-tweak** : the training scripts are an example of how to train a diffusion model for a specific task and won’t work out-of-the-box for every training scenario. You’ll likely need to adapt the training script for your specific use-case. To help you with that, we’ve fully exposed the data preprocessing code and the training loop so you can modify it for your own use.
  * **Beginner-friendly** : the training scripts are designed to be beginner-friendly and easy to understand, rather than including the latest state-of-the-art methods to get the best and most competitive results. Any training methods we consider too complex are purposefully left out.
  * **Single-purpose** : each training script is expressly designed for only one task to keep it readable and understandable.

Our current collection of training scripts include:

Training | SDXL-support | LoRA-support  
---|---|---  
[unconditional image generation](https://github.com/huggingface/diffusers/tree/main/examples/unconditional_image_generation) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/training_example.ipynb) |  |   
[text-to-image](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image) | 👍 | 👍  
[textual inversion](https://github.com/huggingface/diffusers/tree/main/examples/textual_inversion) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_textual_inversion_training.ipynb) |  |   
[DreamBooth](https://github.com/huggingface/diffusers/tree/main/examples/dreambooth) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb) | 👍 | 👍  
[ControlNet](https://github.com/huggingface/diffusers/tree/main/examples/controlnet) | 👍 |   
[InstructPix2Pix](https://github.com/huggingface/diffusers/tree/main/examples/instruct_pix2pix) | 👍 |   
[Custom Diffusion](https://github.com/huggingface/diffusers/tree/main/examples/custom_diffusion) |  |   
[T2I-Adapters](https://github.com/huggingface/diffusers/tree/main/examples/t2i_adapter) | 👍 |   
[Kandinsky 2.2](https://github.com/huggingface/diffusers/tree/main/examples/kandinsky2_2/text_to_image) |  | 👍  
[Wuerstchen](https://github.com/huggingface/diffusers/tree/main/examples/wuerstchen/text_to_image) |  | 👍  
  
These examples are **actively** maintained, so please feel free to open an issue if they aren’t working as expected. If you feel like another training example should be included, you’re more than welcome to start a [Feature Request](https://github.com/huggingface/diffusers/issues/new?assignees=&labels=&template=feature_request.md&title=) to discuss your feature idea with us and whether it meets our criteria of being self-contained, easy-to-tweak, beginner-friendly, and single-purpose.

##  Install

Make sure you can successfully run the latest versions of the example scripts by installing the library from source in a new virtual environment:

Copied
    
    
    git clone https://github.com/huggingface/diffusers
    cd diffusers
    pip install .

Then navigate to the folder of the training script (for example, [DreamBooth](https://github.com/huggingface/diffusers/tree/main/examples/dreambooth)) and install the `requirements.txt` file. Some training scripts have a specific requirement file for SDXL or LoRA. If you’re using one of these scripts, make sure you install its corresponding requirements file.

Copied
    
    
    cd examples/dreambooth
    pip install -r requirements.txt
    # to train SDXL with DreamBooth
    pip install -r requirements_sdxl.txt

To speedup training and reduce memory-usage, we recommend:

  * using PyTorch 2.0 or higher to automatically use [scaled dot product attention](../optimization/fp16#scaled-dot-product-attention) during training (you don’t need to make any changes to the training code)
  * installing [xFormers](../optimization/xformers) to enable memory-efficient attention

[ Update on GitHub](https://github.com/huggingface/diffusers/blob/main/docs/source/en/training/overview.md)

[←Using Custom Blocks with Mellon](/docs/diffusers/modular_diffusers/mellon) [Create a dataset for training→](/docs/diffusers/training/create_dataset)
