Created: 2024-02-06 16:10
#paper
## Main idea
System prompts are really important to define specific behavior of [[Large Language Models (LLMs)]]. For this reason, companies are treating them as secrets, hidden to the user who is making the query.
However, this paper shows how easy it is to extract such prompt. Accessing the system prompt can help attackers to design more effective attacks.

## Details

The authors defined the attacks as $a_i$ and the output of an LLM as $f_p(q)$, where  $q$ is a query (input from the user) and $p$ is he system prompt.

An attack (i.e. extraction of the system prompt) is successful if $f_p(a_i)$ has a BLEU score $\geq 0.6$ compared to the prompt $p$. The threshold is high so there could be (and there are) false negatives.
As the attacker can try multiple attacks queries (max 19), the attack is successful if at least one attack query leaks the prompt.

### Datasets

Two sources of prompts were used in the experiments: ShareGPT and Awesome-ChatGPT-Prompts.

### Models

The models that were tested are: GPT3.5 and GPT4 and Vicuna-13B. All models were used through APIs.
## Results

The authors came up with a list of simple attack queries with the goal of elicit- ing a response from the language model that contains the prompt.
A DeBERTa model, fine-tuned on a subset of ShareGPT, was used to classify when an extraction matches the groundtruth.
The estimate of an extraction $e_i$ being successful, conditioned on other attacks no the same prompt, is given by $P_{DeBERTa}(e_i)=E_{\sigma}[P(e_i|\sigma(e_{j!=i}))]$. 

The authors observe that the prompt extraction attacks are highly effective, capable of extracting > 60% of prompts across all model and dataset pairs. Among the three models, GPT-3.5 is the most vulnerable, with 89% of prompts extractable on average across two held-out datasets. GPT-4 ignores the attack (and follows the actual prompt) more often than GPT- 3.5, resulting in slightly lower prompt extractability (81.9% average).
Likely due to Vicuna being a smaller, less- capable model, it is the hardest model to extract prompts from.
![[prompts_as_secrets_results.png|400]]

The authors used the $P_{DeBERTa}$ heuristic to determine whether an extracted prompt matches the groundtruth.

**Note:** Attacks and more details are in the appendixes of the paper.

![[prompt_as_secret_attacks.png|400]]
### Defense technique

The authors used a very simple defense method: when there is a 5-gram overlap between the LLM's generation and the hidden prompt, the defense returns an empty string -> this reduces to 0% the success rate of attacks.
Of course this can be bypassed: we can instruct the model to hide the prompt in the output, so that we can retrieve it and not trigger the defense mechanism. The more the model is good in following instructions, the more it is to use this attack.

## References
1. [Paper](https://arxiv.org/pdf/2307.06865.pdf)
## Tags
#cybersecurity #AML #llm #prompting
