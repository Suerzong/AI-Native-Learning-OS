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

Introduction to smolagents

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

[Introduction to smolagents](</learn/agents-course/unit2/smolagents/introduction>)[Why use smolagents?](</learn/agents-course/unit2/smolagents/why_use_smolagents>)[Quick Quiz 1](</learn/agents-course/unit2/smolagents/quiz1>)[Building Agents That Use Code](</learn/agents-course/unit2/smolagents/code_agents>)[Writing actions as code snippets or JSON blobs](</learn/agents-course/unit2/smolagents/tool_calling_agents>)[Tools](</learn/agents-course/unit2/smolagents/tools>)[Retrieval Agents](</learn/agents-course/unit2/smolagents/retrieval_agents>)[Quick Quiz 2](</learn/agents-course/unit2/smolagents/quiz2>)[Multi-Agent Systems](</learn/agents-course/unit2/smolagents/multi_agent_systems>)[Vision and Browser agents](</learn/agents-course/unit2/smolagents/vision_agents>)[Final Quiz](</learn/agents-course/unit2/smolagents/final_quiz>)[Conclusion](</learn/agents-course/unit2/smolagents/conclusion>)

Unit 2.2 The LlamaIndex framework

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

# [](<#introduction-to-smolagents>) Introduction to smolagents

![Unit 2.1 Thumbnail](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit2/smolagents/thumbnail.jpg)

Welcome to this module, where you’ll learn **how to build effective agents** using the [`smolagents`](<https://github.com/huggingface/smolagents>) library, which provides a lightweight framework for creating capable AI agents.

`smolagents` is a Hugging Face library; therefore, we would appreciate your support by **starring** the smolagents [`repository`](<https://github.com/huggingface/smolagents>) :

![staring smolagents](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit2/smolagents/star_smolagents.gif)

## [](<#module-overview>) Module Overview

This module provides a comprehensive overview of key concepts and practical strategies for building intelligent agents using `smolagents`.

With so many open-source frameworks available, it’s essential to understand the components and capabilities that make `smolagents` a useful option or to determine when another solution might be a better fit.

We’ll explore critical agent types, including code agents designed for software development tasks, tool calling agents for creating modular, function-driven workflows, and retrieval agents that access and synthesize information.

Additionally, we’ll cover the orchestration of multiple agents as well as the integration of vision capabilities and web browsing, which unlock new possibilities for dynamic and context-aware applications.

In this unit, Alfred, the agent from Unit 1, makes his return. This time, he’s using the `smolagents` framework for his internal workings. Together, we’ll explore the key concepts behind this framework as Alfred tackles various tasks. Alfred is organizing a party at the Wayne Manor while the Wayne family 🦇 is away, and he has plenty to do. Join us as we showcase his journey and how he handles these tasks with `smolagents`!

> In this unit, you will learn to build AI agents with the `smolagents` library. Your agents will be able to search for data, execute code, and interact with web pages. You will also learn how to combine multiple agents to create more powerful systems.

![Alfred the agent](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/this-is-alfred.jpg)

## [](<#contents>) Contents

During this unit on `smolagents`, we cover:

### [](<#1-why-use-smolagents>) 1️⃣ Why Use smolagents

`smolagents` is one of the many open-source agent frameworks available for application development. Alternative options include `LlamaIndex` and `LangGraph`, which are also covered in other modules in this course. `smolagents` offers several key features that might make it a great fit for specific use cases, but we should always consider all options when selecting a framework. We’ll explore the advantages and drawbacks of using `smolagents`, helping you make an informed decision based on your project’s requirements.

### [](<#2-codeagents>) 2️⃣ CodeAgents

`CodeAgents` are the primary type of agent in `smolagents`. Instead of generating JSON or text, these agents produce Python code to perform actions. This module explores their purpose, functionality, and how they work, along with hands-on examples to showcase their capabilities.

### [](<#3-toolcallingagents>) 3️⃣ ToolCallingAgents

`ToolCallingAgents` are the second type of agent supported by `smolagents`. Unlike `CodeAgents`, which generate Python code, these agents rely on JSON/text blobs that the system must parse and interpret to execute actions. This module covers their functionality, their key differences from `CodeAgents`, and it provides an example to illustrate their usage.

### [](<#4-tools>) 4️⃣ Tools

As we saw in Unit 1, tools are functions that an LLM can use within an agentic system, and they act as the essential building blocks for agent behavior. This module covers how to create tools, their structure, and different implementation methods using the `Tool` class or the `@tool` decorator. You’ll also learn about the default toolbox, how to share tools with the community, and how to load community-contributed tools for use in your agents.

### [](<#5-retrieval-agents>) 5️⃣ Retrieval Agents

Retrieval agents allow models access to knowledge bases, making it possible to search, synthesize, and retrieve information from multiple sources. They leverage vector stores for efficient retrieval and implement **Retrieval-Augmented Generation (RAG)** patterns. These agents are particularly useful for integrating web search with custom knowledge bases while maintaining conversation context through memory systems. This module explores implementation strategies, including fallback mechanisms for robust information retrieval.

### [](<#6-multi-agent-systems>) 6️⃣ Multi-Agent Systems

Orchestrating multiple agents effectively is crucial for building powerful, multi-agent systems. By combining agents with different capabilities—such as a web search agent with a code execution agent—you can create more sophisticated solutions. This module focuses on designing, implementing, and managing multi-agent systems to maximize efficiency and reliability.

### [](<#7-vision-and-browser-agents>) 7️⃣ Vision and Browser agents

Vision agents extend traditional agent capabilities by incorporating **Vision-Language Models (VLMs)** , enabling them to process and interpret visual information. This module explores how to design and integrate VLM-powered agents, unlocking advanced functionalities like image-based reasoning, visual data analysis, and multimodal interactions. We will also use vision agents to build a browser agent that can browse the web and extract information from it.

## [](<#resources>) Resources

  * [smolagents Documentation](<https://huggingface.co/docs/smolagents>) \- Official docs for the smolagents library
  * [Building Effective Agents](<https://www.anthropic.com/research/building-effective-agents>) \- Research paper on agent architectures
  * [Agent Guidelines](<https://huggingface.co/docs/smolagents/tutorials/building_good_agents>) \- Best practices for building reliable agents
  * [LangGraph Agents](<https://langchain-ai.github.io/langgraph/>) \- Additional examples of agent implementations
  * [Function Calling Guide](<https://platform.openai.com/docs/guides/function-calling>) \- Understanding function calling in LLMs
  * [RAG Best Practices](<https://www.pinecone.io/learn/retrieval-augmented-generation/>) \- Guide to implementing effective RAG

[ Update on GitHub](<https://github.com/huggingface/agents-course/blob/main/units/en/unit2/smolagents/introduction.mdx>)

[←Frameworks for AI Agents](</learn/agents-course/unit2/introduction>) [Why use smolagents?→](</learn/agents-course/unit2/smolagents/why_use_smolagents>)

[Introduction to smolagents](<#introduction-to-smolagents>)[Module Overview](<#module-overview>)[Contents](<#contents>)[1️⃣ Why Use smolagents](<#1-why-use-smolagents>)[2️⃣ CodeAgents](<#2-codeagents>)[3️⃣ ToolCallingAgents](<#3-toolcallingagents>)[4️⃣ Tools](<#4-tools>)[5️⃣ Retrieval Agents](<#5-retrieval-agents>)[6️⃣ Multi-Agent Systems](<#6-multi-agent-systems>)[7️⃣ Vision and Browser agents](<#7-vision-and-browser-agents>)[Resources](<#resources>)
