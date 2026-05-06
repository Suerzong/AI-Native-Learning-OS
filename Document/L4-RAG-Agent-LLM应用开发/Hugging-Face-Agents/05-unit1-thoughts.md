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

Thought: Internal Reasoning and the ReAct Approach

# Agents Course

🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseDeep RL CourseDiffusion CourseLLM CourseMCP CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. Welcome to the course

Live 1. How the course works and Q&A;

Unit 1. Introduction to Agents

[Introduction](</learn/agents-course/unit1/introduction>)[What is an Agent?](</learn/agents-course/unit1/what-are-agents>)[Quick Quiz 1](</learn/agents-course/unit1/quiz1>)[What are LLMs?](</learn/agents-course/unit1/what-are-llms>)[Messages and Special Tokens](</learn/agents-course/unit1/messages-and-special-tokens>)[What are Tools?](</learn/agents-course/unit1/tools>)[Quick Quiz 2](</learn/agents-course/unit1/quiz2>)[Understanding AI Agents through the Thought-Action-Observation Cycle](</learn/agents-course/unit1/agent-steps-and-structure>)[Thought, Internal Reasoning and the Re-Act Approach](</learn/agents-course/unit1/thoughts>)[Actions, Enabling the Agent to Engage with Its Environment](</learn/agents-course/unit1/actions>)[Observe, Integrating Feedback to Reflect and Adapt](</learn/agents-course/unit1/observations>)[Dummy Agent Library](</learn/agents-course/unit1/dummy-agent-library>)[Let’s Create Our First Agent Using smolagents](</learn/agents-course/unit1/tutorial>)[Unit 1 Final Quiz](</learn/agents-course/unit1/final-quiz>)[Conclusion](</learn/agents-course/unit1/conclusion>)

Unit 2. Frameworks for AI Agents

Unit 2.1 The smolagents framework

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

# [](<#thought-internal-reasoning-and-the-react-approach>) Thought: Internal Reasoning and the ReAct Approach

> In this section, we dive into the inner workings of an AI agent—its ability to reason and plan. We’ll explore how the agent leverages its internal dialogue to analyze information, break down complex problems into manageable steps, and decide what action to take next.
>
> Additionally, we introduce the ReAct approach, a prompting technique that encourages the model to think “step by step” before acting.

Thoughts represent the **Agent’s internal reasoning and planning processes** to solve the task.

This utilises the agent’s Large Language Model (LLM) capacity **to analyze information when presented in its prompt** — essentially, its inner monologue as it works through a problem.

The Agent’s thoughts help it assess current observations and decide what the next action(s) should be. Through this process, the agent can **break down complex problems into smaller, more manageable steps** , reflect on past experiences, and continuously adjust its plans based on new information.

## [](<#-examples-of-common-thought-types>) 🧠 Examples of Common Thought Types

Type of Thought | Example
---|---
Planning | “I need to break this task into three steps: 1) gather data, 2) analyze trends, 3) generate report”
Analysis | “Based on the error message, the issue appears to be with the database connection parameters”
Decision Making | “Given the user’s budget constraints, I should recommend the mid-tier option”
Problem Solving | “To optimize this code, I should first profile it to identify bottlenecks”
Memory Integration | “The user mentioned their preference for Python earlier, so I’ll provide examples in Python”
Self-Reflection | “My last approach didn’t work well, I should try a different strategy”
Goal Setting | “To complete this task, I need to first establish the acceptance criteria”
Prioritization | “The security vulnerability should be addressed before adding new features”

> **Note:** In the case of LLMs fine-tuned for function-calling, the thought process is optional. More details will be covered in the Actions section.

## [](<#-chain-of-thought-cot>) 🔗 Chain-of-Thought (CoT)

**Chain-of-Thought (CoT)** is a prompting technique that guides a model to **think through a problem step-by-step before producing a final answer.**

It typically starts with:

> _“Let’s think step by step.”_

This approach helps the model **reason internally** , especially for logical or mathematical tasks, **without interacting with external tools**.

### [](<#-example-cot>) ✅ Example (CoT)

Copied

    Question: What is 15% of 200?
    Thought: Let's think step by step. 10% of 200 is 20, and 5% of 200 is 10, so 15% is 30.
    Answer: 30

## [](<#-react-reasoning--acting>) ⚙️ ReAct: Reasoning + Acting

A key method is the **ReAct approach** , which combines “Reasoning” (Think) with “Acting” (Act).

ReAct is a prompting technique that encourages the model to think step-by-step and interleave actions (like using tools) between reasoning steps.

This enables the agent to solve complex multi-step tasks by alternating between:

  * Thought: internal reasoning
  * Action: tool usage
  * Observation: receiving tool output

### [](<#-example-react>) 🔄 Example (ReAct)

Copied

    Thought: I need to find the latest weather in Paris.
    Action: Search["weather in Paris"]
    Observation: It's 18°C and cloudy.
    Thought: Now that I know the weather...
    Action: Finish["It's 18°C and cloudy in Paris."]

![ReAct](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/ReAct.png) (d) is an example of the ReAct approach, where we prompt "Let's think step by step", and the model acts between thoughts.

## [](<#-comparison-react-vs-cot>) 🔁 Comparison: ReAct vs. CoT

Feature | Chain-of-Thought (CoT) | ReAct
---|---|---
Step-by-step logic | ✅ Yes | ✅ Yes
External tools | ❌ No | ✅ Yes (Actions + Observations)
Best suited for | Logic, math, internal tasks | Info-seeking, dynamic multi-step tasks

> Recent models like **Deepseek R1** or **OpenAI’s o1** were fine-tuned to _think before answering_. They use structured tokens like `<think>` and `</think>` to explicitly separate the reasoning phase from the final answer.
>
> Unlike ReAct or CoT — which are prompting strategies — this is a **training-level technique** , where the model learns to think via examples.

[ Update on GitHub](<https://github.com/huggingface/agents-course/blob/main/units/en/unit1/thoughts.mdx>)

[←Understanding AI Agents through the Thought-Action-Observation Cycle](</learn/agents-course/unit1/agent-steps-and-structure>) [Actions, Enabling the Agent to Engage with Its Environment→](</learn/agents-course/unit1/actions>)

[Thought: Internal Reasoning and the ReAct Approach](<#thought-internal-reasoning-and-the-react-approach>)[🧠 Examples of Common Thought Types](<#-examples-of-common-thought-types>)[🔗 Chain-of-Thought (CoT)](<#-chain-of-thought-cot>)[✅ Example (CoT)](<#-example-cot>)[⚙️ ReAct: Reasoning + Acting](<#-react-reasoning--acting>)[🔄 Example (ReAct)](<#-example-react>)[🔁 Comparison: ReAct vs. CoT](<#-comparison-react-vs-cot>)
