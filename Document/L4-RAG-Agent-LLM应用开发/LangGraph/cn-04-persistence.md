# 持久化（Persistence）

LangGraph 内置持久化层，将图状态保存为检查点（Checkpoints）。当你使用检查点器编译图时，图状态的快照会在执行的每一步保存，组织到线程（Threads）中。这使人机协作工作流、对话记忆、时间旅行调试和容错执行成为可能。

## 为什么要用持久化

持久化是以下功能所必需的：

  * **人机协作**：检查点器通过允许人类检查、中断和批准图步骤来促进人机协作工作流。
  * **记忆**：检查点器允许交互之间的"记忆"。后续消息可以发送到同一线程，该线程保留对之前消息的记忆。
  * **时间旅行**：检查点器允许"时间旅行"，让用户重放先前的图执行以审查和调试。还可以在任意检查点分叉图状态以探索替代轨迹。
  * **容错**：检查点提供容错和错误恢复能力。

## 核心概念

### 线程（Threads）

线程是分配给检查点器保存的每个检查点的唯一 ID。它包含一系列运行的累积状态。调用图时，必须在配置中指定 `thread_id`：

    {"configurable": {"thread_id": "1"}}

### 检查点（Checkpoints）

线程在特定时间点的状态称为检查点。检查点是在每个超步（Super-step）保存的图状态快照，由 `StateSnapshot` 对象表示。

### 超步（Super-steps）

LangGraph 在每个超步边界创建检查点。超步是图的单个"滴答"，该步骤中调度的所有节点执行（可能并行）。

## 获取和更新状态

### 获取状态

    # 获取最新状态快照
    config = {"configurable": {"thread_id": "1"}}
    graph.get_state(config)

### 获取状态历史

    config = {"configurable": {"thread_id": "1"}}
    list(graph.get_state_history(config))

### 重放（Replay）

重放从先前的检查点重新执行步骤。使用先前的 `checkpoint_id` 调用图以重新运行该检查点后的节点。

### 更新状态

使用 `update_state` 编辑图状态。这创建一个具有更新值的新检查点——不会修改原始检查点。

## 内存存储（Memory Store）

状态模式指定一组在图执行过程中填充的键。检查点器将状态写入线程，实现状态持久化。要在**线程之间**保留信息，需要使用 `Store` 接口。

    from langgraph.store.memory import InMemoryStore
    store = InMemoryStore()

    user_id = "1"
    namespace = (user_id, "memories")
    store.put(namespace, memory_id, {"food_preference": "I like pizza"})

    # 搜索记忆
    memories = store.search(namespace)

### 语义搜索

存储支持语义搜索，允许你根据含义而非精确匹配查找记忆：

    store = InMemoryStore(index={"embed": embeddings, "dims": 1536})
    memories = store.search(namespace, query="What does the user like to eat?")

## 检查点库

  * `langgraph-checkpoint`：基础接口，包含内存检查点器 `InMemorySaver`
  * `langgraph-checkpoint-sqlite`：基于 SQLite 的检查点器
  * `langgraph-checkpoint-postgres`：基于 PostgreSQL 的检查点器，用于生产环境
