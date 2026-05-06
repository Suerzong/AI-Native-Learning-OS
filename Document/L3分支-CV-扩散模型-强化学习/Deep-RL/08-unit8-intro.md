Deep RL Course documentation

Introduction

# Deep RL Course

🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseDeep RL CourseDiffusion CourseLLM CourseMCP CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

EN

[ ](https://github.com/huggingface/deep-rl-class)

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

#  Introduction

![Unit 8](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit9/thumbnail.png)

In Unit 6, we learned about Advantage Actor Critic (A2C), a hybrid architecture combining value-based and policy-based methods that helps to stabilize the training by reducing the variance with:

  * _An Actor_ that controls **how our agent behaves** (policy-based method).
  * _A Critic_ that measures **how good the action taken is** (value-based method).

Today we’ll learn about Proximal Policy Optimization (PPO), an architecture that **improves our agent’s training stability by avoiding policy updates that are too large**. To do that, we use a ratio that indicates the difference between our current and old policy and clip this ratio to a specific range[1−ϵ,1+ϵ] [1 - \epsilon, 1 + \epsilon] [1−ϵ,1+ϵ] .

Doing this will ensure **that our policy update will not be too large and that the training is more stable.**

This Unit is in two parts:

  * In this first part, you’ll learn the theory behind PPO and code your PPO agent from scratch using the [CleanRL](https://github.com/vwxyzjn/cleanrl) implementation. To test its robustness you’ll use LunarLander-v2. LunarLander-v2 **is the first environment you used when you started this course**. At that time, you didn’t know how PPO worked, and now, **you can code it from scratch and train it. How incredible is that 🤩**.
  * In the second part, we’ll get deeper into PPO optimization by using [Sample-Factory](https://samplefactory.dev/) and train an agent playing vizdoom (an open source version of Doom).

![Environment](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit10/environments.png) These are the environments you're going to use to train your agents: VizDoom environments

Sound exciting? Let’s get started! 🚀

[ Update on GitHub](https://github.com/huggingface/deep-rl-class/blob/main/units/en/unit8/introduction.mdx)

[←Additional Readings](/learn/deep-rl-course/unit7/additional-readings) [The intuition behind PPO→](/learn/deep-rl-course/unit8/intuition-behind-ppo)
