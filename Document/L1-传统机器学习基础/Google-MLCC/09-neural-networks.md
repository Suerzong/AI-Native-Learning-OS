#  Neural networks
  * This module explores neural networks, a model architecture designed to automatically identify nonlinear patterns in data, eliminating the need for manual feature cross experimentation.

  * You will learn the fundamental components of a deep neural network, including nodes, hidden layers, and activation functions, and how they contribute to prediction.

  * The module covers the training process of neural networks, using the backpropagation algorithm to optimize predictions and minimize loss.

  * Additionally, you will gain insights into how neural networks handle multi-class classification problems using one-vs.-all and one-vs.-one approaches.

  * This module builds on prior knowledge of machine learning concepts such as linear and logistic regression, classification, and working with numerical and categorical data.

You may recall from the [Feature cross exercises](</machine-learning/crash-course/categorical-data/feature-cross-exercises>) in the [Categorical data module](</machine-learning/crash-course/categorical-data>), that the following classification problem is nonlinear:

![Figure 1. Cartesian coordinate plane, divided into four
      quadrants, each filled with random dots in a shape resembling a
      square. The dots in the top-right and bottom-leftquadrants are blue,
      and the dots in the top-left and bottom-right quadrants are orange.](/static/machine-learning/crash-course/neural-networks/images/nonlinear_simple.png) **Figure 1.** Nonlinear classification problem. A linear function cannot cleanly separate all the blue dots from the orange dots.

"Nonlinear" means that you can't accurately predict a label with a model of the form \\(b + w_1x_1 + w_2x_2\\). In other words, the "decision surface" is not a line.

However, if we perform a feature cross on our features $x_1$ and $x_2$, we can then represent the nonlinear relationship between the two features using a [**linear model**](</machine-learning/glossary#linear-model>): $b + w_1x_1 + w_2x_2 + w_3x_3$ where $x_3$ is the feature cross between $x_1$ and $x_2$:

![Figure 2. The same Cartesian coordinate plane of blue and orange
      dots as in Figure 1.  However, this time a white hyperbolic curve is
      plotted atop the grid, which separates the blue dots in the top-right
      and bottom-left quadrants \(now shaded with a blue background\) from
      the orange dots in the top-left and bottom right quadrants \(now
      shaded with an orange background\).](/static/machine-learning/crash-course/neural-networks/images/nonlinear_simple_feature_cross.png) **Figure 2.** By adding the feature cross _x_ 1 _x_ 2, the linear model can learn a hyperbolic shape that separates the blue dots from the orange dots.

Now consider the following dataset:

![Figure 3. Cartesian coordinate plane, divided into four quadrants.
      A circular cluster of blue dots is centered at the origin of the
      graph, and is surrounded by a ring of orange dots.](/static/machine-learning/crash-course/neural-networks/images/nonlinear_complex.png) **Figure 3.** A more difficult nonlinear classification problem.

You may also recall from the [Feature cross exercises](</machine-learning/crash-course/categorical-data/feature-cross-exercises>) that determining the correct feature crosses to fit a linear model to this data took a bit more effort and experimentation.

But what if you didn't have to do all that experimentation yourself? [**Neural networks**](</machine-learning/glossary#neural_network>) are a family of model architectures designed to find [**nonlinear**](</machine-learning/glossary#nonlinear>) patterns in data. During training of a neural network, the [**model**](</machine-learning/glossary#model>) automatically learns the optimal feature crosses to perform on the input data to minimize loss.

In the following sections, we'll take a closer look at how neural networks work.

[Help Center](<https://support.google.com/machinelearningeducation>)

[ Previous arrow_back  Test your knowledge (10 min)  ](</machine-learning/crash-course/overfitting/test-your-knowledge>)

[ Next Nodes and hidden layers (15 min)  arrow_forward  ](</machine-learning/crash-course/neural-networks/nodes-hidden-layers>)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](<https://creativecommons.org/licenses/by/4.0/>), and code samples are licensed under the [Apache 2.0 License](<https://www.apache.org/licenses/LICENSE-2.0>). For details, see the [Google Developers Site Policies](<https://developers.google.com/site-policies>). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.
