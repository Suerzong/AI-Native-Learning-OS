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

Summarization

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

# [](#summarization) Summarization

Summarization creates a shorter version of a document or an article that captures all the important information. Along with translation, it is another example of a task that can be formulated as a sequence-to-sequence task. Summarization can be:

  * Extractive: extract the most relevant information from a document.
  * Abstractive: generate new text that captures the most relevant information.

This guide will show you how to:

  1. Finetune [T5](https://huggingface.co/google-t5/t5-small) on the California state bill subset of the [BillSum](https://huggingface.co/datasets/FiscalNote/billsum) dataset for abstractive summarization.
  2. Use your finetuned model for inference.

> To see all architectures and checkpoints compatible with this task, we recommend checking the [task-page](https://huggingface.co/tasks/summarization)

Before you begin, make sure you have all the necessary libraries installed:

Copied


    pip install transformers datasets evaluate rouge_score

We encourage you to login to your Hugging Face account so you can upload and share your model with the community. When prompted, enter your token to login:

Copied


    >>> from huggingface_hub import notebook_login

    >>> notebook_login()

## [](#load-billsum-dataset) Load BillSum dataset

Start by loading the smaller California state bill subset of the BillSum dataset from the 🤗 Datasets library:

Copied


    >>> from datasets import load_dataset

    >>> billsum = load_dataset("billsum", split="ca_test")

Split the dataset into a train and test set with the `train_test_split` method:

Copied


    >>> billsum = billsum.train_test_split(test_size=0.2)

Then take a look at an example:

Copied


    >>> billsum["train"][0]
    {'summary': 'Existing law authorizes state agencies to enter into contracts for the acquisition of goods or services upon approval by the Department of General Services. Existing law sets forth various requirements and prohibitions for those contracts, including, but not limited to, a prohibition on entering into contracts for the acquisition of goods or services of $100,000 or more with a contractor that discriminates between spouses and domestic partners or same-sex and different-sex couples in the provision of benefits. Existing law provides that a contract entered into in violation of those requirements and prohibitions is void and authorizes the state or any person acting on behalf of the state to bring a civil action seeking a determination that a contract is in violation and therefore void. Under existing law, a willful violation of those requirements and prohibitions is a misdemeanor.\nThis bill would also prohibit a state agency from entering into contracts for the acquisition of goods or services of $100,000 or more with a contractor that discriminates between employees on the basis of gender identity in the provision of benefits, as specified. By expanding the scope of a crime, this bill would impose a state-mandated local program.\nThe California Constitution requires the state to reimburse local agencies and school districts for certain costs mandated by the state. Statutory provisions establish procedures for making that reimbursement.\nThis bill would provide that no reimbursement is required by this act for a specified reason.',
     'text': 'The people of the State of California do enact as follows:\n\n\nSECTION 1.\nSection 10295.35 is added to the Public Contract Code, to read:\n10295.35.\n(a) (1) Notwithstanding any other law, a state agency shall not enter into any contract for the acquisition of goods or services in the amount of one hundred thousand dollars ($100,000) or more with a contractor that, in the provision of benefits, discriminates between employees on the basis of an employee’s or dependent’s actual or perceived gender identity, including, but not limited to, the employee’s or dependent’s identification as transgender.\n(2) For purposes of this section, “contract” includes contracts with a cumulative amount of one hundred thousand dollars ($100,000) or more per contractor in each fiscal year.\n(3) For purposes of this section, an employee health plan is discriminatory if the plan is not consistent with Section 1365.5 of the Health and Safety Code and Section 10140 of the Insurance Code.\n(4) The requirements of this section shall apply only to those portions of a contractor’s operations that occur under any of the following conditions:\n(A) Within the state.\n(B) On real property outside the state if the property is owned by the state or if the state has a right to occupy the property, and if the contractor’s presence at that location is connected to a contract with the state.\n(C) Elsewhere in the United States where work related to a state contract is being performed.\n(b) Contractors shall treat as confidential, to the maximum extent allowed by law or by the requirement of the contractor’s insurance provider, any request by an employee or applicant for employment benefits or any documentation of eligibility for benefits submitted by an employee or applicant for employment.\n(c) After taking all reasonable measures to find a contractor that complies with this section, as determined by the state agency, the requirements of this section may be waived under any of the following circumstances:\n(1) There is only one prospective contractor willing to enter into a specific contract with the state agency.\n(2) The contract is necessary to respond to an emergency, as determined by the state agency, that endangers the public health, welfare, or safety, or the contract is necessary for the provision of essential services, and no entity that complies with the requirements of this section capable of responding to the emergency is immediately available.\n(3) The requirements of this section violate, or are inconsistent with, the terms or conditions of a grant, subvention, or agreement, if the agency has made a good faith attempt to change the terms or conditions of any grant, subvention, or agreement to authorize application of this section.\n(4) The contractor is providing wholesale or bulk water, power, or natural gas, the conveyance or transmission of the same, or ancillary services, as required for ensuring reliable services in accordance with good utility practice, if the purchase of the same cannot practically be accomplished through the standard competitive bidding procedures and the contractor is not providing direct retail services to end users.\n(d) (1) A contractor shall not be deemed to discriminate in the provision of benefits if the contractor, in providing the benefits, pays the actual costs incurred in obtaining the benefit.\n(2) If a contractor is unable to provide a certain benefit, despite taking reasonable measures to do so, the contractor shall not be deemed to discriminate in the provision of benefits.\n(e) (1) Every contract subject to this chapter shall contain a statement by which the contractor certifies that the contractor is in compliance with this section.\n(2) The department or other contracting agency shall enforce this section pursuant to its existing enforcement powers.\n(3) (A) If a contractor falsely certifies that it is in compliance with this section, the contract with that contractor shall be subject to Article 9 (commencing with Section 10420), unless, within a time period specified by the department or other contracting agency, the contractor provides to the department or agency proof that it has complied, or is in the process of complying, with this section.\n(B) The application of the remedies or penalties contained in Article 9 (commencing with Section 10420) to a contract subject to this chapter shall not preclude the application of any existing remedies otherwise available to the department or other contracting agency under its existing enforcement powers.\n(f) Nothing in this section is intended to regulate the contracting practices of any local jurisdiction.\n(g) This section shall be construed so as not to conflict with applicable federal laws, rules, or regulations. In the event that a court or agency of competent jurisdiction holds that federal law, rule, or regulation invalidates any clause, sentence, paragraph, or section of this code or the application thereof to any person or circumstances, it is the intent of the state that the court or agency sever that clause, sentence, paragraph, or section so that the remainder of this section shall remain in effect.\nSEC. 2.\nSection 10295.35 of the Public Contract Code shall not be construed to create any new enforcement authority or responsibility in the Department of General Services or any other contracting agency.\nSEC. 3.\nNo reimbursement is required by this act pursuant to Section 6 of Article XIII\u2009B of the California Constitution because the only costs that may be incurred by a local agency or school district will be incurred because this act creates a new crime or infraction, eliminates a crime or infraction, or changes the penalty for a crime or infraction, within the meaning of Section 17556 of the Government Code, or changes the definition of a crime within the meaning of Section 6 of Article XIII\u2009B of the California Constitution.',
     'title': 'An act to add Section 10295.35 to the Public Contract Code, relating to public contracts.'}

There are two fields that you’ll want to use:

  * `text`: the text of the bill which’ll be the input to the model.
  * `summary`: a condensed version of `text` which’ll be the model target.

## [](#preprocess) Preprocess

The next step is to load a T5 tokenizer to process `text` and `summary`:

Copied


    >>> from transformers import AutoTokenizer

    >>> checkpoint = "google-t5/t5-small"
    >>> tokenizer = AutoTokenizer.from_pretrained(checkpoint)

The preprocessing function you want to create needs to:

  1. Prefix the input with a prompt so T5 knows this is a summarization task. Some models capable of multiple NLP tasks require prompting for specific tasks.
  2. Use the keyword `text_target` argument when tokenizing labels.
  3. Truncate sequences to be no longer than the maximum length set by the `max_length` parameter.

Copied


    >>> prefix = "summarize: "


    >>> def preprocess_function(examples):
    ...     inputs = [prefix + doc for doc in examples["text"]]
    ...     model_inputs = tokenizer(inputs, max_length=1024, truncation=True)

    ...     labels = tokenizer(text_target=examples["summary"], max_length=128, truncation=True)

    ...     model_inputs["labels"] = labels["input_ids"]
    ...     return model_inputs

To apply the preprocessing function over the entire dataset, use 🤗 Datasets `map` method. You can speed up the `map` function by setting `batched=True` to process multiple elements of the dataset at once:

Copied


    >>> tokenized_billsum = billsum.map(preprocess_function, batched=True)

Now create a batch of examples using [DataCollatorForSeq2Seq](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DataCollatorForSeq2Seq). It’s more efficient to _dynamically pad_ the sentences to the longest length in a batch during collation, instead of padding the whole dataset to the maximum length.

Copied


    >>> from transformers import DataCollatorForSeq2Seq

    >>> data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)

## [](#evaluate) Evaluate

Including a metric during training is often helpful for evaluating your model’s performance. You can quickly load a evaluation method with the 🤗 [Evaluate](https://huggingface.co/docs/evaluate/index) library. For this task, load the [ROUGE](https://huggingface.co/spaces/evaluate-metric/rouge) metric (see the 🤗 Evaluate [quick tour](https://huggingface.co/docs/evaluate/a_quick_tour) to learn more about how to load and compute a metric):

Copied


    >>> import evaluate

    >>> rouge = evaluate.load("rouge")

Then create a function that passes your predictions and labels to [compute](https://huggingface.co/docs/evaluate/v0.4.6/en/package_reference/main_classes#evaluate.EvaluationModule.compute) to calculate the ROUGE metric:

Copied


    >>> import numpy as np


    >>> def compute_metrics(eval_pred):
    ...     predictions, labels = eval_pred
    ...     decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    ...     labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    ...     decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    ...     result = rouge.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)

    ...     prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
    ...     result["gen_len"] = np.mean(prediction_lens)

    ...     return {k: round(v, 4) for k, v in result.items()}

Your `compute_metrics` function is ready to go now, and you’ll return to it when you setup your training.

## [](#train) Train

> If you aren’t familiar with finetuning a model with the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer), take a look at the basic tutorial [here](../training#train-with-pytorch-trainer)!

You’re ready to start training your model now! Load T5 with [AutoModelForSeq2SeqLM](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForSeq2SeqLM):

Copied


    >>> from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer

    >>> model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

At this point, only three steps remain:

  1. Define your training hyperparameters in [Seq2SeqTrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Seq2SeqTrainingArguments). The only required parameter is `output_dir` which specifies where to save your model. You’ll push this model to the Hub by setting `push_to_hub=True` (you need to be signed in to Hugging Face to upload your model). At the end of each epoch, the [Trainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer) will evaluate the ROUGE metric and save the training checkpoint.
  2. Pass the training arguments to [Seq2SeqTrainer](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Seq2SeqTrainer) along with the model, dataset, tokenizer, data collator, and `compute_metrics` function.
  3. Call [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train) to finetune your model.

Copied


    >>> training_args = Seq2SeqTrainingArguments(
    ...     output_dir="my_awesome_billsum_model",
    ...     eval_strategy="epoch",
    ...     learning_rate=2e-5,
    ...     per_device_train_batch_size=16,
    ...     per_device_eval_batch_size=16,
    ...     weight_decay=0.01,
    ...     save_total_limit=3,
    ...     num_train_epochs=4,
    ...     predict_with_generate=True,
    ...     fp16=True, #change to bf16=True for XPU
    ...     push_to_hub=True,
    ... )

    >>> trainer = Seq2SeqTrainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=tokenized_billsum["train"],
    ...     eval_dataset=tokenized_billsum["test"],
    ...     processing_class=tokenizer,
    ...     data_collator=data_collator,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

Once training is completed, share your model to the Hub with the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.push_to_hub) method so everyone can use your model:

Copied


    >>> trainer.push_to_hub()

> For a more in-depth example of how to finetune a model for summarization, take a look at the corresponding [PyTorch notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/summarization.ipynb).

## [](#inference) Inference

Great, now that you’ve finetuned a model, you can use it for inference!

Come up with some text you’d like to summarize. For T5, you need to prefix your input depending on the task you’re working on. For summarization you should prefix your input as shown below:

Copied


    >>> text = "summarize: The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history, which will lift up American workers and create good-paying, union jobs across the country. It'll lower the deficit and ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per year will pay a penny more in taxes."

Tokenize the text and return the `input_ids` as PyTorch tensors:

Copied


    >>> from transformers import AutoTokenizer

    >>> tokenizer = AutoTokenizer.from_pretrained("username/my_awesome_billsum_model")
    >>> inputs = tokenizer(text, return_tensors="pt").input_ids

Use the [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) method to create the summarization. For more details about the different text generation strategies and parameters for controlling generation, check out the [Text Generation](../main_classes/text_generation) API.

Copied


    >>> from transformers import AutoModelForSeq2SeqLM

    >>> model = AutoModelForSeq2SeqLM.from_pretrained("username/my_awesome_billsum_model")
    >>> outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)

Decode the generated token ids back into text:

Copied


    >>> tokenizer.decode(outputs[0], skip_special_tokens=True)
    'the inflation reduction act lowers prescription drug costs, health care costs, and energy costs. it's the most aggressive action on tackling the climate crisis in american history. it will ask the ultra-wealthy and corporations to pay their fair share.'

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/summarization.md)

[←Translation](/docs/transformers/tasks/translation) [Multiple choice→](/docs/transformers/tasks/multiple_choice)

[Summarization](#summarization)[Load BillSum dataset](#load-billsum-dataset)[Preprocess](#preprocess)[Evaluate](#evaluate)[Train](#train)[Inference](#inference)
