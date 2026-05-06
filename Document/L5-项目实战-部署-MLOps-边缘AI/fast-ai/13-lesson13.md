[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [13: Backpropagation & MLP](../Lessons/lesson13.html)

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
  2. [13: Backpropagation & MLP](../Lessons/lesson13.html)

# 13: Backpropagation & MLP

In this lesson, we dive into backpropagation and the creation of a simple Multi-Layer Perceptron (MLP) neural network. We start by reviewing basic neural networks and their architecture, then move on to implementing a simple MLP from scratch. We focus on understanding the chain rule and backpropagation in the context of neural networks, and demonstrate how to calculate derivatives using Python and the SimPy library.

We also discuss the importance of the chain rule in calculating the gradient of the mean squared error (MSE) applied to a model, and demonstrate how to use PyTorch to calculate derivatives and simplify the process by creating classes for ReLU and linear functions. We then explore the issues with floating point math and introduce the log sum exp trick to overcome these issues. Finally, we create a training loop for a simple neural network.

## Concepts discussed

  * Basic neural network architecture
  * Multi-Layer Perceptron (MLP) implementation
  * Gradients and derivatives
  * Chain rule and backpropagation
  * Python debugger (pdb)
  * PyTorch for calculating derivatives
  * ReLU and linear function classes
  * Log sum exp trick
  * `log_softmax()` function and cross entropy loss
  * Training loop for a simple neural network

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-13-official-topic/101876)
  * [The Intuitive Notion of the Chain Rule](https://webspace.ship.edu/msrenault/geogebracalculus/derivative_intuitive_chain_rule.html)
  * [The Matrix Calculus You Need For Deep Learning](https://explained.ai/matrix-calculus/)
  * [Part 1 Excel workbooks](https://github.com/fastai/course22/tree/master/xl)
  * [Calculus help topic](https://forums.fast.ai/t/calculus-help-topic/102020)
  * [Simple Neural Net Backward Pass](https://nasheqlbrm.github.io/blog/posts/2021-11-13-backward-pass.html)

[ __ 12: Mean shift clustering ](../Lessons/lesson12.html)

[ 14: Backpropagation __](../Lessons/lesson14.html)
