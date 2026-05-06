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

[Introduction](/learn/llm-course/chapter3/1)[Processing the data](/learn/llm-course/chapter3/2)[Fine-tuning a model with the Trainer API](/learn/llm-course/chapter3/3)[A full training loop](/learn/llm-course/chapter3/4)[Understanding Learning Curves](/learn/llm-course/chapter3/5)[Fine-tuning, Check!](/learn/llm-course/chapter3/6)[End-of-chapter quiz](/learn/llm-course/chapter3/7)

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

[ Pytorch ](?fw=pt)[ TensorFlow ](?fw=tf)

Copy page

# [](#introduction) Introduction

[](https://discuss.huggingface.co/t/chapter-3-questions)

In [Chapter 2](/course/chapter2) we explored how to use tokenizers and pretrained models to make predictions. But what if you want to fine-tune a pretrained model to solve a specific task? That’s the topic of this chapter! You will learn:

  * How to prepare a large dataset from the Hub using the latest 🤗 Datasets features
  * How to use the high-level `Trainer` API to fine-tune a model with modern best practices
  * How to implement a custom training loop with optimization techniques
  * How to leverage the 🤗 Accelerate library to easily run distributed training on any setup
  * How to apply current fine-tuning best practices for maximum performance

> 📚 **Essential Resources** : Before starting, you might want to review the [🤗 Datasets documentation](https://huggingface.co/docs/datasets/) for data processing.

This chapter will also serve as an introduction to some Hugging Face libraries beyond the 🤗 Transformers library! We’ll see how libraries like 🤗 Datasets, 🤗 Tokenizers, 🤗 Accelerate, and 🤗 Evaluate can help you train models more efficiently and effectively.

Each of the main sections in this chapter will teach you something different:

  * **Section 2** : Learn modern data preprocessing techniques and efficient dataset handling
  * **Section 3** : Master the powerful Trainer API with all its latest features
  * **Section 4** : Implement training loops from scratch and understand distributed training with Accelerate

By the end of this chapter, you’ll be able to fine-tune models on your own datasets using both high-level APIs and custom training loops, applying the latest best practices in the field.

> 🎯 **What You’ll Build** : By the end of this chapter, you’ll have fine-tuned a BERT model for text classification and understand how to adapt the techniques to your own datasets and tasks.

This chapter focuses exclusively on **PyTorch** , as it has become the standard framework for modern deep learning research and production. We’ll use the latest APIs and best practices from the Hugging Face ecosystem.

To upload your trained models to the Hugging Face Hub, you will need a Hugging Face account: [create an account](https://huggingface.co/join)

[ Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter3/1.mdx)

[←End-of-chapter quiz](/learn/llm-course/chapter2/9) [Processing the data→](/learn/llm-course/chapter3/2)

[Introduction](#introduction)
