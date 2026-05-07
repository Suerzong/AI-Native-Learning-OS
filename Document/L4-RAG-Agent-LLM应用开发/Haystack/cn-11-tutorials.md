[![Haystack](/images/logos/haystack.png)](</>)

  * 概览
    * [ 什么是 Haystack？ ](</overview/intro>)
    * [ 快速入门 ](</overview/quick-start>)
    * [ 演示 ](</overview/demo>)
  * [ 文档 ](<https://docs.haystack.deepset.ai/docs>)
  * 学习
    * [ 教程与实践指南 ](</tutorials>)
    * [ Cookbook ](</cookbook>)
    * [ 实验 ](<https://github.com/deepset-ai/haystack-experimental>)
    * [ 发布说明 ](</release-notes>)
    * [ DataCamp 新课程：构建 AI Agent ](<https://app.datacamp.com/learn/courses/building-ai-agents-with-haystack>)
    * [ DeepLearning.AI：构建 AI 应用 ](<https://www.deeplearning.ai/short-courses/building-ai-applications-with-haystack/>)
  * [ 集成 ](</integrations>)
  * [ 博客 ](</blog>)
  * Haystack Enterprise
    * [ 注册 Haystack Enterprise 试用 ](<https://www.deepset.ai/deepset-studio>)
    * [ Haystack Enterprise 平台 ](<https://www.deepset.ai/products-and-services/deepset-ai-platform>)
    * [ Haystack Enterprise 博客 ](<https://www.deepset.ai/blog>)
    * [ 招聘 ](<https://www.deepset.ai/careers>)
[ 获取企业支持 ](<https://www.deepset.ai/products-and-services/haystack-enterprise>) [ 快速入门 ](</overview/quick-start>)

# 教程

无论你是初学者还是有经验的用户，这些教程都将引导你了解 Haystack 的功能和特性，让你轻松理解和实现它们。 [ 贡献 ](<https://github.com/deepset-ai/haystack-tutorials/blob/main/Contributing.md#contributing-to-haystack-tutorials>)

## 22 个面向所有级别的教程和实践指南

所有级别 初学者 中级 高级 重置过滤器 排序方式：级别 最后更新 最新 重置过滤器

  * [ 完整实践指南：评估 ](</tutorials/guide_evaluation/>) 学习关于评估的一切内容的引导式实践指南
  * [ 初学者 10 分钟 精选 ] 创建你的第一个带检索增强的问答管道 使用 OpenAI GPT 模型构建你的第一个生成式 QA 管道 (</tutorials/27_first_rag_pipeline/>)
  * [ 初学者 10 分钟 精选 ] 构建工具调用 Agent 学习如何创建一个可以使用网页搜索工具回答问题的 Agent (</tutorials/43_building_a_tool_calling_agent/>)
  * [ 高级 20 分钟 精选 ] 使用 InMemoryChatMessageStore 的对话式 RAG Agent 学习如何使用对话历史进行 RAG，以实现基于文档的多轮对话 (</tutorials/48_conversational_rag/>)
  * [ 高级 20 分钟 精选 ] Haystack Agent 的人机交互 学习如何使用确认策略在工具执行前获取用户输入，以实现更安全、更可控的 AI 系统 (</tutorials/47_human_in_the_loop_agent/>)
  * [ 高级 20 分钟 精选 ] 使用 Haystack 创建多 Agent 系统 使用专门处理特定任务的 Agent 构建更复杂、模块化的 Agent 工作流 (</tutorials/45_creating_a_multi_agent_system/>)
  * [ 高级 20 分钟 精选 ] 创建视觉+文本 RAG 管道 构建一个多模态 RAG 管道，可以基于图像和文本来回答问题 (</tutorials/46_multimodal_rag/>)
  * [ 中级 10 分钟 精选 ] 构建带回退到网页搜索的 Agentic RAG 学习如何在必要时将查询路由到基于 Web 的 RAG 路线 (</tutorials/36_building_fallbacks_with_conditional_routing/>)
  * [ 初学者 5 分钟 ] 使用元数据过滤文档 学习如何在检索时使用元数据过滤到特定文档 (</tutorials/31_metadata_filtering/>)
  * [ 初学者 15 分钟 ] 预处理不同类型的文件 学习如何构建基于文件类型预处理文件的索引管道 (</tutorials/30_file_type_preprocessing_index_pipeline/>)
  * [ 中级 20 分钟 ] 创建自定义 SuperComponents 学习如何使用 @super_component 装饰器创建带有输入和输出映射的自定义 SuperComponents (</tutorials/44_creating_custom_supercomponents/>)
  * [ 初学者 10 分钟 ] 嵌入元数据以改善检索 学习如何在索引时嵌入元数据，以提高检索结果的质量 (</tutorials/39_embedding_metadata_for_improved_retrieval/>)
  * [ 初学者 10 分钟 ] 序列化 LLM 管道 学习如何在 YAML 和 Python 之间序列化和反序列化你的管道 (</tutorials/29_serializing_pipelines/>)
  * [ 高级 20 分钟 ] 使用 TurboQuant 和 Haystack 压缩 KV 缓存 使用 TurboQuant KV 缓存压缩在消费级 GPU 上运行大型 LLM，显著减少内存使用 (</tutorials/49_turboquant_quantization_with_huggingface/>)
  * [ 初学者 10 分钟 ] 构建抽取式 QA 管道 学习如何构建一个使用抽取式模型来显示查询答案位置的 Haystack 管道 (</tutorials/34_extractive_qa_pipeline/>)
  * [ 中级 15 分钟 ] 创建混合检索管道 学习如何组合基于关键词的检索和稠密检索以增强检索效果 (</tutorials/33_hybrid_retrieval/>)
  * [ 初学者 10 分钟 ] 使用 OpenAI 生成结构化输出 学习如何使用 Pydantic 模型或 JSON schema 通过 OpenAI 模型生成结构化输出 (</tutorials/28_structured_output_with_openai/>)
  * [ 中级 15 分钟 ] 按语言分类文档和查询 学习如何按语言分类文档和路由查询，适用于索引和 RAG 管道 (</tutorials/32_classifying_documents_and_queries_by_language/>)
  * [ 中级 15 分钟 ] 评估 RAG 管道 学习如何使用统计和基于模型的评估指标评估你的 RAG 管道 (</tutorials/35_evaluating_rag_pipelines/>)
  * [ 高级 20 分钟 ] 构建带函数调用的聊天 Agent 学习如何使用 OpenAI 函数调用构建具有 Agent 行为的聊天应用 (</tutorials/40_building_chat_application_with_function_calling/>)
  * [ 初学者 10 分钟 ] 检索句子周围的上下文窗口 学习如何使用 SentenceWindowRetriever 检索上下文窗口 (</tutorials/42_sentence_window_retriever/>)
  * [ 中级 25 分钟 ] 使用 TransformersTextRouter 和 TransformersZeroShotTextRouter 进行查询分类 学习如何使用分类模型路由用户问题和其他文本输入 (</tutorials/41_query_classification_with_transformerstextrouter_and_transformerszeroshottextrouter/>)

## 想在 GitHub 上贡献？

我们在 GitHub 上的开源仓库中维护这些教程。如果你想贡献，请前往仓库提交编辑或建议新教程。 [ 贡献 ](<https://github.com/deepset-ai/haystack-tutorials/blob/main/Contributing.md#contributing-to-haystack-tutorials>)

## 在找教程？

输入关键词然后点击「搜索」按钮，我们将搜索所有教程。

## 未找到结果

你可以尝试不同的关键词或检查可能的拼写错误。

## 发生了错误

请稍后重试。

Powered by [ ![deepset](/images/logos/deepset.png) ](<https://www.deepset.ai/>) 使用智能上下文工程构建自定义 AI Agent 和 RAG 应用，由开源 AI 编排驱动。 © 2026 deepset GmbH. 保留所有权利。

  * 社区
  * [活动](<https://luma.com/haystack>)
  * [GitHub 讨论](<https://github.com/deepset-ai/haystack/discussions>)
  * [Discord](<https://discord.com/invite/xYvH6drSmA>)
  * [Hugging Face](<https://huggingface.co/deepset>)

  * 资源
  * [文档](<https://docs.haystack.deepset.ai/docs/intro>)
  * [教程](</tutorials>)
  * [Cookbook](</cookbook>)
  * [发布说明](</release-notes>)
  * [实验](<https://github.com/deepset-ai/haystack-experimental>)

  * 公司
  * [关于](<https://www.deepset.ai/about>)
  * [招聘](<https://www.deepset.ai/careers>)

© 2026 deepset GmbH. 保留所有权利。
