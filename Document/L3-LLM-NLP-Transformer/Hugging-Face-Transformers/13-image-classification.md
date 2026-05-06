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

Image classification

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

Task recipes

Natural language processing

Audio

Computer vision

[Image classification](/docs/transformers/tasks/image_classification)[Image segmentation](/docs/transformers/tasks/semantic_segmentation)[Video classification](/docs/transformers/tasks/video_classification)[Object detection](/docs/transformers/tasks/object_detection)[Zero-shot object detection](/docs/transformers/tasks/zero_shot_object_detection)[Zero-shot image classification](/docs/transformers/tasks/zero_shot_image_classification)[Depth estimation](/docs/transformers/tasks/monocular_depth_estimation)[Image Feature Extraction](/docs/transformers/tasks/image_feature_extraction)[Mask Generation](/docs/transformers/tasks/mask_generation)[Keypoint detection](/docs/transformers/tasks/keypoint_detection)[Knowledge Distillation for Computer Vision](/docs/transformers/tasks/knowledge_distillation_for_image_classification)[Keypoint matching](/docs/transformers/tasks/keypoint_matching)[Training vision models using Backbone API](/docs/transformers/tasks/training_vision_backbone)

Multimodal

[Training scripts](/docs/transformers/run_scripts)[Glossary](/docs/transformers/glossary)[Philosophy](/docs/transformers/philosophy)[Models Timeline](/docs/transformers/models_timeline)[Notebooks with examples](/docs/transformers/notebooks)[Community resources](/docs/transformers/community)[Troubleshoot](/docs/transformers/troubleshooting)

API

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#image-classification) Image classification

Image classification assigns a label or class to an image. Unlike text or audio classification, the inputs are the pixel values that comprise an image. There are many applications for image classification, such as detecting damage after a natural disaster, monitoring crop health, or helping screen medical images for signs of disease.

This guide illustrates how to:

  1. Fine-tune [ViT](../model_doc/vit) on the [Food-101](https://huggingface.co/datasets/ethz/food101) dataset to classify a food item in an image.
  2. Use your fine-tuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/image-classification)

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate accelerate pillow torchvision scikit-learn trackio

We encourage you to log in to your Hugging Face account to upload and share your model with the community. When prompted, enter your token to log in:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-food-101-dataset) Load Food-101 dataset

Start by loading a smaller subset of the Food-101 dataset from the 🤗 Datasets library. This will give you a chance to experiment and make sure everything works before spending more time training on the full dataset.

Copied


    >>> from datasets import load_dataset

    >>> food = load_dataset("ethz/food101", split="train[:5000]")

Split the dataset’s `train` split into a train and test set with the `train_test_split` method:

Copied


    >>> food = food.train_test_split(test_size=0.2)

Then take a look at an example:

Copied


    >>> food["train"][0]
    {'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=512x512 at 0x7F52AFC8AC50>,
     'label': 79}

Each example in the dataset has two fields:

  * `image`: a PIL image of the food item
  * `label`: the label class of the food item

To make it easier for the model to get the label name from the label id, create a dictionary that maps the label name to an integer and vice versa:

Copied


    >>> labels = food["train"].features["label"].names
    >>> label2id, id2label = dict(), dict()
    >>> for i, label in enumerate(labels):
    ...     label2id[label] = str(i)
    ...     id2label[str(i)] = label

Now you can convert the label id to a label name:

Copied


    >>> id2label[str(79)]
    'prime_rib'

## [](#preprocess) Preprocess

The next step is to load a ViT image processor to process the image into a tensor:

Copied


    >>> from transformers import AutoImageProcessor

    >>> checkpoint = "google/vit-base-patch16-224-in21k"
    >>> image_processor = AutoImageProcessor.from_pretrained(checkpoint)

Apply some image transformations to the images to make the model more robust against overfitting. Here you’ll use torchvision’s [`transforms`](https://pytorch.org/vision/stable/transforms.html) module, but you can also use any image library you like.

Crop a random part of the image, resize it, and normalize it with the image mean and standard deviation:

Copied


    >>> from torchvision.transforms import RandomResizedCrop, Compose, Normalize, ToTensor

    >>> normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)
    >>> size = (
    ...     image_processor.size["shortest_edge"]
    ...     if "shortest_edge" in image_processor.size
    ...     else (image_processor.size["height"], image_processor.size["width"])
    ... )
    >>> _transforms = Compose([RandomResizedCrop(size), ToTensor(), normalize])

Then create a preprocessing function to apply the transforms and return the `pixel_values` \- the inputs to the model - of the image:

Copied


    >>> def transforms(examples):
    ...     examples["pixel_values"] = [_transforms(img.convert("RGB")) for img in examples["image"]]
    ...     del examples["image"]
    ...     return examples

To apply the preprocessing function over the entire dataset, use 🤗 Datasets `with_transform` method. The transforms are applied on the fly when you load an element of the dataset:

Copied


    >>> food = food.with_transform(transforms)

