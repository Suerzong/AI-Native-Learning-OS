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

[Introduction](/learn/llm-course/chapter5/1)[What if my dataset isn't on the Hub?](/learn/llm-course/chapter5/2)[Time to slice and dice](/learn/llm-course/chapter5/3)[Big data? 🤗 Datasets to the rescue!](/learn/llm-course/chapter5/4)[Creating your own dataset](/learn/llm-course/chapter5/5)[Semantic search with FAISS](/learn/llm-course/chapter5/6)[🤗 Datasets, check!](/learn/llm-course/chapter5/7)[End-of-chapter quiz](/learn/llm-course/chapter5/8)

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

[](https://discuss.huggingface.co/t/chapter-5-questions)

In [Chapter 3](/course/chapter3) you got your first taste of the 🤗 Datasets library and saw that there were three main steps when it came to fine-tuning a model:

  1. Load a dataset from the Hugging Face Hub.
  2. Preprocess the data with `Dataset.map()`.
  3. Load and compute metrics.

But this is just scratching the surface of what 🤗 Datasets can do! In this chapter, we will take a deep dive into the library. Along the way, we’ll find answers to the following questions:

  * What do you do when your dataset is not on the Hub?
  * How can you slice and dice a dataset? (And what if you _really_ need to use Pandas?)
  * What do you do when your dataset is huge and will melt your laptop’s RAM?
  * What the heck are “memory mapping” and Apache Arrow?
  * How can you create your own dataset and push it to the Hub?

The techniques you learn here will prepare you for the advanced tokenization and fine-tuning tasks in [Chapter 6](/course/chapter6) and [Chapter 7](/course/chapter7) — so grab a coffee and let’s get started!

[ Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter5/1.mdx)

[←End-of-chapter quiz](/learn/llm-course/chapter4/6) [What if my dataset isn't on the Hub?→](/learn/llm-course/chapter5/2)

[Introduction](#introduction)
