Created: 2024-06-20 15:16
#paper
## Main idea
The paper combines [[Graph Neural Network]] and [[Large Language Models (LLMs)]] in a RAG scenario.
An overview of the approach is the following:
1) The GNN reason over a dense KG to retrieve answer candidates for a given question; 
2) the shortest path in the KG that connects the question to the answer candidates are extracted to represent useful KG reasoning;
3) the paths are then verbalized and passed to an LLM for reasoning in a RAG context.

![[GNN-RAG.png|600]]
## In deep

### GNN
The GNN goes over the KG and classifies the nodes as *answers* or *not answers*. The model is trained with pairs *question/answers*.
GNN reasoning depends on the question-relation matching operation $\omega(q, r)$. A common implementation of $\omega(q, r)$ is $\phi(q (k) \odot r)$, where function $\phi$ is a neural network, and $\odot$ is the element-wise multiplication. Question representations $q(k)$ and KG relation representations $r$ are encoded via a shared pretrained LM.
The choice of the LM model certainly influences the results of the GNN, so the authors tried two different LMs, *SBERT* and $LM_{SR}$ (a pretrained LM for question-relation matching over the). Both models improve RAG-based KGQ.

### LLM
After obtaining the reasoning paths by GNN-RAG, they are verbalized and given as input to a LLM. However, LLMs are sensitive to the input prompt template and the way that the graph information is verbalized. To solve this, RAG prompt tuning can be done (on open-weights models). The model used in this paper was Llama2-Chat-7B and the prompt is: *“Based on the reasoning paths, please answer the given question.\n Reasoning Paths: {Reasoning Paths} \n Question: {Question}”. The reasoning paths are verbalised as “{question entity} → {relation} → {entity} → · · · → {relation} → {answer entity}"*

### Retrieval Augmentation (RA)
The paper explains why the GNN are more suited for multi-hop information, compared to LLM for example (which are better for single-hop retrieval).
![[GNN_retrieval.png|400]]
The metric used here is called *Answer Coverage*, which evaluates whether the retriever is able to fetch at least one correct answer for RAG.

Retrieval augmentation (RA) combines the retrieved KG information from different approaches to increase diversity and answer recall. **GNN-RAG+Ensemble** takes the union of the retrieved paths of the two different GNNs ($GNN+SBERT$ & $GNN+LM_{SR}$) as input for RAG.

## Results

![[GNN_RAG_results.png]]
From the summary above, we can observe that:
1. GNN-based retrieval is more efficient (\#LLM Calls, \#Input Tokens) and effective (*F1*) than LLM-based retrieval, especially for complex questions (*CWQ*); see rows (e-f) vs. row (*d*). 
2. Retrieval augmentation works the best (*F1*) when combining GNN-induced reasoning paths with LLM-induced reasoning paths as they fetch non-overlapping KG information (increased \#Input Tokens) that improves retrieval for KGQA; see rows (*h*) & (*i*). 
3. Augmenting all retrieval approaches does not necessarily cause improved performance (*F1*) as the long input (\#Input Tokens) may confuse the LLM; see rows (*g/j*) vs. rows (*e/h*). 
4. Although the two GNNs perform differently at KGQA (*F1*), they both improve RAG with LLMs; see rows (*a-b*) vs. rows (*e-f*).

## Limitations
The approach assumes that the subgraph contains the answer and if it has disconnected parts, the shortest path extraction algorithm of GNN-RAG may return empty reasoning paths.

## References
1. [Paper](https://arxiv.org/pdf/2405.20139)

## Code
1. [Repository](https://github.com/cmavro/GNN-RAG)

## Tags
#knowledgegraph #llm #rag #gnn 
