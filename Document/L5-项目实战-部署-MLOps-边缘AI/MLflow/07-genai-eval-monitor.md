Skip to main content[](/docs/latest/)LLMs & Agents

  * [LLMs & Agents](/docs/latest/genai/)
  * [Machine Learning](/docs/latest/ml/)
[API Reference](https://mlflow.org/docs/latest/api_reference/index.html)[Self-Hosting](/docs/latest/self-hosting/)[Community](/docs/latest/community/)[GitHub](https://github.com/mlflow/mlflow)Search

  * [Overview](/docs/latest/genai/)
  * [Live Demo](/docs/latest/genai/demo/)
  * **Getting Started**
  * [ Set Up MLflow Server](/docs/latest/genai/getting-started/connect-environment/)
  * [Start Tracing](/docs/latest/genai/tracing/quickstart/)
  * [Evaluate LLMs and Agents](/docs/latest/genai/eval-monitor/quickstart/)
  * [Try MLflow's AI Assistant](/docs/latest/genai/getting-started/try-assistant/)
  * [Automatic Issue Detection](/docs/latest/genai/eval-monitor/ai-insights/detect-issues/)
  * **Core Components**
  * [ Tracing (Observability)](/docs/latest/genai/tracing/)
  * [Evaluation & Monitoring](/docs/latest/genai/eval-monitor/)
    * [Quickstart](/docs/latest/genai/eval-monitor/quickstart/)
    * [Automatic Issue Detection](/docs/latest/genai/eval-monitor/ai-insights/detect-issues/)
    * [Running Evaluations](/docs/latest/genai/eval-monitor/running-evaluation/eval-examples/)
    * [Automatic Evaluation](/docs/latest/genai/eval-monitor/automatic-evaluations/)
    * [Judges and Scorers](/docs/latest/genai/eval-monitor/scorers/)
    * [Evaluation Datasets](/docs/latest/genai/datasets/)
    * [Annotation](/docs/latest/genai/assessments/feedback/)
    * [AI Insights](/docs/latest/genai/eval-monitor/ai-insights/ai-issue-discovery/)
    * [Migrating from MLflow 2 LLM Evaluation](/docs/latest/genai/eval-monitor/legacy-llm-evaluation/)
    * [FAQ](/docs/latest/genai/eval-monitor/faq/)
  * [Prompt Management & Optimization](/docs/latest/genai/prompt-registry/)
  * [AI Gateway](/docs/latest/genai/governance/ai-gateway/)
  * **More Features**
  * [ Version Tracking](/docs/latest/genai/version-tracking/)
  * [Packaging & Deployment](/docs/latest/genai/flavors/)
  * [MCP](/docs/latest/genai/mcp/)
  * [Agent Serving](/docs/latest/genai/serving/agent-server/)
  * **References**
  * [ Concepts](/docs/latest/genai/concepts/trace/)
  * [Request Features](/docs/latest/genai/references/request-features/)
  * [Managed MLflow](/docs/latest/genai/getting-started/databricks-trial/)

  * [](/docs/latest/)
  * Evaluation & Monitoring
On this page

# Evaluating LLMs and Agents with MLflow

MLflow's evaluation and monitoring capabilities help you systematically measure, improve, and maintain the quality of your LLM applications and AI agents throughout their lifecycle from development through production.   
**Try the MLflow LLMs and Agents Demo**  
The quickest way to learn about MLflow for LLMs and AI Agents is to try the demo. **Click to launch the demo ↓**

#### **Public Demo**​

Visit **[demo.mlflow.org](https://demo.mlflow.org/#/experiments/1/overview)** to explore a publicly hosted MLflow instance pre-loaded with sample data.

#### **Starting from UI**​

To start the demo, click on the "Start Demo" button on the top page of the MLflow UI.

#### **Starting from CLI**​

Alternatively, you can start the demo from the command line using the `mlflow demo` command. This option does not require you to have a running MLflow server.bash
    
    
    uvx mlflow demo  
    

A core tenet of MLflow's evaluation capabilities is **Evaluation-Driven Development**. This is an emerging practice to tackle the challenge of building high-quality LLM/Agentic applications. MLflow is an open source AI engineering platform that is designed to support this practice and help you quickly build production-quality AI agents and LLM applications.

## Key Capabilities​

  * Dataset Management
  * Human Feedback
  * LLM-as-a-Judge
  * Systematic Evaluation
  * Production Monitoring

#### Create and maintain a High-Quality Dataset​

Before you can evaluate your LLM application or AI agent, you need test data. **Evaluation Datasets** provide a centralized repository for managing test cases, ground truth expectations, and evaluation data at scale.Think of Evaluation Datasets as your "test database" - a single source of truth for all the data needed to evaluate your AI systems. They transform ad-hoc testing into systematic quality assurance.[Learn more →](/docs/latest/genai/datasets/)

#### Track Annotation and Human Feedbacks​

Human feedback is essential for building high-quality LLM applications and AI agents that meet user expectations. MLflow supports collecting, managing, and utilizing feedback from end-users and domain experts.Feedbacks are attached to traces and recorded with metadata, including user, timestamp, revisions, etc.[Learn more →](/docs/latest/genai/assessments/feedback/)

#### Scale Quality Assessment with Automation​

Quality assessment is a critical part of building high-quality LLM applications and AI agents, however, it is often time-consuming and requires human expertise. LLMs are powerful tools to automate quality assessment.MLflow offers various built-in [LLM-as-a-Judge](https://mlflow.org/llm-evaluation) scorers to help automate the process, as well as a flexible toolset to build your own LLM judges with ease.[Learn more →](/docs/latest/genai/eval-monitor/)

#### Evaluate and Enhance quality​

Systematically assessing and improving the quality of LLM applications and AI agents is a challenge. MLflow provides a comprehensive set of tools to help you evaluate and enhance the quality of your applications.Being the industry's most-trusted open source [AI engineering platform](https://mlflow.org/genai) for agents and LLM applications, MLflow provides a strong foundation for tracking your evaluation results and effectively collaborating with your team.[Learn more →](/docs/latest/genai/eval-monitor/quickstart/)

#### Monitor Applications in Production​

Understanding and optimizing LLM application and AI agent performance is crucial for efficient operations. [MLflow Tracing](https://mlflow.org/llm-tracing) captures key metrics like latency and token usage at each step, as well as various quality metrics, helping you identify bottlenecks, monitor efficiency, and find optimization opportunities.[Learn more →](/docs/latest/genai/tracing/prod-tracing/)

## Running an Evaluation​

Each evaluation is defined by three components: | Component| Example| **Dataset**  
Inputs & expectations (and optionally pre-generated outputs and traces)| 
    
    
    [  
      {"inputs": {"question": "2+2"}, "expectations": {"answer": "4"}},  
      {"inputs": {"question": "2+3"}, "expectations": {"answer": "5"}}  
    ]

| **Scorer**  
Evaluation criteria| 
    
    
    @scorer  
    def exact_match(expectations, outputs):  
        return expectations == outputs

| **Predict Function**  
Generates outputs for the dataset| 
    
    
    def predict_fn(question: str) -> str:  
        response = client.chat.completions.create(  
            model="gpt-4o-mini",  
            messages=[{"role": "user", "content": question}]  
        )  
        return response.choices[0].message.content

The following example shows a simple evaluation of a dataset of questions and expected answers. python
    
    
    import os  
    import openai  
    import mlflow  
    from mlflow.genai.scorers import Correctness, Guidelines  
      
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  
      
    # 1. Define a simple QA dataset  
    dataset = [  
        {  
            "inputs": {"question": "Can MLflow manage prompts?"},  
            "expectations": {"expected_response": "Yes!"},  
        },  
        {  
            "inputs": {"question": "Can MLflow create a taco for my lunch?"},  
            "expectations": {"expected_response": "No, unfortunately, MLflow is not a taco maker."},  
        },  
    ]  
      
      
    # 2. Define a prediction function to generate responses  
    def predict_fn(question: str) -> str:  
        response = client.chat.completions.create(  
            model="gpt-4o-mini", messages=[{"role": "user", "content": question}]  
        )  
        return response.choices[0].message.content  
      
      
    # 3.Run the evaluation  
    results = mlflow.genai.evaluate(  
        data=dataset,  
        predict_fn=predict_fn,  
        scorers=[  
            # Built-in LLM judge  
            Correctness(),  
            # Custom criteria using LLM judge  
            Guidelines(name="is_english", guidelines="The answer must be in English"),  
        ],  
    )  
    

## Review the results​

Open the MLflow UI to review the evaluation results. You can use the following command to start the UI: bash
    
    
    mlflow server --port 5000  
    

You should see a new evaluation run is created under the "Runs" tab. Click on the run name to view the evaluation results.

## Next Steps​

### [QuickstartLearn MLflow's evaluation workflow in action.Start evaluating →](/docs/latest/genai/eval-monitor/quickstart/)### [Evaluate AgentsEvaluate AI agents with specialized techniques and custom scorers.Evaluate agents →](/docs/latest/genai/eval-monitor/running-evaluation/agents/)### [Building ScorersGet started with MLflow's powerful scorers for evaluating qualities.Learn about scorers →](/docs/latest/genai/eval-monitor/scorers/)[PreviousFAQ](/docs/latest/genai/tracing/faq/)[NextQuickstart](/docs/latest/genai/eval-monitor/quickstart/)

  * Key Capabilities
  * Running an Evaluation
  * Review the results
  * Next Steps
© 2025 MLflow Project, a Series of LF Projects, LLC.[Components](https://mlflow.org)[Releases](https://mlflow.org/releases)[Blog](https://mlflow.org/blog)[Docs](/docs/latest/)[Ambassador Program](https://mlflow.org/ambassadors)
