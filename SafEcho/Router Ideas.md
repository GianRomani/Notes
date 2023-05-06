Notation:
- Tool -> what is orchestrated by the router
- Router -> [[LLM]] (does is have to be one?) that orchestrate
- Agent = router in most cases

Our problem:
- input -> task planner -> router -> models -> consolidation (put everything together) -> result
- tools should talk to each other?
- from the task planner we have different tasks for different models:
	- are the tasks defined by the Task planner? If yes, has the router just to orchestrate the jobs of the tools?
	- do we have the Task planner?
- Privacy: can we use OpenAI models? Most of the examples and papers use these models (i.e. we are not sure about other models performance)

[[LLamaIndex]]:
- tools have descriptions used by the agent to decide which to pick
- inputs and outputs are strings
- indexes, retrievers, response synthesis, and query engines can be used on top of the proprietary data.
- we can use more than one tool at the same time (e.g. semantic search + summarization -> [Colab](https://colab.research.google.com/drive/1Asq_obABBUxTqUPTGv8yFfCDqhC-ta4u?usp=sharing))
- What about memory? -> combine with LangChain ([tutorial](https://gpt-index.readthedocs.io/en/latest/guides/tutorials/building_a_chatbot.html))
- LlamaDebugHandler tracks events and timing stats

[[ReAct - Synergizing reasoning and acting in language models]]:
- Solving process demonstrated by ReAct is more factual and grounded, whereas CoT is more accurate in formulating reasoning structure but can easily suffer from hallucinated facts or thoughts;
- Best version is given by ReAct+CoT and external knowledge;
- tested with GPT-3 and PaLM, what about other models?
- How does fine-tuning works? Is it necessary?

[[LangChain]]:
- it helps with instantiation of models, memory, agents, chains;
- prompts: we can use template (even ones that have already been written) and few shot examples;
- we can use indexes (with retriever)
- we can define custom tool (and a tool can be another LLM)


