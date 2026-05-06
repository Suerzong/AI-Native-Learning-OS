Deep RL Course documentation

Deep Q-Learning

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

#  Deep Q-Learning

![Unit 3 thumbnail](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit4/thumbnail.jpg)

In the last unit, we learned our first reinforcement learning algorithm: Q-Learning, **implemented it from scratch** , and trained it in two environments, FrozenLake-v1 ☃️ and Taxi-v3 🚕.

We got excellent results with this simple algorithm, but these environments were relatively simple because the **state space was discrete and small** (16 different states for FrozenLake-v1 and 500 for Taxi-v3). For comparison, the state space in Atari games can **contain 10910^{9}109 to101110^{11}1011 states**.

But as we’ll see, producing and updating a **Q-table can become ineffective in large state space environments.**

So in this unit, **we’ll study our first Deep Reinforcement Learning agent** : Deep Q-Learning. Instead of using a Q-table, Deep Q-Learning uses a Neural Network that takes a state and approximates Q-values for each action based on that state.

And **we’ll train it to play Space Invaders and other Atari environments using[RL-Zoo](https://github.com/DLR-RM/rl-baselines3-zoo)**, a training framework for RL using Stable-Baselines that provides scripts for training, evaluating agents, tuning hyperparameters, plotting results, and recording videos.

![Environments](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit4/atari-envs.gif)

So let’s get started! 🚀

[ Update on GitHub](https://github.com/huggingface/deep-rl-class/blob/main/units/en/unit3/introduction.mdx)

[←Additional Readings](/learn/deep-rl-course/unit2/additional-readings) [From Q-Learning to Deep Q-Learning→](/learn/deep-rl-course/unit3/from-q-to-dqn)
