# Bibliography for our results
Created: 2022-09-24 15:21
#note

## Not persistent results
[[BERTopic]] and [[Top2Vec]] do not offer the possibility to fix the seed number to reproduce results.

In BERTopic [paper,](https://arxiv.org/pdf/2203.05794.pdf) the results are obtained in the following way: fixed number of topics (from 10 to 50 with steps of 10) and three runs for every test, i.e. 15 runs.


## Evaluation metrics
There is concern that standard ways used to evaluate topic models can not be used with neural topic models -> see [here](https://proceedings.neurips.cc/paper/2021/file/0f83556a305d789b1d71815e8ea4f4b0-Paper.pdf). 
Solutions:
- consider topics words meaning -> [[Similarity]] : [page 44](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf) 
- OCTIS -> [here](https://aclanthology.org/2021.eacl-demos.31.pdf)

Why our metrics are good (or not):
- original coherence [paper](http://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf);
- [this](https://www.baeldung.com/cs/topic-modeling-coherence-score) and [this](https://palmetto.demos.dice-research.org/) site;
- [RBO](https://dl.acm.org/doi/pdf/10.1145/1852102.1852106?casa_token=oKu_SItzVa0AAAAA:HCtnFDz99wg9XYDz-_3HLlXkEIkZMivH4w6BxJdm-Hqd0vxuPTiIg8YTMsWyjnGdiu91Yvlu) ;
- how coherence scores are computed [Towards Data Science](https://towardsdatascience.com/understanding-topic-coherence-measures-4aa41339634c). 
## References
1. 

## Code
1. 

#### Tags
#bibliography