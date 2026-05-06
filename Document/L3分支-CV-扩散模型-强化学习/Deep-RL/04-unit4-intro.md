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

![thumbnail](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit6/thumbnail.png)

In the last unit, we learned about Deep Q-Learning. In this value-based deep reinforcement learning algorithm, we **used a deep neural network to approximate the different Q-values for each possible action at a state.**

Since the beginning of the course, we have only studied value-based methods, **where we estimate a value function as an intermediate step towards finding an optimal policy.**

![Link value policy](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit3/link-value-policy.jpg)

In value-based methods, the policy **(π) only exists because of the action value estimates since the policy is just a function** (for instance, greedy-policy) that will select the action with the highest value given a state.

With policy-based methods, we want to optimize the policy directly **without having an intermediate step of learning a value function.**

So today, **we’ll learn about policy-based methods and study a subset of these methods called policy gradient**. Then we’ll implement our first policy gradient algorithm called Monte Carlo **Reinforce** from scratch using PyTorch. Then, we’ll test its robustness using the CartPole-v1 and PixelCopter environments.

You’ll then be able to iterate and improve this implementation for more advanced environments.

![Environments](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit6/envs.gif)

Let’s get started!

[ Update on GitHub](https://github.com/huggingface/deep-rl-class/blob/main/units/en/unit4/introduction.mdx)

[←Hands-on](/learn/deep-rl-course/unitbonus2/hands-on) [What are the policy-based methods?→](/learn/deep-rl-course/unit4/what-are-policy-based-methods)
