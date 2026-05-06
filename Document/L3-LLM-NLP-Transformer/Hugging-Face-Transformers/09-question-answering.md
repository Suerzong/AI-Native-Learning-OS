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

Question answering

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

# [](#question-answering) Question answering

Question answering tasks return an answer given a question. If you’ve ever asked a virtual assistant like Alexa, Siri or Google what the weather is, then you’ve used a question answering model before. There are two common types of question answering tasks:

  * Extractive: extract the answer from the given context.
  * Abstractive: generate an answer from the context that correctly answers the question.

This guide will show you how to:

  1. Finetune [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) on the [SQuAD](https://huggingface.co/datasets/squad) dataset for extractive question answering.
  2. Use your finetuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/question-answering)

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate

We encourage you to login to your Hugging Face account so you can upload and share your model with the community. When prompted, enter your token to login:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-squad-dataset) Load SQuAD dataset

Start by loading a smaller subset of the SQuAD dataset from the 🤗 Datasets library. This’ll give you a chance to experiment and make sure everything works before spending more time training on the full dataset.

Copied


    >>> from datasets import load_dataset

    >>> squad = load_dataset("squad", split="train[:5000]")

Split the dataset’s `train` split into a train and test set with the `train_test_split` method:

Copied


    >>> squad = squad.train_test_split(test_size=0.2)

Then take a look at an example:

Copied


    >>> squad["train"][0]
    {'answers': {'answer_start': [515], 'text': ['Saint Bernadette Soubirous']},
     'context': 'Architecturally, the school has a Catholic character. Atop the Main Building\'s gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend "Venite Ad Me Omnes". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.',
     'id': '5733be284776f41900661182',
     'question': 'To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?',
     'title': 'University_of_Notre_Dame'
    }

There are several important fields here:

  * `answers`: the starting location of the answer token and the answer text.
  * `context`: background information from which the model needs to extract the answer.
  * `question`: the question a model should answer.

## [](#preprocess) Preprocess

The next step is to load a DistilBERT tokenizer to process the `question` and `context` fields:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

There are a few preprocessing steps particular to question answering tasks you should be aware of:

  1. Some examples in a dataset may have a very long `context` that exceeds the maximum input length of the model. To deal with longer sequences, truncate only the `context` by setting `truncation="only_second"`.
  2. Next, map the start and end positions of the answer to the original `context` by setting `return_offset_mapping=True`.
  3. With the mapping in hand, now you can find the start and end tokens of the answer. Use the `sequence_ids` method to find which part of the offset corresponds to the `question` and which corresponds to the `context`.

Here is how you can create a function to truncate and map the start and end tokens of the `answer` to the `context`:

Copied


    >>> def preprocess_function(examples):
    ...     questions = [q.strip() for q in examples["question"]]
    ...     inputs = tokenizer(
    ...         questions,
    ...         examples["context"],
    ...         max_length=384,
    ...         truncation="only_second",
    ...         return_offsets_mapping=True,
    ...         padding="max_length",
    ...     )

    ...     offset_mapping = inputs.pop("offset_mapping")
    ...     answers = examples["answers"]
    ...     start_positions = []
    ...     end_positions = []

    ...     for i, offset in enumerate(offset_mapping):
    ...         answer = answers[i]
    ...         start_char = answer["answer_start"][0]
    ...         end_char = answer["answer_start"][0] + len(answer["text"][0])
    ...         sequence_ids = inputs.sequence_ids(i)

    ...         # Find the start and end of the context
    ...         idx = 0
    ...         while sequence_ids[idx] != 1:
    ...             idx += 1
    ...         context_start = idx
    ...         while sequence_ids[idx] == 1:
    ...             idx += 1
    ...         context_end = idx - 1

    ...         # If the answer is not fully inside the context, label it (0, 0)
    ...         if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
    ...             start_positions.append(0)
    ...             end_positions.append(0)
    ...         else:
    ...             # Otherwise it's the start and end token positions
    ...             idx = context_start
    ...             while idx <= context_end and offset[idx][0] <= start_char:
    ...                 idx += 1
    ...             start_positions.append(idx - 1)

    ...             idx = context_end
    ...             while idx >= context_start and offset[idx][1] >= end_char:
    ...                 idx -= 1
    ...             end_positions.append(idx + 1)

    ...     inputs["start_positions"] = start_positions
    ...     inputs["end_positions"] = end_positions
    ...     return inputs

