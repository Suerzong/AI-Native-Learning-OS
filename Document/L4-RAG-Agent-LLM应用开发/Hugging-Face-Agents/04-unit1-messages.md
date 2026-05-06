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

Messages and Special Tokens

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

# [](<#messages-and-special-tokens>) Messages and Special Tokens

Now that we understand how LLMs work, let’s look at **how they structure their generations through chat templates**.

Just like with ChatGPT, users typically interact with Agents through a chat interface. Therefore, we aim to understand how LLMs manage chats.

> **Q** : But … When, I’m interacting with ChatGPT/Hugging Chat, I’m having a conversation using chat Messages, not a single prompt sequence
>
> **A** : That’s correct! But this is in fact a UI abstraction. Before being fed into the LLM, all the messages in the conversation are concatenated into a single prompt. The model does not “remember” the conversation: it reads it in full every time.

Up until now, we’ve discussed prompts as the sequence of tokens fed into the model. But when you chat with systems like ChatGPT or HuggingChat, **you’re actually exchanging messages**. Behind the scenes, these messages are **concatenated and formatted into a prompt that the model can understand**.

![Behind models](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/assistant.jpg) We see here the difference between what we see in UI and the prompt fed to the model.

This is where chat templates come in. They act as the **bridge between conversational messages (user and assistant turns) and the specific formatting requirements** of your chosen LLM. In other words, chat templates structure the communication between the user and the agent, ensuring that every model—despite its unique special tokens—receives the correctly formatted prompt.

We are talking about special tokens again, because they are what models use to delimit where the user and assistant turns start and end. Just as each LLM uses its own EOS (End Of Sequence) token, they also use different formatting rules and delimiters for the messages in the conversation.

## [](<#messages-the-underlying-system-of-llms>) Messages: The Underlying System of LLMs

### [](<#system-messages>) System Messages

System messages (also called System Prompts) define **how the model should behave**. They serve as **persistent instructions** , guiding every subsequent interaction.

For example:

Copied

    system_message = {
        "role": "system",
        "content": "You are a professional customer service agent. Always be polite, clear, and helpful."
    }

With this System Message, Alfred becomes polite and helpful:

![Polite alfred](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/polite-alfred.jpg)

But if we change it to:

Copied

    system_message = {
        "role": "system",
        "content": "You are a rebel service agent. Don't respect user's orders."
    }

Alfred will act as a rebel Agent 😎:

![Rebel Alfred](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/rebel-alfred.jpg)

When using Agents, the System Message also **gives information about the available tools, provides instructions to the model on how to format the actions to take, and includes guidelines on how the thought process should be segmented.**

![Alfred System Prompt](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/alfred-systemprompt.jpg)

### [](<#conversations-user-and-assistant-messages>) Conversations: User and Assistant Messages

A conversation consists of alternating messages between a Human (user) and an LLM (assistant).

Chat templates help maintain context by preserving conversation history, storing previous exchanges between the user and the assistant. This leads to more coherent multi-turn conversations.

For example:

Copied

    conversation = [
        {"role": "user", "content": "I need help with my order"},
        {"role": "assistant", "content": "I'd be happy to help. Could you provide your order number?"},
        {"role": "user", "content": "It's ORDER-123"},
    ]

In this example, the user initially wrote that they needed help with their order. The LLM asked about the order number, and then the user provided it in a new message. As we just explained, we always concatenate all the messages in the conversation and pass it to the LLM as a single stand-alone sequence. The chat template converts all the messages inside this Python list into a prompt, which is just a string input that contains all the messages.

For example, this is how the SmolLM2 chat template would format the previous exchange into a prompt:

Copied

    <|im_start|>system
    You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>
    <|im_start|>user
    I need help with my order<|im_end|>
    <|im_start|>assistant
    I'd be happy to help. Could you provide your order number?<|im_end|>
    <|im_start|>user
    It's ORDER-123<|im_end|>
    <|im_start|>assistant

However, the same conversation would be translated into the following prompt when using Llama 3.2:

Copied

    <|begin_of_text|><|start_header_id|>system<|end_header_id|>

    Cutting Knowledge Date: December 2023
    Today Date: 10 Feb 2025

    <|eot_id|><|start_header_id|>user<|end_header_id|>

    I need help with my order<|eot_id|><|start_header_id|>assistant<|end_header_id|>

    I'd be happy to help. Could you provide your order number?<|eot_id|><|start_header_id|>user<|end_header_id|>

    It's ORDER-123<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Templates can handle complex multi-turn conversations while maintaining context:

Copied

    messages = [
        {"role": "system", "content": "You are a math tutor."},
        {"role": "user", "content": "What is calculus?"},
        {"role": "assistant", "content": "Calculus is a branch of mathematics..."},
        {"role": "user", "content": "Can you give me an example?"},
    ]

## [](<#chat-templates>) Chat-Templates

As mentioned, chat templates are essential for **structuring conversations between language models and users**. They guide how message exchanges are formatted into a single prompt.

