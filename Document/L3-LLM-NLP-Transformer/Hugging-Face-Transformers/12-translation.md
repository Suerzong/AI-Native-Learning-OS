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

Translation

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

# [](#translation) Translation

Translation converts a sequence of text from one language to another. It is one of several tasks you can formulate as a sequence-to-sequence problem, a powerful framework for returning some output from an input, like translation or summarization. Translation systems are commonly used for translation between different language texts, but it can also be used for speech or some combination in between like text-to-speech or speech-to-text.

This guide will show you how to:

  1. Finetune [T5](https://huggingface.co/google-t5/t5-small) on the English-French subset of the [OPUS Books](https://huggingface.co/datasets/opus_books) dataset to translate English text to French.
  2. Use your finetuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/translation).

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate sacrebleu

We encourage you to login to your Hugging Face account so you can upload and share your model with the community. When prompted, enter your token to login:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-opus-books-dataset) Load OPUS Books dataset

Start by loading the English-French subset of the [OPUS Books](https://huggingface.co/datasets/opus_books) dataset from the 🤗 Datasets library:

Copied


    >>> from datasets import load_dataset

    >>> books = load_dataset("opus_books", "en-fr")

Split the dataset into a train and test set with the `train_test_split` method:

Copied


    >>> books = books["train"].train_test_split(test_size=0.2)

Then take a look at an example:

Copied


    >>> books["train"][0]
    {'id': '90560',
     'translation': {'en': 'But this lofty plateau measured only a few fathoms, and soon we reentered Our Element.',
      'fr': 'Mais ce plateau élevé ne mesurait que quelques toises, et bientôt nous fûmes rentrés dans notre élément.'}}

`translation`: an English and French translation of the text.

## [](#preprocess) Preprocess

The next step is to load a T5 tokenizer to process the English-French language pairs:

Copied


    >>> from transformers import AutoTokenizer

    >>> checkpoint = "google-t5/t5-small"
    >>> tokenizer = AutoTokenizer.from_pretrained(checkpoint)

The preprocessing function you want to create needs to:

  1. Prefix the input with a prompt so T5 knows this is a translation task. Some models capable of multiple NLP tasks require prompting for specific tasks.
  2. Set the target language (French) in the `text_target` parameter to ensure the tokenizer processes the target text correctly. If you don’t set `text_target`, the tokenizer processes the target text as English.
  3. Truncate sequences to be no longer than the maximum length set by the `max_length` parameter.

Copied


    >>> source_lang = "en"
    >>> target_lang = "fr"
    >>> prefix = "translate English to French: "


    >>> def preprocess_function(examples):
    ...     inputs = [prefix + example[source_lang] for example in examples["translation"]]
    ...     targets = [example[target_lang] for example in examples["translation"]]
    ...     model_inputs = tokenizer(inputs, text_target=targets, max_length=128, truncation=True)
    ...     return model_inputs

To apply the preprocessing function over the entire dataset, use 🤗 Datasets `map` method. You can speed up the `map` function by setting `batched=True` to process multiple elements of the dataset at once:

Copied


    >>> tokenized_books = books.map(preprocess_function, batched=True)

Now create a batch of examples using [DataCollatorForSeq2Seq](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForSeq2Seq). It’s more efficient to _dynamically pad_ the sentences to the longest length in a batch during collation, instead of padding the whole dataset to the maximum length.

Copied


    >>> from transformers import DataCollatorForSeq2Seq

    >>> data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)

## [](#evaluate) Evaluate

Including a metric during training is often helpful for evaluating your model’s performance. You can quickly load a evaluation method with the 🤗 [Evaluate](https://huggingface.co/docs/evaluate/index) library. For this task, load the [SacreBLEU](https://huggingface.co/spaces/evaluate-metric/sacrebleu) metric (see the 🤗 Evaluate [quick tour](https://huggingface.co/docs/evaluate/a_quick_tour) to learn more about how to load and compute a metric):

Copied


    >>> import evaluate

    >>> metric = evaluate.load("sacrebleu")

Then create a function that passes your predictions and labels to [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) to calculate the SacreBLEU score:

Copied


    >>> import numpy as np


    >>> def postprocess_text(preds, labels):
    ...     preds = [pred.strip() for pred in preds]
    ...     labels = [[label.strip()] for label in labels]

    ...     return preds, labels


    >>> def compute_metrics(eval_preds):
    ...     preds, labels = eval_preds
    ...     if isinstance(preds, tuple):
    ...         preds = preds[0]
    ...     decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)

    ...     labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    ...     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    ...     decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)

    ...     result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    ...     result = {"bleu": result["score"]}

    ...     prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    ...     result["gen_len"] = np.mean(prediction_lens)
    ...     result = {k: round(v, 4) for k, v in result.items()}
    ...     return result

Your `compute_metrics` function is ready to go now, and you’ll return to it when you setup your training.

## [](#train) Train

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the basic tutorial [here](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load T5 with [AutoModelForSeq2SeqLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSeq2SeqLM):

Copied


    >>> from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer

    >>> model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

At this point, only three steps remain:

  1. Define your training hyperparameters in [Seq2SeqTrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Seq2SeqTrainingArguments). The only required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model). At the end of each epoch, the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) will evaluate the SacreBLEU metric and save the training checkpoint.
  2. Pass the training arguments to [Seq2SeqTrainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Seq2SeqTrainer) along with the model, dataset, tokenizer, data collator, and `compute_metrics` function.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = Seq2SeqTrainingArguments(
    ...     output_dir="my_awesome_opus_books_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     weight_decay=0.01,
    ...     save_total_limit=3,
    ...     num_train_epochs=2,
    ...     predict_with_generate=True,
    ...     fp16=True, #change to bf16=True for XPU
    ...     push_to_hub=True,
    ... )

    >>> trainer = Seq2SeqTrainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_books["train"],
    ...     eval_dataset=tokenized_books["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

Once training is completed, share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for translation, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/translation.ipynb).

## [](#inference) Inference

Great, now that you’ve finetuned a model, you can use it for inference!

Come up with some text you’d like to translate to another language. For T5, you need to prefix your input depending on the task you’re working on. For translation from English to French, you should prefix your input as shown below:

Copied


    >>> text = "translate English to French: Legumes share resources with nitrogen-fixing bacteria."

Tokenize the text and return the `input_ids` as PyTorch tensors:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_opus_books_model")
    >>> inputs = tokenizer(text, return_tensors="pt").input_ids

Use the [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) method to create the translation. For more details about the different text generation strategies and parameters for controlling generation, check out the [Text Generation](../main_classes/text_generation) API.

Copied


    >>> from transformers import AutoModelForSeq2SeqLM

    >>> model = AutoModelForSeq2SeqLM.from_pretrained("username/my_awesome_opus_books_model")
    >>> outputs = model.generate(inputs, max_new_tokens=40, do_sample=True, top_k=30, top_p=0.95)

Decode the generated token ids back into text:

Copied


    >>> tokenizer.decode(outputs[0], skip_special_tokens=True)
    'Les lignées partagent des ressources avec des bactéries enfixant l'azote.'

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/translation.md)

[←Masked language modeling](/docs/transformers/tasks/masked_language_modeling) [Summarization→](/docs/transformers/tasks/summarization)

[Translation](#translation)[Load OPUS Books dataset](#load-opus-books-dataset)[Preprocess](#preprocess)[Evaluate](#evaluate)[Train](#train)[Inference](#inference)
