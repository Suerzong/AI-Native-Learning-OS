# 任务生成规则

任务必须服务于当前最小薄弱点。每个任务前必须先给出足够完成任务的知识点讲解，不能直接把学习者丢进题目。

## 任务前知识讲解

生成任务前，先生成"本次知识点"。它必须回答：

- 这个知识点在 TensorFlow/Keras 中对应什么 API 或代码模式。
- 它背后的数学或工程原理是什么。
- tensor shape 在这一步会怎么变。
- 初学者最容易犯什么错误。
- 本次任务只要求掌握到什么边界。

如果学习者等级是 0-2，知识讲解必须先用直观语言解释，再给 API 签名和代码。
如果学习者等级是 3-5，可以减少基础解释，但仍要说明本次任务依赖的关键知识和 shape 变化。

## 任务类型

| 类型 | 作用 | 示例 |
|---|---|---|
| 识别题 | 建立 API 地图 | 找到 TensorFlow 中创建 tensor 的函数有哪些 |
| 解释题 | 建立理解 | 解释 Eager Execution 和 Graph Execution 的区别 |
| Shape 预测题 | 建立形状直觉 | 预测 Conv2D 的输出 shape |
| 修改题 | 形成操作能力 | 修改 Sequential 模型的层结构 |
| API 编写题 | 形成 API 调用能力 | 写出正确构建 tf.data pipeline 的代码 |
| 代码编写题 | 形成完整代码能力 | 从零写出 Keras 模型训练流程 |
| 调试题 | 形成排错能力 | 找出 dtype 不匹配错误 |
| 迁移题 | 检查泛化 | 把 MNIST 模型迁移到 CIFAR-10 |
| 对比题 | 加深框架理解 | 对比 TensorFlow 和 PyTorch 实现同一功能的差异 |
| 部署题 | 检查端到端能力 | 完成 SavedModel → TF Lite 转换 |
| 小项目 | 组合技能 | 完整图像分类项目（含部署） |

## 好任务的格式

```md
## 任务名称

- 本次知识点：
- 目标技能：
- 起始材料：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 复测问题：
```

## Shape 预测题格式

```md
## 任务名称

- 目标技能：预测 X 操作后的 tensor shape
- 输入 tensor：shape 为 (a, b, c)
- 操作：具体操作描述
- 要求：不运行代码，写出输出 shape
- 必须写出的推理过程：
- 常见错误：
```

## API 编写题格式

```md
## 任务名称

- 目标函数：
- 函数签名：
- 参数说明：
- 返回值：
- 写出调用的要求：
- 常见错误：
```

## 难度控制

- 如果学习者等级是 0-1：给识别题和解释题，不要求写代码。
- 如果学习者等级是 2：给小修改题和 Shape 预测题，可以参考代码完成。
- 如果学习者等级是 3：给 API 编写题和调试题，要求不看文档写出正确调用。
- 如果学习者等级是 4：给迁移题和代码编写题，要求从零写完整代码。
- 如果学习者等级是 5：给小项目和部署题（多模块协同）。

## TensorFlow 特有的任务设计原则

1. **每个任务必须包含 shape 追踪**：让学习者在每一步标注 tensor shape。
2. **先预测再运行**：要求学习者先在纸上写结果，再用代码验证。
3. **错误驱动学习**：故意给有 bug 的代码，让学习者读错误信息并修复。
4. **从简单到复杂**：先练单个 API，再组合成训练流程，再组合成完整项目。
5. **部署意识**：从第二层开始就问"这个模型怎么转成 TF Lite 给嵌入式用"。
6. **对比学习**：如果学习者有 PyTorch 经验，适时用对比题加深理解（如 tf.data vs DataLoader）。
7. **Keras 优先**：优先使用 Keras 高级 API 降低门槛，仅在需要自定义时使用低级 API（GradientTape）。

## TensorFlow-PyTorch 对照参考

当学习者有 PyTorch 基础时，可用以下对照辅助理解：

| 功能 | PyTorch | TensorFlow/Keras |
|------|---------|-----------------|
| 创建 tensor | `torch.tensor()` | `tf.constant()` |
| 可变 tensor | `torch.tensor().requires_grad_()` | `tf.Variable()` |
| 自动求导 | `autograd` / `backward()` | `tf.GradientTape()` |
| 模型定义 | `nn.Module` 子类 | `tf.keras.Model` 或 Sequential |
| 训练循环 | 手写 loop | `model.fit()` 或自定义 loop |
| 数据加载 | `DataLoader` + `Dataset` | `tf.data.Dataset` |
| 模型保存 | `torch.save(state_dict)` | `model.save()` (SavedModel) |
| 端侧格式 | ONNX → NCNN/MNN | TF Lite |
