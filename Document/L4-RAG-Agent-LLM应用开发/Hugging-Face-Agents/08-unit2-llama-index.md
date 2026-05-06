[![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Hugging Face](</>)

  * [ Models ](</models>)
  * [ Datasets ](</datasets>)
  * [ Spaces ](</spaces>)
  * [ Buckets new](</storage>)
  * [ Docs ](</docs>)
  * [ Enterprise ](</enterprise>)
  * [Pricing](</pricing>)
  *   * * * *

  * [Log In](</login>)
  * [Sign Up](</join>)

Agents Course documentation

Introduction to LlamaIndex

# Agents Course

🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseDeep RL CourseDiffusion CourseLLM CourseMCP CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. Welcome to the course

Live 1. How the course works and Q&A;

Unit 1. Introduction to Agents

Unit 2. Frameworks for AI Agents

Unit 2.1 The smolagents framework

Unit 2.2 The LlamaIndex framework

[Introduction to LLamaIndex](</learn/agents-course/unit2/llama-index/introduction>)[Introduction to LlamaHub](</learn/agents-course/unit2/llama-index/llama-hub>)[What are Components in LlamaIndex?](</learn/agents-course/unit2/llama-index/components>)[Using Tools in LlamaIndex](</learn/agents-course/unit2/llama-index/tools>)[Quick Quiz 1](</learn/agents-course/unit2/llama-index/quiz1>)[Using Agents in LlamaIndex](</learn/agents-course/unit2/llama-index/agents>)[Creating Agentic Workflows in LlamaIndex](</learn/agents-course/unit2/llama-index/workflows>)[Quick Quiz 2](</learn/agents-course/unit2/llama-index/quiz2>)[Conclusion](</learn/agents-course/unit2/llama-index/conclusion>)

Unit 2.3 The LangGraph framework

Unit 3. Use Case for Agentic RAG

Unit 4. Final Project - Create, Test, and Certify Your Agent

Bonus Unit 1. Fine-tuning an LLM for Function-calling

Bonus Unit 2. Agent Observability and Evaluation

Bonus Unit 3. Agents in Games with Pokemon

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](</join>)

to get started

Copy page

# [](<#introduction-to-llamaindex>) Introduction to LlamaIndex

Welcome to this module, where you’ll learn how to build LLM-powered agents using the [LlamaIndex](<https://www.llamaindex.ai/>) toolkit.

LlamaIndex is **a complete toolkit for creating LLM-powered agents over your data using indexes and workflows**. For this course we’ll focus on three main parts that help build agents in LlamaIndex: **Components** , **Agents and Tools** and **Workflows**.

![LlamaIndex](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit2/llama-index/thumbnail.png)

Let’s look at these key parts of LlamaIndex and how they help with agents:

  * **Components** : Are the basic building blocks you use in LlamaIndex. These include things like prompts, models, and databases. Components often help connect LlamaIndex with other tools and libraries.
  * **Tools** : Tools are components that provide specific capabilities like searching, calculating, or accessing external services. They are the building blocks that enable agents to perform tasks.
  * **Agents** : Agents are autonomous components that can use tools and make decisions. They coordinate tool usage to accomplish complex goals.
  * **Workflows** : Are step-by-step processes that process logic together. Workflows or agentic workflows are a way to structure agentic behaviour without the explicit use of agents.

## [](<#what-makes-llamaindex-special>) What Makes LlamaIndex Special?

While LlamaIndex does some things similar to other frameworks like smolagents, it has some key benefits:

  * **Clear Workflow System** : Workflows help break down how agents should make decisions step by step using an event-driven and async-first syntax. This helps you clearly compose and organize your logic.
  * **Advanced Document Parsing with LlamaParse** : LlamaParse was made specifically for LlamaIndex, so the integration is seamless, although it is a paid feature.
  * **Many Ready-to-Use Components** : LlamaIndex has been around for a while, so it works with lots of other frameworks. This means it has many tested and reliable components, like LLMs, retrievers, indexes, and more.
  * **LlamaHub** : is a registry of hundreds of these components, agents, and tools that you can use within LlamaIndex.

All of these concepts are required in different scenarios to create useful agents. In the following sections, we will go over each of these concepts in detail. After mastering the concepts, we will use our learnings to **create applied use cases with Alfred the agent**!

Getting our hands on LlamaIndex is exciting, right? So, what are we waiting for? Let’s get started with **finding and installing the integrations we need using LlamaHub! 🚀**

[ Update on GitHub](<https://github.com/huggingface/agents-course/blob/main/units/en/unit2/llama-index/introduction.mdx>)

[←Conclusion](</learn/agents-course/unit2/smolagents/conclusion>) [Introduction to LlamaHub→](</learn/agents-course/unit2/llama-index/llama-hub>)

[Introduction to LlamaIndex](<#introduction-to-llamaindex>)[What Makes LlamaIndex Special?](<#what-makes-llamaindex-special>)
