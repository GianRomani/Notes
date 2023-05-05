Created: 2023-05-03 15:15
#note
With the latest rise of [[LLMs]], it has now become possible to build smart, dynamic, and capable context-aware chatbots.
LLMs are amazing in several tasks among which reasoning (chain-of-thought prompting) and acting (action planner generation).

We should use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for improved performance, human interpretability, and trustworthiness on a diverse set of language and decision-making tasks.

 A **basic idea** is that based on user input, the LLM decides whether a tool is required to answer the query or not. If so, the LLM will decide which of the given tools is best for helping with an answer. It then triggers the selected tool, gets an answer, and then decides if the answer suffices. If not, repeat.
 The new proposition for chatbot development goes like this:
1.  Define a set of tools required for achieving the chatbot task (like getting a weather forecast based on location). Also, describe how and when each tool should be used.
2.  Define a policy for how the chatbot should behave. For example, to be polite, always respond with a follow-up question, etc.
3.  Feed it to an LLM as a prompt for every user input.


## References
1. [Towards Data Science](https://betterprogramming.pub/action-driven-llms-the-future-of-chatbot-development-is-here-80c0d07d278a)

## Code
1. [Code from TDS](https://gist.github.com/assafelovic/7746354b021a1cc152db306aa457826d)
2. [LangChain](https://github.com/hwchase17/langchain)