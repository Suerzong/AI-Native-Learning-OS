Deep RL Course documentation

Introduction to Q-Learning

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

#  Introduction to Q-Learning

![Unit 2 thumbnail](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit3/thumbnail.jpg)

In the first unit of this class, we learned about Reinforcement Learning (RL), the RL process, and the different methods to solve an RL problem. We also **trained our first agents and uploaded them to the Hugging Face Hub.**

In this unit, we’re going to **dive deeper into one of the Reinforcement Learning methods: value-based methods** and study our first RL algorithm: **Q-Learning.**

We’ll also **implement our first RL agent from scratch** , a Q-Learning agent, and will train it in two environments:

  1. Frozen-Lake-v1 (non-slippery version): where our agent will need to **go from the starting state (S) to the goal state (G)** by walking only on frozen tiles (F) and avoiding holes (H).
  2. An autonomous taxi: where our agent will need **to learn to navigate** a city to **transport its passengers from point A to point B.**

![Environments](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit3/envs.gif)

Concretely, we will:

  * Learn about **value-based methods**.
  * Learn about the **differences between Monte Carlo and Temporal Difference Learning**.
  * Study and implement **our first RL algorithm** : Q-Learning.

This unit is **fundamental if you want to be able to work on Deep Q-Learning** : the first Deep RL algorithm that played Atari games and beat the human level on some of them (breakout, space invaders, etc).

So let’s get started! 🚀

[ Update on GitHub](https://github.com/huggingface/deep-rl-class/blob/main/units/en/unit2/introduction.mdx)

[←Live 1. How the course work, Q&A, and playing with Huggy 🐶](/learn/deep-rl-course/live1/live1) [What is RL? A short recap→](/learn/deep-rl-course/unit2/what-is-rl)
