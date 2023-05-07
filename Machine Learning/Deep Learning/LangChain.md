Created: 2023-05-05 13:42
#note

LangChain is a framework that enables quick and easy development of applications that make use of [[LLM]]s.

The framework is organized into six modules each module allows you to manage a different aspect of the interaction with the LLM. 

-   [**Models**](https://python.langchain.com/en/latest/modules/models.html): Allows you to instantiate and use different models.
-   [**Prompts**](https://python.langchain.com/en/latest/modules/prompts.html): The prompt is how we interact with the model to try to obtain an output from it. By now knowing how to write an effective prompt is of critical importance. This framework module allows us to better manage prompts. For example, by creating templates that we can reuse.
-   [**Indexes**](https://python.langchain.com/en/latest/modules/indexes.html): The best models are often those that are combined with some of your textual data, in order to add context or explain something to the model. This module helps us do just that.
-   [**Chains**](https://python.langchain.com/en/latest/modules/chains.html): Many times to solve tasks a single API call to an LLM is not enough. This module allows other tools to be integrated. For example, one call can be a composed chain with the purpose of getting information from Wikipedia and then giving this information as input to the model. This module allows multiple tools to be concatenated in order to solve complex tasks.
-   [**Memory**](https://python.langchain.com/en/latest/modules/memory.html): This module allows us to create a persisting state between calls of a model. Being able to use a model that remembers what has been said in the past will surely improve our application.
-   [**Agents**](https://python.langchain.com/en/latest/modules/agents.html): An agent is an LLM that makes a decision, takes an action, makes an observation about what it has done, and continues in this manner until it can complete its task. This module provides a set of agents that can be used.

Whereas a _chain_ defines an immediate input/output process, the logic of agents allows a step-by-step thought process. The advantage of this step-by-step process is that the LLM can work through multiple reasoning steps or tools to produce a better answer.

To create a custom tool, [check here](https://www.pinecone.io/learn/langchain-tools/).

# Agent types

LangChain offers several types of agents:
- **Zero Shot ReAct** (zero-shot-react-description): we use this agent to perform _“zero-shot”_ tasks on some input. That means the agent considers _one single_ interaction with the agent — it will have no _memory_;
- **Conversational ReAct** (conversational-react-description): We can think of this agent as the same as **Zero Shot ReAct** agent, but with _conversational memory_ (remember to initialize the memory buffer);
- **ReAct Docstore** (react-docstore): As before, it uses the ReAct methodology, but now it is explicitly built for information search and lookup using a LangChain _docstore_ which allows us to store and retrieve information using traditional retrieval methods;
- **Self-Ask With Search** (self-ask-with-search): This agent is the first to consider when connecting an LLM with a search engine. The agent will perform searches and ask follow-up questions as often as required to get a final answer.


## References
1. [Pinecone book](https://www.pinecone.io/learn/langchain/)
2. [Marcello Politi's post](https://towardsdatascience.com/develop-applications-powered-by-language-models-with-langchain-d2f7a1d1ad1a)
3. [Basics Tutorial](https://www.classcentral.com/course/youtube-langchain-basics-tutorial-1-llms-prompttemplates-with-colab-151908)
4. [Medium](https://towardsdatascience.com/a-gentle-intro-to-chaining-llms-agents-and-utils-via-langchain-16cd385fca81)
5. [Agents](https://www.pinecone.io/learn/langchain-agents/)

## Code
1. [Intro](https://colab.research.google.com/github/pinecone-io/examples/blob/master/generation/langchain/handbook/00-langchain-intro.ipynb#scrollTo=b96WIvouLQ-7)
2. [GitHub](https://github.com/hwchase17/langchain)
3. [Docs](https://python.langchain.com/en/latest/index.html)
4. [Collection of content relative to LangChain](https://github.com/kyrolabs/awesome-langchain)