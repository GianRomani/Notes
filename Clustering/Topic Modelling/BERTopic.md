# BERTopic
Created: 2022-05-03 09:08
#paper
 
 The firsts #topic_modeling  approaches used bag-of-words representations to create topics, but this method has the limit that they do not consider the semantic relationships among words. As an answer to this issue, text embedding techniques became popular in NLP. In papers such [clusters of pretrained word embeddings](https://arxiv.org/pdf/2004.14914.pdf) or [Top2Vec](https://arxiv.org/pdf/2008.09470.pdf), topic representations are extracted from word embeddings. In particular, documents are clustered and then topic representations are got from finding words close to a cluster's centroid. That means that words close to a cluster's centroid are the most representative of that cluster, but in reality a cluster will not always lie within a sphere around a cluster centroid.
## Main idea

BERTopic is a topic modeling technique that uses BERT embeddings and a class-based TF-IDF to create dense clusters, allowing for easily interpretable topics whilst keeping important words in the topic descriptions.

## In deep

## References
1. [Paper](https://arxiv.org/abs/2203.05794)
2. [TowardsDataScience guide](https://towardsdatascience.com/interactive-topic-modeling-with-bertopic-1ea55e7d73d8)
3. [TowardsDataScience Code](https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6)

## Code
1. [GitHub](https://github.com/MaartenGr/BERTopic)
