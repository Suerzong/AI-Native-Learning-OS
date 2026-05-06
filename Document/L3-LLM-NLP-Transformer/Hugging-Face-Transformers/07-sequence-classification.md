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

Text classification

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

[Text classification](/docs/transformers/tasks/sequence_classification)[Token classification](/docs/transformers/tasks/token_classification)[Question answering](/docs/transformers/tasks/question_answering)[Causal language modeling](/docs/transformers/tasks/language_modeling)[Masked language modeling](/docs/transformers/tasks/masked_language_modeling)[Translation](/docs/transformers/tasks/translation)[Summarization](/docs/transformers/tasks/summarization)[Multiple choice](/docs/transformers/tasks/multiple_choice)

Audio

Computer vision

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

# [](#text-classification) Text classification

Text classification is a common NLP task that assigns a label or class to text. Some of the largest companies run text classification in production for a wide range of practical applications. One of the most popular forms of text classification is sentiment analysis, which assigns a label like 🙂 positive, 🙁 negative, or 😐 neutral to a sequence of text.

This guide will show you how to:

  1. Finetune [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) on the [IMDb](https://huggingface.co/datasets/imdb) dataset to determine whether a movie review is positive or negative.
  2. Use your finetuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/text-classification).

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate accelerate

We encourage you to login to your Hugging Face account so you can upload and share your model with the community. When prompted, enter your token to login:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-imdb-dataset) Load IMDb dataset

Start by loading the IMDb dataset from the 🤗 Datasets library:

Copied


    >>> from datasets import load_dataset

    >>> imdb = load_dataset("imdb")

Then take a look at an example:

Copied


    >>> imdb["test"][0]
    {
        "label": 0,
        "text": "I love sci-fi and am willing to put up with a lot. Sci-fi movies/TV are usually underfunded, under-appreciated and misunderstood. I tried to like this, I really did, but it is to good TV sci-fi as Babylon 5 is to Star Trek (the original). Silly prosthetics, cheap cardboard sets, stilted dialogues, CG that doesn't match the background, and painfully one-dimensional characters cannot be overcome with a 'sci-fi' setting. (I'm sure there are those of you out there who think Babylon 5 is good sci-fi TV. It's not. It's clichéd and uninspiring.) While US viewers might like emotion and character development, sci-fi is a genre that does not take itself seriously (cf. Star Trek). It may treat important issues, yet not as a serious philosophy. It's really difficult to care about the characters here as they are not simply foolish, just missing a spark of life. Their actions and reactions are wooden and predictable, often painful to watch. The makers of Earth KNOW it's rubbish as they have to always say \"Gene Roddenberry's Earth...\" otherwise people would not continue watching. Roddenberry's ashes must be turning in their orbit as this dull, cheap, poorly edited (watching it without advert breaks really brings this home) trudging Trabant of a show lumbers into space. Spoiler. So, kill off a main character. And then bring him back as another actor. Jeeez! Dallas all over again.",
    }

There are two fields in this dataset:

  * `text`: the movie review text.
  * `label`: a value that is either `0` for a negative review or `1` for a positive review.

## [](#preprocess) Preprocess

The next step is to load a DistilBERT tokenizer to preprocess the `text` field:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

Create a preprocessing function to tokenize `text` and truncate sequences to be no longer than DistilBERT’s maximum input length:

Copied


    >>> def preprocess_function(examples):
    ...     return tokenizer(examples["text"], truncation=True)

To apply the preprocessing function over the entire dataset, use 🤗 Datasets `map` function. You can speed up `map` by setting `batched=True` to process multiple elements of the dataset at once:

Copied


    tokenized_imdb = imdb.map(preprocess_function, batched=True)

Now create a batch of examples using [DataCollatorWithPadding](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorWithPadding). It’s more efficient to _dynamically pad_ the sentences to the longest length in a batch during collation, instead of padding the whole dataset to the maximum length.

Copied


    >>> from transformers import DataCollatorWithPadding

    >>> data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

## [](#evaluate) Evaluate

Including a metric during training is often helpful for evaluating your model’s performance. You can quickly load a evaluation method with the 🤗 [Evaluate](https://huggingface.co/docs/evaluate/index) library. For this task, load the [accuracy](https://huggingface.co/spaces/evaluate-metric/accuracy) metric (see the 🤗 Evaluate [quick tour](https://huggingface.co/docs/evaluate/a_quick_tour) to learn more about how to load and compute a metric):

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

Your `compute_metrics` function is ready to go now, and you’ll return to it when you setup your training.

## [](#train) Train

Before you start training your model, create a map of the expected ids to their labels with `id2label` and `label2id`:

Copied


    >>> id2label = {0: "NEGATIVE", 1: "POSITIVE"}
    >>> label2id = {"NEGATIVE": 0, "POSITIVE": 1}

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the basic tutorial [here](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load DistilBERT with [AutoModelForSequenceClassification](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification) along with the number of expected labels, and the label mappings:

Copied


    >>> from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

    >>> model = AutoModelForSequenceClassification.from_pretrained(
    ...     "distilbert/distilbert-base-uncased", num_labels=2, id2label=id2label, label2id=label2id
    ... )

At this point, only three steps remain:

  1. Define your training hyperparameters in [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments). The only required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model). At the end of each epoch, the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) will evaluate the accuracy and save the training checkpoint.
  2. Pass the training arguments to [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) along with the model, dataset, tokenizer, data collator, and `compute_metrics` function.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_model",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=2,
    ...     weight_decay=0.01,
    ...     eval_strategy="epoch",
    ...     save_strategy="epoch",
    ...     load_best_model_at_end=True,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_imdb["train"],
    ...     eval_dataset=tokenized_imdb["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

> [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) applies dynamic padding by default when you pass `tokenizer` to it. In this case, you don’t need to specify a data collator explicitly.

Once training is completed, share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for text classification, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb).

## [](#inference) Inference

Great, now that you’ve finetuned a model, you can use it for inference!

Grab some text you’d like to run inference on:

Copied


    >>> text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

The simplest way to try out your finetuned model for inference is to use it in a [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline). Instantiate a `pipeline` for sentiment analysis with your model, and pass your text to it:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")
    >>> classifier(text)
    [{'label': 'POSITIVE', 'score': 0.9994940757751465}]

You can also manually replicate the results of the `pipeline` if you’d like:

Tokenize the text and return PyTorch tensors:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
    >>> inputs = tokenizer(text, return_tensors="pt")

Pass your inputs to the model and return the `logits`:

Copied


    >>> from transformers import AutoModelForSequenceClassification

    >>> model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits

Get the class with the highest probability, and use the model’s `id2label` mapping to convert it to a text label:

Copied


    >>> predicted_class_id = logits.argmax().item()
    >>> model.config.id2label[predicted_class_id]
    'POSITIVE'

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/sequence_classification.md)

[←Unsloth](/docs/transformers/community_integrations/unsloth) [Token classification→](/docs/transformers/tasks/token_classification)

[Text classification](#text-classification)[Load IMDb dataset](#load-imdb-dataset)[Preprocess](#preprocess)[Evaluate](#evaluate)[Train](#train)[Inference](#inference)
