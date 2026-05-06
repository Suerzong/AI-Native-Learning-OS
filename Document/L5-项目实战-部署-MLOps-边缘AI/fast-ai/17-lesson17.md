[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [17: Initialization/normalization](../Lessons/lesson17.html)

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
  * Papers from the lesson

  * [__Report an issue](https://github.com/fastai/course22-web/issues/new)

  1. [Part 2](../Lessons/part2.html)
  2. [17: Initialization/normalization](../Lessons/lesson17.html)

# 17: Initialization/normalization

In this lesson, we discuss the importance of weight initialization in neural networks and explore various techniques to improve training. We start by introducing changes to the miniai library and demonstrate the use of HooksCallback and ActivationStats for better visualization. We then dive into the importance of having zero mean and unit standard deviation in neural networks and introduce the Glorot (Xavier) initialization.

We also cover variance, standard deviation, and covariance, and their significance in understanding relationships between data points. We create a novel Generalized ReLU activation function and discuss the Layer-wise Sequential Unit Variance (LSUV) technique for initializing any neural network. We explore normalization techniques, such as Layer Normalization and Batch Normalization, and briefly mention other normalization methods like Instance Norm and Group Norm.

Finally, we experiment with different batch sizes, learning rates, and optimizers like Accelerated SGD, RMSProp, and Adam to improve performance.

## Concepts discussed

  * Callback class and TrainLearner subclass
  * HooksCallback and ActivationStats
  * Glorot (Xavier) initialization
  * Variance, standard deviation, and covariance
  * General ReLU activation function
  * Layer-wise Sequential Unit Variance (LSUV)
  * Layer Normalization and Batch Normalization
  * Instance Norm and Group Norm
  * Accelerated SGD, RMSProp, and Adam optimizers
  * Experimenting with batch sizes and learning rates

## Video

## Papers from the lesson

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-17-official-topic/102602)
  * [Understanding the difficulty of training deep feedforward neural networks - Xavier Glorot, Yoshua Bengio](http://proceedings.mlr.press/v9/glorot10a)
  * [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification - Kaiming He et al](https://arxiv.org/abs/1502.01852)
  * [LSUV - All you need is a good init - Dmytro Mishkin, Jiri Matas](https://arxiv.org/abs/1511.06422)
  * [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift - Sergey Ioffe, Christian Szegedy](https://arxiv.org/abs/1502.03167)
  * [Layer Normalization - Ba, Kiros, Hinton](https://arxiv.org/abs/1607.06450)

[ __ 16: The Learner framework ](../Lessons/lesson16.html)

[ 18: Accelerated SGD & ResNets __](../Lessons/lesson18.html)
