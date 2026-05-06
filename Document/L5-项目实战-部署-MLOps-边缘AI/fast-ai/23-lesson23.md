[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [23: Super-resolution](../Lessons/lesson23.html)

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
  2. [23: Super-resolution](../Lessons/lesson23.html)

# 23: Super-resolution

In this lesson, we work with Tiny Imagenet to create a super-resolution U-Net model, discussing dataset creation, preprocessing, and data augmentation. The goal of super-resolution is to scale up a low-resolution image to a higher resolution. We train the model using AdamW optimizer and mixed precision, achieving an accuracy of nearly 60%. We also explore the potential for improvement by examining the results of other models on Tiny Imagenet from the Papers with Code website.

We discuss the limitations of using a convolutional neural network for image super-resolution and introduce the concept of U-net, a more efficient architecture for this task. We implement perceptual loss, which involves comparing the features of the output image and the target image at an intermediate layer of a pre-trained classifier model. After training the U-net model with the new loss function, the output images are less blurry and more similar to the target images.

Finally, we discuss the challenges of comparing different models and their outputs. We demonstrate how perceptual loss has improved the results significantly, but also note that there isn’t a clear metric to use for comparison. We then move on to gradually unfreezing pre-trained networks, a favorite trick at fast.ai. We copy the weights from the pre-trained model into our model and train it for one epoch with frozen weights for the down path. This results in a significant improvement in loss.

## Concepts discussed

  * Tiny Imagenet dataset
  * Creating a super-resolution U-Net model
  * Data preprocessing and augmentation
  * Perceptual loss
  * Gradually unfreezing pre-trained networks
  * Experimenting with cross connections in Unet

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-23-official-topic/103965)
  * [TrivialAugment: Tuning-free Yet State-of-the-Art Data Augmentation](https://arxiv.org/pdf/2103.10158.pdf)
  * [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)

[ __ 22: Karras et al (2022) ](../Lessons/lesson22.html)

[ 24: Attention & transformers __](../Lessons/lesson24.html)
