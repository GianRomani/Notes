Created: 2023-05-09 11:16
#note

It can be used to build, deploy and manage [[Large Language Models (LLMs)]] Agents that access individual APIs or sources of data, such as GitHub, Google Calendar, or a database.

![[fixie_architecture.png | 500]]
The core Fixie services run on the cloud, while agents can operate anywhere (hosted by Fixie, customer or third parties). Fixie's registry has all the data needed to access the agents.

Agent can be created and hosted by the customer. It should be easy to wrap third-party AI services and use few-shots prompts.
By default, agents use the `text-davinci-003` model from OpenAI with a default temperature of `0` and a `maximum_tokens` size of 1,000.

Tool as called Funcs -> they are invoked by Agents.
Embeds (images, videos, texts, etc) can be attached to a query or response.
External knowledge can be used.

Agents can authenticate to third-party services to perform actions on behalf of the user.
An API to store the state related to a user of a chat session is offered. It is a key-value store (think of cookies in web browser).

There is a limit of 1000 queries for day, but additional credits can be purchased.

## Summary
**Pros**:
-   it offers an architecture to easily build applications
-   it is free (but has a limit on daily requests)
-   most services are on the cloud
-   Agents can be hosted by the customer, Fixie, or third-parties
-   Third-party AI services and products should be easy to use (check [this](https://github.com/fixie-ai/fixie-examples/blob/main/agents/langchain_search/main.py "https://github.com/fixie-ai/fixie-examples/blob/main/agents/langchain_search/main.py") simple example for LangChain)
-   We can define custom tools (in Fixie they are called Funcs)
-   We can add Embeds (images, videos, texts, etc) to a query or response
-   Agents can authenticate to third-party services to perform actions on behalf of the user
-   An API to store the state related to a user of a chat session is offered. It is a key-value store (think of cookies in a web browser)
-   Docs are easy to read in most cases

**Cons**:
-   Is not clear which kinds of agents are already implemented (they say they use text-davinci-003, but that is it) → how can we use ReAct? (maybe through LangChain)
-   Some parts of the docs are not super clear

## References
1. [Website](https://www.fixie.ai/)
2. [Docs](https://docs.fixie.ai/)

## Code
1. [GitHub](https://github.com/fixie-ai/fixie-examples)