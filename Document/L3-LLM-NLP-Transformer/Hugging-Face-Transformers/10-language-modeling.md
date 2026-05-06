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

Causal language modeling

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

# [](#causal-language-modeling) Causal language modeling

There are two types of language modeling, causal and masked. This guide illustrates causal language modeling. Causal language models are frequently used for text generation. You can use these models for creative applications like choosing your own text adventure or an intelligent coding assistant like Copilot or CodeParrot.

Causal language modeling predicts the next token in a sequence of tokens, and the model can only attend to tokens on the left. This means the model cannot see future tokens. GPT-2 is an example of a causal language model.

This guide will show you how to:

  1. Finetune [DistilGPT2](https://huggingface.co/distilbert/distilgpt2) on the [r/askscience](https://www.reddit.com/r/askscience/) subset of the [ELI5](https://huggingface.co/datasets/dany0407/eli5_category) dataset.
  2. Use your finetuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/text-generation)

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate

We encourage you to log in to your Hugging Face account so you can upload and share your model with the community. When prompted, enter your token to log in:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-eli5-dataset) Load ELI5 dataset

Start by loading the first 5000 examples from the [ELI5-Category](https://huggingface.co/datasets/dany0407/eli5_category) dataset with the 🤗 Datasets library. This’ll give you a chance to experiment and make sure everything works before spending more time training on the full dataset.

Copied


    >>> from datasets import load_dataset

    >>> eli5 = load_dataset("dany0407/eli5_category", split="train[:5000]")

Split the dataset’s `train` split into a train and test set with the `train_test_split` method:

Copied


    >>> eli5 = eli5.train_test_split(test_size=0.2)

Then take a look at an example:

Copied


    >>> eli5["train"][0]
    {'q_id': '7h191n',
     'title': 'What does the tax bill that was passed today mean? How will it affect Americans in each tax bracket?',
     'selftext': '',
     'category': 'Economics',
     'subreddit': 'explainlikeimfive',
     'answers': {'a_id': ['dqnds8l', 'dqnd1jl', 'dqng3i1', 'dqnku5x'],
      'text': ["The tax bill is 500 pages long and there were a lot of changes still going on right to the end. It's not just an adjustment to the income tax brackets, it's a whole bunch of changes. As such there is no good answer to your question. The big take aways are: - Big reduction in corporate income tax rate will make large companies very happy. - Pass through rate change will make certain styles of business (law firms, hedge funds) extremely happy - Income tax changes are moderate, and are set to expire (though it's the kind of thing that might just always get re-applied without being made permanent) - People in high tax states (California, New York) lose out, and many of them will end up with their taxes raised.",
       'None yet. It has to be reconciled with a vastly different house bill and then passed again.',
       'Also: does this apply to 2017 taxes? Or does it start with 2018 taxes?',
       'This article explains both the House and senate bills, including the proposed changes to your income taxes based on your income level. URL_0'],
      'score': [21, 19, 5, 3],
      'text_urls': [[],
       [],
       [],
       ['https://www.investopedia.com/news/trumps-tax-reform-what-can-be-done/']]},
     'title_urls': ['url'],
     'selftext_urls': ['url']}

While this may look like a lot, you’re only really interested in the `text` field. What’s cool about language modeling tasks is you don’t need labels (also known as an unsupervised task) because the next word _is_ the label.

## [](#preprocess) Preprocess

The next step is to load a DistilGPT2 tokenizer to process the `text` subfield:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")

You’ll notice from the example above, the `text` field is actually nested inside `answers`. This means you’ll need to extract the `text` subfield from its nested structure with the [`flatten`](https://huggingface.co/docs/datasets/process#flatten) method:

Copied


    >>> eli5 = eli5.flatten()
    >>> eli5["train"][0]
    {'q_id': '7h191n',
     'title': 'What does the tax bill that was passed today mean? How will it affect Americans in each tax bracket?',
     'selftext': '',
     'category': 'Economics',
     'subreddit': 'explainlikeimfive',
     'answers.a_id': ['dqnds8l', 'dqnd1jl', 'dqng3i1', 'dqnku5x'],
     'answers.text': ["The tax bill is 500 pages long and there were a lot of changes still going on right to the end. It's not just an adjustment to the income tax brackets, it's a whole bunch of changes. As such there is no good answer to your question. The big take aways are: - Big reduction in corporate income tax rate will make large companies very happy. - Pass through rate change will make certain styles of business (law firms, hedge funds) extremely happy - Income tax changes are moderate, and are set to expire (though it's the kind of thing that might just always get re-applied without being made permanent) - People in high tax states (California, New York) lose out, and many of them will end up with their taxes raised.",
      'None yet. It has to be reconciled with a vastly different house bill and then passed again.',
      'Also: does this apply to 2017 taxes? Or does it start with 2018 taxes?',
      'This article explains both the House and senate bills, including the proposed changes to your income taxes based on your income level. URL_0'],
     'answers.score': [21, 19, 5, 3],
     'answers.text_urls': [[],
      [],
      [],
      ['https://www.investopedia.com/news/trumps-tax-reform-what-can-be-done/']],
     'title_urls': ['url'],
     'selftext_urls': ['url']}

Each subfield is now a separate column as indicated by the `answers` prefix, and the `text` field is a list now. Instead of tokenizing each sentence separately, convert the list to a string so you can jointly tokenize them.

Here is a first preprocessing function to join the list of strings for each example and tokenize the result:

Copied


    >>> def preprocess_function(examples):
    ...     return tokenizer([" ".join(x) for x in examples["answers.text"]])

To apply this preprocessing function over the entire dataset, use the 🤗 Datasets `map` method. You can speed up the `map` function by setting `batched=True` to process multiple elements of the dataset at once, and increasing the number of processes with `num_proc`. Remove any columns you don’t need:

Copied


    >>> tokenized_eli5 = eli5.map(
    ...     preprocess_function,
    ...     batched=True,
    ...     num_proc=4,
    ...     remove_columns=eli5["train"].column_names,
    ... )

This dataset contains the token sequences, but some of these are longer than the maximum input length for the model.

You can now use a second preprocessing function to

  * concatenate all the sequences
  * split the concatenated sequences into shorter chunks defined by `block_size`, which should be both shorter than the maximum input length and short enough for your GPU RAM.

Copied


    >>> block_size = 128


    >>> def group_texts(examples):
    ...     # Concatenate all texts.
    ...     concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    ...     total_length = len(concatenated_examples[list(examples.keys())[0]])
    ...     # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
    ...     # customize this part to your needs.
    ...     if total_length >= block_size:
    ...         total_length = (total_length // block_size) * block_size
    ...     # Split by chunks of block_size.
    ...     result = {
    ...         k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
    ...         for k, t in concatenated_examples.items()
    ...     }
    ...     result["labels"] = result["input_ids"].copy()
    ...     return result

Apply the `group_texts` function over the entire dataset:

Copied


    >>> lm_dataset = tokenized_eli5.map(group_texts, batched=True, num_proc=4)

Now create a batch of examples using [DataCollatorForLanguageModeling](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForLanguageModeling). It’s more efficient to _dynamically pad_ the sentences to the longest length in a batch during collation, instead of padding the whole dataset to the maximum length.

Use the end-of-sequence token as the padding token and set `mlm=False`. This will use the inputs as labels shifted to the right by one element:

Copied


    >>> from transformers import DataCollatorForLanguageModeling

    >>> tokenizer.pad_token = tokenizer.eos_token
    >>> data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

## [](#train) Train

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the [basic tutorial](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load DistilGPT2 with [AutoModelForCausalLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForCausalLM):

Copied


    >>> from transformers import AutoModelForCausalLM, TrainingArguments, Trainer

    >>> model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

At this point, only three steps remain:

  1. Define your training hyperparameters in [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments). The only required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model).
  2. Pass the training arguments to [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) along with the model, datasets, and data collator.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_eli5_clm-model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     weight_decay=0.01,
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=lm_dataset["train"],
    ...     eval_dataset=lm_dataset["test"],
    ...     data_collator=data_collator,
    ...     processing_class=tokenizer,
    ... )

    >>> trainer.train()

Once training is completed, use the [evaluate()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.evaluate) method to evaluate your model and get its perplexity:

Copied


    >>> import math

    >>> eval_results = trainer.evaluate()
    >>> print(f"Perplexity: {math.exp(eval_results['eval_loss']):.2f}")
    Perplexity: 49.61

Then share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for causal language modeling, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb).

## [](#inference) Inference

Great, now that you’ve finetuned a model, you can use it for inference!

Come up with a prompt you’d like to generate text from:

Copied


    >>> prompt = "Somatic hypermutation allows the immune system to"

The simplest way to try out your finetuned model for inference is to use it in a [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline). Instantiate a `pipeline` for text generation with your model, and pass your text to it:

Copied


    >>> from transformers import pipeline

    >>> generator = pipeline("text-generation", model="username/my_awesome_eli5_clm-model")
    >>> generator(prompt)
    [{'generated_text': "Somatic hypermutation allows the immune system to be able to effectively reverse the damage caused by an infection.\n\n\nThe damage caused by an infection is caused by the immune system's ability to perform its own self-correcting tasks."}]

Tokenize the text and return the `input_ids` as PyTorch tensors:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_eli5_clm-model")
    >>> inputs = tokenizer(prompt, return_tensors="pt").input_ids

Use the [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) method to generate text. For more details about the different text generation strategies and parameters for controlling generation, check out the [Text generation strategies](../generation_strategies) page.

Copied


    >>> from transformers import AutoModelForCausalLM

    >>> model = AutoModelForCausalLM.from_pretrained("username/my_awesome_eli5_clm-model")
    >>> outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)

Decode the generated token ids back into text:

Copied


    >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)
    ["Somatic hypermutation allows the immune system to react to drugs with the ability to adapt to a different environmental situation. In other words, a system of 'hypermutation' can help the immune system to adapt to a different environmental situation or in some cases even a single life. In contrast, researchers at the University of Massachusetts-Boston have found that 'hypermutation' is much stronger in mice than in humans but can be found in humans, and that it's not completely unknown to the immune system. A study on how the immune system"]

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/language_modeling.md)

[←Question answering](/docs/transformers/tasks/question_answering) [Masked language modeling→](/docs/transformers/tasks/masked_language_modeling)

[Causal language modeling](#causal-language-modeling)[Load ELI5 dataset](#load-eli5-dataset)[Preprocess](#preprocess)[Train](#train)[Inference](#inference)
