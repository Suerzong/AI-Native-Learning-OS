#  Production ML systems
  * This module explores the broader ecosystem of a production ML system, emphasizing that the model itself is only a small part of the overall system.

  * You will learn to choose the appropriate training and inference paradigms (static or dynamic) based on your specific needs.

  * The module covers key aspects of production ML systems, including testing, identifying potential flaws, and monitoring the system's components.

  * As a prerequisite, familiarity with foundational machine learning concepts, including linear regression, data types, and overfitting, is assumed.

  * Building upon previous modules, this content shifts focus to the practical aspects of deploying and maintaining ML models in real-world scenarios.

So far, this course has focused on building machine learning (ML) models. However, as Figure 1 suggests, real-world production ML systems are large ecosystems and the model is just a single, relatively small part.

![Figure 1. ML system diagram containing the following components:
            data collection, feature extraction, process management tools,
            data verification, configuration, machine resource management,
            monitoring, serving infrastructure, and ML model code. The ML
            model code part of the diagram is dwarfed by the other nine
            components.](/static/machine-learning/crash-course/images/MlSystem.png) **Figure 1.** A real-world production ML system comprises many components.

At the heart of a real-world machine learning production system is the ML model code, but it often represents only 5% or less of the total codebase in the system. That's not a misprint; it's significantly less than you might expect. Notice that an ML production system devotes considerable resources to the input data: collecting it, verifying it, and extracting features from it.

[Help Center](<https://support.google.com/machinelearningeducation>)

[ Previous arrow_back  Test your knowledge (10 min)  ](</machine-learning/crash-course/llm/test-your-knowledge>)

[ Next Static vs. dynamic training (10 min)  arrow_forward  ](</machine-learning/crash-course/production-ml-systems/static-vs-dynamic-training>)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](<https://creativecommons.org/licenses/by/4.0/>), and code samples are licensed under the [Apache 2.0 License](<https://www.apache.org/licenses/LICENSE-2.0>). For details, see the [Google Developers Site Policies](<https://developers.google.com/site-policies>). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.
