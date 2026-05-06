[ Practical Deep Learning for Coders ](../index.html)

  * [ __ ](https://github.com/fastai/course22)

[ __ ]( "Toggle reader mode")

__

  1. [Part 2](../Lessons/part2.html)
  2. [11: Matrix multiplication](../Lessons/lesson11.html)

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
  2. [11: Matrix multiplication](../Lessons/lesson11.html)

# 11: Matrix multiplication

In this lesson, we discuss various techniques and experiments shared by students on the forum, such as interpolating between prompts for visually appealing transitions and improving the update process in text-to-image generation, and a novel approach to decreasing the guidance scale during image generation. We then dive into a new paper called DiffEdit, which focuses on semantic image editing using text-conditioned diffusion models. We walk through the process of reading and understanding the paper, emphasizing the importance of grasping the main idea and not getting bogged down in every detail.

We then embark on a deep exploration of matrix multiplication using Python, compare APL with PyTorch, and introduce the concept of Frobenius norm. We also discuss the powerful concept of broadcasting, which allows for operations between tensors of different shapes, and demonstrate its efficiency in speeding up matrix multiplication. The techniques introduced in this lesson allow us to speed up our initial Python implementation by a factor of around five million, including leveraging the GPU for massive parallelism!

## Concepts discussed

  * Diffusion improvements 
    * Interpolating between prompts for visually appealing transitions
    * Improving the update process in text-to-image generation
    * Decreasing the guidance scale during image generation
  * Understanding research papers
  * Matrix multiplication using Python and Numba
  * Comparing APL with PyTorch
  * Frobenius norm
  * Broadcasting in deep learning and machine learning code

## Video

## Lesson resources

  * [Discuss this lesson](https://forums.fast.ai/t/lesson-11-official-topic/101508)
  * [DiffEdit: Diffusion-based semantic image editing with mask guidance](https://arxiv.org/abs/2210.11427)
  * Math notation 
    * [Greek letters](https://en.wikipedia.org/wiki/Greek_alphabet)
    * [All in one mathematics cheat sheet](https://ourway.keybase.pub/mathematics_cheat_sheet.pdf) (PDF)
    * [Glossary of mathematical symbols](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols#Other_brackets) (wikipedia)
    * [pix2tex](https://github.com/lukas-blecher/LaTeX-OCR) (open source) or [Mathpix](https://mathpix.com/) (commercial)
    * [Greek Letters for Deep Learning](https://ankiweb.net/shared/info/2118139507) \- Anki deck containing fastai-related Greek letters
    * [Detexify](https://detexify.kirelabs.org/classify.html) Draw math symbols

[ __ 10: Diving Deeper ](../Lessons/lesson10.html)

[ 12: Mean shift clustering __](../Lessons/lesson12.html)
