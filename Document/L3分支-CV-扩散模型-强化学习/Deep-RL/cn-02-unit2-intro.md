Deep RL Course documentation

Q-Learning 简介

# Deep RL Course

## Q-Learning 简介

在本课程的第一单元中，我们学习了强化学习（RL）、RL 流程以及解决 RL 问题的不同方法。我们还**训练了第一个智能体并将其上传到 Hugging Face Hub**。

在本单元中，我们将**深入研究强化学习方法之一：基于价值的方法（Value-Based Methods）**，并学习我们的第一个 RL 算法：**Q-Learning**。

我们还将**从头实现第一个 RL 智能体**——一个 Q-Learning 智能体，并在两个环境中训练它：

  1. Frozen-Lake-v1（非滑动版本）：智能体需要**从起始状态（S）到达目标状态（G）**，只能在冰冻瓦片（F）上行走并避开冰窟窿（H）。
  2. 自动出租车：智能体需要**学会在一个城市中导航**，将乘客从 A 点运送到 B 点。

具体来说，我们将：

  * 学习**基于价值的方法**。
  * 学习**蒙特卡洛（Monte Carlo）和时序差分（Temporal Difference）学习之间的区别**。
  * 学习并实现**第一个 RL 算法**：Q-Learning。

本单元对于后续学习 Deep Q-Learning（第一个在 Atari 游戏上达到人类水平的 Deep RL 算法）**至关重要**。

让我们开始吧！
