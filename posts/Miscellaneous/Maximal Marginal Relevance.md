Created: 2022-07-01 09:43
#paper

## Main idea
MMR tries to reduce the redundancy of results while at the same time maintaining query relevance of results for already ranked documents/phrases etc.
One approach to reach this could consist in using cosine similarity among the results and set a threshold to decide which terms are to be kept. But an issue with this approach is that you need to set manually the threshold (0.9 in code) above which terms will be clubbed together.
MMR, instead, selects the phrase in the final keyphrases list according to a combined criterion of query relevance and novelty of information.

## In deep
$MMR=Argmax_{D_i \in R\ S}[\lambda (Sim_1(D_i,Q)-(1-\lambda)max_{D_j \in S} Sim_2(D_i,D_j))]$, where Q is the query (i.e. a description of document category), D is a set of documents related to query Q, S is a subset of documents in R already selected, R\ S is the set of unselected documents in R and $\lambda$ is a constant in range [0-1] for diversification of results. Cosine similarity can be considered for $Sim_1$ and $Sim_2$.

## References
1. [Paper](https://arxiv.org/pdf/2010.00117.pdf)
2. [TowardsDataScience](https://medium.com/tech-that-works/maximal-marginal-relevance-to-rerank-results-in-unsupervised-keyphrase-extraction-22d95015c7c5)

## Code
1. [GitHib](https://github.com/morningmoni/RL-MMR?utm_source=catalyzex.com)
