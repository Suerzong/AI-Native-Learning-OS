[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 1](../Lessons/lesson1.html)
  2. [7: Collaborative filtering](../Lessons/lesson7.html)

  * [ Practical Deep Learning](../index.html)

  * Part 1 __

    * [ 1: Getting started](../Lessons/lesson1.html)

    * [ 2: Deployment](../Lessons/lesson2.html)

    * [ 3: Neural net foundations](../Lessons/lesson3.html)

    * [ 4: Natural Language (NLP)](../Lessons/lesson4.html)

    * [ 5: From-scratch model](../Lessons/lesson5.html)

    * [ 6: Random forests](../Lessons/lesson6.html)

    * [ 7: Collaborative filtering](../Lessons/lesson7.html)

    * [ 8: Convolutions (CNNs)](../Lessons/lesson8.html)

    * [ Bonus: Data ethics](../Lessons/lesson8a.html)

    * Summaries __

      * [ Lesson 1](../Lessons/Summaries/lesson1.html)

      * [ Lesson 2](../Lessons/Summaries/lesson2.html)

      * [ Lesson 3](../Lessons/Summaries/lesson3.html)

      * [ Lesson 4](../Lessons/Summaries/lesson4.html)

      * [ Lesson 5](../Lessons/Summaries/lesson5.html)

      * [ Lesson 6](../Lessons/Summaries/lesson6.html)

      * [ Lesson 7](../Lessons/Summaries/lesson7.html)

      * [ Lesson 8](../Lessons/Summaries/lesson8.html)

  * Part 2 __

    * [ Part 2 overview](../Lessons/part2.html)

    * [ 9: Stable Diffusion](../Lessons/lesson9.html)

    * [ 10: Diving Deeper](../Lessons/lesson10.html)

    * [ 11: Matrix multiplication](../Lessons/lesson11.html)

    * [ 12: Mean shift clustering](../Lessons/lesson12.html)

    * [ 13: Backpropagation & MLP](../Lessons/lesson13.html)

    * [ 14: Backpropagation](../Lessons/lesson14.html)

    * [ 15: Autoencoders](../Lessons/lesson15.html)

    * [ 16: The Learner framework](../Lessons/lesson16.html)

    * [ 17: Initialization/normalization](../Lessons/lesson17.html)

    * [ 18: Accelerated SGD & ResNets](../Lessons/lesson18.html)

    * [ 19: DDPM and Dropout](../Lessons/lesson19.html)

    * [ 20: Mixed Precision](../Lessons/lesson20.html)

    * [ 21: DDIM](../Lessons/lesson21.html)

    * [ 22: Karras et al (2022)](../Lessons/lesson22.html)

    * [ 23: Super-resolution](../Lessons/lesson23.html)

    * [ 24: Attention & transformers](../Lessons/lesson24.html)

    * [ 25: Latent diffusion](../Lessons/lesson25.html)

    * [ Bonus: Lesson 9a](https://youtu.be/0_BBRNYInx8)

    * [ Bonus: Lesson 9b](https://youtu.be/mYpjmM7O-30)

  * Resources __

    * [ The book](../Resources/book.html)

    * [ Forums](../Resources/forums.html)

    * [ Kaggle](../Resources/kaggle.html)

    * [ Testimonials](../Resources/testimonials.html)

## On this page

  * Video
  * Resources

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 1](../Lessons/lesson1.html)
  2. [7: Collaborative filtering](../Lessons/lesson7.html)

# 7: Collaborative filtering

You interact nearly every day with _recommendation systems_ —algorithms which guess what products and services you might like, based on your past behavior. These systems largely rely on _collaborative-filtering_ , an approach based on linear algebra that fills in the missing values in a matrix. Today we’ll see two ways to do this: one based on a classic linear algebra formulation, and one based on deep learning.

## Video

This lesson is based partly on [chapter 8](https://github.com/fastai/fastbook/blob/master/08_collab.ipynb) of the [book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527).

## Resources

  * Notebooks for this lesson: 
    * Road to the top: [part 3](https://www.kaggle.com/code/jhoward/scaling-up-road-to-the-top-part-3) and [part 4](https://www.kaggle.com/code/jhoward/multi-target-road-to-the-top-part-4)
    * [Collaborative Filtering Deep Dive](https://www.kaggle.com/code/jhoward/collaborative-filtering-deep-dive/notebook)
  * [Spreadsheets](https://github.com/fastai/course22/tree/master/xl) for this lesson: 
    * [Softmax and cross-entropy](https://github.com/fastai/course22/blob/master/xl/entropy_example.xlsx)
    * [Collaborative filterings and embeddings](https://github.com/fastai/course22/blob/master/xl/collab_filter.xlsx)
  * [Things that confused me about cross-entropy](https://chris-said.io/2020/12/26/two-things-that-confused-me-about-cross-entropy/) by Chris Said
  * [Label Smoothing Explained using Microsoft Excel](https://amaarora.github.io/posts/2020-07-18-label-smoothing.html) by Aman Arora

[ __ 6: Random forests ](../Lessons/lesson6.html)

[ 8: Convolutions (CNNs) __](../Lessons/lesson8.html)
