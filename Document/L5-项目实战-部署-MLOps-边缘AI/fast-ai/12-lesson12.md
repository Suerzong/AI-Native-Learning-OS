[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [12: Mean shift clustering](../Lessons/lesson12.html)

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
  2. [12: Mean shift clustering](../Lessons/lesson12.html)

# 12: Mean shift clustering

In this lesson, we start by discussing the CLIP Interrogator, a Hugging Face Spaces Gradio app that generates text prompts for creating CLIP embeddings. We then dive back into matrix multiplication, using Einstein summation notation and torch.einsum to simplify code and improve performance. We explore GPU acceleration with CUDA and Numba, demonstrating how to write a kernel function for matrix multiplication and launch it on the GPU.

Next up we exercise our tensor programming skills by implementing mean shift clustering, a technique for identifying clusters within a dataset. We create synthetic data, explain the mean shift algorithm, and introduce the Gaussian kernel for penalizing distant points. We implement the mean shift clustering algorithm using PyTorch and discuss the importance of tensor manipulation operations for efficient GPU programming.

Finally, we optimize the mean shift algorithm using PyTorch and GPUs, demonstrating how to calculate weights, multiply matrices, and sum up points to obtain new data points. We explore the impact of changing batch sizes on performance and encourage viewers to research other clustering algorithms.

The lesson concludes with an introduction to calculus, focusing on derivatives and the calculus of infinitesimals.

## Concepts discussed

  * CLIP Interrogator
  * Inverse problems
  * Matrix multiplication
  * Einstein summation notation and torch.einsum
  * GPU acceleration and CUDA
  * Numba
  * Mean shift clustering
  * Gaussian kernel
  * Norms
  * Euclidean distance
  * Calculus 
    * Derivatives and Infinitesimals

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-12-official-topic/101702)
  * [CLIP Interrogator](https://huggingface.co/spaces/pharma/CLIP-Interrogator)
  * [Essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3blue1brown)

[ __ 11: Matrix multiplication ](../Lessons/lesson11.html)

[ 13: Backpropagation & MLP __](../Lessons/lesson13.html)
