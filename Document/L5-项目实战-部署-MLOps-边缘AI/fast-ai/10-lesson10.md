[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [10: Diving Deeper](../Lessons/lesson10.html)

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
  * Links from the lesson

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [10: Diving Deeper](../Lessons/lesson10.html)

# 10: Diving Deeper

This lesson creates a complete Diffusers pipeline from the underlying components: the VAE, unet, scheduler, and tokeniser. By putting them together manually, this gives you the flexibility to fully customise every aspect of the inference process.

We also discuss three important new papers that have been released in the last week, which improve inference performance by over 10x, and allow any photo to be “edited” by just describing what the new picture should show.

In the second half of the lesson Jeremy begins the “from scratch” implementation of Stable Diffusion. He introduces the “miniai” library which will be created by students during the course, and discusses organising and simplifying code. The lesson discusses the Python data model, tensors, and random number generation. Jeremy introduces the Wickman-Hill random number generation algorithm and compares the performance of custom and Pytorch’s built-in random number generators. The lesson concludes with creating a linear classifier using a tensor.

## Concepts discussed

  * Papers: 
    * Progressive Distillation for Fast Sampling of Diffusion Models
    * On Distillation of Guided Diffusion Models
    * Imagic
  * Tokenizing input text
  * CLIP encoder for embeddings
  * Scheduler for noise determination
  * Organizing and simplifying code
  * Negative prompts and callbacks
  * Iterators and generators in Python
  * Custom class for matrices
  * Dunder methods
  * Python data model
  * Tensors
  * Pseudo-random number generation 
    * Wickman-Hill algorithm
    * Random state in deep learning
  * Linear classifier using a tensor

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-10-official-topic/101171)
  * [Paper walkthrough video](https://www.youtube.com/watch?v=ZXuK6IRJlnk) by @johnowhitaker covering _Progressive Distillation for Fast Sampling of Diffusion Models_
  * [diffusion-nbs repo](https://github.com/fastai/diffusion-nbs) (we continue walking through `stable_diffusion.ipynb` that we touched upon last time)
  * [Fashion-MNIST reimplementation](https://mlops.systems/computervision/fastai/parttwo/2022/10/24/foundations-mnist-basics.html) of the lesson, with notes, by @strickvl

## Links from the lesson

  * [Course 2022p2 repo](https://github.com/fastai/course22p2)
  * [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)
  * [Imagic paper](https://arxiv.org/abs/2210.09276). Within a few hours [stable diffusion versions](https://twitter.com/Buntworthy/status/1582307817884889088?s=20&t=BAiIP4MoZXt6ptq2kp9Xug) are appearing.
  * APL: [Array programming - fast.ai Course Forums](https://forums.fast.ai/c/array-programming/56)

[ __ 9: Stable Diffusion ](../Lessons/lesson9.html)

[ 11: Matrix multiplication __](../Lessons/lesson11.html)
