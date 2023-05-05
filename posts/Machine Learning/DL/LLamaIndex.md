Created: 2023-05-05 10:09
#note

These days, a variety of retrieval techniques for [[LLM]]-powered QA have emerged. One common among all these techniques is that each typically works better for certain QA use cases, and works less well for other use cases.

How can we try unifying all these techniques under a single query interface?
One answer is **Routing**.

A Router consists in the LLM agent/tool abstraction -> an agent decides which tool to pick for the current task at hand. In this way we can augment the prompts for the LLM with *context data*.
To perform LLM’s data augmentation in a performant, efficient, and cheap manner, we need to solve two components:
-   Data Ingestion
-   Data Indexing

That’s where the **LlamaIndex** comes in. LlamaIndex is a simple, flexible interface between external data and LLMs.

At the current moment, the way a tool is defined in LLamaIndex is just with a text description attached to it. The router uses the text description in deciding which underlying query engine to select to execute the query.
![[llama_index_router.jpeg | 500]]
In LlamaIndex, the Router is called RouterQueryEngine.
Indexes, retrievers, response synthesis, and query engines can be easily used. 
A query engine is an abstract query interface that takes in a natural language input, and can (optionally) use retrievers/response synthesis modules to return an output that the user would want.

We can use more than one tool at the same time (e.g. semantic search + summarization -> [Colab](https://colab.research.google.com/drive/1Asq_obABBUxTqUPTGv8yFfCDqhC-ta4u?usp=sharing)).

There are extensions to this that would make routing more sophisticated, effectively adding agent-like behaviors over your data:
- **Non-LLM-based routing.** Routing to query engines not with LLM calls, but with other (faster?) techniques like embedding lookup;
- **Routing to not only one query engine, but multiple query engines using a decision heuristic.*;
- **Indexing/Retrieving the set of query engines**;
- Incorporating not only automatic “selection” of a query engine, but also the **automatic determination of which parameters the query engine** should use (as in Structured Tools in [[LangChain]]).

Challenges:
- **Latency**: adding LLM calls adds latency costs;
- **Accuracy**: if the router makes a wrong decision, then the error will propagate

## References
1. [Medium](https://medium.com/@jerryjliu98/unifying-llm-powered-qa-techniques-with-routing-abstractions-438e2499a0d0)
2. [Twitter](https://twitter.com/jerryjliu0/status/1653789212620230658?s=20)
3. [Docs](https://gpt-index.readthedocs.io/en/latest/)
4. [LlamaIndex twitter page](https://twitter.com/gpt_index)
5. [MRKL Systems](https://arxiv.org/pdf/2205.00445.pdf)

## Code
1. [GitHub](https://github.com/jerryjliu/llama_index)
2. [Colab example](https://colab.research.google.com/drive/1Asq_obABBUxTqUPTGv8yFfCDqhC-ta4u?usp=sharing)