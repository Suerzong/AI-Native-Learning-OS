[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [14: Backpropagation](../Lessons/lesson14.html)

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

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [14: Backpropagation](../Lessons/lesson14.html)

# 14: Backpropagation

In this lesson, we dive into the implementation of the chain rule in neural network training using backpropagation. We refactor our code to make it more efficient and flexible, and explore PyTorch’s `nn.Module` and `nn.Sequential`. We also create custom PyTorch modules, build our own implementation of `nn.Module`, and learn about optimizers, DataLoaders, and Datasets. We show how to work with Hugging Face datasets, and introduce the nbdev library.

We look at how to map the code from the previous lesson to the math behind backpropagation. Next, we refactor our code using PyTorch’s `nn.Module`, which automatically tracks layers and parameters. We also create a sequential model using `nn.Sequential` and demonstrate how to create custom PyTorch modules. We then introduce the concept of an optimizer, which simplifies the process of updating parameters based on gradients and learning rates. We create a custom SGD optimizer from scratch and explore PyTorch’s built-in DataLoader. We also create a proper training loop using PyTorch DataLoader.

Throughout the lesson, we emphasize the importance of understanding the underlying code and not relying solely on other people’s code. This allows for greater flexibility and creativity in building custom solutions. We also discuss the use of `**kwargs` and delegates in fastcore, callbacks, and dunder methods in Python’s data model.

## Concepts discussed

  * Backpropagation and the chain rule
  * Refactoring code for efficiency and flexibility
  * PyTorch’s `nn.Module` and `nn.Sequential`
  * Creating custom PyTorch modules
  * Implementing optimizers, DataLoaders, and Datasets
  * Working with Hugging Face datasets
  * Using nbdev to create Python modules from Jupyter notebooks
  * `**kwargs` and delegates
  * Callbacks and dunder methods in Python’s data model
  * Building a proper training loop using PyTorch DataLoader

## Video

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-14-official-topic/102018)

[ __ 13: Backpropagation & MLP ](../Lessons/lesson13.html)

[ 15: Autoencoders __](../Lessons/lesson15.html)
