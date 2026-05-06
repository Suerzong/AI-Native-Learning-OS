[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [22: Karras et al (2022)](../Lessons/lesson22.html)

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
  2. [22: Karras et al (2022)](../Lessons/lesson22.html)

# 22: Karras et al (2022)

Jeremy begins this lesson with a discussion of improvements to the DDPM/DDIM implementation. He explores the removal of the concept of an integral number of steps, making the process more continuous. He then delves into predicting the amount of noise in an image without passing the time step as input and modifies the DDIM step to use the predicted alpha bar for each image.

The focus of the lesson is to study and implement the 2022 paper by Karras et al, [Elucidating the Design Space of Diffusion-Based Generative Models](https://arxiv.org/abs/2206.00364). The paper uses _pre-conditioning_ to ensure that inputs and targets to the model are scaled to unit variance. The model predicts an interpolated version of the clean image and the noise, depending on the amount of noise present in the input.

The lesson covers various sampling techniques, such as the Euler sampler, Ancestral Euler sampler, and Heuns method. Jeremy explains the concepts behind these methods and demonstrates how they can be used to improve the sampling process. He emphasizes the importance of understanding the underlying concepts and techniques in research papers and demonstrates how these can be applied to improve model performance.

## Concepts discussed

  * DDPM/DDIM improvements
  * Predicting the amount of noise in an image
  * Noise scheduling for diffusion models
  * Scaling input and output images
  * Importance of unit variance inputs and outputs
  * Implementation and performance of different samplers 
    * Euler sampler
    * Ancestral Euler sampler
    * Heuns method
    * LMS sampler

## Video

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-22-official-topic/103586)

[ __ 21: DDIM ](../Lessons/lesson21.html)

[ 23: Super-resolution __](../Lessons/lesson23.html)
