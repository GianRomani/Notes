Created: 2023-05-03 16:02
#paper
## Main idea
ReAct combines reasoning and acting with large language models for solving diverse language reasoning and decision making tasks.
With this paradigm, we prompt [[Large Language Models (LLMs)]]s to generate both verbal reasoning traces and actions that are pertinent to a task, and then interact with the external environments to incorporate additional information into reasoning.

## Results
- ReAct outperforms consistently Action-only prompting;
- ReAct is better than CoT on Fever, but not on HotpotQA;
- The retrieval of information knowledge is vital for ReAct;
- ReAct hallucinates less than CoT;
- ReAct + CoT is the best for prompting LLMs;
- ReAct can improve a lot thanks to fine-tuning

## Ideas for future works
- Explore how to better fine-tune in specific domains.
- Human-in-the-loop behavior correction

## In deep

The idea of ReAct is simple: we augment the agent’s action space to $\hat{A} = A \cup L$, where L is the space of language. An action $\hat{a}_t \in L$ in the language space, which we will refer to as a thought or a reasoning trace, does not affect the external environment, thus leading to no observation feedback. Instead, a thought $\hat{a}_t$ aims to compose useful information by reasoning over the current context $c_t$, and update the context $c_t+1 = (c_t, \hat{a}_t)$ to support future reasoning or acting.

However, as the language space *L* is unlimited, learning in this augmented action space is difficult and requires strong language priors. In this paper, the authors mainly focus on the setup where a frozen large language model, PaLM-540B, is prompted with few-shot in-context examples to generate both domain-specific actions and free-form language thoughts for task solving. Each in-context example is a human trajectory of actions, thoughts, and environment observations to solve a task instance. For the tasks where reasoning is of primary importance, they alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple thought-action-observation steps. In contrast, for decision making tasks that potentially involve a large number of actions, thoughts only need to appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself.

Further tests on GPT3, demonstrate how this model outperforms PaLM-540B.

The baselines for comparisons are: 
1. Standard prompting;
2. Chain of Thought (CoT);
3. Acting-only prompting.

Since decision making and reasoning capabilities are integrated into a large language model, ReAct enjoys several unique features: 
1. **Intuitive and easy to design**: Designing ReAct prompts is straightforward as human annotators just type down their thoughts in language on top of their actions taken. No ad-hoc format choice, thought design, or example selection is used in this paper. Detail prompt designs for each task are in Sections 3 and 4 of the paper.  
2. **General and flexible**: Due to the flexible thought space and thought-action occurrence format, ReAct works for diverse tasks with distinct action spaces and reasoning needs, including but not limited to QA, fact verification, text game, and web navigation. 
3. **Performant and robust**: ReAct shows strong generalization to new task instances while learning solely from one to six in-context examples, consistently outperforming baselines with only reasoning or acting across different domains.
4. **Human aligned and controllable**: ReAct promises an interpretable sequential decision making and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover, humans can also control or correct the agent behavior on the go by thought editing.

### Datasets
Two datasets are considered, to challenge knowledge retrieval and reasoning: 
1. **HotPotQA** (Yang et al., 2018), a multi-hop question answering benchmark that requires reasoning over two or more Wikipedia passages;
2. **FEVER** (Thorne et al., 2018), a fact verification benchmark where each claim is annotated SUPPORTS, REFUTES, or NOT ENOUGH INFO, based on if there exists a Wikipedia passage to verify the claim.

### External knowledge
To support ReAct with external knowledge a simple Wikipedia API is used with three actions:
1. search[entity] -> which returns the first 5 sentences from the corresponding entity wiki page if it exists, or else suggests top-5 similar entities from the Wikipedia search engine;
2. lookup[string] -> which would return the next sentence in the page containing string, simulating Ctrl+F functionality on the browser;
3. finish[answer] ->which would finish the current task with answer.

### ReAct + CoT
The authors observe that the problem solving process demonstrated by ReAct is more factual and grounded, whereas CoT is more accurate in formulating reasoning structure but can easily suffer from hallucinated facts or thoughts. They therefore propose to incorporate ReAct and CoT-SC, and let the model decide when to switch to the other method based on the following heuristics:  
1. ReAct → CoT-SC: when ReAct fails to return an answer within given steps, back off to CoT-SC. They set 7 and 5 steps for HotpotQA and FEVER respectively as they find more steps will not improve ReAct performance;
2. CoT-SC → ReAct: when the majority answer among n CoT-SC samples occurs less than n/2 times (i.e. internal knowledge might not support the task confidently), back off to ReAct.

## References
1. [Paper](https://arxiv.org/pdf/2210.03629.pdf)
2. [Summary](https://tsmatz.wordpress.com/2023/03/07/react-with-openai-gpt-and-langchain/)

## Code
1. [GitHub](https://react-lm.github.io/)

## Tags
#chatbot #llm #dl 
