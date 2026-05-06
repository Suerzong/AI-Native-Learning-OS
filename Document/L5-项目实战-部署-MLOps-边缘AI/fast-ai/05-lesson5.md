[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 1](../Lessons/lesson1.html)
  2. [5: From-scratch model](../Lessons/lesson5.html)

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
  * Lesson notebooks
  * Links from the lesson

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 1](../Lessons/lesson1.html)
  2. [5: From-scratch model](../Lessons/lesson5.html)

# 5: From-scratch model

Today we look at how to create a neural network from scratch using Python and PyTorch, and how to implement a training loop for optimising the weights of a model. We build up from a single layer regression model up to a neural net with one hidden layer, and then to a deep learning model. Along the way we’ll also look at how we can use a special function called _sigmoid_ to make binary classification models easier to train, and we’ll also learn about _metrics_.

## Video

This lesson is based partly on [chapter 4](https://github.com/fastai/fastbook/blob/master/04_mnist_basics.ipynb) and [chapter 9](https://github.com/fastai/fastbook/blob/master/09_tabular.ipynb) of the [book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527).

## Lesson notebooks

  * [Linear model and neural net from scratch](https://www.kaggle.com/code/jhoward/linear-model-and-neural-net-from-scratch)
  * [Why you should use a framework](https://www.kaggle.com/code/jhoward/why-you-should-use-a-framework)
  * [How random forests really work](https://www.kaggle.com/code/jhoward/how-random-forests-really-work/)

## Links from the lesson

  * [OneR paper](https://link.springer.com/article/10.1023/A:1022631118932)
  * Some great Titanic notebooks: [1](https://www.kaggle.com/code/mrisdal/exploring-survival-on-the-titanic); [2](https://www.kaggle.com/code/cdeotte/titanic-wcg-xgboost-0-84688/notebook); [3](https://www.kaggle.com/code/pliptor/divide-and-conquer-0-82296); [4](https://www.kaggle.com/code/cdeotte/titanic-using-name-only-0-81818/notebook)

[ __ 4: Natural Language (NLP) ](../Lessons/lesson4.html)

[ 6: Random forests __](../Lessons/lesson6.html)
