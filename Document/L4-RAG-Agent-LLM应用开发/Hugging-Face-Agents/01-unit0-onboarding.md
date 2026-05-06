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

Onboarding: Your First Steps ⛵

# Agents Course

🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseDeep RL CourseDiffusion CourseLLM CourseMCP CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

ENESFRKORU-RUVIZH-CN

[ ](<https://github.com/huggingface/agents-course>)

Unit 0. Welcome to the course

[Welcome to the course 🤗](</learn/agents-course/unit0/introduction>)[Onboarding](</learn/agents-course/unit0/onboarding>)[(Optional) Discord 101](</learn/agents-course/unit0/discord101>)

Live 1. How the course works and Q&A;

Unit 1. Introduction to Agents

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

# [](<#onboarding-your-first-steps->) Onboarding: Your First Steps ⛵

![Time to Onboard](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit0/time-to-onboard.jpg)

Now that you have all the details, let’s get started! We’re going to do four things:

  1. **Create your Hugging Face Account** if it’s not already done
  2. **Sign up to Discord and introduce yourself** (don’t be shy 🤗)
  3. **Follow the Hugging Face Agents Course** on the Hub
  4. **Spread the word** about the course

### [](<#step-1-create-your-hugging-face-account>) Step 1: Create Your Hugging Face Account

(If you haven’t already) create a Hugging Face account [here](<https://huggingface.co/join>).

### [](<#step-2-join-our-discord-community>) Step 2: Join Our Discord Community

👉🏻 Join our discord server [here.](<https://discord.gg/UrrTSsSyjb>)

When you join, remember to introduce yourself in `#introduce-yourself`.

Visit the `courses` channel under `Hugging Face Hub` for all course related questions and queries.

If this is your first time using Discord, we wrote a Discord 101 to get the best practices. Check [the next section](<discord101>).

### [](<#step-3-follow-the-hugging-face-agent-course-organization>) Step 3: Follow the Hugging Face Agent Course Organization

Stay up to date with the latest course materials, updates, and announcements **by following the Hugging Face Agents Course Organization**.

👉 Go [here](<https://huggingface.co/agents-course>) and click on **follow**.

![Follow](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/hf_course_follow.gif)

### [](<#step-4-spread-the-word-about-the-course>) Step 4: Spread the word about the course

Help us make this course more visible! There are two ways you can help us:

  1. Show your support by ⭐ [the course’s repository](<https://github.com/huggingface/agents-course>).

![Repo star](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/please_star.gif)

  2. Share Your Learning Journey: Let others **know you’re taking this course**! We’ve prepared an illustration you can use in your social media posts

![](https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/share.png)

You can download the image by clicking 👉 [here](<https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/share.png?download=true>)

### [](<#step-5-running-models-locally-with-ollama-in-case-you-run-into-credit-limits>) Step 5: Running Models Locally with Ollama (In case you run into Credit limits)

  1. **Install Ollama**

Follow the official Instructions [here.](<https://ollama.com/download>)

  2. **Pull a model Locally**

Copied

         ollama pull qwen2:7b

Here, we pull the [qwen2:7b model](<https://ollama.com/library/qwen2:7b>). Check out [the ollama website](<https://ollama.com/search>) for more models.

  3. **Start Ollama in the background (In one terminal)**

Copied

         ollama serve

If you run into the error “listen tcp 127.0.0.1:11434: bind: address already in use”, you can use command `sudo lsof -i :11434` to identify the process ID (PID) that is currently using this port. If the process is `ollama`, it is likely that the installation script above has started ollama service, so you can skip this command to start Ollama.

  4. **Use`LiteLLMModel` Instead of `InferenceClientModel`**

To use `LiteLLMModel` module in `smolagents`, you may run `pip` command to install the module.

Copied

        pip install 'smolagents[litellm]'

Copied

        from smolagents import LiteLLMModel

        model = LiteLLMModel(
            model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
            api_base="http://127.0.0.1:11434",  # Default Ollama local server
            num_ctx=8192,
        )

  5. **Why this works?**

  * Ollama serves models locally using an OpenAI-compatible API at `http://localhost:11434`.
  * `LiteLLMModel` is built to communicate with any model that supports the OpenAI chat/completion API format.
  * This means you can simply swap out `InferenceClientModel` for `LiteLLMModel` no other code changes required. It’s a seamless, plug-and-play solution.

Congratulations! 🎉 **You’ve completed the onboarding process**! You’re now ready to start learning about AI Agents. Have fun!

Keep Learning, stay awesome 🤗

[ Update on GitHub](<https://github.com/huggingface/agents-course/blob/main/units/en/unit0/onboarding.mdx>)

[←Welcome to the course 🤗](</learn/agents-course/unit0/introduction>) [(Optional) Discord 101→](</learn/agents-course/unit0/discord101>)

[Onboarding: Your First Steps ⛵](<#onboarding-your-first-steps->)[Step 1: Create Your Hugging Face Account](<#step-1-create-your-hugging-face-account>)[Step 2: Join Our Discord Community](<#step-2-join-our-discord-community>)[Step 3: Follow the Hugging Face Agent Course Organization](<#step-3-follow-the-hugging-face-agent-course-organization>)[Step 4: Spread the word about the course](<#step-4-spread-the-word-about-the-course>)[Step 5: Running Models Locally with Ollama (In case you run into Credit limits)](<#step-5-running-models-locally-with-ollama-in-case-you-run-into-credit-limits>)
