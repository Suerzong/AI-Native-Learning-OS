# 人机协作中断（Interrupts）

中断允许你在特定点暂停图执行，并在继续之前等待外部输入。当触发中断时，LangGraph 使用其[持久化](https://docs.langchain.com/oss/python/langgraph/persistence)层保存图状态并无限期等待，直到你恢复执行。

## 使用 `interrupt` 暂停

在节点中调用 `interrupt()` 函数暂停图执行：

    from langgraph.types import interrupt

    def approval_node(state: State):
        # 暂停并请求批准
        approved = interrupt("Do you approve this action?")
        # 恢复时，Command(resume=...) 返回该值
        return {"approved": approved}

你需要：
  1. 一个**检查点器**来持久化图状态
  2. 配置中的**线程 ID**
  3. 在要暂停的位置调用 `interrupt()`

## 恢复中断

使用包含恢复值的 `Command` 再次调用图来恢复：

    from langgraph.types import Command

    # 初始运行——命中中断并暂停
    config = {"configurable": {"thread_id": "thread-1"}}
    result = graph.invoke({"input": "data"}, config=config, version="v2")
    print(result.interrupts)

    # 使用人工响应恢复
    graph.invoke(Command(resume=True), config=config, version="v2")

## 常见模式

### 批准或拒绝

    def approval_node(state) -> Command[Literal["proceed", "cancel"]]:
        is_approved = interrupt({"question": "Do you want to proceed?", "details": state["details"]})
        if is_approved:
            return Command(goto="proceed")
        else:
            return Command(goto="cancel")

    # 批准
    graph.invoke(Command(resume=True), config=config)
    # 拒绝
    graph.invoke(Command(resume=False), config=config)

### 审查和编辑状态

    def review_node(state):
        edited_content = interrupt({"instruction": "Review and edit this content", "content": state["generated_text"]})
        return {"generated_text": edited_content}

### 工具中的中断

将中断直接放在工具函数中，暂停执行以供审查：

    @tool
    def send_email(to: str, subject: str, body: str):
        response = interrupt({"action": "send_email", "to": to, "message": "Approve sending?"})
        if response.get("action") == "approve":
            return f"Email sent to {to}"
        return "Email cancelled"

### 验证人工输入

使用循环中的多个 `interrupt` 调用来验证输入：

    def get_age_node(state):
        prompt = "What is your age?"
        while True:
            answer = interrupt(prompt)
            if isinstance(answer, int) and answer > 0:
                break
            prompt = f"'{answer}' is not a valid age."
        return {"age": answer}

## 中断规则

  * **不要**将 `interrupt` 调用包裹在 try/except 中
  * **不要**重新排序节点内的 `interrupt` 调用
  * **不要**在 `interrupt` 调用中返回复杂值
  * 中断前的副作用必须是幂等的