To apply the preprocessing function over the entire dataset, use 🤗 Datasets `map` function. You can speed up the `map` function by setting `batched=True` to process multiple elements of the dataset at once. Remove any columns you don’t need:

Copied


    >>> tokenized_squad = squad.map(preprocess_function, batched=True, remove_columns=squad["train"].column_names)

Now create a batch of examples using [DefaultDataCollator](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DefaultDataCollator). Unlike other data collators in 🤗 Transformers, the [DefaultDataCollator](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DefaultDataCollator) does not apply any additional preprocessing such as padding.

Copied


    >>> from transformers import DefaultDataCollator

    >>> data_collator = DefaultDataCollator()

## [](#train) Train

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the basic tutorial [here](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load DistilBERT with [AutoModelForQuestionAnswering](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForQuestionAnswering):

Copied


    >>> from transformers import AutoModelForQuestionAnswering, TrainingArguments, Trainer

    >>> model = AutoModelForQuestionAnswering.from_pretrained("distilbert/distilbert-base-uncased")

At this point, only three steps remain:

  1. Define your training hyperparameters in [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments). The only required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model).
  2. Pass the training arguments to [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) along with the model, dataset, tokenizer, and data collator.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_qa_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=3,
    ...     weight_decay=0.01,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_squad["train"],
    ...     eval_dataset=tokenized_squad["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ... )

    >>> trainer.train()

Once training is completed, share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for question answering, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering.ipynb).

## [](#evaluate) Evaluate

Evaluation for question answering requires a significant amount of postprocessing. To avoid taking up too much of your time, this guide skips the evaluation step. The [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) still calculates the evaluation loss during training so you’re not completely in the dark about your model’s performance.

If you have more time and you’re interested in how to evaluate your model for question answering, take a look at the [Question answering](https://huggingface.co/course/chapter7/7?fw=pt#post-processing) chapter from the 🤗 Hugging Face Course!

## [](#inference) Inference

Great, now that you’ve finetuned a model, you can use it for inference!

Come up with a question and some context you’d like the model to predict:

Copied


    >>> question = "How many programming languages does BLOOM support?"
    >>> context = "BLOOM has 176 billion parameters and can generate text in 46 languages natural languages and 13 programming languages."

Tokenize the text and return PyTorch tensors:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("my_awesome_qa_model")
    >>> inputs = tokenizer(question, context, return_tensors="pt")

Pass your inputs to the model and return the `logits`:

Copied


    >>> import torch
    >>> from transformers import AutoModelForQuestionAnswering

    >>> model = AutoModelForQuestionAnswering.from_pretrained("my_awesome_qa_model")
    >>> with torch.no_grad():
    ...     outputs = model(**inputs)

Get the highest probability from the model output for the start and end positions:

Copied


    >>> answer_start_index = outputs.start_logits.argmax()
    >>> answer_end_index = outputs.end_logits.argmax()

Decode the predicted tokens to get the answer:

Copied


    >>> predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    >>> tokenizer.decode(predict_answer_tokens)
    '176 billion parameters and can generate text in 46 languages natural languages and 13'

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/question_answering.md)

[←Token classification](/docs/transformers/tasks/token_classification) [Causal language modeling→](/docs/transformers/tasks/language_modeling)

[Question answering](#question-answering)[Load SQuAD dataset](#load-squad-dataset)[Preprocess](#preprocess)[Train](#train)[Evaluate](#evaluate)[Inference](#inference)
