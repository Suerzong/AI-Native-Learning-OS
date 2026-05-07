# 基本用法

## 什么是强化学习？

在深入了解 Gymnasium 之前，让我们先理解我们要实现的目标。强化学习就像通过试错教学——智能体通过尝试动作、接收反馈（奖励）并逐渐改进行为来学习。就像用零食训练宠物、通过练习学骑自行车或反复玩游戏来掌握视频游戏一样。

关键在于我们不会直接告诉智能体该做什么。相反，我们创建一个环境，让它可以安全地实验并从行为的后果中学习。

## 为什么选择 Gymnasium？

无论你想训练智能体玩游戏、控制机器人还是优化交易策略，Gymnasium 都为你提供了构建和测试想法的工具。Gymnasium 的核心是提供所有单智能体强化学习环境的 API，并实现常见环境：cartpole、pendulum、mountain-car、mujoco、atari 等。

Gymnasium 的核心是 `Env`，一个高级 Python 类，表示强化学习理论中的马尔可夫决策过程（MDP）。该类为用户提供开始新 episode、执行动作和可视化智能体当前状态的能力。

## 初始化环境

在 Gymnasium 中初始化环境非常简单，可以通过 `make()` 函数完成：


    import gymnasium as gym

    # 创建一个适合初学者的简单环境
    env = gym.make('CartPole-v1')


## 理解智能体-环境循环

在强化学习中，经典的「智能体-环境循环」表示学习如何发生：

  1. **智能体观察**当前情况（就像看游戏屏幕）
  2. **智能体选择动作**（就像按按钮）
  3. **环境响应**新情况和奖励
  4. **重复**直到 episode 结束

## 你的第一个 RL 程序


    import gymnasium as gym

    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset()

    episode_over = False
    total_reward = 0

    while not episode_over:
        action = env.action_space.sample()  # 随机动作
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        episode_over = terminated or truncated

    print(f"Episode 结束！总奖励: {total_reward}")
    env.close()


## 动作空间和观测空间

每个环境通过 `action_space` 和 `observation_space` 属性指定有效动作和观测的格式：

- `Box`：描述具有上下限的有界空间（如连续控制或图像像素）
- `Discrete`：描述离散空间 `{0, 1, ..., n-1}`（如按钮按下）
- `MultiBinary`：描述任意 n 维形状的二元空间
- `MultiDiscrete`：由一系列不同动作数的离散空间组成
- `Dict`：描述简单空间的字典
- `Tuple`：描述简单空间的元组

## 修改环境

包装器（Wrappers）是修改现有环境的便捷方式，无需直接更改底层代码。大多数通过 `make()` 创建的环境已默认包装了 `TimeLimit`、`OrderEnforcing` 和 `PassiveEnvChecker`。

常见的包装器：
- `TimeLimit`：在超过最大步数时发出截断信号
- `ClipAction`：将动作裁剪到有效动作空间内
- `RescaleAction`：将动作重新缩放到不同范围

## 下一步

现在你已了解基础，接下来可以：
1. **训练实际智能体**——用智能替代随机动作
2. **创建自定义环境**——构建自己的 RL 问题
3. **记录智能体行为**——保存训练的视频和数据
4. **加速训练**——使用向量化环境和其他优化
