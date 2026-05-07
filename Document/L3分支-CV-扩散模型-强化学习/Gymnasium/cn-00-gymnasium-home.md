![Gymnasium Logo](_images/gymnasium-text.png)

##  强化学习的 API 标准，提供多样化的参考环境集合

[![Lunar Lander](_images/lunar_lander.gif) ](_images/lunar_lander.gif)

**Gymnasium 是 OpenAI Gym 库的维护分支。** Gymnasium 接口简单、Pythonic，能够表示通用 RL 问题，并提供了从旧 Gym 环境的[迁移指南](introduction/migration_guide/)：


    import gymnasium as gym

    # 初始化环境
    env = gym.make("LunarLander-v3", render_mode="human")

    # 重置环境以生成第一个观测
    observation, info = env.reset(seed=42)
    for _ in range(1000):
        # 这里可以插入你的策略
        action = env.action_space.sample()

        # 在环境中执行动作（状态转移）
        # 接收下一个观测、奖励以及 episode 是否终止或截断
        observation, reward, terminated, truncated, info = env.step(action)

        # 如果 episode 结束，则重置以开始新的 episode
        if terminated or truncated:
            observation, info = env.reset()

    env.close()
