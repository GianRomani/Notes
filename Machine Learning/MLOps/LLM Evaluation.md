Created: 2026-02-20 10:00
#note

Large Language Models and AI agents produce probabilistic outputs that demand systematic evaluation beyond traditional unit testing paradigms. Unlike deterministic software, LLM outputs vary based on temperature settings, model versions, and input variations, necessitating robust measurement frameworks that capture quality across multiple dimensions. Effective evaluation enables teams to detect regressions, compare model versions, and ensure production systems maintain acceptable performance standards before deployment.

## Evaluation Types

| Type | Description | Best For |
|------|-------------|----------|
| **Assertion-based** | Hard checks on outputs (length, format, presence of keywords) | Deterministic requirements |
| **LLM-as-judge** | Another LLM grades agent outputs against rubrics | Fast iteration, nuanced quality |
| **Human annotation** | Domain experts label outputs on quality scales | Ground truth, critical domains |
| **Reference-based** | Compare against gold-standard outputs (BLEU, ROUGE) | Text generation, summarization |
| **RAG Triad** | Context relevance, groundedness, answer relevance | Retrieval-augmented systems |

## LLM-as-Judge Pattern

The **LLM-as-judge** approach leverages a capable model to evaluate another model's outputs against explicit rubrics. The judge model receives the input prompt, generated output, and evaluation criteria, returning structured scores and reasoning. This pattern enables rapid iteration cycles without expensive human review; evaluation happens instantly at scale during testing phases.

However, LLM-as-judge carries systematic biases worth acknowledging. **Position bias** causes judges to favor outputs presented first in comparative evaluations. **Verbosity bias** leads judges to prefer longer, more detailed responses over concise correct answers. **Self-alignment bias** causes judges to favor outputs matching their own writing style. Mitigation strategies include employing **multiple independent judges** (typically 3-5), randomizing output presentation order, and using explicit rubric anchors that define what excellent, good, acceptable, and poor performance actually entails.

## Metrics for Agent Evaluation

### Functional Metrics
- **task_complete**: Boolean indicating whether the agent successfully completed the requested task
- **tool_call_success_rate**: Percentage of tool invocations that executed without errors
- **steps_to_completion**: Number of agent steps required to solve the task (fewer is better)
- **error_rate**: Percentage of runs encountering failures or exceptions

### Quality Metrics
- **output_quality**: LLM-judge score on overall response quality (typically 1-10 scale)
- **instruction_following**: Degree to which outputs adhere to specified constraints and requirements
- **hallucination_rate**: Percentage of factual claims that cannot be verified against source materials
- **relevance**: Proportion of output content directly addressing the user's query

### Efficiency Metrics
- **latency_p50, p95, p99**: 50th, 95th, and 99th percentile response times in milliseconds
- **token_usage**: Total input and output tokens consumed per task
- **cost_per_task**: Actual monetary cost including API calls and infrastructure

## Evaluation Dataset

A robust evaluation dataset forms the foundation for reliable quality measurement. Strong datasets exhibit **diverse inputs** spanning different difficulty levels, edge cases, and user personas. Each example requires **expected outputs** defined by domain experts or derived from human demonstrations. **Metadata** annotations capture task category, expected difficulty, relevant knowledge domains, and evaluation strategy.

Dataset bootstrapping follows a staged approach: Begin with seed examples (10-50 high-quality hand-written cases), apply systematic **augmentation** through paraphrasing and parameter variation, generate **synthetic examples** using templates or models, and continuously **capture production failures** to expand coverage. This progression balances human effort against dataset scale.

## CI/CD Integration

Evaluation frameworks integrate into continuous integration pipelines to prevent regressions. Each pull request triggers evaluation runs against the standard dataset, generating quality reports that block merges if metrics fall below established **quality gates**. Common gates specify minimum thresholds for task completion rate (>95%), hallucination rate (<5%), and p95 latency (<2000ms). This automated feedback loop accelerates iteration while maintaining production readiness.

## RAG Evaluation (RAG Triad)

Retrieval-augmented generation systems require specialized evaluation beyond standard LLM metrics. The **RAG Triad** framework measures three orthogonal dimensions:

- **Context relevance**: Assesses whether retrieved documents contain information needed to answer the query
- **Groundedness**: Measures whether generated responses derive from retrieved context rather than model hallucinations
- **Answer relevance**: Evaluates whether the final response actually addresses the user's question

See [[RAG]] for architectural details on retrieval pipelines.

## Evaluation Frameworks

| Framework | Strengths | Use Case |
|-----------|-----------|----------|
| **RAGAS** | Purpose-built for RAG systems, comprehensive metrics, open-source | RAG-specific evaluation |
| **DeepEval** | Simple assertion syntax, rich built-in metrics, LLM-as-judge support | General LLM evaluation |
| **LangSmith Evals** | Integrated with LangChain ecosystem, dataset management, tracing | Agent/chain evaluation |
| **Braintrust** | Real-time collaboration, detailed diffs, regression detection | Team-based evaluation |
| **MLflow Evaluate** | Model comparison, built-in metrics, experiment tracking | End-to-end MLOps |

## References

- [MLflow Evaluate](https://mlflow.org/docs/latest/llms/llm-evaluate/index.html)
- [RAGAS Documentation](https://docs.ragas.io/)
- [DeepEval Documentation](https://docs.confident-ai.com/)

#### Tags: #mlops #evaluation #testing #llm #genai

Links to: [[LLM Observability]], [[Langfuse]], [[RAG]], [[Prompts as Infrastructure]], [[AI Agents]]
