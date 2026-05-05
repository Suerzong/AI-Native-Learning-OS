# skill-map: reinforcement-learning — 强化学习（Q-Learning、SARSA、DQN）

## 目标

理解强化学习的基本框架和核心算法，能实现简单的 Q-Learning，理解深度强化学习（DQN）的思路。

## 必知概念

### 强化学习框架
- **Agent（智能体）**：做决策的主体
- **Environment（环境）**：Agent 与之交互的外部世界
- **State（状态）**：环境的当前描述
- **Action（动作）**：Agent 可以执行的操作
- **Reward（奖励）**：Agent 执行动作后获得的反馈
- **Policy（策略）**：状态到动作的映射 π(s) -> a
- **目标**：找到使累积奖励最大的策略

### 马尔可夫决策过程（MDP）
- **状态转移**：P(s'|s, a) — 在状态 s 执行动作 a 后转移到 s' 的概率
- **折扣因子 gamma**：控制未来奖励的重要性（0~1）
- **回报（Return）**：G_t = r_t + gamma * r_{t+1} + gamma^2 * r_{t+2} + ...

### 探索与利用（Exploration vs Exploitation）
- **利用（Exploitation）**：选择当前已知最优的动作
- **探索（Exploration）**：尝试新的动作以发现更好的策略
- **Epsilon-Greedy**：以 epsilon 概率随机探索，1-epsilon 概率利用
- **UCB（Upper Confidence Bound）**：考虑不确定性的选择策略

### Q-Learning
- **Q 函数**：Q(s, a) — 在状态 s 执行动作 a 的长期价值
- **更新公式**：Q(s,a) = Q(s,a) + alpha * [r + gamma * max(Q(s',a')) - Q(s,a)]
- **特点**：Off-policy（学习的策略和行为的策略可以不同）
- **Q-Table**：存储所有状态-动作对的 Q 值

### SARSA
- **更新公式**：Q(s,a) = Q(s,a) + alpha * [r + gamma * Q(s',a') - Q(s,a)]
- **特点**：On-policy（学习的策略就是行为的策略）
- **与 Q-Learning 的区别**：Q-Learning 用 max(Q(s',*))，SARSA 用实际选择的 Q(s',a')

### DQN（Deep Q-Network）
- **核心思想**：用神经网络替代 Q-Table
- **经验回放（Experience Replay）**：存储经验 (s, a, r, s')，随机采样训练
- **目标网络（Target Network）**：单独的网络计算目标值，定期更新
- **解决的问题**：Q-Table 在状态空间大时不可行

## 必知概念对比

| 特性 | Q-Learning | SARSA | DQN |
|------|------------|-------|-----|
| 策略 | Off-policy | On-policy | Off-policy |
| 存储 | Q-Table | Q-Table | 神经网络 |
| 更新目标 | max Q(s',a') | Q(s',a') | 神经网络预测 |
| 适用场景 | 小状态空间 | 小状态空间 | 大状态空间 |

## 常见错误

1. **Q 值更新公式写错**
   ```python
   # 错误：gamma 位置不对
   Q[s][a] = Q[s][a] + alpha * (r + gamma * np.max(Q[s_next]) - Q[s][a])

   # 正确的公式
   Q[s][a] = Q[s][a] + alpha * (r + gamma * np.max(Q[s_next]) - Q[s][a])
   ```

2. **边界处理错误**
   ```python
   # 在网格边缘向上移动时越界
   if action == UP:
       s_next = s - width  # 可能 < 0

   # 应该检查边界
   if action == UP and s >= width:
       s_next = s - width
   else:
       s_next = s  # 保持不动
   ```

3. **没有处理终止状态**
   ```python
   # 错误：终止状态也计算 Q 值更新
   if done:
       Q[s][a] = Q[s][a] + alpha * (r + gamma * np.max(Q[s_next]) - Q[s][a])
       # 终止状态没有后续状态！

   # 正确
   if done:
       Q[s][a] = Q[s][a] + alpha * (r - Q[s][a])
   ```

## 训练阶梯

### Step 1: RL 框架理解（Level 0→1）
- 理解 Agent-Environment 交互
- 画出 RL 交互循环图
- 举出 RL 的应用场景

### Step 2: Epsilon-Greedy（Level 1→2）
- 实现 Epsilon-Greedy 策略
- 理解探索-利用权衡
- 观察 epsilon 对学习的影响

### Step 3: Q-Learning（Level 2→3）
- 手动走一遍 Q 值更新
- 实现 Q-Table
- 在简单环境中验证

### Step 4: SARSA（Level 3）
- 理解与 Q-Learning 的区别
- 对比两种算法的行为差异
- 理解 on-policy vs off-policy

### Step 5: DQN（Level 3→4）
- 理解用神经网络替代 Q-Table
- 理解经验回放的作用
- 了解 DQN 在 Atari 游戏中的应用

### Step 6: 实际应用（Level 4→5）
- 设计合适的奖励函数
- 处理连续状态空间
- 考虑嵌入式设备上的 RL 部署

## 掌握标准

- **Level 3**: 能实现 Q-Learning 算法，能在简单环境中找到最优策略
- **Level 4**: 理解 SARSA、DQN 的原理，能设计 RL 问题
- **Level 5**: 能在实际场景中应用 RL，能考虑嵌入式部署的限制

## 参考资料

- materials/noob/035_ml-basic-framework-of-reinforcement-learning.md
- materials/noob/036_ml-exploration-exploitation.md
- materials/noob/037_ml-qlearning-sarsa.md
- materials/noob/038_ml-deep-reinforcement-learning.md
- materials/noob/058_ml-reinforcement-learning.md