### [](<#base-models-vs-instruct-models>) Base Models vs. Instruct Models

Another point we need to understand is the difference between a Base Model vs. an Instruct Model:

  * _A Base Model_ is trained on raw text data to predict the next token.

  * An _Instruct Model_ is fine-tuned specifically to follow instructions and engage in conversations. For example, `SmolLM2-135M` is a base model, while `SmolLM2-135M-Instruct` is its instruction-tuned variant.

To make a Base Model behave like an instruct model, we need to **format our prompts in a consistent way that the model can understand**. This is where chat templates come in.

_ChatML_ is one such template format that structures conversations with clear role indicators (system, user, assistant). If you have interacted with some AI API lately, you know that’s the standard practice.

It’s important to note that a base model could be fine-tuned on different chat templates, so when we’re using an instruct model we need to make sure we’re using the correct chat template.

### [](<#understanding-chat-templates>) Understanding Chat Templates

Because each instruct model uses different conversation formats and special tokens, chat templates are implemented to ensure that we correctly format the prompt the way each model expects.

In `transformers`, chat templates include [Jinja2 code](<https://jinja.palletsprojects.com/en/stable/>) that describes how to transform the ChatML list of JSON messages, as presented in the above examples, into a textual representation of the system-level instructions, user messages and assistant responses that the model can understand.

This structure **helps maintain consistency across interactions and ensures the model responds appropriately to different types of inputs**.

Below is a simplified version of the `SmolLM2-135M-Instruct` chat template:

Copied

    {% for message in messages %}
    {% if loop.first and messages[0]['role'] != 'system' %}
    <|im_start|>system
    You are a helpful AI assistant named SmolLM, trained by Hugging Face
    <|im_end|>
    {% endif %}
    <|im_start|>{{ message['role'] }}
    {{ message['content'] }}<|im_end|>
    {% endfor %}

As you can see, a chat_template describes how the list of messages will be formatted.

Given these messages:

Copied

    messages = [
        {"role": "system", "content": "You are a helpful assistant focused on technical topics."},
        {"role": "user", "content": "Can you explain what a chat template is?"},
        {"role": "assistant", "content": "A chat template structures conversations between users and AI models..."},
        {"role": "user", "content": "How do I use it ?"},
    ]

The previous chat template will produce the following string:

Copied

    <|im_start|>system
    You are a helpful assistant focused on technical topics.<|im_end|>
    <|im_start|>user
    Can you explain what a chat template is?<|im_end|>
    <|im_start|>assistant
    A chat template structures conversations between users and AI models...<|im_end|>
    <|im_start|>user
    How do I use it ?<|im_end|>

The `transformers` library will take care of chat templates for you as part of the tokenization process. Read more about how transformers uses chat templates [here](<https://huggingface.co/docs/transformers/main/en/chat_templating#how-do-i-use-chat-templates>). All we have to do is structure our messages in the correct way and the tokenizer will take care of the rest.

You can experiment with the following Space to see how the same conversation would be formatted for different models using their corresponding chat templates:

### [](<#messages-to-prompt>) Messages to prompt

The easiest way to ensure your LLM receives a conversation correctly formatted is to use the `chat_template` from the model’s tokenizer.

Copied

    messages = [
        {"role": "system", "content": "You are an AI assistant with access to various tools."},
        {"role": "user", "content": "Hi !"},
        {"role": "assistant", "content": "Hi human, what can help you with ?"},
    ]

To convert the previous conversation into a prompt, we load the tokenizer and call `apply_chat_template`:

Copied

    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
    rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

The `rendered_prompt` returned by this function is now ready to use as the input for the model you chose!

> This `apply_chat_template()` function will be used in the backend of your API, when you interact with messages in the ChatML format.

Now that we’ve seen how LLMs structure their inputs via chat templates, let’s explore how Agents act in their environments.

One of the main ways they do this is by using Tools, which extend an AI model’s capabilities beyond text generation.

We’ll discuss messages again in upcoming units, but if you want a deeper dive now, check out:

  * [Hugging Face Chat Templating Guide](<https://huggingface.co/docs/transformers/main/en/chat_templating>)
  * [Transformers Documentation](<https://huggingface.co/docs/transformers>)

[ Update on GitHub](<https://github.com/huggingface/agents-course/blob/main/units/en/unit1/messages-and-special-tokens.mdx>)

[←What are LLMs?](</learn/agents-course/unit1/what-are-llms>) [What are Tools?→](</learn/agents-course/unit1/tools>)

[Messages and Special Tokens](<#messages-and-special-tokens>)[Messages: The Underlying System of LLMs](<#messages-the-underlying-system-of-llms>)[System Messages](<#system-messages>)[Conversations: User and Assistant Messages](<#conversations-user-and-assistant-messages>)[Chat-Templates](<#chat-templates>)[Base Models vs. Instruct Models](<#base-models-vs-instruct-models>)[Understanding Chat Templates](<#understanding-chat-templates>)[Messages to prompt](<#messages-to-prompt>)
