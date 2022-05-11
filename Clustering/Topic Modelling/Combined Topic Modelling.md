# Pre-training is a Hot Topic, Contextualized Document Embeddings improve Topic Coherence
Created: 2022-05-09 11:49
#paper

In this paper the authors combine contextualized representations with neural topic models. This improves topic coherence in a significant way. The model is called Combined Topic Model (CTM).

## Main idea
CTM is built around two components:
1. Neural topic model [ProdLDA](https://arxiv.org/pdf/1703.01488.pdf);
2. Sentence BERT.

**Note**: other topic models or pre-trained representations can be used, as long as the topic model extends an autoencoder and the pre-trained representations embed the documents.

## In deep
![[CTM.PNG]]

As #cluster_metrics normalized pointwise [[Mutual Information]], external word embeddings topic coherence and inverse rank-biased overlap are used. 
## References
1. [Paper](https://aclanthology.org/2021.acl-short.96.pdf)

## Code
1. [GitHub]([GitHub - MilaNLProc/contextualized-topic-models: A python package to run contextualized topic modeling. CTMs combine contextualized embeddings (e.g., BERT) with topic models to get coherent topics. Published at EACL and ACL 2021.](https://github.com/MilaNLProc/contextualized-topic-models))
