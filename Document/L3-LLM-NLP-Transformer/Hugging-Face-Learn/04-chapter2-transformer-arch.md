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

LLM Course documentation

Introduction

# LLM Course

🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseDeep RL CourseDiffusion CourseLLM CourseMCP CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

ARBNDEENESFAFRGJHEHIIDITJAKOMYNEPLPTRORURUMTETHTRVIZH-CNZH-TW

[ ](https://github.com/huggingface/course)

0\. Setup

1\. Transformer models

2\. Using 🤗 Transformers

[Introduction](/learn/llm-course/chapter2/1)[Behind the pipeline](/learn/llm-course/chapter2/2)[Models](/learn/llm-course/chapter2/3)[Tokenizers](/learn/llm-course/chapter2/4)[Handling multiple sequences](/learn/llm-course/chapter2/5)[Putting it all together](/learn/llm-course/chapter2/6)[Basic usage completed!](/learn/llm-course/chapter2/7)[Optimized Inference Deployment](/learn/llm-course/chapter2/8)[End-of-chapter quiz](/learn/llm-course/chapter2/9)

3\. Fine-tuning a pretrained model

4\. Sharing models and tokenizers

5\. The 🤗 Datasets library

6\. The 🤗 Tokenizers library

7\. Classical NLP tasks

8\. How to ask for help

9\. Building and sharing demos

10\. Curate high-quality datasets

11\. Fine-tune Large Language Models

12\. Build Reasoning Models new

Course Events

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#introduction) Introduction

[](https://discuss.huggingface.co/t/chapter-2-questions)

As you saw in [Chapter 1](/course/chapter1), Transformer models are usually very large. With millions to tens of _billions_ of parameters, training and deploying these models is a complicated undertaking. Furthermore, with new models being released on a near-daily basis and each having its own implementation, trying them all out is no easy task.

The 🤗 Transformers library was created to solve this problem. Its goal is to provide a single API through which any Transformer model can be loaded, trained, and saved. The library’s main features are:

  * **Ease of use** : Downloading, loading, and using a state-of-the-art NLP model for inference can be done in just two lines of code.
  * **Flexibility** : At their core, all models are simple PyTorch `nn.Module` classes and can be handled like any other models in their respective machine learning (ML) frameworks.
  * **Simplicity** : Hardly any abstractions are made across the library. The “All in one file” is a core concept: a model’s forward pass is entirely defined in a single file, so that the code itself is understandable and hackable.

This last feature makes 🤗 Transformers quite different from other ML libraries. The models are not built on modules that are shared across files; instead, each model has its own layers. In addition to making the models more approachable and understandable, this allows you to easily experiment on one model without affecting others.

This chapter will begin with an end-to-end example where we use a model and a tokenizer together to replicate the `pipeline()` function introduced in [Chapter 1](/course/chapter1). Next, we’ll discuss the model API: we’ll dive into the model and configuration classes, and show you how to load a model and how it processes numerical inputs to output predictions.

Then we’ll look at the tokenizer API, which is the other main component of the `pipeline()` function. Tokenizers take care of the first and last processing steps, handling the conversion from text to numerical inputs for the neural network, and the conversion back to text when it is needed. Finally, we’ll show you how to handle sending multiple sentences through a model in a prepared batch, then wrap it all up with a closer look at the high-level `tokenizer()` function.

> ⚠️ In order to benefit from all features available with the Model Hub and 🤗 Transformers, we recommend [creating an account](https://huggingface.co/join).

[ Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter2/1.mdx)

[←Certification exam](/learn/llm-course/chapter1/11) [Behind the pipeline→](/learn/llm-course/chapter2/2)

[Introduction](#introduction)
