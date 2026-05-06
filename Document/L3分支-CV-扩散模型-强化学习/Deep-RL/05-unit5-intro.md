Deep RL Course documentation

An Introduction to Unity ML-Agents

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

#  An Introduction to Unity ML-Agents

![thumbnail](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit7/thumbnail.png)

One of the challenges in Reinforcement Learning is **creating environments**. Fortunately for us, we can use game engines to do so. These engines, such as [Unity](https://unity.com/), [Godot](https://godotengine.org/) or [Unreal Engine](https://www.unrealengine.com/), are programs made to create video games. They are perfectly suited for creating environments: they provide physics systems, 2D/3D rendering, and more.

One of them, [Unity](https://unity.com/), created the [Unity ML-Agents Toolkit](https://github.com/Unity-Technologies/ml-agents), a plugin based on the game engine Unity that allows us **to use the Unity Game Engine as an environment builder to train agents**. In the first bonus unit, this is what we used to train Huggy to catch a stick!

![MLAgents environments](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit5/example-envs.png) Source: [ML-Agents documentation](https://github.com/Unity-Technologies/ml-agents)

Unity ML-Agents Toolkit provides many exceptional pre-made environments, from playing football (soccer), learning to walk, and jumping over big walls.

In this Unit, we’ll learn to use ML-Agents, but **don’t worry if you don’t know how to use the Unity Game Engine** : you don’t need to use it to train your agents.

So, today, we’re going to train two agents:

  * The first one will learn to **shoot snowballs onto a spawning target**.
  * The second needs to **press a button to spawn a pyramid, then navigate to the pyramid, knock it over, and move to the gold brick at the top**. To do that, it will need to explore its environment, which will be done using a technique called curiosity.

![Environments](https://huggingface.co/datasets/huggingface-deep-rl-course/course-images/resolve/main/en/unit7/envs.png)

Then, after training, **you’ll push the trained agents to the Hugging Face Hub** , and you’ll be able to **visualize them playing directly on your browser without having to use the Unity Editor**.

Doing this Unit will **prepare you for the next challenge: AI vs. AI where you will train agents in multi-agents environments and compete against your classmates’ agents**.

Sound exciting? Let’s get started!

[ Update on GitHub](https://github.com/huggingface/deep-rl-class/blob/main/units/en/unit5/introduction.mdx)

[←Additional Readings](/learn/deep-rl-course/unit4/additional-readings) [How ML-Agents works?→](/learn/deep-rl-course/unit5/how-mlagents-works)