Now create a batch of examples using [DefaultDataCollator](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DefaultDataCollator). Unlike other data collators in 🤗 Transformers, the `DefaultDataCollator` does not apply additional preprocessing such as padding.

Copied


    >>> from transformers import DefaultDataCollator

    >>> data_collator = DefaultDataCollator()

## [](#evaluate) Evaluate

Including a metric during training is often helpful for evaluating your model’s performance. You can quickly load an evaluation method with the 🤗 [Evaluate](https://huggingface.co/docs/evaluate/index) library. For this task, load the [accuracy](https://huggingface.co/spaces/evaluate-metric/accuracy) metric (see the 🤗 Evaluate [quick tour](https://huggingface.co/docs/evaluate/a_quick_tour) to learn more about how to load and compute a metric):

Copied


    >>> import evaluate

    >>> accuracy = evaluate.load("accuracy")

Then create a function that passes your predictions and labels to [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) to calculate the accuracy:

Copied


    >>> import numpy as np


    >>> def compute_metrics(eval_pred):
    ...     predictions, labels = eval_pred
    ...     predictions = np.argmax(predictions, axis=1)
    ...     return accuracy.compute(predictions=predictions, references=labels)

Your `compute_metrics` function is ready to go now, and you’ll return to it when you set up your training.

## [](#train) Train

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the basic tutorial [here](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load ViT with [AutoModelForImageClassification](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForImageClassification). Specify the number of labels along with the number of expected labels, and the label mappings:

Copied


    >>> from transformers import AutoModelForImageClassification, TrainingArguments, Trainer

    >>> model = AutoModelForImageClassification.from_pretrained(
    ...     checkpoint,
    ...     num_labels=len(labels),
    ...     id2label=id2label,
    ...     label2id=label2id,
    ... )

At this point, only three steps remain:

  1. Define your training hyperparameters in [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments). It is important you don’t remove unused columns because that’ll drop the `image` column. Without the `image` column, you can’t create `pixel_values`. Set `remove_unused_columns=False` to prevent this behavior! The only other required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model). At the end of each epoch, the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) will evaluate the accuracy and save the training checkpoint.
  2. Pass the training arguments to [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) along with the model, dataset, tokenizer, data collator, and `compute_metrics` function.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_food_model",
    ...     remove_unused_columns=False,
    ...     eval_strategy="epoch",
    ...     save_strategy="epoch",
    ...     learning_rate=5e-5,
    ...     per_device_train_batch_size=16,
    ...     gradient_accumulation_steps=4,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=3,
    ...     warmup_steps=0.1,
    ...     logging_steps=10,
    ...     report_to="trackio",
    ...     run_name="food101",
    ...     load_best_model_at_end=True,
    ...     metric_for_best_model="accuracy",
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     data_collator=data_collator,
    ...     train_dataset=food["train"],
    ...     eval_dataset=food["test"],
    ...     processing_class=image_processor,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

Once training is completed, share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for image classification, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/image_classification.ipynb).

## [](#inference) Inference

Great, now that you’ve fine-tuned a model, you can use it for inference!

Load an image you’d like to run inference on:

Copied


    >>> ds = load_dataset("ethz/food101", split="validation[:10]")
    >>> image = ds["image"][0]

The simplest way to try out your finetuned model for inference is to use it in a [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline). Instantiate a `pipeline` for image classification with your model, and pass your image to it:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline("image-classification", model="my_awesome_food_model")
    >>> classifier(image)
    [{'score': 0.31856709718704224, 'label': 'beignets'},
     {'score': 0.015232225880026817, 'label': 'bruschetta'},
     {'score': 0.01519392803311348, 'label': 'chicken_wings'},
     {'score': 0.013022331520915031, 'label': 'pork_chop'},
     {'score': 0.012728818692266941, 'label': 'prime_rib'}]

You can also manually replicate the results of the `pipeline` if you’d like:

Load an image processor to preprocess the image and return the `input` as PyTorch tensors:

Copied


    >>> from transformers import AutoImageProcessor
    >>> import torch

    >>> image_processor = AutoImageProcessor.from_pretrained("my_awesome_food_model")
    >>> inputs = image_processor(image, return_tensors="pt")

Pass your inputs to the model and return the logits:

Copied


    >>> from transformers import AutoModelForImageClassification

    >>> model = AutoModelForImageClassification.from_pretrained("my_awesome_food_model")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits

Get the predicted label with the highest probability, and use the model’s `id2label` mapping to convert it to a label:

Copied


    >>> predicted_label = logits.argmax(-1).item()
    >>> model.config.id2label[predicted_label]
    'beignets'

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/image_classification.md)

[←Text to speech](/docs/transformers/tasks/text-to-speech) [Image segmentation→](/docs/transformers/tasks/semantic_segmentation)

[Image classification](#image-classification)[Load Food-101 dataset](#load-food-101-dataset)[Preprocess](#preprocess)[Evaluate](#evaluate)[Train](#train)[Inference](#inference)
