# 评估模块指南

评估是确保 RAG 应用质量的关键步骤。LlamaIndex 提供了多种评估工具。

## 评估类型

### 响应评估

评估 LLM 生成的响应质量：

  * **正确性（Correctness）**：响应是否正确回答了问题
  * **忠实度（Faithfulness）**：响应是否忠实于检索到的上下文
  * **相关性（Relevancy）**：响应是否与查询相关
  * **语义相似性（Semantic Similarity）**：响应与参考答案的语义相似度

### 检索评估

评估检索系统的质量：

  * **命中率（Hit Rate）**：检索到的节点中包含正确答案的比例
  * **MRR（Mean Reciprocal Rank）**：正确答案在检索结果中的排名质量

## 使用评估器

    from llama_index.core.evaluation import FaithfulnessEvaluator

    evaluator = FaithfulnessEvaluator(llm=llm)
    response = query_engine.query("What is the capital of France?")
    eval_result = evaluator.evaluate_response(response)
    print(eval_result.passing)  # True/False

## 成本分析

跟踪和优化 LLM 调用的成本：

    from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
    from llama_index.core import Settings

    token_counter = TokenCountingHandler()
    Settings.callback_manager = CallbackManager([token_counter])

    # 运行查询后查看 token 使用量
    print(f"Embedding tokens: {token_counter.total_embedding_token_count}")
    print(f"LLM prompt tokens: {token_counter.prompt_llm_token_count}")
    print(f"LLM completion tokens: {token_counter.completion_llm_token_count}")

## 标签数据集评估

使用标注数据集进行系统性评估：

    from llama_index.core.evaluation import LabelledRagDataset
    from llama_index.core.llama_dataset import LabelledEvaluatorDataset

    # 创建评估数据集
    dataset = LabelledRagDataset.from_json("eval_dataset.json")

    # 运行评估
    evaluator = CorrectnessEvaluator()
    eval_results = evaluator.evaluate_dataset(dataset)
