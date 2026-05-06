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

7\. Classical NLP tasks

[Introduction](/learn/llm-course/chapter7/1)[Token classification](/learn/llm-course/chapter7/2)[Fine-tuning a masked language model](/learn/llm-course/chapter7/3)[Translation](/learn/llm-course/chapter7/4)[Summarization](/learn/llm-course/chapter7/5)[Training a causal language model from scratch](/learn/llm-course/chapter7/6)[Question answering](/learn/llm-course/chapter7/7)[Mastering LLMs](/learn/llm-course/chapter7/8)[End-of-chapter quiz](/learn/llm-course/chapter7/9)

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

[ Pytorch ](?fw=pt)[ TensorFlow ](?fw=tf)

Copy page

# [](#introduction) Introduction

[](https://discuss.huggingface.co/t/chapter-7-questions)

In [Chapter 3](/course/chapter3), you saw how to fine-tune a model for text classification. In this chapter, we will tackle the following common language tasks that are essential for working with both traditional NLP models and modern LLMs:

  * Token classification
  * Masked language modeling (like BERT)
  * Summarization
  * Translation
  * Causal language modeling pretraining (like GPT-2)
  * Question answering

These fundamental tasks form the foundation of how Large Language Models (LLMs) work and understanding them is crucial for effectively working with today’s most advanced language models.

To do this, you’ll need to leverage everything you learned about the `Trainer` API and the 🤗 Accelerate library in [Chapter 3](/course/chapter3), the 🤗 Datasets library in [Chapter 5](/course/chapter5), and the 🤗 Tokenizers library in [Chapter 6](/course/chapter6). We’ll also upload our results to the Model Hub, like we did in [Chapter 4](/course/chapter4), so this is really the chapter where everything comes together!

Each section can be read independently and will show you how to train a model with the `Trainer` API or with your own training loop, using 🤗 Accelerate. Feel free to skip either part and focus on the one that interests you the most: the `Trainer` API is great for fine-tuning or training your model without worrying about what’s going on behind the scenes, while the training loop with `Accelerate` will let you customize any part you want more easily.

> If you read the sections in sequence, you will notice that they have quite a bit of code and prose in common. The repetition is intentional, to allow you to dip in (or come back later) to any task that interests you and find a complete working example.

[ Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter7/1.mdx)

[←End-of-chapter quiz](/learn/llm-course/chapter6/10) [Token classification→](/learn/llm-course/chapter7/2)

[Introduction](#introduction)
