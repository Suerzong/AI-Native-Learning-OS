#  Embeddings
  * This module explains how to create embeddings, which are lower-dimensional representations of sparse data that address the problems of large input vectors and lack of meaningful relations between vectors in one-hot encoding.

  * One-hot encoding creates large input vectors, leading to a huge number of weights in a neural network, requiring more data, computation, and memory.

  * One-hot encoding vectors lack meaningful relationships, failing to capture semantic similarities between items, like the example of hot dogs and shawarmas being more similar than hot dogs and salads.

  * Embeddings offer a solution by providing dense vector representations that capture semantic relationships and reduce the dimensionality of data, improving efficiency and performance in machine learning models.

  * This module assumes familiarity with introductory machine learning concepts like linear regression, categorical data, and neural networks.

Imagine you're developing a food-recommendation application, where users input their favorite meals, and the app suggests similar meals that they might like. You want to develop a machine learning (ML) model that can predict food similarity, so your app can make high quality recommendations ("Since you like pancakes, we recommend crepes").

To train your model, you curate a dataset of 5,000 popular meal items, including borscht, hot dog, salad, pizza, and shawarma.

![Figure 1. A set of illustrations of five food items. Clockwise from
       top-left: borscht, hot dog, salad, pizza, shawarma.](/static/machine-learning/crash-course/embeddings/images/food_images.png) **Figure 1.** Sampling of meal items included in the food dataset.

You create a `meal` feature that contains a [**one-hot encoded**](</machine-learning/glossary#one-hot-encoding>) representation of each of the meal items in the dataset. [**Encoding**](</machine-learning/glossary#encoder>) refers to the process of choosing an initial numerical representation of data to train the model on.

![Figure 2. Top: a visualization of the one-hot encoding for borscht.
       The vector \[1, 0, 0, 0, ..., 0\] is displayed above six boxes,
       each aligned from left
       to right with one of the vector numbers. The boxes, from left to right
       contain the following images: borscht, hot dog, salad, pizza, \[empty\],
       shawarma. Middle: a visualization of the one-hot encoding for hot dog.
       The vector \[0, 1, 0, 0, ..., 0\] is displayed above six boxes, each
       aligned from left to right with one of the vector numbers. The boxes have
       the same images from left to right as for the borscht visualization
       above. Bottom: a visualization of the one-hot encoding for shawarma. The
       vector \[0, 0, 0, 0, ..., 1\] is displayed above six boxes, each aligned
       from left to right with one of the vector numbers. The boxes have
       the same images from left to right as for the borscht and hot dog
       visualizations.](/static/machine-learning/crash-course/embeddings/images/food_images_one_hot_encodings.png) **Figure 2.** One-hot encodings of borscht, hot dog, and shawarma. Each one-hot encoding vector has a length of 5,000 (one entry for each menu item in the dataset). The ellipsis in the diagram represents the 4,995 entries not shown.

## Pitfalls of sparse data representations

Reviewing these one-hot encodings, you notice several problems with this representation of the data.

  * **Number of weights.** Large input vectors mean a huge number of [**weights**](</machine-learning/glossary#weight>) for a [**neural network**](</machine-learning/glossary#neural-network>). With M entries in your one-hot encoding, and N nodes in the first layer of the network after the input, the model has to train MxN weights for that layer.
  * **Number of datapoints.** The more weights in your model, the more data you need to train effectively.
  * **Amount of computation.** The more weights, the more computation required to train and use the model. It's easy to exceed the capabilities of your hardware.
  * **Amount of memory.** The more weights in your model, the more memory that is needed on the accelerators that train and serve it. Scaling this up efficiently is very difficult.
  * **Difficulty of supporting on-device machine learning (ODML).** If you're hoping to run your ML model on local devices (as opposed to serving them), you'll need to be focused on making your model smaller, and will want to decrease the number of weights.

In this module, you'll learn how to create **embeddings** , lower-dimensional representations of sparse data, that address these issues.

[Help Center](<https://support.google.com/machinelearningeducation>)

[ Previous arrow_back  Test your knowledge (10 min)  ](</machine-learning/crash-course/neural-networks/test-your-knowledge>)

[ Next Embedding space and static embeddings (10 min)  arrow_forward  ](</machine-learning/crash-course/embeddings/embedding-space>)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](<https://creativecommons.org/licenses/by/4.0/>), and code samples are licensed under the [Apache 2.0 License](<https://www.apache.org/licenses/LICENSE-2.0>). For details, see the [Google Developers Site Policies](<https://developers.google.com/site-policies>). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.
