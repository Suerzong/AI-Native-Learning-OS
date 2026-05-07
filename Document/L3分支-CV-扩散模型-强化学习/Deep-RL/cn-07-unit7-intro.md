Deep RL Course documentation

PPO 简介

# Deep RL Course

## 简介

在第六单元中，我们学习了 Advantage Actor Critic（A2C），一种结合了基于价值和基于策略方法的混合架构。

今天我们将学习近端策略优化（Proximal Policy Optimization，PPO），一种通过**避免过大的策略更新**来提高智能体训练稳定性的架构。为此，我们使用一个比率来指示当前策略和旧策略之间的差异，并将此比率裁剪到特定范围 [1-ε, 1+ε]。

这样做将确保**策略更新不会太大，训练更加稳定**。

本单元分为两部分：

  * 在第一部分中，你将学习 PPO 的理论，并使用 CleanRL 实现从头编写你的 PPO 智能体。你将使用 LunarLander-v2 测试其鲁棒性。LunarLander-v2 是你**开始本课程时使用的第一个环境**。当时你不知道 PPO 是如何工作的，现在你可以**从头编写它并训练它**。
  * 在第二部分中，我们将使用 Sample-Factory 更深入地了解 PPO 优化，并训练一个在 VizDoom（Doom 的开源版本）中玩耍的智能体。

让我们开始吧！
