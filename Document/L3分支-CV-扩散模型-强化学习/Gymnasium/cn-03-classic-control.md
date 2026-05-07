# 经典控制

可以通过以下方式安装此环境集的依赖：

    pip install gymnasium[classic-control]

有五个经典控制环境：Acrobot、CartPole、Mountain Car、Continuous Mountain Car 和 Pendulum。所有这些环境的初始状态在其给定范围内是随机的。此外，Acrobot 的动作会附加噪声。对于两个 Mountain Car 环境，汽车的动力不足以爬上山顶，因此需要一些努力才能到达顶部。

在 Gymnasium 环境中，这组环境可以被认为是相对容易用策略解决的环境。

所有环境都可以通过每个环境文档中指定的参数进行高度配置。
