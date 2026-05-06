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

3\. Fine-tuning a pretrained model

4\. Sharing models and tokenizers

5\. The 🤗 Datasets library

6\. The 🤗 Tokenizers library

[Introduction](/learn/llm-course/chapter6/1)[Training a new tokenizer from an old one](/learn/llm-course/chapter6/2)[Fast tokenizers' special powers](/learn/llm-course/chapter6/3)[Fast tokenizers in the QA pipeline](/learn/llm-course/chapter6/3b)[Normalization and pre-tokenization](/learn/llm-course/chapter6/4)[Byte-Pair Encoding tokenization](/learn/llm-course/chapter6/5)[WordPiece tokenization](/learn/llm-course/chapter6/6)[Unigram tokenization](/learn/llm-course/chapter6/7)[Building a tokenizer, block by block](/learn/llm-course/chapter6/8)[Tokenizers, check!](/learn/llm-course/chapter6/9)[End-of-chapter quiz](/learn/llm-course/chapter6/10)

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

[](https://discuss.huggingface.co/t/chapter-6-questions)

In [Chapter 3](/course/chapter3), we looked at how to fine-tune a model on a given task. When we do that, we use the same tokenizer that the model was pretrained with — but what do we do when we want to train a model from scratch? In these cases, using a tokenizer that was pretrained on a corpus from another domain or language is typically suboptimal. For example, a tokenizer that’s trained on an English corpus will perform poorly on a corpus of Japanese texts because the use of spaces and punctuation is very different in the two languages.

In this chapter, you will learn how to train a brand new tokenizer on a corpus of texts, so it can then be used to pretrain a language model. This will all be done with the help of the [🤗 Tokenizers](https://github.com/huggingface/tokenizers) library, which provides the “fast” tokenizers in the [🤗 Transformers](https://github.com/huggingface/transformers) library. We’ll take a close look at the features that this library provides, and explore how the fast tokenizers differ from the “slow” versions.

Topics we will cover include:

  * How to train a new tokenizer similar to the one used by a given checkpoint on a new corpus of texts
  * The special features of fast tokenizers
  * The differences between the three main subword tokenization algorithms used in NLP today
  * How to build a tokenizer from scratch with the 🤗 Tokenizers library and train it on some data

The techniques introduced in this chapter will prepare you for the section in [Chapter 7](/course/chapter7/6) where we look at creating a language model for Python source code. Let’s start by looking at what it means to “train” a tokenizer in the first place.

[ Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter6/1.mdx)

[←End-of-chapter quiz](/learn/llm-course/chapter5/8) [Training a new tokenizer from an old one→](/learn/llm-course/chapter6/2)

[Introduction](#introduction)
