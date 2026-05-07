Deep RL Course documentation

Deep Q-Learning

# Deep RL Course

## Deep Q-Learning

在上一单元中，我们学习了第一个强化学习算法：Q-Learning，**从头实现了它**，并在两个环境 FrozenLake-v1 和 Taxi-v3 中训练了它。

这个简单算法取得了出色的结果，但这些环境相对简单，因为**状态空间是离散且较小的**（FrozenLake-v1 有 16 个不同状态，Taxi-v3 有 500 个）。相比之下，Atari 游戏的状态空间可以**包含 10^9 到 10^11 个状态**。

正如我们将看到的，在大规模状态空间环境中，生成和更新 **Q 表可能变得低效**。

因此在本单元中，**我们将学习第一个深度强化学习智能体**：Deep Q-Learning。Deep Q-Learning 使用神经网络代替 Q 表，接收状态并基于该状态近似每个动作的 Q 值。

我们**将使用 RL-Zoo 训练它来玩 Space Invaders 和其他 Atari 环境**。

让我们开始吧！
