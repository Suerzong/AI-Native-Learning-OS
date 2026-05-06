[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [16: The Learner framework](../Lessons/lesson16.html)

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

  * Concepts discussed
  * Video
  * Lesson resources

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [16: The Learner framework](../Lessons/lesson16.html)

# 16: The Learner framework

In Lesson 16, we dive into building a flexible training framework called the learner. We start with a basic callbacks Learner, which is an intermediate step towards the flexible learner. We introduce callbacks, which are functions or classes called at specific points during the training process, and demonstrate the creation of a simple callback. We also introduce the concept of CancelFitException, CancelEpochException, and CancelBatchException.

Next, we explore metrics and create a MetricsCB callback to print out metrics during training. We introduce the torcheval library and create a DeviceCB callback to handle moving the model and data to the appropriate device. We refactor the code using a context manager to simplify the code and make it easier to maintain and add callbacks in the future.

We then focus on looking inside the models to diagnose and fix problems during training. We introduce a set_seed function and train a model with a high learning rate of 0.6 to test the stability of the training. Finally, we discuss analyzing the training process by looking at the mean and standard deviation of each layer’s activations, using PyTorch hooks and creating histograms of the activations.

## Concepts discussed

  * Building a flexible training framework
  * Basic Callbacks Learner
  * Callbacks and exceptions (CancelFitException, CancelEpochException, CancelBatchException)
  * Metrics and MetricsCB callback
  * torcheval library
  * DeviceCB callback
  * Refactoring code with context managers
  * set_seed function
  * Analyzing the training process
  * PyTorch hooks
  * Histograms of activations

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-16-official-topic/102472)
  * [Cyclical Learning Rates for Training Neural Networks - Leslie Smith](https://arxiv.org/abs/1506.01186)
  * [A disciplined approach to neural network hyper-parameters: Part 1 – learning rate, batch size, momentum, and weight decay - Leslie Smith](https://arxiv.org/abs/1803.09820)
  * [Methods for Automating Learning Rate Finders - Zach Mueller](https://www.novetta.com/2021/03/learning-rate/)

[ __ 15: Autoencoders ](../Lessons/lesson15.html)

[ 17: Initialization/normalization __](../Lessons/lesson17.html)
