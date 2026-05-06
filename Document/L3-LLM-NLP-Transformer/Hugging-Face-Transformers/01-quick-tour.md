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

Quickstart

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

# [](#quickstart) Quickstart

Transformers is designed to be fast and easy to use so that everyone can start learning or building with transformer models.

The number of user-facing abstractions is limited to only three classes for instantiating a model, and two APIs for inference or training. This quickstart introduces you to Transformers’ key features and shows you how to:

  * load a pretrained model
  * run inference with [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)
  * fine-tune a model with [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer)

## [](#set-up) Set up

To start, we recommend creating a Hugging Face [account](https://hf.co/join). An account lets you host and access version controlled models, datasets, and [Spaces](https://hf.co/spaces) on the Hugging Face [Hub](https://hf.co/docs/hub/index), a collaborative platform for discovery and building.

Create a [User Access Token](https://hf.co/docs/hub/security-tokens#user-access-tokens) and log in to your account.

notebook

CLI

Paste your User Access Token into `notebook_login` when prompted to log in.

Copied


    from huggingface_hub import notebook_login

    notebook_login()

Install PyTorch.

Copied


    !pip install torch

Then install an up-to-date version of Transformers and some additional libraries from the Hugging Face ecosystem for accessing datasets and vision models, evaluating training, and optimizing training for large models.

Copied


    !pip install -U transformers datasets evaluate accelerate timm

## [](#pretrained-models) Pretrained models

Each pretrained model inherits from three base classes.

**Class** | **Description**
---|---
[PreTrainedConfig](/docs/transformers/v5.8.0/en/main_classes/configuration#transformers.PreTrainedConfig) | A file that specifies a models attributes such as the number of attention heads or vocabulary size.
[PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel) | A model (or architecture) defined by the model attributes from the configuration file. A pretrained model only returns the raw hidden states. For a specific task, use the appropriate model head to convert the raw hidden states into a meaningful result (for example, [LlamaModel](/docs/transformers/v5.8.0/en/model_doc/llama2#transformers.LlamaModel) versus [LlamaForCausalLM](/docs/transformers/v5.8.0/en/model_doc/llama2#transformers.LlamaForCausalLM)).
Preprocessor | A class for converting raw inputs (text, images, audio, multimodal) into numerical inputs to the model. For example, [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend) converts text into tensors and [ImageProcessingMixin](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.ImageProcessingMixin) converts pixels into tensors.

We recommend using the [AutoClass](./model_doc/auto) API to load models and preprocessors because it automatically infers the appropriate architecture for each task and machine learning framework based on the name or path to the pretrained weights and configuration file.

Use [from_pretrained()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) to load the weights and configuration file from the Hub into the model and preprocessor class.

When you load a model, configure the following parameters to ensure the model is optimally loaded.

  * `device_map="auto"` automatically allocates the model weights to your fastest device first.
  * `dtype="auto"` directly initializes the model weights in the data type they’re stored in, which can help avoid loading the weights twice (PyTorch loads weights in `torch.float32` by default).

Copied


    from transformers import AutoModelForCausalLM, AutoTokenizer

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", dtype="auto", device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

Tokenize the text and return PyTorch tensors with the tokenizer. Move the model to an accelerator if it’s available to accelerate inference.

Copied


    model_inputs = tokenizer(["The secret to baking a good cake is "], return_tensors="pt").to(model.device)

The model is now ready for inference or training.

For inference, pass the tokenized inputs to [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) to generate text. Decode the token ids back into text with [batch_decode()](/docs/transformers/v5.8.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode).

Copied


    generated_ids = model.generate(**model_inputs, max_length=30)
    tokenizer.batch_decode(generated_ids)[0]
    '<s> The secret to baking a good cake is 100% in the preparation. There are so many recipes out there,'

> Skip ahead to the [Trainer](#trainer-api) section to learn how to fine-tune a model.

## [](#pipeline) Pipeline

The [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) class is the most convenient way to inference with a pretrained model. It supports many tasks such as text generation, image segmentation, automatic speech recognition, document question answering, and more.

> Refer to the [Pipeline](./main_classes/pipelines) API reference for a complete list of available tasks.

Create a [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) object and select a task. By default, [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) downloads and caches a default pretrained model for a given task. Pass the model name to the `model` parameter to choose a specific model.

text generation

image segmentation

automatic speech recognition

Use `Accelerator` to automatically detect an available accelerator for inference.

Copied


    from transformers import pipeline
    from accelerate import Accelerator

    device = Accelerator().device

    pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf", device=device)

Prompt [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) with some initial text to generate more text.

Copied


    pipeline("The secret to baking a good cake is ", max_length=50)
    [{'generated_text': 'The secret to baking a good cake is 100% in the batter. The secret to a great cake is the icing.\nThis is why we’ve created the best buttercream frosting reci'}]

## [](#trainer) Trainer

[Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) is a complete training and evaluation loop for PyTorch models. It abstracts away a lot of the boilerplate usually involved in manually writing a training loop, so you can start training faster and focus on training design choices. You only need a model, dataset, a preprocessor, and a data collator to build batches of data from the dataset.

Use the [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments) class to customize the training process. It provides many options for training, evaluation, and more. Experiment with training hyperparameters and features like batch size, learning rate, mixed precision, torch.compile, and more to meet your training needs. You could also use the default training parameters to quickly produce a baseline.

Load a model, tokenizer, and dataset for training.

Copied


    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from datasets import load_dataset

    model = AutoModelForSequenceClassification.from_pretrained("distilbert/distilbert-base-uncased")
    tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
    dataset = load_dataset("rotten_tomatoes")

Create a function to tokenize the text and convert it into PyTorch tensors. Apply this function to the whole dataset with the `map` method.

Copied


    def tokenize_dataset(dataset):
        return tokenizer(dataset["text"])
    dataset = dataset.map(tokenize_dataset, batched=True)

Load a data collator to create batches of data and pass the tokenizer to it.

Copied


    from transformers import DataCollatorWithPadding

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

Next, set up [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments) with the training features and hyperparameters.

Copied


    from transformers import TrainingArguments

    training_args = TrainingArguments(
        output_dir="distilbert-rotten-tomatoes",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=2,
        push_to_hub=True,
    )

Finally, pass all these separate components to [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) and call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to start.

Copied


    from transformers import Trainer

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        processing_class=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()

Share your model and tokenizer to the Hub with [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub).

Copied


    trainer.push_to_hub()

Congratulations, you just trained your first model with Transformers!

## [](#next-steps) Next steps

Now that you have a better understanding of Transformers and what it offers, it’s time to keep exploring and learning what interests you the most.

  * **Base classes** : Learn more about the configuration, model and processor classes. This will help you understand how to create and customize models, preprocess different types of inputs (audio, images, multimodal), and how to share your model.
  * **Inference** : Explore the [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline) further, inference and chatting with LLMs, agents, and how to optimize inference with your machine learning framework and hardware.
  * **Training** : Study the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) in more detail, as well as distributed training and optimizing training on specific hardware.
  * **Quantization** : Reduce memory and storage requirements with quantization and speed up inference by representing weights with fewer bits.
  * **Resources** : Looking for end-to-end recipes for how to train and inference with a model for a specific task? Check out the task recipes!

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/quicktour.md)

[←Installation](/docs/transformers/installation) [Dynamic weight loading→](/docs/transformers/weightconverter)

[Quickstart](#quickstart)[Set up](#set-up)[Pretrained models](#pretrained-models)[Pipeline](#pipeline)[Trainer](#trainer)[Next steps](#next-steps)
