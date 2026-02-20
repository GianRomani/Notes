Created: 2024-11-11 17:38
#paper
## Main idea
Simulate human red teaming exercise, in which an LLM is tested in a multi turn scenario. Based on the LLM's answers, this approach selects the most suitable attacks from a pool of "classic" approaches and adapt them to the specific exercise.

## Results
GOAT achieves ASR@10 of 97% against Llama 3.1 and 88% against GPT- 4-Turbo on the JailbreakBench dataset (Chao et al., 2024), outperforming an earlier highly effective multi-turn method, Crescendo.

## In deep
### Components
1. Red teaming attacks dataset: collection of published adversarial prompts that will be extended by the attacker LLM. The attacker accepts single attack or multiple ones in its context;
2. Attacker LLM: "unsafe" LLM instructed to perform red teaming exercises, directed with a variant of Chain-of-Thought;
3. Multi-turn chaining framework: framework that allows to chain the attacker and attacked LLMs and to use a judge at the end of the chat.


## References
1. 

## Code
1. 

## Tags
#aisecurity #llm 
