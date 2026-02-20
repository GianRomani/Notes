Created: 2023-05-09 12:21
#paper
## Main idea
The idea is that [[Large Language Models (LLMs)]] can dialogue with other models and thus exploit their capabilities. The authors started with the intuition that any AI model could be defined in the textual form “by summarizing its model function.” So the idea is to use language as an interface between an LLM to another model.
Obviously, to be able to do this we need a large number of high-quality model descriptions. So what we need is to tie LLMs to the community (GitHub, HuggingFace, and so on).

The process can be defined in four steps:
-   **Task Planning:** ChatGPT analyze the requests by the user (understand intention) and transform the question into possible solvable tasks.
-   **Model Selection:** ChatGPT selects the appropriate models (expert models) that are present in HuggingFace (the model are selected based on the provided description)
-   **Task Execution:** the model is invoked and executed, then the results are returned to ChatGPT
-   **Response Generation:** ChatGPT integrates the results of the models and generates the answers

## Results
In theory, this approach has advantages over previous approaches. HuggingGPT is not limited to the visual component but can integrate any tasks and models because it cooperates with other models. Also, it can solve more complex tasks because it can cooperate with multiple models and organize task execution.

**Note**: the approach is not compared to other ones in the paper.

**Limitations**:
- Efficiency. The bottleneck of efficiency lies in the inference of the large language model. For each round of user requests, HuggingGPT requires at least one interaction with the large language model during the task planning, model selection, and response generation stages. These interactions greatly increase the response latency and lead to a degradation of user experience;
- TContext length. Limited by the maximum number of tokens that the LLM can accept, HuggingGPT also faces a limitation on the maximum context length;
- Stability:
	- Large language models occasionally fail to conform to instructions when inferring, and the output format may defy expectations, leading to exceptions in the program workflow. 
	- The state of the expert model hosted on Hugging Face’s inference endpoint is uncontrollable. The expert models on Hugging Face may be affected by network latency or service state, leading to errors in the task execution stage.

## In deep
![[HuggingGPT.png |600]]
### Task Planning
The first step is to understand the tasks involved in answering the user’s question. The model receives a user request, has to interpret the intentions, and transforms this request into multiple tasks. After that, it must plan the order and dependencies based on its knowledge.

HuggingGPT uses Specification-based Instruction for this first step, i.e. it draws four slots for task parsing:
-   **Task ID**, the model provides a unique identifier for each task. This ID is used to identify both the task and the tasks that are dependent and all the resources that are generated.
-   **Task type,** each task can be of various types (language, visual, video, audio, and so on).
-   **Task dependencies,** define the pre-requisites for each task (the model only launches a task if all its pre-requisites are complete).
-   **Task arguments,** this slot contains all the arguments that are required for the execution of a task (from text to images or other resources). These contents can be derived from the user’s query or from the results of other tasks

The model also exploits another approach called Demonstration-based Parsing, i.e. by injecting several demonstrations into the prompts, HuggingGPT allows the large language model to better understand the intention and criteria for task planning.

### Model selection
Once HuggingGPT parsed a list of tasks, you need to choose the appropriate model for each task (match task and models). This is possible because we have the description of the models.
Since there are different models for the same task, the authors relied on the community, the models are in fact ranked based on the number of downloads (this number should partly reflect the quality of a model). After that, a number of models are selected (top-k candidates) and HuggingGPT chooses from these.

### Task execution
Once the task is assigned to a model, we then need the model to execute it (the model is used only in inference). To speed up execution HuggingGPT uses hybrid inference endpoints. The selected model takes the task arguments as input and then sends the results back to the language model (ChatGPT). Moreover, if the model has no resource dependencies its inference can be parallelized. In other words, tasks that are not dependent on each other can be executed simultaneously.

### Response Generation
The last step is the generation of a response. This occurs when all tasks have been completed. During this step, HuggingGPT integrates all the information that was obtained from the previous steps into a kind of concise summary.

## References
1. [Paper](https://arxiv.org/pdf/2303.17580.pdf)
2. [Medium](https://levelup.gitconnected.com/hugginggpt-give-your-chatbot-an-ai-army-cfadf5647f98)

## Code
1. [Jarvis](https://github.com/microsoft/JARVIS?utm_source=catalyzex.com)

## Tags
#llm #dl 