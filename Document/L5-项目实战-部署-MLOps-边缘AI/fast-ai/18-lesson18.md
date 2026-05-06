[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [18: Accelerated SGD & ResNets](../Lessons/lesson18.html)

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
  2. [18: Accelerated SGD & ResNets](../Lessons/lesson18.html)

# 18: Accelerated SGD & ResNets

In this lesson, we dive into various stochastic gradient descent (SGD) accelerated approaches, such as momentum, RMSProp, and Adam. We start by experimenting with these techniques in Microsoft Excel, creating a simple linear regression problem and applying the different approaches to solve it. We also introduce learning rate annealing and show how to implement it in Excel. Next, we explore learning rate schedulers in PyTorch, focusing on Cosine Annealing and how to work with PyTorch optimizers. We create a learner with a single batch callback and fit the model to obtain an optimizer. We then explore the attributes of the optimizer and explain the concept of parameter groups.

We continue by implementing the OneCycleLR scheduler from PyTorch, which adjusts the learning rate and momentum during training. We also discuss how to improve the architecture of a neural network by making it deeper and wider, introducing ResNets and the concept of residual connections. Finally, we explore various ResNet architectures from the PyTorch Image Models (timm) library and experiment with data augmentation techniques, such as random erasing and test time augmentation.

## Concepts discussed

  * Stochastic gradient descent (SGD) accelerated approaches 
    * Momentum
    * RMSProp
    * Adam
  * Learning rate annealing
  * PyTorch learning rate schedulers 
    * Cosine Annealing
    * OneCycleLR
  * Working with PyTorch optimizers
  * Neural network architecture improvements 
    * Deeper and wider networks
    * ResNets
    * Residual connections
  * Data augmentation techniques 
    * Random erasing
    * Test time augmentation
  * Creating custom schedulers and experimenting with model performance

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-18-official-topic/102750)
  * The course’s [fashion mnist challenge](https://forums.fast.ai/t/a-challenge-for-you-all/102656) topic
  * Excel [optimisers spreadsheet](https://github.com/fastai/course22p2/blob/master/xl/graddesc.xlsm)
  * Papers 
    * [Cyclical Learning Rates for Training Neural Networks](https://arxiv.org/abs/1506.01186)
    * [Fixup Initialization: Residual Learning Without Normalization](https://arxiv.org/abs/1901.09321)
    * [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
  * Fashion-MNIST Benchmark [Papers with Code](https://paperswithcode.com/sota/image-classification-on-fashion-mnist)

[ __ 17: Initialization/normalization ](../Lessons/lesson17.html)

[ 19: DDPM and Dropout __](../Lessons/lesson19.html)
